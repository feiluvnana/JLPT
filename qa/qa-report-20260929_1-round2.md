# QA report — 20260929_1, round 2 (SCOPED re-review, runs once)

QA: FAIL (1 finding, 0 automatic)

The one finding is a non-blocking evidence-wording fix. It goes to the 問題2-7
解説 cell and is applied directly under `jlpt-test-generation` §"The fix loop".
It changes no key and replaces no item, so it earns no further review. No
automatic-fail class was found in scope. Both replaced items are sound. Each has
exactly one defensible answer, and my blind answers agree with both keys.

- Reviewed 2026-09-29 by a fresh context. It authored nothing in this paper and did not write round 1.
- **Source revision (sha1[:12]), read at the start and re-read before writing. Unchanged, and equal to the stage-3 §10.6 hand-off:**
  - `言語知識・読解.md` = `9224fc9b938d` (mtime 19:30:58)
  - `聴解.md` = `95a511336329`
  - `聴解スクリプト.txt` = `53d84554fe79` (equals `聴解_チャプター.json` `script_sha`)
  - `_sections/問1-6_文字語彙.md` = `ac552ba2e183`
  - `_sections/問7-9_文法.md` = `b65ab1fdd3f0`
  - repo HEAD `6da8d61`
- **Solved from:** `qa/20260929_1/keyless.md`, rebuilt fresh by `make keyless 20260929_1` (931 lines, render sha `07e10920e683`). I wrote all ten 問題2 and 問題8 answers, and the 46 permutation enumeration, to scratch before opening any key row.
- **Entry gate:** `make check` exits non-zero on exactly one FAIL, the expected stage-5 line `20260929_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)`. The WARNs naming this paper are the set stage 3 §6/§10.5 dispositioned: 問題8 form-family 1/5 tagged, the 問題12/13 theme-token lines, the composed 聴解問題5 headline repeat, the 聴解 slot-theme repeat, 問題1/2 question punctuation, and pools_sha. There is no new WARN.
- **Files edited:** none except this report. Scratch files are under the session scratchpad, prefix `qa2_20260929_1_`.
- **Scope** (`jlpt-test-generation` §"The fix loop"): I blind-solved the two replaced items, 問題2-7 (F2 reroll, 基盤 → 応接) and 問題8-46 (F1 re-cut). I re-read their 大問 columns (問題2 6–10 and 問題8 43–47). I checked both new items against every other 大問 for a keyed-form leak. This was not a full re-pass.

---

## 1. Blind answers against the keys

| item | my blind answer | key | result |
|---|---|---|---|
| 問題2-6 てんかん | 3 転換 | 3 | agree |
| **問題2-7 おうせつ** | **3 応接** | **3** | agree |
| 問題2-8 おさない | 4 幼い | 4 | agree |
| 問題2-9 やぶれる | 2 破れる | 2 | agree |
| 問題2-10 くぶん | 2 区分 | 2 | agree |
| 問題8-43 | 3 | 3 | agree |
| 問題8-44 | 1 | 1 | agree |
| 問題8-45 | 2 | 2 | agree |
| **問題8-46** | **2** | **2** | agree |
| 問題8-47 | 3 | 3 | agree |

The keys agree with `test_spec.json` `answer_positions`: 問題2_語彙 = [3, 3, 4, 2, 2] and 問題8 = [3, 1, 2, 2, 3]. `qa_eval.py` was not run, because it takes a 101-answer vector.

## 2. Walkthrough of the scoped items

| 項目 | 鍵 | 判定 | 決め手 / どこが問題か | どう直すか |
|---|---|---|---|---|
| 問題2-7 応接 | 3 | 要修正 (R2-F1, 解説 wording only) | 「母は朝から客の**おうせつ**に追われていた。」 Only 応接 is a word, and 客の応接 (receiving visitors) fits 追われる. The item is sound. The 解説's band citation 「見出し番号704」 is inaccurate: #704 is 応対. | See R2-F1. |
| 問題8-46 したがって | 2 | OK | したがって、(3)→早めに作って(4)→**おく(2)**→のがいいでしょう(1). This is the one grammatical ordering of 24 (§2.2). | — |
| 問題2 column (6, 8, 9, 10) | 3/4/2/2 | OK | No option repeats across items. There is no shared glyph that gives a clue (接 and 設 appear only in 7). The composition is intact: 和語 2 (幼い, 破れる) and bare compounds 3 (転換, 応接, 区分). | — |
| 問題8 column (43, 44, 45, 47) | 3/1/2/3 | OK | 43 だけあって, 44 わりに, 45 限りは, 46 したがって and 47 もとにして are five different functions. No card is shared between items. The splices read cleanly: 「着物屋の一人娘に生まれただけあって」「九十という年のわりに」「朝からの雨がやまない限りは」「利用者へのアンケートの結果をもとにして」. | — |

### 2.1 問題2-7 in detail

- **Grid shape and kana skeleton** (moji-goi §"The 2×2 component matrix"):
  - A=応(オウ), B=欧(オウ); C=接(セツ), D=設(セツ). Each column has one reading.
  - `python3 tools/matrix_helper.py validate --reading おうせつ 欧設 欧接 応接 応設` → `2x2 Cartesian Matrix Check: PASS (Cartesian shape AND kana skeleton — all four options read 「おうせつ」)`.
- **Exactly one real word.** 応接 is the word. 欧設, 欧接 and 応設 are pseudo-compounds, which the owner allows (official ships 支接/施接/支設). None of them is a real word or homophone with this reading, and おうせつ has no second 表記.
- **常用:** 欧, 応, 接 and 設 are all 常用. The gate's glyph line is `ok`.
- **Stem shape:** 18 JP chars, no 「、」, plain form, with a person as the actor (母). With it, 13 of the 15 問題1/2/5 stems are comma-free, against the author target of ≥9.
- **Band evidence, verified line by line:**
  - `refs/JLPT_N2_NEW/7. N2 7-2016/booklet.md` L135 reads 「37 （会社で）課長「山下さん、A 社の木村様が（ ） 、応接室に案内してください。」」. This is an official N2 問題7 stem that prints 応接室 **unglossed**, so the exam-maker assumes an N2 candidate reads it. Confirmed.
  - `refs/Hajimete/vocab_reference.md` L22111–22113 reads 「おうせつくする＞ / 応接（する） / 704」. This is the index, and it confirms 応接 is in the N2 2500 book. **The entry it points to is not an 応接 headword**, though:
    - L10075–10077 read 「704 / 応対 / 」くする＞」, so #704 is **応対**.
    - 応接 appears only as that entry's related word, OCR-garbled at L10123 as 「感善くする） recepion/抜待/img tiep」 (= 応接（する） reception／接待／tiếp đón).
    - The 解説 and the reroll log call 応接 「見出し番号704」 / "the headword … #704". The book supports "an N2 related word under #704 応対" but not "headword #704". This is the moji-goi Part 0 rule 「confirm each is the headword and not a fragment」. The band verdict does not move: the official unglossed 応接室 alone carries it. The record is still wrong, so it is filed as R2-F1.
  - The whole archive (31 booklets and 31 scripts) has one occurrence of 応接, L135 above, and it has no （注）. So the 「official glosses what it will not test」 test does not trigger.
- **Rotation and provenance:**
  - `logs/ledger.json` history[19] `items.orthography[1]` = 応接, which equals `test_spec.json`.
  - `reroll_log` rows 12–14 record 基盤 → 金魚 → 温室 → 応接.
  - No other ledger entry and no other `tests/*/言語知識・読解.md` holds 応接, so there is no cooldown hit.
  - `pools.json` has 0 remaining 基盤/金魚 entries and 1 応接 entry.
- **Artifacts:** the rendered 言語知識・読解.html, 解答.html and 練習.html are newer than the Markdown. Each carries 応接 and has 0 occurrences of 基盤.

### 2.2 問題8-46 in detail

Frame: 「（料理の本で）煮物は、火を止めたあと、冷めていく間に味が中までしみ込みます。＿＿ ＿＿ ★ ＿＿。」. The cards are A = のがいいでしょう, B = おく, C = したがって、 and D = 早めに作って.

**Enumeration.** This is structural, not by naturalness. I did it blind, then compared it with the 解説.

1. The four card tails, in a column:

   | card | tail |
   |---|---|
   | A | 言い切り (でしょう) |
   | B | 辞書形 |
   | C | 接続詞＋読点 |
   | D | テ形 |

2. A's 形式名詞 「の」 needs a 連体形 host **immediately before** it. That is a backward-pointing bound element, so it is legal adjacency (bunpou.md source 3). Only B ends in a 連体形, so the count is 1. A also cannot open the sentence right after 「。」. **This forces the block ［B→A］.**
3. D ends in a テ形 and needs a following auxiliary or verb. The candidates fail:
   - 「作ってのが」 is ungrammatical.
   - 「作ってしたがって、」 is ungrammatical.
   - Only 「作っておく」 remains.
   - Conversely, B's auxiliary おく needs a テ形 immediately before it. C's 「て」 is the tail of a conjunction plus 読点, and verbal 従う would need a 〜に that no card supplies.
   **This forces ［D→B→A］.**
4. There are three slots left for C:
   - **C-DBA**: grammatical. ★ = B = 2.
   - **D-C-BA**: splits 作って|おく. Ungrammatical.
   - **DB-C-A**: splits おく|の. Ungrammatical.
   - **DBA-C**: 「…のがいいでしょうしたがって、。」 does not close the sentence. Ungrammatical.
   Every other ordering of the 24 breaks the ［D→B→A］ chain.

**Result: exactly one of 24 survives, ★ = 2.** The 解説's forced-block proof, its tail column and its last-slot proof state the same derivation. Its 「て」-count claim (「『て』の字で終わるカードは…2枚」) is true: it counts two and then excludes C on grammatical grounds, rather than claiming one. `make verify-scramble` prints `FREE UNITS: 1 [したがって、 ｜ 早めに作って＋おく ｜ のがいいでしょう]`, `ARTIFACT: ok` and `UNDECIDED 24/24`. Uniqueness therefore rests on the written proof, which I re-derived independently. `--audit-claims` finds no 「〜で終わるのは『…』だけ」 claim in 46 to audit.

- **Round-1 F1's rival is gone.** 「食事の→数時間前に」 was the second free unit, and it is removed. The one free card left is the connective. Nothing follows the blanks except 「。」, so bunpou.md leg (b), 「adverbial card + contiguous block ⇒ two ★」, does not apply: a sentence connective cannot follow its own clause.
- **Register:** the frame is now 「（料理の本で）」, a printed text, so written-style したがって is apt. That was round 1's secondary note.
- **Logic:** 冷めていく間に味がしみ込む → したがって早めに作っておく is a valid cause → conclusion. 「したがって」 is used correctly, and no option is broken Japanese.
- **Length:** the card sum is 22 JP chars, inside the 16–29 target. The assembled sentence is about 52 chars.
- **Provenance:** the spec and ledger `grammar_p8` entry is still 「順接接続(〜したがって…)」, the drawn target, kept as F1 ordered. Key position 2 is kept.

### 2.3 Cross-大問 keyed-form leak check (both new items)

I grepped the whole keyless render (931 lines):

| string | hits outside its own item | verdict |
|---|---|---|
| 応接 / おうせつ / 応対 | 0 | no leak |
| したがって / 従って | 0 (only 46's card) | no leak. The 読解 prose and （注） lines carry 0, so the one-key-per-paper exposure count is 0 ≤ 1 |
| 早めに | 問題5-24 option 1 「早めに」; 聴解4 「早めに返事する」 | **Considered, not filed.** 早めに is a *distractor* of 24 (key だいたい, for 大まかに). Seeing 早めに作って in 46 tells a solver nothing about 24, and 46's ★ is おく, not 早めに. The moji-goi option-reuse rule binds within one 大問, and 問題5 and 問題8 are different 大問. |
| 作って | 問題10 prose 「広報紙を作っていて」, 聴解 「作って飲む」 | ordinary verb use, not a keyed form |
| ておく (★'s card おく) | 問題9 prose ×2, 問題11 （注3） 「しまっておく」, 問題11 and 問題12 options | out of scope. 46 keys the connective したがって, and ★ landing on the aspect auxiliary おく is not the tested point. This is the same class as the 授受/使役 exclusion 1 in exam-qa-review §3 |
| 煮物 / しみ込 / 冷め | 0 | no domain echo. The 食 domain is shared with 問題11(4) (bowl size), but no decisive detail crosses, as stage-3 §10.4 records |

## 3. Findings

| id | item | class | evidence | proposed fix | owner | auto? |
|---|---|---|---|---|---|---|
| **R2-F1** | 問題2-7 解説 cell (`_sections/問1-6_文字語彙.md` key row 7, merged `言語知識・読解.md` L517); also `qa/blueprint-rerolls-20260929_1.md` row 14 | Band-evidence misstatement. The cited line is an index pointer, and the entry it points to is a different headword. | 解説: 「帯: N2（Hajimete 索引の見出し「応接（する）」L22112、見出し番号704。…」. Reroll log: "Hajimete's index lists the headword 「応接（する）」 (L22112, #704)". But `vocab_reference.md` L10075–10077 is 「704 / 応対 / 」くする＞」, so #704 is **応対**. 応接 is that entry's related word (L10123, OCR 「感善くする） recepion/抜待/img tiep」). moji-goi Part 0 asks the author to 「confirm each is the headword and not a fragment」. | Reword the band clause to: 「帯: N2（Hajimete #704『応対』の関連語「応接（する）」、索引 L22111–22113→704、本文 L10123。公式 7/2016 booklet L135 が「応接室」を注なしで印刷）」. Make the same one-line correction in reroll-log row 14. Then run `make assemble` → `make booklet` → `make sheet` → `make check`. No key, option or stem changes. | 文字・語彙 author (解説); orchestrator (reroll log) | no |

**Considered and not filed:**

- **問題5-24 「早めに」 vs 46 「早めに作って」:** different 大問, a distractor rather than a key, and no elimination information (§2.3).
- **したがって as a bare-connective card, against the QA skill's "no option may be an adverb alone":** the owner is bunpou.md, which records a bare adverb/particle card as official practice (§問題8 calibration). Its binding invariant is ★-uniqueness and at most one free unit, and 46 meets both. The connective is the single free unit, and it is structurally pinned (§2.2).
- **46's last-slot sentence 「『おく』は後ろに形式名詞『の』を要求する塊の前半」:** it reads as forward-pointing, but it restates the ［おく→の］ block the 解説 derived earlier from の's backward demand (legal source 3). It is not the illegal particle-forward leg, and `illegal_legs()` does not fire.
- **応接 vs 応対 as a band call:** 応接室 is printed unglossed in an official N2 stem, which is positive evidence. Only the citation wording is wrong.

## 4. Root-cause rows (new)

| finding | code | tests showing the class | owning file | proposed edit |
|---|---|---|---|---|
| R2-F1 | RULE-UNENFORCEABLE (minor) | 1 on record here. It is a sibling of the 恩 case (qa-report-20260911_1-round2 NEW-2): both are a presence claim resting on a line that was not the headword. | `.agents/question-authoring/references/moji-goi.md` Part 0 §"The KEY must be N2", the OCR paragraph | Add one sentence: 「`vocab_reference.md` の索引行（読み／語／番号）は見出しではなく参照である。番号の指す本文エントリを開き、その語が見出し語か関連語かを書き、本文の行番号を引用すること。」 Not string-decidable, so no gate check is proposed. |

**Round-1 rows, as seen from this scope (not re-verified in full):** RC F1 proposed that `free_unit_count()` count a connective card as its own unit. 46 now prints the connective as its own segment with `FREE UNITS: 1`, so something in that direction may have landed, but I did not check the founding-case re-run the row demands (old 46 must print 2). RC F2 (orthography pool sweep) and RC-BP-1 / RC-S3-2 are outside this scope. They stay open until applied or rejected, and they block the next `make sample`.

## 5. Coverage and skips

**Ran:**

- `make keyless 20260929_1`, then a blind solve of 問題2 (6–10) and 問題8 (43–47) before any key or 解説 row was opened.
- A structural 24-ordering enumeration for 46.
- For 問題2-7:
  - `matrix_helper validate --reading`;
  - 常用 and real-word checks;
  - reading back the Hajimete L22112 index line **and** the #704 entry it points to (L10060–10130);
  - reading 7/2016 booklet L135;
  - an archive-wide occurrence and gloss grep for 応接.
- `make verify-scramble 20260929_1` and `verify_scramble.py --audit-claims`.
- A spec ↔ ledger ↔ pools check for 応接 and for 46's `grammar_p8` entry, and a rotation grep across all ledger history and every `tests/*` booklet.
- The 問題2 and 問題8 column re-reads.
- A cross-大問 grep of the new items' forms (§2.3).
- A check that the rendered HTML is newer than the Markdown and that no stale string (基盤, 数時間前に) survives.
- `make check` as the entry gate, with every line naming this paper read.

**Not run, by scope** (the fix loop allows only a scoped review):

- Every other item and the 読解/聴解 halves, including round 1's F3–F7 wording, apparatus and bank dispositions.
- `qa_eval.py`, which needs a 101-answer vector.
- The textbook PDF page read for 応接. The Hajimete PDF (45 MB) is under the read cap, but the OCR entry plus the official unglossed occurrence already settle the band. The only open point is citation wording, which the fix resolves.

**Band record** (exam-qa-review §3, "a re-drawn key's BAND is a named QA question"): key 応接 was drawn, and its band was checked against:

- official 7/2016 booklet L135 「応接室」 (unglossed, N2 問題7 stem);
- Hajimete N2単語2500 #704 応対, where 応接（する） is a related word (index L22112, body L10123).

Verdict: in band.
