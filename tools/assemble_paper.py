#!/usr/bin/env python3
"""Assemble `言語知識・読解.md` from the stage-2 fragments, in the official layout.

Stage 3 used to merge `_sections/*.md` by hand, and the layout drifted with
every author: 19 of 29 generated papers shipped without the 【文字・語彙】/
【文法】/【読解】 part banners, and every one printed instruction lines the
official booklet never uses (問題5 「次の言葉の使い分けとして…」 came from the
scaffold itself). The layout is a format fact, so it now comes from the level
table (`jlpt-exam-structure/references/levels/<LEVEL>.json`: each 大問's
`instruction`, the part `banners`, the `key_heading`) and this script stamps it.

What it does:
- **assemble** (default): read `tests/<id>/_sections/*.md` — each a booklet body,
  then a literal `<!-- KEY -->` line, then that fragment's key tables — and
  write `tests/<id>/言語知識・読解.md`: banner + bodies in 大問 order, ONE key
  heading, then the key tables in the same order. Every `## 問題N` line is
  re-stamped with the canonical instruction.
- **--normalize**: re-stamp an already-merged paper in place (banners inserted
  where missing, instruction lines replaced). Layout only — no item, option,
  passage or key byte changes.
- **--check**: report the layout differences and exit 1 if any; writes nothing.
  `make check` runs the same comparison (`layout_problems()`).

Filled per paper: 問題9's blank range from the level's shape, 問題10/11's
passage count from their `### (k)` sub-headings, and 問題14's source line
(「右のページは、…である。」) from the author's own heading, which is the one
part of an instruction that describes the paper's content.

Usage:
    python3 tools/assemble_paper.py tests/20260928_1
    python3 tools/assemble_paper.py tests/20260917_1 --normalize
    python3 tools/assemble_paper.py tests/20260917_1 --check
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".agents" / "jlpt-exam-structure" / "scripts"))
import level as LEVEL  # noqa: E402

TARGET = "言語知識・読解.md"
KEY_MARK = "<!-- KEY -->"
HEAD_RE = re.compile(r"^## 問題(\d+)\b[ 　]*(.*)$")
BANNER_RE = re.compile(r"^# 【[^】]+】\s*$")
SOURCE_RE = re.compile(r"(?:右|次)のページは、(.+?)である。")
# What `scaffold_sections.py` writes into a slot. A fragment still carrying one
# is unfinished, and assembling it would ship the placeholder.
PLACEHOLDERS = ("選択肢1", "解説をここに記述", "（本文）", "〈…の案内〉", "例文（", "設問\n", "カード1", "（未抽選）")


class LayoutError(ValueError):
    pass


def _mondai(level: str) -> list[dict]:
    return LEVEL.gengo(level)["mondai"]


def _q9_range(level: str, max_q: int | None) -> tuple[int, int]:
    g = LEVEL.gengo(level)
    shapes = LEVEL.gengo_shapes(level)
    counts = shapes.get(max_q, shapes[g["generated_shape"]])
    idx = next(i for i, m in enumerate(g["mondai"]) if m["mondai"] == "問題9")
    first = sum(counts[:idx]) + 1
    return first, first + counts[idx] - 1


def canonical_heading(level: str, n: int, block: str, author_line: str,
                      max_q: int | None = None) -> str:
    """The official `## 問題N …` line for 大問 N, given its body block."""
    m = next((x for x in _mondai(level) if x["mondai"] == f"問題{n}"), None)
    if m is None or not m.get("instruction"):
        raise LayoutError(f"{level} table has no instruction for 問題{n}")
    fields: dict[str, object] = {}
    tmpl = m["instruction"]
    if "{first}" in tmpl:
        fields["first"], fields["last"] = _q9_range(level, max_q)
    if "{passages}" in tmpl:
        k = len(re.findall(r"^### \((\d+)\)", block, re.M))
        if not k:
            raise LayoutError(f"問題{n} has no `### (k)` passage sub-headings")
        fields["passages"] = k
    if "{source}" in tmpl:
        src = SOURCE_RE.search(author_line)
        if not src:
            raise LayoutError(
                f"問題{n}'s heading must say what the page is: "
                f"「右のページは、〈…の案内〉である。」 — got {author_line!r}")
        fields["source"] = src.group(1)
    return f"## 問題{n} " + tmpl.format(**fields)


def _split_blocks(body: str) -> list[tuple[int | None, list[str]]]:
    """[(大問 number or None for preamble, lines)] in document order."""
    blocks: list[tuple[int | None, list[str]]] = [(None, [])]
    for line in body.splitlines():
        h = HEAD_RE.match(line)
        if h:
            blocks.append((int(h.group(1)), [line]))
        else:
            blocks[-1][1].append(line)
    return blocks


def restamp(body: str, level: str, max_q: int | None = None) -> str:
    """Body with banners in place and every 問題N heading canonical."""
    part_of = {int(m["mondai"][2:]): m["part"] for m in _mondai(level)}
    banners = LEVEL.gengo(level)["banners"]
    out: list[str] = []
    current_part = None
    for n, lines in _split_blocks(body):
        if n is None:
            kept = [ln for ln in lines if not BANNER_RE.match(ln)]
            while kept and not kept[-1].strip():
                kept.pop()
            out.extend(kept)
            continue
        block = "\n".join(lines)
        part = part_of.get(n)
        if part is None:
            raise LayoutError(f"問題{n} is not a 大問 of {level}")
        if part != current_part:
            if out and out[-1].strip():
                out.append("")
            out += [f"# {banners[part]}", ""]
            current_part = part
        body_lines = [ln for ln in lines[1:] if not BANNER_RE.match(ln)]
        head_src = lines[0]
        # Older papers print a bare `## 問題N` and put the instruction on the
        # next non-blank line; lift that line into the heading so it is
        # replaced, not printed twice (問題14's source clause is read from it).
        first = next((i for i, ln in enumerate(body_lines) if ln.strip()), None)
        if (first is not None and not HEAD_RE.match(head_src).group(2).strip()
                and body_lines[first].strip().endswith("選びなさい。")):
            head_src = body_lines.pop(first)
        out.append(canonical_heading(level, n, block, head_src, max_q))
        out.extend(body_lines)
    text = "\n".join(out).strip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def _max_q(body: str) -> int | None:
    nums = [int(x) for x in re.findall(r"^\*\*(\d+)\*\*", body, re.M)]
    return max(nums) if nums else None


def _split_key(text: str) -> tuple[str, str]:
    m = re.search(r"^#+\s*(解答|【?正解).*$", text, re.M)
    if not m:
        raise LayoutError("no answer-key heading (# 解答…) found")
    return text[:m.start()], text[m.end():]


def normalize(text: str, level: str) -> str:
    body, keys = _split_key(text)
    head = LEVEL.gengo(level)["key_heading"]
    return restamp(body, level, _max_q(body)) + f"\n# {head}\n\n" + keys.lstrip("\n")


def layout_problems(text: str, level: str) -> list[str]:
    """Lines where a merged paper differs from the official layout."""
    try:
        want = normalize(text, level)
    except LayoutError as e:
        return [str(e)]
    got_lines, want_lines = text.rstrip("\n").splitlines(), want.rstrip("\n").splitlines()
    if got_lines == want_lines:
        return []
    probs = []
    got_heads = [ln for ln in got_lines if HEAD_RE.match(ln) or BANNER_RE.match(ln)]
    want_heads = [ln for ln in want_lines if HEAD_RE.match(ln) or BANNER_RE.match(ln)]
    for w in want_heads:
        if w not in got_heads:
            probs.append(f"missing or different: {w}")
    return probs or ["blank-line layout differs from the assembled form"]


def assemble(test_dir: Path, level: str, allow_placeholders: bool = False) -> str:
    sec = test_dir / "_sections"
    frags = sorted(sec.glob("*.md"),
                   key=lambda p: int(re.match(r"問(\d+)", p.name).group(1))
                   if re.match(r"問(\d+)", p.name) else 999)
    if not frags:
        raise LayoutError(f"no fragments in {sec.relative_to(ROOT)}")
    bodies, keys = [], []
    for f in frags:
        t = f.read_text(encoding="utf-8")
        if t.count(KEY_MARK) != 1:
            raise LayoutError(f"{f.name}: needs exactly one `{KEY_MARK}` line")
        b, k = t.split(KEY_MARK)
        # RC-R2-3(a), qa-report-20260928_1-round2: a scaffold orientation
        # comment rode into 20260928_1's 言語知識・読解.md between 問題9 and
        # 【読解】, where the 読解 measurements read it as 問題9's closing. The
        # scaffold no longer writes one; this refuses any that an author left,
        # because the paper is the one place a note must never ship.
        note = re.search(r"<!--.*?-->", b + k, re.S)
        if note:
            raise LayoutError(f"{f.name}: carries an HTML comment "
                              f"({note.group(0)[:50]!r}…) — author notes belong "
                              f"in the stage hand-off, not the paper; delete it")
        if re.search(r"^#+\s*(解答|【?正解)", b, re.M):
            raise LayoutError(f"{f.name}: a fragment must not carry its own key heading")
        bodies.append(b.strip("\n"))
        keys.append(k.strip("\n"))
    body = "\n\n".join(bodies) + "\n"
    everything = body + "".join(keys)
    left = {p.strip(): everything.count(p) for p in PLACEHOLDERS if p in everything}
    if left and not allow_placeholders:
        raise LayoutError(f"fragments still hold scaffold placeholders {left} — "
                          f"finish authoring first")
    nums = [int(x) for x in re.findall(r"^\*\*(\d+)\*\*", body, re.M)]
    shapes = LEVEL.gengo_shapes(level)
    want_n = LEVEL.gengo(level)["generated_shape"]
    if sorted(nums) != list(range(1, want_n + 1)):
        missing = sorted(set(range(1, want_n + 1)) - set(nums))
        extra = sorted(q for q in set(nums) if nums.count(q) > 1 or q > want_n)
        raise LayoutError(f"questions must run 1..{want_n} once each "
                          f"(missing {missing}, duplicated/extra {extra})")
    assert want_n in shapes
    head = LEVEL.gengo(level)["key_heading"]
    return restamp(body, level, want_n) + f"\n# {head}\n\n" + "\n\n".join(keys) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("test_dir", type=Path)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--normalize", action="store_true",
                      help="re-stamp an existing 言語知識・読解.md in place")
    mode.add_argument("--check", action="store_true",
                      help="report layout differences; write nothing")
    ap.add_argument("--allow-placeholders", action="store_true",
                    help="assemble unfinished fragments (layout testing only)")
    args = ap.parse_args()
    d = args.test_dir.resolve()
    level = LEVEL.declared_level(d) or LEVEL.level_of(d.name)
    target = d / TARGET
    try:
        if args.check:
            probs = layout_problems(target.read_text(encoding="utf-8"), level)
            for p in probs:
                print(f"  {d.name}: {p}")
            return 1 if probs else 0
        if args.normalize:
            text = normalize(target.read_text(encoding="utf-8"), level)
        else:
            text = assemble(d, level, args.allow_placeholders)
    except LayoutError as e:
        sys.exit(f"{d.name}: {e}")
    target.write_text(text, encoding="utf-8")
    print(f"wrote {target} ({level} layout)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
