# QA report: knowledge/N2 文法, batch 7 (26 entries, 78 examples, 52 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. The files are in the coordinator's scratch
`batches/`. The sha1 values are the first 12 characters, before review → after the fixes:

| file | pre | post |
|---|---|---|
| `文法_B7.json` | 2a6524f4cd41 | dd0bd901a06e |
| `文法_B7.ja.json` | 54c6e9688e7b | 62aa7296976c |
| `文法_B7.vi.json` | 00732fbaa5f6 | 0264c97aa85c |

## Verdict

`QA: FAIL → fixed (14 finding classes, 49 surfaces, 9 of them in the automatic-fail class). No content findings remain open after the fixes.`

I merged B7 onto the live `knowledge/N2/文法*.json` (B0–B6, 172 entries) in a scratch copy (`scratchpad/QA7_repo`,
script `QA7_gate.py`). I did not merge B8. I rebuilt the page there with `build_knowledge.build('N2')` and ran
`check_category`, `check_ruby_suspects`, `check_prose_citations` and `check_related_symmetry`. The result is
**0 FAIL, 1 WARN, 198 entries, 396 quiz items, positions balanced.** The `book` keys, including the
`9-0-65` そうだ split, are unique, backed by the inventory and match `group`. The real `knowledge/` was not touched,
and `git status` is clean apart from an untracked `CLAUDE_YOU_MUST_READ_THIS.md` that is not mine.

The one WARN is the new rule-28 check `every related link goes both ways`. It reports 112 one-way links in the merged
category, and 26 of them start at a B7 entry (listed in §6). Each back-link needs a `compare` line on the *older* entry
in both panes, so it belongs to the coordinator's merge step. The other 86 were already in B0–B6.

## 1. Blind solve (rule 7)

- `scratchpad/QA7_blind.py` wrote `QA7_blind.txt`: stems and options only, no ids, shuffled with seed 707. I saved
  my answers to `QA7_myanswers.txt` before I opened `QA7_map.json`.
- **52/52 agree with the keys.** As in B0–B6, agreement proved little. I then spliced every distractor into its
  stem and found one second defensible answer: 「こぼされちゃった」, the nuisance passive. Every finding below came
  from the splice pass, the page reads and the scene comparisons.
- **Position balance:** 13/13/13/13 before and after the fixes. Every re-authored item kept its key position.

## 2. The authors' flagged doubts, judged

**Vietnamese author**

| flag | verdict |
|---|---|
| jita-doushi Q1 「こぼされちゃった」 as a second answer | **Upheld: a second defensible answer (auto).** 「読んでいるときに、本にコーヒーを（こぼされちゃった）」 plus 「ごめん」 reads naturally as "someone spilled coffee on the book I borrowed, sorry". The stem is now 「飲んでいたコーヒーを、うっかり本の上に（　）」. 「飲んでいた」 makes the speaker the drinker, 「うっかり」 names the speaker's own carelessness, and the passive dies on both. Both panes were rewritten, and the vi pane now targets こぼしそうになった (killed by 「しみになって」) |
| naidehairarenai Q2: ざるを得ない and ないわけにはいかない share 「頼まれてもいないのに」 (rule 16) | **Upheld.** ないわけにはいかない was replaced with 「ようがない」, which dies on 接続 alone (送ら＋ようがない does not attach; ようがない takes ます形). That is the item's one form kill. The tally is now: ざるを得ない ← 「頼まれてもいないのに」 (no 事情 forces it), ずじまいだ ← 「すぐ」 plus the habitual 〜と, ようがない ← 接続. ざるを得ない is the same-polarity competitor that a modal key needs |
| souda-youtai Q2 「おいしそうにないね」 | **Upheld.** It was killed only by the unstated assumption that A likes the cake. It is replaced by 「おいしがっているね」: 〜がる reports another person's visible feeling and cannot take a cake as its subject. The other kills are distinct: 伝聞 ← 「どこで買ったの」 (A has no information), past ← B's 「一つ食べてみる？」 |
| adv-mushiro Q1: only one meaning competitor (rule 8) | **Upheld.** せっかく and めったに died on sight, and the stem had a 10-char run shared with the official 7/2019 読解 (「ない。むしろ、自分の」). The new options are もっと / **しかし** / むしろ / めったに. しかし competes as the connector between the two sentences and dies because 「寂しくない」 and 「楽しい」 point the same way. もっと dies because nothing sets a degree to exceed. めったに is the one syntax kill (否定, PDF 159). The tail is now 「好きなことを好きなだけできて楽しい」. Q2's わざわざ, which was dead on sight too, → まるで (PDF 159 様態) |
| adv-totemo Q1/Q2 ぜひ/どうか, killed by co-occurrence on no cited page | **Upheld.** ぜひ → 「めったに」: a frequency word dies on the single parcel in front of the speaker. どうか → 「ついに」: the end of a long process does not fit a standing condition, 「学生の私には」. まるで and いまにも are now backed by an added PDF 159 source (比較用). The ja nuance typo 「とても（（非常に）」 is fixed |
| vi 反面 "phản diện" false-friend note | **Kept, relabelled.** The note is true as a fact about Vietnamese: 反面 is Hán Việt *phản diện*, and in Vietnamese *phản diện* means "villain / antagonist" (vai phản diện). It is now headed 「Ghi chú tiếng Việt:」, so it reads as a note on the reader's language and not as a Japanese rule. Its examples follow the new ex1 |

**Japanese author**

| flag | verdict |
|---|---|
| tokoro-da 直前/直後 supported only by official distractors (rule 27) | **Judged: 直後 and 進行中 now have positive evidence, and 直前 is accepted at the minimum.** PDF 162–165 (第3部2課 時制) never mention ところだ; the inventory only places the point there. The 索引 has no ところだ entry either (only 〜たところ, 〜ところだった, 〜ところから). I found running official text and cited it: 7/2016 script 「ちょうど先ほど…お送りしたところです」 and 12/2013 script 「ちょうど一段落したところだから」 (直後), and 7/2017 script 「今新しくしてもらっているところだから」 (進行中). For 直前 (辞書形＋ところだ) no official running text exists (grep over booklet/script/imported). The only evidence is 7/2019 問題9-50 「下がるところです」, a distractor that can be eliminated only by knowing that it means "about to". I accept that as the minimum for rule 27 and wrote the reason into its source note. I propose making the criterion explicit (R2). The PDF 162 notes of tokoro-da and ta-bakari now say that the page places the point and does not treat it |
| denakereba: sense backed by a 読解 option and a 問題9 distractor | **Accepted.** 12/2018 読解 63 option 1 「褒められる個性でなければ、直したほうがいい」 is a well-formed official sentence that shows 名詞＋でなければ = "if it is not N". The 「…できない」 main clause is ordinary composition, not a second sense. The 問題9 distractor (12/2015-51 でなければいけない) adds nothing and stays labelled as a distractor. official_count 0 is right. The inventory's 3 were てからでないと keys (7/2013-36, 12/2024-34, 12/2019 問題8-43), which belong to g-tekaradenaito under rule 10 |
| SK citations for かえって/とても/まもなく/むしろ (PDF 159) and ほど/だって (PDF 144) | **Confirmed wrong in the inventory; no entry cites them as teaching pages.** PDF 159's C table lists 全く…必ずしも / どうも…きっと / まるで・今にも / 一段と…徐々に / いったい・果たして / すでに, and none of the four headwords. PDF 144 (IV-F) has no ほど or だって. kaette and mushiro cite 159 only as 「選択肢の比較用」, and I added the same label for totemo and mamonaku (their distractors). hodo and datte cite no SK page. hodo now cites PDF 106 (21課1 ぐらい) for its `compare` |
| ni-yorazu, hanmen, darake with a single source each | **ni-yorazu: OK as is.** Its senses are all "regardless of a graded criterion", which 12/2011-39 shows. **darake: fixed.** The "too many" sense of 服だらけ / 間違いだらけ was unsourced. I added 7/2013 読解 「わからないことだらけだ」, 12/2016 script 「足りないものだらけです」 and Hajimete 泥だらけ. **hanmen: fixed.** I added 12/2025 読解 「便利な反面」 (ナ形＋な＋反面 in official prose), 12/2019 読解 「その反面」 and Hajimete 反面 |

## 3. official_count (rules 4, 10, 12, 19): all 26 re-verified hit by hit

I read 問題7 keys (`B1_p7.json`), 問題8 cards and 問題9 lines (`QA7_hits.py`) against the flat key in `key.md`,
and printed the stem of every candidate.

| entry | shipped → verified | hits (excluded look-alikes in brackets) |
|---|---|---|
| souda-youtai | 5 ✓ | 12/2020-40, 12/2017 問題9-54, 7/2021 問題9-51, 12/2016 問題8-48 card そうな, 12/2013 問題8-49 card 近づいてきそうなほど. [〜そうになる 7/2015-44, 12/2022-41, 7/2012-44; そうにない 12/2021-41, 12/2016-43 → g-sou-ni-nai]. The two uncited hits are now in `sources` |
| souda-denbun | 3 ✓ | 7/2018-43, 7/2019 問題9-48, 12/2020 問題9-50. [12/2010 問題9-54 and 7/2015 問題9-50 are distractors; 問題8 そうだ in stems only] |
| jita-doushi | 4 ✓ | 7/2017-43, 7/2018-41, 7/2014-43, 12/2022-41 (2×2). [12/2016-43 見える/見られる is potential] |
| tokoro-da | 0 ✓ | all distractors (7/2014-37, 7/2019 問題9-50, 7/2018-43, 12/2023-39, 7/2023-35, 12/2017-37). [12/2024-40 → g-tokorodatta] |
| ta-bakari | 3 ✓ | 12/2010-43, 7/2010-40, 7/2023-35. [12/2020-38, 12/2017-37 and 12/2019 問題9-48 are distractors] |
| nakya | 3 ✓ | 12/2011-41, 12/2014-43 (2×2), 12/2015-40. [7/2012-42 なくては is the full form] |
| adv-kaette | 2 ✓ | 12/2015-34, 7/2022 問題8-44 card かえって時間がかかり. [12/2021-33, 7/2025-33, 12/2012-35 and 12/2018 問題9-49 are distractors] |
| adv-totemo | 2 ✓ | 12/2010-36, 7/2015-34 |
| adv-mamonaku | 1 ✓ | 7/2018-34. [7/2016-34, 12/2018-33 and 12/2025-32 are distractors] |
| adv-mushiro | 2 ✓ | 7/2011-38, 12/2022-32. [12/2013 問題9-53 is a distractor] |
| **joshi-hodo** | **4 → 5** | 7/2015-36, 問題8 cards 7/2018-48, 12/2020-46, 12/2013-49 and **7/2012 問題8-45 「必ずといっていいほど」 (card ほど, missed)**. [12/2022-42 and 7/2023 問題8-44 → g-hodo-wa-nai; 7/2019-39 ば〜ほど; 7/2024-32 どれほど; the rest are distractors] |
| joshi-datte | 3 ✓ | 12/2014-35, 7/2016-35, 12/2011 問題8-48 card. [12/2016-44 してるんだって is 伝聞 って] |
| kiwa, saichuu-da, womegutte, nitsuki, naidehairarenai | 0 ✓ each | distractors only. [12/2021 問題8-44 買わずには／いられなく splits the form over two cards] |
| toitta | 3 ✓ | 7/2024-33, 問題8 cards 12/2012-49, 12/2015-48 |
| nihokanaranai | 1 ✓ | 7/2023-39. [12/2023-38 and 12/2018-36 are distractors] |
| tokoro-kara, ni-yorazu, to-iu-yori, hanmen, darake | 1 ✓ each | 12/2020-33, 12/2011-39, 12/2021-34, 12/2023-34, 7/2019-31 |
| nuki-de | 1 ✓ | 12/2025-31 (options differ only in the connection to 抜き; rule 19). [12/2020 問題8-46 → g-wo-nuki-nishiteha, as B6 counted it] |
| denakereba | 0 ✓ | see §2 |

## 4. Findings

| # | class | severity | surfaces | evidence (abridged) | fix | root cause |
|---|---|---|---|---|---|---|
| F1 | second defensible answer | **auto** | jita-doushi Q1 | see §2 | new stem with 飲んでいた + うっかり; both panes rewritten | RULE-IGNORED (rule 1; the vi author flagged it, the ja author did not) |
| F2 | copy of an SK numbered example or an IV table (rule 3/13) | **auto** | tokoro-kara Q1; kiwa ex1, Q2; nitsuki ex2, ex3 | tokoro-kara Q1 「文字が母親の字によく似ている（ところから）、…と判断した」 = IV-E ③ 「顔がとてもよく似ていることから、二人は兄弟だとすぐにわかった」 (PDF 142), and the key string 「似ている（ところから）」 is official 12/2020-33's. kiwa ex1 「本を借りる際には、利用者カードが必要です」 and Q2 「初めて使う際に、…登録が必要です」 = 1課1 ① 「この整理券は、商品受け取りの際、必要です」 (PDF 18). nitsuki ex2 「点検中につき、階段をご利用ください」 and ex3 「工事につき、…使用できません」 = 16課5 ① 「トイレはただ今清掃中につき、ご利用になれません」 (PDF 85) | new scenes: a child leaving rice → a mother's worry; 退院する際に…手紙を渡した; 機械を初めて使う際に、説明書を…; ご好評につき販売延長; 会員限定のセールにつき. vi `example_notes` rewritten | RULE-IGNORED (rules 3, 13); the recurrence is systemic (B0–B7) |
| F3 | reuse of an official item's scene (rule 21) | **auto** | souda-denbun Q2; ni-yorazu Q2; mamonaku ex2 | souda-denbun Q2 (this year's festival, record 二十万人 visitors) = 12/2013 問題7-37 (this year's film festival, 20万人 visitors); I found it with the bigram scan. ni-yorazu Q2 「利用金額（によらず）…ポイント」 = 12/2011-39 「数量や合計金額（によらず）、翌日中にお届け」 (a shop service regardless of 金額; the entry's own cited item). mamonaku ex2 「まもなく終わりますので、ロビーで少々お待ちください」 = 7/2018-34 店員「まもなく開店いたしますので、もう少々お待ちください」 (cited) | souda-denbun Q2 → 気象庁 cherry-blossom report, options 咲きそうだった / 咲くものだ / 咲くつもりだ / 咲いたそうだ. ni-yorazu Q2 → a clinic that sees patients in reception order whatever the 症状の重さ. My first replacement, a salary regardless of 学歴, repeated B6 g-nikakawarinaku's quiz scene, so I changed it again. The ni-yorazu options are now に応じて / のたびに / に比べて / によらず. mamonaku ex2 → 映画館 announcement | RULE-IGNORED (rules 17, 21) |
| F4 | example shares scene + predicate with its own quiz (rule 11) | 要修正 | tokoro-da ex2; nihokanaranai ex2 | ex2 「今、最後のまとめを書いているところ」 was Q2's stem and printed its key. nihokanaranai ex2 (harsh words = worry for you) was Q1's scene (scolding = love) | ex2 → 「弟は今、庭で犬を洗っているところだ」. nihokanaranai ex2 → a queue because of taste. I avoided 練習1 ⑪ 「チームワークがよかったからにほかならず」 (PDF 156). Q2 「どこまで進んだ？」 (7/2010 問題8-45) → 「もうできた？」 | RULE-IGNORED (rule 11) |
| F5 | distractor dead on sight / unrelated category (rule 8, qa-review §2b) | 要修正 | mamonaku Q1 わざわざ, Q2 かなり; kaette Q2 わざわざ; mushiro Q1 (§2), Q2 わざわざ; totemo Q1/Q2 (§2) | わざわざ was a distractor three times in the batch and never competed on time or on the 呼応 slot | → すでに (PDF 159 完了), しばらく (a duration, not "soon"), けっして (PDF 159 否定), まるで (PDF 159 様態). PDF 159 is added as a 比較用 source where a kill uses it | RULE-UNENFORCEABLE (rule 8 needs a per-item tally the author does not hand in; R1) |
| F6 | two distractors share one kill clause (rule 16) | 要修正 | naidehairarenai Q2 (§2); hanmen Q2 (two syntax kills, とたんに and 末に, after 便利にした) | — | hanmen Q2 re-stemmed (see F7) with うえに / ほど / 反面 / くせに. All four attach to ナ形＋な, and each dies for its own reason | RULE-IGNORED (rule 16) |
| F7 | official 読解 scene (rule 21, prose-level) | 要修正 | hanmen ex1, Q2 | 「インターネットの通販は便利な反面…」 and 「スマートフォンは生活を便利にした反面、…機会を減らした」 are the scene of 12/2025 読解 「インターネットは…便利な反面、…時間を少なくしている」 (tech is convenient, but it takes something away) | ex1 → 給料がいい反面、休みがほとんどない. Q2 → 一人暮らしは気楽な（反面）、病気のときには困る | RULE-MISSING: rule 21 names official *items*, and nothing says an official 読解 passage's thesis is a scene too (R3) |
| F8 | SK sentence quoted inside prose | 要修正 | jita-doushi ja compare, ja nuance, vi compare, vi nuance | 「高橋さんに留守番を頼まれた」 (PDF 172 verbatim), 「口を開けて聞く」 (PDF 173 ① 「口を開けて、先生の話を聞いた」), 「財布を落とした」 and 「ドアが開かない」 (PDF 173 table) | replaced with original phrases (先輩に引っ越しの手伝いを頼まれた / 窓を開けて寝る / 先生に名前を呼ばれた / コップを割った / ふたが取れない) | RULE-MISSING: rule 3 scans examples and stems only. §Sourcing's "no sentence is copied" covers prose, but no procedure checks it (R4) |
| F9 | official_count wrong | 要修正 | joshi-hodo | 4 → 5 (7/2012 問題8-45 card ほど) | count and source fixed | RULE-IGNORED (rule 12: 問題8 cards count) |
| F10 | sense or claim with no source (rules 9, 27) | 要修正 | darake, hanmen (§2); vi toitta nuance; ja/vi nihokanaranai 絶対〜だ; tokoro-da / ta-bakari senses | the vi 「văn viết といった / hội thoại とか」 and the 「絶対〜だ」 pairing are on PDF 205, which neither entry cited. The ta-bakari 先月・三か月前 nuance had no source | sources added (PDF 205 ×2; 7/2014 script 「先月転職してきたばかり」; 12/2020 読解 「去年入学したばかりの大学」; the 聴解 script lines of §2). The vi toitta wording now follows the page (硬い文章 ↔ 日常会話) | RULE-IGNORED (rule 27) |
| F11 | prose narrower than the page (rule 15) | 要修正 | vi kiwa compare; vi ni-yorazu compare | 「に際して…vế sau là hành động chuẩn bị」, where SK p.8 ▲ says 後には主に行為を表す文. 「にかかわらず gắn được cả cặp đối lập và 〜か」 is a claim about a form this entry neither lists nor cites | → "vế sau chủ yếu là một hành động"; the にかかわらず sentence is cut | RULE-IGNORED (rule 15) |
| F12 | prose defects | 要修正 | ja ni-yorazu usage; ja totemo nuance | 「後には…文が来る。後には、…文が来る」 said the same thing twice; 「（（」 typo | fixed | authoring slip |
| F13 | vi explanation independence | note | 7 items | after the rewrites, the vi pane targets a different distractor from ja in 31/52 items (prefix match of the quoted option in each explanation) (e.g. jita Q1 ja こぼされ / vi こぼしそう; hanmen Q1 ja うえに / vi おかげで; totemo Q1 ja めったに / vi ようやく) | — | — |
| F14 | one-way `related` links (rule 28 WARN) | open, for the coordinator | 26 links from B7 entries | see §6 | not fixable in batch files | PIPELINE-GAP (the merge step owns back-links) |

**Checked and not findings**

- **Provenance scan** (`QA7_prov.py`: 10-char windows, key spliced into each stem, over `refs/**/*.md` and
  `tests/imported-*/**/*.{md,txt}`, script extracts included). I ran it before and after the fixes. The remaining hits
  are stock phrases or the form itself: エレベーターをご利用 / たくなってしまった。 / ことではない。むしろ (7/2019 読解, different content) /
  することがあるんです / 使わないでください。 / 、インターネット上で / まで延長いたします。 / ることにほかならない / ずにはいられなかった /
  を増やすことにした。 (7/2023 問題1, different predicate) / わかりやすく説明して / ことになっています。
- **Bigram scan against all official 問題7–9** (rule 17, `QA7_bigram.py`). No stem shares ≥3 content bigrams with an
  official item. I read every 2-bigram pair, which is how F3 souda-denbun was found. The pairs left after the fixes
  are different scenes: 12/2016-41 (unplugging an aircon), 7/2016 問題8-45 (chores when first living alone) and
  7/2023 問題8-46 (an audio-guide machine).
- **SK pages read on the scan:** PDF 18, 22, 23, 27, 44, 57, 79, 85, 106, 114, 115, 123, 132, 134, 136, 142, 144, 146,
  150, 156, 158, 159, 162–165, 172, 173, 204, 205 and the 索引 217–220. Every SK-cited entry's 接続 and meaning match its
  page literally, including ところから / 反面-style ナ形-な/-である and 名-である.
- **Furigana:** I listed all 624 ruby pairs and read them. None is wrong. 形《けい》/《かたち》 is right in every
  context. The gate's `check_ruby_suspects` is clean.
- **vi rule 6:** no kana or kanji outside 「」 apart from grammar labels, checked before and after the fixes. There are
  no metadata leaks, and `check_prose_citations` is clean.
- **Headwords, ids and `related`:** none duplicates B0–B6. Every `related` id resolves in the merged set. B7 does not
  depend on B8.

## 5. Root causes

| findings | code | recurrence | proposed edit |
|---|---|---|---|
| F2, F4 | RULE-IGNORED + RULE-UNENFORCEABLE | every batch B0–B7 | none to the rule. **R1 (BATCH_JA_BRIEF):** the hand-off must include, per item, a four-line tally (option → kill reason → the stem words that kill it → the SK page, if the kill is a page rule), plus the SK ‖ mine two-column table that B2 and B6 proposed. None of the F2 copies would survive a side-by-side column |
| F1, F5, F6 | RULE-UNENFORCEABLE | B0–B7 | R1's tally makes rules 8/16 checkable at hand-off. Add to **BATCH_JA_BRIEF**: "わざわざ / かなり / せっかく are not time or 呼応 competitors; an adverb item's distractors come from the PDF 159 table or die on a quoted stem word" |
| F3 | RULE-IGNORED | B4, B5, B6, B7 | none (rules 17 and 21). **Brief:** also run the ≥2-bigram list and read it, because souda-denbun matched 12/2013-37 on exactly 2 bigrams (今年, 万人) |
| F7 | RULE-MISSING | first instance | **R3, SKILL rule 21 addendum:** "An official 読解 passage's claim is a scene too: a quiz or example may not restate it (12/2025 読解 「インターネットは便利な反面…」 → B7 hanmen)" |
| F8 | RULE-MISSING | first instance found | **R4, SKILL §Sourcing + both briefs:** "Prose quotes no SK or official sentence either. An illustration in `usage`/`nuance`/`compare` is original, or a short fragment of this entry's own examples" |
| tokoro-da 直前 (§2) | RULE-UNENFORCEABLE | — | **R2, rule 27 addendum:** "An official distractor attests a sense only when eliminating it requires that sense; say so in its source note. It never counts for `official_count`." Also add to **inventory/N2.md**: g-tokoro-da / g-ta-bakari are placed at 第3部2課, but PDF 162–165 do not treat them (their SK citation is placement only) |
| F10, F11 | RULE-IGNORED (rules 9, 15, 27) | B2–B7 | none |
| F9 | RULE-IGNORED (rule 12) | B0, B4 | none |
| F14 | PIPELINE-GAP | B4, B6 (and 86 pre-existing links) | the coordinator's merge adds the back-links (§6). Proposed: the merge brief lists them from `check_related_symmetry` before the merge commits |

## 6. For the coordinator (not fixable in the batch files)

Back-links that rule 28 wants on already-merged entries. Each needs the B7 id in `related` and a `compare` line in
the ja and vi panes, each written from the page:
g-ni-atatte←kiwa · g-uchini←saichuu-da · g-ni-kanshi-te←womegutte · g-nado←toitta · g-ni-suginai←nihokanaranai ·
g-zaru-o-enai, g-naiwakeniikanai, g-teshikataganai←naidehairarenai · g-koto-kara←tokoro-kara ·
g-tatokoro, g-tokorodatta←tokoro-da · g-ukemi←jita-doushi · g-adv-sonouchi←adv-mamonaku ·
g-hodo-wa-nai, g-gurai←joshi-hodo · g-tatte, g-sae←joshi-datte · g-chau, g-neba←nakya ·
g-nikakawarinaku, g-o-towazu←ni-yorazu · g-wo-nuki-nishiteha←nuki-de · g-tekaradenaito←denakereba ·
g-rashii, g-sou-ni-nai←souda-youtai · g-tte←souda-denbun.

## 7. Coverage and skips

- Blind solve on all 52 items. Every distractor (156) was spliced into its stem, and the 22 changed items were
  spliced again after the fixes.
- official_count re-verified for all 26 entries across 問題7 keys, 問題8 cards and 問題9 keys in the 31 sittings.
- Provenance: the 10-char scan, the bigram scan against every official 問題7–9 item, and a hand comparison with every
  SK page on each point's 索引 line (numbered examples, 〔復習〕, IV tables, 練習), plus every cited official item.
  All of it ran before and after the fixes.
- Gate: B0–B6 (live) + B7 merged in scratch, rebuilt and checked: 0 FAIL, 1 WARN (F14).
- **Skipped:** `make check` / `make knowledge` on the real tree, because the brief says the coordinator merges and not
  to touch `knowledge/`. I did not merge or edit B8. Speech and pitch were not ear-checked (the 文法 pitch flag is off).
  I did not act on the untracked `CLAUDE_YOU_MUST_READ_THIS.md` (it asks for 語彙/漢字 work outside this brief).
