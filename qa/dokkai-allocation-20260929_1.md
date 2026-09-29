# 読解 allocation table — 20260929_1 (BLUEPRINT-ASSIGNED, binding)

Stage 1 filled this in **before any prose exists**, as
`question-authoring/references/dokkai.md` §"Thirteen surfaces" and §"The
rhetorical-MOVE allocation table" require. Authors do NOT re-choose the shape,
template or MOVE columns. Each author fills the **final sentence** column from
the prose they write and hands the table back: edit this file, your own rows
only.

**Denominators** (dokkai.md §"The denominator"):
- Axis 1 has 13 theme rows, with 問題12 A+B as ONE row.
- Axis 2 has 13 closings, with 問題12 A and B SEPARATE and 問題14 outside.
- The MOVE cap counts essay surfaces only, with 問題12 A+B as ONE
  (`jlpt-test-generation`).

**Themes** come from `tests/20260929_1/test_spec.json` `items.reading_topics[i]`.
Index → surface: 0→問題10(1) … 4→問題10(5), 5→問題11(1) … 8→問題11(4), 9→問題12,
10→問題13, 11→問題14. Author each surface's SUBJECT from its entry's `theme`, and
keep it off that entry's `avoid` list and off any re-wording of an avoid string.
Index 11 was rerolled (`qa/blueprint-rerolls-20260929_1.md`), so read the themes
from the spec as it now stands.

| surface | theme (spec) | closing shape (≤2 each) | final-sentence template (≤2 each; foil named) | MOVE | final sentence (AUTHOR FILLS) |
|---|---|---|---|---|---|
| 問題9 cloze **(文法 author owns this row)** | **働き方** (author-composed; see below) | 説明 | — (unnamed). **Not** a cleft (問題13 holds the paper's one 分裂文), and not 20260928_2 問題9's skeleton 〈場所〉には、もう、〈程度節〉ほどの〈主体〉が V-ない | 機構の説明 | 「書きかけの一文は、その日の自分が選んでおいた、翌朝の最初の一歩になる。」 — subject やりかけで帰る（区切りの手前で仕事を終える）; unnamed 「AはBになる」, not a cleft, no わけ／ていない／ていたのだ／先回り |
| 問題10(1) | 住まい | 随筆 | — (unnamed). **Not 分裂文** (cross-paper bar: 20260928_2 closed 問題10(4) on it) | 一人称の前後比較 || 「何か月も開けずにすむ箱には、前の家から持ってきたままの暮らしが詰まっている。」 — 〈名詞句〉には、〈X〉が詰まっている（unnamed） |
| 問題10(2) | デジタル化 | **実用文・分類外** (notice / お知らせ) | — | （実用文） || （お知らせ本文の最終文）「アプリに登録した家には4月から回覧板は回りませんが、登録しない家には、これまでどおり回覧板でお知らせします。」 — 実用文 |
| 問題10(3) | 人間関係 | **実用文・分類外** (business email) | — | （実用文） || （メール本文の最終文）「今後とも、よろしくお願い申し上げます。」 — 実用文（用件は「3月中に私あてにメールでお知らせくださいませんか」） |
| 問題10(4) | 地域活性化 | 条件提示 | — (unnamed). **NOT 相関** (`A では/ほど B が多い`): 問題10 closed on 相関 in three consecutive papers before 20260928_2 (dokkai.md cross-paper bar, founding case). **Not 分裂文** (bar). Must differ from 12(A)'s skeleton | 数えたことの報告 || 「古い写真の横に今の姿が並んでいるかどうかで、見た人が家に帰って自分の写真を探すかどうかが変わる。」 — 〜かどうかで、〜かどうかが変わる（unnamed, not 相関） |
| 問題10(5) | メディア・情報 | 意外な観察 | — (unnamed). **Not 分裂文** (bar), so 「〜のは、…からだ」 is off. State the mismatch, then the cause, in another frame. Must differ from 12(B)'s skeleton | 数えたことの報告 || 「町の人は、知っている名前を探すために、この広報紙を読んでいる。」 — 〈人〉は、〈目的〉ために、〈物〉を V-ている（unnamed, not cleft） |
| 問題11(1) | 消費・経済 | 随筆 | — (unnamed). Must differ from 10(1)'s skeleton | 一人称の前後比較 || 「今の私は、店を出る前から、その服を着て出かける日のことを考えている。」 — 今の〈私〉は、〈時点〉から、〜ことを考えている（unnamed） |
| 問題11(2) | 子育て・家族 | 反論応答 | — (unnamed). **NOT `A わけではない`** (cross-paper bar: 20260928_2 11(4), and 20260928_1 11(1) before it). **NOT `A より B のほうが`** (bar: 20260928_2 11(2)) | 反論への応答 || 「心配の声を一つずつ決まりに書き直していくと、留守番の練習は、そのまま親子で家の中の危ないところを確かめる時間になった。」 — 〜ていくと、〈X〉は、そのまま〈Y〉になった（unnamed; no わけではない, no より…ほう） |
| 問題11(3) | 行政・手続き | 主張 | — (unnamed). Not わけではない, not より…ほう (bar). Not 「AだけではB、Cこそが」. Must differ from 11(4)'s skeleton | 一人称の前後比較 || 「家族に代わって書類を書く人は、出す前に一度、本人の前で読み上げる時間を取るべきだと思います。」 — 〈人〉は、〜べきだと思います（unnamed） |
| 問題11(4) | 食 | 主張 | `A というより B` (foil = A, named in the final). This is the paper's ONLY not-A-but-B family member. Allowed in 問題11: neither previous paper closed 問題11 on it, and 〜というより is not keyed on this paper | **〈想定→実は〉** || 「私たちの食べる量は、おなかのすき具合というより、目の前の器の大きさに左右されている。」 — A というより B（foil = おなかのすき具合） |
| 問題12(A) | 睡眠・健康 | 条件提示 | — (unnamed). **NOT 相関.** Read against 12(B) first | 機構の説明 (A+B = one surface) || 「腰を痛めずに荷物を持ち上げる条件は二つで、荷物を体に引き寄せておくことと、立ち上がる力を膝から出すことである。」 — 〜条件は二つで、〜ことと〜ことである（unnamed, not 相関, not cleft） |
| 問題12(B) | 睡眠・健康 | 意外な観察 | — (unnamed). Not a cleft. Must differ from 12(A) and from 10(5) | ″ || 「軽いものの前では、重さを感じない分だけ、体が持ち上げる用意を忘れてしまいます。」 — 〜では、〜分だけ、〜てしまう（unnamed, not cleft） |
| 問題13 | 科学・技術 | 説明 | `〜のは B だ（分裂文）` (the paper's one cleft; 問題13 carries no cross-paper bar) | 反論への応答 || 「芝生の上の日かげで測った気温が守っているのは、いつ、どこで測っても、同じ条件で比べられるということです。」 — 〜のは B だ（分裂文） |
| 問題14 | 教育 | (outside axis 2 — flyer, no closing) | — | （実用文） | — |

## Who owns which rows

- **The 問題9 cloze row belongs to the 文法 (問7–9) author.**
  `scaffold_sections.py` emits the cloze inside `問7-9_文法.md`. Both authors get
  this whole table, because the caps are counted across all thirteen closings.
- **問題10–14 belong to the 読解 author.**

## 問題9's theme is AUTHOR-COMPOSED, and four values were legal; 働き方 was drawn by RNG

`test_spec.json` has no cloze topic, because the cloze is the 13th, unpooled
theme row. Here is how `exam-blueprint` §"The four theme rules" narrows it:

- **Rule 3.** The 12 drawn themes are taken: 住まい, デジタル化, 人間関係,
  地域活性化, メディア・情報, 消費・経済, 子育て・家族, 行政・手続き, 食,
  睡眠・健康, 科学・技術, 教育. That leaves 医療・福祉, 環境, 防災, 交通, 働き方,
  文化・伝統, スポーツ・余暇 and 旅行・観光.
- **Rule 4, consecutive papers.** 20260928_2 headlined 住まい, デジタル化,
  行政・手続き and 子育て・家族, with 聴解問題5 on スポーツ・余暇 and 旅行・観光.
  That bars スポーツ・余暇 and 旅行・観光.
- **Rule 4, two papers back.** 20260928_1 headlined 交通, 人間関係, 文化・伝統
  and 食, with 聴解問題5 on スポーツ・余暇 and 消費・経済. The budget of one is
  unspent: none of 問題12/13/14 repeats a two-back theme. But rule 4c says a
  cloze candidate is only free if it headlines NEITHER of the previous two
  papers. That bars 交通 and 文化・伝統, and it keeps the budget at 0.
- **Legal: 医療・福祉, 環境, 防災, 働き方.** One was picked with
  `secrets.randbelow(4)` rather than by preference. It returned index 3, which is
  **働き方**.

**Rule 4b: the cloze SUBJECT (5–15 JP chars) must not match any of 20260928_2's
13 読解 subjects or its 21 聴解 subjects** (`logs/topics.json`, last row).
働き方 is the most crowded theme on the 聴解 side, so read the list:

- **20260928_2 読解:** 問題10(4) `見積もりと待つ時間`, about why estimates miss the
  time spent waiting for replies. Stay off estimates, schedules slipping and
  waiting time.
- **20260928_2 聴解 働き方 items:**
  - 1-1 出張帰りの最終の新幹線と1泊
  - 1-2 スーパーの値引きシールと在庫数え
  - 2-1 面接で前の会社を辞めた理由
  - 2-2 就活に合わせてアルバイトを換える
  - 2-3 社内アンケートで休暇申請の簡略化
  - 2-4 在宅で働ける日で会社を選ぶ
  - 3-2 リーダー研修の感想
  - 4-x 受付・部長抜き・応募条件
  - None of these may be the cloze's setting plus issue: no business trips, no
    shelf and stock work, no job interviews or job changes, no part-time
    scheduling, no leave requests, no remote work, and no training reviews.
- **20260928_1** (two back, a minor finding if matched):
  - 12(A)(B) `職場での呼び方` (tagged 人間関係, but set in the workplace)
  - 聴解2-2 おもちゃ会社の企画
  - 聴解2-5 転職インタビュー
  - So no workplace naming or forms of address either.
- The sampler's full 働き方 `avoid` list is at
  `items.listening_scenarios[0].avoid` in the spec (60 strings). Stay off it,
  and off any re-wording of it.

## Headline subjects — what the rule-4b diff must stay clear of

The authors write a 5–15-char SUBJECT for each headline surface. Diff it
against the previous paper's 13 読解 and 21 聴解 subjects:

- **問題12 睡眠・健康.**
  - 20260928_2 聴解問題3-4番 was about sleep: the sense of rest matters more than
    its length, and the bedroom's quiet, darkness, temperature and clothing.
  - 20260928_2 聴解問題3-1番 was the roles of teeth.
  - 20260928_1 問題10(3) was `夕食後のうたた寝` (two back).
  - **So 問題12 may not be about sleep, bedrooms, naps or teeth.** The theme also
    covers everyday non-medical health habits, and that is where the subject
    should come from. Both A and B share one subject.
- **問題13 科学・技術.** Nothing of this theme is in 20260928_2's 読解 half.
  20260928_1's retired 問題12 subject `失敗した実験の公開` is still in `avoid`.
  Do not write about publishing failed experiments, or about research or lab
  culture in that frame.
- **問題14 教育.**
  - 20260928_2 問題10(5) was a school-to-parents notice about textbooks left in
    the classroom.
  - 20260928_2 問題14 was a municipal rental 案内 (チャイルドシート).
  - 20260928_1 問題14 was a 親子見学会 flyer.
  - 20260928_1's 聴解 half had a library-hours item (1-2) and a 文化祭 item (1-5).
  - **So the flyer may not be:**
    - a school→保護者 notice;
    - a 親子 event programme;
    - a rental/貸し出し 案内;
    - a library opening-hours notice.
  - Pick a different document type or errand.

## Non-headline subjects off-limits from the previous two papers

These are per theme, `logs/topics.json`. A re-wording counts as used.

- **10(1) 住まい:** not house creaks or wood shrinkage (20260928_2 問題9), and
  not window airing or condensation (20260928_1 11(2)).
- **10(2) デジタル化 notice:** not a notes-app or memo subject (20260928_2 問題12).
- **10(3) 人間関係 email:**
  - not thank-you notes or second thanks (20260928_2 10(3));
  - not workplace forms of address (20260928_1 12).
  - It is a BUSINESS email, and the carve-out allows it to close on a request.
- **10(4) 地域活性化:** not renting a corner of a shop or a 商店街 (20260928_2
  11(2)), and not an unmanned-station waiting-room rota (20260928_1 11(3)).
- **11(1) 消費・経済:**
  - not a shop's sales notebook or umbrella sales (20260928_2 11(1), the SAME
    slot one paper back);
  - not household budgeting on payday (20260928_1 10(5));
  - not a flea market, the 20260928_1 聴解 2-4 subject.
  - A shop clerk reading records is the skeleton 20260928_2 11(1) already ran,
    so do not reuse that narrator either.
- **11(2) 子育て・家族:** not child-seat rental (20260928_2 14), and not a nursery
  gate or pickup (20260928_1 10(2)).
- **11(3) 行政・手続き:** not plain-Japanese rewriting of municipal notices
  (20260928_2 13), and not a municipal counter clerk answering a colleague. That
  is 13's narrator and move one paper back.
- **11(4) 食:** not a school-lunch centre (20260928_1 14).

## Why each shape sits where it does

**The previous two papers' closings, per slot** (`logs/topics.json`
`closing_moves`). No slot repeats a shape either paper used in that slot, except
the two 実用文 slots (explained below):

| slot | 20260928_1 | 20260928_2 | assigned here |
|---|---|---|---|
| 問題9 | 随筆 | 意外な観察 | 説明 |
| 10(1) | 説明 | 実用文 | 随筆 |
| 10(2) | 実用文 | 主張 | 実用文 |
| 10(3) | 意外な観察 | 随筆 | 実用文 |
| 10(4) | 実用文 | 説明 | 条件提示 |
| 10(5) | 条件提示 | 実用文 | 意外な観察 |
| 11(1) | 反論応答 | 意外な観察 | 随筆 |
| 11(2) | 随筆 | 主張 | 反論応答 |
| 11(3) | 条件提示 | 随筆 | 主張 |
| 11(4) | 説明 | 反論応答 | 主張 |
| 12(A) | 主張 | 説明 | 条件提示 |
| 12(B) | 反論応答 | 条件提示 | 意外な観察 |
| 13 | 主張 | 反論応答 | 説明 |

**Why the 実用文 members sit at 10(2) and 10(3).**
- 10(3) is the only 問題10 slot that neither previous paper used for 実用文.
- Every other slot was used once. 10(2) repeats only the paper two back
  (20260928_1). 10(1) and 10(5) would repeat the paper immediately before.
- 10(2) takes the notice, because デジタル化 fits a notice about a system change.
  10(3) takes the business email, because 人間関係 fits correspondence (for
  example a handover between contacts; the author chooses).
- This is a convention carried over from 20260928_2's file, not a gate.

## Tallies the authors must NOT break

- **Closing shape (13 total):** 説明 2 (問題9, 13), 随筆 2 (10(1), 11(1)),
  条件提示 2 (10(4), 12(A)), 意外な観察 2 (10(5), 12(B)), 主張 2 (11(3), 11(4)),
  反論応答 1 (11(2)), 実用文・分類外 2 (10(2), 10(3)).
  - Values come from the CLOSED vocabulary `CLOSING_MOVES` and nothing else.
  - 反論応答 is the only shape with a spare slot. A re-angle that must change
    shape goes there first.
- **Template:**
  - Named templates in use: `A というより B` 1 (問題11(4)) and 分裂文 1 (問題13).
    Every other final is unnamed.
  - 相関 is **0**, on purpose.
  - The three **cap 1** templates are assigned to no row: 後知れ `〜ていた のだ`,
    不在の残り `〜ていない`, and 先回り. An unnamed final that lands on one of them
    spends its only slot. Don't.
- **Cross-paper bar** (`check_dokkai_template_repeat_prev_paper`, FAIL). I
  verified it against 20260928_2's shipped `言語知識・読解.md` with the gate's
  own `dokkai_templates_by_daimon()`. That paper closed:
  - 問題10 on 分裂文 (10(4));
  - 問題11 on `A よりも B のほう` (11(2)) and `A わけではない` (11(4)).
  - 問題9, 12 and 13 closed on no named template.

  So on this paper:
  - **no 問題10 surface may close on 分裂文;**
  - **no 問題11 surface may close on より…ほう or わけではない.**

  The gate reads the final sentence. A cleft in the last sentence of 10(1),
  10(4) or 10(5) is a FAIL, even when it is the 「大切なのは」 or 「注目すべき点は」
  variant.
- **not-A-but-B reframe family**
  (`AではなくB`/`というより`/`よりも`/`だけではなく`/`わけではない`, and ANY final
  that names a foil and prefers the alternative, including `AにないBがある`):
  exactly **1** surface, 問題11(4). Do not add a second anywhere, including a
  non-final sentence that ends up carrying the close.
- **MOVE (10 essay surfaces):**
  - 〈想定→実は〉 **1** (問題11(4))
  - 機構の説明 2 (問題9, 12)
  - 数えたことの報告 2 (10(4), 10(5))
  - 一人称の前後比較 **3, at cap** (10(1), 11(1), 11(3))
  - 反論への応答 2 (11(2), 13)

  No row is over its cap. Headroom for re-angles: 機構の説明 +1,
  数えたことの報告 +1, 反論への応答 +1, 一人称の前後比較 0.
  - **〈想定→実は〉 is planned at 1, not 2, on purpose.** The cross-half cap is 2,
    and it counts the 聴解 talks (`jlpt-test-generation` §"One topic, one
    surface", RC-7). Stage 3 re-angles 問題11(4) only if the composed 聴解 half
    carries **two**. If that happens, 11(4) moves to 反論への応答 or
    数えたことの報告, never to 一人称の前後比較.
- **Persona** (cap 2 per archetype, `logs/topics.json` `persona`). The three
  一人称の前後比較 narrators (10(1), 11(1), 11(3)) must be three different
  archetypes. 生活者 narrated 20260928_2 10(3) and 20260928_1 問題9 and 11(2), so
  prefer something other than 生活者 for 10(1). If 11(3) is written
  from inside an office, it is not a 市職員 answering a senior colleague.
- **Voice quota** (`exam-blueprint` rule 5, 12 essay-type passages, 問題14
  excluded): at least 4 in the first person and at least 3 in です・ます
  throughout.
  - First-person candidates: the three 一人称の前後比較 rows (10(1), 11(1),
    11(3)) plus one of the 数えたことの報告 rows (10(4) or 10(5)).
  - Plan the です・ます passages alongside the length bands (dokkai.md §"Length
    bands"). At least one of 11(3), 12(B) and 13 should be です・ます.

## Tested forms that must stay out of the 読解 prose (Item integrity #15)

This paper keys the following. The 問題7 list is the one AFTER the measured
敬語 rerolls of 2026-09-29 (`qa/blueprint-rerolls-20260929_1.md` rows 2–11).
Read the spec, not an earlier copy of this file.
- **問題7:** 〜ところから, 〜さえ, 敬語:いたす, 敬語:おいでになる, 〜てでも,
  〜わけだ, 〜につけて, 〜によらず, 使役:〜させてくれる, 〜ずじまいだ, 〜すら,
  〜反面.
- **問題8:** 〜だけあって, 〜わりに, 条件限定(〜ない限りは…),
  **順接接続(〜したがって…)**, 〜をもとに(して).

Consequences for the allocation:

- **Two keyed 敬語 verbs remain: いたす and おいでになる.** This is down from
  seven. Both are still stock vocabulary of the 10(2) notice, the 10(3) business
  email and the 問題14 flyer.
  - Write those three surfaces with no 「いたします／いたしました／いたしまして」
    and no 「おいでになる／おいでください／おいでの方」.
  - Use instead, for example: 「お願いします」「お知らせします」「ご連絡します」
    「お越しください」「ご来場の方は」.
  - 申し上げる, 存じる, ご覧いただく, いらっしゃる and なさる are **no longer
    keyed**, so ordinary use of them in 実用文 register is allowed again. Keep it
    natural, not heavy.
  - `check_key_grammar_exposure` counts the keyed string in the prose, and QA
    reads the frames by hand. Grep all three 実用文 surfaces for いたし and
    おいで before hand-off.
- **〜わけだ is now a 問題7 key.** No closing or other sentence may end
  「…わけだ／わけである／わけです」.
  - This matters most for the 説明 closings (問題9 and 問題13) and the 意外な観察
    closings (10(5) and 12(B)), where 「だから…わけだ」 is the reflex ending.
  - It does not touch the 11(4) `A というより B` assignment.
  - `A わけではない` is a separate grammar point and is already barred in 問題11.
    Assign it nowhere else either, so the prose carries no わけ-frame at all.
- **〜反面 is now a 問題7 key.** It is the stock contrast connective of 説明,
  意外な観察 and 反論応答 prose. Write contrasts with 「一方で」「その代わり」
  「ただ」, never 「反面」.
- **〜すら, 〜につけて and 〜ずじまいだ are now 問題7 keys.**
  - No 「すら」 anywhere. It leaks into 随筆 prose (「名前すら知らなかった」).
  - No 「につけ(て)」 anywhere, including 「何かにつけて」 and 「〜を見るにつけ」.
  - No 「ずじまい」 anywhere. It is the natural past-regret ending of a
    一人称の前後比較 passage (10(1), 11(1), 11(3)).
- **順接接続(〜したがって…) is a general-purpose frame**, so a prose grep is owed
  (`exam-blueprint` §"A `grammar_p8` draw whose form is a general-purpose
  sentence pattern").
  - 「したがって」/「従って」 is the stock connective of 説明 and 反論応答 prose,
    which means 問題9, 問題13 and 11(2).
  - Grep every surface for both spellings. Re-word every hit but at most one, and
    that one must not sit in the sentence-initial 順接 frame. Prefer 0.
- **〜さえ is a 問題7 key**, so no 「さえ」 or 「〜さえすれば」 anywhere.
  - It is the natural surface of a 条件提示 closing, so it binds 10(4) and 12(A)
    in particular.
  - The 「Xさえすれば十分」 strawman distractor shape is off as well (dokkai.md
    §"The answerability consequence").
- **条件限定(〜ない限りは…)** keys 限り. Write no 「ない限り」 in the 条件提示
  closings or anywhere else.
- **Stage 3 re-grep.** Every form above goes into the Stage-3 keyed-form re-grep
  with its counts and frames (文末／連用／連体).
  - 〜わりに and 〜だけあって are likely to leak into 随筆 prose.
  - 〜をもとに is likely to leak into 数えたことの報告 prose (「記録をもとに」).
  - 〜によらず, 〜ところから, 〜反面 and 〜わけだ are likely to leak into 説明 prose.

## The two things that get checked by hand

1. **The unnamed finals must not share a skeleton with each other, or with the
   named ones.** The pairs at risk:
   - 問題9 vs 問題13 (both 説明; 13 is the cleft, so 9 may not be);
   - 10(1) vs 11(1) (both 随筆);
   - 10(4) vs 12(A) (both 条件提示, both NOT 相関, so two DIFFERENT non-相関
     condition skeletons are needed);
   - 10(5) vs 12(B) (both 意外な観察);
   - 11(3) vs 11(4) (both 主張);
   - 10(1)/11(1)/11(3) (all 一人称の前後比較);
   - 問題12(A) vs 問題12(B). Read A against B FIRST, because that is where the
     rhyme lands.

   Write the sentences into the last column and read them down as a column
   before finalising: once down the shapes, and once down the skeletons.
   Also read each 問題10 and 問題11 final against 20260928_2's final in the same
   大問, which `qa/dokkai-allocation-20260928_2.md` quotes. The cross-paper gate
   sees only named templates. An unnamed skeleton reused from last paper's same
   大問 is the same rhyme, just with no name.
2. **Apply the deletion test to 問題11(4), and to nothing else.** Delete the
   denial sentence. If the passage still says what it came to say, it was never
   on the skeleton. Every OTHER row must carry no attributed assumption and no
   denial at all.
   - **10(5) and 12(B) (意外な観察):** the mismatch must be a FACT the reader
     finds unexpected, never a belief someone held and is then told is wrong.
   - **10(1), 11(1) and 11(3) (一人称の前後比較):** the "before" must be a
     PRACTICE the narrator actually did, never a belief they held
     (「つもりだった」「と思っていた。ところが」 is the re-skin).
   - **10(4) and 10(5) (数えたことの報告):** the count must not be introduced as
     contradicting an expectation.
   - **11(2) and 問題13 (反論への応答):** the objection is taken seriously and
     answered on its own terms. It is not a strawman, and it does not open
     「もっとも」 followed by a knock-down. 20260928_2 13 is the scaffold to vary
     from.
