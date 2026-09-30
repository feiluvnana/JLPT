# QA report: knowledge/N2 文法, batch 2 (25 points, 75 examples, 50 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of this batch.
Files are in the coordinator's scratch `batches/`. Sha1 values are the first 12 characters, pre-review → post-fix.

| file | pre | post |
|---|---|---|
| `文法_B2.json` | 32342f2839ef | 197f09514d7c |
| `文法_B2.ja.json` | 674b5863e2ad | 008a8cae85fa |
| `文法_B2.vi.json` | 5da1a116d311 | 27124b1d779c |

## Verdict

`QA: FAIL → fixed (22 findings; 5 in the automatic-fail class). 0 content findings open after the fixes.`

I validated the result with the gate's own script on a scratch repo copy (`scratchpad/QB2_repo`). It has the real
`.agents/` and `knowledge/`, refs/tests/tools symlinked in, and batch 0+1+2+3 merged into `knowledge/N2/文法*.json`.
I rebuilt it with `build_knowledge.py --level N2` and then ran `check_knowledge.py`: **0 FAIL, 0 WARN**, with
97 entries, 194 quiz items and positions balanced. The real `knowledge/` is untouched (`git status` is clean
apart from this report).

## 1. Blind solve

I solved from `scratchpad/QB2_blind.txt`: stems and options only, no ids, shuffled with seed 20260930. My answers
went into `QB2_myanswers.txt` before I opened `QB2_map.json`.

- **50/50 agree with the keys.** As batch 0 already showed, agreement proves little. Seven of the items below
  passed the blind solve and still had a second defensible answer, a form-only kill, or a template stem. I found
  them only by splicing each distractor into its stem.
- Batch position balance is 12/12/13/13, unchanged by the fixes (no key moved).

## 2. Per-entry walkthrough

"SK p." is the PDF page (index book page +10). Every SK page was read on the scan. Official counts were checked
hit by hit in `booklet.md` 問題7–9 against `answer_keys.json`, using my own scripts `QB2_hits.py` / `QB2_key.py`.
問題8 cards count, per `bunpou.md` §Inventory.

| entry | SK p. | 接続 / meaning vs source | official_count (verified) | verdict |
|---|---|---|---|---|
| g-hazu | SK外 | ✓ | **5 → 6**: 7/2010-43 k1, 7/2017-44 k1, plus 問題8 cards 12/2010-48, 12/2012-48, 7/2016-48, 7/2019-47 | count fixed (F8); Q1 explanation fixed (F17) |
| g-bekida | 115 ✓ | ✓ literal (する→するべき・すべき; べき＋名) ▲ 規則には使わない / 目上には直接使わない | 2 ✓ (7/2023-41 k3; 7/2014 問題8-46 card すべき) | ex1 changed (F21) |
| g-koto-ni-naru | SK外 | ✓ | **5 → 4**: 7/2021-41, 7/2022-41, 12/2016-42, 12/2019 問題9-51 (こととなる). 7/2024-41 「ということになる」 is B3 `g-to-iu-koto-ni-naru`'s hit | count and source fixed (F10); Q1 fixed (F3); nuance cut (F13) |
| g-sura | SK外 (107 さえ) | ✓ | 4 ✓ (7/2021-31 = 12/2011-34, 7/2023 問題8-43, 12/2013 問題8-48 「疑問にすら」) | Q2 fixed (F6) |
| g-fukugou | SK外 | ✓ | **5 → 6**: 7/2019-36, 12/2020-40, 7/2021-38 & 39, plus 問題8 cards 12/2013-49 (動き出して), 12/2015-47 (治りかけていた), 12/2016-48 (動き出し) | count fixed (F8); Q2 explanation fixed (F17) |
| g-keigo-o-ni-naru | 204 (context only) | ✓ | **2 → 1**: 12/2011-44 only. 12/2016-38 「お越しになりました」 is B3 `g-keigo-okoshi`'s. 7/2016-37 おいでになる is also a special verb | count and source fixed (F10) |
| g-koso | 106 復習 ✓ | ✓ | 3 ✓ (12/2020-32, 12/2012-33, 12/2010 問題8-49 card) | nuance claim cut (F13) |
| g-keigo-mousu | SK外 | ✓ | 4 ✓ (12/2010-39, 12/2022-40, 12/2025-41, 7/2018-39) | OK |
| g-kotodarou | 127 ✓ | ✓ literal (疑問詞＋普通形, ナ だ-な/-である, 名 だ-である) ▲ 程度の疑問詞・なんと・いったい | **0 ✓**: no keyed ことだろう/ことか in any 問題7–9 | nuance claim cut (F13) |
| g-toittemo | 75 ✓ | ✓ (名・普通形) | 3 ✓ (7/2010 問題8-46 card, 12/2023 問題8-46 card, 7/2023 問題9-48 k3) | ex2 template (F12); compare fixed (F14) |
| g-sae | 107 ✓ | ✓ A/B; ▲A 「後には話者の意向・働きかけの文は来ない」 backs 3 explanations in the batch | 3 ✓ (12/2024-31 k3, 12/2013-33 k4, 12/2011 問題8-46 card) | Q2 fixed (F2) |
| g-tabi-ni | SK外 | ✓ | 4 ✓ (12/2022-37, 7/2013-42, 7/2022 問題8-43 card, 12/2017 問題8-49 card) | OK |
| g-ni-oite | 132 ✓ | ✓ (場所・分野・時期, 硬い) | 3 ✓ (12/2013-34 k4, 12/2016-35 k2, 7/2025 問題9-51 k1) | Q1 template (F11); Q2 second answer (F1) |
| g-keigo-ukagau | 204 (context only) | ✓ meaning | 2 ✓ (7/2021-40 k4, 7/2024-42 k2) | compare claim cut (F15) |
| g-gurai | 106 ✓ | ✓ literal (ナ だ-な); ▲ 名詞には「ぐらい」が多い | 2 ✓ (12/2011-35 k4, 12/2015-41 k3) | OK (flagged Q1 judged OK, below) |
| g-tedemo | 107 ✓ | ✓ (動て形＋でも; ▲ 後には希望・意向) | **0 ✓**: only distractors (7/2022-34, 7/2014-?, 12/2014-40 「となってでも」) | nuance claim cut (F13) |
| g-koto-ni | 139 ✓ | ✓ (動た形・イい・ナな) | 1 ✓ (7/2021-36 k1) | OK |
| g-koto-kara | 142 ✓ | ✓ literal | 3 ✓ (7/2022-37 k4, 7/2024 問題8-43 card, 12/2018 問題8-46 card) | ex1 copy (F12) |
| g-tatte | 205 ✓ (であっても/だって row) | ✓ | 1 ✓ (12/2025-42 k2; 12/2014-35 and 7/2016-35 are も-meaning だって) | OK |
| g-kotoda | 118 ✓ | ✓ ▲ 過去・否定・疑問の形はない / 意志動詞 / 目上には使わない | **0 ✓** | Q1 fixed (F4) |
| g-kotoda-26-5 | 127 ✓ | ✓ (イい・ナな; 動た形) | **0 ✓** (12/2024 問題9-50 key is 4, not 「感動したことだ」) | OK |
| g-karaniha | 89 ✓ | ✓ literal (ナ/名 だ-である; 上は 辞書形/た形) | 3 ✓ (12/2025-34, 12/2016-37, 12/2021 問題8-43 card 以上は) | ex3 template (F12); nuance claim cut (F13) |
| g-nishiteha | 96 ✓ | ✓ literal | 2 ✓ (7/2018-33 k3, 7/2025 問題8-44 card) | Q2 template + weak distractors (F7) |
| g-towa-iinagara | 134 ✓ (とはいいながら only; とはいえ is not in the SK index) | ✓ | 3 ✓ (7/2010-42 k3, 12/2013 問題9-53 k4, 7/2014 問題9-52 k2) | nuance/compare claims (F14) |
| g-ka-douka | SK外 | ✓ | 6 ✓ (12/2010-44, 7/2025-37, 12/2024-37, 問題8 cards 7/2019-46, 12/2016-49, 7/2016-49 疑問節) | Q2 fixed (F5); nuance claim (F13) |

**The authors' flagged doubts, judged:**

- **たって Q1 「今から走っ（たら）、もう間に合わないよ」: OK.** It is a meaning kill, which rule 2 asks for. たら is a plain
  conditional, and "if you run you won't make it" contradicts what running does. Only the concessive fits.
- **すら Q2 (として/にとって/に対して): finding F6.** All three die for reasons unrelated to "even" (にとって needs an
  evaluative predicate). Replaced with だけに / でこそ / として.
- **伺う compare, "参る does not raise the place visited": finding F15, in both panes.** The 謙譲語I/II claim is
  standard 敬語の指針 doctrine. It is not on SK p.194, which the entry cites: that page is 第3部12課 文体の一貫性
  (硬い文章では読み手への敬語を使わない), and nothing in refs/ backs the claim. I cut it and replaced it with a
  meaning contrast (参る = 行く・来る only, with no 聞く sense).
- **ことになる Q1, ことがある killed by 「会社の決定で」: finding F3.** 「来年から…担当することがある」 ("from next year
  there will be times I handle it") is grammatical and not absurd. The doubt resolves against the item.
  Replaced with ことか.
- **ぐらい Q1 「メールすら送ってくれてもいい」: OK.** The kill is not just "unnatural". SK p.107 ▲ (さえA) says 「後には
  話者の意向を表す文や働きかけの文は来ない」, and 「〜てくれてもいいじゃないか」 is a 働きかけ. The entry itself treats
  すら as さえA's synonym. The ja explanation already argues it this way.
- **The official_count zeros: 4, not 5.** ことだろう・ことか, てでも, ことだ(忠告) and ことだ(感嘆) are the only zeros
  in the batch. All four are confirmed 0 by a 問題7–9 grep plus key lookups. No fifth zero exists.
- **g-ka-douka Q2 「会議で何を話す（　）」: finding F5.** のは, ことは and ほど all die by one syntax rule (疑問詞 needs
  か), so the item was a one-choice item.
- **g-gurai Q1 "weakest kill": OK, as above.**
- **伺う vs 参る against SK p.194: unchecked-able. Cut (F15).**
- **g-koto-ni-naru's 「ことになりました」 modesty claim: finding F13, both panes.** No ref backs it. It was replaced
  in ja by a meaning statement ("tells the result without naming who decided") and dropped from vi.

## 3. Findings

| # | item | class | evidence | fix |
|---|---|---|---|---|
| F1 | g-ni-oite Q2 | second defensible answer (auto) | 「子どもの成長（に沿った）遊びの役割は、非常に大きい」 = "the role of growth-appropriate play is large". It is grammatical and sensible | に沿った → に反する. Both panes rewritten |
| F2 | g-sae Q2 | form-only kills (auto, rule 2) | 「地元の人で（　）」: だけ and なら do not attach after 「で」. That is two 接続-only eliminations | options now carry their own connector: でさえ / でこそ / だけあって / として. Both panes rewritten |
| F3 | g-koto-ni-naru Q1 | second defensible answer (auto) | 「会社の決定で、来年から私が担当する（ことがある）」 is grammatical and plausible | ことがある → ことか |
| F4 | g-kotoda Q1 | second defensible answer (auto) | 「緊張しないためには、前の日に何度も練習しておく（ことはない）」 reads as coherent advice ("don't over-practise"). Stem also followed SK 24課2 ① 「〜ためには…しておくことだ」 | new stem ends 「…練習しておく（　）。それが一番の方法だ。」, which kills ことはない. Both panes rewritten |
| F5 | g-ka-douka Q2 | one-choice item (auto, rule 2 in spirit) | のは/ことは/ほど all die by the single 疑問詞 rule; the ja explanation killed them in one clause | stem 「会議で何を話す（　）、まだ決めていない」, options かどうか / ことか / か / にしても: one rule kill (かどうか), two meaning kills. Both panes rewritten |
| F6 | g-sura Q2 | distractors dead for an unrelated reason | にとって/として/に対して do not compete on "even" | → ですら / だけに / でこそ / として. Both panes rewritten |
| F7 | g-nishiteha Q2 | SK template + weak distractors | 「今日は日曜日（にしては）、公園に人が少ない」 ≈ SK 19課2 ① 「今日は2月にしては暖かかった」; として/において/にとって are weak | new stem 「今日の彼女は、プロの歌手（　）高い声がよく出ていなかった」, options だけあって / にとって / をはじめ / にしては. SK p.96 ▲ だけあって＋高い評価 kills the main rival. Both panes rewritten |
| F8 | g-hazu, g-fukugou official_count | undercount | 問題8 card hits never counted: 4 for はず, 3 for 複合動詞 | 6 and 6 |
| F10 | g-koto-ni-naru, g-keigo-o-ni-naru official_count | double count across batches | 7/2024-41 「ということになる」 is cited by B3 g-to-iu-koto-ni-naru; 12/2016-38 「お越しになりました」 by B3 g-keigo-okoshi | 5 → 4 (source swapped to 12/2016-42); 2 → 1 (source removed) |
| F11 | g-ni-oite Q1 | SK template | 「決勝戦は…市民競技場（において）行われる」 ≈ SK IV-A ① 「本日A館において就職説明会が行われる」 (event held at a venue) | new stem 「今回の調査（　）、若者の読書時間が年々減っていることがわかった」, options において / にとって / に対して / をめぐって |
| F12 | g-koto-kara ex1, g-karaniha ex3, g-toittemo ex2 | textbook template ×3 | 「昔近くに大きな市場があったことから『市場前』という名前になった」 ≈ SK IV-E ① (名前の由来 → 名前がついた). 「家を買うと決めた上は、…なければならない」 ≈ SK 17課5 ⑥ 「会社を辞めると決めた上は、…必要がある」. 「英語が話せるといっても、旅行で困らない程度です」 ≈ SK 14課5 ② 「料理ができるといっても、…簡単なものだけです」 | new: 「利用者が年々減っていることから、このバス路線は来年の春で廃止されることが決まった」 / 「チームの代表に選ばれた上は、全力を尽くすつもりだ」 / 「休みを取ったといっても、午前中の半日だけです」. vi notes re-translated |
| F13 | ja nuance of g-koto-ni-naru, g-kotodarou, g-ka-douka, g-karaniha, g-koso, g-tedemo; vi nuance of g-koto-ni-naru, g-karaniha | claims no ref backs | 「ことになりました」は控えめで丁寧 / 会話では「何度言ったかわからない」 / のかどうか＝迷い / 「上は」は最も硬い / こそ はマイナスの結果にあまり使わない / てでも は他人を批判する文に使わない | cut, or replaced by what SK's ▲ or the archive states (e.g. g-ka-douka: 「〜のかどうか」「〜のか」が試験によく出る = 12/2010, 7/2025, 12/2024) |
| F14 | ja compare of g-toittemo and g-towa-iinagara; ja nuance of g-towa-iinagara; vi compare of g-towa-iinagara | unbacked contrasts | 「とはいえ…後には話し手の意見や判断が来る」 contradicts towa's own usage (実際の状態 too). The ながらも/ものの "less 反論" ranking has no ref | rewritten from SK p.75 (イメージとの違い) and p.134 (予想との違い), plus the archive count (とはいえ ×3, とはいいながら ×0) and the syntactic fact that ものの/ながらも cannot open a sentence |
| F15 | g-keigo-ukagau compare, both panes | unbacked claim | 謙譲語I/II "raises the person visited" is on no cited page | meaning contrast instead |
| F16 | g-koso usage | trimmed | 「文末に『のだ』が来ることが多い」 moved to nuance so the removed claim's slot is not empty | — |
| F17 | g-hazu Q1, g-fukugou Q2 (ja explanations) | false kill | 「ことはない…可能動詞には合わない」: 話せることはない is grammatical, and the kill is meaning. 「きった…待つという動作には使わない」: 待ちきれない is everyday | rewritten to meaning kills |
| F21 | g-bekida ex1 | in-category echo | 「約束の時間に遅れるなら、前もって連絡するべきだ」 is the same scene as g-gurai Q1 「約束に遅れるなら、メールぐらい…」 | → 「使わない部屋の電気は、こまめに消すべきだ」 |

(F9, F18–F20 are not used; numbering follows my working notes.)

**Checked and not findings:**

- Provenance: my own 10-char scan (`QB2_prov.py`) over refs/**/*.md, tests/imported-*/**/*.md and *.txt was run
  before and after the fixes. It finds only stock phrases: よろしくお願いいたします / たことがありますか / ご連絡申し上げます /
  さなければならない / コミュニケーションの / がわかるようになった.
- Furigana: all 987 ruby pairs listed and read. None wrong.
- vi rule 6: no kana/kanji run outside 「」 (`QB2_viq.py`, labels excluded).
- vi `example_notes`: all 75 faithful; the four changed examples were re-translated.
- ja/vi independence: the vi explanations target a different distractor in about half the items (g-hazu Q2
  ことだ vs 次第だ; g-kotoda Q2 ものか vs わけだ; …). No mirrored framing.
- No metadata leaks in either pane.
- `related`: all 25 entries' ids resolve (B0, B2, B3). No headword collides with B0, B1, B3, B4 or B6.
- The authors' remaining register tags and remarks (すら 硬い, ことに 少し硬い, はず 意志には使わない) were left as
  ordinary usage notes. They are not contrastive claims, but none is on a cited page.

## 4. Root causes

Recurrence: the second-answer, form-only kill, SK template and miscount classes all shipped in B0 as well. That
makes them two papers' worth, so they are systemic by definition.

| findings | code | cause | proposed edit |
|---|---|---|---|
| F1, F3, F4 | RULE-IGNORED + RULE-MISSING | R1 (splice) was binding, and the author even FLAGGED F3 as a doubt, but kept it. The author briefs lack the qa-review ground rule "doubt resolves against the item" | `BATCH_JA_BRIEF.md`: "**A distractor you had to defend in your report is a replaced distractor.** If you list an item as a doubt, replace the option before hand-off." |
| F2 | RULE-IGNORED (R2) | the printed form before the blank included a particle (人**で**), and two options died on it | R2 addendum: "The printed form includes any particle printed before the blank (〜で, 〜に). If options must differ in connector, put the connector in each option." |
| F5 | RULE-MISSING | R2 counts attachment to the printed form only. Three options can attach to 話す and still all die by ONE co-occurrence rule (疑問詞＋か) | SKILL §Quiz integrity rule 2 addendum: "At most one distractor may die by a pure syntax or co-occurrence rule. If your explanation kills three options in one clause, the item is a one-choice item." (the exam-qa-review §2b tell) |
| F6, F7 | RULE-MISSING | exam-qa-review §2b ("a distractor eliminable on sight for a reason unrelated to the tested point") was never carried into the knowledge rules | SKILL §Quiz integrity: new rule 8, "each distractor competes on the tested meaning; name the meaning contrast it fails on" |
| F7, F11, F12 (5 surfaces) | RULE-UNENFORCEABLE | R3's "compare with SK's numbered examples" is carried out from memory. The string scan passes all five | `BATCH_JA_BRIEF.md` R3: "In your report, give a two-column table per entry: SK's numbered examples (scenario + predicate) beside each of your examples and stems. A row that matches both columns is rewritten." This is verifiable after the fact |
| F8 | RULE-UNENFORCEABLE (R4) | authors counted 問題7 keys and missed 問題8 cards | R4 addendum: "grep the whole 問題7–9 block, 問題8 cards included (bunpou.md §Inventory rule 2)" |
| F10 | RULE-MISSING (not gate-decidable) | one official item was credited to two entries in different batches, where one entry's headword contains the other's form (ということになる ⊃ ことになる; お越しになる is a special verb, not productive お〜になる) | I ran the obvious gate predicate: the same `M/YYYY 問題N-K` in two entries' `sources[].note`, over B0 + B1–B4 + B6. It fires on **27** citations before the fix and 25 after. Most are legitimate: a key that carries two points (「言ってくれるたびに」 = てくれる + たびに; 「にすぎないとはいえ」), or a note that cites a distractor. **The duplicate is the trigger, never the verdict, so no gate check.** Proposed R4 addendum for the batch briefs: "Before counting a hit, check whether another entry in knowledge/ or batches/ has the keyed string itself as its headword. If so, the hit is that entry's, not yours." |
| F13, F14, F15 | RULE-MISSING (author briefs) | only the QA brief says "claims no ref backs are verified or cut". The author briefs ask for depth and nuance, so authors supply textbook-lore pragmatics | `BATCH_JA_BRIEF.md` + `BATCH_VI_BRIEF.md` + SKILL §Sourcing: "Every contrastive or pragmatic claim (X is more formal than Y, X is used to sound modest, X ranks the addressee) must be on a cited page or countable in the archive. Otherwise leave it out." |
| F17 | RULE-UNENFORCEABLE | "the explanation says what rules the strongest distractor out" does not require the stated rule to be TRUE. Two explanations invented a restriction | SKILL §Quiz integrity: "a kill is either a meaning contradiction with a quoted stem word, or a rule printed on the entry's cited page. Never an invented usage restriction." |
| F21 | RULE-MISSING (minor) | nobody reads examples against the category's quiz stems | brief line: "no example may share scene + predicate with any quiz stem in the category" |

## 5. Coverage

- Blind solve and distractor splice on all 50 items. The 7 changed items were re-solved and re-spliced after the fix.
- SK pages read on the scan: 75, 89, 96, 106, 107, 115, 118, 127, 132, 134, 139, 142, 204, 205, plus the 索引
  (217–220), to confirm which points are SK外.
- `official_count`: all 25 entries were re-verified hit by hit, including every count ≥5 and every 0.
- Bands (gate): ja maxima are meaning 37, usage 85, nuance 72, compare 77, quiz 78 (caps 40/100/100/100/80). vi
  maxima are 61, 167, 165, 169, 143 (caps ×1.8 = 72/180/180/180/144). vi quiz is at 143/144, flush against the cap.
- Gate: `check_knowledge.py` on the merged scratch copy (B0 + B1 + B2 + B3) after `build_knowledge.py`: 0 FAIL,
  0 WARN.

## 6. Skips

- I did not run `make knowledge` or `make check` on the real tree. The brief forbids touching the real `knowledge/`,
  and the coordinator merges. The gate ran on the scratch copy instead.
- I measured a duplicate-citation gate check (F10) and rejected it: it fires on 25 legitimate shared citations. No
  gate edit is proposed for it.
- No pitch or speech check (文法 pitch is off).
