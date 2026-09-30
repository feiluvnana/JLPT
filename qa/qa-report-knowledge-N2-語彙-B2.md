# QA report: knowledge/N2 語彙, batch 2 (56 words, 109 examples)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. Files are in the coordinator's
scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B2.json` | 139cab675ea1 | 9df0c9628210 |
| `語彙_B2.ja.json` | ccc99865245c | f8ffed46d8ac |
| `語彙_B2.vi.json` | f82c87926af0 | b4e2be56b365 |
| live `knowledge/N2/語彙.json` | 8e64cd274a41 | 6294ce323ccf |
| live `knowledge/N2/語彙.ja.json` | 02efa273ddb4 | 761528045247 |
| live `knowledge/N2/語彙.vi.json` | 40ab13c5b6d4 | d09fcc1f92a3 |

## Verdict

`QA: FAIL → fixed (6 finding classes: 17 examples, 1 count, 1 source, 3 look-alike links, 3 prose fields; plus 8 live back-links). 0 content findings are open after the fixes.`

**Validation.** I copied `.agents/` and `knowledge/` into a scratch copy (`scratchpad/QAV2_root`), applied the live
back-link patch there, merged B2 into the 52 live words, rebuilt `語彙.html` with `build_knowledge.build_category`, and ran
`check_knowledge.check_category`. The result was **0 FAIL, 0 WARN**: 108 entries, 193 generated items (85 reading and
108 meaning), integrity rules kept, cards in book order.

**Live files.** After that I patched the live files (the back-links in §6), ran `make knowledge LEVEL=N2`, and ran
`check_knowledge.py`. It reports **1 FAIL, 0 WARN**. That FAIL is expected: `every related id exists` fails because the
9 new live back-links point at B2 ids that exist only after the merge. `merge_batch.py 語彙 2` clears it. Its own
related-id check passes on the merged set, as the scratch run shows.

**No reading is wrong.**

## 1. Readings, Hajimete numbers, headwords

- **Readings.** I checked all 56 `reading`s by hand. 38 are confirmed by an official 問題1 key or a 問題2 kana stem
  that I read in `booklet.md` and `key.md`. For example: 7/2016 問題1-4 おさめた, 12/2017 問題1-2 じゅうなん,
  12/2019 問題1-1 ひとしく, 7/2023 問題1-3 もはん and 12/2015 問題1-3 そんがい. The rest are standard readings.
- **Furigana.** I extracted and read all 675 ruby pairs in the three files, and again for the new text. There are no
  errors. 十分 is read じっぷん for minutes and じゅうぶん for "enough"; 入り口 uses 口《ぐち》.
- **Hajimete numbers.** I opened PDF pp. 11–13, 15–16, 45, 56, 140, 148, 150, 161, 175, 196, 209 and 257. That confirms
  23 of 56 entries, including **all 8 inventory rows the author corrected**: 役目 = No.6 (p.11), 尊重 = No.14 (p.12),
  着々 = No.758 (p.140), 勇ましい = No.792 (p.148), 文句 = No.874 (p.161), 傾向 = No.961 (p.175),
  刺激 = No.1147 (p.209) and 乏しい = No.1428 (p.257).
- **Related words.** The ＋ and ↔ related words cited for `v-o-*` ids are printed where the author said. 永久に is the
  ＋ of No.267 (p.56), テクニック the ＋ of No.804 技 (p.150, 第7章 Section 1 競技), 好調 the ↔ of No.1071 不調 (p.196),
  and 豊かな the ↔ of No.1428 (p.257). The `group` labels match the chapter/section of those pages.
- **Senses.** The SK 語彙 senses are confirmed on the page or in the extract: くどい ①② and 険しい ①② (PDF 107), 削る ①②
  (PDF 95), and いったん ① with 愚痴 in the 絶えず line (PDF 132).
- **Excluded senses (rule 27).** The vi author left four senses out on purpose: 会計 = accounting, 豊か = wealthy,
  柔軟 = physically supple, 辛い = つらい. I checked the ja pane, the examples and the usages, and none of them uses those
  senses either. For 辛い, the valid reading つらい is never offered as a reading distractor.

## 2. official_count: hit by hit for all 56

`QAV2_items.py` parses every sitting's 問題1–6 into items with keys. `QAV2_find.py` prints every item whose stem or
options contain the word, in its kanji and kana forms. I read each hit.

- **55 counts are correct.** I excluded distractor-only hits, stem-only hits and a 語形成 stem: 恵まれる 12/2010 1-2,
  頼もしい 12/2017 4-22, 直接 7/2010 5-23, 催促 7/2023 4-19, 活気 7/2013 4-20, 避難 7/2012 4-17, 好調 7/2012 4-21 and
  12/2012 4-22, 険しい 7/2011 2-7, 7/2014 4-18 and 7/2015 4-20, 柔軟 7/2016 4-16, 節約 12/2024 4-16 and 12/2025 4-16,
  返品 12/2016 3-14 (stem), 豊か 7/2012 3-13 (stem), and 着々 7/2012 6-32 (an option of 合同).
- **Every count ≥ 2** was re-read. 乏しい 7/2015 1-5 = 12/2021 1-2 is a reprint and is already noted. 永久に 7/2017 2-10
  and 12/2021 2-10 are **not** a reprint: the stems differ.
- **C1: 乏しい 2 → 3.** 7/2012 問題6-28 is a 用法 item with the headword **とぼしい** printed in kana. Key 2 is
  「この国は天然資源にとぼしい」. The author's search missed it. **Fix:** added the source, `official_count` 3, and the
  item's misuses in the nuance of both languages.

## 3. Generated quizzes: every item dumped and read, in both languages

`QAV2_dump.py` calls `quiz_gen.generate()` on the merged 108 entries (live plus B2). The dumps are `QAV2_quiz.txt`
(pre-fix) and `QAV2_quiz2.txt` (post-fix).

- **Reading items.** No distractor is a valid reading of its headword.
- **Meaning items.** No current distractor is a correct gloss of its key. The fixes changed no generated item. The three
  pairs below are not paired today, so the links are preventive.

The vi author flagged three pairs. My verdicts:

| pair | verdict |
|---|---|
| あらかじめ / 備える (v-0942) | **Link.** 備える's gloss 「前もって準備しておく」 / "chuẩn bị sẵn từ trước" reads as a gloss of あらかじめ, as in あらかじめ〜ておく. Today the pos differs, but the generator only prefers the same pos, so a thinner pool would pair them. `related` both ways, and `compare` in both languages. The live 備える compare is rewritten to cover 用心 and あらかじめ. |
| 生じる / 続出 (v-1163) | **Link.** 生じる's vi gloss "Phát sinh, nảy sinh (vấn đề…)" is a plausible answer for 続出, whose 出 is "xuất". 続出 is 同じようなことが次々に起こる. `related` both ways, and `compare` in both languages (one occurrence vs a series). |
| 活気 / 和やか | **Link.** The ja glosses are distinct: lively vs calm and harmonious. The vi glosses both describe an atmosphere ("không khí sôi động" and "vui vẻ (bầu không khí)"), so "vui vẻ" could be picked for 活気. `related` both ways. The live 和やか compare now covers 温厚, 鮮やか and 活気. |

## 4. Examples: provenance, sense, naturalness

The 10-char window scan found only function-word overlaps (「ことはできなかった。」, 「コンサートのチケット」). Its corpus was
`refs/**/*.md`, `tests/imported-*`, every scratch batch and `knowledge/**`. Then I did the rule 13/21 comparison by
hand. Each example was set against the Hajimete example on its page (and on its `related` entries' pages), the SK 語彙
lines, and **every official item in `sources`**.

| # | entry | finding | fix |
|---|---|---|---|
| E1 | 逆らう ex1 「川の流れに逆らって、ボートをこいだ」 | Same scene and predicate as SK PDF 96 ① 「流れに逆らって川上に泳ぐ」 (moving against a river current). | → 「時代の流れに逆らって、祖父は今もパソコンを使わずに手紙を手で書いている」 |
| E2 | ぐち ex2 「ぐちを言う前に、自分で動いてみなさい」 | A copy of Hajimete No.874 文句 ② 「文句ばかり言っていないで、行動しなさい」. That is the page of the related entry 文句. | → 「隣のおばあさんは、ひざが痛いとぐちをこぼしながらも、毎朝の散歩を欠かさない」 |
| E3 | くどい ex1 / ex2 | ex1 (a manager repeating the same warning) matches SK ① 「先輩は何度も同じことを言って話がくどい」. ex2 (a cake with layers of cream, 少しくどい) matches SK ② 「バターが大量に使われていて、少しくどい」. | → a novel whose repeated explanations make the reader stop reading. → 「若いころは脂の多い肉が好きだったが、最近はくどく感じるようになった」 |
| E4 | 催促 ex1 「なかなか返してくれないので、友人に催促した」 | Same frame as Hajimete No.198 「料理がなかなか来ないので、催促した」. | → 「取引先に代金の支払いを催促したが、まだ入金がない」 |
| E5 | 刺激 ex1 / ex2 | ex1 「この薬は胃への刺激が強い」 matches Hajimete ① 「この化粧品は刺激が強くて」. ex2 「好奇心を刺激するような絵本」 matches the cited 12/2022 問題1-2 「絵を見て、想像力が刺激されました」. | → 「目に強い刺激を感じたら、すぐに水で洗ってください」. → 「ライバルの活躍に刺激されて、彼も毎朝走るようになった」 |
| E6 | 乏しい ex1 / ex2 | ex1 (a region short of water) matches the newly cited 7/2012 「この国は天然資源にとぼしい」. ex2 「彼は経験に乏しいが…」 has Hajimete's frame 「彼は想像力が乏しく…」. | → 「このチームは若い選手が多く、大きな試合の経験に乏しい」. → 「このお弁当は彩りに乏しいので、ミニトマトを添えた」 |
| E7 | 豊か ex1 「この地方は水が豊かで、昔から米作りが盛んだ」 | Same frame as SK PDF 152 「この辺りは自然が豊かで…」 and the cited 7/2021 「故郷は自然がゆたかなところ」. | → 「森の中を歩くと、豊かな緑に心が落ち着く」 |
| E8 | 節約 ex1 「電気代を節約するために、…すぐ消している」 | Same frame as the cited 7/2023 問題4-17 「食費を節約するために、なるべく外食をしないようにしている」. | → 「旅行中は、バスに乗らずに歩いて交通費を節約した」 |
| E9 | 模範 ex1 「新入社員のよい模範だ」 | Same scene as the cited 7/2013 問題1-5 「教師は生徒の模範となるような行動」 (a senior as a model for juniors). | → 「田中さんの作文は、模範としてクラスで読み上げられた」 |
| E10 | 頼もしい ex1 「…見回ってくれて、頼もしかった」 | Same predicate as the cited 7/2016 問題4-22 「…助けてくれて、とても頼もしかった」. | → 「…家の周りを見回る父の背中が頼もしく見えた」 |
| E11 | 納める ex1 「授業料は…振り込んで納めてください」 | Same scene as the cited 7/2016 問題1-4 「期日までに入学金を納めた」 (paying a school fee). | → 「会社員の税金は、毎月の給料から引かれて納められる」 |
| E12 | 辛い ex1 「このカレーは辛すぎて、水を何杯も飲んだ」 | Same frame as the cited 7/2010 問題1-2 「この料理は辛くて食べられない」. My first rewrite (disliking spicy food) matched 7/2025 問題1-2, so I discarded it. | → 「とうがらしを入れすぎて、スープが辛くなってしまった」 |
| E13 | 傾向 ex2 「車を持たない若者が増えている傾向がある」 | 「増えている傾向がある」 is redundant. It also reuses 7/2025's 「増えるけいこうがある」 and Hajimete's 「最近増える傾向」. | → 「私は、緊張すると早口になる傾向がある」. I avoided 「食事を抜く」, which is too close to 12/2021's 「食事をする傾向」. |
| E14 | 好調 ex1 「営業部の成績は好調が続いている」 | The は…が double subject reads unnaturally. | → 「…営業部は好調が続いている」 |

Every changed example got a new vi `example_notes` translation, written from the Japanese. The re-scan is clean. The
only new hit is the generic ending 「く感じるようになった」. All other examples are natural N2 sentences in the tested sense.

## 5. Prose

- **Official-distractor claims.** I checked every quoted option list in both languages against the booklet lines.
  All are real, including 逆らう 「敵らって」「拒って」「争って」, 暮らす 「幕らして」「募らして」「墓らして」, 刺激
  「さてき」「さげき」「してき」 / 「じえき」「じげき」「しえき」, 着々 「すらすら」「続々と」「ぐんぐん」「慎重に」, 豊か
  「恵か」「富か」「満か」「福か」, and 損害 「ひかい」「ひがい」.
- **P1: vi 反省 misquote.** It quoted 「どんなに反省しても思い出せない」. The booklet prints
  「…どんなに反省しても全く思い出せない」 (12/2016 問題6-32 ①). Fixed.
- **P2: ja わりと usage (rule 15 for 語彙).** 「形容詞や副詞の前につく」 was a restriction that the entry's own official key
  「わりとすいている」 (わりと before a verb) contradicts. → 「わりと簡単だ」「わりと早く終わる」「わりとすいている」のように使う.
- **P3: ja 辛い nuance.** It said 「味を表す」…「くさい」. くさい is a smell, so this now reads 「味やにおいを表す」. The vi
  pane already said "vị, mùi".
- **Other claims.** Checked without change: 直接 ↔ 間接 (Hajimete prints 間接 next to 直接), 起床 ↔ 就寝, 好調 ↔ 不調,
  ぐち = 愚痴 (SK PDF 132), 頑丈's 「厳重に管理」 (an official 7/2021 問題6 option), 努める / 務める (7/2022 問題1-4) and
  責める / 攻める (Hajimete No.787).
- **Hán Việt.** All glosses are correct: tị nạn, khởi sàng, điều tiết, tiết ước, mô phạm, nhu nhuyễn, tổn hại,
  vĩnh cửu, phong, tước, huệ.
- **vi quoting.** A script found no Japanese outside 「」 in any vi field.
- **Citations in prose.** None: no sitting date, SK or page reference in any prose field.
- **Translation check.** vi is not a translation of ja. The quoted misuses, collocations and framing differ throughout.
- **Bands.** After the fixes, everything is within the bands. The largest new field is vi 生じる compare at 150 of 180.

## 6. Live back-links (batch-1 entries that B2 points at)

I added the back-link and wrote a `compare` in both languages for five entries. Each compare is written from the items,
not translated from the other language:

- 運賃 ← 会計
- 徐々に ← 着々
- 順調 ← 着々, 好調
- 依然 ← 永久に
- 豊富 ← 豊か

Per §3, I also completed the reverse direction of the three look-alike pairs on the live side: 備える (+あらかじめ),
続出 (+生じる) and 和やか (+活気). **That is 8 live entries in total, 3 more than the five named.** Both-ways linking
needs them. The live diff touches only those 8 entries' `related` and `compare`.

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| E1–E12 (reworded copies) | Rules 13 and 21 exist, but the author ran only the 10-char scan. None of these copies shares 10 characters with its source. Two kinds were new: a copy from a **related entry's** Hajimete page (E2), and copies of the **official items cited in the entry's own `sources`** (E5, E8–E12). | Add to the LEX brief: *before hand-off, print one table per entry: its examples beside the Hajimete example(s) on its page and on its `related` entries' pages, its SK 語彙 lines, and the stem of every official item in `sources`. Rewrite any row where scene and predicate match.* The 10-char scan is not evidence that an example is original. |
| C1 (乏しい 7/2012) | The author searched the kanji form. A 問題6 headword may be printed in kana (とぼしい). | Add to rule 4 / rule 28: *search every sitting for the kanji form **and** the hiragana reading, stem-trimmed for verbs and adjectives, and read each hit.* `QAV2_find.py` does this. |
| P2 (わりと) | Rule 15 (a restriction must match the page) is written for 接続 in 文法. | Extend rule 15 to 語彙: *a usage restriction in prose (「〜の前につく」, 「〜には使わない」) must not be contradicted by any official item the entry cites.* |
| あらかじめ/備える, 生じる/続出, 活気/和やか | Rule 28 has the author dump and read the generated items, but these pairs have different pos and are not generated today. The dump cannot show them. | Add to rule 28: *also list near-synonyms across pos and across batches (live entries included); the generator only prefers the same pos.* |
| one-way links into live entries | `merge_batch.py` adds entries but never back-links. Five live entries had empty `related`/`compare`, and patching them before the merge leaves the live gate red until the merge. | Have `merge_batch.py` apply back-links at merge time from a `語彙_B<N>.backlinks.json` (id → related + compare per language), or have the gate WARN on one-way `related` links. |
| E13, E14, P1, P3 | Author slips that no check covers. | None needed; one QA round covers them. |

## For the coordinator

- **Merge.** Merge B2 with `merge_batch.py 語彙 2`. That clears the live `related` FAIL. Then run `make knowledge` and
  `make check`.
- **Book order of 好調.** `v-o-kouchou` has the group 「第9章 健康のために／病気になる前に」, a label no numbered word
  carries yet. By the §Book order rule it sorts after the 「N2単語2500外（公式）」 group, so it is the last card on the page
  today. It moves into place when No.1069–1075 are authored. That is correct under the rule, but it looks odd for now.
- **Dropped words.** The author listed them in the inventory follow-up (継ぐ, あえて, とっさ, 気配り, せい, ごく, はう,
  流し, 甘み, 気配, 乗り継ぐ). I did not re-verify them. Recount them from scratch when they are authored.
