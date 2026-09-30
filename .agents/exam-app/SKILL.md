---
name: exam-app
description: Single owner of rendering and running the exam. Owns the whole app surface — Markdown sources → booklet HTML with A4 print geometry and furigana helpers (NO PDF, ever), the MERGED problem+answer sheet 解答.html with radio bubbles, an embedded 聴解 audio player and in-page 180-point grading, the untimed 練習.html (練習モード) that lays the same paper out flat with a per-question model answer, the ONE local server and test list, the static GitHub Pages build that keeps answers in localStorage, and CLI grading (scaled 0–180 scores, pass/fail evaluation, 採点結果.json) via grade_answers.py. Use whenever generating/regenerating/fixing exam booklets or formatting (answers squashed on one line, cramped spacing, furigana misaligned, tables splitting across pages); whenever the user wants to take/answer/solve a test on screen, mentions the answer sheet, マークシート, 解答用紙, 練習モード / practice mode, the test list, playing the listening audio while answering, or publishing/hosting the exam on GitHub Pages; and whenever the user asks to grade, score, check answers, 採点, 答え合わせ, or analyze exam results.
---

# Exam App (冊子レンダリング・解答用紙・サーバー・採点)

One skill owns booklet rendering, the merged problem+answer sheet, the
server, the static Pages twin, and grading — all in `.agents/exam-app/scripts/`:

| Script | Job |
| - | - |
| `build_booklet.py` | Markdown → booklet HTML (`言語知識・読解.html`, `聴解.html`); shared CSS, `render_body()` (the one render chain) and ruby/furigana helpers |
| `build_interactive.py` | Markdown → `解答.html`, the merged sheet with in-page grading; also the `--keyless` QA render |
| `build_practice.py` | Markdown → `練習.html`, 練習モード: the same paper flat, no clock, no grading, one model answer per question |
| `serve_sheet.py` | the ONE local server: portal, test list, exam, results, saved into `tests/<id>/`; also serves `knowledge/` and `drill/` (built by `jlpt-knowledge` / `jlpt-drill`) |
| `build_pages.py` | the static GitHub Pages build into `_site/` |
| `grade_answers.py` | CLI grading twin: scaled scores, pass/fail, `採点結果.json` |
| `app_style.py`, `portal_view.py`, `index_view.py`, `local_store.py` | shared modules |

## Shared modules — one copy of everything

- `app_style.py` holds `APP_CSS`; both builders import it. Add chrome there,
  never in either script — two copies drift, and no gate sees a drifted
  colour. Must stay free of bare element selectors (loads on top of the
  booklet stylesheet).
- `portal_view.py` — the level chooser and module chooser, plus the page shell
  (lang_ui's sticky bar, the scrolling title header, `PORTAL_CSS`) every portal
  screen and the exam list render through. Labels live in the language
  registry's `portal` namespace (`exam-model-answer/references/languages/<code>/portal.json`),
  one `.lang-pane` per language.
- `index_view.py` — the exam list's CSS/cards/actions, fed the same test objects
  by `/api/tests?level=` or a baked manifest. `make check` fails if `INDEX_CSS`
  or `PORTAL_CSS` is defined anywhere but its owner.
- `local_store.py` — `window.JLPTStore`, the ONLY place the localStorage key
  schema is written.
- `build_interactive.render_bodies()` calls `build_booklet.render_body()` for
  both halves (and imports its `CSS`/`SCREEN_CSS`), so sheet, practice page and
  booklet run ONE render chain — boxes, option grid, item-number boxes,
  underlines and 聴解 auto-furigana cannot differ. Sibling imports, both in
  this skill's `scripts/`.
- `build_pages.py` calls `build_interactive.build()` rather than copying
  `解答.html`, which would ship a sheet POSTing to a nonexistent API.
- `build_practice.py` imports the sheet's own `strip_key()`,
  `inject_gengo()`/`inject_choukai()` (through their `after=` hook),
  `render_bodies()`, `player_html()`, `PLAYER_JS` and `CHROME_JS`, and
  exam-model-answer's `explanation_box_html()`/`EXPLANATION_CSS` and
  `lang_ui` (the bar + dropdown), plus its registry-derived `LANGS`/`PRIMARY`/`UI`/
  `LANG_NAME`/`load_details()`/`kaisetsu_path()` — its own labels come from
  the registry's `practice.json` (exam-model-answer §"Languages — one
  registry"). It formats no exam text and no explanation prose of its own
  — 練習モード is the same paper and the same explanations, laid out differently.

## Execution

```bash
python3 .agents/exam-app/scripts/build_booklet.py tests/<id>/言語知識・読解.md tests/<id>/聴解.md   # make booklet <id>
python3 .agents/exam-app/scripts/build_interactive.py tests/<id>                                    # make sheet <id> — writes BOTH 解答.html and 練習.html
python3 .agents/exam-app/scripts/build_practice.py tests/<id>                                       # make practice <id> (練習.html alone)
python3 .agents/exam-app/scripts/serve_sheet.py                                                      # make serve (--port 8765, --no-open; NO test id)
python3 .agents/exam-app/scripts/build_pages.py                                                       # make pages (then make preview-pages)
python3 .agents/exam-app/scripts/build_interactive.py tests/<id> --keyless                           # make keyless <id> -> qa/<id>/keyless.md
python3 .agents/exam-app/scripts/grade_answers.py --test-dir tests/<id>                              # make grade <id>
```

Re-run the booklet AND sheet build after ANY edit to the `.md` sources — they
are the single source of truth; the grader parses keys out of them and the
sheet builder parses questions out of them. Editing HTML by hand is always wrong.

## Booklet rendering (`build_booklet.py`)

`言語知識・読解.md` + `聴解.md` → their HTML twins in the same folder. That is
the whole pipeline. **No PDF.**

### Why no PDF — this rule lives here now

`@page { size: A4 }` and page-break rules stay in the CSS, so Cmd-P from the
browser gives the same A4 booklet. Removing the PDF step removed a real
defect: WeasyPrint and wkhtmltopdf laid absolute-positioned `<rt>` out
differently, so whichever was on PATH silently changed the furigana output.
**Never reintroduce weasyprint/wkhtmltopdf/poppler** — no PDF toolchain at all.

### Non-negotiables baked into the script (know WHY they exist)

1. **`nl2br` is mandatory** — without it every vertically-stacked option
   list collapses onto one unreadable line.
2. **CJK fonts**: body = YuMincho (real booklets are 明朝 — confirmed via
   `pdffonts` on every `refs/JLPT_N2_NEW/` booklet), headings/bold =
   YuGothic. Ship as system fonts on macOS/Windows 8.1+; fallback chain adds
   Hiragino Mincho ProN/Hiragino Sans and Google-Fonts Noto Serif/Sans JP.
   Never put a sans-serif font ahead of YuMincho in the body chain — regressed
   once already (commit `116cc88` silently rendered a whole booklet
   sans-serif). Verify: `fc-list | grep -iE "yumincho|yugothic"`.
3. **Options (`widen()`)**: printed as official — `1　はしら`, no period. A
   line with 3+ options becomes a grid of 4 equal columns, 2×2, or one per
   line, whichever the LONGEST option fits (`COLS_*_MAX_EM`), so no option
   wraps mid-word; a vertical ` 1. …` line keeps its row. The sheet's parsers
   read the Markdown before `widen()`, so bubble counts never depend on it.
4. **Tables**: `width:100%; border-collapse:collapse; page-break-inside:avoid`.
5. **Page-break control**: avoid inside tables/blockquotes and inside one
   item (stem + options), avoid after headings; 読解 and the key open a new
   page, each 聴解 問題 too; line-height ≥1.9 for Japanese. `@page` prints
   「— N —」 and the section name as running head.
5a. **The official look** (`style_exam()`, exam part only): boxed item number
   (`strong.bk-qn`) with the stem hanging past it; bold-Gothic
   「問題N」 + hanging instruction, no shading; 【文字・語彙】-style parts as
   small boxed labels; the tested word `**word**` UNDERLINED in 明朝
   (`strong.bk-tw`) — a bold span that fills its own line or opens one as a
   label (`**夕食**　…`) stays bold; ーメモー → centred 「― メモ ―」. The
   Markdown conventions do not change. The first paragraph's leading U+3000
   indent survives Markdown (`keep_indent()`).
5b. **Cover** (booklet HTML only; the sheet has its gate): level, section name
   and minutes from the level table, 注意 box, 受験番号・名前 lines. A named
   `@page bk-cover` resets the counter so page 1 is the first question page.
6. Layout per `jlpt-exam-structure`: horizontal options for 文字・語彙・文法,
   vertical for 聴解 and 問題6.
7. **Ruby furigana**: `<ruby>漢字<rt>かんじ</rt></ruby>`, stacked by hand
   (not `ruby-position` — old PDF renderers ignored it and dropped the base
   below the reading). `ruby` is `inline-block; position:relative;
   line-height:1`; `rt` is `position:absolute; bottom:calc(100% + 0.1em);
   left/right:-0.6em`. `fit_ruby()` gives ruby a `min-width` when the reading
   is wider than its base; `mark_furigana_blocks()` adds `class="furi"`
   (line-height 2.1) only to blocks containing ruby.
8. **Vocabulary notes** (`（注1）…`): `.vocab-notes` (10pt, no rule) under the
   passage; inline （注N） markers print small and raised (`.bk-chu`).
9. **Passage boxes are not optional decoration** — official booklets print
   every 問題9–14 passage/notice inside a thin black rule on white, separate
   from the questions below it (`.passage-box`, produced by `box_passages()`).
   A box over `FLOW_CHARS` or holding a table carries a hidden `.bk-flow`
   first child and may break across pages (a scroll container or an
   unbreakable over-tall box printed 問題14 as a blank page); 問題14's flyer
   (`FLYER_START`) opens its own page. The open tag stays exactly
   `<div class="passage-box">` — the gate and `build_practice` match it.
   **14 boxes per paper**: 問題9 ×1, 問題10 ×5, 問題11 ×4, 問題12 ×2 (A and B
   box separately), 問題13 ×1, 問題14 ×1 — `make check`
   (`check_passage_boxes`) FAILs any other count, in the Markdown AND in both
   built HTML files. The box comes from pattern-matching the source, so an
   authoring dialect the boxer misses prints an unboxed passage with no error:
   both the `## 問題N` + inline instruction and the bare-heading + instruction-
   paragraph forms are matched, and 問題12's texts may be labelled `### A` or
   `**A**`. A dialect that ships boxless is a `box_passages()` bug — teach the
   boxer, never hand-edit HTML (2026-08-20: three papers rendered 0 boxes and
   three more merged 問題12's A and B into one, all green).
10. **`add_choukai_furigana()`'s pykakasi output needs a fixup pass** — a
   2026-08 audit found real wrong readings: bare `人` came back `にん` instead
   of `ひと` (genuine `にん` compounds like 三人/本人 are long enough that
   kakasi already merges them, so a standalone `人` is always "hito"); `方`
   right after hiragana came back `ほう` instead of `かた`; `小さい`/`小さく`
   came back with a bogus chouon. All three are corrected by `fix_hira()`
   inside `add_choukai_furigana()` — if you touch that function again or
   spot another wrong reading, fix it there (not the generated HTML) and
   rebuild every test's `聴解.html`.

`SCREEN_CSS` is the screen-only shell: a centered 60em column plus a
`--gutter` variable the sheet's sticky bar/audio player use — entirely inside
`@media screen`, so `@page` A4 geometry is untouched.

### `verify()` — automatic, aborts the build

Runs on every build on the HTML STRING, before anything is written (a failing
build leaves the previous file, never a freshly stamped bad one); aborts on mojibake, an `<ol>` in the output (stems must
be bold `**6**`, never `N.` list syntax which restarts numbering), or a
gap in the bold stem numbers (they must run 1..max contiguously, whatever the
level's count). Still check by eye that key/
explanation tables render at the end of both files and furigana sits over
its base; Cmd-P to preview pagination.

## The three screens (behind the portal)

Entering the site is two portal screens before the list, identical in both
deployments (`portal_view.py`):

| URL (= `_site/` file) | Screen |
| - | - |
| `/` (`index.html`) | level chooser — N1–N5 cards: status (`level.py`: calibrated / structured / scaffold, `none` without a table), test count, 知識 availability. A level with nothing is disabled (「準備中」), never hidden |
| `/<LEVEL>/` (`<LEVEL>/index.html`) | module chooser — three cards: 試験 (→ `exam/`), 知識 (→ `../knowledge/<LEVEL>/`, built by `jlpt-knowledge`; its categories counted by `knowledge_data.summary()`, a category shown only with ≥1 entry) and ドリル (→ `../drill/<LEVEL>/`, built by `jlpt-drill` — 大問別練習, 聴解トレーニング, 復習ノート, 進捗ダッシュボード, 読解ライブラリ); a module with nothing (no tests / no `index.html`) is disabled 「準備中」, never hidden |
| `/<LEVEL>/exam/` (`<LEVEL>/exam/index.html`) | screen 1 below, that level only, with a breadcrumb back |

**Every link is relative** and names `index.html` — Pages serves from
`/<repo>/`; `make check` fails an absolute `href="/…"` on any portal page.

`解答.html` merges the problem booklet and radio bubbles into one
deliverable: answer **inside the booklet**, press 「採点する」, the 180-point
result appears immediately. `make serve` (no test id) covers every test; the
same screens ship as a static Pages site — only where answers are kept differs.
The paper's other mode, 練習.html, is its own page and not one of these three —
see 練習モード below. Both link back to their level's list,
`../../<LEVEL>/exam/index.html` (`build_interactive.list_href()`).

| # | Screen | Where it lives | What it does |
| - | ------ | -------------- | ------------ |
| 1 | テスト一覧 | `GET /<LEVEL>/exam/` — `serve_sheet.py` | that level's tests, answered count, last score, origin badge (`imported`/`generated`), under two collapsed `<details>` groups + a search box |
| 2 | 受験 | `GET /tests/<id>/解答.html` | the exam, in two timed phases (below); each click autosaves |
| 3 | 採点結果 | same page, `#screen-result` | rendered on 「採点する」 or fetched from `採点結果.json` |

A graded test is never locked — 「解答に戻ってやり直す」 reopens screen 2 with
saved answers, re-grading overwrites `採点結果.json`. That is AFTER the sitting;
during one, the phase machine below decides what reopens. `解答.html` is NOT the
booklets, which `build_booklet.py` overwrites on every build; there are no
per-section `*_解答.html` files.

**`make mp3` obliges `make sheet`.** The player embeds `聴解_チャプター.json`
verbatim, so every chapter offset comes from the MP3 build that wrote that
file. Rebuild audio and the sheet seeks to the previous build's offsets while
the Markdown stays byte-identical — the chapter JSON is stamped as a
**fourth source** of `解答.html`, and `make check` fails a sheet older than
its chapters.

## 練習モード — `練習.html`, the paper's other mode

The sitting above is one way to use a paper; studying it is the other, and they
want opposite pages. `練習.html` is built from the same Markdown by the same
injectors, and it is deliberately NOT a sitting:

| | `解答.html` (試験モード) | `練習.html` (練習モード) |
| - | - | - |
| What is on screen | one section at a time, behind a 開始する gate | all 101 items, both sections, from the start |
| Clock | 105分 / 50分, auto-submits at 00:00 | none |
| Score | 180 points, once, when 聴解 goes in | none — nothing is added up |
| Model answer | after grading (or in `模範解答.html`) | one button per question, any time |
| 読解 passage | Japanese only | 原文 / 訳 toggle per passage, in the learner-language editions |
| Record kept | `ユーザー解答.json` + `採点結果.json` | **nothing** |

- **The way in is a button under 言語知識・読解's 開始する button** (`gate()`),
  because that is the moment the choice is actually made — finding the practice
  page must not cost you the start of a sitting. `make sheet` writes BOTH pages,
  so the link cannot point at a practice page built from a superseded booklet;
  `make model-answer <id>` rebuilds it too, because `詳細解説.json` is the one
  source it has that `解答.html` does not (`make check` fails a practice page
  older than its explanations); `make practice <id>` rebuilds it alone.
- **One 解説 reveal per question**, injected right after that question's bubble
  row through `radios(after=…)`. Opening it shows 正解: N, the 聴解 script for a
  listening item, and exam-model-answer's own `.explanation-box` — the same
  markup `模範解答.html` prints, in both languages behind the same
  `.lang-pane` mechanism and the same stored preference
  (`build_model_answer.LANG_STORE_KEY`). No explanation prose is formatted here.
- **One 原文 / 訳 toggle per 読解 passage, in the learner-language editions only**
  (2026-09-10). Studying a passage means reading it, and a learner who is
  working the paper in Tiếng Việt (or any registry learner language) should not
  have to open `模範解答.html` to see what it says. So the control is exam-model-answer's own — `ptext_switch_html()`,
  `PASSAGE_TOGGLE_CSS`, `PASSAGE_TOGGLE_JS`, over the `passage_translation` that
  already lives on the first item of each group in `詳細解説.<code>.json`
  (AGENTS.md §2). One mechanism, one copy; nothing about the learner files
  changes. Four things
  are this page's own and none of them may be re-decided quietly:
  - **原文 is the default.** `模範解答.html` opens on the translation because its
    answers are already out; here the questions are still live, and opening on
    the 訳 would hand over the passage the item is asking about.
  - **The toggle is learner-editions-only, and the Japanese edition is
    untouched** — the control and the translation pane sit in one
    `.lang-pane[data-lang="<code>"]` per learner language that has translated
    that group, inside a `.passage-tr` wrapper; the booklet's own box is not
    wrapped in a pane at all. Switching edition resets
    every passage to 原文 (`resetPassageText()`), so no group is ever left
    showing a pane the current edition does not render.
  - **The booklet's boxes are moved, never copied.** A paper prints exactly 14
    `.passage-box` divs and `make check` (`check_passage_boxes`) counts them in
    this file too, so the source appears once: the toggle wraps the box(es) and
    the translation is a `.pr-tr` panel beside them. 問題12 is ONE 詳細解説 group
    printed as TWO boxes, so its run — A's label, both boxes, B's label — sits
    under one toggle and one translation.
  - **A group with no translation gets no control** and no empty box; a paper
    mid-pipeline renders exactly as before.
- **The verdict is per item and appears with the answer**: opening a reveal
  compares your selection with the key and marks 正解/不正解 for that question
  alone. No total is computed anywhere on the page — 採点 belongs to the sitting,
  and a practice page that scored you would be a second, untimed grader.
- **Nothing is stored.** No POST, no localStorage, no download: marks made in
  practice are gone on reload. A second answer store beside the sitting's is
  exactly the desync 「One store per build」 exists to prevent, and there is no
  score to keep. The only thing read back from the browser is the explanation
  language. **The 原文/訳 choice rides nothing and is stored nowhere** — it is
  per passage and per visit, exactly as on `模範解答.html`. Persisting it would
  mean a second key, and one that means nothing on the sitting's page; a reader
  who wants the translation is one click from it.
- The container id is `screen-exam`, reused on purpose: this IS the exam screen
  with the phase machine taken out, so the sheet's layout, bubbles, player
  chrome and 「聴解 ｜ 問題2」 read-out apply unchanged. `make check`
  (`check_practice_mode`, plus the per-test half) asserts the link resolves, the
  two pages carry the same 101 questions, every question has a reveal, and the
  page carries no clock, grader or store.

## Grading — press 「採点する」 (in-page: the normal path)

Grades all 101 questions against embedded keys, evaluates section cutoffs
(≥19/60) and total (≥90/180), switches to screen 3, and saves to whichever
store this build uses (`採点結果.json`/`ユーザー解答.json`): into `tests/<id>/`
under `make serve`, into localStorage on Pages, or as browser downloads with
no server/store. Unanswered items appear as 「未解答」 chips, not wrong — the
CLI grader still grades a partial paper, and the clock below can submit one.

**Grading happens ONCE, when 聴解 goes in.** There is no score at the
言語知識・読解 hand-off: half the answer key on screen mid-exam is not a
mid-point summary, it is a leak. `submitAll()` grades all 101 items.

**Advancing or grading BY HAND needs the section complete** — 聴解へ進む and
採点する stay `disabled` until every item in the live section is answered
(`updateCounter`), and both handlers re-check and scroll to the first gap. The
clock is the one thing allowed to submit an incomplete section.

## Screen 2 is a two-phase sitting, not a worksheet

`PHASE` is the only thing that decides what is on screen, what is answerable,
and which clock runs. `render()` is the only function that acts on it; nothing
else touches the visibility of a section, a gate, a tab or a control.

| PHASE | On screen | Clock | Ends by |
| - | - | - | - |
| `gengo` | 言語知識・読解 (71 items) | 105分 | 聴解へ進む, or 00:00 |
| `choukai` | 聴解 (30) + the player | 50分, or the recording +1分 | 採点する, or 00:00 |
| `done` | the whole paper, unlocked, no clock | — | re-grading overwrites |

- **Each section sits behind a 開始する gate.** The clock does not move until it
  is pressed, so opening a test to look at it costs nothing — and since this
  clock submits the paper by itself, "started by accident" would otherwise be a
  lost sitting. 聴解's gate is also where you get your headphones on.
- **gengo → choukai is ONE WAY.** The 読解 booklet is collected before 聴解 in
  the real sitting, so its items leave the screen and its radios are `disabled`.
  The confirm says so before it happens; at 00:00 there is no confirm.
- **00:00 auto-submits the section** — `timeUp()`, the one submit path that
  skips the completeness check. `EXPIRING` guards it against the 500 ms
  interval re-entering while its alert is up.
- **The clock only runs while the exam is in front of you**: `clockRunning()`
  wants the tab visible AND focused AND its section on screen, so switching
  tabs freezes it and the readout says 「（停止中）」. Deliberately this repo's
  choice over exam realism — it means a practice sitting can be paused by
  switching away. Recomputed from `Date.now()` on every paint, so a throttled
  background timer cannot make it drift.
- **A graded paper reopens whole.** `done` is review mode: both halves visible
  and answerable, no clocks, 採点する live again — the documented "a graded test
  is never locked" behaviour, now confined to after the sitting.
- **消去 is the escape hatch**, and the only way back into a section you have
  left: it resets the clocks and the phase along with the answers, because a
  half-run countdown with no answers under it is not a state anyone can finish
  from.

**The two allowances belong to `jlpt-exam-structure`** (§'言語知識…— 105 min',
§'聴解 — ~50 min'), and its level table carries them per level as `timing`
(`references/levels/<LEVEL>.json`), which is what `section_limits()` enforces.
`GENGO_LIMIT_MIN` / `CHOUKAI_LIMIT_MIN` are N2's row, and `make check`
(`check_exam_time_limits`) reads them back against the skill prose so the two
cannot drift. Change the exam's timing there first, never in the builder.

**Every level-dependent number the app prints comes from that table** — the
大問 map and era shapes, the 聴解 labels, section names, per-section max and
cutoff, total and pass mark (N2: 60/19 ×3, 180, 90), the study advice and the
「JLPT N2」 titles. `level.py` resolves a test's level from its folder name
(`n1-…`, `imported-n1-…`; bare = N2); the portal's level chooser routes by it
and the list shows it on every card. The audio-release fallback URL is `level.REPO`.

**聴解's clock is never shorter than its audio.** The recording IS that section
and an official one can run past 50 minutes (imported-n2-2025-12 is 51.4), so
`section_limits()` takes whichever is longer, the allowance or the recording
plus a minute — read off `聴解_チャプター.json`'s `duration` for a generated
test, off ffprobe for an imported one (optional: `make sheet` must not grow a
binary dependency `make mp3` already owns), and off the `<audio>` element's own
metadata at runtime for a machine that has neither and for the Pages build.

**Where the sitting is kept: `ユーザー解答.json`, in a `受験状態` block** beside
the answers — phase, both remaining times, which sections have started. It is
the record of ONE sitting and has to survive a reload with the answers it
belongs to. Every reader of that file picks the two answer halves out BY NAME
and ignores the rest (`grade_answers.py`, `serve_sheet.py`'s progress count,
`flattenSaved()`), so this cost no grader change and left `採点結果.json`'s
shape — the one `make check` compares field for field — untouched. Phase
changes write through the debounce (`persistNow`); a running clock also
heartbeats every 15 s, so a tab killed mid-section hands back 15 seconds, not
the section.

**全設問解答チェック表 expands as one list** — 「すべての設問詳細を展開」builds
detail blocks for all 101 items from the still-in-DOM exam screen plus
あなたの答え/正解 (display-only).

### One source of truth for the grading data

`grade_answers.py` is the in-page grader's CLI twin. `computeResult()`
returns the **same document** `grade_answers.py` writes, stays free of DOM
and `Date`, and `make check` runs it under node and compares field for field
against the Python grader. There is no Markdown report — the result is data.

`ANSWER_KEY`, `TAXONOMY`, `ADVICE`, and section definitions are **serialized
out of `grade_answers.py` at build time** — never hand-write those tables
into JS (a second copy is exactly how the grader's 大問 ranges once drifted
from `jlpt-exam-structure`). Re-run `build_interactive.py` after changing any
of them.

## The answer key must never be VISIBLE — one truncation, three build modes

The key is embedded as JS data so grading works offline, but never
_rendered_. `strip_key()` truncates everything from the key heading onward,
and the builder errors if it can't find that heading — never loosen the
check. Every emitted document goes through the same `strip_key()`.

| Mode | Command | Writes | Keys |
| - | - | - | - |
| server sheet (default) | `make sheet <id>` | `tests/<id>/解答.html` | embedded JS, never rendered |
| Pages sheet | `make pages` | `_site/tests/<id>/解答.html` | same |
| **keyless render** | `make keyless <id>` | `qa/<id>/keyless.md` | **none, anywhere** |

### `--keyless` — the QA blind-solve render

`exam-qa-review`'s first ground rule is blind-solve before reading the keys
— unexecutable before this existed, since the keys live at the END of the
same two Markdown files the paper lives in. `--keyless` emits the whole paper
through `strip_key()` plus `聴解スクリプト.txt` verbatim, embeds no key data
at all, and scans the text with `KEY_HEADING` BEFORE writing, refusing to
write a render that still carries one. Header carries each source's `sha1[:12]` —
what the QA report header must name. Not a deliverable: lands in
`qa/<id>/keyless.md` (gitignored), beside the QA report.

## Audio player (聴解 only)

- `<audio src="聴解.mp3">` is referenced relatively, never embedded (a ~30MB
  base64 blob would be ~40MB of HTML). Controls: play/scrub, ±10s, speed
  0.75–1.5, chapter dropdown.
- **Chapter marks** come from `聴解_チャプター.json` (exact assembler offsets,
  not silence-detection guesses) — absent, the dropdown just hides itself.
  Entries carry no `type`: a label without 番/質問 (「問題2」) is a 大問 header,
  the rest are indented items; an explicit `type` still wins.
- Some browsers block `file://` media: a 「MP3を選ぶ」 picker is always
  present as fallback. Never require a web server.

## Serving (`serve_sheet.py`) — five things it must keep doing

1. **One server, every test** — no arguments, serves the whole `tests/`
   tree; routes `/`, `/<LEVEL>/`, `/<LEVEL>/exam/` (rendered per request; a
   folder URL without its slash redirects), `/api/tests[?level=]`,
   `/tests/<id>/…`, `/knowledge/<LEVEL>/…`, `/drill/<LEVEL>/…`, `POST /api/tests/<id>/
   {answers,submit,clear}`. Only paths under `tests/`, `knowledge/` and `drill/`
   (`SERVED_ROOTS`) are reachable.
2. **The portal and the list read the disk, never a cache** — the pages and
   `GET /api/tests` carry `Cache-Control: no-store`.
3. **Range requests** — `聴解.mp3` is ~30MB and `<audio>` re-requests with
   `Range:` on every seek; the handler answers `206 Partial Content` itself
   and advertises `Accept-Ranges: bytes`.
4. **Client disconnects are not errors** — swallow `BrokenPipeError`/
   `ConnectionResetError`, never re-raise.
5. **Threaded** (`ThreadingHTTPServer`) — a single-threaded server would
   queue 採点する behind an in-flight MP3 stream.

## Two deployments, one app — `make serve` and GitHub Pages

Same three screens, two storage backends, never two apps:

| | `make serve` (local) | GitHub Pages (`make pages`) |
| - | - | - |
| Portal | `/`, `/<LEVEL>/` rendered per request | `_site/index.html`, `_site/<LEVEL>/index.html`, baked |
| Screen 1 | `/<LEVEL>/exam/`, `GET /api/tests?level=` reads disk | `_site/<LEVEL>/exam/index.html`, progress from localStorage |
| 知識 / ドリル | `knowledge/<LEVEL>/*`, `drill/<LEVEL>/*` served as files | every `*.html` under them (sub-folders included) copied to `_site/knowledge/<LEVEL>/`, `_site/drill/<LEVEL>/` (`copy_module`) |
| Screens 2–3 | `解答.html`, `--storage server` | `_site/.../解答.html`, `--storage local` |
| Answers | `ユーザー解答.json` via `POST /api/…` | `localStorage[jlpt-mock/v1/<id>/…]` |
| Result | `採点結果.json` via `POST /api/…` | `localStorage[…]` |

```bash
make pages            # every test → _site/   (make pages 1 for one test)
make preview-pages    # python3 -m http.server -d _site 8766
```

`.github/workflows/pages.yml` runs this on push. `_site/` is **gitignored** —
CI rebuilds from `tests/`; MP3s (~30MB/test) are copied in, `--no-audio`
skips them. Pages' CDN answers `Range:`; `make preview-pages`'s
`http.server` does not (a preview-only limitation).

**CI deploys WITHOUT audio, on purpose — and the reason is billing.** The MP3s
used to be LFS-tracked, and `actions/checkout` with `lfs: true` smudged every
LFS object in the tree: the `refs/` archive (~2.6 GB the site never reads) plus
~0.5 GB of `tests/*/聴解.mp3`, on every push. That exhausted the account's LFS
budget, and past that point the batch API refuses every object and **checkout
itself fails** — no page gets built at all. LFS was removed on 2026-08-24:
`tests/**/*.mp3` and `refs/**/*.{pdf,mp3}` are now gitignored and live in the
`audio` and `refs` Releases instead (AGENTS.md §3, `make upload-files`).

What that means for the deploy: a CI checkout simply HAS no `聴解.mp3`, so
`make pages` finds nothing to copy and each sheet falls back to the release URL
`…/releases/download/audio/<test_id>.mp3`, which the browser streams directly.
**So the audio does play on the deployed site — as long as the test's MP3 has
been uploaded.** Ship a new test's audio with `make upload-files TARGET=tests
TEST=<id>`; forget it and the page deploys with a player that 404s.
`build_pages.is_lfs_pointer()` stays as a guard for old clones that still carry
a pointer stub — copying a stub would deploy a silent player and a card
claiming audio, all green. The sheet's 「MP3を選ぶ」 picker still plays a local
file either way.

**One store per build.** Exactly one backend is live per build, chosen at
BUILD time (`--storage server|local`), never sniffed at runtime — a server
sheet contains no localStorage code at all. `make check` asserts every
`解答.html` is always the server build with no store prefix.

**What Pages cannot do:** no disk, so local builds grow a 「採点結果を保存
（JSON）」 button and a 「バックアップを保存/読み込む」 pair — one JSON per
test's two documents, and how answers move between browsers. Say so on the
page: clearing site data loses the lot.

### Screen 1 groups the cards — collapsed by default

The list holds one level (chosen upstream — there is no level switcher) and its
labels are the `portal` namespace's `list_*` strings, both languages in the
markup (JS builds panes; `title=`/`confirm()` use the language on screen).

`origin` already decides the badge, so it decides the grouping: 公式過去問
(`imported-*`) and 模擬試験 (everything else) are two `<details>`, **shut on
load** — twenty cards opened flat is a scroll, two summary lines is a choice.
Each summary carries its own 件数 and 採点済み count. The search box above them
filters on id + origin (space-separated terms, all must match) and force-opens
whichever group holds a hit; a group with no hit renders 「該当するテストは
ありません。」 rather than vanishing, so the two halves stay in the same places.
Open/shut is kept in JS (`OPEN`), because `refreshList()` re-renders on every
`pageshow` and a group must not snap shut on the way back from a graded exam.
The search box lives in the static shell, NOT inside `#cards` — re-rendering
the list must not destroy the field being typed into.

## On-screen layout — one design across three screens

**One sticky bar per page, and it is exam-model-answer's `lang_ui.topbar_html()`**
(2026-09-30): breadcrumb left (level › module › page, relative links), the
page's own compact controls, then the language dropdown — the original `#bar`'s
size (≈50px desktop, 44px phone, 1.8em side padding; the owner rejected a 40px
slim bar as too small, 2026-09-30), one line at 375px (crumbs ellipsize, `tb-wide` controls drop, `tb-long`/
`tb-short` labels swap), hidden in print. Every page but the two booklets carries
exactly one (`make check`, `check_site_chrome`). The sheet's old `#bar` is merged
into it: `解答.html`'s right side is the two section tabs, the 「聴解 ｜ 問題2」
read-out (`#where`), then `#bar-controls` — clock, counter, 消去, 聴解へ進む, 採点する
(same ids, same gating); its page crumb reads 受験 / 採点結果 by
`html.is-result-mode`. `練習.html`'s is the read-out, answered count, 解説をすべて開く
and 試験モードへ. Page titles/heroes (portal, list, 模範解答) are ordinary content
under it; 模範解答's tabs+search no longer stick.

**解答.html's chrome is bilingual** — gates, bar, dialogs, result screen, player,
advice — from the registry's `exam` namespace. Markup built in Python is
`.lang-pane`s (`T()`); JS builds markup with `P()` (every language, CSS-switched)
and plain text (confirm/alert, `title=`, the clock) with `S()` (the language on
screen), repainted on the switcher's `langchange` event. The weak-大問 advice
under the 大問 table is picked per language by 大問 code (`exam.json` `advice`);
`採点結果.json` keeps the Japanese `advice` unchanged. Exam wording — stems,
options, passages, scripts, section names, 大問 names — stays Japanese.

Screens 2–3 keep the booklets' centered 60em measure, moved onto
`#screen-exam`/`#screen-result` so the bar spans the window like screen 1.
Screen 1's `<main>` is wider (80em) for cards — don't widen the exam/result
columns to match, and don't use `width:100vw` (includes the scrollbar,
shoves 採点する off-screen). All inside `@media screen`. `initSpy()`/
`updateSpy()` track the nearest heading above the bar (「聴解 ｜ 問題2」);
`fitPlayer()` measures the bar (`#topbar`) and sets the player's sticky offset —
never hard-code it.

**Bubbles** look like マークシート ovals (`.qa label`, CSS only): a tall oval
with its digit, filled solid when chosen; the radio is transparent over it, so
behaviour and every `input[name=q_…]` lookup are unchanged.

## Answer capture

Every radio click writes to the one place this build uses (and so does every
phase change and every clock freeze — same document, see 受験状態 above):
`ユーザー解答.json` via `POST /api/tests/<id>/answers` (debounced ~250ms)
under `make serve`, or the matching localStorage key on Pages — nothing in
the page knows which backend it talks to. 採点する writes `採点結果.json`
plus the same shape: `{"言語知識_読解": {"33": 2, …}, "聴解": {"問1-1": 2, …}}`.

## Parser contract (why the Markdown conventions are load-bearing)

- 言語知識: `**33** stem` then indented ` 1. … 2. …`, OR 問題6's `**28 募集**`,
  OR 問題9's all-on-one-line form. **問題7 dialogue stems may span lines**
  after `**N**` — `inject_gengo` must keep `cur` across those lines
  (flushing on every non-option line once dropped radios for Q32/39–42).
- 聴解: `**1番**` + indented options (問題1/2 only), OR a bare bubble row
  `**1番** 1・2・3・4` for 問題3/4/5. **All of 問題5 takes the bubble-row
  form, including `質問1`/`質問2`** — this repo prints no options for either
  item, so 質問N is a bubble row, not a heading over an option list.
- `**例**` rows get a STATIC row with the answer pre-filled, never radios —
  the number comes from the 解答用紙 grid's `**(n)**` cell, read before
  `strip_key` truncates it; `make check` asserts it equals the announced number.
- **The builder warns loudly** on a question with no radio group or a group
  with no key — always a Markdown bug, never noise.

## CLI grading (`grade_answers.py`)

Parses keys from the two Markdown sources, reads responses, writes
`採点結果.json`. **User answers are auto-discovered**: `ユーザー解答*.json` in
the test dir only (matched NFC-normalised; a stray file in the shell's cwd is
not merged); inline `--answers-gengo`/`--answers-choukai` override. With no
answers loaded it exits without writing, so a real `採点結果.json` is never
replaced by an empty grading. Rounding is half-up (`js_round`), `Math.round`'s rule.

- **Scaled 0–180 scoring**: raw section counts → 0–60 per section —
  言語知識 (51 items), 読解 (20 items), 聴解 (30 answers; 問題5-2番 yields two).
- **The scale is proportional, an approximation — say so.** The real exam
  equates scores across sittings (得点等化), which needs statistics this repo
  doesn't have. Never describe the output as a real JLPT score or "improve"
  it with invented difficulty weights.
- **Pass/fail (published N2 criteria)**: total ≥90/180 AND every section
  ≥19/60 — failing any one sectional cutoff is 不合格 regardless of total.
- **Taxonomy**: 大問→question ranges owned by `jlpt-exam-structure`;
  `GENGO_QUESTION_TAXONOMY` asserts at import that its ranges tile 1–71 with
  no gap/overlap. No copy of the table lives in this doc.
- **Advice integrity**: weak-area advice maps to the matching Shin Kanzen
  Masuta N2 study area.

## Result document (`採点結果.json`) — the schema is a contract

Data, not prose. `解答.html` and the test list read it back;
`result_payload()` in `grade_answers.py` is its only Python definition,
`computeResult()` builds the identical structure, `make check` compares both
field for field:

```jsonc
{
  "test_id": "1",
  "graded_at": "2026-08-05T09:12:33+00:00",   // the ONLY field allowed to differ between graders
  "summary": {
    "passed": false, "total_scaled_score": 118, "max_scaled_score": 180,
    "cutoff_passed": true, "overall_threshold_passed": true,
    "sections": {
      "言語知識（文字・語彙・文法）": {"raw_correct": 33, "raw_total": 51, "scaled_score": 39, "cutoff": 19, "passed_cutoff": true},
      "読解":   {"raw_correct": 14, "raw_total": 20, "scaled_score": 42, "cutoff": 19, "passed_cutoff": true},
      "聴解":   {"raw_correct": 20, "raw_total": 30, "scaled_score": 40, "cutoff": 19, "passed_cutoff": true}
    }
  },
  "taxonomy_stats": { "問1": {"name": "漢字読み (Kanji Reading)", "section": "言語知識", "correct": 3, "total": 5, "percentage": 60.0} },
  "weak_areas": [ {"code": "問3", "name": "…", "section": "言語知識", "percentage": 33.3, "advice": "…"} ],
  "detail_gengo":  {"1": {"correct": 4, "user": 2, "is_correct": false}},
  "detail_choukai": {"問1-1": {"correct": 2, "user": null, "is_correct": false}}
}
```

The result screen renders 総合判定, 得点サマリー, 大問別詳細分析,
全設問解答チェック表. 大問 ratings: `優` (≥80%), `良` (60–79%), `要強化`
(<60%) — plain text, no emoji. **These bands are a repo-internal study
diagnostic, not the official 参考情報** (the real 合否結果通知書 reports A/B/C
only for 文字・語彙/文法, 合否判定の対象外) — keep the distinction; aligning
the two means changing both graders plus the parity test.

## Verification

```bash
make check            # the real gate — asserts everything below, every test on disk
```

Booklets: `verify()` on every build. Sheet: 101 radio groups, every expected
key present, no shared group name, 4 options per gengo question and 3 for
問題4 (393 inputs total), no emoji in report labels, and the in-page grader
matching `grade_answers.py`'s `採点結果.json` field for field. Deployments:
both deployments render the portal through `portal_view` and the list through
`index_view`, the server routes the Pages tree and serves exactly `tests/` +
`knowledge/` + `drill/`, every module chooser carries all three cards, portal links are relative, every sheet/practice page links back to
its level's list; the localStorage prefix
lives in exactly one module; every `解答.html` is the server build; `_site/`
is gitignored with `.nojekyll`.

Two option-counting bugs the sheet checks were written to prevent (both
shipped and made the exam partly unanswerable): **one bubble per horizontal
question** (`option_run()` counts a consecutive `1..k` run only, so
`1. 価格が3.5倍…` isn't miscounted), and **問題5's 質問1/質問2 colliding with
1番** — 質問N always belongs to 2番 whenever the section is 問題5, in both
parser paths.

Manual spot-check after a parser change:
`python3 .agents/exam-app/scripts/build_interactive.py tests/1` — expect
exactly 101 items, zero warnings. After any scoring JS change, `make check`
runs the parity check (extracts the last `<script>`, stubs the DOM, calls
`computeResult()` under node, compares with `grade_answers.result_payload()`).

## Environment

`python3 -m pip install markdown pykakasi` plus Noto CJK JP fonts. **No PDF
toolchain** — no weasyprint, no wkhtmltopdf, no poppler.
