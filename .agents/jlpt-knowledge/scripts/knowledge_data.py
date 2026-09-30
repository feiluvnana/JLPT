"""The knowledge module's data layer — ONE reader for the builder, the gate and the portal.

A category's data lives under `knowledge/<LEVEL>/` in one of two layouts
(jlpt-knowledge/SKILL.md §Files):

    single file   <stem>.json            shared Japanese material
                  <stem>.<code>.json     one language's prose, for EVERY language
    split         <stem>/<part>.json     the same pair, once per part (a 課, a
                  <stem>/<part>.<code>.json  topic, a range of words); `<part>`
                                         carries no "." and parts load in name order

A category uses one layout, never both. Ids are unique across the whole
category, so `related` may point into another part.

Language codes are never written here: a file's code is read off its name and
compared with the registry (langs.order()). Dependency-free (json + pathlib), so
`make serve` can import it for the portal's entry counts.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
KNOWLEDGE = ROOT / "knowledge"
CATEGORIES_JSON = Path(__file__).resolve().parents[1] / "references" / "categories.json"

sys.path.insert(0, str(ROOT / ".agents" / "exam-model-answer" / "scripts"))
import langs  # noqa: E402

INDEX_HTML = "index.html"


def levels() -> list[str]:
    return [k for k in json.loads(CATEGORIES_JSON.read_text(encoding="utf-8"))
            if not k.startswith("_")]


def categories(level: str) -> list[dict]:
    """The level's category specs, in display order ([] = no knowledge module yet)."""
    table = json.loads(CATEGORIES_JSON.read_text(encoding="utf-8"))
    return list(table.get(level, {}).get("categories", []))


def level_dir(level: str) -> Path:
    return KNOWLEDGE / level


def page_path(level: str, stem: str) -> Path:
    """The category page. For a split category it is a small list of the parts;
    the cards live on one page per part (part_page_path)."""
    return level_dir(level) / f"{stem}.html"


def part_page_path(level: str, stem: str, part: str) -> Path:
    """A split category's page for one part: `<stem>/<part>.html`, beside its data."""
    return level_dir(level) / stem / f"{part}.html"


@dataclass
class Part:
    """One shared file and the language files beside it."""
    name: str                       # "" for the single-file layout
    shared: Path
    lang_files: dict[str, Path] = field(default_factory=dict)   # active codes only


@dataclass
class Category:
    level: str
    spec: dict
    parts: list[Part] = field(default_factory=list)
    layout: str = "none"            # single | split | none | both
    stray: list[Path] = field(default_factory=list)    # language files for an inactive code
    orphan: list[Path] = field(default_factory=list)   # language files with no shared file

    @property
    def stem(self) -> str:
        return self.spec["stem"]

    @property
    def kind(self) -> str:
        return self.spec["kind"]

    def sources(self) -> list[Path]:
        """Every data file the built page is made from — what it stamps."""
        out = []
        for p in self.parts:
            out.append(p.shared)
            out += [p.lang_files[c] for c in langs.order() if c in p.lang_files]
        return out


def category_page_sources(cat: "Category") -> list[Path]:
    """What a SPLIT category's list page is made from: every part's shared file
    (it prints each part's label and entry count). Single layout: cat.sources()."""
    return [p.shared for p in cat.parts]


def part_page_sources(cat: "Category", part: "Part") -> list[Path]:
    """What one part page is made from: its own shared + language files, plus the
    other parts' shared files — a `related` link into another part prints that
    entry's headword (and, for a guide, the primary language's title)."""
    out = [part.shared] + [part.lang_files[c] for c in langs.order() if c in part.lang_files]
    for p in cat.parts:
        if p is part:
            continue
        out.append(p.shared)
        if cat.kind == "guide" and langs.primary() in p.lang_files:
            out.append(p.lang_files[langs.primary()])
    return out


def _split_name(name: str) -> tuple[str, str | None] | None:
    """'01.json' -> ('01', None); '01.xx.json' -> ('01', 'xx'); else None."""
    bits = name.split(".")
    if len(bits) == 2 and bits[1] == "json":
        return bits[0], None
    if len(bits) == 3 and bits[2] == "json":
        return bits[0], bits[1]
    return None


def locate(level: str, spec: dict) -> Category:
    stem = spec["stem"]
    d = level_dir(level)
    cat = Category(level=level, spec=spec)
    active = set(langs.order())

    single = []
    if d.is_dir():
        for f in sorted(d.iterdir()):
            sp = _split_name(f.name) if f.is_file() else None
            if sp and sp[0] == stem:
                single.append((f, sp[1]))
    split = []
    sub = d / stem
    if sub.is_dir():
        for f in sorted(sub.iterdir()):
            sp = _split_name(f.name) if f.is_file() else None
            if sp:
                split.append((f, sp[0], sp[1]))

    has_single = any(c is None for _, c in single)
    has_split = any(c is None for _, _, c in split)
    cat.layout = ("both" if has_single and has_split else "single" if has_single
                  else "split" if has_split else "none")

    groups: dict[str, list[tuple[Path, str | None]]] = {}
    for f, code in single:
        groups.setdefault("", []).append((f, code))
    for f, part, code in split:
        groups.setdefault(part, []).append((f, code))

    for name in sorted(groups):
        files = groups[name]
        shared = next((f for f, c in files if c is None), None)
        langs_here = [(f, c) for f, c in files if c is not None]
        if shared is None:
            cat.orphan += [f for f, _ in langs_here]
            continue
        part = Part(name=name, shared=shared)
        for f, c in langs_here:
            if c in active:
                part.lang_files[c] = f
            else:
                cat.stray.append(f)
        cat.parts.append(part)
    return cat


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_entries(cat: Category) -> tuple[list[dict], dict[str, dict[str, dict]]]:
    """(entries in display order, {code: {id: prose}}), unvalidated.

    Each entry gains `_part` (its part name) so a message can say where it lives.
    The gate validates; the builder trusts the gate and skips what it cannot read.
    """
    entries: list[dict] = []
    prose: dict[str, dict[str, dict]] = {c: {} for c in langs.order()}
    for p in cat.parts:
        try:
            doc = read_json(p.shared)
        except (OSError, json.JSONDecodeError):
            continue
        for e in doc.get("entries", []) if isinstance(doc, dict) else []:
            if isinstance(e, dict):
                entries.append({**e, "_part": p.name})
        for c, f in p.lang_files.items():
            try:
                lp = read_json(f)
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(lp, dict):
                for k, v in lp.items():
                    if isinstance(v, dict):
                        prose[c].setdefault(k, v)
    return entries, prose


def summary(level: str) -> dict[str, int]:
    """{stem: entry count} for every category of the level — the portal's counts."""
    return {spec["stem"]: len(load_entries(locate(level, spec))[0])
            for spec in categories(level)}


# --- book order: the ONE order a category's cards are listed in ---------------
# jlpt-knowledge/SKILL.md §Book order. categories.json `order` says how a key is
# read: "book" = the entry's shared `book` field [section, lesson, item(, split)];
# "id" = off the id through `order_series`. The builder sorts every page by it and
# the gate FAILs an entry without a key and a page listed in any other order.
INVENTORY_DIR = CATEGORIES_JSON.parent / "inventory"
_INV: dict[str, dict] = {}
NO_KEY = (99, 0, 0, 0, 0, "", "", "")      # sorts last; the gate FAILs every such entry


def inventory(level: str) -> dict:
    """references/inventory/<LEVEL>.json ({} when the level has none), read once."""
    if level not in _INV:
        p = INVENTORY_DIR / f"{level}.json"
        try:
            _INV[level] = read_json(p) if p.is_file() else {}
        except (OSError, ValueError):
            _INV[level] = {}
    return _INV[level]


def inventory_rows(level: str, stem: str) -> list[dict]:
    rows = inventory(level).get(stem, {})
    rows = rows.get("entries", []) if isinstance(rows, dict) else []
    return [r for r in rows if isinstance(r, dict) and isinstance(r.get("id"), str)]


def valid_book(v) -> bool:
    """[section, lesson, item] or [section, lesson, item, split]: ints, section/item/split >= 1."""
    return (isinstance(v, list) and len(v) in (3, 4)
            and all(isinstance(x, int) and not isinstance(x, bool) for x in v)
            and v[0] >= 1 and v[1] >= 0 and v[2] >= 1 and (len(v) == 3 or v[3] >= 1))


def book_group(spec: dict, book) -> str | None:
    """The `group` label a book key implies (categories.json `book_sections`)."""
    if not valid_book(book):
        return None
    fmt = (spec.get("book_sections") or {}).get(str(book[0]))
    if not isinstance(fmt, str):
        return None
    lesson = book[1]
    letter = "ABCDEFGHIJ"[lesson - 1] if 1 <= lesson <= 10 else "?"
    return fmt.replace("{n}", str(lesson)).replace("{L}", letter)


def _gojuon(s: str) -> str:
    s = plain(s or "")
    return "".join(chr(ord(c) - 0x60) if 0x30A1 <= ord(c) <= 0x30F6 else c for c in s)


def order_keys(spec: dict, entries: list[dict], level: str) -> dict[str, tuple]:
    """{id: sortable key} for every entry that HAS a book-order key (see module note)."""
    out: dict[str, tuple] = {}
    how = spec.get("order")
    ids = [e for e in entries if isinstance(e.get("id"), str)]
    if how == "book":
        for e in ids:
            b = e.get("book")
            if valid_book(b):
                out[e["id"]] = (0, *b, *([0] * (4 - len(b))), "", "", e["id"])
        return out
    if how != "id":
        return out
    series = [s for s in spec.get("order_series") or [] if isinstance(s, str)]
    inv = {r["id"]: i for i, r in enumerate(inventory_rows(level, spec["stem"]))}
    pats = [(i, re.compile(s)) for i, s in enumerate(series) if s != "inventory"]
    inv_rank = series.index("inventory") if "inventory" in series else None
    loose = []                                  # (series rank, entry): unnumbered ids
    for e in ids:
        eid = e["id"]
        for i, rx in pats:
            m = rx.fullmatch(eid) or (rx.match(eid) if not rx.groups else None)
            if m:
                if rx.groups:
                    out[eid] = (i, int(m.group(1)), 0, 0, 0, "", "", eid)
                else:
                    loose.append((i, e))
                break
        else:
            if inv_rank is not None and eid in inv:
                out[eid] = (inv_rank, inv[eid], 0, 0, 0, "", "", eid)
    # unnumbered: under their group label, groups in the order of their first numbered
    # entry (a label no numbered entry uses comes after), then by reading in gojūon order
    first: dict[str, tuple] = {}
    for e in ids:
        k, g = out.get(e["id"]), e.get("group")
        if k and isinstance(g, str) and (g not in first or k < first[g]):
            first[g] = k
    rank = {g: n for n, g in enumerate(sorted(first, key=lambda g: first[g]))}
    rk = spec.get("reading")

    def _say(e):   # 漢字 has no reading field: its first 音 (else 訓) reading sorts it
        if rk:
            return str(e.get(rk, ""))
        for f in ("on", "kun"):
            v = e.get(f)
            if isinstance(v, list) and v:
                return str(v[0])
        return ""
    for i, e in loose:
        g = e.get("group") if isinstance(e.get("group"), str) else ""
        out[e["id"]] = (i, rank.get(g, len(rank)), 0, 0, 0, g if g not in rank else "",
                        _gojuon(_say(e)), e["id"])
    return out


def book_sorted(spec: dict, entries: list[dict], level: str) -> list[dict]:
    """`entries` in book order (stable; an entry without a key goes last)."""
    keys = order_keys(spec, entries, level)
    return sorted(entries, key=lambda e: keys.get(e.get("id"), NO_KEY))


# --- plain text: what the bands count and the search box matches -------------
FURIGANA = re.compile(r"｜?([^｜《》]+?)《([^》]*)》")


def plain(text: str) -> str:
    """Furigana markup stripped: ｜漢字《かんじ》 -> 漢字. What a band counts."""
    return FURIGANA.sub(r"\1", text or "").replace("｜", "").replace("**", "")


def readings(text: str) -> str:
    """Only the ruby readings, joined — so a search for かんじ finds 漢字."""
    return " ".join(m.group(2) for m in FURIGANA.finditer(text or ""))


# --- source-sha stamps --------------------------------------------------------
# The same `<!-- src_sha: <name>=<12-hex sha1> -->` format build_booklet.py
# stamps into every exam page (exam-app), so one regex reads them all. `<name>`
# is the path relative to knowledge/<LEVEL>/ because a split category's part files
# share base names across categories ("01.json").
def source_sha(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()[:12]


def stamp_name(level: str, path: Path) -> str:
    return path.relative_to(level_dir(level)).as_posix()


def src_sha_comments(level: str, sources: list[Path]) -> str:
    return "".join(f"\n<!-- src_sha: {stamp_name(level, p)}={source_sha(p)} -->\n"
                   for p in sources if p.is_file())


STAMP = re.compile(r"<!-- src_sha: (.+?)=([0-9a-f]{12}) -->")


def read_stamps(page: Path) -> dict[str, str]:
    return dict(STAMP.findall(page.read_text(encoding="utf-8")))
