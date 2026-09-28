#!/usr/bin/env python3
"""聴解 script grammar and the measured pacing constants — no synthesis.

`聴解スクリプト.txt` is WRITTEN by `tools/compose_choukai.py`; this module is
the one copy of how that file is parsed (item/speaker regexes, the 大問 item
counts, `validate_script`), of the speaker-label → gender/pitch map the gate and
`tools/choukai_profile.py` resolve labels through, and of the pacing values
measured across the 31 official sittings (`references/official_pacing.md`),
which `make check` diffs against the SKILL's pacing table.
Edge-TTS synthesis was retired 2026-09-08 (choukai-audio Part 0); its
generator `make_choukai_mp3.py` was deleted and only this grammar kept.
"""

import re

FEMALE = "ja-JP-NanamiNeural"
MALE = "ja-JP-KeitaNeural"

# Speaker label → voice (gender) and pitch offset. Retained from the TTS cast
# because it is the GENDER contract: `make check` resolves every
# 「〜の男の人」/「〜の女の人」 narration through it, and `choukai_profile.py`
# derives voice balance and same-gender pitch margins (Part 2's 1.9 st target)
# from `voice` and `pitch`. `label in SPEAKER_MAP` is also how the register
# gates recognise a speaker turn at all — an unmapped label is read as
# narration, so 女1/女2 were added (2026-09-09, a 問題例集 mother/daughter item)
# rather than left invisible. ONE naming scheme for a gendered role:
# 男性/女性 + role (a parallel `職員2` set was removed unused, 2026-08-21).
SPEAKER_MAP = {
    "男":     {"voice": MALE,   "rate": "+0%", "pitch": "+0Hz"},
    "男1":    {"voice": MALE,   "rate": "+4%", "pitch": "+18Hz"},
    "男2":    {"voice": MALE,   "rate": "-8%", "pitch": "-16Hz"},
    "夫":     {"voice": MALE,   "rate": "+0%", "pitch": "-12Hz"},
    "学生":   {"voice": MALE,   "rate": "+6%", "pitch": "+14Hz"},
    "部長":   {"voice": MALE,   "rate": "-6%", "pitch": "-18Hz"},
    "店長":   {"voice": MALE,   "rate": "+0%", "pitch": "+10Hz"},
    "女":     {"voice": FEMALE, "rate": "+4%", "pitch": "+0Hz"},
    # ±20 Hz on the 210 Hz female base is 3.3 st apart, over Part 2's 1.9 st.
    "女1":    {"voice": FEMALE, "rate": "+4%", "pitch": "+20Hz"},
    "女2":    {"voice": FEMALE, "rate": "+4%", "pitch": "-20Hz"},
    "妻":     {"voice": FEMALE, "rate": "+4%", "pitch": "+16Hz"},
    "店員":   {"voice": FEMALE, "rate": "+6%", "pitch": "+22Hz"},
    "先生":   {"voice": FEMALE, "rate": "+0%", "pitch": "-16Hz"},
    "医者":   {"voice": FEMALE, "rate": "+0%", "pitch": "-10Hz"},
    "専門家": {"voice": FEMALE, "rate": "+0%", "pitch": "-22Hz"},
    "レポーター": {"voice": FEMALE, "rate": "+6%", "pitch": "+25Hz"},
    "教室の人":   {"voice": FEMALE, "rate": "+0%", "pitch": "+12Hz"},
    # Gender chosen to contrast with the other speaker the item's narration names.
    "職員":   {"voice": FEMALE, "rate": "+0%", "pitch": "-14Hz"},   # vs 学生 (male)
    "係員":   {"voice": FEMALE, "rate": "+6%", "pitch": "+18Hz"},   # vs 男の人
    "担当者": {"voice": FEMALE, "rate": "+0%", "pitch": "-20Hz"},
    "講師":   {"voice": FEMALE, "rate": "+0%", "pitch": "-25Hz"},
    "アナウンス":   {"voice": FEMALE, "rate": "+0%", "pitch": "+8Hz"},
    "アナウンサー": {"voice": FEMALE, "rate": "+4%", "pitch": "+20Hz"},
    "教授":   {"voice": MALE,   "rate": "-6%", "pitch": "-20Hz"},   # vs 学生 (male)
    "FP":     {"voice": MALE,   "rate": "+0%", "pitch": "-14Hz"},
    # Gendered role pairs (REPORT-CHOUKAI.md §4.1)
    "男性職員":   {"voice": MALE,   "rate": "+0%", "pitch": "-14Hz"},
    "女性職員":   {"voice": FEMALE, "rate": "+0%", "pitch": "-14Hz"},
    "男性係員":   {"voice": MALE,   "rate": "+0%", "pitch": "+8Hz"},
    "女性係員":   {"voice": FEMALE, "rate": "+6%", "pitch": "+18Hz"},
    "男性担当者": {"voice": MALE,   "rate": "+0%", "pitch": "-20Hz"},
    "女性担当者": {"voice": FEMALE, "rate": "+0%", "pitch": "-20Hz"},
    "男性講師":   {"voice": MALE,   "rate": "-6%", "pitch": "-24Hz"},
    "女性講師":   {"voice": FEMALE, "rate": "+0%", "pitch": "-25Hz"},
    "男性専門家": {"voice": MALE,   "rate": "-6%", "pitch": "-10Hz"},
    "女性専門家": {"voice": FEMALE, "rate": "+0%", "pitch": "-22Hz"},
    "男性店員":   {"voice": MALE,   "rate": "+4%", "pitch": "+12Hz"},
    "女性店員":   {"voice": FEMALE, "rate": "+6%", "pitch": "+22Hz"},
    "男性医者":   {"voice": MALE,   "rate": "+0%", "pitch": "-8Hz"},
    "女性医者":   {"voice": FEMALE, "rate": "+0%", "pitch": "-10Hz"},
    "男性アナウンサー": {"voice": MALE, "rate": "+4%", "pitch": "+6Hz"},
    "女性アナウンサー": {"voice": FEMALE, "rate": "+4%", "pitch": "+20Hz"},
}

# --- Pacing (seconds), measured across the 31-sitting archive -------------
# refs/JLPT_N2_NEW/ 2010-2025; per-sitting tables, sample counts and method in
# references/official_pacing.md. Every value sits inside the measured band; do
# not guess new ones. `make check` diffs these against the SKILL's table.
GAP_BETWEEN_LINES = 0.9        # turn gap; official median 0.51, p75 0.75, p90 1.08 (n=465)
GAP_AFTER_PRE_QUESTION = 3.0   # 問題1/2: after the question, before the talk
GAP_OPTION_READING = 20.0      # 問題2 only: official 20.22 s [20.19-20.81]
GAP_BETWEEN_SPOKEN_CHOICES = 3.0    # 問題3/5: between spoken choices 1〜4, official 3.10 s
GAP_BETWEEN_SPOKEN_RESPONSES = 2.2  # 問題4: official 2.23 s [2.14-2.31], n=795
GAP_BEFORE_REPEATED_QUESTION = 3.0  # 問題1/2 talk → question again, 2.94 s [2.81-3.19], n=74
GAP_AFTER_SHITSUMON1 = 10.0    # 問題5 two-question item: answer time for 質問1,
                               # placed BEFORE the 質問2 line (2番's choices are spoken)
# Pauses INSIDE one turn: official same-speaker pauses measure median 0.40 s
# [p75 0.53, p90 0.72]. The cap must stay under the turn gap (or one speaker
# sounds like two) and the floor above the cap (a ~0.1 s 促音 closure is never
# a pause to shape).
GAP_WITHIN_TURN_MAX = 0.5
SHAPE_PAUSE_FLOOR = 0.6

ANSWER_PAUSE = {               # answer time after each scored item
    "問題1": 12.0,
    "問題2": 12.0,
    "問題3": 8.0,
    "問題4": 8.0,
    "問題5": 10.0,
}
# An 例 gets no answer pause: official runs the practice item straight into
# 「最もよいものは◯番です。解答用紙の…」 (archive histogram: 12 × 12 s, 17 × 8 s).
PAUSE_AFTER_INSTRUCTION = 3.0
PAUSE_DEFAULT = 1.5

# The two pause LADDERS (F8). A flat 0.5 s within-turn cap put 37% of sub-2 s
# pauses on one value (20260807_1, 2026-08-21) against a 35% spike ceiling; the
# turn-gap ladder keeps GAP_BETWEEN_LINES as its median and reaches past 1.05 s
# for the 21–24% long-pause share both reference corpora show
# (official_pacing.md §6.1). The within-turn ladder tops out at official p90.
WITHIN_TURN_LADDER = (0.40, 0.40, 0.60, 0.72)
TURN_GAP_LADDER = (0.65, 0.90, 0.90, 1.15, 1.40)

# --- Script grammar ---------------------------------------------------------
ITEM_RE = re.compile(r"^(例。|\d+番。)")
SPEAKER_RE = re.compile(r"^([^:: ]{1,6})[::](.*)$")
CHOICE_RE = re.compile(r"^[1-4]、")

# 「最もよいものは◯番です。」 is an 例-ONLY line: it belongs to the 問題1〜4
# practice confirmation, which always continues with 「解答用紙の…」. A bare
# reveal after a scored item speaks the answer aloud and ruins the exam.
REVEAL_RE = re.compile(r"^(?:質問[12]の)?最もよいものは\d番です。")
EXAMPLE_CONFIRM_RE = re.compile(
    r"^最もよいものは\d番です。解答用紙の問題\dの例のところを見てください。")
ANNOTATION_RE = re.compile(r"[（(]※")

# Required structure of a full N2 script. Counts INCLUDE the 例 where one exists.
# 問題5 has no 例 (「この問題には練習はありません。」) and its 2番 block carries two
# questions (質問1/質問2), giving 3 answers from 2 item blocks.
EXPECTED_ITEMS = {"問題1": 6, "問題2": 7, "問題3": 6, "問題4": 12, "問題5": 2}
NEEDS_EXAMPLE = ("問題1", "問題2", "問題3", "問題4")
# The canonical opening is `choukai-audio` §"The opening announcement"
# (「Nにの…」 was an edge-tts digit workaround, removed 2026-09-11).
OPENING = "これから、N2の聴解試験を始めます"
CLOSING = "これで、聴解試験を終わります。"
NO_PRACTICE = "この問題には練習はありません。"
TYPO_RE = re.compile(r"問題用紙になに印刷")   # 「何も印刷」 mistyped


def validate_script(blocks, *, require_p5_question_markers: bool = True):
    """Raise SystemExit on anything that would corrupt the exam. Two classes:

    (1) lines that must never be SPOKEN (answer reveals, authoring notes), and
    (2) STRUCTURE — the 例/practice machinery and item counts. A missing 例 or
        announcer line is silent in the audio, so both are enforced here.
    """
    errors = []
    section = None
    items = {k: 0 for k in EXPECTED_ITEMS}
    examples = {k: 0 for k in EXPECTED_ITEMS}
    confirms = {k: 0 for k in EXPECTED_ITEMS}
    practice_cue = {k: 0 for k in EXPECTED_ITEMS}
    no_practice = {k: 0 for k in EXPECTED_ITEMS}
    text = "\n".join(blocks)

    for bi, block in enumerate(blocks):
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        if not lines:
            continue
        first = lines[0]
        m = re.match(r"^(問題[1-5])。$", first)
        if m:
            section = m.group(1)
            if len(lines) > 1:
                errors.append(f"block {bi} — header 「{first}」 must be a single-line block (got {len(lines)} lines)")
        is_example = first.startswith("例。")
        if ITEM_RE.match(first) and section:
            items[section] += 1
            if is_example:
                examples[section] += 1

        for line in lines:
            # --- class 1: must never be spoken ---
            if ANNOTATION_RE.search(line):
                errors.append(f"block {bi} — authoring annotation would be read "
                              f"aloud: {line}")
            if TYPO_RE.search(line):
                errors.append(f"block {bi} — typo 「なに印刷」 (should be "
                              f"「何も印刷」): {line}")
            if REVEAL_RE.match(line):
                if EXAMPLE_CONFIRM_RE.match(line):
                    if section:
                        confirms[section] += 1
                    continue
                errors.append(
                    f"block {bi} — answer revealed for a scored item"
                    + (" (例 block, but not the full 解答用紙 confirmation)"
                       if is_example else "") + f": {line}")
            # --- class 2: structural cues ---
            if section:
                if "では、練習しましょう。" in line:
                    practice_cue[section] += 1
                if NO_PRACTICE in line:
                    no_practice[section] += 1

        # 問題5's two-question item must be ONE block, or the answer pause lands
        # between 質問1 and 質問2 instead of after the item.
        if "質問1。" in block and "質問2。" not in block:
            errors.append(f"block {bi} — 質問1 without 質問2 in the same block; "
                          f"the 問題5 two-question item must not be split")

        # …and both markers must BE there: the 10 s answer time for 質問1 is
        # keyed off 「質問2。」, and `verify_fidelity._split_spoken_block` reads
        # both to split 問5-2-1 from 問5-2-2 (incident 20260904_1, 2026-09-04:
        # 1.17 s where 10 s belongs).
        if ITEM_RE.match(first) and section == "問題5":
            spoken = sum(1 for l in lines if CHOICE_RE.match(l))
            missing = [t for t in ("質問1。", "質問2。") if t not in block]
            if require_p5_question_markers and spoken >= 8 and missing:
                errors.append(
                    f"block {bi} — 問題5 two-question item ({spoken} spoken "
                    f"choice lines) is missing {'/'.join(missing)}; the "
                    f"{GAP_AFTER_SHITSUMON1:g} s answer pause for 質問1 is keyed "
                    f"off 「質問2。」. Prefix each question line "
                    f"(「質問1。<question>」/「質問2。<question>」)")

        # Every item (例/N番) must carry its own dialogue/speech/options in the
        # SAME block: a stray blank line splits one item into marker-only /
        # dialogue / repeated-question blocks and every pause keyed off a
        # block's first line lands in the wrong place (shipped in tests 2, 3, 4).
        # 問題4's stimulus is conventionally untagged, so it is checked for its
        # spoken option lines instead of a speaker tag.
        if ITEM_RE.match(first) and section:
            rest = lines[1:]
            if section == "問題4":
                if sum(1 for l in rest if CHOICE_RE.match(l)) < 3:
                    errors.append(
                        f"block {bi} ({first[:30]}…) — item has fewer than 3 "
                        f"spoken option lines (`1、`/`2、`/`3、`) in the same "
                        f"block as its marker; they were likely split into a "
                        f"separate block by a stray blank line, which "
                        f"corrupts pause placement (see "
                        f"choukai-audio/SKILL.md 'Block conventions')")
            elif not any(SPEAKER_RE.match(l) for l in rest):
                errors.append(
                    f"block {bi} ({first[:30]}…) — item has no speaker-tagged "
                    f"line in the same block as its marker; the dialogue/speech "
                    f"was likely split into a separate block by a stray blank "
                    f"line, which corrupts pause placement (see "
                    f"choukai-audio/SKILL.md 'Block conventions')")

    # --- whole-file structure ---
    if OPENING not in text:
        errors.append(f"missing opening announcement 「{OPENING}…」")
    if blocks[-1].strip() != CLOSING:
        errors.append(f"the last block of the script must be exactly 「{CLOSING}」 on its own line")
    # 問題5 prints nothing for EITHER item, so BOTH 1番 and 2番 get a spoken
    # 「問題用紙に何も印刷されていません…」 lead-in of their own. (問題3/4 say the
    # phrase inside a 「問題Nでは、…」 block, so never satisfy this startswith.)
    if "問題5。" in text:
        lead_ins = sum(1 for b in blocks
                       if b.strip().startswith("問題用紙に何も印刷されていません"))
        if lead_ins != 2:
            errors.append(
                f"問題5: {lead_ins} lead-in block(s) starting with 「問題用紙に何も"
                f"印刷されていません」, expected 2 (one before 1番, one before 2番)")

    for sec, want in EXPECTED_ITEMS.items():
        if f"{sec}。" not in text:
            errors.append(f"{sec} section header 「{sec}。」 missing")
            continue
        if items[sec] != want and not (sec == "問題5" and items[sec] in (2, 3)):
            errors.append(f"{sec}: {items[sec]} item block(s), expected {want}"
                          + (" (例 + scored items)" if sec in NEEDS_EXAMPLE else ""))
        if sec in NEEDS_EXAMPLE:
            if examples[sec] != 1:
                errors.append(f"{sec}: {examples[sec]} 例 block(s), expected exactly 1")
            if practice_cue[sec] != 1:
                errors.append(f"{sec}: 「では、練習しましょう。」 appears "
                              f"{practice_cue[sec]} time(s), expected exactly 1")
            if confirms[sec] != 1:
                errors.append(f"{sec}: {confirms[sec]} 例 confirmation line(s) "
                              f"(「最もよいものは◯番です。解答用紙の…」), expected exactly 1")
        else:
            if examples[sec]:
                errors.append(f"{sec} must have NO 例 ({NO_PRACTICE})")
            if no_practice[sec] != 1:
                errors.append(f"{sec}: 「{NO_PRACTICE}」 appears "
                              f"{no_practice[sec]} time(s), expected exactly 1")

    # --- speaker labels must all be in the map ---
    unmapped = set()
    for block in blocks:
        for line in block.split("\n"):
            m = SPEAKER_RE.match(line.strip())
            if m and m.group(1) not in SPEAKER_MAP:
                unmapped.add(m.group(1))
    if unmapped:
        errors.append(f"speaker label(s) not in SPEAKER_MAP (every gate that "
                      f"parses turns would read them as narration): {sorted(unmapped)}")

    if errors:
        raise SystemExit(
            "The script violates the choukai contract.\n"
            "See .agents/choukai-audio/SKILL.md.\n\n  "
            + "\n  ".join(errors))
    print(f"  script OK: {len(blocks)} blocks, items "
          + ", ".join(f"{k}={items[k]}" for k in EXPECTED_ITEMS))
