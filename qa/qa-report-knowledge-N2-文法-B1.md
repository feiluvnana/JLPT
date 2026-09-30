# QA report — knowledge/N2 文法, batch 1 (25 points / 75 examples / 50 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. Files in scratch
`batches/` (sha1, first 12 characters): pre-review → post-fix

| file | pre | post |
|---|---|---|
| `文法_B1.json` | 2946f50eee08 | 5b2785559259 |
| `文法_B1.ja.json` | 7bc03218091b | 0ff8a63953ff |
| `文法_B1.vi.json` | 3605fbc8e70d | 99d8bb9bb5e3 |

## Verdict

`QA: FAIL → fixed (17 findings, 1 automatic-fail class: a second defensible answer). After the fixes, 0 content findings are open.`
The gate ran on a scratch repo (`scratchpad/QA1_repo`: a copied `.agents/` and `knowledge/`, with batch 0 + B1 + B2 + B3 merged)
and the page was built there. It reports **0 FAIL and 0 WARN on any B1 id**. The one remaining FAIL is a band overflow in
`文法_B3.vi.json`, which another context is still writing. The real `knowledge/` was not touched.

## 1. Blind solve (rule 7)

- I wrote an extraction of all 50 items with stem and options only, no ids, shuffled with seed 4242
  (`scratchpad/QA1_blind.txt`), and saved my answers to `QA1_myanswers.txt` before I opened `QA1_map.json`.
- **50/50 agree with the keys.** Agreement is only the floor; the findings below came from the splice pass.
- Answer positions are 12 / 13 / 12 / 13, before and after the fixes. No fix moved a key.

## 2. Splice pass (rule 1) and the form rule (rule 2)

I wrote each of the 150 distractors into its stem and named the stem words that kill it. Rule 2 holds on all 50 items:
at least 3 of the 4 options attach to the printed form, and no item has more than one kill that rests on 接続 alone.

The authors' flagged doubts:

| flag | verdict |
|---|---|
| kudasaru Q1 「社長が（お越しいただき）」 | **Finding F1.** 「〜がお越しいただき」 is a misuse that native business Japanese produces all the time, so a hostile solver defends it. Doubt goes against the item. I replaced the option with the fake form 「お越ししてくださり」 (the お越し + する error, the 参られます type in bunpou.md). |
| joken Q1 着けば／着くと ruled out by the 文末 rule | **OK.** SK 第3部3課 p.158 ◆文末の制限 prints 「×そのDVDを借りれば、後でわたしにも見せてください」 and limits と with 希望・働きかけ. This rule is the point the item tests, not a form-only kill. |
| dake Q1 泣きたい（ほど）泣けばいい | **Item OK, explanations fixed (F9).** 「ほど」 expresses degree (泣きたいほどつらい) and does not take the 「V-たいだけV」 repetition that SK 4課6 ▲ describes. It is the strongest distractor, but both explanations argued 「しか」, the weakest. Both now name ほど. |
| te-kuru Q2 降ったばかりだので | **OK.** It is the item's only 接続 kill, and 降っていった / 降っておいた die on meaning. |
| toshitara Q2 とすると／となると, both killed by one rule | **Rule OK.** SK 15課1 ▲ says 「とすると・となると」 are not followed by 希望・意向・働きかけ, and the tested point is that rule. The stem was still a near-copy of SK p.159 and was rewritten (F5). |
| mai-24-5 Q1, two distractors killed by one rule | **OK.** I found three different kills. しまいか: 〜まいか needs the 〜ようか pair or ではあるまいか. するべきだ: inverts the speaker's decision. しないものだ: a general norm, not the speaker's own resolve. |
| ukemi 18 / joken 23 official_count | **Both wrong (F10).** Recounted hit by hit (§3): 8 and 20. |
| vi: te-morau Q1/Q2, te-kureru Q2, kudasaru Q2 decided by が／に／は | **OK under rule 2.** All four options attach, so none is a 接続 kill. The particle marks who acts, and that is the point 授受 tests (SK p.175: 「〜てもらう」と「〜てくれる」は主語が違います). A topicalised に (先生には → 先生は) was considered: bare 「先生は」 with いただく/もらう still reads as the receiver, so the kill stands. |
| vi: shieki-ukemi 「す」-ending verbs have no される short form | **Cut (F12).** SK p.171 (PDF 181) has no short form and no す rule. The claim is true Japanese, but no cited ref backs it. Removed from both panes; the short form stays, stated without the exception. |
| vi: toha ex1 一期一会 | **OK.** The reading いちごいちえ and the gloss are correct. It has no provenance hit, and the vi note ("Ichigo ichie" (nhất kỳ nhất hội)) is a faithful translation. |

## 3. official_count (rule 4): 17 of 25 entries re-verified hit by hit

These are every entry with a count of 5 or more and every 0, read in `B1_p7.json` (booklet.md + key.md flat keys, spot-checked
against the booklets) and in the 問題8/9 blocks.

**The counting rule I applied.** Rule 4 and the brief say "問題7/9 key or 問題8 card". Read literally, it counts any
conditional or passive anywhere in a key or card, which would give 条件 about 26 and 受身 about 17 of 31 sittings. I counted a
sitting when:

- a 問題7/9 keyed option carries the form and the options contrast it; or
- a 問題8 card carries the form as a unit (auxiliary, particle or construction: 〜ていただける, なら, 〜んだったら, おかげだ);
- but never an inflection that every sentence carries (a passive or causative verb, a ば/たら verb card);
- and never a look-alike that is a separate SK point (か〜ないかのうちに, ならともかく, ものなら, ば〜ほど, ようでいて, definitional vs surprise とは, おいでくださり for てくれる).

| entry | shipped | verified | sittings |
|---|---|---|---|
| g-te-ageru | 0 | **0** ✓ | none (12/2014-48 「自分でやって」 is lexical やる) |
| g-te-morau | 10 | **10** ✓ | P7: 7/2010-39, 12/2019-42, 7/2019-41, 7/2021-41, 7/2022-41, 7/2023-42, 12/2013-41, 12/2018-42. P8: 12/2021-46, 7/2012-47 |
| g-te-kureru | 10 | **9** | P7: 12/2010-41, 12/2022-37, 12/2023-40, 12/2015-42, 7/2015-42, 12/2017-42/44. P8: 7/2019-46, 12/2024-46, 7/2011-47. Dropped 7/2018 問題9-54, where all four options carry 支えてくれている |
| g-ukemi | 18 | **8** | P7: 12/2019-40, 12/2022-41, 12/2012-44, 12/2014-44. P9: 12/2011-51, 7/2015-52, 12/2016-53, 7/2023-49. Excluded: potential/spontaneous られる (7/2021-38, 12/2016-43, 12/2020 P9-50, 7/2018 P9-53) and all-passive option sets (12/2021-35, 7/2014 P9-53, 12/2019 P9-51, 7/2022 P9-49) |
| g-shieki | 12 | **8** | P7: 12/2010-41, 7/2010-39, 7/2021-41, 12/2023-40, 7/2024-35, 12/2012-41, 12/2013-42, 7/2014-35/42. 欠かせない and ません are look-alikes |
| g-shieki-ukemi | 7 | **6** | P7: 7/2010-40, 7/2011-35, 7/2012-44, 7/2018-43. P9: 7/2019-52, 7/2013-54 |
| g-okageda | 6 | **6** ✓ | P7: 7/2021-35, 7/2023-42, 7/2012-41. P8: 7/2022-44, 12/2011-49, 12/2015-47 |
| g-keigo-kudasaru | 5 | **5** ✓ | P7: 12/2019-36, 12/2020-41, 7/2025-34, 7/2012-38, 12/2017-44. 12/2020-41 reprints 7/2012-38, but they are distinct sittings |
| g-keigo-itadaku | 8 | **8** ✓ | P7: 7/2010-39, 12/2021-40, 7/2023-42, 12/2024-35, 12/2013-38, 12/2014-39. P9: 12/2012-54. P8: 7/2012-48 |
| g-joken | 23 | **20** | P7/P9 contrast: 12/2019, 12/2020, 7/2021, 12/2022, 7/2022, 12/2023, 7/2023, 12/2024, 7/2024, 12/2012, 12/2014, 7/2014, 12/2015, 12/2016, 12/2017, 7/2010. P8 なら/んだったら cards: 12/2025-44, 12/2011-48, 7/2015-49, 7/2018-46. Excluded: としたら (own entry), ならともかく, ものなら, ば〜ほど, 〜ばいい, 〜たらどう, and keigo items where every option is たら/でしたら |
| g-you-ni | 11 | **11** ✓ | P7: 7/2010, 12/2019 (×2), 7/2019, 12/2021, 12/2022, 7/2025, 12/2025, 12/2014, 7/2016, 7/2018. P8: 12/2015-45. Excluded: ようになる, というように, ご覧のように, このように |
| g-toshite | 7 | **7** ✓ | P7: 7/2019-38, 7/2023-34, 12/2025-36. P8: 7/2022-46, 12/2023-44, 7/2015-46, 12/2018-43. としても (concessive) excluded |
| g-rashii | 14 | **14** ✓ | P7: 12/2010-35, 7/2022-42, 7/2023-35, 7/2025-35, 12/2012-39, 7/2014-43, 12/2015-43. P9: 7/2015-54, 7/2016-52. P8: 7/2010-48, 12/2019-46, 12/2024-45, 12/2011-45, 7/2018-48 |
| g-uchini | 9 | **8** | P7: 7/2025-36, 12/2011-38, 12/2012-36, 7/2014-41, 12/2017-36, 7/2017-42. P8: 12/2010-46, 12/2018-47. Dropped 7/2021 問題8-45 「言い終わるか終わらないかのうちに」, which is SK 1課5 g-kanaikanouchini, a separate point |
| g-tonaruto | 0 | **0** ✓ | 「となると」 appears only in 読解 prose (12/2021, 7/2011, 12/2012) |
| g-mai-24-5 | 0 | **0** ✓ | no まい key or card |
| g-toha | 0 | **0** ✓ | 7/2021 and 7/2014 問題8 「〜とは、ずいぶん勇気が…」 is surprise-とは, not definitional; 12/2020-44 is a stem |

Also confirmed: toshitara 2 (7/2012-43, 7/2016-42; 12/2023-36 is ようとしたら), sou-ni-nai 2, mai 1, and tte 2 on the 問題7 keys.
The ni-taishite nuance 「米1に対して水10」 (ratio use) is backed by official 12/2024 問題7-33 (いちご100グラムに対して) and
12/2020 問題8-44.

## 4. Per-entry check against the SK page

I read PDF pages 22, 31, 45, 70–71, 78, 85, 97, 111, 119, 136, 138–139, 168–169, 176–177, 180–185 and 204.

- **接続:** correct for every SK-numbered entry, including the (な)/である notation. uchini A/B, ni-taishite B (普通形 ナ形/名 だ→な/である ＋の), mai (普通形＋の(ナ形/名 だ→な) ＋ではあるまいか; II・III ます形＋まい; するまい・すまい), dake, okageda, toshite, toshitara, tonaruto and toha all match their pages.
- **Meanings and ▲ notes:** match. Examples: okageda 意向・働きかけ×; toshite 行為・評価; mai 一人称×・丁寧/過去×; mai-24-5 話者以外の意志 → と思っているようだ; toha 後に意味・本質.
- **Readings:** every example shows its entry's own reading. mai examples are 推量, mai-24-5 examples are 意志, and toshitara and tonaruto are kept apart.
- **Page errors:** one wrong page (F11) and one contradicted claim (F8).

## 5. Findings

| # | item | severity | evidence | fix |
|---|---|---|---|---|
| F1 | g-keigo-kudasaru Q1 | **auto (second defensible answer)** | 「社長が自ら…（お越しいただき）」 is widely accepted business usage | option 1 → 「お越ししてくださり」 (fake お越し＋する). Both panes rewritten |
| F2 | g-mai Q1 | textbook copy | 「これだけしっかり準備したのだから…失敗をすることは（あるまい）」 is SK 22課4 ① 「何度も計算し直したのだから、間違いはあるまい」 (also on SK IV-C p.126): same scenario and predicate | new stem 「駅からこれだけ遠い店なら、平日の昼に客が大勢来ることは（　）」. Both panes rewritten |
| F3 | g-mai Q2 | textbook copy | 「この計画には無理がある（のではあるまいか）」 is SK ⑤ 「…協力を得るのは無理なのではあるまいか」 | new stem: a dictionary too detailed for beginners → 「かえって使いにくい（　）。もっと簡単なものから…」. The first draft's 「かえってわかりにくい」 hit 12/2021 読解 in the scan and was changed |
| F4 | g-mai ex3, ex1 | textbook copy + register | ex3 「読書離れの原因は…にあるのではあるまいか」 is SK ④ 「生物が減ったのは、農薬…が原因ではあるまいか」. ex1 「あの慎重な彼が…するまい」 reads better with は | ex3 → 「子どもに必要なのは、高いおもちゃよりも親と過ごす時間なのではあるまいか」. ex1 → 「慎重な彼のことだから、そんな簡単なミスはするまい」. vi notes re-translated |
| F5 | g-toshitara Q1, Q2 | textbook copy ×2 | Q1 「工場を建てる（となると）…三年はかかる」 is SK 15課1 ⑤ 「引っ越すとなると、かなりのお金がかかる」. Q2 「一週間休みが取れる（としたら）、ヨーロッパを…旅行したい」 is SK p.159 「行くとしたら、南アメリカに行きたい」 | Q1 → 「来週から工事が始まる（　）、この道はしばらく通れなくなるだろう」. Q2 → 「もし生まれ変わる（　）、今度は鳥になって空を飛んでみたい」. Keys and options unchanged. Both panes rewritten |
| F6 | g-mai-24-5 Q2, ex3 | textbook copy | Q2 「新しいスマホを（買おうか買うまいか）…迷っている」 is SK 24課5 ④ 「掃除ロボットを買おうか買うまいか決心がつかない」. ex3 「会社を辞めようか辞めるまいか…悩んだ」 is close to SK ⑤ (引き受けようか引き受けまいか…迷った) | Q2 → 「同窓会の案内が届いたが、（行こうか行くまいか）、まだ返事を出せずにいる」, with all four options re-cut on 行く. ex3 → 「友達に本当のことを話そうか話すまいか」. Both panes rewritten |
| F7 | g-tonaruto ex1; g-te-iku Q1; g-keigo-kudasaru ex2 | textbook / official template | 「新しい機械のこととなると目が輝く」 is SK IV-D p.129 「山のこととなると目が輝く」. te-iku Q1 「玄関で見送っていると、息子は…歩いていった」 mirrors SK 5課 練習1-4 「玄関の外に出て待っていると、子供たちは…帰ってきた」. kudasaru ex2 「本日は…お集まりくださり、…ありがとうございます」 is the frame of official 12/2019-36 and 7/2025-34 | ex1 → 「…だれよりも熱心に質問する」 (ja usage re-synced). te-iku Q1 → 「ホームで手を振っていると、友達を乗せた電車はゆっくりと（離れていった）」. kudasaru ex2 → 「大学の恩師がご紹介くださった会社に、来月から勤めることになった」. vi notes and quiz explanations rewritten |
| F8 | g-ukemi ja `nuance` | contradicts SK | 「する人が大切でない時…（「〜によって受け継がれる」）」: SK p.170 A-2 says によって marks the actor when it IS important | rewritten: actor unneeded → no agent; actor important → 「〜によって」 |
| F9 | g-dake Q1, both panes | explanation argues the weakest distractor + band | Both explanations argued しか and never mentioned ほど. Another agent's gate run also found the ja explanation at 81 chars, over the 80 cap | both rewritten around ほど; ja now 79 chars. Two new strings that sat flush at the cap were trimmed (g-mai ja Q2 80→75, g-dake vi Q1 144→123) |
| F10 | official_count ×6 | wrong count | ukemi 18→8, joken 23→20, shieki 12→8, te-kureru 10→9, shieki-ukemi 7→6, uchini 9→8 (§3) | set |
| F11 | g-ukemi `sources`; g-tonaruto `sources` | bad citation | ukemi cited 12/2021-35 「紹介されて」, but all four options are passive and the item tests 以来. tonaruto cited PDF 138 (the もの table); the (のこと)となると row is on PDF 139 (本のp.129) | ukemi → 12/2014 問題7-44 (されつつある vs させられ…). tonaruto page → 139 |
| F12 | g-shieki-ukemi usage (ja+vi) | unbacked claim | 「す」で終わる動詞は「話させられる」だけ: no cited ref (SK p.171 has no short form at all) | cut from both panes |
| F13 | g-sou-ni-nai nuance (ja+vi) | unbacked claim | 「そうもない」は「そうにない」より少し強い: SK外 entry, no ref | cut from both panes |
| F14 | g-mai ja `nuance` | unbacked claim | 「かなり強い推量」: SK gives only ⇒〜ないだろう | rewritten: まい = negative 推量, ではあるまいか = positive 推量, 一人称× |

**Judged NOT findings:**

- The 10-char scan over `refs/**/*.md` + `tests/imported-*/**/*.{md,txt}` now finds only stock phrases (申し訳ございませんが, ありがとうございます, していただけませんか, 海外旅行に行くことに, たほうがいいと思う。…), and those were read at the source.
- The vi pane has no Japanese outside 「」 (scripted scan, labels excepted).
- Every example_note is faithful, and the 8 notes touched here were re-translated from the new Japanese.
- No metadata leaks.
- The vi pane is written, not translated. Its explanations target a different distractor in 11 of 50 items (te-ageru Q2 くれる vs ja もらう, ni-taishite Q2 うえに vs ばかりか, tte Q2 わけか vs ものか, toshitara Q1 にしては vs ばかりに, …). It carries Vietnamese-specific traps (được/bị for 受身, "bắt/cho" for 使役, kẻo for ないうちに) and mirrors no ja sentence structure.
- Every `related` id resolves (batch 0, B1, B2 伺う・ことになる・たって, B3 参る・にしたら・として〜ない・ということだ). No headword duplicates another batch.
- Furigana was hand-read on every ruby pair (the full list is in the scratch run); no misreading was found (教《おそ》わる, 閉《し/と》, 足《た》りない, 三十分《さんじゅっぷん》, 一人称《いちにんしょう》 are all correct).
- toha Q2 (three distractors die on the ▲ 「後に意味・本質の説明」 rule) is kept: the kill is the tested point, not an unrelated one.

## 6. Root causes

| finding | code | cause | proposed edit |
|---|---|---|---|
| F10, F11 (ukemi cite) | RULE-UNENFORCEABLE | Rule 4 says "confirmed hit by hit" but never defines a hit for morphology families. The author regex (`B1_q.py`) matched any passive or conditional inside any key, card or stem, and potential られる passed as passive. This is batch 0's R4 class again, in a new shape: 6 of 17 re-verified counts were wrong | **SKILL §Quiz integrity rule 4** and N2.md "Rules for batch authors": "A sitting counts when a 問題7/9 KEYED option carries the form **and the options contrast it**, or a 問題8 card carries the form as a unit (auxiliary, particle, construction). Never count an inflection every sentence carries (受身・使役 verbs, ば/たら verb cards), a potential/spontaneous られる, or a look-alike that is another SK point. List the counted sittings in the report." |
| F2–F7 (7 copies) | RULE-UNENFORCEABLE (scope) | Rule 3 says compare against "the cited Shin Kanzen page's numbered examples". Four copies came from SK pages that were not the cited page: IV-C p.126, IV-D p.129, 第3部3課 p.159, and 第3部5課 練習. Three (mai ①⑤, mai-24-5 ④) were on the cited page itself (RULE-IGNORED) | **Rule 3**: "…against every SK page that treats the point: the 課 page, its 練習 items, the IV summary tables (p.126–129) and any 第3部 cross-reference (→第1部15課) — AND the official items cited in `sources` (a thank-you formula copied from the cited 問題7 is a copy)." **BATCH_JA_BRIEF**: "Write a scenario first that SK does not use; only then choose the predicate." |
| F1 | RULE-MISSING | No rule covers distractors that are misuses natives widely tolerate | **BATCH_JA_BRIEF / bunpou-side rule for 知識**: "A 敬語 distractor may not be a misuse natives commonly produce (〜が〜いただく, 二重敬語 お越しになられる, さ入れ言葉). Use a form that does not exist (お越しする, 参られる) or a humble verb on the superior's action." |
| F8, F12–F14 | RULE-UNENFORCEABLE | "claims that no ref backs are verified or cut" exists only in the QA brief. The author brief never says it, so the author could not know | **BATCH_JA_BRIEF / BATCH_VI_BRIEF**: "Every usage/nuance claim beyond the cited page's ⇒ and ▲ must be on a page you can cite (SK, official item) or left out; strength or frequency claims (「少し強い」「かなり強い」) need a source." |
| F9 | RULE-IGNORED | The SKILL already says "what rules the strongest distractor out" | none; process note |

## 7. Coverage

- Blind solve and splice on all 50 items; every distractor has a named kill (§2).
- SK pages read for all 21 SK-backed entries; official items read for the 4 SK外 entries.
- 17 of 25 official_counts verified hit by hit (every count of 5 or more and every 0), plus toshitara, sou-ni-nai, mai and tte on 問題7.
- Provenance: a 10-char scan of every example, stem and long option (re-run after the fixes), plus a hand comparison with the SK numbered examples, 練習 items and IV tables.
- Prose: ja and vi read in full for all 25 entries; vi scanned for 「」 compliance.
- Gate: `check_knowledge.py` on the scratch repo with batch 0 + B1 + B2 + B3 merged, and `build_knowledge.py` there. **B1: 0 FAIL, 0 WARN.** Bands are inside cap after the rewrites.

## 8. Skips

- I did not run `make check` or `make knowledge` on the real tree (brief: never touch `knowledge/`; the coordinator merges).
- I did not ear-check speech (文法 pitch flag is off).
- Seven counts under 5 were not re-derived beyond their 問題7 keys: dake, te-kuru, te-iku, ni-taishite, tte, and partly sou-ni-nai and toshitara.
