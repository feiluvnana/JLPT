# QA report: knowledge/N2 文法, batch 3 (27 points, 81 examples, 54 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch.
Files are in scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `文法_B3.json` | 06f8ab397e05 | 86a3f6c003d3 |
| `文法_B3.ja.json` | ae03fb75659e | 80000769f30c |
| `文法_B3.vi.json` | 2f02702a8586 | 8bfcb975d7f8 |

## Verdict

`QA: FAIL → fixed (14 findings, 5 automatic-fail class). 0 content findings are open after the fixes.`

I merged B1, B2 and B3 into a scratch copy of `knowledge/` (`scratchpad/QA3_repo`), rebuilt the pages there and ran
`check_knowledge.py` on it: **0 FAIL, 0 WARN**. The real `knowledge/` was not touched.

**B3 must merge after B1 and B2.** Six of its `related` ids resolve only in those batches (g-okageda,
g-toshitara, g-kotoda, g-nishiteha, g-sae, g-keigo-ukagau). Merging B3 on its own is refused.

## 1. Blind solve

- **Extraction:** `scratchpad/QA3_blind.py` wrote `QA3_blind.txt` (stem and options only, no ids, no patterns,
  shuffled with seed 33). I solved all 54 items there and saved my answers to `QA3_myanswers.txt` before I opened
  the keys.
- **Result: 54/54 agree with the keys.** As B0 showed, agreement is only the floor. Seven items had a second
  defensible answer, a weak kill, or a rule-2 breach. I found those by splicing each distractor into its stem,
  not by the solve itself.
- **Position balance:** 14/13/14/13 before and after the fixes. Every re-authored item kept its key position.

## 2. Per-entry walkthrough

I read each Shin Kanzen page on the scan (PDF pages 49, 53, 57, 79, 85, 93, 96, 97, 100, 107, 110, 114, 118, 122,
126, 139, 142, 144, 159). I re-counted `official_count` for **all 27 entries**, hit by hit. The counting covered
問題7 keyed options (`B1_p7.json`), 問題8 **cards** (`QA3_p8.py`) and 問題9 keyed options, each checked against the
flat key.

| entry | SK page / 接続 check | official_count (verified) | verdict |
|---|---|---|---|
| g-keigo-okoshi | 敬語, no SK page; official only | 4 ✓ (12/2020-41, 7/2012-38 reprint, 12/2014-39, 12/2016-38) | Q2 furigana fixed (F11) |
| g-teshikataganai | p.122 ✓ (動て形・イ形くて・ナ形で) | 4 ✓ (7/2014-38, 7/2019-34, 7/2024 問題8-46 card, 12/2025 問題8-45 card) | ex1 fixed (F10); Q1 explanation fixed (F14) |
| g-zu-ni-sumu | SK外 ✓ | 3 ✓ (12/2025-39, 7/2025 問題8-47, 7/2016 問題8-49) | OK |
| g-keigo-mairu | 敬語 ✓ | 2 ✓ (12/2023-41, 7/2011-37) | ex2 fixed (F10) |
| g-mono-da-honshitsu | p.114 ✓ 23課1 (▲ 過去形不可, 総称的主語) | 2 ✓, but the cited 12/2010 問題8-47 has ものだ in the printed STEM, not on a card. Replaced by 12/2021 問題9-50 「落語とは…楽しむものなのだ」 (key 1). 12/2014 問題9-51 「これは…するものだ」 is borderline and was not counted | Q2 fixed (F8); cite fixed (F12) |
| g-mono-da-chuukoku | p.118 ✓ 24課3 | 0 ✓ (7/2025-40 is a distractor) | Q2 fixed (F7) |
| g-mono-da-kaisou | p.126 ✓ 26課2A (動た形; ▲ 1度だけ不可) | 0 ✓ (the 7/2012 cite is reading prose, labelled as such) | OK |
| g-mono-da-kangai | p.126 ✓ 26課2B (普通形, ナ形な; ▲ 意志的行為不可, よく・ずいぶん) | **1 → 2** (+7/2023 問題9-51 「いいものだと思います」, key 1) | Q1 fixed (F1); ex2 fixed (F10) |
| g-muke-da | p.49 ✓ | 1 ✓ (7/2018-35. 12/2022-33 「に向けて」 is a different point) | Q2 fixed (F9) |
| g-shidai-da | p.53 ✓ | 2 ✓ (12/2023-38, 7/2019 問題8-43 card. 7/2013-37 and 7/2015-37 are B0's ます形+次第) | ex1 fixed (F10) |
| g-amari | p.85 ✓ | 2 ✓ (7/2015-35, 12/2024 問題8-47 card) | OK |
| g-warini | p.96 ✓ (ナ形 な/である) | 1 ✓ (7/2023 問題8-47 card) | ex2 fixed (F10) |
| g-kiri | p.100 ✓ | **2 → 3** (+7/2013 問題8-46 card 「きり」. 7/2017 問題8-46 is already cited) | count fixed (F12) |
| g-toshitenai | p.107 ✓ (literal) | 0 ✓ | Q1 and Q2 fixed (F3, F4) |
| g-wake-da | p.142 ✓ (literal, incl. だ-の/-な/-である) | **3 → 6** (7/2010 問題9-51, 7/2012 問題9-53, 7/2017 問題9-51, 7/2018 問題9-54, 12/2018 問題9-51, 7/2019 問題9-50; all keyed) | ex2 fixed (F10); count fixed |
| g-gachi | SK外 ✓ | 2 ✓ | OK (doubt judged in §4) |
| g-adv-masaka | p.159 ✓ | 2 ✓ | OK |
| g-joshi-mo | SK外 | **4 → 7** (+7/2012-33 夕飯も食べないで, 12/2019-35 30分もあれば, 12/2015-43 一日もない, 7/2025 問題8-45 card 200名もの) | count fixed |
| g-toshitemo | p.79 ✓ (literal) | **3 → 4** (7/2019-32 plus cards 12/2010 問題8-47, 12/2011 問題8-47, 7/2022 問題8-47. 12/2012 「いずれにしても」 was not counted) | count fixed |
| g-nishitara | p.97 ✓ | 0 ✓ | OK |
| g-nishitemonishitemo | p.57 + p.134 ✓ | 0 ✓ | Q1 fixed (F2) |
| g-eru | p.93 ✓ (▲ 能力的可能には使いにくい) | 0 ✓ | ex3 and Q2 fixed (F6); vi nuance fixed (F13) |
| g-tatokoro | p.100 ✓ | **2 → 3** (+7/2018-36 「病院に行った（ところ）」, key 4) | count fixed |
| g-kanenai | p.110 ✓ | 1 ✓ (12/2023 問題8-45 card) | OK |
| g-to-iu-koto-da | p.139 ✓ (IV-D lists ということだ as 伝聞 only) | 1 ✓ (12/2017-38) | OK |
| g-to-iu-koto-ni-naru | SK外 ✓ (not in IV-D) | 2 ✓ (7/2024-41; 12/2014 問題9-52 「だから…問題ないということだ」) | Q1 fixed (F5) |
| g-buri | SK外 | 2 ✓ | OK |

## 3. Findings

| # | item | class | evidence | fix |
|---|---|---|---|---|
| F1 | g-mono-da-kangai Q1 | doubtful distractor | 「ずいぶん大人になった（ことか）」. ことか needs どんなに・なんと・何度, and both authors flagged it. The doubt counts against the item | ことか → わけではない, which denies what the stem just described (背が伸びて父にそっくり). Both panes rewritten |
| F2 | g-nishitemonishitemo Q1 | second defensible answer (auto) | 「行くとか行かないとか、…返事をください」 reads as a quoted reply. 「行くにつけ行かないにつけ」 is an N1 pair meaning "either way", which is close to the key | options now やら / にしろ / というか / たり. というか・というか is SK p.134's N2 pair for impressions. 行くたり is the item's one 接続 kill. Both panes rewritten |
| F3 | g-toshitenai Q1 | SK copy | 「家計簿をつけ始めてから一日（として）書き忘れたことがない」 matches SK 21課4 ③ 「これまで一度として練習を休んだことはない」 in scenario and predicate (a habit never missed; 〜たことがない) | stem 「八月は雨が続き、晴れた日は一日（　）なかった」 with options として / だけ / ずつ / おきに. 雨が続き kills だけ and おきに |
| F4 | g-toshitenai Q2 | rule 2 breach + weak kill | 誰でも and 誰にでも both die by grammar (two form kills). 「誰かが手を挙げなかった」 dies only on feel | options now 何人かが / 誰でも / 誰一人として / 誰かが, and the stem adds 「…ので、予定より早く終わった」. The new clause kills both partial quantifiers |
| F5 | g-to-iu-koto-ni-naru Q1 | copies an official item's apparatus (auto) | a printer calculation plus the distractor 「ということにする」 reproduces official 7/2024 問題7-41, which the entry itself cites (calculation 通勤時間 → ということになる, distractor ということにする) | new stem, a rule-based deduction: 「部長以上しか出席できない。課長の私は、出席できない（　）」. Options わけがない / どころではない / ということになる / ものだ |
| F6 | g-eru ex3 + Q2 | B0-F8 template ×2 | 「あの真面目な彼が嘘をつくなんて、あり得ない」 and 「彼が約束を忘れるなんて、（あり得ない）」 are the template B0 F8 named (a good person does wrong → unbelievable). The example also printed the quiz frame | ex3 → an elevator with two safety devices, so the accident 起こり得ない. Q2 → last year's champion that cannot win a game this year |
| F7 | g-mono-da-chuukoku Q2 | second defensible answer (auto) | 「借りたものは、早めに返す（ものか）」 is a grammatical defiant refusal, and nothing in the stem ruled it out | stem gets 「（先輩が後輩に）人から…」. An advice frame cannot carry a refusal. Both panes rewritten |
| F8 | g-mono-da-honshitsu Q2 | borderline distractor | 「間違いは起こる（ことだ）」 follows the ordinary 「失敗はよくあることだ」 shape | ことだ → ところだ, which contradicts 「どんなに気をつけていても」 (a generality) |
| F9 | g-muke-da Q2 | SK copy | 「高齢者向けに…開発した」 matches SK 8課5 ① 「一人暮らしの高齢者向けに設計」 | → 目の不自由な人向けに…腕時計. Both panes rewritten |
| F10 | 6 examples | SK scenario copies + self-echo | teshikataganai ex1 (面接の結果が気になって ≈ SK 25課2 ③ 面接…心配でならない, same page); kangai ex2 (「世界も狭くなったものだ」 ≈ SK 26課2 ⑤ 「便利な世の中になったものだ」); warini ex2 (「七十歳という年齢のわりには足腰が丈夫」 ≈ SK 19課 復習 「80歳という年齢を考えると…若々しい」); shidai-da ex1 (努力次第 ≈ SK 9課3 ② トレーニング次第で勝てるかどうか); wake-da ex2 (money arithmetic ≈ SK IV-E ② 会費); mairu ex2 (「ただいま担当者を呼んで参りますので…お待ちください」 was its own Q1 stem nearly word for word, so the card showed the answer) | all rewritten, with new vi `example_notes` |
| F11 | g-keigo-okoshi Q2 | wrong furigana (pronunciation) | 「午後２｜時《とき》」. ２時 is じ, and speech would read it as とき | → 《じ》 |
| F12 | 6 counts + 1 cite | official_count wrong | see §2. Every miss was a 問題8 card or a 問題9 key. The authors' corrections covered 問題7 only | corrected, and one confirming source added per entry |
| F13 | vi honshitsu `compare`, vi eru `nuance` | claim vs SK | the vi pane said 感慨 = 「thể た kèm よく/ずいぶん」, but SK p.116 has 普通形 (ex1 「珍しいこともある」 is non-past). It also said 「英語を話し得る」 "là sai", while SK p.83 says 使いにくい | reworded |
| F14 | ja teshikataganai Q1 (+2 more) | wrong kill named / at the cap | the explanation killed 寂しがるおそれがある as "third person". The real kill is おそれがある (a future bad event) against the current state 毎日. Three ja explanations sat at exactly 80/80 | rewritten. ja quiz max is now 77 and vi quiz max 135 |

**Provenance scan (my own, 10-char windows over `refs/**/*.md` + `tests/imported-*`)**, run before and after the
fixes (`QA3_prov.py`). The only hits are stock phrases (少々お待ちください, …なければならない。, うまくいかなかった。).

**vi rule 6 scan:** no kana/kanji run of 2+ characters outside 「」 apart from the grammar labels. **Independence:** the vi
explanations target a different distractor from ja in most items (for example okoshi Q1 おいでになり vs 参りまして,
teshikataganai Q2 楽しみにするしかない vs わけがない), and I found no mirrored sentences. **Metadata leaks:** none.

## 4. The authors' flagged doubts, judged

- **ものだ split into 4: genuine.** SK gives separate headwords: 23課1 (本質), 24課3 (忠告), and 26課2 A (回想, 動た形 only,
  ▲ 1度だけ不可) / B (感慨, 普通形, ▲ 意志的行為不可). Their 接続 and constraints differ.
- **ということだ → 伝聞 + 結論 (SK外): genuine.** SK IV-D p.129 lists ということだ as 伝聞 only. The 結論 reading is keyed
  officially twice (7/2024-41, 12/2014 問題9-52).
- **感慨 Q1 ことか: replaced (F1).** SK itself pairs ずいぶん with 感慨ものだ, so the stem stays.
- **回想 Q1 ことだ: OK.** 「よく寄ったことだ」 is neither 忠告 ことだ (past tense) nor B2's 感嘆 ことだ (イ/ナ形 feelings).
- **わけだ Q1 vs わけではない: OK.** 「それじゃあ」 draws a consequence from A's line. わけではない would deny the very
  consequence that line supports.
- **伝聞 Q2 というものだ: OK.** SK p.104 ▲: というものだ is a 常識的評価, so it cannot close a 「によると」 hearsay line.
  Noted: official 12/2017-38 also pairs によると with a というものだ distractor. The scenario differs, so this is not a copy.
- **本質 vs 感慨 (「珍しいこともあるものだ」): OK as 感慨.** The subject is one specific event (a strict teacher laughing),
  which is SK B's あきれる・驚く. It is not a 総称的 truth.
- **がち (TOO_EASY in bunpou.md) as a knowledge entry: OK.** It is an official N2 key twice (7/2022-39, 12/2013-44). The
  TOO_EASY list governs exam keys, not study cards. The list and the archive disagree, though (see R5).
- **Counts:** I re-verified all 27, not a third. Every 0 holds (として〜ない, 得る, にしたら, にしても〜にしても, 忠告, 回想).
  Six counts were still wrong after the author's corrections (§2).
- **vi: joshi-mo Q2 「百人きり」: OK.** 「人気の店なので」 predicts many people, and きり ("only") contradicts it. しか is the
  one 接続 kill.
- **vi: kaisou Q2 verb-form item: OK under rule 2.** 出かける, 出かけた and 出かけない all attach to ものだ; only 出かけよう
  does not. The choice rests on 十年前…住んでいたころ + 週末のたびに (a past habit).
- **vi: kangai Q1 and nishitemonishitemo Q1:** fixed (F1, F2).

## 5. Root causes

| finding(s) | code | recurrence | proposed edit |
|---|---|---|---|
| F3, F9, F10 | RULE-UNENFORCEABLE | B0 (F6–F8) and B3: systemic | **R1** below. R3 names "the cited page's numbered examples". The copies here came from the 復習 lines and from the NEIGHBOURING headword on the same page (25課2 beside 25課1), and one example duplicated its own quiz stem |
| F5 | RULE-MISSING | first instance | **R2**. The provenance rule compares sentences, not an item's apparatus (scenario type + distractor) against the official item the entry itself cites |
| F12 | RULE-UNENFORCEABLE | B0 (8/20 wrong) and B3 (6/27 still wrong after a correction pass) | **R3**. R4 says "grep booklets", and authors grep 問題7. A promoted script would decide it |
| F1, F2, F7, F8 | RULE-UNENFORCEABLE | B0 F1–F3 and B3 | **R4**. The authors' splice lists named kills of the form "sounds odd / some speakers accept". A kill resting on feel is not a kill |
| F4 | RULE-IGNORED | — | rule 2 (at most one 接続-only kill) is specific and was skipped. Nothing to change |
| F6 | RULE-IGNORED | — | B0 F8 names this exact template. Nothing to change beyond R1's "list the named templates" |
| F11 | GATE-BLIND | first found | **R6**: a WARN in `check_knowledge` for `時《とき》` after a numeral (`[0-9０-９一二三四五六七八九十]｜?時《とき》`). The founding string is `午後２｜時《とき》` from pre-fix B3 g-keigo-okoshi Q2. I have not added or run it (reviewers do not edit the gate) |
| F13, F14 | RULE-IGNORED | — | "claims no ref backs are verified or cut" (brief step 5). Nothing to change |

### Proposed additions

**`BATCH_JA_BRIEF.md`**

- **R1 (extends R3):** "Read your examples and stems against EVERY sentence printed on the cited SK page. That
  includes the 〔復習〕 lines at the top and the examples of the other headwords on the same page, not just your own
  headword's ①②③. Never let an example repeat one of your own quiz stems: the card is shown next to the quiz, so the
  example gives the answer away. Known templates to avoid are 'a good person did X → 信じがたい/あり得ない' (B0 F8, B3 F6)
  and 'technology → 世の中/世界が〜になったものだ' (B3 F10)."
- **R2 (new):** "Open every official item you cite in `sources`. Your quiz item must not reuse its scenario type
  together with any of its distractors. (B3 F5 reproduced 7/2024 問題7-41's calculation + ということにする while
  citing it.)"
- **R3 (extends R4):** "A hit is a 問題7 keyed option, a 問題8 CARD, or a 問題9 keyed option. The form printed in a
  問題8 STEM outside the cards does not count (B3's 12/2010 問題8-47 ものだ). Run the lister over all three."
  Suggested tool: promote `scratchpad/QA1_hits.py` + `QA3_p8.py` (both read `B1_p7.json`/`B1_p89.json`) into
  `.agents/jlpt-knowledge/scripts/official_hits.py <regex>`. It printed every B3 miss in one run.
- **R4 (extends R1):** "If your splice list says a distractor dies because it 'sounds odd' or 'some speakers might
  accept it', replace it. Do not defend it. Any doubt you flag in your own report means replace, by default."

**`BATCH_VI_BRIEF.md`**

- **R5-vi:** "When a vi field states a 接続 or a restriction (thể た only, 'là sai'), it must match the SK page's
  wording: SK's 使いにくい is 'nghe gượng', not 'sai'."

**`question-authoring/references/bunpou.md` (owner decision, not applied)**

- **R5:** `〜がち` is listed as TOO_EASY "alone", yet official N2 keyed it in 7/2022 問題7-39 (休みがち) and 12/2013
  問題7-44 (思ってしまいがち). Either narrow the entry (for example 名詞+がち like 病気がち) or cite the evidence for it.

**`jlpt-knowledge/SKILL.md` §Quiz integrity**

- Add as rule 8: "The official_count lister counts 問題7 keys, 問題8 cards and 問題9 keys." Add R1's two sentences to
  rule 3.

## 6. Coverage

- Blind solve on all 54 items, then a splice of every distractor on all 54.
- SK page read for all 21 SK-cited entries (19 PDF pages). Official-only entries were read in booklet.md.
- official_count re-verified for all 27 entries across 問題7, 問題8 cards and 問題9 in the 31 sittings.
- Provenance: 10-char scan over all 81 examples and 54 stems, before and after the fixes. Each example was also read by
  hand against its SK page.
- Furigana: every `漢字《よみ》` pair was listed and read. One wrong (F11).
- Bands: `knowledge_data.plain()` from the gate. ja maxima: meaning 29, usage 75, nuance 73, compare 80, quiz 77.
  vi maxima: 59/165/170/174/135.
- Gate: merged B1+B2+B3 into a scratch copy, rebuilt, ran `check_knowledge.py`: 0 FAIL, 0 WARN.

## 7. Skips

- `make check` on the real tree was not run. The batch is not merged yet, and merging is the coordinator's step.
  The scratch-copy gate run stands in for it.
- Pitch and speech were not ear-checked (the 文法 pitch flag is off).
