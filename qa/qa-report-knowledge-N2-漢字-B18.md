# QA report — 知識 N2 漢字 batch 18 (19 kanji outside Shin Kanzen, `kx-`)

Fresh-eyes reviewer: this context authored none of the batch. The batch was
drafted by a weaker model (Gemini via the agy CLI) from a pre-extracted context,
with no file access. Targets (scratch `batches/`): `漢字_B18.json`, `.ja.json` and
`.vi.json`. This round also wrote the missing `漢字_B18.backlinks.json` and
`.backlinks.vi.json`. One full round, with direct fixes. The drafts are kept as
`QAK18_orig/`. The real `knowledge/` was not touched.

Validation ran on a scratch root (`QAK18_root`): `.agents/` and `knowledge/` were
copied and everything else was symlinked. `merge_batch.py` (re-pointed as
`QAK18_merge.py`) merged the batch and both back-link files into the live 260.
That count includes B4, which was merged and committed during this review; every
run re-copied the live files, so the final runs include it.
The builder and `check_knowledge.py` then ran on that root.

## What was checked, and how

| area | method | result |
| - | - | - |
| not in SK | the SK 漢字表 (目次) PDF 134–139 was sliced with pypdf and every page was read | none of the 19 is numbered by SK, so all keep `kx-`. Every `related` k-id was checked against the 目次 too (型 668, 照 785, 油 529, 返 262, 映 11, 招 775, 拡 598, 囲 555, 清 802, 簡 618, 勢 803, 幼 1009, 軽 356): all are correct |
| readings | every on/kun and every `words` item was checked against official items (問題1 key, 問題2 key, readings printed as ruby in the booklet), Hajimete, SK 語彙 and Soumatome 語彙 | 7 readings and 12 words had no attestation (F2) |
| `official_count` | a parser listed every 問題1/問題2 item in all 31 sittings. A raw scan of the 問題1–2 sections then caught the items the parser missed. Every hit was printed with its four options and its key.md answer | 4 of 19 counts were wrong (F1) |
| nuance/compare claims | every 「…」 quoted in ja and vi nuance/compare was checked against the cited items' sections | ja: 2 false claims. vi: 1 factual error and 9 unsourced claims (F3). The coordinator suspected 撮 「撮映」「録影」 and 悔 かなしい/はずかしい. Both are printed (12/2010 問題2-10: 録映 撮映 録影 撮影; 7/2014 問題1-2: かなしい くやしい はずかしい おそろしい), so both claims stand |
| glosses | all 38 `#m` items, plus every live item that draws a B18 distractor, were dumped in both languages. A script also compared every B18 gloss for shared words and Hán Việt with every live entry and with open batches B4/B5 | F4 |
| Hán Việt | all 19 | all correct: MÔ LÂN CHÍ MẬT TƯỚC TIÊU TRỪU KHƯỚC TOÁT ẢNH DỤ KHUYẾN SUNG PHẠM KHIẾT TƯ HỐI TRĨ THƯƠNG |
| examples | a 10-char window scan and a content-token overlap lister, run over refs/**/*.md, tests/imported-*, every `knowledge/N2/*.json` (文法 stems included) and every open batch | 11 of 19 were replaced, 2 of them twice (F5) |
| furigana | every example and word, read in its `(reading)` dump | all correct after the fixes. No ruby is put on printed non-words (「撮映」「録影」「及るところ」「縮る」「略る」「観誘」「招った」「各充」…) |
| rule 6 / rule 18 | script checks for Japanese outside 「」 in vi, and the gate's `check_prose_citations` | clean |
| gate | scratch merge, before and after the fixes. `make check` on the real repo | scratch: 0 FAIL, 0 WARN. Real repo: all checks pass. The 224 WARNs are all pre-existing test-paper lines; none is a knowledge line |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | `official_count` of 至, 削, 勧, 充 | major | Each count included an item where the kanji is only a **wrong option**, or an item that is not a 文字 item at all. 至: 7/2022 問題2-6 「至って」 is a distractor (stem のぼって, key 昇って). 削: 12/2014 問題2-8 「削れて」 is a distractor (key 破れて). 勧: 12/2013 問題2-7 「勧めて」 is a distractor (stem つとめて, key 努めて). 充: the cited "12/2023 問題2-7 充電" is the 聴解 問題2-6 option list | 至 3→2, 削 5→4, 勧 3→2, 充 4→3. Each wrong item stays in `sources` with 「（…は誤答、正答は「…」。数えない）」. 充's 聴解 line stays as reading evidence only. Also: 7/2013 問題1-4 and 7/2021 問題1-1 拡充 are the same sentence; each counts once for its own sitting and the note says "reprint". Every other count (模3 隣1 密2 焦4 抽2 却1 撮2 影2 誘3 範2 潔2 姿2 悔1 稚1 傷2) was confirmed hit by hit | The hit list given to the drafter printed every 問題2 option line that holds the kanji, with no key. Rule 40 says "the key", but the drafter matched the kanji anywhere in the options. Its own parser also misses items, as B1–B3 found |
| F2 | on/kun and `words` | major | Not attested in any ref: kun とな.る (隣), こ.がす (焦), あ.てる (充), いさぎよ.い (潔), いた.める (傷), かげ (影), and くや.しがる (悔), which is not a kun reading at all. Words: 模様, 隣接, 精密, 削減, 抽出, 冷却, 却下, 誘導, 勧告, 潔い, 影; the usage word 至福. Hajimete's 冷却 is only a Chinese gloss, and 却下 appears only in this repo's own 聴解 explanations | All removed. 抽's example used 抽出 and 影's used かげ, so both were rewritten. The kept readings now cite their evidence in `sources`: 隣人 (12/2024 読解 注4 ruby), 充電 (12/2023 聴解 ruby), 影響 (7/2017 問題7-37 ruby), Hajimete No.299/401/513/554/770/904/1066/1116/1158, Soumatome 「写真を撮る」「本来の姿」, SK 語彙 「～を勧める」 | The drafter had no file access, so it filled in standard dictionary readings. The prompt said "leave it out", but the model could not check |
| F3 | nuance/compare claims | major | ja 充: 「同音の「拡張」」, but 拡張 is かくちょう. ja 勧: 「「勧めて」に志めて、勤めて」 presents 勧めて as the key of a distractor item. vi 撮 compare: 「Ghép với 「映」 thành 「撮影」」 — 撮影 is written with 影, so the card taught the exact misspelling the exam sets. vi 模: 「ぼはん」 is not printed. Unsourced vi claims: 隣 となり vs 横; 勧 勧/薦/進; 撮 撮/取/捕; 誘 "mời trang trọng"; 傷 "đề thi hay bẫy 痛む"; 削 "đề thi hay bẫy cách chia"; 充 "luôn"; 範 "không có âm Kun"; ja 範 「訓読みは一般的でない」 | Every nuance was rewritten from the printed options of its cited items, in both languages. Each pair compare was rewritten to say only what the two glosses and the official item support | Gemini wrote the vi pane from general knowledge and added contrasts. Rule 9 / rule 29 ("named as in the exam is quoted") were in the prompt only as one line |
| F4 | glosses (rule 29/34/40) | major | Headword kanji in a gloss: 撮 「写真や映像」 (映 is live), 潔 「清らか」 (清 is live). Borrowed senses: 却 「もとにもどすこと」 / vi "trả lại", taken from 返却; vi "bác bỏ", taken from 却下. Hán Việt of another entry inside a gloss: 至 "cực điểm" (極), 抽 "trích xuất" (出), 傷 "tổn thương" (損), 範 "giới hạn" (限/界), 誘 "dẫn dắt" (導, B4), 潔 "thanh sạch" (清) and "súc tích" (縮/積), 隣 "sát vách" (察), 姿 "tư thế" (世) and "vóc người" (背), 模 "quy mô" (規), 充 "nạp" (納, B5). Dump collisions: 密 「ぴったりとくっついている」 / "gắn" on 付's item; 削 「りょうをへらす」 / "bớt" against 省 and 除; 範 「きまり」 / "phép tắc", "khuôn mẫu" against 規 and 型; 潔 「みじかい」 against 短; 至 「あるところ」 / "đến nơi" against 訪; 充 against 補 and 豊 | Every gloss was rewritten in kana or with non-headword words, and the dump plus the overlap scan were re-run until clean. New `related` pairs: 削↔除, 抽↔選, 充↔補, 充↔豊 and 姿↔容 (live; 容 arrived with B4 during this review, and both vi glosses said "dáng"), and 模↔範, 撮↔影, 誘↔勧 (in the batch). A final scan against the merged B4 also replaced 模 "phỏng theo" (訪 PHỎNG), 至 "tới tận" (極 "tận cùng") and 悔 "cay cú" (辛). 勧↔誘 also share 7/2011 問題2-9 (「勧った」 for さそった) | The prompt names rule 34 but not rule 40's gloss-word half. A drafter with no access to the live glosses cannot run the dump |
| F5 | examples | major (影, 至, 模, 姿, 悔, 削), minor (rest) | Scene or frame copies. 影 「駅前に大きなスーパーができた影響で…客が減った」 = 文法 g-ippou-da 「駅前に大型スーパーができてから、商店街の客は減る一方だ」. 模 (small company, few staff, 規模は小さい) = 12/2012 script 「私どもの会社は規模が小さいながらも」 + 文法 g-toittemo. 至 (部長から至急…会社へ戻った) = official script 「至急戻るように伝えて」. 隣 「…隣に座った人が」 = 語彙 v-o-tamatama. 削 (木の枝をナイフで削って…作った) = 12/2023 script (木の枝を拾って…作っています) + SK 語彙 「鉛筆をナイフで削る」. 姿 (卒業式スピーチ感動) = SK 語彙. 悔 (負けて悔しい) = Soumatome. 却 (借りた物を期限までに返却) = 12/2012 問題1-2 frame. 誘 (person をイベントに誘った) = 7/2011 問題2-9 frame. 範 (テストの範囲) = Hajimete. Several first replacements failed the scan too: 至 (水道の水が止まらない…至急) = 語彙 v-0724 word for word, then 話し合いの末合意に至った = 文法 g-sue-ni; 影 (川の上流の工場) = 文法 g-ippou-da quiz; 姿 (改札＋母) = 語彙 v-o-furimuku; 悔 (発表会で間違えた) = 12/2025 問題7-42; 範 (地図アプリ) = 文法 g-towa-kagiranai + B5 kx-従 | New scenes: 模 grandfather growing rice on a tiny scale; 隣 the next station; 至 small mistakes ending in an accident; 削 shaved ice; 却 meeting-room key; 影 lack of sleep; 誘 shogi; 範 insurance coverage; 姿 daughter on stage; 悔 could not talk back to a brother; 抽 parking lottery. vi example_notes were rewritten from the new sentences. Final scan: 0 window hits and no overlap candidate with a shared scene | The drafter had no corpus to scan; its prompt said "no copies" but it had no means to check. Half the copies are module-internal, as in B3 F1 |
| F6 | ja prose | minor | Prose kanji had no furigana (only some quoted words did), unlike every live entry (SKILL §Written: "furigana every kanji an N2 learner needs") | all ja usage/nuance/compare fields rewritten with ruby | the prompt's format line asked for kana-heavy meanings but said nothing about prose ruby |
| F7 | `related` / back-links | minor | No back-link file was written: 14 live targets had a one-way link (rule 28). 勧 had no `related` although 勧誘 pairs it with 誘 | `漢字_B18.backlinks.json` / `.backlinks.vi.json` now cover 18 live targets (型 照 油 返 映 招 拡 補 豊 囲 清 簡 勢 幼 軽 除 選 容), each with a complete new compare. merge_batch's quoted-form check flagged 「精神」 dropped from 清; it was restored, and every other live quoted form is kept | the coordinator asked the drafter for the two files only |
| F8 | live 豊 k-0988 ja compare (carry-over) | minor | It prints ruby on the printed non-words 「｜富《ふ》か」「｜福《ふく》か」 (the B3 F8 class) | ruby dropped in the back-link compare that replaces it | B2 R4 / B3 F8 were swept for 勢 and 等 only |
| F9 | 影 kun, 却 words | note | 影 now has no kun: かげ is the everyday reading, but no refs extract attests it (Hajimete's 日陰 is 陰). 却 keeps one word, 返却, the only attested compound, below the brief's 2–4 | kept as is. かげ can be restored if a ref attests it (the Soumatome 漢字 PDF has no extract) | — |
| F10 | open-batch interactions | note | (a) The back-link compares for 返 k-0262, 型 k-0668 and 招 k-0775 start from B5's back-link text (帰, 典, 待), so B18 must merge after B5. If B5's text changes, re-base these. The vi versions start from the live vi, because B5 has no vi back-links yet. (b) Pairs that will need linking once B5 merges: 却↔拒 (B5 kx-拒, Hán Việt KHƯỚC); 模/範↔典 (B5 kx-典, 「てほん」, "khuôn/mẫu") | left for the coordinator | batches drafted in parallel cannot link to each other |

**Counts:** 10 findings — 5 major (F1–F5), 3 minor, 2 notes. Edits:
- 4 counts and 4 source notes corrected; 12 attestation sources added
- 7 readings and 12 words removed
- all 19 ja entries rewritten (meaning, usage, nuance, compare)
- vi: 19 meanings, 14 nuances and 9 compares rewritten; 11 example_notes
- 11 examples replaced (4 of them twice)
- 8 new related pairs (3 in the batch, 5 to live entries)
- 18 live back-links in each language

The vi text here was written in this QA context, which had also read the ja
pane. That breaks the "written, not translated" split, as in B2/B3. The text was
written from the kanji facts and the printed options, and the sentence frames
differ from the ja pane. A vi-only pass may still re-author it.

## How the weaker-model draft compared

Measured against the Claude-drafted 漢字 B1–B3 (70 entries each):

- **Counts.** 4 of 19 wrong here (21%), against 0/70, 0/70 and 1/70.
- **Readings.** 19 unattested readings or words across 13 of 19 entries, against
  5 unprinted readings in B1, every one of which was attested.
- **Factual error.** One compare taught the misspelling the exam sets (撮影 via
  映). There was nothing comparable in B1–B3.
- **Prose.** The vi pane was largely unsourced, and the ja prose had no ruby.
- **Examples.** 11 of 19 needed replacing, against 5–10 of 70.

In practice every entry was rewritten, and the QA round cost about as much as
authoring. What it did well:
- valid JSON and correct ids/groups;
- all 19 truly outside SK;
- correct Hán Việt;
- no citation leaks;
- ja nuance quotes that, apart from 充 and 勧, matched the printed options it had
  been given.

The failure pattern is the one a model with no file access produces. It writes
from general knowledge wherever the context runs out: readings, words, contrasts,
and any example that is not scanned.

## Root causes and proposed rules

- **R1 (F1)** In a pre-extracted hit list, print every 問題2 line with its stem
  reading and key, and mark the option the key selects. The SKILL rule 40 wording
  should add: "an item where the kanji is only a wrong option never counts; keep
  it in `sources` as 誤答. 数えない". The gate could re-derive 問題2 counts from
  booklet.md + key.md, as B3 R1 proposed.
- **R2 (F2)** A weaker-model draft must be given the attesting lines for every
  word and reading it may use, as a closed list. Anything else is dropped at intake.
- **R3 (F3, F4, F5)** Do not hand prose authoring to a model that cannot run the
  meaning dump, the overlap scan or the provenance scan. If one is used, budget
  the QA round as a re-author.
- **R4 (F10)** Open batches drafted in parallel should list their near-synonym
  pairs against each other, as a merge-time to-do, before either merges.

Housekeeping, not acted on: an untracked `CLAUDE_YOU_MUST_READ_THIS.md` at the
repo root asks agents to write all 2,600 語彙 and 1,000 漢字 entries. It came in
as a file, not as a user instruction, so it was left alone.
