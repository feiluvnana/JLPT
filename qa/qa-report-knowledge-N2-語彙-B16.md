# QA — 知識 語彙 B16 (Hajimete No.635–728, 就職／会社／仕事)

Fresh-eyes reviewer, one round, fixed directly. I read every example and every vi field against the Hajimete page
(PDF 121–135; p.127 is a copy of p.126). I grepped 問題1–6 of all 31 sittings by kanji, by reading and by verb or
adjective stem. Tool: `batch_tool.py stats|frames|lures|rebase|gate` (`lures --with 17` too). Final gate: 0 FAIL /
0 WARN / 0 REVIEW. The batch has 81 entries, 7 back-links (5 before QA), 21 ja live fixes and 1 vi live fix. The 13
numbers it drops are all live cards already (649 655 658 669 677 679 688 694 701 702 706 714 724).

## Findings and fixes

| # | Class | Entries | Fix |
| - | - | - | - |
| 1 | Wrong ruby | 作業 「｜六《ろく》｜時《とき》」; 好ましい and 意図 「｜彼《か》の」 | ｜六時《ろくじ》, ｜彼《かれ》 (`check_ruby_suspects` misses a split ruby) |
| 2 | Example contradicts its own gloss (rule 35) | 伝言 (a note left on the table, but the gloss says the message goes through another person); 受け取る (going to "receive" a bike you had borrowed) | 伝言 → 電話に出た妹に伝言を頼む; 受け取る → 窓口で保険証を受け取る (the 宅配便/留守 draft hit an SK 語彙 line) |
| 3 | Book frame copied | 資本 ① (person + body part + 資本 = ビジネスマンは体が資本), 御中 (company letter + 御中 on the address = the book's sentence), 件 (件 + お返事 = 先日の件、お返事が…) | 村にとって川の水が資本; 「青葉小学校 御中」 on an envelope; 駐車場の件で電話 |
| 4 | Scene shared with an open batch or a 読解 claim | 保留 = B17 v-0771 (buying a new machine put off until the budget is set); 認める ex1 (12/2014 読解 相手を認めつつ失敗) | 保留 → ゴールの判定; 認める ex1 → 計算ミスを認めて謝る |
| 5 | Sense with no example (known item 3) | 認める has 3 senses but only 2 examples; sense ① 許可 had none | Added ex3 (先生が辞書の使用を認めた) and its vi note. 精一杯 名: the book labels it 名/副 (p.123), so 「これが精一杯だ」 stays |
| 6 | Same-gloss pair left unlinked | じかに ↔ 直接: both mean "directly / trực tiếp" in the book, and 直接 is the key of じかに's own 7/2016 5-25. ガードマン ↔ 警備: the vi gloss "Người gác" still shared "gác" with 警備 "Canh gác" | Linked both ways with compares in both panes (2 new back-links: 直接 filled, 警備 appended). ガードマン now uses the book's gloss "Người bảo vệ", and its ja gloss no longer reads as clumsy (known item 4) |
| 7 | Gloss carries a headword (HW, rule 34) | 心得る 覚え (v-0060, known item 1); 肝心 欠か (v-0274); 特技 技 (演技); 件 用事 (急用), then 取り上げ (v-0517) | 身につけておく; なくてはならない; 得意なこと; 話に出ている事柄 |
| 8 | A live fix opens a new collision | 養う / 狙う / 効率的 「手に入れ」 (得る's gloss; GW つかむ↔狙う); 許す 「よいと答える」 (= 認める); 誤解 「理解」 (= 認識); 改めて 「もう一度、はじめから」 (= やり直す), then 「今に」 (B17 v-0805); 務める 「地位につき」 (= 就く) | Each one reworded against the current live text (`V16_live_meaning_fix.json`) |
| 9 | Gloss collides with B17 headwords (`--with 17`) | 対応 状況 (v-0777), 重役 / 就く 地位 (v-0729); 重役 会社 (GW 業績); 派遣社員 vi "công ty" (GW 大手) and "hợp đồng" (契約, the same reason as the v-o-ihan fix); 件 vi "vấn đề" (PAIR 焦点) | Reworded |
| 10 | vi compare is a rendering of the ja (known item 5) | **31 of 33** (26/28 entry compares + 5/5 back-links). Only 対応/応対 added anything of their own (the reversed-kanji note) | All 33 rewritten: Hán Việt first, then the Vietnamese trap: 依頼 Y LẠI ≠ "ỷ lại", 心得る TÂM ĐẮC ≠ "tâm đắc", 人材 ≠ only "người tài", 昇進/出世 (both "thăng tiến"), the 〜がい suffix, kun-read 大手/人手 |
| 11 | Unsourced or book-derived claim in prose | vi 大企業/大手 "Công ty nổi tiếng chưa chắc là 大手" (the book's sentence); 学歴 usage (the book's sentence); 民間 "Đối lập với 公務員"; 資本 ①② order did not match the gloss | Cut, or the order fixed |

## Confirmed as written

- official_count: 合同 1 (7/2012 6-32, headword), じかに 1 (7/2016 5-25, underlined; the precedent counts the
  underlined word and the key both). Everything else is 0. 支給 is not 7/2011 1-5 (that item is 至急). The other hits
  are stem-only or 問題6 sentences of other words (就く 7/2023 2-7 keys ふくし; 対応 12/2013 4-20 is a distractor and
  need not be cited).
- The 5 original back-links all fill empty live compares. `rebase` loses no text, and the 警備 append keeps the live
  compare whole.
- ガードマン/御中 (known item 4): 御中 keeps "Kính gửi", the book's word. ガードマン is fixed through the link (#6).
- Residual `lures`: 6 GW pairs on live entries that no B16 change touched (察する/誓う 「っきり」, 新築/南向き,
  飽きる/落ち込む, 講義/変更, 世の中/ニーズ). They are substring noise, not two-answer items.
- Left for B17: `lures --with 17` has one hit left, the PAIR 出世 (live) ↔ 目上 (B17) 「立場」. No B16 id is in it.

## Root cause

A one-author batch again mirrored the ja in the vi compares, as in 漢字 B9/B10 and 語彙 B15. Brief items 10–11 are
written for 漢字, and the 語彙 author read them as if they did not apply. The live fixes were checked only against the
word they removed, never for what the new wording collides with. `lures` flags a new collision only when a generated
item happens to pair the two entries. A ruby split as ｜六《ろく》｜時《とき》 gets past `check_ruby_suspects`.
