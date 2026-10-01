# QA report — 知識 N2 漢字 batch 7 (73 kanji, SK 99–182; 48→59 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes.

Both panes were written by Claude authors, kept apart from each other.

Files reviewed (scratch `batches/`):
- `漢字_B7.json`, `.ja.json`, `.vi.json`
- `.backlinks.json`, `.backlinks.vi.json`
- `K7_live_meaning_fix.json` (101 ja edits) and `K7vi_live_meaning_fix.json` (21 vi edits)

The originals are kept in `QAK7_orig/`. `QAK7_fix.py` applies every fix to those originals, so the round can be re-run.

Validation ran on a scratch root, `QAK7_root`:
- `.agents/` and the CURRENT live `knowledge/` (post 7e81da0, B6 merged) were copied fresh; everything else is symlinked.
- `QAK7_run.sh` applies both fix files to the copied `漢字.{ja,vi}.json`.
- It then runs `merge_batch.py`, re-pointed as `QAK7_merge.py`.
- Last, it runs the builder and `check_knowledge.py`.

The real `knowledge/` was not edited. Every live-entry fix goes through the two fix files.

## What was checked, and how

| area | method | result |
| - | - | - |
| ids / coverage | SK 別冊 list pages PDF 147–153, sliced with pypdf and read as images | All 73 ids match the page, including the 3 numbers the OCR missed: 秋133 週136 十138. Together with the 11 live ids (事 弱 手 受 住 重 出 書 色 人 世), 99–182 is complete. `group` 「ステップ1 第1回〜第14回」 is right |
| on / kun / words | the same pages | 73/73 readings match, okurigana and (他)/(自・他) marks included. Words the page lacks are attested elsewhere: 品質 (7/2016 1-5), 新聞 (7/2013 1-1), 声援 (7/2021 1-3), 社会/会社 (the page prints 社会科学) |
| `official_count` (rule 40) | Parser over the 問題1/2 sections of 31 sittings (301 items). The 10 items it misses were read by hand (7/2019 1-4; 12/2023 1-2, 1-3, 2-9, 2-10; 7/2023 1-4, 2-10; 12/2013 1-4; 7/2018 2-8). Every 問題1 sentence holding a B7 kanji was checked against its key | Only 声 counts: 1 (7/2021 1-3 声援; options しえん せいいん しいん printed). No 問題2 key holds a B7 kanji. Every other 問題1 hit lies outside the underlined word (最小限 → そんがい, 以上 → とうぼう, 海外市場 → かくじゅう, 素晴らしい → さいのう …) |
| prose option claims | All four options of every cited item printed: 12/2021 2-6, 12/2017 2-8, 7/2024 2-8 and 2-9, 7/2023 2-10, 12/2023 2-7, 7/2019 2-6, 12/2012 2-7, 7/2022 2-7, 12/2020 2-10, 12/2016 2-7, 12/2015 2-10 | All true |
| back-link base text | All 48 ja and 48 vi back-links diffed against the CURRENT live compare, sentence by sentence for every rewrite | F4. 41 ja back-links extend the live text verbatim. The three B6-first swaps (系 開 修) were built on the live text, but 系 and 修 still dropped a contrast. 地 世 気 would have undone B6 QA. 収 dropped its own sense |
| generated quizzes | All 489 `#r` and `#m` items dumped before and after the fixes. All 73 B7 meaning items and all 73 reading items read in both languages. Gloss collision scans: ja substring, vi words and bigrams, Hán Việt inside glosses, and a "tail-word" scan (another entry's gloss word, e.g. こころ, おと, いと, inside a gloss) over every unlinked pair touching B7 or a fixed gloss | F3, F5, F6 |
| live fix files | Each of the 122 edits read against its card's words, examples and the CURRENT live text. The 16 ids B6 also fixed were compared with B6 QA's final text | F5 |
| examples | 10-char windows and a ≥2-token lister over refs/**/*.md, tests/imported-*, every `knowledge/N2/*.json` (quiz stems included) and the open batches 語彙_B8, 語彙_B9 and 漢字_B8. Every hit was read for scene and frame. A separate lister ran over all 709 official 問題6 option sentences. Replacements were rescanned over 3 rounds | F1 |
| furigana | All 737 distinct ruby pairs in examples, words, prose and back-links, read in a dump | F2 |
| rule 6 / rule 18 | script; gate | clean (ナ形容詞 is a grammar label) |
| gate | scratch merge, before and after | before: 0 FAIL, 0 WARN, but 3 REVIEW lines (地 drops 「地区」, 気 drops 「空気」, 世 drops 「〜界」「世界」). After: **0 FAIL, 0 WARN**; 489 entries; back-links on 59 live entries; no REVIEW line in either language |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | 16 examples | major (西 寝 糸 主 取 図 川 四), minor (rest) | Scene and frame copies. 西 「来月から関西の支店で働くことになった」 = 文法 g-koto-ni-naru 「来月から大阪の支社で働くことになった」 (10-char hit). 寝 (昼寝 → 外が暗くなっていた) = g-adv-itsunomani. 糸 (釣り糸が岩に) = 語彙 v-o-karamaru. 主 (この地方, みかんの栽培) = 語彙 v-0482. 取 (棚の上の箱を取った) = live 手 k-1046. 図 (本棚を組み立てた) = live 組 k-0440. 車 (電車の窓から海) = live 色 k-0153. 思 (冷たい → 思わず声) = 語彙 v-o-fureru. 少 (少年が一人で旅) = 語彙 v-0850. 青 (財布がないと気づいて) = 語彙 v-o-jitabata. 親 (引っ越してきたばかり, 隣の人) = 文法 g-sura. 心 (夜道を一人で) = 語彙_B9 v-0155. 先 (注文した本が届く) = 語彙 v-o-toiawaseru. 始 (バス路線, 開始/廃止) = 文法 g-koto-kara. 四 (四つ角を右に曲がると…) = the 7/2015 問題6 misuse 「交差点を右に曲がると、行方に…」 with the right word restored (rule 39) | All 16 rewritten, each vi example_note rewritten from the new sentence. The rescans caught copies in my own drafts: 7/2025 問題8-44 (洗濯物を外に干す), live 針 k-0797 (ボタンを糸で), 7/2011 and 7/2022 問題6 (この町は川で分かれる; 大雨で川の水が茶色く濁る), 文法 g-chuushin (研修で機械の使い方), 文法 g-toiuto (子どものころの思い出), 文法 g-kiwa (退院, 手紙), 文法 g-hanmen (町, 観光客), 語彙 v-0942 (雪, 車のタイヤ), 漢字_B8 k-0238 (弟の顔が青く) and k-0232 (焼く前の肉). Final scan: no window hit; no ≥2-token hit shares scene and predicate | The author's K7_prov listed hits but did not read open-batch frames or the 問題6 option sentences. LEX_JA_BRIEF's ADDED frame-scan rule is in place, but the check is still done by eye |
| F2 | 時, 持 examples | minor (pronunciation) | 「｜兄《あに》の｜腕《うで》**｜時計《とけい》**」: the split ruby makes ▶ speech read うでとけい (rendaku lost). 「｜水《みず》とう」 reads みずとう for 水筒 (すいとう) | → 「**｜腕時計《うでどけい》**」, 「｜水筒《すいとう》」 | `check_ruby_suspects` does not join a ruby with the word it sits in. B6 R4 named exactly this (学《がく》校《こう》) |
| F3 | gloss collisions the generator cannot see | major (思/考, 止/禁, 声/音, 字/漢, 者/員, 者/手, 社/会), minor (rest) | ja 思 「…かんがえたり…」 vs 考 「…かんがえること」. 禁 「…とめること」 vs 止 「…とめること」. 声 「…くちからだすおと」 vs 音 「…おと」. 漢 「…もじのかんじ」 vs 字 「…もじ」. vi 員 "người làm một việc" vs 者 (its own compare says "người làm việc gì"). 手, as fixed by K7 (「あることをする人」), = 者 「あることをするひと」 word for word. Compound partners whose gloss names the compound (B4 R2): 社 「かいしゃ」 (会社), 習 / 学 (学習), 取 / 受 (受け取る), 時 「じかん」 (時間, 間), 心 / 精 (精神). None of these pairs co-occur in today's dump; they are linked because the sha1 ranking changes on every merge | 11 pairs linked both ways, each with a compare in both languages: the 10 the authors listed plus 者↔手. New live back-link targets: 考 学 禁 音 員 手 漢 会 受 精 間 (48 → 59). Every new live compare extends the current text verbatim, except vi 員, which is rewritten inside the 180 cap and keeps every old quoted form (merge's REVIEW is clean). The vi live fixes for 漢 ("chữ Hán") and 間 ("thời gian") are withdrawn: the links make them unnecessary, and the original glosses are better | B6 R2 (compound partners) is still not in the briefs. The authors flagged these pairs as doubts and left them open |
| F4 | back-links built on stale or compressed text | major (地 世 気), minor (系 修 収) | 地, 世 and 気 were written for the pre-B6 text. Each REPLACED the live compare and dropped B6 QA's new link sentence (「区とは「地区」で組む」, 「界とは「世界」で組む」, 「空とは「空気」で組む」). Merge printed REVIEW for all three. 系 (B6-first swap) cut 係's sense 「かかわりや、かかりのひと」; 修 (B6-first swap) cut 直's 「もとどおりにすること」, the contrast with 修's なおす; 収 cut its own sense 「収はうちに取り入れること」, which is the contrast with 領. The compressed vi back-links (開 気 失 修 損) keep every contrast; 損 drops "(việc làm, cơ hội)" from 失う and is accepted | All six rebuilt as the CURRENT live text plus the B7 sentence. 系 (96) and 地/世/気 fit unchanged. 修 drops only 「考えをふかめ」 from 研's sense; 収 drops only 領's 「国の土地」. 気 keeps the author's one real change: no ruby on the printed non-word 「気嫌」 | The B7 ja files were written before B6 merged. Only three back-links were swapped for B6-first versions; the other three were never rebased. merge's REVIEW catches dropped quoted forms, not dropped contrasts (B6 R6) |
| F5 | live gloss fixes | major (降 抱 手 善), minor (設 優 音, 去 区) | 降: K7 put back 「あめや雪」, the word B6 QA removed because it collides with 雨. 抱: 「こころにおもいをもつこと」 now glosses 思. 手: 「あることをする人」 = 者 (F3). 善: 「ひととしてのおこないが、よいこと」 now matches 偉 「おこないや、ちいがりっぱなこと」. 設: 「つくってととのえること」 changed B6's sense and moved toward 備 (設備). 優: 「ほかよりうえ」 reads as 上's gloss. 音 (live, unfixed): 「みみにきこえるもの」 prints 耳's gloss word on 耳's item. B6 glosses 去 「その場から」 and 区 「小さく」 print B7 headwords (author doubt) | 降 → 「たかいところからひくいところへおりること。また、雪などがふること。」 抱 → 「…また、きもちなどを、むねにもつこと。」 善 → 「わるいところがなく、よいこと。また、よりよくすること。」 設 → 「たてものやばしょなどを、あたらしくつくること。」 (B6's sense) 優 → 「…ほかよりすぐれていること。」 音 → 「きこえてくるもの。おと。」 去 → 「そのばから…」 区 → 「まちをいくつかにくぎった…」 The no-op 診 entry was removed. B7 耳 → 「かおのりょうがわにある、ものをきくところ。みみ。」 (it printed 音's おと). 手's text is kept; the 者↔手 link (F3) resolves it. The other 94 ja and 19 vi edits are accepted: kana-only, with the sense intact and no semantic competitor | The K7 author removed B7 headword kanji (rule 34) but did not re-run the gloss-WORD check (rule 40) against the CURRENT live text. B6 R3 asked for exactly that. The file was written before B6 QA changed 降 |
| F6 | 氏 sources | minor | The 〜氏 sense ("ông, bà") had no cited source. The SK page prints 氏 alone; the sense is printed in 12/2020 問題2-10 「西村氏の作品の中では…」 | that item added to `sources` with 「（文中に「西村氏」。数えない）」 | Rule 27 sourcing was done for words, not for the sense of a word printed bare |

## Author doubts, judged

- **Pairs to link** (思↔考, 習↔学, 止↔禁, 声↔音, 者↔員, 字↔漢, 社↔会, 取↔受, 心↔精, 時↔間): all 10 linked (F3), plus 者↔手.
- **去 「その場から」, 区 「小さく」**: kana'd (F5). 区 also loses 「ちいさく」, 小's gloss word.
- **早速 → そうそく**: accepted. It is the generator's fabricated misreading (ソウ is 早's 音, as in 開発 → ひらはつ). No dictionary reading of 早速 is そうそく (only さっそく; old さそく), and the pitch dataset does not list it.
- **Hán Việt labels that are Vietnamese words** (車 XA / 遠 "xa", 場 TRƯỜNG / 校 "trường", 前 TIỀN / 金 貨 額 賃 "tiền", 秋 THU / 収 "thu"): lures, not second answers. Every option leads with its own label, and the definition after the dash cannot gloss the asked kanji. This follows B6's 省 TỈNH / 県 ruling. Left unlinked.
- **氏 "ông, bà" sourced only by an official item**: the sense is correct and is now cited (F6).
- **Generator note, not a B7 defect**: a single-kanji word gets its kanji's other reading as a fabricated distractor (森 → しん, 石 → せき). The live set already has 顔 がん, 兄 きょう, 係 けい, 型 けい and 隣 りん, which earlier rounds accepted.

**Counts:** 6 findings: 4 major (F1, F3, F4, F5), 2 minor. Edits:
- 16 examples rewritten and 2 rubies fixed, each with its vi note
- 1 source added; 1 B7 gloss (耳 ja)
- 11 related pairs, with 11 batch compares × 2 languages
- 11 new back-link targets × 2 languages; 6 ja back-links rebased
- ja live fixes: 5 changed (降 抱 善 設 優), 3 added (去 区 音), 1 removed (診); vi live fixes: 2 withdrawn (漢 間)

The vi text of the new compares and notes was written in this QA context, which had also read the ja pane. As in B2–B6, this breaks the "written, not translated" split for those fields. They were written from the kanji facts and the Japanese sentences, not from the ja prose. A vi-only pass may re-author them.

## Root causes and proposed rules

- **R1 (F4) — PROCESS.** When a batch is written against a tree that later changes, rebase EVERY back-link onto the current live text, not only the ones the author spotted. A rewrite (not a prefix extension) needs a sentence-by-sentence diff against the live compare. `merge_batch.py` could print every non-prefix back-link with both texts, so it is read before merging.
- **R2 (F5) — RULE-UNENFORCED.** B6 R3 is in LEX_JA_BRIEF, but a fix file written before the previous QA landed reintroduced the removed word. Rule: diff a live-fix file against the CURRENT live text immediately before merging, and treat any id another batch has touched since as unread.
- **R3 (F3) — RULE-MISSING in the briefs.** Add B6 R2 verbatim to both author briefs, and add: "Any pair you flag as a link candidate is linked before hand-off, or the report says why not."
- **R4 (F2) — GATE-BLIND, second time.** `check_ruby_suspects` should WARN when a ruby run ends inside a longer dictionary word whose reading differs (腕+時計《とけい》 → うでどけい; 水《みず》+とう → すいとう).
- **R5 (F1) — saturation.** Add these scenes to the saturated list: new job at a 支店/支社, 昼寝 → 外が暗い, 釣り糸, みかん栽培, 棚の上の箱, 本棚を組み立てる, 電車の窓から海, 注文した本, 洗濯物を外に干す, a river splitting a town, 大雨 → 川が濁る.

## Merge steps for the coordinator

1. Apply `batches/K7_live_meaning_fix.json` (103 entries: 101 − 診 + 去 区 音, with 降 抱 善 設 優 changed by QA) and `batches/K7vi_live_meaning_fix.json` (19 entries: 漢 and 間 withdrawn) as `meaning` overwrites in `knowledge/N2/漢字.ja.json` and `漢字.vi.json`. Apply them to the CURRENT live files (post 7e81da0).
2. Run `python3 merge_batch.py 漢字 7`. It should print +73 entries and back-links applied to 59 live entries, with no REVIEW line. `K7_backlinks_ifB6first.json` is superseded; do not apply it.
3. Run `make knowledge`, then `make check`. Read every line.
4. Open-batch notes: 漢字_B8 k-0238 (弟の顔が青白く) and k-0232 (焼く前に肉を…) were near B7's first drafts, and B7 moved off them. 語彙_B9 v-0155 (夜道を一人で) no longer shares B7's scene.
