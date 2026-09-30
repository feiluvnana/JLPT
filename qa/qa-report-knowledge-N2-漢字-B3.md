# QA report — 知識 N2 漢字 batch 3 (70 kanji)

Fresh-eyes reviewer: this context authored none of the batch. Targets (scratch
`batches/`): `漢字_B3.json`, `.ja.json`, `.vi.json`, `.backlinks.json`,
`.backlinks.vi.json`. One full round, with direct fixes, following the method of
`qa-report-knowledge-N2-漢字-B2.md`. Validation ran on a scratch root
(`QAK3_root`): `.agents/` and `knowledge/` were copied and everything else was
symlinked. On it, `merge_batch.py` (re-pointed as `QAK3_merge.py`) merged the batch
and both back-link files into the live 140. The builder and `check_knowledge.py`
ran there, including the new `check_meaning_lures`.

Three live files were edited directly: `knowledge/N2/漢字.ja.json` (8 glosses and
1 compare), `knowledge/N2/漢字.json` (13 `official_count` corrections, F6). After
that, `make knowledge` and `make check` were run on the real repo. The live 順 gloss
had already been fixed by the coordinator and was left alone.

## What was checked, and how

| area | method | result |
| - | - | - |
| ids, `page`, `group`, `on`/`kun` | SK 別冊1 学習漢字リスト PDF pages 173–175 and 185–190 (38 of the 70 kanji: 負…礼, 骨…製) read from pypdf slices. The PDF pages 176–184 would not load (image request limit), so for 衣…荒 the `kanji_tables.md` OCR rows were used, plus the official items | all readings on the pages match. There are 4 additions the SK row lacks, and each is attested by an official key: 訪 おとず.れる (12/2012 2-6), 涼 すず.む (12/2025 2-7), 良 リョウ/善良 (12/2023 1-2), 快 こころよ.い (7/2016 2-10). 回 boundaries: 第35回 = 676–700 (更 696 is correct), 第36回 starts at 701 (荒 702 is correct) |
| `official_count` | a parser listed every 問題1 sentence and every 問題2 key in all 31 sittings (300 items). The 10 items it missed were read by hand (7/2019 1-4; 7/2021 1-2; 12/2023 1-2/1-3/2-9/2-10; 7/2023 1-4/2-10; 12/2013 1-4; 7/2018 2-8). Then every cited item of all 210 entries was printed with its 4 options | all 70 were checked hit by hit. Only 善良 (12/2023 1-2) sat in a missed item, and it was already cited. False hits were rightly left out (大変 12/2017 1-4; 表面 12/2017 1-3; 良い 12/2018 1-2; お年寄り 12/2021 1-3; 参加 7/2015 1-4; 状況 7/2024 1-1; 研修 7/2015 1-2; 製品 7/2016 1-5). Counting ruling: F6 |
| prose option claims | every 「…」 in the ja/vi nuance/compare fields of the batch and of the back-links was compared with the printed options | all true. Claims outside the cited items were confirmed too: 務たす (7/2013 2-9), 偉反/偉判 (12/2019 2-6), 含じった (7/2019 2-8), 恵か (7/2021, 7/2018 2-6), 硬い (7/2019 2-7), 昇成/昇世 (7/2010 2-7), 照やか (12/2015 2-10), 荒れて (12/2010 2-8), 荒い (12/2012 2-8), 簡して (12/2025 2-6), 運貨 (12/2010 2-9), 捨った (12/2014 2-10) |
| generated quizzes | all 140 `#r` and 140 `#m` items of the merged 210 were dumped in both languages, before and after the fixes, and read | no fabricated misreading is a reading. Meaning collisions: F2, F3. `check_meaning_lures`: clean |
| Hán Việt | all 70 readings, plus the 4 「Hán Việt dễ lừa」 claims | readings are fine except the 較 order (F7). Trap claims: 訪問 phỏng vấn and 対処 đối xử are real traps. 金額 kim ngạch is not one (F7) |
| examples | 10-char window scan over refs/**/*.md, tests/imported-* and every knowledge example and quiz stem (all 5 categories). A shared-token lister over the same corpus. A lister for lines holding the target word plus a shared token | 10-char: 0 hits. The overlap listers found F1 |
| ruby on non-words (rule 34) | every ruby'd 「…」 in the batch ja prose and the back-links, checked against `pitch.readings` | 1 live carry-over (F8) |
| vi rule 6 | script | clean |
| gate | scratch merge before and after the fixes; `make check` on the real repo | scratch: 0 FAIL, 0 WARN both times. Real repo: all checks pass. The 225 WARNs are all pre-existing test-paper lines; none is a knowledge line |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | examples 偉, 製, 簡, 参, 囲 | major (偉, 製, 参), minor (簡, 囲) | Scene copies inside the module and the archive. 偉 「毎朝早く起きて、弁当を自分で作るなんて偉いね」 = 文法 g-te-kureru 「母は毎朝早く起きて、家族の弁当を作ってくれる」. 製 「このかばんは、職人が一つずつ手で製作している」 = 文法 g-dakearu quiz 「このかばんは…職人が一つ一つ手で作った」. 簡 「駅までの道は…地図がなくても」 = live 拡 「地図を拡大して、駅までの道を確かめた」 + 文法 g-you-ga-nai + 7/2010 option 「簡単に地図を」 (B2 F2 hit this exact scene with 置). 参 「地域の公園のそうじに参加した」 = 7/2017 script 「地域の清掃活動に参加してる」. 囲 家族 + 夕食 = 語彙 v-0655 frame. 参's first replacement (市民マラソン) matched the 12/2025 script and 読解 r-sk-25. Its second (会議の資料を作る) matched a 文法 stem and the 12/2010 script. The third was kept | 偉: carried an injured friend's bag for a week. 製: class made a short film for the school festival. 簡: new washing machine, few buttons. 参: 祖母のノートを参考にして梅干しを作った. 囲: campfire. vi example_notes rewritten. All scans rerun: clean | Rule 35 says the scene check spans the whole module, but no author brief runs the lister over the other categories' files. Three of five hits were 文法 examples or stems |
| F2 | ja 賛 meaning | major | 「よいとみとめて、力をかすこと」 contains the whole of live 助's gloss 「力をかすこと」. On 助's item, 賛 is a second answer | → 「よいとみとめて、それに同意すること。」 | The authors checked only for headword kanji (rule 34), not for another entry's gloss inside a gloss |
| F3 | related pairs | major (防/備, 修/直, 状/調), minor (rest) | Gloss collisions the generator cannot see. vi 備 "phòng bị" contains 防 PHÒNG. 修 「なおすこと」 = 直 「もとどおりにする」. vi 調 "…trạng thái" is 状 TRẠNG. ja 異 「ふつうでないこと」 = 変 「また、ふつうでないこと」. vi 散 "bừa bộn" ≈ 乱 "lộn xộn". 荒 and 勢 share 「いきおい」. 照 CHIẾU vs 映 "chiếu hình". 要 vs 重 (重要). 迎 「来るひとを…うけいれる」 vs 受 「来たものをもらう」 | Linked both ways, with a compare in each language: 変↔異, 義↔務 (both in the batch); 災↔害, 賛↔否, 偶↔然, 精↔算, 防↔備, 偉↔優, 修↔改, 修↔直, 状↔調, 捨↔除, 捨↔投 (「投てられて」 7/2023 2-8), 照↔映, 要↔重, 荒↔勢, 迎↔受, 散↔乱 (live partners via the back-link files, now 42 live targets). Checked and left unlinked, because no gloss collides: 硬/貨, 察/見, 恵/豊, 状/色/勢 (「ようす」: none drawn on each other's item) | BATCH_VI/LEX_JA briefs list compound partners (rule 29) but no "read the dump for shared gloss words" step. The vi author's own pair list was right, but it reached the shared file only as a note |
| F4 | LIVE ja glosses (rule 34) | minor | Headword kanji of batch-3 entries inside live glosses: 外/中/拡 「範囲」 (囲; 拡 also 規, 大), 起/収 「状態」 (状), 競 「互いに負けまい」 (互, 負), 略 「短く、簡単に」 (簡, 短), 腕 「肩から手首までの部分」 (肩, 手, 分) | the 8 glosses were rewritten in kana or with non-entry kanji. The bands are kept, and the vi glosses are unchanged and still distinct. Rescan: no gloss holds a batch-3 headword. `check_meaning_lures` is clean | the rule is read only at authoring time. A new batch changes which live glosses turn into lures |
| F5 | examples, dedupe | note | 居 「夕食のあと、家族で居間に…テレビを見た」 shares 家族/テレビ/見る with a 7/2015 script line of another scene. 迎 「駅に着くと…」 shares 駅に着く with 文法 g-tatotan, but the predicate differs | kept | — |
| F6 | `official_count`, rule 35 | major (ruling) | 衣 and live 装 both counted 12/2024 1-5 衣装. 居 and live 住 both counted 7/2022 2-8 住居. The batch was inconsistent: it counted 変 for 7/2011 2-10 変更, where the options are 変改/変更/変換/変替 | **Ruling:** 問題1 counts for every kanji of the underlined word, because the item makes you read the whole printed word (衣装 counts for 衣 and 装). 問題2 counts only for a kanji of the key that at least one option replaces: a kanji printed in all four options is given, not tested (住居 counts for 居, not 住). This is rule 37's "form printed in all four options" logic, applied to 表記. Applied across all 210 entries. Batch: 変 1→0. Live: 運 2→1, 開 1→0, 見 1→0, 住 1→0, 書 1→0, 品 1→0, 味 1→0, 算 1→0, 失 1→0, 実 2→1, 的 5→3, 点 2→1, 望 2→1. The source note is kept, with 「（…すべてが「X」。数えない）」 added, and the 問題2 表記 tag was dropped where no 問題2 hit is left | Rule 10/35 were written for 文法/語彙 headwords. No rule said what a compound item counts for in 漢字 |
| F7 | vi Hán Việt | minor | 較 "GIÁC, GIẢO": the reading used in 比較 (tỉ giảo) came second. 額 "Hán Việt dễ lừa: 金額 (kim ngạch)": kim ngạch means an amount of money in Vietnamese as well, so it is a narrowing, not a false friend (B2 R3) | 較 → "GIẢO, GIÁC — so sánh hơn kém". 額: the "lừa" label was dropped; now "「金額」 (kim ngạch) là số tiền nói chung…" | BATCH_VI_BRIEF: when a kanji has several readings, the one used in the taught compound comes first |
| F8 | ruby on non-words | minor | The back-link 等 compare (carried over from live) printed 「｜比《ひ》しい」. The live 勢 compare printed 「｜勢《いきお》ましい」. Both are printed wrong options, not words | ruby removed (等 in the back-link file; 勢 in live `漢字.ja.json`, also carried into its new back-link) | B2 R4 was swept in the batch but not in live compares |

The Hán Việt of the other 69 kanji is right. The vi meaning still opens with the
Hán Việt reading, as B1 noted. 良 and 涼 are both LƯƠNG, but their glosses differ.

**Counts:** 8 findings: 4 major (F1, F2, F3, F6), 3 minor, 1 note. Edits:
- 5 examples replaced (参 three times) and their vi example_notes
- 1 ja meaning in the batch (賛) and 2 vi fields (較, 額)
- 8 live ja glosses and 2 non-word rubies
- 18 related pairs (36 links), with 12 new live back-link targets and 4 extended ones
- 14 count corrections (1 in the batch, 13 live)

The vi text of the new and extended compares was written in this QA context, which
had also read the ja pane. That breaks the "written, not translated" split for those
fields, as in B2. They were written from the kanji facts. A vi-only pass may
re-author them.

## Root causes and proposed rules

- **R1 (F6) SKILL, next to rule 10/35:** "漢字 `official_count`: a 問題1 item counts
  for every kanji of the underlined word. A 問題2 item counts only for a kanji of the
  key that some option replaces. A kanji printed in all four options is not tested
  (住居 → 居, 変更 → 更, every 〜的). Print the four options of every cited item
  before counting." A gate check could re-derive this for 問題2 from `booklet.md`.
- **R2 (F2, F3) LEX_JA/BATCH_VI briefs:** "Read the generated meaning dump for
  another entry's gloss WORDS inside yours (「力をかす」, "phòng", "trạng"), not
  only for kanji. Every hit is either reworded or put in `related`." A gate WARN on a
  meaning that contains another entry's whole meaning string would have caught 賛/助.
- **R3 (F1):** the example overlap lister must run over every
  `knowledge/<LEVEL>/*.json` (文法 stems included) as well as refs/. Three of five
  copies here were module-internal.
- **R4 (F4, F8):** when a batch adds headwords, rerun rule 34 and B2 R4 over the
  LIVE files too. The coordinator's new `check_meaning_lures` covers the lure half.
- Housekeeping: `refs/refs` is a self-referencing symlink that another session
  created at 06:41. It makes every `refs/**` glob list files twice. It was not
  created here and was left in place.
