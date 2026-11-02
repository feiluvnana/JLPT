# QA report — 20261102_2 (Stage 4, round 2, SCOPED)

QA: PASS on the scoped items (0 automatic; 1 要修正 finding, bookkeeping only: the 3-12 解説 band line. No key, option or stem change)

- Reviewed 2026-11-02 17:48–17:58 JST by a context that authored nothing in this paper and did not run round 1.
- Scope, per `jlpt-test-generation` §"The fix loop" (one scoped re-review, at most once): 問題3-12 (F1, rerolled twice, now 〜色(地方色)) and 問題7-31 (F5, new stem and three new distractors, key form 〜つつも), each re-read against its own 大問 as a column. F2, F3 and F4 are confirmed on disk in one line each (§3.4) and were not re-reviewed. Nothing else was re-passed.
- Source revision (sha1[:12]). The values were the same at the start, before writing, and in the keyless render header:
  - `言語知識・読解.md` = `72b9de313bda` (mtime 17:47:16; round 1 read `9adcca3051f0`)
  - `聴解.md` = `b3f27a901759` (unchanged since round 1)
  - `聴解スクリプト.txt` = `22953465495b` (moved from round 1's `04f2f9dcff6f`: the F3 replay; the gate reports `聴解.mp3 was built from today's 聴解スクリプト.txt (script_sha 22953465495b)`)
  - `test_spec.json` = `524dd495b539` (mtime 17:45:38, the entry-#6 reroll)
  - Repo HEAD `aa025ac`.
- Solved from `qa/20261102_2/keyless.md` (`make keyless 20261102_2`, 965 lines). **Blindness disclosure:** the brief's reading order put `qa/blueprint-rerolls-20261102_2.md` #5–#6 and round-1 F5 before the solve. Both print the key position (「key 2」 for 3-12; 「key position 1 kept」 for 31), so the two answers were not blind. My solve was independent on the merits (§2), and every proof below rests on a quoted fact, not on agreement with the key. See RC-R2-3.
- `make check`: exit 2, with exactly one FAIL: `20261102_2: 詳細解説.json explains every keyed item (30 entries for 101 keys)`. That is the expected stage-5 FAIL. This paper's WARNs: 聴解2-2番 slot theme 教育, the 1-1番 「、」 placement, `drill/N2` stale and the suite `pools_sha` record. All are round-1 dispositions and unchanged. Relevant ok lines:
  - `問題7 stem distribution (mean 45.3 in 36-52, 2 under 34 (need 2), spread 39 ≥ 25)`
  - `no word appears twice in one 大問's options`
  - `no 問題7 form printed in more than 2 items' options`
  - `no 問題3 option set repeats 20261102_1's (worst 0.111, ceiling 0.30)`
  - `ledger history entry records the same draw as test_spec.json`
  - `rotation claim holds`
  - `no Shin Kanzen 目次 grammar point is drawn twice inside its cooldown`
  - `no 問題7/8/9 keyed form appears more than 1× in the 問題10-14 prose`
  - `no （注N） headword is reused as plain text in 問題1-9 or the 聴解 script`
  - `（注N） markers … numbered in reading order`
  - `every drawn 聴解 clip carries a QA script-read record (0 of 29 unread)`

## 1. Blind-solve diff (scoped items)

| item | blind | key | |
|---|---|---|---|
| 問題3-12 地方（　） | 2 色 | 2 | agree |
| 問題7-31 予約を取らなければと（　） | 1 思いつつも | 1 | agree |

2/2, no mismatch. Answers were saved before any key table was opened: `/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/4c04ee6c-0667-4210-8165-898b3b795c1d/scratchpad/qa2_blind_answers.json`.

## 2. Per-item walkthrough (scope only)

| 項目 | 鍵 | 判定 | どこが問題か / deciding quote | どう直すか |
|---|---|---|---|---|
| 問題3-12 地方色 | 2 | OK (要修正: 解説 band line only) | 「私の生まれた町の祭りは、地方（　）が強い。」 「地方色が強い」 is the set collocation: a local flavour shows strongly. 1 地方味, 3 地方感, 4 地方調: none is a word (0 hits in all 31 `booklet.md`/`script.md`, the four extracts and every `tests/*` paper; the key 地方色 also has 0 hits, so the call rests on the lexicon, see §3.1). Key band: Shin Kanzen 漢字N2 #153 色 「ショク 〜色 特色」 (page opened, §3.1) | R2-F1 |
| 問題3 column (11–13) | 1,2,4 | OK | 半/仮/副/超 (prefixes) · 味/色/感/調 · 型/式/流/順. Twelve different affixes (gate ok). No option string appears in another item. 調 (12) sits beside 式/流 (13) in the style family, but none of the three forms a word with the other item's base (五十音調/地方式/地方流 are not words), so neither item eliminates the other | — |
| 問題7-31 つつも | 1 | OK | 「歯医者の予約を取らなければと（思いつつも）、気づけば一か月もたってしまった。」 「気づけば…てしまった」 means the intended act never happened, so the front clause must be concessive. Each distractor dies for its own reason (§3.2) | — |
| 問題7 column (31–42) | — | OK | Option tails read down the column: 31's とたん/につけ/末に print nowhere else in 問題7–9. 31 思ったとたん and 35 かと思うと are both immediate-succession forms, but in different items and with different strings. Gate `no 問題7 form printed in more than 2 items' options` ok. Two stems now end in 「てしまった」 (31, 41). Noted, no rule | — |

## 3. Scoped checks

### 3.1 問題3-12 (F1: 〜振り(久し振り) → 下〜(下請け) → 〜色(地方色))

- **Draw, spec = ledger.** `test_spec.json` and the `logs/ledger.json` entry for 20261102_2 agree field for field:
  - `items` are equal.
  - `seed` is equal and ends `…+reroll-one(word_formation:1,91189987)+reroll-one(word_formation:1,1061369)`.
  - `pools_sha` is `cf187cf62829` in both.
  - `word_formation` = `['半〜(半永久)', '〜色(地方色)', '〜順(五十音順)']`.
  - `reroll_log` #5 (out 〜振り(久し振り), in 下〜(下請け), 17:42:47) and #6 (out 下〜(下請け), in 〜色(地方色), 17:45:38) carry reasons that match `qa/blueprint-rerolls-20261102_2.md` #5–#6.
  - `answer_positions["問題3_語彙"]` = `[1, 2, 4]`, so slot 12 is still 2.
  - `pools.json` L1772 carries 「〜色(地方色)」.
  - No earlier ledger entry contains 〜色 or 地方色, so there is no cooldown question.
  - The drawn carrier 地方 is the one printed, so this is not a sense substitute. The orchestrator's refusal of 下書き for 下〜(下請け) was correct under the same reading.
- **Productive-base test (round-1 RC-1, proposed for moji-goi Part 3).** Not yet in `moji-goi.md` (Part 3, L476–486, has no productive-base sentence; `grep -rl "productive base" .agents/` returns nothing), so I applied the RC-1 text as written:
  - 地方 is a free noun.
  - 地方色 is not a word learned whole below N2. The suffix is productive on free nouns (国際色, 政治色).
  - A candidate who does not know 〜色＝特色 cannot answer from the base. **Pass.** This is the opposite of 久し振り, whose base 久し is not free.
- **Key band (step 3, re-drawn key): checked against a book page.** `refs/Shinkanzen/kanji_tables.md` L1632–1635 renders 色's ショク row as OCR noise (「~笹軽省」), so I rendered `Shin_Kanzen_Masuta_N2-Kanji.pdf` PDF p.151 (printed p.18) with `pdftoppm`. Entry **153 色** prints: ショク 「〜色　特色」; いろ 「色」; (特) 「景色」. The suffix 〜色 (ショク) is a printed headword in the N2 kanji book. **Key band: N2.** The author's 解説 band line says only 「抽出・公式31回分に「地方色」の行は見つからない」 → R2-F1.
- **Distractor band and family.** I rendered `Shin_Kanzen_Masuta_N2-Goi.pdf` PDF p.180 (printed p.173, 7章3課 単語の後ろに漢字をプラス):
  - 〜感 is headed under 「6. 人の気持ち・能力に関係のある漢字」: 安心感・存在感・満足感・不安感・責任感・緊張感・危機感. That supports the 解説's framing of 感.
  - 〜味 (人間味) and 〜調 (七五調) are real 漢語 suffixes.
  - All four options are one-character suffixes of the property/feel family. That is the same shape as official 12/2023 #11 対抗（心） with 心/欲/願/熱.
- **Two-answer hunt.**
  - 3 地方感: colloquial 〜感 is productive on nouns (昭和感, 手作り感), but 地方感 is in no dictionary I can cite, no archive line, and no extract, and 「祭りは地方感が強い」 is not standard written Japanese. The official model is the same lexical-gap death: 7/2025 #11 「新たな教育（論）」, where 則/理/規 form no word.
  - 4 地方調 is not a word (do not confuse it with 地方調査).
  - 1 地方味 is not a word.
  - 性 (地方性 is attested) was correctly kept out (reroll #6).
  - **One answer.**
- **Provenance.** I searched for 「地方色」, 「祭りは、地方」 and 「生まれた町の祭り」 across the 31 `booklet.md`/`script.md`, the four extracts, `refs/External`, every `tests/imported-*` paper and every other `tests/*` paper. There are 0 hits, so the stem is not a lift.
- **Stem shape.** Plain style, first person (私の…). The です・ます count stays 8/25. 問題3 is outside the 問題1/2/5 comma count.
- **Leak read.** 地方 is also printed in 問題2-10 「かんとう地方」 and 問題6-29 opt 3. Neither tests 地方 or 〜色. 問題4-18 opt 3 地味 contains 味 but is a different word.

### 3.2 問題7-31 (F5: new stem, new distractors)

- **Key proof.** In 〜つつも, the action named in the front clause is not carried out. 「気づけば一か月もたってしまった」 says the booking never happened, so the 逆接 is required. The key is fully natural.
- **Distractors, one death each.**
  - 2 思ったとたん: とたん needs an unexpected event immediately after the trigger. 「気づけば一か月」 is the opposite of immediacy.
  - 3 思うにつけ: 〜につけ needs a spontaneously arising feeling or recollection in the main clause, each time the trigger occurs (「将来を思うにつけ不安になる」). A month passing unnoticed is not that kind of clause.
  - 4 思った末に: 〜た末に needs a prolonged effort or deliberation (悩んだ/考えた) ending in an outcome. 「〜なければと思う」 is a single thought, not a process, and 「気づけば」 (unawares) denies any purposeful arc.
  - None of the three survives. The 解説 (L551) states the same three deaths correctly.
- **Band.** 〜つつも is a pool `grammar_p7` entry and an ALLOW line in `level_band_grammar.txt` (L133). The Shin Kanzen N2 文法 index (PDF p.218, printed p.209, opened) prints 「〜つつ(も) 65, 126」 as its own headed form.
- **Off-scope draw question, checked because the repair sits next to it.** 20261102_1 keyed 問題8 「経過状況(〜つつ…する)」. The same index heads 「〜つつ 13, 126」 and 「〜つつある 13, 126」 on p.13, apart from 〜つつ(も) on p.65, so under the 2026-09-28 one-目次-number ruling these are different points. There is no cooldown repeat, which matches the gate's ok.
- **F5's own concern is cleared.**
  - The new stem is off the 「体に悪いと知りつつ」 frame.
  - 「思いつつ」 occurs in no `tests/*/聴解スクリプト.txt`, so neither this paper's 聴解 nor 20261102_1's speaks the frame.
  - `20260904_2` #38 and `20260827_2` #42 (the earlier つつも keys) use different frames.
- **Provenance scan of the new stem.**
  - 0 hits anywhere for 「予約を取らなければ」, 「なければと思いつつ」, 「気づけば一か月」 and 「一か月もたって」.
  - 「歯医者の予約」 has one hit, official 12/2017 聴解 「あしたの歯医者の予約時間、手帳に書いとくべきだった」, a different frame with no つつ.
  - Two near frames exist and are not lifts:
    - Official 12/2019 問題8-44 「11時までには寝ようと思いつつ、ついテレビを見続けてしまい」 shares only 「と思いつつ」. That 5-char run is the form's canonical collocation, the same reasoning as round-1 F4's 「海が荒れる」.
    - Official 7/2023 問題8-45 (`tests/imported-n2-2023-07` L172) 「返事をしなければと思いながらも、…まだ返事ができていない」 shares 「なければと思い」 (7 chars) with a different act and a synonym form.
  - **Not filed.** Note that round 1's own proposed stem, 「早く返事をしなければと思い（　）、気づけば一週間もたってしまった。」, shared an **11-char** run 「返事をしなければと思い」 with that official line. The author did not adopt it → RC-R2-1.
- **Column, keyed-form re-grep.**
  - つつ appears in 問題10–14 only as 「一つつけて」 (L329), which is not the form.
  - とたん, につけ and 末に appear nowhere else in the paper except 「週末に」 and 「つける」, which are not the forms.
  - The paper keys つつ nowhere in 問題8/9.

### 3.3 問題7 distribution after the re-stem

The gate reports mean 45.3, 2 stems under 34 and spread 39, all inside the `bunpou.md` §問題7 bars. My JP-char count, labels included, is 31=29, 36=25, 41=26, so the short-stem floor holds under either counting. Round 1 had 31 at 21 chars. The new stem is longer but still short.

### 3.4 Round-1 fixes on disk (confirmed only, not re-reviewed)

- **F2:** 11(4) now prints 「週末に夜ふかしをするのは」 bare. The glosses run （注1）寝つく / （注2）体内時計 / （注3）一回り / （注4）宵の口 (L387–390), renumbered with body markers in order (gate ok).
- **F3:** `聴解スクリプト.txt` L182 reads 「女:だといいんだけどね。とにかく、なるべく疲れないのがいいのよ。」 (also `tests/20260910_1` L122, the declaration L3919 and `詳細解説.json`). The read row `kanzenmoshi:cd1-21` → `F3`. The ear-check is still open from round 1.
- **F4:** 問題1-2 is now 「台風が近づくと海が**荒れる**。」, no longer the Hajimete 例文.

## 4. Findings

### R2-F1: 問題3-12 解説 band line names no positive evidence; a book page settles it (要修正, bookkeeping; owner: 文字・語彙 author)

- **Evidence.** `言語知識・読解.md` L528 ends 「帯: プールの採録（`word_formation` 「〜色(地方色)」）。抽出・公式31回分に「地方色」の行は見つからない。土台の「地方」は自由な名詞で、地方色はN3以下の固まった語ではない。」 `moji-goi.md` Part 0 §"The KEY must be N2" requires that a re-drawn key's band go into the record "with the book and page that confirmed it". The page exists (§3.1). This is the same bookkeeping class as `qa-report-20261102_1-round2` R2-F1.
- **Fix (replacement text).** In L528, replace the sentence beginning 「帯:」 with: 「帯: 新完全マスター漢字N2 学習漢字リスト 153「色」ショク 「〜色　特色」（印刷 p.18／PDF p.151、ページを開いて確認）。プールの採録（`word_formation` 「〜色(地方色)」）。土台の「地方」は自由な名詞で、地方色はN3以下の固まった語ではない。」 Then run `make booklet`/`make sheet` (no autofix) and carry the same band fact into `詳細解説.json` at stage 5.
- **Optional, same pass (round-1 debt, out of scope).** 問題1-4 お礼状's band line (L520) says no extract headword was found. The same Shin Kanzen 語彙N2 page I opened (printed p.173, PDF p.180, 「〜状 招待状・紹介状・案内状・お礼状・年賀状・挑戦状」) prints お礼状. If the author edits L520, that is the citation.

## 5. Root-cause rows

| RC | finding | code | papers showing the class | owner | proposed edit |
|---|---|---|---|---|---|
| RC-R2-1 | §3.2: round 1's proposed F5 stem shares an 11-char run 「返事をしなければと思い」 with official 7/2023 問題8-45 | RULE-MISSING | Reviewer-authored repair collateral: `20260928_2` round-2 R2-F1 (an option wording), `20261008_1` round-2 R2-F1 (a re-angle), and now a stem in this paper's round 1 (not shipped, because the author changed it). 3 papers, so systemic | `exam-qa-review/SKILL.md` §3, beside "A replacement option YOU propose is a new distractor" | Add: 「**A replacement STEM you propose is new text and runs the provenance scan before it goes in the report** — the 31 `booklet.md`/`script.md`, every `tests/imported-*`, the textbook extracts, and the previous two papers — and the report quotes the longest shared run. Founding case: qa-report-20261102_2 F5 proposed 「早く返事をしなければと思い（　）…」, 11 chars of official 7/2023 問題8-45.」 Not a gate item: the reviewer's text never reaches a file the gate reads |
| RC-R2-2 | §3.1 (evidence used for the 3-12 call) | RULE-UNENFORCEABLE (the rule's cited evidence is wrong, so a reviewer who checks it cannot reproduce it) | 2 files carry the same error | `question-authoring/references/moji-goi.md` Part 3 L481 and `exam-qa-review/SKILL.md` §3 問題3 bullet (L469–471) | Both cite official 7/2025 #11 as 「教育→則/理/論/規, only **教育観** attaches」 (the QA file adds "beside the key"). The booklet prints 1 則 2 理 3 論 4 規, and `key.md` gives 11→**3**, so the key is **教育論**. 観 is not printed. Replace with 「official 7/2025 #11 「新たな教育（　）」 offers 則/理/論/規 and only 教育論 (key 3) forms a word」. The rule's verdict does not change |
| RC-R2-3 | §header, blindness disclosure | PIPELINE-GAP | 1 (`20261102_1` round 2 solved before opening its reroll record, so it did not hit this) | `jlpt-test-generation` §"The fix loop" | After 「one fresh context blind-solves only the replaced items」 add: 「— and reads `qa/blueprint-rerolls-<id>.md` and the round-1 finding's repair text only after its answers are written down: both print the key position.」 |

Round 1's RC-1 (productive-base sentence in moji-goi Part 3, pool re-carrier of 〜振り(久し振り)) is still unapplied. `pools.json` L1720 「〜振り(久し振り)」 and L1747 「下〜(下請け)」 are unchanged, and reroll #5 adds 下〜(下請け) to the same re-carrier list. RC-1 through RC-6 and the three rows above block the next `make sample` until each is applied or rejected with a reason.

## 6. Coverage

- **Step 0:** scoped solve from `keyless.md` (§1), with the blindness caveat in the header.
- **Steps 1–2b:** key proof and every distractor's death for 12 and 31 (§3.1, §3.2).
- **Step 2.5:** 地方色 band from the Shin Kanzen 漢字N2 page (#153, printed p.18). Distractor family from the Shin Kanzen 語彙N2 page (printed p.173). つつも from the Shin Kanzen 文法N2 index (printed p.209).
- **Step 3:** 問題3 and 問題7 option columns; 問題7 distribution; keyed-form re-grep for つつも; provenance scans of both new stems.
- **Step 6:** spec = ledger for reroll #5–#6, answer positions, pool presence, cooldown.
- Round-1 F2/F3/F4: on-disk confirmation only (§3.4).

## 7. Skips

- **Everything outside the scope** (the other 99 items, 聴解, round-1 F2–F4 beyond the one-line confirmations, the F3 ear-check): not re-passed, per the fix-loop rule.
- **No playback** in this environment. Nothing in scope needed it.
- I edited nothing except this report. Scratch files:
  - `/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/4c04ee6c-0667-4210-8165-898b3b795c1d/scratchpad/qa2_blind_answers.json`
  - `/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/4c04ee6c-0667-4210-8165-898b3b795c1d/scratchpad/qa2_check.txt` (make check output)
  - `/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/4c04ee6c-0667-4210-8165-898b3b795c1d/scratchpad/qa2_kanji-151.png`
  - `/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/4c04ee6c-0667-4210-8165-898b3b795c1d/scratchpad/qa2_goi-180.png`
  - `/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/4c04ee6c-0667-4210-8165-898b3b795c1d/scratchpad/qa2_bunpou-218.png` (the rendered book pages)

## Dispositions (orchestrator, 2026-11-02)

| finding | disposition |
|---|---|
| R2-F1 問題3-12 band sentence | **Fixed** by the 文字・語彙 author with the reviewer's text. The extract's entry 153 sits under PDF p.151; its 〜色 line is OCR-garbled, so the wording rests on the reviewer's page check. Also: 1-4 お礼状's band line now cites Shin Kanzen 語彙N2 printed p.173 (PDF p.180). The cell notes that the extract has OCR-garbled お礼状 as 「お礼験」. Rebuilt (assemble, lint-draft, booklet, sheet). |
| RC-R2-3 (blind order) | Accepted as an orchestrator error: the round-2 brief told the reviewer to read reroll #5–#6 before solving. The proposed rule edit is still open, with the other RC rows. |
