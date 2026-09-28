# 読解 allocation table — 20260928_1 (ORCHESTRATOR-ASSIGNED, binding)

Filled in by the orchestrator **before any prose exists**, as
`question-authoring/references/dokkai.md` §"Thirteen surfaces" and §"The
rhetorical-MOVE allocation table" require. The authors do NOT re-choose the
shape, template or MOVE columns. The author fills the **final sentence** column
from the prose it writes and hands the completed table back (edit this file,
your own rows only).

Denominators (dokkai.md §"The denominator"): axis 1 = 13 theme rows (問題12 A+B
as ONE); axis 2 = 13 closings (問題12 A and B SEPARATE, 問題14 outside); the MOVE
cap counts essay surfaces only with 問題12 A+B as ONE (`jlpt-test-generation`).

Themes come from `tests/20260928_1/test_spec.json` `items.reading_topics[i]`
(index → surface: 0→問題10(1) … 4→問題10(5), 5→問題11(1) … 8→問題11(4),
9→問題12, 10→問題13, 11→問題14). Each surface's SUBJECT is authored from its
entry's `theme` and must avoid that entry's `avoid` list (and any re-wording of
an avoid string).

| surface | theme (spec) | closing shape (≤2 each) | final-sentence template (≤2 each) | MOVE | final sentence (AUTHOR FILLS) |
|---|---|---|---|---|---|
| 問題9 cloze **(文法 author owns this row)** | **交通** (author-composed, see below) | 随筆 | — (none of the 7 named) | 一人称の前後比較 | 乗り換えのたびに見上げてきた板の一枚一枚が、今ではわたしの頭の中で、駅の地図になってつながっている。 (skeleton: `X が、今では Y になってつながっている` — unnamed; subject `案内板で乗り換える`; before = following the phone's step-by-step route guidance, after = reading the station signboards — both PRACTICES, no belief stated or denied) |
| 問題10(1) | 医療・福祉 | 説明 | — | 機構の説明 | 杖が床を押し返す分だけ、痛む足が受け止める重さは軽くなります。 |
| 問題10(2) | 子育て・家族 | **実用文・分類外** (notice / お知らせ) | — | （実用文） | ご連絡のない方には、お子さんをお渡しできません。（署名「みなみ保育園」が続く） |
| 問題10(3) | 睡眠・健康 | 意外な観察 | `〜のは B だ（分裂文）` | ~~〈想定→実は〉~~ → **機構の説明** (stage-3 F2) | 夜の眠りを細かく切っていたのは、夕食後の、あの短いうたた寝（注）だった。 |
| 問題10(4) | 環境 | **実用文・分類外** (business email) | — | （実用文） | ご回答をいただけますと幸いです。（署名「ひかり工業　総務課　西村」が続く） |
| 問題10(5) | 消費・経済 | 条件提示 | `A では/ほど B が多い（相関）` | 数えたことの報告 | 数えてみると、給料日に払う予定を書き出していた家庭ほど、月の終わりにお金が足りなくなった回数が少なかった。 |
| 問題11(1) | 防災 | 反論応答 | `A わけではない` | 反論への応答 | 見て回る私たちは、塀が安全かどうかを決めているわけではないのです。 |
| 問題11(2) | 住まい | 随筆 | — | 一人称の前後比較 | 窓を開ける5分のおかげで、閉めきった部屋に暮らしていても、外の季節がどのあたりまで来ているのかが分かるようになった。 |
| 問題11(3) | 地域活性化 | 条件提示 | — (**NOT** 相関 — vary the 条件提示 skeleton) | 数えたことの報告 | この二つがそろえば、翌年もたいていの人が当番表に名前を書いてくれます。 |
| 問題11(4) | 教育 | 説明 | — | 機構の説明 | 位のずれによる間違いは、書く紙の形を変えるだけで防げる種類の間違いなのである。（QA F4 で改稿） |
| 問題12(A) | ~~スポーツ・余暇~~ → ~~科学・技術~~ → **人間関係** (stage-3 F1) | 主張 | `A というより B` | 反論への応答 (A+B = one surface) | 呼び方は、相手の立場を示す札というより、声をかける側が越える段差の高さそのものである。（R2-F2 に合わせ、問題9 と重なる「たびに／前に…ている」を外して改稿） |
| 問題12(B) | ~~スポーツ・余暇~~ → ~~科学・技術~~ → **人間関係** | 反論応答 | — | ″ | 本人が自分で選んで名札に書いた呼び方は、その日から、互いに口にする名前として使われていく。（QA F4・R2-F2 で改稿） |
| 問題13 | 文化・伝統 | 主張 | — | **〈想定→実は〉** | 初めて寄席へ出かける人には、よく演じられる噺のあらすじを一つ読んでから行くことを、私は勧めたいと思います。 |
| 問題14 | 食 | (outside axis 2 — flyer, no closing) | — | （実用文） | — |

## Who owns which rows

- **The 問題9 cloze row belongs to the 文法 (問7–9) author** —
  `scaffold_sections.py` emits the cloze inside `問7-9_文法.md`. Both authors get
  this whole table, because the caps are counted across all thirteen closings.
- **問題10–14 belong to the 読解 author.**

## 問題9's theme is AUTHOR-COMPOSED, and only ONE value is legal: 交通

`test_spec.json` has no cloze topic; the cloze is the 13th, unpooled theme row.
Against `exam-blueprint` §"The four theme rules":

- Rule 3: the 12 drawn themes (医療・福祉, 子育て・家族, 睡眠・健康, 環境,
  消費・経済, 防災, 住まい, 地域活性化, 教育, スポーツ・余暇, 文化・伝統, 食) are taken.
  Left: デジタル化, メディア・情報, 働き方, 行政・手続き, 人間関係, 旅行・観光, 交通,
  科学・技術.
- Rule 4 (consecutive): `20260917_1` headlined 環境, メディア・情報, 働き方,
  行政・手続き (+ 聴解問題5 消費・経済, 科学・技術) — barred.
- Rule 4 (two-back, at most ONE repeat): `20260914_1` headlined デジタル化, 教育,
  人間関係, 旅行・観光 (+ 聴解問題5 スポーツ・余暇, 防災). This paper's 問題12
  (スポーツ・余暇) already repeats one of those, so the budget is spent — barred.
- **Remaining: 交通.**

The cloze **subject** (a 5–15-char topic string) must also be diffed against all
13 読解 and 21 聴解 subjects of `20260917_1` (`logs/topics.json`, last row) —
that paper's 聴解問題2-1番 is a 郵便局 delivery-time errand (交通), and
`20260914_1` 問題10(4) is 踏切の遮断時間 (交通); do not reuse either subject.

## Tallies the authors must NOT break

- **Closing shape:** 随筆 2, 説明 2, 意外な観察 1, 条件提示 2, 反論応答 2, 主張 2,
  実用文・分類外 2 = 13. Values come from the CLOSED vocabulary `CLOSING_MOVES`
  and nothing else.
- **Template:** 分裂文 1 (問題10(3)), 相関 1 (問題10(5)), `わけではない` 1
  (問題11(1)), `というより` 1 (問題12(A)), unnamed 9. No named template over 2.
- **not-A-but-B reframe family** (`AではなくB`/`というより`/`よりも`/`だけではなく`/
  `わけではない` — ONE move in five grammars): exactly **2** surfaces, 問題11(1)
  and 問題12(A). Do not add another member anywhere else, including a non-final
  sentence that ends up carrying the close.
- **MOVE:** 〈想定→実は〉 **2** (問題10(3), 問題13) — the plan-2 target, not the
  3 ceiling; 機構の説明 2, 数えたことの報告 2, 一人称の前後比較 2, 反論への応答 2.
  Ten essay surfaces, no row over cap.

## The two things that get checked by hand

1. **The nine "unnamed template" finals must not share a skeleton with each
   other.** Write the sentences into the last column and read them down as a
   column before finalising.
2. **Apply the deletion test to the two 〈想定→実は〉 rows and to nothing else.**
   Delete the denial sentence: if the passage still says what it came to say, it
   was never on the skeleton. Every OTHER row must carry no attributed
   assumption + denial at all. 問題9 and 問題11(2) (一人称の前後比較) are at risk:
   their "before" must be a PRACTICE the narrator actually did, never a belief
   they held. 問題10(5)/問題11(3) (数えたことの報告): the count must not be
   introduced as contradicting an expectation.

## Stage-3 repairs (2026-09-28, orchestrator ruling)

- **F1 (gate FAIL, rule 1):** the composed 聴解問題5-1番 (dance contest props) is
  honestly スポーツ・余暇, the theme 問題12 had drawn. 問題12 is the 読解 side and is
  re-angled: `--reroll-one reading_topics:9 --seed 39520803` → **科学・技術** (legal:
  not in this paper's 12 other 読解 themes; its only prior headline is
  `20260917_1`'s COMPOSED 聴解問題5-2, a rule-4 WARN, not a FAIL). New A/B pair,
  same shapes/templates/MOVE as before.
- **F2 (hand read):** 〈想定→実は〉 ran on 3 surfaces across the two halves
  (問題10(3), 問題13, 聴解問題2-5番) against the cross-half cap of 2. The 読解 side is
  re-angled: 問題10(3) leaves the skeleton for **機構の説明** (now 3 of ≤3); its
  closing shape (意外な観察) and 分裂文 final are kept. **Ruling on the per-label
  question:** the cross-half cap of 2 is the 〈想定→実は〉 cap (the only MOVE whose own
  cap is 2); the other MOVEs keep their ≤3 caps across both halves, so 反論への応答
  on 11(1), 12 and 聴解問題3-5番 (= 3) is inside its cap.
- MOVE tally after repair: 〈想定→実は〉 1 読解 + 1 聴解 = 2; 機構の説明 3 (問題10(1),
  10(3), 11(4)); 数えたことの報告 2; 一人称の前後比較 2; 反論への応答 2 読解.

### F1 correction — 科学・技術 was ILLEGAL, and the ruling above was wrong

The gate FAILs 科学・技術 (rule 4): the composed-half exemption covers a repeat
whose carrier on THIS paper is its own composed 聴解問題5, not one whose
previous-paper side is composed. My "a rule-4 WARN" reading was wrong. The
科学・技術 pair (失敗した実験を公開するか) was written and is discarded.

Further rerolls, each forced by an illegal draw, never by preference:
`reading_topics:9 --seed 6670416` → 交通 (illegal: the 問題9 cloze's composed
theme, rule 1); `--seed 43431270` → 行政・手続き (illegal: 20260917_1 問題14, rule 4).
The sampler enforces neither rule on a headline slot (known gap,
stage3-report-20260914_1 R4), so `sample_items.py` gained `--exclude-theme`
(rule-forbidden themes only) and the last reroll was:

    --reroll-one reading_topics:9 --seed 89576765 \
      --exclude-theme 環境 メディア・情報 働き方 行政・手続き 消費・経済 科学・技術   # rule 4: 20260917_1 headlines incl. its 聴解問題5
      --exclude-theme 交通 文化・伝統 食 スポーツ・余暇                         # rule 1: this paper's other headlines incl. 聴解問題5

(each theme passed as its own `--exclude-theme`; the ledger seed string does not
record them, so this line is the record). → **人間関係**. It spends the one
two-back repeat against 20260914_1 (問題13, 頼めない人 / 町の助け合い窓口) — the subject must be far from that one.
