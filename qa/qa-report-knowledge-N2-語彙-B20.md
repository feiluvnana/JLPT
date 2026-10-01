# QA — 知識 語彙 B20 (Hajimete No.964–1047, 自然・休日・旅行)

Fresh-eyes reviewer; authored nothing. One round, direct fixes. Final tool state:
gate 0 FAIL / 0 WARN / 0 REVIEW; lures 0 hits; frames 1 noun-only K hit (体育館/生徒 vs a
漢字 example; the predicate differs, so it is not a frame copy); 10-char 0.

Scope checked: all 75 entries against PDF 177–189 (ids, readings, pos, VI line). The 9 numbers
not carded (988, 999, 1001, 1010, 1016, 1021, 1030, 1034, 1037) are live. official_count:
昇る 1 (7/2022 問題2-6) and 引き返す 1 (12/2019 問題5-23) both confirmed; I grepped 問題1–6
of all 31 sittings for every headword and found no missed keyed hit.

## Findings and fixes

| # | Finding | Fix | Root cause |
| - | - | - | - |
| 1 | 12 wrong rubies: 日《にち》 for ひ ×7 (日の光, 日なた ×3, 運動会の日, 多い日, 祭りの日; 休みの日 dropped with its example), 床《とこ》, 街並《まちなみ》み, 数《かず》席, 五十｜人《ひと》, 常備｜薬《くすり》, やり方《ほう》 ×2 | corrected; also live 印《いん》 in v-0621 (inside a B20 fix) and v-0856 賞 (new live fix) → しるし | pykakasi readings; split rubies on compounds hide the error from a whole-word diff |
| 2 | 30 usage lines copied the Hajimete example phrase (広大な森林, 生物に関する調査, 夕焼けがきれいだ, 旅先から手紙を送る, 日本の各地を回る, 現在の位置を調べる …) | replaced in both panes | usage was built from the book sentence; rule 32 covers prose, and `frames` scans only examples |
| 3 | Example frames copied from the book or an official stem: だらだら, こもる ×2, ぐうぐう ex1, ばったり ex2, 便 (later flight), 出来事 (7/2013 「学校で…出来事」), 日光 (強い日光 clashed with 日差しが強い) | 8 examples and their notes rewritten | same as B12/B14 |
| 4 | "Sách ghi kèm" ×17 in vi usage names the source (rule 18); live uses "Từ liên quan" | replaced | not caught by `check_prose_citations` (it reads ja only) |
| 5 | vi compares: 16 of 22 restated the ja contrast (7 clause by clause, 9 with only a Hán Việt prefix) | 12 rewritten around the Vietnamese trap (THỔ ĐỊA ≠ ông thổ địa, "tình cờ" glosses four words, "dư dụ" is not Vietnamese …); 4 left (0974, 0975, 1022, 1025), since each adds its own content | AUTHOR_BRIEF 10/11/15 not applied in a one-author draft |
| 6 | Known lures: 予測 fix 「どうなる」⊃うなる; 敷金/賃貸 PAIR; 日光=日差し | 予測 → 「この先に起こることを、今のうちに推し量ること」; 敷金↔賃貸 and 日光↔日差し linked both ways | — |
| 7 | Dropped links whose glosses collide (the book glosses ばったり, たまたま, 思いがけず and 偶然 all as "tình cờ") | linked 風景↔情景, ばったり↔たまたま, ばったり↔思いがけず, 切り替える↔替える; shortened the live 替える, たまたま and 思いがけず compares to fit the band, keeping every 「」 form | — |
| 8 | B21 collisions: 休息/くつろぐ vs 休養 ("nghỉ ngơi", 体を休める); しばしば vs しきりに (何回も) | 休息 「活動をしばらくやめて、ひと息入れること」/"Nghỉ giải lao, dừng tay một lát"; くつろぐ "Thư giãn, thả lỏng thoải mái"; しばしば 「たびたび。間をおいてくり返し。」/"Thường, hay (xảy ra)". No back-link into B21 | — |
| 9 | v-0824 綿 fix said 「木からとれるわた」, which is wrong | 「わたの実からとれるわたや…」 | lure-avoidance edit changed the sense |
| 10 | Uncounted official distractor hits missing from sources | added 間もなく 12/2010 #20; ゆっくり 12/2015 #26 and 7/2025 #25 (「数えない」) | grep was done by kanji only |

Rebase: all back-links sit on the CURRENT live text, B19 included. 7 compares were shortened on
purpose (替える, たまたま, 思いがけず, 情景 ja/vi); none loses a 「」 form. 27 live fixes (26 + 賞);
賞 is a ruby-only change, which rebase reports as "already live".
