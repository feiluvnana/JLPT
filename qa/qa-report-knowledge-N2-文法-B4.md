# QA report: knowledge/N2 文法, batch 4 (25 points, 75 examples, 50 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch.
Files are in scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `文法_B4.json` | 43277dd3b9e5 | 1ed4941d4e6a |
| `文法_B4.ja.json` | de61c1d3b493 | edf862c48d46 |
| `文法_B4.vi.json` | ff560c4c92f3 | 75af00023c07 |

## Verdict

`QA: FAIL → fixed (26 findings, 4 automatic-fail class). 0 content findings are open after the fixes.`

Batch 4 was written before rules 12–15 existed, and most findings fall under those rules. There were 11 textbook or
official scenario copies (rule 13), 3 敬語 distractors that natives commonly produce (rule 14), and 5 prose restrictions
that were not in the page's wording (rule 15).

I merged B4 and the current B6 into a scratch copy of `knowledge/` (`scratchpad/QA4_repo`: `.agents/` and `knowledge/`
copied, everything else symlinked), rebuilt it with `build_knowledge.py --level N2` and ran `check_knowledge.py`:
**0 FAIL, 0 WARN, 147 entries, 294 quiz items, positions balanced.** The real `knowledge/` was not touched. The
`knowledge/N2/*.html` changes now in the working tree date from 16:14, before my build, and belong to another context.

**B4 now has to merge together with or after B6.** Two `related` ids resolve only there: g-ni-kagiri and
g-nikakawarinaku (the coordinator's cross-links, §5).

## 1. Blind solve

- **Extraction:** `scratchpad/QA4_blind.py` wrote `QA4_blind.txt`: stem and options only, no ids, shuffled with seed 4444.
  I saved my answers to `QA4_myanswers.txt` before I opened `QA4_map.json`.
- **Result: 50/50 agree with the keys.** Every finding below came from splicing each distractor into its stem, from the
  page reads and from the scenario comparisons.
- **Position balance:** 12/13/13/12 before and after the fixes. No key moved.

## 2. Per-entry walkthrough

I read every cited SK page on the scan: PDF 26, 27, 31, 40, 41, 70, 71, 74, 75, 78, 88, 97, 101, 134, 139, 144 and 159.
I re-counted `official_count` for **all 25 entries**, hit by hit, with `QA4_hits.py` (問題7 keys against the flat key,
plus 問題9) and `QA4_p8.py` (問題8 cards against stems).

| entry | SK page / 接続 | official_count (verified) | fixes |
|---|---|---|---|
| g-keigo-oide | 敬語 (official only) | 3 ✓ (12/2019-36, 7/2025-34, 7/2016-37) | Q1 and Q2 (F3) |
| g-toiuto | p.71 ✓ | 2 ✓ (P8 cards 7/2013-45, 12/2015-48) | ex1–3 and Q2 (F4) |
| g-toieba | p.70 ✓ | 0 ✓ (12/2016 P8-45 「何が大切かといえば」 is the question-topic かといえば; counted for none of the three entries) | ex1, nuance (F5) |
| g-toittara | p.71 ✓ | 0 ✓ | Q1, furigana (F6) |
| g-wo-tsuuji-te | p.31 ✓ (A ▲比較的長い期間; B ▲直接的手段× 間に入るもの) | 1 ✓ (12/2017-33) | ex1 (F18), nuance (F25) |
| g-to-no-koto | p.139 ✓ | 2 ✓ (7/2023-40, 12/2014-37) | vi compare (F24) |
| g-nomi | p.144 ✓ | 0 ✓ | Q1 and Q2 (F7) |
| g-neba | SK外 | **1 → 2** (7/2012-43 and 7/2022 P8-46; see §4) | count (F20), nuance (F25) |
| g-tsuide-ni | SK外 | 2 ✓ (12/2018-32, 7/2016 P8-47; 7/2016-33 「についで」 excluded) | ex2 (F18), nuance (F25) |
| g-naidemonai | SK外 | 1 ✓ (12/2011-40) | ex2 (F18) |
| g-keigo-goran | 敬語 | 3 ✓ (12/2021-40, 12/2012-43, 12/2013-38) | Q1 and Q2 (F2) |
| g-adv-ittai | p.159 ✓ (文末 = 質問) | 2 ✓ (7/2025-33, 12/2018-33) | 接続 and prose (F22) |
| g-tekaradenaito | p.27 ✓ | 2 ✓ (12/2024-34, 7/2013-36) | ex2 and Q2 (F17) |
| g-karatoitte | p.75 ✓ | 1 ✓ (12/2022-36) | ex2 and Q2 (F16) |
| g-nitotte | p.97 ✓ | 1 ✓ (7/2017 P8-47) | Q2 (F14) |
| g-tai-garu | SK外 | 4 ✓ (12/2024-36, 12/2012-41, 12/2014-42, 7/2018-37; 7/2025-42 excluded because its key is たくなって) | Q1 and Q2 (F10) |
| g-tehajimete | p.26 ✓ | 0 ✓ (12/2013 P8-48 has the form in the stem only) | Q2, nuance (F11) |
| g-te-irai | p.27 ✓ | 2 ✓ (12/2016 P8-46 card; 12/2021-35, see §4) | Q2 (F13) |
| g-ni-kagira-zu | p.40 ✓ | 1 ✓ (7/2019 P8-45) | Q1 (F1), ex3 (F19), link (F26) |
| g-nimokakawarazu | p.74 ✓ (名・普通形 ナ/名 -である) | 1 ✓ (12/2012-38) | Q2 (F15), link (F26) |
| g-mononara | p.78 ✓ | 2 ✓ (7/2017-34; 12/2013-35, see §4) | Q2 (F9) |
| g-dakeni | p.88 ✓ (＊名だ×) | 1 ✓ (12/2014-36) | Q1 (F8) |
| g-tokorodatta | p.101 ✓ | 1 ✓ (12/2024-40) | Q1 and Q2 (F12) |
| g-kara-suru-to | p.134 ✓, but it lists only からすると・からいうと | 2 ✓ (P8 cards 7/2024-47, 7/2010-49) | から見ると removed (F21) |
| g-koto-de | SK外 | 4 ✓ (12/2021-38, 7/2023-37, 12/2013-41, 12/2025 P8-47) | vi metadata (F23) |

## 3. Findings

| # | item | severity | evidence | fix | root cause |
|---|---|---|---|---|---|
| F1 | ni-kagira-zu Q1 | **auto: second answer** | 「市民（に限り）、誰でも無料で利用できます」: 「〜に限り、どなたでも」 is ordinary notice Japanese (the vi author flagged it). All three distractors also died by one clause | stem 「市民（　）、市外から来た人でも無料で…」. Options に限って / **に限らず** / に限り / を問わず: を問わず is a rule kill (it needs a noun with a range). Both panes rewritten | RULE-IGNORED (rule 1: splice) |
| F2 | goran Q1, Q2 | **auto (rule 14)** + rule 13 | 「夜景を拝見できます」 and 「拝見してください」 are misuses natives commonly produce. Q2 also reused official 12/2021-40's scenario and 拝見 distractor (showing rooms, ご覧いただく) | Q1 option → 「お見ください」, a form that does not exist. Q2 → a tour-bus guide: 「右手に富士山を（ご覧いただけます）」, with 「ご拝見になれます」 (does not exist), お目にかかれます and 拝見いたします | RULE-MISSING at authoring time (rules 13 and 14 came later) |
| F3 | oide Q1, Q2 | rule 14 + rule 13 | Q1 「ロビーに参っております」 is a common misuse. Q1 reused official 7/2025-34 (inn staff to a guest, with 参り/伺い as distractors). Q2 reused 7/2016-37 (a company, someone arriving, with 参ったら/伺ったら) | Q1 → a hospital waiting room, options ございます / **おいでになります** / 伺っております / おいでしております. Q2 → a professor going to a conference (行く reading), options 参る / 伺う / お越しする / **おいでになる** | RULE-MISSING at authoring time |
| F4 | toiuto Q2, ex1–3 | **auto: SK copy** | Q2 「例の店というと、先月オープンしたカレー屋さんのことですか」 = SK p.71 ④ 「トップっていうと、去年オープンしたイタリアンレストランのことですよね」 (flagged by vi). ex3 used the same shop frame. ex2 「京都といえば…思い浮かべる」 = ② 「オーストラリアといえば…思い浮かべる」. ex1 (夏の果物) had the same scene as Q1 (秋の食べ物) | Q2 → confirming which 田中さん is meant. New ex1 (childhood memory), ex2 (a town's festival), ex3 (半額というと、五万円ですね) | RULE-IGNORED (rule 3) + rule 11 |
| F5 | toieba ex1, nuance (ja + vi) | SK template + unsourced claim | ex1 (a cake from the shop by the station → 駅前といえば + news) is SK p.70 ①'s template (a souvenir from Hawaii → ハワイといえば + news). ja 「前の話とのつながりは弱くてもよい」 contradicts SK's 関連のある別の話. The vi example 「遠いといえば遠いが、静かだ」 is SK ③'s content | ex1 → soccer → a new practice field. The ja nuance rewritten to SK's ▲. vi example → 「高いといえば高いが、長く使える」 | rule 13 / rule 9 |
| F6 | toittara Q1; ja Q2 | rule 8 + SK frame + wrong furigana | Q1's options were のわりに / にもかかわらず / ものの: three adversatives killed in one clause, and ものの also dies by 接続 (名＋ものの). The stem (「引っ越し前日の忙しさ」) followed SK ① (「締め切り前の仕事の忙しさ」). ja Q2 had 「厳《いかめ》しい」 | new stem (a roller coaster's speed). Options のわりに / といっても (SK p.75 ▲) / にもかかわらず / **といったら**. Furigana → 《きび》 | rule 8 (authored before B2's rule reached the brief) / GATE-BLIND (readings) |
| F7 | nomi Q1, Q2; ja usage | rule 8 | Q1 killed さえ, すら and まで in one clause. Q2's ばかりか and だけでなく died only by syntax (they need a following も), because nothing in the stem ruled out other channels. 「お知らせや規則によく出てくる」 is unsourced | Q1 → a bus-only road (「一般の車は通れません」). Options **のみ** / しか (the one syntax kill) / に限らず / まで. Q2 stem adds 「お電話やメールでのお申し込みはできません」. Usage trimmed to SK's 硬い言い方 | rule 8 |
| F8 | dakeni Q1 | rule 8 | わりに / にもかかわらず / ものの: three "expected result" kills in one clause | options わりに / **だけに** / どころか / からといって (the SK p.75 ▲ 部分否定 kill) | rule 8 |
| F9 | mononara Q2 | SK frame (flagged by vi) + second parse | 「運べるものなら運んでみてよ」 follows SK p.78 ③ 「やれるものならやってみろ」. ものを also parsed as noun + を (「運べるものを運んでみて」) | new stem: a wish to talk with a late grandfather. Options **ものなら** / ものの / ものを / からには | rule 13 |
| F10 | tai-garu Q1, Q2 | rule 13 (official) | Q1 (grandmother wants to dress the grandchildren; they 着たがらない; distractors てほしがる/着せたがらない) ≈ 12/2024-36 (parent wants the child to play piano; やりたがらない; distractors てほしくない/やらされない). Q2 (うちの犬 + 怖くて) ≈ 7/2018-37 (うちの犬 + 行きたくなかった). Both are cited in `sources` | Q1 → the younger brother and a new game: 遊びたい / 遊ばせたがる / **遊びたがる** / 遊びたがらない. Q2 → a sister who is afraid of the dark | RULE-MISSING at authoring time |
| F11 | tehajimete Q2; ja nuance | **auto: official scenario copy**; rule 15 | 「海外で一人で生活してはじめて、自分の国の文化について深く考える」 = official 12/2013 問題8-48 「留学中、自分の国のことを聞かれて初めて…気づいた」. It is not cited, and the 10-char scan misses it. The ja nuance 「後に否定の文は来ない」 is not the SK ▲ | Q2 → teaching a friend maths → 説明の難しさに気がついた. The nuance keeps only what SK states | **RULE-MISSING**: rule 13 covers cited official items only (R1) |
| F12 | tokorodatta Q1, Q2 | rule 13 | Q1 (もう少しで + a household near-miss + distractor つもりだった) ≈ 12/2024-40 (もう少しで…洗濯するところだった, distractor つもりだった). Q2 (a mistake → 危うく late for an interview) ≈ SK p.101 ③ (oversleeping → 危うく試験が受けられない) | Q1 distractor → 焦がしそうもなかった. Q2 → nearly sending internal files outside the company | rule 13 |
| F13 | te-irai Q2 | rule 13 | 「注意されて以来…甘いものを一切口にしていない」 ≈ SK p.27 ③ 「子供が生まれて以来、外で酒を飲んでいない」 (since an event, has not consumed X) | → 「毎朝の散歩を一日も休んでいない」 | rule 13 |
| F14 | nitotte Q2 | rule 13 ×2 | 「古い辞書は私にとって…大切なもの」 ≈ SK p.97 ③ (an ordinary stone is a treasure to me). My first replacement (「夜遅くまで開いている…スーパー」) hit official 12/2012-40's stem in the re-scan | → 「駅のすぐ前にある新しいマンションは、車を持っていない人たち（にとって）…便利だ」 | rule 13 |
| F15 | nimokakawarazu Q2 | rule 13 | 「雪が激しく降っているにもかかわらず、配達の人は時間どおりに届けてくれた」 ≈ SK p.74 ① (workers keep working in bad weather) | → a dictionary published twenty years ago that is still used. からといって is killed by the ▲ 部分否定 rule, ばかりに by its "bad result" rule | rule 13 |
| F16 | karatoitte Q2, ex2 | weak distractors + template | 「降っているおかげで…中止になるわけではない」 ("it's not thanks to X that…") and the ばかりに scope reading are grammatical. ex2 「眠いからといって、授業中に寝てはいけない」 ≈ SK ②③ + official 12/2022-36 (sleeping late on a day off) | options **からといって** / だけに / うえに / どころか. ex2 → driving on an empty road | rule 1 / rule 13 |
| F17 | tekaradenaito ex2, Q2; ja usage, compare | rule 13 / rule 15 | ex2 (can't enter the venue until you buy a ticket) ≈ SK p.27 ③ (can't board until cleaning is done). Q2's 「〜かどうかわからない」 = ②'s predicate. ja 「規則・手順…でよく使う」 is unsourced. compare 「後に肯定の文」 narrows SK's wording | ex2 → site registration. Q2 → 「洗濯機には入れないほうがいい」. Prose restated in SK wording | rule 13 / rule 15 |
| F18 | wo-tsuuji-te ex1, tsuide-ni ex2, naidemonai ex2 | rule 11 | ex1 and Q1 are both regional climate year-round. ex2 and Q2 are both 出張のついでに + a visit. naidemonai ex2 (「怒った理由も、わからないでもない」) printed Q2's answer on the card | a museum open all year / 犬の散歩のついでに / 「寂しそうに見えないでもない」 | RULE-MISSING at authoring time |
| F19 | ni-kagira-zu ex3 | rule 13 (復習 line) | 「子どもに限らず大人も」 reuses the 6課 〔復習〕 pair 子供だけでなく大人も | → 男性に限らず女性の間でも…流行っている | rule 13 |
| F20 | neba official_count | wrong count | 7/2012-43 has a 2×2 option set (なければならない / なくていい × としたら / ことで). The key's なければならない is contrasted | 1 → 2; the source note says why | rule 12 (see §4) |
| F21 | kara-suru-to | rule 5 | 「から見ると」 is in the pattern, reading and connection, but SK p.134 lists only からすると・からいうと, and no official key has it | removed; ex2 → 足跡の大きさからすると. ja/vi usage and nuance rewritten; the frequency claims were cut | rule 5 |
| F22 | adv-ittai | rule 15 | connection and prose required a 疑問詞 (「いったいだけでは文にならず、疑問詞…が必要」). SK p.159 states only 文末 = 質問 | 接続 → 「いったい 〜 ＋ 質問の文末」. The 疑問詞 point is now a tendency backed by the archive (2/2 keys) | rule 15 |
| F23 | vi pane, 26 strings | metadata leak | "SK:", "SK ghi…", "SK p.129", "(SK 3課5)", "(13課3)": source tags in learner prose. B0–B3 have none. **B5's vi has 27** | stripped; the sentences reworded | RULE-MISSING (R3) |
| F24 | vi to-no-koto compare | rule 15 (flagged by vi) | "Ở nghĩa 'nghe nói', hai dạng này là một" is stronger than SK p.129, which only lists the two in one 伝聞 row | → both are 伝聞 after 普通形; ということだ also has the 結論 use | rule 15 |
| F25 | ja prose, 7 claims | rule 9 | wo-tsuuji-te 「電話のような直接的な道具」 (電話を通して is ordinary Japanese); neba 「以上・ためにはとよく使われる」 (this also hinted at both quiz stems); tsuide-ni 「後の行動は話し手の意志」 (SK外, no page); naidemonai 「ことも多い」; tai-garu 「ことが多い」; tokorodatta 「よく使う」; nomi (F7) | cut or restated | rule 9 |
| F26 | ni-kagira-zu, nimokakawarazu | coordinator request | — | related += g-ni-kagiri / g-nikakawarinaku (B6). Both panes' `compare` now contrast them, written from B6's items: に限り narrows the range; にかかわらず (no にも) means 〜に関係なく | — |

For every changed quiz item, both explanations were rewritten from the item. The vi explanations each target their own
distractor; for example, nomi Q2 ja targets ばかりか while vi targets しか/だけでなく. Every changed example has a new vi
`example_notes`.

**Provenance** (`QA4_prov.py`: 10-char windows, key spliced into each stem, run over `refs/**/*.md` + `tests/imported-*`)
was re-run after the fixes. It finds stock phrases only (ことができます, ご注意ください, なければならないので,
ていない人たちにとって, …). I also ran a kanji-bigram overlap of every stem against all 問題7–9 items
(`QA4 bigram scan`, inline), and read its 4 hits: none is a copy.

**Checks after the fixes:**
- **vi rule 6** (`QA4_vi6.py`): nothing outside 「」 except grammar labels (thể て/た/ない/ます, ナ/イ形容詞, 課).
- **Bands** (`knowledge_data.plain`): ja maxima are meaning 33, usage 88, nuance 80, compare 83, quiz 79. vi maxima are
  67/153/151/152/141. Nothing sits at a cap.
- **Furigana:** all 993 ruby pairs were listed and read. One reading was wrong (F6).

## 4. The authors' flagged doubts, judged

- **Stem-printed forms (て以来 12/2021-35, ものなら 12/2013-35): COUNTED.** In both items the four options differ only
  in the connection to the form printed beside the blank (されて/される/されている/された + 以来; 行き/行こう/行ける/
  行きたい + ものなら). The item tests that form's 接続 and nothing else. Rule 12's literal "key carries the form" does
  not fit this shape, so I propose an amendment (R4).
- **neba 7/2012-43 reassigned to toshitara: overruled, counted for BOTH.** The option set is a 2×2
  (なければならない/なくていい × としたら/ことで), so each point is contrasted. Rule 10 (the "another entry's headword"
  rule) applies when only one of the two points is contrasted. B1's toshitara count stays.
- **Keys carrying a second headword:** each was judged by what the options contrast.
  - 12/2021-40 ご覧いただきました: the options contrast the verb (参り/拝見/お越し/ご覧), and いただく is on two options.
    It is **goran's** hit.
  - 12/2012-41 行かせたがっている: a 2×2 (使役 × たがる). It counts for both tai-garu and B1 shieki.
  - 12/2021-38 するようにしたことで and 12/2013-41 聞いてもらうことで: both 2×2. They count for koto-de and for B1 you-ni /
    te-morau.
- **参る for 社長 in a 社内朝礼: kill sound, item replaced anyway.** 謙譲 for the listeners' superior is not a common
  native misuse. The item still reused 7/2016-37's scenario and distractors (F3).
- **にもかかわらず / にしては / のわりに sharing one kill in the といったら items:**
  - Q1 had three adversatives (with ものの) and was fixed (F6).
  - Q2 has two (にもかかわらず, にしては) plus に比べて. I kept it: two options sharing one kill is within rule 8, and I
    applied that limit batch-wide (R5).
- **以来 as a distractor in てからでないと Q1: OK.** SK p.27 ▲ says 以来 attaches to 過去のある時点 with a state
  continuing to now. The stem is a standing rule (この薬は…できません) with no past point.
- **vi, ni-kagira-zu Q1 に限り: a real second answer (F1).**
- **vi, rule 14 on 拝見できます and 参っております: both replaced (F2, F3).** 拝見してください was replaced as well.
- **vi, toiuto Q2/ex3 = SK ④: copies (F4).** **mononara Q2 = SK ③: replaced (F9).**
- **vi, to-no-koto compare: widened; fixed (F24).**
- **Counts:** all 25 re-verified; one was wrong (F20). Every 0 holds: といえば, といったら, のみ, てはじめて.

## 5. Cross-batch findings for the coordinator (not fixed: merged files)

- **B1 g-keigo-kudasaru (5):** it counts 12/2019-36 and 7/2025-34. Their keyed string おいでくださり is THIS batch's
  headword, and their options contrast only the verb (まいり/ご覧になり/お目にかかり; 伺い/お越しになり/参り). Under
  rules 10 and 12 they belong to g-keigo-oide, so kudasaru → **3**.
- **B1 g-keigo-itadaku (8):** 12/2021-40 has いただく on two options, uncontrasted, so itadaku → **7**.
- **B6 reverse links:** g-ni-kagiri and g-nikakawarinaku do not yet list g-ni-kagira-zu / g-nimokakawarazu. Adding them
  needs a `compare` in both B6 panes.
- **B5 vi:** 27 "SK"/課 source tags (the F23 class). Its QA should strip them.

## 6. Root causes and proposed rules

| finding(s) | code | proposed edit |
|---|---|---|
| F11, F14 (second hit) | RULE-MISSING | **R1**, SKILL rule 13 + `BATCH_JA_BRIEF.md`: "Compare every quiz stem with ALL official 問題7–9 items, cited or not, not only the ones in `sources`. A scenario an uncited official item uses is the same copy." The 10-char scan cannot see it (12/2013-48 shares no 10-char window). A kanji-bigram overlap lister (≥3 shared content bigrams against `B1_p7.json`/`B1_p89.json`) printed 4 candidates for 50 stems, which is cheap to read. It should be promoted with `official_hits.py` (B3 R3). |
| F2, F3, F10, F12 | RULE-MISSING at authoring time (rules 13/14 postdate B4) | none beyond R1. The B5/B6 authors had the rules |
| F23 | RULE-MISSING | **R3**, `BATCH_VI_BRIEF.md` + `BATCH_JA_BRIEF.md` + SKILL §Written: "Prose never names its source: no 'SK', page numbers or 課 numbers. The card prints `sources`; the prose states the rule." Gate candidate: a WARN on `\bSK\b\|p\.\d+\|\d+課\d` in any language file's prose. The founding strings are B4 vi (26) and B5 vi (27). I have not added it (reviewers do not edit the gate) |
| F20, §4 | RULE-UNENFORCEABLE | **R4**, rule 12 amendment: "Also count a 問題7 item whose four options differ only in the 接続 to a form printed beside the blank (12/2021-35 以来, 12/2013-35 ものなら). A 2×2 option set counts for both points it crosses (7/2012-43, 12/2012-41, 12/2021-38, 12/2013-41); rule 10 applies only when one point is uncontrasted." |
| F6, F7, F8 | RULE-UNENFORCEABLE | **R5**, rule 8 clarification: "A meaning cluster is ONE kill: adversatives (わりに/にもかかわらず/ものの/にしては) or restrictives (のみ/に限り/に限って/さえ・すら as 'extreme'). At most two options may share it." |
| F9 | RULE-MISSING | **R6**, QA brief step 1: "Splice every もの/こと distractor in both parses: conjunctive and noun + particle (「運べるものを運んで」)." |
| F21, F22, F24, F25 | RULE-IGNORED (rules 5, 9, 15) | none. The rules are specific. Both briefs already carry the post-B2 lines, but the B4 ja author wrote the frequency claims ("よく", "多い") anyway. Add to `BATCH_JA_BRIEF.md`: "よく・多い need a count" |
| F4, F5, F13–F19 | RULE-IGNORED (rules 3, 11, 13) | none. The two-column SK table that B2 QA proposed would have exposed F4, F13 and F15 at authoring time |

## 7. Coverage

- Blind solve on all 50 items, then a splice of all 150 distractors. After the fixes, every re-authored item was spliced
  again.
- SK page read for all 17 SK-cited entries. The 8 official-only entries were read in booklet.md.
- official_count re-verified for all 25 entries across 問題7 keys, 問題8 cards and 問題9 in the 31 sittings.
- Provenance: 10-char scan plus the bigram scan against official items, before and after the fixes, and a hand
  comparison against each cited SK page (numbered examples, 〔復習〕 lines and neighbouring headwords) and every cited
  official item.
- Gate: B4 + B6 merged into a scratch copy, rebuilt, `check_knowledge.py`: 0 FAIL, 0 WARN.

## 8. Skips

- `make check` was not run on the real tree. The batch is not merged, and merging is the coordinator's step. The
  scratch-copy gate run stands in for it.
- Speech and pitch were not ear-checked (the 文法 pitch flag is off).
- I did not edit B1 or B6 (§5).
