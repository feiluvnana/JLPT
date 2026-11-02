# Blueprint rerolls — 20261102_1

Base draw: `make sample 20261102_1 SEED=72353322`. The seed came from the
orchestrator's RNG and was used verbatim. It had 0 hits in `logs/ledger.json`
before the draw. The authoritative record is the spec's `seed` string and
`rotation.reroll_log`, and the ledger row mirrors both. This note does not keep
a reroll count: count from the `seed` string.

## Stage-1 rerolls: two `--reroll-one`, each with a fresh RNG seed

Each seed came from `python3 -c "import secrets; print(secrets.randbelow(10**8))"`.
Nothing was hand-substituted. The index chose which entry left; the sampler
chose which entry arrived.

### 1. `reading_topics:11` (問題14): 消費・経済 → 子育て・家族, seed 42529410

- **Rule.** `exam-blueprint` §"The four theme rules", rule 4. No theme may
  headline two consecutive papers. Index 11 is always 問題14, which is a 読解
  headline.
- **Collision.** 消費・経済 is the theme of 20261008_1's 聴解問題5-2番, which is
  a headline surface one paper back. `check_theme_repeat_cross_test()` FAILs
  this when it sits on a 読解 headline of the current paper. Only a theme
  carried by this paper's own composed 聴解問題5 drops to a WARN. 消費・経済
  also headlined 20261002_1's 問題12, two papers back, so it would also have
  spent the two-back budget of one.
- **Why at stage 1.** No gate can see this before Stage 3 writes the
  `logs/topics.json` row. By then the 問題14 flyer would already be written.
  The sampler has no cross-test headline constraint (`exam-blueprint`
  §"WHAT THIS STILL DOES NOT FIX").
- **Exclusions.** `--exclude-theme` was given every headline theme of the
  previous two papers that this paper is not already keeping: 消費・経済, 環境,
  住まい, 旅行・観光 and メディア・情報. Kept themes are excluded by the sampler.
- **Result.** 子育て・家族. It headlines neither 20261008_1 nor 20261002_1.

### 2. `grammar_p7:9`: 〜抜きで(は) → 〜がたい, seed 10002230

- **Rule.** `exam-blueprint` §"One grammar point, one pool entry", which says
  "not kanji *and* kana". `grammar_p7[9]` 〜抜きで(は) and `grammar_p7[5]`
  〜ぬきにして are one point, 〜(を)ぬきにして／〜抜きで, written once in kanji
  and once in kana. Both were drawn into the same 問題7, so the paper would key
  one point twice.
- **Why the sampler let it through.** `taken_tokens()` compares strings, and
  ぬき ≠ 抜き. Neither entry is in `grammar_point_identity` or
  `grammar_form_families`, so `check_grammar_point_identity` and
  `check_p8_form_family` cannot see the pair.
- **Result.** 〜がたい. The sampler's identity line printed
  `form»がたい: last drawn 14 draw(s) back (20260903_1)`, which is outside the
  10-draw `grammar_p7` window.
- **Pool defect, open.** This file does NOT fix it. Stage 1 may not edit
  `pools.json`.
  - **Proposed repair.** Add both entries to `grammar_point_identity` under
    their Shin Kanzen N2 文法 目次 number, read from the page image. Otherwise,
    retire one spelling, following the 2026-09-28 precedent (〜にせよ〜にせよ
    etc.).
  - **Same class still in the pool.** `〜に決まっている` / `〜にきまっている`,
    the known duplicate noted in exam-blueprint, is already folded under 22課6.

## Checked and found compliant, so no reroll

- **問題1 訓読み: 2 of 5** (物音, 蒸し暑い). The band is 2–2. After reroll 3: 物音, 末っ子, still 2 of 5.
- **問題7 敬語: 2 of 12** (敬語:存じる, 敬語:ご覧いただく). This is at the cap
  of 2.
- **問題2:**
  - 和語 count, by `is_wago_orthography()`: 3 (量る, 預ける, 収める). That is
    inside 1–3.
  - Bare compounds, by `is_bare_compound()`: 2 (解放, 過失). That is inside 1–3.
- **Answer positions:** 19/23/21/27. The band is 19–27. 聴解問題5's last two
  keys are 2 and 4, so they are not equal.
- **Rotation, `make check`:** every category is outside its frozen window. No
  問題7↔問題8 form crosses inside its cooldown. No Shin Kanzen 目次 point that
  the map knows of is drawn twice.
- **問題8 form-family coverage WARN (1/5 tagged).** This is the known
  pool-map class (`check_pool_grammar_form_families`), not a draw defect. By
  hand: the five 問題8 forms (つつ, たびに, 状況において, をきっかけに,
  ほど〜はない) share no point with each other or with any 問題7 form.

## QA-repair reroll: one `--reroll-one`, seed given by the orchestrator

### 3. `kanji_reading:4` (問題1-5): 蒸し暑い(むしあつい) → 末っ子(すえっこ), seed 85970684

- **Finding.** qa-report-20261102_1 F1 (自動不合格), root cause RC-1. The
  printed span 蒸し暑い carries a medial 「し」. With the kanji covered, □し□い
  fits only むしあつい, so the okurigana selects the key on sight. No compliant
  訓 set exists for the target: neither 蒸's readings nor the 体感 field
  supplies three real □し□い words. The target is undrawable.
- **Command.** `sample_items.py --test-id 20261102_1 --reroll-one
  kanji_reading:4 --seed 85970684 --reason "moji-goi Part 1 (okurigana
  exposure, qa-report-20261102_1 F1): …"`. The seed came from the
  orchestrator's RNG and was used verbatim. It was the first seed tried.
- **Result.** 末っ子(すえっこ). The identity line printed `never drawn` in the
  175-draw `kanji_reading` window.
  - `is_kun_target` = True, so 問題1 stays at 2 of 5 訓 (物音, 末っ子).
  - `has_reading_trap` = True (促音).
  - `answer_positions` 問題1[4] = 4 is unchanged.
- **Drawable check.** Branch (b), field=人の呼び名（〜っ子）:
  ひとりっこ/あまえっこ/うれっこ/すえっこ.
  - All four fit the kanji-wildcard skeleton □っ□, so the RC-1 predicate
    passes.
  - All four are real words, so the 訓 set is non-word-free.
  - The second reading まっし belongs to the spelling 末子 and is kept out of
    the options.
