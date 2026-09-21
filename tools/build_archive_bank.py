#!/usr/bin/env python3
"""Bank hand-declared 聴解 items cut from the 21 UN-IMPORTED archive sittings.

`build_choukai_bank.py` owns the official half of `logs/choukai_bank.json` — 290
items cut out of the ten `tests/imported-n2-*` sittings — and
`build_textbook_bank.py` owns the slot-free half. This owns a THIRD half: one
record per item declared in
`.agents/choukai-audio/references/archive_items.json`, resolved straight against
`refs/JLPT_N2_NEW/`, measured, guarded, and handed back for
`build_choukai_bank.main()` to append. One writer for one file, as before.

This is route C of `.agents/choukai-audio/references/archive_bank_expansion.md`
§0. Read that file before declaring anything; §6 Step 2/3 is what this module
implements, §7 is the acceptance bar every declaration has to clear, and §9 is
the exclusion list.

The archive is THREE sources in one folder, and only one of them is bad
-----------------------------------------------------------------------
| what                      | file         | trust                  |
|---------------------------|--------------|------------------------|
| the recording             | `*.mp3`      | exact                  |
| the key                   | `key.md` / `answer_keys.json` | **exact** |
| the printed 問題1/2 options | `booklet.md` | **exact** (text layer) |
| the dialogue              | `script.md`  | **OCR, ~97 %**         |

So the key and the option lists come for free and are RE-CHECKED here
mechanically (guards 1 and 2 below), while every line of learner-visible
Japanese is hand-declared and image-verified. `script.md` must never be pasted
into a declaration unchecked: measured at ~7 wrong characters per item, and
**44 of its 316 spoken-option blocks (13.9 %) are not in ascending digit order**
because the script PDF lays them in two columns and the OCR reads them visually
(`archive_bank_expansion.md` §3.2, §3.4). Every bank text field is printed to a
learner (§3.1) — there is no internal-only text field.

Slot-preserving, and therefore NOT slot-free
--------------------------------------------
An archive clip speaks its own 「N番。」, exactly like an imported official one,
so it is banked WITH its number call, `needs_number_call: False`, locked to the
slot it occupied. `target_slot != slot` — the pre-2020 問題5 2番/3番, which would
have to be re-cut and given a harvested call — is refused here and deferred to
§6 Step 3's second sub-case.

`source` vs `provenance`, and why both exist
--------------------------------------------
These are the same JEES recordings as the imported half, so `source` stays
`"official"`: tagging them anything else makes `check_choukai_source_mix()`'s
`set(sources) <= {"official"}` test stop meaning what it says and FAILs the
control paper. They are nevertheless a different POOL, and the control paper
`20260807_1` must keep drawing only from the ten hand-verified imports, so every
record also carries `provenance: "archive"` (the imported half is `"imported"`
by absence). **`compose_choukai.draw()` does not yet read it** — that filter is
`archive_bank_expansion.md` §6 Step 5 and it is a prerequisite for composing
ANY paper once archive records are in the bank. Until it lands, banking is safe
(no draw has happened) and composing is not.

No preambles (§6 Step 4)
------------------------
`build_choukai_bank.build_sitting()` emits one preamble clip per section whose
`text` is lifted from an import's `聴解スクリプト.txt`. The archive has no such
text — all 31 `script.md` begin at 問題1, because the script PDFs print neither
the opening announcement nor the 問題N instructions — and the pre-2020 問題5
preamble has a different internal structure besides. The bank already holds 50
preambles from 10 sittings, which is ample. **Archive records are items only.**
Do not try.

Usage
-----
    python3 tools/build_archive_bank.py                 # measure and report
    python3 tools/build_archive_bank.py --json          # print the records
    python3 tools/build_archive_bank.py --scout 2014-12 # structural pause map
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from build_textbook_bank import (  # noqa: E402
    CHAR_RATE_OFFICIAL, EXPECTED_OPTIONS, PRINTED_OPTION_SECTIONS,
    SPOKEN_CHOICE_RE, TYPE_BANDS, Refused, figure_dependent, speech_runs,
    spoken_shape, window_span)
from choukai_segment import (  # noqa: E402
    ANSWER_SPLIT, OPTION_READING, expected_gaps, find_pauses, measure,
    slots_for)

ITEMS_PATH = (ROOT / ".agents" / "choukai-audio" / "references"
              / "archive_items.json")
ARCHIVE_DIR = ROOT / "refs" / "JLPT_N2_NEW"
ANSWER_KEYS = ARCHIVE_DIR / "answer_keys.json"

# The ten sittings the official half already banks from `tests/imported-n2-*`.
# An archive declaration for one of these would double-bank the same recording
# under two ids, so it is refused.
IMPORTED_SITTINGS = frozenset(
    d.name.removeprefix("imported-n2-")
    for d in (ROOT / "tests").glob("imported-n2-*"))

# Same guard margin `build_choukai_bank.GUARD_S` uses: keep the cut this far
# inside the surrounding structural silence so a soft breath or a speech tail
# the envelope read as quiet is never clipped. The composer lays its own
# canonical answer pause after the clip, so trimmed silence is not lost.
GUARD_S = 0.25

# --- §7 check 11: loudness ---------------------------------------------------
#
# `build_audio` runs ONE `loudnorm` pass over the CONCATENATED file, so relative
# level differences between source clips survive into the paper and a listener
# hears the recording change mid-sitting (`archive_bank_expansion.md` §8.4).
#
# MEASURED 2026-09-17 with `choukai_segment.measure` (integrated LUFS, gated
# K-weighted) over all 31 archive MP3s — NOT `volumedetect`'s `mean_volume`,
# which runs ~4 dB low and is what §8.4/§9's original table was built from
# (`choukai-audio` Part 4 step 1: "Never `volumedetect`"). The two orderings do
# not agree, which is why the hold list below is re-derived rather than copied.
#
#   31-sitting median   -18.06 LUFS        band = median +/- 3.0 dB
#   the ten imports     -20.28 .. -15.55   (every one inside the band)
#   outside the band    2015-07 -13.49, 2019-07 -21.27, 2019-12 -21.40
#
# Those three are exactly the three `archive_bank_expansion.md` §9 names as
# loudness holds — arrived at from a different measurement, which is the
# corroboration worth having. (§9's own figures, -15.3/-22.9/-23.3 dB, are
# `mean_volume` readings copied out of `audio_inspection.md`; they rank the
# same three at the extremes but they are not LUFS.)
#
# A sitting outside the band is HELD (not "excluded" — nothing is wrong with the
# item), until §8.4's per-clip gain at cut time exists, which is a composer
# change and is not in this cut.
ARCHIVE_LUFS_BAND = (-21.06, -15.06)

# --- §9 exclusions that are structural, not per-item -------------------------
# 32 kHz MP3s, against 44.1/48 kHz everywhere else — an audible bandwidth step
# after the composer's resample. Measured from `ffprobe`; held until someone
# listens and records that the step is inaudible.
HELD_SAMPLE_RATE_SITTINGS = frozenset({"2010-12", "2016-07"})

# The composer draws 問題4 slots 1..11 only and `harvest_number_calls.py` has no
# 「12番。」, so a 12番 from one of the 13 sittings that ran twelve is dead weight.
MAX_SLOT = {"問題1": 5, "問題2": 6, "問題3": 5, "問題4": 11, "問題5": 2}

# A `source_page` has to say the lines were read off a rendered page, not off
# `script.md`. §7 check 9 is the expensive check and the point of route C, so
# the declaration is required to carry its evidence.
VERIFIED_RE = re.compile(r"image-verified\s+\d{4}-\d{2}-\d{2}")

RUBY_RE = re.compile(r"《[^》]*》")
ITEM_MARKER_RE = re.compile(r"^(\d+)番。")
# The digit that OPENS a spoken option line, in either width.
OPTION_DIGIT_RE = re.compile(r"^\s*([1-4１-４])\s*[、.．。]")


def _bare(text: str) -> str:
    """NFKC, ruby-stripped, whitespace-free — the form two witnesses compare in."""
    text = RUBY_RE.sub("", text or "")
    text = unicodedata.normalize("NFKC", text)
    return re.sub(r"[\s　]", "", text)


# ---------------------------------------------------------------- the archive

@lru_cache(maxsize=1)
def archive_index() -> dict[str, dict]:
    """{'2014-12': {'folder': …, 'answers': {('問題3', 2): 3, …}}} for all 31."""
    try:
        exams = json.loads(ANSWER_KEYS.read_text(encoding="utf-8"))["exams"]
    except (OSError, ValueError, KeyError) as exc:       # pragma: no cover
        raise Refused(
            f"cannot read {ANSWER_KEYS.relative_to(ROOT)} — it is tracked in "
            f"git (AGENTS.md §3), so this is a broken checkout: {exc}")
    out: dict[str, dict] = {}
    for folder, exam in exams.items():
        answers: dict[tuple[str, int], int] = {}
        for entry in exam.get("items", []):
            if entry.get("part") != "聴解" and entry.get("section") != "聴解":
                continue
            answers[(f"問題{entry['mondai']}", int(entry["no"]))] = int(
                entry["answer"])
        out[f"{exam['year']}-{exam['month']:02d}"] = {
            "folder": exam.get("folder", folder), "answers": answers}
    return out


def sitting_dir(sitting: str) -> Path:
    index = archive_index()
    if sitting not in index:
        raise Refused(
            f"{sitting}: no such sitting in "
            f"{ANSWER_KEYS.relative_to(ROOT)} (have "
            f"{len(index)}: {min(index)} … {max(index)})")
    return ARCHIVE_DIR / index[sitting]["folder"]


def sitting_audio(sitting: str) -> Path:
    folder = sitting_dir(sitting)
    mp3 = sorted(p for p in folder.glob("*.mp3")) if folder.is_dir() else []
    if not mp3:
        raise Refused(
            f"{sitting}: no MP3 under {folder.relative_to(ROOT)}. The archive "
            f"is a release asset, not a git object (AGENTS.md §3) — restore "
            f"with:\n  gh release download refs --pattern 'JLPT_N2_NEW.zip' "
            f"--dir /tmp && unzip -n /tmp/JLPT_N2_NEW.zip -d refs/")
    return mp3[0]


@lru_cache(maxsize=64)
def sitting_lufs(sitting: str) -> float:
    """Integrated LUFS of one sitting's recording (§7 check 11)."""
    _env, lufs = measure(sitting_audio(sitting))
    return float(lufs)


@lru_cache(maxsize=64)
def booklet_text(sitting: str) -> str:
    """That sitting's `booklet.md`, bare — the EXACT printed-option witness."""
    path = sitting_dir(sitting) / "booklet.md"
    if not path.is_file():
        raise Refused(
            f"{sitting}: no booklet.md — `*.md` extracts are TRACKED "
            f"(AGENTS.md §3), so a missing one is a defect, not a missing "
            f"binary. Re-run `make extract-archive`")
    return _bare(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- text shaping

def derive_text(spec: dict) -> tuple[str, str, list[str], str]:
    """(script, stem, options, explanation script) from a declaration.

    The archive half is banked in the OFFICIAL record's shape, not the textbook
    one, because it IS an official record in every way that matters downstream
    (`compose_choukai.resolve()` reads `script`/`answers`/`explanation` straight
    off it). So:

    * top-level `script` — every declared line, 「N番。」 included;
    * `explanation[…]["script"]` — the same minus the 「N番。」 marker and minus
      the spoken 「N、…」 choice lines, which is what the ten imports store;
    * `explanation[…]["stem"]` — situation line + the question read after the
      talk, concatenated, which is `derive_text`'s own non-printed shape in
      `build_textbook_bank`.

    **§7 check 6 lives here**: the spoken options are keyed by their OWN digit
    and the digits must read 1..N ascending after that. 14 % of the archive's
    OCR'd option blocks are in visual order, not digit order, and a parser that
    harvests them in file order silently re-keys the item
    (`archive_bank_expansion.md` §3.4 / §8.2).
    """
    section = spec["section"]
    slot = int(spec["slot"])
    lines = list(spec["script_lines"])
    if not lines:
        raise Refused(f"{spec['id']}: no script_lines")

    marker = ITEM_MARKER_RE.match(lines[0])
    if not marker:
        raise Refused(
            f"{spec['id']}: script_lines[0] must open with 「{slot}番。」 — an "
            f"archive clip speaks its own number call and is banked with it")
    if int(marker.group(1)) != slot:
        raise Refused(
            f"{spec['id']}: script_lines[0] says 「{marker.group(1)}番。」 but "
            f"the declaration is slot {slot}")

    digits: list[int] = []
    options: list[str] = []
    plain: list[str] = []
    for line in lines:
        hit = OPTION_DIGIT_RE.match(unicodedata.normalize("NFKC", line))
        if hit:
            if not SPOKEN_CHOICE_RE.match(line):
                raise Refused(
                    f"{spec['id']}: spoken option 「{line[:14]}…」 must be "
                    f"written 「N、…」 with a 読点 — the parsers key on "
                    f"`^[1-4]、` (choukai-audio Part 1 block conventions)")
            digits.append(int(unicodedata.normalize("NFKC", line)[0]))
            options.append(SPOKEN_CHOICE_RE.match(line).group(2).strip())
        else:
            plain.append(line)

    printed = section in PRINTED_OPTION_SECTIONS
    if printed:
        if digits:
            raise Refused(
                f"{spec['id']}: {section} PRINTS its options, so script_lines "
                f"must carry no 「N、…」 line — found {len(digits)}. Move them "
                f"to printed_options; left in the script they are counted as "
                f"spoken characters and the CHAR_RATE guard refuses the item")
        options = [str(o) for o in (spec.get("printed_options") or [])]
        if not options:
            raise Refused(
                f"{spec['id']}: {section} PRINTS its options and none are "
                f"declared — add a `printed_options` array copied from that "
                f"sitting's booklet.md")
    else:
        if spec.get("printed_options"):
            raise Refused(
                f"{spec['id']}: {section} SPEAKS its options, so they belong "
                f"in script_lines as 「N、…」 lines, not in printed_options")
        if digits != list(range(1, len(digits) + 1)):
            raise Refused(
                f"{spec['id']}: spoken option digits read {digits}, not "
                f"1..{len(digits)} ascending. 44 of the archive's 316 spoken "
                f"option blocks are laid in two columns and OCR reads them in "
                f"VISUAL order (archive_bank_expansion.md §3.4) — re-sort the "
                f"declaration by each line's own digit and re-read the page; a "
                f"block taken in file order silently re-keys the item")

    # lines[0] carries the marker and is never a choice line, so it is plain[0].
    body = lines[0][marker.end():]
    tail = plain[1:]
    stem = body
    if tail and not re.match(r"^[^:：]{1,6}[:：]", tail[-1]):
        stem += tail[-1]

    script = "\n".join(lines)
    exp_script = "\n".join([body] + tail)
    return script, stem, options, exp_script


# ---------------------------------------------------------------- one item

def build_one(spec: dict) -> dict:
    """Measure and validate one declared archive item; return its bank record."""
    item_id = spec.get("id", "<no id>")
    section = spec["section"]
    slot = int(spec["slot"])
    sitting = spec["sitting"]

    if section not in TYPE_BANDS:
        raise Refused(f"{item_id}: unknown section {section!r}")
    if sitting in IMPORTED_SITTINGS:
        raise Refused(
            f"{item_id}: {sitting} is already imported as "
            f"tests/imported-n2-{sitting} and banked by build_choukai_bank.py "
            f"— declaring it here would bank the same recording twice")

    # --- §6 Step 3: first cut takes slot-preserving items only.
    target = int(spec.get("target_slot", slot))
    if target != slot:
        raise Refused(
            f"{item_id}: target_slot {target} != slot {slot}. The clip speaks "
            f"「{slot}番。」, so placing it elsewhere needs a number-call re-cut "
            f"— archive_bank_expansion.md §6 Step 3's second sub-case, "
            f"deliberately deferred")

    # --- §9: slots the composer cannot place, and shapes that do not exist.
    shape = slots_for(sitting)
    if section not in shape:
        raise Refused(f"{item_id}: {sitting} has no {section}")
    if not 1 <= slot <= shape[section]:
        raise Refused(
            f"{item_id}: {sitting} runs {shape[section]} {section} item(s), "
            f"so it has no {slot}番 (answer_keys.json)")
    if slot > MAX_SLOT[section]:
        raise Refused(
            f"{item_id}: compose_choukai.SECTIONS caps {section} at "
            f"{MAX_SLOT[section]} slot(s) and logs/choukai_number_calls.json "
            f"harvests 1番–11番 only — a {slot}番 has no slot and no number "
            f"call (archive_bank_expansion.md §9)")

    # --- §7 check 1: the key is exact and free. Nothing may override it.
    index = archive_index()
    official_key = index[sitting]["answers"].get((section, slot))
    if official_key is None:
        raise Refused(
            f"{item_id}: answer_keys.json has no key for {sitting} "
            f"{section}-{slot}番")
    if int(spec["answer"]) != official_key:
        raise Refused(
            f"{item_id}: declared answer {spec['answer']} but "
            f"answer_keys.json says {official_key} for {sitting} {section}-"
            f"{slot}番 — the key file is EXACT (colour-parsed and cross-checked "
            f"365/365 against the script PDFs' （正解:N）), so the declaration "
            f"is what is wrong")

    # --- §7 check 9: the transcript has to carry its verification evidence.
    source_page = spec.get("source_page", "")
    if not VERIFIED_RE.search(source_page):
        raise Refused(
            f"{item_id}: source_page must record the image verification — "
            f"「… (image-verified YYYY-MM-DD)」. `script.md` is OCR at ~7 wrong "
            f"characters per item and every bank text field is printed to a "
            f"learner (archive_bank_expansion.md §3). Render the page with "
            f"`pdftoppm -r 300` and read it")

    # --- §7 check 11 + §9: loudness and bandwidth holds.
    if sitting in HELD_SAMPLE_RATE_SITTINGS:
        raise Refused(
            f"{item_id}: {sitting}'s MP3 is 32 kHz against 44.1/48 kHz "
            f"everywhere else — an audible bandwidth step after the composer's "
            f"resample. HELD (archive_bank_expansion.md §9); admit only after "
            f"someone listens and records that the step is inaudible")
    lufs = sitting_lufs(sitting)
    lo, hi = ARCHIVE_LUFS_BAND
    if not lo <= lufs <= hi:
        raise Refused(
            f"{item_id}: {sitting} measures {lufs:.2f} LUFS, outside the "
            f"{lo:.1f}–{hi:.1f} band (31-sitting median ±3 dB). `build_audio` "
            f"runs ONE loudnorm pass over the concatenated paper, so the step "
            f"is audible mid-sitting (archive_bank_expansion.md §8.4). HELD "
            f"until §8.4's per-clip gain at cut time exists")

    audio = sitting_audio(sitting)

    # --- §7 checks 3/4/5: the span is MEASURED inside the declared bracket.
    #     `window_span` is imported, never re-implemented: it already refuses a
    #     window edge that falls inside speech, which is the failure a second
    #     windowing implementation would reintroduce.
    if "window" not in spec:
        raise Refused(
            f"{item_id}: archive items resolve by `window` — a bracket between "
            f"the structural silences either side of the item. Find one with "
            f"`python3 tools/build_archive_bank.py --scout {sitting}`")
    start, end, answer_pause, _h, _t = window_span(audio, spec["window"])
    span = end - start

    band = TYPE_BANDS[section]
    if not band[0] <= span <= band[1]:
        raise Refused(
            f"{item_id}: body span {span:.1f}s ({start:.1f}–{end:.1f}s) is "
            f"outside {section}'s {band[0]:.0f}–{band[1]:.0f}s band — the "
            f"window is probably bracketing the wrong item. Re-scout "
            f"{sitting}")

    chars, lines_n, choices = spoken_shape(spec["script_lines"])
    gaps = expected_gaps(section, slot, lines_n, choices)
    rate = (span - gaps) / max(chars, 1)
    if not CHAR_RATE_OFFICIAL[0] <= rate <= CHAR_RATE_OFFICIAL[1]:
        raise Refused(
            f"{item_id}: {span:.1f}s of audio against {chars} transcribed "
            f"characters implies {rate:.3f} s/char, outside "
            f"{CHAR_RATE_OFFICIAL[0]}–{CHAR_RATE_OFFICIAL[1]} — this clip is "
            f"the right length for a {section} item but does not say what the "
            f"transcript says. Re-check {source_page}")

    # --- §7 check 8: a 問題2 clip must CONTAIN its ~20 s option-reading pause.
    if section == "問題2":
        env, file_lufs = measure(audio)
        inside = [p for p in find_pauses(env, file_lufs)
                  if start < p.start and p.end < end
                  and OPTION_READING[0] <= p.duration <= OPTION_READING[1]]
        if not inside:
            raise Refused(
                f"{item_id}: no {OPTION_READING[0]:.0f}–"
                f"{OPTION_READING[1]:.0f}s option-reading pause inside "
                f"{start:.1f}–{end:.1f}s. A 問題2 item's 20 s pause sits INSIDE "
                f"the clip and the composer never re-times it (choukai-audio "
                f"Part 0 rule 3) — the window was cut from the pause's end")

    script, stem, options, exp_script = derive_text(spec)

    want_options = EXPECTED_OPTIONS[section]
    if len(options) != want_options:
        source = ("printed_options" if section in PRINTED_OPTION_SECTIONS
                  else "spoken choice line(s)")
        raise Refused(f"{item_id}: {len(options)} {source}, {section} takes "
                      f"{want_options}")
    if len(set(options)) != len(options):
        raise Refused(f"{item_id}: two options are identical")
    if not 1 <= official_key <= want_options:
        raise Refused(
            f"{item_id}: key {official_key} is outside 1–{want_options}")

    # --- §7 check 2: every printed option has to be verbatim in booklet.md.
    #     Free, exact, and the mechanical half of the 「演技力」 second-witness
    #     rule (archive_bank_expansion.md §3.3).
    if section in PRINTED_OPTION_SECTIONS:
        flat = booklet_text(sitting)
        missing = [o for o in options if _bare(o) not in flat]
        if missing:
            raise Refused(
                f"{item_id}: printed option(s) not found verbatim in "
                f"{sitting}'s booklet.md: "
                + "; ".join(f"「{o}」" for o in missing)
                + " — booklet.md is an EXACT text layer on all 31 sittings, so "
                  "a miss is a hand-typing slip in the declaration")

    # --- §7 check 7: a picture-legend item cannot be composed.
    if figure_dependent(options):
        raise Refused(
            f"{item_id}: the option set is picture labels "
            f"({', '.join(options)}) — a composed booklet embeds no figure, so "
            f"the item reaches the learner unanswerable "
            f"(build_textbook_bank.figure_dependent; "
            f"qa/root-cause-20260917_1.md RC-2)")

    # --- the declaration's own second witness, when it supplies one. `stem`
    #     and `options` carry hand-applied furigana in an official record, and
    #     the derived forms do not — so a furigana'd copy is accepted only when
    #     it is character-identical to the derived one once ruby is stripped.
    key = f"問{section[-1]}-{slot}"
    payload = dict(spec.get("explanation") or {})
    for field, derived in (("stem", stem), ("options", options)):
        given = payload.get(field)
        if given is None:
            payload[field] = derived
            continue
        if field == "options":
            if ([_bare(o) for o in given] != [_bare(o) for o in derived]):
                raise Refused(
                    f"{item_id}: explanation.options disagree with the spoken "
                    f"option lines once furigana is stripped — the two are one "
                    f"transcription and must not drift")
        elif _bare(given) != _bare(derived):
            raise Refused(
                f"{item_id}: explanation.stem disagrees with the script's "
                f"situation + question lines once furigana is stripped")
    payload["script"] = exp_script

    vi = dict(spec.get("explanation_vi") or {})
    if len(vi.get("options_analysis") or []) != len(options):
        raise Refused(
            f"{item_id}: the Vietnamese pane analyses "
            f"{len(vi.get('options_analysis') or [])} options, not "
            f"{len(options)}")
    if len(payload.get("options_analysis") or []) != len(options):
        raise Refused(
            f"{item_id}: the Japanese pane analyses "
            f"{len(payload.get('options_analysis') or [])} options, not "
            f"{len(options)}")

    return {
        "id": item_id,
        "sitting": sitting,
        # No `source_test`: there is no tests/ folder behind an archive record.
        "source": "official",
        # …and this is how the control paper stays official-ONLY. See the module
        # docstring; `compose_choukai.draw()` has to read it before any paper is
        # composed against a bank carrying archive records.
        "provenance": "archive",
        "source_page": source_page,
        "kind": "item",
        "section": section,
        "slot": slot,
        "needs_number_call": False,
        "figure_dependent": False,     # refused above, never banked as True
        "audio": {
            "path": str(audio.relative_to(ROOT)),
            "start": round(max(0.0, start - GUARD_S), 3),
            "end": round(end + GUARD_S, 3),
            "answer_pause": round(answer_pause, 3),
        },
        "script": script,
        "answers": {key: official_key},
        "explanation": {key: payload},
        "explanation_vi": {key: vi},
        "kaisetsu_cell": {key: spec.get("kaisetsu_cell", "")},
        "measured": {"span": round(span, 3), "chars": chars, "lines": lines_n,
                     "rate": round(rate, 4), "lufs": round(lufs, 2)},
    }


def build_records(verbose: bool = False) -> tuple[list[dict], list[str]]:
    """(records, refusals) over every archive item the data file declares."""
    if not ITEMS_PATH.is_file():
        return [], []
    data = json.loads(ITEMS_PATH.read_text(encoding="utf-8"))
    records, refusals = [], []
    seen: set[str] = set()
    for spec in data.get("items", []):
        item_id = spec.get("id", "<no id>")
        if item_id in seen:
            refusals.append(f"{item_id}: declared twice")
            continue
        seen.add(item_id)
        try:
            record = build_one(spec)
        except Refused as exc:
            refusals.append(str(exc))
            continue
        records.append(record)
        if verbose:
            m = record["measured"]
            print(f"ok    {record['id']:<26} {record['section']}-"
                  f"{record['slot']}  {m['span']:6.1f}s  {m['chars']:4d} chars"
                  f"  {m['rate']:.3f} s/char  {m['lufs']:7.2f} LUFS  key "
                  f"{list(record['answers'].values())[0]}")
    return records, refusals


# ---------------------------------------------------------------- scouting

def scout(sitting: str) -> int:
    """Print the structural pause map of one sitting, to bracket its items.

    A declaration names a WINDOW between two structural silences. This is how
    you find them without guessing: every pause of `ANSWER_SPLIT`s or more, in
    order, with the speech run that follows it. An item's window is
    `[previous answer pause's middle, this answer pause's middle]`.
    """
    audio = sitting_audio(sitting)
    env, lufs = measure(audio)
    pauses = find_pauses(env, lufs)
    runs, duration = speech_runs(audio)
    print(f"{sitting}  {audio.relative_to(ROOT)}")
    print(f"  {duration / 60:.1f} min   {lufs:.2f} LUFS   "
          f"shape {slots_for(sitting)}")
    print(f"  {'#':>3}  {'start':>9}  {'end':>9}  {'dur':>6}   next speech")
    for i, p in enumerate(pauses, 1):
        if p.duration < ANSWER_SPLIT:
            continue
        nxt = next((r[0] for r in runs if r[0] >= p.end - 0.01), duration)
        print(f"  {i:>3}  {p.start:9.2f}  {p.end:9.2f}  {p.duration:6.2f}   "
              f"{nxt:9.2f}")
    return 0


# ---------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true",
                    help="print the records instead of the report")
    ap.add_argument("--scout", metavar="SITTING",
                    help="print one sitting's structural pause map (YYYY-MM)")
    args = ap.parse_args(argv)

    if args.scout:
        try:
            return scout(args.scout)
        except Refused as exc:
            print(f"REFUSED  {exc}")
            return 1

    records, refusals = build_records(verbose=not args.json)
    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=1))
        return 1 if refusals else 0

    from collections import Counter
    by_section = Counter(f"{r['section']}" for r in records)
    by_sitting = Counter(r["sitting"] for r in records)
    print(f"\n{len(records)} archive item(s): "
          + (", ".join(f"{k} {v}" for k, v in sorted(by_section.items()))
             or "none")
          + "  |  " + (", ".join(f"{k} ×{v}" for k, v in sorted(by_sitting.items()))
                       or "no sittings"))
    for line in refusals:
        print(f"REFUSED  {line}")
    return 1 if refusals else 0


if __name__ == "__main__":
    raise SystemExit(main())
