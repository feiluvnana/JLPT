#!/usr/bin/env python3
"""The 知識 batch tool — one script for every check a batch author or reviewer runs
before a batch is merged (jlpt-knowledge/SKILL.md §Batch tool).

    python3 .agents/jlpt-knowledge/scripts/batch_tool.py <cmd> <cat> <batch> [--batches DIR]

    merge   <cat> <n> [<n> ...]  merge QA-passed batches into knowledge/<LEVEL>/ (writes the REAL
                                 tree; --root DIR writes another one). Applies the batch's live-fix
                                 files and back-links; refuses what merge_batch.py refused.
    gate    <cat> <n>            the merge + build + check_knowledge on a TEMP copy; prints only
                                 FAIL / WARN / REVIEW lines, marking a WARN the live tree has too
    frames  <cat> <n>            each example / hand-made stem against every module sentence, the
                                 other open batches, refs/**/*.md and tests/imported-*: shared
                                 content tokens (top 3 per sentence), official 問題6 sentences
                                 marked; plus the 10-char window provenance scan
    lures   <cat> <n>            generated quizzes on the merged tree, suspect items only: gloss
                                 word / Hán Việt overlap key↔distractor, a gloss carrying another
                                 entry's headword, a fake reading that is a real word's reading,
                                 unlinked same-pos pairs sharing a distinctive gloss word
    rebase  <cat> <n>            each back-link's new compare against the live one, each live fix
                                 against the live meaning — only what a human must look at
    stats   <cat> <n>            band use per field, id coverage, example_notes vs examples

Batch files (in --batches DIR, default $KNOWLEDGE_BATCHES):
    <cat>_B<n>.json  .<code>.json  .backlinks.json {live_id: {add_related, <primary>_compare}}
    <cat>_B<n>.backlinks.<code>.json {live_id: compare}
    <P><n>_live_meaning_fix.json  <P><n><code>_live_meaning_fix.json   {id: meaning}
        P = V for 語彙, K for 漢字 (LIVE_FIX_PREFIX)

`--with N` (repeatable) merges other open batches first (gate/lures/frames/rebase), e.g.
`gate 漢字 9 --with 8` when B9 was written on top of B8.

Every subcommand prints one line per actionable hit and a one-line summary.
The real knowledge/ tree is only written by `merge`.
"""

from __future__ import annotations

import argparse
import difflib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import knowledge_data as D   # noqa: E402
import langs                 # noqa: E402  (knowledge_data put its folder on sys.path)

REPO = D.ROOT
LIVE_FIX_PREFIX = {"語彙": "V", "漢字": "K"}
CUT = 160                    # max chars of one quoted text in an output line


class Refuse(Exception):
    """A merge precondition failed (merge_batch.py's assertions)."""


def need(ok, msg):
    if not ok:
        raise Refuse(msg)


def bname(n: str) -> str:
    n = str(n)
    return n if n[:1].isalpha() else f"B{n}"    # "2" -> B2; "G1" stays (guide batches)


def bnum(n: str) -> str:
    return re.sub(r"^[A-Za-z]+", "", bname(n))


def rj(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def wj(p: Path, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def pl(t) -> str:
    """Furigana markup stripped. D.plain's lazy pattern is quadratic on a long text with no
    《, so a text without ruby skips it and a long one is stripped line by line."""
    t = str(t or "")
    if "《" not in t:
        return t.replace("｜", "").replace("**", "")
    if len(t) > 2000:
        return "\n".join(D.plain(x) if "《" in x else x.replace("｜", "").replace("**", "")
                         for x in t.split("\n"))
    return D.plain(t)


def short(t, n=CUT) -> str:
    t = re.sub(r"\s+", " ", pl(t)).strip()
    return t if len(t) <= n else t[:n - 1] + "…"


def spec_of(level: str, stem: str) -> dict:
    for s in D.categories(level):
        if s["stem"] == stem:
            return s
    raise SystemExit(f"no category {stem!r} at {level} (references/categories.json)")


def batches_dir(a) -> Path:
    d = a.batches or os.environ.get("KNOWLEDGE_BATCHES")
    if not d:
        raise SystemExit("where are the batches? pass --batches DIR or set KNOWLEDGE_BATCHES")
    d = Path(d)
    if (d / "batches").is_dir() and not any(d.glob("*_B*.json")):
        d = d / "batches"
    return d


# --------------------------------------------------------------------------
# Loading a batch and its side files
# --------------------------------------------------------------------------
def fix_files(bdir: Path, stem: str, n: str) -> dict[str, Path]:
    """{code: live-fix file} for batch n (primary = <P><n>_…, learner = <P><n><code>_…)."""
    p = LIVE_FIX_PREFIX.get(stem)
    out = {}
    if not p or not bnum(n):
        return out
    for c in langs.order():
        tag = "" if c == langs.primary() else c
        for d in (bdir, bdir.parent):
            f = d / f"{p}{bnum(n)}{tag}_live_meaning_fix.json"
            if f.is_file():
                out[c] = f
                break
    return out


def load_batch(bdir: Path, stem: str, n: str) -> dict:
    n = bname(n)
    sp = bdir / f"{stem}_{n}.json"
    if not sp.is_file():
        raise SystemExit(f"no batch file {sp}")
    b = {"name": n, "entries": rj(sp)["entries"], "prose": {}, "bl": {}, "bl_lang": {}, "fix": {}}
    for c in langs.order():
        p = bdir / f"{stem}_{n}.{c}.json"
        b["prose"][c] = rj(p) if p.is_file() else None
    blp = bdir / f"{stem}_{n}.backlinks.json"
    b["has_bl"] = blp.is_file()
    if b["has_bl"]:
        b["bl"] = rj(blp)
        for c in langs.learners():
            p = bdir / f"{stem}_{n}.backlinks.{c}.json"
            b["bl_lang"][c] = rj(p) if p.is_file() else None
    for c, f in fix_files(bdir, stem, n).items():
        b["fix"][c] = rj(f)
    return b


def live_files(kdir: Path, stem: str):
    shared_p = kdir / f"{stem}.json"
    if not shared_p.is_file():
        raise SystemExit(f"{shared_p} not found — batch_tool handles the single-file layout only")
    shared = rj(shared_p)
    prose = {}
    for c in langs.order():
        p = kdir / f"{stem}.{c}.json"
        prose[c] = rj(p) if p.is_file() else {}
    return shared_p, shared, prose


_Q = re.compile(r"「([^」]+)」")


def quoted(t) -> set[str]:
    return set(_Q.findall(re.sub(r"《[^》]*》|｜", "", t or "")))


# --------------------------------------------------------------------------
# merge — merge_batch.py's logic, plus the live-fix files
# --------------------------------------------------------------------------
def merge_tree(level: str, stem: str, nums: list[str], kdir: Path, bdir: Path, *,
               strict: bool = True, fixes: bool = True, say=print):
    """Merge batches into (shared, prose) read from kdir — in memory.

    strict (merge): refuse a missing language file, as merge_batch.py did.
    not strict (gate/lures): a missing language file is a stub pane — the batch's
    entries get no prose in that language and the live compare stays."""
    shared_p, shared, prose = live_files(kdir, stem)
    have = {e["id"] for e in shared["entries"]}
    live_ids = set(have)
    loaded = [load_batch(bdir, stem, n) for n in nums]
    info = {"stubs": [], "fixed": Counter(), "fix_clash": set(), "bl": 0, "batch_ids": set(),
            "fix_ids": set(), "loaded": loaded}
    for b in loaded:
        n = b["name"]
        ids = [e["id"] for e in b["entries"]]
        clash = have & set(ids)
        need(not clash, f"{n}: ids already present: {sorted(clash)}")
        need(len(ids) == len(set(ids)), f"{n}: duplicate ids inside the batch")
        for c in langs.order():
            pr = b["prose"][c]
            if pr is None:
                need(not strict, f"{n}: no {stem}_{n}.{c}.json — author that language before merging")
                info["stubs"].append(f"{n}.{c}")
                continue
            need(set(pr) == set(ids),
                 f"{n}/{c}: prose ids != shared ids: {sorted(set(pr) ^ set(ids))[:5]}")
            prose[c].update({i: pr[i] for i in ids})
        shared["entries"].extend(b["entries"])
        have |= set(ids)
        info["batch_ids"] |= set(ids)
        say(f"{n}: +{len(ids)} entries")

    # Back-links into LIVE entries (rule 28), prepared by the batch's authors.
    by_id = {e["id"]: e for e in shared["entries"]}
    prim = langs.primary()
    for b in loaded:
        n = b["name"]
        if not b["has_bl"]:
            continue
        bl = b["bl"]
        for c, pl_ in b["bl_lang"].items():
            if pl_ is None:
                need(not strict, f"{n}: no {stem}_{n}.backlinks.{c}.json")
                info["stubs"].append(f"{n}.backlinks.{c}")
        for lid, spec_bl in bl.items():
            need(lid in by_id, f"{n}: back-link target {lid} is not a live entry")
            rel = by_id[lid].setdefault("related", [])
            rel += [r for r in spec_bl["add_related"] if r not in rel]
            new = spec_bl[f"{prim}_compare"]
            lost = quoted(prose[prim].get(lid, {}).get("compare", "")) - quoted(new)
            if lost:
                say(f"  REVIEW {lid}: back-link drops quoted form(s) {sorted(lost)} from the live compare")
            prose[prim].setdefault(lid, {})["compare"] = new
            for c, pl_ in b["bl_lang"].items():
                if pl_ is None:
                    continue
                need(lid in pl_, f"{n}: no {c} compare for back-link target {lid}")
                lost_c = quoted(prose[c].get(lid, {}).get("compare", "")) - quoted(pl_[lid])
                if lost_c:
                    say(f"  REVIEW {lid} [{c}]: back-link drops quoted form(s) {sorted(lost_c)}")
                prose[c].setdefault(lid, {})["compare"] = pl_[lid]
        info["bl"] += len(bl)
        say(f"{n}: back-links applied to {len(bl)} live entries")

    # Live meaning fixes {id: meaning}, one file per language (a later batch wins a clash).
    if fixes:
        seen: dict[str, dict] = defaultdict(dict)
        for b in loaded:
            for c, fx in b["fix"].items():
                for lid, m in fx.items():
                    need(lid in by_id, f"{b['name']}: live fix for {lid}, which is no entry")
                    if lid not in prose[c]:
                        need(not strict, f"{b['name']}: live {c} fix for {lid}, which has no {c} prose")
                        continue
                    if lid in seen[c] and seen[c][lid] != m:
                        info["fix_clash"].add(f"{lid}[{c}]")
                    seen[c][lid] = m
                    prose[c][lid]["meaning"] = m
                    info["fixed"][c] += 1
                    info["fix_ids"].add(lid)
                say(f"{b['name']}: {len(fx)} live {c} meaning fix(es) applied")
        info["live_ids"] = live_ids

    missing = sorted({r for e in shared["entries"] for r in e.get("related", []) if r not in have})
    need(not missing, f"related ids that resolve nowhere: {missing}")

    spec = spec_of(level, stem)
    fails = []
    import check_knowledge as CK
    CK.check_book_order(level, spec, [{**e, "_where": e["id"]} for e in shared["entries"]],
                        lambda name, ok, detail="": fails.append(f"{name}: {detail}") if not ok else None)
    if strict:
        need(not fails, "book order — refusing the merge:\n  " + "\n  ".join(fails))
    info["book_fails"] = fails
    shared["entries"] = D.book_sorted(spec, shared["entries"], level)
    order = [e["id"] for e in shared["entries"]]
    prose = {c: {i: pr[i] for i in order if i in pr} for c, pr in prose.items()}
    info["live_ids"] = live_ids
    return shared_p, shared, prose, info


def write_tree(kdir: Path, stem: str, shared_p: Path, shared: dict, prose: dict):
    wj(shared_p, shared)
    for c, pr in prose.items():
        wj(kdir / f"{stem}.{c}.json", pr)


def cmd_merge(a):
    root = Path(a.root) if a.root else REPO
    kdir = root / "knowledge" / a.level
    try:
        shared_p, shared, prose, info = merge_tree(a.level, a.cat, a.batch + a.with_, kdir,
                                                   batches_dir(a), strict=True)
    except Refuse as ex:
        raise SystemExit(f"refused: {ex}")
    write_tree(kdir, a.cat, shared_p, shared, prose)
    if info["fix_clash"]:
        print(f"NOTE fix clash (later batch wins): {sorted(info['fix_clash'])}")
    print(f"{a.cat}: {len(shared['entries'])} entries total")


# --------------------------------------------------------------------------
# A temp copy of the repo (gate) and the merged tree in memory (lures, frames)
# --------------------------------------------------------------------------
def temp_repo() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="kbatch_"))
    shutil.copytree(REPO / ".agents", tmp / ".agents", symlinks=True,
                    ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(REPO / "knowledge", tmp / "knowledge",
                    ignore=shutil.ignore_patterns("*.html"))
    for n in ("refs", "tools", "tests", "logs"):
        if (REPO / n).exists():
            os.symlink(REPO / n, tmp / n)
    return tmp


def merged(a, quiet=True):
    """(spec, entries, prose, info) of live + batch (+ --with) merged in memory, stubs allowed."""
    lines = []
    try:
        _, shared, prose, info = merge_tree(a.level, a.cat, a.with_ + a.batch,
                                            REPO / "knowledge" / a.level, batches_dir(a),
                                            strict=False, say=lines.append)
    except Refuse as ex:
        raise SystemExit(f"merge refused: {ex}")
    info["lines"] = lines
    return spec_of(a.level, a.cat), shared["entries"], prose, info


def _parse_check(out: str) -> list[tuple[str, str, str]]:
    rows = []
    for ln in out.splitlines():
        bits = ln.split("\t", 2)
        if len(bits) == 3 and bits[0] in ("FAIL", "WARN", "skip", "ok"):
            rows.append(tuple(bits))
    return rows


def _norm_name(n: str) -> str:
    return re.sub(r"\d+", "#", n)


def cmd_gate(a):
    bdir = batches_dir(a)
    tmp = temp_repo()
    try:
        kdir = tmp / "knowledge" / a.level
        lines = []
        try:
            shared_p, shared, prose, info = merge_tree(a.level, a.cat, a.with_ + a.batch, kdir, bdir,
                                                       strict=False, say=lines.append)
        except Refuse as ex:
            print(f"FAIL merge refused: {ex}")
            print("gate: 1 FAIL (merge)")
            return 1
        write_tree(kdir, a.cat, shared_p, shared, prose)
        env = {**os.environ, "BT_GIT_ROOT": str(REPO)}
        me = tmp / ".agents" / "jlpt-knowledge" / "scripts" / "batch_tool.py"
        r = subprocess.run([sys.executable, str(me), "_check", a.cat, "x", "--level", a.level, "--build"],
                           capture_output=True, text=True, env=env, cwd=tmp)
        if r.returncode not in (0, 1):
            print("FAIL build/check crashed:\n" + "\n".join(r.stderr.strip().splitlines()[-12:]))
            return 1
        rows = _parse_check(r.stdout)
        base = subprocess.run([sys.executable, str(Path(__file__).resolve()), "_check", a.cat, "x",
                               "--level", a.level], capture_output=True, text=True, cwd=REPO)
        live = {_norm_name(n) for s, n, _ in _parse_check(base.stdout) if s in ("FAIL", "WARN")}
    finally:
        if a.keep:
            print(f"(temp tree kept: {tmp})")
        else:
            shutil.rmtree(tmp, ignore_errors=True)
    review = [ln.strip() for ln in lines if "REVIEW" in ln]
    for ln in review:
        print(ln)
    for f in info["book_fails"]:
        print(f"FAIL merge book order: {short(f, 300)}")
    nf = nw = new = 0
    nok = sum(s == "ok" for s, _, _ in rows)
    for s, n, d in rows:
        if s in ("skip", "ok"):
            continue
        tag = " (live too)" if _norm_name(n) in live else ""
        if s == "FAIL":
            nf += 1
        else:
            nw += 1
            new += not tag
        print(f"{s} {n}{tag} — {short(d, 400)}")
    nf += len(info["book_fails"])
    stubs = f"; stub panes {info['stubs']}" if info["stubs"] else ""
    fx = ", ".join(f"{c} {k}" for c, k in info["fixed"].items()) or "none"
    clash = f"; fix clash {sorted(info['fix_clash'])}" if info["fix_clash"] else ""
    print(f"gate {a.cat} {'+'.join(bname(x) for x in a.with_ + a.batch)}: {nf} FAIL, {nw} WARN "
          f"({new} not on live), {nok} ok, {len(review)} REVIEW; +{len(info['batch_ids'])} entries, "
          f"{info['bl']} back-links, live fixes {fx}{stubs}{clash}")
    return 1 if nf else 0


def cmd__check(a):
    """Internal: build (optional) and check one category of the tree this copy lives in.
    Prints STATUS<TAB>name<TAB>detail lines for gate to read."""
    import check_knowledge as CK
    spec = spec_of(a.level, a.cat)
    if a.build:
        import build_knowledge as BK
        BK.build_category(a.level, spec)
    git_root = os.environ.get("BT_GIT_ROOT")

    def git_tracks(path):
        if not git_root:
            return CK._default_git_tracks(path)
        r = subprocess.run(["git", "-C", git_root, "ls-files", "--", path], capture_output=True, text=True)
        return bool(r.stdout.strip())

    def emit(status):
        def f(name, ok, detail=""):
            print(f"{status if not ok else 'ok'}\t{name}\t{detail if not ok else ''}".replace("\n", " "))
            return ok
        return f

    CK.check_one(a.level, spec, emit("FAIL"), emit("WARN"),
                 lambda name, why="": print(f"skip\t{name}\t{why}"), git_tracks)
    return 0


# --------------------------------------------------------------------------
# Text tools: tokens, sentence corpus
# --------------------------------------------------------------------------
_RUN = re.compile(r"[一-龥々〆ヶ]+|[ァ-ヺー]{2,}")
_HIRA3 = re.compile(r"[ぁ-ゖ]")
# single kanji too common to be a content token, and common multi-char words
STOP1 = set("人日今時前中後方何事者年月一二三四五十百千万気少多大小上下先間話家子言見思行来出入手目口心力"
            "物所回度分半全生会社店町母父兄姉弟妹私彼自同次毎週朝夜昼円本私")
STOPW = set("自分 今日 毎日 時間 本当 友達 学校 先生 会社 仕事 日本 私達 彼女 子供 子ども 大学 今年 去年 "
            "来年 今月 先月 来月 今週 先週 来週 明日 昨日 一人 二人 最近 部屋 電話 場合 問題 必要 一緒 "
            "大切 大事 様子 意味 言葉 気持 以上 以下 以外 ほか".split())
_SENT_SPLIT = re.compile(r"(?<=[。？！?!])|\n")
_MD = re.compile(r"^[#>\s|*\-]+|\*\*|`")


def toks(s: str) -> set[str]:
    out = set()
    for m in _RUN.finditer(s):
        t = m.group()
        if len(t) == 1 and t in STOP1:
            continue
        if t in STOPW:
            continue
        out.add(t)
    return out


def subs(t: str) -> set[str]:
    return {t[i:j] for i in range(len(t)) for j in range(i + 2, len(t) + 1)} if len(t) >= 2 else set()


class Corpus:
    """Sentences with tags, indexed for shared-token lookup."""

    def __init__(self):
        self.rows: list[tuple[str, str]] = []     # (tag, plain sentence)
        self.seen: dict[str, int] = {}
        self.tok: list[set[str]] = []

    def add(self, tag: str, s: str, lo=8, hi=220):
        if len(s) > 4 * hi:
            return
        s = re.sub(r"\s+", "", _MD.sub("", pl(s))).strip()
        if not (lo <= len(s) <= hi) or len(_HIRA3.findall(s)) < 3:
            return
        if s in self.seen:
            return
        self.seen[s] = len(self.rows)
        self.rows.append((tag, s))

    def index(self):
        self.run_idx: dict[str, set[int]] = defaultdict(set)    # exact run -> rows
        self.sub_idx: dict[str, set[int]] = defaultdict(set)    # substring (>=2) of a run -> rows
        self.tok = []
        for i, (_, s) in enumerate(self.rows):
            ts = toks(s)
            self.tok.append(ts)
            for t in ts:
                self.run_idx[t].add(i)
                for u in (subs(t) if len(t) <= 8 else ()):
                    self.sub_idx[u].add(i)
        self.n = max(1, len(self.rows))
        self._cache: dict[str, set[int]] = {}

    def rows_for(self, t: str) -> set[int]:
        """Rows holding t: the same run, a run t is part of, or a run that is part of t."""
        if t in self._cache:
            return self._cache[t]
        if len(t) == 1:
            out = self.run_idx.get(t, set())
        else:
            out = set(self.sub_idx.get(t, set()))
            for u in subs(t):
                out |= self.run_idx.get(u, set())
        self._cache[t] = out
        return out

    def idf(self, t: str) -> float:
        return math.log(self.n / (1 + len(self.rows_for(t))))


def module_sentences(level: str, skip_ids: set[str]):
    """(tag, text) for every example and quiz stem of every live category at the level."""
    for spec in D.categories(level):
        cat = D.locate(level, spec)
        entries, _ = D.load_entries(cat)
        for e in entries:
            if e.get("id") in skip_ids:
                continue
            for k, x in enumerate(e.get("examples") or [], 1):
                yield f"K:{spec['stem']}:{e.get('id')}#ex{k}", x
            for k, q in enumerate(e.get("quiz") or [], 1):
                if isinstance(q, dict):
                    yield f"K:{spec['stem']}:{e.get('id')}#q{k}", str(q.get("stem", "")).replace("（　）", "")


def open_batches(bdir: Path, level: str, skip: set[str]):
    """[(stem, name, entries)] of batch files whose ids are not live yet (not `skip`)."""
    live = {}
    out = []
    for f in sorted(bdir.glob("*_*.json")):
        m = re.fullmatch(r"(.+)_([BG]\d+)\.json", f.name)
        if not m or f"{m.group(1)}_{m.group(2)}" in skip:
            continue
        stem = m.group(1)
        if stem not in live:
            try:
                live[stem] = {e.get("id") for e in D.load_entries(D.locate(level, spec_of(level, stem)))[0]}
            except SystemExit:
                continue
        try:
            es = rj(f)["entries"]
        except (ValueError, KeyError):
            continue
        if es and not ({e["id"] for e in es} & live[stem]):
            out.append((stem, m.group(2), es))
    return out


def ref_tag(p: Path) -> str:
    rel = p.relative_to(REPO).as_posix()
    m = re.search(r"JLPT_N\d_NEW/[^/]*?(\d{1,2}-\d{4})/(\w+)\.md$", rel)
    if m:
        return f"{m.group(1)} {m.group(2)}"
    m = re.match(r"tests/(imported-[^/]+)/(?:.*/)?([^/]+)$", rel)
    if m:
        return f"{m.group(1).replace('imported-', 'imp:')} {m.group(2)[:8]}"
    rel = rel.replace("refs/", "").replace("Shinkanzen/", "SK:").replace("Soumatome/", "SM:")
    return rel.replace("Hajimete/", "HJ:").replace("_reference.md", "").replace(".md", "")


def refs_files() -> list[Path]:
    fs = sorted((REPO / "refs").rglob("*.md"))
    for t in sorted((REPO / "tests").glob("imported-*")):
        fs += [p for p in t.iterdir() if p.is_file() and p.suffix in (".md", ".txt")]
    return fs


def official_m6() -> list[tuple[str, str]]:
    """[(tag, sentence)] — every official 問題6 option sentence; ✗ marks a misuse (wrong option)."""
    try:
        sys.path.insert(0, str(REPO / "tools"))
        import goi_profile as G
        items = G.official_items()
    except Exception:  # noqa: BLE001 — no archive on this machine: no marks, never a crash
        return []
    out = []
    for it in items:
        if it["mondai"] != 6:
            continue
        sit = re.search(r"(\d{1,2}-\d{4})", it["paper"])
        for k, o in enumerate(it["options"], 1):
            mark = "○" if k == it["key"] else "✗"
            out.append((f"問題6{mark} {sit.group(1) if sit else it['paper']}#{it['no']} {it['stem']}", o))
    return out


def batch_texts(spec: dict, entries: list[dict], prose_prim: dict | None):
    """(id, label, text, kind) of a batch: examples and hand-made quiz stems/options ('ex'),
    and the primary-language prose fields ('prose')."""
    for e in entries:
        for k, x in enumerate(e.get("examples") or [], 1):
            yield e["id"], f"ex{k}", x, "ex"
        for k, q in enumerate(e.get("quiz") or [], 1):
            if isinstance(q, dict):
                yield e["id"], f"q{k}", str(q.get("stem", "")), "ex"
                for j, o in enumerate(q.get("options") or [], 1):
                    yield e["id"], f"q{k}.{j}", str(o), "opt"
        pr = (prose_prim or {}).get(e["id"]) or {}
        for f in ("meaning", "usage", "nuance", "compare", "title", "body", "quiz"):
            v = pr.get(f)
            for j, t in enumerate(v if isinstance(v, list) else [v] if v else [], 1):
                yield e["id"], f"{f}{j if isinstance(v, list) else ''}", str(t), "prose"


def norm10(t: str) -> str:
    return re.sub(r"[\s　*]", "", pl(t))


# --------------------------------------------------------------------------
# frames
# --------------------------------------------------------------------------
def cmd_frames(a):
    bdir = batches_dir(a)
    spec = spec_of(a.level, a.cat)
    names = [bname(x) for x in a.batch]
    me = [load_batch(bdir, a.cat, n) for n in names]
    entries = [e for b in me for e in b["entries"]]
    prim = {}
    for b in me:
        prim.update(b["prose"].get(langs.primary()) or {})
    my_ids = {e["id"] for e in entries}

    C = Corpus()
    for tag, s in official_m6():
        C.add(tag, s)
    n_m6 = len(C.rows)
    for tag, s in module_sentences(a.level, my_ids):
        for piece in _SENT_SPLIT.split(re.sub(r"［[^］]*］", "\n", s)):
            C.add(tag, piece)
    others = open_batches(bdir, a.level, {f"{a.cat}_{n}" for n in names})
    for stem, n, es in others:
        for e in es:
            for k, x in enumerate(e.get("examples") or [], 1):
                C.add(f"B:{stem}_{n}:{e['id']}#ex{k}", x)
            for k, q in enumerate(e.get("quiz") or [], 1):
                if isinstance(q, dict):
                    for piece in _SENT_SPLIT.split(re.sub(r"［[^］]*］", "\n", str(q.get("stem", "")))):
                        C.add(f"B:{stem}_{n}:{e['id']}#q{k}", piece)
    for e in entries:                       # the batch's own other cards (rule 11 is category-wide)
        for k, x in enumerate(e.get("examples") or [], 1):
            C.add(f"self:{e['id']}#ex{k}", x)
    files = refs_files()
    for p in files:
        tag = ref_tag(p)
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for s in _SENT_SPLIT.split(text):
            C.add(tag, s)
    C.index()

    lines, n_sent, hit_sent = [], 0, 0
    kinds = Counter()
    for eid, lab, text, kind in batch_texts(spec, entries, None):
        if kind != "ex":
            continue
        n_sent += 1
        bold = {pl(x) for x in re.findall(r"\*\*(.+?)\*\*", text)}
        s = pl(text)
        hw_toks = set()
        for bw in bold:
            hw_toks |= toks(bw)
        mine = toks(s) - hw_toks
        cand: dict[int, list[str]] = defaultdict(list)
        for t in mine:
            rows = C.rows_for(t)
            if len(rows) > 0.01 * C.n:      # too common to carry a frame
                continue
            for r in rows:
                cand[r].append(t)
        scored = []
        for r, ts in cand.items():
            tag, cs = C.rows[r]
            if tag.startswith(f"self:{eid}#"):
                continue
            # a single kanji (a verb stem: 飲, 運) weighs half a word
            wt = sum(1 if len(t) > 1 else 0.5 for t in ts)
            w = any(bw and bw in cs for bw in bold) or any(r in C.rows_for(t) for t in hw_toks)
            need_ = 2.5 if tag[:2] not in ("K:", "B:", "se", "問題") else 1.5 if tag.startswith("問題6") else 2
            if len(ts) < 2 or wt + w < need_:
                continue
            score = sum(C.idf(t) for t in ts) + (3 if w else 0)
            scored.append((wt + w, score, r, ts, w))
        scored.sort(key=lambda x: (-x[0], -x[1]))
        keep = scored
        if keep:
            hit_sent += 1
        for _, _, r, ts, w in keep[:3]:
            tag, cs = C.rows[r]
            k = "M6" if tag.startswith("問題6") else tag.split(":")[0] if tag[:2] in ("K:", "B:") or tag.startswith("self") else "refs"
            kinds[k] += 1
            mark = "!! " if tag.startswith("問題6✗") else ""
            lines.append(f"{mark}{eid} {lab} [{tag}] {'W+' if w else ''}{len(ts)} {'/'.join(sorted(ts))} ⇢ {short(cs, 90)}")
    for ln in lines:
        print(ln)
    prov = provenance(a, spec, entries, prim, others, my_ids)
    print(f"frames {a.cat} {'+'.join(names)}: {n_sent} sentences, {hit_sent} with frame hits "
          f"({len(lines)} lines: {dict(kinds)}; '!!' = an official 問題6 misuse sentence); "
          f"corpus {len(C.rows)} sentences ({n_m6} 問題6, {len(others)} open batches, {len(files)} refs/tests files); "
          f"10-char: {prov} span(s)")


def provenance(a, spec, entries, prim, others, my_ids) -> int:
    """Rule 3/32: every 10-char window of examples, stems and primary prose against refs/**/*.md
    and tests/imported-* (all texts) and against the module + open batches (examples/stems)."""
    texts = list(batch_texts(spec, entries, prim))
    win: dict[str, list[int]] = defaultdict(list)
    norm = []
    for i, (eid, lab, t, kind) in enumerate(texts):
        p = norm10(t)
        norm.append(p)
        for j in range(len(p) - 9):
            w = p[j:j + 10]
            if len(_HIRA3.findall(w)) == 10 or re.fullmatch(r"[ぁ-ゖァ-ヺー「」、。・〜（）]+", w):
                continue                     # pure kana windows are function words, not a copy
            win[w].append(i)
    if not win:
        return 0
    found: dict[int, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))

    def scan(tag: str, text: str, idxs_ok):
        c = norm10(text)
        for j in range(len(c) - 9):
            w = c[j:j + 10]
            if w in win:
                for i in win[w]:
                    if idxs_ok(i):
                        found[i][w].add(tag)

    for p in refs_files():
        try:
            scan(ref_tag(p), p.read_text(encoding="utf-8", errors="ignore"), lambda i: True)
        except OSError:
            pass
    ex_only = lambda i: texts[i][3] != "prose"   # noqa: E731
    for tag, s in module_sentences(a.level, my_ids):
        scan(tag, s, ex_only)
    for stem, n, es in others:
        for e in es:
            for k, x in enumerate(e.get("examples") or [], 1):
                scan(f"B:{stem}_{n}:{e['id']}", x, ex_only)
    for k, (eid2, lab2, t2, kind2) in enumerate(texts):   # within the batch: another entry's text
        if kind2 == "ex":
            scan(f"self:{eid2}#{lab2}", t2, lambda i, e2=eid2: ex_only(i) and texts[i][0] != e2)
    spans = 0
    for i in sorted(found):
        eid, lab, t, kind = texts[i]
        ws = found[i]
        p = norm[i]
        # merge overlapping windows into spans
        pos = sorted({j for j in range(len(p) - 9) if p[j:j + 10] in ws})
        groups, cur = [], []
        for j in pos:
            if cur and j > cur[-1] + 1:
                groups.append(cur)
                cur = []
            cur.append(j)
        if cur:
            groups.append(cur)
        for g in groups:
            span = p[g[0]:g[-1] + 10]
            tags = sorted({tg for j in g for tg in ws.get(p[j:j + 10], ())})
            spans += 1
            print(f"PROV {eid} {lab} 「{span}」 ← {', '.join(tags[:3])}{f' +{len(tags) - 3}' if len(tags) > 3 else ''}")
    return spans


# --------------------------------------------------------------------------
# lures
# --------------------------------------------------------------------------
JA_EDGE = "をにがはのとでやもへ"
JA_TAIL = ("こと", "もの", "する", "した", "して", "される", "ている", "ない")
JA_STOP_PHRASE = {"ている", "すること", "ること", "ような", "ように", "ところ", "られる", "させる", "なること",
                  "ものを", "ことを", "ことが", "ことに", "ものが", "ものの", "ことの", "について", "として",
                  "などの", "などを", "などが", "などで", "するこ", "ある", "いる", "なる", "また"}
VI_STOP = set("và của cho làm là có không một các những với ra vào lại được việc cái số theo ở trong đi hay "
              "còn đã sau trước người khi để mà thì như này đó điều sự cách bị bằng rất quá hơn nhau khác "
              "lên xuống từ về đến tới nên nhưng hoặc cũng vẫn đang sẽ chỉ mình ai gì nào nói chuyện "
              "thường thứ phải do quen đọc".split())
JA_STOP_RUN = {"様子", "気持", "程度", "物事", "状態", "場所", "自分", "相手", "以上", "意味"}


def ja_runs(t: str) -> set[str]:
    return {m.group() for m in re.finditer(r"[一-龥々〆ヶ]{2,}|[ァ-ヺー]{2,}", pl(t))} - JA_STOP_RUN


def _starts_word(text: str, core: str) -> bool:
    i = text.find(core)
    while i >= 0:
        if i == 0 or text[i - 1] in "|" + JA_EDGE or not re.match(r"[ぁ-ゖー]", text[i - 1]):
            return True
        i = text.find(core, i + 1)
    return False


def ja_common(a: str, b: str) -> list[str]:
    """Shared gloss words of two primary glosses: shared 2+ kanji/katakana runs, plus maximal
    common substrings of >= 4 chars that are not only function fragments."""
    a, b = pl(a), pl(b)
    out = set(ja_runs(a) & ja_runs(b))
    a2 = re.sub(r"[、。・（）()「」\s]", "|", a)
    b2 = re.sub(r"[、。・（）()「」\s]", "|", b)
    n, m = len(a2), len(b2)
    best: set[str] = set()
    prev = [0] * (m + 1)
    for i in range(1, n + 1):
        cur = [0] * (m + 1)
        for j in range(1, m + 1):
            if a2[i - 1] == b2[j - 1] and a2[i - 1] != "|":
                cur[j] = prev[j - 1] + 1
                L = cur[j]
                if L >= 4 and (i == n or j == m or a2[i:i + 1] != b2[j:j + 1]):
                    best.add(a2[i - L:i])
        prev = cur
    for s in sorted(best, key=len, reverse=True):
        core, prev_ = s, None
        while core != prev_:
            prev_ = core
            for t in JA_TAIL:
                if core.endswith(t) and len(core) > len(t):
                    core = core[:-len(t)]
            core = core.strip(JA_EDGE)
            if len(core) > 1 and re.match(r"[一-龥々]", core[-1]) and re.match(r"[ぁ-ゖ]", core[-2]):
                core = core[:-1]          # 「ために人」: the kanji opens the next word
        if len(core) < 3 or core in JA_STOP_PHRASE or any(core in o for o in out):
            continue
        # a kana-only match must start a word in both glosses (after a particle, a kanji,
        # punctuation or the start) — else it is the tail of one word and the head of the next
        if re.fullmatch(r"[ぁ-ゖー]+", core) and not (_starts_word(a2, core) and _starts_word(b2, core)):
            continue
        out.add(core)
    return sorted(out)


def vi_split(t: str) -> tuple[set[str], list[str]]:
    """(Hán Việt syllables before an em dash, gloss words) — Japanese in 「」 dropped."""
    t = re.sub(r"「[^」]*」", " ", t or "")
    hv, g = t.split("—", 1) if "—" in t else ("", t)
    hvs = {w.lower() for w in re.findall(r"[^\W\d_]+", hv)} - {"quen", "đọc"}
    words = [w.lower() for w in re.findall(r"[^\W\d_]+", g)]
    return hvs, words


def _vi_items(t: str) -> set[str]:
    t = re.sub(r"「[^」]*」", " ", t or "")
    t = t.split("—", 1)[1] if "—" in t else t
    return {x.strip().lower() for x in re.split(r"[,;()（）/.…]", t)
            if len(x.split()) == 1 and len(x.strip()) >= 2}


def vi_common(a: str, b: str) -> list[str]:
    ha, ga = vi_split(a)
    hb, gb = vi_split(b)
    out = []
    bga = {" ".join(ga[k:k + 2]) for k in range(len(ga) - 1)}
    bgb = {" ".join(gb[k:k + 2]) for k in range(len(gb) - 1)}
    big = {x for x in bga & bgb if not set(x.split()) <= VI_STOP}
    out += sorted(big)
    inbig = {w for x in big for w in x.split()}
    # a single syllable counts only as a whole gloss item (「đủ」 in "chân; đủ (…)"): inside a
    # compound (thức ăn / thức dậy) it is another word
    out += sorted((_vi_items(a) & _vi_items(b)) - VI_STOP - inbig)
    for h in ha - hb:
        if h in gb and h not in VI_STOP:
            out.append(f"HV {h}")
    for h in hb - ha:
        if h in ga and h not in VI_STOP:
            out.append(f"HV {h}")
    return out


def gloss_common(code: str, a: str, b: str) -> list[str]:
    # the primary (Japanese) gloss is matched by runs and kana chunks; every learner
    # language by words, word pairs and the reading before an em dash (Hán Việt in vi)
    return ja_common(a, b) if code == langs.primary() else vi_common(a, b)


def lure_forms(e: dict, spec: dict) -> set[str]:
    """What a gloss must not print for entry e: its headword, (語彙) the verb/adjective stem,
    (漢字) the kanji."""
    hw = re.sub(r"[〜～\s]", "", pl(e.get(spec["headword"], "")))
    out = {hw} if hw else set()
    pos = str(e.get("pos") or "")
    if pos.startswith(("動詞", "イ形容詞", "い形容詞")) and len(hw) >= 2 and re.search(r"[一-龥]", hw[:-1]):
        out.add(hw[:-1])
    return {x for x in out if re.search(r"[一-龥々ァ-ヺ]", x) or len(x) >= 3}


def related_pairs(entries):
    rel = defaultdict(set)
    for e in entries:
        for r in e.get("related") or []:
            rel[e["id"]].add(r)
            rel[r].add(e["id"])
    return rel


def skeleton(w: str) -> str:
    return "".join(re.findall(r"[一-龥々〆ヶ]", w))


def reverse_readings():
    """{(kanji skeleton, hiragana reading): [spellings]} over the pitch dataset — a fake
    reading listed for another SPELLING of the same word (送り仮名 / 々 variants) is a
    second right answer the integrity rule (which looks up the exact spelling) cannot see."""
    import quiz_gen as QG
    if QG.PITCH is None:
        return None
    exact, _ = QG.PITCH._index()
    rev = defaultdict(list)
    for w, rs in exact.items():
        sk = skeleton(w)
        if sk:
            for r in rs:
                rev[(sk, QG.to_hira(r))].append(w)
    return rev


def cmd_lures(a):
    import quiz_gen as QG
    spec, entries, prose, info = merged(a)
    entries = [e for e in entries if isinstance(e.get("id"), str)]
    by_id = {e["id"]: e for e in entries}
    inv = set(info["batch_ids"]) | set(info["fix_ids"])
    gen = QG.generate(spec, entries, prose)
    rel = related_pairs(entries)
    hwof = {e["id"]: QG.headword(e, spec) for e in entries}
    lines = []
    cnt = Counter()
    n_items = 0
    paired = set()
    rev = None
    for eid, items in sorted(gen.items()):
        for it in items:
            owners = {d.get("owner") for d in it["distractors"]}
            if eid not in inv and not (owners & inv):
                continue
            n_items += 1
            if it["kind"] == "meaning":
                forms = lure_forms(by_id[eid], spec)
                for d in it["distractors"]:
                    o = d["owner"]
                    paired.add(frozenset((eid, o)))
                    for c, key in it["key"].items():
                        dt = d["text"].get(c, "")
                        hit = [f for f in forms if f and f in pl(dt)]
                        if hit:
                            cnt["LURE"] += 1
                            lines.append(f"LURE {eid} {hwof[eid]} [{c}] wrong option {o} {hwof.get(o)} "
                                         f"「{short(dt, 60)}」 prints 「{hit[0]}」")
                        com = gloss_common(c, key, dt)
                        if com:
                            cnt["GW"] += 1
                            lines.append(f"GW {eid} {hwof[eid]} ↔ {o} {hwof.get(o)} [{c}] {com[:4]} :: "
                                         f"「{short(key, 50)}」 | 「{short(dt, 50)}」")
            else:
                for d in it["distractors"]:
                    if "kanji" not in d:
                        continue
                    if rev is None:
                        rev = reverse_readings() or {}
                    ws = [w for w in rev.get((skeleton(it["word"]), d["text"]), []) if w != it["word"]]
                    if ws:
                        cnt["READ"] += 1
                        lines.append(f"READ {eid} {it['word']}: fake 「{d['text']}」 ({d['kanji']} {d['is']}→{d['as']}) "
                                     f"is the dataset's reading of {ws[:3]}")
    # a gloss (any language) that carries another entry's headword / stem / kanji
    forms = {e["id"]: lure_forms(e, spec) for e in entries}
    owners_of = defaultdict(set)
    for i, fs in forms.items():
        for f in fs:
            owners_of[f].add(i)
    for c in langs.order():
        for eid, pr in prose[c].items():
            g = pl((pr or {}).get("meaning", ""))
            if c != langs.primary():
                g = " ".join(re.findall(r"「([^」]*)」", g))
            if not g:
                continue
            carried = []
            for f, own in owners_of.items():
                if len(f) == 1 and spec["headword"] != "kanji":
                    continue
                if f in g and f not in pl(by_id[eid].get(spec["headword"], "")):   # 挙げる/挙: its own
                    carried += [f"{o} 「{f}」" for o in sorted(own)
                                if o != eid and (eid in inv or o in inv) and o not in rel[eid]]
            if carried:
                cnt["HW"] += 1
                lines.append(f"HW {eid} {hwof.get(eid)} [{c}] gloss 「{short(g, 50)}」 carries "
                             f"{', '.join(carried[:5])} (unlinked)")
    # unlinked same-pos pairs sharing a distinctive gloss word, batch involved
    df = {c: Counter() for c in langs.order()}
    words = {c: {} for c in langs.order()}
    for c in langs.order():
        for e in entries:
            m = (prose[c].get(e["id"]) or {}).get("meaning", "")
            if not m:
                continue
            if c == langs.primary():
                ws = ja_runs(m)
            else:
                hv, gw = vi_split(m)
                ws = {" ".join(gw[k:k + 2]) for k in range(len(gw) - 1)
                      if not {gw[k], gw[k + 1]} <= VI_STOP}
            words[c][e["id"]] = ws
            df[c].update(ws)
    pos1 = lambda e: str(e.get("pos") or "").split("・")[0]   # noqa: E731
    for x in sorted(inv):
        if x not in by_id:
            continue
        for e in entries:
            y = e["id"]
            if y == x or y in rel[x] or frozenset((x, y)) in paired or (y in inv and y < x):
                continue
            if pos1(by_id[x]) != pos1(e):
                continue
            # a near-synonym shares a distinctive word in one pane AND a gloss word in every
            # pane that glosses both; one pane alone is a shared topic (お金, 銀行)
            if not any(w for c in langs.order() for w in words[c].get(x, set()) & words[c].get(y, set())
                       if df[c][w] <= 4):
                continue
            gl = {c: ((prose[c].get(x) or {}).get("meaning"), (prose[c].get(y) or {}).get("meaning"))
                  for c in langs.order()}
            gl = {c: v for c, v in gl.items() if v[0] and v[1]}
            sh = {c: gloss_common(c, *v) for c, v in gl.items()}
            if gl and all(sh.values()):
                cnt["PAIR"] += 1
                lines.append(f"PAIR {x} {hwof[x]} / {y} {hwof[y]} "
                             + " ".join(f"[{c}] {sh[c][:2]}" for c in gl) + " — unlinked, same pos")
    for ln in lines:
        print(ln)
    print(f"lures {a.cat} {'+'.join(bname(x) for x in a.with_ + a.batch)}: {n_items} generated items involve "
          f"the batch/fixed ids; {dict(cnt) or 'no hits'} (LURE wrong option prints the headword; GW shared "
          f"gloss word or Hán Việt; READ fake reading is real for another spelling of the word; HW gloss carries another headword; "
          f"PAIR unlinked look-alikes){'; stub panes ' + str(info['stubs']) if info['stubs'] else ''}")


# --------------------------------------------------------------------------
# rebase
# --------------------------------------------------------------------------
def _flat(t) -> str:
    return re.sub(r"[\s　]", "", pl(t))


def _units(t: str, code: str) -> list[str]:
    t = pl(t)
    if code == langs.primary():
        return list(re.sub(r"[\s　]", "", t))
    return re.findall(r"「[^」]*」|[^\s,;.:()（）「」]+|[,;.:()（）]", t)


def lost_parts(old: str, new: str, code: str) -> list[tuple[str, str]]:
    """(live fragment, what replaced it) for every deleted/replaced stretch of the live text
    that carries content — punctuation and function words do not hold a contrast."""
    a, b = _units(old, code), _units(new, code)
    sep = "" if code == langs.primary() else " "
    out = []
    for t, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if t not in ("delete", "replace"):
            continue
        gone = [u for u in a[i1:i2] if not re.fullmatch(r"[,;.:()（）、。・\s]+", u)
                and u.lower() not in VI_STOP and u not in ("ghép", "có")]
        if code == langs.primary():
            gone = [u for u in gone if u not in JA_EDGE]
        if gone:
            out.append((sep.join(a[i1:i2]), sep.join(b[j1:j2])))
    return out


def cmd_rebase(a):
    bdir = batches_dir(a)
    _, shared, live = live_files(REPO / "knowledge" / a.level, a.cat)
    prim = langs.primary()
    ok = changed = fresh = ext = 0
    nfix = same = 0
    for n in a.batch:
        b = load_batch(bdir, a.cat, n)
        pairs = []                     # (lid, code, new)
        for lid, sb in b["bl"].items():
            pairs.append((lid, prim, sb.get(f"{prim}_compare", "")))
        for c, d in b["bl_lang"].items():
            if d is None:
                print(f"NOTE {b['name']}: no backlinks.{c}.json — the {c} compares stay as they are")
                continue
            pairs += [(lid, c, t) for lid, t in d.items()]
        for lid, c, new in pairs:
            old = (live[c].get(lid) or {}).get("compare", "")
            if lid not in live[prim]:
                print(f"MISSING {lid}: not a live entry")
                continue
            fo, fn = _flat(old), _flat(new)
            if not fo:
                fresh += 1
                continue
            if fo in fn:
                ok += 1
                continue
            gone = lost_parts(old, new, c)
            if not gone:
                ext += 1                 # the live text survives whole, with insertions
                continue
            changed += 1
            lost = sorted(quoted(old) - quoted(new))
            diff = "; ".join(f"「{short(x, 50)}」→「{short(y, 30)}」" for x, y in gone[:4])
            print(f"BL {lid} [{c}]{' LOST ' + str(lost) if lost else ''} {diff}"
                  + (f" +{len(gone) - 4} more" if len(gone) > 4 else ""))
        for c, fx in b["fix"].items():
            for lid, m in fx.items():
                old = (live[c].get(lid) or {}).get("meaning")
                if old is None:
                    print(f"FIX {lid} [{c}]: no live {c} meaning to fix")
                    continue
                if _flat(old) == _flat(m):
                    same += 1
                    continue
                nfix += 1
                print(f"FIX {lid} [{c}] 「{short(old, 70)}」 → 「{short(m, 70)}」")
    print(f"rebase {a.cat} {'+'.join(bname(x) for x in a.batch)}: back-links {ok} keep the live compare whole, "
          f"{ext} keep it with insertions, {fresh} fill an empty one, {changed} rewrite part of it "
          f"(printed live→new: check no contrast is lost); "
          f"live fixes {nfix} change a meaning, {same} already live")


# --------------------------------------------------------------------------
# stats
# --------------------------------------------------------------------------
def cmd_stats(a):
    import check_knowledge as CK
    bdir = batches_dir(a)
    spec = spec_of(a.level, a.cat)
    kind = spec["kind"]
    _, shared, live = live_files(REPO / "knowledge" / a.level, a.cat)
    live_ids = {e["id"] for e in shared["entries"]}
    for n in a.batch:
        b = load_batch(bdir, a.cat, n)
        ids = [e["id"] for e in b["entries"]]
        sid = set(ids)
        lo, hi = spec.get("examples", [0, 99])
        qlo, qhi = spec.get("quiz", [0, 99])
        nex = Counter(len(e.get("examples") or []) for e in b["entries"])
        nq = Counter(len(e.get("quiz") or []) for e in b["entries"])
        print(f"{b['name']}: {len(ids)} entries ({len(ids) - len(sid)} duplicate ids, "
              f"{len(sid & live_ids)} already live); examples per entry {dict(sorted(nex.items()))} "
              f"(spec {lo}–{hi}); quiz {dict(sorted(nq.items()))} (spec {qlo}–{qhi})")
        for c in langs.order():
            pr = b["prose"][c]
            if pr is None:
                print(f"  {c}: NO FILE")
                continue
            miss, extra = sorted(sid - set(pr)), sorted(set(pr) - sid)
            f = langs.length_factor(c)
            parts = []
            for k, cap in CK.KNOWLEDGE_BANDS[kind].items():
                lim = int(cap * f)
                vals = []
                for i in ids:
                    v = (pr.get(i) or {}).get(k)
                    vals += [len(pl(x)) for x in (v if isinstance(v, list) else [v] if isinstance(v, str) else [])]
                if not vals:
                    continue
                over = sum(x > lim for x in vals)
                hot = sum(x > 0.75 * lim for x in vals)
                parts.append(f"{k} max {max(vals)}/{lim} >75% {hot}" + (f" OVER {over}" if over else ""))
            bad_notes = []
            if c != langs.primary():
                for e in b["entries"]:
                    notes = (pr.get(e["id"]) or {}).get("example_notes")
                    if len(notes or []) != len(e.get("examples") or []):
                        bad_notes.append(e["id"])
            bad_q = [e["id"] for e in b["entries"]
                     if len((pr.get(e["id"]) or {}).get("quiz") or []) != len(e.get("quiz") or [])]
            print(f"  {c}: ids {len(sid & set(pr))}/{len(sid)}"
                  + (f" MISSING {miss[:5]}" if miss else "") + (f" EXTRA {extra[:5]}" if extra else "")
                  + f"; {'; '.join(parts)}"
                  + (f"; example_notes≠examples {len(bad_notes)} {bad_notes[:4]}" if bad_notes else "")
                  + (f"; quiz explanations≠items {bad_q[:4]}" if bad_q else ""))
        if b["has_bl"]:
            not_live = sorted(set(b["bl"]) - live_ids)
            line = f"  back-links: {len(b['bl'])} targets" + (f", NOT LIVE {not_live[:5]}" if not_live else "")
            for c, d in b["bl_lang"].items():
                if d is None:
                    line += f"; {c}: NO FILE"
                    continue
                f = langs.length_factor(c)
                lens = [len(pl(t)) for t in d.values()]
                diff = set(d) ^ set(b["bl"])
                line += (f"; {c}: {len(d)}" + (f" ids≠ {sorted(diff)[:4]}" if diff else "")
                         + (f", compare max {max(lens)}/{int(100 * f)}" if lens else ""))
            jl = [len(pl(v.get(f"{langs.primary()}_compare", ""))) for v in b["bl"].values()]
            if jl:
                line += f"; {langs.primary()} compare max {max(jl)}/100"
            print(line)
        for c, fx in b["fix"].items():
            not_live = sorted(set(fx) - live_ids)
            lim = int(40 * langs.length_factor(c))
            lens = [len(pl(t)) for t in fx.values()]
            print(f"  live fix [{c}]: {len(fx)} ids" + (f", NOT LIVE {not_live[:5]}" if not_live else "")
                  + (f", meaning max {max(lens)}/{lim}" if lens else ""))
    return 0


# --------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("cmd", choices=["merge", "gate", "frames", "lures", "rebase", "stats", "_check"])
    ap.add_argument("cat")
    ap.add_argument("batch", nargs="+")
    ap.add_argument("--level", default="N2")
    ap.add_argument("--batches", help="the batch folder (default $KNOWLEDGE_BATCHES)")
    ap.add_argument("--with", dest="with_", action="append", default=[],
                    help="another open batch to merge first (repeatable)")
    ap.add_argument("--root", help="merge: the repo root to write (default: this repo)")
    ap.add_argument("--keep", action="store_true", help="gate: keep the temp tree")
    ap.add_argument("--build", action="store_true", help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    a.with_ = [bname(x) for x in a.with_]
    if a.cmd != "merge" and a.cmd != "_check" and len(a.batch) > 1:
        ap.error(f"{a.cmd} takes one batch; merge others first with --with")
    fn = {"merge": cmd_merge, "gate": cmd_gate, "frames": cmd_frames, "lures": cmd_lures,
          "rebase": cmd_rebase, "stats": cmd_stats, "_check": cmd__check}[a.cmd]
    return fn(a) or 0


if __name__ == "__main__":
    sys.exit(main())
