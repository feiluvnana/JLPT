# Blueprint rerolls — 20261102_2

Base draw: `make sample 20261102_2 SEED=60783915`. The seed came from the
orchestrator's RNG (`secrets.randbelow(10**8)`) and was used verbatim. It had
0 hits in `logs/ledger.json` before the draw. The authoritative record is the
spec's `seed` string and `rotation.reroll_log`; the ledger row mirrors both.
This note keeps no reroll count: count from the `seed` string.

## Stage-1 reroll: one `--reroll-one`, with a fresh RNG seed

The seed came from `python3 -c "import secrets; print(secrets.randbelow(10**8))"`
(0 ledger hits). Nothing was hand-substituted. The index chose which entry
left; the sampler chose which entry arrived.

### 1. `reading_topics:9` (問題12): 地域活性化 → 人間関係, seed 72058050

- **Rule.** `exam-blueprint` §"The four theme rules", rule 4: no theme headlines
  two consecutive papers. Index 9 is always 問題12, a 読解 headline.
- **Collision.** 地域活性化 is the theme of 20261102_1's 聴解問題5-1番 (公園の
  ゴミを減らす提案), a headline surface one paper back.
  `check_theme_repeat_cross_test()` FAILs a repeat that sits on a 読解
  headline of the current paper (`overlap_all & cur_reading_head`). Only a
  theme carried by THIS paper's own composed 聴解問題5 drops to a WARN.
- **Why at stage 1.** No gate can see this before Stage 3 writes the
  `logs/topics.json` row, and by then the A/B pair would be written. The
  sampler has no cross-test headline constraint (`exam-blueprint` §"WHAT THIS
  STILL DOES NOT FIX").
- **Exclusions.** `--exclude-theme` was given every headline theme of the
  previous two papers that this paper is not already keeping: 地域活性化, 交通,
  科学・技術 (20261102_1) and 行政・手続き, 医療・福祉, 消費・経済 (20261008_1).
  Two-back themes were excluded too because 問題14 住まい already spends the
  two-back budget of one (住まい = 20261008_1 問題13). Kept themes are excluded
  by the sampler. That left three legal themes: 防災, 文化・伝統, 人間関係.
- **Result.** 人間関係. It headlines neither 20261102_1 nor 20261008_1. Its
  `avoid` list (60 subjects) was rebuilt by `draw_authored_themes()`.

## Checked and found compliant, so no reroll

- **Theme rules (読解 headlines 問題9 防災 / 問題12 人間関係 / 問題13 メディア・情報 /
  問題14 住まい).**
  - Rule 1: four distinct. Rule 3: the 12 drawn themes plus the cloze's 防災
    are 13 distinct. Rule 2: no headline theme appears on a non-headline
    読解 surface.
  - Rule 4, one back (20261102_1: スポーツ・余暇, 交通, 食, 子育て・家族, and
    聴解問題5 地域活性化, 科学・技術): no overlap after the reroll.
  - Rule 4, two back (20261008_1: 行政・手続き, 環境, 住まい, 医療・福祉, and
    聴解問題5 旅行・観光, 消費・経済): overlap = {住まい} (問題14) = 1, which is the
    budget. It is now spent, so the cloze's theme was drawn only from values
    that headline neither paper (`qa/dokkai-allocation-20261102_2.md`).
- **問題1 訓読み: 2 of 5** by `is_kun_target()` (新たな, 軟らかい; 植木 scores
  音 under the no-tail 湯桶/重箱 ruling). The band is 2–2.
- **問題1 two targets share 植** (植物(しょくぶつ), 植木(うえき)). No
  exam-blueprint or question-authoring rule bars it, and the two readings
  differ, so it is not a duplicate draw. Flagged for the 文字・語彙 author:
  neither item's option set may print the other item's keyed reading, or one
  item cues the other.
- **問題2:** 和語 by `is_wago_orthography()` 2 (一通り, 一休み), inside 1–3. Bare
  compounds by `is_bare_compound()` 3 (気体, 意義, 関東), at the cap of 3.
- **問題7 敬語: 1 of 12** (敬語:いらっしゃる). The cap is 2.
- **Grammar identity.** 問題7 〜つつも against 20261102_1's 問題8
  経過状況(〜つつ…する): neither entry is in `grammar_point_identity`, and the
  つつ family is taken-only (in-paper), so two consecutive papers may each draw
  one. Checked on the page anyway, because a shared Shin Kanzen 目次 heading
  would make it a cooldown repeat the map cannot see. The SK N2 文法 索引 (book
  p.209, PDF p.218) heads 〜つつ (p.13, with 〜つつある) and 〜つつ(も) (p.65)
  separately. So they are two points, and nothing was rerolled. In this paper
  no 問題8 form shares a point or family with a 問題7 form (〜に伴って 9課2 and
  〜てたまらない 25課1 are the only mapped ones).
- **Answer positions:** 22/20/24/24 over the 90 four-choice items. The band is
  19–27. 聴解問題5's last two keys are 1 and 2, so they are not equal.
- **Rotation:** the sampler printed no relaxation, and `make check` reads every
  category against its frozen window (see the stage-1 report).

## Stage-2 rerolls: two `--reroll-one`, seeds given by the orchestrator

Both targets were reported undrawable by the stage-2 文字・語彙 author under
`moji-goi.md` §"Build the set BEFORE you accept the target". Neither was
hand-substituted.

### 2. `kanji_reading:1` (問題1-2): 新たな(あらたな) → 荒れる(あれる), seed 81861961

- **Finding.** The printed span 新たな carries the okurigana 「たな」. With the
  kanji covered, □たな admits only へた(な) and あらた(な) as real na-adjectives,
  so no four-option 訓 set exists. Neither 新's readings (シン・あたら・あら・にい)
  nor a look-alike yields a real □たな word (branch a empty). No three
  same-field real words exist either (branch b empty). The target is
  undrawable.
- **Command.** `sample_items.py --test-id 20261102_2 --reroll-one
  kanji_reading:1 --seed 81861961 --reason "kanji_reading: 新たな(あらたな)
  undrawable — moji-goi Part 1 okurigana exposure: …"`. The seed came from the
  orchestrator's RNG and was used verbatim.
- **Result.** 荒れる(あれる).
  - `is_kun_target` = True, so 問題1 stays at 2 of 5 訓.
  - `has_reading_trap` = False.
  - `answer_positions` 問題1[1] = 4 is unchanged.
- **Drawable check.** Branch (b), field=安定した状態の崩れ:
  ゆれる/くずれる/みだれる/あれる.
  - All four fit the skeleton ^.+れる$ (□れる).
  - All four are real 一段 verbs (揺れる・崩れる・乱れる・荒れる, 常用音訓), so the
    訓 set is non-word-free.
  - 荒れる has one reading. あらい belongs to the spelling 荒い and is kept out
    of the options.
  - The set shares no kanji with 植物 or 植木, so the 植 note is unaffected.
  - Authored as 問題1-2 「今夜は海が**荒れる**そうです。」, key 4.

### 3. `kanji_reading:3` (問題1-4): 軟らかい(やわらかい) → 引っ越し(ひっこし), seed 93737640 — STILL UNDRAWABLE

- **Finding.** The printed span 軟らかい carries the okurigana 「らかい」. With
  the kanji covered, □らかい admits only やわらかい as a real i-adjective
  (なめらか・ほがらか・やすらか are na-adjectives). Official 7/2024 tests
  柔らかい in 問題2, not 問題1. The target is undrawable.
- **Command.** `sample_items.py --test-id 20261102_2 --reroll-one
  kanji_reading:3 --seed 93737640 --reason "kanji_reading: 軟らかい(やわらかい)
  undrawable — moji-goi Part 1 okurigana exposure: …"`. The seed came from the
  orchestrator's RNG and was used verbatim.
- **Result.** 引っ越し(ひっこし).
  - `is_kun_target` = True.
  - `has_reading_trap` = True (促音).
  - `answer_positions` 問題1[3] = 2 is unchanged.
- **Drawable check: FAILS.** The skeleton is ^.+っ.+し$ (□っ□し).
  - **Branch (a) is empty.** 引 reads イン・ひ-く・ひ-ける and 越 reads エツ・こ-す・
    こ-える. The look-alikes 超 (こ-す) and 起 (お-こす) give no real □っ□し noun
    (おっこし is not a word).
  - **Branch (b) is empty.** The real words matching □っ□し are
    ほったらかし・やりっぱなし・つけっぱなし・ぶっとおし・いっぱし, and none shares a
    semantic field with 引っ越し (住まいを移ること). A label over them would be a
    form label (「〜っ〜し の名詞」), not a field. `moji-goi.md` §"The two-branch
    rule" fails such a label.
  - **Corpus check.** A regex sweep of the Hajimete, Shinkanzen and Soumatome
    extracts plus the 31 archive booklets for [一-龯ぁ-ん]+っ[一-龯ぁ-ん]+し
    found no other moving-related noun; the only lexical hit was 引っ越し itself.
  - **Next step.** Reported to the orchestrator for another `--reroll-one
    kanji_reading:3`. The draw must stay 訓 and must not share 植. 問題1-4 is
    still a scaffold placeholder in `_sections/問1-6_文字語彙.md`.

### 4. `kanji_reading:3` (問題1-4): 引っ越し(ひっこし) → お礼状(おれいじょう), seed 65436359

- **Finding.** Entry #3's drawable check failed. 引っ越し's skeleton □っ□し admits
  no same-field real 訓 set: ほったらかし/やりっぱなし share the form only, so a
  label over them would be a form label, not a field.
- **Command.** `sample_items.py --test-id 20261102_2 --reroll-one
  kanji_reading:3 --seed 65436359 --reason "kanji_reading: 引っ越し(ひっこし)
  undrawable — …"`. The seed came from the orchestrator's RNG and was used
  verbatim. The sampler auto-excluded 軟らかい.
- **Result.** お礼状(おれいじょう).
  - `is_kun_target` = True, because the printed prefix 「お」 is kana. 問題1 is
    therefore 2 of 5 訓 (荒れる, お礼状), inside the 2–2 band.
  - 植木 scores 音 under the no-tail ruling, as in the stage-1 note.
  - `has_reading_trap` = True (拗音 じょう).
  - `answer_positions` 問題1[3] = 2 is unchanged.
- **Drawable check: passes, in the 背骨 shape.** The body 礼状 is an on-reading
  compound, so the set is built from derivations, as for 背骨 (12/2024) and
  物音 (20261102_1), and carries no field.
  - Options: 2×2 {れい／れ}×{じょう／しょう} → おれいしょう/おれいじょう/
    おれじょう/おれしょう.
  - All four fit the skeleton ^お.+$. Each non-key option is a 長短 or 清濁
    derivation of the key's own reading, which `moji-goi.md`'s RESOLVE step 6
    permits.
  - The set shares no kanji with 植物 or 植木.
  - It avoids 20261102_1 問題1-2's 礼=らい trap.
  - Authored as 問題1-4 「私は先生に**お礼状**を書いた。」, key 2.

## QA-repair reroll: one `--reroll-one`, seed given by the orchestrator

### 5. `word_formation:1` (問題3-12): 〜振り(久し振り) → 下〜(下請け), seed 91189987

- **Finding.** qa-report-20261102_2 F1 (自動不合格), root cause RC-1. The
  drawn carrier 久し is not a productive base. 久しぶり is one lexicalised word
  taught at N5 (お久しぶりです), so the item was answered from the N5 word, not
  from the N2 affix 〜ぶり. The pool entry names the carrier, so this was a pool
  defect, not an authoring one.
- **Command.** `sample_items.py --test-id 20261102_2 --reroll-one
  word_formation:1 --seed 91189987 --reason "word_formation: 〜振り(久し振り)
  too easy — …(qa-report-20261102_2 F1)"`. The seed came from the
  orchestrator's RNG and was used verbatim.
- **Result.** 下〜(下請け). `answer_positions` 問題3[1] = 2 is unchanged.
- **Drawable check.** The tested affix 下〜 is drawable; the pool's carrier
  下請け was not used.
  - **Why not 下請け.** 「請け」 is not a free base, so 下請け tests one
    lexicalised business word, not the affix. That is the shape RC-1 bars.
  - **The carrier used.** 下〜 in its productive sense 「本番の前の準備としての」
    (下書き・下見・下調べ・下準備), carried on 下書き.
  - **Options.** 上/下/裏/表. All four form real 〜書き words (上書き・下書き・
    裏書き・表書き), so knowing 「書き」 decides nothing; the prefix's meaning
    does. 下書き appears bare in official 12/2017 読解 (booklet L445).
  - **The stem.** 「私は作文を、まず鉛筆で（　）書きしてから清書した。」, key 2.
    「まず鉛筆で…清書した」 fixes the pre-清書 stage. 上書き (writing over),
    裏書き (endorsement) and 表書き (envelope front) each die for their own
    reason.
  - **Second-answer screen.** 前書き (preface) was kept out of the options
    because it is a second real 〜書き word near the frame.
  - **Distinct affixes.** The twelve 問題3 affixes stay distinct (半/仮/副/超,
    上/下/裏/表, 型/式/流/順).
- **Refused by the orchestrator (ruling after the authoring above).** The
  下書き item was not accepted. Under `exam-blueprint`, a parenthetical is a
  disambiguating gloss, so 下〜(下請け) fixes the 「subordinate」 sense of 下〜.
  下書き tests a different sense (「preliminary」), which makes it a sense
  substitute, i.e. a hand substitution. The orchestrator rerolled the slot
  (entry #6), and the 下書き item was removed from the fragment.
- **Pool follow-up (exam-blueprint).** 下書き is also an `orthography` entry,
  and this paper does not record it as drawn there. The pool's `下〜(下請け)`
  carrier should be re-carriered to a productive base (e.g. 下〜(下書き) or
  下〜(下調べ)) per RC-1, and 〜振り(久し振り) re-carriered to 〜ぶり(十年ぶり) or
  retired.

### 6. `word_formation:1` (問題3-12): 下〜(下請け) → 〜色(地方色), seed 1061369

- **Finding.** Entry #5's drawn sense (下〜 = subordinate, carrier 下請け) has
  no productive base: 「請け」 is not a free word. Its only authored item tested
  a different sense and was refused as a substitute.
- **Command.** `sample_items.py --test-id 20261102_2 --reroll-one
  word_formation:1 --seed 1061369`. The seed came from the orchestrator's RNG
  and was used verbatim.
- **Result.** 〜色(地方色). `answer_positions` 問題3[1] = 2 is unchanged.
- **Drawable check: passes, in the drawn sense.**
  - **Sense.** 〜色 in the 地方色 sense, 「a characteristic tinge or flavour」:
    国際色, 政治色, 宗教色.
  - **Base.** It sits on the drawn base 地方, which is a free noun, so the base
    is productive.
  - **Not a fixed lower-level word.** 地方色 is not a word learned whole below
    N2 (RC-1).
  - **Options.** 味/色/感/調, all real one-character 漢語 suffixes of the
    性質・感じ family (人間味, 安心感, 七五調). None forms a word with 地方
    (地方味/地方感/地方調). 味 is the deliberate near-miss: 「味わい」 sits close
    to 「色」.
  - **Second-answer screen.** 性 was kept out, because 地方性 is attested.
  - **Distinct affixes.** The twelve 問題3 affixes stay distinct (半/仮/副/超,
    味/色/感/調, 型/式/流/順).
  - **The stem.** 「私の生まれた町の祭りは、地方（　）が強い。」, key 2. It shares
    no run of 6 or more characters with the textbook extracts.
