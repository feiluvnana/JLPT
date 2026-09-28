# QA report — 20260928_2, round 2 (SCOPED re-review, runs once)

QA: FAIL (2 findings, 0 automatic)

Both findings are non-blocking wording/bookkeeping fixes to be applied directly
under `jlpt-test-generation` §"The fix loop"; neither changes a key or replaces
an item, so neither earns a further review. No automatic-fail class was found
in scope.

- Reviewed 2026-09-28 by a fresh context that authored nothing in this paper and did not write round 1.
- **Source revision (sha1[:12]), read at the start and re-read before writing. Unchanged:**
  - `言語知識・読解.md` = `072884f51c29` (mtime 21:19:32)
  - `聴解.md` = `45cf4858ee05` (21:20:57)
  - `聴解スクリプト.txt` = `7d632868bf49` (21:20:57; equals `聴解_チャプター.json` `script_sha`)
  - `qa/dokkai-allocation-20260928_2.md` = `468e47101ba5`; repo HEAD `d3e32a5`
- **Solved from:** `qa/20260928_2/keyless.md`, rebuilt fresh by `make keyless 20260928_2` (932 lines). I answered 27 and 53 before I opened either key row.
- **Entry gate:** `make check` exits 1 on exactly one FAIL, the expected `20260928_2: 詳細解説.json explains every keyed item (30 entries for 101 keys)`. The WARNs naming this paper are the same three round 1 resolved (聴解問題5 headline repeat, the slot-theme row, pools_sha). No new WARN.
- **Files edited:** none except this report.
- **Scope** (`jlpt-test-generation` §"The fix loop"): I blind-solved the two replaced items (問題6-27 and 問題10(2)/53) and re-read 問題6, 問題10 and the 13-final column. I also spot-read the round-1 wording fixes F3, F4 and F6. This was not a full re-pass.

---

## 1. Blind answers against the keys

| item | my blind answer | key | result |
|---|---|---|---|
| 問題6-27 もうかる | 4 | 4 | agree |
| 問題10-53 | 3 | 3 | agree |

- **Blind-strategy check on 53** (character bigrams shared with the passage, then option length):
  - Overlap by option: 1 = 19, 2 = 12, 3 = 11, 4 = 18. The key has the **lowest** overlap.
  - Length by option: 30 / 28 / 28 / 29. The second-longest option is 4.
  - Neither mechanical strategy picks the key.
- **Paper-level gate lines are unchanged and inside their bars:**
  - uniquely-longest key 4/20 = 20 %;
  - (tied-)longest key 5/20 = 25 %;
  - strict top-overlap key 25 %;
  - max/min option-length ratio ≤ 1.65.

## 2. Walkthrough of the scoped items

| 項目 | 鍵 | 判定 | 決め手 / どこが問題か | どう直すか |
|---|---|---|---|---|
| 問題6-27 もうかる | 4 | OK | 4 「駅前にできたパン屋は、毎日行列ができるほど**もうかって**いるらしい。」 The shop is the subject, the verb is intransitive, and the sense is 利益が出る. | — |
| 問題10-53 | 3 | OK | 「最初の何回かを、水の中で息を吐く練習に使ってみてほしい」 becomes 「初めに水中で息を出すことに慣れるとよい」 (最初→初めに, 水の中→水中, 吐く→出す). | — |
| 56-1 (F3) | 4 | OK | 「どの教科書を置いて帰るかは、それぞれの家庭で決めてよい」 is killed by 「その日の宿題に使う教科書は、必ず持ち帰らせて」 plus 担任が…伝え. It depends on the passage. | — |
| 62-1 (F3) | 2 | OK | 「荷物が重く、名所を回る時間が短くなってしまう旅」 has a true half (the stairs episode) and a false half: the passage says 「宿と名所のあいだを行き来するだけ」 and never says the time was short. This is one fact changed, with no second answer. | — |
| 69-2 (F3) | 3 | 要修正 (R2-F1) | 「やさしい日本語で書くと、日本語を母語とする人には読みにくくなる」 is not an on-sight elimination. It is killed by 「日本語を母語とする人たちからも、読みやすくなったと言われる」. That same line already kills 67-4 and 68-2, so all three 問題13 items carry the same foil. | See R2-F1. |
| 55-2 (watched) | 4 | OK | 「待つ時間は一回ごとが長いので…多めに」 is killed by 「一回ごとには半日ほどでも…何度も繰り返されます」. 必ず is gone. | — |
| 64 stem (F6) | 1 | OK | 「質問ばかりでじれったいという苦情について、筆者はそれをどういうものだと考えているか。」 The antecedent is now in the stem. It is worded differently from round 1's proposal but does the same job, and it leans toward no option. The key is still decided by 「そう感じるのは当然だろう」 plus 「遅らせているわけではない」. | — |
| （注） (F4) | — | OK | 駆け込む, 相次ぐ and 詰め込む are now unglossed (they appear in the body only). The new glosses 花むこ, 店番 and 通信指令室 appear 0 times in the 31 official booklets and are not tested anywhere. In-body count is 25 with 0 orphans. The new 10(2) gloss 力む never appears as an official option. Its one archive occurrence (12/2012 読解, 「所有だと力んでみても」) is unglossed but in a different sense, so it is a legitimate contextual gloss. | — |

### 問題6-27 in detail

- **Exactly one correct sentence.** Each distractor fails for its own reason, and all three are plausible learner errors:
  1. 「株で大金を**もうかって**」 has a を-object. もうかる is intransitive; the transitive verb is もうける. This is the classic learner error for this pair.
  2. 「毎月の給料から少しずつ貯金して、口座に百万円が**もうかった**」 describes money saved by the speaker's own effort. That is not a profit, and 「口座に〜が V」 is the frame of たまる.
  3. 「第一志望の大学に**もうかった**」 is a sound-alike of 受かった. It is tempting, not absurd.
- **The colloquial 得をする sense** (moji-goi §"A word's OTHER attested sense"). もうかる also means an expense or time saved as a windfall: 「タクシー代がもうかった」, 「休講で一時間もうかった」.
  - Option 1: a を-object fails in either sense.
  - Option 2: this is the only one near the second sense, and it does not fall into it. 百万円 is accumulated by deliberate saving, not a cost avoided. The sentence also keeps たまる's locative 口座に.
  - Option 3: fits neither sense.
  - No distractor is a second attested collocation.
- **Word form:** all four options bold a conjugated form of the verb (もうかって / もうかった / もうかった / もうかっている). There is no form tell. The key is kept at position 4, as `answer_positions` requires.
- **Band, written down as exam-qa-review §3 requires.** Key もうかる, drawn by `reroll-one(usage:1,71464738)` (ledger `reroll_log`: out 懸念, in 儲かる).
  - **The positive test is the archive.**
    - N2 7/2023 prints 「18 簡単にお金が**もうかる**というような話に、すぐ（ ）のはやめたほうがいい。」 (`refs/JLPT_N2_NEW/14. N2 7-2023/booklet.md` L63). This is an unglossed word in a 文脈規定 stem, i.e. assumed known.
    - N2 12/2023 読解(4) prints 「確実に儲（もう）かるとわかった時点で」 (`14. N2 12-2023/booklet.md` L690). It carries only a reading, no （注）, while the next word, 目算, is glossed （注1）.
    - So official does not gloss it, which is the opposite of the おのずと case.
  - **Textbook extracts:** 0 hits for もうか/儲/もうけ in the Shin Kanzen 語彙, Soumatome 語彙 and Hajimete extracts. That is OCR and weak evidence either way.
  - **Verdict:** inside the N2 band, not N1-hard. It is not TOO_EASY either: no N3 headline source on disk names it, and the もうかる/もうける transitivity split is a real N2 usage discrimination.
  - **Missing record:** the band line owed for a re-draw appears in no QA or fix report. Only the ledger reason and the 解説's notation citation record it. It is recorded here now; see §5.
- **The 表外-kana rule.** 儲 is not in `references/joyo_kanji.txt`, so the word must print in kana.
  - Stem and all four options print もうかる, as official 7/2023 does (moji-goi §"Every printed glyph must be 常用": 「問題4/5/6 print them in kana as official does」).
  - The kanji appears only in the key-table 解説 (「もうかる（儲かる）」), which is not a printed item.
  - `pools.json` keeps the headword 儲かる, a word that is on-band with an off-band spelling, which is the standing-list case, not a deletion.
- **問題6 as a column.** The five targets are もしかしたら (adverb), もうかる (verb), 頻繁 (na-adjective), 負う (verb) and 共感 (noun/suru).
  - The distractor devices vary across the column. 27 uses transitivity, a wrong collocation and a sound-alike. 29 uses a wrong-verb sound-alike (負って→負けて) and a wrong collocation (かぜを負う). Where both 27-3 and 29-4 rely on a sound-alike, the sound is different each time.
  - Positions run 1 4 3 2 3.
  - The gate's 問題6 length distribution is mean 26.5, median 25, range 20–35, with 3 over 30. That is inside both the FAIL envelope and the author target.
  - もうかる appears in no other generated paper, so the rotation line is ok. It is not in this paper's 聴解 script. The item's only other kanji interaction is 一生懸命 inside 27-3, which is harmless.
  - The column reads well.

### 問題10(2) in detail

**Against its allocation row** (主張 / no named template / 一人称の前後比較):

- **Final:** 「これから泳ぎを覚えようとする大人には、最初の何回かを、水の中で息を吐く練習に使ってみてほしい。」
  - It is a direct recommendation to the reader, which makes it 主張.
  - It names no foil, so it is outside the not-A-but-B family.
  - It is none of the ten named templates: not 相関, not the 分裂文 cleft, not ていた＋のだ, not ていない, not 先回り.
  - The genre carve-out does not apply. The final prescribes to the reader, so this is 主張, not 随筆.
- **MOVE:**
  - The "before" is PRACTICE: 「息が苦しくなるまで休まずに泳いでいた」.
  - The "after" is PRACTICE: 「まず十五分ほど壁につかまって顔を水につけ、鼻からゆっくり息を吐く」.
  - No third-party belief is quoted, nothing is corrected, and there are no records and no counting.
  - Deletion test: there is no denial sentence to delete, so the passage is off 〈想定→実は〉.

**Against its spec theme and avoid list:**

- The theme is スポーツ・余暇 (`reading_topics[1]`, origin authored). The shipped subject is 泳ぎ始めの息の練習, which is on-theme.
- None of the 57 avoid strings is about swimming or breathing technique. The nearest is 「市民プールの係員が話す、利用証を新しくするやり方」, a different subject.
- `logs/topics.json` rows across all papers carry no 泳/プール surface except 20260821_1 聴解3-3 (pool ID renewal) and 20260904_2 聴解5-2 (a pool class choice). Neither shares the subject.
- Provenance: the official booklets touch 水泳 only in 問題-level stems (12/2024 L130 「水に顔をつけること( )できなかった」 is a 問題7 stem, not a passage). No passage reproduces this one.

**Against the pattern F2 named** (20260928_1 問題10(5) and 20260917_1 問題10(1)):

- Both of those end 「数えてみると、…ほど、…回数が少なかった／相談が多かった」, built on records re-read and grouped contrast examples.
- The new 10(2) has none of it:
  - no 記録/手帳/数える;
  - no 「並べてみると」;
  - no 「〜ほど…回数」 (its two ほど are 「半年ほど」 and 「十五分ほど」, both approximations);
  - no 条件提示 and no 相関.
- Its persona (趣味の実践者) and claim (「泳ぎを覚えようとする大人は、最初の何回かを水の中で息を吐く練習に使うとよい」) differ from 職業人 / 「…書き出しておく家庭ほど…足りなくなりにくい」 and 観察者 / 「…時間帯が変わると…顔ぶれが変わる」.
- An abstract family resemblance remains: "do the preparatory step first". It shares no apparatus, move, template or closing, and I do not file it.
- F2 is cleared.

**Against this paper's 10(3) and 11(3)** (一人称の前後比較 is now at its cap of 3). The three passages side by side:

| | opening (before, ていた) | pivot | after | ending |
|---|---|---|---|---|
| 10(2) | 「初めのころは、…休まずに泳いでいた」 | 「半年ほどして、やり方を変えた。今は、…」 | 息を吐く練習 → 水を飲まなくなった | prescription to the reader (主張) |
| 10(3) | 「私は以前、その場で…終わりにしていた」 | 「三年ほど前から、…ようにしている」 | a third-party episode (友人への電話) | motion-metaphor generalisation (随筆) |
| 11(3) | 「私は長いあいだ、…出かけていました」 | 「五年前、…。それからは、…ようにしました」 | two third-party episodes (宿の人, おかみさん) | proportion generalisation 「〜たびに…一つ増えます」 (随筆) |

- **Verdict: compliant.**
  - 10(2) is the only one of the three with no 〜ようにする pivot, no third-party episode and a prescriptive close.
  - The three finals sit on three different unnamed skeletons.
  - The MOVE count is 3, which the owner's table allows (≤3).
- **Watch, not filed:** 10(2) and 10(3) are adjacent and share the before→time-pivot→after arc, so a reader meets the move twice in a row. See the proposal in §4.

**The keyed-form re-grep** over the new 10(2) block, glosses included, covers the 17 問題7/8 forms plus 問題9's 一方/耳につく/わけだ/力がたまらない. Every one gives **0 hits**.

### Whole 問題10 and the 13-final column, re-read

**問題10 as a block:**

| passage | subject | MOVE | shape |
|---|---|---|---|
| (1) | email | 実用文 | 実用文 |
| (2) | swimming | 前後比較 | 主張 |
| (3) | second thanks | 前後比較 | 随筆 |
| (4) | waiting time | 機構の説明 | 説明 / 分裂文 |
| (5) | school notice | 実用文 | 実用文 |

Themes are distinct. The stems vary: 問い合わせ, 筆者の考え, どのようなもの, 説明に合う, 伝えたいこと.

**SHAPE column, read down the 13 finals:**

| shape | count | surfaces |
|---|---|---|
| 意外な観察 | 2 | 9, 11(1) |
| 実用文・分類外 | 2 | 10(1), 10(5) |
| 主張 | 2 | 10(2), 11(2) |
| 随筆 | 2 | 10(3), 11(3) |
| 説明 | 2 | 10(4), 12A |
| 反論応答 | 2 | 11(4), 13 |
| 条件提示 | 1 | 12B |

- Nothing exceeds 2.
- The two 主張 finals are on different skeletons: 11(2) is 「AことよりBことのほうが…力になる」 (the より…ほう template, with a foil) and 10(2) is an unnamed, foil-free request.

**TEMPLATE column, read separately:**

- 分裂文 1 (10(4)), より…ほう 1 (11(2)), わけではない 1 (11(4)). The paper holds 0 相関 and 0 of each cap-1 template.
- The not-A-but-B family stays at 2 (11(2), 11(4)).
- The 9 unnamed finals are pairwise distinct. I checked the pairs at risk named in the allocation: 9 vs 11(1), 10(3) vs 11(3), 12A vs 12B, and now 10(2) vs 11(2).
- I verified all 13 finals are in the paper as the allocation quotes them. 11(2) carries the （注5） marker inside 「ともし（注5）続ける」.
- The gate agrees: `no more than 2 読解 passages close on one sentence template (13 finals read …)` ok.

**MOVE column, 10 essay surfaces, 問題12 counted as one:**

| MOVE | count | surfaces |
|---|---|---|
| 〈想定→実は〉 | 1 | 11(2) |
| 機構の説明 | 3 | 9, 10(4), 12 |
| 数えたことの報告 | 1 | 11(1) |
| 一人称の前後比較 | 3 | 10(2), 10(3), 11(3) |
| 反論への応答 | 2 | 11(4), 13 |

- The cross-half 〈想定→実は〉 count stays at 2 (11(2) plus 聴解3-4), unchanged, which is the cap.
- Keys do not inherit a monoculture: 53's key is a practice recommendation, and the 前後比較 keys 54 and 61/62 are about consequences.

---

## 3. Findings

| id | item | class | evidence | proposed fix | owner | auto? |
|---|---|---|---|---|---|---|
| **R2-F1** | 問題13 option 69-2 (with 67-4, 68-2) | Distractor-set monotony created by the F3 fix: one passage line kills one distractor in each of the three 問題13 items | The three distractors:<br>• 67-4 「日本語を母語とする人から、長い文は読みにくいと言われたから」<br>• 68-2 「文が短くなりすぎて、日本語を母語とする人に不満を持たれた」<br>• 69-2 (new) 「やさしい日本語で書くと、日本語を母語とする人には読みにくくなる」<br>One sentence kills all three: 「こうして書いたお知らせは、日本語を母語とする人たちからも、読みやすくなったと言われるようになりました」. A solver learns "the 母語-speaker complaint option is wrong" once and uses it three times, and the only （注） in the region (（注5）母語) draws the eye to it. This is not an on-sight elimination (it needs the passage), so it is not automatic. Round 1 proposed this exact wording, and the fixer applied it faithfully. | Rebuild 69-2 from a different clause, with one fact changed and no 母語 actor. Example: 「易しく書き直したお知らせは、元の文と並べて配れば、正確さも守れる」. It is plausible, because 先輩's worry about 正確さ is in the passage, and it is killed only by reading the passage: the passage's remedy is 文の組み立て (「一つの文には条件を一つだけ」), not keeping the original beside it. Avoid a より…ほう option, since that is 11(2)'s final template. Avoid a 「〜さえすれば」 sufficiency strawman too. Keep the printed length within 1.65 of the set. Re-sync the 69 解説. Run `make check`. Re-grep keyed forms over 問題13's options (exclusion 3 makes it out of scope, but confirm no new frame). | 読解 author | no |
| **R2-F2** | `qa/dokkai-allocation-20260928_2.md` §"Why each shape sits where it does" and §"Tallies the authors must NOT break" | Bookkeeping desync: the binding allocation artifact contradicts its own re-allocated row and the paper | The 問題10(2) row now says 主張 / no template / 一人称の前後比較, but the file still says:<br>• slot table 「10(2) … assigned here 条件提示」<br>• tallies 「主張 1」「条件提示 2」「相関 1 (問題10(2))」「unnamed 9」<br>• 「数えたことの報告 2 (10(2), 11(1)), 一人称の前後比較 2 (10(3), 11(3))」<br>• voice-quota note 「数えたことの報告 rows (10(2), 11(1))」<br>• §"two things checked by hand": 「問題10(2) and 問題11(1) (数えたことの報告)」<br>The true values are 主張 2, 条件提示 1, 相関 0, unnamed 10, 数えたことの報告 1, 一人称の前後比較 3 (at cap). `logs/topics.json`'s notes already carry the right tallies. This file is what the next author and QA read as the column. | Update the four stale passages to the shipped values. Mark 一人称の前後比較 as **at cap (3)**, so any further re-angle must go to 数えたことの報告 or 反論への応答, not here. | orchestrator (allocation owner) | no |

**Considered and not filed:**

- **27-2 against the 得をする sense of もうかる.** Rejected with a reason (§2).
- **10(2)'s "do the preparatory step first" claim against 20260928_1 10(5).** It shares no apparatus, move, template or closing. It is an abstract resemblance only.
- **10(2)/10(3) adjacency on one MOVE.** It is within the owner's ≤3 cap. See the §4 proposal.
- **Gloss 力む.** It is not an official option, and its archive occurrence is in another sense. It is legitimate as a contextual gloss.
- **趣味の実践者 (10(2)) against 実践者 (12B) in `persona`.** Even read as one token, that is 2, which is the cap.

## 4. Root-cause rows (new)

| finding | code | tests showing the class | owning file | proposed edit |
|---|---|---|---|---|
| R2-F1 | RULE-MISSING | 1 (this paper; not measured wider) | `.agents/question-authoring/references/dokkai.md` §"読解 distractors — no free eliminations"; `exam-qa-review` §2 (a proposed-fix text is itself a new distractor) | Add one line: 「When rebuilding a distractor, list every other option in the same 大問 and do not reuse a foil (the same actor + the same claimed reaction) that another item's distractor already carries: one passage sentence must not kill distractors in two items.」 Also add to exam-qa-review §3: a QA-proposed replacement option is checked against the 大問's other option sets before it is written into the report. This is human judgement, not string-decidable at a useful precision, so no gate check is proposed. |
| R2-F2 | RULE-IGNORED (process) | 1 | `jlpt-test-generation` §"The fix loop" already requires the author/orchestrator to update the records a fix moves. `topics.json` was updated; the allocation file's derived sections were not. | Nothing new is required. Optionally, add to the fix-loop paragraph: 「a re-allocation edits the row AND re-derives the file's tally and per-slot sections.」 |

**Proposal, not a root-cause row (it blocks nothing):** consider an allocation guideline that no two adjacent 問題10 essay slots carry the same MOVE. Nothing here measures whether official avoids it, so it is left as a question for the owner.

**Still open from round 1, confirmed by this read:** RC F1's pool edit has not landed. `pools.json` still carries 懸念 at L1832 and L3318, so the next draw can pick it again. It must be applied (evidence field or deletion) or rejected before the next `make sample`. Round 1's other RC rows (F2, F3, F4, F6) are outside this scope. I did not check whether they have been applied.

## 5. Coverage and skips

**Ran:**

- `make check` as the entry gate. Every line was read for this paper: the one expected FAIL and the three known WARNs, which were resolved in round 1 and are unchanged.
- `make keyless 20260928_2`, then a blind solve of 27 and 53 and the bigram/length strategies on 53.
- Key proof and distractor elimination for 27 and 53.
- Band and 表外 checks for 27.
- The 問題6 column read.
- For 10(2):
  - allocation, theme, avoid-list and topics.json row checks;
  - a provenance grep against the 31 booklets and the Shin Kanzen 読解 extract;
  - the cross-paper pattern check against 20260928_1 10(5) and 20260917_1 10(1);
  - the in-paper MOVE-sibling check against 10(3) and 11(3);
  - the keyed-form re-grep.
- The whole-問題10 and 13-final re-read, shape and template read separately, plus the MOVE column.
- Spot reads of 55, 56, 62, 64, 67–69 and the （注） set.

**Not run, by scope:**

- Everything else in the paper.
- `qa_eval.py`. It takes a 101-answer vector, and a 2-item solve does not supply one.

**Band record:** the re-drawn key's band line (exam-qa-review §3, moji-goi Part 0 §"The KEY must be N2") is recorded in §2 above. No fix report carried it.

**聴解:** out of scope, but noted.

- The listening shas moved since round 1. The move is a text-only `--replay`: one draw record, seed 99207311, 29 clips. The MP3 (20:32) predates the script (21:20) by design, since the audio did not change.
- `make check` confirms `聴解.mp3 was built from today's 聴解スクリプト.txt (script_sha 7d632868bf49)`.
- I did not re-verify the F5/F7/F8 dispositions.

## Dispositions (orchestrator, 2026-09-28): fixed directly, no further review

| finding | disposition |
|---|---|
| R2-F1 69-2 shared foil | **Fixed** by the 読解 author: 69-2 is now 「易しく書き直したお知らせは、元の文と並べて配れば、正確さも守れる」. 68-2 carried the same foil and was rebuilt too, as 「文を短く切りすぎて、同じ話が何度も繰り返されていた」. Keys 67=1, 68=4 and 69=3 are unchanged. |
| R2-F2 stale allocation tallies | **Fixed**: only the derived tallies were re-derived (主張 2, 条件提示 1, 相関 0, 数えたことの報告 1, 一人称の前後比較 3 at cap). No row changed. |
| Round-1 RC F1 pool edit | **Applied**: both 懸念 entries were deleted from `pools.json`. |
