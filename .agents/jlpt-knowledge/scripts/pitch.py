#!/usr/bin/env python3
"""Pitch-accent lookup over the vendored open dataset (references/pitch/).

The dataset is `references/pitch/accents.tsv.gz`: one row per (word, reading)
with the accent-drop positions UniDic 3.1.1 records for it (the UniDic
Consortium / NINJAL), filled for compounds UniDic's short-unit lexicon lacks
from Open JTalk 1.11's naist-jdic accent column. Both BSD-3-Clause —
`references/pitch/ATTRIBUTION.txt`, README.md.
None of `refs/` records pitch accent, so this is the ONLY source, and the rule
is: a word the dataset does not cover gets no line — never a guess. That is why
there is no する-verb / な-adjective / compound derivation here: each of those
is a rule-based guess, and the caller must pass the lexical headword instead.

Convention (the standard 東京 notation, same as NHK and 大辞林):
    0   平板 — low first mora, high to the end, the particle stays high
    1   頭高 — high first mora, drop after it
    n   drop after the n-th mora (n == mora count is 尾高: the particle drops)

API (dependency-free, stdlib only):
    lookup(word, reading="") -> list[int] | None
    readings(word) -> dict[str, list[int]]          # every reading the data has
    source(word, reading="") -> "unidic" | "openjtalk" | None
    morae(kana) -> list[str]
    NOTICE                                           # one-line credit text

CLI:
    python3 pitch.py 学校 がっこう          -> がっこう [0]  が|っ|こ|う
    python3 pitch.py 端                     -> every reading of 端
    python3 pitch.py --coverage             -> hit rate over the Hajimete N2 headwords
    python3 pitch.py --rebuild LEX_CSV [NAIST_CSV]
                                            -> regenerate accents.tsv.gz (README.md)
"""

from __future__ import annotations

import gzip
import re
import sys
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "references" / "pitch" / "accents.tsv.gz"
ROOT = HERE.parents[2]

NOTICE = ("Pitch accent: UniDic 3.1.1 (c) 2011-2021 The UniDic Consortium, (c) 2022 Teruaki Oka; "
          "Open JTalk 1.11 dictionary (c) 2008-2016 Nagoya Institute of Technology, "
          "(c) 2009 Nara Institute of Science and Technology. BSD 3-Clause licenses.")

# Small kana that fuse with the preceding mora. っ/ッ, ん/ン and ー are morae of
# their own; ヵ/ヶ are counters (か/こ), not glides, so they stand alone too.
_SMALL = set("ゃゅょぁぃぅぇぉゎャュョァィゥェォヮ")


def to_hira(s: str) -> str:
    """Katakana -> hiragana (ァ..ヶ and ヽヾ); everything else untouched."""
    out = []
    for c in s:
        o = ord(c)
        if 0x30A1 <= o <= 0x30F6 or o in (0x30FD, 0x30FE):
            out.append(chr(o - 0x60))
        else:
            out.append(c)
    return "".join(out)


def morae(kana: str) -> list[str]:
    """Split kana into morae: きゃ is one, がっこう is が|っ|こ|う, コーヒー is コ|ー|ヒ|ー."""
    out: list[str] = []
    for ch in kana.strip():
        if ch in _SMALL and out:
            out[-1] += ch
        else:
            out.append(ch)
    return out


def _norm_word(w: str) -> str:
    w = w.strip()
    w = re.sub(r"｜?([^｜《》]+)《[^》]*》", r"\1", w)   # tolerate furigana markup
    return w


@lru_cache(maxsize=1)
def _index() -> tuple[dict, dict]:
    """(exact, folded): word -> {reading: (drops, source)}; `folded` keys are hiragana-folded."""
    exact: dict[str, dict[str, tuple[list[int], str]]] = {}
    folded: dict[str, dict[str, tuple[list[int], str]]] = {}
    with gzip.open(DATA, "rt", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            word, reading, drops, src = line.rstrip("\n").split("\t")
            rec = ([int(x) for x in drops.split(",")], src)
            exact.setdefault(word, {})[reading] = rec
            folded.setdefault(to_hira(word), {}).setdefault(reading, rec)
    return exact, folded


def _records(word: str) -> dict[str, tuple[list[int], str]]:
    exact, folded = _index()
    w = _norm_word(word)
    return exact.get(w) or folded.get(to_hira(w)) or {}


def readings(word: str) -> dict[str, list[int]]:
    """Every reading the dataset lists for `word` (exact spelling, else kana-folded)."""
    return {r: list(v) for r, (v, _s) in _records(word).items()}


def _resolve(word: str, reading: str | None) -> tuple[str, tuple[list[int], str]] | None:
    rs = _records(word) if word else {}
    if not rs:
        return None
    r = to_hira((reading or "").strip())
    if r:
        return (r, rs[r]) if r in rs else None
    if len(rs) == 1:
        return next(iter(rs.items()))
    return None


def lookup(word: str, reading: str | None = "") -> list[int] | None:
    """Accent-drop positions for (word, reading), or None when the dataset does not know.

    1. (word, reading) exact, kana normalised (katakana == hiragana).
    2. Only when NO reading is given: word alone, if the dataset has exactly one
       reading for it. A given reading that the dataset does not list is None —
       applying another reading's accent would be a guess.
    Values that do not fit the reading's mora count are dropped (never drawn).
    Several values = the source lists several accepted accents, in its order.
    """
    hit = _resolve(word, reading)
    if not hit:
        return None
    r, (vals, _src) = hit
    n = len(morae(r))
    vals = [v for v in vals if 0 <= v <= n]
    return vals or None


def source(word: str, reading: str | None = "") -> str | None:
    """Which vendored source answered: "unidic" (primary) or "openjtalk" (fill), else None."""
    hit = _resolve(word, reading)
    return None if not hit else SOURCES[hit[1][1]]


SOURCES = {"u": "unidic", "n": "openjtalk"}


# ---------------------------------------------------------------- maintenance

_F = ("surface lid rid cost pos1 pos2 pos3 pos4 cType cForm lForm lemma orth pron "
      "orthBase pronBase goshu iType iForm fType fForm iConType fConType lType kana "
      "kanaBase form formBase aType aConType aModType lid2 lemma_id").split()
_KANJI = re.compile(r"[㐀-鿿豈-﫿々〆]")


def rebuild(lex_csv: str, naist_csv: str | None = None) -> int:
    """Regenerate accents.tsv.gz (README.md "How to update").

    Primary: UniDic's lex_*.csv, column aType. Fill (optional): Open JTalk's
    mecab-naist-jdic/naist-jdic.csv, column 14 ("drop/morae") — used ONLY for a
    (word, reading) UniDic does not list: UniDic is a short-unit dictionary, so
    compounds such as 図書館 / 初対面 / 手数料 are absent from it. Where both list
    a key they agree 96.0% of the time; UniDic wins every conflict.
    """
    import csv
    acc: dict[tuple[str, str], list[int]] = {}
    src: dict[tuple[str, str], str] = {}
    lemmas: dict[tuple[str, str], set[str]] = {}
    with open(lex_csv, encoding="utf-8") as f:
        for r in csv.reader(f):
            d = dict(zip(_F, r))
            if d["pos1"] in ("記号", "補助記号", "空白") or d["goshu"] == "記号":
                continue                       # symbols: not headwords
            if d["pos2"] == "固有名詞" and d["pos4"] != "国":
                continue                       # proper names, except country names (日本)
            if d["orth"] != d["orthBase"] or d["cForm"] not in ("*", "終止形-一般"):
                continue                       # dictionary form only
            if d["iForm"] not in ("*", "基本形") or d["fForm"] not in ("*", "基本形"):
                continue                       # no rendaku / sound-change forms (ばし for 箸)
            if d["kana"] != d["lForm"] and not _KANJI.search(d["orth"]):
                continue                       # kana spelling variants (おもいっきし)
            vals = [int(x) for x in d["aType"].split(",") if x.isdigit()]
            if not vals:
                continue                       # aType "*" = UniDic does not know
            key = (d["orth"], to_hira(d["kana"]))
            lst = acc.setdefault(key, [])
            lst.extend(v for v in vals if v not in lst)
            src[key] = "u"
            lemmas.setdefault(key, set()).add(d["lemma_id"])
    # A kana spelling shared by different words (はし = 箸/橋/端) would merge their
    # accents into one misleading list: such a key is dropped, so it answers None.
    for key, ids in lemmas.items():
        if len(ids) > 1 and not _KANJI.search(key[0]) and len(acc[key]) > 1:
            del acc[key]
            src[key] = "u"                     # still "answered" — the fill must not re-add it
    if naist_csv:
        with open(naist_csv, encoding="utf-8") as f:
            for r in csv.reader(f):
                if len(r) < 15 or r[0] != r[10] or r[9] not in ("*", "基本形"):
                    continue                   # dictionary form only
                if r[4] == "記号" or r[5] in ("固有名詞", "接尾", "数"):
                    continue                   # symbols, names, suffixes, numerals
                a = r[13].split("/")[0]
                key = (r[0], to_hira(r[11]))
                if not a.isdigit() or src.get(key) == "u":
                    continue                   # UniDic already answers this key
                lst = acc.setdefault(key, [])
                if int(a) not in lst:
                    lst.append(int(a))
                src[key] = "n"
    DATA.parent.mkdir(parents=True, exist_ok=True)
    body = ["# word\treading (hiragana)\taccent drops in source order (0 = 平板, n = drop after mora n)"
            "\tsource (u = UniDic 3.1.1 aType, n = Open JTalk 1.11 naist-jdic)\n",
            "# Derived data — see ATTRIBUTION.txt and README.md in this folder\n"]
    body += [f"{w}\t{k}\t{','.join(map(str, v))}\t{src[(w, k)]}\n" for (w, k), v in sorted(acc.items())]
    with open(DATA, "wb") as raw, gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, filename="") as g:
        g.write("".join(body).encode("utf-8"))    # mtime=0: byte-identical rebuilds
    _index.cache_clear()
    return len(acc)


def _hajimete_headwords() -> list[str]:
    """Best-effort headwords from the OCR'd Hajimete list: a 1-2500 number line, then the word."""
    p = ROOT / "refs" / "Hajimete" / "vocab_reference.md"
    lines = p.read_text(encoding="utf-8").splitlines()
    jp = re.compile(r"^[぀-ヿ一-鿿々ー〜]+$")
    heads: dict[int, str] = {}
    for a, b in zip(lines, lines[1:]):
        a, b = a.strip(), b.strip()
        if re.fullmatch(r"\d{1,4}", a) and 1 <= int(a) <= 2500 and jp.match(b) and len(b) <= 10:
            heads.setdefault(int(a), b)
    return list(dict.fromkeys(heads.values()))


def coverage() -> None:
    heads = _hajimete_headwords()
    known = [w for w in heads if readings(w)]
    single = [w for w in heads if lookup(w) is not None]
    n = len(heads) or 1
    print(f"Hajimete N2 headwords parsed from OCR: {len(heads)} unique (of 2500 in the book)")
    print(f"  in dataset (any reading):          {len(known):5d}  {100 * len(known) / n:5.1f}%")
    print(f"  word-only lookup answers (1 reading): {len(single):5d}  {100 * len(single) / n:5.1f}%")
    fill = [w for w in single if source(w) == "openjtalk"]
    print(f"    of which from the Open JTalk fill:  {len(fill):5d}")
    miss = [w for w in heads if not readings(w)]
    print("  sample misses (OCR noise, する/な forms, compounds):", " ".join(miss[:40]))


def _main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--rebuild":
        print(rebuild(argv[1], argv[2] if len(argv) > 2 else None), "rows ->", DATA)
        return 0
    if argv[0] == "--coverage":
        coverage()
        return 0
    word, reading = argv[0], (argv[1] if len(argv) > 1 else "")
    if reading:
        v = lookup(word, reading)
        print(f"{word} {reading} {v if v is not None else 'unknown'}  {'|'.join(morae(to_hira(reading)))}")
        return 0 if v is not None else 1
    rs = readings(word)
    if not rs:
        print(f"{word} unknown")
        return 1
    for r, v in rs.items():
        print(f"{word} {r} {v}  {'|'.join(morae(r))}")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
