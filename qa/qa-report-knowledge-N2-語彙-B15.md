# QA — 知識 語彙 B15 (Hajimete No.553–632, 試験／大学・大学院／パソコン(スマホ))

Fresh-eyes reviewer, one round, fixed directly. Every example was read against the Hajimete example on the same
page (PDF 109–119; 修了 PDF 103, 学習/教養 PDF 105). Every vi field, back-link and live fix was read too. I grepped
問題1–6 of all 31 sittings by kanji, by reading and by single-kanji stem (限, 迫, 勘, 訳, 仕上). Tool:
`batch_tool.py stats|frames|lures|rebase|gate`. Final gate: 0 FAIL / 0 WARN / 0 REVIEW. 66 entries, 8 back-links,
21 ja live fixes and 1 vi live fix.

The range drops 14 numbers, and each is already a live card: 554 579 584 586 587 589 590 592 595 600 608 614.

## Findings and fixes

| # | Class | Entries | Fix |
| - | - | - | - |
| 1 | Book frame copied (`frames` was clean) | 課題 ① (「Xの課題は…だった」 = 小論文の課題は…), フォント (「太い/細いフォントで…書く」), 貼り付ける (「コピーして…に貼り付ける」), 強調 (emphasis shown by bigger or bolder letters), 完成 (「何度も/十年かけて…ついに/やっと完成した」), 本番 (本番 + 緊張) | New scene and new predicate; vi example_notes rewritten |
| 2 | Official 問題6 misuse frame | 述べる (「店長が朝礼で今後の考えを述べた」 ≈ 7/2018 6-31 option 4 「社長は記者会見の演説で、今後の事業方針について述べた」) | 面接で理由を述べる |
| 3 | Module scene collision, found by the QA re-run | 本番 rewrite 1 hit 文法 g-wakeganai q1 (一度も練習…本番); 順序 hit v-o-aimai (説明書/部品) | 本番 → バレエの本番 (the ピアノ and 発表会 versions hit 文法 g-dakeni and g-nishiteha); 順序 → 発表の順序をくじで決める. `frames` is now left with one 2-token hit (面接/理由 in a 聴解 script, different predicate) |
| 4 | Odd or illogical example | 上書き保存 (「古い写真を上書き保存」), 順序 (「ベルが鳴った順序で案内」) | Rewritten |
| 5 | Gloss narrower than its own example (rule 35) | 明確 「言いたいことが迷わずに伝わる」 (taken from the book example; our example is about a fee) | 「誰が見ても、ほかの意味にとれないようす」. The 紛らわしい/確実/明確 compares were updated to match. The first wording 「はっきり…」 hit 抽象的 (GW) |
| 6 | Missing links (rule 4: the book glosses are alike) | 学問 "learning, study" ↔ 学習 "learning"; 完成 "completion / sự hoàn thành" ↔ 修了 "completion / hoàn thành" | Linked both ways, with compares in both panes (3 new back-links: 学習 appended, 教養 and 修了 filled) |
| 7 | Rewording that dodged a collision and lost the sense | 学問 ja 「…得る、深い理解」 (学問 is not "understanding"); vi avoided the book's "học vấn" | ja 「物事を深く調べて、筋道を立ててまとめたもの」; vi "Học vấn, sự học…". The first QA wording hit 提供/分野/学会 (PAIR) and was redone |
| 8 | Live vi gloss took another headword's book gloss | 教養 vi "Học vấn…" is Hajimete's VI line for 学問 (B14 QA's replacement for "Giáo dưỡng") | `V15vi_live_meaning_fix.json`: 「Học thức, vốn hiểu biết rộng về văn hóa」 |
| 9 | Uncounted hit not cited | 完成: 7/2012 問題5-25 (仕上げて → key 完成させて) | Added with 「数えない」 |
| 11 | Gloss prints a headword from the open batch B16 (flagged by the coordinator) | 学会 「成果」 (v-0717), 転送 「受け取っ」 (v-0656), live fix 計画 「手順」 (v-0725). 学問 「得る」 had already gone in fix 7 | 「わかったことを発表する会」; 「届いたものを、そのまま…送ること」; 計画 「段取り」. The 向き合う/専念 fixes that remove 取り組む are kept |
| 10 | vi compare mirrors the ja | 20 of 23 compares restate the ja contrast (only 段落, ほんの and わずか stand on their own). Most add one collocation | The 6 with a real Vietnamese trap were rewritten: 挑戦/取り組む (KHIÊU CHIẾN ≠ "khiêu chiến"), 確実/明確 (XÁC THỰC ≠ "xác thực"), 完成/終了 (HOÀN THÀNH covers 修了/完了 in Vietnamese). The other 14 were left as parallel-plus-collocation |

## Confirmed as written

- official_count 迫る 1 (12/2011 4-18 key 迫って), 必死 1 (12/2013 5-26, underlined), わずか 1 (12/2011 5-24, underlined).
  Everything else is 0. The extra hits are stem-only and need not be cited: 課題 in 7/2022 #15 and 7/2012 #14,
  手書き in 7/2021 #23, 挙げる in 7/2022 2-10, 限りない in 7/2015 #18, 勘定 (a different word).
- 完成 and 12/2023 5-22: the item tests the underlined 仕上げる and 完成させる is its paraphrase. No live card
  counts a 問題5 key option, so 0 stands.
- Live fixes (21 ja): each one removes a B15 headword or stem from a live gloss. Each still fits its card's
  examples. 批評 「それぞれ言う」 is fine. The leftover PAIR 批評/鑑賞 has distinct glosses; it is not a quiz risk.
- The remaining lures (GW 更新/違反, 新築/南向き, 肌/つや, 講義/変更, 分野/上達 「よって」) are not caused by
  B15's wording.

## Root cause

The author checked examples with `frames` only. Those copies are in the book's frame with new nouns, which the
tool cannot see (brief item 12). Collisions were solved by rewording a gloss instead of linking, even where
the book glosses two words alike. The vi compares were written as mirrors of the ja (brief items 10/11), not
from the Hán Việt.
