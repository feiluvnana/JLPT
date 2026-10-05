# 読解 allocation table — 20261002_1 (BLUEPRINT-ASSIGNED, binding)

Stage 1 filled this in **before any prose exists**, as
`question-authoring/references/dokkai.md` §"Thirteen surfaces" and §"The
rhetorical-MOVE allocation table" require. Authors do NOT re-choose the shape,
template or MOVE columns. Each author fills the **final sentence** column from
the prose they write and hands the table back: edit this file, your own rows
only.

**Denominators** (dokkai.md §"The denominator"):
- Axis 1 has 13 theme rows, with 問題12 A+B as ONE row.
- Axis 2 has 13 closings, with 問題12 A and B SEPARATE and 問題14 outside.
- The MOVE cap counts essay surfaces only, with 問題12 A+B as ONE (10 here).

**Themes** come from `tests/20261002_1/test_spec.json` `items.reading_topics[i]`.
Index → surface: 0→問題10(1) … 4→問題10(5), 5→問題11(1) … 8→問題11(4), 9→問題12,
10→問題13, 11→問題14. Base draw `make sample 20261002_1 SEED=15443619`, no
reroll. Author each surface's SUBJECT from its entry's `theme`, and keep it off
that entry's `avoid` list and off any re-wording of an avoid string.

| surface | theme (spec) | closing shape (≤2 each) | final-sentence template (≤2 each; foil named) | MOVE | final sentence (AUTHOR FILLS) |
|---|---|---|---|---|---|
| 問題9 cloze **(文法 author owns this row)** | **メディア・情報** (author-composed; RNG, see below) | 随筆 | — (unnamed). Not a cleft, not the not-A-but-B family | 一人称の前後比較 | 「何年かたって開いても、その一行があれば、はさみを手にした日の自分に会うことができる。」 — subject 切り抜き帳（新聞の切り抜きに切り抜いた理由を一行書き添えるようになった）; before = clipping and pasting articles with date and paper name only, never re-reading them (a PRACTICE, no belief, no 思っていた); after = writing one line of why beside each clipping. Skeleton 〈〜ても、〜があれば、〜ことができる〉: unnamed, not a cleft, no ではなく／だけでなく／わけ／ていない／ていたのだ／先回り, and not 20260929_1 問題9's 「AはBになる」 |
| 問題10(1) | 子育て・家族 | **実用文・分類外** (notice / お知らせ) | — | （実用文） | （実用文の結び）「ご協力をお願いいたします。」 — subject: けやき通り児童館の平日午前「親子の時間」のお知らせ（QA F2: 地名・開始日・見出しを改稿） |
| 問題10(2) | 医療・福祉 | 意外な観察 | — (unnamed). Not a cleft. State the mismatch as a FACT, then the cause. Must differ from 11(4)'s skeleton | 数えたことの報告 (the paper's ONLY one; persona bar below) | 紙の番号と図の名前を結ぶ手がかりがない以上、図の前を通った人も、案内台まで来て番号を見せることになる。 — skeleton 〜ない以上、…ことになる; subject: 病院の案内図と予約票の番号のずれ（一日分の質問の数え）（QA F13） |
| 問題10(3) | 住まい | 主張 | — (unnamed; **round 2 R-1**: was `A だけではない。B こそが〜`, now no named template and no not-A-but-B member on the paper) | 一人称の前後比較 (**round 2 R-1**, was 〈想定→実は〉: cross-half cap reached by 聴解2-3番+3-2番. Before = PRACTICE of storing everything in the back closet; after = shelf/drawer where things are used. Legal: paper-wide 2→3 = cap; 20260929_1 問題10 used it once, so no per-大問 bar) | いつも使う物のしまい場所は、使う場所からすぐ手の届くところに決めておくとよい。 — 主張 kept (prescription to the reader); skeleton 〈N〉は、…ところに決めておくとよい — differs from 問題9 〈〜ても、〜があれば、〜ことができる〉 and 11(2) 〈前のN〉は、今では〜として…残っている; subject unchanged: 収納の置き場所 |
| 問題10(4) | 環境 | **実用文・分類外** (business email) | — | （実用文） | （実用文の結び）「よろしくお願いいたします。」 — subject: 使い終わったインク容器の引き取りを尋ねるメール |
| 問題10(5) | デジタル化 | 条件提示 | — (unnamed). **Not 相関** (`A では/ほど B が多い`); must differ from 13's skeleton | 反論への応答 (**QA round 1 swap**, was 機構の説明: 客の「この機能はあてにならない」を認めて条件で答える。11(1) が 機構の説明 を取るため) | 充電器と家の無線の両方につながったまま画面の消えている時間が来るまで、写真は電話の中で順番を待っている。 — skeleton 〈条件〉が来るまで、〈物〉は…待っている; subject: 写真の自動保存が動く条件 |
| 問題11(1) | 科学・技術 | 説明 | `〜のは B だ（分裂文）` (the paper's one cleft; 問題11 carries no cleft bar — 20260929_1 closed 問題11 only on `A というより B`) | 機構の説明 (**QA round 1 F3**, was 反論への応答, at cap) | 凍った物を電子レンジで温めるときに大切なのは、熱くなった所の熱を、冷たい所へ分ける時間をとることです。 — 分裂文 (the paper's one); subject (F3 re-author): 冷凍食品を電子レンジで温めるとむらができる仕組み（袋の温め方の一行の理由）; persona 職業人; not a measurement/protocol subject; not 20260929_1 問題13's 気温 domain |
| 問題11(2) | 文化・伝統 | 随筆 | — (unnamed). Must differ from 問題9's skeleton | 一人称の前後比較 | 子どものころ初めの音で覚えた札は、今では一つの歌として、読む人の声と一緒に耳に残っている。 — skeleton 〈前の実践のN〉は、今では〜として…残っている; subject: かるたの読み手をして変わった取り方 |
| 問題11(3) | 食 | 反論応答 | — (unnamed). **NOT `A というより B`** (cross-paper bar: 20260929_1 11(4)) | 反論への応答 | それで今は、味噌汁や炒め物には粉を使い、瓶のだしは、湯豆腐やおひたしのように、味つけのうすい料理の日に回している。 — skeleton 反論を認めたうえでの使い分け; subject: 家で取るだしと粉のだし |
| 問題11(4) | スポーツ・余暇 | 意外な観察 | — (unnamed). **NOT `A というより B`** (bar). Not a cleft (11(1) holds it). Must differ from 10(2) | 機構の説明 | 下りでは、筋肉が伸ばされながら体の重さを受け止めるので、息は楽なままでも、脚には翌日まで残る傷がついていく。 — skeleton 〜ので、…ままでも、…V-ていく; subject: 山の下りで脚が痛む仕組み |
| 問題12(A) | 消費・経済 | 主張 | — (unnamed). Not the not-A-but-B family (10(3) holds it). Read against 12(B) first | 反論への応答 (A+B = one surface) | 毎日決まった量を使う物は、一度に多めに買っておくのが、家計にとって賢いやり方である。 — skeleton 〜のが、…賢いやり方である; subject (A+B): 日用品のまとめ買い |
| 問題12(B) | 消費・経済 | 説明 | — (unnamed). Not a cleft. Must differ from 12(A) and from 11(1) | ″ | まとめ買いの安さは、使うより先にお金を払い、そのお金が何か月もかけて品物の形で戻ってくるという仕組みの上に成り立っています。 — skeleton 〈X〉は、…という仕組みの上に成り立っている (QA F4 re-angle: 先払いで手元のお金が減るという異論; cue/visibility/storage を離れた) |
| 問題13 | 人間関係 | 条件提示 | — (unnamed). **NOT 分裂文** (cross-paper bar: 20260929_1 問題13). Not 相関 either; must differ from 10(5) | 機構の説明 | 会の終わりに次の名前が決まっている集まりでは、帰り道の「また頼むね」は、ただのお礼の言葉として受け取られます。 — skeleton 〜ている〈集団〉では、Xは…として受け取られる（相関でない: 数量の増減なし）; subject: 仲間内の幹事役が一人に決まる仕組み |
| 問題14 | 防災 | (outside axis 2 — flyer, no closing) | — | （実用文） | — |

## Who owns which rows

- **The 問題9 cloze row belongs to the 文法 (問7–9) author.**
  `scaffold_sections.py` emits the cloze inside `問7-9_文法.md`. Both authors get
  this whole table, because the caps are counted across all thirteen closings.
- **問題10–14 belong to the 読解 author.**

## The previous paper (20260929_1), per 大問 — what is barred here

Read from its shipped `tests/20260929_1/言語知識・読解.md` with the gate's own
`dokkai_templates_by_daimon()` / `passage_final_sentence()` (the finals match
`qa/dokkai-allocation-20260929_1.md` and `qa/stage3-report-20260929_1.md` §5).

| 大問 | 20260929_1 named templates | 20260929_1 MOVEs |
|---|---|---|
| 問題9 | none (unnamed 「AはBになる」) | 機構の説明 |
| 問題10 | none (10(1) 〈N〉には〈X〉が詰まっている; 10(4) 〜かどうかで〜かどうかが変わる; 10(5) 〈人〉は、〈目的〉ために〜V-ている; 10(2)(3) 実用文) | 一人称の前後比較 (10(1)), 数えたことの報告 ×2 (10(4), 10(5)) |
| 問題11 | **`A というより B`** (11(4)); the rest unnamed (11(1) 今の〈私〉は〜ことを考えている; 11(2) 〜ていくと、XはそのままYになった; 11(3) 〜べきだと思います) | 一人称の前後比較 ×2 (11(1), 11(3)), 反論への応答 (11(2)), 〈想定→実は〉 (11(4)) |
| 問題12 | none (A 〜条件は二つで、〜ことと〜ことである; B 〜では、〜分だけ、〜てしまう) | 機構の説明 |
| 問題13 | **分裂文** | 反論への応答 |

**Template bar (gated, `check_dokkai_template_repeat_prev_paper`):** no 問題11
surface closes on `A というより B`; 問題13 does not close on 分裂文 (incl.
「大切なのは」「注目すべき点は」 variants). Also do not reuse an UNNAMED skeleton
from the table above in the same 大問 — the gate cannot see it, QA can.

**MOVE totals in 20260929_1 (10 essay surfaces):** 一人称の前後比較 3,
機構の説明 2, 数えたことの報告 2, 反論への応答 2, 〈想定→実は〉 1.

## The new MOVE cross-paper bar is unsatisfiable as literally written — the reading applied here

`dokkai.md` MOVE table: "A MOVE the previous paper used twice may be assigned
at most once here." 20260929_1 used **every** non-skeleton MOVE at least twice
(above). Read paper-wide, this paper could then assign 機構の説明 1 +
数えたことの報告 1 + 一人称の前後比較 1 + 反論への応答 1 + 〈想定→実は〉 2 = **6
slots for 10 essay surfaces**. No allocation exists. The same is true of nearly
any pair of consecutive papers: ten surfaces over five MOVEs with caps 2/3/3/3/3
force at least three MOVEs to ≥2, so the next paper is always left short.
**This is a rule defect. It needs an owner ruling** (AGENTS.md §0).

What this table applies instead, pending that ruling:

1. **Per 大問, which is how the rule's parent is scoped.** F7's root-cause row
   says "extend the new cross-paper TEMPLATE bar to the MOVE column", and the
   template bar is per 大問. So a MOVE that 20260929_1 used twice inside one 大問
   gets at most one surface in that 大問 here:
   - 問題10 had 数えたことの報告 ×2, so here it gets **1** (10(2)).
   - 問題11 had 一人称の前後比較 ×2, so here it gets **1** (11(2)).
   - Both are satisfied.
2. **Paper-wide, as close to the literal text as 10 surfaces allow.**
   - 数えたことの報告 is the MOVE F7 was about. It gets exactly **1** surface on
     the whole paper, which is literal compliance.
   - 一人称の前後比較 was at cap (3) and drops to **2**.
   - 〈想定→実は〉 stays at **1**, leaving headroom for the 聴解 half (see below).
   - That leaves 6 surfaces for 機構の説明 and 反論への応答, and each gets **3**
     (its cap). Both were at 2 in 20260929_1, so the literal bar is broken
     for these two, and for 一人称の前後比較, by one surface each.
3. **No surface carries the same MOVE as the same seat in 20260929_1.** Every row
   moved.

Proposed rule text for the owner: 「A MOVE the previous paper used twice IN ONE
大問 may be assigned at most once in that 大問, and 数えたことの報告 (the F7
MOVE) at most once per paper while the previous paper ran it twice.」

## Persona bar: 「〈役〉が〈N年分〉を数える」 is OFF this paper

20260929_1 ran it twice: 10(4) 世話役が6年分, 10(5) 役場職員が2年分. Per the
bar, it may not repeat within two papers. So the one 数えたことの報告 row (10(2)
医療・福祉) must not be:

- a role-holder counting multi-year records, sheets, postcards or notebooks;
- a counting role (世話役, 係, 担当, 職員) reading back N years of anything.

Use a single, bounded count instead, for example one week, one day, or one
batch. Do not introduce the count as contradicting an expectation either:
that is the 〈想定→実は〉 re-skin.

## 問題9's theme is AUTHOR-COMPOSED; メディア・情報 was drawn by RNG from three legal values

- **Rule 3.** The 12 drawn themes are taken: 子育て・家族, 医療・福祉, 住まい,
  環境, デジタル化, 科学・技術, 文化・伝統, 食, スポーツ・余暇, 消費・経済,
  人間関係, 防災. That leaves 睡眠・健康, 交通, 働き方, 教育, 地域活性化,
  行政・手続き, メディア・情報 and 旅行・観光.
- **Rule 4 / 4c** (a cloze candidate is free only if it headlines NEITHER of
  the previous two papers):
  - 20260929_1 headlined 働き方, 睡眠・健康, 科学・技術 and 教育, plus 聴解問題5
    スポーツ・余暇 and 旅行・観光.
  - 20260928_2 headlined 住まい, デジタル化, 行政・手続き and 子育て・家族, plus
    聴解問題5 スポーツ・余暇 and 旅行・観光.
  - That bars 睡眠・健康, 働き方, 教育, 旅行・観光 and 行政・手続き.
- **Legal: 交通, 地域活性化, メディア・情報.** One was picked with
  `secrets.randbelow(3)`, not by preference. It returned index 2, which is
  **メディア・情報**.

**Rule 4b, the cloze SUBJECT** (5–15 JP chars) must not match the previous
paper's 13 読解 or 21 聴解 subjects:

- 20260929_1 10(5) `広報紙の小さな欄`: a town newsletter and reader postcards
  (same theme, one paper back, non-headline). The cloze may not be about
  newsletters, 広報紙, reader postcards, or a column of readers' voices.
- 20260929_1 聴解3-3: an anime broadcast abroad and translated manga. Stay off
  overseas broadcasting and translation of comics.
- 20260928_2 has no メディア・情報 surface.
- The full used list for this theme is 28 subjects, from
  `used_subjects_by_theme()['メディア・情報']`. Stay off all of them and off any
  re-wording. Among them are:
  - graph axes;
  - AI summaries;
  - source-tracing and misinformation;
  - review stars;
  - notification-off reading;
  - streaming plans;
  - e-books;
  - subtitles;
  - press photographers;
  - local-paper closure;
  - interview notes checked before print;
  - weather-forecast probability.

The cloze is 一人称の前後比較, so its "before" must be a PRACTICE the narrator
had, never a belief they held.

## Why 実用文 sits at 10(1) and 10(4) — RNG

The slots used for 実用文 in recent papers:

- 20260929_1 used 10(2) and 10(3).
- 20260928_2 used 10(1) and 10(5).
- 20260928_1 used 10(2) and 10(4).

10(4) is the only slot neither of the previous two papers used, so it takes one.
The second slot came from `secrets.randbelow(2)` over {10(1), 10(5)}, the two
slots used only two papers back, and returned **10(1)**. A second
`secrets.randbelow(2)` decided which slot gets the notice. It put the
**notice at 10(1)** (子育て・家族) and the **business email at 10(4)** (環境).

Constraints on the two 実用文 surfaces:

- **10(1) notice.** It may not be:
  - a school→保護者 textbook notice (20260928_2 10(5));
  - a チャイルドシート rental (20260928_2 14);
  - a 回覧板 and app notice (20260929_1 10(2)).
- **10(4) email.** It may not be:
  - a handover between contacts (20260929_1 10(3));
  - a commission-a-workshop request (20260928_2 10(1)).
  - Also stay off シャツ re-use (20260929_1 聴解2-3, 環境).

## Why 〈想定→実は〉 is at 10(3), and 1 not 2

- **Seat.** 20260929_1 ran the skeleton at 11(4) on 食, with the bowl
  experiment. This paper's 11(4) and 食 (11(3)) are both kept off it, so the
  same seat and the same theme do not carry it two papers running.
- **Count.** The cross-half cap is 2, and it counts the composed 聴解 talks
  (`jlpt-test-generation` §"One topic, one surface"). 20260929_1 reached 2 that
  way (11(4) + 聴解3-2). Stage 3 re-angles 10(3) only if the composed 聴解 half
  carries **two**. If it does, 10(3) may NOT move to 数えたことの報告
  (that MOVE is spent) and may not move to 反論への応答 or 機構の説明 (both at
  cap 3). Its only legal target is 一人称の前後比較 (2 → 3), written on a
  PRACTICE, not a belief. Otherwise the 聴解 draw is
  reported and the 読解 side keeps 1.
- **Deletion test.** Applies to 10(3), and to nothing else.

## 10(3)'s template was drawn by RNG

10(3) carries the paper's one not-A-but-B family member. Any of the five named
family templates was legal in 問題10, because 20260929_1 closed 問題10 on no
named template. `secrets.randbelow(5)` over [ではなく, より…ほう, だけではない…こそ,
というより, わけではない] returned index 2, which is **`A だけではない。B こそが〜`**.
That is also the 主張 shape's stock form. Name the foil A in the final, and keep
「こそ」 to the final; do not let it recur elsewhere in the passage.

## Headline subjects — what the rule-4b diff must stay clear of

Headline themes, checked:

- 問題12 消費・経済, 問題13 人間関係 and 問題14 防災 headline neither 20260929_1
  nor 20260928_2.
- So there is no consecutive repeat, and the two-back budget of one is unspent.
- Rule 4 is clear for the 読解 headline set. This paper's 聴解問題5 theme is not
  known until `make mp3` (a WARN-only draw audit).

Each headline surface gets a 5–15-char SUBJECT. Diff it against:

- **問題12 消費・経済 (A+B, one subject).**
  - 20260929_1 11(1) `着る日から買う服` and 20260928_2 11(1) `雑貨店の傘の売れ方`:
    no clothes buying, no sale timing, no shop sales records.
  - 聴解 (20260929_1): a coupon at the register, bakery advertising, a gift box
    with flowers, change from a vending machine, a cloak-room offer.
  - 聴解 (20260928_2): paying a seminar fee by transfer, an earphone sell-out.
  - So no coupons or discounts at the till, no shop publicity, no gift
    packaging, no payment-method choice.
  - 12 is 反論への応答 as a pair: A takes a position, and B takes a named
    objection seriously. Neither side is a strawman.
- **問題13 人間関係.**
  - 20260929_1 10(3) `電話だけの取り決めの引き継ぎ` (an email).
  - 20260928_2 10(3) `二度目のお礼`.
  - 聴解: a 50-year sweets shop, a chance reunion, an apology.
  - So no thanking, no handovers, no workplace forms of address
    (20260928_1 12).
  - 13 is 機構の説明 closing on a non-相関, non-cleft 条件提示. It explains how
    something between people works, and denies no assumption.
- **問題14 防災.**
  - 20260928_2 11(4) `119番の質問`: no emergency-call procedure.
  - 20260928_1 11(1) `ブロック塀の点検`: no wall inspection.
  - The flyer may not be a rental 案内 or a 親子 event programme (recent 問題14
    types). Pick a different document type or errand.

## Non-headline subjects off-limits from the previous two papers

These are per theme, from `logs/topics.json`. A re-wording counts as used.

- **10(2) 医療・福祉:**
  - not a vet or pet illness (20260928_2 聴解2-6);
  - not doctor shortage or scholarships (20260929_1 聴解3-5).
- **10(3) 住まい:**
  - not moving boxes (20260929_1 10(1));
  - not house creaks or wood shrinkage (20260928_2 問題9).
- **10(5) デジタル化:**
  - not a 回覧板 app (20260929_1 10(2));
  - not phone memos being re-read (20260928_2 12).
- **11(1) 科学・技術:**
  - not thermometer placement or official temperatures (20260929_1 13).
  - 11(1) is a 反論への応答 closing on the paper's one cleft: the objection is
    real and answered on its own terms, with no 「もっとも」 knock-down.
- **11(2) 文化・伝統:** not dyeing or 手ぬぐい (20260928_2 10(1)).
- **11(3) 食:**
  - not bowl size and portion (20260929_1 11(4));
  - not vegetable intake (聴解3-4);
  - not portion too large (聴解4-4).
- **11(4) スポーツ・余暇:**
  - not swimming breath practice (20260928_2 10(2));
  - not a swimming-club membership (20260929_1 聴解5-1);
  - not an athlete's retirement (聴解2-4);
  - not a kids' football class (20260928_2 聴解5-1);
  - not tidying a tent after a baseball game.

## Tallies the authors must NOT break

- **Closing shape (13).**
  - 随筆 2 (問題9, 11(2))
  - 意外な観察 2 (10(2), 11(4))
  - 主張 2 (10(3), 12(A))
  - 条件提示 2 (10(5), 13)
  - 説明 2 (11(1), 12(B))
  - 反論応答 1 (11(3))
  - 実用文・分類外 2 (10(1), 10(4))
  - Values come from the CLOSED `CLOSING_MOVES` and nothing else.
  - 反論応答 is the only shape with a spare slot.
  - No seat repeats the shape 20260929_1 or 20260928_2 put in that seat (checked
    against both papers' `closing_moves`).
- **Template.**
  - Named: `A だけではない。B こそが〜` 1 (10(3)) and 分裂文 1 (11(1)). Every
    other final is unnamed.
  - 相関 **0**.
  - The three cap-1 templates are assigned to no row: 後知れ `〜ていた のだ`,
    不在の残り `〜ていない`, and 先回り. An unnamed final that lands on one of them
    spends its only slot, so don't let one land there.
- **not-A-but-B reframe family** (ではなく／というより／よりも／だけではなく／
  わけではない, and ANY final naming a foil and preferring the alternative):
  exactly **1**, 10(3).
- **MOVE (10 essay surfaces).**
  - 〈想定→実は〉 1 (10(3))
  - 数えたことの報告 1 (10(2))
  - 一人称の前後比較 2 (問題9, 11(2))
  - ROUND 2 (R-1): 〈想定→実は〉 0 on the 読解 side (10(3) moved); 一人称の前後比較 3, at cap (問題9, 10(3), 11(2)); not-A-but-B family 0; named templates: 分裂文 1 (11(1)) only.
  - 機構の説明 **3, at cap** (11(1), 11(4), 13) — QA round 1: 11(1) took 機構の説明, 10(5) moved to 反論への応答
  - 反論への応答 **3, at cap** (10(5), 11(3), 12)
  - Headroom: 一人称の前後比較 +1 only. 数えたことの報告 has none, because of the
    cross-paper bar. 〈想定→実は〉 has none, because the 聴解 half is
    unpredictable.
- **Persona** (cap 2 per archetype). The three 反論への応答 narrators and the
  three 機構の説明 narrators must not collapse onto 解説者. 20260929_1 ran 解説者
  at 12(A) and 13 (2, at cap). Use at most 2 解説者 on this paper.
- **Voice quota** (12 essay-type passages, 問題14 excluded).
  - At least 4 in the first person. Candidates: 問題9, 11(2), 10(2) and 10(3),
    with 11(3) as a fifth.
  - At least 3 in です・ます throughout. Plan it alongside the length bands. At
    least one of 12(B), 13 and 11(1) should be です・ます.

## Tested forms that must stay out of the 読解 prose (Item integrity #15)

This paper keys the following (read the spec, not this copy, if anything
rerolls):

- **問題7:** 〜ところだった, 〜っぱなし, 〜ざるを得ない, 〜といっても,
  敬語:申し上げる, 〜ことなく, 〜ものがある, 〜と言っても過言ではない,
  〜といい〜といい, 〜はさておき, 〜にわたって, 〜にしたがって.
  - 敬語 count 1 of 12, inside the cap of 2.
- **問題8:** 限定表現(〜のみならず…も), 〜に先立って, 〜にしては, **〜ことから**,
  〜どころか.

Consequences:

- **敬語:申し上げる is keyed.**
  - It is the stock closing of the 10(4) business email (「よろしくお願い申し上げます」,
    which 20260929_1 10(3) closed on) and of the 10(1) notice and the 問題14
    flyer (「お知らせ申し上げます」).
  - No 「申し上げ」 anywhere. Use 「よろしくお願いいたします」 instead.
    いたす is not keyed on this paper.
- **〜に先立って:** no 「に先立ち／に先立って」 in the notice, the email or the
  flyer (「説明会に先立ち」 is the reflex).
- **〜にしたがって:** no 「にしたがって／に従って／に従い」, including 「指示に従って」
  in the 防災 flyer and the notice. To be safe, also no sentence-initial
  「したがって」.
- **〜にわたって:** no 「にわたって／にわたり／にわたる」. 「長年にわたって」 is the
  reflex in 一人称の前後比較 and 数えたことの報告.
- **〜ことから is a general-purpose frame, so a prose grep is owed**
  (`exam-blueprint` §"A `grammar_p8` draw whose form is a general-purpose
  sentence pattern").
  - 「…ことから、」 is the stock causal link of 説明, 機構の説明 and 意外な観察
    prose: 10(2), 10(5), 11(1), 11(4), 12(B) and 13.
  - Grep every surface. Re-word every hit but at most one, and that one must
    not be in the tested 「〜ことから（理由・根拠）」 frame. Prefer 0.
- **〜のみならず…も:** no 「のみならず」. Prefer 「だけでなく」 sparingly, and not in
  10(3), which holds the だけではない final.
- **〜ざるを得ない, 〜と言っても過言ではない, 〜ものがある:** these are the
  reflex endings of 主張 and 随筆 prose (10(3), 12(A), 問題9, 11(2)). None
  anywhere.
- **〜といっても:** no 「といっても／と言っても」 as a connective. It leaks into
  反論への応答 concessions (11(1), 11(3), 12).
- **〜ところだった, 〜っぱなし, 〜ことなく, 〜どころか, 〜にしては, 〜はさておき,
  〜といい〜といい:** none anywhere.
  - 「〜ところだった」 is the near-miss ending of first-person anecdotes.
  - 「つけっぱなし／出しっぱなし」 leak into 住まい and 環境 prose.
- **Stage 3 re-grep.** Every form above goes into the Stage-3 keyed-form re-grep
  with its counts and frames.

## The two things that get checked by hand

1. **The unnamed finals must not share a skeleton with each other, or with the
   named ones.** The pairs at risk:
   - 問題9 vs 11(2) (both 随筆, both 一人称の前後比較);
   - 10(2) vs 11(4) (both 意外な観察);
   - 10(5) vs 13 (both 条件提示, both NOT 相関, so two DIFFERENT non-相関
     condition skeletons are needed);
   - 11(1) (cleft) vs 12(B) (説明, not cleft);
   - 12(A) vs 12(B). Read A against B FIRST.

   Also read each final against 20260929_1's final in the same 大問 (quoted in
   `qa/dokkai-allocation-20260929_1.md`).
2. **Apply the deletion test to 10(3), and to nothing else.** Every other row
   carries no attributed assumption and no denial.
   - **10(2) and 11(4) (意外な観察):** the mismatch is a FACT, not a belief that
     gets corrected.
   - **問題9 and 11(2) (一人称の前後比較):** the "before" is a PRACTICE the
     narrator actually did. 「つもりだった」 or 「と思っていた。ところが」 is the
     re-skin.
   - **10(2) (数えたことの報告):** the count is not introduced as contradicting an
     expectation, and it is not an N年分 record count (persona bar).
   - **11(1), 11(3) and 12 (反論への応答):** the objection is taken seriously and
     answered on its own terms. Three of these on one paper is the cap, so vary
     how each one is set up:
     - 11(1): a colleague's or a reader's objection;
     - 11(3): the narrator's family;
     - 12: A vs B.
     None may open 「もっとも」 and then knock the objection down.
