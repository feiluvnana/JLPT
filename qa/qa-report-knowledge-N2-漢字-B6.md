# QA report — 知識 N2 漢字 batch 6 (78 kanji, SK 1–98; 37→45 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes.

Both panes were written by Claude authors, kept apart from each other.

Files reviewed (scratch `batches/`):
- `漢字_B6.json`, `.ja.json`, `.vi.json`
- `.backlinks.json`, `.backlinks.vi.json`
- `K6_live_meaning_fix.json` (51 ja edits) and `K6vi_live_meaning_fix.json` (14 vi edits)

The originals are kept in `QAK6_orig/`.

Validation ran on a scratch root, `QAK6_root`:
- `.agents/` and `knowledge/` were copied fresh; everything else is symlinked.
- `QAK6_run.sh` applies both fix files to the copied `漢字.{ja,vi}.json`.
- It then runs `merge_batch.py`, re-pointed as `QAK6_merge.py`.
- Last, it runs the builder and `check_knowledge.py`.

The real `knowledge/` was not edited.

## What was checked, and how

| area | method | result |
| - | - | - |
| ids / coverage | SK 漢字 目次 PDF 134 (sliced with pypdf, read as an image) | All 78 ids match the 目次, including the 8 numbers the OCR missed: 屋16 回28 学35 楽36 休46 言73 口79 作96. Together with the 20 live ids, 1–98 is complete. `group` 「ステップ1 第1回〜第14回」 is right. The `related` targets checked here are also right (大190 弱127 住139) |
| on / kun / words | SK 別冊 list pages, PDF 141–147, all read as images | 78/78 match the page, every okurigana included. The (他) and (自・他) marks match the ja usage labels |
| 建つ 自動詞 (author doubt) | page convention | Kept. The page marks only (他) and (自・他). Unmarked verbs are intransitive (下がる, 曲がる, 広がる, 降りる), so 建つ is 自 |
| `official_count` (rule 40) | Parser over the 問題1/2 sections of 31 sittings (301 items). The 9 items it misses were read by hand (7/2019 1-4; 12/2023 1-2, 1-3, 2-9, 2-10; 7/2023 1-4, 2-10; 12/2013 1-4; 7/2018 2-8). Every 問題1 sentence that contains a B6 kanji was checked against its key | 0 is correct for all 78. No 問題2 key contains a B6 kanji. Every 問題1 hit is outside the underlined word (e.g. 一言 in 7/2019 1-4, 係員 in 12/2017 1-2, 危険 in 12/2016 1-4) |
| prose option claims | All four options of every cited item printed: 7/2021 2-10, 7/2014 2-10, 7/2019 2-10, 7/2017 2-10, 7/2022 2-8, 12/2019 2-9 and 2-10, 12/2024 2-6 and 2-9, 7/2018 2-9, 7/2016 2-7, 7/2025 2-7, 12/2025 2-10, 12/2015 2-6 | All true, including vi 「警護」 and 「混雑」 |
| back-link base text | Each B6 back-link was diffed against the CURRENT live compare (post d0a62f5), in both panes | All 37 ja back-links extend the current text verbatim. That includes the two repaired targets in this batch, 照 k-0785 and 拡 k-0598, so no repair is undone. 32 vi back-links extend the current text. The other 5 (療 住 講 設 製) are rewrites that keep every old element |
| generated quizzes | All 416 `#r` and `#m` items dumped, before and after the fixes. All 78 B6 meaning items and all 78 B6 reading items read in both languages. Gloss-collision scan (ja substrings, vi words and bigrams, Hán Việt inside glosses) over every unlinked pair involving a B6 entry or a fixed live gloss | F3, F4, F5 |
| live fix files | Each of the 65 edits read against its card's words, examples and quiz | F6 |
| examples | 10-char windows and a ≥2-token lister over refs/**/*.md, tests/imported-*, every `knowledge/N2/*.json` (quiz stems included) and the open batches 語彙_B7 and 漢字_B7 (there is no 語彙_B8). Every hit was read for scene and frame; the batch was also checked against itself. Replacements were rescanned over 5 rounds | F1 |
| furigana | Every ruby in examples, words, prose and back-links, 695 pairs, read in a dump | F2 |
| rule 6 / rule 18 | script; gate | clean |
| gate | scratch merge, before and after | before: 0 FAIL, 0 WARN, 37 back-links. After: **0 FAIL, 0 WARN**; 416 entries; back-links on 45 live entries; merge prints no REVIEW line |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | 19 examples | major (公 験 今 楽 駅 院 京), minor (rest) | Scene and frame copies. 公 (審判, どちらのチームにも, fairness) = 語彙 v-1258 平等, a 10-char hit. 験 (exam eve, early to bed) = 文法 g-dake. 今 (trip, sunny, good) = the official 問題6 misuse sentence 「…晴れて、妥当な天気になった」 (7/2021, 12/2014) with the right predicate put back (rule 39). 楽 (relax → いいアイデアが出る) = the 7/2022 misuse 「いいアイデアが生じない」, also SK 語彙. 駅 (fell asleep, woke at the terminal) = the 12/2016 misuse sentence 「居眠りをして…一駅延長」. 院 (grad school or a job, undecided) = 7/2025 聴解 問題2-1. 京 (dream of becoming a singer) = 語彙_B7 v-0108 and the 7/2022 script. 何 (先輩, 相談にのる) = SK 語彙. 学 (researcher of children's language) = 7/2014 問題3. 苦 (〜のにも時間がかかる) = 語彙 v-o-chuushouteki, a 10-char hit. 安 and 建 (built near the station → improvement) = 文法 g-okageda and g-ippou-da. 牛 (car stops to let something cross) = 漢字_B7 k-0179. 危 (bike down a slope) = 語彙_B7. 教 (shogi, a third time: kx-剣, kx-誘). In-batch duplicates: 漢/五, 歌/作, 今/三 | All 19 rewritten (高 only for F2). The rescans caught copies inside my own replacements and those were rewritten too: g-tte (new bakery by the station), g-ba-yokatta (spare alarm clocks), g-mochiron (料理教室), the 12/2021 問題6 misuse sentence 「牧場で牛を栽培」, kx-施 「この試験は、年に二回実施される」, the 7/2012 script (need the slip to enter the venue), g-kanenai, g-sae and g-adv-mushiro (年齢は関係ない), 漢字_B7 k-0119 and k-0159, 読解 r-setsuzokushi. vi example_notes were rewritten from each new sentence. Final scan: no window hit; no ≥2-token hit shares scene and predicate | B4 R1 and B5 R1 are still not in LEX_JA_BRIEF. The author's `K6_prov.py` listed hits but did not catch official 問題6 misuse sentences (rule 39) or open-batch frames |
| F2 | 高 example | minor (pronunciation) | 「この｜学《がく》｜校《こう》は」: the split ruby makes ▶ speech read がくこう | → 「｜学校《がっこう》」 | `check_ruby_suspects` does not join adjacent single-kanji rubies; sokuon is lost when they are split |
| F3 | gloss collisions the generator cannot see | major (員/属, 工/製, 楽/快, 界/世), minor (rest) | ja 員 「なかまやそしきに入っているひと」 vs 属 「あるなかまや、まとまりに入っていること」. 工 「どうぐやきかいで、ものをつくるしごと」 vs 製 「原料から、しなものをつくること」 (vi "nghề làm đồ" / "chế tạo sản phẩm"). 楽 「からだやこころに、むりがない」 / "thảnh thơi" vs 快 「きもちがよい」 / "thoải mái". 界 「せかいや…」 names 世界, against 世. Compound partners whose gloss names the compound's sense (B4 R2): 公平 (vi 公 "không thiên vị" vs 平 「かたよりがない」), 空気 (気 「くうきのような」), 学校 (校), 学科 and 科学 (学/科, both 「がくもん」), 区分 (区 「くぎる・くべつ」 vs 分 「わける」; vi "ngăn ra" vs "chia, tách"), 地区 (vi "khu" vs "vùng"). 係 「かかわりがある」 vs 密 「かかわりがふかい」 (密接な関係, 12/2011 1-2) | 11 pairs linked both ways, each with a compare in both languages: 員↔属, 工↔製, 楽↔快, 界↔世, 公↔平, 空↔気, 学↔校, 学↔科, 区↔分, 区↔地, 係↔密. New live back-link targets: 属 快 世 平 気 分 地 密 (37 → 45). 製's existing back-link was extended. 快's and 製's new texts keep every old contrast and quoted form. My first draft dropped 快「全体」/好「すきなこと」 and 「建設」「構造」; both were caught and restored | LEX_JA/VI briefs: the authors checked compound partners only for same-string glosses. "Names the compound's sense" (B4 R2) is not in the briefs |
| F4 | gloss borrows a compound sense (rule 29) | minor | ja 医 「…いしゃにかんするがくもん」 takes 学 from 医学. vi 家 "(nhà văn…)" takes 作家 from 作 | 医 → 「いしゃや、いしゃのしごと。」 (it then no longer competes with 学 or 治). 家 → "người theo một nghề chuyên môn" | same as F3 |
| F5 | reading quiz 三 | minor | 三's item asked 三つ, and the fabricated みつ is a dictionary reading (みつ【三つ】 = みっつ). The pitch dataset lists only みっつ | 「三つ」 dropped from `words` (みっ.つ stays in kun and in the usage prose). The item is now 三 → さん, with distractors みっ / 去る / 刺す | the dataset blind spot that rule 28's dump is there to catch |
| F6 | live fix files | minor | Three ja kana substitutions hid the B6 kanji but kept the same gloss word. 降 「あめや雪がふる」 still carries 雨's gloss word 「あめ」 (the vi fix removed "mưa" for exactly this reason). 接 「人とあって相手をする」 still carries 会's 「あう」 (the vi fix dropped "gặp gỡ"). 管 「中がからの」 reads as the particle から | 降 → 「…また、雪などがふること。」 接 → 「…また、人のあいてをすること。」 管 → 「中がからっぽの細長いつつ…」. The other 48 ja edits and all 14 vi edits are accepted: kana-only or a dropped gloss word, with the sense intact and no new collision | The ja author removed headword kanji (rule 34) but did not re-run the gloss-word check (rule 40) on the result |
| F7 | vi back-link 険 | minor | Kept 剣 "là thanh gươm", a sense B5 F4 cut from 剣's own card (no ref attests it) | → 「剣」 có trong 「真剣」 (nghiêm túc), bộ 「刂」 | the author extended the live text without re-checking it against B5 |
| F8 | vi 後 nuance | minor | 「あと」 (thời gian sau) is presented as time-only. あと is also spatial (rule 9) | → 「あと」 (「後」: sau đó) | — |

## Author doubts, judged

- **Compound partners** (界↔世, 区↔分/地, 験↔受, 公↔平, 空↔気, 学↔校, 国↔家, 作↔家, 楽↔快):
  - Linked: 界↔世, 区↔分, 区↔地, 公↔平, 空↔気, 学↔校, 楽↔快 (plus 学↔科, F3).
  - 国↔家: not linked. 国家 is named only by 国's own gloss; 家's gloss does not compete.
  - 作↔家: not linked. vi 家 was reglossed instead (F4).
  - 験↔受: not linked. After the vi fix, no gloss collides.
  - None of these pairs co-occur in today's dump. They are linked because the sha1 ranking changes on every merge.
- **省 TỈNH vs 県 "tỉnh".** A lure, not a second answer, so it is left unlinked. Every vi option leads with its own Hán Việt label, and 省's definition after the dash ("xem xét lại; lược bớt") cannot gloss 県. The two are not paired today. If an owner wants it closed, the cheapest step is a vi-only compare on 県. A ja compare would need an unsourced claim about 省.
- **受 vi fix loses the exam sense.** Accepted. 「dự thi」 is 受験's sense borrowed from 験 (rule 29), and the ja gloss never had it. 受験 stays in `words` and usage. Restoring the sense would require a 受↔験 link.
- **険 compare keeps 剣 "thanh gươm".** A defect, fixed (F7).
- **建つ 自動詞.** Correct by the page convention (see the table).
- **上京 glossed beyond the page.** Accepted. 「地方からとうきょうへ出ること」 is the word's standard modern sense, and the page prints the word. 京's 「とくに、とうきょう」 is defensible (京浜/京葉). The singer example was replaced anyway (F1).
- **何か dropped.** Right. なんか is a real reading, and the generator would have fabricated it from 何's なん. The prose keeps 「何か」 under なに, as the page does.

**Counts:** 8 findings: 2 major (F1, F3), 6 minor. Edits:
- 19 examples (+1 ruby fix), each with its vi note
- 1 word removed
- 11 related pairs, with 11 batch compares × 2 languages
- 8 new back-link targets and 1 extended, × 2 languages; 1 vi back-link fixed
- 2 glosses (医 ja, 家 vi) and 1 vi nuance
- 3 entries in `K6_live_meaning_fix.json`

The vi text of the new compares and notes was written in this QA context, which had also read the ja pane. As in B2–B5, this breaks the "written, not translated" split for those fields. They were written from the kanji facts and the Japanese sentences, not from the ja prose. A vi-only pass may re-author them.

## Root causes and proposed rules

- **R1 (F1) — RULE-UNENFORCED, third time.** Put B4 R1 / B5 R1 into LEX_JA_BRIEF verbatim. Add: "Grep the official 問題6 options (every sitting) for your scene; a misuse sentence with the right word restored is a copy (rule 39). Read the open batches (`batches/*_B*.json`) as part of the module." Common scenes are saturated: station, 改札, alarm clock, grandparent teaching, shogi, exam eve, trip weather, 年齢は関係ない, 年に二回. Authors should start from an unusual setting.
- **R2 (F3/F4) — RULE-MISSING in the briefs.** Add B4 R2 to both author briefs: "For every `words` compound whose other kanji is an entry, link it when EITHER gloss names the compound's sense (くうき, せかい, がくもん, không thiên vị), in either language."
- **R3 (F6) — RULE-GAP.** A live-gloss fix that swaps a kanji for kana must re-run the gloss-WORD check (rule 40), not only the kanji check (rule 34). Mirror whichever pane's fix removed a collision.
- **R4 (F2) — GATE-BLIND.** `check_ruby_suspects` should WARN when two adjacent single-kanji rubies form a word the pitch dataset reads differently (学《がく》校《こう》 vs がっこう).
- **R5 (F5) — DATA-BLIND.** `pitch.readings` lacks みつ for 三つ. Consider a small override list of variant readings (みつ【三つ】, よつ【四つ】) consulted by `invalid_readings`.
- **R6 (F3 base text) — PROCESS.** `merge_batch.py` lists dropped quoted forms but not dropped contrasts. My own first draft of the 快/製 back-links dropped two contrasts that the REVIEW check would not have flagged. A reviewer should diff each rewritten (non-prefix) back-link against the live text sentence by sentence.

## Merge steps for the coordinator

1. Apply `batches/K6_live_meaning_fix.json` (51 entries, 3 changed by QA) and `batches/K6vi_live_meaning_fix.json` (14, unchanged) as `meaning` overwrites in `knowledge/N2/漢字.ja.json` and `漢字.vi.json`.
2. `python3 merge_batch.py 漢字 6`. It should print +78 entries and back-links applied to 45 live entries, with no REVIEW lines.
3. `make knowledge`, then `make check`. Read every line.
4. Open-batch note: 漢字_B7 k-0179 (car stops for a crossing) and k-0159 (〜の出し方を教えてくれた) are no longer shared with B6.
