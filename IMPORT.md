# IMPORT.md — the prompt for importing an external test

Copy everything below the line to an agent, filling in the ⟨⟩ placeholders.

- **Slug**: lowercase letters/digits/hyphens, **starting with the level**:
  `n2-2025-12`, `n1-2025-12`. The folder becomes `tests/imported-⟨slug⟩/`, and
  the level is read from the slug.
- The level needs a structure table at `structured` or better (`make levels`);
  an N1 import is possible once `N1.json` is filled (README "Adding a level").
- The script PDF, MP3 and key PDF are optional — delete the lines you don't have.

---

Import an external JLPT exam into this repository as `tests/imported-⟨slug⟩/`.

Source files:
- Booklet PDF: `⟨path/to/booklet.pdf⟩`
- Listening script PDF (optional): `⟨path/to/script.pdf⟩`
- Listening audio MP3 (optional): `⟨path/to/audio.mp3⟩`
- Answer-key PDF (optional): `⟨path/to/key.pdf⟩`

**Read first, in full, before your first tool call:** `AGENTS.md`, then
`.agents/external-test-import/SKILL.md`. That skill owns the workflow; this
prompt only fixes the order and the stop conditions.

**Before step 1:** `tests/imported-⟨slug⟩/` does not exist, and `make levels`
shows the slug's level at `structured` or `calibrated`. If not, stop and report.

**Three steps, in order:**

1. **Source → deliverables.** `make init-import SLUG=⟨slug⟩`, then transcribe the
   booklet, script and audio into the repo's files. Fidelity over invention:
   never improve an item, never swap a key, keep the source's apparatus
   (（注N）, （中略）, setting labels, printed URLs), and copy the original MP3.
   **Never run `make mp3` on an import** — no synthesis path exists; without an
   MP3 the 聴解 half is text only, and the report says so.
2. **Verify by hand, then gate.** Reconcile **every** key against the official
   answer sheet (the sheet wins); the item count is whatever the sitting
   printed, and it must be one of the level table's era shapes. Check coverage
   both ways, and repair only what the source's own print/OCR plainly got wrong,
   and only where the text or the key settles it. For a line that won't resolve,
   stop at the first rung that settles it: re-read the extract in context →
   cross-check the same fact elsewhere in the source → rasterize the page and
   read the ink (decisive lines only, cropped, high dpi). A doubtful line may
   stay as printed only after you have looked at the ink — say which page.
   Then `make booklet`, `make sheet`, `make check` (every line, WARN included).
   No `exam-qa-review` pass.
3. **Model answer, last.** Author `詳細解説.json` (JA), then `詳細解説.vi.json`
   (VI) **in a separate context** — written from the items, never translated,
   both inside `exam-model-answer`'s terseness bands. **Solve each item before
   you explain it**, then compare with the key: an explanation written backwards
   from the key justifies a wrong key just as fluently. If your solve still
   disagrees after climbing the ladder, the source wins — report it, never
   re-key. Then `make model-answer imported-⟨slug⟩` and `make check` again.

Binding: this is an **import, not a generation** — never run `sample_items.py`,
never touch `logs/ledger.json`.

**Finish:** commit `tests/imported-⟨slug⟩/`, then report per `AGENTS.md` §0.7:
skills read, steps run, how the keys reconciled (count and any disagreement),
every repair to the source's own text, every doubtful line left as printed (with
its page), and anything skipped.
