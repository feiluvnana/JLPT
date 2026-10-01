# QA — 知識 語彙 B14 (Hajimete No.480–552, 産業／学校／勉強)

Fresh-eyes reviewer, one round, fixed directly. Read every example against the Hajimete example on its
page (PDF 97–108), every vi field, every back-link and live fix. Tool: `batch_tool.py stats|frames|lures|rebase|gate`.
Final gate: 0 FAIL / 0 WARN / 0 REVIEW; 65 entries, 10 back-links, 9 ja live fixes.

## Findings and fixes

| # | Class | Entries | Fix |
| - | - | - | - |
| 1 | official_count missed | 妨げる | 7/2023 問題6-30 keys さまたげる (key 3). Changed 0 to 1 and added the source. Its example is not one of the misuse sentences |
| 2 | distractor hits not cited | 提案 (12/2020 4-15), ステップ (12/2015 4-19) | Added to `sources` with 「数えない」 |
| 3 | book frame copied | 推薦 (高校から大学に推薦してもらう), 志す (〜を志して努力を続ける), 取り上げる ② (子どもからゲームを取り上げた), 図 (図でわかりやすく説明する) | New scenes and predicates; vi example_notes rewritten |
| 4 | example contradicts the card's own compare | 意志 (「会社を辞めるという意志」 describes 意思) | New example about persistence |
| 5 | repeated scene in the batch | 提案 / 取り上げる ① (both 町内会 agenda) | 取り上げる ① changed to a magazine feature |
| 6 | frame hits introduced by the QA rewrites | 委員 (問題6 misuse 12/2017-30, 漢字 B13 掃除当番), 図 (B15 棚 assembly) | Rewritten until frames was clean (only 2-token hits with different predicates remain) |
| 7 | gloss prints its own headword | なじむ ja meaning 「なじんで…」 | Rewritten |
| 8 | gloss holds another headword's stem (rule 34/9) | 教養 「学んで」 (学ぶ is in this batch) | 「…などから得た」 |
| 9 | wrong ruby (split compound) | vi 修了証書 (｜書《かき》), 複数回答 (｜答《こたえ》), 根気強い (｜強《つよ》) | Whole-word ruby |
| 10 | Hán Việt traps | 生産 SINH SẢN, 意思 Ý TỨ: real, kept. 情緒 TÌNH TỰ: real, but "nghĩa khác hẳn" overstated it (tình tự also means feelings), so it was softened. 高等 CAO ĐẲNG: "động vật cao đẳng" really does mean higher animals, so the trap was moved to 高等学校 ≠ trường cao đẳng | — |
| 11 | thin vi nuance | 11 bare "Hán Việt X, như tiếng Việt" notes | Set to "". 法則 (≈ "phép tắc") and 旺盛 (reverse of "thịnh vượng") rewritten as real traps |
| 12 | vi prose | 基礎 compare cited its source ("Sách dịch…", rule 18); 提案 called 案 a "dạng ngắn"; 不可欠 had an etymology split; 教養 gloss "Giáo dưỡng" (upbringing in Vietnamese); 農家 usage repeated the book line | Rewritten |
| 13 | link padding | 現地↔現状 (they share only 現; the glosses do not collide) | Link and both compares cut. 現状↔現在 kept |
| 14 | missing link | 地道↔こつこつ (both glossed đều đặn / 目立たない努力) | Linked both ways. Back-link to live こつこつ: ja appended; vi live text trimmed by 9 characters (all 「」 forms kept) to fit the 180 cap |
| 15 | live fix | 農薬 「畑の…米」 (rice is not grown in 畑); 初歩 「学問などを身につける」 narrowed the meaning and collided with 教養/学力 | 「野菜や米などを…」; 「何かを習うときの…」 |

## Confirmed as written

- 志す: 7/2024 問題2-6 keys 志望 (options 希望/志望/指望/貴望). It counts for live 志望, not for 志す (oc 0).
- 著しい: 7/2021 1-2 is correct, and the nuance quotes the printed options exactly.
- Link clusters: 教わる/学ぶ/学習/学力 and 意志/意思/意欲 all have real gloss collisions, so they stay.
- The other 7 ja live fixes are sound.
- The 8 numbers not carded in the range (482, 487, 513, 519, 521, 537, 538, 545) are already live.
- `lures` PAIR 批評/鑑賞 is a false positive (it shares only 「作品など」). The 6 GW hits are on live pairs and pre-date this batch.

## Root cause

- `frames` cannot see a frame copied from the Hajimete page when the nouns are changed. It missed 4 copies again (it missed 18 in B13), so the read against the page stays a required step.
- `lures` does not catch a te-form stem (学んで ← 学ぶ) or a gloss that holds its own headword. Both were found by reading.
- The 問題6 keyed-word grep was not run on kana-only keys (さまたげる). It should search the reading as well as the kanji.
