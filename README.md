# JLPT Mock Exam Workshop

Generates, calibrates, renders, and grades **official-quality JLPT mock exams**,
plus imports real past papers into the same format. The pipeline is built for
all five levels (N1–N5); **N2 is the calibrated one today**, and adding another
level is mostly a matter of adding its `refs/` archive — see
[Adding a level](#adding-a-level).

Repository: <https://github.com/feiluvnana/JLPT> (renamed from `JLPT-N2` on
2026-09-28; the old URL redirects). Live site:
<https://feiluvnana.github.io/JLPT/>.

Each test is a folder under `tests/<test_id>/` holding a complete sitting:

- `言語知識・読解.html` — Language Knowledge & Reading booklet (A4 print geometry, furigana)
- `聴解.html` + `聴解.mp3` — Listening booklet and audio composed from real recordings
- `聴解スクリプト.txt` — the transcript of the clips the audio is cut from
- `解答.html` — one merged answer sheet: every item (N2: 71 言語知識・読解 + 30 聴解),
  radio bubbles, embedded audio player, **in-page 180-point grading**
- `採点結果.json` — the grading result, read back by the result screen

Item selection is never left to a language model's memory: grammar points,
vocabulary and kanji are drawn by a seeded RNG from a non-repeating pool and
recorded in `logs/ledger.json` so papers don't repeat; reading topics are
authored against an assigned theme and an avoid-list; the listening half is
composed from banked real recordings.
Difficulty is calibrated against 31 sittings of real N2 past papers and the
Shin Kanzen Master textbooks in `refs/`.

> **Scope of this file.** README owns **environment setup only** — what to
> install and how to verify it. Everything else has exactly one owner
> elsewhere, and this file deliberately does not restate it:
>
> | You want | Read |
> | --- | --- |
> | The rules, **where everything lives** (§2 map), file naming, command router | **`AGENTS.md`** |
> | To generate a new mock exam | `GENERATE.md` → `.agents/jlpt-test-generation/SKILL.md` |
> | To import an external PDF / past paper | `IMPORT.md` → `.agents/external-test-import/SKILL.md` |
> | How any one subsystem works | the 10 skills in `.agents/<name>/SKILL.md` |
>
> If this file and an owner file ever disagree, **the owner wins** — and the
> disagreement is a defect to fix, not to route around.

---

## Prerequisites

| # | Requirement | Needed for | Required? |
| - | --- | --- | --- |
| 1 | **Python ≥ 3.10** | everything (CI runs 3.12) | **yes** |
| 2 | `markdown`, `pykakasi` | booklet + answer-sheet rendering, furigana | **yes** |
| 3 | — | Edge-TTS was retired 2026-09-08: `make mp3` composes the audio from real recordings, no internet (`choukai-audio` Part 0) | — |
| 4 | **ffmpeg** *and* **ffprobe** on `PATH` | `make mp3` — concat, loudness, duration | for listening audio |
| 5 | `pdfplumber`, `pypdf`, `pdfminer.six` | PDF extraction (`make extract-*`, imports) | for imports/refs |
| 6 | **GNU Make + a POSIX shell** | the `make` targets use `test -n … \|\| ( … )` | **yes** |
| 7 | **Git** (no LFS) | Git LFS was removed 2026-08-24. NO binary is in git: the listening MP3s and the 2.6 GB `refs/` archive both come from GitHub Releases — see [Binaries live in Releases](#binaries-live-in-releases) | **yes** |
| 7b | **`gh`** (GitHub CLI, authenticated) | fetching those binaries and `make upload-files` | for audio/refs |
| 8 | **Git symlink support** | `.claude/skills/*` are 10 symlinks into `.agents/*` | **yes** |
| 9 | **Noto Serif CJK JP + Noto Sans CJK JP** | the booklet CSS names these two fonts explicitly | for correct print output |
| 10 | **Node.js** | one gate check compares the in-page grader with `grade_answers.py` | optional (check skips) |
| 11 | **poppler** (`pdftoppm`) | `make extract-archive` page rasterisation | optional |
| 12 | `mutagen` | MP3 duration in `write_external_chapters.py` | optional |

There is no `requirements.txt` — install the Python packages with the one-liner
in your platform's section below.

---

## Setup — macOS

```bash
# 1. System tools
brew install python git gh ffmpeg node poppler
brew install --cask font-noto-serif-cjk-jp font-noto-sans-cjk-jp

# 2. Python packages
python3 -m pip install markdown pykakasi pdfplumber pypdf pdfminer.six mutagen

# 3. Clone — 40 MB, no binaries
git clone https://github.com/feiluvnana/JLPT.git jlpt && cd jlpt

# 4. Verify
make check
```

The clone carries no audio and no `refs/`; both are fetched on demand
([below](#binaries-live-in-releases)).

### Binaries live in Releases

Nothing large is in git — Git LFS was removed on 2026-08-24 after the archive
exhausted the account's LFS budget, at which point the LFS API refuses *every*
object, `actions/checkout` fails outright, and no CI deploy runs at all.
Two GitHub Releases hold it instead, and `AGENTS.md` §3 owns the rules:

| Release | Assets | Size |
| --- | --- | --- |
| `audio` | one `<test_id>.mp3` per test | ~0.6 GB total |
| `refs` | one zip per `refs/` folder (`JLPT_N2_NEW.zip`, `Shinkanzen.zip`, …; `logs/upload_manifest.json` lists them) | ~2.6 GB total |

```bash
# a single test's listening audio
gh release download audio -p '20260821_1.mp3' -O 'tests/20260821_1/聴解.mp3'

# one source's refs tree (past papers / Shin Kanzen / 総まとめ)
gh release download refs -p 'Shinkanzen.zip' -D /tmp && unzip -n /tmp/Shinkanzen.zip -d refs/

# push new or changed binaries back (uploads only what changed)
make upload-files TARGET=all
```

What git DOES carry is the part the pipeline actually reads — the `*.md`
extracts (`booklet.md`, `script.md`, `key.md`, `audio_inspection.md`, the
textbook reference extracts) plus `answer_keys.json`, 3.7 MB in all. So a clone
with no archive still runs every `make` target and passes `make check`, which
`skip`s the archive-only checks and says so. You need the binaries only to
re-run `make extract-*`, read a PDF page directly, or listen to official audio.

---

## Setup — Windows

### Recommended: WSL2 + Ubuntu

Everything behaves exactly as it does on macOS, and you avoid the native
Windows incompatibilities listed under [Native Windows](#native-windows-git-bashmsys2).

```powershell
wsl --install -d Ubuntu     # then reboot and open Ubuntu
```

```bash
# Inside Ubuntu
sudo apt update
sudo apt install -y python3 python3-pip make ffmpeg git gh nodejs \
                    poppler-utils fonts-noto-cjk
pip install markdown pykakasi pdfplumber pypdf pdfminer.six mutagen

# CRLF must stay off — see Troubleshooting
git config --global core.autocrlf false

git clone <repo-url> ~/jlpt && cd ~/jlpt
make check
```

⚠️ **Clone into the WSL filesystem (`~/jlpt`), not `/mnt/c/...`.** Cross-OS
file I/O against the (optional, 2.6 GB) `refs/` tree is dramatically slower.

To open the exam in your normal Windows browser, run `make serve` in WSL and
visit <http://127.0.0.1:8765> — WSL2 forwards localhost automatically.

### Native Windows (Git Bash/MSYS2)

Workable, but one thing in the repo assumes a Unix host today:

- **The `Makefile` hardcodes `python3`.** The python.org installer only creates
   `python.exe` / `py.exe`; `python3.exe` exists in the Microsoft Store build.
   Either use the Store build, or add a `python3` shim, or call the scripts
   directly (`python .agents/exam-app/scripts/build_interactive.py tests/<id>`).

Then:

```powershell
winget install Python.Python.3.12 Git.Git GitHub.cli Gyan.FFmpeg OpenJS.NodeJS.LTS
winget install ezwinports.make        # or use MSYS2 / choco install make
```

- **Fonts** — download **Noto Serif CJK JP** and **Noto Sans CJK JP** from
  <https://github.com/notofonts/noto-cjk/releases>, then right-click →
  *Install for all users*. (`Yu Gothic`, already on Windows, covers the app UI.)
- **Symlinks** — enable **Developer Mode** (Settings → System → For developers),
  then `git config --global core.symlinks true`, **before cloning**. Without it
  the 10 files under `.claude/skills/` check out as text stubs containing a path,
  the skills stop resolving, and `make check` fails
  `every skill is symlinked under .claude/skills/`.
- **Console encoding** — set `PYTHONUTF8=1`. `make check` prints Japanese
  filenames (`聴解.mp3`), and the Windows console code page (cp1252/cp932)
  raises `UnicodeEncodeError` on them. (File I/O itself is safe: every one of
  the repo's ~112 `read_text`/`write_text` calls passes `encoding=` explicitly.)

Then run the same Python-package and clone steps as macOS, in Git Bash.

### Not available on Windows — and not needed

`tools/extract_jlpt_n2_new.py` builds a Swift + Vision OCR helper only when
`sys.platform == "darwin"`, so `script.md`'s OCR layer can't be regenerated off
a Mac. This costs you nothing: every extract is already committed, so you
never need to re-run `make extract-archive`.

---

## Verify your install

```bash
python3 --version                              # ≥ 3.10
python3 -c "import markdown, pykakasi, pdfplumber, pypdf, pdfminer; print('py deps ok')"
ffmpeg -version | head -1 && ffprobe -version | head -1
gh auth status | head -2                        # for the audio/refs Releases
make check                                     # read EVERY line, including WARN
```

`make check` is the read-only gate (`tools/check_consistency.py`). Every check
in it exists because that exact inconsistency shipped broken at least once, and
each failure message *is* its own documentation — it names the rule, the
incident, and the repair. **A FAIL blocks the work; a WARN must be resolved or
explicitly justified.** Green is the floor, not a verdict on a paper's content.

---

## Everyday commands

`make help` prints the full list; **`AGENTS.md` §4 is the authoritative router**
(it maps every target to the skill that documents it). The short version:

```bash
make serve            # ONE server for every test → http://127.0.0.1:8765 (no test id)
make sheet <id>       # rebuild 解答.html + 練習.html (exam + practice mode)
make booklet <id>     # rebuild both booklet HTMLs
make mp3 <id> REPLAY=1  # re-render 聴解 from its recorded draw (SEED=n = a NEW draw)
make grade <id>       # CLI grading → 採点結果.json
make knowledge        # rebuild the 知識 (knowledge) pages → knowledge/<LEVEL>/ (LEVEL=N2)
make drill            # rebuild the ドリル (drill) pages → drill/<LEVEL>/ (after any test / clip-bank change)
make check            # the gate
make pages            # static GitHub Pages build → _site/
```

Per-test targets take the id positionally (`make sheet 20260917_1`) or as
`TEST=…`; always pass one. `make serve` takes no id — one server covers every test.

### Levels

A test's folder name says its level: bare ids are N2 (`20260917_1`), every
other level carries a prefix (`n1-20261005_1`), and imports name it in the slug
(`imported-n1-2025-12`). Per-test commands need nothing more — `make sheet
n1-20261005_1` grades and titles it as N1. The archive commands take `LEVEL=`
(default `N2`):

```bash
make levels                         # every level: scaffold / structured / calibrated, and what is missing
make extract-archive LEVEL=N1       # refs/JLPT_N1_NEW/*/ -> booklet.md, script.md, audio_inspection.md
make extract-keys LEVEL=N1          # that level's answer-key PDF -> key.md + answer_keys.json
make goi-profile LEVEL=N1 BASELINE=1
```

The test list shows each test's level and has an N1–N5 switcher; a level with
no test yet is shown greyed out.

### Adding a level

Each level has a structure table,
`.agents/jlpt-exam-structure/references/levels/<LEVEL>.json`. Everything that
depends on the level reads it: the grader, the answer sheet, the model answer,
the test list, the sampler, the 聴解 composer, the profilers and `make check`.
`N1.json` is already there as a scaffold. For N1 (or `python3
.agents/jlpt-exam-structure/scripts/level.py --scaffold N3` to start another):

1. **Add the archive** under `refs/JLPT_N1_NEW/`, laid out like
   `refs/JLPT_N2_NEW/` (one folder per sitting: booklet PDF, script PDF, MP3,
   plus the answer-key PDF at the top), then run `make extract-archive LEVEL=N1`
   and `make extract-keys LEVEL=N1`. Upload it with `make upload-files
   TARGET=refs`; it becomes `JLPT_N1_NEW.zip` on the `refs` release.
2. **Fill the structure** in `N1.json`. Take `scoring` and `timing` from
   jlpt.jp, and `gengo`/`choukai` (the 大問 list, with one shapes row per era)
   from the extracted `booklet.md`/`key.md`. Then set `"status": "structured"`.
   At that point N1 past papers can be imported (`make init-import
   SLUG=n1-2025-12`), rendered, served and graded, and `make check` runs the
   structural contracts on them and visibly skips the rest.
3. **Calibrate** to reach `"status": "calibrated"`. This is content work, not
   plumbing: teach the three profilers N1's 大問 numbering and take the founding
   measurement with `BASELINE=1`. Build `pools/N1.json` from the N1 textbook
   volumes; keep their extracts under `refs/<Book>/N1/` so they don't collide
   with N2's. Write N1's bands in the question-authoring references, and
   re-measure the sampler's `DRAW`/target rates. Once N1 is calibrated, `make
   sample n1-<date>_1` and `make mp3` stop refusing it, and N1's items and
   聴解 clips go to their own `logs/N1/` ledger, bank and draw record.

Every number in a table is an official jlpt.jp fact or a measurement of that
level's own archive. None is carried over from N2 (`AGENTS.md` §4). `make
check` fails any test whose level is still a scaffold, so a new level can't
pass the gate just because it has nothing in it.

Still open: whether an N1 paper should also avoid 読解/聴解 subjects an N2
paper used. `logs/topics.json` is shared across levels for now, and the item
ledgers are separate.

### Taking a test

```bash
make serve
```

Opens the test list; pick a test, answer every item with the 聴解 audio
playing in-page, submit, and the result screen scores it out of 180 with
per-section pass/fail. Answers land in `ユーザー解答.json`, the result in
`採点結果.json`.

Each test also opens in **練習モード** — the button under 開始する on the first
screen. Same paper, every question on one page, no clock and no score, and a
「解説を見る」 button per question that shows that item's model answer and
explanation (Japanese or Vietnamese). Nothing is saved in practice mode; use the
exam mode when you want the sitting on record.

### Generating a new mock exam

Don't improvise it — copy the prompt in **`GENERATE.md`** to an agent. It runs
five stages as separate subagents: blueprint (seeded pool draw) → 3 parallel
authoring sections (文字・語彙 / 文法 / 読解) → build + gate (the 聴解 half is
composed from real recordings here) → fresh-eyes QA → model answer (Japanese
and Vietnamese, written separately).

### Importing a real past paper

Copy the prompt in **`IMPORT.md`**. Imported tests live in
`tests/imported-<slug>/`, where the `imported-` prefix marks a folder as
external and the slug starts with the level (`imported-n2-2025-12`).

### Publishing

`make pages` builds a static, server-free twin of the app into `_site/`
(answers kept in `localStorage`); `make preview-pages` serves it on
<http://127.0.0.1:8766>. Pushing to `master` deploys it via
`.github/workflows/pages.yml` — enable it once in **Settings → Pages → Source:
GitHub Actions**. `_site/` is a build artifact: gitignored, never committed.

---

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `make check` fails **`built HTML matches the Markdown it stamps`** on a clean checkout | CRLF. There is no `.gitattributes`, and Git for Windows defaults to `core.autocrlf=true`, so line endings change the source hash the HTML stamps. `git config --global core.autocrlf false`, then re-clone. |
| `make check` fails **`every skill is symlinked under .claude/skills/`** | Symlinks checked out as text stubs. Enable Developer Mode + `core.symlinks true`, then re-clone. |
| `UnicodeEncodeError` while printing 聴解 / 解答 filenames | Windows console code page. `set PYTHONUTF8=1`. |
| `make mp3` fails immediately | `ffmpeg`/`ffprobe` not on `PATH`, `SEED=`/`REPLAY=1` missing, or `refs/JLPT_N2_NEW/` absent (archive clips read from it — `choukai-audio` Part 0). |
| `聴解.mp3` fails the gate as built from a superseded script | The bank or composer changed after the audio. `make mp3 <id> REPLAY=1` re-renders the recorded draw — never a seeded re-run, which re-draws the paper. |
| Booklet renders Japanese in the wrong typeface | Noto Serif/Sans CJK JP not installed — the CSS falls back to a generic `serif`. |
| `refs/` PDFs/MP3s are missing entirely | Expected on a fresh clone — the archive is gitignored and lives in the `refs` release ([Binaries live in Releases](#binaries-live-in-releases)). The `*.md` extracts beside them are tracked and enough for most work. |
| `tests/*/聴解.mp3` is missing and the player shows nothing | The clone has no binaries. Either `gh release download audio -p '<id>.mp3' -O 'tests/<id>/聴解.mp3'`, or just take the test online — the deployed sheet falls back to the `audio` release URL. |
| A `make extract-*` or PDF read fails on a missing `refs/` file | Fetch that source's zip: `gh release download refs -p 'JLPT_N2_NEW.zip' -D /tmp && unzip -n /tmp/JLPT_N2_NEW.zip -d refs/`. Never re-source or re-commit the archive. |
| `make upload-files` dies on `HTTP 404: Not Found (…/releases/assets/<id>)` | The active `gh` account cannot write to this repo — GitHub returns 404, not 403, for an unauthorized asset overwrite. `gh auth status` shows who is active; `gh auth switch --user <owner>` picks the account that owns the repo. |
| `make check` fails `no exam MP3 is tracked in git` | A `聴解.mp3` is still in the index from before the MP3s were gitignored. `git rm --cached -- 'tests/*/聴解.mp3'` untracks them; the files stay on disk. |
| `make check` fails `exam MP3(s) are on the `audio` release` | Those MP3s were composed but never uploaded, and git no longer carries them — run `make upload-files` and commit `logs/upload_manifest.json`. |
| `This repository exceeded its LFS budget` | You are on a pre-2026-08-24 clone. LFS is gone: there is no `.gitattributes`, and `refs/**/*.{pdf,mp3}` plus `tests/**/*.mp3` are gitignored. Never re-add an LFS rule — an exhausted budget makes checkout itself fail. |
| `skip grader parity — node not installed` | Expected. Install Node.js to enable that check. |

---

## Third-party data

- Pitch accent (knowledge module): UniDic 3.1.1 + Open JTalk 1.11 dictionary,
  BSD-3-Clause — `.agents/jlpt-knowledge/references/pitch/`.

---

## Contributing (and for agents)

**Read `AGENTS.md` end to end before your first change** — start with §0, the
read-everything-first compliance rule. Every defect this repo has shipped came
from skipping a rule that was already written down, not from a hard problem.

Then: run `make check` and read every line before reporting anything as done,
and put content changes through the `exam-qa-review` pass in a context that
did not author them.
