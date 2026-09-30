# QA report: knowledge/N2 語彙, batch 4 (69 words, 138 examples, 12 → 22 live back-links)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. Files are in the coordinator's scratch
`batches/`; the pre-review copies are in `scratchpad/QAV4_bak/`, and `QAV4_patch.py` rebuilds every fix from them.
sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B4.json` | 0df0429abdf5 | 295f60b5ee18 |
| `語彙_B4.ja.json` | 0b3a676ee8cb | 2016b918958c |
| `語彙_B4.vi.json` | 28d679146c74 | a308c1d20c77 |
| `語彙_B4.backlinks.json` | 281d76b20b3d | 096db099363b |
| `語彙_B4.backlinks.vi.json` | d3924ce6178a | e4fa3e0bcfcc |
| live `knowledge/N2/語彙.ja.json` | e5827f338b81 | e540e83ab3bb |

## Verdict

`QA: FAIL → fixed (4 finding classes: 26 examples in 23 entries, 12 unlinked look-alike pairs, 8 glosses that contain another headword, 3 prose fields). 0 content findings are open after the fixes.`

**Validation.** `QAV4_gate.py` copies `.agents/` and `knowledge/` into `scratchpad/QAV4_root`. It applies the four live
gloss fixes there, then runs `merge_batch.py`'s own code with REPO set to the scratch root. That code merges B4, applies
both back-link files and checks book order. The script then rebuilds `語彙.html` with `build_knowledge.build_category`
and runs `check_knowledge.check_category`. The result is **0 FAIL, 0 WARN**: 241 entries, 427 generated items (186
reading and 241 meaning), 22 live entries back-linked, cards in book order. The first post-fix run failed three vi
compare bands (190, 193 and 194 of 180 characters). I trimmed them and re-ran.

**Live files.** I patched four live ja meanings (§3) and ran `make knowledge LEVEL=N2`. `make check` exits 0 ("All checks
passed"). Its only knowledge-related warning was that the drill pages were stale against `語彙.json`, which the batch-4
author's live `group` edit had changed. `make drill LEVEL=N2` cleared it. Straight afterwards another context merged
文法 B10 and edited `check_knowledge.py` (not me), and the drill pages became stale against `文法.json`. The other
warnings concern the exam pools and papers. They predate this work, and none is on a knowledge line.

**No reading, Hajimete number or official count is wrong.**

## 1. Readings, Hajimete numbers, groups, senses

- **Readings.** I checked all 69 by hand. 48 have a kanji headword, and every one gets a generated reading item. 18 of
  those 48 are confirmed by an official 問題1 key or 問題2 kana stem that I read in `booklet.md` and the key, for example
  7/2014 1-1 おおはば, 12/2016 1-4 ともなう, 12/2013 1-3 しせい, 12/2023 1-5 びょうどう, 12/2024 2-10 あつかましい and
  12/2012 2-6 おとずれる. I checked the other 30 on the Hajimete page furigana (next point). The 21 kana/katakana words
  get no reading item, which is correct. Katakana readings (`ぷらん`, `にーず`) follow the live convention (`すむーず`).
- **Furigana.** I read all 798 distinct ruby pairs across the five files after the fixes. There are no errors. The pairs
  checked in context include 九十歳《きゅうじゅっさい》, 声《ごえ》 (うなり声), 岸《ぎし》 (向こう岸), 止《ど》 (日焼け止め),
  推《お》/量《はか》 (推し量る), 傷《いた》 (傷んだ) and 三《みっ》 (三つ).
- **Reading distractors.** No distractor is a valid reading of its headword. 改める's distractor あらためて is 改めて's
  reading, not its own. The 186 reading items did not change during the fixes.
- **Hajimete numbers.** I opened every cited page, all 40 of them: PDF 180, 182, 183, 185–188, 196, 197, 201, 202, 205,
  206, 208–210, 217, 218, 220, 221, 225–235, 242–244, 246 and 251–258. That covers all 61 numbered words. Every
  number, `page` (PDF page) and headword is right. Every `group` matches its section on the page. The chapter-11 labels
  (性格 1327–, いい気分 1356–, ブルーな気分 1374–, プラスのイメージ 1396–, マイナスのイメージ 1415–) confirm the author's
  inventory note and the author's two live `group` fixes (温厚 → 性格, 快い → いい気分).
- **Unnumbered words.** あいまい, あわただしい, いらいら, おそらく, ぐったり, じたばた, すっきり and ずるい are not Hajimete
  headwords. すっきり appears there only inside the example sentences for 気味 and 気分転換.
- **Senses (rule 27).**
  - **こぐ**: Hajimete No.1001 gives rowing only (「ボートをこぐのが得意だ」, gloss "row / 划(船) / chèo"). The meaning and
    both examples are about rowing. The bicycle sense is correctly absent.
  - **プラン, FIXED.** The page gives 「夏休みのプランを立てる」 plus 計画, and the one cited item, 12/2013 5-24, keys 計画.
    ex1 「旅行会社で、温泉に二泊するプランを申し込んだ」 and the usage 「料金プラン」 teach a sense on neither: a
    bookable package. That sense occurs only in official 読解/聴解 (12/2024, 7/2011, 7/2017 script), and those are
    scenes the example would then copy. ex1 → 「結婚式の細かいプランを決めるのに…」. usage → 「将来のプラン」.
  - **深刻, FIXED.** The page (「少子化は深刻な問題だ」) and both official items (7/2010 6-30 key 「深刻な悩み」, 12/2023
    5-23 = 重大な) give the grave-situation sense. ex2 「父の深刻な顔」 (a grave look) is in neither and is not covered by
    the meaning. It is replaced (§4 E14), and 「深刻な顔」 is out of the vi usage.
  - **Other senses, checked.** Hajimete prints both senses of 訪れる, 視野, 姿勢 and 見逃す. 見逃す's "miss a programme"
    sense in the vi pane is backed by the 12/2019 2-9 stem 「楽しみにしていたドラマをみのがしてしまった」. The page also
    prints both senses of だらしない (① sloppy, ② 「部長はだらしない」 = weak), 流す (① 涙, ② 音楽) and うなる (① dog
    growl, ② groan).

## 2. official_count: hit by hit for all 69

`QAV4_find.py` prints every parsed 問題1–6 item whose stem or options contain the word's form. The parser cannot split
12/2010, so I grepped that booklet's 問題1–6 lines by hand. They hold one B4 hit: 4-20 key 相次いで (count stays 1). 冷静
there is a 問題8 card, which 語彙 does not count.

- **All 69 counts are correct**, including the two 2s: 衰える (7/2019 4-17 key おとろえた, 12/2024 4-15 key 衰えて) and
  深刻 (7/2010 6-30 headword, 12/2023 5-23 underlined word). あいまい is 3 (7/2010 4-21 key, 7/2013 5-24 underlined
  word, 7/2019 4-16 key).
- **The ten 0s are confirmed**: うなる (only うなずく 12/2019 4-19 matches), こぐ, 思いがけず, もむ, 肌 (12/2023 4-18 has it
  only in the stem), つや, 実に (7/2016 5-25 確実に is a substring), 改める (7/2013 1-3 keys the adverb 改めて, which is
  live v-0706 — rule 10), 流す (12/2012 5-26 情報が流れて is 流れる) and 現に.
- **Excluded hits, confirmed on the booklet line.**
  - Distractor-only: 衰えない (7/2010 4-19), 伴って (12/2017 2-7, where 従って is correct), 隠して (7/2018 5-23), 寄付
    (12/2016 4-16), 急激 (12/2018 4-20), 姿勢 (7/2014 4-21), 活発 (7/2011 4-18, 7/2017 4-16), 頑固に (7/2012 4-21),
    あつかましい (12/2017 4-22, 7/2024 4-20, 12/2022 1-5), だらしない (12/2017 5-26), 質素 (12/2013 4-17, 7/2010 4-21),
    かすか (7/2019 4-16, 12/2022 4-17), 名所 (12/2012 4-20), 訂正 (12/2011 4-17), すっきり (12/2012 4-18, 12/2016 4-17,
    7/2015 4-17, 12/2015 4-20), ずるい (12/2015 1-5, 7/2017 1-1) and あやまった (12/2024 1-2).
  - Stem-only: 訪れる (7/2016 5-23, 12/2017 4-18, 7/2010 6-29, 7/2025 2-8), 大幅 (7/2012 4-20, 7/2016 6-32), 名所
    (12/2020 5-21) and おそらく (12/2015 6-31).
  - A different word: 思いがけない (7/2013 5-25) and 誤り (7/2017 5-24).
- **Borderline counts I kept.** ずるい counts the 7/2016 5-27 key (the paraphrase of ひきょうな). That follows the live
  convention for 問題5 keys: 直接, 会計 and 文句 count the same way. 驚かす counts 7/2015 2-7 「驚かせて」 (the ～せる
  variant; no 驚かせる entry exists, and the ja usage names the variant).
- **Rule 35, part 1.** I grepped the `sources` of all 172 live entries for every B4 headword form. No live entry counts
  a hit that belongs to a B4 word.
- **Official-distractor claims in prose.** I checked every quoted option list and misuse fragment in both languages
  against the booklet line, and all are real. Examples: 大幅 「おおふく」「だいはば」「だいふく」, 伴う 「はらう」「あつかう」「すくう」,
  急激 (準備／パン／ファン), 行方 (バス／高層ビル／日曜日), 頑固 (瓶のふた／体／守り), だらしない (味／草／知識; vi "súp nhạt"
  = 塩がたりなかった), 心強い (姉／英語／人間) and あわただしい (気温／忘れ物／町の発展).

## 3. Generated quizzes: every item dumped and read, in both languages

`QAV4_dump.py` runs `quiz_gen.generate()` over the merged 241 entries. The dumps are `QAV4_quiz.txt` (pre-fix) and
`QAV4_quiz2.txt` (post-fix). `QAV4_mq.txt` holds the 181 meaning items that have a B4 key or a B4 distractor. I read
every one.

- **No current distractor glosses its key.** The fixes changed no distractor entry and no key position. Only gloss
  texts changed, and I re-read every item they appear in.
- **Pos decides what is reachable.** The generator ranks candidates by (same `pos` first, hash), so a cross-pos pair
  appears only when the key's pos string is rare. くたくた (ナ形容詞・副詞) draws 名詞 distractors today, so 疲労 is a
  live risk for it. The links below cover pairs a same-pos draw can produce now, plus the author's flagged cross-pos
  pairs as prevention (rule 28, B2 addition).

| pair | verdict |
|---|---|
| 寄付 / 援助 (live v-0180) | **Link.** 困っている人や団体…のために、お金や物を差し出す vs 困っている人を、お金や物などで助ける. The glosses are near-identical, share no kanji and are both 名詞; 援助 already sits in 訂正's item. |
| 予測 / 見当 (live v-0406) | **Link.** 前もって推し量る vs だいたいこうだろうと考える。予想. Both 名詞. |
| 頑固 / わがまま (live) | **Link.** vi 「わがまま」 "Ích kỷ, bướng" glosses 頑固 "Cố chấp". Different pos strings, so this is prevention. |
| 厚かましい / わがまま (found in QA) | **Link.** 自分の都合ばかり考えて vs 周りのことを考えず、自分のしたいように. |
| すっきり / 快い (live) | **Link.** vi "dễ chịu" appears in both glosses. |
| 疲労 / くたくた (live) + ぐったり | **Link, all three.** くたくた's rare pos makes 疲労 reachable; ぐったり–くたくた was already linked. |
| 冷静 / 温厚 (live) | **Link.** Both ナ形容詞; vi "điềm đạm" is in 温厚's gloss and reads as 冷静. |
| 活発 / 陽気 (live) | **Link.** 陽気's vi gloss "hoạt bát" is 活発's Hán Việt. |
| 衰える / 傾く (live) | **Link.** Both 動詞. 傾く's gloss 「会社などの勢いが弱くなる」 and 衰える's 「力や勢い…が弱くなる」 said the same thing. |
| 急激 / たちまち (live) | **Link.** The official 急激 misuses 「急激に売れていく」「ファンが急激に取り囲んだ」 are たちまち territory. |
| 姿勢 / スタイル (live) | **Link.** Both 名詞: 体の構え方 vs 体つき, vi "Tư thế" vs "Vóc dáng". 格好 was already linked to both. |
| 要求 / 催促 (found in QA) | **Link.** Both 名詞, and both glosses end 「相手に…求めること」. |
| 隠す / こそこそ | **No link.** 動詞 vs 副詞, so they are never paired. The rule-34 defect is fixed instead (next point). |

- **Glosses that contained another headword (rule 34).** `QAV4_glosshw.py` searches every ja `meaning` for every other
  headword (word or verb/adjective stem). **Fixed in B4**:
  - 視野 contained 範囲 → 「目で見渡せる広さ。また、物事を考えるときの広がり。」
  - 衰える contained 勢い → 「力や働きなどが、だんだん弱くなる。」
  - 心強い contained 頼 (頼る/頼もしい) → 「支えになるものがあって、安心できる様子。」

  **Fixed in the live file, because B4 adds the headword they contain**:
  - 逆らう v-0017: 流れ → 「水や風の進む向き」 (流す is a same-pos 動詞)
  - こそこそ v-0092: 隠れて → こっそり
  - 荒れる v-0948: 肌 → 皮膚
  - 傾く v-0949: 勢いが弱くなる → 経営が悪くなる (勢い v-0793)

  The remaining hits are `related` pairs (改正 ⊃ 改め, ひきょう ⊃ ずるい), substrings (確実に, どうなる) or live-only pairs
  that B4 does not touch. They are listed in "For the coordinator".
- **おそらく vs 文法 g-adv-osoraku.** The glosses were near-copies: ja 「たぶん。きっとそうなる…」 vs 「たぶん。…そうなる
  可能性が高い」, and vi "Có lẽ, chắc là (nói khi đoán)" vs "Có lẽ, chắc là (phỏng đoán)". 「きっと」 also overstated the
  word's certainty. → ja 「たぶん。そうなるだろうと推測する気持ち。」, vi "Có lẽ, nhiều khả năng là (khi đoán)". ex2 had the
  frame of the 文法 quiz 1 stem (someone's expected act is missing → guess the reason); it is replaced (E21). ex1 and
  the 文法 examples share no scene.

The new live back-links (10 entries) go in the back-link files. That makes 22, up from 12: 援助, 見当, わがまま, 快い, 温厚,
陽気, 傾く, たちまち, スタイル and 催促 are added, and くたくた's existing entry gains 疲労. Each has a complete new compare in
both languages. The B4 side has 13 new `related` ids, and the compares of 寄付, 予測, 頑固, 厚かましい, すっきり, 疲労,
ぐったり, 冷静, 活発, 衰える, 急激, 姿勢 and 要求 are rewritten to cover them. I wrote every compare from the items, not
translated from the other language.

## 4. Examples: provenance, frame, naturalness

The 10-char scan (`QAV4_prov.py`) covers `refs/**/*.md`, `tests/imported-*`, every scratch batch and `knowledge/**`. It
found only function-word overlaps in the examples. Then came the rule 13/21/31/35 table (`QAV4_table.txt`). It puts
every example beside the Hajimete example on its page, the SK/Soumatome lines, every official item or 読解/聴解 line that
holds the word, and every knowledge card, stem or open batch that holds it. I also grepped the whole module for scene
nouns (台風, 地震, ピアノ, 子犬…).

| # | entry | finding | fix |
|---|---|---|---|
| E1 | プラン ex1 | Sense on no cited page (§1). | → 「結婚式の細かいプランを決めるのに、二人で半年もかかった」 |
| E2 | 思いがけず ex1 「…作文が、思いがけず賞をもらった」 | The subject 作文 cannot receive a prize. | → 「…作文で、思いがけず賞をもらった」 |
| E3 | 名所 ex1 「有名な名所よりも、小さな路地を歩くのが好きだ」 | The claim of the 12/2011 読解 (skip the 観光名所, go to the market), and 有名な名所 is redundant. | → 「その古い橋は、今では町を代表する名所になっている」 |
| E4 | 疲労 ex2 「疲労を回復させるには、十分な睡眠が一番だ」 | The claim of the 7/2023 問題7 stem 「睡眠には…疲労をとる効果がある」. | → 「マラソンのあと、足に疲労が残って…」 |
| E5 | 衰える ex2 「…食欲が少しも衰えない」 | 食欲が衰える is the 7/2022 聴解 script line. | → 「…好奇心が少しも衰えない」 |
| E6 | 負担 ex1 「重いかばんを毎日持ち歩くと、肩に負担がかかる」 | The frame of the 文法 example 「重い荷物を持って階段を上るのは…負担だ」 and the 12/2022 読解 claim (sitting posture → load on the back). | → 「転勤にかかる引っ越しの費用は、会社が半分負担してくれる」 (the cost sense of the usage line) |
| E7 | 負担 ex2 「新人に仕事を任せすぎると…」 | The claim of the 7/2023 読解 (仕事を覚える側の負担). | → 「一人で三つの係を引き受けるのは、負担が大きすぎる」 |
| E8 | 肌 ex2 「このせっけんは、肌にやさしい材料で…」 | The scene of 7/2011 問題7-41 (せっけん and 肌). | → 「肌が弱いので、洗剤を使うときは手袋をしている」 |
| E9 | 急激 ex1 「山の天気は変わりやすく、気温が急激に…」 | The premise of 文法 B10 g-ni-koshi-takotohanai 「山の天気は変わりやすい」. | → 「夜になって気温が急激に下がり、道が凍ってしまった」 |
| E10 | 姿勢 ex1 「…姿勢が悪いと腰を痛めやすい」 | The claim of the 12/2022 読解 (姿勢 → 腰への負担 → 腰痛). | → 「写真を撮りますから、みなさん姿勢を正してください」 |
| E11 | 改める ex2 「駅の案内板は…表示を改めた」 | The subject 案内板 cannot act. | → 「駅では、…案内板の表示を改めた」 |
| E12 | 流す ex2 「この店では、いつも静かなピアノの曲を流している」 | Live ふさわしい 「静かなピアノの曲は…」, plus the store-music scene of the 12/2019 2-8 stem and the 12/2017 script. | → 「空港では、飛行機の出発が遅れるという放送を、何度も流していた」. The usage (ja 「放送を流す」) and vi meaning ("thông báo") now cover it. |
| E13 | 隠す ex1 「弟は、点数の悪かったテストをベッドの下に隠していた」 | The frame of 漢字_B3 「妹は、父へのプレゼントを本だなのうしろに隠しておいた」. | → 「泥棒は、盗んだ宝石を庭の土の中に隠していた」 |
| E14 | 寄付 ex1 「地震で被害を受けた町に…寄付した」 | The scene of the 12/2010 読解 (地震で家を失った人のために寄付した). | → 「ある会社が工場の跡地を市に寄付し、そこは公園になった」 |
| E15 | 深刻 ex1 「医者の足りない地域では、深刻な状況が続いている」 | The SK 「水不足が深刻」 and 12/2011 「家不足が深刻」 frame (shortage → serious). | → 「空気の汚れが深刻になり、外で運動できない日もある」 |
| E16 | 深刻 ex2 「父の深刻な顔」 | Unsourced sense (§1), and 7/2016 読解 has 「深刻そうな顔」. | → 「会社の経営が思ったより深刻な状態だと知って…」 |
| E17 | 中継 ex1 「今夜のサッカーの試合は、テレビで生中継される」 | The 7/2016 読解 line 「その試合が深夜にテレビで生中継された」. | → 「毎年の花火大会は、地元のテレビ局が生中継している」 (bold now on 中継) |
| E18 | 訂正 ex1 「新聞社は…翌日訂正を出した」 | The Hajimete frame (a news outlet corrects its own error). | → 「申込書の電話番号を書き間違えたので、二重線を引いて訂正した」 |
| E19 | 典型的 ex2 「…私の典型的な一日の始まりだ」 | Unnatural (a calque of "my typical day"). | → 「この病気の典型的な症状は、高い熱とせきだ」 |
| E20 | 清潔 ex2 「病院のシーツは毎日取り替えられ、いつも清潔だ」 | The frame of 漢字_B3 「子どもが使うタオルは、いつも清潔なもの」. | → 「看護師に、傷の周りをいつも清潔にしておくように言われた」 |
| E21 | 冷静 ex2 「火事のときこそ、冷静な判断が必要だ」 | The scene of an SK 漢字 table line (火事 and 冷静). | → 「負けている時こそ、監督には冷静な判断が求められる」 |
| E22 | あわれ ex1 「雨の中、捨てられた子犬があわれな声で鳴いていた」 | The scene of 文法 g-te-ageru 「雨の中で鳴いていた子犬を…」. | → 「けがをして飛べなくなった小鳥が、あわれな声で鳴いていた」 |
| E23 | おそらく ex2 | The frame of the 文法 quiz stem (§3). My first rewrite (「いつも行列ができているから…」) reused the 12/2014 問題7-40 scene, so I discarded it. | → 「隣の部屋の電気が消えているから、おそらくもう出かけたのだろう」 |
| E24 | すっきり ex1 「一晩ぐっすり寝たら、頭がすっきりした」 | The scene of the 7/2024 6-28 misuse 「よく眠ったので…頭がはきはきとしている」, with the right word put in. | → 「熱が下がって、ようやく体がすっきりした」 |
| E25 | すっきり ex2 「冷たいシャワーを浴びると…すっきりする」 | The claim of the 12/2011 読解 (冷水で顔を洗う → 頭をすっきりさせる). | → 「長い間悩んでいた問題が解決して、気分がすっきりした」 |
| E26 | ずるい ex2 「宿題を友達に写させてもらうような…」 | The scene of an SK あつかましい line on the cited p.125 「ただで宿題の答えを教えてもらおうなんて」. | → 「テストのときにこっそり教科書を見るのは、ずるいことだ」 |

- **Checked without change.**
  - 伴う ex2 (typhoon with rain and wind approaching) against the 7/2013 script 「雷を伴った」. The predicate differs.
  - ニーズ ex2 (a town survey) against the 読解 options 「ニーズ調査を行う」 and 「消費者のニーズを調べて」. It is an
    event, not either passage's claim.
  - 心強い ex2 against Hajimete 「彼がいてくれると…」. The subject and the cause differ.
- **vi notes.** Every changed example has a new vi `example_notes` translation, written from the Japanese. A scan of the
  new sentences against refs, knowledge and all batches is clean.

## 5. Prose

- **Rule 35 restrictions.** An entry's own examples must satisfy its prose. 流す's usage and vi meaning now cover
  「放送を流す」; 衰える's new gloss covers 人気/好奇心-type 力. プラン and 深刻 no longer teach a sense their prose and pages
  lack.
- **Hán Việt notes.** I checked each one against the Hajimete VI gloss (rule 35). None contradicts it, including
  改正 "cải chính" (a Vietnamese word meaning "correct false news", flagged correctly with 訂正 as the Japanese for
  that), 深刻 "thâm khắc", 活発 "hoạt bát", 頑固 "ngoan cố", 清潔 "thanh khiết" and 貴重 "quý trọng".
- **vi quoting.** A script found no Japanese outside 「」 except the label ナ形容詞 (allowed by rule 6).
- **Citations in prose.** There are none in any language: no sitting date, SK or page reference. Short official misuse
  fragments follow the B1–B3 practice.
- **Translation check.** vi is not a translation of ja. The collocation lists, the trap framing and the Hán Việt notes
  differ throughout.
- **Bands.** After the fixes, everything is within the bands. The largest fields are the ja ぐったり compare at 83 of
  100, the ja 続出 back-link at 88 of 100 and the vi 姿勢 compare at 180 of 180.

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| E3, E4, E7, E10, E14, E16, E17, E25 (official 読解 or 聴解 claim or scene) | The author's provenance table compared examples with 問題1–6 stems, Hajimete and SK. Rule 31 ("an official 読解 passage's claim counts as a scene") was never applied to 語彙 examples, and a 10-char window cannot see a paraphrased claim. | LEX_JA_BRIEF: *grep every 読解 passage and 聴解 script that contains the headword, and write the claim each one makes, before writing an example.* |
| E6, E9, E12, E13, E20, E22, E23 (cross-module scene) | Rule 35 extends rule 11 to the whole module, but the author compared only the live 語彙 file, not 文法 examples and quiz stems or the open 漢字/文法 batches. | Add to the brief: *grep the headword's key noun in `knowledge/N2/*.json` AND every open `batches/*.json`, and read the hits.* |
| E24 (an official misuse, corrected) | The author checked the key's own items, not the misuse sentences of *other* 問題6 items, which name the right word only implicitly. | Extend rule 21 to 語彙: *an example may not be an official 問題6 wrong option with the right word put back.* |
| E1, E16 (sense) | Rule 27 is applied to `meaning`, and the examples slip past it. | Rule 27 already says "or an example". Add to the brief: *list each example's sense beside the page gloss in the hand-off table.* |
| E2, E11, E19 (naturalness) | No subject/predicate or naturalness read of the examples. | QA-only; keep. |
| 12 look-alike pairs | The vi author flagged 10 pairs but may not edit the shared file (B3 finding, repeated). No step asks who links them. | SKILL rule 28 addition: *the vi author's flagged pairs are linked by the coordinator or QA before merge; QA also dumps each pos class to find same-pos glosses that share an ending (「…求めること」).* |
| 8 glosses containing a headword | Rule 34 was written for 漢字. Nothing checks 語彙 glosses for other headwords, and a batch adds headwords that live glosses already contain (隠す ⊂ こそこそ). | Gate: *WARN when a 語彙/漢字 `meaning` contains another entry's headword or verb stem, unless the two are `related`* (`QAV4_glosshw.py` is a working prototype). |
| おそらく gloss near-copy of 文法 | The author read 文法.ja.json as a tone model and did not compare it with the 文法 card of the same word. | Add to the brief: *when a 語彙 headword is also a 文法 card, write a gloss and scenes distinct from that card's.* |

## For the coordinator

- **Merge.** Run `merge_batch.py 語彙 4`. It applies 22 back-links (12 from the authors, 10 from QA). Then run `make
  knowledge`, `make drill LEVEL=N2` and `make check`.
- **Live edits already made.** Four live ja meanings are patched in `knowledge/N2/語彙.ja.json`: 逆らう v-0017, こそこそ
  v-0092, 荒れる v-0948 and 傾く v-0949 (§3). The pre-edit copy is `scratchpad/QAV4_bak/live_語彙.ja.json.pre`. Keep
  these edits when merging: the merge reads the live files, so nothing overwrites them. The author's two live `group`
  fixes in `語彙.json` (温厚, 快い) are correct (§1).
- **Live-only gloss hits, not fixed.** These pre-date B4. 頼もしい contains 任せ, 福祉 contains 暮ら, ふさわしい contains
  場面, 受け入れる and 拡充 contain 組織, ベテラン contains 分野, 中断 contains いったん, 評判 contains 世間, and 快い
  contains 頼 and 受け入れる. All are cross-pos or already `related`, except ふさわしい/場面 and 評判/世間. Those two are
  worth a look in the next 語彙 batch QA.
- **Not mine.** The live 文法 files, `check_knowledge.py` and a new `qa-report-knowledge-N2-文法-B10.md` changed while I
  worked (another context). An untracked `CLAUDE_YOU_MUST_READ_THIS.md` in the repo root is out of this QA's scope, and
  I did not act on it.
