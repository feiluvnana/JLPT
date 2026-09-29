# Blueprint rerolls — 20260929_1 (why each `--reroll-one` ran)

Base draw: `make sample 20260929_1 SEED=53778138`. The orchestrator drew that seed
by RNG, and it was unused in `logs/ledger.json`. Every reroll below used a fresh
`secrets.randbelow(10**8)` seed, and each was forced by a rule: theme rule 4, or
the measured 敬語 cap the orchestrator decided on. None was run to get a "nicer"
draw. The authoritative record is the spec's `seed` string and
`rotation.reroll_log`, which the ledger row mirrors. This file only explains the
evidence behind each reason. Count rerolls from the seed string; this note holds
no count.

| # | reroll | out → in | reason |
|---|---|---|---|
| 1 | `reading_topics:11` seed 60808941, `--exclude-theme` ×8 | スポーツ・余暇 → 教育 | **Theme rule 4, consecutive papers.** Index 11 is 問題14, a 読解 headline surface. スポーツ・余暇 is the theme of 20260928_2's 聴解問題5-1番 (市のスポーツセンターの親子サッカー教室), which is a headline surface of the immediately previous paper. `check_theme_repeat_cross_test` puts the previous paper's composed 聴解問題5 into its headline set, and FAILs when that set overlaps this paper's 読解 headlines. The WARN-only carve-out covers only THIS paper's composed 聴解問題5, so it does not apply here. The draw would also have been a two-back repeat, because 20260928_1's 聴解問題5-1番 is スポーツ・余暇 too. **Exclusions** (rule-forbidden themes only): 20260928_2's six headline themes 住まい, デジタル化, 行政・手続き, 子育て・家族 (読解 headlines) and スポーツ・余暇, 旅行・観光 (聴解問題5), plus this paper's own 問題12 睡眠・健康 and 問題13 科学・技術 (rule 1). The sampler also excluded the kept themes by itself. The two-back themes (交通, 人間関係, 文化・伝統, 食, 消費・経済) were NOT excluded, because the budget of one was unspent. The draw landed on 教育, which is a headline of neither paper. |

| 2 | `grammar_p7:11` seed 21599915 | 敬語:申し上げる → 〜反面 | **Measured 敬語 cap (orchestrator decision 2026-09-29, section below).** Official 問題7 keys at most 2 敬語 items per sitting, and this draw keyed 7. The excess is rerolled from the later indices first, down to 2. Kept: index 2 敬語:いたす and index 3 敬語:おいでになる. |
| 3 | `grammar_p7:10` seed 77591135 | 敬語:存じる → 敬語:〜させていただく | Same reason. **The redraw landed on 敬語 again**, so index 10 was rerolled again (row 4). |
| 4 | `grammar_p7:10` seed 82599346 | 敬語:〜させていただく → 敬語:ございます | Same reason. **敬語 again**, so rerolled again (row 5). |
| 5 | `grammar_p7:10` seed 87503709 | 敬語:ございます → 〜すら | Same reason. Not 敬語, so it was accepted. |
| 6 | `grammar_p7:9` seed 34625502 | 敬語:ご覧いただく → 〜ずじまいだ | Same reason. Accepted on the first draw. |
| 7 | `grammar_p7:6` seed 2203518 | 敬語:いらっしゃる → 敬語:〜させていただく | Same reason. **敬語 again** (row 8). |
| 8 | `grammar_p7:6` seed 16422696 | 敬語:〜させていただく → 敬語:ございます | Same reason. **敬語 again** (row 9). |
| 9 | `grammar_p7:6` seed 22189440 | 敬語:ございます → 敬語:いらっしゃる | Same reason. **敬語 again. It is the SAME entry this index's first reroll (row 7) had rejected.** `--reroll-one` bars only the entry it is replacing right now, not the ones earlier rerolls of that index rejected (see the root-cause row). Rerolled again (row 10). |
| 10 | `grammar_p7:6` seed 76660069 | 敬語:いらっしゃる → 〜につけて | Same reason. Accepted. |
| 11 | `grammar_p7:5` seed 29696137 | 敬語:なさる → 〜わけだ | Same reason. Accepted on the first draw. |
| 12 | `orthography:1` seed 35245633 | 基盤 → 金魚 | **QA F2 (qa-report-20260929_1), off-level/unattested KEY.** 基盤 has 0 occurrences in all four vocabulary/kanji extracts and in every `refs/**/*.md` (precedent qa-report-20260928_2 F1 懸念). The orchestrator decided to reroll. Before this run, 基盤 was deleted from `pools.json` `orthography`: the ledger shows no shipped paper drew it (the other ledger hits are the unrelated topic string 「本人確認アプリの共通基盤統合…」). |
| 13 | `orthography:1` seed 35461085 | 金魚 → 温室 | **Same F2 criterion, plus golden rule side 1.** 金魚 has 0 hits in the four extracts, and both kanji are elementary grade 1–2 (金 小1, 魚 小2), so a 表記 item on it is N3-or-below. Official prints it only as unglossed 読解 prose (12/2022 booklet L300). Rerolled. The pool entry is left in place; see the section below. |
| 14 | `orthography:1` seed 69736911 | 温室 → 応接 | **Same F2 criterion.** 温室 has no headword or example line in the four extracts. Its 5 Hajimete hits (L8156, L18104, L18142, L18153, L18227) are Chinese gloss text 「温室效应」 under 地球温暖化, and it has 0 hits in the 31 booklets and scripts. **応接 was accepted:** In Hajimete, 「応接（する）」 is a related word under headword #704 『応対』 (index L22111–22113 → 704; body L10123, OCR-garbled). It is not headword #704 itself (corrected per qa-report-20260929_1-round2 R2-F1). Official 7/2016 prints 応接室 unglossed (booklet L135). |

Every `grammar_p7` reroll carries the same `--reason` text in `rotation.reroll_log`,
which cites the measurement below. The seed string and the ledger row were
verified to mirror the spec after the last reroll.

**New 問題7 list (12):**

| index | entry |
|---|---|
| 0 | 〜ところから |
| 1 | 〜さえ |
| 2 | 敬語:いたす |
| 3 | 敬語:おいでになる |
| 4 | 〜てでも |
| 5 | 〜わけだ |
| 6 | 〜につけて |
| 7 | 〜によらず |
| 8 | 使役:〜させてくれる |
| 9 | 〜ずじまいだ |
| 10 | 〜すら |
| 11 | 〜反面 |

That is 敬語 **2 of 12**, the official maximum. 使役:〜させてくれる is a causative
授受 form, not 尊敬／謙譲／丁重語, so it is not counted.

## The 敬語 measurement behind rows 2–11

**Method:**
- Every `refs/JLPT_N2_NEW/*/booklet.md` 問題7 block was parsed with
  `tools/goi_profile.py`'s own `_blobs()` and `split_options()`. The region runs
  from the 問題7 line to the 問題8 line.
- Keys come from `refs/JLPT_N2_NEW/answer_keys.json`.
- Each KEYED option was matched against a broad 尊敬／謙譲／丁重語 +
  くださる／いただく pattern, and every hit was then read by hand. The scripts are
  in the session scratchpad (`bp_20260929_1_keigo*.py`).

**Coverage:**
- **All 31 sittings, 372 items.** 371 parsed. The one unparsed item, 12/2010 #37,
  is keyed 「わけではない」, which is not 敬語.
- **Two regex hits were struck by hand:**
  - 7/2018 #42 「しておきなさいよ」 is a plain imperative.
  - 12/2023 #36 「使おうとしたら」 is not 敬語.
- **Cross-check:** the 10 `tests/imported-*` papers were parsed separately from
  their own `言語知識・読解.md` and key tables. They give identical counts and
  items for all 10 sittings they cover (2021-07 … 2025-12).

**Per-sitting count of 敬語-keyed 問題7 items:**

| count | sittings |
|---|---|
| **2** (4 sittings) | 12/2013 (ご覧いただく, いたしましょうか); 7/2016 (おいでになったら, お聞きしてもよろしいでしょうか); 12/2017 (ございます, してくださいました); 12/2023 (駐車なさらないよう, まいります) |
| **1** (21 sittings) | 7/2010, 12/2010, 7/2011, 12/2011, 7/2012, 12/2012, 12/2014, 12/2016, 7/2017, 7/2018, 12/2019, 12/2020, 7/2021, 12/2021, 7/2022, 12/2022, 7/2023, 7/2024, 12/2024, 7/2025, 12/2025 |
| **0** (6 sittings) | 7/2013, 7/2014, 7/2015, 12/2015, 12/2018, 7/2019 |

**Band: 0–2, max 2, median 1** (mean 0.94). The draw's 7 was 3.5× the official
maximum.

## Root-cause row proposal (NOT applied — owner decision)

| id | defect | class | proposed repair | measured band |
|---|---|---|---|---|
| RC-BP-1 | `grammar_p7` has no per-paper 敬語 cap. The 2026-09-28 audit added eleven 敬語/使役 entries. Every never-used entry weighs `10**9+1` in `weighted_sample_no_replacement()`, against ~10 for a cooled entry, so the new 敬語 entries took 7 of 12 問題7 slots on the first draw after the audit. No gate saw it. A second, smaller hole showed up on the way: `--reroll-one` bars only the entry it is replacing right now, so a later reroll of the same index can hand back an entry an earlier one rejected (row 9). | PIPELINE-GAP | (a) Add `"grammar_p7": 2` to `KEIGO_CAP`-style per-paper caps in `sample_items.py`, using an `is_keigo_grammar()` predicate: the pool's `敬語:` prefix. Enforce it the way `sample_keigo_capped()` does, in the full draw AND in `--reroll`/`--reroll-one` (count kept entries). Size the `cooldown_for()` sub-pool depth by the cap, as the quick_response branch already does. (b) Have `check_spec_blend` (or a new `check_spec_p7_keigo_cap`) FAIL a spec over the cap. (c) Optional: have `--reroll-one` also exclude every entry this paper's `reroll_log` already rejected at that index. | official 問題7 敬語 keys per sitting: 0–2 (max 2, median 1; 31 of 31 sittings) |

- **Headline set after the reroll:** 問題12 睡眠・健康, 問題13 科学・技術, 問題14 教育.
  The 問題9 cloze is 働き方, derived by RNG in `qa/dokkai-allocation-20260929_1.md`.
  聴解問題5 is composed at stage 3.
  - **Rule 1:** the four 読解 headlines are distinct.
  - **Rule 3:** all 13 読解 themes are distinct: 12 drawn plus the cloze.
  - **Rule 4 against 20260928_2:** 0 repeats. Its headlines were 住まい,
    デジタル化, 行政・手続き and 子育て・家族, plus 聴解5 スポーツ・余暇 and 旅行・観光.
  - **Rule 4 against 20260928_1:** 0 repeats. Its headlines were 交通, 人間関係,
    文化・伝統 and 食, plus 聴解5 スポーツ・余暇 and 消費・経済.
  - Stage 3 must still read this paper's composed 聴解問題5 against rule 1. A
    clash there is a WARN, not a 読解 repair.
- **`kanji_reading` validity rules 1–5.** Each hit line below was opened and read.
  - 輪(わ): Shin Kanzen 漢字 #1035 gives 輪 as リン／わ (ゆびわ).
  - 活発(かっぱつ): Hajimete L18444 「活発な」 / L18446 「かっぱつ」.
  - 製品(せいひん): SK and Hajimete carry it, e.g. Hajimete L4243 乳製品. The
    archive has 40 hits.
  - 素直(すなお): SK 語彙 extract L977 「すなお」. The archive has 6 hits, e.g.
    12/2010 booklet L450.
  - 夜明け(よあけ): Hajimete L4220 「夜明け」 / L28234 「よあけ」.
  - The 訓 count is 2: 輪 and 夜明け. That is inside the sampler's `KUN_FLOOR`–`KUN_CAP`.
  - None of the five is undrawable, so there was no reroll.
  - 製品 is on the easy side. It is not in the 2026-09-28 N5/N4 removal class,
    so it is a QA §2.5 judgement, not a reroll.
- **`orthography` 表外 check:** every glyph in 転換, 基盤, 幼い, 破れる and 区分
  is 常用. No reroll.
- **Zero-hit draws, left for QA §2.5 and not rerolled.** These have zero hits in
  the SK, Soumatome and Hajimete extracts AND in the 31 booklets: 基盤
  (orthography), 裏返す (context_words) and 衛生的だ (paraphrase).
  - Absence in an OCR extract is not band evidence (exam-blueprint §"A NEW
    `usage`/… entry"), and none of the three is plainly off-band.
  - The authors should still verify each key against the textbook pages.
- **Grammar rotation:** the sampler's `assert_rotation()` passed. `make check`
  re-reads cross-category rotation and point identity; see the gate result in
  the stage-1 report.

## History of the 敬語 flag

At first I flagged the 7-of-12 敬語 draw and did not reroll it, because no written
rule caps it. The orchestrator then decided to settle it by measurement. The
measurement put official at a maximum of 2, so rows 2–11 were run. RC-BP-1 above
is the proposed permanent fix. Until it is applied, the next blueprint must run
the same count by hand.

## QA-round rerolls of `orthography:1` (rows 12–14)

The stage-1 note above listed 基盤 as a zero-hit draw "left for QA §2.5". QA filed it as F2, and the orchestrator ruled a reroll. I read the redraws against the same criterion F2 used: at least one headword or example line in Shinkanzen, Soumatome or Hajimete, and not plainly N3-or-below. Two redraws failed that test and were rerolled with fresh `secrets.randbelow(10**8)` seeds. The third, 応接, passed. Only 基盤 was deleted from `pools.json`, which the orchestrator authorised after a ledger check: 20260929_1 was the only paper whose `orthography` draw held it. 金魚 and 温室 are **pool-defect candidates** under the same criterion. Neither has been drawn by any other paper, but deleting them is left to the orchestrator/owner. The key position stays 3 (`answer_positions` 問題2_語彙 = [3, 3, 4, 2, 2], unchanged).

**Orchestrator decision on the pool candidates (2026-09-29):** 金魚 is deleted from
`pools.json` `orthography` (grade 1–2 elementary kanji, below the N2 band; no
ledger row drew it as an orthography item, only as topic strings). 温室 is kept:
it is ordinary N2 vocabulary (温室効果) whose only gap is a headword line in the
OCR extracts, and absence from OCR text is weak evidence. It stays listed here as
a candidate for a page check.
