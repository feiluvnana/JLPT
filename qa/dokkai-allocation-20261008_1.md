# 読解 allocation table — 20261008_1 (BLUEPRINT-ASSIGNED, binding)

Stage 1 filled this in **before any prose exists**, as
`question-authoring/references/dokkai.md` §"Thirteen surfaces", §"The named
templates" and §"The rhetorical-MOVE allocation table" require. Authors do NOT
re-choose the shape, template or MOVE columns. Each author fills the two
**AUTHOR FILLS** columns from the prose they write and hands the table back:
edit this file, your own rows only.

**Denominators** (dokkai.md §"The denominator"):
- Axis 1 (theme) has 13 rows, with 問題12 A+B as ONE row.
- Axis 2 (closing shape and final-sentence template) has 13 closings, with
  問題12 A and B SEPARATE and 問題14 outside.
- The MOVE cap counts essay surfaces only, with 問題12 A+B as ONE (10 here).

**Themes** come from `tests/20261008_1/test_spec.json` `items.reading_topics[i]`.
Index → surface: 0→問題10(1) … 4→問題10(5), 5→問題11(1) … 8→問題11(4), 9→問題12,
10→問題13, 11→問題14. Base draw `make sample 20261008_1 SEED=24370401`, no
reroll (`qa/blueprint-rerolls-20261008_1.md`). Author each surface's SUBJECT
from its entry's `theme`. Keep it off that entry's full `avoid` list in the
spec, off any re-wording of an avoid string, and off every previous-paper
CLAIM below (exam-blueprint Part II, "claims, not only subjects").

## Who owns which rows

- **問題9 (the cloze) belongs to the 文法 (問7–9) author.**
  `scaffold_sections.py` emits the cloze inside `問7-9_文法.md`.
- **問題10–14 belong to the 読解 author.**
- Both authors get this whole table, because the caps are counted across all
  thirteen closings.

## The allocation

| surface | owner | theme | closing shape (≤2 each) | final-sentence template (≤2 each; cap-1 rows unused) | MOVE | voice / persona (plan) | AUTHOR FILLS: final sentence | AUTHOR FILLS: which previous claim (20261008_1's ← 20261002_1 key) this is NOT, and why |
|---|---|---|---|---|---|---|---|---|
| 問題9 cloze | **文法** | **行政・手続き** (author-composed; RNG, see below) | 反論応答 | — (unnamed). Not a cleft, not the not-A-but-B family, not 「〜ても、〜があれば、〜ことができる」 (20261002_1 問題9) | 反論への応答 | 評論 or 解説; 職業人 (e.g. a counter clerk) or 論者. Objection taken seriously, answered on its own terms; no 「もっとも」 knock-down | 「ただ、その一時間にも、そこにしか来られない人のための入り口を、一つ開けておきたい。」 — unnamed skeleton 〈決まりは続けていく。ただ、Xにも、Yのための入り口を一つ開けておきたい〉 (rule kept + one exception channel); 11(4) must not reuse it. SUBJECT 「役場窓口の昼休み閉鎖」: 町役場住民課の職員（一人称・だ／である）が、正午〜一時の窓口閉鎖に寄せられた住民の手紙（昼休みしか来られない）に、閉鎖の理由（昼は手薄で待ち時間・間違いが多い）と木曜夜・土曜午前への振り替えで答え、夜も土曜も来られない人がいたことは認めて、前日までの電話予約で昼に一人残る例外を作った。Body 645 JP chars. **Keyed forms for the Stage-3 grep (must not recur in 読解 prose):** [論理接続] 49「かといって」 (distractors つまり／たとえば／なぜなら); [文末モーダル] 51「べきだった」 (べき family; distractors べきだ／べきではない／べきではなかった); [慣用・形式名詞] 48「耳が痛い」 (耳が早い／耳を貸す／耳が遠い); [内容推論] 50「仕事を休まずに来られる」. Prose carries none of this paper's 問題7/8 keyed forms (grep: として／といった／ものだ／とは／にしたら・にすれば／わけ／に応じて／に基づいて／ばかりに／ございます etc. = 0) and no もっとも／ではなく／こそ／だけでは／つもり. 問題9 option hand-diff vs 20261002_1 and 20260929_1 問題9 (all blanks): 0 repeats except the ordinary connective なぜなら (20260929_1-48, exempt); no はず/もの family (used by those two papers); no echo of this paper's quick_response/grammar_p7/grammar_p8 strings. | NOT 20261002_1 問題9 (writing one line of why you clipped an article brings back that day's feeling): a different assertion — about when a counter is open and for whom, not about recording a reason. NOT the "X fails because a link or cue is missing, and supplying it fixes X" family (10(2), 10(5)): the objector lacks open HOURS, not a cue, and the answer is a moved schedule plus an appointment exception. NOT 13's "a role sticks to one person": nobody ends up holding a role. No 〈想定→実は〉 beat (no attributed belief denied; the concession 「考えが及んでいなかった」 admits an unconsidered group), no 「もっとも」 knock-down. |
| 問題10(1) | 読解 | 科学・技術 | 説明 | **`〜のは B だ（分裂文）`** (the paper's one cleft). 問題10 carries no cleft bar: 20261002_1 closed 問題10 on no named template | 機構の説明 | 解説; 解説者 or 職業人. DOMAIN must NOT be heat/food heating or appliances (20261002_1 11(1)), nor a measuring protocol (20260929_1 13) | 「夕方の空が赤く見えるのは、その長い道のりの間に青い光が先に散って抜け落ち（注）、残った赤い光が目に届くからだ。」 — 分裂文 (the paper's one). SUBJECT 「夕焼けが赤い理由」: 光が空気の粒で散る、青は散りやすく赤は散りにくい、夕方は光の道のりが長い。解説者, だ／である. | NOT 20261002_1 11(1) (a package instruction exists because of a hidden heating mechanism): no tool, label, manual or instruction is explained — a sky colour is. Domain is atmospheric light, not appliance/heating physics and not a measuring protocol. NOT the cue-missing family: nothing is missing and nothing is fixed. |
| 問題10(2) | 読解 | 交通 | **実用文・分類外** (business email) | — | （実用文） | メール; 実務者. No 「ございます」 (keyed, 問題7) and no 「申し上げ」 needed | 「よろしくお願いいたします。」＋署名 (実用文). SUBJECT 「校外学習で42人が電車に乗る前の事前連絡の要否」: 小学校の担任から鉄道会社お客さま係へのメール。 | NOT 20261002_1 10(4) (ask a supplier to take back used containers): an inquiry whether advance notice is needed; nothing is returned or collected. Not a handover between contacts (20260929_1 10(3)), not a commission request (20260928_2 10(1)). No ございます／申し上げ. |
| 問題10(3) | 読解 | デジタル化 | 条件提示 | — (unnamed). **NOT 相関** (問題10 closed on 相関 three papers running before; 11(2) holds the paper's one). Not 「〈条件〉が来るまで、〈物〉は…待っている」 (20261002_1 10(5)), not 「〜ない以上、…ことになる」 (10(2)). A checkable condition, no exhortation | 数えたことの報告 | 一人称随筆; 利用者 counting their OWN use over one bounded span (one day or one week). The count is not introduced as contradicting an expectation | 「調べたその場で一度紙の端に書き写してから使った字は、その週のうちに二度調べることはなかった。」 — unnamed 〈Xした字は、その週のうちにYすることはなかった〉 (condition → outcome; no では/ほど, not 相関). SUBJECT 「一週間、スマートフォンで調べた漢字を数える」: 利用者本人の一週間（31回中12回が同じ字の調べ直し）。 | NOT 20261002_1 10(5) (auto-backup waits until three conditions meet) and not its 〈条件〉が来るまで…待っている skeleton; not 10(2)'s 〜ない以上…ことになる. Not the cue-missing family: no link between two things is missing — the claim is that copying a character once by hand ends the repeat look-ups. The count is a plain one-week tally, not set against an expectation; no phone-photo, cloud or neighbourhood-app subject. |
| 問題10(4) | 読解 | 文化・伝統 | 随筆 | — (unnamed). Must differ from 11(3)'s skeleton | 一人称の前後比較 | 一人称随筆; 趣味の実践者. The "before" is a PRACTICE, never a belief (no 「つもりだった」「と思っていた。ところが」) | 「今の私の句には、どれも、それを書きつけた（注3）道の角が一つずつついてくる。」 — unnamed 〈今のNには、どれも、Xが一つずつついてくる〉. SUBJECT 「俳句を机でなく散歩の途中で作る」: 趣味の実践者。前＝季語の本から言葉を選んで机で作る（PRACTICE）、後＝足を止めた所で目の前のものを書く。 | NOT 20261002_1 11(2) (reading whole poems aloud turned cards into poems) and not its 「〈前のN〉は、今では〜として…残っている」 skeleton: the claim is where a poem is made and that the place stays attached to it. The before is a practice, never a belief (no つもりだった／と思っていた。ところが). No かるた, festival, exhibition, 手書き or calligraphy subject. Skeleton differs from 11(3)'s 〈今は、Xたら、…のを待つことにしている〉. |
| 問題10(5) | 読解 | メディア・情報 | **実用文・分類外** (notice / お知らせ) | — | （実用文） | 通知. No 「ございます」 | 「ご理解とご協力をお願いいたします。」＋署名 (実用文). SUBJECT 「図書館が全国紙の保存期間を1年から3か月に短くするお知らせ」 (地元の新聞は1年のまま、古い記事は一階の記事検索のパソコンで)。 | NOT 20261002_1 10(1) (児童館の平日午前を親子の時間にする): a storage-period change, not a time slot. Not a 回覧板/app notice (20260929_1 10(2)), a school textbook notice (20260928_2 10(5)), a newsletter, clippings or translated-comics subject. No ございます, no 掲載／臨時 (問題2/6 targets). |
| 問題11(1) | 読解 | 旅行・観光 | 意外な観察 | — (unnamed). **NOT 分裂文** (cross-paper bar: 20261002_1 11(1)). Not the not-A-but-B family (12(B) holds it) | **〈想定→実は〉** (the paper's ONLY one on the 読解 side) | 一人称随筆; 旅行者 | 「この島では、船の時刻も、島の人の出かける予定も、毎日、少しずつ遅れていく潮の時刻に合わせて決まっていく。」 — unnamed (no のは, not 分裂文, no foil). SUBJECT 「島の船の時刻表が毎日ずれる理由」: 旅行者。想定「船を動かす人の都合でずらしている」→「実はそうではなかった」→ 浅い港には潮が満ちている間しか入れず、その時刻が毎日約50分遅れる。The paper's ONLY 〈想定→実は〉; deletion test: removing 「ところが…実はそうではなかった」 collapses the passage. | NOT 20261002_1 11(1) (the package's heating instruction exists for a hidden mechanism): the final asserts that the boat and the islanders' plans both run on tide time, not why a printed instruction says what it says. The timetable is the nearest echo of that claim, which is why the final was re-angled onto the islanders' day — QA should read the two together. Not a group-tour course choice (20260929_1 聴解5-2). Not 分裂文 (cross-paper bar), not the not-A-but-B family. |
| 問題11(2) | 読解 | 防災 | 条件提示 | **`A では/ほど B が多い（相関）`** (the paper's one). **NOT 分裂文** (bar) | 数えたことの報告 | 解説 or 一人称; a 係 at ONE drill or one event (not N年分 records — persona bar). No victims, no disaster narrative (neutrality) | 「名簿の記録では、出る前に両どなりの家の戸をたたいた班ほど、そろうまでに時間はかかったが、最後まで来ない家は少なかった。」 — 相関 (the paper's one). SUBJECT 「一回の避難訓練で、両どなりに声をかけてから出た班の集まり方」: 町内会の係が一回の訓練で到着時刻と来ない家を数える（22分 vs 15分、3世帯 vs 11世帯）。 | NOT 20261002_1 問題14 (extinguisher refill notice) and not 13 (a role sticks to one person). Nearest family is "a missing cue, supplied, fixes X" (10(2)/10(5)); this claim is a trade-off — knocking slows full assembly AND cuts no-shows — so nothing is simply fixed. One drill, not an N年分 record; no victims, no 119, no block walls, no 札 subject; the count is not set against an expectation. |
| 問題11(3) | 読解 | 人間関係 | 随筆 | — (unnamed). **NOT 分裂文** (bar). Must differ from 10(4) and from 「〈前のN〉は、今では〜として…残っている」 (20261002_1 11(2)) | 一人称の前後比較 | 一人称随筆; a friend or colleague (not 幹事, not 引き継ぎ) | 「今は、美香の声が途中で小さくなったら、手にしていた湯のみ（注4）を置いて、次の言葉が出てくるのを待つことにしている。」 — unnamed 〈今は、Xたら、Yを置いて、Zのを待つことにしている〉. SUBJECT 「友人の相談の電話で、すぐ助言するのをやめて最後まで聞く」: 一人称。前＝話の途中で意見を言っていた（PRACTICE）、後＝口をはさまず待つ。 | NOT 20261002_1 13 (organiser role sticks via thanks and unwritten facts): nobody holds a role; NOT 20261002_1 11(2) 「〈前のN〉は、今では〜として…残っている」. No 幹事, handover, thanking ritual, 呼び方 or 紹介 subject. The before is a practice (advising mid-story), not a corrected belief. Skeleton differs from 10(4). |
| 問題11(4) | 読解 | 食 | 反論応答 | — (unnamed). **NOT 分裂文** (bar). Not 「それで今は、AにはX、BにはYを使い分けている」 (20261002_1 11(3)) and not 「〜ので、…ままでも、…V-ていく」 (11(4)). Must differ from 問題9 | 反論への応答 | です・ます; 職業人 (e.g. a shop or canteen cook), NOT 家庭の料理人 (20261002_1 11(3)). The objection comes from customers or a colleague, not family | 「棚のパンには、焼き上がってから一時間の休みを取らせ、それから袋に入れています。」 — unnamed 〈NにはXの休みを取らせ、それからYています〉 (no のは, no foil, no わけではない; 先回り regex checked: no 前に／たびに／先に). SUBJECT 「焼いたパンを一時間置いて売るパン屋と、冷ますと香りが逃げるという客の声」: 職業人（パン屋）、です・ます。客の声を「たしかに」「私も惜しい」と認めたうえで、家で切ったときにつぶれない形のために一時間を守り、焼きたてと一時間置いたパンの切り口を比べて見せて説明する（hold and explain; no schedule change, no exception, no relocated cause）。Re-angled after qa-report-20261008_1 F3 and round-2 R2-F1. | NOT 問題9 (a town-office clerk keeps noon closing and opens ONE exception channel after admitting an unconsidered group): nothing is changed and no exception is opened; none of 問題9's 決まり／これからも／続けていく／考えが及ぶ. NOT 〈想定→実は〉 (R2-F1): deletion test run — the customer's 「香りも逃げてしまう」 is conceded, never denied, and no 'real cause' is relocated (the oven paragraph is gone), so there is no denial sentence to delete; cross-half count back to 2 (11(1), 聴解2-4番). NOT 20261002_1 11(3) (use homemade dashi only where its difference shows) and not its 11(4) 〜ので、…ままでも、…V-ていく. No dashi, portion, bowl or vegetable-intake subject; no もっとも knock-down. |
| 問題12(A) | 読解 | 環境 | 説明 | — (unnamed). Not a cleft (10(1) holds it). Not 「〜のが、…賢いやり方である」 (20261002_1 12(A)). Read against 12(B) FIRST | 機構の説明 (A+B = one surface) | 評論 or 解説; 解説者 | 「池に水の流れをつくり、底の泥を時々取り除けば、栄養は水面の近くにとどまらず、夏の間も水は澄んだまま保たれる。」 — unnamed 〈Xし、Yすれば、Zず、Wまま保たれる〉 (not cleft). SUBJECT (A+B) 「夏に公園の池の水が緑になる理由」: A＝日光・温かい水・栄養（落ち葉や泥）と動かない水の仕組み。 | NOT 20261002_1 12(A) (bulk-buying daily goods is the smart household move) and not its 「〜のが、…賢いやり方である」: no purchase-unit or household-budget claim. Explains a mechanism and its condition; no 「〜と思われがちだが」. Read against 12(B): A's remedy is water flow + mud removal, B's is not feeding bread; the common point is small plants multiplying. |
| 問題12(B) | 読解 | 環境 | 主張 | **`A だけではない。B こそが〜`** (RNG, below; the paper's only not-A-but-B member). Not 「〈X〉は、…という仕組みの上に成り立っている」 (20261002_1 12(B)) | ″ | です・ます; 論者. Name the foil A in the final, but do NOT attribute it as a 通説 that gets denied (no 「〜と思われがちだが」「実は」): 12 must not become a second 〈想定→実は〉 | 「池の水を緑にしているのは、夏の日ざしだけではありません。私たちが何気なく投げ入れるパンこそが、池の水の色を変えているのです。」 — `A だけではない。B こそが〜` (the paper's only not-A-but-B member; foil A＝夏の日ざし, named and not attributed). 論者, です・ます. | NOT 20261002_1 12(B) (bulk buying's cheapness rests on paying months ahead) and not 「〈X〉は、…という仕組みの上に成り立っている」: no money claim. The foil is not presented as a 通説 that gets denied (no 思われがち／実は), so 12 is not a second 〈想定→実は〉. No container return, forestry, clothing re-use, leaves, green-curtain or bee subject. |
| 問題13 | 読解 | 住まい | 主張 | — (unnamed). Not 分裂文 (20260929_1 問題13 used it; not barred, but avoid), not the not-A-but-B family. Not 「〜ている〈集団〉では、Xは…として受け取られる」 (20261002_1 問題13) | 数えたことの報告 | 一人称, です・ます; 住人 counting over one bounded span (e.g. one month or one season). Ends on a prescription to the reader; no rejection of a single-factor view | 「寒い土地で古い家に住む方は、天気予報でマイナス4度より下がると聞いた晩には、日の当たらない側を通る管の蛇口を、細く開けてから休んでください。」 — unnamed prescription 〈〜方は、〜晩には、〜を、〜てから休んでください〉. SUBJECT 「古い借家の台所の水が凍る朝を一冬数える」: 住人、です・ます。12〜2月の90朝で6回、すべて予報が氷点下4度以下の晩の翌朝、凍るのは北側の壁の外を通る台所の管だけ。 | NOT 20261002_1 13 (the organiser role sticks to one person): no role. NOT 20261002_1 10(3) storage placement, and no moving, repair-scheduling, lighting or condensation (窓を開ける5分) subject. No purchase-unit/household-budget argument (a water-cost aside was cut for that reason). Not a measuring protocol: the narrator copies a forecast onto a calendar and places no instrument. One season, not N年分; the count is not set against an expectation; no rejection of a single-factor view. |
| 問題14 | 読解 | 医療・福祉 | (outside axis 2 — flyer, no closing) | — | （実用文） | 案内. No 「ございます」. Deadlines as dates (qa-report-20261002_1 F12) | — | SUBJECT 「しらとり市 訪問理容・美容の案内」 (対象者2条件、料金表3行＋出張料500円、1回1,500円の利用券は出張料に使えない、初回は申請書に保険証か手帳のコピー、前の月の20日までに電話、訪問は火・金、変更は前日午後5時まで). NOT 20261002_1 14 (extinguisher refill): a different document type and errand; not a scholarship call or child-seat rental. Deadlines are a calendar rule (前の月の20日) and a 前日 offset, never 「前の週の〜曜日」. No ございます. |

## The previous paper (20261002_1), per 大問 — what is barred here

Read from its shipped `tests/20261002_1/言語知識・読解.md` with the gate's own
`dokkai_closing_scopes()` / `passage_final_sentence()` /
`FINAL_SENTENCE_TEMPLATES`. The MOVEs are the post-round-2 column of
`qa/dokkai-allocation-20261002_1.md` (10(3) re-angled to 一人称の前後比較).

| 大問 | 20261002_1 named templates | 20261002_1 unnamed skeletons (do not reuse in the same 大問) | 20261002_1 MOVEs |
|---|---|---|---|
| 問題9 | none | 〈〜ても、〜があれば、〜ことができる〉 | 一人称の前後比較 |
| 問題10 | none | 10(2) 〜ない以上、…ことになる; 10(3) 〈N〉は、…ところに決めておくとよい; 10(5) 〈条件〉が来るまで、〈物〉は…待っている; 10(1)(4) 実用文 | 数えたことの報告 (10(2)), 一人称の前後比較 (10(3)), 反論への応答 (10(5)) |
| 問題11 | **`〜のは B だ（分裂文）`** (11(1)) | 11(2) 〈前のN〉は、今では〜として…残っている; 11(3) それで今は、AにはX、BにはYを使い分けている; 11(4) 〜ので、…ままでも、…V-ていく | **機構の説明 ×2** (11(1), 11(4)), 一人称の前後比較 (11(2)), 反論への応答 (11(3)) |
| 問題12 | none | A 〜のが、…賢いやり方である; B 〈X〉は、…という仕組みの上に成り立っている | 反論への応答 |
| 問題13 | none | 〜ている〈集団〉では、Xは…として受け取られる | 機構の説明 |

**Template bar (gated, `check_dokkai_template_repeat_prev_paper`):** no 問題11
surface closes on 分裂文, including 「大切なのは」「注目すべき点は」「確かめるべきは」
and 「〜こと／点は、…だ」 variants. No other 大問 is barred, because 20261002_1
closed no other 大問 on a named template. The unnamed skeletons above are a QA
read, not a gate.

**MOVE bar (dokkai.md, per 大問):** 20261002_1 used 機構の説明 twice in 問題11, so
問題11 here gets at most one. It gets **0**. No other 大問 of 20261002_1 used a
MOVE twice. No seat carries the MOVE 20261002_1 put in that seat.

**Persona bar:** 「〈役〉が〈N年分〉を数える」 ran twice in 20260929_1 (10(4)
世話役 6年分, 10(5) 役場職員 2年分). It skips two papers, so it is still OFF this
paper. The three 数えたことの報告 rows (10(3), 11(2), 13) each count ONE bounded
span (a day, a week, one drill, one month or one season). None is a role-holder
reading back N years of records, sheets, postcards or notebooks. Each count is a
plain report: it is not introduced as contradicting an expectation, which would
be the 〈想定→実は〉 re-skin.

## The previous paper's 13 claims — what each surface must NOT restate

From `logs/topics.json`, row 20261002_1, `claim` (問題12 A and B listed
separately, so 14 lines). Write, in the last column of your row, which of these
your surface is NOT, and why. "Not" means a different assertion, not only a
different subject: two surfaces asserting the same move on different subjects
are one essay twice.

| key | 20261002_1 claim | theme there | nearest row here (read these two together) |
|---|---|---|---|
| 問題9 | 記事に切り抜いた理由を一行書き添えておけば、何年たって開いても、その記事を選んだ日の自分の気持ちまで戻ってくる。 | メディア・情報 | 10(5), 10(4) |
| 問題10(1) | 来月10日から平日の午前は小さな子どもと家族のための時間にするので、遊び方とベビーカーの置き場所に協力してほしい。 | 子育て・家族 | 10(5) notice |
| 問題10(2) | 案内図があっても人が尋ねに来るのは、予約票の番号と図の診療科の名前とを結ぶ手がかりがないからである。 | 医療・福祉 | 14, 問題9 |
| 問題10(3) | いつも使う物のしまい場所は、使う場所からすぐ手の届くところに決めておくとよい。 | 住まい | 13 |
| 問題10(4) | 新しい容器を届けに来たときに、使い終わった容器を持ち帰ってもらえるかを知りたい。 | 環境 | 10(2) email, 12 |
| 問題10(5) | 自動保存があてにならないように見えるのは、充電・家の無線・画面の消えた時間の三つがそろうまで写真が送られないからである。 | デジタル化 | 10(3), 10(1) |
| 問題11(1) | 凍った物を電子レンジで温めるとむらが広がるので、熱くなった所の熱を冷たい所へ分ける時間をとることが大切で、袋の温め方の指示はそのためにある。 | 科学・技術 | 10(1), 11(4) |
| 問題11(2) | 読み手として歌を終わりまで声に出したことで、初めの音で覚えていた札が一つの歌として聞こえるようになった。 | 文化・伝統 | 10(4) |
| 問題11(3) | 取っただしと粉のだしの違いは料理によって出たり隠れたりするので、味つけのうすい料理にだけ取っただしを使えばよい。 | 食 | 11(4) |
| 問題11(4) | 下りでは筋肉が伸ばされながら体を受け止めるので、息は楽でも筋肉に小さな傷がつき、翌日に痛みが出る。 | スポーツ・余暇 | 10(1), 11(1) |
| 問題12(A) | 傷まず毎日決まった量を使う日用品は、まとめて買うほうが安く、無駄にもならないので家計に賢い。 | 消費・経済 | 12(A), 13 |
| 問題12(B) | まとめ買いの安さは何か月分ものお金を先に払うことの上に成り立っているので、買う前にその月のほかの払いが済むかを考えるべきだ。 | 消費・経済 | 12(B), 13 |
| 問題13 | 幹事役が一人に偏るのは、お礼の言葉と書かれない事情と互いの気づかいが重なるからで、事情を共有し次の幹事を会の終わりに決めれば役は回る。 | 人間関係 | 11(3), 問題9 |
| 問題14 | 消火器の詰め替えと引き取りの料金・受付日と場所・申し込みと受け取りの方法・窓口の扱い・本数の上限を知らせる。 | 防災 | 11(2), 14 |

Claim families to stay off, read across the column:
- **"X fails because a link or cue is missing, and supplying it fixes X"**
  (10(2), 10(5)). 問題9, 10(1), 10(3) and 14 must not assert it.
- **"use A only where its difference shows"** (11(3)). 11(4) must not end on a
  use-it-here-not-there split.
- **"a tool's printed instruction exists because of a hidden mechanism"**
  (11(1)). 10(1) must not explain why a label, manual or package instruction
  says what it says.
- **"buy in bulk / pay up front"** (12(A)/(B)). 12 and 13 must not make a
  household-budget or purchase-unit argument.
- **"a role sticks to one person because of thanks and unwritten
  circumstances"** (13). 11(3) and 問題9 must not explain who ends up holding a
  role.

### Domains of the previous papers' 科学・技術 / 消費・経済 surfaces

| paper | surface | theme | DOMAIN (stay out of it on 10(1), 12 and 13) |
|---|---|---|---|
| 20261002_1 | 問題11(1) | 科学・技術 | domestic appliance physics: microwave heating of frozen food, and why the package's heating instructions say what they say |
| 20261002_1 | 問題12(A)/(B) | 消費・経済 | household purchasing: bulk buying of daily goods, unit price against paying up front |
| 20260929_1 (two back, minor) | 問題13 | 科学・技術 | measurement protocol: where an official thermometer is placed and why |
| 20260929_1 (two back, minor) | 問題11(1) | 消費・経済 | clothes-buying timing: sale-season buying against buying when needed |

This paper's only 科学・技術 surface is 10(1). It may not be appliance or
heating physics, a measuring or observation protocol, or "why the instruction
says X". This paper has no 消費・経済 surface (it is barred from the cloze, see
below). 12 環境 and 13 住まい must still keep off a purchase-unit or
household-budget claim.

## Avoid lists, per row (the spec holds the full list; this is the near history)

The full `avoid` list for 10(1)–14 is `items.reading_topics[i].avoid` in the
spec. It runs 23–60 subjects per theme and must be read in full. The rows below are
the previous two papers' same-theme subjects (読解 and 聴解), which is where a
near-miss is likeliest:

- **問題9 行政・手続き** (no spec seat): the used list is
  `used_subjects_by_theme()['行政・手続き']`, 23 subjects, all of which are off.
  Among them: tax-return counters and numbered tickets; ID-document checks;
  convenience-store certificates; pension procedure guides; signing or
  form-filling help at a counter; online certificate applications; public-comment
  notices; proxy requests for 住民票; towed-bicycle retrieval; dog-registration
  sessions; やさしい日本語 notices; a clerk's years at a counter; and, two papers
  back, **20260929_1 11(3) 家族の書類を本人の前で読み上げる**: no filling in
  forms on a family member's behalf. 20261002_1 has no 行政・手続き surface.
- **10(1) 科学・技術:** 20261002_1 11(1) microwave heating; 20260929_1 13
  thermometer placement. Also off: failed-experiment publishing, citizen
  river-creature counts, cloud formation (all in the spec list).
- **10(2) 交通 (email):** no 交通 surface in either previous paper. The full
  list (46) is in the spec.
- **10(3) デジタル化:** 20261002_1 10(5) automatic photo backup; 20260929_1
  10(2) 回覧板 app. No phone-photo, cloud-backup or neighbourhood-app subject.
- **10(4) 文化・伝統:** 20261002_1 11(2) かるた reader; 聴解1-5 exhibition hanging;
  聴解2-6 mud festival. No かるた, no festival, no exhibition set-up.
- **10(5) メディア・情報 (notice):** 20261002_1 問題9 clippings notebook;
  20260929_1 10(5) town newsletter column; 聴解3-3 anime abroad. Not a
  newsletter, clippings, or translated-comics notice.
- **11(1) 旅行・観光:** 20260929_1 聴解5-2 group-tour half-day courses
  (cycling to an author's house, brush-making). Not a course choice on a group
  tour.
- **11(2) 防災:** 20261002_1 問題14 fire-extinguisher refill. Also off (older):
  119 calls, block-wall inspection. No extinguishers, no emergency-call procedure.
- **11(3) 人間関係:** 20261002_1 13 organiser role sticking to one person;
  20260929_1 10(3) handover of phone-only agreements; 聴解: chance reunion,
  modesty, apology. No 幹事, no handover, no thanking ritual.
- **11(4) 食:** 20261002_1 11(3) home dashi vs powder; 20260929_1 11(4) bowl
  size; 聴解3-4 vegetable intake; 聴解4-4 portion too big. No dashi, no portion,
  bowl or vegetable-intake subject.
- **12 環境:** 20261002_1 10(4) ink-container take-back; 聴解2-1 forestry
  event; 20260929_1 聴解2-3 shirt re-use. No container return, forestry, or
  clothing re-use.
- **13 住まい:** 20261002_1 10(3) storage placement; 聴解2-2 moving estimate;
  聴解2-5 repair-day mix-up; 20260929_1 10(1) unopened moving boxes. No storage,
  moving or repair-scheduling subject.
- **14 医療・福祉:** 20261002_1 10(2) hospital wayfinding vs ticket numbers;
  聴解3-4 care robots; 20260929_1 聴解3-5 doctor-shortage scholarships. Recent
  問題14 document types are off as well: fire-extinguisher refill (20261002_1),
  scholarship call (20260929_1) and child-seat rental (20260928_2). Pick a
  different document type and errand.

## Headline surfaces — rule 4 and the rule-4b subject diff

- **Rule 4 (themes).** This paper's 読解 headlines are 問題9 行政・手続き,
  問題12 環境, 問題13 住まい and 問題14 医療・福祉.
  - 20261002_1 headlined メディア・情報, 消費・経済, 人間関係 and 防災, plus
    聴解問題5 働き方 and 睡眠・健康.
  - 20260929_1 headlined 働き方, 睡眠・健康, 科学・技術 and 教育, plus 聴解問題5
    スポーツ・余暇 and 旅行・観光.
  - **No overlap with either paper.** The two-back budget of one is unspent.
    This paper's 聴解問題5 theme is unknown until `make mp3` (WARN-only draw
    audit).
- **Rule 4b (subjects).** Each headline author writes a 5–15-char SUBJECT
  first. Diff it against all 13 読解 and 21 聴解 subjects of 20261002_1 in
  `logs/topics.json` `surfaces`. Same setting with a different issue is allowed
  and goes into `notes`. Same setting with the same issue means re-subject.
  Known near-hits:
  - 問題9 行政・手続き: 20261002_1 has no 行政 surface. 聴解2-5 (repair-day
    mix-up) and 聴解1-4 (rebooking a ticket) are not 行政. Stay off counters
    where people ask where to go (that is 10(2)'s 案内台 claim, one paper back).
  - 問題12 環境: 20261002_1 10(4) ink containers; 聴解2-1 forestry.
  - 問題13 住まい: 20261002_1 10(3) storage; 聴解2-2 moving; 聴解2-5 repair day.
  - 問題14 医療・福祉: 20261002_1 10(2) hospital map; 聴解3-4 care equipment.

## 問題9's theme is AUTHOR-COMPOSED; 行政・手続き was drawn by RNG from three legal values

- **Rule 3.** The 12 drawn themes are taken: 科学・技術, 交通, デジタル化,
  文化・伝統, メディア・情報, 旅行・観光, 防災, 人間関係, 食, 環境, 住まい and
  医療・福祉. That leaves 睡眠・健康, 働き方, 教育, 子育て・家族, 地域活性化,
  消費・経済, スポーツ・余暇 and 行政・手続き.
- **Rules 4 and 4c.** A cloze candidate is free only if it headlines NEITHER of
  the previous two papers. That bars メディア・情報, 消費・経済, 人間関係, 防災,
  働き方 and 睡眠・健康 (20261002_1), and 科学・技術, 教育, スポーツ・余暇 and
  旅行・観光 (20260929_1).
- **Legal: 子育て・家族, 地域活性化, 行政・手続き.** `secrets.randbelow(3)`
  returned index 2, which is **行政・手続き**.
- The cloze is 反論への応答: someone's objection to a procedure or a counter
  practice is conceded where it is right and answered on its own terms. It is
  not a strawman, and it opens on no 「もっとも」 knock-down. No politics or
  elections (neutrality).

## Why 実用文 sits at 10(2) and 10(5) — RNG

- The slots used for 実用文 recently: 20261002_1 used 10(1) and 10(4).
  20260929_1 used 10(2) and 10(3). 20260928_2 used 10(1) and 10(5).
- 10(5) is the only slot neither previous paper used, so it takes one.
- The second slot came from `secrets.randbelow(2)` over {10(2), 10(3)}, the two
  slots used only two papers back. It returned index 0, which is **10(2)**.
- A second `secrets.randbelow(2)` decided which slot gets which document. It put
  the **business email at 10(2)** (交通) and the **notice at 10(5)**
  (メディア・情報).
- **10(2) email.** It may not be a handover between contacts (20260929_1
  10(3)), an ink-container take-back (20261002_1 10(4)), or a commission
  request (20260928_2 10(1)).
- **10(5) notice.** It may not be a 児童館 time-slot notice (20261002_1 10(1)),
  a 回覧板/app notice (20260929_1 10(2)), or a school textbook notice
  (20260928_2 10(5)).

## Why 〈想定→実は〉 is at 11(1), and 1 not 2

- **Count.** The cross-half cap is 2, and it counts the composed 聴解 talks
  (`jlpt-test-generation` §"One topic, one surface"). The 聴解 half is not drawn
  yet, so the 読解 side takes **1** and leaves 1 for the composer.
  - If the composed 聴解 carries two, Stage 3 re-angles 11(1).
  - Its legal targets: 機構の説明 (問題11 has 0 of the 1 the per-大問 bar
    allows, paper-wide 2→3), 一人称の前後比較 (2→3) or 反論への応答 (2→3).
  - It may NOT move to 数えたことの報告, which is at cap 3.
- **Seat.** 20261002_1 ran the skeleton nowhere on the 読解 side after round 2.
  20260929_1 ran it at 11(4) on 食. 11(1) on 旅行・観光 repeats neither the seat
  nor the theme.
- **Deletion test.** It applies to 11(1), and to nothing else. On every other
  row, deleting any sentence must leave no "assumption denied" beat. 12(B)'s
  `だけではない…こそ` foil is named, never attributed and then denied.

## The two RNG-picked named templates

- **Not-A-but-B family.** 問題12 closed on no named template in 20261002_1, so
  any family template was legal there. `A わけではない` is NOT a candidate,
  because 〜わけではない is this paper's 問題8 target (Item integrity #15).
  `secrets.randbelow(4)` over [ではなく, より…ほう, だけではない…こそ, というより]
  returned index 2, which is **`A だけではない。B こそが〜`**. A second
  `secrets.randbelow(2)` over the two 主張 closings {12(B), 13} returned
  **12(B)**. Name the foil A in the final and keep 「こそ」 to the final.
- **Cleft and 相関.** These were placed by rule, not by RNG.
  - 分裂文 cannot sit in 問題11 (bar), so it went to the 説明 closing outside
    問題11 that no previous seat holds: 10(1).
  - 相関 is kept out of 問題10 (three papers running before 20261002_1), so the
    paper's one went to the other 条件提示 row: 11(2).

## Tallies the authors must NOT break

- **Closing shape (13).** Values come from the CLOSED `CLOSING_MOVES` and
  nothing else.
  - 反論応答 2 (問題9, 11(4))
  - 説明 2 (10(1), 12(A))
  - 条件提示 2 (10(3), 11(2))
  - 随筆 2 (10(4), 11(3))
  - 主張 2 (12(B), 13)
  - 意外な観察 1 (11(1)), the only shape with a spare slot
  - 実用文・分類外 2 (10(2), 10(5))
  - No seat repeats the shape 20261002_1 put in that seat (all 13 checked
    against its `closing_moves`). Against 20260929_1 the only repeat is 10(2)
    実用文・分類外. That is by construction: the RNG above draws the second
    実用文 slot from the slots used two papers back.
- **Template (13 closings).**
  - Named: 分裂文 1 (10(1)), 相関 1 (11(2)), `A だけではない。B こそが〜` 1
    (12(B)). Every other final is unnamed.
  - `A わけではない` **0**. It is a keyed 問題8 form and must not appear in any
    読解 prose, final or not.
  - The three cap-1 templates are assigned to no row: 後知れ `〜ていた のだ`,
    不在の残り `〜ていない`, and 先回り. An unnamed final that lands on one of
    them spends its only slot, so don't let one land there.
- **not-A-but-B reframe family.** This covers ではなく, というより, よりも,
  だけではなく and わけではない, and ANY final that names a foil and prefers the
  alternative (「AにないBがある」 included). Exactly **1**, at 12(B).
- **MOVE (10 essay surfaces, 12 A+B as one).**
  - 〈想定→実は〉 1 (11(1))
  - 数えたことの報告 **3, at cap** (10(3), 11(2), 13)
  - 機構の説明 2 (10(1), 12)
  - 一人称の前後比較 2 (10(4), 11(3))
  - 反論への応答 2 (問題9, 11(4))
  - Headroom: 機構の説明 +1 (but not in 問題11 beyond 1), 一人称の前後比較 +1,
    反論への応答 +1. 数えたことの報告 has none. 〈想定→実は〉 has none on the
    読解 side, because the 聴解 half is unpredictable.
  - 20261002_1 ran 一人称 3 / 機構 3 / 反論 3 / 数えた 1 / 想定 0. This paper
    moves weight onto 数えたことの報告, which is why the persona bar above matters
    on three rows.
- **Persona** (cap 2 per archetype). Plan: 職業人 at most 2 (問題9 and 11(4) if
  both use it), 解説者 at most 2 (10(1) and 12(A)). The three counters (10(3)
  利用者, 11(2) 係, 13 住人) are three different archetypes.
- **Voice quota** (12 essay-type passages, 問題14 excluded).
  - At least 4 in the first person. Planned: 10(3), 10(4), 11(1), 11(3) and 13
    (5).
  - At least 3 in です・ます throughout. Planned: 11(4), 12(B) and 13, plus the
    two 実用文 (10(2), 10(5)). Write です・ます and the length band together.

## Tested forms that must stay out of the 読解 prose (Item integrity #15)

This paper keys the following (read the spec, not this copy, if anything
rerolls):

- **問題7:** 〜てならない, 〜やら〜やら, 〜とは, 〜ものだ・ものではない,
  〜(よ)うではないか, 〜(か)と思うと・(か)と思ったら, 〜にしたら・にすれば・
  にしてみれば, 敬語:ございます, 〜はともかく, 〜といった, 〜に即して,
  〜に違いない. 敬語 count 1 of 12, inside the cap of 2.
- **問題8:** 原因理由構文(〜ばかりに…てしまった), **〜わけではない**, **〜として**,
  **〜に応じて**, **〜に基づいて**.

Consequences:

- **敬語:ございます is keyed.** It is the reflex of the 10(2) email, the 10(5)
  notice and the 問題14 flyer (「〜でございます」「ございましたら」). Use none
  anywhere. Write 「です」, and 「ご不明な点があれば」 for the closing line.
- **〜わけではない** is both a keyed 問題8 frame AND a named final template. It
  appears in NO final and in no mid-passage sentence (including
  「〜わけではありません」). It is the reflex concession of 反論への応答 (問題9,
  11(4)) and of 12(B).
- **〜として, 〜に応じて, 〜に基づいて, 〜ばかりに are general-purpose frames, so
  a prose grep is owed** (`exam-blueprint` §"A `grammar_p8` draw whose form is a
  general-purpose sentence pattern").
  - 「〜として」 is everywhere in 説明 and 機構の説明 prose (10(1), 12(A)).
  - 「〜に応じて」 shows up in notices and flyers (料金は〜に応じて) and in
    条件提示.
  - 「〜に基づいて／に基づき」 shows up in 数えたことの報告 (記録に基づいて) and in
    notices.
  - 「〜ばかりに」 shows up in first-person regret.
  - Grep every surface. Re-word every hit but at most one, and that one must not
    be in the tested frame. Prefer 0.
- **〜といった, 〜ものだ, 〜とは, 〜にしたら／にすれば are also general.**
  - 「AやBといったC」 is the stock enumerator of 説明 prose.
  - 「〜ものだ」 is the stock ending of 随筆 (10(4), 11(3)).
  - 「〜とは」 is a definitional or surprise topic marker.
  - 「〈人〉にしたら／にすれば」 is the stock perspective frame of 反論への応答.
  - None anywhere, and treat each as owing the same grep.
- **〜(よ)うではないか, 〜に違いない, 〜てならない, 〜はともかく, 〜に即して,
  〜やら〜やら, 〜(か)と思うと／と思ったら:** none anywhere.
  - 「〜ようではないか」 is the reflex exhortation of a 主張 final (12(B), 13).
  - 「〜に違いない」 is the reflex inference of 意外な観察 (11(1)).
  - 「〜と思ったら」 leaks into first-person anecdotes (10(4), 11(1), 11(3)).
- **Stage 3 re-grep.** Every form above goes into the Stage-3 keyed-form re-grep
  with its counts and frames (文末／連用／連体). That includes any 問題9
  [論理接続] key once the 文法 author has written the cloze.

## The two things that get checked by hand

1. **The unnamed finals must not share a skeleton with each other, with the
   named ones, or with 20261002_1's skeleton in the same 大問 (table above).**
   The pairs at risk:
   - 10(4) vs 11(3) (both 随筆, both 一人称の前後比較);
   - 問題9 vs 11(4) (both 反論応答, both 反論への応答);
   - 10(3) (non-相関) vs 11(2) (相関), so two DIFFERENT condition skeletons;
   - 12(B) vs 13 (both 主張; only 12(B) carries the foil);
   - 10(1) (cleft) vs 12(A) (説明, not cleft);
   - 12(A) vs 12(B). Read A against B FIRST.
2. **Apply the deletion test to 11(1), and to nothing else.** Every other row
   carries no attributed assumption and no denial.
   - **10(4) and 11(3) (一人称の前後比較):** the "before" is a PRACTICE the
     narrator actually did. 「つもりだった」 or 「と思っていた。ところが」 is the
     re-skin.
   - **10(3), 11(2) and 13 (数えたことの報告):** the count is not introduced as
     contradicting an expectation, and it is not an N年分 record count.
   - **問題9 and 11(4) (反論への応答):** the objection is taken seriously and
     answered on its own terms. Vary the set-up: 問題9 is a resident's or
     reader's objection to a procedure; 11(4) is a customer's or colleague's.
     Neither opens 「もっとも」 and then knocks the objection down.
   - **10(1) and 12 (機構の説明):** no 「〜と思われがちだが」 opening.
