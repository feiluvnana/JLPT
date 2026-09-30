# QA report — knowledge/N2 文法, batch 0 (20 points / 60 examples / 40 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch.
Files (sha1, first 12 characters): pre-review → post-fix

| file | pre | post |
|---|---|---|
| `knowledge/N2/文法.json` | 2f83e8ca2d8c | 1440fce76a8f |
| `knowledge/N2/文法.ja.json` | 02a063b062b4 | 05ee73082187 |
| `knowledge/N2/文法.vi.json` | 849486e237d0 | 1e25b6bbf6d7 |

## Verdict

`QA: FAIL → fixed (16 findings, 3 automatic-fail class). After the fixes, 0 open content findings.`
The only FAILs left are the two stale-page lines (`文法.html`, `index.html`). They cannot be cleared
right now because `make knowledge` and `make check` both crash on
`AttributeError: module 'build_model_answer' has no attribute 'LANG_SWITCH_JS'`. That crash comes from
another context's uncommitted refactor of `build_model_answer.py` / `lang_ui.py`, not from these files. I
built the three JSON files against HEAD's builder in a scratch export: **0 FAIL, 0 WARN**, and the new
content renders (the new option strings are in the page, and the group label 「第1部 18課」 appears ×24).
**Run `make knowledge LEVEL=N2` once that refactor lands.**

## 1. Blind solve

I solved from a scripted extraction of the 40 items (stem and options only, no `answer`):
`scratchpad/QA_B0_blind.txt`. My answers went to `QA_B0_myanswers.txt` before I compared them with the keys.

- **40/40 agree with the keys.** Agreement is the floor. Five items passed the blind solve and still had a
  second defensible answer or a form-only key (F1–F5 below). I found those by writing each distractor into
  its stem and asking what fact in the stem kills it, not by the solve itself.
- **Caveat, a process defect in my own extraction:** the script printed each item's entry id
  (`[g-ni-suginai]` …), which tells you the tested pattern. The solve was therefore not fully blind on
  "which pattern". The page itself is fine: `quizView` shows the source card ("quiz_from") only after the
  answer. Recommendation R7 covers this.
- Position balance: 10/10/10/10 before and after (no fix moved a key).

## 2. Per-entry walkthrough (SK page read on the scan, official cites read in booklet.md + answer_keys.json)

| entry | SK PDF p. | 接続 / meaning vs SK | official_count (verified) | verdict |
|---|---|---|---|---|
| g-ni-atatte | 18 ✓ | ✓. The マイナスイメージ note (入院・別れ) is SK's own ▲ 「マイナスイメージの言葉（別れ・入院・倒産など）にはつかない」 | 2 ✓ (7/2019-33, 7/2025-31) | OK |
| g-ippou-da | 22–23 (cited 23; heading is on 22) | ✓ ▲「変化を表す動詞」 | 4 ✓ (7/2010-37, 12/2015-37, 12/2018-35, 7/2025-38). Inventory's 6 is wrong: it counts 12/2010-43 「ばかりだというのに」 | page → 22; Q1 fixed (F3) |
| g-shidai | 27 ✓ | ✓ ▲ 希望・意向・働きかけ | 2 ✓ | OK |
| g-ni-watatte | 30 ✓ | ✓ | 2 ✓ | OK. Ex1 is close to SK ① (20キロにわたって渋滞) but not a copy |
| g-ni-tsurete | 52 ✓ | ✓ ▲ 意志的な行為は来ない | 3 ✓ | OK |
| g-o-towazu | 62 ✓ | ✓ ▲ lists 天候, which validates vi's 「天候を問わず」 | 2 ✓ | OK |
| g-dokoroka | 66 ✓ | **✗** SK: ナ形 だ-(な)/-である. The data made な mandatory | 2 ✓ | fixed (F11) |
| g-wake-dewa-nai | 67 ✓ | ✓ | 2 ✓ (12/2010-37 key 4, 12/2024-38). Inventory's 1 is wrong: it lists 12/2010-37 as "stem" | OK |
| g-monono | 74 ✓ | ✓ | 2 ✓ | Q2 fixed (F6) |
| g-nagara-mo | 74 ✓ | ✓ (動ます・イ形い・ナ形/名 (+であり)) | 2 ✓ | Q2 fixed (F5) |
| g-gatai | 92 ✓ | ✓ ▲ 能力的には使わない | 2 ✓. Inventory's 5 is wrong: it counts 「ありがたい」 in 12/2023-42, 12/2021 問題8-46, 7/2012 問題8-48 | ex1 + Q1 fixed (F8) |
| g-wake-niwa-ikanai | 92 ✓ | ✓ ▲ 主語は一人称 | 2 ✓. Inventory's 3 counts 7/2025-40 「乗らないわけにはいかない」, which is SK 25課4, a separate point | ex3 tail fixed (F13) |
| g-kaneru | 92 ✓ | ✓ (見かねて is SK's own ③) | 2 ✓ (7/2016-39 = 12/2020-39 reprint, noted) | OK |
| g-you-ga-nai | 93 ✓ | ✓ | 2 ✓ | Q2 fixed (F7) |
| g-sue-ni | 101 ✓ | ✓ | 5 ✓ (7/2011-34, 7/2013-34, 7/2016-36, 12/2019-31, 12/2017 問題8-45). Inventory's 4 misses 7/2011 | OK |
| g-ni-chigai-nai | 111 ✓ | ✓ | **2 → 3** (+12/2016 問題9-54 「結果に違いない」, key 3) | fixed (F12); ex3 fixed (F9) |
| g-ni-suginai | 114 ✓ | **✗** SK: ナ形/名 だ→である. The data said only 「だ」を取る | 2 ✓ | fixed (F11); Q1/Q2 fixed (F1, F4) |
| g-shika-nai | 115 ✓ | ✓ | 3 ✓ (12/2014-38, 12/2015-38, 7/2025 問題8-46). Inventory's 5 counts 名詞+でしかない (7/2011-42, 12/2024-42) | Q1 fixed (F2); usage fragment (F13) |
| g-koto-wa-nai | 119 ✓ | ✓ ▲ 話者自身には使わない | 2 ✓ (7/2015-39 key 1, 7/2022-40). Inventory's 1 misses 7/2015 | ex3 fixed (F10) |
| g-zaru-o-enai | 123 ✓ | ✓ | 2 ✓ | Q2 fixed (F5); ex2 fixed (F13) |

**Quiz rows.** Each was solved, then every distractor was spliced into its stem with the killing fact
named. 29 of 40 were OK as shipped. The other 11 are the rows in the findings table, with the flagged
items judged as follows:

- **Q24 行か＋ざるを得ない: OK.** ずにはいられない and ないでほしい both attach to 「行か」, so 3 of 4
  options are grammatical and the choice is semantic.
- **Q38 お越しいただくことはありません: OK.** The わざわざ frame is SK's own co-occurrence and the
  sentence is original.
- **Q20 and Q40: automatic-fail class** (only the key attaches). See F5.

## 3. Findings

| # | item | class | evidence | fix |
|---|---|---|---|---|
| F1 | Q34 (g-ni-suginai q2) | second defensible answer (auto) | 「最終バスに乗り遅れてしまった。ここからホテルまで歩いて帰る（ことはない）」 reads as "no need to walk, take a taxi". Only an implied necessity rules it out | stem now 「…乗り遅れたうえに、タクシーも一台も走っていない」. Both panes rewritten |
| F2 | Q35 (g-shika-nai q1) | second defensible answer (auto) | 「財布を家に忘れてきた。昼ご飯は我慢する（ことはない／わけにはいかない）」: "borrow from a colleague" makes both options defensible | stem now 「…忘れてきたうえに、お金を借りられる人もいない」. Both panes rewritten |
| F3 | Q3 (g-ippou-da q1) | borderline distractor + SK template | 「ものだ」 is defensible as a general truth ("short-handed → overtime rises, that's how it is"). The stem was also SK 2課3 ① 「残業が増えるばかりだ」 | new stem 「この川の水は、上流に工場ができてから汚れる（　）」. ものだ → ところだ, which 〜てから rules out |
| F4 | Q33 (g-ni-suginai q1) | distractors dead for an unrelated reason + false explanation | a bare noun 会社員 kills わけではない and ことはない by 接続 alone, leaving a 2-way item. The ja explanation said 「しかない」は…「会社員」に直接はつかない, which is false and contradicts g-shika-nai's own nuance (名詞＋しかない) | options now に限らない / にすぎない / どころではない / 次第だ, all noun-attaching. Both panes rewritten |
| F5 | Q40 (g-zaru-o-enai q2), Q20 (g-nagara-mo q2) | printed form selects the key on sight (auto) | 「使わ（　）」: only ざるを得ない attaches, and the ja explanation said as much (「使わ」の形につくのは「ざるを得ない」だけ). 「社長であり（　）」: only ながら attaches | Q40 options now なくて済む / ないではいられない / ざるを得ない / ないとも限らない, all on 使わ. Q20 re-stemmed so the options carry their own connection: 「日本語学校の先生（であるうえに／であるだけに／でありながら／である以上）、漢字の読み間違いが多い」 |
| F6 | Q18 (g-monono q2) | textbook template | 「セールで洋服を買ったものの、まだ一度も着ていない」 ≈ SK 14課2 ② 「高価な着物を買ったものの、着るチャンスがない」 | new stem 「一次試験には合格した（　）、面接で落ちてしまい…」 |
| F7 | Q28 (g-you-ga-nai q2) | textbook template | 「連絡先を聞いていなかったので、お礼を言いたくても言いようがない」 ≈ SK 18課4 ① 「連絡先がわからないので…知らせたくても知らせようがない」 | new stem (a finder who left without giving a name) |
| F8 | g-gatai ex1 + Q21 | textbook template ×2 | 「親友がそんな嘘をついたとは、信じがたい」 and 「あれほど真面目な彼が約束を破ったとは、信じ（　）」 both follow SK 18課1 ① 「あの優しい彼がそんなひどいことをしたとは信じがたい」 | ex1 → 「優劣はつけがたい」. Q21 → a ten-year show ending. I also avoided 忘れがたい and 理解しがたい, which sit in official 12/2024-39 and 7/2010-38 frames |
| F9 | g-ni-chigai-nai ex3 | broken Japanese (auto) | 「この字の書き方は、田中さんのメモに違いない」: the subject (a writing style) cannot be a memo | → 「机の上のメモは、字の形から見て、田中さんのものに違いない」. vi usage and note synced |
| F10 | g-koto-wa-nai ex3 | wrong meaning shown | 「準備しておけば緊張することはない」 reads as the non-occurrence ことはない ("won't get nervous"), not 必要はない | → 「時間は十分あるから、急いで答えを出すことはない」 |
| F11 | g-dokoroka, g-ni-suginai `connection` | 接続 wrong vs SK | p.66 「ナ形 だ-(な)/-である」 and p.114 「ナ形 だ-である・名 だ-である」 | both rewritten from the page |
| F12 | g-ni-chigai-nai `official_count` | undercount | 12/2016 問題9-54 key 3 「結果に違いない」 | 3, with the source added |
| F13 | g-zaru-o-enai ex2, g-shika-nai ja usage, g-wake-niwa-ikanai ex3 | lifted fragments | 「イベントは中止せざるを得ない」 is a 10-char run in official 7/2017 聴解 script 6番. 「これは買うしかない」 is SK 23課6 ③ verbatim. 「…わけにもいかず、困っ…」 is SK 18課2 ③'s tail | rewritten. The 10-char scan over refs/**/*.md + tests/imported-* now finds only stock phrases (申し訳ございませんが / しなければならない。…) |
| F14 | vi pane, 20 prose fields | Japanese outside 「」 | e.g. 「(増える, 減る)」, 「男女, 昼夜, 季節…」, 「(知る, 小さい, 新人)」, 「riêng する →」 | quoted. Grammar-label kana (thể ます/た/ない, ナ形容詞) stay as labels |
| F15 | vi g-ni-chigai-nai nuance | contradicts SK | "chủ quan, dựa vào cảm nhận" (subjective, based on feeling), but SK p.111 defines に違いない as 「ある根拠があり」 and names にきまっている as the 主観的・直感的 one. It also contradicted its own usage line (dựa vào dấu hiệu, based on signs) | rewritten: a sign-based conviction vs はずだ's inference from rules and knowledge. The はずだ contrast is kept, and it is correct |
| F16 | all 20 `group` | label migration | 「第N課」 | → 「第1部 N課」 from the inventory |

**Judged NOT findings (the authors' flagged items):**

- g-ni-atatte's マイナス note: SK p.18 says exactly this.
- vi 「雨を問わず」 ✗ / 「天候を問わず」 ✓: correct, and SK p.62 ▲ lists 天候.
- vi 「はずだ」 vs 「に違いない」: the contrast is right; only the "chủ quan / cảm nhận" framing was wrong (F15).
- ja/vi independence: the vi explanations target a different distractor in 9 of 40 items, carry
  Vietnamese-specific traps (Hán Việt mnemonics; "không những…mà còn" = ばかりか, not どころか), and mirror
  no ja sentence. Written, not translated. ✓
- No metadata leaks in either pane.
- Every vi `example_notes` entry is a faithful translation of its example (the four changed ones were
  re-translated).

## 4. Root causes (for B1+)

| finding(s) | code | cause | edit |
|---|---|---|---|
| F1, F2, F3 | RULE-UNENFORCEABLE | The brief says "exactly ONE defensible answer … SOLVE EVERY QUIZ ITEM BLIND". A blind solve finds the best answer; it does not find the second defensible one. All three items passed my own blind solve | R1 |
| F4, F5 | RULE-MISSING | Nothing says a knowledge quiz may not be decided by 接続 alone. The exam rule (qa-review: "printed okurigana selects the key on sight") was never carried over to 知識 | R2 |
| F6, F7, F8, F13 | RULE-UNENFORCEABLE + GATE-BLIND | "never a textbook sentence" is checked by nobody. Authors model sentences on the SK page they just read, one lexical swap away | R3 |
| F12 + inventory miscounts | RULE-WRONG (inventory) | The brief tells authors to use the inventory's `sittings_tested` when `count_confidence` is ok. Measured on this batch it is wrong for 8 of 20 points: a substring hit in ありがたい; ばかりだ merged into 一方だ; でしかない counted as しかない; ないわけにはいかない counted as わけにはいかない; misses at 12/2010-37, 7/2015-39, 7/2011-34. Batch 0 happened to hand-count | R4 |
| F11 | RULE-IGNORED (partial) | The brief says verify 接続 on the page; two entries simplified SK's (な)/である notation | R5 |
| F9, F10 | RULE-MISSING | No instruction to check that each example shows the entry's OWN meaning (ことはない has two readings) | R5 |
| F14 | GATE-BLIND | `check_knowledge.py` has no learner-pane "Japanese outside 「」" check. `exam-model-answer` states the rule and the knowledge SKILL does not import it | R6 |
| blind-solve id leak | PIPELINE-GAP (QA procedure) | the extraction printed entry ids | R7 |

### Exact additions for `BATCH_JA_BRIEF.md` (the coordinator's brief)

Add under "Per entry → quiz" and "Validate":

- **R1 — the distractor splice, written down.** "For each quiz item, write each of the three distractors
  into the stem and name the WORDS IN THE STEM that make it wrong. If the kill rests on an unstated
  assumption ('he surely has no taxi', 'she can't borrow money', 'this is a specific case, not a general
  truth'), write that assumption into the stem as a clause (〜うえに、…もない). Put the splice list in your
  report." (Founding cases: B0 Q34 ことはない, Q35 ことはない/わけにはいかない, Q3 ものだ.)
- **R2 — no form-only keys.** "At least three of the four options must attach grammatically to the
  printed form right before the blank, so the choice is made on meaning. If the stem ends in 未然形
  (使わ), 連用形 (であり), a bare noun, or た形, choose distractors that attach there, or let each option
  carry its own connector (でありながら / であるうえに …). A 接続-only elimination is allowed for at most ONE
  distractor per item, and the explanation must not argue the key by form alone." (Founding cases:
  Q40 「使わ」, Q20 「であり」, Q33 「会社員」.)
- **R3 — provenance scan before hand-off.** "Before you hand off, strip furigana and bold, then check
  every 10-character window of every example and quiz stem against `refs/**/*.md` and
  `tests/imported-*/*.md`. Any hit that is not a stock phrase (申し訳ございませんが, しなければならない。)
  must be rewritten. Also read your sentences against the SK page's numbered examples: same scenario
  plus same predicate (bought clothes → never wore them; no contact info → can't tell them; 彼が〜した
  とは信じがたい) counts as a copy even with the words changed. Change the scenario, not the nouns."
- **R4 — official_count is hand-counted, not copied.** "Treat the inventory's `sittings_tested` as a
  lead list, not a number. Open every cited item in booklet.md, confirm the keyed option IS your form
  (via `refs/JLPT_N2_NEW/answer_keys.json`), and drop hits on look-alikes. Known false-hit shapes:
  ありがたい for がたい, ばかりだ for 一方だ, 名詞＋でしかない for しかない, ないわけにはいかない for
  わけにはいかない. Then grep the booklets for the form to catch misses. `official_count` = sittings you
  confirmed; cite each one in `sources` or list them in your report."
- **R5 — 接続 and meaning, literally.** "Copy SK's 接続 notation faithfully, including optional (な)
  and である: 「ナ形 だ-(な)/-である」 means 静か／静かな／静かである. For a same-form point with two
  readings (ことはない = 必要はない vs 起こらない; ながら = 同時 vs 逆接), check that all three examples and
  both quiz stems show THIS entry's reading. Read each example once as a native editor: does the subject
  fit the predicate?"
- **R6 (learner-language brief, and `jlpt-knowledge/SKILL.md` §Written, not translated)** "In the
  learner pane, every Japanese word or phrase sits inside 「」, parenthesised word lists included; only
  the grammar labels thể ます / thể た / thể ない / ナ形容詞 stay bare." Proposed gate: a WARN in
  `check_knowledge.check_prose_entry` for a learner-language prose field with a kana/kanji run of 2 or
  more characters outside 「」, excluding the labels ます/た/ない/ナ形容詞/イ形容詞. The founding
  measurement is this batch's pre-fix vi file, which gives 20 hits on lexical items (listed in F14).
- **R7 (QA procedure, `jlpt-knowledge/SKILL.md` §Batch workflow step 4)** "The QA extraction prints
  stem and options only, without entry ids or patterns, in shuffled order."

Also worth doing: `references/inventory/N2.md` "Rules for batch authors" should say that
`count_confidence: ok` does not mean the count was verified per hit. The eight miscounts above are the
evidence.

## 5. Coverage

- Blind solve and splice on all 40 items.
- SK page read for all 20 entries (PDF 18, 22, 23, 27, 30, 52, 62, 66, 67, 74, 92, 93, 101, 111, 114,
  115, 119, 123).
- Every cited official item checked against booklet.md + answer_keys.json.
- 10-character provenance scan over all 60 examples and 40 stems.
- Furigana read by hand on every example, stem, and new string.
- Band counts via the gate: all within cap (ja maxima meaning 30 / usage 71 / quiz 75 of 40 / 100 / 80).
- `check_knowledge.py`: 0 content FAIL, 0 WARN. The two stale-page FAILs are blocked (see Verdict).

## 6. Skips

- `make knowledge LEVEL=N2` and `make check` on the real tree: both crash in a concurrent, uncommitted
  `build_model_answer.py` refactor (`LANG_SWITCH_JS` removed; `lang_ui.py` untracked). I did not touch
  those files. I verified the build in a scratch export of HEAD instead.
- I did not ear-check pitch or speech (the 文法 pitch flag is off).
