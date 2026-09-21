# 読解 allocation table — 20260917_1 (ORCHESTRATOR-ASSIGNED, binding)

Filled in by the orchestrator **before any prose exists**, as
`question-authoring/references/dokkai.md` §"Thirteen surfaces" and §"The
rhetorical-MOVE allocation table" require, and passed to the stage-2 読解
author. The author does NOT re-choose these columns. The author fills the
`theme` column from `tests/20260917_1/test_spec.json` and the **final sentence**
column from the prose it writes, then hands the completed table back.

Denominators (dokkai.md §"The denominator"): axis 1 = 13 theme rows (問題12 A+B
as ONE); axis 2 = 13 closings (問題12 A and B SEPARATE, 問題14 outside); the MOVE
cap counts essay surfaces only with 問題12 A+B as ONE (`jlpt-test-generation`).

| surface | closing shape (≤2 each) | final-sentence template (≤2 each) | MOVE | theme | final sentence (AUTHOR FILLS) |
|---|---|---|---|---|---|
| 問題9 cloze **(文法 author owns this row)** | 説明 | — (none of the 7 named) | 機構の説明 | **author-composed — see constraint below** | |
| 問題10(1) | 条件提示 | `A では/ほど B が多い（相関）` | 数えたことの報告 | | |
| 問題10(2) | 随筆 | — | 一人称の前後比較 | | |
| 問題10(3) | **実用文・分類外** (business email) | — | （実用文） | | |
| 問題10(4) | **実用文・分類外** (notice / お知らせ) | — | （実用文） | | |
| 問題10(5) | 意外な観察 | `〜のは B だ（分裂文）` | **〈想定→実は〉** | | |
| 問題11(1) | 説明 | — | 機構の説明 | | |
| 問題11(2) | 反論応答 | `A だけではない。B こそが〜` | 反論への応答 | | |
| 問題11(3) | 条件提示 | — | 数えたことの報告 | | |
| 問題11(4) | 随筆 | ~~`〜のは B だ（分裂文）`~~ → **分裂文ではない**（QA F2 の修復で結び直した） | 一人称の前後比較 | 睡眠・健康 | `いまは、眠れないまま朝を待つ夜があっても、私は時間を数えずにいられる。` |
| 問題12(A) | 主張 | `〜のは、A ではなく B だ` | 反論への応答 (A+B = one surface) | メディア・情報 | `相手に確かめてもらうべきは、書き手の見方ではなく、調べれば答えの決まることである。` |
| 問題12(B) | 反論応答 | — | ″ | メディア・情報 | `どこを断るかがはっきりしていれば、全文を見せても、記事は書いたまま残る。` |
| 問題13 | 主張 | — | **〈想定→実は〉** | | |
| 問題14 | (outside axis 2 — flyer, no closing) | — | （実用文） | | — |

**2026-09-21 (fix round)**: 問題11(4)'s row is updated too. QA F2 measured three
cleft-sentence closings on this paper against an official maximum of two
(問題10(5), 問題11(4), 問題12(A) — and 問題12(A)'s skeleton is BOUND by the row
below, so it could not move). The repair re-closed 問題11(4) off the cleft, so its
final-sentence template cell no longer reads `〜のは B だ（分裂文）`; the shipped
sentence is in the row's last column. 問題10(5) still runs the cleft, and
問題12(A)'s `〜のは、A ではなく B だ` is its 下位型 — two in total, inside the cap.

**2026-09-21**: the two 問題12 rows' `theme` and `final sentence` columns are
filled from the SHIPPED text of `_sections/問10-14_読解.md` after the 問題12 (A+B)
re-angle onto 「取材した相手に、記事を出す前に原稿を見せるかどうか（会報・広報の
書き手）」, which closed stage-3 F1/F3/F4. The other rows' two author columns are
still empty; they were never filled at authoring time, and filling them now from
the shipped passages is a separate read this build pass did not do.

## Who owns which rows

- **The 問題9 cloze row belongs to the 文法 (問7–9) author**, not the 読解 author —
  `scaffold_sections.py` emits the cloze inside `問7-9_文法.md`. Both authors get
  this whole table anyway, because the caps are counted across all thirteen
  closings and neither author can verify its own rows alone. Stage 3 reads the
  merged table.
- **問題10–14 belong to the 読解 author.**

## 問題9's theme is AUTHOR-COMPOSED, and only three values are legal

`test_spec.json` has no `cloze_topic` — the sampler drew 12 `reading_topics`
(問題10(1)–(5), 問題11(1)–(4), 問題12, 問題13, 問題14) and the cloze is the
**13th, unpooled** theme row. Stage 1 worked out the legal set against
`exam-blueprint` §"The four theme rules":

- The 12 drawn themes are all taken (rule 3: all thirteen carry DIFFERENT themes).
- Rule 4 permits **at most ONE** headline theme to repeat, and only against the
  paper-before-last — and **this paper has already spent that budget**: 問題13
  drew 働き方, which headlined `20260911_1`'s 問題12.
- `20260914_1` (one paper back) headlined デジタル化 / 教育 / 人間関係 / 旅行・観光
  / スポーツ・余暇 / 防災, so those are barred outright.

**Legal values for the 問題9 theme: 環境, 子育て・家族, 文化・伝統. Pick ONE.**
交通 / 科学・技術 / 地域活性化 are free under rule 3 but would be a SECOND
two-back repeat and are therefore barred here.

On top of the theme, the cloze **subject** (5–15 JP chars) must be diffed
against all 13 読解 subjects AND all 21 聴解 subjects of `20260914_1` — the cloze
is one of the two unpooled surfaces and `20260817_3` is the precedent for a
cloze subject colliding with the paper's own 聴解 stimulus.

## Tallies the author must NOT break

- **Closing shape:** 説明 2, 条件提示 2, 随筆 2, 反論応答 2, 主張 2, 意外な観察 1,
  実用文・分類外 2 = 13. Every shape ≤2. Values come from the CLOSED vocabulary
  `CLOSING_MOVES` and nothing else — inventing an eighth label is the
  `20260904_2` F7 defect.
- **Template:** 分裂文 2, 相関 1, `だけではない…こそが` 1, `AではなくB` 1,
  unnamed 8. No named template over 2.
- **not-A-but-B reframe family** (`AではなくB`/`というより`/`よりも`/`だけではなく`/
  `わけではない` — ONE move in five grammars): exactly **2** surfaces, 問題11(2)
  and 問題12(A). Do not add a sixth-form member anywhere else, including in a
  non-final sentence position that ends up carrying the close.
- **MOVE:** 〈想定→実は〉 **2** (問題10(5), 問題13) — this is the plan-2 target,
  not the 3 ceiling; 機構の説明 2, 数えたことの報告 2, 一人称の前後比較 2,
  反論への応答 2. Ten essay surfaces, no row over cap.

## The two things that actually get checked by hand

1. **The eight "unnamed template" finals must not share a skeleton with each
   other.** T0 is the absence of a named template, not a licence: eight finals
   on one home-grown pattern is exactly the `20260817_3` five-on-one-skeleton
   defect with a different denominator. Write the eight sentences into the last
   column and read them down as a column before finalising.
2. **Apply the deletion test to the two 〈想定→実は〉 rows and to nothing else.**
   Delete the denial sentence: if the passage still says what it came to say, it
   was never on the skeleton. Every OTHER row must FAIL to collapse — i.e. must
   carry no attributed assumption + denial at all. The most common re-skin is
   一人称の前後比較 whose "before" is the narrator's mistaken BELIEF rather than
   their PRACTICE (`20260911_1`, nine of ten surfaces). 問題10(2) and 問題11(4)
   are the two at risk here: their "before" must be a PRACTICE the narrator
   actually did, never a belief they held.
