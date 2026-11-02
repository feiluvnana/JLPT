# QA report — 20261102_1 (Stage 4, round 2, SCOPED)

QA: PASS on the scoped items (0 automatic; 2 要修正 findings, both bookkeeping/解説 wording, no key or option change)

- Reviewed 2026-11-02 12:48–12:54 JST by a context that authored nothing in this paper and did not run round 1.
- Scope, per `jlpt-test-generation` §"The fix loop" (one scoped re-review, at most once): 問題1-5 (F1 reroll), 問題13-67 (F2), 問題13 glosses (F3), 問題11(1) (F4) and the columns they sit in. Nothing else was re-passed.
- Source revision (sha1[:12]); identical at start, before writing, and after the keyless rebuild:
  - `言語知識・読解.md` = `24294f7546c2` (mtime 12:47:38; round 1 read `2fafe9e2d989`)
  - `聴解.md` = `215002704be0` (unchanged since round 1)
  - `聴解スクリプト.txt` = `a59eb1a6cedb` (moved from round 1's `a2b4a179d009`: the F5–F7 bank replays; out of this scope)
  - `qa/dokkai-allocation-20261102_1.md` = `a8e4901ff8a5`
  - Repo HEAD `e6e7bf0`.
- Solved from `qa/20261102_1/keyless.md` (`make keyless 20261102_1`, 923 lines). The scoped items were answered from that file before any key, 解説, reroll record or allocation row was opened.
- `make check`: exit 2 with exactly one FAIL, `20261102_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)`, the expected stage-5 FAIL. This paper's WARNs: 問題8 family-tag coverage, 聴解3-1番 交通 slot theme, 2-3番 「、」 placement (all round-1 dispositions, unchanged), and `drill/N2` pages older than this paper's Markdown (build output, rebuilt by `make drill`/`make pages`; not a paper defect). Relevant ok lines: `every 問題1 option carries the printed okurigana`, `（注N） markers and definitions pair 1-to-1`, `numbered in reading order`, `0 orphan(s)`, `読解 has substantial （注N） glosses (… got 26)`, `option length ratios within 1.65`, `key rank dominant share 40%`, `no 問題7/8/9 keyed form … in the 問題10-14 prose`, `no more than 2 読解 passages close on one sentence template`.

## 1. Blind-solve diff (scoped items)

| item | blind | key | |
|---|---|---|---|
| 問題1-5 末っ子 | 4 | 4 | agree |
| 問題11-57 | 2 | 2 | agree |
| 問題11-58 | 2 | 2 | agree |
| 問題13-67 | 3 | 3 | agree |
| 問題13-68 | 4 | 4 | agree |
| 問題13-69 | 1 | 1 | agree |

6/6, no mismatch.

## 2. Per-item walkthrough (scope only)

| 項目 | 鍵 | 判定 | どこが問題か / deciding quote | どう直すか |
|---|---|---|---|---|
| 問題1-5 末っ子 | 4 | OK | 「私の父は**末っ子**として育ちました。」 1 ひとりっこ 2 あまえっこ 3 うれっこ 4 すえっこ. Band evidence found (see §3) | — |
| 問題1 column (1–5) | 3,4,2,3,4 | OK | 物音/礼儀/恐怖/接触/末っ子; no option string shared across items; 訓 = 物音, 末っ子 (2 of 5) | — |
| 問題11-57 | 2 | OK | 「部屋の隅までは照らせません。炎は大きいのですが、ゆらゆらと揺れて、光が一定しないのです」; 1 dies on 「ろうも垂れにくい」, 3 on 「すすも少ししか出ません」, 4 on 「炎は大きい」 | — |
| 問題11-58 | 2 | 要修正 (解説 only) | Key: 「「暗い」という言い方は、ろうそくを部屋の明かりとして使うことを前提にしています」. **R2-F2** on option 4's kill clause | §4 R2-F2 |
| 問題13-67 | 3 | OK | 「五つ目の玉ねぎを刻み終えたとき、ふと気がついた。その日はまだ、一度も顔を洗いに行っていない」 + 「顔を洗いに立つことがなくなった」 | — |
| 問題13-68 | 4 | OK | 「よく切れる刃は、部屋をつぶさずに分けていくので、こわれる部屋が少なく、目にしみるものもあまり出てこない」 | — |
| 問題13-69 | 1 | OK | 「やはり涙はほとんど出なかった」 + the teacher's explanation; 4 dies on 「涙の量はあまり変わらなかった」 | — |
| 問題13 glosses | — | OK | 注1 作り置き … 注6 すっと; all six markers in the body, in reading order | — |
| 問題11(1) passage | — | 要修正 (bookkeeping) | Passage sound; the allocation file is stale. **R2-F1** | §4 R2-F1 |

## 3. Scoped checks

### 3.1 問題1-5 (F1 reroll: 蒸し暑い → 末っ子, key 4)

- **Draw.** `test_spec.json` and `logs/ledger.json` both record `reroll-one kanji_reading:4`, seed 85970684, out 蒸し暑い, in 末っ子. The ledger has 末っ子 only in this entry (2 hits: items list and reroll `in`), so there is no cooldown repeat. The pool entry exists (`pools.json` L205, between 末(すえ) and 粉末). `answer_positions` 問題1[4] = 4 is kept.
- **Round-1 F1 wildcard predicate** (each kanji run replaced by `.+`): `末っ子` → `^.+っ.+$`. ひとりっこ, あまえっこ, うれっこ and すえっこ all match (4/4). With the kanji covered, 「□っ□」 fits every option, so the okurigana does not select the key. The gate's tail check is also ok.
- **moji-goi Part 1.**
  - Whole word underlined: yes, `**末っ子**`.
  - 訓 band: 物音 and 末っ子 are 訓, so 2 of 5 (KUN_FLOOR = KUN_CAP = 2).
  - Reading trap: っ is in the key but shared by all four options. That is legitimate; the trap stratification is a corpus statistic, not a per-item requirement.
  - Two-branch rule: branch (a) is empty (末 = マツ/バツ/すえ; look-alikes 未/本 give no 〜っこ word), so the set uses branch (b). The written label is `field=人の呼び名（〜っ子）`, and all four options sit inside it without a qualifying clause: one-child, a clingy child, a popular person, the youngest child.
  - Every option is a real 和語 noun, so the 訓 set contains no non-word.
  - Second reading: まっし belongs to the spelling 末子 and is correctly kept out.
  - The stem 「として育ちました」 accepts all four, so meaning cannot narrow the choice. The item tests 末 = すえ only.
- **Band evidence (round-1 debt): CLEARED.** The OCR extract `refs/Shinkanzen/kanji_tables.md` L3883–3888 renders the entry as garbage (「末 / 宵柴 / マツ / 業業っ / すえ」), so I opened the page instead. I rendered `refs/Shinkanzen/Shin_Kanzen_Masuta_N2-Kanji.pdf` PDF p.174 (printed p.41, 別冊1 学習漢字リスト) with `pdftoppm -r 150`. Entry **518 末** prints: マツ 「月末（げつまつ）」; すえ 「末（すえ）　末っ子（すえっこ）」. 末っ子 is a printed headword example under 末's すえ reading in the N2 kanji book. Key band: N2 (Shin Kanzen N2 漢字, 別冊1 #518, printed p.41).
  - The author's 解説 line (L514) still says 「帯の証拠は未済の債務」. That sentence should now cite this page. It is folded into R2-F1's bookkeeping fix.
  - Distractor band, noted but not filed: 甘えっ子 and 売れっ子 have 0 hits in any extract. The author recorded them as 常用音訓 debts, which moji-goi's RESOLVE procedure step 4 permits for a miss. They are ordinary real words, and a distractor's band is not an automatic-fail axis.
- **Column read.** No option string recurs across 問題1-1…5. 末 appears elsewhere only as kanji: 問題7-32 option 「末に」 and 「週末」 in 問題13. Neither prints the reading すえ in kana, so there is no leak.

### 3.2 問題13-67 (F2: key wording)

- Options measure 30/32/25/27 printed chars (29/31/24/26 JP), ratio 1.28, inside 1.65. The key is now the uniquely shortest option. The gate's rank spread check is ok (dominant rank 40% ≤ 45%).
- Longest run each option shares with the passage: 1 「包丁で玉ねぎを刻」 (8), 2 「玉ねぎの」 (4), 3 (key) 「、顔を洗いに立」 (7), 4 「窓を開け」 (4). The key does not out-overlap the distractors.
- Grounding: 「何個も刻んだのに」 ← 「五つ目の玉ねぎを刻み終えたとき」; 「顔を洗いに立たずに済んでいた」 ← 「一度も顔を洗いに行っていない」 and 「顔を洗いに立つことがなくなった」. Every content word is now in the source. Round-1's 目 vs 顔 contradiction is gone.
- Distractors are still wrong:
  - 1: 切り口 after sharpening is never described (切り口 appears only in the dull-knife mechanism).
  - 2: dies on 「次の週も、同じ店で同じ玉ねぎを買ってきて」.
  - 4: dies on 「窓を開けたり…涙の量はあまり変わらなかった」.
- 解説 (L584): every quote is verbatim in the passage, and each distractor is killed by a named fact. Confirmed.

### 3.3 問題13 glosses (F3)

- Body markers, in reading order: 作り置き（注1）, みじん切り（注2）, 研ぐ（注3）, 砥石（注4）, 細胞（注5）, すっと（注6). The definition lines are 注1–注6 with the same headwords, 1-to-1. ちくちくする and 目にしみる now print bare. The old 注5/注6 definition lines are gone, and nothing in the file mentions 注7/注8.
- Definitions:
  - 細胞 「生き物の体を作っている、とても小さな単位」: accurate, not circular. 細胞 is not in any of the three vocabulary extracts. Official prints it bare once, in a 問題8 stem (12/2022 #46), but the 「official uses it unglossed」 test is refuted (`dokkai.md` §（注N） refuted check), and the official-option test does not apply because it is not a 問題3–5 option. Kept.
  - すっと 「引っかかることなく、なめらかに」: accurate for 「刃が…すっと入る」. Kept.
- No definition shares a 4+ char run with the key of an item whose stem names it (gate ok). The paper total is 26 in-body markers, gate ok, with no padding added.

### 3.4 問題11(1) (F4: last paragraph deleted)

- **Re-read.** The passage now ends: 「明かりとして比べられれば、和ろうそくは洋ろうそくにかないません。けれども、それは、和ろうそくが長く求められてきた役目とは別の物差し（注5）です。」 It closes cleanly. です・ます throughout, and （注5）物差し still sits in the body. No orphan.
- **Allocation row** (L53: 反論への応答, resolution 「反論の前提を問い直す」, 職人, です・ます). Matches:
  - the objection is conceded on its own measure (「たしかに…部屋の隅までは照らせません」, the author's own 停電 night);
  - its premise is named (「「暗い」という言い方は…前提にしています」);
  - nothing is kept against a cost, no exception channel is opened, and there is no 「もっとも」 knock-down.
- **〈想定→実は〉 deletion test.** There is no denial sentence (no ところが/しかし/ではなかった/実は). Delete the premise sentence and the passage still makes its point through the usage report and the final, and it never collapses into "X was wrong, actually Y". The customer's 暗い is conceded twice, never denied. **Not the skeleton.** The paper stays at 1 (10(1)).
- **Against 20261008_1 11(4)'s closing.** Its last two sentences are 「ですから、…と聞かれたときには、…説明し、…見ていただくようにしています。」 and 「棚のパンには、…てから一時間の休みを取らせ、それから袋に入れています。」 (a 〜ています practice sequence). 11(1)'s last two are a 〜れば concession plus a けれども reframe of the measure. No practice, no sequence adverb, no 〜ています, so the beat round 1 named is gone. Same 大問 and the same persona archetype (職人/店主), but the skeleton is different.
- **問題11 column.**
  - (1) concession + reframe;
  - (2) mechanism consequence 「…同じようには頭を守れない。」;
  - (3) 「…言ってくれれば、…まず要らなくなる。」 (条件提示);
  - (4) 「寝る時刻は、前とほとんど同じである。…もう半分は起きている。」
  - Four different finals. 11(1)'s penultimate and 11(3)'s final are both 〜ば clauses, but only finals are read for templates, and 11(1)'s final is not conditional. Noted, not filed.
- **Templates.** The new final matches no `FINAL_SENTENCE_TEMPLATES` row (no ではなく, よりも…ほう, だけでは/こそ, というより, わけではない, 相関, cleft, ていたのだ, ていない) (gate ok).
  - **Not-A-but-B family, hand read.** `dokkai.md` says 「ANY final that names a foil and prefers the alternative is a member」. This final names a foil (being compared 「明かりとして」) and sets it aside as 「別の物差し」 against 「長く求められてきた役目」. I read it as a member.
  - The family therefore counts **2** (12(A) 「運転の荒さだけで起きるわけではない」, 11(1)). The rule rejects 3, so it complies. The allocation planned "exactly 1, at 12(A)", so the tally is stale (R2-F1).
  - The gate prints `0 of 13 surfaces` close on the family. It misses 12(A)'s わけではない too (RC-R2-1).
- **Shared-MOVE pair** 11(1) / 12: the resolutions are now 「反論の前提を問い直す」 against 「譲歩して一部を変える」, and the personas are 職人 against 論者/利用者. Different on both, compliant.
- **Item 57/58 re-solve:** §1; both agree. **58's revised 解説** (L575): every quote is verbatim in the passage, and the dropped 「筆者は使い道を聞いている」 clause is gone. Option 4's kill is R2-F2.

## 4. Findings

### R2-F1: allocation file and 解説 band note left stale by the F1/F4 repairs (要修正, bookkeeping; owner: 読解 author for the allocation, 文字・語彙 author for L514)

- **Evidence.**
  - `qa/dokkai-allocation-20261102_1.md` L444 still reads 「反論: 11(1) 「理由を示して変えない」 (職人) against 12 「譲歩して一部を変える」」. The 11(1) row (L53) says the resolution is now 「反論の前提を問い直す」. The fix loop requires that "a re-allocation edits the allocation row AND re-derives that file's per-slot table and tallies" (qa-report-20260928_2-round2 R2-F2).
  - The same file's "not-A-but-B reframe family … Exactly **1**, at 12(A)" (L423–425) and 11(1)'s template cell 「Unnamed」 (L53) do not reflect the new final, which names a foil (§3.4).
  - `言語知識・読解.md` L514 (問題1-5 解説) ends 「帯: 抽出…に見出し語の行は見つからない…（帯の証拠は未済の債務）」, which the book page now settles.
- **Fix (replacement text).**
  - L444 → 「反論: 11(1) 「反論の前提を問い直す」 (職人) against 12 「譲歩して一部を変える」 (論者 / 利用者).」
  - L423–425 → 「… Exactly **2**: 12(A) (`A わけではない`, foil 運転の荒さ) and 11(1) (unnamed template; foil 「明かりとして比べる」物差し, after QA F4). At the cap; a third is a rewrite.」
  - L53 template cell → prefix 「Unnamed; not-A-but-B family member (foil: 明かりとして比べる物差し), QA round 2.」
  - L514, replace the band sentence with 「帯: 新完全マスター漢字N2 別冊1 学習漢字リスト 518「末」すえ 「末（すえ）　末っ子（すえっこ）」（印刷 p.41／PDF p.174、ページを開いて確認）。」 Then re-run `make booklet`/`make sheet` (no autofix).

### R2-F2: 問題11-58 option 4's 解説 kills it on the weaker clause (要修正, 解説 wording only; owner: 読解 author)

- **Evidence.** Option 4 is 「暗く感じるのは使い方が古いためで、客の側が改めるべきだ」. The 解説 says only 「4の、客が改めるべきだということは述べていない」. After F4 the passage ends on 「…とは別の物差しです」. A hostile reader could argue that this final implies the customer's yardstick is the wrong one, which is a soft cousin of 「客の側が改めるべき」. The clean, string-checkable death is the first clause: nothing in the passage says the usage is 古い. The author concedes the darkness and reports different uses. The author does not call room lighting an old way of using candles.
- **Fix.** Replace the option-4 sentence of the 解説 (L575) with 「4の「使い方が古い」ということは述べておらず、筆者は暗さを認めたうえで、使う場が違えば問われることも違うと述べているだけで、客に改めるよう求めてはいない。」 The key and options are unchanged. Carry the same wording into `詳細解説.json` at stage 5.

## 5. Root-cause rows

| RC | finding | code | papers showing the class | owner | proposed edit |
|---|---|---|---|---|---|
| RC-R2-1 | §3.4 family count | GATE-BLIND (`REFRAME_CLOSING` lacks わけではない and というより, which `dokkai.md` lists as family members) | 20261102_1 12(A) (gate prints 0 of 13 while the allocation itself names it), plus 20260807_1, 20260813_1, 20260817_2 and 20260821_1, whose わけではない finals are recorded in the `FINAL_SENTENCE_TEMPLATES` comment (L2758–2761). 2+ papers, so systemic | `tools/check_consistency.py` `check_dokkai_closing_reframe`, final-2-sentence mode | Count a final as a family member when it matches any not-A-but-B row of `FINAL_SENTENCE_TEMPLATES` (`(では\|じゃ)なく`, `より(も\|は)?…(ほう\|方)`, `だけで(は\|も)?(ない\|なく)\|こそが?`, `というより`, `わけでは(ない\|ありません)`) **or** `REFRAME_CLOSING`. Keep the cap at 2. Before committing, run it on 20261102_1 (it must print ≥1, for 12(A)) and over every paper on disk, and list the ids that move. The unmarked member (11(1)'s 「別の物差し」) stays a hand read, as `dokkai.md` already says |
| RC-R2-2 | R2-F1 | RULE-IGNORED | 1 here; the class is qa-report-20260928_2-round2 R2-F2's | `jlpt-test-generation` §"The fix loop" (already says to re-derive tallies) | Process failure. No edit |

## 6. Coverage

- Step 0: scoped blind solve from `keyless.md` (§1).
- Steps 1–2b: 問題1-5, 57, 58, 67, 68 and 69: key proof plus every distractor's death (§2, §3).
- Step 2.5: 末っ子's band, from the book page itself (§3.1).
- Step 3: 問題1 okurigana skeleton; 問題13 gloss pairing and numbering; 67's lengths and overlap. The keyed-form re-grep is covered by the gate line (`no 問題7/8/9 keyed form … in the 問題10-14 prose`), re-run on this revision after the F3/F4 prose edits.
- Step 5, landing site of F4: MOVE and deletion test, allocation row, previous paper's same-大問 last two sentences (RC-3's proposed bar), 問題11 column, template column, not-A-but-B family, and shared-MOVE pair (§3.4).
- Step 6: reroll provenance; spec = ledger for the F1 draw (§3.1).

## 7. Skips

- **Everything outside the scope** (the other 92 items, 聴解, and round-1 F5–F8): not re-passed, per the fix-loop rule. That includes the 聴解スクリプト sha move from the F5–F7 replays: the F5 ear-check and the F6/F7 replays are round-1 items, not in this scope.
- **No playback** in this environment. Nothing in scope needed the ear.
- I edited nothing except this report. Scratch: `/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/87a5eab4-5dc5-4727-bd01-de360ff16047/scratchpad/qa2_1102_check.txt` (make check output) and `/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/87a5eab4-5dc5-4727-bd01-de360ff16047/scratchpad/qa2_1102_kanji-174.png` (the rendered book page).

## Dispositions (orchestrator, 2026-11-02): fixed directly, no further review (the scoped re-review runs at most once)

| finding | disposition |
|---|---|
| R2-F1 stale allocation tallies + 問題1-5 band line | **Fixed.** Allocation L444 (11(1) 反論の前提を問い直す), L423–425 (reframe family = 2, at cap), L53 template cell prefixed. 問題1-5 解説 band now cites 新完全マスター漢字N2 別冊1 #518 (印刷 p.41／PDF p.174). |
| R2-F2 item 58 option-4 解説 | **Fixed**, with one deviation: 「使い方が古い」 is option 4's wording, not passage text, so it is written without 「」 (a quoted string must trace to the passage): 「4の、使い方が古いということは述べておらず、筆者は暗さを認めたうえで、使う場が違えば問われることも違うと述べているだけで、客に改めるよう求めてはいない。」 Stage 5 carries the same reasoning. |

RC-R2-1 (reframe check blind to わけではない) joins round 1's open rows.
