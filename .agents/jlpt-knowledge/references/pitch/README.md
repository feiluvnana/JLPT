# Pitch-accent dataset (vendored, third-party)

Nothing in `refs/` records pitch accent, so the knowledge pages' accent line comes
from this folder and nowhere else. **A word it does not cover gets no line —
never a guess** (no する-verb, な-adjective or compound derivation; an entry
can carry a checked `pitch` override instead — `jlpt-knowledge/SKILL.md`).

| File | What |
| - | - |
| `accents.tsv.gz` | the data: 262,514 (word, reading) rows, 1.9 MB gzipped / 7.7 MB raw |
| `ATTRIBUTION.txt` | the credit line — printed in the footer of every page that draws a line |
| `LICENSE-UniDic.txt`, `LICENSE-OpenJTalk.txt` | the upstream license texts, verbatim (BSD-3 requires them to travel with the data) |

Reader: `.agents/jlpt-knowledge/scripts/pitch.py` (`lookup`, `readings`, `source`,
`morae`; `python3 pitch.py --help`).

## Sources and why these two

1. **UniDic 3.1.1** (`unidic-cwj-3.1.1.zip`, NINJAL / the UniDic Consortium,
   2022-09; sha256 `6f547a3e…c644ad310`), file `lex_3_1.csv`, column `aType`.
   Triple-licensed GPL / LGPL / **BSD-3-Clause**; this repo takes it under BSD-3.
   The accent annotation is NINJAL's own work — clean provenance. **Primary.**
   It is a short-unit lexicon, so compounds (図書館, 初対面, 手数料) are absent.
2. **Open JTalk 1.11** (`open_jtalk-1.11.tar.gz`, 2018-12; sha256
   `20fdc6ae…18de71f`), file `mecab-naist-jdic/naist-jdic.csv`, column 14
   (`drop/morae`). BSD-3 (Nagoya Institute of Technology; NAIST for the
   naist-jdic lexicon). **Fill only**: used for a (word, reading) UniDic does not
   list at all; UniDic wins every conflict. On keys both list they agree 96.0%.

Rejected: **Kanjium** `accents.txt` (labelled CC BY-SA 4.0) — its README does
not say where the accent numbers come from (kanjium issue #13 asks, unanswered),
and its author is quoted in yomitan issue #227 as "It's not listed due to
potential copyright issues, but it's from 2-3 legitimate sources" — unclear
provenance, which the knowledge rules forbid. It was used only as an outside sanity
check (below), never vendored.
NHK / 大辞林 scrapes: copyrighted, excluded.

## Format

UTF-8 TSV inside gzip, two `#` header lines, then
`word <TAB> reading(hiragana) <TAB> drops <TAB> source`:

```
橋	はし	2	u
端	はし	0	u
頭	あたま	2,3	u
図書館	としょかん	2	n
```

`drops` is the standard 東京 notation: `0` 平板, `1` 頭高, `n` = the pitch
falls after mora `n` (`n` = mora count is 尾高). Several values = the source
lists several accepted accents, in the source's order (not a frequency rank).
`source`: `u` UniDic, `n` Open JTalk.

What the build keeps (all in `pitch.rebuild()`): dictionary forms only (UniDic
`終止形-一般` / uninflected; naist `基本形`); no symbols, no proper names except
country names (日本); no rendaku/sound-change rows (ばし for 箸) and no kana
spelling variants (おもいっきし); a kana-only spelling shared by several UniDic
lemmas with different accents is dropped (はし alone answers None — pass 箸/橋/端).
Values larger than the reading's mora count are discarded at lookup.

## Verification (2026-09-30)

- 32/32 hand spot-checks against the standard accent: 箸 はし 1, 橋 はし 2,
  端 はし 0, 雨 1, 飴 0, 学校 0, 先生 3, 日本 にほん 2, 桜 0, 男 3, 花 2, 鼻 0,
  食べる 2, 見る 1, 行く 0, 赤い 0, 白い 2, 静か 1, 相談 0, 電話 0, コーヒー 3,
  神 1, 紙 2, 柿 0, 牡蠣 1, 弟 4, 心 2(,3), 頭 (2,)3, and from the fill 図書館 2,
  初対面 2, 手数料 2, お金 0.
- Outside check against Kanjium on shared keys: UniDic rows agree 99.2%, the
  Open JTalk fill 94.7% — so a fill-sourced line is the less certain one
  (`pitch.source()` tells a caller which it got).
- Coverage: `python3 pitch.py --coverage` over the Hajimete N2 headwords the
  OCR yields (1,383 of 2,500): 73% have an entry, 66% resolve word-only to one
  reading. Most misses are OCR-garbled headwords, する/な forms and set phrases.

## How to update

```bash
curl -LO https://clrd.ninjal.ac.jp/unidic_archive/cwj/3.1.1/unidic-cwj-3.1.1.zip   # 551 MB
curl -L -o open_jtalk-1.11.tar.gz \
  "https://sourceforge.net/projects/open-jtalk/files/Open%20JTalk/open_jtalk-1.11/open_jtalk-1.11.tar.gz/download"
unzip -j unidic-cwj-3.1.1.zip 'unidic-cwj-3.1.1/lex_3_1.csv'
tar xzf open_jtalk-1.11.tar.gz open_jtalk-1.11/mecab-naist-jdic/naist-jdic.csv
python3 .agents/jlpt-knowledge/scripts/pitch.py --rebuild lex_3_1.csv \
        open_jtalk-1.11/mecab-naist-jdic/naist-jdic.csv
```

The gzip is written with `mtime=0`, so the same inputs give a byte-identical
file. For a newer UniDic, update the version in `ATTRIBUTION.txt`, `NOTICE` in
`pitch.py` and this file, re-copy the license texts, re-run the spot-checks,
then `make knowledge` (the pages are not stamped with the dataset).
