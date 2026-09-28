#!/usr/bin/env python3
"""
JLPT Mock Exam Grading & Diagnostic Script.

Grades user responses against official answer keys in tests/<test_id>/,
calculates standardized scaled scores (0-180), evaluates Pass/Fail criteria,
identifies weak sub-sections, and writes the structured result document
tests/<test_id>/採点結果.json.

Usage:
    # 1. Build the merged answer sheet (once per test, or `make sheet 1`):
    python3 .agents/exam-app/scripts/build_interactive.py tests/1

    # 2. Answer it in a browser (`make serve`, pick the test), press 「採点する」 —
    #    that already writes 採点結果.json and ユーザー解答.json. To re-grade from the CLI:
    python3 .agents/exam-app/scripts/grade_answers.py --test-dir tests/1 --user-answers tests/1/ユーザー解答.json

    # 3. Quick grade via CLI strings:
    python3 .agents/exam-app/scripts/grade_answers.py --test-dir tests/1 --answers-gengo "1:4,2:2,3:1..." --answers-choukai "問1-1:2,問1-2:3..."
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# The 大問 map, the era shapes, the 聴解 labels and the scoring bands are the
# LEVEL's structure table (jlpt-exam-structure/references/levels/<LEVEL>.json,
# read through level.py) — not literals here. They used to be: 問1 was 1-8, 問11
# was 60-64 and 問14 was 71-75 while jlpt-exam-structure said otherwise, so every
# 大問別 diagnostic filed questions under the wrong 大問.
#
# THE EXAM HAS ERAS and an imported past paper may belong to any of them
# (jlpt-exam-structure §"The counts below are the CURRENT era's"). A generated
# mock is always the level's `generated_shape` (N2: 71); an import is whatever
# its sitting printed. 7/2021 is a 72-question N2 paper — 問題11 ran 3 passages
# x 3Q — and before the table was era-aware its Q72 fell outside every 大問.
# One row per shape, counts in 大問 order; ranges are derived, so a count and a
# range cannot drift apart.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "jlpt-exam-structure" / "scripts"))
import level as LEVEL  # noqa: E402


def gengo_shapes(level: str = LEVEL.DEFAULT_LEVEL) -> dict:
    return LEVEL.gengo_shapes(level)


def _generated_shape(level: str) -> int:
    return LEVEL.gengo(level)["generated_shape"]


# N2's table, under the names callers already use.
GENGO_SHAPES = gengo_shapes()
_GENGO_LABELS = [(m["code"], m["grader_name"],
                  "言語知識" if i < LEVEL.gengo()["goi_mondai"] else "読解")
                 for i, m in enumerate(LEVEL.gengo()["mondai"])]


def gengo_taxonomy(max_q: int | None = None, level: str = LEVEL.DEFAULT_LEVEL) -> dict:
    """The 大問 map for a paper whose last question is `max_q`.

    Unknown counts fall back to the level's generated shape — a mangled key
    table must not crash the grader — but every shape this repo has actually
    seen is a row in the level table.
    """
    g = LEVEL.gengo(level)
    shapes = LEVEL.gengo_shapes(level)
    counts = shapes.get(max_q, shapes[g["generated_shape"]])
    tax, q = {}, 1
    for i, (m, n) in enumerate(zip(g["mondai"], counts)):
        tax[m["code"]] = {"name": m["grader_name"], "range": (q, q + n - 1),
                          "section": "言語知識" if i < g["goi_mondai"] else "読解",
                          "total": n}
        q += n
    return tax


def gengo_goi_cutoff(max_q: int | None = None, level: str = LEVEL.DEFAULT_LEVEL) -> int:
    """Last question of 文字・語彙＋文法; 読解 starts at the next one."""
    g = LEVEL.gengo(level)
    shapes = LEVEL.gengo_shapes(level)
    return sum(shapes.get(max_q, shapes[g["generated_shape"]])[:g["goi_mondai"]])


# The current era's map, kept under its historical name for callers that grade a
# generated N2 mock (always 71).
GENGO_QUESTION_TAXONOMY = gengo_taxonomy()

# Guard: every shape must tile 1..max_q exactly, with no gap and no overlap.
for _level in LEVEL.available():
    if not LEVEL.has_structure(_level):
        continue
    for _max_q, _counts in LEVEL.gengo_shapes(_level).items():
        assert sum(_counts) == _max_q, (
            f"{_level} gengo shape {_max_q} sums to {sum(_counts)}, not {_max_q}")
        _covered = [q for s in gengo_taxonomy(_max_q, _level).values()
                    for q in range(s["range"][0], s["range"][1] + 1)]
        assert sorted(_covered) == list(range(1, _max_q + 1)), (
            f"{_level} gengo_taxonomy({_max_q}) must tile questions 1-{_max_q} exactly "
            f"(got {len(_covered)} entries, duplicates/gaps present)")


def choukai_taxonomy(level: str = LEVEL.DEFAULT_LEVEL) -> dict:
    return {m["code"]: {"name": m["grader_name"], "section": "聴解"}
            for m in LEVEL.choukai(level)["mondai"]}


CHOUKAI_QUESTION_TAXONOMY = choukai_taxonomy()


# Weak-area study advice, keyed by 大問 group — the level table's `advice`, since
# it names that level's textbooks. Module level so that build_interactive.py
# (exam-app) serializes the SAME strings into the in-page grader — one source of
# truth, no drift between the two implementations.
def advice_for(level: str = LEVEL.DEFAULT_LEVEL) -> dict:
    return {code: a["text"] for a in (LEVEL.load(level).get("advice") or [])
            for code in a["codes"]}


ADVICE = [(a["codes"], a["text"]) for a in LEVEL.load().get("advice") or []]
ADVICE_FOR = advice_for()


def parse_gengo_keys(gengo_md_path: Path) -> dict:
    """Extract correct answers for Language Knowledge & Reading (Questions 1 to 71)."""
    if not gengo_md_path.is_file():
        raise FileNotFoundError(f"File not found: {gengo_md_path}")

    text = gengo_md_path.read_text(encoding="utf-8")
    answers = {}

    for line in text.splitlines():
        line_str = line.strip()
        if line_str.startswith("|") and line_str.endswith("|"):
            cells = [c.strip() for c in line_str.split("|")[1:-1]]
            # Iterate through cell pairs: (Q, Ans)
            for i in range(len(cells) - 1):
                q_clean = re.sub(r"[\*\s]", "", cells[i])
                a_clean = re.sub(r"[\*\s]", "", cells[i+1])
                if q_clean.isdigit() and a_clean.isdigit():
                    q_num = int(q_clean)
                    a_num = int(a_clean)
                    if 1 <= q_num <= 75 and 1 <= a_num <= 4:
                        answers[q_num] = a_num

    return answers


def parse_choukai_keys(choukai_md_path: Path) -> dict:
    """
    Extract correct answers for Listening (Choukai).
    Returns dict mapping item key (e.g. '問1-1', '問4-5', '問5-2-1') to correct answer option (1-4).
    """
    if not choukai_md_path.is_file():
        return {}

    text = choukai_md_path.read_text(encoding="utf-8")
    answers = {}

    # Find answer section after # 【正解・解説】 or # 解答・解説
    m = re.search(r"#+\s*【?正解[・\s]解説】?", text)
    ans_text = text[m.start():] if m else text

    current_mondai = None
    for line in ans_text.splitlines():
        line_str = line.strip()
        mondai_match = re.search(r"##\s*問題([1-5])", line_str)
        if mondai_match:
            current_mondai = int(mondai_match.group(1))
            continue

        if current_mondai and line_str.startswith("|"):
            # Table row parsing
            # Matches: | 1 | **2** | ... or | 1 | 2 | or | 3番-質問1 | 2 |
            cells = [c.strip() for c in line_str.split("|")[1:-1]]
            if len(cells) >= 2:
                q_label = re.sub(r"[\*\s]", "", cells[0])
                ans_str = re.sub(r"[\*\s]", "", cells[1])

                # Validate answer choice (1-4)
                if ans_str.isdigit() and 1 <= int(ans_str) <= 4:
                    ans_val = int(ans_str)
                    # Extract sub question label
                    if current_mondai in [1, 2, 3, 4]:
                        q_digit = re.search(r"(\d+)", q_label)
                        if q_digit:
                            answers[f"問{current_mondai}-{q_digit.group(1)}"] = ans_val
                    elif current_mondai == 5:
                        if "質問1" in q_label:
                            answers["問5-3-1" if ("3" in q_label or "3番" in q_label) else "問5-2-1"] = ans_val
                        elif "質問2" in q_label:
                            answers["問5-3-2" if ("3" in q_label or "3番" in q_label) else "問5-2-2"] = ans_val
                        elif re.search(r"^1$|^1番$|1番(?!.*質問)", q_label) or (
                                "1" in q_label and "質問" not in q_label and "2" not in q_label):
                            answers["問5-1"] = ans_val
                        elif re.search(r"^2$|^2番$|2番(?!.*質問)", q_label) or (
                                "2" in q_label and "質問" not in q_label and "3" not in q_label):
                            answers["問5-2"] = ans_val

    return answers


def grade(gengo_keys: dict, choukai_keys: dict, user_answers: dict,
          level: str = LEVEL.DEFAULT_LEVEL) -> dict:
    """
    Grading engine.
    Calculates raw scores, scaled scores (0-60 for each section), Pass/Fail, and category stats.
    """
    user_gengo = user_answers.get("言語知識_読解", {})
    user_choukai = user_answers.get("聴解", {})

    max_q = max(gengo_keys.keys()) if gengo_keys else _generated_shape(level)
    goi_cutoff = gengo_goi_cutoff(max_q, level)
    taxonomy = gengo_taxonomy(max_q, level)
    sc = LEVEL.scoring(level)
    (sec_goi, sec_dokkai, sec_choukai) = sc["sections"]

    # 1. Language Knowledge (Goi & Bunpou: Q1 - Q51/54)
    goi_bunpou_total = goi_cutoff
    goi_bunpou_correct = 0
    gengo_detail = {}

    for q in range(1, goi_cutoff + 1):
        correct = gengo_keys.get(q)
        user_choice = user_gengo.get(str(q))
        if user_choice is not None:
            user_choice = int(user_choice)
        is_correct = (user_choice == correct) if correct is not None and user_choice is not None else False
        if is_correct:
            goi_bunpou_correct += 1
        gengo_detail[q] = {
            "correct": correct,
            "user": user_choice,
            "is_correct": is_correct
        }

    # 2. Reading (Dokkai: Q52/55 - Q71/75)
    dokkai_total = max_q - goi_cutoff
    dokkai_correct = 0
    for q in range(goi_cutoff + 1, max_q + 1):
        correct = gengo_keys.get(q)
        user_choice = user_gengo.get(str(q))
        if user_choice is not None:
            user_choice = int(user_choice)
        is_correct = (user_choice == correct) if correct is not None and user_choice is not None else False
        if is_correct:
            dokkai_correct += 1
        gengo_detail[q] = {
            "correct": correct,
            "user": user_choice,
            "is_correct": is_correct
        }

    # 3. Listening (Choukai)
    choukai_total = len(choukai_keys) if choukai_keys else LEVEL.choukai(level)["generated_shape"]
    choukai_correct = 0
    choukai_detail = {}

    for k, correct in choukai_keys.items():
        user_choice = user_choukai.get(k)
        if user_choice is not None:
            user_choice = int(user_choice)
        is_correct = (user_choice == correct) if user_choice is not None else False
        if is_correct:
            choukai_correct += 1
        choukai_detail[k] = {
            "correct": correct,
            "user": user_choice,
            "is_correct": is_correct
        }

    # Scaled Scores (JLPT Scale out of 60 per section)
    scaled_goi_bunpou = round((goi_bunpou_correct / goi_bunpou_total) * sec_goi["max"]) if goi_bunpou_total > 0 else 0
    scaled_dokkai = round((dokkai_correct / dokkai_total) * sec_dokkai["max"]) if dokkai_total > 0 else 0
    scaled_choukai = round((choukai_correct / choukai_total) * sec_choukai["max"]) if choukai_total > 0 else 0

    total_scaled_score = scaled_goi_bunpou + scaled_dokkai + scaled_choukai

    # Pass/Fail evaluation
    # Overall >= the level's pass mark AND every section >= its cutoff (N2: 90, 19)
    cutoff_pass = (scaled_goi_bunpou >= sec_goi["cutoff"]) and (scaled_dokkai >= sec_dokkai["cutoff"]) \
        and (scaled_choukai >= sec_choukai["cutoff"])
    overall_pass = total_scaled_score >= sc["pass"]
    is_passed = overall_pass and cutoff_pass

    # Sub-category breakdown
    taxonomy_stats = {}
    for code, spec in taxonomy.items():
        start, end = spec["range"]
        cat_correct = sum(1 for q in range(start, end + 1) if gengo_detail.get(q, {}).get("is_correct"))
        cat_total = (end - start + 1)
        taxonomy_stats[code] = {
            "name": spec["name"],
            "section": spec["section"],
            "correct": cat_correct,
            "total": cat_total,
            "percentage": round((cat_correct / cat_total) * 100, 1) if cat_total > 0 else 0
        }

    # Listening mondai breakdown
    choukai_mondai_stats = {f"問題{m}": {"correct": 0, "total": 0} for m in range(1, 6)}
    for k, item in choukai_detail.items():
        m = re.search(r"問([1-5])", k)
        if m:
            m_name = f"問題{m.group(1)}"
            choukai_mondai_stats[m_name]["total"] += 1
            if item["is_correct"]:
                choukai_mondai_stats[m_name]["correct"] += 1

    for m_name, stats in choukai_mondai_stats.items():
        tot = stats["total"]
        cor = stats["correct"]
        taxonomy_stats[m_name] = {
            "name": choukai_taxonomy(level).get(m_name, {}).get("name", m_name),
            "section": "聴解",
            "correct": cor,
            "total": tot,
            "percentage": round((cor / tot) * 100, 1) if tot > 0 else 0
        }

    return {
        "summary": {
            "passed": is_passed,
            "total_scaled_score": total_scaled_score,
            "max_scaled_score": sc["max"],
            "cutoff_passed": cutoff_pass,
            "overall_threshold_passed": overall_pass,
            "sections": {
                sec_goi["name"]: {
                    "raw_correct": goi_bunpou_correct,
                    "raw_total": goi_bunpou_total,
                    "scaled_score": scaled_goi_bunpou,
                    "cutoff": sec_goi["cutoff"],
                    "passed_cutoff": scaled_goi_bunpou >= sec_goi["cutoff"]
                },
                sec_dokkai["name"]: {
                    "raw_correct": dokkai_correct,
                    "raw_total": dokkai_total,
                    "scaled_score": scaled_dokkai,
                    "cutoff": sec_dokkai["cutoff"],
                    "passed_cutoff": scaled_dokkai >= sec_dokkai["cutoff"]
                },
                sec_choukai["name"]: {
                    "raw_correct": choukai_correct,
                    "raw_total": choukai_total,
                    "scaled_score": scaled_choukai,
                    "cutoff": sec_choukai["cutoff"],
                    "passed_cutoff": scaled_choukai >= sec_choukai["cutoff"]
                }
            }
        },
        "taxonomy_stats": taxonomy_stats,
        "detail_gengo": gengo_detail,
        "detail_choukai": choukai_detail
    }


def result_payload(results: dict, test_id: str, graded_at: str | None = None) -> dict:
    """The 採点結果.json document.

    This is the ONLY report artifact — there is no Markdown report any more.
    The in-page grader in 解答.html builds the identical structure (the exam app
    saves it over POST /api/tests/<id>/submit), and `make check` compares the two
    documents field by field, so the shape here is a contract, not a preference.
    Entries with no items are dropped so a partially built test cannot show a
    大問 as 0% purely because it has no questions yet.
    """
    stats = {code: s for code, s in results["taxonomy_stats"].items() if s["total"]}
    weak = [{"code": code, "name": s["name"], "section": s["section"],
             "percentage": s["percentage"], "advice": advice_for(LEVEL.level_of(test_id)).get(code, "")}
            for code, s in stats.items() if s["percentage"] < 60]
    return {
        "test_id": test_id,
        "graded_at": graded_at or datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "summary": results["summary"],
        "taxonomy_stats": stats,
        "weak_areas": weak,
        "detail_gengo": {str(q): d for q, d in results["detail_gengo"].items()},
        "detail_choukai": results["detail_choukai"],
    }


def main():
    parser = argparse.ArgumentParser(description="Grade user responses for JLPT mock test.")
    parser.add_argument("--test-dir", required=True, help="Path to test output directory, e.g. tests/1")
    parser.add_argument("--user-answers",
                        help="Comma-separated user answer JSON file(s). "
                             "Default: ユーザー解答*.json in the test dir or cwd.")
    parser.add_argument("--answers-gengo", help="Quick gengo answers string like '1:4,2:2,3:1...'")
    parser.add_argument("--answers-choukai", help="Quick choukai answers string like '問1-1:2,問1-2:3...'")

    args = parser.parse_args()

    test_path = Path(args.test_dir)
    gengo_md = test_path / "言語知識・読解.md"
    choukai_md = test_path / "聴解.md"

    if not gengo_md.exists():
        print(f"Error: {gengo_md} not found.", file=sys.stderr)
        sys.exit(1)

    # 1. Parse correct answer keys
    gengo_keys = parse_gengo_keys(gengo_md)
    choukai_keys = parse_choukai_keys(choukai_md)

    print(f"Loaded answer keys for {test_path}:")
    print(f"  - 言語知識・読解: {len(gengo_keys)} questions parsed")
    print(f"  - 聴解: {len(choukai_keys)} questions parsed")

    # 2. Load user answers. Source of truth is the JSON saved by the merged
    #    answer sheet (解答.html), which covers both halves in one file. Several
    #    matching files still merge cleanly; CLI strings override.
    user_answers = {"言語知識_読解": {}, "聴解": {}}

    if args.user_answers:
        sources = [Path(x.strip()) for x in args.user_answers.split(",")]
    else:
        sources = sorted(test_path.glob("ユーザー解答*.json")) + \
                  sorted(Path.cwd().glob("ユーザー解答*.json"))

    for ua_path in sources:
        if not ua_path.exists():
            print(f"  warning: {ua_path} not found", file=sys.stderr)
            continue
        loaded = json.loads(ua_path.read_text(encoding="utf-8"))
        user_answers["言語知識_読解"].update(loaded.get("言語知識_読解", {}))
        user_answers["聴解"].update(loaded.get("聴解", {}))
        print(f"Loaded user answers from {ua_path}")
    if not sources:
        print("  no ユーザー解答*.json found — run `make serve`, pick this test "
              "from the list, answer, then press 「採点する」.", file=sys.stderr)

    if args.answers_gengo:
        pairs = args.answers_gengo.split(",")
        for pair in pairs:
            if ":" in pair:
                q, a = pair.strip().split(":")
                user_answers["言語知識_読解"][q.strip()] = int(a.strip())

    if args.answers_choukai:
        pairs = args.answers_choukai.split(",")
        for pair in pairs:
            if ":" in pair:
                q, a = pair.strip().split(":")
                user_answers["聴解"][q.strip()] = int(a.strip())

    # 3. Perform Grading
    level = LEVEL.declared_level(test_path) or LEVEL.level_of(test_path.resolve().name)
    results = grade(gengo_keys, choukai_keys, user_answers, level)

    # 4. Save the structured result document
    payload = result_payload(results, test_path.name)
    out_json = test_path / "採点結果.json"
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    # 5. Print summary output to stdout
    summary = results["summary"]
    status_str = "PASSED (合格)" if summary["passed"] else "FAILED (不合格)"
    print(f"\n==========================================")
    print(f"       JLPT {level} GRADING RESULT ({test_path.name})")
    print(f"==========================================")
    print(f" Final Result    : {status_str}")
    sc = LEVEL.scoring(level)
    print(f" Total Scaled    : {summary['total_scaled_score']} / {sc['max']} (Pass threshold: {sc['pass']})")
    for (sec_name, sec_data), sec in zip(summary["sections"].items(), sc["sections"]):
        pass_cut = "OK" if sec_data["passed_cutoff"] else f"FAIL (Cutoff < {sec['cutoff']})"
        print(f"  - {sec_name:<16}: {sec_data['scaled_score']:2d}/{sec['max']} (Raw: {sec_data['raw_correct']}/{sec_data['raw_total']}) [{pass_cut}]")
    if payload["weak_areas"]:
        print(" Weak areas (<60%): " +
              ", ".join(f"{w['code']} {w['percentage']}%" for w in payload["weak_areas"]))
    print(f"==========================================")
    print(f"Result document saved to: {out_json}\n")


if __name__ == "__main__":
    main()