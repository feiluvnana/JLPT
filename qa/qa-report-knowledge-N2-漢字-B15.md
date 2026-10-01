# QA report — 知識 N2 漢字 batch 15 (72 kanji, SK 755–870; 36 → 53 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes. One author (Sonnet) wrote both panes, the vi pane first.

Files: scratch `batches/漢字_B15.*` and `K15_live_meaning_fix.json` (3 ja, kept unchanged). The originals are in `QAK15_orig/`, and the fixes are in `QAK15_fix.py`, which rebuilds the batch from the originals. Built on the live tree at bd0325e (B14 live). Live `knowledge/` was not touched.

## Checks

| area | method | result |
| - | - | - |
| ids / readings | SK 別冊 pp.54–60 (PDF 187–193) read as page images, all 72 entries, including 章 (780) and 測 (841), which the OCR missed | Every id, word and 第N回 group matches the page. 15 entries left out the on reading of an empty row (F3) |
| official_count | Parser over 問題1/2 of 31 sittings (301 items), plus the 9 items it misses, read by hand | 著 = 1 (7/2021 問題1-2 「著しい」, key 3 いちじるしい, cited). Every other entry is 0. The 問題1 hits are stem-only, and every cited 問題2 item is a distractor marked 「数えない」 |
| 著しい | The SK page prints only チョ 著者 | The kun reading comes from the official item, which is cited in `sources`. Allowed |
| furigana | All 588 ruby pairs. Each pair that differs from pykakasi (about 200) was read in context | No wrong reading. The one markup error was in 兆: a stray 「を｜こえた」 with no ruby (F6) |
| back-links | `$T rebase` against live at bd0325e | All 36 original back-links started from the current live compare. The 17 new back-links append to live, and 6 were compressed to stay under the cap (調, 捨, 与, 清, 理, plus the 拾 tail), keeping every 「」 form |
| frames / lures / gate | `$T` before and after | frames: 0 hits. lures: 2 GW, both 賃↔労/工. All three are live entries outside B15, so this is pre-existing. gate: 0 FAIL, 0 WARN, 0 REVIEW |

## Findings

| # | where | severity | finding → fix | root cause |
| - | - | - | - | - |
| F1 | vi `example_notes` ×26 | major | 26 of 72 vi example translations described a different sentence from the shared example. Examples: 周's note was about a phone call, 署's about a petition, 植's about a grandmother's garden, 昔's about cherry trees. All 26 were rewritten from the current example | The vi pane was written first, against draft examples that were replaced later. No tool compares a note with its example |
| F2 | links | major (brief 4, items 1–2) | Added both ways: 築↔建, 述↔術, 就↔職, 授↔捨・拾・採・与, 贈↔与, 召↔招, 紹↔招・迎, 焼↔焦, 純↔清, 伸↔延, 掃↔除, 準↔調, 整↔調, 整↔理. Also two unflagged collisions: **舟↔船** (舟's ja gloss repeated 船's word for word, with 「ちいさな」 added) and **緒↔共** (共's gloss is 「いっしょにすること」). That makes 17 new targets, and every compare names the partner. 存/孫↔損 was **not linked**: they share only ソン, with no shared gloss word and no shared 問題2 set (損's sets are 罪害毒 / 苦悪劣 / 劣危悪 / 消失) | Compares named the kanji, but `related` did not include them. `lures` does not see a gloss that copies another word for word with one word added |
| F3 | on lists ×15 | minor | 舟 召 焼 城 伸 吹 昔 浅 捜 窓 贈 側 袋 探 仲 had `on: []`, but the page prints an on row with no words. Live keeps that row (歯 シ, 似 ジ, 拾 シュウ), so the reading was added. The prose for 召, 焼 and 伸 now names it, and 「Chỉ có âm Kun」 became 「Âm Kun」 | Different convention from live |
| F4 | glosses (item 3) | major (rule 27/29) | 緒 「いとぐち / đầu mối」 → 「「いっしょ」のかたちで…」 / 「(trong 「いっしょ」) cùng nhau」. 舟 → no 「ちいさな」 / 「thuyền」. 諸 lost 「たくさんの / nhiều」 (a GW with 多), and its 「ことばのまえについて」 wording, which made a PAIR with 第. 召 lost 「gọi đến」 and now reads 「「めしあがる」のかたちで、めうえのひとが、たべる・のむこと」. 兆 lost 「(10^12)」. The TRIỆU note is a real false friend (Vietnamese triệu = 10^6), so it stays. 掃 dropped 「すてて」 (捨's stem). 州 was kept, because the word 州 supports it | Dictionary sense, not the page |
| F5 | k-0845 孫 example | minor (item 5) | The 祖父/祖母 + 孫 scene overlapped B14 刻 and four other module sentences. It is now 「初めての孫が生まれて、隣の夫婦はとても喜んでいる」 | Saturated scene |
| F6 | k-0870 example; 共, 探 vi | minor | The stray 「｜こえた」 was removed. Japanese outside 「」 in two vi strings was quoted | Typo |
| F7 | vi compares | minor (brief 10/11) | **About 28 of 54 vi compares (52%) mirror the ja content.** These are compound-partner lines, same-on lists and radical contrasts, with HV labels added. None renders the ja sentence by sentence. The other 26 lead with a Vietnamese trap (THỤ, CHU, THUẬT, THÀNH, THẦN, TÍNH, TÍCH, TỔ, TƯỢNG, TRẮC, TÔN, ĐOẠN, TẶNG/TĂNG, THIÊU/TIÊU, TRIỆU). They were left as they are | Same as B12–B14 |

Merge: `merge_batch.py` / `$T merge 漢字 15` with `K15_live_meaning_fix.json`, then `make knowledge`, then `make check`.
