# QA — 知識 漢字 B17 (SK 967–1046, 48 entries, last SK batch)

Fresh-eyes reviewer; authored nothing. Rebased on live eb786cb (B16 merged).
Tools: `batch_tool stats|rebase|frames|lures|gate 漢字 17`. Final gate: 0 FAIL / 0 WARN / 0 REVIEW.

## Checks
- **Source**: all 48 cards read against SK 別冊 PDF 198–202 (p.65–69): id, kanji, 音/訓 rows,
  words, 特 readings (木綿, 浴衣). No defects. 腰 1014 and 令 1037 (OCR-missed) are right.
- **official_count**: all 0 — matches the inventory (every hit is a 問題2 distractor) and a grep for
  腰/令/命令 (one 12/2021 語彙 option, not 問題1/2). Every distractor hit is in `sources` with 「数えない」.
- **訳 / 綿 double-kanji words**: the reading items ask 言い訳 / 木綿. One answer each, and わけ/わた
  are excluded by `invalid_readings`.
- **Completeness** (live + B17): SK 1–1046 all carded, no duplicate ids or kanji. Of the 79 inventory
  `kx-` kanji, 68 are live `kx-` cards and 11 resolve to SK numbers (求640 憎833 柔762 材724 警673
  一4 統902 伝473 待188 判937 帰44). Nothing is uncarded.

## Findings (fixed in the batch files)
1. 募 example copied the scene of 語彙 v-o-kanyuu (町内の祭りの手伝いを勧誘). The first replacement
   hit the 12/2022 聴解 script (研究室の実験…募集), so it is now a local football team recruiting players.
2. 列 example shared its scene with v-0574 (a new game's release day). Now a queue at immigration.
3. 訳 example shared its scene with v-o-datou (an explanation for being late). Now an excuse for
   missing a deadline.
4. 捕 Hán Việt was given as BỔ, which made it look like 補. The dictionary reading is BỘ. Fixed in the
   meaning and the compare, and in the live 補 back-link (vi).
5. Missing links, added both ways with a compare in both panes:
   - 辺↔被 (same 7/2018 問題2-8 set)
   - 踊↔舞 (both glossed "múa" in vi)
   - 腰↔要 (腰's vi named 要 unlinked, and both carry Hán Việt YÊU)

   要's live compare (91/100) was compressed. All three 「」 compounds are kept; the dropped
   fragments only restated 要's own meaning or 主's gloss.
6. Pairs not linked:
   - 棒↔泥: the glosses don't collide and there is no shared 問題2 set.
   - 復/腹/複↔副: they share only the reading フク.
7. Mirroring: 9 of the 27 vi compares follow the ja contrast. 967 (復) was the bare mirror and was
   rewritten around PHỤC/PHÚC/PHỨC. The other 8 add Hán Việt or radical detail.

## Root cause
The author's frames check only flags shared predicates. Three scenes were reused with a different
predicate (a rule 39 module-scene grep would have caught them). The 捕 error came from a Hán Việt
reading chosen to match 補 rather than taken from the dictionary (rule 29).

## Not done / notes
- Scratch `漢字_B18.*` (19 kx) is stale. All 19 are already live, and `frames` still counts it as an open batch.
- `inventory/N2.md` names only 求 as kx→SK. The other 10 resolutions are visible only in the data.
