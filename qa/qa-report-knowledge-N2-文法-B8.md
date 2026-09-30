# QA report: knowledge/N2 文法, batch 8 (25 points, 75 examples, 50 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. Files are in the coordinator's
scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `文法_B8.json` | 852fc4397e5b | def20661e680 |
| `文法_B8.ja.json` | bbf457cdd617 | 8261cdb8e2e0 |
| `文法_B8.vi.json` | 9fd000fa3641 | eded14214c5d |

Live file: `knowledge/N2/文法.json`, entry `g-shika-nai` only, `sources` +1 row (coordinator decision, §3).

## Verdict

`QA: FAIL → fixed (12 finding classes, 3 automatic-fail items with a second answer, 11 official-scene or
official-apparatus reuses). 0 content findings are open after the fixes.`

I merged live 文法 (172) + B7 + B8 into a scratch copy (`scratchpad/QA8_repo`: `.agents/` and `knowledge/`
copied, the rest symlinked; `QA8_gate.sh`), rebuilt it with `build_knowledge.py --level N2` and ran
`check_knowledge.py`: **0 FAIL, 1 WARN, 223 entries.** The WARN is the new category-wide
`check_related_symmetry` (86 one-way links on the real tree before B8; B8 adds 30, all outward to
entries outside the batch, §6). Answer positions: 12/13/13/12 before and after; no key moved.

**B8 must merge together with or after B7.** `g-adv-imanimo → g-souda-youtai` and
`g-joshi-bakari → g-ta-bakari` resolve only in B7.

**Real tree, needs action now:** my `g-shika-nai` edit to `knowledge/N2/文法.json` was swept into commit
99329c2 without a rebuild, so `knowledge/N2/文法.html` is stale on HEAD and `check_knowledge.py` FAILs
there (`文法.html matches the data it stamps`). Run `make knowledge LEVEL=N2`. I did not rebuild, because
the brief does not let me touch the real `knowledge/` beyond that one entry.

## 1. Blind solve (rule 7)

- `scratchpad/QA8_blind.py` wrote `QA8_blind.txt`: stem and options only, no ids, shuffled with seed 808.
  I saved my answers to `QA8_myanswers.txt` before I opened `QA8_map.json`.
- **50/50 agree with the keys.** As in B0–B6, agreement proved little. Every finding came from the splice
  pass, the official-item comparison and the page reads.
- Every re-authored item was spliced again after the fix. Three of my own first replacements failed that
  re-splice and were changed again: nido-to Q2 つい ("don't inadvertently lie" is readable) → さっそく;
  nikotaete Q1 に比べて ("more than requested") → をめぐって; ni-kagiru Q1's first new stem (train vs
  car in a jam) hit official 7/2024 問題7-40 → a language-learning scene.

## 2. The coordinator's decisions and the authors' flags, judged

| flag | verdict |
|---|---|
| zonjiru: 存じ上げる "know a person" | **Dropped (rule 27).** SK PDF 204–205 (book p.194–195) is the style lesson 12課 and has no 敬語 table and no 存じ上げる. A grep of every `refs/**/*.md` extract and `tests/imported-*` finds 0 hits of 存じ上げ. Pattern/reading/connection → 存じる / ぞんじる / 存じます・存じております・存じません. ex3 (存じ上げて) and Q1's option 存じ上げられます (→ お存じです, a non-form) are gone. ja and vi meaning/usage were rewritten. |
| 7/2025 問題8-46 「その人にしかない」 | **Moved.** The card is 名詞＋に＋しか. g-joshi-shika 2 → 3 (source added; connection and both usages now list 「に」). Live g-shika-nai never listed the item in `sources`, only in the count. Its count stays 3 because **12/2021 問題7-31 「会議が終わるのを待つ（しか）ないね」** (options しか/だけ/まで/さえ, key 1) is 動詞辞書形＋しかない and was missing (B0 counted 12/2014-38, 12/2015-38, 7/2025 P8-46). The source row added there names both moves. |
| ja: 承る narrowed to orders/bookings | **Upheld, and narrowed further (rule 27).** The archive's uses are 全国発送 (7/2013-38, key), ホテルのご予約 (7/2010 script), the 7/2013 読解 「お申し込み…ホームページで承ります」 and a meal add-on (12/2024 読解). 相談 (ex1) and ご意見・ご要望 (ex3) are on no cited item. The meaning is now 注文・予約・申し込み. ex1 and ex3 were replaced, and the 7/2013 読解 line was added as a source. ja and vi meaning, usage and compare were aligned. |
| vi: itasu Q2 「ご連絡いたしかねます」 | **Replaced. It was a second answer, not just soft.** With 「メールで」 in the stem, "once decided, we cannot contact you by email" is a coherent sentence. The stem also reused official 12/2013 問題7-43's scene (「戻りましたらこちらからお電話（いたしましょうか）」). New Q2: an interview, 「大学では経済を（勉強いたしました）」, with なさいました / していただきました / 申しました. |
| vi: g-ue Q2 次第 dies only by connection | **Kept.** It is the item's single 接続-only elimination, which rules 2 and 8 allow. 末 dies on meaning, and the key is argued on meaning (the order of name and key). The item did change for another reason: あまり was also a distractor in official 12/2010 問題7-33 (ご予約の（うえ）、ご来店ください, options あげく/あまり/うえ/ほう), the same notice shape → 最中. |
| vi: g-ue Q1 ところ killed by an uncited rule | **The rule is printed**: SK 20課1, PDF 100 (book p.90) ▲ 「過去の一度だけの出来事について言う。後には、結果を表す文が来る」. That page is now in `sources`. But ところ and とたん (SK PDF 19 ▲ 話者の希望・意向を表す文…は来ない) were both killed by the one clause 「決めたい」 (rule 16). とたん → つもりで, which 「実際に」 kills. |
| vi: uketamawaru Q2 「承られております」 "non-existent" | **Kept; wording fixed.** 謙譲語＋尊敬「られる」 is the same fake-form construction bunpou.md prescribes (参られます), and natives do not commonly produce it (rule 14). The ja nuance and both explanations now call it a 謙譲/尊敬 mismatch, not an unattested string. |
| vi: te-oku compare 「〜とく」 "only in speech" | **Not what the page says.** PDF 204 (book p.194), 硬い文章の基本: 「縮約形や会話にだけ現れる言い方は使いません」. The page says 縮約形 are not used in 硬い文章. It does not say they are used only in conversation. vi te-oku compare (「chỉ dùng khi nói chuyện」) and ja teru-toku compare (「会話だけで使う形」) were widened past the page (rule 15). Both now say it is a 話し言葉 form not used in 硬い文章. ja te-oku compare and ja teru-toku nuance 「改まった文章」 → 「硬い文章」. |

## 3. official_count (rules 4, 10, 12, 19): all 25 re-verified hit by hit

I checked 問題7 keys (`B1_p7.json`, with the option sets printed), 問題8 cards and 問題9 lines (`QA8_hits.py`),
each against the flat key.

| entry | shipped → verified | hits / exclusions |
|---|---|---|
| ni-kagiru | 1 ✓ | 12/2013 P8-47 card 寝るに限る |
| te-oku | 3 ✓ | 12/2022-35 (ておく × てくる), 7/2018-42 (ておく vs てある), 7/2023-37. Not counted: 12/2019-39 ようにしておくと (the contrast is ようにする/なる, g-you-ni), 7/2014-44 (ておく uncontrasted) |
| made-ni-naru | 1 ✓ | 7/2024-38. 7/2010-41 is a distractor |
| kuse-ni | 0 ✓ | 7/2021-36 and 7/2016-40 are distractors |
| ni-sonaete | 1 ✓ | 12/2019-34 |
| keigo-uketamawaru | 1 ✓ | 7/2013-38. 12/2022-40 and 7/2014-39 are distractors |
| keigo-zonjiru | 0 ✓ | only ご存じ items (honorific) and 聴解 / 読解 text |
| keigo-itasu | 1 ✓ | 12/2013-43 |
| keigo-sasete-itadaku | 1 ✓ | 7/2010-39 |
| teru-toku | 2 ✓ | 12/2011-41 (とく/てる/ちゃう contractions contrasted), 12/2016-44 |
| adv-osoraku | 1 ✓ | 12/2019-33 |
| adv-nido-to | 2 ✓ | 7/2023-32, 12/2016 P8-47 card |
| adv-tatoe | 1 ✓ | 7/2017-35 (options differ only after たとえ, rule 19). 12/2017-35 is a distractor |
| adv-imanimo | 2 ✓ | 12/2013 P8-49 and 12/2016 P8-48 cards |
| adv-itsunomani | 1 ✓ | 12/2023-33. 12/2025-32 いつのまにか is a distractor in a different frame |
| **joshi-shika** | **2 → 3** | 12/2018-38, 12/2019-38, **+7/2025 P8-46** (from g-shika-nai). 12/2021-31 待つしかない belongs to g-shika-nai (rule 10) |
| **joshi-bakari** | **5 → 6** | 12/2012-34, 12/2017-37, 7/2013-43, 7/2010 P8-47, 7/2024 P8-47, **+12/2023 P8-46 card 「わからないことばかりで」** (also counted by g-toitte-mo; the card holds both, rule 19). Not counted: たばかり keys (g-ta-bakari) |
| ue | 2 ✓ | 12/2010-33, 7/2022 P8-46. Not counted: 辞書形＋上で (7/2014 P8-46, 12/2016 P8-45) and 仕事の上では (7/2013 P8-49) |
| ue-6-5 | 1 ✓ | 12/2015 P8-46. 7/2021-36 is a distractor |
| nikotaete | 1 ✓ | 12/2011-37. 7/2022-35 is a distractor |
| womotoni | 0 ✓ | 12/2015-35 and 12/2016-35 を基にして are distractors |
| nomotode | 0 ✓ | 7/2014-33 is a distractor; 12/2019 問題9 text only |
| wakeganai | 1 ✓ | 7/2011-43. 7/2012-37 is a distractor |
| toiumonoda | 0 ✓ | 12/2017-38 is a distractor |
| monogaaru | 0 ✓ | 7/2018 問題9 text only |
| live g-shika-nai | 3 → 3 | −7/2025 P8-46, +12/2021-31 |

## 4. Findings

| # | class | surfaces | evidence (abridged) | fix |
|---|---|---|---|---|
| F1 | **second defensible answer (auto)** | monogaaru Q2; itasu Q2; made-ni-naru Q2 | 「この絵は…見る人を引きつける（ものだ）」 is grammatical in the noun reading (＝引きつける作品だ). Rule 20's もの splice was skipped. 「ご連絡いたしかねます」: see §2. 「…母が…完走する（わけがなかった）」 stays readable as a past judgment, because nothing in the stem says she finished | ものだ → にすぎない; itasu Q2 re-authored; わけがなかった → ものだった (回想, which 「最初は…走れなかった」 kills) |
| F2 | **official scene or apparatus reused (auto; rules 13, 21)** | ni-kagiru Q1; made-ni-naru Q1; itasu Q2; nido-to Q2; itsunomani Q1; joshi-shika Q1; joshi-bakari Q2; nikotaete Q1; ue Q2 | ailment → remedy に限る = 12/2013 P8-47 (a grandfather's cold: 寝るに限る). An event's participation growing international = 7/2024-38 (Olympics 14 → 200 countries). A bad one-off experience → 二度と…たくない = 7/2023-32 (restaurant). 「…（いつのまに）…のだろう」 after noticing something new = 12/2023-33, **with 3 of its 4 options** (いまにも/いつのまに/そのうち). にしか/からしか/からだけ = **3 of 4 options of 12/2018-38**. A mother scolds a child who does one thing all the time = 12/2012-34. An institution changes a service in answer to users' 声 = 12/2011-37. お〜の上 notice + あまり = 12/2010-33 | new scenes: making Japanese friends; a company from 3 staff to branches worldwide; an interview; 「こんなうそは二度と…」; ピーマン became liked; をしか (non-form) for にしか; a chatting coworker; doctors answering a disaster area's 要請; あまり → 最中 |
| F3 | SK copy (rules 3, 13) | toiumonoda ex1; nomotode ex3 | 「約束の時間に一時間も遅れて謝らないなんて、失礼というものだ」 ≈ SK 23課2 ② (PDF 114) 「他人の物を断りもなく使うなんて、あつかましいというものだ」. 「学校の許可のもとに、生徒たちは夜の校舎で…観察会を開いた」 ≈ SK 8課4 ④ (PDF 49) 「校庭でのキャンプファイヤーは…周辺住民の了解のもとに10年も続いている」 | 「晴れた休みの日に一日中家にいるのは、もったいないというものだ」; 「両国の合意のもとに、新しい橋の建設が始まった」 |
| F4 | example ↔ quiz scene + predicate (rule 11), incl. across the category | osoraku Q1 vs live g-adv-masaka ex2; te-oku Q2 vs live g-kotoda Q1; sasete-itadaku Q2 vs live g-nitsuki ex; wakeganai ex1 vs own Q1; zonjiru ex2 vs own Q2; nomotode ex1 vs own Q2; nikotaete ex1 vs womotoni Q1 | 「空がこんなに暗いから、（おそらく）…雨が降り出すだろう」 vs 「空が暗いけど、まさか雪は降らないだろう」, where まさか is the distractor. 「発表の前の晩に何度も練習しておいた」 vs 「面接で…前の日に何度も…練習しておく（ことだ）」. Shop closing notice vs 「店内改装中につき、しばらく休業いたします」. Practice → performance ×2. 伺いたいと存じます ×2. 「厳しい〜のもとに」 ×2. City + residents' wishes + park ×2 | new Q1 (a late colleague → 電車が遅れているのだろう); new Q2 (moving → 住所を知らせておいた); new Q2 (受付終了 at an information session; ex2 → 参考にさせていただきます); new ex (正直な田中さんが盗むわけがない; 検討すべきだと存じます; 駅までの道…存じております; 公平な審査; 社員の希望 → 保育所) |
| F5 | shared kill clause (rule 16) | ue Q1 | ところ and とたん both die on 「決めたい」 (SK PDF 100 and 19: no 希望 after) | とたん → つもりで |
| F6 | sense not on a cited page (rule 27) | zonjiru; uketamawaru | §2 | §2 |
| F7 | widened, narrowed or unsourced claims (rules 9, 15) | te-oku compare ja+vi; teru-toku compare/nuance ja; osoraku compare ja; joshi-shika nuance ja | "only in speech": §2. 「まさか…否定の推量とだけ一緒に使う」: SK p.151 (PDF 159) lists まさか under 推量・否定の推量, and live g-adv-masaka shows 〜とは思わなかった. 「それだけで少ないという気持ち」 is on no page | rewritten to the page; joshi-shika nuance now states what the official items show (にしかない＋名詞) and that しか replaces を/が (7/2014 読解 「月しか見えません」) |
| F8 | official_count (rules 4, 10, 19) | joshi-shika, joshi-bakari, live g-shika-nai | §3 | counts and sources fixed |
| F9 | dead-on-sight distractor (qa-review §2b) | toiumonoda Q2 次第だ | 「上司として失格次第だ」 dies without reading the stem | → に越したことはない (same 23課, killed by なんて) |
| F10 | furigana | ja teru-toku Q2 explanation | 「｜前《ぜん》から続いている」 | → まえ |
| F11 | connection incomplete (rule 5) | joshi-shika | the connection omitted に, which the moved 7/2025 card carries | 「（＋に・から・で・によって など）」 |
| F12 | explanation targets | every changed item | — | both panes rewritten per item, the vi one from the item. After the fixes, vi targets a different distractor from ja in 27/50 items (16/50 before) |

**Checked and not findings**

- **Provenance** (`QA8_prov.py`: 10-char windows, key spliced in, over `refs/**/*.md`, which includes every
  `script.md`, and `tests/imported-*`), run before and after the fixes. Hits after the fixes are stock
  phrases only: 申し訳ございません / かしこまりました / お世話になりました / させていただきます。 /
  でお届けいたします / お受け取りください / されることになった / にかなくなっていた. The **kanji-bigram scan
  against all official 問題7–9 items** (rule 17, `QA8_bigram.py`): after the fixes, 0 stems share ≥3 bigrams.
  The one ≥3 hit found during fixing (my 講演会 司会 draft vs 12/2019-36) was changed. The 2-bigram hits
  were read, and none shares a scene.
- **SK pages read on the scan:** PDF 18, 19, 26, 41, 45, 48, 49, 66, 100, 114, 127, 138, 145, 151, 159, 204,
  205 and the 目次 (PDF 3–7). 接続 matches the page for all 8 SK entries (上で, 上に, にこたえて, をもとに,
  のもとで, わけがない, というものだ, ものがある), and the ▲ restrictions in prose match the page wording.
- **Rule 22:** no new key is printed as a wrong option in an equivalent official frame (12/2025-32's
  いつのまにか sits in a 「（　）たたないうちに」 frame).
- **vi rule 6** (`QA8_viq.py`): no unquoted kana or kanji. No metadata leaks. The gate's
  `check_prose_citations` is clean. All vi `example_notes` for new examples were re-translated and read
  against the Japanese.
- **Headwords and ids:** no B8 headword duplicates live 文法 or B7. Book keys match the inventory, and the gate
  is green on `book`. Bands: ja maxima meaning 33, usage 77, nuance 71, compare 80, quiz 80; vi maxima 65 /
  151 / 156 / 158 / 142 (caps 72 / 180 / 180 / 180 / 144).
- **ja/vi independence:** the pre-fix mirroring was argument-level (items with one strong distractor), not
  sentence-level. vi carries its own traps (「に備えて」 after the noun vs Vietnamese "phòng khi" + clause;
  thể て vs thể た in てばかり/たばかり; 「たとえ」 ≠ 「たとえば」).

## 5. Root causes

| findings | code | recurrence | proposed edit |
|---|---|---|---|
| F2 | RULE-IGNORED (rules 13, 17, 21) + GATE-BLIND for the option-set half | B3, B4, B5, B6, B8: every batch | **R1 (gate, `check_knowledge.py`, WARN):** for each authored 文法 quiz, count options shared with any official 問題7 option set (after stripping ruby). WARN at ≥3 of 4. Founding cases: B8 joshi-shika Q1 vs 12/2018-38 (にしか/からしか/からだけ) and itsunomani Q1 vs 12/2023-33 (いまにも/いつのまに/そのうち). Both must fire and nothing else in B8 should. I have not built it (reviewers do not edit the gate). **R2 (BATCH_JA_BRIEF):** "For your entry's form, print EVERY official item that keys it (not only the ones you cite) and write each one's scene in one line before writing a stem." Six of the nine F2 items reused the scene of an item already in the entry's own `sources` |
| F4 | RULE-UNENFORCEABLE (rule 11 says "in the category", but authors scan only their batch) | B4, B5, B8 | **R3 (BATCH_JA_BRIEF):** "Grep the merged `knowledge/N2/文法.json` + open batches for your quiz's content words and your key's scene before hand-off. Rule 11 is category-wide: live g-adv-masaka ex2 and g-kotoda Q1 were each repeated by a B8 stem." |
| F1 | RULE-IGNORED (rule 20: splice every もの/こと distractor in both readings) | B4 R6, B8 | none; the rule is specific |
| F5 | RULE-IGNORED (rule 16) | B6, B8 | add to rule 16: "A shared kill clause includes a main-clause constraint: two conjunctions whose ▲ both forbid a 希望/意向 main clause die on the same words." |
| F6 | RULE-IGNORED (rule 27) | 語彙 B1, B8 | none |
| F7 | RULE-IGNORED (rules 9, 15) | B2–B6, B8 | none. The p.194 contraction wording now appears in four entries' sources (chau, teru-toku, te-oku, 敬語), so give **BATCH_VI_BRIEF / JA_BRIEF** its exact text: "硬い文章では縮約形や会話にだけ現れる言い方は使わない — it does NOT say 縮約形 are conversation-only." |
| F8 | RULE-IGNORED (rules 10, 19) | B0 (12/2021-31 missed), B8 | none |
| one-way related (gate WARN) | PIPELINE-GAP | every batch since B0 | the coordinator's planned back-link pass: B8 adds 30 outward links, whose back-links need a `compare` on 29 live/B7 entries in both languages |

## 6. Coverage and skips

- Blind solve and splice on all 50 items. Every changed item was re-spliced, and three of my own drafts were
  replaced again (§1).
- official_count: all 25 entries hit by hit (§3).
- Gate: `QA8_gate.sh` (live + B7 + B8 merged in scratch, rebuilt, `check_knowledge.py`): 0 FAIL, 1 WARN (the
  category-wide related-symmetry WARN).
- **Skipped:** `make check` on the real tree. The batch is not merged, and I did not run `make knowledge`
  (see Verdict: `文法.html` is now stale on HEAD because of the g-shika-nai edit; the coordinator must
  rebuild). Pitch and speech were not checked (文法 pitch is off). No back-links were added to live or B7
  entries (outside my edit scope).
