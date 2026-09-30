#!/usr/bin/env python3
"""The knowledge module's gate checks — called by tools/check_consistency.py.

    python3 .agents/jlpt-knowledge/scripts/check_knowledge.py      # standalone, same checks

`check_all(check, warn, skip, git_tracks)` takes the gate's own reporters so a
knowledge line reads, counts and exits exactly like every other `make check` line.
Every rule here is documented in jlpt-knowledge/SKILL.md; each message names the
rule and the repair.

FAIL: schema violations, duplicate ids, `related` to a missing id, a quiz item
without 4 distinct options or with its answer out of range, a `sources[].ref`
that does not resolve (a tracked refs/ extract missing = FAIL, a refs/ binary on
a machine without the archive = skip, as check_refs does), language prose for an
id the shared file does not have, band breaches, a language file carrying
shared-material keys, a stale or missing built page, the band table in
SKILL.md drifting from KNOWLEDGE_BANDS, a generated 語彙/漢字 quiz item (quiz_gen.py)
that breaks the integrity rules (a distractor that is a valid reading of the
headword, a meaning distractor from a `related` entry, a key that is not the
entry's own), the pitch dataset failing to load for a category that needs it,
and book order (SKILL §Book order): a category without an `order` rule, an entry
without a book-order key (文法: a valid `book` its inventory row assigns), two
entries on one key unless categories.json `book_splits` documents the split, a
`group` label the `book` key does not imply, a built page whose cards are not
listed in book order.
WARN: a shared entry with no prose in some active language, quiz answer
positions unbalanced across a category, a language file for an inactive code,
a repeated headword, an entry whose generated item was skipped for want of
safe distractors.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import knowledge_data as D   # noqa: E402
import langs             # noqa: E402  (knowledge_data put its folder on sys.path)
import quiz_gen as QG     # noqa: E402  (the generated 語彙/漢字 items)
PITCH = QG.PITCH

ROOT = D.ROOT
SKILL_MD = HERE.parent / "SKILL.md"

# The length caps, PRIMARY language, characters with furigana markup stripped.
# Every other language is held to cap × its length_factor (languages/<code>/
# meta.json). SKILL.md §Bands prints this table and the gate asserts they agree —
# edit here, then refresh the table.
KNOWLEDGE_BANDS = {
    "item": {"meaning": 40, "usage": 100, "nuance": 100, "compare": 100, "quiz": 80},
    "guide": {"title": 30, "body": 200, "quiz": 80},
}
GUIDE_BODY_PARAGRAPHS = (1, 6)

ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
ARCHIVE_BINARY = (".pdf", ".mp3", ".rar", ".wav", ".m4a", ".zip")

# Keys a shared entry may carry beyond its category's `fields`.
SHARED_COMMON = {"id", "examples", "sources", "related", "quiz", "group", "tags", "official_count",
                 "pitch", "book"}
PROSE_KEYS = {"item": {"meaning", "usage", "nuance", "compare", "example_notes", "quiz"},
              "guide": {"title", "body", "example_notes", "quiz"}}


def _rel(p: Path) -> str:
    """A data path as messages print it: knowledge/<LEVEL>/…"""
    try:
        return p.relative_to(D.KNOWLEDGE.parent).as_posix()
    except ValueError:
        return p.as_posix()


def _bad(problems: list[str], where: str, msg: str):
    problems.append(f"{where}: {msg}")


def _is_str(v, empty_ok=False) -> bool:
    return isinstance(v, str) and (empty_ok or bool(v.strip()))


def shared_keys(spec: dict) -> set[str]:
    return SHARED_COMMON | set(spec.get("fields", {}))


def check_shared_entry(spec: dict, e: dict, where: str, problems: list[str]):
    kind = spec["kind"]
    unknown = set(e) - shared_keys(spec) - {"_part"}
    if unknown:
        _bad(problems, where, f"unknown key(s) {sorted(unknown)} — a shared entry holds only "
             f"{sorted(shared_keys(spec))}; learner prose goes in the language files")
    if kind == "item":
        for f, typ in spec.get("fields", {}).items():
            v = e.get(f)
            if typ == "str" and not _is_str(v, empty_ok=(f != spec["headword"])):
                _bad(problems, where, f"`{f}` must be a{' non-empty' if f == spec['headword'] else ''} string")
            if typ == "list" and not (isinstance(v, list) and all(_is_str(x) for x in v)):
                _bad(problems, where, f"`{f}` must be a list of non-empty strings")
        if spec["headword"] == "kanji" and not (e.get("on") or e.get("kun")):
            _bad(problems, where, "a kanji needs at least one 音読み or 訓読み")
    lo, hi = spec.get("examples", [0, 99])
    ex = e.get("examples", [])
    if not (isinstance(ex, list) and all(_is_str(x) for x in ex)):
        _bad(problems, where, "`examples` must be a list of non-empty strings")
    elif not lo <= len(ex) <= hi:
        _bad(problems, where, f"{len(ex)} example(s); {spec['stem']} takes {lo}–{hi}")
    srcs = e.get("sources")
    if not (isinstance(srcs, list) and srcs):
        _bad(problems, where, "`sources` must list at least one {ref, page?, note?} — refs/ "
             "decides which points exist and what they mean, and every entry cites it")
    else:
        for s in srcs:
            if not (isinstance(s, dict) and _is_str(s.get("ref"))) or set(s) - {"ref", "page", "note"}:
                _bad(problems, where, f"bad source {s!r} — {{ref, page?, note?}}")
            elif "page" in s and not (isinstance(s["page"], int) and s["page"] >= 1):
                _bad(problems, where, f"source page {s['page']!r} must be a positive int")
    if not isinstance(e.get("related", []), list):
        _bad(problems, where, "`related` must be a list of ids")
    if "group" in e and not _is_str(e["group"]):
        _bad(problems, where, "`group` must be a non-empty string")
    if "tags" in e and not (isinstance(e["tags"], list) and all(_is_str(t) for t in e["tags"])):
        _bad(problems, where, "`tags` must be a list of non-empty strings")
    if "official_count" in e and not (isinstance(e["official_count"], int)
                                      and not isinstance(e["official_count"], bool)
                                      and e["official_count"] >= 0):
        _bad(problems, where, "`official_count` must be an int >= 0")
    if "pitch" in e:
        pv = e["pitch"]

        def drops(v):
            return isinstance(v, list) and v and all(isinstance(x, int) and not isinstance(x, bool)
                                                     and x >= 0 for x in v)
        if "words" in spec.get("fields", {}):
            words = {D.plain(w) for w in e.get("words", []) or [] if isinstance(w, str)}
            if not (isinstance(pv, dict) and all(k in words and drops(v) for k, v in pv.items())):
                _bad(problems, where, "`pitch` on a 漢字 entry is {<word in `words`, markup stripped>: "
                     "[drop positions]} — only for words whose accent you checked")
        elif not drops(pv):
            _bad(problems, where, "`pitch` must be a non-empty list of accent-drop positions (ints >= 0)")
    qlo, qhi = spec.get("quiz", [0, 99])
    qs = e.get("quiz", [])
    if not isinstance(qs, list):
        _bad(problems, where, "`quiz` must be a list")
        return
    if not qlo <= len(qs) <= qhi:
        _bad(problems, where, f"{len(qs)} quiz item(s); {spec['stem']} takes {qlo}–{qhi}")
    for n, q in enumerate(qs, 1):
        qw = f"{where} quiz {n}"
        if not isinstance(q, dict) or set(q) - {"stem", "options", "answer"}:
            _bad(problems, qw, "a quiz item is exactly {stem, options, answer}")
            continue
        if not _is_str(q.get("stem")):
            _bad(problems, qw, "empty stem")
        opts = q.get("options")
        if not (isinstance(opts, list) and len(opts) == 4 and all(_is_str(o) for o in opts)):
            _bad(problems, qw, "needs exactly 4 non-empty options")
        elif len({D.plain(o).strip() for o in opts}) != 4:
            _bad(problems, qw, f"duplicate options {opts} — four DIFFERENT choices, one defensible")
        a = q.get("answer")
        if not (isinstance(a, int) and not isinstance(a, bool) and 1 <= a <= 4):
            _bad(problems, qw, f"answer {a!r} must be 1–4 (1-based)")


def band_problems(kind: str, code: str, pr: dict, where: str, problems: list[str]):
    f = langs.length_factor(code)
    caps = KNOWLEDGE_BANDS[kind]
    for k, cap in caps.items():
        lim = int(cap * f)
        vals = pr.get(k)
        vals = vals if isinstance(vals, list) else [vals] if isinstance(vals, str) else []
        for i, v in enumerate(vals, 1):
            if isinstance(v, str) and len(D.plain(v)) > lim:
                _bad(problems, where, f"{code} `{k}`{f'[{i}]' if len(vals) > 1 or k in ('quiz', 'body') else ''} "
                     f"is {len(D.plain(v))} chars > {lim} ({cap} × {f:g})")


def check_prose_entry(spec: dict, code: str, eid: str, pr, entry: dict, where: str,
                      problems: list[str]):
    kind = spec["kind"]
    if not isinstance(pr, dict):
        _bad(problems, where, "prose must be an object")
        return
    leaked = set(pr) & (shared_keys(spec) - {"quiz"})
    if leaked:
        _bad(problems, where, f"carries shared-material key(s) {sorted(leaked)} — the shared "
             f"file is the ONE copy of them; a language file holds prose only")
    unknown = set(pr) - PROSE_KEYS[kind] - leaked
    if unknown:
        _bad(problems, where, f"unknown key(s) {sorted(unknown)} — allowed {sorted(PROSE_KEYS[kind])}")
    if kind == "item":
        optional = set(spec.get("prose_optional", []))
        for k in ("meaning", "usage", "nuance", "compare"):
            empty_ok = k in optional or (k == "compare" and not entry.get("related"))
            if not _is_str(pr.get(k), empty_ok=empty_ok):
                _bad(problems, where, f"`{k}` must be a {'string' if empty_ok else 'non-empty string'}"
                     + (" (\"\" only when `related` is empty)" if k == "compare" and not empty_ok else ""))
    else:
        if not _is_str(pr.get("title")):
            _bad(problems, where, "`title` must be a non-empty string")
        body = pr.get("body")
        lo, hi = GUIDE_BODY_PARAGRAPHS
        if not (isinstance(body, list) and lo <= len(body) <= hi and all(_is_str(b) for b in body)):
            _bad(problems, where, f"`body` must be {lo}–{hi} non-empty paragraphs")
    if "example_notes" in pr:
        if code == langs.primary():
            _bad(problems, where, "the primary language carries no `example_notes` — the "
                 "examples ARE in it")
        elif not (isinstance(pr["example_notes"], list)
                  and len(pr["example_notes"]) == len(entry.get("examples", []))
                  and all(isinstance(x, str) for x in pr["example_notes"])):
            _bad(problems, where, f"`example_notes` must be one string per example "
                 f"({len(entry.get('examples', []))})")
    nq = len(entry.get("quiz", []) or [])
    qx = pr.get("quiz", [])
    if nq and not (isinstance(qx, list) and len(qx) == nq and all(_is_str(x) for x in qx)):
        _bad(problems, where, f"`quiz` must hold one non-empty explanation per quiz item ({nq})")
    elif not nq and qx:
        _bad(problems, where, "`quiz` explanations for an entry with no quiz items")
    band_problems(kind, code, pr, where, problems)


def ref_status(ref: str, git_tracks) -> str:
    """ok | missing | absent-binary.

    Mirrors check_refs: a refs/ extract (`*.md`/`*.json`, tracked in git) must be
    on disk, so a missing one FAILs. A refs/ binary is gitignored and lives on the
    `refs` release, so a machine without that source SKIPs it — unless the
    source's folder IS on this machine with other binaries in it, in which case a
    cited file that is not there is a wrong path, and FAILs.
    """
    p = ROOT / ref
    if p.exists():
        return "ok"
    if not ref.startswith("refs/"):
        return "missing"
    if p.suffix.lower() in (".md", ".json") or git_tracks(ref):
        return "missing"
    folder = p.parent
    while folder != ROOT / "refs" and not folder.exists():
        folder = folder.parent
    if folder != ROOT / "refs" and any(f.suffix.lower() in ARCHIVE_BINARY
                                       for f in folder.rglob("*") if f.is_file()):
        return "missing"
    return "absent-binary"


def _default_git_tracks(path: str) -> bool:
    import subprocess
    try:
        out = subprocess.run(["git", "ls-files", "--", path], cwd=ROOT,
                             capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return False
    return bool(out.stdout.strip())


def check_band_doc(check):
    """SKILL.md's band table must print KNOWLEDGE_BANDS (the constant owns the numbers)."""
    text = SKILL_MD.read_text(encoding="utf-8") if SKILL_MD.is_file() else ""
    got = {}
    for kind, field, cap in re.findall(r"^\|\s*(item|guide)\s*\|\s*`(\w+)`\s*\|\s*(\d+)\s*\|", text, re.M):
        got.setdefault(kind, {})[field] = int(cap)
    check("jlpt-knowledge/SKILL.md band table == check_knowledge.KNOWLEDGE_BANDS", got == KNOWLEDGE_BANDS,
          f"doc {got} vs code {KNOWLEDGE_BANDS} — edit KNOWLEDGE_BANDS, then refresh the table from it")


def check_category(level: str, spec: dict, check, warn, skip, git_tracks):
    stem, kind = spec["stem"], spec["kind"]
    tag = f"knowledge/{level}/{stem}"
    cat = D.locate(level, spec)
    problems: list[str] = []

    if cat.layout == "none":
        warn(f"{tag}: has a shared file", False,
             f"neither {stem}.json nor {stem}/<part>.json exists — the page says 準備中; "
             f"create the category's shared file (jlpt-knowledge §Files)")
    check(f"{tag}: one layout (single file OR split parts)", cat.layout != "both",
          f"both {stem}.json and {stem}/ exist — move every entry into one of them")
    check(f"{tag}: every language file has its shared file", not cat.orphan,
          f"{[_rel(p) for p in cat.orphan]} — a language file sits "
          f"beside the shared file of the same name")
    warn(f"{tag}: language files are for active languages", not cat.stray,
         f"{[_rel(p) for p in cat.stray]} — not in "
         f"languages/index.json `order`; the page ignores them")

    entries: list[dict] = []
    for p in cat.parts:
        rel = _rel(p.shared)
        try:
            doc = D.read_json(p.shared)
        except json.JSONDecodeError as ex:
            _bad(problems, rel, f"does not parse: {ex}")
            continue
        if not isinstance(doc, dict) or not isinstance(doc.get("entries"), list):
            _bad(problems, rel, "must be {category, level, kind, entries: [...]}")
            continue
        for k, want in (("category", stem), ("level", level), ("kind", kind)):
            if doc.get(k) != want:
                _bad(problems, rel, f"`{k}` is {doc.get(k)!r}, expected {want!r}")
        extra = set(doc) - {"category", "level", "kind", "entries", "part"}
        if extra:
            _bad(problems, rel, f"unknown top-level key(s) {sorted(extra)}")
        for i, e in enumerate(doc["entries"]):
            if not isinstance(e, dict):
                _bad(problems, f"{rel}[{i}]", "entry must be an object")
                continue
            eid = e.get("id")
            where = f"{rel} {eid if isinstance(eid, str) else f'[{i}]'}"
            if not (isinstance(eid, str) and ID_RE.match(eid)):
                _bad(problems, where, f"id {eid!r} must match {ID_RE.pattern} (stable ascii)")
            check_shared_entry(spec, e, where, problems)
            entries.append({**e, "_where": where, "_part": p.name})

    ids = Counter(e.get("id") for e in entries)
    dups = sorted(i for i, n in ids.items() if n > 1 and isinstance(i, str))
    check(f"{tag}: ids are unique across the category", not dups, f"duplicated: {dups}")
    known = set(ids)
    dangling = [f"{e['_where']} → {r}" for e in entries for r in (e.get("related") or [])
                if isinstance(e.get("related"), list) and r not in known]
    self_rel = [e["_where"] for e in entries if e.get("id") in (e.get("related") or [])]
    check(f"{tag}: every `related` id exists", not dangling and not self_rel,
          "; ".join(dangling[:8] + [f"{w} relates to itself" for w in self_rel[:3]])
          + " — point at an id in this category, or drop it")

    missing_refs, absent = [], set()
    for e in entries:
        for s in e.get("sources") or []:
            if isinstance(s, dict) and isinstance(s.get("ref"), str):
                st = ref_status(s["ref"], git_tracks)
                if st == "missing":
                    missing_refs.append(f"{e['_where']}: {s['ref']}")
                elif st == "absent-binary":
                    absent.add(s["ref"])
    check(f"{tag}: every `sources[].ref` resolves", not missing_refs,
          "; ".join(missing_refs[:8]) + " — cite a path that exists in the tree "
          "(AGENTS.md §3 lists them); a tracked refs/*.md extract must be present")
    if absent:
        skip(f"{tag}: {len(absent)} cited refs/ binaries resolve",
             "the refs/ source archive is not on this machine (gitignored; AGENTS.md §3)")

    if spec["kind"] == "item" and entries:
        hw = Counter((D.plain(str(e.get(spec["headword"], ""))),
                      D.plain(str(e.get(spec.get("reading") or "", "")))) for e in entries)
        rep = [f"{h}（{r}）" if r else h for (h, r), n in hw.items() if n > 1]
        warn(f"{tag}: no headword is entered twice", not rep,
             f"{rep[:6]} — merge them, or make the headwords differ if they are different points")

    by_id = {e.get("id"): e for e in entries if isinstance(e.get("id"), str)}
    for code in langs.order():
        files = [(p, p.lang_files.get(code)) for p in cat.parts]
        have: set[str] = set()
        for p, f in files:
            if f is None:
                continue
            rel = _rel(f)
            try:
                doc = D.read_json(f)
            except json.JSONDecodeError as ex:
                _bad(problems, rel, f"does not parse: {ex}")
                continue
            if not isinstance(doc, dict):
                _bad(problems, rel, "must be an object {id: prose}")
                continue
            part_ids = {e.get("id") for e in entries if e.get("_part") == p.name}
            for eid, pr in doc.items():
                if eid not in part_ids:
                    _bad(problems, rel, f"prose for {eid!r}, which its shared file "
                         f"{p.shared.name} does not have — add the entry there or drop the prose")
                    continue
                have.add(eid)
                check_prose_entry(spec, code, eid, pr, by_id[eid], f"{rel} {eid}", problems)
        lacking = [i for i in by_id if i not in have]
        warn(f"{tag}: every entry has {langs.name(code)} prose", not lacking,
             f"{len(lacking)} of {len(by_id)} without it ({lacking[:5]}…) — the card shows "
             f"{'only the shared material' if code == langs.primary() else 'the primary prose'} "
             f"until it is written (jlpt-knowledge §Batch workflow: one context per language)")

    check(f"{tag}: schema, bands and prose ({len(entries)} entries)", not problems,
          "; ".join(problems[:10]) + (f"; … {len(problems) - 10} more" if len(problems) > 10 else "")
          + " — jlpt-knowledge/SKILL.md §Schemas/§Bands")

    answers = Counter(q.get("answer") for e in entries for q in (e.get("quiz") or [])
                      if isinstance(q, dict))
    n = sum(answers.values())
    if n >= 8:
        exp = n / 4
        off = {k: answers.get(k, 0) for k in (1, 2, 3, 4)
               if not 0.5 * exp <= answers.get(k, 0) <= 1.5 * exp}
        warn(f"{tag}: quiz answer positions balanced ({n} items)", not off,
             f"counts {dict(sorted((k, answers.get(k, 0)) for k in (1, 2, 3, 4)))} — each "
             f"position should hold {exp * 0.5:.0f}–{exp * 1.5:.0f}; reorder options, "
             f"never re-key without re-solving")

    if QG.types(spec):
        check_generated(level, spec, cat, check, warn)

    check_book_order(level, spec, entries, check)

    # The built page(s), each stamped with every data file it was made from. A
    # split category is a list page plus one card page per part.
    if cat.layout == "split":
        pages = [(D.page_path(level, stem), D.category_page_sources(cat))]
        pages += [(D.part_page_path(level, stem, p.name), D.part_page_sources(cat, p))
                  for p in cat.parts]
    else:
        pages = [(D.page_path(level, stem), cat.sources())]
    for page, srcs in pages:
        name = _rel(page)
        want = {D.stamp_name(level, f): D.source_sha(f) for f in srcs}
        if not page.is_file():
            check(f"{name} is built", False, f"run `make knowledge LEVEL={level}`")
            continue
        got = D.read_stamps(page)
        stale = sorted({k for k, _ in set(want.items()) ^ set(got.items())})
        check(f"{name} matches the data it stamps", not stale,
              f"{len(stale)} file(s) changed since the build ({stale[:4]}) — run "
              f"`make knowledge LEVEL={level}`; the JSON is the single source of truth")
        if cat.layout == "split" and page == D.page_path(level, stem):
            continue                     # the parts list: it holds no cards
        mine = [e for e in entries if cat.layout != "split" or e.get("_part") == page.stem]
        want_ids = [e["id"] for e in D.book_sorted(spec, mine, level) if isinstance(e.get("id"), str)]
        shown = page_card_ids(page)
        check(f"{name} lists its cards in book order", shown == want_ids,
              (f"page order differs from book order at card {next((i for i, (a, b) in enumerate(zip(shown, want_ids)) if a != b), min(len(shown), len(want_ids))) + 1}"
               if shown is not None else "no card list (`const E = [...]`) found in the page")
              + f" — run `make knowledge LEVEL={level}`; the builder sorts by knowledge_data.book_sorted "
                f"and nothing on the page may reorder cards (SKILL §Book order)")
    sub = D.level_dir(level) / stem
    built = {pg for pg, _ in pages}
    stray = [_rel(h) for h in (sorted(sub.glob("*.html")) if sub.is_dir() else []) if h not in built]
    if cat.layout == "split" or sub.is_dir():
        check(f"{tag}/: no part page without its part", not stray,
              f"{stray[:4]} — a leftover of a removed part or an un-split category; "
              f"`make knowledge LEVEL={level}` deletes them")


_PAGE_E = re.compile(r"^const E = (\[.*\]);$", re.M)


def page_card_ids(page: Path) -> list[str] | None:
    """The ids of the cards a built page embeds, in the order it lists them."""
    m = _PAGE_E.search(page.read_text(encoding="utf-8"))
    if not m:
        return None
    try:
        return [c.get("id") for c in json.loads(m.group(1))]
    except (ValueError, AttributeError):
        return None


def check_book_order(level: str, spec: dict, entries: list[dict], check):
    """SKILL §Book order: every entry has a key, keys are unique unless a documented
    same-number split, and (文法) the `book` key is one the inventory assigns and
    implies the entry's `group` label."""
    tag = f"knowledge/{level}/{spec['stem']}"
    how = spec.get("order")
    check(f"{tag}: categories.json declares its book order", how in ("book", "id"),
          f"`order` is {how!r} — \"book\" (a `book` field per entry) or \"id\" (with `order_series`); "
          f"every category is listed in the order of its book, never a custom one")
    if how not in ("book", "id") or not entries:
        return
    keys = D.order_keys(spec, entries, level)
    nokey = [e["_where"] for e in entries if isinstance(e.get("id"), str) and e["id"] not in keys]
    rule = ("a valid `book` [section, lesson, item(, split)] copied from its inventory row"
            if how == "book" else f"an id matching `order_series` {spec.get('order_series')}")
    check(f"{tag}: every entry has a book-order key", not nokey,
          f"{len(nokey)} without one ({nokey[:5]}) — needs {rule} (SKILL §Book order)")
    if how != "book":
        return
    probs = []
    splits = spec.get("book_splits") or {}
    rows = D.inventory_rows(level, spec["stem"])
    inv_by_id = {r["id"]: r["book"] for r in rows if D.valid_book(r.get("book"))}
    inv_keys = {tuple(b[:3]) for b in inv_by_id.values()}
    by_triple: dict[tuple, list[dict]] = {}
    for e in entries:
        b = e.get("book")
        if not D.valid_book(b):
            continue
        t = tuple(b[:3])
        by_triple.setdefault(t, []).append(e)
        want = D.book_group(spec, b)
        if want is None:
            probs.append(f"{e['_where']}: section {b[0]} is not in categories.json `book_sections`")
        elif e.get("group") != want:
            probs.append(f"{e['_where']}: `group` 「{e.get('group')}」 but `book` {b} is 「{want}」")
        if inv_keys and t not in inv_keys:
            probs.append(f"{e['_where']}: `book` {b} is no position the inventory assigns")
        ib = inv_by_id.get(e.get("id"))
        if ib and (b[:3] != ib[:3] or (len(ib) == 4 and b != ib)):
            probs.append(f"{e['_where']}: `book` {b} but its inventory row says {ib}")
        if len(b) == 4 and "-".join(map(str, t)) not in splits:
            probs.append(f"{e['_where']}: split key {b} — {'-'.join(map(str, t))} is not in `book_splits`")
    for t, es in by_triple.items():
        if len(es) < 2:
            continue
        name = "-".join(map(str, t))
        subs = [e["book"][3] if len(e["book"]) == 4 else None for e in es]
        if name not in splits or None in subs or len(set(subs)) != len(subs):
            probs.append(f"{', '.join(e.get('id', '?') for e in es)} share book {list(t)} — one entry per "
                         f"position, unless a same-number split listed in categories.json `book_splits` "
                         f"with a distinct 4th element each")
    check(f"{tag}: `book` keys are unique, inventory-backed and match `group`", not probs,
          "; ".join(probs[:8]) + (f"; … {len(probs) - 8} more" if len(probs) > 8 else "")
          + " — the key is derived once from the Shin Kanzen 目次 (inventory `book`); fix the "
            "entry, never the page (SKILL §Book order)")


def check_generated(level: str, spec: dict, cat: D.Category, check, warn):
    """The builder's generated 語彙/漢字 items (quiz_gen.py) re-verified against the data —
    the integrity rules that make generation safe (SKILL.md §Quiz integrity):
    a reading distractor is never the key, never a reading the vendored dataset lists
    for the headword, never another same-headword entry's reading; a meaning
    distractor never comes from this entry, its `related` (either direction) or a
    same-headword entry, and is that owner's own meaning, differing from the key."""
    tag = f"knowledge/{level}/{spec['stem']}"
    entries, prose = D.load_entries(cat)
    entries = [e for e in entries if isinstance(e.get("id"), str)]
    if not entries:
        return
    kinds = QG.types(spec)
    if "reading" in kinds:
        check(f"{tag}: the pitch dataset loads (the reading quiz's integrity check needs it)",
              QG.dataset_ok() and PITCH is not None,
              "references/pitch/accents.tsv.gz or pitch.py failed to load — without it no "
              "reading item can be proved safe, so none is generated")
    by_id = {e["id"]: e for e in entries}
    hw = {e["id"]: QG.headword(e, spec) for e in entries}
    # (word, reading) pairs, walked here from the data rather than taken from the generator
    same_word: dict[str, set[str]] = {}
    for e in entries:
        if spec["headword"] == "kanji":
            for w in e.get("words") or []:
                r = QG.kana_of(w)
                if r:
                    same_word.setdefault(D.plain(w).strip("〜～"), set()).add(r)
        else:
            r = QG.to_hira(QG.clean(str(e.get(spec.get("reading") or "", ""))))
            if r:
                same_word.setdefault(hw[e["id"]], set()).add(r)
    gen = QG.generate(spec, entries, prose)
    problems, n, seen = [], 0, set()
    for eid, items in gen.items():
        e = by_id.get(eid)
        for it in items:
            n += 1
            w = f"{eid} {it['qid']}"
            if it["qid"] in seen or it["qid"] != QG.qid(eid, it["kind"]):
                _bad(problems, w, "qid repeated or not <id>#r / <id>#m")
            seen.add(it["qid"])
            opts, a = it.get("options") or [], it.get("answer")
            flat = [o if isinstance(o, str) else D.plain(o.get(langs.primary(), "")) for o in opts]
            if len(opts) != 4 or len(set(flat)) != 4 or not (isinstance(a, int) and 1 <= a <= 4):
                _bad(problems, w, f"needs 4 distinct options and an answer 1–4: {flat} / {a!r}")
                continue
            if opts[a - 1] != it["key"]:
                _bad(problems, w, "the keyed option is not the entry's own reading/meaning")
            ds = [o for i, o in enumerate(opts) if i != a - 1]
            if it["kind"] == "reading":
                word, key = it["word"], it["key"]
                valid = set(same_word.get(word, set()))
                if PITCH is not None:
                    valid |= {QG.to_hira(r) for r in PITCH.readings(word)}
                if key not in same_word.get(word, set()):
                    _bad(problems, w, f"key 「{key}」 is not a reading the entry gives 「{word}」")
                for d in ds:
                    if d == key or d in valid:
                        _bad(problems, w, f"distractor 「{d}」 is a valid reading of 「{word}」 "
                             f"(entry data or the vendored UniDic/Open JTalk dataset)")
            else:
                mine = QG.meanings(prose, eid)
                if any(it["key"].get(c) != mine.get(c) for c in it["key"]):
                    _bad(problems, w, "keyed meaning is not the entry's own `meaning`")
                banned = {eid} | set(e.get("related") or []) | {
                    x["id"] for x in entries
                    if eid in (x.get("related") or []) or hw[x["id"]] == hw[eid]}
                for d in it["distractors"]:
                    o = d.get("owner")
                    if o in banned:
                        _bad(problems, w, f"meaning distractor from {o}, which is this entry, "
                             f"a `related` look-alike or a same-headword entry")
                    theirs = QG.meanings(prose, o) if o in by_id else {}
                    for c, t in d["text"].items():
                        if theirs.get(c) != t or D.plain(t).strip() == D.plain(mine.get(c, "")).strip():
                            _bad(problems, w, f"{c} distractor 「{D.plain(t)}」 is not {o}'s own "
                                 f"meaning, or equals the key")
    check(f"{tag}: {n} generated quiz items keep the integrity rules", not problems,
          "; ".join(problems[:8]) + (f"; … {len(problems) - 8} more" if len(problems) > 8 else "")
          + " — quiz_gen.py must exclude it (jlpt-knowledge §Quiz integrity); never hand-patch a page")
    short = []
    for e in entries:
        got = {it["kind"] for it in gen.get(e["id"], [])}
        if "reading" in kinds and "reading" not in got and QG.reading_target(e, spec):
            short.append(f"{e['id']}#r")
        if "meaning" in kinds and "meaning" not in got and langs.primary() in QG.meanings(prose, e["id"]):
            short.append(f"{e['id']}#m")
    warn(f"{tag}: every entry gets its generated quiz items", not short,
         f"{len(short)} skipped for want of 3 safe distractors ({short[:6]}) — normal while a "
         f"category is small; it fills as batches land")


def check_index(level: str, check):
    page = D.level_dir(level) / D.INDEX_HTML
    srcs = [p.shared for spec in D.categories(level) for p in D.locate(level, spec).parts]
    want = {D.stamp_name(level, f): D.source_sha(f) for f in srcs}
    if not page.is_file():
        check(f"knowledge/{level}/index.html is built", False, f"run `make knowledge LEVEL={level}`")
        return
    got = D.read_stamps(page)
    check(f"knowledge/{level}/index.html matches the data it stamps", got == want,
          f"run `make knowledge LEVEL={level}` (the index prints every category's entry count)")


def check_store_keys(check):
    """The knowledge module's localStorage prefix is spelled once, in local_store.py."""
    ls_path = ROOT / ".agents" / "exam-app" / "scripts" / "local_store.py"
    src = ls_path.read_text(encoding="utf-8")
    m = re.search(r'^KNOWLEDGE_PREFIX = "([^"]+)"', src, re.M)
    mock = re.search(r'^STORAGE_PREFIX = "([^"]+)"', src, re.M)
    check("local_store.py defines the knowledge store under its own prefix",
          bool(m) and bool(mock) and not m.group(1).startswith(mock.group(1) + "/"),
          "JLPTStore.ids() lists every key under STORAGE_PREFIX as a test; the knowledge "
          "store must live elsewhere")
    if m:
        leak = [_rel(p) for p in HERE.glob("*.py") if m.group(1) in p.read_text(encoding="utf-8")]
        check("knowledge localStorage keys are spelled only in local_store.py", not leak,
              f"also in {leak} — use JLPTKnowledgeStore")


# Readings that have shipped wrong more than once (B3 F11, B5 QA, 2026-09-30):
# a numeral + 時 read とき, a numeral + 分 read ふん where Japanese says ぷん
# (一/三/四/六/八/十; 十分 is じゅっぷん as a duration), and 入 read いっ. Each
# pattern allows the optional ruby group, so both ｜六時《ろくとき》 and
# 六時《ろくとき》-style markup are seen. A WARN, not a FAIL: 十分《じゅうぶん》
# ("enough") is right, and a reviewer decides.
RUBY_SUSPECTS = [
    (re.compile(r"[0-9０-９一二三四五六七八九十百]+｜?時《[^》]*とき》|時《とき》(?=\S*[0-9０-９])"),
     "a clock time read とき — should be じ"),
    (re.compile(r"｜?[一三四六八十百]分《[^》]*ふん》"), "分 after 一/三/四/六/八/十 read ふん — should be ぷん"),
    (re.compile(r"｜?入《いっ》"), "入 read いっ — should be はい/い"),
]


def check_ruby_suspects(level: str, spec: dict, warn):
    """WARN on the furigana errors that have shipped twice (RUBY_SUSPECTS)."""
    cat = D.locate(level, spec)
    hits = []
    for part in cat.parts:
        files = part.lang_files.values() if isinstance(part.lang_files, dict) else part.lang_files
        for path in [part.shared] + [p for p in files if p]:
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for rx, why in RUBY_SUSPECTS:
                for m in rx.finditer(text):
                    hits.append(f"{_rel(path)}: 「{m.group(0)}」 ({why})")
    warn(f"knowledge/{level}/{spec['stem']}: no known-bad furigana readings", not hits,
         "; ".join(hits[:6]) + (f" … and {len(hits) - 6} more" if len(hits) > 6 else "")
         + " — fix the ruby by hand (jlpt-knowledge §Quiz integrity; exam-model-answer "
           "furigana pitfalls)")


# Prose never names its source (SKILL §Quiz integrity rules 18/28): a sitting date
# 「7/2019」, a book-page tag 「（本のp.43）」「SK」 or 「この本」 inside a learner's
# text. Citations live in `sources` (whose notes may carry dates — only the
# language files are read here). Found by the B4, B5 and 漢字 B1 QA rounds.
PROSE_CITES = re.compile(r"(?<![0-9])(?:1[0-2]|[1-9])/20[0-9]{2}(?![0-9])|本のp\.?[0-9]|この本|(?<![A-Za-z])SK(?![A-Za-z])")

GUIDE_CITES = re.compile(r"新完全マスター|完全模試|総まとめ|Shin ?Kanzen|Soumatome|本のp|この本|例題|"
                         r"第[0-9０-９一二三]部|(?<![A-Za-z])SK(?![A-Za-z])|\\btr\\. ?[0-9]|[Vv]í dụ [0-9]+ (?:của|trong) sách|Trang [0-9]")


def check_prose_citations(level: str, spec: dict, warn):
    # A guide may state exam history (「12/2022から問題11は4文章」) and point at a
    # paper that is ON this site, so dates are allowed there; a book, page,
    # part or 例題 number never is (読解 G2 QA: 105 live guide paragraphs cited
    # 『完全模試』 / "Shin Kanzen (tr.N)" / 「第1部」).
    rx = PROSE_CITES if spec.get("kind") == "item" else GUIDE_CITES
    cat = D.locate(level, spec)
    hits = []
    for part in cat.parts:
        files = part.lang_files.values() if isinstance(part.lang_files, dict) else part.lang_files
        for path in files:
            if not path or not path.is_file():
                continue
            for eid, pr in D.read_json(path).items():
                for field, v in pr.items():
                    for t in (v if isinstance(v, list) else [v]):
                        m = rx.search(str(t))
                        if m:
                            hits.append(f"{_rel(path)} {eid}.{field}: 「{m.group(0)}」")
    warn(f"knowledge/{level}/{spec['stem']}: prose names no source", not hits,
         "; ".join(hits[:6]) + (f" … and {len(hits) - 6} more" if len(hits) > 6 else "")
         + " — citations belong in `sources`; say 「問題1で」, never the sitting or book")


def check_all(check, warn, skip, git_tracks=None):
    git_tracks = git_tracks or _default_git_tracks
    print("\nknowledge module (jlpt-knowledge: knowledge/<LEVEL>/)")
    check_band_doc(check)
    check_store_keys(check)
    probs = []
    for lv in D.levels():
        for spec in D.categories(lv):
            if spec.get("kind") not in KNOWLEDGE_BANDS:
                probs.append(f"{lv}/{spec.get('stem')}: kind {spec.get('kind')!r}")
            for k in ("label", "desc"):
                if spec.get(k) not in langs.ui(langs.primary(), "knowledge"):
                    probs.append(f"{lv}/{spec.get('stem')}: {k} {spec.get(k)!r} is not a knowledge.json key")
            for f in spec.get("facts", []):
                if f"field_{f}" not in langs.ui(langs.primary(), "knowledge"):
                    probs.append(f"{lv}/{spec.get('stem')}: no knowledge.json label field_{f}")
    check("categories.json kinds and label keys resolve", not probs, "; ".join(probs))
    for lv in D.levels():
        if not D.categories(lv):
            continue
        if not D.level_dir(lv).is_dir():
            skip(f"knowledge/{lv}/", "no knowledge data for this level yet")
            continue
        for spec in D.categories(lv):
            check_category(lv, spec, check, warn, skip, git_tracks)
            check_ruby_suspects(lv, spec, warn)
            check_prose_citations(lv, spec, warn)
        check_index(lv, check)


if __name__ == "__main__":
    fails, warns = [], []

    def _check(name, ok, detail=""):
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}" + (f" — {detail}" if detail and not ok else ""))
        if not ok:
            fails.append(name)
        return ok

    def _warn(name, ok, detail=""):
        print(f"  {'ok  ' if ok else 'WARN'}  {name}" + (f" — {detail}" if detail and not ok else ""))
        if not ok:
            warns.append(name)

    def _skip(name, why):
        print(f"  skip  {name} — {why}")

    check_all(_check, _warn, _skip)
    print(f"\n{len(fails)} FAIL, {len(warns)} WARN")
    sys.exit(1 if fails else 0)
