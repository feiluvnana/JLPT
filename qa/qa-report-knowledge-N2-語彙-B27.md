# QA — 知識 語彙 B27 (Hajimete No.1505–1546, 副詞 / 接続表現)

I reviewed this batch with fresh eyes and authored none of it. It got one round, with fixes made directly in the batch dir.
What I checked:
- Hajimete PDF pp.271–277 for all 42 headwords: pos, ＝/＋ words, VI line, the 👉 notes.
- Every example next to its note.
- Every ruby pair in context, against pykakasi. All the differences are correct kun/okurigana splits.
- The tool runs: `frames`, `lures`, `rebase`, `gate`, plus a hand scan of vi/ja gloss overlaps with same-pos live cards.

The batch was rebased on live after the B25 and B26 merges (1706 entries).

## Findings (all fixed)

| # | class | finding | fix |
| - | - | - | - |
| 1 | headword | v-1538 had the headword 「一方、」. The comma was there only to dodge the duplicate-headword WARN against live v-1165 一方. | Chose (a). v-1538 is dropped and No.1538 is folded into v-1165 as sense ③ (pos 名詞・接続詞, plus the conjunction example, a p.276 source note, and ja/vi meaning, usage and nuance). This is the brief's own rule: drop a number that is already a card. Option (b) can only clear the WARN by changing the gate, which needs the owner's OK. The merge tool cannot carry examples or sources into a live entry, so `QAV27_fold1165.py` runs after `merge`. The B27 back-link to v-1165 is removed. |
| 2 | HW in live gloss (`lures` missed) | さらに 「①そのうえ…」 carried その上, and its vi was identical to その上's ("Hơn nữa, thêm vào đó"). 単なる 「…ただそれだけの」 carried ただ. | V27 fixes for v-1079 and v-1111. 1528↔1079 linked in both panes, through the v-1079 back-link. |
| 3 | live fix defect | v-0285 and v-0848 swapped または for あるいは, which is open B28's headword (v-o-aruiwa). | Reworded without it. |
| 4 | stale live fix | The fixes to 深刻 (v-1270) and 重大 (v-o-juudai) replaced B25's ひどく text. That text holds no B27 headword. | Both fixes dropped, so B25's text stands. The other 19 fixes rebase cleanly. |
| 5 | gloss holds own/batch headword | ただ 「ただ、…」, ただし 「ただ、…」, そこで 「それで。…」, しかも 「そのうえ。…」 | Reworded. |
| 6 | gloss collision (unlinked) | 何しろ/どうせ ("Dù sao thì" in both), 何しろ/なぜなら 「理由を言うときの言葉」, 何とも/一切/一向に (少しも, "hoàn toàn không"), とても/一切/さっぱり, いかにも/さすが ("đúng là"), どうか/くれぐれも ("Xin hãy"), しかし/ただし ("tuy nhiên"), また/そればかりか (ほかにも) | Glosses reworded toward the book's VI line. 1509↔1524 and 1532↔1540 linked. Also linked the look-alikes それで↔それでも/それでは, ところが↔ところで, それとも↔それでは, with compares in both panes. |
| 7 | frame copy (book page) | いかに (いかに〜かがわかる), また (job title. また, art), なお (announcement. なお、〜てください), さて (さて、〜ましょう). それにしては reused p.276's neighbouring line (shop + 客が多い/少ない). | New examples, with each note rewritten in the same edit. Usage lines that copied the book phrase (〜でもある, 「なお、〜てください」, 「さて、〜しましょう」) are rewritten. |
| 8 | prose claim | いかに: 「あとに「わかる」「感じる」が続く」 is unsourced. しかし: 「だが」「けれども」 were called 同じ意味, but the book marks them ＋ (related). | Rewritten: 似た意味 / Từ liên quan. |
| 9 | translation | 10 of the 39 non-empty vi compares mirrored the ja (なぜか, 何とも, いかに, いかにも, そこで, なぜなら, そうはいっても, ただ, ただし, さて). | All 10 rewritten, leading with the Vietnamese trap. |
| 10 | second pass | Some of my own replacements hit new problems. The なお example matched 12/2013 script (なお、…終了の予定です). The さて example matched a 文法 card (長い冬が終わって). The また example had a 10-char span from 7/2012 (町として知られている). My そこで and また glosses carried the headwords 状況 and 別に. My shortened v-1079 vi back-link dropped 「さらに〜も」. | All replaced or restored, and the tools were re-run. |
| 11 | typo | どうせ vi "dằng nào" | "Đằng nào cũng" |

Kept as is:
- **lures HW, 25 hits.** All are substring false positives: 〜するとき/一度〜すると, かどうか, ところ＋が, そこ＋で, それ＋で.
- **Live 「。また、」 and the comparative より.** 「。また、」 is a sense separator that appears 197 times in live glosses, and より is the comparative particle (33 times). Neither is the conjunction or adverb sense.
- **なぜなら 「なぜかというと」.** This is the book's ＝ word, and なぜか is linked.
- **PAIR 削除/保存.** These are opposites, so not near-synonyms.
- **pos 接続詞.** New for this category; the gate accepts it.
- **official_count = 0 for all.** 問題1–6 hold only distractor hits (どうせ in 12/2012 問題5-24, とても in 12/2021 問題5-25), and both are recorded as 数えない. The conjunctions that appear in 問題7–9 blanks are not counted, which follows every live 語彙 card.

## Root cause
- `lures` HW does not match the kana reading of a kanji headword (その上 ↔ そのうえ) or 2-kana headwords (ただ). It also flags kana substrings without word boundaries.
- The author drafted the live fixes before the B25/B26 QA rewrites and did not check B28's headwords (brief item 9).
- Brief items 12 and 15 were applied only partly.

## Final state
- `gate 語彙 27` on live (1798 entries, after B30–32): 0 FAIL, 0 WARN, 0 REVIEW.
- `QAV27_fold1165.py --gate` (merge + fold + build + check, live 1798 → 1839): 0 FAIL, 0 WARN. The duplicate-headword WARN is gone.
- `lures`: only the 25 substring HW false positives and PAIR 削除/保存 remain.
- `rebase`: every back-link keeps the live compare whole, and all 21 fixes apply onto current text.
- One leftover: open B33's v-o-seizauranai copies B27 しかし's 「アプリを入れてみた」. That is for B33 to fix.
- The なお example was replaced after the last frames run, to get away from a 12/2025 市民マラソン script line. It was not re-scanned.
- Coverage: No.1–1546 are all v-NNNN cards, except No.1538, which is now a v-1165 source.
