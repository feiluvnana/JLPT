#!/usr/bin/env python3
"""The drill module's gate checks — called by tools/check_consistency.py.

    python3 .agents/jlpt-drill/scripts/check_drill.py      # standalone, same checks

`check_all(check, warn, skip)` takes the gate's own reporters. Every rule is
documented in jlpt-drill/SKILL.md; each message names the rule and the repair.

FAIL: the drill store's keys spelled outside local_store.py or under the exam
store's prefix; the `drill` UI namespace unregistered; a built page missing, or
one the builder would not write; any non-HTML file under drill/<LEVEL>/ (the
module authors no data — its pools are read from tests/ and logs/); a page
without exactly one `.topbar` and one `.lang-select`, with the retired
`.lang-btn`, or with a root-absolute link; a baked item with no primary-language
explanation (explanations come from 詳細解説, never retyped).
WARN: a page older than the data it bakes (any test, the clip bank or a 知識
file changed since `make drill`) — the drill is a derived view that every
test edit moves, so staleness is a work item, not a broken page.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drill_data as D     # noqa: E402
import langs               # noqa: E402
import level as LEVEL      # noqa: E402

ROOT = D.ROOT
LOCAL_STORE = ROOT / ".agents" / "exam-app" / "scripts" / "local_store.py"
ABS_LINK = re.compile(r'''(?:href|src)=["']/(?!/)''')


def _rel(p: Path) -> str:
    try:
        return p.relative_to(ROOT).as_posix()
    except ValueError:
        return p.as_posix()


def check_store(check):
    src = LOCAL_STORE.read_text(encoding="utf-8")
    m = re.search(r'^DRILL_PREFIX = "([^"]+)"', src, re.M)
    mock = re.search(r'^STORAGE_PREFIX = "([^"]+)"', src, re.M)
    check("local_store.py defines the drill store under its own prefix",
          bool(m) and bool(mock) and not m.group(1).startswith(mock.group(1) + "/"),
          "JLPTStore.ids() lists every key under STORAGE_PREFIX as a test; JLPTDrillStore "
          "must live elsewhere (jlpt-drill/SKILL.md §Store)")
    if m:
        leak = [_rel(p) for p in HERE.glob("*.py") if m.group(1) in p.read_text(encoding="utf-8")]
        check("drill localStorage keys are spelled only in local_store.py", not leak,
              f"also in {leak} — use window.JLPTDrillStore")


def check_level(level: str, check, warn, skip):
    import build_drill as B          # imported late: it pulls in the renderers
    out = D.level_dir(level)
    gp, cp = D.gengo_pool(level), D.choukai_pool(level)
    if not gp.items and not cp.clips:
        if out.is_dir():
            check(f"drill/{level}/ has a pool behind it", False,
                  "no test with 詳細解説 and no playable clip for this level — delete the folder")
        return
    if not out.is_dir():
        # Build output, gitignored: `make pages` (and so CI) builds it. A clone
        # that has not run `make drill` has nothing to check — a skip, not a pass.
        skip(f"drill/{level}/ is not built on this machine — `make drill LEVEL={level}` "
             f"(make pages builds it for the site)")
        return
    tag = f"drill/{level}"
    want = set(B.expected_pages(level, gp))
    have = {p.relative_to(out).as_posix() for p in out.rglob("*.html")}
    check(f"{tag}: every tool page is built ({len(want)} pages)", not (want - have),
          f"missing {sorted(want - have)[:5]} — run `make drill LEVEL={level}`")
    check(f"{tag}: no page the builder does not write", not (have - want),
          f"{sorted(have - want)[:5]} — a leftover; `make drill LEVEL={level}` deletes them")
    data = [_rel(p) for p in out.rglob("*") if p.is_file() and p.suffix != ".html"]
    check(f"{tag}: holds built pages only — no authored data", not data,
          f"{data[:5]} — the drill module authors nothing: items, clips and explanations "
          f"are read from tests/*/詳細解説*.json and logs/choukai_bank.json")

    bad_chrome, bad_links, stale = [], [], []
    now_sources = {D.stamp_name(p) for p in gp.sources + cp.sources if p.is_file()}
    for rel in sorted(want & have):
        page = out / rel
        text = page.read_text(encoding="utf-8")
        if (text.count('class="topbar"') != 1 or text.count('class="lang-select"') != 1
                or 'class="lang-btn' in text):
            bad_chrome.append(rel)
        if ABS_LINK.search(text):
            bad_links.append(rel)
        stamps = D.read_stamps(page)
        changed = [n for n, sha in stamps.items()
                   if not (ROOT / n).is_file() or D.source_sha(ROOT / n) != sha]
        if changed:
            stale.append(f"{rel} ({changed[0]})")
    idx = D.read_stamps(out / D.INDEX_HTML) if (out / D.INDEX_HTML).is_file() else {}
    unstamped = sorted(now_sources - set(idx))
    check(f"{tag}: every page carries one lang_ui top bar and one language dropdown",
          not bad_chrome, f"{bad_chrome[:4]} — render the page through lang_ui.topbar_html()")
    check(f"{tag}: every link is relative", not bad_links,
          f"{bad_links[:4]} — a root-absolute href/src breaks the Pages repo subpath")
    warn(f"{tag}: pages match the data they bake", not stale and not unstamped,
         (f"{len(stale)} page(s) older than their data ({stale[:3]})" if stale else "")
         + (f"; {len(unstamped)} source(s) not in the build ({unstamped[:3]})" if unstamped else "")
         + f" — run `make drill LEVEL={level}` (tests/, logs/choukai_bank.json and knowledge/ "
           f"are the source of truth)")

    no_prose = [i.id for i in gp.items
                if not (i.prose.get(langs.primary()) or {}).get("why_correct")]
    check(f"{tag}: every 言語知識・読解 item bakes its 詳細解説 explanation "
          f"({len(gp.items)} items, {len(gp.passages)} passages)", not no_prose,
          f"{len(no_prose)} without why_correct ({no_prose[:4]}) — author it in that test's "
          f"詳細解説.json (exam-model-answer); the drill never writes prose")
    bad_q = [q.id for c in cp.clips for q in c.questions
             if not (q.prose.get(langs.primary()) or {}).get("why_correct")
             or not 1 <= q.answer <= max(len(q.options), 3 if c.code == "問題4" else 4)]
    check(f"{tag}: every playable clip bakes a key and its bank explanation "
          f"({len(cp.clips)} clips; {len(cp.unplayable)} bank clip(s) not located in any test's audio)",
          not bad_q, f"{bad_q[:4]} — fix the record in logs/choukai_bank.json (choukai-audio Part 0)")
    missing = {c: sum(1 for i in gp.items if c not in i.prose) for c in langs.learners()}
    warn(f"{tag}: every item has prose in every registry language",
         not any(missing.values()),
         f"{missing} item(s) show the primary explanation under a note — author that "
         f"language's 詳細解説 file (exam-model-answer)")


def check_all(check, warn, skip, git_tracks=None):
    print("\ndrill module (jlpt-drill: drill/<LEVEL>/)")
    check("the `drill` UI namespace is registered", "drill" in langs.NAMESPACES,
          "add it to langs.NAMESPACES so check_language_registry holds every language's "
          "drill.json to the primary's keys")
    check_store(check)
    for lv in LEVEL.available():
        if not LEVEL.has_structure(lv):
            continue
        if not D.level_tests(lv) and not D.level_dir(lv).is_dir():
            skip(f"drill/{lv}/", "no test of this level yet")
            continue
        check_level(lv, check, warn, skip)


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
