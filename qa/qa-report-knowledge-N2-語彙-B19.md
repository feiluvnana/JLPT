# QA — 知識 語彙 B19 (Hajimete No.884–963, PDF 164–176)

Fresh-eyes reviewer; authored nothing. One round, fixed directly in the batch dir.
Scope: 69 entries. The 11 dropped numbers are all live: 888 890 902 904 913 925 929 942 948 949 961.
900 占い and 906 宝くじ are printed headwords on PDF 166/167, so they are kept. Back-links went from 2 to 9.
There are 23 ja live fixes and 1 vi live fix. All are rebased on the live text after B18 (f5d0ffd).

## Findings and fixes

| # | Finding | Fix | Root cause |
|---|---|---|---|
| 1 | No live fix file. 23 live glosses carried a B19 headword: あまりに, 当た, 災害, 去る, 身近, 組み合わせ, 行動 ×4, 及ぶ, 気候, 共通, 静ま, あふれる, 瞬間, and 「にわか」 inside 「相手にわかる」 | `V19_live_meaning_fix.json` (23) rewords each one, checked against that card's own examples. Two second-round lures were fixed too: 心当たり→思いつく and 抽象的→大まか. 示す's 気持ち/tình cảm made a PAIR with 込める, so `V19vi_live_meaning_fix.json` adds the vi fix. 防災 also avoids B20's 前もって | The author ran `lures` but treated the HW lines as optional |
| 2 | Wrong rubies (13 ×「人《にん》」 for a bare 人), plus 占《せん》う, お金《きん》, 長い間《ま》, 床《とこ》, 二十歳《はたち》年上, 梅雨入《つゆいり》り/梅雨明《つゆあけ》け (okurigana repeated), 凝り性《せい》 (the page has しょう), 散歩/行楽/洗濯日和《ひより》 (the page has びより) | All corrected in both panes and the back-links | These are pykakasi-style readings. Rule 12 (diff against pykakasi) cannot catch them. Read each ruby in context |
| 3 | Missed official_count: 属する 12/2011 問題2-10 (key 属して) and いっそう 12/2019 問題5-24 (underlined 一層, key もっと) | Each set to 1 with its source. 9 distractor hits were added as 「数えない」 (当たる ×2, 直後, 観測 ×2, 応答, 共通, ぐんぐん, 身近) | No reading/stem grep (brief item 13). ブーム 1, 覆う 1 and 達する 1 are re-derived and correct |
| 4 | Unlinked colliding pairs | Linked both ways with compares in both panes: ブーム↔流行 (official 問題5 pair), 当たる↔外れる, 日和↔陽気, 凝る↔熱中 (both glossed "say mê" on the page), 静まる↔収まる, 瞬間↔途端 (〜た瞬間 ≈ 〜た途端), 去る↔離れる (same-pos glosses collide). The live compares for 外れる ja, 途端 ja+vi, 流行 vi and 陽気 vi were compressed. Every 「」 form is kept (checked by script) | Partner links were skipped because the live compares were full |
| 5 | Frame copies: 凝る copied the book's 最近〜に凝って frame and live 熱中's 「父は最近…熱中」. にわか copied the book's sky-darkens frame. びしょびしょ shared 公園/遊ぶ with a 問題6 misuse sentence (12/2017 #30). 応答 was unnatural, and its replacement matched two 問題6 メール/送る sentences | 4 examples replaced, with their notes rewritten. `frames` 0 | Linked partners' examples and the book frame have to be read by hand |
| 6 | vi prose named its source (Sách ghi kèm ×2, Sách chú ×2). 夕立 vi ignored the book's "mưa giông" | Reworded | — |
| 7 | Prose errors: 達する 「他動詞はない」 is false (目的を達する). 本来 「文頭でも」 is not what the page shows (この地域は本来、…). 接近 says 「に」 but quoted an example without it. 四季's usage quoted 「春夏秋冬」 as a usage. びしょびしょ 「中までぬれている」 has no source. 達する nuance repeated the official stem (PROV) | Cut or corrected | Rules 9/27/35 |
| 8 | Translation: 12 of 16 vi entry compares and both vi back-link sentences only restated the ja (14/18) | Rewritten to lead with the Hán Việt and the Vietnamese trap: 初歩 ≠ "sơ bộ", 急速 ≠ "cấp tốc", 流行 ≠ "lưu hành", 一段 ≠ "một đoạn", 陽気 ≠ "dương khí", 達 ≠ "đạt được", and 凍える/冷え込む both glossed "lạnh cóng" | Same as B17/B18 |

## For the coordinator
- B20 clash: `V20_live_meaning_fix.json` also rewrites v-o-bousai, and its wording keeps 「災害」 (a B19 headword). Drop the B20 line and keep the B19 one, which avoids both 災害 and 前もって.
- For B20 to resolve (from `lures --with 20`): 日差し(B19)/日光 PAIR, plus 予測 「うなる」 and 敷金/賃貸 (B20-side).

Gate: 0 FAIL / 0 WARN / 0 REVIEW (also `gate 20 --with 19`). `frames` 0. `lures` 2 GW, the same live-only pair B18 left.
