# QA — 知識 語彙 B26 (Hajimete No.1435–1504, 慣用句①気・心・胸 / ②頭・顔 / ③体)

Fresh-eyes reviewer; authored nothing. One round, fixed directly in the batch dir.
Checked: Hajimete PDF pp.261–270 (all 70 headwords, readings, pos, ＋/↔ words, VI line),
every example next to its note, every ruby pair in context (468 unique pairs),
`frames` / `lures` / `rebase` / `gate --with 25`.

## Findings (all fixed)

| # | class | finding | fix |
| - | - | - | - |
| 1 | ruby | 6 wrong: 店に入《い》る (はい), 心が通《とお》って (かよ), 先輩の年《ねん》 (とし), ダイエット中《なか》 (ちゅう), 手に入《い》る in vi usage (はい), 決めておいた分《ふん》 (ぶん); 口数《くちすう》 ×4 → くちかず; 怒《いか》る ×2 → おこる | corrected |
| 2 | frame copy (book p.) | 11 examples kept the Hajimete example's frame: 心が通う, 心を許す (〜にだけ), 胸をはずませる (〜を前に), 頭が痛い (living costs), 耳を傾ける (all listen to teacher), 口に合う (Japanese food / foreign guest), 手に入れる (long-wanted item), 手にする① (pretty item in a shop), 手につかない (thinking of a person), 肩を落とす (sibling fails a test), 足を引っ張る (my mistake drags the team) | new scenes, notes rewritten in the same edit |
| 3 | module scene | 3 replacements re-hit module cards (first flight = v-0832; residents vs plan = v-o-teikou; reception + name called = k-0686) | replaced again |
| 4 | usage copies book phrase | 優勝を手にする, 勉強が手につかない | 成功を手にする, 何も手につかない |
| 5 | prose claim | 耳を疑う 「聞いたことの前に『と聞いて』が来る」 (wrong, and its own example breaks it); vi 口に合う "người ăn là chủ thể" (subject is the food); vi 手を貸す "không cần chăm lo hết", 気を遣う "hay đi với khách…" (unsourced) | rewritten |
| 6 | book ＋/↔ missing | 馬が合う, ↔気が弱い (both panes); 気にかける, 心配り, 口を滑らす, 手に入る, 腕を上げる (ja pane) | added |
| 7 | HW in live gloss | 恐縮 「気をつかって」 and 配慮 「気を使う」 carry 気を遣う (kanji variant, so `lures` missed it) | V26 fix for v-1137. B25's QA adopted the identical v-0739 text, so it is dropped from V26 (B25 owns it) |
| 8 | gloss collision | 気が小さい↔おく病 ("Nhát gan" both), 腕が上がる↔上達, 手に入れる↔得る, 心を配る↔気配り, plus the brief's 弱気/短気/無口/気を抜く/腕/取り組む pairs | 10 back-links, compares compressed (rebase-checked) |
| 9 | translation | 15 of 19 distinct vi compare texts (37 of 47 entries) mirrored the ja | 15 rewritten, trap first |

Kept as is: 気が小さい = "nhát gan". The book prints EN "timid" and its own example
(気が小さいのに大きなことを言う) shows timidity. Its VI "nhỏ nhen, hẹp bụng" and ZH 小心眼
describe 心が狭い, so the vi compare warns against them. pos follows each phrase's head
word (〜い → イ形容詞, otherwise 動詞), which matches the 慣 rule. official_count is 0 for
all 70: every booklet hit is a 読解 passage, a 注, or a literal 頭が痛い option.

## Root cause
Item 12 (read every example against the book's example) and item 15 (vi compare written
first) were not applied. The author only spot-checked rubies. `lures` HW matches only
the exact headword spelling, so 気をつかう/気を使う went through.

## Final state
`gate 語彙 26 --with 25`: 0 FAIL, 0 WARN, 0 REVIEW. `lures`: no hits. `frames`: 0 `!!`, 0 PROV,
no 10-char span. The remaining 2-token overlaps are different scenes.
Merge order: B25 first. The back-links to v-1378 (弱気, B25's own card) and v-1339 (B25 back-link)
are built on B25's current text, so re-run `rebase` if B25 changes them again.
