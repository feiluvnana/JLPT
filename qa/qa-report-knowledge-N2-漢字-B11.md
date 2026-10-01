# QA report — 知識 N2 漢字 batch 11 (72 kanji, SK 385–487; 28 → 40 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes. One author (Sonnet) wrote both panes.

Files: scratch `batches/漢字_B11.*`, `K11_live_meaning_fix.json` (18 → 19 ja), `K11vi_live_meaning_fix.json` (1 → 2 vi). The originals are in `QAK11_orig/`. `QAK11_fix.py` rebuilds every fix from those originals plus the CURRENT live tree (B10 live, 5168740). Live `knowledge/` was not touched.

## Checks

| area | method | result |
| - | - | - |
| ids / readings | SK 別冊 pp.33–39 (PDF 166, 168, 170, 172) read as images: 22 entries (際 信 神 成 制 性 政 星 身 打 太 対 退 第 題 宅 達 単 暖 談 池 遅 竹 虫 注 得 熱 念 馬 配) | All ids, on/kun, words and (自・他) marks match the page |
| official_count | Parser over 問題1/2 of 31 sittings (301 items), plus the 9 items it misses, read by hand | 0 is right for all 72. No 問題2 key holds a B11 kanji, and every 問題1 hit is outside the underlined word. 7 distractor-only hits were missing from `sources` (F5) |
| examples | `frames` (0 hits), then all 72 read once | No scene or frame copies, and no 問題6 misuse |
| lures | `lures` before and after | Before: GW 接/礼, HW 出(行), HW 践(実践). After: GW 接/礼 and GW 践/送 (HV TIỄN vs the word "tiễn"). Both are judged not two-answer. Both pairs predate B11, and B10 accepted the same pairs |
| translation | vi read field by field against ja | `meaning` and `usage` are written for the vi reader. **`compare` restated the ja in 29 of 33 entries** (F3) |
| back-links | `rebase`, plus a read of all 28 | All 28 keep the live text. 7 had defects (F4). 12 new targets were added for the links (F1) |
| gate | `batch_tool gate` | After the fixes: 0 FAIL, 0 WARN, 0 REVIEW. The own-kanji ruby check is clean |

## Findings

| # | where | sev | defect → fix | root cause |
| - | - | - | - | - |
| F1 | links | major (rules 28/29/40) | Added the author's link-at-merge pairs, both ways with a compare in both panes: 増↔減, 増↔加, 追↔加, 卒/商/職↔業, 注↔意, 暖↔温, 性↔格, 式↔形, 念↔記. Added 7 pairs the author left unlinked: 身↔申 and 池↔遅 (same Hán Việt THÂN/TRÌ and the same on reading), 制↔製 (CHẾ, both in the 12/2016 製造 option set), 池↔地 (也 and チ), 身↔診 (身断/身談 in 12/2022 2-9), 急↔速 (both cards have 急速, and K11's 急 fix 「はやいこと」 collides with 速), 数↔算 (算's fixed gloss 「かずをかぞえること」 is 数える). 地/他 is not linked: the readings differ, 地 has 10 characters left for its compare, and 他↔池 already names 也 | Link candidates were found only by compound partner. They were not found by shared Hán Việt or by a live fix's new wording |
| F2 | ja meaning 竹 馬 虫 式 笑 | minor (rule 27/29) | 竹/馬/虫 claimed things the page does not show (ふし, のせてはしる, はねやあし) → 「しょくぶつの、たけ」 etc. 式 「かたち」 borrowed its sense from 形式 → 「ものごとの、きまったやりかた」. 笑 had no subject → 「おかしさやうれしさが…」 | Glosses were written from general knowledge, not from the page |
| F3 | vi compare, 29 of 33 | major (brief rule 10/11) | Rewritten for the vi reader, leading with the Hán Việt and the trap: 昨 TẠC/作 TÁC differ only in tone; 史/使 are both SỬ; 卒 TỐT ≠ "tốt"; 若 NHƯỢC ≠ "nhược" (yếu); 速/早 = nhanh ≠ sớm; 単/短 ĐOẢN = ngắn; 談/断 ダン in 診断. 申 also had 「ネ」 for 「礻」 | This is the third batch in a row with the same defect (B9 71%, B10 98%, B11 88%). The brief did not prevent it |
| F4 | back-links 鳥 雨 短 世 居 大 使 | major (▶ speech) / minor | Two rubies were wrong: 鳥 ｜下《さ》 → した, and 雨 ｜上《じょう》 → うえ. 3 vi strings began with a space. The 世 ja was a fragment with no verb, and the vi said 成 "đứng cạnh" 世 (wrong: 成 replaces 世). The 居/大/使 vi sentences were vague. All were fixed | The author's helper ruby'd from a reading table, not by sense |
| F5 | sources 種 成 戦 速 得 当 身 | minor (rule 40) | Added 8 distractor-only citations, each marked 「数えない」 (介種, 帰成, 戦ましい, 速座に, 集得/収得, 得う, 当票/当標, 身断/身談) | The author's own scan found these hits but cited only some of them |
| F6 | live fixes | minor | 行 (K11): 「まえにむかって、いく」 only swapped 進 for kana, and still matched 進's gloss → 「どこかへ、いくこと。また、なにかをおこなうこと」. 修: 「ちからにする」 → 「ちからをつける」. Two older HW hits swept in by this batch: 出 (carried 行) and 践 vi (quoted 実践). Both fixed. 製 vi was at 178/180, so its 精 clause was shortened to make room for 制, and every 「」 form was kept. k-0020 builds on K10's 「熱とひかり」: correct | A live fix was checked for the kanji it removes, not for the meaning it leaves |

**Defect rate.** 17 of 72 entries (24%) had a content defect other than mirroring: 5 glosses, 7 missing links, 5 more with missing sources. 7 of 28 back-links (25%). 2 of 19 live fixes. The vi compare mirrored the ja in 29 of 33 (88%). Edits: every vi compare in the batch (33 rewritten, 9 new), 5 ja glosses, 18 link pairs added (12 new back-link targets), 7 back-links repaired, 8 sources, 4 live fixes.

**Merge note.** B12 is being authored now. It shares the 鳥 (k-0203) back-link and the k-0766 live fix with B11. Merge B11 first, then run `rebase` on B12.
