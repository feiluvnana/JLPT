# Stage 3 (build + gate) — 20260928_1

Run 2026-09-28 in one context. This context authored nothing, and it changed no
authored wording.

## 1. What I read, in full, from disk

- `AGENTS.md`, `CLAUDE.md`
- `.agents/exam-app/SKILL.md` (whole file)
- `.agents/choukai-audio/SKILL.md` (whole file, Part 0 first)
- `.agents/jlpt-test-generation/SKILL.md`: the pipeline table, the reading map,
  §"Stage 3 — build + gate" and §"One topic, one surface" (whole)
- `qa/dokkai-allocation-20260928_1.md` (the binding allocation, including the 13
  final sentences)
- `logs/topics.json`: the rows for `20260917_1` and `20260914_1`, all fields
- I also read these while resolving specific lines:
  - `exam-blueprint/SKILL.md` §"What still governs a self-authored surface",
    §"The four theme rules" (rules 1–5, 4b, 4c) and §"Mutually exclusive form
    families"
  - `tools/check_consistency.py`: `_headline_parts`, `check_topics_themes`, and
    the `THEME_TOKENS` table
  - `qa/stage3-report-20260917_1.md`, for how earlier stage-3 reports disposed
    of the same classes of finding
- Inputs:
  - the three `tests/20260928_1/_sections/*.md` fragments, through the merged
    `言語知識・読解.md`, which I read from 問題7 to the end of the key
  - `tests/20260928_1/test_spec.json`
  - the composer's `聴解スクリプト.txt` and `聴解.md` (read in full)
  - `logs/choukai_draws.json`

## 2. Every command I ran, in order

```
make assemble 20260928_1
make autofix 20260928_1                      # clean, nothing changed
make lint-draft 20260928_1                   # clean
make verify-scramble 20260928_1              # exit 0; all five UNDECIDED (see §7)
make mp3 20260928_1 SEED=71649214            # the only seed used
python3 tools/choukai_segment.py tests/20260928_1/聴解.mp3
make upload-files TARGET=tests TEST=20260928_1   # BLOCKED: gh auth (see §8)
make booklet 20260928_1
make sheet 20260928_1
make check                                   # run 1: 2 FAIL
make findings                                # to attribute WARNs to test ids
make check                                   # run 2, after the topics.json row: 3 FAIL
make check                                   # run 3, after the notes patch (final, §7)
```

**Seeds.** I used exactly one: `71649214`, verbatim from the brief. There was no
re-draw, so no other seed was tried.

## 3. What I wrote

- `tests/20260928_1/言語知識・読解.md`: written by `make assemble`, and not
  touched afterwards (autofix found nothing to change).
- The whole 聴解 half, written by the composer:
  - `聴解スクリプト.txt`, `聴解.md`, `聴解.mp3` and `聴解_チャプター.json`
  - the 30 聴解 entries in each `詳細解説` pane
- `言語知識・読解.html`, `聴解.html`, `解答.html`, `練習.html`: written by
  `make booklet` and `make sheet`.
- `logs/choukai_draws.json`: one row appended by the composer. The 29 earlier
  rows are byte-identical to the pre-run copy.
- `logs/topics.json`: one row appended for 20260928_1. It has these maps:
  - `surfaces`, `themes`, `shapes` (all 29 聴解)
  - `closing_moves`, `voices`, `persona`, `claim`
  - `notes`

  Every 「…」 span was checked against the paper before the append; the gate
  reports 41 of 41 spans found. The persona cap is at most 2 (生活者, 職業人 and
  論者 have two each). No other row changed.
- **Not written:** `logs/upload_manifest.json`, because the upload was blocked
  (§8).

## 4. The whole-paper table

### 4.1 読解 + 問題9 cloze

What was drawn for each surface: `test_spec.json` `reading_topics[i]` gives a
theme and an avoid list only. There is no drawn subject string. So the drawn
column below is the theme, and "on draw" means that the shipped subject is
about that theme and matches none of the entry's avoid strings or rewordings of
them. I checked all 12 against their avoid lists; none matches.

| surface | shipped subject | theme (shipped = drawn) | on draw | closing | final-sentence template | MOVE | 20260917_1 same seat | 20260914_1 same seat |
|---|---|---|---|---|---|---|---|---|
| 問題9 | 案内板で乗り換える (phone route guidance → station signboards) | 交通 (author-composed) | yes | 随筆 | unnamed (`…が、今では…になってつながっている`) | 一人称の前後比較 | 緑のカーテン | 共同編集の書類 |
| 10(1) | 杖を反対の手で持つ理由 | 医療・福祉 | yes | 説明 | unnamed (`…分だけ…軽くなる`, proportional; see §5.2) | 機構の説明 | 窓口の開く時間帯 | 祭りの笛 |
| 10(2) | 保育園の門の暗証番号化と迎えの事前連絡 | 子育て・家族 | yes | 実用文 | — | （実用文） | 旅の絵はがき | 手話通訳の立ち位置 |
| 10(3) | 夕食後のうたた寝が夜の眠りを切る | 睡眠・健康 | yes | 意外な観察 | 分裂文 | 〈想定→実は〉 | 弁当屋へのメール | 町のメール件名依頼 |
| 10(4) | 年末の会で借りる食器は洗って返すかのメール | 環境 | yes | 実用文 | — | （実用文） | 町内会の屋上駐車場 | 踏切の遮断時間 |
| 10(5) | 給料日の書き出しと月末の不足（相談記録3年分） | 消費・経済 | yes | 条件提示 | 相関 (`ほど`) | 数えたことの報告 | 古道具の直した跡 | 値札改定のお知らせ |
| 11(1) | 通学路のブロック塀点検への反対に応じる | 防災 | yes | 反論応答 | `わけではない` | 反論への応答 | 紹介のしかた | 届け出と役の継続 |
| 11(2) | 窓を開ける5分と外の季節 | 住まい | yes | 随筆 | unnamed (`…おかげで…ようになった`) | 一人称の前後比較 | 教室の30分宿題 | 斜面の植樹 |
| 11(3) | 無人駅の待合室の当番が続く組 | 地域活性化 | yes | 条件提示 | unnamed (`この二つがそろえば…`) | 数えたことの報告 | 通路の私物 | 洗濯物のかご |
| 11(4) | ます目のノートと位のずれ | 教育 | yes | 説明 | unnamed (`…のである`) | 機構の説明 | 眠れない夜 | 外壁修繕の順序 |
| 12(A) | 公園の札を時間と場所を知らせる札に | スポーツ・余暇 | yes (see F1, §6) | 主張 | `というより` | 反論への応答 (A+B one) | 会報の事実確認 | 答案返却の速さ |
| 12(B) | 門の閉まった校庭を市が借りて開く | スポーツ・余暇 | yes | 反論応答 | unnamed (`…は、すでに…にある`) | ″ | ″ | ″ |
| 13 | 落語は筋を知って聞く | 文化・伝統 | yes | 主張 | unnamed (`…ことを、私は勧めたい`) | 〈想定→実は〉 | 引き継ぎ | 頼めない人 |
| 14 | 学校給食センター夏休み親子見学会 | 食 | yes | — | — | （実用文） | 犬の登録と予防注射 | 舟下りの案内 |

**Theme rules, counted on the shipped surfaces:**

- **Rule 3:** 13 of 13 読解 themes are distinct.
- **Rule 2:** no headline theme (交通, スポーツ・余暇, 文化・伝統, 食) appears on
  another 読解 surface.
- **Rule 4, one paper back (20260917_1):** no headline theme repeats. The gate's
  line is `ok`.
- **Rule 4, two papers back (20260914_1):** one repeat, 問題12 スポーツ・余暇.
  That is the whole budget, and the gate's line is `ok`.
- **Rule 1 FAILS:** 聴解問題5-1番 is tagged スポーツ・余暇 (§6 F1).

**問題12 cross-test column:** 公園のボール遊び (here), 会報の事実確認
(20260917_1), 答案返却の速さ (20260914_1). All three differ.

### 4.2 聴解: a draw audit

| slot | clip | shipped subject | theme | 20260917_1 same slot | 20260914_1 same slot |
|---|---|---|---|---|---|
| 1-1 | 2025-12:問題1-1 | ガラス体験の受付、まずエプロン | スポーツ・余暇 | 携帯店の留守電 | 合唱サークルのポスター |
| 1-2 | soumatome:cd2-32 | 図書館の休館日、土曜に来る | 教育 | 説明会の作業分け | 就活の問い合わせ |
| 1-3 | 2025-12:問題1-3 | オーケストラのパンフ、先輩に原稿依頼 | スポーツ・余暇 | 家具の寄付 | **same clip** |
| 1-4 | 2023-12:問題1-4 | 市民文化祭の応募、申請書を提出 | スポーツ・余暇 | レストランの追加注文 | ホテルの行程 |
| 1-5 | soumatome:cd2-3 | 文化祭ライブ、手伝いの人を手配 | 教育 | 学生証の再発行 | 説明動画を短く |
| 2-1 | kanzenmoshi:cd1-13 | 眼鏡なのはコンタクトを切らした | 医療・福祉 | 郵便局の配達 | 講師の条件 |
| 2-2 | 2023-12:問題2-2 | 親子イベント企画、駐車場がない | 働き方 | 企業実習の期待 | 前髪 |
| 2-3 | 2021-12:問題2-3 | レポート、考察と引用の区別 | 教育 | 課長が問題にした報告 | 自転車通勤の理由 |
| 2-4 | 2021-12:問題2-4 | フリマ、値段順に並べる | 消費・経済 | 家具作りの魅力 | 高校でコーチ |
| 2-5 | 2024-07:問題2-5 | 転職の理由、新しい世界 | 働き方 | 犬の容体 | 家具を作る |
| 2-6 | kanzenmoshi:cd1-16 | 事務室へは鍵を借りに | 教育 | 就職先の理由 | 実際に使ってみる |
| 3-1 | shinkanzen:cd2-59 | 仲間言葉としての方言 | 文化・伝統 | リーダーを断る | 片付けの効果 |
| 3-2 | archive:2014-12:問題3-2 | 同じミスを繰り返さない方法 | スポーツ・余暇 | 夏の体調不良 | 地元のごみ |
| 3-3 | 2025-12:問題3-3 | 子どもを注意するとき | 子育て・家族 | 高齢者の社会貢献 | 忘れ物の留守電 |
| 3-4 | archive:2014-12:問題3-4 | 蜂を飼う際の注意 | 環境 | 通販の利用理由 | 館内放送 |
| 3-5 | 2021-07:問題3-5 | 議員、道路と橋の整備を | 交通 | 雲の発生 | メールを使う理由 |
| 4-1…11 | 2024-12:4-1, kanzenmoshi:cd1-33, 2025-07:4-3, 2021-07:4-4, 2024-12:4-5, 2021-07:4-6, 2023-12:4-7, soumatome:cd2-46, kanzenmoshi:cd1-35, shinkanzen:cd2-71, 2025-07:4-11 | see the `shapes` map | 働き方×5, 人間関係×3, 睡眠・健康, 食, 交通 | — | 4-6 is the **same clip** |
| 5-1 | 2022-12:問題5-1 | ダンスコンテスト、手に持つ小道具 | スポーツ・余暇 | 和菓子店の貼紙 | 演劇部の衣装 |
| 5-2 | 2025-12:問題5-2 | 四種の自転車、女3番・男2番 | 消費・経済 | 科学イベント | 防災体験会場 |

## 5. The reads, one axis at a time

### 5.1 MOVE column, read down on its own

Within 読解, the counts match the binding allocation exactly:

| MOVE | surfaces | count |
|---|---|---|
| 機構の説明 | 10(1), 11(4) | 2 |
| 数えたことの報告 | 10(5), 11(3) | 2 |
| 一人称の前後比較 | 問題9, 11(2) | 2 |
| 〈想定→実は〉 | 10(3), 13 | 2 |
| 反論への応答 | 11(1), 12 | 2 |

**The skeleton read** uses the three-beat rubric: an attributed assumption, an
explicit denial, then 実は Y. It covers the ten essay surfaces, with 12 A+B
counted as one.

- **Conservative count: 2.**
  - 10(3): 「と言われ…」, then 「ところが」, then 「…のは…うたた寝だった」.
  - 13: 「私も長く思っていました」, then 「ところが」, then the recommendation.
- **With borderline surfaces: 3.** The borderline one is 11(1): an attributed
  objection, then 「用紙は…求めていません」, then `わけではない`.
- **Not counted, with reasons:**
  - 11(2)'s 「思いがけず増えたものもある」 adds a gain; it denies nothing.
  - 12(B) concedes a worry and hands it to another party; it denies nothing.
  - 問題9 and 11(2) both have a PRACTICE as their "before", not a belief, which
    is what the allocation asked me to check.
- **Deletion test** (the two 〈想定→実は〉 rows only):
  - 13 collapses without its denial, so it is genuinely on the skeleton.
  - 10(3) survives the deletion: the nap mechanism still stands without the
    「年齢のせい…ところが」 frame. Its three beats are explicit, so it counts as on
    the skeleton, but its argument does not need them. That makes it the cheap
    repair for F2.
- **Against the gate and the official band:** the gate prints `1 of 13`, its own
  marker-bearing instrument. Official is 3–4 of 9 conservative, as owned by
  `qa-report-20260911_1` §"F3 の根拠". This paper sits at or below the official
  band, so there is no monoculture inside 読解.

### 5.2 TEMPLATE column, read down separately

Named templates:

- 分裂文 ×1 (10(3))
- 相関 ×1 (10(5)), or ×2 if 10(1)'s proportional 「…分だけ…軽くなります」 is read
  as 相関. Either way it is within the cap of 2.
- `わけではない` ×1 (11(1))
- `というより` ×1 (12A)

The not-A-but-B family has exactly two members (11(1), 12A), as allocated.

I read the unnamed finals down as a column. 問題9 (「今では…つながっている」) and
11(2) (「…おかげで…ようになった」) are both after-state closings of the MOVE
they share, but in different grammar. No two unnamed finals share a skeleton.
**No template is over its cap.**

### 5.3 The 読解 and 聴解 rows read as ONE list

- **問題9 (station signboards) × 問題11(3) (unmanned-station waiting-room
  rota): NOT a finding.** This is the item the brief asked me to adjudicate.
  - They share the setting 駅 only.
  - The subjects differ: wayfinding by signboards versus what keeps volunteers
    on a rota. 11(3) says nothing about trains, platforms or signs; the station
    is its backdrop.
  - No number or condition carries from one surface to the other.
  - The theme tags differ (交通 / 地域活性化). Each tag is honest from its own
    prose: 11(3) is about residents running a community rota.
  - The rule bars one topic on two surfaces. It does not bar one setting.
- **問題14 (給食センター夏休み親子見学会) × 聴解問題2-2番 (toy company's 幼児向け
  夏休み親子体験イベント; the key is 会場に駐車場がない):**
  - They share a domain, a summer parent–child event, and both mention parking
    (the flyer says 「駐車場は10台分しかありません」).
  - Nothing transfers: no 問題14 item keys on parking, and 2-2 is answered from
    its own dialogue.
  - The rule allows a shared domain here, because nobody chose the 聴解 item's
    domain. So this is not a finding. It is recorded for QA to read.
- **Other adjacencies, domain only:**
  - 問題9 / 聴解4-10番 (trains)
  - 10(3) / 聴解4-1番 (sleeping on hot nights)
  - 11(1) / 聴解3-5番 (unsafe structures; different objects, no shared figure)
  - 11(4) / 聴解2-3番 (classroom feedback)

  None of these shares a decisive detail. The gate's `問題14 shares no decisive
  number with any 聴解 item` line is `ok`.
- **The cross-half MOVE cap is breached: see F2 in §6.**

### 5.4 Cross-test, 読解

No 読解 subject repeats 20260917_1 or 20260914_1. Rule 4b adjacencies, all of
them "same setting, different issue", are recorded in the row's `notes`:

- **10(4) × 20260917_1 10(3):** both are a company 総務課 e-mailing a supplier
  about a company event's meals. Here the question is whether borrowed dishes
  must be washed; there it was splitting 80 lunches into two deliveries.
  Different issue, different seat.
- **10(3) × 20260917_1 11(4):** both are adult night-sleep trouble. Here an
  evening nap uses up the night's sleepiness; there the fix was leaving the bed
  instead of lying awake. Different issue, different seat. Theme reuse is legal,
  since neither surface is a headline.
- **Two papers back (minor findings):**
  - 11(3) (the rota lasts when one member is last year's hand) runs the same
    claim family as 20260914_1 11(1) (filings stay on time when one person
    holds the role for 3+ years).
  - 10(5) (a 相談窓口 reads back 3 years of records) shares its method with
    20260914_1 13 (a 窓口 reads back 10 years of records).
- **A cross-paper crutch the allocation owns, not the authors:** the 「N年分の
  記録を読み返して数える」 frame now runs twice in each of the last three papers:
  - 20260914_1: 11(1), 13
  - 20260917_1: 10(1), 11(3)
  - 20260928_1: 10(5), 11(3)

  The same goes for 「a small time-boxed daily change, then an unforeseen gain」:
  - 20260914_1: 11(3)
  - 20260917_1: 10(2), 11(4)
  - 20260928_1: 11(2)

  This is flagged for the next allocation, not for repair here.

### 5.5 Errand identity: `shapes` across three papers, read by hand

- **Two papers back, same slot, the same clip twice** (the composer bars only
  the paper immediately before):
  - `2025-12:問題1-3` (オーケストラのパンフ) was also 20260914_1 聴解問題1-3番.
  - `2021-07:問題4-6` (森君は時間を守る) was also 20260914_1 聴解問題4-6番.

  This is a minor finding, recorded rather than re-drawn: re-drawing to escape
  a repeat the composer's policy allows is seed-shopping. The earlier stage-3
  precedent recorded 2- and 3-back repeats the same way.
- **One paper back:**
  - 聴解2-2番 (課長 names the problem in a plan) and 20260917_1 2-3番 (課長
    names what went wrong in a delivery) share the "evaluator names the one
    failing point" shape.
  - 2-5番 (転職の理由) and 20260917_1 2-6番 (就職先を決めた理由) share the "why
    this company" question.

  In both pairs the errands, keys and distractor logic differ. They are standard
  問題2 ポイント理解 frames, not errand identity, so neither pair belongs in
  `MUTUALLY_EXCLUSIVE_CLIPS`.
- **4-5番 × 20260917_1 4-11番:** 〜ほかない is tested in consecutive papers
  (different clips, different reply types). Noted.
- **5-1番 × 20260914_1 5-1番:** both are "a student club picks one of four
  fixes for a performance" (dance props / theatre costume). This is the gate's
  slot-theme WARN, two papers back, and a lifted clip on both sides. Recorded.
- **Within this paper:**
  - 問題1-3/1-4/1-5 are all student music-performance preparation (a concert
    pamphlet, a festival application, a festival live room). The errands differ,
    and 1-4 and 1-5 are both 文化祭. This is a domain cluster, not a collision,
    and it is recorded for QA.
  - No personal name repeats inside one 大問.

## 6. Findings, for the orchestrator to route (NOT repaired here: each is 読解 content)

- **F1: rule 1 FAIL (the gate): 聴解問題5 and 問題12 both carry スポーツ・余暇.**
  - `make check`: `20260928_1: headline surfaces take five different themes — 聴解問題5
    shares ['スポーツ・余暇'] with a 読解 headline surface`.
  - I tagged 聴解問題5-1番 honestly from the shipped clip: a university dance
    club choosing props for a dance contest. The same clip was tagged
    スポーツ・余暇 when 20260917_1 briefly drew it at its own stage 3.
  - Re-tagging to dodge the rule is forbidden (rule 4c). Re-drawing the 聴解 half
    until the tag moves is seed-shopping, which is forbidden too.
  - So the repair is on the 読解 side: 問題12 is a headline surface and ours to
    re-angle.
  - A second gate line bears on it: `20260928_1 問題12: the shipped prose uses a
    「スポーツ・余暇」 word` WARNs. None of the 11 スポーツ・余暇 tokens occurs in 問題12,
    whose words are ボール遊び / 体を思いきり動かせる / 走り回れる. I judge the tag
    honest (children's ball play is 余暇), so this is a token-list false
    positive. But an independent reviewer might re-tag it 子育て・家族, which
    10(2) already holds. Either way 問題12 is the surface to move.
  - Proposed direction: re-theme 問題12 onto a theme that is free for this paper.
    None of the 12 drawn themes is free. Of the rest, rule 4 bars 20260917_1's
    headlines (環境, メディア・情報, 働き方, 行政・手続き). That leaves 人間関係,
    デジタル化 and 旅行・観光 (20260914_1 headlines, but the two-back budget frees
    up once 問題12 leaves スポーツ・余暇) and 科学・技術 (only on 20260917_1's
    COMPOSED 聴解問題5, which rule 4 treats as a WARN). This means a reroll of
    `reading_topics` entry 9, or an orchestrator-authored theme, then a new A/B
    pair. Only an author context can do that.
- **F2: cross-half MOVE cap exceeded (hand read; no check backs it).**
  - 〈想定→実は〉 runs on three surfaces against a cap of two:
    - 問題10(3)
    - 問題13
    - 聴解問題2-5番: 「転職というと…人もいますけど…前に勤めてた会社に何か不満があった
      わけじゃなく、新たな世界を見てみたい」. That is an attributed general
      view, then an explicit denial, then Y.
  - The rule says the 読解 side is always the one re-angled.
  - Proposed direction: 10(3) is the cheap one, because it passes the deletion
    test (§5.1). Drop the 「と言われ…ところが」 frame and let it stand as 意外な
    観察 of a habit (「本人はそれを眠ったとは数えていない」), keeping its 分裂文
    final. That leaves 13 as the paper's single 読解 surface on the skeleton.
  - The same cap read literally also puts **反論への応答** on three surfaces:
    - 11(1)
    - 12(A+B)
    - 聴解問題3-5番: 「そういった声も理解できますが…他の手段があります」
      (concede, then counter-propose)

    I flag this one with lower confidence. The cap's text was written about the
    〈想定→実は〉 skeleton, and 20260917_1's stage 3 did not apply it to other
    labels. The orchestrator should rule on whether the cap is per-label.
    Re-angling 問題12 for F1 could clear this at the same time.
- **Minor findings (no repair proposed):**
  - the two-back same-slot clip repeats (§5.5)
  - the 問題1 music cluster (§5.5)
  - the two-back claim/method echoes in 11(3) and 10(5) (§5.4)

Any edit to 問題10–14 prose for F1/F2 obliges the skill's re-grep: every
問題7/8/9 keyed form across the 読解 half, with counts and frames. The current
paper's gate line (`no 問題7/8/9 keyed form appears more than 1× in the 問題10-14
prose, or even once in the same 文末/連用/連体 frame`) is `ok`. I edited no prose.

## 7. `make check`: every line naming this test (final run)

The final run ends `FAILED — 3 problem(s)`; the whole gate prints 7417 ok,
272 WARN and 280 skip. Every line that names 20260928_1 (or that names nothing
but concerns it) is in the two tables below. The full output is saved at
`/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/82438f50-5889-4011-97f9-bf5179e64116/scratchpad/stage3-check.txt`.

### FAIL

| line | disposition |
|---|---|
| `40 exam MP3(s) are on the audio release — ['20260928_1'] differ from what was uploaded` | **Blocked, not worked around.** `make upload-files` refused. The active gh account is `td-nguyen-38`, which has no push access to `feiluvnana/JLPT`. The `feiluvnana` account is logged in but inactive. The brief said to stop and report on a gh auth failure, so I did not switch accounts. The fix is the user's: `gh auth switch --user feiluvnana`, then `make upload-files TARGET=tests TEST=20260928_1`, then commit `logs/upload_manifest.json`. |
| `20260928_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)` | **Structural at stage 3.** The 30 聴解 entries come from `make mp3`. The 71 言語知識・読解 entries belong to stage 5, which is prohibited before QA passes. 20260910_1, 20260911_1, 20260914_1 and 20260917_1 all ended stage 3 in this state. |
| `20260928_1: headline surfaces take five different themes — 聴解問題5 shares ['スポーツ・余暇']` | **F1: a content repair on 問題12** (§6). Open. |

### WARN

| line | disposition |
|---|---|
| `問題7 form-family check compares most of the draw (1/12 = 8% family-tagged)` | **True as a coverage statement.** The pool map, not this paper, is thin. **Hand read of all 12 draws:** 〜を通して is the one tagged (媒介). The only overlapping pair is **〜限り (35, 時間の許す限り) and 〜ない限り (38)**, and both are keyed. I judge them **not a family** under exam-blueprint's own membership rule ("one form spelled twice", not "shares a stem"): 限度 and 条件 are separate Shin Kanzen points, the same ruling the skill gives 〜ない限り / 〜に限らず. But a learner sees 「限り」 keyed twice in one 大問, so this is **deferred to QA to confirm**. If QA disagrees, the repair is `--reroll-one grammar_p7:<index>` plus a re-authored item, never a hand swap. |
| `問題1/2 question repeats match in PUNCTUATION too — 問題1-4番` | **False positive for this paper.** The 「、」 difference is in `tests/imported-n2-2023-12/聴解スクリプト.txt` itself (clip `2023-12:問題1-4`). 20260810_1 carries the identical WARN for the same clip. The audio is unaffected. The repair, if anyone wants one, is the import's transcript, then `make choukai-bank`, then REPLAY. |
| `問題12: the shipped prose uses a 「スポーツ・余暇」 word` | **A false positive on tokens** (ボール遊び / 体を動かす are not in the list), **but part of F1.** See §6. |
| `聴解問題5 repeats a headline theme of 20260917_1 (composed paper) — ['消費・経済']` | **Draw audit; no repair exists** (seed-shopping is forbidden). 5-2番 (bicycle choice) and 20260917_1's 消費・経済 聴解5-1番 (和菓子店の宣伝) share nothing but the tag. |
| `no 聴解 slot repeats its own theme in the previous 2 papers — 5-1番=スポーツ・余暇 (20260914_1); 2-2番=働き方 (20260917_1)` | **Rows read side by side.** 5-1: dance props against 演劇部 costume. They share a shape (a club picks one fix for a performance) but not an errand. This is a real two-back adjacency and not repairable, because both are lifted clips. 2-2: an event-plan critique against internship expectations. Different errands; the tag is the tagger. |
| `every stamped spec's pools_sha matches pools.json` (global) | Does not name 20260928_1: its spec's `pools_sha` matches. |
| `skip no 聴解1/2/3/5 errand repeats 20260917_1's` | A skip is not a pass. The `shapes` column was read by hand in §5.5. |

The two pipeline files the orchestrator changed drew no complaint:

- `sample_items.py::is_kun_target`: `問題1 訓読み mix (2 of 5, band 2-2)` is `ok`,
  and so are the ledger/spec writer lines.
- `scaffold_sections.py`, 問題12 `**A**`/`**B**` markers: the passage boxes are
  14/14 in the Markdown, in 言語知識・読解.html, in 解答.html and in 練習.html.

**verify-scramble:** all five 問題8 items print `UNDECIDED`, exit 0. This is the
tool's normal output: it knows only four junction patterns and does not decide
uniqueness. Every item's 解説 carries a per-card last-slot proof
(`ARTIFACT: ok`), and every one has `FREE UNITS: 1`, under the FAIL at 2. Those
proofs are QA's to read against the listed rival orderings.

## 8. 聴解 draw audit: result

- **Composition:** `make mp3 20260928_1 SEED=71649214` gave 45.5 min, 34
  chapters and LUFS −15.44.
- **Segmentation:** `tools/choukai_segment.py` recovers **問題1:5 問題2:6 問題3:5
  問題4:11 問題5:2**, as required.
- **Source mix:**
  - official 20, of which 2 are archive:2014-12
  - kanzenmoshi 4
  - soumatome 3
  - shinkanzen 2

  It draws from 9 sittings.
- **Against 20260917_1**, the paper `previous_slot_clips` bars:
  - 0 of 29 clip ids repeat in the same slot.
  - 0 of 9 slot-free clips repeat in ANY slot.
  - 0 of 5 preambles repeat.
  - No clip is duplicated within the paper.
- **Composer notes:**
  - the standing figure exclusion (4 items)
  - one 問題3 bar, `mimikara:cd2-14`, at 0.57 option-set Jaccard against the
    previous paper. That is the bar working as intended.
  - No slot starved, and no bar was dropped.
- **Two papers back:** 2 same-slot repeats (§5.5).
- **Slots moved:** none. This is the paper's first composition, so the new row
  has no earlier row of its own to diff against. `make mp3` ran once, and the
  29 earlier rows of `logs/choukai_draws.json` are unchanged.
- **Gate:** `no 問題3 option set repeats 20260917_1's (worst 0.077, ceiling 0.30)`
  is `ok`, and the `script_sha` stamp matches.
- **Upload: BLOCKED** (§7, FAIL 1).

## 9. What I skipped, and why

- **The MP3 upload:** blocked on gh auth. Per the brief, I did not switch
  accounts.
- **Stage 5** (`scaffold-explanations`, `model-answer`): prohibited before QA.
- **Every F1/F2 repair:** each is a 読解 content change and goes to an author
  context. I authored nothing and edited no prose.
- **Re-drawing the 聴解 half** for the two-back repeats, the 問題1 music cluster or
  the rule-1 tag: not a defect the composer's rules recognise, and doing it
  would be seed-shopping.
- **Listening to the MP3:** this environment cannot. The substitutes were the
  segmentation round-trip, the `script_sha` match and reading the full
  transcript.
- **`refs/` binaries:** not needed for any question this pass asked.
