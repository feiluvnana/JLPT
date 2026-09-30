# Makefile for the JLPT Mock Exam Pipeline (N1–N5; N2 calibrated)

.PHONY: assemble help check check-tests goi-profile dokkai-profile choukai-profile grade sheet practice model-answer explanation keyless serve pages preview-pages booklet mp3 sample \
       levels init-import extract-pdf extract-archive extract-keys extract-kanji-tables extract-shinkanzen-goi extract-shinkanzen-dokkai extract-shinkanzen \
       lint-draft lint verify-scramble scaffold-explanations \
       scaffold-sections matrix qa-eval autofix findings repair-plan choukai-bank \
       textbook-bank archive-bank number-calls choukai-wear knowledge

# Positional test-id argument: "make grade 1", "make sheet 2", "make sample 5".
# Equivalent: "make grade TEST=1". `serve` is deliberately NOT here: one server
# covers every test, so it takes no id. `pages` builds every test by default;
# "make pages 1" (or TEST=1) narrows it to one.
TARGET_CMDS := assemble grade sheet practice model-answer explanation keyless booklet mp3 pages sample lint-draft lint verify-scramble scaffold-explanations scaffold-sections matrix qa-eval autofix repair-plan upload-files
FIRST_GOAL   := $(firstword $(MAKECMDGOALS))

ifneq ($(filter $(FIRST_GOAL),$(TARGET_CMDS)),)
  POS_ARG := $(word 2,$(MAKECMDGOALS))
  ifneq ($(POS_ARG),)
    # Define dummy target for positional argument so make does not fail with 'No rule to make target'
    $(eval $(POS_ARG):;@:)
  endif
endif

TEST ?= $(POS_ARG)
# A per-test target with no id used to fall back to TEST=1: `make sample SEED=n`
# then created tests/1/ and a ledger row for it, and `make mp3 SEED=n` composed
# into it. No default — name the paper (2026-09-28).
PER_TEST_CMDS := $(filter-out pages repair-plan upload-files matrix,$(TARGET_CMDS))
ifneq ($(filter $(PER_TEST_CMDS),$(MAKECMDGOALS)),)
  ifeq ($(strip $(TEST)),)
    $(error name the test: make $(FIRST_GOAL) <test_id>  (or TEST=<test_id>))
  endif
  ifeq ($(filter sample,$(MAKECMDGOALS)),)
    ifeq ($(wildcard tests/$(TEST)/.),)
      $(error no such test folder: tests/$(TEST)/)
    endif
  endif
endif
TARGET ?= tests
# No default seed on purpose: the seed must be an RNG output passed explicitly
# (SEED=$$(python3 -c "import secrets; print(secrets.randbelow(10**8))")),
# never a hand-picked or remembered number — see exam-blueprint/SKILL.md.
SEED ?=
SLUG ?=
# Exam level for the archive targets (extract-archive/-keys, *-profile). A test
# id already names its own level (n1-… / imported-n1-…; bare = N2), so the
# per-test targets need nothing. See `make levels`.
LEVEL ?= N2
# Explanation language for `make scaffold-explanations`. `ja` scaffolds
# 詳細解説.json (stems, options, passages pre-filled); any other language in the
# registry (.agents/exam-model-answer/references/languages/index.json) scaffolds
# an EMPTY 詳細解説.<lang>.json — that set is written from the items, never
# translated from the Japanese one (exam-model-answer).
#
# LANG is also the LOCALE environment variable, so `LANG ?= ja` inherited the
# shell's C.UTF-8 and a bare `make scaffold-explanations <id>` wrote
# 詳細解説.c.utf-8.json (2026-08-26). Honour LANG only when given on the
# command line; the environment's locale is never a language choice.
ifeq ($(origin LANG),command line)
EXPL_LANG := $(LANG)
else
EXPL_LANG := ja
endif
# GitHub Pages build output. Gitignored: CI builds it, nothing commits it.
SITE ?= _site
PAGES_PORT ?= 8766
# pages narrows to one test only when an id was given explicitly (positional or
# TEST= on the command line); a bare `make pages` builds all tests.
PAGES_TEST = $(if $(POS_ARG),$(POS_ARG),$(if $(filter command line,$(origin TEST)),$(TEST),))
UPLOAD_TEST = $(if $(POS_ARG),$(POS_ARG),$(if $(filter command line,$(origin TEST)),$(TEST),all))

help:
	@echo "=========================================================================="
	@echo "                        JLPT Mock Exam Commands                           "
	@echo "=========================================================================="
	@echo "  make check            Verify docs/code/tests consistency (read-only)"
	@echo "  make check-tests      Same gate, per-test contracts only (skips doc/code checks)"
	@echo "  make sample 5 SEED=n  Sample question pool -> tests/5/test_spec.json + ledger"
	@echo "                        (SEED required, from an RNG: python3 -c 'import secrets; print(secrets.randbelow(10**8))')"
	@echo "  make scaffold-sections 1 Scaffold section authoring templates into tests/1/_sections/"
	@echo "  make assemble 1        Merge tests/1/_sections/ into 言語知識・読解.md in the official layout"
	@echo "  make matrix           2x2 Cartesian matrix generator for 問題1 & 問題2"
	@echo "  make booklet 1        Build booklet HTML for test 1 (言語知識・読解.html & 聴解.html)"
	@echo "  make mp3 1 SEED=n     Compose listening audio for test 1 from official clips (聴解.mp3)"
	@echo "  make choukai-bank     Rebuild logs/choukai_bank.json (official sittings + textbook items)"
	@echo "  make textbook-bank    Measure/validate the Shin Kanzen + Soumatome half of the bank"
	@echo "  make archive-bank     Measure/validate the refs/JLPT_N2_NEW/ half of the bank [SCOUT=YYYY-MM]"
	@echo "  make number-calls     Re-harvest the 11 official 「N番。」 clips textbook items are given"
	@echo "  make choukai-wear     Measure how hard the clip pool is mined (sets TEXTBOOK_SLOTS)"
	@echo "  make sheet 1          Build BOTH modes of test 1: 解答.html (exam) + 練習.html (practice)"
	@echo "  make practice 1       Rebuild only the practice page for test 1 (練習.html)"
	@echo "  make model-answer 1   Build model answer & explanation for test 1 (模範解答.html)"
	@echo "  make explanation 1    Alias for make model-answer"
	@echo "  make scaffold-explanations 1 Scaffold explanation JSON template directly from markdown"
	@echo "  make scaffold-explanations 1 LANG=vi  Scaffold the Vietnamese explanation set (詳細解説.vi.json)"
	@echo "  make lint-draft 1     Fast pre-linter for contractions, reaction turns, abs-quantifiers"
	@echo "  make autofix 1        Auto-fix conversational contractions and stem formatting"
	@echo "  make lint 1           Alias for make lint-draft"
	@echo "  make verify-scramble 1 Permutation & topological validator for 問題8 scrambles"
	@echo "  make qa-eval 1        Structured blind-solve evaluator & QA report generator"
	@echo "  make keyless 1        Blind-solve render for QA: qa/1/keyless.md (no keys)"
	@echo "  make serve            Serve ALL tests: levels -> modules -> list -> exam (no id)"
	@echo "  make grade 1          Grade test 1 (reads tests/1/ユーザー解答*.json)"
	@echo "  make knowledge [LEVEL=N2]  Build the knowledge module: knowledge/<LEVEL>/<category>.html + index.html"
	@echo "  make pages            Build the static GitHub Pages site into _site/ (all tests)"
	@echo "  make pages 1          Same, only test 1"
	@echo "  make preview-pages    Serve _site/ locally to check the Pages build"
	@echo "  make init-import SLUG=n2-2025-12   Scaffold tests/imported-<slug>/"
	@echo "  make extract-pdf PDF=a.pdf OUT=tests/imported-x/_extract/a.txt"
	@echo "  make extract-archive  refs/JLPT_<LEVEL>_NEW/*/ -> booklet.md script.md audio_inspection.md [LEVEL=N2]"
	@echo "  make extract-keys     Answer-key PDF -> per-exam key.md + answer_keys.json [LEVEL=N2]"
	@echo "  make levels           Each JLPT level's status (scaffold/structured/calibrated) and what is missing"
	@echo "  make extract-kanji-tables   Shin Kanzen N2-漢字 別冊1 -> refs/Shinkanzen/kanji_tables.md"
	@echo "  make extract-shinkanzen-goi Shin Kanzen + Soumatome N2 語彙 -> refs/*/goi_reference.md"
	@echo "  make extract-shinkanzen-dokkai Shin Kanzen N2 読解 -> refs/Shinkanzen/dokkai_reference.md"
	@echo "  make extract-shinkanzen       Shin Kanzen N2 聴解 別冊 -> refs/Shinkanzen/choukai_script.md"
	@echo "  make goi-profile [BASELINE=1]  文字・語彙 measurement: archive vs tests (--baseline for the doc tables)"
	@echo "  make dokkai-profile [BASELINE=1] 読解 measurement: archive vs tests (--baseline for the doc tables)"
	@echo "  make choukai-profile [BASELINE=1] 聴解 measurement: archive vs tests (--baseline for the doc tables)"
	@echo "  make findings         Gate in --json mode -> logs/findings.json (slug/tier per finding)"
	@echo "  make repair-plan [1] [TIER=B] 聴解+読解 work order -> qa/[<id>/]repair-plan.{json,md}"
	@echo "  (any per-test target also takes TEST=<id>; there is no default id)"
	@echo "=========================================================================="

check:
	python3 tools/check_consistency.py

check-tests:
	python3 tools/check_consistency.py --tests

goi-profile:
	python3 tools/goi_profile.py --level $(LEVEL) $(if $(BASELINE),--baseline,--official --tests)

dokkai-profile:
	python3 tools/dokkai_profile.py --level $(LEVEL) $(if $(BASELINE),--baseline,--official --tests)

choukai-profile:
	python3 tools/choukai_profile.py --level $(LEVEL) $(if $(BASELINE),--baseline,--official --tests)

# Every level's status and what it is still missing (levels/<LEVEL>.json).
levels:
	python3 .agents/jlpt-exam-structure/scripts/level.py

# The 聴解 work order: findings -> tier -> the batch that must land before a rebuild.
# `findings` is the gate in --json mode, so no number is recomputed (REPORT-CHOUKAI.md §5.0).
# `-` on purpose: this target EMITS findings, it does not gate. A red gate is the
# normal state mid-repair (a script edit makes its MP3 stale until the rebuild
# batch runs), and that is exactly when the work order is needed. `make check` is
# the gate; this is its data feed.
findings:
	-python3 tools/check_consistency.py --json logs/findings.json

repair-plan: findings
	python3 tools/choukai_repair_plan.py $(TEST) $(if $(TIER),--tier $(TIER),)

extract-shinkanzen:
	python3 tools/extract_shinkanzen_choukai.py

sample:
	@test -n "$(SEED)" || (echo 'usage: make sample <id> SEED=$$(python3 -c "import secrets; print(secrets.randbelow(10**8))")'; \
	  echo 'the seed must be an RNG output, never a number an agent picked (exam-blueprint/SKILL.md)'; exit 1)
	python3 .agents/exam-blueprint/scripts/sample_items.py --seed $(SEED) --test-id $(TEST)

scaffold-sections:
	python3 tools/scaffold_sections.py tests/$(TEST)

matrix:
	python3 tools/matrix_helper.py --help

booklet:
	python3 .agents/exam-app/scripts/build_booklet.py tests/$(TEST)/言語知識・読解.md tests/$(TEST)/聴解.md

# `make mp3` composes the whole listening half out of banked clips (a NEW draw:
# script, booklet, MP3, chapters and both 詳細解説 panes' 聴解 entries). SEED must
# be an RNG output, never a number you chose. `REPLAY=1` re-renders the paper's
# RECORDED draw instead — the only safe rebuild after a bank or renderer fix;
# add NO_AUDIO=1 to rewrite the text deliverables and keep the MP3.
mp3:
ifdef REPLAY
	python3 tools/compose_choukai.py $(TEST) --replay $(if $(NO_AUDIO),--no-audio,)
else
	@test -n "$(SEED)" || { echo "SEED= is required for a new draw: SEED=\$$(python3 -c 'import secrets;print(secrets.randbelow(10**8))') — or REPLAY=1 to re-render the recorded one"; exit 1; }
	python3 tools/compose_choukai.py $(TEST) --seed $(SEED)
endif

# One writer for logs/choukai_bank.json: this target builds BOTH halves — the
# official records from the ten imports, then the textbook records
# build_textbook_bank.py measures out of the Shin Kanzen / Soumatome CDs.
choukai-bank:
	python3 tools/build_choukai_bank.py $(if $(CHECK),--check,)

# Report-only: what the textbook half measures, and which declared items the
# duration/rate guards refuse. Writes nothing — `make choukai-bank` does.
textbook-bank:
	python3 tools/build_textbook_bank.py

# The same, for the hand-declared items cut out of the 21 un-imported sittings
# of refs/JLPT_N2_NEW/ (archive_bank_expansion.md, route C). Report-only.
# SCOUT=YYYY-MM prints that sitting's structural pause map instead, which is how
# a declaration's `window` bracket is found — never by guessing at a timestamp.
archive-bank:
	python3 tools/build_archive_bank.py $(if $(SCOUT),--scout $(SCOUT),)

# The 11 official 「N番。」 spans a textbook clip is given, since textbook tracks
# speak no number call. CHECK=1 re-harvests and diffs against the file on disk.
# How many papers spend each clip, measured and projected, per 大問 and per
# source. This is what `compose_choukai.TEXTBOOK_SLOTS` is set FROM: it exits
# non-zero when a slot count projects more than WEAR_CEILING uses per textbook
# clip, and the repair is to grow the pool, never to keep the number.
choukai-wear:
	python3 tools/choukai_wear.py

number-calls:
	python3 tools/harvest_number_calls.py $(if $(CHECK),--check,)

# Writes BOTH modes of the paper: 解答.html (the timed, graded sitting) and
# 練習.html (練習モード — no clock, no grading, per-question model answers). One
# command on purpose: the sitting's 開始する gate links to the practice page, and
# two commands would let that link open a page built from a superseded booklet.
sheet:
	python3 .agents/exam-app/scripts/build_interactive.py tests/$(TEST)

# Just the practice page — for re-rendering after 詳細解説.json changes, which is
# the one source it has that 解答.html does not.
# Stage 3: merge the three _sections/ fragments into 言語知識・読解.md in the
# official layout (banners, canonical 問題N lines, one key heading). Refuses a
# fragment that still holds scaffold placeholders.
assemble:
	python3 tools/assemble_paper.py tests/$(TEST)

practice:
	python3 .agents/exam-app/scripts/build_practice.py tests/$(TEST)

# 練習.html embeds the same 詳細解説 files, so the two are always rebuilt together
# — building one alone left the other stale and reddened the final `make check`.
model-answer:
	python3 .agents/exam-model-answer/scripts/build_model_answer.py tests/$(TEST)
	python3 .agents/exam-app/scripts/build_practice.py tests/$(TEST)

explanation: model-answer

scaffold-explanations:
	python3 tools/scaffold_explanations.py tests/$(TEST) --lang $(EXPL_LANG)

lint-draft:
	python3 tools/lint_draft.py tests/$(TEST)

autofix:
	python3 tools/lint_draft.py tests/$(TEST) --fix

lint: lint-draft

verify-scramble:
	python3 tools/verify_scramble.py tests/$(TEST)


qa-eval:
	python3 tools/qa_eval.py tests/$(TEST) --scaffold-report

# The QA blind-solve render: the same paper with the keys truncated away, into
# qa/<id>/keyless.md. Not a deliverable — tests/<id>/ has a fixed file contract.
keyless:
	python3 .agents/exam-app/scripts/build_interactive.py tests/$(TEST) --keyless

serve:
	python3 .agents/exam-app/scripts/serve_sheet.py

# The knowledge module (jlpt-knowledge): every category page of the level + its index,
# built from knowledge/<LEVEL>/*.json. Re-run after any knowledge JSON edit; the gate
# fails a page whose src_sha stamps no longer match its data.
knowledge:
	python3 .agents/jlpt-knowledge/scripts/build_knowledge.py --level $(LEVEL)

grade:
	python3 .agents/exam-app/scripts/grade_answers.py --test-dir tests/$(TEST)

# The static twin of `make serve`: same three screens, answers kept in the
# browser's localStorage because GitHub Pages has no server and no disk.
pages:
	python3 .agents/exam-app/scripts/build_pages.py $(PAGES_TEST) --out $(SITE) $(PAGES_FLAGS)

preview-pages:
	@test -d $(SITE) || (echo "no $(SITE)/ — run make pages first"; exit 1)
	python3 -m http.server -d $(SITE) $(PAGES_PORT)

init-import:
	@test -n "$(SLUG)" || (echo "usage: make init-import SLUG=n2-2025-12"; exit 1)
	python3 .agents/external-test-import/scripts/init_imported_test.py --slug $(SLUG)

extract-pdf:
	@test -n "$(PDF)" && test -n "$(OUT)" || (echo "usage: make extract-pdf PDF=a.pdf OUT=out.txt"; exit 1)
	python3 .agents/external-test-import/scripts/extract_pdf_text.py "$(PDF)" -o "$(OUT)"

# Turn the refs/JLPT_N2_NEW/ past-paper archive into agent-readable Markdown.
# Read-only with respect to the PDFs/MP3s; writes only the .md/.json beside them.
extract-archive:
	python3 tools/extract_jlpt_n2_new.py --all --level $(LEVEL)

extract-keys:
	python3 tools/extract_jlpt_n2_key.py --level $(LEVEL)

extract-kanji-tables:
	python3 tools/extract_kanji_tables.py

extract-shinkanzen-goi:
	python3 tools/extract_shinkanzen_goi.py

extract-hajimete:
	python3 tools/extract_hajimete.py

extract-shinkanzen-dokkai:
	python3 tools/extract_shinkanzen_dokkai.py

upload-files:
	python3 tools/upload_files.py $(TARGET) $(UPLOAD_TEST)


