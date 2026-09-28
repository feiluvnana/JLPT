---
name: jlpt-test-generation
description: End-to-end workflow for generating a complete JLPT mock exam (N1-N5, primarily N2). Use this skill whenever the user asks to create, generate, or build a JLPT test, mock exam, 模擬試験, practice test, or any subset of one (言語知識, 文字・語彙, 文法, 読解, 聴解/choukai), or asks to regenerate/fix exam deliverables. This is the entry-point skill for generation — it owns the 5-stage pass structure and the per-stage reading map, and routes to the specialized skills. Consult it FIRST before any generated exam work, even for partial requests like "make a listening section" or "create N2 grammar questions". For importing an external PDF/past paper, use external-test-import instead.
---

# JLPT Test Generation (Orchestrator)

**Importing an existing exam** (PDF, past paper, script, MP3) → stop and read
`external-test-import/SKILL.md`; those live in `tests/imported-<slug>/`. This
file is for **generating** new mocks only.

**Read this file to the end before your first tool call.** `AGENTS.md` §0 is
the compliance rule and says what to report at the end; §2–3 own layout,
deliverable filenames, and `refs/` paths.

## The 5-stage pipeline

**Orchestrate, don't work.** The context owning the request spawns subagents and
does no content work itself. State flows between stages **through files on disk
only** — an orchestrator paraphrasing content into a prompt is the "memory of
what I meant" that shipped every historical mis-key.

Two context-isolation rules, non-negotiable in any harness: **(a) no long
single-run authoring** — defects cluster in whatever one context writes last;
**(b) QA is a context that authored nothing** — an author cannot audit its own
intent.

| Stage | Job | Contexts |
|-------|-----|----------|
| 1. Blueprint | Sample the item pools; draw a THEME per themed surface | 1 |
| 2. Author | 文字・語彙 (問1–6) ǀ 文法 (問7–9) ǀ 読解 (問10–14) | **3, in parallel** |
| 3. Build + gate | `make assemble`, **compose 聴解** (`make mp3 <id> SEED=<rng>`), upload the MP3, booklet, sheet, `make check`, whole-paper topic table | 1 |
| 4. QA | `exam-qa-review` in full — blind-solve every item, root-cause table | 1 **fresh** |
| 5. Model answer | `詳細解説.json` (JA) + `詳細解説.vi.json` (VI) → `make model-answer` (also rebuilds `練習.html`) | **2, one per language**, no shared context |

**The fix loop — one full QA round, then direct fixes** (owner rule since
2026-09-28; every other file points here). Stage 4 runs ONCE over the whole
paper. Its findings go back to the author context that owns the section, which
fixes them directly: root-cause the finding, run `make check`, read the diff,
and after any 問題10–14 edit do the keyed-form re-grep plus the 13-final column
re-read (Stage 3). The QA report's disposition column records each fix. **A
second review runs only when a fix changes a key, or replaces an item or
passage wholesale** (a `--reroll`, a re-themed surface, a re-written passage).
Even then it is **SCOPED**: one fresh context blind-solves only the replaced
items and re-reads their 問題 and the column they sit in. It is never a full
re-pass, and it runs **at most once**. Its findings are fixed directly and named
in the final report. Wording and evidence fixes, a stem trim, a re-closed
sentence and a bank/transcript fix get no re-review. PASS closes the *paper*,
not the *generator*: an open row in QA's root-cause table blocks the next run
until it is applied or rejected with a reason.

**`make sample <next>` may not run while any test's QA is open** — not while a
round is being written, not while findings are being applied. It writes
`logs/ledger.json`, the file the open review is auditing, and doing so reds
`make check` for every finished paper on disk. (`20260818_1` was sampled at
11:31 during round 3 of `20260817_3` and did exactly that — R3-6.)

**No subagents available:** approximate with new sessions, one stage each,
handing off through disk. The split that survives every fallback is
**authoring vs QA**.

**One writer per test folder, at a time.** Nothing in the pipeline stops a
second context from editing `tests/<id>/*.md` while a QA pass or a build is in
flight, and the only symptom is a staleness FAIL that reads like an author's
mistake. So: a QA pass **records the source shas it read** in its report header,
and a build or repair that finds them moved **re-runs the pass** rather than
rebuilding on top of it. (`20260907_1`'s `言語知識・読解.md` took three values
inside one round-2 review; the gate FAILed on HTML predating its Markdown for
three minutes and the finding had to be struck as self-cleared —
qa-report-20260907_1-round2, the struck R2-F8.)

## Per-stage reading map

Each subagent reads exactly these, from disk, at the start of its stage — never
the orchestrator's summary — and nothing else:

| Stage | Reads | Writes |
|-------|-------|--------|
| 1 Blueprint | `exam-blueprint/SKILL.md` | `tests/<id>/test_spec.json`, `logs/ledger.json` |
| 2 文字・語彙 | `test_spec.json` + `question-authoring/SKILL.md` + `references/moji-goi.md` + `jlpt-exam-structure/SKILL.md` | 問1–6 fragment |
| 2 文法 | same, with `references/bunpou.md` | 問7–9 fragment |
| 2 読解 | same, with `references/dokkai.md` | 問10–14 fragment |
| 3 Build+gate | `exam-app/SKILL.md`, `choukai-audio/SKILL.md` (**Part 0**), this file's topic-table § | merged `言語知識・読解.md`, the whole 聴解 half, HTML/MP3, `logs/topics.json` row, gate report |
| 4 QA | `exam-qa-review/SKILL.md` | `qa/qa-report-<id>.md` |
| 5 Model answer | `exam-model-answer/SKILL.md` | `詳細解説.json`, `詳細解説.vi.json`, `模範解答.html` |

Stage-2 authors each fill one of the three fragments `make scaffold-sections`
writes to `tests/<id>/_sections/` (`問1-6_文字語彙.md`, `問7-9_文法.md`,
`問10-14_読解.md`): booklet body under canonical `## 問題N` headers, then key/解説
rows under a literal `<!-- KEY -->` marker, key cells pre-filled from
`answer_positions`. Stage 3's `make assemble` merges them — part banners, the
level table's instruction lines, ONE key heading — and refuses a fragment that
still holds a scaffold placeholder. **Authors never type an instruction line or
a key heading.** Parallel authors never share a file. **There is no 聴解
author**: stage 3 composes the listening half from banked clips, so a composed
paper carries no セクション構成表.

### Subagent prompt template

> Read, in full, from disk: [stage's reading-map row]. Your inputs are [files];
> your only outputs are [files]. Author ONLY what `tests/<id>/test_spec.json`
> prescribes — items, topics and `answer_positions` are the contract; do not
> substitute, and treat every `origin` field as binding. Report at the end: what
> you read, what you ran, what you wrote, and anything you skipped and why.
>
> (読解 only) Your assigned closing-move shape per surface is: [surface → shape].

## Stage 1 — blueprint

```bash
make sample <id> SEED=<n>          # -> test_spec.json + ledger
```

- **The seed is an RNG output, never a number you write down.** Run
  `python3 -c "import secrets; print(secrets.randbelow(10**8))"` and use it
  verbatim — agent-"picked" seeds are date-shaped and collide across sessions.
  Must be unused (`logs/ledger.json`).
- A non-N2 id carries its level prefix (`n1-20261005_1`); `make sample` and
  `make mp3` refuse a level whose table is not `calibrated` (`make levels`).
- No harvest step. Each themed surface gets `{theme, origin:"authored",
  avoid:[…]}`; the author invents the subject (`exam-blueprint` Part II).
- Do not run while another test's QA is open (above).

## Stage 2 — authoring

Construction rules: `question-authoring` core + the one reference file from the
reading map.

```bash
make scaffold-sections <id>        # -> the three _sections/ fragments
```

- Author ONLY items in `test_spec.json`; the scaffolded key cells are the
  contract — write each item so its correct option sits where the key says.
- **文字・語彙 stems are quota-bound too** — 問題1/2/5 median 17 JP chars, ≥9 of
  15 comma-free, ≥7 of 25 問題1–5 stems in です・ます with ≥1 first-person and ≤2
  institution-actor, 問題4 median ≤30 and none past 44 (`moji-goi.md` Part 0).
  Fourteen papers missed all of these before they were written down.
- 問題1/2 2×2 matrices: build BY HAND against `moji-goi.md`, then check with
  `python3 tools/matrix_helper.py validate --reading <かな> <4 options>`. **The
  two generators are hard-disabled** (F4, qa-report-20260819_1).
- **Tested items are ALWAYS pool-sampled. Topics are not.** A `reading_topics`
  entry is `{theme, origin:"authored", avoid:[…]}`; the 読解 author invents a
  subject not in `avoid` and not a re-wording of one (`exam-blueprint` Part II).
  `listening_scenarios`/`quick_response` are inert draws — nothing authors from
  them. The grammar, vocabulary and kanji pools remain absolutely binding.
- **`avoid` is only as good as the record**, so Stage 3's `logs/topics.json` row
  is load-bearing for the NEXT paper's draw.
- **Pre-assign each of the 13 読解/cloze surfaces a closing-move shape** from
  `dokkai.md`'s list before spawning, without exceeding its per-shape cap —
  authors left to choose converge on the same "safe" default (documented 3×).
  Pass the 読解 and 文法 subagents their assigned shapes.

## Stage 3 — build + gate

```bash
SEED=$(python3 -c "import secrets; print(secrets.randbelow(10**8))")
make assemble <id> && make autofix <id> && make lint-draft <id> \
  && make verify-scramble <id> && make mp3 <id> SEED=$SEED \
  && make upload-files TARGET=tests TEST=<id> \
  && make booklet <id> && make sheet <id> && make check
```

- **`make assemble`** writes `言語知識・読解.md` from the three fragments.
  `python3 tools/assemble_paper.py tests/<id> --check` reports layout drift;
  `--normalize` re-stamps an already-merged paper.
- **`make mp3` writes the entire 聴解 half** — script, booklet, audio, chapters
  and the 聴解 `詳細解説` entries of both panes — by drawing banked clips
  (`choukai-audio` Part 0). It precedes `make booklet`, which renders the
  `聴解.md` it produces. A draw that must change before QA is a fresh `SEED`;
  after that, only `make mp3 <id> REPLAY=1 [NO_AUDIO=1]`.
- **`make upload-files`** puts the new MP3 on the `audio` release: `make check`
  FAILs any `聴解.mp3` whose bytes are not in `logs/upload_manifest.json`
  (AGENTS.md §3). Re-run it after any rebuild that changes the audio.
- `autofix`/`lint-draft` catch contractions, absolute quantifiers and missing
  blanks at zero token cost before QA.
- `make check` validates every test on disk. **Read every line, including
  WARN.** Fix failures before stage 4: a mis-keyed item is invisible once the
  MP3 is built.
- **A WARN naming this test is resolved, or recorded as deferred-to-QA WITH THE
  REASON, in writing, in `qa/` or the stage-3 report** — a WARN carried silently
  is indistinguishable from one nobody read. (Round 2 of `20260904_1` was handed
  an exit-0 gate as its entry condition while a live
  `check_goi_option_set_valence` WARN named 問題5-24 of that paper; the
  disposition existed only in the orchestrator's prompt, which no reviewer
  reads, and it turned out to be a true positive.)
- **A repair made to clear one gate check is not verified by that check
  passing.** After ANY edit to 問題10–14 prose — （注N） glosses included —
  re-grep every 問題7/8/9 keyed form across the whole 読解 half, record the counts
  AND the frames (文末／連用／連体) in the hand-off, and re-read the edited
  passage's closing move. (`20260903_1` F2: a gloss rewritten to clear a
  byte-identical-gloss FAIL planted 問題8-44's own drawn target in its own frame,
  in printed booklet text, and `make check` went green.)
- Then the **whole-paper topic pass** (below) — no script does it — and
  **append this test's row to `logs/topics.json`** (`surfaces`, `shapes`,
  `claim`, `persona`; format in `exam-blueprint` §"What still governs a
  self-authored surface").

## One topic, one surface (whole-paper pass, stage 3)

The failure mode that survives every automated gate: the same content on two
surfaces of one paper, or recycled from recent papers. Build ONE table — 問題9
cloze, each 問題10–13 passage, the 問題14 flyer, every 聴解 item — with a column
per test (this one and the two before), plus `theme`, `closing move` (読解), and
the DRAWN topic string. Then read it:

- **Fill the theme column from the SHIPPED surface**, not the spec draw — a
  drafted passage wanders off its tag. Apply `exam-blueprint` §"The four theme
  rules" and put the counts in your report.
- **The closing-move column is a 読解 rule** (`dokkai.md` §"Thirteen surfaces").
  Two passages on unrelated subjects both ending 「〜だけでは足りない、〜こそが要る」
  are one essay written twice; official ships that move 5–9 times per 読解 half.
- **Read each surface against its OWN draw before reading it against the
  others.** Nothing compares a shipped surface's SUBJECT to the
  `test_spec.json` string it came from, so a passage can wander off its draw with
  every line green and silently spend a cooldown. (`20260904_3` drew
  「高齢者向け軽スポーツの**普及**」 and shipped a passage arguing **定着**, which
  is `20260904_2` 問題9's subject one paper earlier — the mechanism behind
  qa-report-20260904_3 F1.) **This is a READ, not a gate, and that is measured:**
  the obvious predicate — counting drawn-topic tokens surviving into
  `logs/topics.json` — was run over all 23 papers on 2026-09-05, reports 1–6
  zero-overlap draws on *every* paper (median 3–4, because a surface legitimately
  writes 「自動で走るバス」 for 「自動運転バス」), and does not fire on the founding
  case. A predicate that flags every paper and misses its own founding case is
  refuted. So: put the drawn string in the table and say, per surface, whether
  the shipped subject is the one drawn. A surface that moved is either re-angled
  back onto its draw (no stamp) or stamped `"origin": "reauthored"` in spec AND
  ledger with a note (`exam-qa-review` §"A fix that changes WHAT a surface tests").
- **A 読解 topic and a 聴解 scenario may name one subject and no check sees it.**
  `check_surface_subjects()` matches maximal kanji runs for equality, so
  「健康保険組合からの人間ドック補助案内」 and 「人事部からの健康診断のお知らせ」 — one
  paper, one subject, both 睡眠・健康 — share nothing it can see
  (qa-report-20260904_3 F5). Read the 読解 rows and 聴解 rows as ONE list.
- **No topic appears twice in this paper**, even in a different register (a
  問題14 flyer spelling out a 聴解 item's keyed answer; one subject serving both
  問題9 and 問題10(1)).
- **No 読解 topic repeats the previous test.** Do it as a table read from
  `logs/topics.json` (a lookup, not a re-derivation) and read each ROW across
  the columns; a shared domain in one row is a finding even when theme tags
  differ.
- **A topic/domain match in the 2-tests-back column is a minor finding** — note
  it so a domain doesn't become a crutch one skip apart.
- **聴解 rows are a DRAW audit, not a topic audit** — nobody here chose a 聴解
  subject, so nothing in them can be re-angled. Read `logs/choukai_draws.json`
  and confirm **no clip id repeats the previous paper — in the same slot, and
  for a slot-free (textbook) clip in ANY slot** (`compose_choukai.py::freshest()`
  enforces both, so this is a verification; if a slot's candidates are
  exhausted the composer drops the bar and PRINTS which slot — say so). Then
  read the `shapes` column across three papers for **errand identity** — two
  different clips running one errand, which no id check sees; a confirmed pair
  goes into `MUTUALLY_EXCLUSIVE_CLIPS` (`choukai-audio` Part 0 rule 4). **A 聴解
  repeat is a composer re-draw (fresh `SEED`, before QA) — never a hand
  re-slot or an edit to `聴解.md`.**
- **A 読解 passage may share a domain with a 聴解 item**, because no one picked
  the 聴解 item's domain. Only a shared *decisive detail* — a number or
  condition the reader could carry from one surface to the other — is a
  finding.
- **Give the table a rhetorical-MOVE column, and read it across both halves.**
  A move shared between a 読解 surface and a 聴解 talk is invisible to every
  rule in the repo: the 読解 closing-move cap is 読解-internal, the 聴解 errand
  rule is 聴解-internal, and the subject clause above compares SUBJECTS, which
  differ. `20260907_1` ran *the tool kept its promise; the real change was
  elsewhere* twice — 問題10(1) (digitising the album delivered instant access and
  deleted the viewing ritual) and 聴解問題3-1番 (the transcription tool did save
  typing, but the real change was the meetings) — both tagged デジタル化, and
  round 1 could see the echo without being able to file it
  (qa-report-20260907_1-round2 NEW-1). **Cap: at most two surfaces on one move
  across the two halves.** Not string-decidable, so no check backs this row.
  **The 読解 side is always the one re-angled** — the 聴解 item is a banked
  recording and nobody here chose its move.

  **Read the MOVE column down the SKELETON before the label**, exactly as §5
  requires of the closing column. The recurring skeleton is
  **〈通説または自分の想定した原因 X が述べられる → ところが／しかし／外れた／
  ではなかった → 実は Y〉**; every surface that runs it counts as ONE move however
  differently the two ends are worded (前提の更新・部分最適の反転・予想外の受益者・
  常識の反転 are all this skeleton). **A label spread does not license a skeleton
  pile-up** — a fine label granularity makes any monoculture read as "one over
  the cap", which is how it went unfiled **four** papers running (`20260904_3` 8,
  `20260907_1` 7, `20260910_1` 7, `20260911_1` **10 of 10** essay surfaces).
  **問題12(A)+(B) count as ONE surface for this cap** — the A/B pair
  shares its move by format, and counting them as two consumes the whole quota
  on one 大問. `check_dokkai_belief_denial_monotony()` measures the marker-bearing
  half of this and WARNs above 3; the unmarked reframes it cannot see are why
  the column is still read by hand (qa-report-20260910_1 F2-a/F2-b), and
  `20260911_1` is what that gap costs — the gate printed **1** over a paper
  running the skeleton in every essay surface it had.

  **The official band, and which number is whose.** Hand-measured against the
  full three-beat rubric (attributed assumption + explicit denial + 実は Y),
  essay surfaces only, 問題12 A+B as one: **3 of 9 on N2 7/2025, 4 of 9 on N2
  12/2025, 4 of 9 on N2 12/2024** — conservative; with BORDERLINE surfaces
  counted, 6, 6 and 8 of 9. `qa-report-20260911_1` §"F3 の根拠 — 公式を同一
  ルーブリックで実測" owns those three numbers and names those three sittings;
  cite it, do not restate them bare. This is NOT the `0–3 of 13` the gate
  prints: that is `check_dokkai_belief_denial_monotony()`'s marker-bearing count
  over all 13 surfaces (n=10 imports), a different instrument on a different
  denominator. The generated 8/7/7/10 above are hand reads and belong beside the
  9-surface band, not beside the gate's.

  **Read the MOVE column and the TEMPLATE column SEPARATELY, twice — once down
  each — and re-read BOTH after every repair.** They are different axes: a
  surface can sit on one without sitting on the other, so one pass down a merged
  table misses whichever axis the reader was not holding in mind. The expensive
  case is **repair collateral** — a surface re-angled off one skeleton lands on
  the other, the pair changes clothes and survives, and the second read is the
  only thing that catches it. `qa-report-20260904_1` round 2 is the precedent;
  `20260911_1` is the live case: five of its surfaces — 問題11(1), 問題11(2),
  問題11(4), 問題12(A), 問題12(B) — shared 〈介入 → 数字が動いた〉 *as well as*
  〈想定→実は〉, so the eight re-angles the MOVE cap demands push surfaces INTO a
  template already at its own cap unless both columns are re-read afterwards.
  The table both columns come from is
  `question-authoring/references/dokkai.md` §"The rhetorical-MOVE allocation
  table" — filled in before any prose exists, and re-read as a column after each
  repair, never as a judgement.
- **問題12 (A/B) gets its own cross-test column** — one topic per paper.
- **A duplicated topic in the spec is a sampler defect**: `check_spec_blend`
  fails a repeated draw. `--reroll` the category; never hand-invent a substitute.

## Stage 4 — QA

Read `exam-qa-review/SKILL.md` in full and run it with fresh eyes. A test that
hasn't survived this pass is not done, whatever the gate says.

### Closing a finding includes re-grepping its notes

A repair is finished when **every note that narrates the finding says what is now
on disk.** After applying a fix, grep for the finding id and for the strings the
fix removed, in all four places a repair gets narrated:

1. the 解説 cells in `言語知識・読解.md` — a fix that changes a passage line must
   re-derive **every** cell citing that item, not only the one the finding named
   (`20260821_1` NF-3). `聴解.md` is composer output: a 聴解 fix is a bank fix
   plus `make mp3 <id> REPLAY=1` (`exam-qa-review` §4);
2. `logs/topics.json`'s `notes` for that test;
3. `test_spec.json` and `logs/ledger.json`, if the fix changed what a recorded
   draw shipped as;
4. the QA report's disposition column.

**A note that says a step is 未実施 after you implemented it is the same class of
defect as a note quoting a removed string**, and both are worse than no note: the
next paper's blueprint reads these fields and will chase a fixed bug or trust an
invalidated claim (`20260817_3`, `20260821_1` NF-5).

**Do not pin a repo-wide number in a note.** A warning total is true for one
minute; state the per-test invariant instead ("the only WARN naming this test is
X"), and if you quote a total, date it and say what would move it.

## Stage 5 — model answer (FINAL)

```bash
make scaffold-explanations <id>            # -> 詳細解説.json
make scaffold-explanations <id> LANG=vi    # -> empty 詳細解説.vi.json
make model-answer <id>                     # -> 模範解答.html + 練習.html
make check
```

- **Only AFTER stage 4 returns `QA: PASS`** and all item/option/audio fixes are
  frozen. Generating it earlier is prohibited — any later fix desynchronizes it.
- **Author the 言語知識・読解 entries only.** `make mp3` writes the 聴解 entries
  of both panes from the bank and replaces them on every compose or replay; a
  wrong 聴解 explanation is a `logs/choukai_bank.json` fix.
- **The scaffold PRE-FILLS every `options_analysis` line, and a pre-filled line
  is not an authored one.** A fresh scaffold is 100 % placeholders (393/393 on
  `20260904_2`), and they are well-formed, correctly tagged and inside every
  band — so **both 2021 imports shipped 100 % placeholder Japanese panes green**
  and only a human read caught it. `check_kaisetsu_no_scaffold_placeholders`
  FAILs them now. Replace every line with a reason drawn from THAT item; never
  delete a line, which breaks per-option parity.
- Then scaffold and author `詳細解説.vi.json` **in a second subagent that has not
  seen the Japanese set** — a translation is a defect. Both panes print the exam's
  own wording (stored once, in `詳細解説.json`); only the explanation switches.
- **Every field is capped** by `exam-model-answer`'s terseness bands; the gate
  FAILs an over-cap field. Cut padding, never a concrete reason.
- Concise, learner-friendly prose; zero pipeline metadata (`[kanji-n2.json]`,
  `[N1]`); all four options get individual concrete explanations; furigana
  (`《...》`) on target kanji/stems/key vocabulary.

## Taking the exam

`make serve` (no id — one server lists every test), answer, press 「採点する」:
the page writes `採点結果.json` + `ユーザー解答.json`. CLI: `make grade <id>`.

## Invariants (every run)

- Japanese file names for all deliverables (`AGENTS.md` §2).
- `言語知識・読解.md` is the single editable source, and **every edit carries
  its rebuild in the same change**: `make booklet <id> && make sheet <id>`.
  Every `聴解.*` file is composer output — never hand-edit it; re-render with
  `make mp3 <id> REPLAY=1 [NO_AUDIO=1]` (a seeded re-run re-draws the paper —
  `choukai-audio` Part 0). Artifacts carry the sha of the bytes they were built
  from and the gate compares them. Never hand-edit a sha.
- After any compose or replay, run `python3 tools/choukai_segment.py
  tests/<id>/聴解.mp3` (must recover 5/6/5/11/2) and diff
  `logs/choukai_draws.json` against the previous row.
- **言語知識・読解 items are always original.** Never copy questions from the
  copyrighted textbooks in `refs/` into 問題1–14 — calibration only. The sampled
  topic gives WHAT to write about; compose the words yourself, no web fetch.
- **聴解 is the deliberate exception, since 2026-09-08.** The listening half is
  cut verbatim from banked official and textbook recordings by `make mp3`
  (`choukai-audio` Part 0) — that is the point of the rework, not a violation of the line above.
  It also means a composed paper is **personal study material**: its listening
  items are real exam content, so a composed 聴解 must not be presented as
  original work, and `make pages` publishes it.
- **Finish:** commit `tests/<id>/`, the QA report and the updated `logs/` —
  `logs/upload_manifest.json` included — together with any pipeline changes
  that produced them.
