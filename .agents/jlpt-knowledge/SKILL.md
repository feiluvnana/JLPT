---
name: jlpt-knowledge
description: Single owner of the knowledge module (知識) — the per-level study material that sits beside the exam module (試験) and the drill module (ドリル) in the portal: grammar lists (文法リスト), vocabulary lists (単語 / 語彙), kanji (漢字), and 読解/聴解 strategy guides (読解のコツ, 聴解のコツ), each as searchable study cards plus a per-card self-check quiz, with progress kept per browser. Owns the data schema under knowledge/<LEVEL>/, the builder (make knowledge), the gate checks, and the rules for authoring knowledge content from refs/ with original example sentences and independently written per-language prose. Use whenever the user wants to study or learn N2 grammar, vocabulary or kanji, build or fix a knowledge page, add knowledge entries or a new category or level, or asks about 知識 / 文法リスト / 単語 / 語彙 / 漢字 / 読解のコツ / 聴解のコツ / vocabulary list / grammar list content. Not for ドリル (大問別練習, 聴解トレーニング, 復習ノート, 進捗ダッシュボード, 読解ライブラリ) — that is a separate module under drill/<LEVEL>/.
---

# JLPT Knowledge Module (知識)

The exam module (試験) is a paper you sit; the knowledge module (知識) is what
you study between papers; the drill module (ドリル, `drill/<LEVEL>/`, a separate
module not owned here) is where you practise by question type. Per level, one page per **category**, each with two tabs:

- **学習** — every entry as a card: the shared Japanese material (headword,
  reading, 接続/品詞/音訓, original examples, citations, related links) and the
  prose in the reader's language. Search, filters (課/topic, tag, tested in an
  official sitting, 覚えた status), sort by official frequency, cards rendered 50
  at a time as the reader scrolls.
- **クイズ** — the category's authored quiz items, shuffled, over a chosen subset
  (one 課/topic, only unlearned entries, only last time's misses; 10/20/50/all);
  per-item verdict with that language's explanation, a session score, retry.

URLs (the portal owns `/` and `/<LEVEL>/`, `exam-app`): `knowledge/<LEVEL>/index.html`
(category index, back link `../../<LEVEL>/index.html`) and `knowledge/<LEVEL>/<stem>.html`
(back link `index.html`) — for a split category that page lists the parts, and
the cards are on `knowledge/<LEVEL>/<stem>/<part>.html` (back link `../<stem>.html`). Every link is relative and names a file, so the pages
work from `make serve`, a Pages subpath and disk alike; each page embeds its data,
because the Pages build copies only the `*.html`. Anything that counts entries
(the portal) calls `knowledge_data.summary(level)`, which knows both layouts.

## Categories

`references/categories.json` is the ONE list, per level — stem, kind, label keys,
which shared fields form the card head, and the per-entry example/quiz counts.
N2 today; every other level is `[]` (no knowledge module yet).

| stem | kind | head fields | examples | quiz |
| - | - | - | - | - |
| `文法` | item | `pattern`, `reading`, `connection` | 3 | 2 |
| `語彙` | item | `word`, `reading`, `pos` | 1–3 | 0–2 |
| `漢字` | item | `kanji`, `on`[], `kun`[], `words`[] | 0–2 | 0–2 |
| `読解` | guide | — | 0–6 | 0–3 |
| `聴解` | guide | — | 0–6 | 0–3 |

The JSON is the owner of those counts; the table is a reading aid.

## Files

Under `knowledge/<LEVEL>/`, tracked in git like `tests/`. Per category, ONE of two
layouts (both at once is a FAIL):

```
<stem>.json              shared Japanese material — the one copy, printed in every pane
<stem>.<code>.json       ONE language's prose, for EVERY language, primary included
<stem>/<part>.json       split layout: the same pair once per part — use it when one
<stem>/<part>.<code>.json   file gets large (語彙's 2,500 words: one part per 課/topic)
<stem>.html, index.html  built by `make knowledge` — never edit by hand
<stem>/<part>.html       split layout only: one card page per part, also built
```

`<part>` has no `.`; parts load in name order (`01`, `02`, …). Ids are unique
across the whole category, so `related` crosses parts. Language codes come from
the registry (`exam-model-answer/references/languages/`, `langs.py`): a file for
a code not in `order` is ignored and WARNs.

## Schemas

**Shared file** (`<stem>.json` / `<part>.json`):
`{"category": <stem>, "level": <LEVEL>, "kind": item|guide, "part"?: str, "entries": [...]}`.

Every entry:

| key | | |
| - | - | - |
| `id` | required | stable ascii `[a-z0-9-]`, unique in the category (`g-kanenai`, `v-0412`, `k-dai`) |
| `examples` | required | ORIGINAL Japanese sentences, furigana `｜漢字《かんじ》`; count per categories.json |
| `sources` | required, ≥1 | `{ref, page?, note?}` — `ref` a repo path that exists; `page` the PDF page |
| `related` | optional | ids in the same category |
| `quiz` | optional | `{stem, options[4], answer}`, `answer` 1-based |
| `group` | optional | the grouping label a filter and a quiz scope use: Shin Kanzen 課 (`第12課`) or topic (`時間・時期`) |
| `tags` | optional | free labels (`硬い表現`, `書き言葉`) — one filter |
| `official_count` | optional | how many official sittings in `refs/JLPT_N2_NEW/` test the point (count the `booklet.md` hits; cite one in `sources`) — badge, filter, sort |
| `pitch` | optional | an accent override you have CHECKED: `[drop, …]` for the headword reading; on a 漢字 entry `{"<word, markup stripped>": [drop, …]}` for its `words` (§Pronunciation) |

Plus the category's own head fields: 文法 `pattern`, `reading`, `connection`
(接続 in Japanese notation: `動詞ます形 ＋ かねない`); 語彙 `word`, `reading`,
`pos`; 漢字 `kanji`, `on` (katakana list), `kun` (hiragana list, okurigana after
`.`), `words` (furigana'd compounds) — at least one of `on`/`kun`. A **guide**
entry has no head fields: `id`, `sources`, `examples` (short Japanese sample
lines: a question stem, a cue phrase) and optionally `related`/`quiz`/`group`/`tags`.

**Language file** (`<stem>.<code>.json`): `{"<id>": prose}` — prose only.

- item: `meaning`, `usage`, `nuance`, `compare` (`""` allowed for `compare` when
  `related` is empty, and for `nuance`/`compare` in 語彙/漢字), `quiz` (one
  explanation per quiz item), `example_notes`? (learner languages only: one
  translation per example — like `passage_translation`, a translation of the
  SHARED Japanese, which is allowed; the primary omits it).
- guide: `title`, `body` (1–6 paragraphs), `quiz`, `example_notes`?.

A language file holding a shared key (`pattern`, `examples`, `sources`, …) is a
second copy of material with an owner — FAIL.

## Bands

Characters with furigana markup stripped. The primary language is held to the
cap; every other language to cap × its `length_factor` (meta.json).
`check_knowledge.KNOWLEDGE_BANDS` owns the numbers and the gate asserts this table.

| kind | field | cap |
| - | - | - |
| item | `meaning` | 40 |
| item | `usage` | 100 |
| item | `nuance` | 100 |
| item | `compare` | 100 |
| item | `quiz` | 80 |
| guide | `title` | 30 |
| guide | `body` | 200 |
| guide | `quiz` | 80 |

`quiz` and `body` are per element. `example_notes` is a translation and is not
capped. Aim well under the cap, as in `exam-model-answer` §Length.

## Sourcing — refs/ decides, the author writes

**refs/ decides which points exist and what they mean; the example sentences
are original.** Every entry cites where its point and its reading of it come
from (`sources`), and no sentence is copied from a textbook or a paper — write
a new one that shows the same usage. Every path in `AGENTS.md` §3 is fair game;
per category:

- 文法: `refs/Shinkanzen/Shin_Kanzen_Masuta_N2-Bunpou.pdf` (the inventory and
  its 課) plus the official booklets `refs/JLPT_N2_NEW/` (`booklet.md` per
  sitting — where a point was tested, and `official_count`).
- 語彙: `refs/Hajimete/vocab_reference.md`, `refs/Shinkanzen/goi_reference.md`,
  `refs/Soumatome/goi_reference.md`.
- 漢字: `refs/Shinkanzen/kanji_tables.md`.
- 読解 guides: `refs/Shinkanzen/dokkai_reference.md` + the archive's 読解 items.
- 聴解 guides: `refs/Shinkanzen/choukai_script.md` + `choukai-audio`'s references
  (`official_register.md`, `official_pacing.md`).

The `*.md` extracts are OCR and **secondary evidence** — open the PDF page to
verify a reading or a 接続 before it goes in (`AGENTS.md` §3: absent binary →
stop and ask). Furigana is hand-checked, never pasted from pykakasi unverified
(`exam-model-answer` lists its failure modes).

## Written, not translated

The rule `exam-model-answer` §"Two languages, two rewrites" states for 詳細解説
applies here unchanged: each language's prose is **written** for its reader from
the shared file and refs/, never translated from another language's file. Author
each language in its own context, reading the shared file and the refs — never
the other language's file. In the primary prose, furigana every kanji an N2
learner needs; in a learner language, only on the Japanese being taught.

## Quiz integrity

Four options, exactly ONE defensible answer (solve it before keying it; a
distractor that is also grammatical in the stem is a mis-key), options of
comparable length and register, and answer positions balanced across the
category (the gate WARNs outside ½–1½ × n/4). The explanation says why the key
fits and what rules the strongest distractor out — never 「文脈に合わない」.

Seven rules from the first batch's QA (`qa/qa-report-knowledge-N2-文法-B0.md`,
2026-09-30), each one because the defect shipped through a green gate:

1. **Splice every distractor** into the stem and name the words that kill it.
   A kill that rests on an unstated assumption goes INTO the stem as a clause
   (「歩いて帰る（ことはない）」 was a second answer until the stem said no taxi
   ran).
2. **No form-only keys.** ≥3 of 4 options attach grammatically to the printed
   form before the blank; at most one 接続-only elimination per item, else each
   option carries its own connector. Never argue the key by form alone.
3. **Provenance scan** before hand-off: every 10-char window of examples and
   stems against `refs/**/*.md` and `tests/imported-*`, AND against the cited
   Shin Kanzen page's numbered examples — the same scenario + predicate is a copy
   with new nouns; change the scenario.
4. **`official_count` is confirmed hit by hit** in booklet.md + the key, never
   copied from the inventory's `sittings_tested` (wrong for 8 of 20 points:
   ありがたい counted as がたい, ばかりだ as 一方だ, …).
5. **接続 and meaning copied literally** from the cited page, optional (な)/である
   included; a two-reading form (ことはない, ながら) shows THIS entry's reading in
   every example.
6. **Learner-language panes quote every Japanese word in 「」**, parenthesised
   lists included; only grammar labels (thể ます, ナ形容詞) stay bare.
7. **QA extracts stem + options only, no entry ids, shuffled**, then solves.

Added by batch-2 QA (`qa/qa-report-knowledge-N2-文法-B2.md`):

8. **Every distractor competes on the tested meaning**, and at most one per item
   dies by a pure syntax rule (three ✗ in one clause is a one-choice item). A
   kill is a meaning contradiction with a quoted stem word, or a rule printed on
   the cited page — never an invented usage restriction. The "printed form" of
   rule 2 includes any particle right before the blank.
9. **No unsourced contrastive or pragmatic claim** in any language's prose
   (「〜は謙遜に使う」, 「最も硬い」): it is on a cited page or countable in the
   archive, or it is cut.
10. **Counting**: 問題8 cards count; a hit whose keyed string is another entry's
    headword belongs to THAT entry, not this one.
11. **No example shares scene + predicate with any quiz stem in the category**,
    and a distractor the author had to defend in the report is replaced before
    hand-off.

Added by batch-1 and batch-3 QA (`qa/qa-report-knowledge-N2-文法-B1.md`, `-B3.md`):

12. **What counts as an official hit** (tightens rule 4): a 問題7/問題9 key that
    carries the form AND whose options contrast it, or a 問題8 card that holds the
    form as a unit. Never count an inflection nearly every sentence has (受身・使役
    verbs, ば/たら cards), potential/spontaneous られる, a look-alike that is a
    separate SK point, or a form printed only in a 問題8 stem. List the sittings
    counted in the author's report. (Regex counts had ukemi at 18; hand-read: 8.)
13. **Provenance covers every page that treats the point** (extends rule 3): its
    練習 items, 〔復習〕 lines, the other headwords on the same page, the IV tables
    and 第3部 cross-references — four of seven B1 copies came from a page other
    than the cited one — and every official item cited in `sources` (a quiz may
    not reuse its scenario together with one of its distractors). Pick a scenario
    SK does not use first, then the predicate.
14. **A 敬語 distractor is never a misuse natives commonly produce**
    (「社長がお越しいただき」, 二重敬語) — that is a second answer; use a form that
    does not exist (お越しする, 参られる). A distractor killed only because it
    "sounds odd" is replaced by default.
15. **A 接続 or restriction stated in any language's prose matches the cited
    page's wording**, never a paraphrase that widens or narrows it.

## Pronunciation

- **▶ speech** on every headword reading, every 漢字 `words` compound and every
  example sentence, through the browser's `speechSynthesis` (`ja-JP`; a Japanese
  voice is picked when the voices load, `voiceschanged` included). The page is
  handed the READING: `build_knowledge.speech_text()` resolves `｜漢字《かな》` /
  `漢字《かな》` to the kana at build time, so a voice cannot misread a kanji —
  which makes correct furigana on examples a pronunciation rule too. No voice, no
  API: the buttons and the ふつう/ゆっくり toggle stay hidden. No audio files.
- **Pitch accent line** over the headword kana (the high/low line with its drop
  and a particle slot, CSS borders — prints, theme-neutral). Looked up at build
  time through `scripts/pitch.py` `lookup(word, reading) -> list[int] | None`
  for the categories whose `pitch` flag is true (語彙, 漢字 `words`; 文法 is off —
  a pattern is not a lexical word). An entry's own `pitch` field overrides.
  **Never guess**: unknown is no line, and a missing or failing dataset module
  means no lines at all. A page that drew any line from the dataset prints
  `references/pitch/ATTRIBUTION.txt` in its footer. The dataset is not stamped,
  so after updating it run `make knowledge`.

## Progress (per browser)

`local_store.JLPTKnowledgeStore` (exam-app) is the only place the keys are spelled:
`jlpt-knowledge/v1/<LEVEL>/<category>/覚えた.json`, `…/クイズ履歴.json` and the
speech rate in `jlpt-knowledge/v1/設定.json` — a prefix
`JLPTStore.ids()` never lists as a test. The remembered language is the site-wide
`build_model_answer.LANG_STORE_KEY`.

## Page

`scripts/build_knowledge.py` renders every card and quiz item to HTML in Python —
furigana via `build_model_answer.apply_furigana()`, one `.lang-pane` per active
language (`langs.pane_css()`), chrome labels from `languages/<code>/knowledge.json`
— and embeds them as data. The top of every page is exam-model-answer's
`lang_ui.topbar_html()`: one sticky bar, breadcrumb level › 知識 › category (›
part), language dropdown right (`crumbs()`); no page writes its own switch; the page inserts cards lazily and filters over a
small index. A language without prose for an entry shows the primary prose under
a one-line note, and an entry with no prose still shows its shared material:
never a blank card. Each page stamps `<!-- src_sha: … -->` for every data file it
read; `make check` FAILs a stale or missing page.

Missing prose WARNs for every language, `langs.required()` or not: knowledge content
lands in batches and the page falls back, so a half-authored language is a work
item, not a broken page.

**Size decides the layout.** A page embeds the cards it shows (Pages copies only
the `*.html`), about 4 KB per fully-written entry, so a 2,500-word 語彙 on one page
would be ~11 MB. Hence the split layout builds **one page per part**:

- `<stem>/<part>.html` — the full study + quiz page over that part's entries
  only. Search, filters and the quiz run within the part; the quiz scope
  selector offers the part's groups.
- `<stem>.html` — a small list of the parts (label = the part file's `part`
  field, else its name) with entry and 覚えた counts; the category index links it
  as for any category.
- A `related` id in another part links to `<other part>.html#e-<id>`, which
  opens that page scrolled to the card; a same-part link scrolls in place.
- 覚えた and quiz history stay keyed per **category** (`JLPTKnowledgeStore` is
  given the stem, never the part), so the part list, the category index and
  every part page read one store, and moving an entry between parts loses nothing.
- Each part page stamps its own files plus every other part's shared file (the
  related links print their headwords); the list page stamps every shared file.
  The builder deletes a `<stem>/*.html` whose part is gone and the gate FAILs one
  that is left.

Size a part to a few hundred entries (≤ ~1–2 MB). A single-file category stays
one page. Search text is derived in the browser, not shipped; keep 語彙/漢字
prose short — `nuance`/`compare` may be `""` there.

## Batch workflow (adding content)

1. **Inventory** from refs/: which points, in what 課/topic, cited. N2's is
   done — `references/inventory/N2.json` (+ `N2.md`, whose "Rules for batch
   authors" section is required reading: per-section PDF page offsets,
   `count_confidence`, same-form clusters, part-prefixed `group` labels). It
   carries the batch plan per category in exam-value order; take the next
   batch that is not yet in `knowledge/N2/`, never pick points from memory.
2. **Shared + primary prose, one context**: write the batch's entries into the
   shared file and `<stem>.<primary>.json` (original examples, quiz, sources).
3. **Each learner language, its own context**: read the shared file + refs,
   write `<stem>.<code>.json`. Never open another language's prose file.
4. **Fresh-eyes QA context** (authored nothing): solve every quiz item blind,
   check each meaning/接続 against the cited page, check no example is a
   textbook sentence, check the furigana.
5. `make knowledge LEVEL=<L>`, then `make check` — read every line (§0.5).

## Adding a category or a level

- Category: add an object to the level's list in `references/categories.json`
  (a new `kind` also needs its prose keys and bands in `check_knowledge.py`), add
  its `label`/`desc` keys and any `field_<fact>` label to EVERY language's
  `knowledge.json`, create the empty shared file, `make knowledge`, `make check`.
- Level: fill that level's `categories` list, create `knowledge/<LEVEL>/`,
  `make knowledge LEVEL=<LEVEL>`. The builder, the gate and the portal read the
  level from the table — no code change.
- Language: a registry change only (`langs.py` docstring) — add
  `languages/<code>/knowledge.json` and write `<stem>.<code>.json` per category.

```bash
make knowledge                 # LEVEL=N2 by default: every category page + index.html
python3 .agents/jlpt-knowledge/scripts/check_knowledge.py    # the knowledge lines of `make check`, alone
```
