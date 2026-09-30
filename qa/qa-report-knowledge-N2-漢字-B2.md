# QA report — 知識 N2 漢字 batch 2 (70 kanji)

Fresh-eyes reviewer: this context authored none of the batch. Targets (scratch
`batches/`): `漢字_B2.json`, `.ja.json`, `.vi.json`, `.backlinks.json`,
`.backlinks.vi.json`. One full round, with direct fixes. Method as in
`qa-report-knowledge-N2-漢字-B1.md`. Validation ran on a scratch root: `.agents/`
and `knowledge/` were copied and everything else was symlinked. On that root,
`merge_batch.py` was re-pointed and applied the batch plus both back-link files
to the live 70. The builder and `check_knowledge.py` ran there. Only one live
file was edited: `knowledge/N2/漢字.vi.json`, the 介 gloss (F8). Its page was
then rebuilt with `make knowledge`.

## What was checked, and how

| area | method | result |
| - | - | - |
| ids, `page`, `group` | every entry against SK 別冊1 学習漢字リスト, PDF 141–173 and 202, read from pypdf slices | 70/70 correct |
| `on` / `kun` | every reading against the SK page | 70/70 match the page. The batch adds no reading the page lacks |
| `words` furigana | every compound read by hand | all correct |
| `official_count` | a parser listed every 問題1 sentence and every 問題2 key holding the kanji, across 31 sittings (302 parsed items). The 8 items the parser missed were read by hand (7/2019 1-4, 7/2021 1-2, 12/2023 1-2/1-3/2-9/2-10, 7/2023 1-4/2-10, 12/2013 1-4, 7/2018 2-8). Every hit was read to see whether the kanji is in the target word | all 70 checked, including both 2s (療: 12/2010 1-4 and 7/2016 1-1; 腕: 12/2023 1-1 and 7/2015 2-9). All correct. 投 (12/2023 2-9) and 失 (7/2023 2-10) are among the items the parser missed; both confirmed by hand. False hits were rightly left out: 映画 7/2016 1-3 → 批評; 人通り 12/2020 1-4 → 比較的; 出来事 7/2014 → 悔しい; 機嫌 7/2022 1-3 → 途端に; 建設 12/2021 → 賛否 |
| cited sources | every booklet `note` against the item | all 70 correct |
| prose option claims | every 「…」 list in ja/vi nuance and compare was checked against the printed options | all true. The two that are not in cited items were confirmed elsewhere: 「比しい」 (12/2022 2-10, 等しい) and 「農厚」 (12/2025 2-10, 濃厚) |
| generated quizzes | all 140 `#r` and 140 `#m` items dumped in both languages, before and after the fixes. Live items drawing batch distractors were read too | no fabricated misreading is a real reading. Meaning clashes: F3, F4 |
| Hán Việt | all 70 readings, plus the 15 「Hán Việt dễ lừa」 claims | readings fine except 住 (F5). Traps: F6 |
| examples | 10-char window scan (refs/**/*.md + tests/imported-*). Token-overlap lister over booklet/script lines AND every textbook extract. A second lister for lines holding the target word plus at least 1 shared token. Category-wide scan against every other knowledge example | 10-char scan: 0 hits at first. The overlap listers found F2 |
| vi rule 6 | script | clean |
| rule 18/30 citations | gate `check_prose_citations` | clean |
| gate | scratch merge, before and after the fixes | 0 FAIL, 0 WARN both times. `make check` on the real repo: all checks pass. Its 224 WARNs are all pre-existing test-paper lines, and none is a knowledge line |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | 外 k-0034 example | major (pronunciation) | 「外科に｜通《とお》っている」: to attend a clinic is かよう. ▶ speech read the sentence aloud wrong | → 《かよ》 | `check_ruby_suspects` knows only 3 patterns. 通う/通る is a two-reading kanji the gate cannot judge |
| F2 | examples 行, 降, 薬, 細, 勝, 急, 映, 置, 助, 住 | major (行, 勝, 細), minor (rest) | Scene copies. 行 「この道は工事中のため、車は通行できない」 = Hajimete 「この道は車は通行できない」 with a clause added (the 10-char window misses it). 勝 「人の物を勝手に使ってはいけない」 = Soumatome's paraphrase 「人の物を許可を得ないで使わないでください」. 細 「野菜を細かく切って、スープに入れた」 = SK 語彙 「ネギを刻んでスープに入れる［野菜を〜］」. 降 (snow → all white) = Hajimete 大雪…真っ白. 薬 (cold → bought medicine) = SK 読解 item. 急 (home before the rain) = Hajimete 夕立が降る前に家に帰ろう. 映 (face in a mirror) = Hajimete 鏡に顔を映しながら. 置 「地図で、駅とホテルの位置を確かめた」 = the live 拡 example (map + station + confirm). 助 and 住 repeat scenes from 語彙 v-1357 and 文法 g-tatte. First replacements: 置 (TV moved, room looks larger) hit a 10-char window in SK 語彙 and the 12/2016 script; 降 (rain since morning) matched a 7/2021 option. Both were replaced again | 10 new scenes; vi example_notes rewritten from the new sentences. All scans rerun: clean. 降 「バスを降りるときは…前のドア」 shares バス/降りる/前 with a 12/2020 script line of directions; different scene, kept | Rule 3's window cannot see a clause insertion or a paraphrase. The B1 R4 overlap lister ran on booklets only; half of these copies came from the Hajimete/SK/Soumatome extracts. No brief tells authors to scan the category's other examples |
| F3 | vi 勝, 真, 付 meaning | major (真, 勝) | Rule-29 borrowing from the compound partner. 勝 "tự ý" ← 勝手. 真 "ngay chính giữa" ← 真ん中, which collides with 中 "ở giữa". 付 "ở gần" ← 付近. 勝 appeared in the 破 and 受 items with "tự ý" | 勝 "thắng, giành phần hơn"; 真 "thật, không giả dối; (「ま」) ngay, đúng"; 付 "gắn vào, kèm theo; trao, gửi" | BATCH_VI_BRIEF still lacks the R2 rule from B1 |
| F4 | related pairs | minor | Gloss collisions the generator cannot see. 装 (live) "trang bị, lắp đặt" vs 設 "xây dựng, thiết lập": 設 WAS a distractor on 装's item. ja 優 「ほかより上」 vs 勝 「相手よりまさって」 (they form 優勝). vi 開 "mở ra" vs 拡 "mở rộng". 書 「字をかく」 vs 記 「書きしるす」. 真/中 as in F3 | Linked, with a compare in each language: 反↔映, 画↔映, 真↔中, 書↔記 (all in the batch); 設↔装, 置↔装, 開↔拡, 勝↔優 (live 装, 拡, 優 via the back-link files, now 19 live targets). Left unlinked because no gloss collides (checked in the dump): 地/元, 強/火, 農/薬, 受/付, 手/相, 機/能, 間/違, 気/軽, 元/気, 見/逃, 比/的, 間/世, 中/世, 手/運, 腕/指 | as in B1 R2 |
| F5 | vi 住 meaning | minor | "TRỤ (quen đọc TRÚ)" treats TRÚ as a colloquial variant. Both are dictionary readings | "TRÚ, TRỤ" | — |
| F6 | vi 「Hán Việt lừa」 claims | minor | 5 of 15 are not traps. 反省 phản tỉnh means exactly self-reflection. 予算 dự toán ≈ budget. 事情 sự tình ≈ the circumstances. 機嫌 cơ hiềm and 勝手 thắng thủ are not Vietnamese words, so nothing misleads. True traps, kept: 人間, 出世, 地味 (địa vị), 趣味 (thú vị), 行事, 上品, 陽気, 指摘 (chỉ trích), 表情 (biểu tình), 避難 (tị nạn) | 反省, 予算: "lừa" label dropped. 事情: split from 表情's trap. 機嫌, 勝手: "Âm Hán Việt (…) không gợi ra nghĩa" | BATCH_VI_BRIEF has no test for a trap: the reading must itself be a Vietnamese word with another meaning |
| F7 | ja 願 compare, 望 back-link | minor | 「望には遠くをながめる意味もあり（「希望」「志望」）」: the examples illustrate the wishing sense, not gazing | parenthetical cut | — |
| F8 | live 介 k-0591 vi | minor | "…; giúp đỡ" borrowed from 介護 (B1 厚 class). It now collides with the batch's 助 "hỗ trợ" | "GIỚI — ở giữa, làm trung gian" in `knowledge/N2/漢字.vi.json`; `make knowledge` rebuilt the page | B1 fixed 厚 but did not sweep the other live glosses |
| F9 | ja nuance ruby on non-words | minor | The 問題2 non-word distractors were given furigana kanji by kanji: 戻品《れいひん》, 住屋《じゅうおく》, 好味《こうみ》, 見延《みえん》して…. That presents fake words as readable words | ruby removed from 88 quoted non-words (checked against `pitch.readings`). Kept on real words (住宅, 興味, 補助, 消失…), on single kanji (「偉」「摘」) and on 「外れて」 | LEX_JA_BRIEF says "furigana every kanji" and has no exception for printed wrong options |
| F10 | live 直 k-0467 ja meaning (not fixed) | note | 「…元に戻すという意味もある」 prints the kanji 元 inside a meaning. On 元's item this option shows the headword itself as a lure | not edited (outside my scope). Proposed: 「…また、もとどおりにすること」 | gate: a meaning distractor should not contain the key's headword kanji |

The Hán Việt readings of the other 69 kanji are right. The dictionary reading
comes first, and multi-reading kanji list both (画 HỌA/HOẠCH, 強 CƯỜNG/CƯỠNG,
相 TƯƠNG/TƯỚNG, 難 NAN/NẠN).

**Counts:** 10 findings: 4 major (F1, F2, F3 and the 設→装 collision in F4), 5
minor, 1 note. Edits:
- 1 furigana fix and 12 examples (10 entries, 2 of them replaced twice), each
  with its vi example_note
- 5 vi meanings in the batch and 1 in the live file
- 5 vi trap claims
- 8 related pairs (16 links); 7 new compares and 4 extended ones per language;
  3 new live back-link targets
- 2 ja compare repairs
- ruby removed from 88 non-words

The vi text of the new and extended compares, and of the 3 new back-links, was
written in this QA context, which had also read the ja pane. That breaks the
"written, not translated" split for those 14 fields. They were written from the
kanji facts, not from the ja sentences. A vi-only pass may still re-author them.

## Root causes and proposed rules

- **R1 (F2)** Rule 3/R4: run the overlap lister over EVERY `refs/**/*.md` extract
  (Hajimete/SK/Soumatome example sentences), not only booklets and scripts. Also
  run it against the category's other examples. Every hit here that a scan could
  find came from a textbook line or a sibling card.
- **R2 (F3, F8)** Add B1 R2 to BATCH_VI_BRIEF verbatim. Also sweep the live vi
  glosses once for "; <sense of the compound>" tails (介 was the second).
- **R3 (F6)** BATCH_VI_BRIEF: "『Hán Việt dễ lừa』 only when the Hán Việt reading
  is itself a Vietnamese word whose meaning differs (biểu tình, chỉ trích, thú vị)."
- **R4 (F9)** LEX_JA_BRIEF: "No furigana on a printed wrong option that is not a
  word."
- **R5 (F10)** gate: WARN when a 漢字 `meaning` contains another entry's headword
  kanji.
