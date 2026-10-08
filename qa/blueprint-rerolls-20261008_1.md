# Blueprint rerolls — 20261008_1

Base draw: `make sample 20261008_1 SEED=24370401`. The orchestrator drew the
seed by RNG and checked that it was unused in `logs/ledger.json` (0 hits before
the draw). It was used verbatim. The authoritative record is the spec's `seed`
string and `rotation`, which the ledger row mirrors.
`check_ledger_spec_agreement` is `ok` for this test.

## Rerolls at stage 1: none

(Stage 2 and QA added four `--reroll-one` runs; see "Stage-2 rerolls" below. The spec's `rotation.reroll_log` is authoritative. QA F5, 2026-10-08.)

No `--reroll` or `--reroll-one` ran. Nothing in the sampler output, in
`exam-blueprint`, or in `make check` required one:

- **Per-paper composition rules, all inside band.**
  - 問題1 訓読み is 2 of 5 (冷める, 潜る), band 2–2.
  - 問題7 敬語 is 1 of 12 (敬語:ございます), cap 2.
  - 問題2 和語 is 3 of 5 (敗れる, 快い, 詳しい) and bare compounds are 2
    (契機, 掲載), by `is_wago_orthography()` / `is_bare_compound()`. Both are
    inside 1–3.
  - Katakana in 問題5/6 is 1 (ガイド).
  - `answer_positions` totals are 25/20/26/19, band 19–27.
  - 聴解問題5's last two keys are 3 and 2, not equal.
- **Rotation.** Every drawn pool item is outside its own category's
  frozen window (`check_spec_rotation` ok, 9/9 windows recorded at draw time).
  No grammar form crosses 問題7↔問題8 inside its cooldown. No Shin Kanzen 目次
  point is drawn twice.
- **Undrawable entries.**
  - The five `orthography` entries are all drawable: none is in
    `needs_evidence` and none contains a 表外漢字.
  - No `kanji_reading` entry fails the shape rule.
  - 潜る(もぐる) is attested as a Hajimete headword: `refs/Hajimete/vocab_reference.md`
    L14471 「もぐる」, example L14505. 寝室 is printed in the official 7-2025
    script (`refs/JLPT_N2_NEW/16. N2 7-2025/script.md` L280).
- **Themes.**
  - The 12 reading themes are all distinct.
  - Theme rule 4 holds for the 読解 headline set: 問題12 環境, 問題13 住まい and
    問題14 医療・福祉 headline neither 20261002_1 nor 20260929_1.
  - The cloze theme was chosen by RNG from the three legal values; see
    `qa/dokkai-allocation-20261008_1.md`.

## Drawn entries that QA must band-audit (not a reroll trigger here)

These had **0 headword hits** in all four textbook extracts and in all 31
`booklet.md` files when grepped at stage 1: 初舞台 (context_words), 被災地
(context_words), 奮闘する (usage), and the 総〜 example 総人口 (word_formation;
the affix 総〜 itself is the tested item).

`exam-blueprint` §"Pool entries stay inside the N2 band" says that OCR absence
is weak evidence. Existing entries are "audited when drawn" under
`exam-qa-review` §2.5, and only `orthography` makes a zero-hit entry
undrawable. So these were NOT rerolled at stage 1.

If the stage-2 author or QA finds one off-band, the repair is
`--reroll-one <cat>:<index>` with a `--reason`, never a hand substitution. Each
one gets a row in this file.

## `make check` dispositions for 20261008_1 (stage 1)

- `make check` exit 0: **0 FAIL**, 234 WARN repo-wide, 255 skip.
- **No WARN line names 20261008_1.** Its lines are `ok`, plus these `skip`s:
  - errand-key comparisons (no drawn entry carries a key);
  - 問題7/8 form-family comparisons (no drawn entry is family-tagged);
  - theme records against `logs/topics.json` (no row yet; Stage 3 writes it);
  - 聴解 errand repeat (checked by hand at Stage 3 on the `shapes` column);
  - per-test contracts ("blueprint only — stage 1 done, stage 2 not
    started").
  - None of these is a pass. Each is a later stage's job.
- **One corpus-wide WARN includes this draw's 問題1 targets:**
  `問題1 reading-trap rate across generated papers (33/110, official 40.0%)`.
  - This paper contributes 1 of 5 (りょくちゃ). The corpus was already under
    band before this draw (32/105 = 30.5 %).
  - `sample_kun_capped()` stratifies the trap slots by Bernoulli at
    `TRAP_TARGET_RATE` = 14/35, and `TRAP_FLOOR` is empty. So there is no
    per-paper rule to reroll against.
  - Rerolling until a draw carries more 促音/拗音 targets would be seed-shopping,
    which the repo forbids.
  - **Disposition: not a defect of this draw, and not repaired here.** The
    repair the WARN names is in the sampler (a per-paper floor), and that is an
    owner decision.

## Nothing skipped

Stage 1 ran in full: sample, check of the draw against the blueprint rules, the
allocation table, and `make check`. No source binary was needed.

## Stage-2 rerolls (orchestrator, 2026-10-08)

The 文字・語彙 author found two entries it could not attest at N2 and left them
unwritten rather than substitute. The orchestrator drew each seed by RNG
(`secrets.randbelow(10**8)`) and used it verbatim. `answer_positions` are unchanged.

| # | reroll | out → in | reason |
|---|---|---|---|
| 1 | `usage:3` seed 82200856 | おおらか → 持参 | Glossed in its only archive occurrence (7/2025 booklet L469 「（注3）おおらかに：広い心で」), which fails the exam-qa-review §2.5 gloss test. 0 hits in the Shin Kanzen N2語彙 index, Hajimete and Soumatome. |
| 2 | `word_formation:0` seed 6943260 | 〜ぶる(偉ぶる) → 〜めく(謎めく) | No N2 attestation: 0 hits in the Shin Kanzen 語彙 index (PDF p.210), the 文法 TOC, the Soumatome 語形成 week, Hajimete and all 31 booklets. Same pattern as 20261002_1's 切実. |

**Pool follow-up: applied.** No shipped paper's ledger row held either entry; this
paper's row stopped holding them after the rerolls. Under exam-blueprint
§"Pool entries stay inside the N2 band" they are therefore **deleted outright**
from `pools.json`: 〜ぶる(偉ぶる) from `word_formation`, and おおらか from both
`context_words` and `usage`. The `band_sources.frozen_unsourced` ratchet was
lowered to match: word_formation 99→98, context_words 1359→1358, usage 212→211.
The new entries' band check belongs to the author re-writing items 11 and 29.
| 3 | `word_formation:0` seed 11565207 | 〜めく(謎めく) → 現〜(現時点) | 〜めく fails the same check as 〜ぶる: as a suffix it has 0 hits in the Shin Kanzen 語彙 index (め-row, PDF p.212), the 文法 TOC, Hajimete, Soumatome and the 31 booklets. No shipped paper drew it, so it is deleted from `word_formation`, and the ratchet goes 98→97. |
| 4 | `grammar_p7:10` seed 48018312 | 〜に即して → 〜とみえる | QA F1 (qa-report-20261008_1): 〜に即して is off-band (N1). It is absent from the Shin Kanzen N2文法 索引 (book pp.208–211; the に row has に沿って, not に即して), and 即し occurs 0 times in the 31 booklets. **Band evidence for 〜とみえる (in band):** it is a Shin Kanzen N2文法 headword, 索引 book p.209 (PDF p.218) 「〜とみえる 100, 136」, headed at 実力養成編 第1部 22課-1, book p.100 (PDF p.110): 「⇒ある根拠があって、〜らしい・〜ようだと思う」, connection 普通形＋とみえる, note 「主にほかの人の様子を見て、それを根拠に推量したことを表す文につく。推量した人は文中に表れない」. It has no official 問題7/9 key: 0 hits for とみえ／と見え in the 31 booklets. Shin Kanzen evidence is enough under bunpou.md §Inventory (1). The key stays at position 4, and item 41 is re-authored. 〜に即して is **retired**, not deleted, because 20260904_2's ledger row holds it: `retired_entries.grammar_p7`, drawn_by 20260904_2. `frozen_unsourced` is unchanged, since a retired entry stays in its list and still counts toward the ratchet. |
