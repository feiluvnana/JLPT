# QA report — 知識 N2 漢字 batch 14 (70 kanji, SK 650–754; 40 → 51 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes. One author (Sonnet) wrote both panes, the vi pane first.

Files: scratch `batches/漢字_B14.*` and `K14_live_meaning_fix.json` (2 ja). The vi live-fix file was dropped (F7). The originals are in `QAK14_orig/`, and the fixes are in `QAK14_fix.py` plus small inline edits. Built on the live tree at f0c513d (B13 live). Live `knowledge/` was not touched.

## Checks

| area | method | result |
| - | - | - |
| ids / readings | SK 別冊 pp.48–54 (PDF 181–187) read as 220-dpi images, all 70 entries | Every id, on/kun, word, (他)/(自・他) mark and 第N回 group matches the page |
| official_count | Parser over 問題1/2 of 31 sittings (301 items), plus the 9 items it misses, read by hand | 0 is right for all 70. The 問題1 hits are stem-only (状況, 訓練, 湖, 野菜, 雑誌, 支出, 司会, 歯医者, 知識). Every cited 問題2 item is a distractor, marked 「数えない」 |
| ⟦⟧ markers | grep of the batch files, the fix files and the author's build | The author's `K14_build.py` strips ⟦⟧ before writing, so no file and no built page holds one. The non-word options print plain inside 「」 (志めて, 園技, 構義, 礼義 …). The ruby'd options are all real words |
| furigana | Every ruby pair (640), read in context, before and after the fixes | No wrong reading in the B14 text. One live oddity was carried along (F8) |
| back-links | Diff of every back-link against the live text at f0c513d | All 40 started from the current live compare, including 礼, 志, 怖 and 勧. 礼's vi had no B14 sentence added (F1) |
| frames / lures / gate | `$T` before and after | frames: 1 hit left, against the open B15 (F6). lures: 1 GW, judged a false positive (F7). gate: 0 FAIL, 0 WARN, 0 REVIEW |

## Findings

| # | where | severity | finding → fix | root cause |
| - | - | - | - | - |
| F1 | back-links 礼 事 軍 | major (item 5) | 礼 vi was the live text unchanged, so the 札 contrast was missing. It was rebuilt at 173/180, keeping every 「」 form, plus 札儀. 事 vi ended in the fragment 「+「故」 (CỐ)」, which was rewritten at 166. 軍 said 群 「音がにている」, but both are グン. It now says the reading is the same, and that 君 is only near | Author was at the 180 cap |
| F2 | 妻/婦 伺/訪 雑/乱 幸/福 守/護 均/平 況/情 訓/修 劇/俳 検/省 戸/口 雇/員 肯/賛 候/寒 罪/刑・違 故/災 司/当 誌/刊・写 | major (rule 28/40) | Latent gloss collisions with unlinked entries. 妻's ja gloss was word for word 婦's, and 婦's gloss held 「つま」. Fixed by links (F3) or by rewording the B14 gloss. 婦 got a live ja fix that drops 「つま」 | `lures` checks only the distractor pairs the generator picks today, and the author relied on it |
| F3 | links | major (brief 4 / item 3, 5) | Added both ways: 刷↔印, 構↔講 (same 問題2 option set and 冓), 均↔平, 勤↔務, 劇↔技, 幸↔恵, 幸↔福, 妻↔婦, 守↔護, 士↔師, 君↔様. That makes 11 new back-link targets. 平, 務, 福, 講 and 師 were at the cap, so the live text was compressed, keeping every 「」 form | Compare named the kanji, but `related` did not include it |
| F4 | 境 均 候 冊 肯 協 | major (item 5) | Unlinked kanji named only in compares were reworded out: 景/警 (境), 軍 (均), 後 (候 → compare ""), 刷/殺 (冊), 否 (肯). 協 vi said the three キョウ kanji differ 「only on the left」. Wrong: 協 is 十+劦, while 挟/狭 share 夾 | Author named HV-mates without linking them |
| F5 | 採 伺 万歳 軒 士 構 司 | major (rule 27/29) | Glosses cut back to the page's words: 採 → 「とりいれること。また、てんをつけること。」/ 「lấy, thu nhận; chấm (điểm)」. 伺 → asking only, with the visiting sense dropped. 万歳 lost 「tiếng hô mừng」, and its compare now states the ざい reading. 軒 gains the 〜軒 counter sense, and 「cửa tiệm」 is gone. 士 → 「はかせやぶしのような、ひと」. 構 no longer glosses itself with 「かまう」. 採's ja compare was a tautology and was rewritten | Dictionary sense, not the SK page |
| F6 | 健 司 妻 examples | minor (brief 3) | 健 (保健室+測) and 司 (緊張+声が震えた) shared frames with the open B15. 妻 shared パン屋+近所 with live v-0442. All three were rewritten. **Left for B15 QA:** 刻 「祖父…孫の名前」 against B15 k-0845. The predicates differ | B15 was being written in parallel |
| F7 | live fixes 質, 性 | minor (B13 F5) | The vi fixes only silenced the 械↔性 「giới」 GW that B13 QA had already judged a false positive. They made the gloss worse (「nam hay nữ」), and they created a new 「tính chất」 overlap between 質 and 性. Both were dropped | Changing the data to silence the tool |
| F8 | kx-織 ja (live) | note | Live 組《くみ》 for the kanji 組, where the vi pane uses ソ. Carried along unchanged in the back-link and not fixed here | Live, B13 |
| F9 | vi compares | minor (brief 10/11) | About 30 of 51 vi compares (59%) mirror the ja content. Most are compound-partner lines (「XY」 ghép X với Y), where both panes must say the same fact. None renders the ja sentence by sentence. The rest lead with a Vietnamese HV trap (HIỆP, QUÂN, CỐ, HỒNG, SÁT, CHI, TỪ, CẢNH) | Same as B12/B13 |

**Defect rate.** 31 of 70 entries (44%) had a content defect, mostly latent gloss collisions. 3 of 40 back-links had one. 2 of 3 live fixes had one.
