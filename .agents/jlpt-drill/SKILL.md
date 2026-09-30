---
name: jlpt-drill
description: Single owner of the drill module (ドリル) — the per-level practice tools that sit beside the exam module (試験) and the knowledge module (知識) in the portal, built on the REAL items already in the repo: 大問別練習 (question-type practice by 大問, 公式/模擬, unseen/missed filters, instant verdict + explanation), 聴解トレーニング (listening practice / shadowing on one real clip at a time — speed, ±5 s, A–B loop, script reveal), 復習ノート (mistake notebook with Leitner spaced repetition over exam, drill and 知識 quiz mistakes), 進捗 (progress dashboard: score trend, section scores vs cutoff, per-大問 accuracy, weak areas) and 読解ライブラリ (reading library: every 読解 passage with 原文/訳). Owns drill/<LEVEL>/, the pool reader, the builder (make drill), the gate checks and the JLPTDrillStore schema. Use whenever the user mentions ドリル, 大問別練習, question-type practice, 聴解トレーニング, listening practice, shadowing, 復習ノート, mistake notebook, spaced repetition, 進捗, dashboard, 読解ライブラリ or reading library, or a drill page needs building or fixing. Not for 知識 study cards (文法/語彙/漢字 lists — jlpt-knowledge) and not for sitting a timed paper (exam-app).
---

# JLPT Drill Module (ドリル)

The exam module (試験) is a paper you sit; the knowledge module (知識,
`jlpt-knowledge`) is what you study; the drill module is where you **practise on
the real items** — the same questions, recordings and explanations the exam
module already holds, cut up by question type and fed back by what you got
wrong.

## Sources — the module authors nothing

**No exam content and no explanation prose is written for this module.** Every
pool is baked out of material that already has an owner, by
`scripts/drill_data.py` (the one reader; the builder and the gate both use it):

| pool | read from | owner |
| - | - | - |
| 言語知識・読解 items | `tests/<id>/詳細解説.json` (stem/options/passage — the one copy of the exam wording) + `詳細解説.<code>.json` per language | `exam-model-answer` |
| their keys and 大問 | `grade_answers.parse_gengo_keys()` / `gengo_taxonomy(max_q, level)` — era-aware, so a 72-item 2021-07 paper files its questions correctly | `exam-app`, `jlpt-exam-structure` |
| 聴解 clips | `logs/choukai_bank.json` — script, keys, `explanation` / `explanation_<code>` (official) and `explanation[_<code>]_payload` (slot-free) | `choukai-audio` |
| where a clip plays | an official record's own `audio` offsets in its `source_test`'s `聴解.mp3`; otherwise the chapter mark of the first generated paper that drew it (`logs/choukai_draws.json` slot → `聴解_チャプター.json` 「問題N k番」, to the next mark) | `choukai-audio` |
| 知識 quiz entries | `knowledge_data` (for 復習ノート's links to a card) | `jlpt-knowledge` |
| 大問 → 知識 category | `references/knowledge_links.json` (keyed by the level table's `part`) | here |

A wrong explanation is fixed where it lives (`詳細解説*.json`, the bank record)
and the drill rebuilt — never here. Explanations render through
exam-model-answer's own `explanation_box_html()` (tags by index against the key),
passages through `format_passage_text()`, furigana through `apply_furigana()`,
the 読解 原文/訳 control through `ptext_switch_html()` + `PASSAGE_TOGGLE_*`.
A language with no prose for an item shows the primary explanation under a
one-line note, never a blank box (the gate WARNs).

**A clip the pool cannot locate is skipped and counted**, never guessed: a
slot-free (textbook) or archive record plays only through a generated paper
whose chapters cover it. N2 today: 388 playable clips (398 questions) of 393
bank items; the 5 unplayable ones were never drawn by a paper on disk.

## Ids

Item id everywhere: `<test_id>:<key>`, key as in `詳細解説.json` (`20260929_1:33`,
`imported-n2-2025-12:問1-1`). A 聴解 clip has ONE canonical id per question — the
official sitting's own, or for a clip only a generated paper plays, the first
paper in draw order that drew it; every other paper's copy is an **alias**
(`ChoukaiPool.aliases`), so an exam mistake in any sitting lands on the clip's
record. A 知識 quiz item is `知識:<LEVEL>:<category>:<entry id>#<n>`.

## Tools and pages

`drill/<LEVEL>/`, **built pages only** (a non-HTML file there FAILs: this module
holds no data) and **gitignored** — unlike `knowledge/`, every input is already
tracked (tests/, logs/choukai_bank.json, knowledge/), so `make pages` (and the
Pages CI) builds them fresh; committing ~16 MB of pages would re-add a snapshot
to history on every test or 知識 change. Unbuilt on a machine = the gate SKIPs. Every page embeds its data (Pages
copies only `*.html`), links relatively, renders its top through
`lang_ui.topbar_html()` (crumbs level › ドリル › tool, the one language
dropdown) and takes its labels from the registry's `drill` namespace
(`exam-model-answer/references/languages/<code>/drill.json`).

| page | tool |
| - | - |
| `index.html` | the five tools, pool sizes, live due / attempt counts |
| `大問別練習.html` | hub: every 大問 with its pool and your accuracy; 聴解 大問 link to 聴解トレーニング. **Resolves `?items=<id>,…`**: ids on one page → redirect there; spread over several → a list of links |
| `大問別練習/<code>.html` | one 大問 (`問1`…`問14`): filters 出典 (公式 = `imported-*` / 模擬), 未回答 / 間違い (drill attempts, then exam results), count; one item at a time, verdict + explanation on answering; `?items=…[&review=1]`, `?status=missed`, `?origin=` |
| `聴解トレーニング.html` | one clip at a time, played as its span `[start, end]` of `../../tests/<id>/聴解.mp3` with the release URL (`level.audio_release_url`) as the `error` fallback and a 「MP3を選ぶ」 picker, like the sheet's player; ▶/❚❚, restart, ±5 s, speed 0.75–1.25, A–B loop, a span-relative seek bar; answer bubbles (問題1/2 and 問題5's two-question item print their options, 問題3/4 do not — as in the booklet); script + explanation open only after every question of the clip is answered; `?items=` (canonical or alias ids), `?mondai=問題N`, `?status=` |
| `復習ノート.html` | the mistake notebook (below) |
| `進捗.html` | score trend per graded test (pass mark as a reference line), the latest sitting's section scores vs the cutoff (both from the level table's `scoring`), per-大問 accuracy across exams (`taxonomy_stats`) and drills, weak areas (< 60 % with ≥ 5 answers — the result screen's 要強化 band) linking to `大問別練習/<code>.html?status=missed` / `聴解トレーニング.html?mondai=…` and the 知識 categories of that 大問's part. Inline SVG, one series per chart, a table view under each, the dataviz reference palette |
| `読解ライブラリ.html`, `読解ライブラリ/<code>.html` | every 読解 passage (the level table's 読解 大問) grouped ONCE (by text, as 模範解答 does), shortest first, filters 出典 / length; each learner pane carries 原文/訳 (`passage_translation`), 原文 by default as on 練習.html; questions and answer + explanation revealable; a link to practise that passage's items |

**Size decides the split** (`SPLIT_LIMIT`, 3 MB): 大問別練習 and 読解ライブラリ are
one page per 大問 (the largest, 問7/問11, are ~1.3–2 MB); 聴解トレーニング is one
page (~1.9 MB). The builder prints every page's size and flags one over the limit
— split it the same way before shipping it.

## Store

`local_store.JLPTDrillStore` (exam-app) is the ONLY place its keys are spelled,
under its own prefix so `JLPTStore.ids()` never lists it:

```
jlpt-drill/v1/attempts.json  {"<itemId>": [{"t": ms, "ok": 0|1, "choice": n, "tool": "practice"|"listening"}, …]}   newest 20 kept
jlpt-drill/v1/srs.json       {"<itemId|knowledgeId>": {"box": 1..5, "due": ms, "n"?: 知識 tries seen}}
```

**It is localStorage in both deployments, `make serve` included** — a drill
answer is not a sitting and has no file on disk; every page says so. Exam
answers/results stay in JLPTStore / `tests/<id>/採点結果.json` and 知識 history in
JLPTKnowledgeStore; the drill **reads** them and copies nothing. Exam results:
under `make serve` `GET api/tests?level=` plus each graded test's
`tests/<id>/採点結果.json` (served as a file — no new endpoint); on Pages (or
anywhere that API does not answer JSON) `JLPTStore.ids()` + `result(id)`.

## 復習ノート — Leitner 1 / 3 / 7 / 14 / 30

- **Collected, not copied**: every answered-and-wrong item in an exam result,
  every drill item whose LAST attempt was wrong, every 知識 quiz item whose last
  try was wrong, and everything already in `srs.json`.
- Box *b* comes back every `DRILL_INTERVALS_DAYS[b-1]` days
  (`local_store.py` owns the numbers). A mistake not yet in `srs.json` is box 1,
  due now. Wrong anywhere in the drill → box 1, due in 1 day. Right while under
  review (in `srs.json`, a `&review=1` deep link, or a known exam mistake) → up
  one box (5 stays 5). A right answer to an item never missed enrols nothing.
- **Practised in place**: due items are grouped per 大問 and per 知識 category;
  a group's button deep-links `大問別練習.html?items=…&review=1` (or
  `聴解トレーニング.html?…`); the 復習ノート never renders items itself. A 知識
  item links to its card (`knowledge/<LEVEL>/<page>#e-<id>`) and is self-graded
  できた / まだ; a 知識 quiz retried on the card since the last review
  (`history.n` grew) is applied automatically on the next visit.

## Gate (`check_drill.py`, called from `make check`)

FAIL: the store's prefix outside `local_store.py` or under the exam prefix; the
`drill` namespace unregistered; an expected page missing or an unexpected one
present; non-HTML files under `drill/<LEVEL>/`; a page without exactly one
`.topbar` and one `.lang-select`, with `.lang-btn`, or with a root-absolute
link; a baked item with no primary `why_correct`; a clip question without a key
or explanation. The registry check greps these scripts for learner-language
literals like every builder. WARN: a page older than the data it stamps (every
test edit moves the pool — run `make drill`); items missing a learner language's
prose.

## Adding a level, a language, a tool

- **Level**: nothing to write — the pool follows the level's tests and table;
  add its `part → 知識 stems` row to `references/knowledge_links.json`, then
  `make drill LEVEL=<L>`.
- **Language**: a registry change (`langs.py`) plus `languages/<code>/drill.json`
  with the primary's keys, written for that reader; content falls back per item.
- **Tool**: add it to `drill_data.TOOLS`, a page function and its
  `expected_pages()` entry in `build_drill.py`, its labels in every `drill.json`,
  and a row above.

```bash
make drill                        # LEVEL=N2 by default: every page + index.html
python3 .agents/jlpt-drill/scripts/check_drill.py    # the drill lines of `make check`, alone
```
