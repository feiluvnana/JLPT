# QA report — 知識 N2 漢字 batch 1 (70 kanji)

Fresh-eyes reviewer: this context authored none of the batch. Targets (scratch
`batches/`): `漢字_B1.json`, `漢字_B1.ja.json`, `漢字_B1.vi.json`. One full round,
direct fixes. The real `knowledge/` was not touched. Every check was run on a
scratch root (copied `.agents/` + `knowledge/`, the rest symlinked), with the
batch merged into `knowledge/N2/漢字.json` and both language files.

## What was checked, and how

| area | method | result |
| - | - | - |
| ids = SK 漢字 number | every one of the 70 against the SK 別冊1 学習漢字リスト, PDF 141–201, read page by page from a pypdf slice | 70/70 correct; `page` and 別冊 page in every `note` correct; every `group` (ステップ/回) correct |
| `on` / `kun` | every reading against the SK page | 65 match the page exactly. The 5 readings the page does not print were confirmed on official items (below) |
| `words` furigana | every compound read by hand | all correct (湿気 しっけ: SK prints しっけ/しっき, and the dataset knows both) |
| added readings | the cited official item and its key | 収 おさ.まる (7/2025 1-5, key 3 おさまった); 競 きそ.う (7/2016 1-2, key 1 きそって; 7/2021 2-9); 装 ショウ (12/2024 1-5, key 2 いしょう); 逃 のが.す (12/2019 2-9 見逃して); 乱 みだ.れる (12/2010 2-8, 7/2023 1-2, 12/2017 1-1). All 5 confirmed |
| `official_count` | a parser listed every 問題1 sentence that holds the kanji, and every 問題2 key that holds it, in all 31 sittings (302 items), with the key. Each hit was read to see whether the kanji is in the target word | 70/70 correct. A reprint counts once per sitting (調/順 12/2021, 拡 7/2021, 破/片 7/2021), following rule 16. False hits were rightly left out (好調 in 7/2011 1-1, where the target is 敗れて; 世代 12/2021 1-2 → 乏しい; 危険 12/2016 → 伴う; 接する 12/2019 1-1 → 等しく) |
| distractor claims in prose | a script pulled every 「…」 in usage/nuance/compare (ja and vi) and looked for it in the cited booklets. Each miss was then read by hand | ja: all true. vi: one false claim (F4) |
| related pairs | the official item behind each pair, printed | 乱/破 12/2010 2-8, 損/害 7/2019 2-9 (罪 害 損 毒), 豊/富 7/2021 2-6 and 7/2018 2-6, 傾/倒 7/2013 2-8, 除/省/略 7/2018 2-10, 治/救 7/2017 2-8 (治う 助う 救う 療う), 争/競 12/2015 2-8, 7/2021 2-9 and 7/2016 1-2, 離/逃 12/2022 2-8, 勢/勇 12/2019 2-7. All real, and every compare is correct except the 富/福 shape claim (F5) |
| generated quizzes | built the scratch copy and dumped all 70 `#r` and 70 `#m` items in both languages; read each one | every fabricated misreading was read (はこどう, かひん/おひん, そんじゅう, しゅっせい, そうじょ, げんぞう, いそう, けいぎ, …). None is a reading of its compound. Several (そんじゅう, げんぞう, いそう, さげき) are the official distractors themselves. Meaning clashes: F2/F3 |
| Hán Việt | all 70 against standard (Thiều Chửu-style) readings | 67 fine. 濃 and 重 fixed (F6). **賃 NHẪM is correct** (Thiều Chửu 賃 nhẫm; "LẪM" is wrong), so it is kept |
| 「Hán Việt dễ lừa」 | each warning checked | all 15 true: 接続 = tiếp tục, 装置 = trang trí, 運転 = vận chuyển, 招待 = chiêu đãi, 消極的 = tiêu cực, 公害/利害 (lợi hại), 理解 = lý giải, 出世 = xuất thế, 景気 = cảnh khí, 濃厚 = nồng hậu, 高等 = cao đẳng, 口実 = khẩu thực, 講義 = giảng nghĩa, 湿 = thấp, plus 刺激/紹介/面接/大勢. 情景 carries no trap claim in the vi pane, so there was nothing to check |
| examples | 10-char window scan against `refs/**/*.md` + `tests/imported-*`. Also a content-token overlap lister against every official booklet/script line (≥3 shared tokens), with each candidate read | 10-char scan: 0 hits at first. The overlap lister found 5 official scenes (F7); the first replacement for 極 then hit a 10-char window and was replaced again |
| rule 6 (vi: Japanese in 「」) | script | clean. The only bare kana is the grammar label "tính từ đuôi な" |
| rule 18 (no citations in prose) | script | ja: 90 fields broken (F1). vi: clean |
| gate | `check_knowledge.py` on the merged scratch copy, before and after the fixes | 0 FAIL, 0 WARN both times; bands, schema and key balance all ok |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | ja pane, 90 usage/nuance/compare fields | major | Sitting citations in learner prose: 「（7/2019・12/2012）」, 「12/2010 問題2で並んだ」, 「12/2024に出た」. There were also 9 references to the book: 「この本の表にないが」 (乱, 収, 競, 装, 逃), 「この本の表で『ゆたか』と読むのは豊」, 「この本の表でゾウと読むのは…」, 「この本の表に訓読みはない」 (富), 「…音読みホウの語はない」 (抱). The last two are also false: 富 has と.む/とみ and 抱 has ホウ (抱負) | Every date was stripped. 「問題1/問題2」 stays, because it names the exam item type, not a source. The 9 book sentences were rewritten or cut. 富 and 抱 no longer claim a missing reading | Rule 18 names only "SK, page or 課 numbers". LEX_JA_BRIEF says nothing about sittings in prose. The vi author, working to BATCH_VI_BRIEF, wrote none |
| F2 | 永 k-0568 / 久 k-0636 (known) | minor | Both are in 永久 and they were not linked. 久's meaning item could draw 永 as a distractor | Linked both ways. A compare written in each language | LEX_JA_BRIEF defines `related` as look-alike shapes only |
| F3 | 濃 k-0919 / 厚 k-0699; 理/論; 世/景 | major (濃 item) | 濃's generated meaning item used 厚 as a distractor, and vi 厚 read "HẬU — dày; **đậm, nồng**", which is also 濃's meaning (the two form 濃厚). In ja, 論 「筋道を立てて考えや意見を述べること」 competed with 理 「物事の筋道」, and in vi LUẬN "lý luận" contained LÝ. 景 「世の中の経済のようす」 appeared as a distractor on 世's item | 濃↔厚 linked, with compares in both languages. vi 厚 → "HẬU — dày, bề dày". 論 ja → 「意見を述べて話し合うこと。また、まとまった考え。」, vi → "LUẬN — bàn luận, tranh luận; bài luận". 景 ja → 「ながめ、けしき。また、『景気』の形で経済のようす。」 | The generator can see shared kanji only in 語彙. A gloss that borrows a compound's second kanji (厚 ← 濃厚) is invisible to it (SKILL §Quiz integrity residual risk) |
| F4 | vi 備 nuance | minor | 「蓄える」 is named as a distractor 「trong đề」. The 7/2022 2-9 options are 備える 準える 整える 控える | 「蓄える」 → 「控える」 | vi author wrote a distractor from memory; no brief rule requires quoting only printed options |
| F5 | ja 福 k-0968 and 富 k-0960 compare | minor | 「富と福は右側が同じ形」: 富 is 宀 over 畐 and has no right side | → 「『畐』の部分が同じ。富はうかんむり…、福はしめすへん…」 (the vi pane already said this correctly) | — |
| F6 | vi meaning 濃, 重 | minor | 濃 "NỒNG" is the common reading; the dictionary reading is NÙNG. 重 gave only TRỌNG, though its "chồng lên" sense is TRÙNG | "NÙNG (quen đọc NỒNG) — đậm, đặc"; "TRỌNG, TRÙNG — nặng, quan trọng; chồng lên". 濃厚's "nồng hậu" trap note is kept, since that is the Vietnamese word | BATCH_VI_BRIEF has no Hán Việt rule |
| F7 | examples 装, 倒, 害, 久, 極 | major (装), minor (rest) | Each reuses an official scene. 装 「式には、きちんとした服装で行くつもりだ」 is 12/2021 問題4-18 and 7/2013-22 「卒業パーティーには、ちゃんとした（格好）で行った…」. 倒 「強い風で、庭の木が倒れた」 is 12/2017 用法 option 「強い風が吹いたせいで、庭の木の枝が…」. 害 「台風で…被害が出た」 is 7/2011 用法 option 「台風の…被害は出なかった」. 久 「久しぶりに…会って話した」 is 7/2019 「会うのは久しぶりだったので、いくら話しても…」. 極 「積極的に取り組みたい」 is the 12/2018 読解 「積極的に仕事に取り組む」. The first replacement for 極 (「会議では…積極的に意見を言った」) matched 12/2023 word for word, so it was replaced again | New scenes: 山登り＋服装; a sudden stop on a train＋倒れそうに; 大雪＋被害を受けた; 実家＋母の料理; 消極的な性格 (it also teaches the tiêu cực trap). vi example_notes rewritten from the new sentences. Both scans rerun: clean | Rule 3's 10-char window cannot see a reworded official scene. Rule 17's bigram check is written for quiz stems only, not for examples |
| F8 | generator (not batch data) | note | Four pairs share a reading target, so the category holds two identical `#r` items: 永/久 → 永久, 的/極 → 積極的, 介/護 → 介護, 豊/富 → 豊富. 的's item then tests 積 (せき/せっ), not 的 | Not fixed: `quiz_gen.reading_target` picks by hash and does not know about the other entries. A data-side fix would mean dropping the official compound from one card | proposal R3 |
| F9 | 険 example | note | 「険しい坂道を…登った」 is near 12/2020 1-3 「思ったより険しい山道だった」: same noun family, different predicate. 険しい＋山道/坂道 is the word's basic collocation | kept | — |

Not a defect, recorded so nobody checks it again: the vi meaning text starts with
the Hán Việt reading ("VẬN — …"). A Vietnamese reader who knows the character can
answer the meaning quiz from the reading alone. The format is the vi author's
design, so it is kept.

**Counts:** 9 findings — 3 major (F1, F3, F7), 4 minor, 2 notes. Edits: 90 ja
fields de-cited, 9 of them rewritten; 4 ja and 4 vi meanings; 4 new compares in
each language; 2 new related pairs (4 links); 5 examples and their vi notes;
1 vi nuance.

## Root causes and proposed rules

- **R1 (F1)** SKILL rule 18 + LEX_JA_BRIEF: "Prose names no sitting, no date,
  no item number and no book ('この本', 'SK'). 『問題2で…が並んだ』 is fine; the
  sitting goes in `sources`." A gate WARN on `\d{1,2}/20\d\d` or `この｜?本` in any
  language file's prose would catch it (B4 R3 proposed the SK half of this).
- **R2 (F3, F2)** LEX_JA_BRIEF / BATCH_VI_BRIEF for 語彙/漢字: "A meaning gloss
  must not borrow a sense that belongs to a compound's other kanji (厚 ≠ 'đậm'
  from 濃厚). Two kanji that form an N2 compound together, or whose glosses share
  a content word, go in `related`." Reviewers should keep dumping the generated
  items. Of the 140 in this batch, the one real clash showed up only in the vi pane.
- **R3 (F8)** `quiz_gen.reading_target`: prefer a `words` item that no other
  entry's reading item already uses (cheap, deterministic). Reviewers do not edit
  the generator, so this is left to the owner.
- **R4 (F7)** Extend rule 17 to examples in every category: run the ≥3
  shared-content-token lister over booklet + script lines, and read each hit. This
  batch's `QAK1_bigram.py` did the job in one pass.
- **R5 (F4, F6)** BATCH_VI_BRIEF: "A distractor named 『trong đề』 is quoted
  from the printed options. A Hán Việt reading is the dictionary one; add the
  common one only as '(quen đọc …)'."

## Validation after fixes

`check_knowledge.py` on the merged scratch copy: **0 FAIL, 0 WARN**. The 10-char
provenance scan of all 70 examples finds 0 hits, and the overlap lister shows no
candidate for the replaced examples. The ja and vi prose hold 0 citation or book
strings. All 140 generated items were regenerated and the changed ones re-read.
