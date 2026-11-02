# 読解 allocation table — 20261102_2 (BLUEPRINT-ASSIGNED, binding)

Stage 1 filled this table in **before any prose exists**, as
`question-authoring/references/dokkai.md` requires in §"Thirteen surfaces",
§"The named templates" and §"The rhetorical-MOVE allocation table".

- Authors do NOT re-choose the theme, shape, template, MOVE, resolution or
  persona columns.
- Each author fills the two **AUTHOR FILLS** columns from the prose they write
  and hands the table back. Edit your own rows only.

**Denominators** (dokkai.md §"The denominator"):

- **Axis 1, theme.** 13 rows. 問題12 A+B is ONE row.
- **Axis 2, closing shape and final-sentence template.** 13 closings. 問題12 A
  and B are SEPARATE rows. 問題14 is outside this axis.
- **MOVE cap.** Essay surfaces only, 問題12 A+B as ONE: **10**, because
  問題10(1) and 問題10(2) are 実用文.

**Themes** come from `tests/20261102_2/test_spec.json` `items.reading_topics[i]`.

- **Index → surface.** 0→問題10(1) … 4→問題10(5), 5→問題11(1) … 8→問題11(4),
  9→問題12, 10→問題13, 11→問題14.
- **Draw.** `make sample 20261102_2 SEED=60783915`, plus one
  `reading_topics:9` reroll (rule 4, 地域活性化 → 人間関係, seed 72058050),
  recorded in `qa/blueprint-rerolls-20261102_2.md`.
- **What to avoid.** Author each surface's SUBJECT from its entry's `theme`,
  and keep it off: that entry's full `avoid` list in the spec; any re-wording
  of an avoid string; every previous-paper CLAIM below (exam-blueprint Part
  II, "claims, not only subjects"); and the previous paper's same-seat last
  two sentences (RC-3, table below).

## Who owns which rows

- **問題9, the cloze, belongs to the 文法 (問7–9) author.**
  `scaffold_sections.py` emits it inside `問7-9_文法.md`.
- **問題10–14 belong to the 読解 author.**
- Both authors get this whole table: the caps count across all thirteen
  closings.

## The allocation

| surface | owner | theme | closing shape (≤2 each) | final-sentence template | MOVE (resolution) | voice / persona (plan) | AUTHOR FILLS: final sentence (+ penultimate) | AUTHOR FILLS: which previous claim (20261102_1's) this is NOT, and why |
|---|---|---|---|---|---|---|---|---|
| 問題9 cloze | **文法** | **防災** (author-composed; RNG, below) | 随筆 | Unnamed. **NOT 相関 — gated bar** (20261102_1 問題9). Not 〈記録を並べてみると、…日では、…が、目に見えて多かった〉, nor its penultimate 〈…日の記録を見ると、…のは、どれも…だった〉. Must differ in skeleton from 11(3), the other 随筆 | **一人称の前後比較**. Resolution: ONE household preparedness PRACTICE the narrator changed (how they store, check or carry something for an emergency), and what that changed in their ordinary week. The "before" is a practice, never a belief | 一人称随筆; **生活者**. Not a role-holder (係・町内会) and no counting of other households | Subject: 風呂の残り湯を翌日の夕方まで残す (title 「残り湯」). Penultimate: 〈帰りの早い夫が湯船を洗う日が週に三日ほどでき、私は寝る前に風呂場でしゃがみこむことがなくなった。〉 Final: 〈非常の時のために始めた小さな備えが、家の中の仕事の受け持ちまで、いつのまにか動かすこともある。〉 Template: unnamed (〜こともある; no のは/ではなく/だけ/こそ/ほど/では＋数量, not 〜ていない/〜ていたのだ). Before = drain the bath at once and wash the tub at night; after = keep the water until just before the next evening's fill; week change = tub-washing moved to whoever is home first. No denied belief anywhere (deletion test: nothing to delete). Keys: 48 なにしろ, 49 どうしようもなく, 50 抜くことにした, 51 先に家に着いた者 — Stage-3 re-grep: なにしろ sentence-initial in 読解 prose | NOT 20261102_1 問題9 (task order/fatigue, a count of days, 「目に見えて多かった」): nothing is counted or ordered, and the result is a shift in who does a chore. NOT 11(2) helmets (same theme): a household water-storage habit, not equipment or a mechanism. NOT 11(4) "move an object to force a behaviour": no object moves, only the drain time. NOT 10(5) "change the medium of a check" |
| 問題10(1) | 読解 | 環境 | **実用文・分類外** (business email; RNG, below) | — | （実用文） | メール, です・ます; 実務者 | Subject: 雑貨店から仕入れ先への、詰め物を空気入りの小袋から丸めた紙に替えられるかの問い合わせ. Penultimate: 〈紙なら古紙として出せるので、助かります。〉 Final: 〈替えていただける場合、代金やお届けの日が変わるかどうかも、お知らせください。〉 No いらっしゃ／踏まえて | NOT 20261102_1 10(4) "pasted photos degrade → send originals separately" nor 10(3) "changed mailing → open early": the request is to change the supplier's packing material for unbreakable goods. Closing pair is reason + "also tell me whether price/date change" — neither "work proceeds on what we have / sample in N days" nor "unchanged items stay as before" |
| 問題10(2) | 読解 | 子育て・家族 | **実用文・分類外** (notice / お知らせ; RNG, below) | — | （実用文） | 通知, です・ます; 施設・団体（通知） | Subject: 保育園からの、使ったおむつを6月から園で捨てる（持ち帰り不要）というお知らせ. Penultimate: 〈なお、新しいおむつは、毎朝ご家庭からお持ちいただくようお願いします。〉 Final: 〈一枚ずつに、お子さんの名前をお書きください。〉 No に伴い／をはじめ／いらっしゃ | NOT 20261102_1 10(3) "mailing changes colour → open early" nor 14 "おさがり交換会": a nursery stops a daily take-home chore. No 児童館 slot, no exchange event, no envelope. Closing pair is two plain instructions (bring new nappies; label each), not "unchanged items stay as before" — 「これまでどおり」 deliberately absent |
| 問題10(3) | 読解 | スポーツ・余暇 | 説明 | Unnamed. Not a cleft (plan 0). Not 〈Xでは、…を、いちばん用心するそうだ〉 (20261102_1 10(1)), not 〈ただ、…ため、…は一人一人に合わせて調整しています〉 (10(2)). Must differ in skeleton from 12(A), the other 説明 | **機構の説明**. Resolution: how ONE piece of leisure/sports equipment or ONE technique does its job, or how two such things differ, and it stops there. Nothing is denied anywhere | 解説, **です・ます**; **職業人** (an instructor or coach). No physics of ice, slipping, friction or light (20261102_1 10(1)); no climbing (問題9) | Subject: 自転車教室の指導者が説明する、後ろの歯車の大小とペダルの重さ（変速機）. Penultimate: 〈小さい歯車では、一こぎで遠くまで進みますが、ペダルは重くなります。〉 Final: 〈上り坂で大きい歯車に切り替えると、ペダルをこぐ回数は増えますが、一回ごとに足にかかる力は小さくてすみます。〉 Template: unnamed trade-off 「〜と、Aは増えますが、Bは小さくてすみます」 (no のは, no では/ほど＋数量). Nothing denied; deletion test empty | NOT 20261102_1 10(1) "a hidden surface layer, not the obvious cause, explains X": a gear-ratio trade-off, no surface property, no friction/ice/light. NOT 10(2) "slowing gives a slow body part time": no body-timing claim. No hearsay 〜そうだ tail, no 「ただ、…調整しています」 tail. Skeleton differs from 12(A) (〜のが早い advice) |
| 問題10(4) | 読解 | 働き方 | 条件提示 | **`A では/ほど B が多い（相関）`**, the paper's only 相関. Do NOT write the correlation with 「〜に伴って／に伴い」 or 「一方」 (keyed 問題8 forms). Not 〈声に出すようになってから、…Nの多くは…になった〉 (20261102_1 10(5)) | **数えたことの報告**. Resolution: the narrator counts ONE bounded span (a week or a month) of something in their OWN workplace, and reports which condition went with more (or less) of an outcome. The count is not introduced as contradicting an expectation | 一人称随筆; **観察者**. NOT 「〈役〉が〈N年分〉を数える」. NOT "do the hardest task first while fresh" (20261102_1 問題9's claim) | Subject: 設計事務所の電話受付が一か月数えた「少々お待ちください」の回数とホワイトボードの帰社時刻. Penultimate: 〈先月、電話の相手に「少々お待ちください」と言った回数を、日ごとに付けてみた。〉 Final: 〈一か月分の記録を見ると、出かけた所員が戻る時刻まで書いていった日ほど、電話の相手を待たせた回数が少なかった。〉 = 相関 (evidential frame + 〜た日ほど + 回数が少なかった); no に伴って／一方. Count not framed against an expectation | NOT 20261102_1 問題9 "hard task first while fresh / fatigue": the condition is a return time written on a shared board, nothing about task order. NOT 10(5) "since I began V-ing most of my N became N'". One month, own workplace, receptionist as observer (not 〈役〉が〈N年分〉). Differs from 11(1) in what was counted (waits on the phone vs torn dumplings) and what it showed (a quantity correlation vs a categorical zero) |
| 問題10(5) | 読解 | 旅行・観光 | 反論応答 | Unnamed. No not-A-but-B family member in the last two sentences. Not 〈声に出すようになってから、私が…Nの多くは、…Nになった〉 (20261102_1 10(5)) | **反論への応答**. Resolution: **「理由を示して変えない」**. A named objection to the narrator's way of travelling or hosting is taken seriously, and the narrator keeps the way, giving the reason. No exception channel, no reservation route, no "keep the rule, open one door" (20261008_1 問題9) | 一人称随筆; **旅行者** (not a host or guide: 職業人 is spent by 10(3) and 11(2)) | Subject: 旅は行きも帰りも各駅停車で行く筆者と、着いてからの時間が減るという友人の声. Penultimate: 〈そのたびに顔を上げて外を眺めているうちに、仕事のことが頭から抜けていく。〉 Final: 〈次の旅の切符も、もう各駅停車で買ってある。〉 Objection granted (「たしかにそのとおりで」), way kept with a reason; no exception route, no とはいえ／つつも／としたら, no not-A-but-B in the last two | NOT 20261102_1 11(1) "true on its yardstick, but the wrong yardstick" (反論の前提を問い直す): the narrator accepts less time at the destination as a real cost and keeps the practice for an independent reason (the slow train empties work from their head). NOT 10(5)'s "since I began V-ing, most of my N became N'" beat. No ferry/tide, hot spring, ski or map-less travel |
| 問題11(1) | 読解 | 食 | 条件提示 | Unnamed, **NOT 相関 — gated bar** (20261008_1 11(2) closed 11 on it two back; this paper's 相関 is 10(4)). **No 〜れば condition**: 20261102_1 11(3) closed 問題11 on 〈…が自分の口で言ってくれれば、…ことは、まず要らなくなる〉. Use a different condition skeleton (e.g. 〈〜た日には／ときは、…一度も…なかった〉), no quantity up/down | **数えたことの報告**. Resolution: a short count (days or weeks) of the narrator's OWN cooking or eating, and the condition it showed. It must differ from 10(4) in what was counted AND in what the count showed | 一人称随筆; **趣味の実践者**. No kitchen-tool or knife mechanism (20261102_1 問題13), no bread or resting (20261008_1 11(4)) | Subject: 休日にギョーザを包む筆者が八回分付けた、焼くと皮が破れた数とキャベツの水気. Penultimate: 〈残りの四回は、刻んだキャベツに塩をもみこみ、出てきた水を手で固くしぼってから混ぜた回だった。〉 Final: 〈キャベツの水気をしぼってから混ぜた日には、焼いている間に破れたギョーザは、一つも出なかった。〉 = 〈〜た日には、…一つも…なかった〉: categorical zero, no では/ほど＋数量, no 〜れば. Count opened as 「見当がつかなかった」, never against an expectation | NOT 20261102_1 13 "a sharper tool damages less": the condition is the filling's water, not a tool's state; no knife, no salting-and-waiting (no resting). NOT 問題9 "hard part first": nothing about order or fatigue. NOT 11(3)'s 「それからは…確認している」 + 〜れば closing |
| 問題11(2) | 読解 | 教育 | 反論応答 | Unnamed. Not 〈けれども、それは、…とは別の物差しです〉 nor its penultimate 〈…として比べられれば、…にかないません〉 (20261102_1 11(1)). Not a family member, not a cleft | **反論への応答**. Resolution: **「譲歩して一部を変える」**. A named objection to a teaching practice is taken seriously and the narrator changes ONE part of it. The change must NOT be "do the preparation earlier so nobody is kept waiting" (20261102_1 12(B)) and NOT a new exception channel | 一人称随筆, **です・ます**; **職業人** (a teacher or tutor) | Subject: 日記の誤字を赤で直さない小学校の担任と、間違いを覚えてしまうという保護者の心配. Penultimate: 〈同じ字を三回続けて書き誤っていたときには、その字のわきに、鉛筆で小さな丸を一つつけておきます。〉 Final: 〈丸のついた字は、本人が辞書で確かめて、次の日記の終わりに正しく書き直してきます。〉 Concession 「もっともなご心配です」 + checked against a term of diaries; keeps "no red-pen correction", changes ONE part (repeated errors get a pencil mark). 〜ことにした removed (問題9-50 key form) | NOT 20261102_1 11(1) "right on its own yardstick but the wrong yardstick": the parent's point is accepted on its own terms and acted on. NOT 12(B) "change when + prepare earlier": what changes is WHICH errors are marked, not timing; no new exception channel. No absence/homework check, no returning-speed or one-line-feedback claim |
| 問題11(3) | 読解 | デジタル化 | 随筆 | Unnamed. Not 〈返す日を、…が自分の口で言ってくれれば、…まず要らなくなる〉 (20261102_1 11(3)). Must differ in skeleton from 問題9, the other 随筆. Not 後知れ 〜ていたのだ, not 不在の残り 〜ていない (cap-1, unassigned) | **一人称の前後比較**. Resolution: ONE practice with a digital tool the narrator changed, and what it changed in the practice itself. The "before" is a practice, never a belief. Must differ from 問題9 in kind | 一人称随筆; **学生**. No read-aloud/proofreading (20261102_1 10(5)), no phone dictionary or hand-copying (20261008_1 10(3)), no photo files | Subject: 大学の録画授業を一・五倍で止めては戻して見ていた学生が、元の速さで止めずに見るようにした. Penultimate: 〈今は、見終わってから、残った印の所だけを戻って見直している。〉 Final: 〈止めて戻す回数が減った分、九十分の録画は、百分ほどで見終わるようになった。〉 Template unnamed (〜分、…ようになった; no 〜ていない/〜ていたのだ, no 「Aより」 foil). Before = a practice (1.5x + pause/rewind, 「二時間近くかかることもあった」); the "1.5x saves time" arithmetic was cut so no expectation is set up to be contradicted | NOT 20261102_1 10(5) "changing the medium of a check changes what you catch": same medium, the change is playback speed and deferring rewinds. NOT 11(3) "say the date and it's kept". Differs from 問題9 (残り湯: a household preparedness habit whose effect is a chore shift; closes on a generalising 〜こともある) in kind and skeleton |
| 問題11(4) | 読解 | 睡眠・健康 | 意外な観察 | Unnamed. Not a cleft: this shape's natural final 「〜のは、…からだ」 IS the 分裂文 (plan 0). Not 〈…間に、私の頭は、たいていもう半分は起きている〉 nor 〈寝る時刻は、前とほとんど同じである〉 (20261102_1 11(4)) | **機構の説明**. Resolution: a FACT about sleep or rest that does not match another fact (「〜のに」), then its cause. The mismatch is between facts. It is never an attributed belief: no 「〜と思われがちだが」, no 実は (that is 〈想定→実は〉) | 解説; **解説者**. No alarm, waking-by-walking or room layout (20261102_1 11(4)) | Subject: 寝る時刻を遅らせるのは楽なのに早めるのは難しい理由（一回りが二十四時間より少し長い体内時計）. Penultimate: 〈日曜の夜は、時計の上では、まだ宵の口にあたる。〉 Final: 〈体の時計は、遅らせる向きには一晩でも合わせられるが、早める向きには少しずつしか合わせられない。〉 Not a cleft; mismatch stated as two facts with 「それなのに」「〜のに」; no 思われがち, no 実は, no ところが | NOT 20261102_1 11(4) "moving the alarm so you must walk wakes you": no object moved, no waking routine. NOT 10(2) "slowing something gives a slow body part time to act": the claim is a direction asymmetry of a >24h clock. No light/temperature thresholds, no advice (so not the 「起きる時こくをそろえる」 avoid subject) |
| 問題12(A) | 読解 | **人間関係** | 説明 | Unnamed. **NOT `A わけではない` — gated bar** (20261102_1 12(A)). Not 〈…客は…座っていればよいし、運転手も…ばよい〉 (its penultimate). Read against 12(B) FIRST | **機構の説明** (A+B = one surface). 12(A) explains how one everyday relational misunderstanding or habit comes about, and gives the advice that follows from that | 評論; **論者** | Subject: 旅行のお土産を配る習慣（もらった人が返すことで続く）. Penultimate: 〈誰もが同じように感じていても、自分からやめようとは言い出しにくい。〉 Final: 〈負担に思う人の多い集まりなら、一度皆で話し合い、お土産はなしにしようと決めてしまうのが早い。〉 No わけではない, no 〜ばよい pair, no cleft (〜のが早い), no money/price claim | NOT 20261102_1 12(A) "the obvious culprit is not the only cause; the user's own movement is": A gives one mechanism (reciprocity) and a group-decision advice, no foil. NOT 11(3) "name the date yourself and it is kept": no commitment-naming. No lending/returning, listening or consultation |
| 問題12(B) | 読解 | ″ | 意外な観察 | Unnamed. No 「わけではない／わけではありません」 anywhere in the last two sentences. Not 〈…が止まったら、すぐに…へ向かいます〉 / 〈…を手に持ち、…ておきます〉 (20261102_1 12(B)). Not a cleft | ″ Resolution: B starts from the SAME observation as A, presents a fact that does not fit A's account, gives a different cause, and therefore different advice. B does not attribute a belief to A and deny it with 実は | 一人称, **です・ます**; **生活者** | Subject: 手芸の会でお菓子を配るのは入って一年もたたない人たち（話しかけるきっかけ）. Penultimate: 〈それからは、新しい人が入ってきたら、私のほうから、作っている物のことを尋ねるようにしています。〉 Final: 〈話す相手が何人かできた人は、お菓子の箱を持たずに来て、自分から隣の席の人に声をかけています。〉 (re-angled off 「…ずっと少なくなりました」 so it does not rhyme with 10(4)'s 相関 decrease). Same observation as A; non-fitting fact (newcomers who have received nothing give most); different cause (a pretext to talk) and advice (talk to newcomers first). No わけではない, no 実は, no cleft, no というより | NOT 20261102_1 12(B) "change when + compensate by preparing earlier": one action + its result, not two sequenced actions (〜ておきます / 〜たら、すぐに…ます). NOT 11(3) "name the date and it's kept". Read against 12(A): A ends on a group decision 〜のが早い, B on an observed present behaviour 〜ています — different skeletons |
| 問題13 | 読解 | **メディア・情報** | 主張 | **`A だけではない。B こそが〜`** (RNG, below), the paper's ONLY not-A-but-B family member. Name the foil A in the final pair. Not 〈今は、…の上に、…がほとんど残らなくなっている〉 / 〈言われてみると、…いつも…ぬれていた〉 (20261102_1 13) | **〈想定→実は〉**, the paper's ONLY one on the 読解 side (below). Resolution: a widely held view about how people get, read or pass on information is stated and attributed, denied, and Y replaces it; the essay then argues FOR Y | 一人称評論; **利用者** (a reader/viewer/listener writing in the first person). Not 研究者 (20261102_1 10(1) ran 想定 with 研究者) | Subject: 「長い記事は最後まで読まれない」という書き手の通説と、冒頭で話の道筋を示す記事. Penultimate: 〈読み手が途中で画面を閉じる理由は、記事の長さだけではない。〉 Final: 〈話の道筋を初めに示しておくことこそが、長い記事を最後まで読んでもらうための、何よりの工夫である。〉 Foil A = 記事の長さ, named in the penultimate. 想定 attributed to the 知人／書き手の間, denied 「ところが…短い物ばかりではなかった」, 「実は」 Y = an up-front route; then argued for. 疑問提示文 「…届くのだろうか」 | NOT 20261102_1 12(A) family "the audience's own act, not the provider, is the cause": Y is a provider-side structure (the writer shows the route first). NOT 13 "a sharper tool → the side-effect disappears". No notification-off, star ratings, AI summaries, newspaper storage, announcer, anime or celebrity |
| 問題14 | 読解 | **住まい** | (outside axis 2: flyer, no closing) | — | （実用文） | 案内; 施設・団体（案内） | Subject: はなの台市シルバー人材センターの網戸・障子の張り替え受付（1枚料金表、模様入り300円増し、引き取り500円・5枚以上無料、受取時払い、9/1〜9/30、窓口は平日のみ）. No closing. 70 = value (9,100円; 8,500/8,600/9,600 each one fact changed, ascending); 71 = action (9月中に電話で引き取り、届いたときに払う). Longest shared run vs previous 2 papers, imports and archive: 12 chars (gate threshold 20) | NOT 20261102_1 14 (おさがり交換会: coupons per item, overflow 50円, large items by phone) — a paid home-repair order with a size table, a surcharge and a pickup-fee waiver. Not a recent 問題14 type (barber, extinguisher, scholarship, child seat). No frozen pipes, plant care or housework hobby |

## Previous paper (20261102_1), per 大問 — what is barred here

Read from the shipped `tests/20261102_1/言語知識・読解.md` with the gate's own
`dokkai_closing_scopes()`, `passage_final_sentences()` and
`FINAL_SENTENCE_TEMPLATES` (script:
`/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/4c04ee6c-0667-4210-8165-898b3b795c1d/scratchpad/s1_prev.py`).
MOVEs are from `logs/topics.json` notes and the 20261102_1 allocation.

| 大問 | named templates | MOVEs |
|---|---|---|
| 問題9 | **`A では/ほど B が多い（相関）`** | 数えたことの報告 |
| 問題10 | none | 〈想定→実は〉 (10(1)), 機構の説明 (10(2)), 一人称の前後比較 (10(5)); 10(3)/10(4) 実用文 |
| 問題11 | none | 反論への応答 (11(1)), 機構の説明 (11(2)), 数えたことの報告 (11(3)), 一人称の前後比較 (11(4)) |
| 問題12 | **`A わけではない`** (12(A)) | 反論への応答 |
| 問題13 | none | 一人称の前後比較 |

- **Template bar** (gated, `check_dokkai_template_repeat_prev_paper`):
  **問題9 no 相関; 問題12 no `A わけではない`.** 問題10, 11 and 13 are not
  barred by a named template.
- **MOVE bar.** 20261102_1 used no MOVE twice in one 大問, so the per-大問 bar
  is vacuous. Stage 1 added two seat rules on top (precedent:
  `qa/dokkai-allocation-20261102_1.md`):
  - **No seat carries the shape or the MOVE 20261102_1 put in that seat.** All
    13 shapes and all 10 MOVEs were checked.
  - **No seat repeats 20261008_1's (seat, theme, MOVE) triple.** Nearest:
    11(3) 一人称 (there 人間関係, here デジタル化); 12 機構 (there 環境, here
    人間関係).
  - **No theme repeats 20261102_1's (theme, MOVE) pair anywhere.** 食 was
    一人称 there (13) and is 数えた here; 防災 was 機構 (11(2)) and is 一人称
    here; 睡眠・健康 was 一人称 (11(4)) and is 機構 here; 人間関係 was 数えた
    (11(3)) and is 機構 here; スポーツ・余暇 was 数えた (問題9) and is 機構 here;
    働き方 was 一人称 (10(5)) and is 数えた here.
- **Persona bar.** 「〈役〉が〈N年分〉を数える」 last ran in 20260929_1, four
  papers back, so it is free. **This paper keeps it OFF anyway:** the two
  数えた rows (10(4), 11(1)) each count one bounded span of the narrator's own
  work or cooking.

### RC-3 — the previous paper's same-seat LAST TWO sentences

dokkai.md §"A re-angle that answers a cross-paper CLAIM finding bars a
skeleton, not only a final". Read your new last two sentences against these.
The NOT-list bars the closing SKELETON (the beat), not only the final's
template. If a stage-3 or QA repair later re-angles a row, this column is the
one it reads.

| seat | 20261102_1 penultimate | 20261102_1 final |
|---|---|---|
| 問題9 | 易しいコースから始めた日の記録を見ると、一度目で登り切れなかったのは、どれも（51）挑んだコースだった。 | 記録を並べてみると、一番難しいコースから始めた日では、一度目で上まで登り切れたコースが、目に見えて多かった。 |
| 問題10(1) | 実は、氷の表面には、何にも押されていなくても固まりきらない薄い層が最初からあり、温度が下がるにつれて薄くなっていく。 | 雪国では、気温が零度近くまで上がった朝の道を、いちばん用心するそうだ。 |
| 問題10(2) | とろみのある飲み物はゆっくり下りるので、ふたが閉まるまでの時間が生まれるのです。 | ただ、濃すぎるとのどに残るため、濃さは一人一人に合わせて調整しています。 |
| 問題10(3) | この封筒が届いたら、早めに開けて、中の書類で期限を確かめてください。 | お知らせだけの書類は、これまでどおり白封筒でお届けします。 |
| 問題10(4) | 文書のほうは、いただいたもので作業を進めております。 | 写真が届きましたら、三日ほどで見本をお送りします。 |
| 問題10(5) | 字の誤りは、前と同じように見つかる。 | 声に出すようになってから、私が原稿に引く赤線の多くは、一息で読みきれない文を区切る線になった。 |
| 問題11(1) | 明かりとして比べられれば、和ろうそくは洋ろうそくにかないません。 | けれども、それは、和ろうそくが長く求められてきた役目とは別の物差し（注5）です。 |
| 問題11(2) | また、内側の板は、一度つぶれると元の厚さには戻らない。 | 外見に傷がなくても、大きな物を一度受け止めたヘルメットは、次に同じ力を受けたとき、同じようには頭を守れない。 |
| 問題11(3) | それからは、物を渡すとき、「いつごろになりそう？」と一言確認している。 | 返す日を、借りる人が自分の口で言ってくれれば、こちらから催促することは、まず要らなくなる。 |
| 問題11(4) | 寝る時刻は、前とほとんど同じである。 | 目覚ましを止めに部屋を横切って歩く間に、私の頭は、たいていもう半分は起きている。 |
| 問題12(A) | 客はバスが止まりきるまで座っていればよいし、運転手も、客が席に着いたのを確かめてから走り出せばよい。 | 車内のけがは、運転の荒さだけで起きるわけではない。 |
| 問題12(B) | カードを手に持ち、一つ前の停留所を出たら降車ボタンを押しておきます。 | バスが止まったら、すぐに立って降車口へ向かいます。 |
| 問題13 | 言われてみると、研ぐ前の包丁で玉ねぎを刻んだあとは、まな板の上がいつも汁でぬれていた。 | 今は、刻み終えたまな板の上に、玉ねぎの汁がほとんど残らなくなっている。 |

The closing BEATS these carry, which the same seat here may not reuse:

- 問題9: a record re-read → a condition that "visibly" went with more.
- 10(1)/10(2): hearsay 「〜そうだ」 tail; 「ただ、…ため、…調整しています」
  caveat-and-adjust tail. (10(1)/10(2) are 実用文 here, so the bar is on any 問題10
  essay that borrows them, i.e. 10(3)–10(5).)
- 10(3)/10(4) notice/email: "if X arrives, open early" + "unchanged items stay
  as before"; "work proceeds on what we have" + "on receipt, we send a sample in
  N days". This paper's 10(1) email and 10(2) notice must not close on either
  pair.
- 10(5): "the same errors are still found" + "since I began V-ing, most of my
  N became N'".
- 11(1): concession "measured as X, it loses" + "but that is a different
  yardstick".
- 11(2): "once crushed, it does not recover" + "even unmarked, it no longer
  protects".
- 11(3): 「それからは…確認している」 routine + 〜れば condition.
- 11(4): "the bedtime is the same as before" + "by the time I walk there I am
  half awake".
- 12(A): two parallel 〜ばよい prescriptions + わけではない.
- 12(B): two concrete です・ます actions in sequence (〜ておきます / 〜たら、すぐに…ます).
- 13: 「言われてみると、…いつも…ていた」 retrospective + 「今は、…なくなっている」.

## The previous paper's 13 claims — what each surface must NOT restate

From `logs/topics.json`, row 20261102_1, `claim`. 問題12 A and B are listed
separately (14 lines). In the last column of your row, write which of these
your surface is NOT, and why. "Not" means a different assertion, not only a
different subject.

| key | 20261102_1 claim | theme there | nearest rows here |
|---|---|---|---|
| 問題9 | 指の力は登るうちに弱るので、一番難しいコースから始めた日のほうが、一度目で登り切れるコースが目に見えて多かった。 | スポーツ・余暇 | 10(4), 11(1), 10(3) |
| 問題10(1) | 氷がすべるのは体重でとけた水のためではなく、表面にもとからある固まりきらない薄い層のためで、その層は寒いほど薄くなる。 | 科学・技術 | 10(3), 11(4), 13 |
| 問題10(2) | とろみのある飲み物はゆっくり下りるので、動きの遅くなった気管のふたが閉まるまで待てるが、濃さは一人一人に合わせる。 | 医療・福祉 | 11(4), 10(3) |
| 問題10(3) | 期限のある書類は4月から封筒の色を変えて送るので、届いたら早めに開けて期限を確かめてほしい。 | 行政・手続き | 10(2) notice, 14 |
| 問題10(4) | 文書に貼った写真は縮められて印刷がぼやけるので、元のファイルのまま別に送ってほしい。 | デジタル化 | 10(1) email, 11(3) |
| 問題10(5) | 原稿を声に出して読むと詰め込みすぎた文に気づくので、直す中身が字の誤りから文の区切りに変わった。 | 働き方 | 11(3), 問題9, 10(4) |
| 問題11(1) | 和ろうそくが部屋の明かりとして暗いのは確かだが、「暗い」は部屋を照らす道具として比べたときの物差しで、仏壇や寺で使う人に問われるのは炎の静かさや汚さないことである。 | 文化・伝統 | 10(5), 11(2) |
| 問題11(2) | ヘルメットは殻・帯のすきま・内側の板の三つで頭への力を和らげるが、正しく着けないと働かず、一度大きな力を受けたものは同じようには守れない。 | 防災 | 問題9, 10(3) |
| 問題11(3) | 返す日を借りる人が自分の口で言えば、貸した物は催促しなくても返ってくる。 | 人間関係 | 12, 10(4), 11(1) |
| 問題11(4) | 目覚ましを止めに部屋を横切って歩くようにすると、寝る時刻は同じでも、歩く間に頭が起き始める。 | 睡眠・健康 | 11(4), 問題9, 11(3) |
| 問題12(A) | バスの車内のけがは運転の荒さだけでなく、止まる瞬間の揺れの中を客が歩くことで起きるので、客は止まるまで座っていればよい。 | 交通 | 12(A), 13, 10(5) |
| 問題12(B) | 止まる瞬間の揺れが危ないと知って立つのは止まってからにしたが、ほかの人を待たせないよう座ったまま支度を済ませている。 | 交通 | 11(2), 12(B) |
| 問題13 | 包丁をよく研いでおくと、刃が玉ねぎの細胞をつぶさずに切るので、目にしみる成分が出にくく涙が出なくなる。 | 食 | 11(1), 10(3), 11(4) |
| 問題14 | 持ち寄った子ども用品の数に応じて引換券を渡し、引換券の枚数をこえる持ち帰りは1点50円、大きい物は前もって電話で申し込む交換会を知らせる。 | 子育て・家族 | 10(2) notice, 14 |

Claim families that are off-limits, read across the column:

- **"doing the hard part first, while still fresh, gets more done"** (問題9).
  10(4) and 11(1) may not report that order-of-tasks or fatigue set the result.
- **"a surface layer / hidden physical property, not the obvious cause,
  explains X"** (10(1)). 10(3), 11(4) and 13 explain no slipping, melting,
  friction or surface layer.
- **"slowing something down gives a slow body part time to act"** (10(2)).
  11(4) and 10(3) must not make a body-timing claim of that shape.
- **"changed format of a mailing → please open/check early"** (10(3)), **"the
  pasted/compressed file is degraded → send the original separately"**
  (10(4)). 10(1) email and 10(2) notice may not make either request.
- **"reading aloud / changing the medium of a check changes what you catch"**
  (10(5)). 11(3) and 問題9 may not move a check to another medium.
- **"the objection is true on its own yardstick, but that is the wrong
  yardstick"** (11(1)). 10(5) and 11(2) are 「理由を示して変えない」 and
  「譲歩して一部を変える」, never 「反論の前提を問い直す」.
- **"safety equipment works by layered parts and fails once used"** (11(2)).
  問題9 is a household practice, not an equipment mechanism.
- **"say the date out loud and the other person keeps it"** (11(3)). 12 may not
  argue that naming a date/commitment yourself makes people keep it.
- **"moving the alarm so you must walk wakes you"** (11(4)). 11(4) and 問題9
  move no object to force a behaviour.
- **"the obvious culprit (rough driving) is not the only cause; the user's own
  movement at the critical moment is"** (12(A)). 13's 主張 must not be "the
  audience's own act, not the provider, is the cause".
- **"change one part (when) and compensate the cost to others by preparing
  earlier"** (12(B)). 11(2)'s 譲歩 must change a different kind of thing.
- **"a sharper tool damages less, so the bad side-effect disappears"** (13).
  11(1) may not attribute its condition to a tool's sharpness or state.

### Domains of the previous papers' 科学・技術 / 消費・経済 surfaces

This paper has no 科学・技術 and no 消費・経済 surface (neither was drawn).
The domains still bar the mechanism rows (10(3), 11(4), 12) from drifting in:

| paper | surface | theme | DOMAIN |
|---|---|---|---|
| 20261102_1 | 問題10(1) | 科学・技術 | ice physics: why ice is slippery (a pre-existing unfrozen surface layer, not pressure melting) |
| 20261102_1 | 聴解問題5-2番 (composed) | 科学・技術 | choosing summer science events (weather-forecast workshop; history of star observation) |
| 20261102_1 | 聴解問題1-5番 (composed) | 消費・経済 | phone-shop repair: no part, return the loaner |
| 20261102_1 | — | 消費・経済 (読解) | no 読解 surface |
| 20261008_1 (two back) | 問題10(1) | 科学・技術 | atmospheric optics: why the evening sky is red |
| 20261008_1 (two back) | 聴解問題5-2番 (composed) | 消費・経済 | choosing between bicycles at a shopping centre |

- 10(3) スポーツ・余暇: no ice, skating, ski wax, friction, light or optics.
- 11(4) 睡眠・健康: no physics of light or temperature thresholds; no
  "forecast below N degrees, act the night before" (20261008_1 13).
- No row may make a purchase-unit, price or household-budget claim.

## Avoid lists, per row (the spec holds the full list; this is the near history)

The full `avoid` list for 10(1)–14 is in the spec at
`items.reading_topics[i].avoid` (27–60 subjects per theme). Read it in full.
The lines below add the previous two papers' same-theme subjects, from both
読解 and 聴解, because that is where a near-miss is likeliest.

- **問題9 防災** (no spec seat). The used list is
  `used_subjects_by_theme()['防災']`; all of it is off. Near history:
  20261102_1 11(2) disaster helmets; 20261008_1 11(2) evacuation drill,
  knocking on neighbours' doors; 20261002_1 14 extinguisher refill. No helmet
  or protective gear, no drill, no head-count, no extinguisher. Because 住まい
  is 問題14's headline (rule 2), keep the cloze's practice off house structure,
  furniture fixing and repairs: a household preparedness habit, not a home.
- **10(1) 環境 (business email).** Near history: 20261102_1 聴解2-3 (shirts cut
  into knitting yarn), 3-4 (seed dispersal); 20261008_1 12 green pond water.
  Recent emails also off: print shop asking for original photo files
  (20261102_1 10(4)); school-trip rail notification (20261008_1 10(2)); ink
  container take-back (20261002_1 10(4)); handover between contacts
  (20260929_1 10(3)). No clothing reuse, no take-back/recycling-collection
  request, no pond or water-quality topic.
- **10(2) 子育て・家族 (notice).** Near history: 20261102_1 14 子ども用品おさがり
  交換会; 20261002_1 10(1) 児童館 parent-child time-slot notice. Recent notices
  also off: envelope colour for deadline mail (20261102_1 10(3)); library
  newspaper shelf (20261008_1 10(5)); 回覧板/app notice (20260929_1 10(2)). No
  exchange event, no 児童館 time slot, no envelope or mailing change.
- **10(3) スポーツ・余暇.** Near history: 20261102_1 問題9 indoor climbing
  log, 聴解1-1 choir poster, 2-2 athlete retiring; 20261008_1 聴解1-4 goldfish
  tank, 2-5 5000 m race tactics, 4-11 team morale. No climbing, no race tactics,
  no retirement, no pet/aquarium.
- **10(4) 働き方.** Near history: 20261102_1 10(5) editor reading drafts
  aloud, 聴解1-4 lighting material, 2-1 interview nerves, 2-4 choosing a
  company for remote days; 20261008_1 聴解1-3 poster figure, 2-6 job change,
  4-6 farewell-party RSVP. No proofreading, no interview or job choice, no
  remote-work choice, no poster.
- **10(5) 旅行・観光.** Near history: 20261102_1 聴解4-7 hot springs, 4-11 ski
  trip booking; 20261008_1 11(1) island ferry times set by the tide, 聴解5-1
  booking a hotel with a hot spring. No ferry/tide schedule, no hot-spring or
  hotel booking, no ski trip.
- **11(1) 食.** Near history: 20261102_1 13 knife sharpening and onion tears,
  聴解4-9 late-night snacks; 20261008_1 11(4) bread rested an hour, 聴解3-2
  honey history, 4-10 cheap set meal. No knife, no onion, no bread, no resting
  or cooling, no honey, no snack-habit confession.
- **11(2) 教育.** Near history: 20261102_1 聴解1-2 homework after an absence,
  1-3 volunteer Japanese teaching, 2-6 study-group start time, 4-6 school
  festival; 20261008_1 聴解1-1 seminar presentation order, 2-2 sleep-experiment
  recruitment, 3-4 school centenary donation. No absence/homework check, no
  presentation order, no event start time.
- **11(3) デジタル化.** Near history: 20261102_1 10(4) photo files shrinking;
  20261008_1 10(3) phone kanji lookup and hand-copying; 20261002_1 10(5)
  automatic photo backup. No photos, no kanji lookup, no backup.
- **11(4) 睡眠・健康.** Near history: 20261102_1 11(4) alarm across the room;
  20261002_1 聴解5-2 health-event venue. No alarm, no waking routine, no
  health-event choice.
- **12 人間関係.** Near history: 20261102_1 11(3) lending things and the return
  date, 聴解4-2 permission to wait, 4-5 chance meeting; 20261008_1 11(3) a
  friend's phone consultation and waiting before advising, 聴解4-1/4-3/4-8.
  No lending/returning, no listening-before-advising, no consultation.
- **13 メディア・情報.** Near history: 20261102_1 聴解4-4 a singer being
  forgotten; 20261008_1 10(5) library newspaper retention, 聴解2-1 popular
  announcer, 3-3 an anime abroad. No newspaper storage, no announcer, no anime
  or overseas popularity, no celebrity.
- **14 住まい (flyer).** Near history: 20261102_1 聴解3-2 a retiree discovering
  housework; 20261008_1 13 frozen pipes in an old rented house, 聴解1-5 a
  wilting plant by the window. No frozen pipes or winter water, no plant care,
  no housework hobby. Recent 問題14 document types are off: おさがり交換会
  (20261102_1), visiting barber (20261008_1), extinguisher refill (20261002_1),
  scholarship call (20260929_1), child-seat rental (20260928_2). Pick a
  different document type and errand.

## Headline surfaces — rule 4 and the rule-4b subject diff

- **Rule 4 (themes).** This paper's 読解 headlines are 問題9 防災, 問題12
  人間関係, 問題13 メディア・情報 and 問題14 住まい.
  - 20261102_1 headlined スポーツ・余暇, 交通, 食, 子育て・家族, plus 聴解問題5
    地域活性化 and 科学・技術. **No overlap** (after the 問題12 reroll; the draw
    was 地域活性化, which would have FAILed).
  - 20261008_1 headlined 行政・手続き, 環境, 住まい, 医療・福祉, plus 聴解問題5
    旅行・観光 and 消費・経済. **Overlap = {住まい} (問題14) = the two-back budget
    of one, now spent.** No other headline may touch 20261008_1's set.
  - This paper's 聴解問題5 theme is unknown until `make mp3`; it is a WARN-only
    draw audit.
- **Rules 1–3.** The four 読解 headline themes are distinct; none appears on a
  non-headline 読解 surface; all 13 読解 themes are distinct. Drift watch:
  問題9 防災 must not drift into 住まい (14's), 10(2) notice must stay
  子育て・家族, 11(2) 教育 must not drift into 子育て・家族.
- **Rule 4b (subjects).** Each headline author writes a 5–15-char SUBJECT
  first and diffs it against all 13 読解 and 21 聴解 subjects of 20261102_1 in
  `logs/topics.json` `surfaces`. Known near-hits:
  - 問題9 vs 11(2) (helmets, same theme).
  - 12 vs 11(3) (lending), 聴解4-2, 4-5.
  - 13 vs 聴解4-4 (a forgotten singer).
  - 14 vs 聴解3-2 (housework), and 20261008_1 13 (frozen pipes; same theme,
    two back).

  Same setting + different issue is allowed and goes into `notes`; same
  setting + same issue means re-subject.

## 問題9's theme is AUTHOR-COMPOSED; 防災 was drawn by RNG from two legal values

- **Rule 3.** The 12 drawn themes are taken: 環境, 子育て・家族, スポーツ・余暇,
  働き方, 旅行・観光, 食, 教育, デジタル化, 睡眠・健康, 人間関係, メディア・情報,
  住まい. That leaves 医療・福祉, 防災, 交通, 地域活性化, 消費・経済, 文化・伝統,
  行政・手続き, 科学・技術.
- **Rules 4 and 4c.** A cloze candidate is free only if it headlines NEITHER
  previous paper (and the two-back budget is already spent by 住まい).
  20261102_1 bars 交通, 地域活性化, 科学・技術; 20261008_1 bars 医療・福祉,
  消費・経済, 行政・手続き.
- **Legal values:** 防災 and 文化・伝統. `secrets.randbelow(2)` returned 0,
  which is **防災**.
- **Shape and MOVE.** 随筆 / 一人称の前後比較, unnamed template, NOT 相関. The
  4 blanks follow `bunpou.md` §問題9.

## Why 実用文 sits at 10(1) and 10(2) — RNG

- **Recent 実用文 slots:** 20261102_1 10(3), 10(4); 20261008_1 10(2), 10(5);
  20261002_1 10(1), 10(4).
- **First slot.** 10(1) is the only slot neither previous paper used, so it
  takes one.
- **Second slot.** `secrets.randbelow(2)` over {10(2), 10(5)}, the slots used
  only two papers back, returned 0, which is **10(2)**.
- **Document types.** A second `secrets.randbelow(2)` returned 1, which puts
  the **business email at 10(1)** (環境) and the **notice at 10(2)**
  (子育て・家族).
- **The 実用文 rows carry the paper's 敬語 key.** 敬語:いらっしゃる is keyed in
  問題7, and 「〜方がいらっしゃいましたら」「いらっしゃる方は」 are the reflex
  phrasings of an email, notice and flyer. Barred in 10(1), 10(2) and 14 (and
  everywhere else). See the forms section.

## Why 〈想定→実は〉 is at 13, and 1 not 2

- **Count.** The cross-half cap is 2 and it counts the composed 聴解 talks
  (`jlpt-test-generation` §"One topic, one surface"; RC-7: a talk counts when
  the denied X is a belief held independently of the item's own question, not
  a candidate answer ruled out). The 聴解 half is not drawn yet, so the 読解
  side takes **1** and leaves 1 for the composer.
  - If the composed 聴解 carries two, Stage 3 re-angles 13. Its legal targets
    are 数えたことの報告 (2→3), 一人称の前後比較 (2→3) or 反論への応答 (2→3),
    keeping the 主張 shape only if the new MOVE still rejects a single-factor
    view. NOT 機構の説明, which is at cap 3.
- **Seat.** 20261102_1 ran it at 10(1) (科学・技術); 20261008_1 at 11(1)
  (旅行・観光); 20260929_1 at 11(4) (食). 13 on メディア・情報 repeats none of
  those seats or themes, and its persona (利用者) is not 20261102_1's 研究者.
- **Deletion test.** It applies to 13 and to nothing else. On every other row,
  deleting any sentence must leave no "assumption denied" beat. Rows most at
  risk:
  - **11(4) and 12(B)**, 意外な観察 under 機構の説明. The mismatch is between
    two facts. Never 「〜と思われがちだが」「〜と思っていた。ところが」, never 実は.
  - **10(5) and 11(2)**, 反論への応答. The objection is answered on its own
    terms, never set up to be knocked down.
  - **問題9 and 11(3)**, 一人称の前後比較. The "before" is a PRACTICE, never the
    narrator's mistaken belief.
  - **10(4) and 11(1)**, 数えたことの報告. The count is never introduced as
    contradicting an expectation.

## The RNG-picked named template

- **Not-A-but-B family at 13.** Candidates: [`〜のは、A ではなく B だ`,
  `A より B のほうが〜`, `A というより B`, `A だけではない。B こそが〜`].
  `A わけではない` was left out because 20261102_1 just used it (12(A)).
  `secrets.randbelow(4)` returned 3, which is **`A だけではない。B こそが〜`**.
  It is barred nowhere in 問題13 (20261008_1 used it in 問題12, two back).
  13 is the only 主張 closing, so it sits there.
  - Keep 「だけでは(ない)／だけでなく」 and 「こそ」 out of every OTHER final pair,
    especially 10(5), 11(2) (反論応答) and 12(A)/(B).
- **相関.** Placed by rule, not by RNG: barred in 問題9; 20261008_1 closed 問題11
  on it (two back); 問題10 last carried it in 20260928_2. So it went to the
  条件提示 row in 問題10: **10(4)**. 11(1), the other 条件提示, uses a
  different, non-quantity condition skeleton and no 〜れば.
- **分裂文.** Assigned to NO row (plan 0). The 意外な観察 and 説明 rows (10(3),
  11(4), 12(A), 12(B)) are where it lands by reflex — close them on something
  else.
- **Cap-1 templates.** 後知れ `〜ていた のだ`, 不在の残り `〜ていない` and
  先回り are assigned to no row. An unnamed final that lands on one of them
  spends its only slot; the 一人称 rows (問題9, 11(3)) are where 〜ていない and
  〜ていたのだ land by reflex.

## Tallies the authors must NOT break

- **Closing shape (13).** Values come from the CLOSED `CLOSING_MOVES` only.
  - 随筆 2 (問題9, 11(3))
  - 説明 2 (10(3), 12(A))
  - 条件提示 2 (10(4), 11(1))
  - 反論応答 2 (10(5), 11(2))
  - 意外な観察 2 (11(4), 12(B))
  - 主張 1 (13), the only shape with a spare slot
  - 実用文・分類外 2 (10(1), 10(2))
  - No seat repeats the shape 20261102_1 put in that seat (all 13 checked).
- **Template (13 closings).**
  - Named: 相関 1 (10(4)), `A だけではない。B こそが〜` 1 (13). Every other final
    is unnamed.
  - 分裂文 **0**. Cap-1 templates **0**.
- **not-A-but-B reframe family** (ではなく, というより, よりも, だけではなく,
  わけではない, and ANY final that names a foil and prefers the alternative,
  「AにないBがある」 included). Planned **1** (13). Cap 2; a second needs a
  reason in the stage-3 report.
- **MOVE (10 essay surfaces, 12 A+B as one).**
  - 〈想定→実は〉 1 (13)
  - 機構の説明 **3, at cap** (10(3), 11(4), 12)
  - 数えたことの報告 2 (10(4), 11(1))
  - 一人称の前後比較 2 (問題9, 11(3))
  - 反論への応答 2 (10(5), 11(2))
  - Headroom: 数えた +1, 一人称 +1, 反論 +1. 機構 has none. 〈想定→実は〉 has
    none on the 読解 side.
  - 20261102_1 ran 想定 1 / 機構 2 / 数えた 2 / 一人称 3 / 反論 2.
  - Per 大問 here: 問題10 holds 機構 / 数えた / 反論; 問題11 holds 数えた / 反論 /
    一人称 / 機構. No MOVE twice in one 大問, so the next paper inherits no
    per-大問 MOVE bar.
- **Shared-MOVE rows need different resolutions and no shared persona**
  (dokkai.md).
  - 機構 ×3: 10(3) (職業人; how one piece of equipment/technique works, stops
    there) / 11(4) (解説者; a fact that does not fit another fact, then its
    cause) / 12 (論者 + 生活者; one relational habit explained, then a
    non-fitting fact and a different cause and advice).
  - 数えた: 10(4) (観察者; own workplace, one span, 相関) / 11(1) (趣味の実践者;
    own cooking, a categorical condition, no quantity).
  - 一人称: 問題9 (生活者; a household preparedness practice) / 11(3) (学生; a
    digital-tool practice).
  - 反論: 10(5) 「理由を示して変えない」 (旅行者) / 11(2) 「譲歩して一部を変える」
    (職業人).
- **Persona** (cap 2 per archetype). 職業人 2 (10(3), 11(2)), 生活者 2 (問題9,
  12(B)). Every other persona once. 10(5) is a traveller, not a host: a host
  is 職業人 and would break the cap — re-plan, do not relabel.
- **Voice quota** (12 passages, 問題14 excluded).
  - **First person: at least 4.** Planned: 問題9, 10(4), 10(5), 11(1), 11(2),
    11(3), 12(B), 13.
  - **です・ます throughout: at least 3.** Planned: 10(3), 11(2), 12(B), plus
    the two 実用文 (10(1), 10(2)). Write です・ます and the length band
    together.

## Tested forms that must stay out of the 読解 prose (Item integrity #15)

This paper keys the following. Read the spec, not this copy, if anything
rerolls. Scope is 言語知識・読解; composed 聴解 is out of scope (RC-8).

- **問題7:** 〜つつも, 〜を踏まえて, 〜ものなら, 〜はずがない, 〜と同時に,
  〜ことだし, 〜かねない, 〜ないわけにはいかない, 〜のもとで, 〜としたら,
  〜だらけ, 敬語:いらっしゃる. 敬語 count 1 of 12.
- **問題8:** 〜に伴って, 評価反論(〜とはいえ…), 対比表現(〜一方…だ),
  感情強調(〜てたまらない), 〜をはじめ.

Consequences:

- **敬語:いらっしゃる is the 実用文 reflex.** None of 「いらっしゃいましたら」
  「いらっしゃる方」「いらっしゃいます」 anywhere (10(1) email, 10(2) notice, 14
  flyer above all). Write 「〜方は」「お持ちの方は」.
- **Notice and flyer reflexes.** 「〜に伴い／に伴って」 (「工事に伴い」) and
  「〜をはじめ（とする）」 (lists) are the stock phrasings of 10(2) and 14; 「〜を
  踏まえて」 (「ご意見を踏まえて」) is the email reflex of 10(1). Use none.
- **The 反論応答 rows (10(5), 11(2)).** 「〜とはいえ」 is the concession reflex
  and 「〜つつも」 its literary twin; 「〜としたら」 is the reflex of a
  hypothetical objection. Use none — write 「たしかに…。ただ、…」「…が、…」.
- **The 説明 / 意外な観察 rows (10(3), 11(4), 12(A), 12(B)).** 「一方（で）」 is
  the contrast reflex and 「〜と同時に」「〜のもとで」 the mechanism reflexes.
  Use none.
- **The 相関 row (10(4)).** 「〜に伴って」 is the correlation reflex. Write the
  correlation with 「〜では」 or 「〜ほど」.
- **The 主張 row (13).** 「〜かねない」 is the warning reflex and 「〜はずがない」
  the rebuttal reflex. Use none.
- **The 一人称 / 随筆 rows (問題9, 11(3)) and every first-person row.**
  「〜てたまらない」 (feeling), 「〜ないわけにはいかない」 (obligation), 「〜だらけ」
  (description), 「〜ことだし」 (reason), 「〜ものなら」 (hypothetical) are the
  narrative reflexes. Use none.
- **A prose grep is owed for the general-purpose 問題8 frames** (`exam-blueprint`
  §"A `grammar_p8` draw whose form is a general-purpose sentence pattern"):
  とはいえ, 一方, に伴って／に伴い, をはじめ. Grep every surface. Re-word every hit
  except at most one, and that one must not be in the tested frame. Prefer 0.
- **Stage 3 re-grep.** Every form above goes into the Stage-3 keyed-form
  re-grep with counts and frames (文末／連用／連体), including the 問題9 [論理接続]
  key once the 文法 author has written the cloze.

## The two things that get checked by hand

1. **The unnamed finals must not share a skeleton** with each other, with the
   named ones, or with 20261102_1's same-seat last two sentences (RC-3 table).
   Pairs at risk:
   - 問題9 against 11(3): both 随筆, both 一人称の前後比較.
   - 10(3) against 12(A): both 説明, both 機構.
   - 11(4) against 12(B): both 意外な観察, both 機構; neither a cleft.
   - 10(4) (相関) against 11(1) (non-quantity condition, no 〜れば).
   - 10(5) against 11(2): both 反論応答; different resolutions.
   - 12(A) against 12(B): read A against B FIRST.
2. **The MOVE column and the TEMPLATE column are read separately**, once down
   each, and both are re-read after every repair (`jlpt-test-generation`
   §"One topic, one surface"). Run the deletion test on every row except 13.
