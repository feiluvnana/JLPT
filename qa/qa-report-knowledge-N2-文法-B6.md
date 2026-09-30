# QA report: knowledge/N2 文法, batch 6 (25 points, 75 examples, 50 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. Files are in the coordinator's
scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `文法_B6.json` | 351d0e4a09be | f7bc1a079725 |
| `文法_B6.ja.json` | e119a21c0767 | 777890726def |
| `文法_B6.vi.json` | b0a35152ad55 | 1af3bd7ac0d5 |

## Verdict

`QA: FAIL → fixed (9 finding classes, about 70 surfaces fixed, 12 of them in the automatic-fail class). 0 content findings are open after the fixes.`

I merged B6 into a scratch copy of `knowledge/` (`scratchpad/QA6_repo`, with batch 0–3 already merged there, 122 entries), rebuilt it with
`build_knowledge.py --level N2` and ran `check_knowledge.py`: **0 FAIL, 0 WARN**. Answer positions are 244 items, balanced. The real
`knowledge/` was not touched. (`git status` shows `.agents/exam-model-answer/scripts/lang_ui.py` modified. That edit is another context's,
not mine.)

## 1. Blind solve (rule 7)

- `scratchpad/QA6_blind.py` wrote `QA6_blind.txt`: stem and options only, no ids, shuffled with seed 606. I saved my answers to
  `QA6_myanswers.txt` before I opened `QA6_map.json`.
- **50/50 agree with the keys.** As in B0–B3, agreement proved little. Every finding below came from the splice pass or the page comparison.
- **Position balance:** 12/13/13/12 before and after the fixes. Every re-authored item kept its key position.

## 2. The authors' flagged doubts, judged

| flag | verdict |
|---|---|
| ni-sakidatte 接続 inferred from IV-A | **OK, note added.** PDF 132 has no 接続 line. Its example ① 「野外実験を行うに先立って」 shows 動詞辞書形, and ② 「イベントに先立つパレード」 shows 名詞＋に先立つ＋名詞. Official 12/2022 問題8-47 (card 「に先立って」 after 「行う」) confirms the dictionary form. The source note now says where the 接続 comes from. |
| 5 SK外 接続 (nikui, nara-tomokaku, kkonai, te-wa-douka, to-iu-you-ni) | **OK.** Each matches its official keyed forms: 集まりにくい (7/2025 問題8-45); デートで着るならともかく (12/2021-36); 当たりっこない (7/2016-40); 取り上げてみてはどうか / 気をつけてみたらどう (7/2018-44, 12/2010 問題9-54); 冬はスキーというように, 「…。」というように, 意味があるのかというような (7/2017-41, 7/2023-36, 12/2024-37). The SK 索引 (PDF 217–220) has none of the five. |
| tenaranai Q2 「寂しくなるおそれがある」 | **Replaced.** It was killed only by register, so rule 14 applies. The whole stem was also moved off a friend-leaving scene (see F2). The new option 「情けなくなるはずがない」 contradicts 「失敗が続いていて」. |
| nikui Q2 「読みそうだ」 | **Replaced** (with がちだ; see F3). |
| nikui Q1 「歩きかねる」 | **Replaced. It was a second defensible answer.** SK p.82 (PDF 92) defines かねる as 「その状況・その条件・話者の立場では〜できない」, and "under the condition of heavy shoes" fits that definition. The ▲ 「能力的に…使わない」 is exactly the argument a hostile solver turns around. The options are now やすい / にくい / たくなる / すぎる. |
| nado distractors (ほど, に限り, にかけては, をはじめ) | **Replaced.** Q1: ほど / さえ / のおかげで / なんか. Q2 gets a new stem (small wound) with まで / のわりに / など / しか. Each distractor is now a とりたて or cause form that dies on a quoted word, and only one per item is a syntax kill (ほど, しか). |
| nitsukete Q2 (何かにつけて) | **Replaced.** It was an idiom-recognition item whose three distractors all died on sight. The new Q2 tests the ▲ 後には心の動き: 「祖父の昔の話を聞く（につけ）、…ありがたさを感じる」, with ものの / からには (SK ▲ 義務・決意) / に先立って. |
| nara-tomokaku counts the reprint 12/2013-40 = 12/2021-36 twice | **Kept at 2.** B0 (g-kaneru 7/2016-39 = 12/2020-39), B1 (g-keigo-kudasaru 12/2020-41 = 7/2012-38) and B2 (g-sura) all counted a reprint as two sittings, and the schema counts "sittings". The count is consistent with that precedent. I propose making the precedent explicit (R3). |
| wo-nuki counts 「この人抜きには」 (12/2020 問題8-46) | **OK.** The card 「抜きには」 holds the form as a unit (rule 12). The 索引 has no separate 抜き point, so this is not a look-alike. The nuance now cites this card instead of claiming 「よく使う」. |
| vi: SK外 compare lines | **Verified.** nikui↔がたい is SK p.82 ▲. kkonai↔そうにない/はずがない and to-iu-you-ni↔ように are meaning contrasts backed by those entries' own pages. te-wa-douka↔ことだ is SK book p.108 (PDF 118) ▲ 目上には使わない. |
| vi: te-wa-douka 「hay đi với 〜てみる」 | **Kept.** All 3 official keys carry てみる, so the claim is countable in the archive. The ja nuance now states the count too. |

## 3. official_count (rule 4, rule 12): all 25 re-verified hit by hit

I checked 問題7 keys (`B1_p7.json`), 問題8 cards and 問題9 lines (`QA6_hits.py` over `B1_p89.json`), each against the flat key. Where the
OCR had scrambled option order (12/2013-40, 12/2024-37, 7/2023-36) I read the booklet line itself.

| entry | shipped → verified | hits |
|---|---|---|
| to-omou-to | 0 ✓ | 7/2011 問題8-47 and 7/2021 問題8-43 are 「〜と思うと」 = "when I think" |
| **utoshiteiru** | **1 → 0** | 7/2017-42 「取り出そうとしているうちに」 is volitional 〜ようとする (a person trying). The entry's own nuance excludes volition (「主語は人でなくてもよい」, vi 「không có ý định của ai」). Look-alike, rule 12 |
| wohajime | 1 ✓ | 12/2013 問題8-46 card. 7/2025 問題9-51 をはじめ is a distractor (key において) |
| ni-kagiri | 1 ✓ | 12/2025-33. 12/2013 問題8-47 「寝るに限る」 is a different point |
| hamotoyori | 1 ✓ | 7/2013 問題8-47 card |
| ni-kanshi-te | 0 ✓ | distractor only (12/2024-33, 7/2024-33, 7/2015-33) |
| nikaketeha | 1 ✓ | 12/2015-35 |
| ni-sotte | 0 ✓ | distractor only (7/2024-33, 12/2013-34, 7/2016-33) |
| nitsukete | 0 ✓ | none |
| nikakawarinaku | 1 ✓ | 12/2023-32 |
| naikotoniha | 1 ✓ | 7/2015-40 |
| wo-nuki | 1 ✓ | 12/2020 問題8-46 card 「抜きには」 |
| niyotte | 1 ✓ | 7/2015-33 (手段). The によって cards 7/2010-46, 7/2024-45, 12/2018-45 mean "depending on", and 12/2022-46 is a passive agent. Neither sense is this point |
| monodakara | 0 ✓ | 7/2017 問題8-46 「友達からもらったもので」 is もの＋で, not a reason |
| nado | 1 ✓ | 7/2024-31. The なんて in 12/2010-36 and 7/2016-35 are distractors. 12/2014 問題8-46 「日記を書くなんて」 is a clause＋なんて, outside SK's 名(＋助詞) 接続 |
| made | 1 ✓ | 12/2015 問題8-46 |
| nikimatteiru | 1 ✓ | 12/2019-37. 12/2015 問題9-54 is a distractor |
| tenaranai | 1 ✓ | 7/2017-36 |
| naiwakeniikanai | 1 ✓ | 7/2025-40 |
| ni-sakidatte | 1 ✓ | 12/2022 問題8-47 card |
| nikui | 1 ✓ | 7/2025 問題8-45 card. 7/2022-32 and 7/2010-41 are stems only, and 12/2016-42 is a distractor |
| nara-tomokaku | 2 ✓ | 12/2021-36, 12/2013-40 (reprint; see §2) |
| kkonai | 1 ✓ | 7/2016-40. 7/2013-39 is a distractor |
| te-wa-douka | 3 ✓ | 7/2018-44, 12/2010 問題9-54, 12/2022 問題9-51 |
| to-iu-you-ni | 3 ✓ | 7/2017-41, 7/2023-36, 12/2024-37 |

## 4. Findings

| # | class | surfaces | evidence (abridged) | fix |
|---|---|---|---|---|
| F1 | official_count wrong | utoshiteiru | see §3 | 0; source note relabelled as a look-alike |
| F2 | **copy of SK or of an official item (auto)**, rule 3/13 | 32 surfaces: to-omou-to ex2, Q2; wohajime ex1, Q1, Q2; ni-kagiri Q1, Q2; hamotoyori Q2; ni-kanshi-te Q1, Q2; ni-sotte Q1; nikakawarinaku ex1–3; naikotoniha ex1, Q1; wo-nuki ex2, Q2; niyotte ex1; monodakara ex1, Q1; made ex1, ex2; tenaranai ex1, Q1, Q2; naiwakeniikanai ex2, Q1, Q2 | **Official:** 「空が急に暗くなったと思ったら、大粒の雨が降りだした」 ≈ 12/2012 and 12/2021 問題6 「雷が鳴り出したと思ったら、さっさと雨が降り出した」. **Same page, numbered examples:** 「この店では、ラーメンをはじめ、…さまざまな中華料理が楽しめる」 ≈ SK 4課1 ① 「この体育館では水泳をはじめ、いろいろなスポーツが楽しめる」; 「この駐車場は有料ですが、…方に限り、…無料で」 ≈ 5課1 ③ 「この病院は午後6時までですが、…患者さんに限り、時間外でも」; 「部長が…誘ってくれたのだから、忙しくても飲み会に行かないわけにはいかない」 ≈ 25課4 ① 「親友の結婚式だから、忙しくても出席しないわけにはいかない」; 「入学試験の結果が明日…不安でならない」 ≈ 25課2 ③ 「明日の面接で…心配でならない」 (B3 F10 already named this template). **Neighbouring headword:** 「市が決めた計画に沿って工事が進められている」 ≈ 8課2 ② 「国の道路計画に基づいて…道路ができ上がっていく」; 「年齢や経験にかかわりなく、誰でも申し込める」 ≈ 11課1 ③ 「性別、年齢を問わず、だれでも参加できます」. **練習 and IV tables:** 「…増加に関する調査の結果が、新聞に発表された」 ≈ 第2部 練習1-8 (PDF 153) 「職業意識に関する…調査した結果を雑誌に発表した」; 「実物を見ないことには、買うかどうか決められない」 ≈ 練習1 ② (PDF 150) 「現物を見てからでないと買う気にはなりません」; 「地元の人々の協力を抜きにしては…成功はなかった」 ≈ 練習1 ⑪ 「周囲の人たちの協力を抜きにしては優勝は無理だった」; 「借金までして…車を買う」 ≈ IV-F (PDF 144) 「借金までして車を買うんですか」; 「許可が出ないことには…企画は始められない」 ≈ IV-D (PDF 139) 「お金がないことには、この計画は進められない」. **Cited official item:** ni-kagiri Q1 reused 12/2025-33's setting-label notice together with two of its distractors (に際し, にわたり). Also rule 11: monodakara ex1 and Q1 were the same apology-for-lateness scene | every surface rewritten on a new scenario. The replacement monodakara stem hit official 「…いたので、携帯電話に出られなかった」 in my scan, so it was changed again. vi `example_notes` re-translated for all 13 new examples |
| F3 | **second defensible answer / kill on feel (auto)**, rules 1, 8, 11, 14 | tenaranai Q1, Q2; nikui Q1; nikimatteiru Q2; plus the flagged items in §2 | 「今夜は不安どころではない」 and 「成績が下がるどころではない」 both have the "not merely X" reading (「痛いどころじゃない」). 「歩きかねる」: see §2 | どころではない → なふりをする / 下がるところだった. かねる → たくなる |
| F4 | one-clause kills and dead-on-sight sets (rule 8, qa-review §2b) | naiwakeniikanai Q1, Q2 (3:1 on polarity: every distractor meant "not go"); made Q2 (two syntax kills, しか + ほど, plus にかけては); monodakara Q1 (two syntax kills, ものなら + ものか); utoshiteiru Q2 (two options killed by "a bell has no will"); te-wa-douka Q1/Q2 (the same three dead shapes いるところ / はいけない / ばかりいる in both items, and no stem cue in Q1) | naiwakeniikanai now uses 守らずにはいられない / 食べずにはいられない (SK 25課3 ▲ 自然に出てくる感情や行動) and 〜わけにはいかない as same-polarity competitors. made Q2 → しか / はもとより / のように. monodakara Q1 → くせに. utoshiteiru → 鳴りそうもない. te-wa-douka Q1 adds 「じゃあ…きっとよく眠れるよ」 with option しまった; Q2 → きました / もしかたがありません |
| F5 | unsourced or widened claims, rules 9 and 15 (ja; one also in vi) | to-omou-to usage (「目の前で見た」, and 「意外なことが多い」 where SK says the result is always 意外); ni-sakidatte (「に先立ちはさらに硬い」, 「ニュースや案内…」); nikakawarinaku (「を問わず…硬い」: SK has no 硬い tag. The nuance implied を問わず takes no 対立 pairs, but SK ▲ lists 男女・内外・有無); tenaranai compare (会話的 / 少し硬い); nado (「へりくだった言い方」); nikui (づらい = 体や心の負担, and 「この意味でづらいは使わない」: 汚れづらい is attested usage); kkonai (可能動詞によくつく; 改まった場面では…を使う); te-wa-douka (柔らかい); wo-nuki (よく使う); nikimatteiru (「根拠がなくても」 widens SK's 主観的・直感的); niyotte (客観的); hamotoyori ja+vi (「後の例に重点」, 「会話では…が多い」); wohajime (挨拶や報告); to-iu-you-ni (「という」 adds a そのまま feel); nara-tomokaku (vs はともかく 仮定); nikaketeha (自信を強く) | each rewritten to the page's own wording, or to a cited official hit (7/2024-31 私なんか, 7/2016-40, 7/2025 問題8-45, 12/2020 問題8-46, 7/2023-36, the three te-wa-douka keys), or cut. naikotoniha nuance aligned to ▲ 「否定的な意味の文が来る」 |
| F6 | furigana | made usage 「て｜形《かたち》」; te-wa-douka usage 「た｜形《かたち》」 | these read けい | fixed |
| F7 | missing source | nikui | SK p.82 (PDF 92) 〔復習〕 prints 「わかりにくい」「入りづらい」, the page that treats the point | source added |
| F8 | missing genuine cross-links | nara-tomokaku (related []), nikui | B1 explicitly excluded ならともかく from g-joken's count as a look-alike. nikui's Q contrasted かねる | nara-tomokaku → g-joken (a ja and a vi compare were written for it, each from the page); nikui → + g-kaneru |
| F9 | explanation targets | every changed item | — | both panes rewritten per item. vi was written from the item and targets a different distractor from ja in most rewritten items (e.g. ni-kagiri Q1 ja はもとより / vi をはじめ; naiwakeniikanai Q2 ja わけにはいかない / vi ずにはいられない) |

**Checked and not findings**

- **Provenance scan** (`QA6_prov.py`, 10-char windows, key spliced into the blank, over refs/**/*.md and tests/imported-*/**/*.{md,txt}), run
  before and after the fixes. Remaining hits are stock phrases or the grammar form itself: 〜ないわけにはいかない。/ てはどうでしょうか。/
  ってもかまいません。/ できるようになった。/ インターネットの普及 (an official 読解 option on a different predicate) / 利用することによって
  (7/2014 読解, different scenario).
- **vi rule 6:** no kana/kanji outside 「」 apart from labels (`QA6_viq.py`). No metadata leaks. The vi pane is written, not translated: before
  the fixes it targeted a different distractor from ja in 22/50 items, and it carries Vietnamese-specific traps (にもかかわらず vs
  にかかわらず, 憎い homophone, 「解けるっこない」 là sai, "theo" = によると). The mirroring I found was argument-level, where an item has one
  strong distractor, not sentence-level.
- **SK pages read on the scan:** PDF 19, 23, 30, 34, 41, 44, 48, 53, 62, 79, 84, 92, 106, 111, 122, 123, 132, plus the IV/練習 pages 138,
  139, 142, 144, 146, 150, 152, 153 and the 索引 217–220. 接続 and meaning match the page for all 20 SK entries.
- **Headwords and ids:** no headword duplicates batch 0–3, B4 or B5 (ni-kagiri ≠ B5 g-kagiri / g-kagiri-5-2; nikakawarinaku ≠ B4
  g-nimokakawarazu). Every `related` id resolves in the merged set. I did not add B4 or B5 ids.
- **Bands (gate):** every field is inside its cap. The closest are ja quiz 75/80 and vi quiz 141/144.

## 5. Root causes

| findings | code | recurrence | proposed edit |
|---|---|---|---|
| F2 | RULE-IGNORED (rules 3, 11, 13 are specific) + RULE-UNENFORCEABLE | B0, B1, B2, B3, B6: every batch | **R1 (BATCH_JA_BRIEF).** Hand in the two-column table B2 proposed (SK sentence ‖ my sentence) for **every page in the 索引 line of the point**, not just the 課 page. Four of this batch's copies came from 練習 / IV pages (PDF 139, 144, 150, 153), which the 索引 lists and the authors never opened. Also: **"a stock textbook sentence for this grammar point is a copy by default"**: 空が暗くなったと思ったら雨, 親友の結婚式だから出席しないわけにはいかない, 借金までして車を買う |
| F1 | RULE-IGNORED (rule 12) | B1 (ukemi), B3 | none. Rule 12's "look-alike" already covers volitional ようとする |
| F3, F4 | RULE-UNENFORCEABLE | B0–B3, B6 | **R2 (SKILL §Quiz integrity, new rule 16).** "Tally each item's three distractors by polarity and by kill reason before hand-off. Refuse the item if 3 share a polarity opposite to the key, if 2 die by syntax, or if 2 share one kill clause. For a modal key (ないわけにはいかない, にきまっている, てならない), at least one distractor must have the key's polarity and die on nuance (ずにはいられない vs 義理; おそれがある vs certainty). **Test every どころではない distractor for its 'not merely X' reading.**" |
| F5 | RULE-IGNORED (rules 9, 15) | B2, B3, B6 | none to the rule. **R4 (BATCH_JA_BRIEF):** "For an SK外 entry, a register or frequency word (硬い, くだけた, よく使う, 柔らかい, 多い) needs an official hit you can cite by sitting and item number, or it is cut. SK外 has no page to lean on." |
| distractor recurrence | RULE-MISSING | B6: にかけては ×10 as a distractor across 25 entries (×6 after the fixes); に限り, に先立って, に沿って ×6 each | **R5 (SKILL §Quiz integrity).** The category quiz is shuffled across 100+ items, so a form printed as a wrong option six times becomes eliminable on sight (bunpou.md's "one form, one item" measured the same effect on 問題7). Proposal: "no form more than 3× as a distractor per batch." This is not applied here; it needs an owner decision |
| F8 | RULE-MISSING (minor) | — | the coordinator's merge step: at B5 merge, link g-utoshiteiru ↔ g-tsutsuaru (the same SK page contrasts them, PDF 23). At B4 merge, link g-naikotoniha ↔ g-tekaradenaito (SK 練習 PDF 150 pairs them) in addition to the planned B4 links |
| nara-tomokaku reprint | RULE-UNENFORCEABLE | B0, B1, B2, B6 | **R3 (rule 4/12 addendum):** "A reprinted item counts once per sitting it appears in; say 'reprint of X' in the source note." This matches every batch's practice so far |

## 6. Coverage and skips

- Blind solve and a distractor splice on all 50 items. The 27 changed items were re-spliced after the fix (the list is in the scratch run).
- official_count re-verified for all 25 entries across 問題7 keys, 問題8 cards and 問題9 keys.
- Gate: `check_knowledge.py` on the scratch merge (B0–B3 + B6) after `build_knowledge.py`: 0 FAIL, 0 WARN.
- **Skipped:** `make check` and `make knowledge` on the real tree. The brief says the coordinator merges and never to touch `knowledge/`.
  No speech or pitch check (文法 pitch is off). B4 is still being authored, so its cross-links were left for the merge.
