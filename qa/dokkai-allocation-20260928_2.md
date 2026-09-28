# 読解 allocation table — 20260928_2 (BLUEPRINT-ASSIGNED, binding)

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

**Themes** come from `tests/20260928_2/test_spec.json` `items.reading_topics[i]`.
Index → surface: 0→問題10(1) … 4→問題10(5), 5→問題11(1) … 8→問題11(4), 9→問題12,
10→問題13, 11→問題14. Author each surface's SUBJECT from its entry's `theme`, and
keep it off that entry's `avoid` list and off any re-wording of an avoid string.
The spec was rerolled (`qa/blueprint-rerolls-20260928_2.md`), so read the themes
from the spec as it now stands.

| surface | theme (spec) | closing shape (≤2 each) | final-sentence template (≤2 each; foil named) | MOVE | final sentence (AUTHOR FILLS) |
|---|---|---|---|---|---|
| 問題9 cloze **(文法 author owns this row)** | **住まい** (author-composed; see below) | 意外な観察 | — (none of the named ones) | 機構の説明 | 「つなぎ目には、もう、ずれを生むほどの（51 力がたまらない）。」 — skeleton 〈場所〉には、もう、〈程度節〉ほどの〈主体〉が V-ない（程度の否定で原因を言い切る）; no foil, no cleft, not 〜ていない. Subject: 木の家が建って一、二年「パキッ」と鳴るのは乾いて縮む木がつなぎ目に力をためるため（家が鳴る音） |
| 問題10(1) | 文化・伝統 | **実用文・分類外** (business email) | — | （実用文） | 「よろしくお願いいたします。」 — closes on a request (実用文, no authorial move). Subject: さつき工業広報課からこだま染め工房への、創立50年の記念品の手ぬぐい120本を二色で染めてもらえるか、その場合も3月1日の記念式典に間に合うかを尋ねるメール（stage-3 minor: letterhead renamed from みなと電機総務課） |
| 問題10(2) | スポーツ・余暇 | **主張** (QA F2 re-allocation, orchestrator) | — (no named template; NOT 相関) | **一人称の前後比較** | 「これから泳ぎを覚えようとする大人には、最初の何回かを、水の中で息を吐く練習に使ってみてほしい。」 — skeleton 〈読み手〉には、〈期間〉を、〈練習〉に使ってみてほしい（読み手への直接の勧め＝主張、named template なし、foil なし、not 相関）. MOVE 一人称の前後比較: before = the narrator's own PRACTICE (息が苦しくなるまで休まずに泳いでいた), after = the new practice (まず十五分、壁につかまって息を吐く); no third-party belief, nothing corrected, no counting and no records. **Differs from 10(3)** (〈主体〉は〈人〉のもとへ〈物〉を運んでいく, a non-prescriptive motion metaphor) **and 11(3)** (〜たびに…一つ増えます, a non-prescriptive proportion): 10(2) alone ends on a prescription to the reader. Subject: 四十歳を過ぎて泳ぎを習い直す筆者が、息が切れるまで泳ぐのをやめ、最初の十五分を壁につかまって水の中で息を吐く練習にしたら水を飲まなくなった（泳ぎ始めの息の練習）. Superseded twice: 将棋教室の受付表 (stage-3 F4), then 山歩きの手帳 条件提示/相関/数えたことの報告 (qa-report-20260928_2 F2) |
| 問題10(3) | 人間関係 | 随筆 | — | 一人称の前後比較 | 「あとから届くお礼は、手を貸した人のもとへ、その手助けの続きを運んでいく。」 — skeleton 〈主体〉は、〈人〉のもとへ、〈物〉を V-ていく（移動の比喩で一般化、処方なし）; before = the narrator's PRACTICE (その場で礼を言って終わり). Subject: 手伝ってもらったことのその後を、日をおいてもう一度お礼として伝える（二度目のお礼） |
| 問題10(4) | 働き方 | 説明 | `〜のは B だ（分裂文）` | 機構の説明 | 「予定がずれ込むとき、その遅れの多くを占めているのは、この待つ時間です。」 — skeleton 〈…の〉は、〈B〉です（分裂文）; no assumption denied anywhere. Subject: 仕事の見積もりに入りにくいのは手を動かさずに確認や返事を待つ時間で、それが何度も繰り返されて予定がずれる（見積もりと待つ時間） |
| 問題10(5) | 教育 | **実用文・分類外** (notice / お知らせ) | — | （実用文） | 「ご家庭でも、朝のうちにひと声かけていただけますよう、お願いします。」 — closes on a request (実用文). Subject: すずかけ中学校から保護者への、12月から一部の教科書を教室に置いて帰れるが、宿題に使う教科書は持ち帰らせてほしいというお知らせ（stage-3 minor: school renamed from あおば市立ひがし中学校） |
| 問題11(1) | 消費・経済 | 意外な観察 | — (must NOT share 問題9's skeleton) | 数えたことの報告 | 「朝から降る日に来る客は、自分の傘を片手に、この店の戸を開けるのだ。」 — skeleton 〈人〉は、〈物〉を片手に、〈場所〉を V-る のだ（場面の描写で原因を示す）; no foil, no cleft, not 〜ていない. **Differs from 問題9** (〈場所〉には、もう、〈程度節〉ほどの〈主体〉が V-ない): affirmative scene vs degree-negation, no 「には、もう」. Subject: 駅前の雑貨店のノート十年分で、傘は雨の強さと結びつかず、晴れた朝のあと昼過ぎに降り出した日に売れていた（雑貨店の傘の売れ方） |
| 問題11(2) | 地域活性化 | 主張 | `A より B のほうが〜` (foil = A, named in the final) | **〈想定→実は〉** | 「空いた店に新しい店を呼び込むことより、今ある店の一角を貸し出すことのほうが、商店街の明かりを長くともし続ける力になる。」 — skeleton A ことより B ことのほうが〜力になる (foil A = 新しい店を呼び込むこと, named). The one 〈想定→実は〉 surface: 多くの町がそう考え → ところが三軒しかない → 一角を借りた店が続く; deletion test collapses it, as planned. Subject: 家賃補助で呼び込んだ新しい店は三年後に閉まり、古い店の一角を借りて始めた店が続いた（商店街の一角を貸す） |
| 問題11(3) | 旅行・観光 | 随筆 | — (must NOT share 問題10(3)'s skeleton) | 一人称の前後比較 | 「今の旅では、足りない物が一つあるたびに、町の人に声をかける用事が一つ増えます。」 — skeleton 〈場面〉では、X が一つ〜たびに、Y が一つ増える（比例の一般化）; main subject is 用事 (not an artifact), no を-object, not 〜ている, so not 先回り. **Differs from 問題10(3)** (〈主体〉は〈人〉のもとへ〈物〉を運んでいく). Before = PRACTICE (荷物を詰められるだけ詰める). Subject: 大きなかばんをやめて小さなかばん一つで旅をすると、足りない物を町の人に尋ねるたびに話が生まれた（小さなかばんの旅） |
| 問題11(4) | 防災 | 反論応答 | `A わけではない` (foil = A) | 反論への応答 | 「電話口で重ねる質問は、消防車の出発を遅らせているわけではない。」 — skeleton A わけではない (foil A = 消防車の出発を遅らせる). **Re-authored (stage-3 F3)**: was 消防団の昼の団員 (re-skin of 20260928_1 11(1)). Complaint (質問ばかりでじれったい、その間に火が広がる) granted as 当然 and answered on its own terms (二つ分かった時点で出動、残りは走行中に聞いて隊に無線で伝える); no 「もっとも」, no explicit ではない-denial before the final, so the deletion test leaves it off 〈想定→実は〉. Subject: 消防署の通信指令室で119番を受ける係が、質問が多くて出動が遅れるという苦情に、火事か救急かと場所が分かった時点で消防車は出ていると応じる（119番の質問） |
| 問題12(A) | デジタル化 | 説明 | — | 機構の説明 (A+B = one surface) | 「端末の中のメモは、書いた人がその存在を覚えているあいだだけ、画面に呼び出される。」 — skeleton 〈物〉は、〈条件〉あいだだけ、V-られる（仕組みの限定を述べて止まる）; no advice. Subject: スマートフォンのメモは探す言葉を入れて初めて出てくるので、書いたことを覚えていないと見返されない（端末のメモが見返されない仕組み） |
| 問題12(B) | デジタル化 | 条件提示 | — (**NOT** 相関 — vary the 条件提示 skeleton; after QA F2, 問題10(2) is 主張 and the paper holds no 相関) | ″ | 「書いた次の朝に一度開き直すと決めておけば、端末のメモも、手帳のメモと同じように読み返される。」 — skeleton 〜と決めておけば、X も Y と同じように V-られる（点検できる条件を一つ示す、相関ではない）. **Read against 12(A) first:** A = limitation statement (あいだだけ), B = ば-condition; different skeletons. Subject: 書いた翌朝七時に一度知らせを鳴らして開き直せば、端末のメモも読み返される（翌朝に開き直す決まり） |
| 問題13 | 行政・手続き | 反論応答 | — | 反論への応答 | 「易しく書くことと、正確に伝えることは、一つのお知らせの中で、互いのじゃまをせずに並び立ちます。」 — skeleton AとBは、〈場所〉で、互いに V-ずに並び立つ（両立の断言）; unnamed. **Scaffold varied (stage-3 F3b)**: the objection is now a senior colleague's reported words, conceded as 「先輩の言うとおり」 (no 「反対の声…というのです。この心配は、もっとも」), the 疑問提示文 is a how-question (どう書けばよいのでしょうか), and the denial 「減らす必要はありません」 became 「そのまま残せます」 — off 〈想定→実は〉. Subject: 市役所のやさしい日本語の書き直しへの、正確さが削られるという先輩の指摘に、一文に条件を一つずつ置けば条件は減らないと応じる（やさしい日本語のお知らせ） |
| 問題14 | 子育て・家族 | (outside axis 2 — flyer, no closing) | — | （実用文） | — |

## Who owns which rows

- **The 問題9 cloze row belongs to the 文法 (問7–9) author.**
  `scaffold_sections.py` emits the cloze inside `問7-9_文法.md`. Both authors get
  this whole table, because the caps are counted across all thirteen closings.
- **問題10–14 belong to the 読解 author.**

## 問題9's theme is AUTHOR-COMPOSED, and three values were legal; 住まい was drawn by RNG

`test_spec.json` has no cloze topic, because the cloze is the 13th, unpooled
theme row. Here is how `exam-blueprint` §"The four theme rules" narrows it:

- **Rule 3.** The 12 drawn themes are taken: 文化・伝統, スポーツ・余暇, 人間関係,
  働き方, 教育, 消費・経済, 地域活性化, 旅行・観光, 防災, デジタル化, 行政・手続き,
  子育て・家族. That leaves 睡眠・健康, 医療・福祉, 食, 環境, 交通, 住まい,
  メディア・情報 and 科学・技術.
- **Rule 4, consecutive papers.** 20260928_1 headlined 交通, 人間関係, 文化・伝統
  and 食, with 聴解問題5 on スポーツ・余暇 and 消費・経済. That bars 食 and 交通.
- **Rule 4, two papers back (at most ONE repeat).** 20260917_1 headlined 環境,
  メディア・情報, 働き方 and 行政・手続き, with 聴解問題5 on 消費・経済 and
  科学・技術. 問題13 行政・手続き already spends the budget of one, which bars
  環境, メディア・情報 and 科学・技術.
- **Legal: 睡眠・健康, 医療・福祉, 住まい.** One was picked with
  `secrets.randbelow(3)` rather than by preference, and the pick was **住まい**.

**Rule 4b: the cloze SUBJECT (5–15 JP chars) must not match any of 20260928_1's
13 読解 subjects or its 21 聴解 subjects** (`logs/topics.json`, last row).

- Two earlier papers ran 住まい surfaces:
  - 20260928_1 問題11(2), `窓を開ける5分` (a north-facing flat, condensation);
  - 20260917_1 問題11(3), `集合住宅の通路の私物`.
- Stay off both, and off every string in `logs/topics.json` tagged 住まい. The
  sampler's 住まい `avoid` list is at `items.listening_scenarios[0].avoid` in the
  spec, which holds every shipped 住まい subject.

## Headline subjects — what the rule-4b diff must stay clear of

The authors write a 5–15-char SUBJECT for each headline surface. Diff it
against the previous paper's 13 読解 and 21 聴解 subjects:

- **問題12 デジタル化.** No 読解 デジタル化 surface in either of the last two papers.
- **問題13 行政・手続き.** This is the paper's one two-back repeat: 20260917_1
  問題14 was `犬の登録と予防注射の案内`. Keep the subject far from it (no pet
  registration, no vaccination day).
- **問題14 子育て・家族.** 20260928_1 問題10(2) was `みなみ保育園の門の暗証番号`, a
  保育園 notice, and 20260928_1 問題14 was a 親子見学会 flyer (給食センター).
  **Do not write another 保育園 notice or another 親子 event-programme flyer.** A
  different document type or errand is required, so the flyer does not read as a
  re-skin of last paper's 問題14.

## Why each shape sits where it does

**The previous two papers' closings, per slot** (`logs/topics.json`
`closing_moves`). No slot repeats a shape either paper used in that slot:

| slot | 20260917_1 | 20260928_1 | assigned here |
|---|---|---|---|
| 問題9 | 説明 | 随筆 | 意外な観察 |
| 10(1) | 条件提示 | 説明 | 実用文 |
| 10(2) | 随筆 | 実用文 | 主張 (条件提示 until QA F2 re-allocation) |
| 10(3) | 実用文 | 意外な観察 | 随筆 |
| 10(4) | 実用文 | 実用文 | 説明 |
| 10(5) | 意外な観察 | 条件提示 | 実用文 |
| 11(1) | 説明 | 反論応答 | 意外な観察 |
| 11(2) | 反論応答 | 随筆 | 主張 |
| 11(3) | 条件提示 | 条件提示 | 随筆 |
| 11(4) | 随筆 | 説明 | 反論応答 |
| 12(A) | 主張 | 主張 | 説明 |
| 12(B) | 反論応答 | 反論応答 | 条件提示 |
| 13 | 主張 | 主張 | 反論応答 |

**Why the 実用文 members moved to 10(1) and 10(5).** Both previous papers put
実用文 at 10(4), and 20260928_1 also put it at 10(2). 10(1) and 10(5) are the
only two 問題10 slots neither paper used for it. 12(A) and 13 leave 主張 after
two papers of 主張 there, and 12(B) leaves 反論応答.

## Tallies the authors must NOT break

- **Closing shape (13 total), as re-derived after the QA F2 re-allocation of 10(2):**
  意外な観察 2, 条件提示 1 (12(B)), 随筆 2, 説明 2, 反論応答 2, 主張 2 (10(2),
  11(2)), 実用文・分類外 2. Values come from the CLOSED vocabulary `CLOSING_MOVES`
  and nothing else. Neither 主張 uses the canonical 「AだけではB、Cこそが」, which is
  barred on this paper (next section).
- **Template:** 相関 0 (was 1 at 10(2) until QA F2), 分裂文 1 (問題10(4)),
  `A より B のほうが` 1 (問題11(2)), `わけではない` 1 (問題11(4)), unnamed 10. The three **cap 1**
  templates (後知れ `〜ていた のだ`, 不在の残り `〜ていない`, 先回り) are assigned
  to no row. An unnamed final that lands on one of them spends its only slot.
  Don't.
- **not-A-but-B reframe family** (`AではなくB`/`というより`/`よりも`/`だけではなく`/
  `わけではない`, and ANY final that names a foil and prefers the alternative,
  including `AにないBがある`): exactly **2** surfaces, 問題11(2) and 問題11(4). Do
  not add a third anywhere, including a non-final sentence that ends up carrying
  the close.
- **MOVE (10 essay surfaces):** 〈想定→実は〉 **1** (問題11(2)), 機構の説明 3
  (問題9, 10(4), 12), 数えたことの報告 1 (11(1)), 一人称の前後比較 **3, at cap**
  (10(2), 10(3), 11(3)), 反論への応答 2 (11(4), 13). No row is over its cap.
  After the QA F2 re-allocation, 一人称の前後比較 has no headroom: any further
  re-angle goes to 数えたことの報告 or 反論への応答, never here.
  - **〈想定→実は〉 is planned at 1, not 2, on purpose.** The cross-half cap is 2,
    and it counts the 聴解 talks (`jlpt-test-generation` §"One topic, one
    surface", RC-7).
  - The 聴解 half is composed at stage 3 and nobody chooses its moves.
    20260928_1 planned 2 in 読解 and had to re-angle 問題10(3) when its
    聴解問題2-5番 carried a third.
  - One slot of headroom means stage 3 re-angles nothing unless the composed
    half carries **two**.
  - 機構の説明 is at its ceiling of 3. If stage 3 must still move 問題11(2) off
    the skeleton, the move goes to 数えたことの報告 or
    反論への応答 (一人称の前後比較 is now at its cap), never to 機構の説明.
- **Voice quota** (`exam-blueprint` rule 5, 12 essay-type passages, 問題14
  excluded): at least 4 in the first person and at least 3 in です・ます
  throughout. The first-person candidates are the three 一人称の前後比較 rows
  (10(2), 10(3), 11(3)) and the 数えたことの報告 row (11(1)). Plan the です・ます
  passages alongside the length bands (dokkai.md §"Length bands").

## Tested forms that must stay out of the 読解 prose (Item integrity #15)

This paper keys the following:
- **問題7:** 〜ずに済む, **〜というより**, 〜あまり, 〜に応えて, 〜最中だ,
  〜させられる, 〜に限り, 拝見する, 〜とのことだ, 〜だの〜だの, **〜こそ**,
  〜ついでに.
- **問題8:** 〜からすると, 〜に限る, 〜はもとより, 〜をめぐって,
  **補足追加(〜なお…)**.

Consequences for the allocation:

- **No `A というより B` template anywhere**, because 〜というより is a 問題7 key.
  No row is assigned it.
- **No 「こそ」 anywhere in the 読解 half**, because 〜こそ is a 問題7 key. The
  主張 closing on 11(2) is built on `より…ほうが`, not on 「Cこそが」.
- **補足追加(〜なお…) is a general-purpose frame**, so a prose grep is owed
  (`exam-blueprint` §"A `grammar_p8` draw whose form is a general-purpose
  sentence pattern").
  - 「なお、」 is the stock connective of exactly the surfaces this paper has:
    the 10(1) email, the 10(5) notice and the 問題14 flyer.
  - Grep all three and every essay for 「なお」. Re-word every hit but at most
    one, and that one must not sit in the tested sentence-initial 補足 frame.
- **Stage 3 re-grep.** Every other form above goes into the Stage-3 keyed-form
  re-grep with its counts and frames (文末／連用／連体).
  - The ones most likely to leak into this paper's subjects are 〜とのことだ (the
    notice and the email), 〜に限り (the flyer's 「先着…名に限り」) and
    〜からすると (essays).
  - A flyer condition 「〜に限り」 is the 問題7 key in its own frame. Write the
    condition another way (「…の方のみ」「…までの方」).

## The two things that get checked by hand

1. **The ten "unnamed template" finals must not share a skeleton with each
   other.** The pairs at risk are 問題9 vs 問題11(1) (both 意外な観察),
   問題10(3) vs 問題11(3) (both 随筆), 問題10(2) vs 問題11(2) (both 主張) and
   10(2) vs 10(3)/11(3) (all 一人称の前後比較), and 問題12(A) vs 問題12(B) (read A against
   B FIRST, because that is where the rhyme lands). Write the sentences into the
   last column and read them down as a column before finalising: once down the
   shapes, and once down the skeletons.
2. **Apply the deletion test to 問題11(2), and to nothing else.** Delete the
   denial sentence. If the passage still says what it came to say, it was never
   on the skeleton. Every OTHER row must carry no attributed assumption and no
   denial at all.
   - **問題9 and 問題11(1) (意外な観察):** the mismatch must be a FACT the reader
     finds unexpected, never a belief someone held and is then told is wrong.
   - **問題10(2), 問題10(3) and 問題11(3) (一人称の前後比較):** the "before" must be a
     PRACTICE the narrator actually did, never a belief they held.
   - **問題11(1) (数えたことの報告):** the count must not be
     introduced as contradicting an expectation.
   - **問題11(4) and 問題13 (反論への応答):** the objection is taken seriously and
     answered on its own terms. It is not a strawman.
