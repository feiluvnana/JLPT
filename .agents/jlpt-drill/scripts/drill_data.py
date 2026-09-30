"""The drill module's data layer — ONE reader for the builder and the gate.

The ドリル module authors nothing (jlpt-drill/SKILL.md §Sources): every pool it
bakes is read out of material that already has an owner.

    言語知識・読解 items   tests/<id>/詳細解説.json (stem/options/passage — the ONE copy
                          of the exam wording) + 詳細解説.<code>.json (prose per
                          language), keys from grade_answers.parse_gengo_keys(), the
                          大問 of each question from grade_answers.gengo_taxonomy()
                          (the level table, era-aware)
    聴解 clips            logs/choukai_bank.json (script, keys, `explanation*`) —
                          located in a test's 聴解.mp3 by the record's own offsets
                          (an official clip of an imported sitting) or by the
                          chapter mark of a generated paper that drew it
                          (logs/choukai_draws.json + 聴解_チャプター.json)
    knowledge quiz ids    knowledge_data (jlpt-knowledge) — for 復習ノート's links

Item id everywhere: `<test_id>:<key>`, key as in 詳細解説.json ("33", "問1-1").
A 聴解 clip has ONE canonical id per question — the official sitting's own
(`imported-…:問1-1`) or, for a clip only a generated paper plays, the first
paper (in draw order) that drew it; every other paper's copy is an ALIAS of it
(`aliases()`), so a mistake made in any sitting lands on the same record.

Language codes are never written here: they come from the registry (langs).
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
AGENTS = ROOT / ".agents"
for _p in (AGENTS / "exam-model-answer" / "scripts", AGENTS / "exam-app" / "scripts",
           AGENTS / "jlpt-exam-structure" / "scripts", AGENTS / "jlpt-knowledge" / "scripts"):
    sys.path.insert(0, str(_p))

import langs                      # noqa: E402
import level as LEVEL             # noqa: E402
import grade_answers as GA        # noqa: E402

TESTS = ROOT / "tests"
DRILL = ROOT / "drill"
BANK = ROOT / "logs" / "choukai_bank.json"
DRAWS = ROOT / "logs" / "choukai_draws.json"
KNOWLEDGE_LINKS = HERE.parent / "references" / "knowledge_links.json"
GENGO_MD, CHOUKAI_MD = "言語知識・読解.md", "聴解.md"
KAISETSU = "詳細解説.json"
CHAPTERS = "聴解_チャプター.json"
INDEX_HTML = "index.html"

# The tools, in index order: (page stem, label key, description key). The stem is
# the file name under drill/<LEVEL>/; a split tool also has a folder of that name.
TOOLS = (
    ("大問別練習", "tool_practice", "tool_practice_desc"),
    ("聴解トレーニング", "tool_listening", "tool_listening_desc"),
    ("復習ノート", "tool_review", "tool_review_desc"),
    ("進捗", "tool_progress", "tool_progress_desc"),
    ("読解ライブラリ", "tool_library", "tool_library_desc"),
)
PRACTICE, LISTENING, REVIEW, PROGRESS, LIBRARY = (t[0] for t in TOOLS)
SPLIT_TOOLS = (PRACTICE, LIBRARY)      # one page per 大問 under <stem>/<code>.html


def origin(test_id: str) -> str:
    """`official` for an imported past paper, `mock` for a generated one."""
    return "official" if test_id.startswith("imported-") else "mock"


def level_tests(level: str) -> list[Path]:
    """Every test folder of `level` that has a paper and a primary 詳細解説."""
    if not TESTS.is_dir():
        return []
    out = []
    for d in sorted(TESTS.iterdir(), key=lambda p: p.name):
        if not d.is_dir() or (LEVEL.declared_level(d) or LEVEL.level_of(d.name)) != level:
            continue
        if (d / GENGO_MD).is_file() and (d / KAISETSU).is_file():
            out.append(d)
    return out


def gengo_mondai(level: str) -> list[dict]:
    """The level's 言語知識・読解 大問, in order: code, mondai, name, part, section."""
    g = LEVEL.gengo(level)
    return [{"code": m["code"], "mondai": m["mondai"], "name": m["name"],
             "part": m.get("part") or "", "section": "言語知識" if i < g["goi_mondai"] else "読解"}
            for i, m in enumerate(g["mondai"])]


def choukai_mondai(level: str) -> list[dict]:
    return [{"code": m["code"], "mondai": m["code"], "name": m["name"], "part": "聴解",
             "section": "聴解"} for m in LEVEL.choukai(level)["mondai"]]


def choukai_code(key: str) -> str | None:
    """'問3-2' / '問5-2-1' -> '問題3' (the 聴解 大問 code grade_answers uses)."""
    m = re.match(r"問([1-9])-", key)
    return f"問題{m.group(1)}" if m else None


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_details(test_dir: Path) -> dict:
    """{code: 詳細解説 data} for every registry language whose file parses."""
    out = {}
    for c in langs.order():
        p = langs.content_path(test_dir / KAISETSU, c)
        if p.is_file():
            try:
                out[c] = read_json(p)
            except (OSError, ValueError):
                pass
    return out


def test_ranges(level: str, test_dir: Path) -> list[list]:
    """[[code, first, last], …] — this paper's own 大問 map (its era's shape)."""
    keys = GA.parse_gengo_keys(test_dir / GENGO_MD)
    tax = GA.gengo_taxonomy(max(keys) if keys else None, level)
    return [[c, s["range"][0], s["range"][1]] for c, s in tax.items()]


# ------------------------------------------------------------- 言語知識・読解
@dataclass
class Item:
    id: str
    test: str
    origin: str
    key: str
    code: str
    answer: int
    stem: str
    options: list[str]
    group: str | None                 # passage group id, or None
    prose: dict[str, dict]            # {code: 詳細解説 entry} — primary included


@dataclass
class Passage:
    id: str
    test: str
    origin: str
    code: str
    text: str
    translations: dict[str, str] = field(default_factory=dict)   # learner code -> text
    items: list[str] = field(default_factory=list)


@dataclass
class GengoPool:
    items: list[Item] = field(default_factory=list)
    passages: dict[str, Passage] = field(default_factory=dict)
    ranges: dict[str, list[list]] = field(default_factory=dict)  # test -> [[code, lo, hi]]
    skipped: list[str] = field(default_factory=list)              # "<id>: why"
    sources: list[Path] = field(default_factory=list)


def gengo_pool(level: str) -> GengoPool:
    pool = GengoPool()
    prim = langs.primary()
    for d in level_tests(level):
        tid = d.name
        keys = GA.parse_gengo_keys(d / GENGO_MD)
        if not keys:
            pool.skipped.append(f"{tid}: no 言語知識・読解 answer key")
            continue
        pool.sources.append(d / GENGO_MD)
        pool.sources += [langs.content_path(d / KAISETSU, c) for c in langs.order()
                         if langs.content_path(d / KAISETSU, c).is_file()]
        ranges = test_ranges(level, d)
        pool.ranges[tid] = ranges
        det = load_details(d)
        base = det.get(prim) or {}
        by_text: dict[str, str] = {}
        for q in sorted(keys):
            k = str(q)
            iid = f"{tid}:{k}"
            e = base.get(k)
            code = next((c for c, lo, hi in ranges if lo <= q <= hi), None)
            opts = e.get("options") if isinstance(e, dict) else None
            if not isinstance(e, dict) or not code or not isinstance(opts, list) or len(opts) < 2:
                pool.skipped.append(f"{iid}: no stem/options in {KAISETSU}")
                continue
            if not 1 <= keys[q] <= len(opts):
                pool.skipped.append(f"{iid}: key {keys[q]} outside its {len(opts)} options")
                continue
            gid = None
            ptext = (e.get("passage") or "").strip()
            if ptext:
                gid = by_text.get(ptext)
                if gid is None:
                    gid = f"{tid}:p{len(by_text) + 1}"
                    by_text[ptext] = gid
                    pool.passages[gid] = Passage(gid, tid, origin(tid), code, ptext)
                psg = pool.passages[gid]
                psg.items.append(iid)
                for c in langs.learners():
                    tr = ((det.get(c) or {}).get(k) or {}).get("passage_translation")
                    if isinstance(tr, str) and tr.strip() and c not in psg.translations:
                        psg.translations[c] = tr.strip()
            prose = {c: det[c][k] for c in det if isinstance(det[c].get(k), dict)}
            pool.items.append(Item(iid, tid, origin(tid), k, code, keys[q], e.get("stem") or "",
                                   [str(o) for o in opts], gid, prose))
    return pool


# ----------------------------------------------------------------------- 聴解
@dataclass
class Question:
    id: str                            # canonical `<test>:<key>`
    key: str                           # the key in the playing test
    answer: int
    options: list[str]
    stem: str
    prose: dict[str, dict]             # {code: explanation entry}


@dataclass
class Clip:
    id: str                            # bank record id
    code: str                          # 問題N
    source: str                        # bank `source` (official, soumatome, …)
    origin: str                        # official | textbook
    test: str                          # the test whose 聴解.mp3 plays it
    start: float
    end: float
    located: str                       # "offsets" (the record's own) | "chapter"
    script: str
    source_page: str
    questions: list[Question] = field(default_factory=list)


@dataclass
class ChoukaiPool:
    clips: list[Clip] = field(default_factory=list)
    aliases: dict[str, str] = field(default_factory=dict)   # any test item id -> canonical id
    unplayable: list[str] = field(default_factory=list)     # bank ids with no located audio
    skipped: list[str] = field(default_factory=list)
    sources: list[Path] = field(default_factory=list)


def _prose_field(code: str, record: dict) -> dict:
    """The record's explanation block for `code`: `explanation[_<code>]` (keyed by
    item) on an official record, `explanation[_<code>]_payload` on a slot-free one."""
    f = langs.content_field(code, "explanation")
    if isinstance(record.get(f), dict):
        return {"keyed": record[f]}
    if isinstance(record.get(f + "_payload"), dict):
        return {"single": record[f + "_payload"]}
    return {}


def _questions(record: dict, test_keys: list[str], test_id: str, key_table: dict) -> list[Question]:
    """One Question per answer of the clip, mapped onto the playing test's keys by order."""
    if isinstance(record.get("answers"), dict):
        own = list(record["answers"])
    else:
        own = [None]
    if len(own) != len(test_keys):
        return []
    out = []
    for bank_key, tkey in zip(own, test_keys):
        prose = {}
        for c in langs.order():
            blk = _prose_field(c, record)
            ent = (blk.get("keyed") or {}).get(bank_key) if "keyed" in blk else blk.get("single")
            if isinstance(ent, dict):
                prose[c] = ent
        base = prose.get(langs.primary()) or {}
        opts = [str(o) for o in (base.get("options") or [])]
        ans = key_table.get(tkey)
        if ans is None:
            ans = record["answers"][bank_key] if bank_key else record.get("answer")
        out.append(Question(f"{test_id}:{tkey}", tkey, int(ans), opts, base.get("stem") or "", prose))
    return out


def _script(record: dict) -> str:
    if isinstance(record.get("script"), str):
        return record["script"]
    return "\n".join(record.get("script_lines") or [])


def _chapter_spans(test_dir: Path) -> dict[str, tuple[float, float]]:
    """{'問題1-2': (start, end)} off a paper's 聴解_チャプター.json — the mark is on
    the item's number call; it runs to the next mark (or the recording's end)."""
    p = test_dir / CHAPTERS
    if not p.is_file():
        return {}
    d = read_json(p)
    ch = d.get("chapters") or []
    out = {}
    for i, c in enumerate(ch):
        m = re.fullmatch(r"(問題\d)\s*(\d+)番", str(c.get("label", "")))
        if not m:
            continue
        end = ch[i + 1]["start"] if i + 1 < len(ch) else d.get("duration")
        if end is None:
            continue
        out[f"{m.group(1)}-{m.group(2)}"] = (float(c["start"]), float(end))
    return out


def _slot_keys(keys: list[str], slot: str) -> list[str]:
    """'問題5-2' -> the test's keys under it ('問5-2-1', '問5-2-2'); '問題1-3' -> ['問1-3']."""
    m = re.fullmatch(r"問題(\d)-(\d+)", slot)
    if not m:
        return []
    pre = f"問{m.group(1)}-{m.group(2)}"
    return [k for k in keys if k == pre or k.startswith(pre + "-")]


def choukai_pool(level: str) -> ChoukaiPool:
    pool = ChoukaiPool()
    if not BANK.is_file():
        return pool
    bank = read_json(BANK)
    pool.sources.append(BANK)
    records = {r["id"]: r for r in bank.get("records", []) if r.get("kind") == "item"}
    tests = {d.name: d for d in level_tests(level)}
    keytab = {}
    for tid, d in tests.items():
        keytab[tid] = GA.parse_choukai_keys(d / CHOUKAI_MD)
    placed: dict[str, Clip] = {}

    # 1. official clips at their own offsets in the imported sitting they came from
    for rid, r in records.items():
        st = r.get("source_test")
        if not st or st not in tests or not isinstance(r.get("audio"), dict):
            continue
        keys = list(r.get("answers") or {})
        qs = _questions(r, keys, st, keytab.get(st, {}))
        if not qs:
            pool.skipped.append(f"{rid}: its keys do not match {st}")
            continue
        a = r["audio"]
        placed[rid] = Clip(rid, r.get("section", ""), r.get("source", ""), "official", st,
                           float(a["start"]), float(a["end"]) + float(a.get("answer_pause") or 0),
                           "offsets", _script(r), str(r.get("source_page") or ""), qs)

    # 2. every generated paper's draw: aliases, and the clips only a paper can play
    draws = read_json(DRAWS).get("history", []) if DRAWS.is_file() else []
    if DRAWS.is_file():
        pool.sources.append(DRAWS)
    for h in draws:
        tid = h.get("test_id")
        if tid not in tests:
            continue
        d = tests[tid]
        if (d / CHAPTERS).is_file():
            pool.sources.append(d / CHAPTERS)
        spans = _chapter_spans(d)
        tkeys = list(keytab.get(tid, {}))
        for slot, rid in (h.get("clips") or {}).items():
            r = records.get(rid)
            skeys = _slot_keys(tkeys, slot)
            if r is None or not skeys:
                continue
            if rid not in placed and slot in spans:
                qs = _questions(r, skeys, tid, keytab[tid])
                if qs:
                    s, e = spans[slot]
                    placed[rid] = Clip(rid, r.get("section", ""), r.get("source", ""),
                                       "official" if r.get("source") == "official" else "textbook",
                                       tid, s, e, "chapter", _script(r),
                                       str(r.get("source_page") or ""), qs)
            clip = placed.get(rid)
            if clip and len(clip.questions) == len(skeys):
                for k, q in zip(skeys, clip.questions):
                    pool.aliases[f"{tid}:{k}"] = q.id
    for clip in placed.values():
        for q in clip.questions:
            pool.aliases.setdefault(q.id, q.id)
    pool.unplayable = sorted(set(records) - set(placed))
    order = {m["code"]: i for i, m in enumerate(choukai_mondai(level))}
    pool.clips = sorted(placed.values(), key=lambda c: (order.get(c.code, 9), c.origin != "official",
                                                        c.test, c.start))
    return pool


# ----------------------------------------------------------------- knowledge
def knowledge_quiz(level: str) -> dict:
    """{stem: {"label": label key, "entries": {id: {"head", "page", "n"}}}} — the
    knowledge entries that carry a quiz, with the page (relative to
    knowledge/<LEVEL>/) whose `#e-<id>` anchor shows the card."""
    try:
        import knowledge_data as KD
    except Exception:          # noqa: BLE001 — no knowledge module: no knowledge links
        return {}
    out = {}
    for spec in KD.categories(level):
        cat = KD.locate(level, spec)
        entries, prose = KD.load_entries(cat)
        ents = {}
        for e in entries:
            if not isinstance(e.get("id"), str) or not e.get("quiz"):
                continue
            if spec["kind"] == "guide":
                head = (prose.get(langs.primary(), {}).get(e["id"]) or {}).get("title") or e["id"]
            else:
                head = str(e.get(spec.get("headword", ""), e["id"]))
            page = (f"{spec['stem']}/{e['_part']}.html" if cat.layout == "split"
                    else f"{spec['stem']}.html")
            ents[e["id"]] = {"head": KD.plain(head), "page": page, "n": len(e["quiz"])}
        out[spec["stem"]] = {"label": spec["label"], "entries": ents,
                             "available": bool(entries)}
    return out


def knowledge_sources(level: str) -> list[Path]:
    try:
        import knowledge_data as KD
    except Exception:          # noqa: BLE001
        return []
    out = []
    for spec in KD.categories(level):
        out += [p.shared for p in KD.locate(level, spec).parts]
    return out


def knowledge_links(level: str) -> dict[str, list[str]]:
    """{part: [knowledge stems]} — which 知識 categories study a weak 大問's part."""
    if not KNOWLEDGE_LINKS.is_file():
        return {}
    return read_json(KNOWLEDGE_LINKS).get(level, {})


# ---------------------------------------------------------- source-sha stamps
# The `<!-- src_sha: <name>=<12-hex sha1> -->` format every builder stamps.
# `<name>` is repo-relative: the drill pages read tests/, logs/ and knowledge/.
def source_sha(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()[:12]


def stamp_name(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def src_sha_comments(sources: list[Path]) -> str:
    seen = dict.fromkeys(p for p in sources if p.is_file())
    return "".join(f"\n<!-- src_sha: {stamp_name(p)}={source_sha(p)} -->" for p in seen) + "\n"


STAMP = re.compile(r"<!-- src_sha: (.+?)=([0-9a-f]{12}) -->")


def read_stamps(page: Path) -> dict[str, str]:
    return dict(STAMP.findall(page.read_text(encoding="utf-8")))


def level_dir(level: str) -> Path:
    return DRILL / level
