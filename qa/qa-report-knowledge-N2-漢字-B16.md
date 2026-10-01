# QA report — 知識 N2 漢字 batch 16 (73 kanji, SK 871–965; 23 → 46 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes. One author (Sonnet) wrote both panes, the vi pane first.

Files: scratch `batches/漢字_B16.*`. The originals are in `QAK16_bak/`, and the fixes are in `QAK16_fix.py`, which rebuilds the batch from the originals. `K16_live_meaning_fix.json` (4 ja) and `K16vi_live_meaning_fix.json` (1 vi) were checked and kept unchanged. Built on the live tree at 1023d80 (B15 live). Live `knowledge/` was not touched.

## Checks

| area | method | result |
| - | - | - |
| ids / readings / groups | SK 別冊 pp.60–65 read as page images, all 73 entries, including the OCR-missed 到 893, 筒 901 and 箱 932 | Every id, on/kun row, word and 第42–46回 group matches the page. 箱 has no on row, which is correct. The 22 numbers in range that are not in the batch are all live |
| official_count | B15 parser over 問題1/2 of 31 sittings (301 items), plus the 9 items it misses, read by hand | All 73 are 0, confirmed. Every 問題1 hit is stem-only, and every cited 問題2 item is a distractor marked 「数えない」 |
| furigana | All 1,490 ruby pairs. Each pair that differs from pykakasi was read in context | One error (F1). The other readings follow the page: 停留所 ていりゅうじょ, 博士 はくし/はかせ, 五十歳 ごじっさい |
| example ↔ example_note (brief 14) | All 73 read side by side | All 73 match. None translates a replaced draft |
| frames / lures / gate | `$T` before and after | frames: 0 hits. lures: 1 GW (養↔田 「そだてる」). That pair is live and outside B16, and it has been there since B9. gate: 0 FAIL, 0 WARN, 0 REVIEW |

## Findings

| # | where | severity | finding → fix | root cause |
| - | - | - | - | - |
| F1 | k-0898 example | minor | 「｜出入《でいり》り」 repeated the okurigana (brief 12) → 「｜出入《でい》り」 | No tool checks a ruby against the okurigana that follows it |
| F2 | k-0910 鈍 | major (item 4, rule 3/39) | The example 「寝不足…朝から考える力が鈍い」 copied the frame of SK 語彙's 鈍い② (起きたばかり…頭の働きが鈍い). The OCR garbling hid it from `frames`. Rewritten as 「寒さで指先の感覚が鈍くなり…」, with a new vi note. The sense 「chậm / おそい」 is now cited: SK 語彙 鈍い ①②④ and 12/2018 問題6-27 (key 4 「動きが鈍い」, marked 「数えない」, because it is a usage item) | Frame scan reads an OCR extract |
| F3 | 派 博 武 舞 被 meanings | major (rule 29) | Four glosses borrowed a compound's sense: 派 「めだつ」 (from 派手), 博 「ものしりなひと / tiến sĩ, bảo tàng」, 武 「binh khí」 (from 器), 舞 「しばいをするばしょ / sân khấu」 (from 台). Following the 緒/召 precedent, they now read: 派 「「はで」「りっぱ」のかたちで…」, 博 「ひろくものをしっていること… / uyên bác」, 武 「たたかいにかかわること / võ, việc binh」, 舞 「まうこと。「みまう」のかたちで… / múa」. 被 「わるいことをうけること」 was 犯's gloss with one word changed, so it is now 「いやなめにあうこと」 | Page words were glossed instead of the kanji |
| F4 | links | major (brief 4, items 1–3) | Added both ways, with a compare in both panes: **副↔福** (three 問題2 sets), **貧↔富** (shared 「おかねやもの」), **殿↔氏・君・様** (all four are name suffixes, so a meaning quiz could have two answers; rewording only hid this from `lures`), **薄↔濃・厚・縮**, **被↔破・避**, 波↔破, 坂/板/版/販↔反 (their compares already named 反), 帳↔張, 怒↔努, 鈍↔純. Also every unlinked 問題2 pair: 頂↔直, 停↔絶, 怒↔責, 到↔傾, 党↔討, 毒↔損, 拝↔敬, 泊↔招, 抜↔省. That makes 23 new live targets. 12 live compares were compressed to fit the caps (張 vi, 努 vi, 責, 福, 富 vi, 破, 反 vi, 濃 vi, 厚 vi, 氏, 絶 vi, 損, 招 vi, 省 vi). Every 「」 form was kept, as `rebase` confirms | `related` was not filled in when a compare or nuance named the partner |
| F5 | k-0946 vi compare | minor (rule 9) | 「hai chữ mà đề hay đặt vào chỗ của 被」 had the direction backwards (被 is the distractor) and made a frequency claim. Rewritten | Unsourced claim |

## Rulings on the known items

- **Not linked**, because they share only an on reading and no gloss word or 問題2 set (the B15 存/孫↔損 rule): 帳/頂/超↔兆/庁 (チョウ), 副↔準, 童↔重, 認↔任. Look-alikes were linked instead: 帳↔張, 鈍↔純, and 頂↔直 through their 問題2 set.
- **In-batch Hán Việt groups:** ĐỒNG, ĐỘC, NÃO, BẢN, BẠC, VŨ, PHÙ and ĐỒ (徒/途/塗) are needed. Each pair shares a Hán Việt syllable that leads its vi gloss, so rule 40 requires the link. NÃO, BẢN, 筒/銅, 途/塗, 博/薄 and 坂/板/版/販 are also real look-alikes. The 渡 links to 徒/塗 (shared ト only) are padding. They are harmless and were left in.
- **vi compares:** about 29 of 52 (56%) mirror the ja content (compound partners, same-on lists, radical contrasts, with Hán Việt labels added). None renders the ja sentence by sentence. The other 23 lead with a Vietnamese trap. They were left as they are, as in B15.

Merge: `$T merge 漢字 16`, which takes the K16 live fixes, then `make knowledge`, then `make check`.
