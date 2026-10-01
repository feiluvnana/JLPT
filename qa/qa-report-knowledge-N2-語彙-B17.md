# QA — 知識 語彙 B17 (Hajimete No.729–805, 上下関係／退職・転職／競技)

Fresh-eyes reviewer, one round, fixed directly. I read every example and every vi field against the Hajimete page
(PDF 136–150; 139 and 144–146 are これも覚えよう pages with no numbered headwords). I grepped 問題1–6 of all 31
sittings by kanji, by reading and by verb stem. Tool: `batch_tool.py stats|rebase|frames|lures|gate`, plus
`lures --with 18` and `gate --with 18`. Final gate: 0 FAIL, 0 WARN, 0 REVIEW. The batch has 62 entries. The 15
numbers it drops are all live cards already (730 732 742 751 758 769 770 774 775 779 786 790–793). After QA it
has 42 back-links (35 before), 18 ja live fixes (21 before) and 1 vi live fix.

## Findings and fixes

| # | Class | Entries | Fix |
| - | - | - | - |
| 1 | Wrong ruby | さすが 「｜前《ぜん》から思っていた」 | ｜前《まえ》 |
| 2 | Book frame copied (rule 12/13) | サポート (new member + 先輩 + サポートしてくれる = p.132), 独立 (独立して自分の店を開く = p.136), 身の回り (packing belongings before leaving = p.139), 勝負 (同点のまま延長 = 延長's line on p.143) | Replaced. The first replacements for いばる/身の回り/的確/独立 hit official 問題6 misuse sentences, 文法 cards or 漢字 k-0862, and 首になる hit open B18 v-0872 (工場閉鎖), so all were replaced again. Final `frames`: 0 hits |
| 3 | Example contradicts its own gloss (rule 35) | 重なる 「同じ種類の物事が続けて」 vs 疲れと寝不足が重なって; 攻める 「点を取ろうとする」 vs a board-game example | Glosses rewritten: 「いくつも続いたり、一度に起こったりする」 and 「相手に向かっていって、勝とうとする」 |
| 4 | Usage beyond the page (known item 4) | 技 (技を磨く/決める), 敵 (敵を作る, 敵に勝つ); テクニック's vi back-link quoted 技を磨く | 技: 「〜の技」「技をまねる」. 敵: 「敵と味方」「敵をやっつける」 (p.144, p.143). The back-link now quotes 大工の技 |
| 5 | Unsourced claim | vi 満足な〜 "thường đi với phủ định"; 恐縮ですが "mở đầu lời nhờ vả"; 攻める 「守りを攻める」 | Cut |
| 6 | Gloss collisions (rule 34/40) | 指導 「教えて…助ける」 (サポート, then PAIR ガイド and 上達). 退職 「職場」 (派遣社員, known item 1). With B18 (coordinator): お世辞 and 試みる 実際, 身の回り 持ち物 (then PAIR 誇り 身近), 技 身につけ (then 覚え) | Reworded until `lures` and `lures --with 18` show no hit on a B17 id. 退職 is reworded rather than linked, because a compare between 退職 and 派遣社員 would teach nothing |
| 7 | Live fix built on pre-QA B16 text | 改めて (v-0706): B17's 「いまごろになって」 collided with its own 今さら fix. 件 (v-0722) and 就く (v-0698) had no collision to fix. 重役 (v-0674) kept 立場 next to 目上. 認識 (v-0522) 「意味や事情」 equalled B16's 誤解 fix | Dropped the 706, 722 and 698 fixes, so B16's QA text stands. 重役 → 「経営を任されている、高い役の人」. 認識 → 「それがどういうものかを理解する」 |
| 8 | Links (known items 1–2) | 信頼↔依頼, 押し付ける↔引き受ける, 平社員↔新入社員/派遣社員, リストラ↔人事, 敬意↔敬う/尊重 | Linked both ways, with compares in both panes. Only the vi panes of 敬う, 尊重 and 依頼 needed compressing; every 「」 form is kept (rebase lists the 3 rewrites). 出世↔目上 is not linked: 出世's fixed gloss no longer contains 立場 or 地位, and 目上's ja compare (94/100) has no room |
| 9 | vi compare renders the ja (known item 5) | **33 of 35** entry compares (only 攻める and 重なる added anything of their own). **35 of 35** vi back-link sentences | All 70 rewritten: Hán Việt first, then the Vietnamese trap. Examples: 職 CHỨC = "việc làm" ≠ chức vụ; 伴 BẠN ≠ bạn bè; 出世 ≠ xuất thế; "cao cấp" covers both 上等 and 高価; 負 = thua as well as gánh; 敗れる/破れる are homophones |
| 10 | vi gloss off the book's line | 忠告 (the book has "cảnh cáo"), 戦う ("chiến đấu") | Now use the book's words |

## Confirmed as written

- official_count, checked hit by hit against key.md:
  - いばる 1 (7/2024 5-23).
  - 従う 1 (12/2017 2-7, key 従って; the kanji 従 is replaced by the other options).
  - 不平 2 (12/2017 5-24, 7/2024 5-25).
  - 溶け込む 1 (7/2024 4-19, key 2).
  - ハード 1 (12/2019 5-21).
  - やむを得ず 1 (12/2016 5-24): **ruling: it counts**. やむをえない is the same expression in another inflection
    (得ず/得ない). No やむを得ない card exists, and inflected keys already count elsewhere (溶け込んで, 従って).
- Stem-only or distractor hits correctly not counted: 退職 (12/2024 is 定年's 問題6 sentence), 立ち上げる (7/2013
  5-26 underlines みずから), 状況, 開会, 指導, 取り入れる, 観客, 的確, 信頼, 転職, 戦う, 破る, 負う, 恐縮, 反論.
- No missed keyed hit by kanji, reading or stem.
- Back-links: `rebase` loses no text except the 3 authorized compressions. 転勤 and 出世 append to B16's live text.
  The 21→18 ja fixes are rebased on the current live glosses.

## Merge steps

1. Merge with `batch_tool.py merge 語彙 17`, using `V17_live_meaning_fix.json` (18) and `V17vi_live_meaning_fix.json` (1).
2. B18's 案の定 back-link was drafted on B17's pre-QA text. `gate --with 18` gives 2 REVIEWs: it drops B17's
   compare, including 果たして. B18's QA must rebase it onto the merged B17 compare. Its vi now differs.
3. `make knowledge`, then `make check`.

## Root cause

- One author wrote both panes. Again the vi compares rendered the ja: brief items 10–11 are phrased for 漢字, and the
  語彙 author skipped them, as in B15 and B16.
- B17 was built on B16's pre-QA text, so 3 of its live fixes undid or duplicated B16 QA fixes. No tool compares a
  fix with the fix it replaces.
- `frames` cannot see a copy of another headword's line on the same page (勝負 vs 延長).
- `lures` without `--with` misses headwords from the next batch.
