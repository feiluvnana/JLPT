# 読解 allocation table — 20261102_1 (BLUEPRINT-ASSIGNED, binding)

Stage 1 filled this table in **before any prose exists**, as
`question-authoring/references/dokkai.md` requires in §"Thirteen surfaces",
§"The named templates" and §"The rhetorical-MOVE allocation table".

- Authors do NOT re-choose the shape, template, MOVE or resolution columns.
- Each author fills the two **AUTHOR FILLS** columns from the prose they write
  and hands the table back.
- Edit this file, and your own rows only.

**Denominators** (dokkai.md §"The denominator"):

- **Axis 1, theme.** 13 rows. 問題12 A+B is ONE row.
- **Axis 2, closing shape and final-sentence template.** 13 closings. 問題12 A
  and B are SEPARATE rows. 問題14 is outside this axis.
- **MOVE cap.** Essay surfaces only, with 問題12 A+B as ONE: 10 here, because
  問題10(3) and 問題10(4) are 実用文.

**Themes** come from `tests/20261102_1/test_spec.json` `items.reading_topics[i]`.

- **Index → surface.** 0→問題10(1) … 4→問題10(5), 5→問題11(1) … 8→問題11(4),
  9→問題12, 10→問題13, 11→問題14.
- **Draw.** `make sample 20261102_1 SEED=72353322`, plus one
  `reading_topics:11` reroll (rule 4, 消費・経済 → 子育て・家族) and one
  `grammar_p7:9` reroll. Both are recorded in
  `qa/blueprint-rerolls-20261102_1.md`.
- **What to avoid.** Author each surface's SUBJECT from its entry's `theme`.
  Keep it off:
  - that entry's full `avoid` list in the spec;
  - any re-wording of an avoid string;
  - every previous-paper CLAIM below (exam-blueprint Part II, "claims, not
    only subjects").

## Who owns which rows

- **問題9, the cloze, belongs to the 文法 (問7–9) author.**
  `scaffold_sections.py` emits the cloze inside `問7-9_文法.md`.
- **問題10–14 belong to the 読解 author.**
- Both authors get this whole table, because the caps are counted across all
  thirteen closings.

## The allocation

| surface | owner | theme | closing shape (≤2 each) | final-sentence template | MOVE (resolution) | voice / persona (plan) | AUTHOR FILLS: final sentence | AUTHOR FILLS: which previous claim (20261008_1's) this is NOT, and why |
|---|---|---|---|---|---|---|---|---|
| 問題9 cloze | **文法** | **スポーツ・余暇** (author-composed; RNG, below) | 条件提示 | **`A では/ほど B が多い（相関）`**, the paper's only 相関. Write it with **「〜では」, never 「ほど」**, because 〜ほど〜はない is this paper's 問題8 form. Not 〈決まりは続けていく。ただ…入り口を一つ開けておきたい〉 (20261008_1 問題9) | **数えたことの報告**. Resolution: the narrator counts ONE bounded span (one season or one month) of their OWN practice records and reports which condition went with more of an outcome. The count is not introduced as contradicting an expectation | 一人称随筆; **趣味の実践者**, e.g. an amateur club member. Not a role-holder reading back N years of records | 「記録を並べてみると、一番難しいコースから始めた日では、一度目で上まで登り切れたコースが、目に見えて多かった。」 (subject: 室内クライミング — 一番難しいコースから始めた日のほうが一度目で登り切れたコースが多かった; 趣味の実践者, 一人称; 条件提示 / 相関 with 「では」 / 数えたことの報告, one month of own records, 9 visits) | Not 問題9 counter lunch closure + phone-reservation exception: no rule kept, no exception channel opened — the narrator counts one month of their own climbing log and reports which starting order went with more first-try completions. Not 11(2) 'contacting neighbours first is slower but leaves fewer missing': no speed-vs-completeness trade. Not 10(3) 'writing it down once stops a redo': the log only counted. (Filled by stage 3 from `_sections/問7-9_文法.md`; the 文法 author left the cells empty.) |
| 問題10(1) | 読解 | 科学・技術 | 意外な観察 | Unnamed. **NOT 分裂文 — gated bar** (20261008_1 10(1) closed on it). This shape's natural final 「〜のは、…からだ」 IS the cleft, so do not use it. Not 〈V-た字は、その週のうちに二度〜ことはなかった〉 (20261008_1 10(3)) | **〈想定→実は〉**, the paper's ONLY one on the 読解 side (see below) | 一人称随筆 or 解説; **研究者** | 「雪国では、気温が零度近くまで上がった朝の道を、いちばん用心するそうだ。」 (subject: 氷がすべる理由 — 表面の固まりきらない薄い層; 研究者, 一人称) | Not 10(1) 夕焼け (light lost along a long path): no optics, no path a light/water/nutrient takes; the cause is a standing property of the ice surface (a layer that thins with cold). Not 11(2)/12(A)'s count or remedy→result. Not a cleft, no skating (スポーツ・余暇 is 問題9's). |
| 問題10(2) | 読解 | 医療・福祉 | 説明 | Unnamed. **NOT 分裂文 — gated bar**. Not 〈今の私のNには、どれも、〜が一つずつついてくる〉 (20261008_1 10(4)) | **機構の説明**. Resolution: how one thing in a care or clinic setting works, or how two such things differ. Nothing is denied anywhere | 解説, **です・ます**; **職業人**, e.g. a nurse, physiotherapist or care worker. NOT a hospital wayfinding volunteer counting questions (20261002_1 10(2): same seat, same theme) | 「ただ、濃すぎるとのどに残るため、濃さは一人一人に合わせて調整しています。」 (subject: 飲み物のとろみと飲み込み; 介護施設の職員) | Not 10(2) group-rail email nor 20261002_1 10(2) wayfinding count: a swallowing mechanism (気管のふた vs 流れの速さ), nothing counted, nothing denied. Not 12(A)'s nutrient path. |
| 問題10(3) | 読解 | 行政・手続き | **実用文・分類外** (notice / お知らせ; RNG, below) | — | （実用文） | 通知, です・ます; 市・区・町（通知） | 「お知らせだけの書類は、これまでどおり白封筒でお届けします。」 (subject: 期限のある書類をだいだい色の封筒で送る) | Not 問題9 (counter lunch closure + phone reservation) nor 10(5) newspaper shelf: no hours, no reservation, no exception channel — an envelope-colour change for deadline mail. |
| 問題10(4) | 読解 | デジタル化 | **実用文・分類外** (business email; RNG, below) | — | （実用文） | メール, です・ます; 実務者 | 「写真が届きましたら、三日ほどで見本をお送りします。」 (subject: 文書に貼った写真が縮むので元ファイルで別送を依頼) | Not 10(2) group-travel notification nor 10(3) phone kanji / 20261002_1 photo backup: a print shop asks for original photo files instead of pasted ones. |
| 問題10(5) | 読解 | 働き方 | 随筆 | Unnamed. **NOT 分裂文 — gated bar**. Must differ in skeleton from 11(4), the other 随筆. Not 〈今の私のNには、どれも…ついてくる〉 (20261008_1 10(4)) | **一人称の前後比較**. Resolution: ONE concrete work PRACTICE changed, and what it changed in the work itself. The "before" is a practice, never a belief | 一人称随筆; **職業人** | 「声に出すようになってから、私が原稿に引く赤線の多くは、一息で読みきれない文を区切る線になった。」 (subject: 原稿を声に出して読んで直す; 編集者) | Not 10(4) haiku-on-walks: the practice stays at the desk (screen→printed and read aloud); what changed is the kind of correction, not a place stamp. Not 10(3)'s 'write it once, stop redoing'. |
| 問題11(1) | 読解 | 文化・伝統 | 反論応答 | Unnamed; not-A-but-B family member (foil: 明かりとして比べる物差し), QA round 2. **NOT 相関 — gated bar** (20261008_1 11(2)). Not 〈Nには、〜てから一時間の休みを取らせ、それから〜ています〉 (20261008_1 11(4)). Not 〈この島では、AもBも…に合わせて決まっていく〉 (11(1)). Not a cleft | **反論への応答**. Resolution: **「反論の前提を問い直す」** (Stage-3 T2 re-angle, 2026-11-02; was 「理由を示して変えない」, which ran 20261008_1 11(4)'s claim one paper apart). The objection is conceded as true on its own measure, and the passage asks what that measure presupposes. No exception is opened, no practice is defended against a loss, no 実は, no strawman, no 「もっとも」 knock-down | 一人称随筆, **です・ます**; **職人**, a bearer of a craft or performing tradition | 「けれども、それは、和ろうそくが長く求められてきた役目とは別の物差し（注5）です。」 (QA F4, 2026-11-02: the former last paragraph 「暗いとおっしゃるお客様には、まず…お聞きしています。」 was deleted because it kept 20261008_1 11(4)'s 「Nには＋sequence＋〜ています」 closing beat; subject: 和ろうそくは暗いという声と、その前提; 和ろうそく職人, です・ます. Claim: 和ろうそくが部屋の明かりとして暗いのは確かだが、「暗い」は部屋を照らす道具として比べたときの物差しで、仏壇や寺で使う人には炎の静かさや汚さないことが問われる) | Not 11(4) bread-rest 'keep a waiting period for the customer despite a loss' and not 問題9 'keep the rule + one exception': nothing is kept against a cost and no channel is opened — the objection's measure (room lighting) is named as a premise and set beside the use the buyers report. Not 11(1) tide schedule. Not 〈想定→実は〉: the complaint is conceded, never denied. |
| 問題11(2) | 読解 | 防災 | 説明 | Unnamed. **NOT 相関 — gated bar**. Not a cleft. Not 〈Xをし、Yすれば、Zは…保たれる〉 (20261008_1 12(A)'s remedy→result skeleton) | **機構の説明**. Resolution: how a hazard or a piece of safety equipment WORKS. No evacuation drill, no head-count | 解説; **解説者** | 「外見に傷がなくても、大きな物を一度受け止めたヘルメットは、次に同じ力を受けたとき、同じようには頭を守れない。」 (subject: 防災用ヘルメットが頭を守る仕組み; 解説) | Not 11(2) neighbour-knock drill count (no drill, no head-count, no speed-vs-completeness trade) and not a light/water/nutrient path: shell spreads, strap gap delays, liner crushes once. |
| 問題11(3) | 読解 | 人間関係 | 条件提示 | Unnamed. **NOT 相関 — gated bar**, so use a DIFFERENT condition skeleton from 問題9. Not 〈今は、〜たら、…のを待つことにしている〉 (20261008_1 11(3)). Not 〈〜方は、〜と聞いた晩には…てください〉 (20261008_1 問題13) | **数えたことの報告**. Resolution: a short count (days or weeks) of something in the narrator's own exchanges with others, and the condition it showed. It must differ from 問題9 in what was counted AND in what the count showed | 一人称随筆; **観察者**. NOT 友人-listening (20261008_1 11(3)) | 「返す日を、借りる人が自分の口で言ってくれれば、こちらから催促することは、まず要らなくなる。」 (subject: 貸した物が催促なしで返ってくる条件; 観察者, 六週間12件) | Not 11(3) 'stop advising and wait': no listening/advice; not 10(3) 'a note stops a repeat' (the notebook only counted); not 11(2) speed vs completeness. Differs from 問題9 (own climbing month, 相関 with では) in what was counted (lendings) and in what it showed (who names the return day), with a 〜れば condition, no 相関. |
| 問題11(4) | 読解 | 睡眠・健康 | 随筆 | Unnamed. **NOT 相関 — gated bar**. Must differ in skeleton from 10(5) | **一人称の前後比較**. Resolution: ONE sleep or rest PRACTICE the narrator changed, and what it changed. It must differ from 10(5) and 13 in kind | 一人称随筆; **学生** | 「目覚ましを止めに部屋を横切って歩く間に、私の頭は、たいていもう半分は起きている。」 (subject: 目覚ましを一つにして部屋の反対側に置く; 寮生活の大学生) | Not 10(4) desk→walk place-stamp (the alarm moves across the room, the practice is waking), not 13's threshold/night-before precaution, not 11(3) waiting-for-the-other. Before = a practice (3 alarms within reach), not a belief. |
| 問題12(A) | 読解 | **交通** | 主張 | **`A わけではない`** (RNG, below), the paper's ONLY not-A-but-B family member. Name the foil A in the final. Not 「〜のが、…賢いやり方である」 (20261002_1 12(A), two back). Read against 12(B) FIRST | **反論への応答** (A+B = one surface). 12(A) states the position | 評論; **論者** | 「車内のけがは、運転の荒さだけで起きるわけではない。」 (subject: 路線バスの車内事故と、止まる前に立つ客; 論者) — foil A named: 運転の荒さ | Not 12(A) pond remedy→result nor 11(1) natural-cycle schedule: a fall mechanism (the stop-instant jolt) rejected as single-factor 'rough driving'; no price/purchase, no bicycle, no group travel. |
| 問題12(B) | 読解 | ″ | 反論応答 | Unnamed. **NOT `A だけでは〜、B こそが` — gated bar** (20261008_1 12(B)). It is no family member: no ではなく, というより, よりも, だけでは or わけではない in the final two sentences | ″ Resolution: **「譲歩して一部を変える」**. B takes A's point seriously and changes ONE part of its own advice. That change must NOT be "keep the rule and open one exception channel by reservation" (20261008_1 問題9) | 評論 or 一人称, **です・ます**; **利用者** | 「バスが止まったら、すぐに立って降車口へ向かいます。」 (subject: 降り方を一部だけ変えた利用者; です・ます) | Not 12(B) 'the public's small act is the hidden cause, please stop' (no appeal to others) and not 問題9's booking exception: B concedes the stop-instant risk and changes ONE part (when to stand) while keeping the other (not making others wait: card in hand, button early). |
| 問題13 | 読解 | **食** | 意外な観察 | Unnamed. Not a cleft (plan 0 paper-wide). Not 〈〜方は、〜と聞いた晩には…てから休んでください〉 (20261008_1 問題13) | **一人称の前後比較**. Resolution: after ONE cooking or eating PRACTICE changed, an unexpected FACT followed, and the passage gives its cause. The unexpected thing is an outcome. It is not a belief anyone held, so there is no 「思っていた。ところが」 | 一人称随筆; **趣味の実践者** | 「今は、刻み終えたまな板の上に、玉ねぎの汁がほとんど残らなくなっている。」 (subject: 包丁を研ぐようになって玉ねぎで涙が出なくなった; 料理が趣味の一人称) | Not 13 frozen-pipe threshold / night-before precaution and not 11(4) bread resting: the outcome surprise (no tears after weekly sharpening) gets its cause (a sharp edge does not crush the onion's cells). No belief stated or denied; no price, purchase unit or budget. |
| 問題14 | 読解 | **子育て・家族** | (outside axis 2: flyer, no closing) | — | （実用文） | 案内; 施設・団体（案内） | (flyer, no closing) last line: 「最後に残った品物は、子育てひろばが近くの保育園などに届けます。」 (subject: 子ども用品おさがり交換会 — 引換券と持ち帰り料金) | Not 14 visiting barber (no eligibility/application-form/visit-day structure) nor 20260928_2 child-seat rental nor a 児童館 time slot: an exchange event — items in → tickets (1/1/3), over-ticket take-home 50円, big items by phone by 6/7 and delivered 9:30–10:00 to the back door. |

## The previous paper (20261008_1), per 大問 — what is barred here

The table below was read from the shipped `tests/20261008_1/言語知識・読解.md`
with the gate's own `dokkai_closing_scopes()`, `passage_final_sentence()` and
`FINAL_SENTENCE_TEMPLATES`. The script is
`/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/87a5eab4-5dc5-4727-bd01-de360ff16047/scratchpad/bp1102_prev.py`.
The MOVE column is the post-round-2 column, from `logs/topics.json` notes and
`qa/qa-report-20261008_1-round2.md` §4. 11(4) was re-angled off 〈想定→実は〉
and stays 反論への応答.

| 大問 | 20261008_1 named templates | 20261008_1 unnamed final skeletons (QA read; do not reuse in the same 大問) | 20261008_1 MOVEs |
|---|---|---|---|
| 問題9 | none | 〈決まりは続けていく。ただ、Xにも、Yのための入り口を一つ開けておきたい〉 | 反論への応答 |
| 問題10 | **`〜のは B だ（分裂文）`** (10(1): 「夕方の空が赤く見えるのは、…からだ。」) | 10(3) 〈調べた…字は、その週のうちに二度調べることはなかった〉; 10(4) 〈今の私の句には、どれも、…が一つずつついてくる〉; 10(2) and 10(5) 実用文 | 機構の説明 (10(1)), 数えたことの報告 (10(3)), 一人称の前後比較 (10(4)) |
| 問題11 | **`A では/ほど B が多い（相関）`** (11(2): 「…班ほど、…来ない家は少なかった。」) | 11(1) 〈この島では、AもBも、毎日…に合わせて決まっていく〉; 11(3) 〈今は、〜たら、…て、…のを待つことにしている〉; 11(4) 〈棚のパンには、…てから一時間の休みを取らせ、それから袋に入れています〉 | 〈想定→実は〉 (11(1)), 数えたことの報告 (11(2)), 一人称の前後比較 (11(3)), 反論への応答 (11(4)) |
| 問題12 | **`A だけでは〜、B こそが`** (12(B): 「…パンこそが、池の水の色を変えているのです。」) | 12(A) 〈Xをし、Yすれば、Zは…ず、…保たれる〉 | 機構の説明 |
| 問題13 | none | 〈〜方は、…と聞いた晩には、…てから休んでください〉 | 数えたことの報告 |

**Template bar.** This bar is gated by
`check_dokkai_template_repeat_prev_paper`.

- **問題10:** no 分裂文. This includes 「大切なのは」「注目すべき点は」
  「確かめるべきは」 and the 「〜こと／点は、…だ」 variants.
- **問題11:** no 相関.
- **問題12:** no `A だけでは〜、B こそが`.
- **問題9 and 問題13:** not barred, since 20261008_1 closed them on no named
  template.

The unnamed skeletons above are a QA read, not a gate.

**MOVE bar** (dokkai.md, per 大問). 20261008_1 used no MOVE twice in any one
大問. 問題10 and 問題11 each had distinct MOVEs. So the gated-by-hand bar is
vacuous this paper. Stage 1 also set two seat rules on top of it:

- **No seat carries the MOVE 20261008_1 put in that seat.** All 10 were checked.
- **No seat repeats 20261002_1's (seat, theme, MOVE) triple.** The two near
  cases:
  - 10(2) 医療・福祉 is 機構, not 数えた. 20261002_1 10(2) was hospital
    question-counting.
  - 11(2) 防災 is 機構, not 数えた. 20261008_1 11(2) was a drill head-count.

Within this paper, 問題10 holds 想定 / 機構 / 一人称 and 問題11 holds
反論 / 機構 / 数えた / 一人称. No MOVE is used twice in one 大問, so the next
paper inherits no per-大問 MOVE bar.

**Persona bar.** 「〈役〉が〈N年分〉を数える」 last ran in 20260929_1, which is
three papers back, so it is technically free again. 20261008_1 still ran two
near cases: 11(2), where a 係 reports from a 名簿 of one drill, and 13, where a
住人 counts one winter's 90 days. **This paper keeps the persona OFF.** The two
数えた rows (問題9, 11(3)) each count one bounded span of the narrator's OWN
activity. Neither is a role-holder reading back years of records.

## The previous paper's 13 claims — what each surface must NOT restate

These come from `logs/topics.json`, row 20261008_1, `claim`. 問題12 A and B
are listed separately, so there are 14 lines. In the last column of your row,
write which of these your surface is NOT, and why. "Not" means a different
assertion, not only a different subject.

| key | 20261008_1 claim | theme there | nearest rows here (read these two together) |
|---|---|---|---|
| 問題9 | 昼に窓口を閉める決まりは職員が手薄で待ち時間と間違いが多い一時間を避けるために続けるが、昼にしか来られない人のために前日までの電話予約で一人残る入り口を開けておく。 | 行政・手続き | 10(3) notice, 11(1), 12(B) |
| 問題10(1) | 夕方の空が赤いのは、光が空気の中を長く進むうちに散らされやすい青い光が先に失われ、散らされにくい赤い光が残って目に届くからである。 | 科学・技術 | 10(1), 11(2), 10(2) |
| 問題10(2) | 校外学習で児童と教員42人が電車に乗るとき、前もって駅に知らせる必要があるか、あればいつまでにどう知らせるかを知りたい。 | 交通 | 10(4) email, 12, 14 |
| 問題10(3) | 調べた字をその場で一度手で書き写しておけば、同じ週のうちにその字をもう一度調べることはなくなる。 | デジタル化 | 10(4), 問題9, 11(3) |
| 問題10(4) | 俳句を机ではなく散歩の途中の足を止めた場所で作るようになって、どの句にも作った場所がついてくるようになった。 | 文化・伝統 | 11(1), 10(5), 11(4), 13 |
| 問題10(5) | 4月から全国紙は3か月分だけを新聞コーナーに置き、それより前の記事は記事検索のパソコンで読んでもらい、地元の新聞は1年分のまま置く。 | メディア・情報 | 10(3) notice |
| 問題11(1) | この島の船の時刻は船を動かす人の都合ではなく毎日約50分ずつ遅れる潮の満ちる時刻で決まり、島の人の予定もその潮に合わせて決まっていく。 | 「けれども、それは、和ろうそくが長く求められてきた役目とは別の物差し（注5）です。」 (QA F4, 2026-11-02: the former last paragraph 「暗いとおっしゃるお客様には、まず…お聞きしています。」 was deleted because it kept 20261008_1 11(4)'s 「Nには＋sequence＋〜ています」 closing beat; subject: 和ろうそくは暗いという声と、その前提; 和ろうそく職人, です・ます. Claim: 和ろうそくが部屋の明かりとして暗いのは確かだが、「暗い」は部屋を照らす道具として比べたときの物差しで、仏壇や寺で使う人には炎の静かさや汚さないことが問われる) | Not 11(4) bread-rest 'keep a waiting period for the customer despite a loss' and not 問題9 'keep the rule + one exception': nothing is kept against a cost and no channel is opened — the objection's measure (room lighting) is named as a premise and set beside the use the buyers report. Not 11(1) tide schedule. Not 〈想定→実は〉: the complaint is conceded, never denied. |
| 問題11(2) | 出る前に両どなりに声をかけた班は、そろうまでの時間は長くなったが、最後まで来ない家は少なかった。 | 防災 | 11(2), 問題9, 11(3) |
| 問題11(3) | 友人の相談を途中でさえぎって助言するのをやめ最後まで待って聞くようにしたら、友人は初めの話の奥にある本当の迷いまで話すようになった。 | 人間関係 | 11(3), 10(5), 11(4) |
| 問題11(4) | 焼いたパンの香りが時間とともに弱まるのは惜しいが、客は帰宅して切ってから食べるので、湯気を抜いて形を保つための一時間は続ける。 | 食 | 13, 11(1) |
| 問題12(A) | 夏の池が緑になるのは日光・温かい水・栄養がそろって小さな植物が増えるためで、水を動かし底の泥を取れば栄養が水面にとどまらず水は澄んだままになる。 | 環境 | 11(2), 10(2), 12(A) |
| 問題12(B) | 池の水を緑にしているのは日ざしだけでなく、人が投げ入れるパンが底で腐って小さな植物の栄養になるからなので、パンを投げ入れないでほしい。 | 環境 | 12(B), 10(1) |
| 問題13 | 古い家の水道が凍るのは予報が氷点下4度以下の晩の日の当たらない側の管なので、その晩は蛇口を細く開けておけば凍らない。 | 住まい | 11(3), 13, 11(4) |
| 問題14 | 訪問理容・美容を使える人の条件・料金と出張料・利用券の枚数と使えない範囲・申請の方法・電話での申し込みの期限・訪問の曜日と変更の期限を知らせる。 | 医療・福祉 | 14, 10(2) |

These claim families are off-limits. Read them across the column:

- **"keep the rule, open one exception channel"** (問題9). 11(1) gives no
  exception at all. 12(B) changes a part of its advice, but the change is not
  an exception reached by booking or by phone.
- **"X looks or happens this way because of a physical path the light, water or
  nutrient takes"** (10(1), 12(A)). 10(1), 10(2) and 11(2) explain no colour
  change, no optics and no algae or nutrient path.
- **"writing it down once on the spot stops you redoing it"** (10(3)). 問題9
  and 11(3) must not report that a note or record prevented a repeat.
- **"doing the practice out in the world instead of at the desk marks each
  output with its place"** (10(4)). 10(5), 11(4) and 13 must not move a
  practice from the desk to a walk, a commute or outdoors.
- **"the timetable is set by a natural cycle, not by the people running it"**
  (11(1)). 12 must not argue that a schedule follows tide, weather or season.
- **"contacting the neighbours first is slower but leaves fewer missing"**
  (11(2)). 問題9 and 11(3) must not trade speed against completeness.
- **"stop advising and wait, and the other person says more"** (11(3)). 11(3)
  must not be about listening, advice-giving or waiting for someone to finish.
- **"a waiting period is kept for the customer's later use, despite a loss"**
  (11(4)). 13 must not defend or explain resting, cooling or waiting before
  serving.
- **"the public's own small act is the hidden cause, so stop doing it"**
  (12(B)). 12(B) must not be a "please stop doing X" appeal.
- **"below a threshold, do X the night before"** (13). 11(4) and 13 must not
  close on a temperature or forecast threshold or on a night-before precaution.

### Domains of the previous papers' 科学・技術 / 消費・経済 surfaces

| paper | surface | theme | DOMAIN (stay out of it on 10(1), and on 12 and 13 for 消費・経済) |
|---|---|---|---|
| 20261008_1 | 問題10(1) | 科学・技術 | atmospheric optics: why the evening sky is red (light scattering over a path length) |
| 20261008_1 | 聴解問題5-2番 (composed) | 消費・経済 | choosing between bicycles at a shopping centre (commuting stability against folding for the car) |
| 20261008_1 | — | 消費・経済 (読解) | no 読解 surface |
| 20261002_1 (two back, minor) | 問題11(1) | 科学・技術 | domestic appliance physics: microwave heating of frozen food, and why the package instruction says what it says |
| 20261002_1 (two back, minor) | 問題12(A)/(B) | 消費・経済 | household purchasing: bulk buying, unit price against paying up front |

- **10(1).** This paper's only 科学・技術 surface. It may not be optics, sky
  colour or light; appliance or heating physics; a measuring or observation
  protocol; or "why the instruction says X".
- **No 消費・経済 surface.** 問題14 was rerolled off 消費・経済.
- **12 交通 and 13 食** must not make a purchase-unit, price or household-budget
  claim.
- **12 交通** must not be a bicycle-buying choice (the 20261008_1 聴解5-2番
  near-hit).

## Avoid lists, per row (the spec holds the full list; this is the near history)

The full `avoid` list for 10(1)–14 is in the spec, at
`items.reading_topics[i].avoid`. It runs 24–60 subjects per theme, and you must
read it in full. The rows below list the previous two papers' same-theme
subjects, from both 読解 and 聴解, because that is where a near-miss is
likeliest.

- **問題9 スポーツ・余暇** (no spec seat).
  - The used list is `used_subjects_by_theme()['スポーツ・余暇']`. All of it is
    off.
  - Near history:
    - 20261002_1 11(4): hill-walking descents and muscle pain.
    - 20261008_1 聴解2-5: 5000 m race tactics in wind.
    - 聴解1-4: a goldfish tank.
    - 20261002_1 聴解1-1: tennis-club camp logistics.
    - 聴解3-2: railway photography.
  - No hill-walking or descent, no race tactics, no tank or pet care, and no
    camp logistics.
- **10(1) 科学・技術.** See the domain table above. Also off are every
  spec-list subject, for example failed-experiment publishing, citizen
  river-creature counts, cloud formation and deep-sea collaboration.
- **10(2) 医療・福祉.**
  - Near history:
    - 20261008_1 14: visiting barber or beautician for the elderly.
    - 聴解2-3: shoulder rehabilitation.
    - 20261002_1 10(2): hospital map against ticket numbers.
    - 聴解3-4: care robots and assisted wheelchairs.
  - No home-visit service, no shoulder or rehab report, no wayfinding, and no
    care robotics.
- **10(3) 行政・手続き (notice).**
  - Near history: 20261008_1 問題9, a counter's lunch-hour closure with a phone
    reservation.
  - It may not be about counter hours or reservations.
  - Recent notices also off:
    - a library newspaper-shelf notice (20261008_1 10(5));
    - a 児童館 time-slot notice (20261002_1 10(1));
    - a 回覧板 or app notice (20260929_1 10(2)).
- **10(4) デジタル化 (email).**
  - Near history:
    - 20261008_1 10(3): looking up kanji on a phone.
    - 20261002_1 10(5): automatic photo backup.
  - Recent emails also off:
    - school-trip rail notification (20261008_1 10(2));
    - ink-container take-back (20261002_1 10(4));
    - handover between contacts (20260929_1 10(3)).
  - No phone dictionary, no photo or cloud backup, and no group-booking
    notification.
- **10(5) 働き方.**
  - Near history (聴解 only):
    - 20261008_1: poster comparison figure, job-change interview, farewell-party
      RSVP.
    - 20261002_1: cookie box design, recruitment-interview criteria, "why people
      work" talk.
  - No poster or packaging redesign, no interview or recruitment, and no
    "meaning of work" claim.
- **11(1) 文化・伝統.**
  - Near history:
    - 20261008_1 10(4): haiku on walks.
    - 聴解2-4: kimono coordination.
    - 20261002_1 11(2): かるた reader.
    - 聴解1-5: exhibition hanging.
    - 聴解2-6: mud festival.
  - No haiku, poetry, かるた, kimono, exhibition or festival.
- **11(2) 防災.**
  - Near history:
    - 20261008_1 11(2): evacuation drill, knocking on neighbours' doors.
    - 20261002_1 14: fire-extinguisher refill.
  - No drill, no head-count or roster, and no extinguisher.
- **11(3) 人間関係.**
  - Near history:
    - 20261008_1 11(3): a friend's phone consultation.
    - 20261002_1 13: the organiser role sticking to one person.
    - 聴解: teasing, worry about an absent colleague, accepting a gift, a
      forgotten umbrella, modesty.
  - No consultation, no organiser (幹事) role, and no lost-property errand.
- **11(4) 睡眠・健康.**
  - Near history: 20261002_1 聴解5-2, a health-event venue choice that included
    a "can't sleep" consultation.
  - No health-event or venue choice. A sleep subject is fine if it is the
    narrator's own practice.
- **12 交通.**
  - Near history:
    - 20261008_1 10(2): school-trip rail email.
    - 聴解3-1: on-board trolley sales noise.
    - 聴解5-2: bicycle purchase.
  - No group-travel notice, no on-board noise or sales, and no bicycle buying.
- **13 食.**
  - Near history:
    - 20261008_1 11(4): bread rested an hour.
    - 聴解3-2: honey history.
    - 聴解4-10: a cheap set-meal shop.
    - 20261002_1 11(3): home dashi against powder.
  - No bread, bakery, resting or cooling, no dashi, and no honey history.
- **14 子育て・家族.**
  - Near history: 20261002_1 10(1), a 児童館 parent-child hour notice.
  - Recent 問題14 document types are off:
    - visiting barber (20261008_1);
    - extinguisher refill (20261002_1);
    - scholarship call (20260929_1);
    - **child-seat rental (20260928_2)**.
  - Pick a different document type and errand. It must not be a 児童館
    time-slot either.

## Headline surfaces — rule 4 and the rule-4b subject diff

- **Rule 4 (themes).** This paper's 読解 headlines are 問題9 スポーツ・余暇,
  問題12 交通, 問題13 食 and 問題14 子育て・家族.
  - 20261008_1 headlined 行政・手続き, 環境, 住まい and 医療・福祉, plus
    聴解問題5 旅行・観光 and 消費・経済.
  - 20261002_1 headlined メディア・情報, 消費・経済, 人間関係 and 防災, plus
    聴解問題5 働き方 and 睡眠・健康.
  - **No overlap with either paper.** This holds after the 問題14 reroll; the
    draw was 消費・経済, which would have FAILed. The two-back budget of one is
    unspent. This paper's 聴解問題5 theme is unknown until `make mp3`, and is a
    WARN-only draw audit.
- **Rule 1.** The four 読解 headline themes are distinct.
- **Rule 2.** Each headline theme appears nowhere else in the 読解 half. 11(4)
  睡眠・健康 must therefore not drift into parenting (子育て・家族 is
  問題14's).
- **Rule 3.** All 13 読解 themes are distinct.
- **Rule 4b (subjects).** Each headline author writes a 5–15-char SUBJECT
  first and diffs it against all 13 読解 and 21 聴解 subjects of 20261008_1 in
  `logs/topics.json` `surfaces`. Known near-hits:
  - 問題9 vs 聴解2-5 (race tactics) and 聴解4-11 (team morale).
  - 12 vs 10(2) (rail notice) and 聴解3-1 / 5-2.
  - 13 vs 11(4) (bread), 聴解3-2 and 4-10.
  - 14 vs 14 (visiting barber).

  A same setting with a different issue is allowed, and goes into `notes`. A
  same setting with the same issue means re-subject.

## 問題9's theme is AUTHOR-COMPOSED; スポーツ・余暇 was drawn by RNG from three legal values

- **Rule 3.** The 12 drawn themes are taken: 科学・技術, 医療・福祉,
  行政・手続き, デジタル化, 働き方, 文化・伝統, 防災, 人間関係, 睡眠・健康,
  交通, 食 and 子育て・家族. That leaves 環境, 住まい, 教育, 地域活性化,
  消費・経済, スポーツ・余暇, メディア・情報 and 旅行・観光.
- **Rules 4 and 4c.** A cloze candidate is free only if it headlines NEITHER
  previous paper.
  - 20261008_1 bars 環境, 住まい, 旅行・観光 and 消費・経済.
  - 20261002_1 bars メディア・情報 and 消費・経済.
- **Legal values:** 教育, 地域活性化 and スポーツ・余暇.
  `secrets.randbelow(3)` returned 2, which is **スポーツ・余暇**.
- **Shape and MOVE.**
  - The cloze is 条件提示 / 数えたことの報告, with the paper's one 相関 final
    written with 「では」.
  - The 4 blanks follow `bunpou.md` §問題9.
  - The narrator's count is of their own leisure practice. It is not a coach or
    officer reading back years.

## Why 実用文 sits at 10(3) and 10(4) — RNG

- **Recent 実用文 slots:**
  - 20261008_1 used 10(2) and 10(5).
  - 20261002_1 used 10(1) and 10(4).
  - 20260929_1 used 10(2) and 10(3).
- **First slot.** 10(3) is the only slot neither previous paper used, so it
  takes one.
- **Second slot.** `secrets.randbelow(2)` over {10(1), 10(4)}, the slots used
  only two papers back, returned 1, which is **10(4)**.
- **Document types.** A second `secrets.randbelow(2)` returned 1, which puts
  the **notice at 10(3)** (行政・手続き) and the **business email at 10(4)**
  (デジタル化).
- **The 実用文 rows carry the paper's 敬語 keys.** 敬語:存じる and
  敬語:ご覧いただく are keyed in 問題7. The reflex email and notice phrases
  「存じます」「ご覧ください／ご覧いただけます」 are therefore barred in all
  three 実用文 surfaces (10(3), 10(4), 14). See the forms section below.

## Why 〈想定→実は〉 is at 10(1), and 1 not 2

- **Count.** The cross-half cap is 2, and it counts the composed 聴解 talks
  (`jlpt-test-generation` §"One topic, one surface"). The 聴解 half is not drawn
  yet, so the 読解 side takes **1** and leaves 1 for the composer.
  - If the composed 聴解 carries two, Stage 3 re-angles 10(1). Its legal
    targets are 機構の説明 (2→3, and 問題10 would then hold it twice) or
    反論への応答 (2→3).
  - 10(1) may NOT move to 一人称の前後比較, which is at cap 3.
- **Seat.**
  - 20261008_1 ran the skeleton at 11(1) on 旅行・観光.
  - 20261002_1 ran it nowhere on the 読解 side.
  - 20260929_1 ran it at 11(4) on 食.
  - 10(1) on 科学・技術 repeats none of those seats or themes.
- **Deletion test.**
  - It applies to 10(1), and to nothing else.
  - On every other row, deleting any sentence must leave no "assumption denied"
    beat.
  - The rows most at risk:
    - **13**, 意外な観察 with 一人称. Its surprise is an OUTCOME, never 「〜と
      思っていた」.
    - **11(1) and 12(B)**, 反論への応答. Each objection is answered on its own
      terms and never set up to be knocked down.
    - **12(A)**. Its `わけではない` foil is named and rejected as a
      single-factor view. It is never attributed to someone and then denied
      with 実は.

## The RNG-picked named template

- **Not-A-but-B family.**
  - The candidate list was [ではなく, より…ほう, というより, わけではない].
    `A だけではない。B こそが〜` is excluded, because it is barred in 問題12
    and is 20261008_1's.
  - `secrets.randbelow(4)` returned 3, which is **`A わけではない`**.
  - 〜わけではない is NOT a tested form this paper (neither 問題7 nor 問題8).
  - The only 主張 closing is 12(A), so it sits there.
  - Keep 「わけではない／わけではありません」 out of every OTHER final, including
    12(B) and the 反論応答 row 11(1).
- **相関.** Placed by rule, not by RNG.
  - 相関 is barred in 問題11. 問題10 closed on it three papers running before
    20261002_1.
  - 問題13 (意外な観察) is not a 条件提示 row.
  - So it went to the 条件提示 row outside 問題11: **問題9**.
- **分裂文.** Assigned to NO row (plan 0).
  - It is barred in 問題10.
  - 20261002_1 closed 問題11 on it two papers back.
  - The 意外な観察 and 説明 rows (10(1), 10(2), 11(2), 13) are where it lands
    by reflex. Close them on something else.

## Tallies the authors must NOT break

- **Closing shape (13).** Values come from the CLOSED `CLOSING_MOVES` and
  nothing else.
  - 説明 2 (10(2), 11(2))
  - 意外な観察 2 (10(1), 13)
  - 随筆 2 (10(5), 11(4))
  - 反論応答 2 (11(1), 12(B))
  - 条件提示 2 (問題9, 11(3))
  - 主張 1 (12(A)), the only shape with a spare slot
  - 実用文・分類外 2 (10(3), 10(4))
  - No seat repeats the shape 20261008_1 put in that seat. All 13 were checked
    against its `closing_moves`.
- **Template (13 closings).**
  - Named: 相関 1 (問題9) and `A わけではない` 1 (12(A)). Every other final is
    unnamed.
  - 分裂文 **0**.
  - The three cap-1 templates are assigned to no row: 後知れ `〜ていた のだ`,
    不在の残り `〜ていない` and 先回り. The 先回り skeleton also needs
    「たびに」, which is a keyed 問題8 form here. An unnamed final that lands on
    one of them spends its only slot.
- **not-A-but-B reframe family.** This covers ではなく, というより, よりも,
  だけではなく and わけではない, and ANY final that names a foil and prefers
  the alternative (「AにないBがある」 included). Exactly **2**: 12(A) (`A わけではない`) and 11(1) (unnamed template; foil 「明かりとして比べる」物差し, after QA F4). At the cap; a third is a rewrite.
- **MOVE (10 essay surfaces, 12 A+B as one).**
  - 〈想定→実は〉 1 (10(1))
  - 機構の説明 2 (10(2), 11(2))
  - 数えたことの報告 2 (問題9, 11(3))
  - 一人称の前後比較 **3, at cap** (10(5), 11(4), 13)
  - 反論への応答 2 (11(1), 12)
  - Headroom: 機構 +1, 数えた +1, 反論 +1. 一人称 has none. 〈想定→実は〉 has
    none on the 読解 side.
  - 20261008_1 ran 数えた 3 / 機構 2 / 一人称 2 / 反論 2 / 想定 1.
- **Shared-MOVE pairs need different resolutions and no shared persona**
  (dokkai.md).
  - 数えた: 問題9 (趣味の実践者, own leisure season, 相関 with では) against
    11(3) (観察者, own exchanges, a non-相関 condition).
  - 機構: 10(2) (職業人, care or clinic mechanism) against 11(2) (解説者,
    hazard or equipment mechanism).
  - 一人称: 10(5) (職業人, a work practice) against 11(4) (学生, a sleep or
    rest practice) against 13 (趣味の実践者, a cooking or eating practice, with
    an unexpected outcome).
  - 反論: 11(1) 「反論の前提を問い直す」 (職人) against 12 「譲歩して一部を変える」
    (論者 / 利用者).
- **Persona** (cap 2 per archetype). 職業人 2 (10(2), 10(5)), 趣味の実践者 2
  (問題9, 13). Every other persona is used once.
- **Voice quota** (12 passages, 問題14 excluded).
  - **First person: at least 4.** Planned: 問題9, 10(1), 10(5), 11(1), 11(3),
    11(4), 12(B) and 13.
  - **です・ます throughout: at least 3.** Planned: 10(2), 11(1) and 12(B), plus
    the two 実用文 (10(3), 10(4)). Write です・ます and the length band
    together.

## Tested forms that must stay out of the 読解 prose (Item integrity #15)

This paper keys the following. Read the spec, not this copy, if anything
rerolls.

- **問題7:** 敬語:存じる, 〜たとたん, 〜ことになっている, 敬語:ご覧いただく,
  〜ないもの(だろう)か, 〜ぬきにして, 〜にかかわらず, 〜ことだろう・ことか,
  〜てはじめて, 〜がたい, 〜あげく, 〜ないことには. The 敬語 count is 2 of 12,
  at the cap.
- **問題8:** 経過状況(〜つつ…する), 〜たびに, 状況限定(〜状況において…),
  〜をきっかけに, 〜ほど〜はない.

Consequences:

- **The 敬語 keys are the reflexes of the 実用文 rows.** None of these may
  appear anywhere:
  - 「存じます」「存じております」 (email);
  - 「ご覧ください」「ご覧いただけます」 (notice and flyer: write
    「〜を見てください」「〜に載っています」 instead).
- **Notice and flyer reflexes.** 「〜ことになっています」 and 「年齢にかかわらず」
  are the stock phrasings of 10(3) and 14. Use none.
- **The reflex frames of 一人称の前後比較 (10(5), 11(4), 13).**
  - 「〜をきっかけに」, 「〜てはじめて／て初めて」 and 「〜たとたん」 are
    banned. (「〜て初めて」 is also a dokkai.md rhetoric marker.)
  - So are 「〜たびに」, 「〜つつ」 and 「〜あげく」.
  - Write 「〜てから」「〜ようになって」 and plain sequence instead.
- **〜ほど〜はない.** This is also why 問題9's 相関 is written with 「では」. No
  「ほど」 comparative-superlative anywhere.
- **〜状況において／において** is the stock frame of 説明 and 機構 prose (10(2),
  11(2)). Use none.
- **〜がたい.** This is the lexical trap. 「ありがたい」「ありがたく」 contain the
  string, and the email reflex 「ありがたく存じます」 hits two keyed forms at
  once. Use none.
  - Also avoid 「〜しがたい」「信じがたい」. 「信じがたい」 is the reflex of a
    意外な観察 row (10(1), 13).
- **〜ないことには, 〜ぬきにして, 〜ないもの(だろう)か, 〜ことだろう・ことか,
  〜にかかわらず:** none anywhere.
  - 「〜ないことには…ない」 is the reflex of a 主張 final (12(A)).
  - 「〜ないものか」 is the reflex of a 随筆 musing (10(5), 11(4)).
  - 「〜ことか」 is the reflex of an exclamatory 随筆 close.
- **A prose grep is owed for the general-purpose 問題8 frames** (`exam-blueprint`
  §"A `grammar_p8` draw whose form is a general-purpose sentence pattern"):
  たびに, をきっかけに, つつ and において.
  - Grep every surface. Re-word every hit except at most one, and that one must
    not be in the tested frame. Prefer 0.
- **Stage 3 re-grep.** Every form above goes into the Stage-3 keyed-form
  re-grep, with its counts and frames (文末／連用／連体). That includes the
  問題9 [論理接続] key once the 文法 author has written the cloze.

## The two things that get checked by hand

1. **The unnamed finals must not share a skeleton** with each other, with the
   named ones, or with 20261008_1's skeleton in the same 大問 (table above).
   The pairs at risk:
   - 10(5) against 11(4): both 随筆, both 一人称の前後比較.
   - 問題9 (相関) against 11(3) (条件提示, non-相関): two DIFFERENT condition
     skeletons.
   - 11(1) against 12(B): both 反論応答, both 反論への応答.
   - 10(1) against 13: both 意外な観察, and neither is a cleft.
   - 10(2) against 11(2): both 説明, and neither is a cleft.
   - 12(A) (わけではない) against 12(B): read A against B FIRST.
2. **The MOVE column and the TEMPLATE column are read separately**, once down
   each, and both are re-read after every repair (`jlpt-test-generation`
   §"One topic, one surface"). Run the deletion test on every row except 10(1).
   No row other than 10(1) may carry an attributed-belief → denial → 実は beat.
