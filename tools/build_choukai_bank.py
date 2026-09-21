#!/usr/bin/env python3
"""Build the 聴解 clip bank from the imported official sittings.

`logs/choukai_bank.json` is the item bank `sample_items.py` draws from and
`compose_choukai_mp3.py` cuts against. One record per item SLOT per sitting,
carrying the audio offsets plus the exact wording that already exists on disk:
the script block from `聴解スクリプト.txt`, the stem/options/script/explanation
fields from `詳細解説.json` and `詳細解説.vi.json`, and the key parsed by
`exam-app`'s own `parse_choukai_keys`.

Offsets, not audio
------------------
The bank stores byte-free spans and nothing else. `refs/` binaries and
`tests/*/聴解.mp3` are both out of git on purpose (AGENTS.md §3), so a bank of
300 pre-cut MP3s would be 300 more untracked files that a fresh clone lacks and
that no reviewer can read. Clips are cut on demand at compose time from the
sitting's own MP3; the bank stays a reviewable text artifact.

Slot-preserving draws
---------------------
Every record is tagged with the slot it occupied in its source paper, and the
composer may only place it in that same slot. This is not a stylistic choice:
official reads 「N番。」 continuously into the situation line with no pause
between them, so renumbering an item would mean cutting inside speech. Keeping
the slot means every cut lands in a structural silence.

The ten sittings this script banks all run 5/6/5/11/2, so each of their slots
has one candidate per sitting. **This paragraph used to say "all 31 sittings
run the same 5/6/5/11/2 shape" and that is refuted**: measured against
`refs/JLPT_N2_NEW/answer_keys.json`, 11 of the 31 do (2020-12 plus the ten
imports) and 20 do not — 問題4 ran 12 items until 2017-12, 問題2 ran 5 in
2013-07 and 2018-07 … 2019-12, 2012-12 ran 4 問題3 items, and every sitting
before 2020-12 had a three-item 問題5. The shape therefore comes from
`choukai_segment.slots_for(sitting)`, which derives it from that key file, and
not from a constant (`.agents/choukai-audio/references/archive_bank_expansion.md`
§2 and §6 Step 1; re-measured 2026-09-17).

The mixed pool (bank v2)
------------------------
Since 2026-09-08 the bank is not official-only: `tools/build_textbook_bank.py`
appends Shin Kanzen and Soumatome items to the same file, so every record now
carries `source` ("official" | "shinkanzen" | "soumatome") and
`needs_number_call`. This script owns the OFFICIAL records only and always
writes `source: "official"`, `needs_number_call: False` — an official item
speaks its own 「N番。」 and is slot-preserved, which is exactly what the
paragraph above is about. Textbook items have no number call, so they are banked
body-only, are slot-FREE, and the composer prepends a harvested call
(`tools/harvest_number_calls.py`).

Usage
-----
    python3 tools/build_choukai_bank.py              # all imports -> logs/
    python3 tools/build_choukai_bank.py --check      # reconcile only, no write
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from build_archive_bank import (  # noqa: E402
    build_records as build_archive_records)
from build_textbook_bank import (  # noqa: E402
    build_records as build_textbook_records,
    figure_dependent as figure_dependent_options)
from choukai_segment import (  # noqa: E402
    NotSegmented, hint_from_script, segment, slots_for)

BANK_PATH = ROOT / "logs" / "choukai_bank.json"
BANK_VERSION = 2

# Keep the cut this far inside the surrounding silence, so a soft breath or a
# speech tail the envelope read as quiet is never clipped. The composer lays
# its own canonical pause after the clip, so trimmed silence is not lost.
GUARD_S = 0.25

ITEM_RE = re.compile(r"^(\d+)番。")
SECTION_RE = re.compile(r"^問題([1-5])。")


def _load(path: Path):
    """Import a repo script by path (they are not on the import path)."""
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GRADE = _load(ROOT / ".agents" / "exam-app" / "scripts" / "grade_answers.py")


class Reconciliation(Exception):
    """The audio and the text on disk disagree about what this paper contains."""


# ---------------------------------------------------------------- text side

def parse_script_blocks(
        path: Path) -> tuple[dict[tuple[str, int], str], dict[str, list[str]]]:
    """`聴解スクリプト.txt` -> ({(問題N, slot): item block}, {問題N: preamble}).

    Blocks are separated by one blank line and an item block starts with
    `N番。`, the same contract `make_choukai_mp3.py`'s parser uses. Everything
    in a section that is NOT an item block is that section's preamble text —
    the `問題N。` marker and the instruction — and the composer prints it above
    the items it lifted from the same sitting, so the printed instruction is
    always the one the audio speaks.

    Blocks before the first `問題1。` are the opening announcement, returned
    under the key `opening`.

    Position matters: 問題5 carries a SECOND lead-in ("まず話を聞いてください。
    それから、二つの質問を聞いて…") that sits between 1番 and 2番, not before
    1番. Filing every non-item block as a preamble printed it in the wrong place
    in the composed script. Each preamble block is therefore tagged with the
    number of items already seen in its section, and the composer replays them
    at that position. (The AUDIO was always right — 2番's clip starts at 1番's
    answer pause and contains the lead-in.)
    """
    text = path.read_text(encoding="utf-8")
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
    items: dict[tuple[str, int], str] = {}
    preamble: dict[str, list[list]] = {"opening": []}
    section: str | None = None
    seen = 0
    for block in blocks:
        first = block.splitlines()[0]
        sec = SECTION_RE.match(first)
        if sec:
            section = f"問題{sec.group(1)}"
            seen = 0
            preamble.setdefault(section, []).append([0, block])
            continue
        item = ITEM_RE.match(first)
        if item and section:
            seen = int(item.group(1))
            items[(section, seen)] = block
        elif section is None:
            preamble["opening"].append([0, block])
        else:
            preamble[section].append([seen, block])
    return items, preamble


KEY_TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*\**(\d)\**\s*\|\s*(.*?)\s*\|$")


def parse_kaisetsu_cells(md_path: Path) -> dict[str, str]:
    """`聴解.md` -> {問N-M: the 解説 cell}, the per-option grounding lines.

    `exam-app`'s `parse_choukai_keys` already reads the correct-answer column of
    these same tables; this reads the third column, which is the writer's
    「N ✗「script line」→ reason」 grounding. Composing a paper reuses the source
    sitting's own cell rather than re-deriving one, so the booklet says what the
    booklet it came from said.
    """
    text = md_path.read_text(encoding="utf-8")
    marker = re.search(r"#+\s*【?正解[・\s]解説】?", text)
    if not marker:
        return {}
    out: dict[str, str] = {}
    section = None
    for line in text[marker.start():].splitlines():
        head = re.search(r"##\s*問題([1-5])", line)
        if head:
            section = int(head.group(1))
            continue
        row = KEY_TABLE_ROW.match(line.strip())
        if not (row and section):
            continue
        qlabel, _ans, cell = row.groups()
        qlabel = re.sub(r"[*\s]", "", qlabel)
        num = re.match(r"(\d+)", qlabel)
        if not num:
            continue
        key = f"問{section}-{num.group(1)}"
        if section == 5 and "質問" in qlabel:
            key += "-1" if "質問1" in qlabel else "-2"
        out[key] = cell
    return out


def item_key(section: str, slot: int, sub: int | None = None) -> str:
    """The `問N-M` id shared by 詳細解説.json and `parse_choukai_keys`."""
    base = f"問{section[-1]}-{slot}"
    return f"{base}-{sub}" if sub else base


def answer_ids(section: str, slot: int) -> list[str]:
    """The scored answer ids a slot produces — 問題5-2番 carries two.

    Slot 2 is the two-question item in the MODERN 問題5 only; every sitting
    before 2020-12 ran three 問題5 items with 質問1/質問2 on 3番. Those are not
    bankable without a number-call re-cut and are deferred
    (`archive_bank_expansion.md` §2 consequence 2, §6 Step 3), so this stays
    keyed on 2 — deliberately, not by oversight.
    """
    if section == "問題5" and slot == 2:
        return [item_key(section, slot, 1), item_key(section, slot, 2)]
    return [item_key(section, slot)]


# ---------------------------------------------------------------- one sitting

def build_sitting(test_dir: Path) -> list[dict]:
    """Reconcile one imported sitting's audio against its text; emit records."""
    sitting = test_dir.name.removeprefix("imported-n2-")
    audio = test_dir / "聴解.mp3"
    script_path = test_dir / "聴解スクリプト.txt"
    kaisetsu_path = test_dir / "詳細解説.json"
    kaisetsu_vi_path = test_dir / "詳細解説.vi.json"
    booklet = test_dir / "聴解.md"

    for required in (audio, script_path, kaisetsu_path, booklet):
        if not required.is_file():
            raise Reconciliation(f"{test_dir.name}: missing {required.name}")

    script_text = script_path.read_text(encoding="utf-8")
    blocks, preamble_text = parse_script_blocks(script_path)
    kaisetsu = json.loads(kaisetsu_path.read_text(encoding="utf-8"))
    kaisetsu_vi = (json.loads(kaisetsu_vi_path.read_text(encoding="utf-8"))
                   if kaisetsu_vi_path.is_file() else {})
    keys = GRADE.parse_choukai_keys(booklet)
    kaisetsu_cells = parse_kaisetsu_cells(booklet)

    # --- the text must describe the shape the segmenter expects, BEFORE the
    #     audio is touched: a script that is short one item would otherwise
    #     silently align every later slot against the wrong span.
    #
    #     The shape is the SITTING's, not a constant: 20 of the 31 archive
    #     sittings are not 5/6/5/11/2 (see this module's docstring). All ten
    #     imports are modern, so `slots_for` returns `EXPECTED_SLOTS` for every
    #     one of them today and this is a no-op — it stops being one the first
    #     time a pre-2021 sitting is banked.
    expected_slots = slots_for(sitting)
    for section, count in expected_slots.items():
        found = sorted(s for (sec, s) in blocks if sec == section)
        if found != list(range(1, count + 1)):
            raise Reconciliation(
                f"{test_dir.name}: {section} script blocks are {found}, "
                f"expected 1..{count}"
            )

    seg = segment(audio, hint_from_script(script_text), expected_slots)

    records: list[dict] = []
    for section, count in expected_slots.items():
        for slot in range(1, count + 1):
            speech_lo, speech_hi = seg.slot_span(section, slot)
            ids = answer_ids(section, slot)

            missing_key = [i for i in ids if i not in keys]
            if missing_key:
                raise Reconciliation(
                    f"{test_dir.name}: no answer key for {', '.join(missing_key)}"
                )
            missing_exp = [i for i in ids if i not in kaisetsu]
            if missing_exp:
                raise Reconciliation(
                    f"{test_dir.name}: 詳細解説.json has no "
                    f"{', '.join(missing_exp)}"
                )

            closing = seg.answers[section][slot - 1]
            exp_block = {i: kaisetsu[i] for i in ids}
            figure = figure_dependent(exp_block)
            records.append({
                "id": f"{sitting}:{section}-{slot}",
                "sitting": sitting,
                "source_test": test_dir.name,
                "kind": "item",
                # Bank v2: the mixed pool carries textbook items too
                # (`build_textbook_bank.py`). An official item speaks its own
                # 「N番。」 and is slot-preserved; a textbook item does not and
                # is slot-free, so the composer must prepend a harvested call.
                "source": "official",
                "needs_number_call": False,
                "section": section,
                "slot": slot,
                # A FIGURE ITEM CANNOT BE COMPOSED (2026-09-09,
                # qa-report-20260909_1 F1). Official 問題1 occasionally prints a
                # picture and asks which REGION of it to act on; its four
                # printed options are then LABELS of that picture — the bare
                # digits 1-4, or the kana 「ア　イ　ウ」 of a 座席図 — and they
                # mean nothing without the image. A composed paper carries no
                # images (`build_booklet.py` renders no figure for a drawn
                # clip), so such an item reaches the learner as
                # 「1. 1 / 2. 2 / 3. 3 / 4. 4」 and is unanswerable — the
                # automatic-fail class `exam-qa-review` calls an unanswerable
                # item. `20260909_1` shipped one (`2022-12:問題1-2`, a poster
                # layout) all the way to a blind solve, which caught it as the
                # single mismatch in 101 items.
                # FOUR of the 375 banked item records are figure items, measured
                # 2026-09-17 after the ア/イ/ウ half of the predicate landed:
                # `2021-12:問題1-5` (seat selection) and `2022-12:問題1-2`
                # (poster) on digits, `2023-12:問題1-2` and `2024-12:問題1-2` on
                # 「ア　イ　ウ」 seat labels — the two the digits-only predicate
                # missed, after three papers had already shipped one
                # (`qa/root-cause-20260917_1.md` RC-2). That is 1.1 % of the
                # pool; the thinnest slot it touches is 問題1 slot 2, which
                # keeps 7 of its 10 official candidates.
                # The record is KEPT and flagged rather than dropped, so the
                # bank stays a faithful inventory of the corpus and the
                # exclusion is countable.
                "figure_dependent": figure,
                "audio": {
                    "start": round(max(0.0, speech_lo - GUARD_S), 3),
                    "end": round(min(seg.duration, speech_hi + GUARD_S), 3),
                    # 問題5-2番 runs to EOF and keeps its own trailing pause and
                    # the closing announcement, so it declares no answer pause.
                    "answer_pause": round(closing.duration, 3),
                },
                "script": blocks[(section, slot)],
                "answers": {i: keys[i] for i in ids},
                "explanation": exp_block,
                "explanation_vi": {i: kaisetsu_vi[i] for i in ids
                                   if i in kaisetsu_vi},
                "kaisetsu_cell": {i: kaisetsu_cells[i] for i in ids
                                  if i in kaisetsu_cells},
            })

    # --- Section preambles: opening announcement (問題1 only) + the 問題N
    #     instruction + 「では、練習しましょう。」 + the 例 + its confirmation +
    #     「では、始めます。」, lifted as ONE clip. Nothing inside is cut, so the
    #     例 stays coherent and no announcer line is spliced mid-sentence.
    ordered = list(expected_slots)
    for i, section in enumerate(ordered):
        lo = 0.0 if i == 0 else seg.answers[ordered[i - 1]][-1].end
        hi = seg.preamble_end[section].start
        if hi <= lo:
            raise Reconciliation(
                f"{test_dir.name}: {section} preamble is empty "
                f"({lo:.1f}s -> {hi:.1f}s)"
            )
        records.append({
            "id": f"{sitting}:{section}-preamble",
            "sitting": sitting,
            "source_test": test_dir.name,
            "kind": "preamble",
            "source": "official",
            "section": section,
            "slot": 0,
            "audio": {"start": round(max(0.0, lo - GUARD_S), 3),
                      "end": round(hi + GUARD_S, 3)},
            # [after_item_index, block] — 0 means "before the first item"
            "text": preamble_text.get(section, []),
            # 問題5 needs a lead-in block before EACH of its two items. One
            # import (2022-07) transcribes only 1番's, so its 問題5 preamble
            # cannot supply 2番's and the composer must not draw it — the two
            # halves come from different sittings, so a gap here is silent.
            "complete": (section != "問題5"
                         or any(pos == 1
                                for pos, _t in preamble_text.get(section, []))),
            "opening": [t for _pos, t in preamble_text["opening"]] if i == 0 else [],
        })

    return records


# ---------------------------------------------------------------- CLI

def figure_dependent(explanation: dict) -> bool:
    """Do this item's printed options only make sense beside a picture?

    An official 問題1 item occasionally prints a figure and asks which part of
    it to act on; its four printed options are then LABELS of that image —
    either the bare digits 1-4 or the kana 「ア　イ　ウ」 a 座席図 indexes — and
    they carry no meaning on their own. The imported sitting embeds the picture
    (`tests/imported-*/聴解.md` carries it as a base64 block); a COMPOSED paper
    has no figure to embed, so the item reaches the learner as
    「1. 1 / 2. 2 / 3. 3 / 4. 4」 or 「1. ア　イ　ウ / 2. ア　イ　エ / …」.

    Detected from the printed options rather than from the stem's wording,
    because the stem phrasings vary (「ポスターのどこを直しますか」,
    「どの席にしますか」) while the label-only option set is the invariant that
    actually makes the item unrenderable.

    **The predicate itself lives in `build_textbook_bank.figure_dependent`, and
    it is imported, not copied.** Until 2026-09-17 each builder carried its own
    copy that recognised digits only, so every ア/イ/ウ diagram item was banked
    as drawable and three papers shipped one
    (`qa/root-cause-20260917_1.md` RC-2). This function is now only the shape
    adapter: the official half stores its options inside a `詳細解説` block, one
    entry per scored answer id, and an item is figure-dependent if ANY of them
    is a label-only set.
    """
    for entry in (explanation or {}).values():
        if figure_dependent_options((entry or {}).get("options")):
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="reconcile every sitting but write nothing")
    ap.add_argument("--only", action="append", default=None,
                    help="limit to one test dir name (repeatable)")
    args = ap.parse_args(argv)

    dirs = sorted((ROOT / "tests").glob("imported-n2-*"))
    if args.only:
        dirs = [d for d in dirs if d.name in set(args.only)]
    if not dirs:
        print("no imported sittings found under tests/", file=sys.stderr)
        return 1

    all_records: list[dict] = []
    failures = 0
    for test_dir in dirs:
        try:
            records = build_sitting(test_dir)
        except (Reconciliation, NotSegmented) as exc:
            print(f"FAIL  {exc}")
            failures += 1
            continue
        items = [r for r in records if r["kind"] == "item"]
        scored = sum(len(r["answers"]) for r in items)
        print(f"ok    {test_dir.name:<24} {len(items)} items, "
              f"{scored} scored answers, {len(records) - len(items)} glue clips")
        all_records.extend(records)

    if failures:
        print(f"\n{failures} sitting(s) did not reconcile — bank not written")
        return 1

    # --- the textbook half. One writer for one file: a bank half-written by
    #     two scripts could leave official records fresh beside textbook records
    #     from a previous data file, and `bank_version` would not say so.
    textbook, refusals = build_textbook_records()
    for line in refusals:
        print(f"REFUSED  {line}")
    if refusals:
        print(f"\n{len(refusals)} textbook item(s) refused — bank not written. "
              f"A refusal is the guard against a mis-read CD track number "
              f"(build_textbook_bank.py §'The guard'); fix the declaration in "
              f".agents/choukai-audio/references/textbook_items.json or move "
              f"the item to its `excluded` list with a measured reason.")
        return 1
    from collections import Counter as _Counter
    shape = _Counter((r["source"], r["section"]) for r in textbook)
    print(f"ok    textbook items          {len(textbook)} items — "
          + ", ".join(f"{b}/{s} ×{n}" for (b, s), n in sorted(shape.items())))
    all_records.extend(textbook)

    # --- the ARCHIVE half: hand-declared items cut from the 21 un-imported
    #     sittings of `refs/JLPT_N2_NEW/` (route C,
    #     `.agents/choukai-audio/references/archive_bank_expansion.md`). Same
    #     contract as the textbook half — report-only builder, a refusal blocks
    #     the write — and still one writer for one file.
    archive, arch_refusals = build_archive_records()
    for line in arch_refusals:
        print(f"REFUSED  {line}")
    if arch_refusals:
        print(f"\n{len(arch_refusals)} archive item(s) refused — bank not "
              f"written. Each refusal names the acceptance check it failed "
              f"(archive_bank_expansion.md §7); fix the declaration in "
              f".agents/choukai-audio/references/archive_items.json or move "
              f"the item to its `excluded` list with a measured reason.")
        return 1
    if archive:
        ashape = _Counter((r["sitting"], r["section"]) for r in archive)
        print(f"ok    archive items           {len(archive)} items — "
              + ", ".join(f"{s}/{sec} ×{n}"
                          for (s, sec), n in sorted(ashape.items())))
        all_records.extend(archive)

    if args.check:
        print(f"\n--check: {len(all_records)} records reconciled, nothing written")
        return 0

    BANK_PATH.parent.mkdir(parents=True, exist_ok=True)
    BANK_PATH.write_text(json.dumps({
        "version": BANK_VERSION,
        "guard_s": GUARD_S,
        "sittings": [d.name for d in dirs],
        "records": all_records,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nwrote {BANK_PATH.relative_to(ROOT)} — {len(all_records)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
