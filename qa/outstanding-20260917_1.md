# Outstanding work for 20260917_1 (checklist, orchestrator-owned)

Written 2026-09-17. Everything here is BLOCKING for the paper, the commit, or
both. A stale note is a defect class in this repo (`20260817_3`, `20260821_1`
NF-5: a note that quotes a removed string, or says a step is 未実施 after it was
done, is worse than no note — the next paper's blueprint reads these fields).

## A. Stale records created by the 問題12 re-angle — MUST be refreshed

問題12 (A+B) was re-angled from the 問い合わせ先 / 字を大きくする surface onto
**「取材した相手に、記事を出す前に原稿を見せるかどうか（会報・広報の書き手）」**
to close F1 and F4. These still describe the SUPERSEDED surface:

1. `qa/dokkai-allocation-20260917_1.md` — the `theme` and
   `final sentence (AUTHOR FILLS)` columns were never filled, and the row now
   needs the shipped values:
   - 問題12(A) final: `相手に確かめてもらうべきは、書き手の見方ではなく、調べれば答えの決まることである。`
   - 問題12(B) final: `どこを断るかがはっきりしていれば、全文を見せても、記事は書いたまま残る。`
2. `logs/topics.json` — this test's 問題12 `surfaces` / `claim` rows still name
   the old 問い合わせ先 subject.
3. `qa/stage3-report-20260917_1.md` §6 — F1/F3/F4 are now CLOSED; the report
   states them as open. Mark the dispositions rather than rewriting the finding.

## B. The merged paper is STALE

`tests/20260917_1/言語知識・読解.md` predates the 問題12 re-angle. The fragment
`_sections/問10-14_読解.md` is the source of truth. Re-merge mechanically
(bodies 問1-6 → 問7-9 → 問10-14, then ONE key heading + the three key tables in
order) and rebuild — `make booklet` + `make sheet`. Artifacts carry the sha of
the bytes they were built from and the gate compares them.

## C. Re-composition of THREE papers (owner ruling, RC-2)

`20260917_1`, `20260828_1`, `20260904_1` all carry the unanswerable 問題1-2番.
The detector is fixed and the bank is rebuilt, so `make mp3` now REFUSES those
clips — but the papers on disk still contain them.
- Re-compose each at a FRESH RNG seed (not `--replay`: the 問題1-2 slot genuinely
  has to move, so the whole half re-draws).
- Each needs: new MP3 + `make upload-files`, rewritten 聴解 `詳細解説` entries in
  both panes, updated `logs/topics.json` 聴解 rows, `make booklet` + `make sheet`.
- `20260828_1` and `20260904_1` additionally have EXISTING `模範解答.html` and
  `詳細解説` panes built against their old listening half — those must be
  regenerated (`make model-answer`) or they describe audio that no longer exists.
- Diff the moved-slot count from `logs/choukai_draws.json` and report it.

## D. TEXTBOOK_SLOTS["問題3"] — set it only AFTER the pool grows

Must go to **≤1**. RC-1's addendum: 2 makes F2 deterministic, because the two
colliding clips are the unique 2-use pair and 2 slots take exactly them.
Then re-run `make choukai-wear` and read every line.

## E. Verification reads that can only happen at the end

1. **Cross-half read**: the new 問題12 subject against the FINAL 聴解 draw. The
   re-angle was deliberately not tuned to any specific clip, so this is the
   check that it landed clear.
2. **Within-paper option-set Jaccard** across all 30 聴解 items of each
   re-composed paper — by hand, since no gate does it (RC-1). F2 must measure
   clear, not be assumed clear.
3. The MOVE column and the TEMPLATE column re-read SEPARATELY after every
   repair — repair collateral is the documented expensive case.

## F. Then, and only then
Stage 4 QA (fresh eyes, authored nothing) → fix loop → `QA: PASS` →
stage 5 model answer (two contexts, one per language, written not translated) →
`make check` → `make upload-files` → commit + push (user asked for the push).
