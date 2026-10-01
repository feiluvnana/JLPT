# QA report — 知識 N2 漢字 batch 13 (71 kanji, SK 551–649; 64 → 72 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes. One author (Sonnet) wrote both panes, the vi pane first.

Files: scratch `batches/漢字_B13.*` and `K13_live_meaning_fix.json` (3 ja). The originals are in `QAK13_orig/`. The fixes are in `QAK13_fix.py` and `QAK13_fix2.py`, plus one inline edit (荷 usage). Built on the live tree at 869bc2f (B12 live). Live `knowledge/` was not touched.

## Checks

| area | method | result |
| - | - | - |
| ids / readings | SK 別冊 pp.43–48 (PDF 176–181) read as images, all 71 entries | Every id, on/kun and word matches the page. k-0606 is 干 and k-0648 is 叫. 革 599 is present. The one exception: 荷 listed 「荷」, but the page prints only 荷物 under に (F3) |
| range | 551–649 against live + B13 | No number is missing |
| official_count | Parser over 問題1/2 of 31 sittings (301 items), plus the 9 items it misses, read by hand. Live `sources` were also grepped for keyed B13 kanji | 0 is right for all 71. The only 問題1 hits are in stems (応募, 柔軟に対応, 確認, 慣れる, 季節, 覚えて) or a name (丸山). Every cited 問題2 item is a distractor, marked 「数えない」 |
| frames | `frames` + a read of every example | 3 hits, 2 of them real (F2). 案 vs a 7/2014 script line shares only 市/案内, so it was kept |
| lures | `lures` before and after | Before: 1 GW. After: 2 GW, both judged false positives (see F5) |
| furigana | own-kanji reading scan + a read of every ruby in the prose and back-links | 15 wrong rubies (F1) |
| gate | `gate 漢字 13` | 0 FAIL, 0 WARN, 0 REVIEW |

## Findings

| # | where | severity | finding → fix | root cause |
| - | - | - | - | - |
| F1 | 栄 干 官 乾 欧 仮 許 株 及 供 基 · 押/喫 vi · 衣/久 back-links | major (brief 7/12) | Wrong rubies: 上《あ》 ×3, 下《さ》 ×2, 形《けい》 ×4 (when meaning かたち), 日《にち》, 栄《さかえ》, 乾《いぬい》, 米《こめ》 (meaning アメリカ), 仮《かり》 and 許《もと》 (readings not listed), 表《おもて》 (meaning 表), 元《げん》, 衣《ころも》. vi: 押《お》さえる split → 押《おさ》える. 「(店)」 sat outside 「」. 依's example had ruby on katakana | The author did not do the pykakasi-diff pass (brief 12) on the compare fields. Only 4 of these break the gate's own-reading rule, and the gate did not flag even those |
| F2 | 革 漁 株 examples | major (brief 3) | 革 shared a frame with open 漢字_B14 k-0725 (旅先/財布). The first fix then hit live k-0234 (手入れ/years of use). 漁 shared a frame with open 語彙_B15 v-0570 (漁師/波が高い). The first fix then hit live v-0268 (夜明け/船を出した). 株 said 「株を一枚」, which is unnatural. All three were rewritten, and `frames` is now clean | Frames were not re-run against the open batches written in parallel |
| F3 | 荷 | minor (page) | The page prints only 荷物 under に → words and usage were trimmed in both panes | — |
| F4 | 宇 欧 希 革 環 丸 · 応 疑 叫 官 | major (brief 2 / rule 29) | 宇, 欧 and 希 were glossed from their only compound. They now follow the live precedent: 「「うちゅう」のかたちで…」 / 「VŨ — (trong 「うちゅう」) vũ trụ」. The 「なめした」 in 革 → 「どうぶつのかわ」 / 「da (động vật)」. 環's second sense came from 環境, and 丸's 「viên」 was unsourced: both cut. Near-synonym gloss collisions were reworded: 応 「こたえる」 / 「đáp lại」 (= 答), 疑 (≈ 怪's gloss, word for word), 叫 「kêu」 (= 鳴), 官 「cơ quan nhà nước」 (= 府) | No sense is on the SK list page. The author took the compound's sense |
| F5 | 械↔性 | minor (item 4) | This link was made only to clear a GW lure on 「giới」 (in 性's 「giới tính」). It is not a real confusion: the option leads with TÍNH, and no meaning is shared. The link and the two compare sentences were dropped. The GW now shows in `lures` as a judged false positive, like 質↔本 「bản」, which was already live | Linking to silence the tool |
| F6 | links | major (rule 28 / brief 4) | Added both ways: 胃↔未 (both VỊ; vi only, because the ja pane has no contrast), 官↔府, 叫↔鳴, 漁↔両, 羽↔葉. Also the compound partners whose glosses collide: 供↔給 (供給; 「cung cấp」 holds CẤP), 給↔与 (給与). And the near-synonyms: 祈↔願 (祈願), 疑↔怪, 委↔任. That makes 8 new back-link targets. The 任 ja compare was at 95/100, so it was shortened | B12 was not live when the batch was written. The author's lure scan looks only at the generated pairs |
| F7 | 7 capped back-links | major (item 3) | 反 and 変 (both panes) and 員 貨 機 見 望 (vi) now shorten the live compare, keep every 「」 form (the gate shows 0 REVIEW), and add the contrast | Cap |
| F8 | 3 live fixes | minor (rule 34) | The fixes for 下, 調 and 油 had swapped the kanji of 移, 確 and 液 for the kana of those same headwords (うつる, たしかめる, えきたい). Now: 「うえからさがること」, 「くわしくしらべること」, 「みずにとけないもの」 | Rule 34 applied to the kanji only |
| F9 | vi compares | minor (brief 10/11) | About 42 of 62 vi compares (68%) mirrored the ja, against 61% in B12. Four that had a real Vietnamese trap were rewritten to lead with it: 官/管/館 QUAN/QUẢN/QUÁN, 価/仮 GIÁ/GIẢ (tone only), 乾/干 both CAN, 漁/魚 both NGƯ. The 「右」 aside in 羽 was invented and was cut. The rest are shape or compound facts with no Vietnamese angle, and were left as they are (≈60% now) | vi-first did not change the content of the compares |

Hán Việt groups checked (item 4): Y 依/医/衣, VŨ 宇/羽/雨, DỊCH 液/駅/易, CẤP 給/急/級, CỰ 巨/拒/距, QUAN 観/官/関, and HOÀN 環/丸/完. In each group the kanji share both the HV and the on (or, for CỰ, the component). Each is a real one-to-one HV↔on cue, or a lure guard for the meaning quiz. None is padding. 械↔性 was the only link with no such basis.

**Defect rate.** 27 of 71 entries (38%) had a content defect. 10 of 64 back-links had one (2 rubies, plus the 7 capped links and 性). 3 of 3 live fixes had one.
