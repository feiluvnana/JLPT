# QA report: knowledge/N2 語彙, batch 3 (64 words, 128 examples, 13 → 19 live back-links)

Reviewed 2026-09-30/10-01 by a fresh-eyes context that authored none of the batch. Files are in the
coordinator's scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B3.json` | 5427d6740441 | 13888b429bea |
| `語彙_B3.ja.json` | 29684891b9cc | 3d2bb4ad9d9b |
| `語彙_B3.vi.json` | 15a8faac5023 | 5409452cee54 |
| `語彙_B3.backlinks.json` | bc82f586be75 | 9d66eb70dbb7 |
| `語彙_B3.backlinks.vi.json` | a9ecc1311a30 | 56fbc3c6de5f |
| live `knowledge/N2/語彙.json` | a76db7460454 | 26b741687506 |
| live `knowledge/N2/語彙.ja.json` | 8db5f4b0d162 | fe4034448e26 |
| live `knowledge/N2/語彙.vi.json` | 6ef06b9a4363 | 0e4f13bf5c95 |

## Verdict

`QA: FAIL → fixed (5 finding classes: 11 examples, 1 live mis-credited count, 8 look-alike links, 4 prose fields). 0 content findings are open after the fixes.`

**Validation.** `QAV3_gate.py` copies `.agents/` and `knowledge/` into `scratchpad/QAV3_root`. It applies the live
絶える fix there, then runs `merge_batch.py`'s own code with REPO set to the scratch root. That code merges B3, applies
both back-link files and checks book order. The script then rebuilds `語彙.html` with
`build_knowledge.build_category` and runs `check_knowledge.check_category`. The result is **0 FAIL, 0 WARN**: 172
entries, 310 generated items (138 reading and 172 meaning), 19 live entries back-linked, cards in book order. The first
post-fix run failed one band (vi さっさと compare, 183 of 180 characters). I trimmed it and re-ran.

**Live files.** I then patched the live 絶える entry (§2) and ran `make knowledge LEVEL=N2`. `check_knowledge.py`
reports **0 FAIL, 0 WARN**. `make check` exits 0 ("All checks passed"). Its one knowledge-related warning was that
drill pages were stale against the new `語彙.json`. `make drill LEVEL=N2` cleared it. The other 225 warnings concern
the exam pools and papers. They predate this work, and none is on a knowledge line.

**No reading is wrong.**

## 1. Readings, Hajimete numbers, senses

- **Readings.** I checked all 64 by hand. 53 have a kanji headword, and every one of them has a generated reading item.
  28 readings are confirmed by an official 問題1 key or a 問題2 kana stem that I read in `booklet.md` and the key. For
  example: 12/2018 1-5 しょり, 12/2014 1-3 けいぞく, 7/2011 1-5 しきゅう, 12/2025 1-3 とういつ, 7/2021 1-4 かたむいて,
  12/2019 2-8 ようき and 12/2024 2-8 うやまう. The rest are standard readings. The 11 katakana/kana words get no
  reading item, which is correct.
- **Furigana.** I extracted and read all 782 distinct ruby pairs in the five files, plus the new text. There are no
  errors. The pairs checked in context include 組織's 組《そ》/織《しき》, 志《こころざし》/志《し》, 受《じゅ》 (for
  「受ける」の「受」), 一《いつ》 in 統一, 三十分《さんじゅっぷん》 and 七十歳《ななじゅっさい》.
- **Reading distractors.** No distractor is a valid reading of its headword. 絶えず is offered たえる (絶える) as a
  distractor, which is another entry's reading, not its own.
- **Hajimete numbers.** I opened PDF pp. 81, 93, 106, 118, 119, 136, 141, 142, 158, 166, 171 and 174. They confirm the
  cited page for 絶えず No.458 (p.93), 上達 537 (p.106), 目上 730 and 敬う 732 (p.136), 専念 769 and 悔やむ 770 (p.142),
  展開 851, 評判 853 and 評価 854 (p.158), 陽気 929 (p.171), and 荒れる 948 and 傾く 949 (p.174). Every `group` matches the
  section header on its page.
- **陽気's two senses.** Both are sourced. Hajimete p.171 prints both: (名) 「今日は陽気がいい」 for the weather sense and
  (ナ形) 「彼は本当に陽気な人だ」 for the cheerful sense. The page's note says the noun refers to weather and the ナ形 to
  personality. The ナ形 sense also covers music: the cited 12/2019 問題2-8 stem is 「その店にはようきな音楽が流れていた」.
  That supports 「陽気な音楽」 in the ja usage and the vi meaning.
- **Other senses** (rule 27). 荒れる ①② and 傾く ①② are on p.174. 展開 is on p.158 and in the official 7/2021 key
  「ストーリーの展開」. 充実's life sense is the Hajimete example 「毎日が充実」, and its content sense is the
  12/2011 and 12/2017 stems 「福祉が充実している」.

## 2. official_count: hit by hit for all 64, plus the live fix

`QAV3_find.py` prints every parsed 問題1–6 item whose stem or options contain the word's kanji stem or kana. The
parser could not split 12/2010 into items, so I grepped that booklet by hand. It adds only the シーズン key
(12/2010 4-18, already cited), a 上達 distractor (4-17), a 荒れて distractor (2-8) and the stem-only 分野 (5-26).

- **All 64 counts are correct**, including all 5 counts of 2: 帰省 (12/2020 2-7, 7/2025 5-24), 優秀 (12/2024 1-1,
  12/2011 5-25), 競う (7/2016 1-2, 7/2021 2-9), 中断 (12/2015 6-31, 12/2022 6-28) and 傾く (7/2013 2-8, 7/2021 1-4).
- **Excluded hits.** Distractor-only: 上達 (7/2021 4-14), いっせいに 一斉に (12/2014 4-19), 受け入れる (7/2016 4-20),
  引用 (7/2011 4-20, 7/2014 4-17), 継続 (12/2018 4-17), 評価 (7/2010 4-18), ステージ (12/2018 3-14), 荒れる (7/2022 4-16,
  7/2023 1-2), 傾く (12/2012 4-16, 12/2013 4-21), 競う (12/2015 2-8, 12/2025 1-4), 敗れる (12/2022 1-3), 除く (7/2018
  2-10), 悔やむ (7/2019 1-1) and 敬う (12/2025 2-9). Stem-only: 処理 (7/2025 6-28), 充実 (12/2011/12/2017 2-8), 分野
  (12/2022 4-16, 12/2010 5-26), 方針 (12/2022 5-23), 演技 (12/2020 4-14) and 評価 (7/2013 4-20, 7/2014, 7/2019 5-23).
  Affix items (語形成): 分野 7/2022 3-11 (異〜), シーズン 12/2011 3-15 (来〜) and 方針 7/2021 and 7/2024 3-13. 12/2014
  2-8 やぶれて keys 破れる (live), not 敗れる. I checked every source note that quotes a distractor against the booklet
  line; all are real.
- **C1, LIVE: 絶える (v-0391) 1 → 0.** It credited 12/2023 問題2-8, whose key is 絶えず, this batch's v-0458 (rule 10).
  A search of every sitting for 絶え/たえる/たえない finds no other hit. **Fix in the live files:**
  - The 12/2023 source is removed, and so is SK 語彙 p.132, which is about the adverb 「絶えず」 and is now cited on
    v-0458.
  - `official_count` is 0 and the tag 問題2 表記 is dropped.
  - ex2 showed 絶えず, a separate card now: 「川の水は一年中絶えず流れている」. It became
    「卒業して十年たつうちに、彼との連絡はすっかり絶えてしまった」, which is the "die off" sense on p.81.
  - In both languages, the usage no longer teaches 絶えず, and the nuance no longer describes the 表記 item. The new
    nuance explains 「〜が絶えない」. The new vi example_note is written from the Japanese.
  - The back-link compare in both files already contrasts 絶える with 絶えず, so it now matches the card.

## 3. Generated quizzes: every item dumped and read, in both languages

`QAV3_dump.py` runs `quiz_gen.generate()` over the merged 172 entries. The dumps are `QAV3_quiz.txt` (pre-fix) and
`QAV3_quiz2.txt` (post-fix). `QAV3_mq.txt` holds the 140 meaning items that have a B3 key or a B3 distractor.

- **Reading items.** They are sound (§1).
- **Meaning items.** No current distractor is also a correct gloss of its key. The closest pairs are たちまち with the
  distractor いっせいに (同時にそろって is not すぐに) and 徐々に with 絶えず; I kept both. The fixes changed only the
  処理 gloss text. No distractor entry and no key position moved.
- **Look-alikes the vi author named.** Most are different pos, or not paired today. The generator only *prefers* the
  same pos, so these links are preventive (rule 28 addition, B2). My verdicts:

| pair | verdict |
|---|---|
| 敬う / 尊重 (live v-0014) | **Link.** 相手を尊いものと思って大切にする vs 価値のあるものとして大切にすること: either gloss answers the other. `related` both ways; compare in both languages (a person, ancestors or gods vs opinions and individuality). |
| 充実 / 豊か (live) | **Link.** 中身が十分に満ちている vs たっぷりあって満ちている. |
| 多彩 / 豊か (live) | **Link.** Both are ナ形容詞, so they are likely to be paired. vi "Đa dạng" vs "Dồi dào, phong phú": "phong phú" also reads as "varied". The live 豊か compare now covers 乏しい, 豊富, 充実 and 多彩. |
| 一気に / さっさと (live) | **Link.** Both are 副詞. 早く物事をする reads as a gloss for 一気に片付ける. |
| 任せる / 頼る (live) | **Link.** Both are 動詞. 任せる's own gloss says 頼んで, and vi "nhờ cậy" reads as 任せる. |
| 果たす / 完了 (live) | **Link.** 最後までやりとげる vs 全部終わること. |
| 専念 / 努める (live) | **Link.** vi "dốc sức" vs "dồn sức vào một việc". |
| 至急 / さっさと (found in QA) | **Link.** 至急's vi "gấp" vs さっさと's "làm nhanh cho xong". 至急 is 名詞・副詞, so a 副詞 distractor can reach it. |

The new live back-links (6 entries) go in the back-link files. That makes 19 live entries, up from 13: 尊重, 豊か,
さっさと, 頼る, 完了 and 努める are added, each with a complete new compare in both languages. さっさと's compare keeps
its earlier point, taken from the official misuse: rain and objects take たちまち, not さっさと. I wrote every compare
from the items, not translated from the other language.

## 4. Examples: provenance, sense, naturalness

The 10-char scan (`QAV3_prov.py`) covers `refs/**/*.md`, `tests/imported-*`, every scratch batch and `knowledge/**`. It
found only function-word overlaps. Then came the rule 13/21 table (`QAV3_table.txt`). It puts every example beside the
Hajimete example on its page, the SK/Soumatome 語彙 lines, and the stem of every official item in `sources` (§2 list).

| # | entry | finding | fix |
|---|---|---|---|
| E1 | 処理 ex1 「この工場では…古紙を処理している」 | Same frame as Hajimete 「自治体がこの地域のごみを処理している」: an organisation disposing of waste. | → 「事故の処理が終わるまで、この道路は通れません」 |
| E2 | 充実 ex1 「この病院は、最新の設備が充実している」 | Cross-module duplicate: 文法 quiz stem 「このホテルは、温泉とかプール（　）設備が充実している」. | → 「この大学は、留学生のための相談窓口が充実している」 (a library full of books was avoided; it is 12/2019 充満's scene) |
| E3 | 充実 ex2 「ボランティアを始めてから、週末が充実するようになった」 | Hajimete frame 「日本に留学して以来、毎日が充実している」, plus the cited 12/2024 key 「…仕事ができて、毎日が充実している」. | → 「子育てと仕事で忙しいけれど、今の生活はとても充実している」 |
| E4 | うなずく ex1 「…息子は黙ってうなずいた」 | The cited 12/2019 問題4-19 scene: silence, then a nod as the answer. | → 「先生の話に、学生たちは何度も大きくうなずいていた」 |
| E5 | 専念 ex2 「父は会社を辞めて、今は畑仕事に専念している」 | Hajimete 「会社を休んで、育児に専念しようと思う」. My first rewrite (やめて…専念することにした) matched 7/2013 4-21 and 7/2016 6-30, so I discarded it. | → 「今年の夏は家にこもって、卒業論文の仕上げに専念するつもりだ」 |
| E6 | 展開 ex1 「このドラマは、毎回話の展開が早くて…」 | The cited 7/2021 key 「この漫画は、ストーリーの展開が面白い」 (a fiction's story development). | → 「この試合は、後半に入って思いがけない展開になった」 |
| E7 | 多彩 ex2 「歌もダンスも得意で、多彩な才能の持ち主だ」 | The cited 12/2018 key 「小説家や画家として多彩な活動」 (one person, many talents). | → 「この店では、季節の野菜を使った多彩な料理が楽しめる」 |
| E8 | あいにく ex2 「窓側の席を頼んだが、あいにく満席だと言われた」 | SK 「本屋に行ったのだが、あいにく売り切れだった」: asked for something, but none was left. I rejected alternatives that matched the cited 12/2013 key (a prior engagement) or the SK 留守 line. | → 「楽しみにしていた遠足の日は、あいにく朝から強い雨だった」 |
| E9 | 傾く ex2 「近くに大きなスーパーができてから経営が傾いてきた」 | Cross-module duplicate: 文法 example 「駅前に大型スーパーができてから、商店街の客は減る一方だ」. | → 「社長が急に亡くなってから、その旅館の経営は少しずつ傾いていった」 |
| E10 | せめて ex1 「せめて朝ごはんだけは食べたほうがいい」 | The ja usage says せめて is used in a wish or hope sentence, and this example is advice. The vi usage had widened the rule to "hay khuyên người khác", which no cited page supports. | → 「忙しくても、せめて週に一度は家族そろって夕食を食べたい」. The vi usage now covers 〜たい・〜てほしい only. |
| E11 | live 絶える ex2 | Taught the other headword 絶えず (§2). | as §2 |

Every changed example has a new vi `example_notes` translation, written from the Japanese. A scan of the new sentences
against refs, knowledge and all batches is clean.

## 5. Prose

- **Official-distractor claims.** I checked every quoted option list in both languages against the booklet lines. All
  are real, including 施設 「支接」「施接」「支設」, 行事 「ぎょうごと」「こうごと」「こうじ」, 帰省 (the 5-24 wrong options),
  至急 「しっきゅう」「ちっきゅう」「ちきゅう」, 競う 争/戦/討, 勢い 乱/荒/暴, 傾く 頃/倒/到 and 中断's six misuses across
  two sittings. Short quotes of official misuse fragments follow the B1/B2 practice.
- **P1: ja 処理 meaning.** 「集まった物事を、目的に合わせて片付けること」 restricted the word to *accumulated* things.
  → 「仕事や問題、ごみなどを取り扱って、片付けること」.
- **P2: vi 展開 usage (the soft false friend).** It said "Hán Việt 'triển khai', **nhưng** nghĩa cần nhớ ở đây là 'diễn
  biến'". The "nhưng" framed triển khai as wrong, yet Hajimete p.158's own Vietnamese gloss is "triển khai, tiến triển,
  diễn tiến" (and 事業を展開する is real). → "Hán Việt 'triển khai'; ở thẻ này cần nhớ nghĩa 'diễn biến'…". The
  collocation list also gained 「思いがけない展開」 for the new example.
- **P3: vi せめて usage** (E10), and **P4: vi あいにく usage** (the collocation now matches the new example).
- **Checked without change.**
  - Readings and restrictions: 除く vs 省く, 優秀 (both syllables long), 志望 vs 希望, 充満/延期/特別/転職/思い出す/受け取る
    as the correct words for the official misuses, and 専念's 「〜に専念する」 (every official key uses に).
  - The Hán Việt notes: xử lý, kế tục (≠ nối nghiệp), xuất thế (≠ lánh đời), dương khí, đặc thù, ưu tú, phạm vi, phân
    dã, thụ giảng, giảng sư, diên trường, từ thoái.
- **vi quoting.** A script found no Japanese outside 「」 except the grammar label ナ形容詞 (allowed by rule 6).
- **Citations in prose.** There are none in any language: no sitting date, SK or page reference.
- **Translation check.** vi is not a translation of ja. The collocations, framing and trap notes differ throughout.
- **Bands.** After the fixes, everything is within the bands. The largest fields are the ja 豊富 back-link compare at
  93 of 100 and the vi 一気に compare at 167 of 180.

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| C1 (絶える credited with 絶えず's key) | 絶える was authored in B1, before 絶えず had its own card. Rule 10 ("a hit whose keyed string is another entry's headword belongs to THAT entry") was never re-applied when a later batch added the headword. | Add to LEX_JA_BRIEF: *when your batch adds a headword, grep the live entries' `sources` for its form and move any hit credited to a neighbour (絶える ← 絶えず, 破れる/敗れる).* |
| E1, E3, E5 (Hajimete frame), E4, E6, E7 (cited official key), E8 (SK line) | The B2 rule (print one table per entry) exists. The author's copies change nouns but keep the Hajimete/official *frame*: "since X, every day 充実", "quit Y, 専念 to Z", "one person with many talents". | Extend the LEX brief: *compare the frame (cause → predicate, subject type), not just the scene nouns; the entry's sense forces the predicate, so vary the subject and cause.* |
| E2, E9 (cross-module duplicates) | The provenance corpus includes `knowledge/**`, but only a 10-char scan runs on it. The scene of 文法 stems and examples is never compared. | Rule 11 is category-wide; widen it to *the whole knowledge module* for 語彙/漢字 examples (grep the headword's key collocation in `knowledge/N2/文法*.json`). |
| E10, P1 | An example contradicted its own usage line, and a meaning added a restriction (集まった). This is rule 15 applied to the entry's own examples. | Add to rule 15: *the entry's own examples must satisfy every restriction its prose states, in every language.* |
| the unlinked look-alike pairs (8) | The vi author flagged them but may not edit the shared file, and the ja author's dump showed no collision *today*. | Rule 28 addition (B2) already says "across pos and batches". Add: *the vi author's flagged pairs are linked by the coordinator or QA before merge, with the partner's back-link in the backlinks files.* |
| P2 (false-friend framing) | A contrastive claim about the Vietnamese word, not checked against Hajimete's printed VI gloss. | Add to BATCH_VI_BRIEF: *a Hán Việt "false friend" note must not contradict the Vietnamese gloss printed in Hajimete for the word.* |

## For the coordinator

- **Merge.** Run `merge_batch.py 語彙 3`. It now applies 19 back-links (13 from the authors, 6 from QA). Then run
  `make knowledge`, `make drill LEVEL=N2` (the drill pages bake `語彙.json`) and `make check`.
- **Live edit already made.** 絶える (v-0391) is fixed in `knowledge/N2/語彙*.json` (§2), and I rebuilt the knowledge
  and drill pages. Keep this edit when merging: the merge reads the live files, so nothing overwrites it.
- **Dropped words.** The author dropped 志す 535, 区切る 623, ぐっと 763, 負う 764, 逃す 772 and 占い 900. I confirmed each on
  its Hajimete page (pp.106, 118, 141, 142, 166). All are genuine headwords with 0 official hits. They are now in the
  new "語彙 batch 3 follow-up" section of `references/inventory/N2.md`. The note records that 区切り (the ＋ word of
  No.623) is the 12/2025 問題6-30 headword.
- **Not mine.** `knowledge/N2/漢字.vi.json` has an uncommitted change that this QA did not make. An untracked
  `CLAUDE_YOU_MUST_READ_THIS.md` in the repo root asks for the full 2,600 語彙 / 1,000 漢字. It was out of scope for this
  QA, so I did not act on it.
