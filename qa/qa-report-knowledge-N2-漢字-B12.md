# QA report — 知識 N2 漢字 batch 12 (44 kanji, SK 488–548; 45 → 48 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes. One author (Sonnet) wrote both panes, the vi pane first.

Files: scratch `batches/漢字_B12.*`, `K12_live_meaning_fix.json` (7 ja), `K12vi_live_meaning_fix.json` (3 vi). The originals are in `QAK12_orig/`. The fixes are in `QAK12_fix.py` and `QAK12_fix2.py`, plus three inline edits (彼 word, 史/政/種 back-links, 7 vi compares). Built on the live tree at 72758f1 (B11 live). Live `knowledge/` was not touched.

## Checks

| area | method | result |
| - | - | - |
| ids / readings | SK 別冊 pp.39–43 (PDF 172–176) read as images, all 44 entries | Every id, on/kun, word and (他) mark matches the page, with two exceptions: 彼 was missing かの (F1), and 放 had a ruby error (F2). 預 k-0532 is present |
| official_count | Parser over 問題1/2 of 31 sittings (301 items), plus the 9 items it misses, read by hand. The live `sources` were also grepped | 0 is right for all 44. No keyed hit falls on any B12 kanji. The 4 distractor-only items (美やか, 並しい, 勧遊/観遊, 疲老) are cited 「数えない」 |
| examples | `frames` (0 hits), then all 44 read once | No scene or frame copies, no 問題6 misuse, and no saturated scenes |
| lures | `lures` before and after | Before: clean. After the かの fix: READ 彼 (F1), which is now fixed. Final: clean |
| translation | vi read field by field against ja | `meaning` and `usage` are written for the vi reader. The vi `compare` mirrored the ja in 25 of 41 (61%); after the fixes in F6, 18 of 41 (44%) |
| back-links | `rebase`, plus a read of all of them | Every back-link keeps the live text. 6 had ruby defects (F3), and 5 were relation-only at the cap (F4) |
| gate | `batch_tool gate` | 0 FAIL, 0 WARN, 0 REVIEW |

## Findings

| # | where | sev | defect → fix | root cause |
| - | - | - | - | - |
| F1 | 彼 k-0493 | major (page / rule 30) | `kun` was missing かの (the page prints かの 彼女) → `["かれ","かの"]`, and usage was split by reading in both panes. Adding かの made `lures` READ fire: on the word 彼, the distractor 「かの」 is a real reading. Standalone 「彼」 was dropped from `words`; usage still teaches it | The author put the reading in prose only. The reading quiz uses `kun` |
| F2 | 放 ja usage | major (▶ speech) | 「｜放《ほう》れる」 → 「｜放《はな》れる」 (the page reads はなれる) | Ruby copied from the on reading. The ruby scan cannot see it, because pykakasi agrees with ほう |
| F3 | back-links 泣 止 付 疲 部 貿, and 倍/並 ja | minor | 鳴《め》 → めい. 留《と》 → りゅう. 付《つき》 → ふ. 「｜疲《ひ》｜老《ろう》」 → 「疲老」 (a non-word option). 「咅《ぼう》」 → no ruby (咅 is not ボウ). 卯《う》 → ぼう, to match 留's card. 並 「普の上《じょう》」 → うえ | Component and kanji-name rubies were never checked against a reading |
| F4 | back-links at the cap: 登 設 等 (ja), 設 冷 考 (vi) | major (rule 28) | The live compare was compressed, keeping every 「」 form (`rebase` prints the trimmed prose), and the contrast was added: 登/設 ← 癶/殳, 等 ← 「並しい」, 冷 ← レイ, 考 ← 耂 | The author added the relation without the text instead of compressing |
| F5 | links 府↔政, 歴↔史, 類↔種 | major (rules 28/29/30) | Linked both ways, with a compare in both panes (3 new back-link targets). 歴 and 史 both had only 歴史, so both cards asked 歴史 (rule 30). Added 学歴 to 歴 (Hajimete No.642, PDF 122): 史 now asks 歴史 and 歴 asks 学歴. Glosses that took a sense from a compound were reworded: 府 「chính phủ」/「くにの…」, 歴 「lịch sử」, 類 「chủng loại」/「しゅるい」, 由 「tự do」 | B11 was not yet live when the batch was written |
| F6 | vi compare 夫 婦 遊 老 彼 倍 預 | minor (brief 10/11) | Rewritten to lead with the Vietnamese trap: PHU/PHỤ, DU/DỤ, LÃO/LAO and BỈ/BÌ differ only in tone, BỘI/BỘ are near in sound, and 預/予 are both DỰ. 婦 「ở đầu」 was garbled. The other 18 mirrored compares are shape or same-on facts with no Vietnamese angle, and were left as they are | Even vi-first, the author wrote the same contrast list for both panes |

Optional links not made: 倍↔増, 末↔初, 老↔若 and 命↔死. They are antonyms or unrelated senses, so neither can be a second answer on the other's meaning quiz, and `lures` finds no PAIR or GW for them. k-0766 順: the K12 fix builds on K11's text, which is live, and that is confirmed.

**Defect rate.** 9 of 44 entries (20%) had a content defect: 彼, 放, 並, 倍, 府, 歴, 類, 由, 婦. 11 of 45 back-links (24%). 0 of 10 live fixes.
