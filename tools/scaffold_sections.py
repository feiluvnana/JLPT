#!/usr/bin/env python3
"""Scaffold the three stage-2 authoring fragments from `test_spec.json`.

Writes `tests/<id>/_sections/`:
    問1-6_文字語彙.md   問7-9_文法.md   問10-14_読解.md

Each is a booklet body — canonical `## 問題N` lines (the level table, via
`assemble_paper.canonical_heading`), one slot per item carrying its drawn
target — then a literal `<!-- KEY -->` line and that fragment's key table,
with the **key already filled from `answer_positions`**. Authors write items
whose correct option sits where the key says; they never choose a position.
`make assemble <id>` merges the three into `言語知識・読解.md`.

There is no 聴解 fragment: `make mp3` composes the listening half from banked
recordings (choukai-audio Part 0).

Two defects this replaced (skill audit 2026-09-28): every key cell was written
as `1` regardless of `answer_positions`, and 問題9 read a `cloze_topic` spec
key the sampler never writes, so its theme line was always a placeholder.

Usage:
    python3 tools/scaffold_sections.py tests/20260928_1 [--overwrite]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from assemble_paper import canonical_heading, _q9_range  # noqa: E402
import level as LEVEL  # noqa: E402  (on sys.path via assemble_paper)

OPTS = " 1. 選択肢1  2. 選択肢2  3. 選択肢3  4. 選択肢4\n"
OPTS_V = " 1. 選択肢1\n 2. 選択肢2\n 3. 選択肢3\n 4. 選択肢4\n"

# 大問 → (spec item category, how the slot names its target). N2's generated
# paper; a new level brings its own row when it is calibrated.
DRAWN = {
    1: ("kanji_reading", "例文（下線語 **{t}**）"),
    2: ("orthography", "例文（下線語 **{t}** のかな書き）"),
    3: ("word_formation", "例文（（　）に入る接辞「{t}」）"),
    4: ("context_words", "例文（（　）に入る語「{t}」）"),
    5: ("paraphrase", "例文（下線語 **{t}**）"),
    6: ("usage", "**{t}**"),
    7: ("grammar_p7", "例文（文法「{t}」）"),
    8: ("grammar_p8", "リード ＿＿ ＿＿ ★ ＿＿ 末尾。（文型「{t}」）"),
}
VERTICAL = {6}
READING_SHAPE = {10: 5, 11: 4}          # passages; 問題11 is 4 × 2 questions


def _target(x) -> str:
    return x.get("item", x) if isinstance(x, dict) else x


def _ranges(level: str) -> dict[int, range]:
    g = LEVEL.gengo(level)
    counts = LEVEL.gengo_shapes(level)[g["generated_shape"]]
    out, q = {}, 1
    for m, n in zip(g["mondai"], counts):
        out[int(m["mondai"][2:])] = range(q, q + n)
        q += n
    return out


def _key(spec: dict, n: int, rng: range) -> list[int | str]:
    ap = spec.get("answer_positions", {})
    pos = ap.get(f"問題{n}_語彙") or ap.get(f"問題{n}") or []
    if len(pos) != len(rng):
        return ["?"] * len(rng)
    return pos


def _key_table(title: str, spec: dict, rows: list[tuple[int, range]]) -> list[str]:
    out = [KEY, f"## {title}", "| 問題 | 正解 | 解説 |", "|---|---|---|"]
    for n, rng in rows:
        for q, a in zip(rng, _key(spec, n, rng)):
            out.append(f"| {q} | {a} | 解説をここに記述 |")
    return out


KEY = "<!-- KEY -->"


def _drawn_block(spec: dict, n: int, rng: range, level: str) -> list[str]:
    cat, tmpl = DRAWN[n]
    drawn = spec.get("items", {}).get(cat, [])
    out = [canonical_heading(level, n, "", f"## 問題{n}"), ""]
    for i, q in enumerate(rng):
        t = _target(drawn[i]) if i < len(drawn) else "（未抽選）"
        out += [f"**{q}** " + tmpl.format(t=t), OPTS_V if n in VERTICAL else OPTS]
    return out


def scaffold(test_dir: Path, overwrite: bool = False) -> list[Path]:
    spec = json.loads((test_dir / "test_spec.json").read_text(encoding="utf-8"))
    level = spec.get("level") or LEVEL.level_of(test_dir.name)
    r = _ranges(level)
    sec = test_dir / "_sections"
    sec.mkdir(parents=True, exist_ok=True)
    files: dict[str, list[str]] = {}

    moji = []
    for n in range(1, 7):
        moji += _drawn_block(spec, n, r[n], level)
    files["問1-6_文字語彙.md"] = moji + _key_table("文字・語彙", spec, [(n, r[n]) for n in range(1, 7)])

    bun = []
    for n in (7, 8):
        bun += _drawn_block(spec, n, r[n], level)
    first, last = _q9_range(level, None)
    bun += [canonical_heading(level, 9, "", "## 問題9"), "",
            "（問題9: 約500〜700字の文章。題材は著者が決める — 他の11面と重ならないこと。"
            f"空欄は（ {first} ）〜（ {last} ）を本文中に置く）", ""]
    for q in r[9]:
        bun += [f"**{q}**", OPTS]
    files["問7-9_文法.md"] = bun + _key_table("文法", spec, [(n, r[n]) for n in (7, 8, 9)])

    topics = spec.get("items", {}).get("reading_topics", [])
    doc = ["<!-- reading_topics (theme + avoid) — the orchestrator's allocation says "
           "which entry feeds which surface: "
           + "; ".join(f"[{i}] {t.get('theme', t) if isinstance(t, dict) else t}"
                       for i, t in enumerate(topics)) + " -->", ""]
    for n in range(10, 15):
        rng = list(r[n])
        if n in READING_SHAPE:
            k = READING_SHAPE[n]
            per = len(rng) // k
            block = "\n".join(f"### ({i})" for i in range(1, k + 1))
            doc += [canonical_heading(level, n, block, f"## 問題{n}"), ""]
            for i in range(k):
                doc += [f"### ({i + 1})", "", "（本文）", ""]
                for q in rng[i * per:(i + 1) * per]:
                    doc += [f"**{q}** 設問", OPTS_V]
        else:
            head = (f"## 問題{n} 右のページは、〈…の案内〉である。" if n == 14 else f"## 問題{n}")
            doc += [canonical_heading(level, n, "", head), ""]
            doc += (["A", "", "（本文）", "", "B", "", "（本文）", ""] if n == 12 else ["（本文）", ""])
            for q in rng:
                doc += [f"**{q}** 設問", OPTS_V]
    files["問10-14_読解.md"] = doc + _key_table("読解", spec, [(n, r[n]) for n in range(10, 15)])

    written = []
    for name, lines in files.items():
        p = sec / name
        if p.exists() and not overwrite:
            print(f"  kept {p.name} (exists; --overwrite to replace)")
            continue
        p.write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")
        written.append(p)
        print(f"  scaffolded {p.name}")
    return written


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("test_dir", type=Path)
    ap.add_argument("--overwrite", action="store_true")
    a = ap.parse_args()
    if not (a.test_dir / "test_spec.json").is_file():
        sys.exit(f"no test_spec.json in {a.test_dir} — run `make sample` first")
    scaffold(a.test_dir, a.overwrite)
    return 0


if __name__ == "__main__":
    sys.exit(main())
