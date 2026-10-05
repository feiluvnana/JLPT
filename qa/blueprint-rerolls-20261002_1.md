# Blueprint rerolls — 20261002_1 (why each `--reroll-one` ran)

Base draw: `make sample 20261002_1 SEED=15443619`. Each reroll below repairs one
QA finding of `qa/qa-report-20261002_1.md` that the report classes as an
automatic off-level key. The orchestrator drew every seed by RNG
(`secrets.randbelow(10**8)`), and each was used verbatim. None was run to get a
"nicer" draw. The authoritative record is the spec's `seed` string and
`rotation.reroll_log`, which the ledger row mirrors. This file only explains the
evidence behind each reason. `answer_positions` did not change; the spec and the
ledger row were checked before and after.

| # | reroll | out → in | reason | band check of the new entry |
|---|---|---|---|---|
| 1 | `kanji_reading:0` seed 12948275 | 中級(ちゅうきゅう) → 実績(じっせき) | **QA F5, TOO_EASY key.** 初級/中級/上級 are a beginner's own class names. The word has 0 hits in Shin Kanzen N2 漢字, Soumatome and Hajimete N2 2500. The 1/2 discrimination is trivial. Key position 4 is kept. | Hajimete N2 2500 headword **#1122 実績 じっせき 名** (`refs/Hajimete/vocab_reference.md` L15627–15630, opened and read). Official 12/2022 prints 「販売実績」 unglossed (booklet L333). The reading is ordinary 常用 on, and the 訓 count is unchanged (on → on). Never drawn before. |
| 2 | `usage:3` seed 18202796 | 切実 → 身につく | **QA F6, no N2 attestation.** 0 headword hits in all three vocabulary extracts and all 31 booklets; common N1 lists carry it. Key position 3 is kept. | Soumatome 語彙 **L2920 「身につく」**, in its 〜つく list (`refs/Soumatome/goi_reference.md`, opened and read). Shin Kanzen 語彙 L4751 「…意識のうちに身につく」. It is printed in 10+ official booklets (e.g. 7-2011, 12-2011, 7-2019, 12-2025). Never drawn before. |
| 3 | `context_words:6` seed 20420047 | ただ → しつこい | **QA F7, TOO_EASY option set.** Connective ただ forces four N4–N3 connectives (それとも/ただ/つまり/すると). No N2 volume headlines connective ただ. Key position 2 is kept. | Shin Kanzen 語彙 第2部「性質別に言葉を学ぼう」 L1009, as an option of the drill 「ソースの味がくどい」 (an exercise option, not a headword). Official prints it as a 文字・語彙 option in 12-2023 (booklet L24 「おさない／するどい／かしこい／しつこい」) and 12-2018 (L75). Five sittings in all. Never drawn before. |

No reroll landed on an entry the band rules forbid, so no extra seed was drawn.

## Pool follow-up — NOT applied (blocked)

The repair also needs 中級(ちゅうきゅう) (`kanji_reading`), 切実 (`usage`) and ただ
(`context_words`) taken out of `pools.json`. That edit was not made in this pass.

- **The skill and the instruction disagree.** The fix instruction said to *retire*
  these three. But `exam-blueprint` §"Pool entries stay inside the N2 band" says an
  entry that no shipped paper drew is *deleted outright*. The ledger shows that
  only 20261002_1 ever drew them, and after these rerolls its row no longer holds
  them. So a `retired_entries` record with `drawn_by: ["20261002_1"]` would FAIL
  `check_pool_retired_entries()` ("drawn_by names 20261002_1, whose ledger row
  does not hold it").
- **Deletion was blocked.** The deletion was attempted and the session's
  permission layer refused it, so `pools.json` is unchanged. Until the owner
  deletes (or retires) these three, they stay drawable for the next paper.
- **A fourth entry, same headword.** `context_words` also holds 切実 (never drawn).
  F6's evidence applies to it just as much (the 懸念 precedent deleted both).
- **Same class, not in F5.** `kanji_reading` 上級(じょうきゅう) sits beside 中級 and
  has the same TOO_EASY profile.
