# GENERATE.md — the prompt for generating a new mock test

Copy everything below the line to an agent, filling in the one ⟨⟩ placeholder.

- **Test id**: a folder that does not exist under `tests/`. Date-shaped,
  `YYYYMMDD_N` (e.g. `20260928_1`). A level other than N2 is prefixed:
  `n1-20261005_1` — but only a level whose table says `calibrated` can be
  generated (`make levels`; today that is N2 only).
- **No seed**: the agent draws its own from an RNG, twice (blueprint and 聴解).

---

Generate a complete JLPT mock exam as test `⟨test_id⟩` in this repository.

**Read first, in full, before your first tool call:** `AGENTS.md`, then
`.agents/jlpt-test-generation/SKILL.md`. That skill owns the workflow — the
stage table, the per-stage reading map, the subagent prompt template and the
fix loop. This prompt only fixes the order and the stop conditions; where it
seems to disagree with the skill, the skill wins.

**Before stage 1 — preconditions (stop and report if one fails):**
- `tests/⟨test_id⟩/` does not exist, and the level the id names is calibrated
  (`make levels`).
- No other test's QA is open, and every row of the latest QA report's
  root-cause table is applied or rejected with a reason. `make sample` writes
  the ledger an open review is auditing.
- `make check` is green on the tree you start from.

**Run the stages as subagents, in order, handing off through files only.**
You orchestrate; you author nothing.

| # | Stage | Contexts | Done when |
|---|-------|----------|-----------|
| 1 | Blueprint: `make sample ⟨test_id⟩ SEED=<rng>` | 1 | `test_spec.json` + ledger row written |
| 2 | `make scaffold-sections ⟨test_id⟩`, then author 文字・語彙 (問1–6) ǀ 文法 (問7–9) ǀ 読解 (問10–14) into the three fragments | **3, parallel** | no scaffold placeholder left; 読解 got its pre-assigned closing-move shapes |
| 3 | Build + gate: `make assemble`, `make mp3 ⟨test_id⟩ SEED=<rng>` (composes the whole 聴解 half), `make upload-files TARGET=tests TEST=⟨test_id⟩`, booklet, sheet, `make check`, the whole-paper topic table, the `logs/topics.json` row | 1 | gate green, every WARN naming this test resolved or recorded with its reason |
| 4 | QA: `exam-qa-review`, blind-solve every item — ONE full round | 1 **fresh** | `QA: PASS`, or every finding fixed directly by its section's author; a scoped re-review only for a changed key or a replaced item/passage (skill §"The fix loop") |
| 5 | Model answer: `詳細解説.json` (JA) and `詳細解説.vi.json` (VI), then `make model-answer ⟨test_id⟩` (also rebuilds `練習.html`) | **2, separate** | both panes authored inside the terseness bands, no scaffold placeholder left |

Non-negotiables (each is in the skill; they are repeated because each has shipped broken):
1. **Seeds are RNG output**, `python3 -c "import secrets; print(secrets.randbelow(10**8))"`,
   used verbatim — one for stage 1, a fresh one for `make mp3`.
2. **Authors write only what `test_spec.json` prescribes.** Tested items are
   pool-drawn and binding; 読解 subjects are authored from each entry's
   `theme` and must avoid its `avoid` list. An undrawable item is a
   `--reroll`, never a hand substitute.
3. **There is no 聴解 author** — `make mp3` composes the listening half from
   banked clips at stage 3, and every `聴解.*` file is its output, never edited
   by hand (re-render: `make mp3 ⟨test_id⟩ REPLAY=1`).
4. **Read every line of `make check`**, WARN included. Green is the floor.
5. **QA runs in a context that authored nothing**, and stage 5 only starts
   once QA's findings are all closed (PASS, or fixed per the fix loop) — any
   later item fix desynchronizes the explanations.
6. **The Vietnamese pane is written from the items, not translated** — its
   subagent never sees the Japanese set.
7. `make check` once more after `make model-answer`.

**Finish:** commit `tests/⟨test_id⟩/`, `qa/qa-report-⟨test_id⟩*.md` and the updated
`logs/` (`logs/upload_manifest.json` included) in one commit, then give the final report per `AGENTS.md` §0.7: skills
read (per stage), stages run, both seeds, QA rounds and findings, every WARN
naming this test with its disposition, and anything skipped and why.
