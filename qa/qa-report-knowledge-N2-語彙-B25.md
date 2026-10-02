# QA — 知識 語彙 B25 (Hajimete No.1356–1434, 第11章 §2–§5)

Fresh-eyes reviewer, one round, fixed directly in the batch dir. The entry gate was green: 0 FAIL, 0 WARN, frames and lures clean. A green gate did not mean a clean batch.

**Scope.** 66 cards. The 13 dropped numbers are all already live: 1357, 1362, 1379, 1393, 1396, 1397, 1399, 1412, 1413, 1420, 1427, 1428, 1431. Every card was read against PDF pages 246–258 (headword, reading, pos, ＋/↔ and the VI line). Back-links went from 11 to 14 and live fixes from 14 to 21, all rebased onto the live text at a8605f4. The exit gate is 0 FAIL / 0 WARN / 0 REVIEW, and frames and lures are clean.

## Findings → root cause

| # | Finding | Fix | Root cause |
| - | - | - | - |
| 1 | Two keyed hits were missed. 7/2013 問題4-19 keys 「つらくて」. 12/2016 問題5-24 keys 「しかたない」. Both cards had `official_count` 0. | Both counts set to 1. The cited item and the 7/2019 問題5-24 distractor (数えない) went into `sources`. | The author grepped by headword form only, so inflected keys (つらくて, しかたない) were missed. That is brief item 13. |
| 2 | つらい's example was the 7/2013 official scene (parting from friends → つらい). | Replaced. | No `frames` check against keyed 問題4 stems. The tool covers 問題6 only. |
| 3 | 11 more examples copied a Hajimete frame: 1376, 1377, 1408, 1410×2, 1417, 1419, 1423, 1424, 1430, 1434. The new 1430/1419/1376/1377 drafts then hit module scenes and a 問題6 misuse sentence, so they were replaced again. | Replaced, and every vi note was rewritten in the same edit. | Item 12: `frames` cannot see the book page. |
| 4 | Glosses carried other headwords in kana or in inflected form. Fixed in B25 glosses: ものごと ×3 (物事), はなれ (離れる), いきおい (勢い), たよる (頼る), かなわ (かなう), あつかい (扱う), 「何度も」, ただ/ところが (B27), and 1389, which repeated its own しかたがない. Missed in live glosses: 許す (かまわない), きっぱり (ためらわず), 苦痛 and 耐える (つらさ), 静まる (おだやか), 深刻 and 重大 (済まない = すまない), オーダーメイド (「その品」). | Rewritten. The live ones were added as fixes. | `lures` HW checks only kanji headwords and dictionary forms. Kana headwords, inflections and readings pass through it. |
| 5 | Rule-40 near-synonyms that do not share a kanji: そわそわ/いらいら, 弱気/人見知り, 快適/気軽, リフレッシュ/リニューアル, すっと/さっぱり, うっとり/ぼんやり, もっとも/妥当, 見事/優秀, 広々/ゆったり, まごまご/じたばた, 憎らしい/見苦しい, and others. | The vi glosses (and そわそわ/気分転換 in ja) were reworded toward the book's VI line. | `lures` GW/PAIR only looks at items that were actually generated. |
| 6 | Rubies: 点検｜中《なか》, やり方《ほう》 ×2 (the author's pykakasi override `'方':'ほう'`), 鮮《せん》やか ×2, 怒《いか》 ×2. | Corrected. | A ruby script override was applied globally. |
| 7 | 構わない pos 動詞, but the book marks 連語. | Changed to 連語 (precedent: あり得ない). | — |
| 8 | Unsourced claims remained: 謙遜「な態度」, a standalone-reply use of 別に, 「〜てしまった」 under しまった, the 前向き etymology, and the official scene detail in わくわく's nuance. | Cut. | — |
| 9 | Usage collocations and vi compares copied the book's example phrases (ふわふわのパン, 失敗を恐れる, ユニークな建物, 見事な作品, やっかいな仕事). | Replaced. | Item 16. |
| 10 | vi prose had bare Japanese (穏, 訳, 情, 若/弱, 憎). | Quoted. | Item 6. |
| 11 | vi compares that rendered the ja: of 38, **22** mirrored it outright, 14 only added a "đều dịch X" tag, and 2 were independent (1380, 1381). The 5 vi back-link sentences on empty compares also mirrored. | All 22 and the 5 back-links were rewritten to lead with Hán Việt or the Vietnamese trap. | Items 10, 11 and 15. One-author batches still translate the compare. |

## Coordinator items

1. v-0611 fix dropped: B24's live 「大事な部分」 is kept.
2. 洗練 is now 「よくみがかれて、むだがなく上品になること」 (no 抜, no 何度も).
3. The linked pairs are added both ways with a compare in each pane: 謙遜↔謙虚, おく病↔恐れる/心細い (and ↔弱気, which glosses 「nhút nhát」), ためらう↔大胆.
4. Compacted compares. v-1357 keeps 「嫌がらずに受け入れる」. v-o-sukkiri now carries すっと's contrast instead of "similar". Its vi restores 「sạch mồ hôi」 and "dễ chịu" for さっぱり. v-1330 restores 「一人の人の」 and 怒《おこ》. v-o-nagoyaka's contrast survives.
5. Blanking the "Hán Việt = tiếng Việt" and register nuances was right. Three that survived were cut (item 8).
6. The count is 22/38.
7. The live fixes are based on a8605f4: v-1139 → むずかしい, v-0739 → 親切 (drops 気をつかう, a B27 headword), and no また/より/とても in any fix.

## Open for B27

- B27's V27 fixes for v-1270 and v-o-juudai must be rebased onto B25's new text, which uses ひどく and drops 済まない.
- Live 「また、」 and 「より」 appear in many glosses outside B25.
