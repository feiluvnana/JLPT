#!/usr/bin/env python3
"""The exam LEVEL of a test, and the per-level structure table it points at.

One owner for two things every other script used to hard-code for N2:

1. **Which level a test is.** Encoded in the folder name, the same way
   `origin.py` encodes imported/generated: a generated N2 paper keeps its bare
   date id (`20260917_1`), every other level carries a lowercase prefix
   (`n1-20261005_1`), and an import names its level in the slug
   (`imported-n2-2025-12`, `imported-n1-2025-12`). No prefix means N2 — so no
   existing folder was renamed. `test_spec.json` / `import_meta.json` carry a
   `"level"` too; the gate asserts the two agree.

2. **What that level's paper looks like.** `references/levels/<LEVEL>.json` is
   the machine-readable half of `jlpt-exam-structure/SKILL.md`: the 大問 list,
   item-count shapes per era, the 聴解 labels, the scoring bands, and the paths
   of that level's archive, pool, ledger and clip bank. The grader, the answer
   sheet, the model answer, the sampler, the profilers and the gate read it
   from here instead of restating 71 / 30 / 101 / 180.

A table's `status` says how far the level has got:

- ``calibrated`` — every structural field is filled AND the N2-style
  calibration (pools, bands, gate thresholds) exists. Only N2 today.
- ``structured`` — the structural fields are filled from that level's archive,
  so tests can be imported, rendered and graded; calibration is not done, so
  the gate runs the structural contracts and visibly `skip`s the rest.
- ``scaffold`` — paths declared, structure still null. Nothing can be built.

Adding a level is `python3 level.py --scaffold N1`, then filling the table from
the archive (README "Adding a level"). A number in a table is a measurement of
that level's `refs/` archive or an official jlpt.jp fact — never interpolated
from N2 (AGENTS.md §4).

Usage:
    python3 .agents/jlpt-exam-structure/scripts/level.py            # every level's status
    python3 .agents/jlpt-exam-structure/scripts/level.py N1         # one level: what is missing
    python3 .agents/jlpt-exam-structure/scripts/level.py --scaffold N3
"""

from __future__ import annotations

import argparse
import functools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LEVELS_DIR = Path(__file__).resolve().parent.parent / "references" / "levels"

LEVEL_NAMES = ("N1", "N2", "N3", "N4", "N5")
DEFAULT_LEVEL = "N2"
STATUSES = ("scaffold", "structured", "calibrated")

# The one place the GitHub repo is named. The answer sheet and the model answer
# fall back to the `audio` release when a clone has no 聴解.mp3; renaming the
# repo is this line plus a rebuild (GitHub redirects the old repo path, so a
# sheet built before a rename keeps streaming). Renamed JLPT-N2 → JLPT 2026-09-28.
REPO = "feiluvnana/JLPT"

_IMPORTED = "imported-"
_PREFIX_RE = re.compile(r"^(n[1-5])-")


class LevelError(LookupError):
    """A level with no table, or a table missing a field the caller needs."""


def level_of(test_id: str) -> str:
    """``N1``..``N5`` from a tests/ folder name. No level prefix means N2."""
    rest = test_id[len(_IMPORTED):] if test_id.startswith(_IMPORTED) else test_id
    m = _PREFIX_RE.match(rest)
    return m.group(1).upper() if m else DEFAULT_LEVEL


def declared_level(test_dir: Path) -> str | None:
    """The ``level`` a test's own spec/meta file records, if it records one."""
    for name in ("test_spec.json", "import_meta.json"):
        p = test_dir / name
        if p.is_file():
            try:
                lv = json.loads(p.read_text(encoding="utf-8")).get("level")
            except (ValueError, OSError):
                continue
            if lv:
                return str(lv).upper()
    return None


def generated_id(level: str, stem: str) -> str:
    """The folder name for a generated paper at `level` (`stem` = `20261005_1`)."""
    return id_prefix(level) + stem


def id_prefix(level: str) -> str:
    level = normalize(level)
    return "" if level == DEFAULT_LEVEL else level.lower() + "-"


def normalize(level: str) -> str:
    lv = str(level).strip().upper()
    if lv not in LEVEL_NAMES:
        raise LevelError(f"unknown level {level!r}: expected one of {LEVEL_NAMES}")
    return lv


def available() -> list[str]:
    """Levels that have a table on disk, in N1..N5 order."""
    return [lv for lv in LEVEL_NAMES if (LEVELS_DIR / f"{lv}.json").is_file()]


@functools.lru_cache(maxsize=None)
def load(level: str = DEFAULT_LEVEL) -> dict:
    level = normalize(level)
    p = LEVELS_DIR / f"{level}.json"
    if not p.is_file():
        raise LevelError(
            f"no structure table for {level}: {p.relative_to(ROOT)} does not exist — "
            f"run `python3 {Path(__file__).relative_to(ROOT)} --scaffold {level}` "
            f"and fill it from refs/JLPT_{level}_NEW/ (README 'Adding a level')")
    return json.loads(p.read_text(encoding="utf-8"))


def status(level: str) -> str:
    return load(level).get("status", "scaffold")


def is_calibrated(level: str) -> bool:
    return status(level) == "calibrated"


def has_structure(level: str) -> bool:
    return status(level) in ("structured", "calibrated")


def path(level: str, key: str) -> Path:
    """A repo path the table declares (`archive`, `pools`, `ledger`, …)."""
    rel = (load(level).get("paths") or {}).get(key)
    if not rel:
        raise LevelError(f"{level}.json declares no paths.{key}")
    return ROOT / rel


def archive_dir(level: str = DEFAULT_LEVEL) -> Path:
    """`refs/JLPT_<LEVEL>_NEW/` — the official past-paper archive for a level."""
    return path(level, "archive")


def _structure(level: str, section: str) -> dict:
    block = load(level).get(section)
    if not block:
        raise LevelError(
            f"{level}.json has no `{section}` structure yet (status "
            f"{status(level)!r}) — fill it from refs/JLPT_{level}_NEW/*/booklet.md")
    return block


def gengo(level: str = DEFAULT_LEVEL) -> dict:
    return _structure(level, "gengo")


def choukai(level: str = DEFAULT_LEVEL) -> dict:
    return _structure(level, "choukai")


def scoring(level: str = DEFAULT_LEVEL) -> dict:
    return _structure(level, "scoring")


def gengo_shapes(level: str = DEFAULT_LEVEL) -> dict[int, tuple[int, ...]]:
    """{last question number: per-大問 item counts} for every known era."""
    return {int(k): tuple(v) for k, v in gengo(level)["shapes"].items()}


def choukai_labels(level: str = DEFAULT_LEVEL, shape: int | None = None) -> list[str]:
    """The 聴解 answer labels (`問1-1` … `問5-2-2`) for one era's shape."""
    c = choukai(level)
    s = c["shapes"][str(shape or c["generated_shape"])]
    return ([f"問{m}-{i}" for m, n in enumerate(s["counts"], 1)
             for i in range(1, n + 1)] + list(s["mondai5"]))


def choukai_shapes(level: str = DEFAULT_LEVEL) -> dict[int, list[str]]:
    return {int(k): choukai_labels(level, int(k)) for k in choukai(level)["shapes"]}


def total_items(level: str = DEFAULT_LEVEL) -> int:
    """A generated paper's item count: 言語知識・読解 + 聴解 (N2: 71 + 30)."""
    return gengo(level)["generated_shape"] + choukai(level)["generated_shape"]


def audio_release_url(test_id: str) -> str:
    """Where a deployed sheet streams a test's 聴解.mp3 from (AGENTS.md §3)."""
    return f"https://github.com/{REPO}/releases/download/audio/{test_id}.mp3"


# ------------------------------------------------------------------ validation

def problems(table: dict) -> list[str]:
    """Everything wrong with one table, as human-readable lines (empty = fine).

    A ``scaffold`` table may leave the structure null; it may not declare a
    structure that does not tile. Anything at ``structured`` or above must be
    complete, because the grader and the sheet will trust it.
    """
    out: list[str] = []
    lv = table.get("level")
    if lv not in LEVEL_NAMES:
        return [f"level {lv!r} is not one of {LEVEL_NAMES}"]
    st = table.get("status")
    if st not in STATUSES:
        out.append(f"status {st!r} is not one of {STATUSES}")
    if table.get("id_prefix") != ("" if lv == DEFAULT_LEVEL else lv.lower() + "-"):
        out.append(f"id_prefix {table.get('id_prefix')!r} must be "
                   f"{'' if lv == DEFAULT_LEVEL else lv.lower() + '-'!r}")
    paths = table.get("paths") or {}
    for key in ("archive", "pools", "ledger", "choukai_bank", "choukai_draws"):
        if not paths.get(key):
            out.append(f"paths.{key} is missing")
    if paths.get("archive") and paths["archive"] != f"refs/JLPT_{lv}_NEW":
        out.append(f"paths.archive must be refs/JLPT_{lv}_NEW (AGENTS.md §3 naming)")

    need = st in ("structured", "calibrated")
    g, c, s = table.get("gengo"), table.get("choukai"), table.get("scoring")
    if need:
        for name, block in (("gengo", g), ("choukai", c), ("scoring", s)):
            if not block:
                out.append(f"status {st!r} but `{name}` is empty")
    if g:
        labels = g.get("mondai") or []
        n = len(labels)
        if not n:
            out.append("gengo.mondai is empty")
        for key, counts in (g.get("shapes") or {}).items():
            if len(counts) != n:
                out.append(f"gengo.shapes[{key}] has {len(counts)} counts for {n} 大問")
            if sum(counts) != int(key):
                out.append(f"gengo.shapes[{key}] sums to {sum(counts)}, not {key}")
        if str(g.get("generated_shape")) not in (g.get("shapes") or {}):
            out.append("gengo.generated_shape is not one of gengo.shapes")
        if not (0 < (g.get("goi_mondai") or 0) < n):
            out.append("gengo.goi_mondai must split the 大問 list in two")
        for i, m in enumerate(labels, 1):
            for f in ("code", "mondai", "name", "en", "part", "grader_name"):
                if not m.get(f):
                    out.append(f"gengo.mondai[{i}] has no {f}")
    if c:
        if str(c.get("generated_shape")) not in (c.get("shapes") or {}):
            out.append("choukai.generated_shape is not one of choukai.shapes")
        for key, shp in (c.get("shapes") or {}).items():
            got = sum(shp.get("counts") or []) + len(shp.get("mondai5") or [])
            if got != int(key):
                out.append(f"choukai.shapes[{key}] yields {got} labels, not {key}")
        if not c.get("mondai"):
            out.append("choukai.mondai is empty")
        for i, m in enumerate(c.get("mondai") or [], 1):
            for f in ("code", "name", "en", "grader_name"):
                if not m.get(f):
                    out.append(f"choukai.mondai[{i}] has no {f}")
    if s:
        secs = s.get("sections") or []
        if sum(x.get("max", 0) for x in secs) != s.get("max"):
            out.append("scoring.sections' max values do not sum to scoring.max")
        if not (0 < (s.get("pass") or 0) <= (s.get("max") or 0)):
            out.append("scoring.pass is outside 1..scoring.max")
    return out


def missing(level: str) -> list[str]:
    """What still stands between a level and being usable, for the status CLI."""
    t = load(level)
    todo = [f"table: {p}" for p in problems(t)]
    for key in ("archive", "pools"):
        rel = (t.get("paths") or {}).get(key)
        if rel and not (ROOT / rel).exists():
            todo.append(f"{key}: {rel} not on disk")
    for name in ("gengo", "choukai", "scoring"):
        if not t.get(name):
            todo.append(f"structure: `{name}` still null")
    return todo


def scaffold(level: str) -> Path:
    """Write a `scaffold` table for a new level; refuse to overwrite one."""
    level = normalize(level)
    p = LEVELS_DIR / f"{level}.json"
    if p.exists():
        raise LevelError(f"{p.relative_to(ROOT)} already exists")
    low = level.lower()
    table = {
        "level": level,
        "status": "scaffold",
        "id_prefix": id_prefix(level),
        "paths": {
            "archive": f"refs/JLPT_{level}_NEW",
            "pools": f".agents/exam-blueprint/references/pools/{level}.json",
            "ledger": f"logs/{level}/ledger.json",
            "choukai_bank": f"logs/{level}/choukai_bank.json",
            "choukai_draws": f"logs/{level}/choukai_draws.json",
        },
        "scoring": None,
        "gengo": None,
        "choukai": None,
        "_todo": (f"Fill scoring from jlpt.jp's 認定の目安/合否判定 for {level}; fill "
                  f"gengo/choukai (大問 list, one shapes row per era) from "
                  f"refs/JLPT_{level}_NEW/*/booklet.md and key.md; then set status "
                  f"to 'structured'. Test ids at this level start '{low}-'."),
    }
    p.write_text(json.dumps(table, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("level", nargs="?", help="show one level (default: all)")
    ap.add_argument("--scaffold", metavar="LEVEL", help="write a new scaffold table")
    args = ap.parse_args()
    if args.scaffold:
        p = scaffold(args.scaffold)
        print(f"wrote {p.relative_to(ROOT)} — status 'scaffold'. Next: README 'Adding a level'.")
        return 0
    levels = [normalize(args.level)] if args.level else available()
    for lv in levels:
        todo = missing(lv)
        print(f"{lv}: {status(lv)}" + ("" if todo else " — nothing missing"))
        for t in todo:
            print(f"  - {t}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
