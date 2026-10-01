# QA — 知識 語彙 B24 (Hajimete No.1291–1355, PDF 233–245)

Fresh-eyes reviewer; one round, fixed directly in the batch dir. 55 entries (54 drafted +
No.1354 物事, carded by QA). The 10 numbers not carded (1304 1307 1312 1330 1332 1333
1342 1346 1349 1351) are live cards already. Spot-checked against the page images: PDF
234, 242, 244 (24 entries: headword, reading, pos, VI gloss), the rest against the OCR.

Final: `gate` alone, `--with 23` and `--with 25` 0 FAIL / 0 WARN / 0 REVIEW; `lures --with 25`
clean, `--with 23` only B23's PAIRs; `frames` 0 PROV (one weak W+2 hit on 1353, not a copy).

## Findings (fixed)

| # | class | count | what |
|---|---|---|---|
| F1 | usage copies the book's example phrase | 13 ja + 14 vi | 飢えた子ども, 人柄がいい / 温厚な人柄, 穏やかな性質, 無口な人, 人見知りをする, おく病な性格, 大ざっぱな性格, 時間にルーズ, 短気な人, 要領がいい, 乗りがいい, 少子化が進む, vi 物の見方 |
| F2 | gloss carries another headword (rule 34) | 9 | 1294 豊か, 1300/1352/1355 物事, 1329 向く's own 向ける, 1340 ためらう / 恐れる (B25); live 対立 主張, 違反 守る, 運賃 乗る, 本体 主な (主に) |
| F3 | 物事 dropped for rule 34 | 1 card + 65 live glosses | 1354 carded; 65 live glosses reworded one by one against their examples (何か / あること / 仕事など / 全体 …, no ものごと). The 5 B23 glosses with 物事 and B23's own fixes for v-0106 / v-0872 → see merge steps |
| F4 | live fixes that read badly or still collided | 9 of the author's 18 | 品質 「出来やできの」 (doubled; and 品物 PAIR with 価格), 警備 rebuilt from the live text, ステップ, サングラス, 保つ, 農薬 「病気から防ぐ」, 養う; then GW/HW hits the rewording raised (法則, 貢献, 情緒, 姿勢) |
| F5 | examples | 3 | 1305 「この商店街は、かつて大きな工場があり」 (the street had a factory) → 商店街の近くには; 1329 「板に書いている」 → 黒板; 1354's first draft shared 家族に相談 with 漢字 k-0414 |
| F6 | markup / bare Japanese in vi | 4 | 1313 usage 「[少子化]対策」; (性質), (大), (ねばり) outside 「」 |
| F7 | vi pane mirrors ja | 10/14 compares, 9/9 back-link sentences | rewritten to lead with the Hán Việt + the Vietnamese trap (省 TỈNH ≠ tỉnh, 柄 BÍNH, 要領 ≠ "yếu lĩnh", エコ ≠ "môi trường", なれなれしい ≠ thân thiện …) |
| F8 | unsourced claims | 3 | vi 大まか "không chê", vi 正当を主張する (unidiomatic) → 無実を主張する, 開発's product sense: now cited (SK 語彙 p.98 「新商品を開発する」) |
| F9 | links missing | 5 | 支援↔援助, 環境↔周囲, 比較↔比較的 (live compares compressed, every 「」 form kept), 向く↔うつむく / そらす (12/2011, 12/2018, 12/2023 key 「下を向いて」 for うつむく) |

official_count re-derived (booklet + key.md, 4 options printed): 1305 かつて (12/2015 5-27),
1327 人柄 (7/2021 5-23), 1337 無口 (7/2015 5-27), 1339 おく病 (7/2017 5-25) at 1. A grep of
問題1–6 in all 31 sittings found no missed keyed hit (様々 / エネルギー / 調査 occur only as
distractors or in stems).

## Root cause

The author's usage lines were written from the Hajimete example (brief item 16 was not
applied); the rule-34 check skips one-kanji stems (向, 主, 乗, 守), so those needed a hand pass;
the vi compares were again drafted after the ja (items 10–11, 15).
