# QA report: knowledge/N2 語彙, batch 1 (52 words, 104 examples, 89 generated quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. Files are in the coordinator's
scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B1.json` | 4df0f9e139fe | 29d1d67f9bf7 |
| `語彙_B1.ja.json` | 9f233831ddaf | 753610938e3d |
| `語彙_B1.vi.json` | 740dfb532d09 | 882a7a6c8a6a |

## Verdict

`QA: FAIL → fixed (8 finding classes, 25 surfaces). 0 content findings are open after the fixes.`

I merged B1 into a scratch copy of `.agents/` + `knowledge/` (`scratchpad/QAV1_root`; `knowledge/N2/語彙.json` had 0
entries), rebuilt `語彙.html` with `build_knowledge.build_category` and ran `check_knowledge.check_category`:
**0 FAIL, 0 WARN**. The results: 52 entries, 89 generated items (37 reading and 52 meaning), all integrity rules kept,
book order correct. The real `knowledge/` was not touched.

**No reading is wrong.** The headline defect class for this category did not occur.

## 1. Readings (the whole defect class here)

- I checked all 52 `reading`s by hand. 36 are confirmed by an official 問題1 key or a 問題2 kana stem that I read in
  `booklet.md` + `key.md`, for example 12/2022 問題1-1 けいび, 7/2023 問題1-1 うんちん, 12/2022 問題4-20 いだいて and
  7/2016 問題2-10 こころよく. The other 16 are standard readings: ようじん, ふきゅう, さいばい, せつぞく, かっこう, ぞくしゅつ,
  おんこう, だとう, かんりょう, いんたい, じょじょに, and the kana words.
- I opened Hajimete PDF pp. 17, 60, 62–64, 73, 152 and 251. The cited page numbers match: No.309 is on p.64 and
  No.819 鮮やかな is on p.152. かなう is printed on p.63 as the ＋ related word of No.300 かなえる, so the `v-o-kanau`
  source and its Hajimete-chapter `group` are correct.
- **Furigana:** I extracted all 697 ruby pairs in the three files and read each one. There are no misreadings. The
  one style fix: in 4 ja nuances, 「同じ音《おと》の「係」」 became 音《おん》. The text is about 音読み homophones.
- **Generated reading items:** none of the 15 kana-only headwords gets one, so テンポ, ガイド, さっさと and the rest are
  correctly excluded. On 抱く, the valid reading だく is never offered as a distractor.

## 2. Headword, pos, band, official_count

- The headword forms match what the exam prints: 鮮やか and 温厚 appear without な, as in the 問題2 options.
- The pos values are right.
- Every word is an official 問題1–6 key, target or headword, or a numbered Hajimete headword, so all are N2 band.
  わがまま is a 問題5 key, which is the "simpler word" slot. It is N2 study material by SK N2 語彙 第2部 p.114
  (OCR line 「そんなに（わがままな・勝手な）ことを言ったら」).
- **official_count:** I did not stop at a third. I re-verified **all 52**, hit by hit, with a script that dumped every
  問題1–6 line containing the word and its kana (`QAV1_hits2.txt`), and then read each hit. 51 counts were correct.
  Reprints count once per sitting: さっさと 12/2012 = 12/2021, 順調 12/2015 = 12/2021, 妥当 12/2014 = 7/2021, and 格好
  7/2013 = 12/2021. Distractor-only hits are excluded: 普及 12/2013, 7/2024; 接続 12/2013; 格好 7/2014; ぎっしり
  12/2013, 12/2014, 7/2015, 12/2016; とっくに 7/2014; 豊富 12/2013.
- **離れる 4 → 2 (decided).** The two extra hits are 12/2015 問題3-14 and 7/2024 問題3-12. The key in both is the suffix
  〜離れ (現実離れ, 読書離れ), which is a 語形成 item. It is not a key, underline or 問題6 headword of 離れる. The same
  author did not count 12/2022 問題3-12 用心（深く） for 用心, and counting 〜離れ here was inconsistent with that. The
  sources stay, annotated 「接尾語「〜離れ」の語形成。official_count には数えない」.

## 3. Generated quizzes: every item dumped and read, in both languages

`QAV1_dump.py` calls `quiz_gen.generate()` on the batch and writes the dump to `QAV1_quiz.txt`, then `QAV1_quiz2.txt`
after the fixes. The vi author flagged seven pairs. My verdicts:

| pair | verdict |
|---|---|
| さっさと / たちまち | **Defect.** たちまち's ja gloss 「とても短い時間のうちに。すぐに。」 was a distractor in the さっさと item, and it reads as a correct gloss of さっさと (さっさと帰る ≈ すぐに帰る). The official さっさと 問題6 misuse 「さっさと雨が降り出した」 is exactly たちまち's territory. **Fix:** `related` both ways, plus `compare` in ja and vi, each written from the items. |
| 用心 / 備える | Not paired today (different pos), but near-synonyms (前もって気をつける / 前もって準備する). The pair would surface once the 名詞 pool thins. **Fix:** `related` both ways plus `compare` in both languages. |
| 介護 / 福祉 | Paired: 福祉 is a distractor in the 介護 item. Its gloss 「すべての人が安心して暮らせるように、社会が行う支え」 / "Phúc lợi xã hội" is **not** a correct gloss of 介護 (hands-on care of one person). Kept. |
| ぎっしり / 豊富 | Not paired. The glosses are not interchangeable (packed with no gaps vs. plentiful in amount or kind). No change. |
| 快い / 和やか, のんびり / 和やか | Not paired. The glosses cover different domains: a feeling or willing acceptance, a relaxed manner, and the mood among people. No change. |
| 幼い / わがまま | Not paired. 「子どもっぽい」 is not 「自分のしたいようにする」. No change. |

I read all the other meaning items too. No other distractor is a correct gloss of its key. The 鮮やか and くたくた keys
changed because of §4.

## 4. Examples: sense, naturalness, provenance

The 10-char window scan runs against `refs/**/*.md`, `tests/imported-*` and the other scratch batches. It found one
hit. I also compared each example with the Hajimete example on the cited page, the SK 語彙 extract lines, and the
official items cited in `sources`.

| # | entry | finding | fix |
|---|---|---|---|
| E1 | 鮮やか ex2 「鮮やかなシュート」 | The "skilful" sense is in no cited source. Hajimete p.152 glosses only *bright* (「鮮やかなピンクのシャツ」), and all 3 official items are about colour. The ja meaning 「また、技がみごとだ」, ja usage 「手つき」「技術」「記憶」, vi meaning/usage/compare 「kỹ thuật」 were unsourced too. | ex2 → 「空に鮮やかな虹が出た」. The meaning and usage in both languages are cut to colour and shape. |
| E2 | くたくた ex2 (a worn-out T-shirt) | That sense is not in SK p.150, which files the word under 疲れた様子 only, and both official items are about fatigue. The ja/vi meaning carried the extra sense. | ex2 → 「朝から晩まで子どもと遊んで、体がくたくたになった」. The meaning is fatigue only in both languages. |
| E3 | 備える ex1 「地震に備えて、水と食料を三日分用意」 | Same scene and predicate as SK 語彙 備える① 「地震に備えて（水）を買っておく」: a copy with new nouns. | → 「大雪に備えて、車のタイヤを冬用のものに替えた」 |
| E4 | わがまま ex1 「小さいころの私はわがままで、よく母を困らせた」 | Same scene and predicate as SK 「私は、わがままで…子供だったそうで、親は大変だったらしい」. | → 「お客のわがままな注文にも、店員はいやな顔をせずに応じた」 |
| E5 | 世間 ex1 「小説は世間で大きな話題になった」 | Same frame as Hajimete 「政治家の発言が世間で問題になっている」. | → 「世間では連休が始まったが、私は毎日仕事だ」 |
| E6 | 快い ex2 「急な相談にも快く乗ってくれた」 | Mirrors two official items at once: 7/2016 問題2-10 「急なお願いにもかかわらず…こころよく応じて」 and 7/2013 問題6-29 「急な仕事だったが…快く引き受けて」. | → 「重い荷物を運ぶのを頼むと、隣の人は快く手伝ってくれた」 |
| E7 | 破れる ex1 「転んで、ズボンのひざが破れて」 | A near-verbatim duplicate of the scratch `漢字_B1.json` example 「転んだ拍子に、ズボンのひざが破れた」. Two cards in the module would show one sentence. | → 「何度も洗っているうちに、シャツのひじのところが破れてしまった」 |
| E8 | およそ ex1 「駅から会場まで歩いておよそ20分」 | Close to SK 「学校から駅までの距離は、およそ1キロメートルだ」 (distance to the station). Rule 13: pick a scene SK does not use. | → 「この工場では、およそ300人が働いている」 |

After the fixes, the scan is clean. Every changed example has a new vi `example_notes` translation, written from the
Japanese. All other examples are natural N2 sentences that use the word in its tested sense.

## 5. Prose

- **Official-distractor claims:** I checked every quoted distractor list in both languages against the booklet line.
  All are real, including 介護 「かいごう」, 警備 「警秘」「係備」「警護」, 豊富 「ほうふう」 twice, 求人 「きゅにん」,
  幼い 「くどい」, ガイド 「記録」「応援」「準備」, and そそっかしい's 「あわただしい人」 (12/2013 問題6-29).
- **P1 (rule 18):** the ja nuance of およそ named a sitting (「7/2024では…」). Reworded without the source.
- **P2:** the vi nuance of 格好 misquoted the official frame as 「〜な（　）で行く」. The frame is 「ちゃんとした（　）で行く」.
- **Hán Việt glosses:** every one I checked is correct (e.g. 運賃 vận nhẫm, 撮影 toát ảnh, 接続 tiếp tục with its false-friend note).
- **vi quoting:** a script found no Japanese outside 「」 in any vi field.
- **Translation check:** vi is not a translation of ja. Framing and collocation choices differ throughout.
- **Bands:** after the fixes, everything is within the bands. One new vi compare was trimmed from 192 to 156 characters
  (cap 180).

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| E1, E2 (a sense no cited source has) | LEX_JA_BRIEF says "sources decide" for readings, but not for **senses**. The authors wrote dictionary knowledge into the meaning and the second example. | Add to LEX_JA_BRIEF and the SKILL: *every sense in `meaning` and every example's sense must appear on a cited page (Hajimete gloss or example, SK line) or in a cited official item; otherwise cut it.* |
| E3–E6, E8 (scene copies) | The 10-char scan cannot see reworded copies. Rule 13 (compare with the cited page's examples) is written for 文法 and does not name the Hajimete example, the SK 語彙 lines or the official items cited in `sources`. | Extend rule 13 to 語彙/漢字: compare each example with the Hajimete example on the cited page, the SK 語彙 lines for the word, and **every official item in `sources`**. |
| E7 (cross-batch duplicate) | The 語彙 and 漢字 batches were authored in parallel, and neither scan covered the other. | The provenance scan must include every `batches/*.json` and `knowledge/**`. |
| さっさと/たちまち | The author listed no near-synonyms in `related` (only 3 pairs across 52 words). The Residual risk note in SKILL §Quiz integrity was not acted on. | In the LEX brief: *before hand-off, dump `quiz_gen.generate()` over the batch and read every meaning item; any distractor that also glosses the key → `related` or a sharper meaning.* |
| 離れる count | Rule 12 (what counts) is written for grammar and does not say whether a 語形成 suffix counts. | Add to rule 12: *for 語彙, a 問題3 語形成 key counts for the affix, not for the base word.* |
| P1 | Rule 18 was applied to "SK/page/課" only. | Rule 18 already covers it. Add "sitting dates" to its examples. |

## For the coordinator: the 13 dropped Hajimete numbers

I opened pp. 17, 60, 62–64, 73 and 251. The inventory's kana headwords are OCR that lost the kanji, and **their
inventory official counts are substring noise**. For example, かん matched any かん, and かぐ matched other words. Each
official count must be recounted from scratch.

- **Genuine N2 words, must be authored later:** **No.44 is 幹事 (かんじ)**, not 勘 (p.17: 「仲間の飲み会では、いつも私が幹事だ」).
  Also No.307 かぐ = 嗅ぐ (the book prints kana, p.64), No.338 さっと, **No.366 束（たば）** (p.73), No.384 いっそ,
  No.784 破る (the 他動詞 of 破れる, which this batch already has), and No.1001 こぐ.
- **Genuine numbered headwords but basic or function words** (the coordinator's call; omitting them leaves no gate
  failure, only gaps in the book order): No.283 あと (副, 「あと5分で」), No.290 何度も (副), No.1390 しまった
  (感動詞, p.251), No.1531 また and No.1545 さて (接続), and No.130 あいつ.
- No.1130 is 副作用, which is not in batch 1's plan. The coordinator's list probably meant No.130 あいつ.
- The plan's unnumbered 印象的だ, 乱す (folded into 乱れる's usage), うつろ, あみ and ただ were also dropped, and the
  author did not list them. Recount each one before authoring it: in 12/2024 問題5-25 「しぐさは印象的だった」 the target
  is しぐさ, not 印象的.
