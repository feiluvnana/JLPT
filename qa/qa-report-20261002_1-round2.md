# QA report — 20261002_1 (Stage 4, round 2: scoped re-review)

QA: FAIL (2 findings, 0 automatic)

Round-1 F14 is also still open. It is pending an ear-check, and the re-drawn 聴解 half still contains the clip. Neither round-2 finding changes a key or replaces an item. Under `jlpt-test-generation` §"The fix loop", both are fixed directly and get no further review.

- **Reviewed:** 2026-10-05 10:18, by a context that wrote nothing in this paper and did not run round 1.
- **Source revision.** These shas were the same at the start and before writing. The mtimes did not move.
  - `言語知識・読解.md` = `1b77661c9e98` (18:47:58)
  - `聴解.md` = `3eef7acf4224` (18:37:47)
  - `聴解スクリプト.txt` = `1997305f7a72` (18:37:47). This equals `聴解_チャプター.json` `script_sha`.
- **Solved from** `qa/20261002_1/keyless.md` (`make keyless 20261002_1`, 924 lines). Every scoped item and all 30 聴解 items were answered from that file before any key was opened.
- **Scope**, per `jlpt-test-generation` §"The fix loop":
  - 問題1-1, 問題4-20 and 問題6-29 (rerolled)
  - 問題8-44 (re-closed)
  - 問題10(5)/56, 問題11(1)/57–58 and 問題12(B)/65–66
  - the whole re-composed 聴解 half (seed 63138204)
  - each item's whole 大問 for interactions
  - a quick disposition check of round-1 F1–F14
- **Entry gate.** `make check` exits 2 with exactly one FAIL: `20261002_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)`. That FAIL belongs to stage 5 and is expected. This paper's WARNs are in §5.

## 1. Blind-solve diff

**Agreement: 9/9 on the scoped 言語知識・読解 items, and 30/30 on 聴解. There are no mismatches.**

| item | reviewer | key | |
|---|---|---|---|
| 1 | 4 | 4 | agree |
| 20 | 2 | 2 | agree |
| 29 | 3 | 3 | agree |
| 44 | 4 | 4 | agree |
| 56 | 1 | 1 | agree |
| 57 | 1 | 1 | agree |
| 58 | 2 | 2 | agree |
| 65 | 1 | 1 | agree |
| 66 | 4 | 4 | agree |

聴解, reviewer = key on every item:

| 大問 | keys |
|---|---|
| 問題1 | 3,1,2,1,2 |
| 問題2 | 2,1,3,3,4,1 |
| 問題3 | 1,1,3,3,2 |
| 問題4 | 1,3,2,3,3,1,2,2,1,1,3 |
| 問題5 | 3, 1, 4 |

**Blind strategy passes, re-run over all 18 items 52–69 because 56–58 and 65–66 changed.**

| measure | result | bar |
|---|---|---|
| Most bigrams shared with the item's own passage | 4/18 = 22% | ≤45% |
| Second-longest option | 5/18 = 28% | ≤45% |
| Uniquely longest key | 3/18 = 17% (52, 66, 69) | ≤30% |
| Worst per-item max/min ratio | 1.42 (66) | 1.65 |

Key lifts:

| key | longest shared run with its passage |
|---|---|
| 56 | 5 characters, 「画面の消え」 |
| 57 | 5 characters |
| 58 | 5 characters, 「冷たい所へ」 |
| 65 | 6 characters, 「、一つあたり」 |
| 66 | about 4 characters, 「多めに買」 |

No key is a lift.

## 2. Walkthrough (scoped items)

| 項目 | 鍵 | 判定 | 決め手／どこが問題か | どう直すか |
|---|---|---|---|---|
| 問題1-1 実績 | 4 じっせき | OK | 「この一年の**実績**が認められました」. The four options form a 2×2 {じっ/じつ}×{せき/ぜき}, and all are the target's word form. The band is Hajimete N2 2500 #1122, as stated in `qa/blueprint-rerolls-20261002_1.md` #1; that file's band line was read. The word occurs nowhere else in the paper. | — |
| 問題4-20 しつこい | 2 | OK | 「答えがわかるまで（　）質問してくる」. 1: いさぎよく is the opposite (giving up readily). 3: いさましく is courage, not repetition. 4: たくましく is sturdiness. Each one dies on meaning for its own reason, and the 解説 gives three separate reasons. The options split 3:1 on tone (three positive traits against one negative one). The stem is not a complaint frame, though, so valence alone does not pick the key (see §6). Band: official 12/2023 L24 prints しつこい as an option. | — |
| 問題6-29 身につく | 3 | OK | 「毎日少しずつ練習を続けたら、ピアノの基本が**身についた**」. 1: 疲れがたまる. 2: ソースがつく. 4: 心にしみる. None of the three is an attested collocation of 身につく. Band: Soumatome L2920. | — |
| 問題8-44 | 4 | 要修正 (解説) | **Ordering.** The keyed order is 駅前の→図書館の→開館に→先立って, with ★ on 開館に.<br>**Rivals.**<br>• 開館に must be immediately followed by 先立って, the only に-complement.<br>• A の-card cannot stand last before 「、市は」.<br>• 図書館の→駅前の→開館に is nonsense, and in any case leaves ★ on 4.<br>• Fronting 先立って (read as 先だって) clashes with 来月.<br>So the item is sound and F9 is closed.<br>**The 解説 contains a false "only" claim (R2-F2).** | R2-F2 |
| 問題10-56 | 1 | OK | 「三つがそろうのを待って、まとめて送る」 and 「充電器と家の無線の両方につながったまま画面の消えている時間が来るまで、写真は電話の中で順番を待っている」.<br>• 2: the battery is not mentioned.<br>• 3: denied by 「電源につながれ」.<br>• 4: denied by 「画面が使われていない」 and 「その場では送らず」. | — |
| 問題11-57 | 1 | OK | 「溶けた所はさらに熱を受け取り、そのすぐ隣の凍った所はなかなか溶けないので、温まり方のむら…は、時間とともに大きくなります」.<br>• 2 is the reverse of 「表面から数センチほどの深さまで」.<br>• 3 (cold air) and 4 (strong ovens) are not stated. | — |
| 問題11-58 | 2 | OK | 「溶けた所から凍った所へ、熱が伝わる間をつくるため」 and 「熱くなった所の熱を、冷たい所へ分ける時間をとること」.<br>• 1 is denied by the 「かき混ぜてください」 line.<br>• 3 is not stated.<br>• 4 is the reverse of 「弱い出力で時間をかける」. | — |
| 問題12-65 | 1 | OK, with a prose defect in B | A says 「一個あたり二割ほど安い」. B says 「一つあたりの値段は、たしかに安くなります」.<br>• 2 is in A only.<br>• 3 is in neither.<br>• 4 is in B only. | R2-F1 |
| 問題12-66 | 4 | OK | A: 「毎日決まった量を使う物は、一度に多めに買っておくのが…賢いやり方」. B: 「何か月分ものお金を今日まとめて払う、という条件」.<br>• 1: A dismisses the space problem (「半年もすれば、棚はまた空いてくる」).<br>• 2: this is A only.<br>• 3: A excludes food (「食品と違って」), and B does not tell anyone to stop. | — |

**聴解 (all 30, composed).** Each key was proved from the script's deciding line, and every printed 問題1/2 option was traced to a script line.

- **1-2 option 4 「大学に行く」** is never spoken. I opened 『完全模試』 問題冊子 p.33 (pypdf slice, rendered at 110 dpi). The book prints exactly 1 電車に乗る／2 きっさ店に戻る／3 電話をする／4 大学に行く. The transcription is faithful. This is a publisher distractor, not an OCR loss.
- **1-1 is now 2022-12:問題1-1** (tennis camp, the man phones the pension). It is unambiguous: 「ペンションにも、到着時間の変更を伝えてあるよね？」「そうでした、すみません」.

## 3. Interaction re-read (each scoped item's 大問 or column)

- **問題1, 問題4, 問題6.**
  - No option repeats inside a 大問. The gate line `no word appears twice in one 大問's options` is ok.
  - 実績, しつこい and 身につく occur nowhere else in the paper or the 聴解 script.
  - 問題4 keys are 3,2,3,3,1,1,2. 問題6 keys are 1,2,1,3,4.
  - The spec, the ledger and `rotation.reroll_log` agree field for field: three reroll-one entries, and the seed string is `15443619+reroll-one(…)×3`.
  - None of the three new words appears in any earlier generated paper.
- **問題8.**
  - に先立って is keyed only at 44.
  - In the previous two papers it was only a 問題7 distractor (20260929_1 #37, 20260928_2 #34), never a key.
  - No card repeats across 43–47.
- **Keyed-form re-grep over 問題10–14 prose and （注N） lines, after the re-authoring.** All 20 forms keyed in 問題7/8/9 occur **0** times:
  - ところだった, っぱなし, ざるを得ない, といっても, 申し上げる, ことなく, ものがある, と言っても過言ではない
  - といい, はさておき, にわたって, にしたがって, のみならず, に先立って, にしては, ことから
  - どころか, ものだ, ところが, 目を通す
- **問題10 column.**
  - The stems are spread out: 伝えたいこと, なぜか, 考えに合う, 問い合わせ, どのように考えているか. Two are 考え stems, so the ≥2 rule holds.
  - 10(5) is now a 反論への応答 MOVE, and the objection 「この機能はあてにならない」 is conceded (「たしかに…ことがある」) and answered on its own terms, so it is not a strawman.
  - Closing 条件提示, skeleton 〈条件〉が来るまで…待っている. This differs from 13's 〜ている〈集団〉では…受け取られる.
- **問題11 column.**
  - 11(1) puts the 事実 item first (57 なぜか) and the 考え item second (58). Across 問題11 there are two 考え stems (58, 62) plus 64's 説明.
  - The new passage is です・ます and is not a measurement or protocol subject, so F3 is closed.
  - The closing is the paper's one cleft (「大切なのは、…ことです」), and no other final is a cleft.
- **Closing column, 13 finals** (read off the passages and checked against `logs/topics.json` `closing_moves`):

  | shape | surfaces |
  |---|---|
  | 随筆 | 2 (9, 11(2)) |
  | 意外な観察 | 2 (10(2), 11(4)) |
  | 主張 | 2 (10(3), 12A) |
  | 条件提示 | 2 (10(5), 13) |
  | 説明 | 2 (11(1), 12B) |
  | 反論応答 | 1 (11(3)) |
  | 実用文 | 10(1), 10(4) |

  Every shape is ≤2.
- **MOVE column, per `qa/dokkai-allocation-20261002_1.md`.** 機構の説明 3 (11(1), 11(4), 13) and 反論への応答 3 (10(5), 11(3), 12), both at the cap and not over it. 11(1) is not 〈想定→実は〉 in disguise: delete-the-denial test, nothing is denied.
- **問題12.**
  - B no longer touches storage or visibility. It is a prepayment and cash-flow objection, so F4 is closed, including the 10(3) crowding.
  - A and B are read as one 反論への応答 pair. B's final skeleton 〈X〉は…という仕組みの上に成り立っている is unique in the column.
- **Provenance scan, 14-character shared runs.** I scanned 10(5), 11(1), 12(B) and the 44 sentence against all 31 `refs/JLPT_N2_NEW/*/booklet.md`, every `tests/*` paper and `refs/Shinkanzen/dokkai_reference.md`.
  - The only hit is 12(B)'s 「月末にお金が足りなくなりやすい」, which matches 20260928_1 問題10(5) option 3.
  - That paper is three back and outside the two-paper window. Not filed (§6).
- **Topic.**
  - No previous paper treats microwave heating or uneven heating, automatic photo backup, or bulk-buy prepayment. The searches covered 電子レンジ, 解凍, 冷凍食品, まとめ買い and 無線: 20260812_2 has まとめ買い only as a food-loss aside, and 20260928_2 has 無線 only as a fire-dispatch radio.
  - Headline set {メディア・情報, 消費・経済, 人間関係, 防災} plus composed 聴解問題5 {働き方, 睡眠・健康}. Against 20260929_1, the authored slots repeat nothing; the two composed slots repeat (WARN, draw audit, §5). Against 20260928_2, nothing repeats.

## 4. Composed 聴解: checks 1–6, re-run in full (the half was re-composed)

1. **Draw** (`logs/choukai_draws.json`, seed 63138204).
   - 0 of 29 slots repeat 20260929_1 in place.
   - No slot-free textbook clip repeats any of 20260929_1's, in any slot.
   - `kanzenmoshi:cd1-04` is refused in `textbook_items.json` with the F1 reason, and it appears 0 times in `logs/choukai_bank.json`.
   - Two papers back (allowed and recorded): `soumatome:cd1-44` (1-4), `soumatome:cd2-47` (4-1) and `shinkanzen:cd2-66` (4-2) are the same recordings as 20260928_2's. The `topics.json` surfaces note it.
2. **Round-trip.** `python3 tools/choukai_segment.py tests/20261002_1/聴解.mp3` prints `ok 46.1 min LUFS -15.90 問題1:5 問題2:6 問題3:5 問題4:11 問題5:2`. The chapters are `source: composed`. The MP3 is 2 s older than the script, but both come from the same composer run, and the gate prints `聴解.mp3 was built from today's 聴解スクリプト.txt (script_sha 1997305f7a72)`.
3. **Ear spot-check.** Skipped: there is no playback in this environment (§7).
4. **Bank keys.** All 30 blind answers equal the keys. No bank mis-key.
5. **Key balance against the 31-sitting archive band.**

   | 大問 | keys | mode | band |
   |---|---|---|---|
   | 問題1 | 3,1,2,1,2 | 2 | 2–4 ✓ |
   | 問題2 | 2,1,3,3,4,1 | 2 | 2–4 ✓ |
   | 問題3 | 1,1,3,3,2 | 2 | 2–4 ✓ |
   | 問題4 | 1,3,2,3,3,1,2,2,1,1,3 | 4 | 4–7 ✓ |
   | 問題5 | 3,1,4 | 1 | 1–3 ✓ |

6. **I read all 29 clips and the 5 preambles plus the opening as Japanese.**
   - For each 問題1/2 item, I traced the key through the lines before the deciding one. No line contradicts its own speaker's conclusion.
   - Lines carried as official or source ink, not filed:
     - 2-3 「りーさん」 (official 7/2021, already recorded in round 1)
     - 2-4's mixed 「⋯」/「…」 (cosmetic)
     - 2-2's 引越し/引っ越し (cosmetic)
   - **1-3 「書いていておいて」 is still drawn** (2022-12:問題1-3). Round-1 F14 therefore still binds this paper (§7).
   - The opening reads 「N2聴解。これから、N2の聴解試験を始めます。」. The NEW-1 typo is absent.

## 5. `make check` WARNs naming this paper

| WARN | resolution |
|---|---|
| 聴解問題5 repeats 20260929_1 headline themes ['働き方','睡眠・健康'] | **Composed draw audit.** No repair exists short of seed-shopping, which is forbidden. 5-1 is a restaurant award-ceremony attendance item and 5-2 is a health-event floor plan. No number or condition crosses into 20260929_1's 働き方 問題9 or its 睡眠・健康 問題12, and the authored half repeats nothing. |
| drill/N2 pages older than their data | Global gitignored build output. It names no defect of this paper. |

The other global WARNs belong to other papers and name no item here.

Gate observation: `読解 lexical load` prints novel 16.1% against the author target ≤15.8%. That is under `NOVEL_SHARE_WARN` 16.8, so it prints ok (§6).

## 6. Findings

### R2-F1 — 問題12(B): 「一つあたりで見れば二百円ほど得をしています」 states a per-unit gain that the numbers deny (要修正; key unchanged)

- **Evidence.** 「四個入りなら四百円のところを、十二個入りで千円払うとします。一つあたりで見れば二百円ほど得をしています」.
  - Per unit, the price falls from 100 to about 83 yen, a saving of about 17 yen.
  - 200 yen is the TOTAL saving against three 4-packs (1200 → 1000).
  - 「一つあたり…二百円」 reads as 200 yen a piece, which is impossible when a piece costs 100 yen. A careful reader stalls on B's central example.
  - This is the self-reconciliation failure (mode 1): the number was not re-derived after the re-angle. 65 and 66 do not depend on the figure.
- **Fix.** Replace the clause with 「同じ十二個を四個入りでそろえるより二百円ほど安く済みますが、その日の支払額は六百円多くなります」.
  - It keeps 「一つあたりの値段は、たしかに安くなります」 in ¶1, so 65's common point is untouched.
  - It does not borrow A's wording 「四個入りを三つ買うのに比べて」.
  - Re-check that 65 and 66 still hold. Re-sync the 65/66 解説 cells if they quote the line (they do not today). Carry the change into 詳細解説 at stage 5, including the VI `passage_translation`.
- **Owner.** question-authoring/dokkai.
- **Root cause.** RULE-IGNORED (exam-qa-review step 1, self-reconciliation). Process failure, no skill edit.

### R2-F2 — 問題8-44 解説: 「四枚のうち名詞で始まるカードは『図書館の』と『開館に』の二枚である」 is false (要修正; key unchanged)

- **Evidence.**
  - 「駅前の」 also begins with a noun (駅前). The true count is three cards.
  - The 解説's conclusion survives, because it goes on to reject 「図書館の駅前の開館に」 on meaning. But the stated ground is false.
  - This is exactly the claim shape `exam-qa-review` §3 says to verify by writing the four cards in a column (`qa-report-20260914_1` F5). The next fix pass would reason from it.
- **Fix.** Change the sentence to 「四枚のうち名詞で始まり『の』の係り先になれるのは『駅前の』『図書館の』『開館に』の三枚で、『駅前の』と『図書館の』はどちらも直後に名詞が要るので、」 and keep the existing 図書館の駅前の rejection that follows. Carry the change into 詳細解説 at stage 5.
- **Owner.** question-authoring/bunpou.
- **Root cause.** RULE-IGNORED. The rule exists in `exam-qa-review` §3 and in `bunpou.md`'s final-slot proof, and the re-close did not re-verify the card tally.

### Carried, not new

- **F14** (round 1), 1-3 「書いていておいて」: still open pending an ear-check.
  - The re-draw kept `2022-12:問題1-3`, so the holder list is 20261002_1 (and imported-n2-2022-12).
  - Offset: 問題1 3番 starts at 369.29 s in `tests/20261002_1/聴解.mp3`, and the line is about 70–90 s into the item (about 440–460 s).
  - Repair route as in round 1.
- **Pool follow-up for F5–F7, blocked.** `pools.json` still holds 中級(ちゅうきゅう) ×1, 切実 ×2 (`usage` and `context_words`) and connective ただ, and 上級 sits beside 中級.
  - The paper is repaired. But this open RULE-UNENFORCEABLE row **blocks the next `make sample`** until the owner deletes or retires these entries (`exam-qa-review` §6.5). See `qa/blueprint-rerolls-20261002_1.md` §"Pool follow-up".

### Looked at, not filed (with reasons)

- **20 option tone.** The options split 3:1 on valence, but the stem carries no complaint frame, each distractor is killed by a different meaning, and the gate's one-clause check is ok. This is not the `20260904_1` F1 shape.
- **（注N） count is exactly 25,** the floor. The gloss rule did not fire on any 11(1) gloss: 揺り動かす, こすれ合う, むら, 芯 (1 sitting), 解凍 and 出力 are each 0–1 sittings in the archive. One weakness: 「こすれ合う：…触れ合って、こする」 defines the word by its own stem. If 11(1) is touched again, use a non-circular definition such as 「表面どうしが触れたまま、何度も行ったり来たりする」.
- **11(2) （注4）霧** is a borderline gloss. It has 0 archive occurrences, so the official-unglossed rule cannot fire. Not in scope for this round.
- **Lexical load novel 16.1%** is over the 15.8 author target and under the 16.8 WARN line. A dense 11(1) is plausible as the cause. No action required.
- **12(B) 「月末にお金が足りなくなりやすい」** matches 20260928_1 問題10(5) option 3, and the advice is similar (check the month's other payments before spending). That paper is three back, outside the two-paper window, and the decisive claim differs (prepayment against payday planning).
- **`logs/topics.json` 問題14 `surfaces`** still says 「前の週の金曜日までに電話申し込み」, a string F12 removed from the flyer. This QA was told another agent is editing that file concurrently, so I did not edit it. It is flagged here so that the updater re-greps per `jlpt-test-generation` §"Closing a finding includes re-grepping its notes".

## 7. Round-1 dispositions, quick on-disk check

| F | holds? | evidence |
|---|---|---|
| F1 | yes | `kanzenmoshi:cd1-04` is refused with its reason, absent from the bank, and the half was re-composed (seed 63138204). The new 1-1 is unambiguous. |
| F2 | yes | けやき通り児童館 (no other paper uses it), 来月10日から, the new title, and 52 option 1 no longer opens with a month. |
| F3 | yes | 11(1) is replaced with a microwave-heating mechanism, not a measurement protocol. |
| F4 | yes | B is re-angled to prepayment, off storage and visibility. |
| F5–F7 | yes (paper) | The rerolls are in the spec, the ledger and reroll_log. Pool retirement is blocked (§6). |
| F8 | yes | 63-4 reads 「受け止める働き方は、使うエネルギーが少ないから」. |
| F9 | yes | The post-blank now starts with 「、市は…」, and every ordering was re-checked. The 解説 carries R2-F2. |
| F10 | yes | 10(3) 「けれども、」 and 10(2) 「…と聞く質問だった。」. The keyed-form re-grep finds 0 hits. |
| F11 | yes | The 畳 and ブレーキ glosses are gone, and 25 in-body markers remain. |
| F12 | yes (paper) | 「受付日の2日前の金曜日（6月7日の分は6月5日、6月21日の分は6月19日）」, with the 71 解説 synced. The `topics.json` note is stale (§6). |
| F13 | yes | 「案内台まで来て番号を見せることになる」. |
| F14 | open | Pending an ear-check; the clip is still drawn. |

## 8. Skips

- **聴解 check 3 (two-item ear spot-check) and F14's ear-check were not run.** This environment has no audio playback. The offset is recorded above for the user.
- **Not a full re-pass.** Items outside the scope were not re-solved, per §"The fix loop". The only exceptions are the 読解 strategy passes, re-run over all 18 items because five of them changed, and the 13-final closing column.
- **No root-cause rows were opened.** Both findings are RULE-IGNORED.
- **No edits.** Only this report was written, with scratch files under `qa2-*` in the session scratchpad.

## Dispositions (orchestrator, 2026-10-03) — fixed directly, no further review (the scoped re-review runs at most once)

| finding | disposition |
|---|---|
| R2-F1 12(B) 「一つあたりで…二百円」 | **Fixed** by the 読解 author with the proposed sentence; every number in 12(A)/(B) re-derived; keys unchanged. |
| R2-F2 8-44 解説 card count | **Fixed** by the 文法 author (three noun-initial cards); verify-scramble clean, key/★ unchanged. |
| stage-3 R-1 〈想定→実は〉 at 3 (聴解3-2番 counted as round 1 counted 2-3番) | **Fixed**: 10(3) re-angled to 一人称の前後比較 (subject and 54's key/options unchanged; 解説 rewritten); paper now at 2 = cap. |
| (looked-at) こすれ合う circular gloss | **Fixed**: 「触れている物どうしが、押し合いながら動く」. |
| (looked-at) topics.json 問題14 stale deadline | **Fixed** by the stage-3 finish pass; 10(3) surface/claim/notes re-recorded after the re-angle. |
