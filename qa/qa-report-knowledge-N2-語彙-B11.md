# QA — 知識 語彙 batch 11 (Hajimete No.242–310)

Fresh-eyes reviewer (wrote none of the batch). One author wrote both panes. Checked against live at 289a4c9 (B10 merged).
63 entries; 6 numbers dropped because they are already live cards: 262 あらかじめ, 269 起床, 295 いったん, 299 削る, 301 調節, 309 用心.
13 back-links (12 from the author plus 買い換える). 9 live meaning fixes.

## Checks run
- `batch_tool stats / frames / lures / rebase / gate`, before and after the fixes.
- Hajimete PDF pp.53, 54, 56, 60, 62 and 64 (book pp.52–63) checked against about 30 entries: ids, readings, pos, senses and VI lines. Also p.153, to confirm 欠かせない is not a headword of its own.
- official_count recounted hit by hit in booklet.md + key.md:
  - 日中 1 (7/2012 問題5-26)
  - 欠かす 2 (7/2018 問題4-19 key 4 「欠かさない」; 12/2021 問題5-24 underlined 「欠かせない」)
  - 何度も 3 (問題5 keys in 12/2010-24, 7/2016-23 and 7/2022-22)
  - ほぼ 1 (7/2011 問題5-26)
- Grep for missed keyed hits across all 63 headwords found none. The near-misses do not count:
  - 7/2023 問題7-39: 欠かせない is a distractor; the key is ほかならない.
  - 7/2013 問題7-41: 欠か〜 is printed in all four options.
  - 12/2014, 7/2015, 12/2012 and 7/2024: 問題8 cards.
- B10 QA's fixes to the 価格 and 重ねる glosses are live. Confirmed.

## Findings and fixes
| # | Finding | Fix | Root cause |
| - | - | - | - |
| 1 | Broken ruby `｜一｜気《いっき》`, `｜至｜急`, `｜世｜間知` (back-link vi) and `｜日｜程`, `｜植｜物` (vi). They render a literal ｜ inside the ruby. | Changed to whole-word ruby. | The gate and the tool have no check for a ｜ inside a ruby base. Proposal: `check_ruby_suspects` should FAIL on `｜[^《]*｜[^《]*《`. |
| 2 | Four vi back-links (のんびり, さっぱり, 世間, さっさと) trimmed live text when appending fit under the 180 cap. 備える vi dropped its example list. | Changed to live + appended sentence. 備える and さっさと needed only small trims, and the example list is kept. | Rule 5 says "append, never rewrite". The author compressed by habit. |
| 3 | Examples: 現在 and 先ほど used 駅前 (a saturated scene). 年代 used 料理教室 (saturated). 今後 shared 毎月+開く with the 12/2013 問題6 催促 misuse sentence. 合間 shared 授業+宿題 with the 12/2023 暮れ misuse sentence. 周辺 shared 工場の事故 with the 7/2023 misuse sentence and a live card. 整える ex1 shared 試合/選手 with 7/2018 演説 and two cards. 寄り道 had a PROV span. | Replaced all eight, plus their vi example_notes, and re-ran frames. The three remaining `!!` lines (乳製品, 欠かす ×2) share only nouns, with different predicates, so they are not copies. | Saturated scenes and `!!` hits were not cleared before hand-off. |
| 4 | あと lure. The author's live fixes changed gloss あと→後, which still prints the word あと in kanji. The あと quiz's distractor ろくに showed 「（後に「ない」が来て）」. 一切's gloss and live 同士 「名詞の後に付いて」 had the same problem. | Five live fixes reworded to avoid both あと and 後. 同士 added to the fix file. ろくに and 一切 glosses lose the parenthesis. | The LURE/HW check matches the kana form only. Proposal: also match the kanji spelling of a kana headword (あと = 後). |
| 5 | 現在's gloss contained B11 headword 過去. | Changed to 「今という時。今の時点。」 | Same as 4. The author fixed 過去 in v-0058 but missed its own entry. |
| 6 | 年中 usage gave 「一年中」 as the noun use, but that is a different word. | Changed to 「年中無休」 (Hajimete p.54's own (名) example), both panes. | A sense not checked on the page. |
| 7 | 周囲 vi nuance claimed that Vietnamese "chu vi" has only sense ①. This was the author's own judgement, unsourced. | Cut (`""`). | Rule 9. |
| 8 | Lures: 見出し shared 文章 / đoạn văn with 削除 (PAIR with 文句). すれ違う shared 反対 / đi ngược with 逆らう. | Glosses reworded. lures now shows 0 PAIR, and the 5 GW lines left are all live-only. | Not run to zero before hand-off. |
| 9 | 替える ↔ 買い換える (B10, now live): the glosses collide (「今…使って…物をやめて」). | Linked both ways, with a compare in both panes. 買い換える added as back-link #13. | Link-at-merge pair. |
| 10 | 乳製品's gloss 「牛乳から作った食品。チーズやバターなど」 restated the 7/2022 問題6 生じる misuse sentence with the right verb put back. | Changed to 「牛などの乳を原料にした食品。」 | Rule 32/39 applied to prose too. |

## Checked and kept
- 間 (ま) is a one-kanji headword, and 23 glosses contain 間. Its current quiz draw (評価 / きっかけ / 独り言) prints no 間. The generator already keeps 夜間, 年間 and 合間 out because they share the kanji. Residual risk: とっさ 「ほんの短い間」 if a future draw picks it. check_meaning_lures would WARN on it.
- 売り買い ↔ 貿易 is a coverage link. Its compare is fine in both panes.
- 食物's Hán Việt "thực vật" really is a Vietnamese word with another meaning, and the note agrees with Hajimete's VI line "đồ ăn".
- vi compares are close to the ja compares, but each states a fact-for-fact contrast. The usage fields are written independently (Hán Việt, collocations). No translation finding.
- さっぱり and 備える ja back-links had to be compressed to fit the 100 cap. The rebase shows the lost words are wording only, and every contrast is kept.

Final gate: 0 FAIL, 0 WARN, 0 REVIEW. lures: 0 LURE / HW / PAIR. frames: 0 PROV.
