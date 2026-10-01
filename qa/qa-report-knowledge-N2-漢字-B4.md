# QA report — 知識 N2 漢字 batch 4 (50 kanji, 37→41 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes.

Files reviewed (scratch `batches/`):
- `漢字_B4.json`, `.ja.json`, `.vi.json`
- `.backlinks.json`, `.backlinks.vi.json`
- `K4_live_meaning_fix.json` (8 ja edits) and `K4vi_live_meaning_fix.json` (4 vi edits)

Validation ran on a scratch root, `QAK4_root`:
- `.agents/` and `knowledge/` were copied fresh; everything else is symlinked.
- `QAK4_run.sh` applies both live fix files to the copied `漢字.{ja,vi}.json`.
- It then runs `merge_batch.py`, re-pointed as `QAK4_merge.py`, with the batch and both back-link files.
- Last, it runs the builder and `check_knowledge.py`.

The real `knowledge/` was not edited.

## What was checked, and how

| area | method | result |
| - | - | - |
| ids / author remaps | SK 漢字 目次 (PDF 134–139), read in full | **好 = No.84** (ステップ1 [カ] row) and **求 = No.640** (第33回) are correct. **841 = 測** and **932 = 箱**, so the inventory rows are mis-parsed, as the author's "Known inventory defects" note says. **額 = 603** is live. All 50 numbers and every `group` (回 boundaries 801/826/851/876/901/926/951/976/1001/1026) match. None of the 19 kanji the note keeps as `kx-` appears in the 目次 (模 隣 至 密 削 焦 抽 却 撮 影 誘 勧 充 範 潔 姿 悔 稚 傷) |
| `on` / `kun` / `words` | SK 別冊 list pages, PDF 146, 181, 190–202, rasterised with pdftoppm and read page by page | 50/50 match the page. Six kun readings the page does not print are each attested by an official key: 束ねる 12/2018 2-9; 恥 はじ 7/2019 1-4; 導く 7/2012 2-6; 敗れる 7/2011 1-1; 絡まる 7/2024 1-3; 養う 7/2018 2-7. Added compounds come from official items: 善良, 総額, 冷蔵庫, 背骨, 大幅, 保証, 疲労, 登録, 途端, 容姿, 迷惑, 逃亡 |
| `official_count` (rule 40) | Parser over every 問題1 sentence and 問題2 key in 31 sittings (302 items). The 10 items it misses were read by hand. The four options of every cited item were printed | 50/50 correct. Every 問題2 hit has the kanji replaced in some option (e.g. 造: 製増/制造; 張: 広張/拡長; 陽: 揚気; 労: 疲老). False hits were rightly not counted: 季節 7/2014 1-5; 努力 12/2011 1-4; 失敗 7/2015 1-3; 平等を求めて 12/2023 1-5; 保存 7/2018 1-2; 連絡 7/2013 1-3. Rule 35 cross-check: all 24 live partners of shared items already credit them (調 額 庫 直 重 負 骨 批 大 逃 易 要 人 良 製 拡 証 短 乱 気 収 疲 登). 失 and 保 rightly do not |
| prose option claims | Every 「…」 option list in ja/vi nuance and compare was checked against the printed options, including 7/2012 2-8 責極的, 12/2024 2-8 尊う/礼う, 7/2013 2-9 担たす, 7/2012 2-10 背, 7/2015 2-7 怖かせて, 12/2025 2-7 冷んだ | all true |
| generated quizzes | All 50 `#r` and 50 `#m` items were dumped in both languages, before and after the fixes. Gloss-word overlap was scanned against all 260 entries (ja substrings, vi words and bigrams), excluding linked pairs. The headword-kanji-in-gloss scan was run too | No fabricated misreading is a real reading of its word (さどう, ほう and れいたい are words, but not readings of 指導, 補う or 冷たい). Collisions: F3. Lures: none |
| live fix files | 8 ja glosses: each removed a batch-4 headword (暮 戻 内容→容 張 評 影響/与 幅). 4 vi glosses: 負, 易, 願, 務 | All 12 accepted unchanged; rescan shows no batch-4 headword in any live gloss. Note: the 易 vi fix ("dễ dãi, qua loa" ← 安易) drops the trade sense. That is acceptable now that 貿↔易 is linked (F3) |
| Hán Việt | All 50, plus the six 「Hán Việt dễ lừa」 claims | F5. Real traps, kept: 恐怖 khủng bố, 迷惑 mê hoặc, 容易 dung dị, 陽気 dương khí, 依頼 ỷ lại |
| examples | 10-char window scan and shared-token lister over refs/**/*.md, tests/imported-*, every `knowledge/N2/*.json` (文法 stems included) and the official scripts. Every replacement was rescanned, in 7 rounds | F1 |
| furigana | Every example and every new prose field read by hand | F2 |
| rule 6 / rule 18 | script; gate `check_prose_citations` | clean |
| gate | scratch merge before and after the fixes | before: 0 FAIL, 0 WARN. After: **0 FAIL, 0 WARN**; merge prints no REVIEW line |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | examples 途 努 軟 迷 背 暮 冷 求 尊 率 節 責 | major (途 冷 軟 迷 求 節), minor (rest) | Scene and frame copies, all 12 of them inside the module. 途 「会社へ行く途中で、かさを家に忘れたことに気がついた」 = 文法 g-tatotan 「…座席に傘を忘れたことに気がついた」. 冷 「スープが冷めないうちに、早く食べてください」 = g-uchini 「料理が温かいうちに、どうぞ召し上がってください」; the token lister missed it. 軟 (shoes, long walk, feet hurt) = g-hanmen and g-nikui quiz stems. 迷 「知らない町で道に迷い…聞いた」 = g-ni-kagiru. 求 (member card at the shop entrance) = g-nitsuki. 節 (choose clothes the night before to save morning time) = 読解 r-sk-02 quiz. 尊 (athlete runs to the end) = g-koto-naku. 率 (new PC → work speeds up) = g-toiumonodehanai. 努 (daily effort → can swim) = g-uchini. 背 (heavy bag, walk from the station) = 聴解 l-sk-17. 暮 (bring in laundry before…) = g-uchini quiz. 責 (sibling, homework help) = g-nagara-mo quiz. The 7 rounds of replacements also caught: 語彙 v-0301 (いすの高さを調節); live 調 k-0466; 語彙 v-0111 (自分を責めないで); 語彙 v-0431 (用途); 語彙 節約 (水を節約); 文法 g-bekida, g-ni-ouji-te, g-tatotan; 聴解 l-sm-12 (夜行バス); SK/Hajimete 夢をかなえる; 12/2012 健康のためにたばこ; 7/2013 初めて…決勝; 12/2013 静かな生活 | 12 new scenes. 節 竹の節. 責 ゴールキーパー. 求 助けを求めた. 尊 美術の先生. 率 宝くじの確率. 途 電話が途中で切れた. 努 階段を使うよう努める. 軟 畑の土. 背 ランドセル. 暮 冬は日が暮れるのが早い. 迷 メニュー. 冷 風呂の湯. vi example_notes rewritten from each new sentence. Final scans are clean | Rule 35 and B3 R3 say the scene scan spans the module. The authors ran it (`K4_prov.py`) but read it at a ≥3-token threshold: 7 of these 12 shared only 2 tokens, or matched on frame (冷/温かい, スープ/料理). See R1 |
| F2 | 担 example | minor (pronunciation) | 「ケーキ｜作《つく》り」: the compound is ケーキづくり (rendaku). ▶ speech reads the ruby aloud | → 「作《づく》り」 | `check_ruby_suspects` cannot see rendaku |
| F3 | related pairs | major (領/受, 容/収, 求/願), minor (rest) | Gloss collisions the generator cannot see. ja 領 「うけとること」 = 受 「人から来たものをもらうこと」. ja 容 「なかに入れること」 = 収 「うちに取り入れること」 (収容). ja 求 「ほしいものを…」, and its example's 'request' sense, compete with 願 「こうなってほしいと思い、たのむ」 and 望. vi 要 "đòi hỏi" competes with 求 "đề nghị" (要求). 絡↔乱 was raised by the vi author: both are used of hair (7/2024 1-3 髪が絡まって; 7/2023 1-2 髪が乱れて). 貿↔易 and 背↔負 are compound partners (rule 29); the vi gloss fixes removed the collision only in vi, and ja 負 still says 「せおって」 | 9 pairs linked both ways, with a compare in each language: 絡↔乱, 貿↔易, 背↔負, 求↔要, 求↔願, 求↔望, 容↔収, 領↔受. Live targets went from 37 to 41 (new: 乱, 易, 要, 受); 負, 願, 望, 収 were extended. 乱's back-link at first dropped 「みだれて」/「散らかる」; both restored (12/2010 2-8 options 破れて 乱れて 荒れて 暴れて). Checked in the dump and left unlinked because no gloss collides: 冷/蔵, 保/証, 失/敗, 指/導, 陽/気, 暴/乱, 要/領, 直/率, 付/属, 逃/亡, 凍/閉 (đóng) | BATCH_VI and LEX_JA briefs: the vi author found 絡/乱 but had no step for a compound partner that appears only in `words` (貿易, 背負う, 要求). See R2 |
| F4 | vi 評 and 労 compares | minor | Unsourced contrast (rule 9). 「批判」 "nghiêng về chê"; 「疲労」 "mệt tích lại lâu ngày" vs 「疲れる」 "mệt nói chung"; usage "mệt mỏi kéo dài" | 評: definitional (批評 nhận xét hay dở; 批判 chỉ ra cái sai, khuyết điểm). 労: verb vs noun, "「疲労がたまる」"; usage "(sự mệt mỏi)" | BATCH_VI_BRIEF ADDED rule, applied |
| F5 | vi Hán Việt 凍, 幅 | minor | "ĐỐNG (quen đọc ĐÔNG)" and "PHÚC (quen đọc BỨC)": hvdic/Thiều Chửu lists both readings as dictionary readings (凍 đông, đống; 幅 phúc, "một âm là bức") | "ĐÔNG, ĐỐNG"; "PHÚC, BỨC" (the B2 F5 precedent for 住) | rule 29 says "(quen đọc …)" is only for a non-dictionary everyday reading |

## Author items, judged

1. **Id remaps.** All confirmed on the 目次: 好 is k-0084, 求 is k-0640, and dropping k-0932 (箱) is right. The `N2.md` "Known inventory defects" paragraph is accurate.
2. **Links.** 絡↔乱 is linked. 貿↔易 and 背↔負 need links in BOTH panes: the vi fixes covered only vi, and rule 29 asks for compound partners. Both linked (F3).
3. **Hán Việt.**
   - **率 SUẤT** stays. hvdic lists luật/lô/soát/suý/suất, and Thiều Chửu's 率直 sense and the modern compounds (xác suất, hiệu suất) are suất. Nothing ties LUẬT to the taught compounds, so it is not added.
   - **凍** → "ĐÔNG, ĐỐNG" (F5).
4. **蔵/庫, 造/製.** Both draw a real distinction:
   - 庫 is the building or container; 蔵 is storing.
   - 製 is making products from materials; 造 also covers structure (構造), and 設 covers buildings.
   - All three are linked, and no unlinked gloss competes with them.
5. **重《ちょう》 in the 尊 nuance.** It stays: the ruby agrees with 「ここではチョウ」 and teaches the reading the item tests.
6. **Prose claims.**
   - 補 has 衤 and 暮 has 日 at the bottom: true (幕 巾, 募 力, 墓 土).
   - 批判 and 疲労 overreached and were rewritten (F4).

**Counts:** 5 findings: 2 major (F1, F3), 3 minor. Edits:
- 12 examples, each with its vi note, plus 1 furigana fix
- 9 related pairs, with 6 batch compares × 2 languages
- 4 new and 4 extended back-link compares × 2 languages
- 4 vi fields (凍, 幅, 評, 労)

The vi text of the new compares was written in this QA context, which had also read the ja pane. As in B2 and B3, this breaks the "written, not translated" split for those 20 fields. They were written from the kanji facts and the official items, not from the ja sentences. A vi-only pass may re-author them.

## Root causes and proposed rules

- **R1 (F1) — RULE-UNENFORCEABLE.** Proposed text for the LEX_JA_BRIEF and SKILL rule 35: "Read EVERY overlap hit with ≥2 shared content tokens against `knowledge/<LEVEL>/*.json`, quiz stems included, and compare the FRAME (time frame + predicate: 〜うちに食べる / 温かいうちに召し上がる), not only the nouns." The threshold of 3 hid 7 of the 12. A gate WARN on a shared (predicate stem + one content noun) pair between a 漢字/語彙 example and any 文法 example or stem would have caught 冷, 迷, 途 and 軟.
- **R2 (F3) — RULE-MISSING.** Proposed text for both author briefs: "For every `words` compound whose other kanji is also an entry, read both glosses in BOTH languages. Link them when either gloss names the compound's sense, or when one pane's fix is the only thing keeping them apart." A gloss fix in one language is not a fix for the other.
- **R3 (F2) — GATE-BLIND.** Add rendaku compounds (〜作り, 〜付き, 〜箱, 〜棚) to `check_ruby_suspects`: WARN on 「<kana or katakana>｜作《つく》り」.
- Housekeeping: `CLAUDE_YOU_MUST_READ_THIS.md` sits untracked at the repo root. It asks for full 語彙/漢字 coverage. I left it alone, because it is outside this review.

## Merge steps for the coordinator

1. Apply `batches/K4_live_meaning_fix.json` and `batches/K4vi_live_meaning_fix.json`, both unchanged, as `meaning` overwrites in `knowledge/N2/漢字.ja.json` and `漢字.vi.json`. This is the same step `QAK4_run.sh` runs.
2. `python3 merge_batch.py 漢字 4`. It should print +50 entries and back-links applied to 41 live entries, with no REVIEW lines.
3. `make knowledge`, then `make check`. Read every line.
