# QA report — 20260928_1 (stage 4, round 2: fresh re-review of the round-1 repairs)

- Reviewed 2026-09-28 15:39 JST, in a fresh context. I authored nothing in this paper and did not write round 1.
- Solved from `qa/20260928_1/keyless.md`, rebuilt fresh with `make keyless 20260928_1` before I opened any key.
- Source revision, checked with `shasum` at the start and again before writing. The shas and mtimes did not change, and both match the hand-off:
  - `言語知識・読解.md` = `86e9ce94fbf337d3ac6ecd7aba4dd4471a6ef8ed`
  - `聴解.md` = `7dc47ce36cd3ae770789039f3d7a482a008fe46b` (unchanged since round 1)
  - `聴解スクリプト.txt` = `cb1695d9ea39862bd45a43aeb4948c7634187f4f` (unchanged since round 1)
- Entry gate: I ran `make check` myself. It has exactly one FAIL, `20260928_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)`. That FAIL is expected, because stage 5 has not started. Every WARN naming this paper is resolved in §6.
- Read in full before starting: `AGENTS.md`, `.agents/exam-qa-review/SKILL.md` (all 1,100 lines), `qa/qa-report-20260928_1.md`, `qa/blueprint-rerolls-20260928_1.md` and `qa/dokkai-allocation-20260928_1.md`. For the closing re-read I also used `question-authoring/references/dokkai.md` §"Thirteen surfaces" and §"MOVE allocation", and `exam-blueprint/SKILL.md` §"One grammar point" and §"Mutually exclusive form families".

## 1. Verdict

QA: FAIL (3 findings, 0 automatic)

**F3 is not counted, and here is why.** F3 is 聴解問題2-2番 「すくない」 against 「少なくない」. It is recorded as **open, pending the user's ear-check**.

- It is one transcript line in a composed clip. It is printed in 練習.html and 模範解答, but it is not in the audio, which says whatever it says. It is not in the booklet either.
- No key depends on it. The key is decided by the next line, 「駐車場がある施設の方が参加者の数が増えると思うんです」.
- Its repair is upstream (`tests/imported-n2-2023-12/聴解スクリプト.txt` L70, then `make choukai-bank`, then `--replay` for 20260904_3, 20260907_1 and this paper). That repair cannot be decided without listening, and nothing here can listen: there is no ASR.
- Holding this paper's FAIL/PASS on it would make the verdict hinge on a fact nobody in this context can establish. For that reason it is carried as a pending item outside the count, not as a pass.
- **If the ear-check says 「少なくない」, the replay must land before stage 5.** Stage 5 writes 模範解答, and 模範解答 prints that line.

## 2. Blind-solve diff

I solved all 71 言語知識・読解 items from the keyless render and diffed them against the key tables: **71/71 agree, 0 mismatches.**

The 聴解 half has byte-identical shas to round 1, which solved it 30/30. I did not re-solve it (§7).

My answers were:

- 1–30: 1 4 3 4 3 / 2 1 3 2 1 / 3 2 4 / 2 4 1 4 3 3 2 / 3 4 1 1 4 / 1 2 2 4 4
- 31–51: 3 3 4 4 2 **1** 1 4 1 2 2 3 / 1 4 2 3 4 / 2 1 4 3
- 52–71: 3 2 3 1 1 / 1 3 3 2 2 4 **4 4** / **2 3** / 2 4 1 / **2** 3

The items this round's scope covers are in bold: 36, 63–64, 65–66 and 70.

Blind strategy passes over 問題10–13 (items 52–69, 18 items), re-run because 11(4) and 12(B) changed:

| strategy | hits | rate | bar |
|---|---|---|---|
| option sharing the most character bigrams with its passage | 2/18 | **11.1 %** | ≤45 % |
| second-longest option (ties broken by position) | 5/18 | **27.8 %** | ≤45 % |

- Round 1 reported 6/18 on the second pass. The difference is tie handling only; no option changed.
- The key is the uniquely longest option in 3/18 items (57, 66, 69).
- The largest printed max/min ratio in any item is 1.40 (item 68).

## 3. Per-question walkthrough (101 rows)

- **Re-reviewed in full this round:** 問題1-2 (F1), all of 問題7 (F2), all of 問題11, 問題12 and 問題14 (F4 and F5). These are the changed items and their whole 大問, per §"Fix, regenerate, re-check, RE-REVIEW".
- **Other 言語知識・読解 rows:** confirmed by my blind solve and by the deciding line, which is quoted.
- **聴解 rows:** carried forward from round 1 on identical bytes (§7).

### 文字・語彙

| 項目 | 鍵 | 判定 | 決め手 / どこが問題か | どう直すか |
|---|---|---|---|---|
| 問題1-1 | 1 | OK | 首相＝しゅしょう. The {しゅ,しゅう}×{しょう,そう} set is unchanged from round 1. | — |
| 問題1-2 | 4 | **OK — F1 closed** | The cell now cites Shin Kanzen N2漢字 #384. I opened `kanji_tables.md` L3066–3073, which reads 「384最 … サイ … もつとも / 叢も」: the headword block, OCR of もっとも／最も. ちっとも now cites `goi_reference.md` L2539 「③少しも／ちっとも～ない」 and L2540 「洗ってもちっともきれいにならなかった。」, both opened and both a headword plus its example. とても and 何とも cite Hajimete L20794 and L20720, both opened, and both are headwords. The band line reads 「帯: N2（最もはShinkanzen N2漢字 #384の学習語として確認）」. The four reroll reasons are in `qa/blueprint-rerolls-20260928_1.md` rows 2–5. Row 4 records 捕らえる as **undrawable** (no three real 〜らえる distractors), not as a preference. | — |
| 問題1-3 | 3 | OK | 「この辺りは夜になると静かです」 | — |
| 問題1-4 | 4 | OK | 柔軟体操＝じゅうなんたいそう | — |
| 問題1-5 | 3 | OK | 副社長＝ふくしゃちょう | — |
| 問題2-6 | 2 | OK | 「交通費が支給される」 | — |
| 問題2-7 | 1 | OK | 威張って | — |
| 問題2-8 | 3 | OK | 「スープの味をみて」 is the general 見る. | — |
| 問題2-9 | 2 | OK | 花火 | — |
| 問題2-10 | 1 | OK | 「書類は…破棄」 | — |
| 問題3-11 | 3 | OK | 未記入 | — |
| 問題3-12 | 2 | OK | 依頼主 | — |
| 問題3-13 | 4 | OK | 多様 | — |
| 問題4-14 | 2 | OK | 「大きな地震に（耐えて）きた」 | — |
| 問題4-15 | 4 | OK | 「外に出る（気がしない）」 | — |
| 問題4-16 | 1 | OK | 「魚を…出したまま…（腐って）」 | — |
| 問題4-17 | 4 | OK | 「一年中日本全国を（飛び回って）」 | — |
| 問題4-18 | 3 | OK | 「伝言を（言付けて）」 (round-1 N1 stands) | — |
| 問題4-19 | 3 | OK | 「ユニフォームが買えない」 fixes the money sense. | — |
| 問題4-20 | 2 | OK | 「ページを開くと…飛び出す」 | — |
| 問題5-21 | 3 | OK | 怠る＝なまける | — |
| 問題5-22 | 4 | OK | プラン＝計画 | — |
| 問題5-23 | 1 | OK | そういえば＝思い出したけど | — |
| 問題5-24 | 1 | OK | ようやく＝やっと | — |
| 問題5-25 | 4 | OK | 直ちに＝すぐに | — |
| 問題6-26 | 1 | OK | 「雑誌も一週間まで貸し出しています」 | — |
| 問題6-27 | 2 | OK | 「五人家族の生活を長い間支えてきた」 | — |
| 問題6-28 | 2 | OK | 「一人一人の意見を尊重する」 | — |
| 問題6-29 | 4 | OK | 「点数が大きく伸びた」 | — |
| 問題6-30 | 4 | OK | 「新しい条件で合意した」 | — |

### 文法 (問題7 re-reviewed whole)

| 項目 | 鍵 | 判定 | 決め手 / どこが問題か | どう直すか |
|---|---|---|---|---|
| 問題7-31 | 3 ようがない | OK | 「住所も電話番号も分からないのでは」 means there is no means. | — |
| 問題7-32 | 3 かのうちに | OK | 「鳴るか鳴らない（　）」 | — |
| 問題7-33 | 4 そうにない | OK | 「この雨では…行われ（そうにない）」 | — |
| 問題7-34 | 4 にとって | OK | 「祖母（にとって）…特別な場所だ」 | — |
| 問題7-35 | 2 限り | OK | 「時間の許す（限り）」 (4課-5, the range sense) | — |
| 問題7-36 | 1 にあたって | **要修正 (R2-F1)** | **The item itself is sound.** 「隣町での二号店の開店（にあたって）、…あいさつをした」. をめぐって needs a dispute to follow, and none does. に基づいて needs a basis for a judgment, and 開店 is not one. に沿って needs a standard or path to follow, and 開店 is not one. All four options are N+compound particles, and neither に際して nor に先立って is offered, so there is no second answer. The stem is 33 characters, and the stem distribution is still in band (the gate reports mean 40.2, 4 under 34, spread 50). The prose grep is 0 for にあたって/当たって. **The draw is not sound.** The Shin Kanzen N2文法 目次 (PDF p.3, read as an image) lists **1課-2 「〜に際して・〜にあたって」 as ONE heading**, the same form as F2's 4課-4 「〜を通じて・〜を通して」. `20260907_1` 問題7-40 **keyed** 〜に際して. That paper is 6 ledger entries back, and grammar_p7's cooldown is 10. The F2 repair therefore landed on F2's own defect class. | Run `--reroll-one grammar_p7:5 --seed <fresh>` again. **Before accepting the draw**, look up its Shin Kanzen 目次 heading and check it against the p7 and p8 draws of the last 10 ledger entries. Keep the key at 1 and re-author item 36. Record the reason as row 11 in `qa/blueprint-rerolls-20260928_1.md`. |
| 問題7-37 | 1 に反して | OK | 「大方の予想（に反して）」 | — |
| 問題7-38 | 4 ない限り | OK | 「よほどの事情が（ない限り）…認めません」 (5課-2, a different heading from 35's) | — |
| 問題7-39 | 1 伺って | OK | The student's own action takes the humble form. | — |
| 問題7-40 | 2 末に | OK | 「話し合いを重ねた（末に）、ようやく」 | — |
| 問題7-41 | 2 っぽい | OK | 「飽き（っぽい）性格で…長続きしなかった」 | — |
| 問題7-42 | 3 に伴って | OK (note) | 「再開発が進むの（に伴って）…少しずつ姿を消している」. Its distractor 4 に際して shares 36's key heading (1課-2). No rule forbids that and it gives no answer away, but it disappears if R2-F1's reroll moves 36 off 1課-2. | — |
| 問題8-43 | 1 | OK | 通い続けているのは→店主の→★いれる一杯の→コーヒーが忘れられない→からだ | — |
| 問題8-44 | 4 | OK | 人が→大勢並んでいる→★からといって→…わけではない | — |
| 問題8-45 | 2 | OK | 年をとった→飼い犬の→★健康のために→毎朝散歩に連れて行く | — |
| 問題8-46 | 3 | OK | お取り寄せした→商品が→★届き次第→お電話でご連絡します | — |
| 問題8-47 | 4 | OK | 例えば…などの→昔ながらの→★保存食を→今も自分で作っている | — |
| 問題9-48 | 2 しかも | OK | 「画面はもう何も教えてくれない。（しかも）、そこは五つの線が集まる大きな駅だった」 | — |
| 問題9-49 | 1 ものだ | OK | 「駅の形は少しずつ頭に入ってくる（ものだ）」 | — |
| 問題9-50 | 4 手元の画面 | OK | 「道順案内に従うだけだったころのわたしなら」 | — |
| 問題9-51 | 3 身についた | OK | 「いつのまにか（身についた）」 | — |

### 読解 (問題11, 12 and 14 re-reviewed whole)

| 項目 | 鍵 | 判定 | 決め手 / どこが問題か | どう直すか |
|---|---|---|---|---|
| 52 | 3 | OK | 「床についた杖には腕から体重の一部がかかり、そのぶん足の負担が減ります」 | — |
| 53 | 2 | OK | 「登録のない方が…前日の夕方5時までに…お知らせください」 | — |
| 54 | 3 | OK | 「ためた分をそこで先に使ってしまい」 | — |
| 55 | 1 | OK | 「こちらで洗ってからお返しするのでしょうか。それとも…」 | — |
| 56 | 1 | OK | 「給料日に払う予定を書き出していた家庭ほど…少なかった」 | — |
| 57 | 1 | OK | 「記入するのはだれが測っても同じ結果になる数字で」. 2 and 3 are the 見立て the form 「求めていません」, and 4 is denied by 「知らせることもしていません」. | — |
| 58 | 3 | OK | 「住民の集めた数字があれば、優先して確認に行く塀を選べます」. 1 is the objection the author answers, 2 is denied by 「外から見ても分かりません」, and 4 is denied by 「「安全です」と知らせることもしていません」. | — |
| 59 | 3 | OK | 「窓を閉めきって暮らしていた」「窓のふちにテープを貼っていた」. 1 is the after-state, 2 is denied by 「暖房をつけ」, and 4 is never said. | — |
| 60 | 2 | OK | 「外の季節がどのあたりまで来ているのかが分かるようになった」. The 3 年 frame and the passage are unchanged. | — |
| 61 | 2 | OK | 「長く続いていたのは、二人のうち一人が前の年から当番をしていた組でした」. 1 is denied by 「一人で当番に入った人は、2年目にはたいてい表から消えています」, 3 is never said, and 4 misuses the お年寄り line. | — |
| 62 | 4 | OK | 「経験者がいれば…その場で教えられます。初めての人が一人で困る時間がないのです」. 1, 2 and 3 are unmentioned levers, each against the passage's two-condition finding. | — |
| 63 | 4 | OK | 「九九は正確に合っている。ずれているのは、数字を書く位置のほうである」. The new final does not touch the deciding line. 1 contradicts it, 2 is denied by 「列が斜めに傾いていく」, and 3 is never said. | — |
| 64 | 4 | OK | 「児童は列を頭の中で保っておく必要がなくなり、その分の注意を、九九や繰り上がりに向けられる」 (¶3, unchanged). The old final 「…先に示しているのである」 was a second witness to key 4. Removing it leaves the key on ¶3, which still decides it on its own. 1 is denied by 「九九を覚え違えていれば、ます目があっても答えは合わない」, 2 by 「字の大きな子も小さな子も」, and 3 is never said. | — |
| 65 | 2 | OK | A: 「言いたいことを一段やわらげてしまう」. B: 「呼び方ひとつで、話しかけやすさはずいぶん変わる」. 1 contradicts A's 「呼ばれる側は気にしていなくても」. 3 is the objection B concedes (「この声はもっともだ」) and A rejects, so it is not shared. 4 is B only. The new B final does not move any of these. | — |
| 66 | 3 | OK | A: 「だれもが名字に「さん」をつけて呼び合うのである」. B: 「一人一人が呼ばれたい呼び方を名札に書いておけばよい」. 2 is the reversal, 1 is B only, and 4 is against both. | — |
| (12B final) | — | **要修正 (R2-F2)** | See §4. | — |
| 67 | 2 | OK | 「話を追うことに気を取られず…耳を向けることができました」 | — |
| 68 | 4 | OK | 「語る人によって、また同じ人でもその日によって、まるで別の噺になる」 | — |
| 69 | 1 | OK | 「あらすじを一つ読んでから行くことを、私は勧めたい」 | — |
| 70 | 2 1,100円 | **OK — F5 closed** | The stem now reads 「田中さんたちが払う料金は、3人分で合わせていくらか。」, and 「当日に」 occurs 0 times in any 問題14 stem (the paper's one remaining hit is item 55's option 3). The key combines two cells: 7月30日 is 「イ　見学と試食」, priced 「子ども一人300円、大人一人400円」, giving 300 + 400 × 2. 700 counts one adult, 1,200 charges the child as an adult, and 800 is エ's 「一組800円」. Every stem detail (娘、夫、3人、7月30日) is on the flyer. | — |
| 71 | 3 | OK | 「エは、はがきでお申し込みください。」「7月10日にセンターに届いたものまで受け付けます。」「全員ぼうしをお持ちください。エでは、エプロンと三角きんも要ります。」 | — |
| (repo) | — | **要修正 (R2-F3)** | `言語知識・読解.md` L213 is a stale scaffold comment inside 問題9's scope. See §4. | — |

### 聴解 (unchanged bytes; round-1 rows carried forward, keys only)

| 大問 | 鍵 | 判定 |
|---|---|---|
| 問題1 1–5番 | 2 3 3 4 3 | OK (round 1) |
| 問題2 1–6番 | 1 1 2 4 4 1 | OK (round 1). **2-2番 is F3, open pending the user's ear-check (§1)** |
| 問題3 1–5番 | 4 3 4 4 3 | OK (round 1) |
| 問題4 1–11番 | 3 2 1 2 1 3 3 3 1 2 2 | OK (round 1) |
| 問題5 1番, 2番 質問1, 質問2 | 4 3 2 | OK (round 1) |

## 4. Findings

| id | item | class | evidence | fix / status |
|---|---|---|---|---|
| F1 | 問題1-2 cell and reroll record | — | Verified on disk (§3). | **CLOSED** |
| F2 | 問題7-36 (the old 〜を通して) | — | The reroll ran with seed 85597537, and the spec equals the ledger field for field. The new item is sound as an item. The landing site is R2-F1. | **CLOSED as a draw; superseded by R2-F1** |
| F3 | 聴解問題2-2番 「すくない」 | a 聴解 script line (check 6) | The key is unaffected. | **OPEN — pending the user's ear-check** (§1). Not counted in this round's verdict. |
| F4 | 11(4), 12(A) and 12(B) closings | — | The 11(4) final is now 「位のずれによる間違いは、書く紙の形を変えるだけで防げる種類の間違いなのである。」 and the 12(B) final is now 「本人が自分の手で書いた一行には、上から配られた決まりにない重みがある。」. Neither matches the 先回り predicate, so the three-way skeleton pile-up is gone. However, 12(B)'s landing site is R2-F2. | **Skeleton CLOSED; see R2-F2** |
| F5 | 問題14-70 stem | — | 「当日に」 is removed (§3). | **CLOSED** |
| **R2-F1** | 問題7-36 〜にあたって | an item redrawn inside the rotation cooldown, judged by the same one-heading-one-point standard that F2 applied | The Shin Kanzen N2文法 目次 lists 1課-2 as 「〜に際して・〜にあたって」 (PDF p.3, read as an image). `20260907_1` 問題7-40 keys 「〜に際して」 (its L158 options are 「1. に際して…」 and key-table L523 reads 「「〜に際して」は改まった場面で…」). That paper is 6 draws back against grammar_p7's 10-draw cooldown. **This is the F2 class again, one repair later.** The owner's letter, "membership is one form spelled twice", does not forbid it, and `make check` passes it: 「rotation claim holds」, and 「問題7 draws at most one entry per form family」 is a skip. But round 1 filed F2 on exactly the heading argument, and the orchestrator acted on it. Accepting the same shape here would apply the bar unevenly. If the orchestrator instead rejects RC-3's heading-level identity, R2-F1 falls with it, and F2's reroll becomes unnecessary in hindsight. Say which in the stage record. | OPEN. Run `--reroll-one grammar_p7:5 --seed <fresh>`. Accept the draw only after checking its 目次 heading against the last 10 ledger entries' p7/p8 draws. Keep the key at 1, re-author 36, record the reason, re-run `make check`, and send item 36 plus all of 問題7 back through re-review. |
| **R2-F2** | 問題12(B) final (F4's landing site) | the not-A-but-B family placed on a third surface, against the binding allocation ("exactly **2** surfaces, 問題11(1) and 問題12(A). Do not add another member anywhere else"). It also re-rhymes the F4 pair on the contrast axis. | 「本人が自分の手で書いた一行には、**上から配られた決まりにない**重みがある。」 names a foil (the top-down rule) and prefers the alternative. That is 「決まりよりも、本人の一行のほうが重い」 in other grammar, the 「AよりもB」 member that `dokkai.md` L233–235 lists ("the same move in five surfaces of grammar"). It sits directly beside 12(A)'s 「相手の立場を示す札**というより**、…」, so A and B both now close on a named-foil contrast: F4's pair, re-clothed (`exam-qa-review` §5, the repair-collateral clause). No gate token sees it: `check_dokkai_closing_reframe_scope` reports 1 of 13 and the template check reports nothing. Measured over the 13 closings of every paper on disk, including all 10 imports, the predicate 「にはない｜にない…(が｜を)(ある｜持)」 in a final fires **only here**. | OPEN. Rewrite 12(B)'s final sentence with **no foil** and no comparison. It must also avoid a ば-conditional (11(3) holds that skeleton: 「この二つがそろえば、…書いてくれます」), a timed 前に/たびに…ている (12(A)), a cleft (10(3)) and 〜なのである (11(4)). Keep the 反論応答 label: the preceding sentence 「上の立場の人が自分から…書いておけば、呼ぶ側は迷わずにすむ」 already answers the objection. Then re-read the shape, template, MOVE and claim columns, and update `logs/topics.json` `claim["問題12(B)"]`, which quotes the current final. |
| **R2-F3** | `言語知識・読解.md` L213 (also `_sections/問10-14_読解.md`, and the three HTML builds as an HTML comment) | a stale scaffold artifact in the shipped source, which blinds the gate on 問題9 | The line is 「<!-- reading_topics (theme + avoid) — … [9] スポーツ・余暇; … -->」. It carries the **pre-reroll** 問題12 theme, which is now 人間関係. It sits after 問題9's 51 and before `# 【読解】`, so `dokkai_closing_scopes()` puts it inside 問題9's prose. `passage_final_sentence()` returns the comment itself as 問題9's final sentence, which means **no closing-scope check measured 問題9 on this paper**, and the comment adds 48 JP characters to 問題9's measured prose (690 as-is, 642 stripped, against a band of 500–700). I re-ran the four closing checks (reframe, reframe scope, belief-denial, final templates) and `check_dokkai_lengths` on the stripped body: the verdicts are identical, so no hidden FAIL. The comment is invisible in the rendered booklet, but it ships in the page source of 言語知識・読解.html, 解答.html and 練習.html. | OPEN. Delete L213 and its blank line from `言語知識・読解.md` and from `_sections/問10-14_読解.md`. Then run `make booklet`, `make sheet` and `make check`. |

Three findings is ≤3, so under the stage-4 loop rule the orchestrator may fix them directly with the same rigor. However, **R2-F1 is a tier-C reroll that re-authors an item**, and a re-authored item is new text. I recommend a fresh re-review of item 36, 問題7 and the 12(B) closing column rather than the direct-fix exception. That is a small scope.

### Rulings asked for in the brief

- **問題9's 「今では…ている」 and the F4 claim family: not the same family, so no finding.**
  - The F4 family is "a small artifact does the person's work before they act": 11(4)'s old 「…先に示している」 and 12(B)'s old 「…前に消している」.
  - 問題9's final is 「乗り換えのたびに見上げてきた板の一枚一枚が、今ではわたしの頭の中で、駅の地図になってつながっている。」. It claims the reverse: the narrator stopped delegating to a device, and the knowledge is now the narrator's own. Its 「たびに」 sits inside a relative clause on 板 (見上げてきた板), not on the main predicate, and つながっている is a resultative state, not an act done in advance.
  - **The skeleton predicate is another matter.** RC-5's regex does fire on this final once 問題9's scope is read correctly. Round 1 could not see this because of R2-F3: the gate read the comment instead. So "fires 3× here" was measured without 問題9. On the true 13 finals the regex gives **問題9 and 12(A) = 2**. RC-5 proposes a cap of 1, which as written would false-fail this paper on 問題9. See RC-R2-4.
  - The `logs/topics.json` note 「now only 問題12(A) keeps it」 is right about the skeleton and wrong about the stated predicate. It is harmless but imprecise, and no quoted string is involved.
- **The 13 finals, down the column. The shape is from the closed vocabulary; the skeleton is normalised.**

| surface | shape | skeleton |
|---|---|---|
| 問題9 | 随筆 | 「X が、今では Y になってつながっている」 (before→after state) |
| 10(1) | 説明 | 「A する分だけ、B は軽くなります」 (proportional) |
| 10(2) | 実用文・分類外 | (notice instruction) |
| 10(3) | 意外な観察 | 分裂文 |
| 10(4) | 実用文・分類外 | (email close) |
| 10(5) | 条件提示 | 相関 |
| 11(1) | 反論応答 | わけではない |
| 11(2) | 随筆 | 「X のおかげで、…分かるようになった」 |
| 11(3) | 条件提示 | 「この二つがそろえば、…てくれます」 (ば-conditional) |
| **11(4)** | 説明 | 「X は、Y だけで防げる種類の N なのである」 (categorical) |
| 12(A) | 主張 | というより (+ 前に…ている) |
| **12(B)** | 反論応答 | 「X には、Y にない Z がある」 (**foil contrast, R2-F2**) |
| 13 | 主張 | 「…ことを、私は勧めたいと思います」 |

  - Shapes: 随筆 2, 説明 2, 意外な観察 1, 条件提示 2, 反論応答 2, 主張 2, 実用文 2. Every shape is ≤2.
  - Named templates: 1 each, and the gate agrees ("13 finals read" OK).
  - Unnamed skeletons: all pairwise distinct.
  - 11(4) as 説明 holds. It classifies the error type and stops. It does not exhort, and it does not use 「こそ」 or the 「だけでは」 construction: 「だけで防げる」 is the inverse, "suffices", and no template token matches.
  - **Round 1's named pair, re-derived on the new text (§5 of the skill):** 11(4) is now categorical/説明 and 12(B) is foil-contrast/反論応答, so the pair no longer shares a skeleton or a label. 12(B) now pairs with 12(A) on the contrast family instead, which is R2-F2.
- **MOVE column: unchanged, and every cap holds.** 〈想定→実は〉 = 問題13 + 聴解2-5 = 2. 機構の説明 3 (10(1), 10(3), 11(4)). 数えた 2. 前後比較 2. 反論への応答 2 in 読解. Neither new final introduces an attributed assumption or a denial. 12(B)'s 「この声はもっともだ」 is a concession that is then answered, which is the 反論への応答 move.

## 5. Root-cause table (new rows only)

Rounds 1's RC-1 to RC-12 stand unchanged. These rows are new.

| id | finding | code | tests showing the class | owning file | proposed edit |
|---|---|---|---|---|---|
| RC-R2-1 | R2-F1 | GATE-BLIND (extends RC-3) | Ledger p7 draws of 〜に際して/〜にあたって fall at indices 2 (0810_2), 12 (0818_1), 15 (0827_1), 23 (0907_1) and 29 (this paper). Within the 10-draw window that gives **3 transitions** (3, 8 and 6 apart), with one at exactly 10. Together with RC-3's 4 を通じて/を通して pairs, this is systemic. | `exam-blueprint` §"Mutually exclusive form families"; `sample_items.py`; `pools.json` | RC-3 proposes `grammar_point_identity`. Build it from the Shin Kanzen N2文法 目次 headings that print two forms under one number, read from PDF pp.3–4 in this round. From those pages: 1課-2 に際して・にあたって, 4課-4 を通じて・を通して, 2課-3 ばかりだ・一方だ, 9課-1 につれて・にしたがって, 9課-2 に伴って・とともに, 11課-2 にかかわりなく・にかかわらず, 12課-2 どころではない・どころか, 12課-4 わけではない・というわけではない, 14課-2 ものの・とはいうものの. The remaining pages must be read before committing. **Also:** `--reroll-one` should print the new draw's identity tokens against the cooldown window before writing the spec, so a fix pass sees a same-heading landing at the moment it happens. That is what let F2's repair land on R2-F1. Before committing, run the check over every spec and grandfather the ids it moves by name. |
| RC-R2-2 | R2-F2 | RULE-UNENFORCEABLE | 1 (this paper). The predicate fires on 0 of the other generated papers and on 0 of 10 imports. | `question-authoring/references/dokkai.md` L233–235; `REFRAME_CLOSING` / `FINAL_SENTENCE_TEMPLATES` in `tools/check_consistency.py` | The five-grammar family list is a list of surfaces, so an author writing a sixth grammar for the same move satisfies it. Add: 「**any** final that names a foil and prefers the alternative — 「AにないBがある」「Aにはない」「Aより」 included — is a member; list the foil in the allocation column」. Gate it only after a measurement. My one-paper measurement is `にはない｜にない[^、。]{0,6}(が｜を)?(ある｜持)` over the 13 finals of every paper: it fires only on 20260928_1 12(B), with 0 official hits, so a token row with a cap of 1 would FAIL nothing else on disk. |
| RC-R2-3 | R2-F3 | PIPELINE-GAP + GATE-WRONG | 1 (the first paper scaffolded since commit 1881278 added the comment at `tools/scaffold_sections.py` L124) | `tools/scaffold_sections.py`, `tools/assemble_paper.py`, `check_consistency.passage_prose` / `dokkai_closing_scopes` | (a) The scaffold's orientation comment must not reach the assembled paper. Either `assemble_paper.py` strips `<!--…-->` lines, or the scaffold writes the note to `_sections/README` instead. (b) `passage_prose()` (or `dokkai_closing_scopes()`) must strip HTML comments before measuring. Founding measurement: 20260928_1's 問題9 final reads as the comment, and its prose measures 690 against 642 JP characters stripped. Every closing check is blind to 問題9 on this paper. (c) Add a gate line that fails any `<!--` in a shipped `言語知識・読解.md` outside the generated banner. |
| RC-R2-4 | RC-5 amendment (round 1's proposal) | GATE-WRONG, prospective | — | round-1 RC-5 | As proposed, RC-5's founding regex fires on 問題9's true final (「乗り換えの**たびに**見上げてきた板…つながっている。」): the たびに is in a relative clause and the ている is a resultative state. Under the proposed cap of 1, it would FAIL this paper. Anchor the timed clause to the main clause: require the 前に/たびに/先に to follow the matrix subject's 「は/が、」 and precede the object. Or cap at 2. Re-run over all papers: on correct scopes the unanchored regex gives this paper 2 (問題9, 12(A)) and 5 other papers 1 each. |

## 6. Coverage

### Steps run on the re-review scope

- **Step 0:** fresh keyless render, a 71-item blind solve, and both strategy passes (§2).
- **Steps 1–2b:** key-by-key proof and distractor elimination for 問題1-2, 問題7 (all 12), 問題11 (57–64), 問題12 (65–66) and 問題14 (70–71). The other 言語知識・読解 rows are confirmed by the blind solve and a quote.
- **Step 2.5:** for 36, にあたって is a Shin Kanzen N2文法 1課-2 headword, so it is N2 on both sides.
- **Step 3:**
  - Keyed-form grep over the 問題10–14 prose and gloss lines after the prose repairs: にあたって/当たって appears 0 times. The two new finals contain no 問題7/8/9 keyed form (「にない」 is not 「ない限り」). The gate line 「no 問題7/8/9 keyed form appears more than 1×…」 is OK.
  - Provenance scan of every re-authored string (「二号店」「一軒ずつ回って」「書く紙の形を変えるだけで」「防げる種類の間違い」「上から配られた決まり」「自分の手で書いた一行」) against the 31 booklets, every `refs/*/*.md` extract and every paper's `言語知識・読解.md`: the only hit outside this paper is 20260911_1's 解説 example 「開店にあたって」, one explanatory phrase and not a copy.
  - Option-length ratio: at most 1.40.
  - 問題7 stem distribution, per the gate: mean 40.2, 4 stems under 34, spread 50.
- **Step 4:** the 聴解 half is unchanged, so round 1's checks 1–6 stand on identical shas. I did not re-run them (§7).
- **Step 5:** the topic table is unchanged. The edits touched finals only, and no subject, theme or headline moved.
  - The `logs/topics.json` 20260928_1 row has all 8 keys.
  - `claim["問題11(4)"]` (「…書く紙の形を変えるだけで防げる。」) and `claim["問題12(B)"]` (「…上から配られた決まりにない重みを持つ。」) match the new finals.
  - The notes record F4 and F5.
  - All 60 quoted 「…」 strings in notes, shapes, surfaces and claim occur in the paper or script.
  - Headline six-slot set, unchanged: 交通, 人間関係, 文化・伝統, 食 and 聴解5 スポーツ・余暇/消費・経済.
- **Step 6:**
  - The spec equals the ledger in items, seed string and pools_sha. The seed string ends `+reroll-one(grammar_p7:5,85597537)`.
  - The reroll reasons are in `qa/blueprint-rerolls-20260928_1.md` (10 rows).
  - The 71 言語知識・読解 positions match `answer_positions` (the gate agrees).
  - Artifact order: `言語知識・読解.html`, `解答.html` and `練習.html` (15:28:43) are newer than their Markdown, and the gate says 「built HTML matches the Markdown it stamps」. `聴解.mp3` (12:40:41) is newer than the script (12:40:02).

### `make check` lines naming 20260928_1 that are not OK

| line | resolution |
|---|---|
| FAIL: 詳細解説.json explains every keyed item (30/101) | Expected. Stage 5 has not run. |
| WARN: 聴解問題5 repeats a 20260917_1 headline (消費・経済, composed) | Draw audit only. Seed-shopping the listening half is forbidden, and round 1's reading stands. |
| note: two-back overlap スポーツ・余暇 is only on composed 聴解問題5 | Recorded, not budgeted. |
| WARN: 聴解 slot themes two back (5-1 スポーツ・余暇; 2-2 働き方) | Round 1 read both side by side (different errands, both lifted). The bytes are unchanged. |
| WARN: 問題1-4番 「、」 punctuation difference | False positive by the check's own statement: import transcript noise, and the audio is identical. |
| WARN: pools_sha (global) | A record, not a defect. This paper is stamped on a reroll. |
| skip: 問題7 form-family check (0 of 12 tagged) | This moved from round 1's "1/12" because を通して left. The skip is exactly why R2-F1 is invisible to the gate (RC-R2-1). |
| skip: errand keys, セクション構成表, 問題5 print shape, scaffold placeholders | Composed or pre-stage-5, by design. |

## 7. Skips

- **聴解 re-solve, and §4 checks 1–6:** not re-run. `聴解.md`, `聴解スクリプト.txt`, `聴解.mp3` and `聴解_チャプター.json` are byte-identical to what round 1 reviewed (same shas; mtimes 12:40, before round 1). The brief scoped this round to the repairs.
- **F3 ear-check:** not possible here (no audio playback, no ASR). It is open pending the user (§1).
- **RC-R2-1's full heading table:** I read Shin Kanzen 目次 pp.3–4 (1課–15課) as images. The remaining 目次 pages were not read, and the table must be completed before RC-R2-1 is committed.
- **Heading-level check of this paper's other 16 grammar draws against the last 10 papers:** not done. Only the rerolled item is in this round's scope, and round 1 folded the others against the last 4 entries. Under RC-R2-1's standard a full pass is owed before the next paper.
- **Edits:** none to `tests/`, `logs/` or any pipeline or skill file. The scratch files are `qa2-toc-*.png` and `qa2-check.txt` in the session scratchpad.
- **Final shas:** re-verified before writing, unchanged (`86e9ce94fbf3` / `7dc47ce36cd3` / `cb1695d9ea39`). The keyless render was built from the same shas.

QA: FAIL (3 findings, 0 automatic)

## Dispositions (orchestrator, 2026-09-28) — fixed directly, no further review

Under `jlpt-test-generation` §"The fix loop" (rule changed 2026-09-28 at the
user's direction: one full round, direct fixes, a scoped re-review at most once
— this round was that one), round 2's findings are closed without a round 3.

| finding | disposition |
|---|---|
| R2-F1 問題7-36 〜にあたって | **Rejected, with reason.** The written family rule (`exam-blueprint`: "one form spelled twice, not shares a stem") binds を通して/を通じて (F2, rerolled) and does not bind にあたって/に際して — two different forms under one Shin Kanzen heading, the same reasoning that kept 〜限り/〜ない限り in this paper. Whether a shared heading should bind across papers is RC-R2-1, left for the owner; item 36 stands. |
| R2-F2 問題12(B) foil final | **Fixed** by the 読解 author: 「本人が自分で選んで名札に書いた呼び方は、その日から、互いに口にする名前として使われていく。」 No foil and no named template. 12(A) was re-closed too (「…声をかける側が越える段差の高さそのものである。」, still `というより`), because with 問題9 measured properly, 12(A) and 問題9 shared the timed 〜ている skeleton. The reframe family is exactly 11(1) and 12(A). |
| R2-F3 stale scaffold comment | **Fixed**: deleted from `言語知識・読解.md` and the fragment, and removed at the source in `tools/scaffold_sections.py` so no future scaffold emits it. |
| F3 聴解問題2-2番 すくない/少なくない | **Open, pending the user's ear-check** (clip cut at the scratchpad `f3-clip.mp3`). No key depends on it. If the audio says 少なくない, the fix is at the bank source, followed by `make mp3 <id> REPLAY=1` for the three papers. That rewrites the 聴解 詳細解説 entries, so it does not block stage 5's 言語知識・読解 authoring. |
