# QA report: knowledge/N2 語彙, batch 5 (60 words, 119 examples, 29 → 31 live back-links)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. Files are in the coordinator's scratch
`batches/`; the pre-review copies are in `scratchpad/QAV5_bak/`, and `QAV5_patch.py` rebuilds every fix from them.
sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B5.json` | 8df7f7915e87 | 973195893212 |
| `語彙_B5.ja.json` | f10c23948862 | 04de23713ebc |
| `語彙_B5.vi.json` | 978a22683b2e | 1c5b3e184e64 |
| `語彙_B5.backlinks.json` | a353e6124613 | c36e2b33db4c |
| `語彙_B5.backlinks.vi.json` | bbba2fd5110f | 43a4eed11d90 |
| `V5_live_meaning_fix.json` | de55b2e46f88 | 7c03bccf740b |

## Verdict

`QA: FAIL → fixed (5 finding classes: 17 examples in 16 entries, 4 unlinked look-alike pairs, 9 prose/source fields, 1 live gloss fix corrected + 1 added). 0 content findings are open after the fixes.`

**Validation.** `QAV5_gate.py` copies `.agents/` and `knowledge/` into `scratchpad/QAV5_root`. It applies the six
meanings in `V5_live_meaning_fix.json` there, then runs `merge_batch.py`'s own code with REPO set to the scratch root.
That code merges B5, applies both back-link files and checks book order. The script then rebuilds `語彙.html` with
`build_knowledge.build_category` and runs `check_knowledge.check_category`. The result is **0 FAIL, 0 WARN**: 301
entries, 535 generated items (234 reading and 301 meaning), 31 live entries back-linked, cards in book order, and no
`REVIEW` line from the merge. The first post-fix run failed one band (the vi ぼんやり compare, 183 of 180 characters). I
trimmed it and re-ran.

**Live files.** I edited no file under `knowledge/`. `make check` on the untouched repo exits 0 ("All checks passed",
224 warnings). None of those warnings is on a knowledge or drill line.

**No reading and no official count is wrong.**

## 1. Readings, headwords, groups, senses

- **Readings.** I checked all 60 by hand. 48 have a kanji headword, and each gets a generated reading item. 38 of those
  48 are confirmed by an official 問題1 key, a 問題2 kana stem, or a kana option or printed ruby that I read in
  `booklet.md` and the key. Examples: 12/2019 1-5 げじゅん, 12/2020 1-5 かこう, 7/2013 1-1 よのなか, 12/2025 1-4
  あらそって, 7/2025 1-5 おさまった, 7/2011 2-10 へんこう, 12/2019 1-3 option ぶんたん, 7/2024 1-2 option ぶんかい and
  7/2017 4-21 ruby けいき. The other 10 are standard readings: いちおう, ほぞん, どうさ, あいず, といあわせる, おおげさ,
  どうにゅう, つよみ, のりつぐ and くぎり.
- **Reading distractors.** No distractor is a valid reading of its headword. For example, 怖い is never offered
  おそろしい, and 争う is never offered きそう.
- **Furigana.** I read all 759 distinct ruby pairs, then the 57 new pairs from the fixes. **Fixed:**
  - 下旬's meaning read 一か月 as 一《ひと》か月; it is now 一《いっ》か月.
  - 劣る's nuance put ruby on the official non-word options 悪って, 負って and 乏って (rule 34). The ruby is removed.
  - 争う's nuance read 抗って as 抗《こう》って. 抗う is a real verb, so it is now 抗《あらが》って.

  Checked in context and correct: 三時間《さんじかん》, 五分《ごふん》, 五十種類《ごじゅっしゅるい》, 十《じゅっ》キロ,
  十日《とおか》, 一日中《いちにちじゅう》, 会議の間《あいだ》じゅう, すき間《ま》, 空《あ》き家《や》, 大通《おおどお》り and
  下《さ》がる.
- **Ids and groups.** 58 words are `v-o-*`. I searched the Hajimete extract and its index for all 60, and none is a
  numbered headword. The hits are other words' example sentences, such as 元's 「使ったものは元の場所に戻してください」,
  or other headwords, such as 胸が痛む, 取り戻す and 答案用紙. ぼんやり is the ＋ word of No.1094 ぼうっと on PDF 200
  (section 症状). 区切り is the ＋ word of No.623 区切る on PDF 118 (section パソコン(スマホ)). Both `group` labels match
  the live labels for those sections.
- **Senses (rule 27).**
  - **一応 (doubt 3).** The "ひととおり / 十分ではないが" sense is sourced after all. Shin Kanzen 語彙 PDF 143 (第2部4章3課
    ⑭) prints 「時間は掛かったが、一応料理が完成した」, but it was not cited. ex1, 「料理を習ったことはないが、一応自分の食事
    くらいは作れる」, used the same scene (cooking, done at a basic level). **Fix:** PDF 143 is now cited. ex1 is replaced
    (E3). The ja meaning is now 「完全ではないが、ひととおり。また、とりあえず。」, which drops せめて's gloss words
    「十分ではな…」 (rule 40). The vi meaning and usage now teach both senses (ex2 is the provisional sense of 7/2010 5-23).
  - **戻す ex2** 「最初の話題に戻しましょう」 taught 話を戻す, which is on no cited page. It is replaced with the
    return-to-an-earlier-state sense (E16). Two sources are added: Hajimete PDF 68 (元's example, the place sense) and the
    12/2018 読解 line 「元の大きさに戻す」 (the state sense). 「話を戻す」 is out of the vi usage.
  - **Verified.** たくましい: SK 語彙 PDF 125 prints 「たくましい体」. ふさぐ: Soumatome PDF 99 prints 「耳をふさぐ」. The
    source note claimed 「穴をふさぐ」 there too, but the page prints 「穴を埋める」, so the note is corrected. 収まる:
    Soumatome PDF 117 prints 「予算内に収まる」. ぼんやり: both senses are on Hajimete PDF 200 (ぼうっと ① 上の空, ② ぼうっと
    山が見える).

## 2. official_count: hit by hit for all 60 (rule 35)

`QAV5_find.py` prints every parsed 問題1–6 item whose stem or options contain the word's kanji or kana form (dump in
`QAV5_find.txt`). The parser merges 12/2010, so I grepped that booklet's 問題1–6 lines by hand. They hold no B5 hit.

- **All 60 counts are correct**, including every count above 1:
  - 争う 3: 12/2015 2-8, 12/2020 4-18 and 12/2025 1-4.
  - 劣る 3: 7/2014 2-10, 7/2016 1-5 and 7/2022 4-16.
  - でたらめ 2, ふもと 2, やかましい 2, 偶然 2, 勧誘 2, 垂直 2, 大げさ 2 and 実践 2.
- **Excluded hits, confirmed on the booklet line.**
  - Distractor-only: 12/2022 1-5 (たくましい, やかましい), 7/2023 4-16 (たくましい), 7/2021 4-18 (たまたま), 12/2015 4-20 and
    12/2019 4-20 (ぼんやり), 12/2016 5-24 (もったいない), 7/2014 2-8, 7/2016 1-2 and 7/2021 2-9 (争う), 7/2017 4-18 (保存),
    7/2016 5-23 (偶然), 7/2019 4-17 (傷む), 12/2019 1-3 (分担), 7/2024 1-2 (分解), 12/2011 3-12, 12/2015 3-12 and 7/2025
    3-13 (劣), 12/2020 4-19 (動作), 7/2017 4-21 (合図), 7/2013 4-16 (問い合わせる), 7/2013 4-22 = 12/2021 4-18 and
    7/2014 4-21 (容姿), 7/2024 4-18 (大げさ), 12/2015 1-5 (こわい), 7/2015 1-5 = 12/2021 1-2 (あやしい), 12/2016 1-2
    (くやしい), 12/2013 2-10 (憎めたら) and 12/2013 1-2 (もどす).
  - Stem-only: 保存 (12/2017 6-28, 7/2018 1-2), 冷蔵庫 (7/2017 6-30, 12/2018 6-26, 12/2022 6-30), つねに (7/2021 2-9,
    12/2019 6-29), 怪しい (12/2018 3-12), 区切り (12/2012 6-28) and 企画 (7/2016 4-21, 7/2022 4-15).
  - A different word: 収める (12/2022 5-22), 治まる (7/2014 5-26), 努める (12/2013 2-7), 怖がる (7/2017 5-25), ぶつかる
    (7/2016 5-26), 倒れる (7/2011 1-1) and 戻る (12/2019 5-23).
- **Borderline counts I kept.** 動作 counts the 12/2024 5-25 key, and ぶつける, もったいない and 一応 each count their
  問題5 keys. That follows the live convention (直接, 会計, ずるい). 偉い does not count 7/2024 5-23 偉そうにして, a
  derived form. The batch applies the same rule to 怖がる, so this is consistent.
- **Rule 35, part 1.** I cross-checked every counted and excluded item note in B5 against all 241 live entries'
  sources. Every shared item is credited to the right side, for example 勇ましい ← 12/2022 1-5, 努める ← 12/2013 2-7,
  負担 ← 12/2019 1-3, 分析 ← 7/2024 1-2 and 格好 ← 7/2013 4-22. No live entry counts a hit that belongs to a B5 word.

## 3. Generated quizzes, both languages (rule 28, rule 40)

`QAV5_dump.py` runs `quiz_gen.generate()` over the merged 301 entries. The dumps are `QAV5_quiz.txt` (pre-fix) and
`QAV5_quiz2.txt` (post-fix). `QAV5_mq.txt` holds the 186 meaning items that have a B5 key or a B5 distractor, and I read
every one. `QAV5_glosshw.py` searches every B5-involved gloss, ja and vi, for another entry's headword **and for gloss
words it shares with an unrelated entry** (rule 40), same pos and cross pos.

- **No current distractor glosses its key.** The links below are preventive, because none of the pairs is drawn today.
  The fixes moved no key position.

| pair | verdict |
|---|---|
| たまたま / 思いがけず (live v-1030) (doubt 4) | **Link.** Both are 副詞, so the generator can pair them. The vi glosses share "tình cờ", and 思いがけず賞をもらった reads as tình cờ. They are now `related` both ways, and the compares of たまたま and 思いがけず (back-link, rewritten) contrast chance timing with surprise. |
| ぼんやり / あいまい (live, found in QA) | **Link.** Both ja glosses end 「…がはっきりしない様子」, and the cards list 「ぼんやりした記憶」 and 「記憶があいまいだ」. New back-link. |
| 導入 / 普及 (live, found in QA) | **Link.** Both are 名詞, and both glosses open 「新しい…技術」. New back-link: 取り入れる vs 行き渡る. |
| 分担 / 役目 (vi) | **Gloss fixed, no link.** The vi glosses shared "đảm nhận … phần". 分担 vi is now "Chia một việc chung ra cho nhiều người cùng làm". |
| 一応 / せめて | **Gloss fixed** (§1): 一応's 「十分ではないが」 was せめて's 「十分ではなくても」. |

- **Headwords inside glosses.** None is left. The only hits are substrings (そうなる ⊃ うなる, 雰囲気 ⊃ 囲) and the
  related pair 評判 ⊃ 評価.
- **Gloss-word overlaps I left.** The rest are generic words (相手, 物事, 仕事, 状態) or cross-pos pairs whose glosses
  mean different things. Examples: 出世 / 偉い share "địa vị cao" (rise vs have), and 傾く / 下降 share "đi xuống"
  (business vs height).

## 4. The six live meaning fixes

| entry | edit | verdict |
|---|---|---|
| 普及 v-0487 | 世の中 → 社会 | **Keep.** 世の中 is now a same-pos headword (rule 34 lure). |
| 敗れる v-0786 | 争い → 勝負 | **Corrected.** 争う is a B5 headword, so the edit is needed. But 「試合や勝負で」 no longer covers the card's own ex2 「選挙に敗れた」 (rule 35). It is now 「試合や選挙などで、相手に負ける。」, which matches the usage 「試合・選挙に敗れる」. |
| 豊か v-o-yutaka | たっぷり → 十分に | **Keep.** The words 十分 it now shares with たっぷり and 充実 are all `related`. |
| 役目 v-0006 | 務め → 仕事 | **Keep.** 務める is `related`, but rule 34 bars another headword's kanji regardless. |
| 抱える v-1248 | 囲む → 包む | **Keep.** Same reason. 包む is no headword. |
| 評判 v-0853 | **added by QA**: 世間の人たち → 多くの人たち | B4 QA flagged 評判 ⊃ 世間 as worth a look. Both are 名詞, and B5 back-links 世間. The new gloss keeps only 評価, its `related` partner. |

## 5. Examples: provenance, frame, sense

The 10-char scan (`QAV5_prov.py`, over `refs/**/*.md`, `tests/imported-*`, every scratch batch and `knowledge/**`)
found only function-word overlaps. The frame table (`QAV5_table.txt`) did the real work. It sets every example beside
every refs line (Hajimete, SK/Soumatome 語彙, all official booklets **and scripts**, 問題7–9 included) and every knowledge
card, stem or open batch that holds the word. I also grepped each replacement's scene nouns over the same corpus
before keeping it.

| # | entry | finding | fix |
|---|---|---|---|
| E1 | 囲む ex1 (doubt 1) | Near copy of 漢字 k-0555 「キャンプの夜、みんなでたき火を囲んで歌った」. | → 「誕生日の夜は、家族みんなでケーキを囲んでお祝いをした」. The vi usage, compare and 抱える back-link now quote 「テーブルを囲む」. |
| E2 | 契機 ex1 (doubt 2) | The g-kikkake quiz 2 frame (空港の開港 → ホテルが次々). 文法 also holds 入院 → たばこ and 創立五十周年 → 社名, which I avoided. | → 「子どもが生まれたことを契機に、夫は働き方を見直した」 |
| E3 | 一応 ex1 (doubt 3) | The SK PDF 143 scene (§1). | → 「英語は得意ではないが、道を聞かれて答えるくらいなら一応できる」 |
| E4 | 偶然 ex1 「偶然つけたテレビに…出ていた」 | The frame of 漢字 「偶然開いたページに、さがしていた言葉がのっていた」. | → 「旅先で入った店の主人は、偶然にも父と同じ町の出身だった」 |
| E5 | たまたま ex1 「たまたま入った古本屋で、ずっと探していた本が見つかった」 | The same 漢字 frame (by chance → the long-sought thing turns up). | → 「電車で隣に座った人が、たまたま私と同じ本を読んでいた」 |
| E6 | 下旬 ex1 「桜は三月の下旬に咲き始める」 | The 漢字 example 「毎年、三月の下旬になると桜が咲く」. The first rewrite (暑い日が続く) hit a 文法 stem, so I discarded it. | → 「新しい図書館は、来年三月の下旬に完成する予定だ」 |
| E7 | 世の中 ex2 「世の中には、自分と同じ誕生日の人がたくさんいる」 | The birthday coincidence of 偶然 ex2 in the same batch, plus the 12/2020 読解 frame 「世の中には…人もいる」. | → 「学校を卒業して世の中に出てみると、知らないことばかりだった」 |
| E8 | もったいない ex2 「晴れた休日を、一日中寝て過ごすのは…」 | The 文法 example 「せっかく晴れた休みの日に、一日中家にいるのは、もったいない」. | → 「夕食のおかずが余ったが、捨てるのはもったいないので、翌日の弁当に入れた」 |
| E9 | ぶつける ex2 「頭を扉にぶつけた」 | The 文法 example 「頭を棚にぶつけてしまった」. I rejected a ball (the cited 7/2018 5-23), a car (Soumatome) and 引っ越し + 家具 (文法). | → 「掃除機を家具にぶつけないように、ゆっくり動かした」 |
| E10 | びっしょり ex1 (夕立 → 洗濯物) | The cited 7/2015 4-17 frame (rain soaks clothes). | → 「水たまりに足を入れてしまい、靴の中までびっしょりになった」 |
| E11 | やかましい ex1 「セミが朝からやかましく鳴く」 | SK 語彙 「夕方になると鳥の声がやかましい」 (animals, time of day). 選挙カー was rejected because 選挙 scenes fill two live cards. | → 「大通りに面した部屋は、車の音で一日中やかましい」 |
| E12 | 怖い ex1 「高いところが怖くて、観覧車にも乗れない」 | Fear → cannot do: the 12/2024 問題7-31 stem 「怖くて水に顔をつけること（さえ）できなかった」 and 文法 「怖くてまだ一人で運転したことがない」. | → 「ジェットコースターは、見ているだけでも怖い」 |
| E13 | 悔しい ex1 「あと一問できていれば合格だった」 | Soumatome 「1番違いで宝くじがはずれて、とてもくやしい」 (missed by one). My first rewrite (簡単な計算を間違えて) was a 文法 stem's scene, so I discarded it. | → 「コンテストで一位を取れると思っていたのに、二位に終わって悔しかった」 |
| E14 | 悔しい ex2 「ゲームで負けたのが悔しくて、夜遅くまで練習した」 | The claim of 12/2011 問題8-48 「試合に負けて本当に悔しかったので、もっと強くなるため…」. | → 「駅前に新しい店ができて、常連の客を取られたのが悔しい」 |
| E15 | 実践 ex1 「料理教室で習った包丁の使い方を、家で実践してみた」 | The 漢字 frame 「本で学んだ方法を、毎日の仕事で実践している」 (learned at A → practised at B). Health-habit scenes are in three official scripts, so I rejected them. | → 「この講座は実践を重視していて、授業の半分は実習だ」 |
| E16 | 変更 ex1 「参加者が増えたので、会場を…ホールに変更した」 | The claim of the 12/2018 聴解 script (受講の数が増えたら…別の教室に変更). Venue changes also appear in the 7/2011 and 7/2025 scripts, and パンの大きさ is an official 問題5 scene. | → 「作者は、読者の意見を聞いて、物語の結末を変更した」 |
| E17 | 戻す ex2 | Unsourced sense (§1). | → 「スマートフォンの設定を、買ったときの状態に戻した」 |

- **Checked without change.**
  - 倒す ex1 (a child running knocks over a vase) against SK 「コップを倒して、お茶をこぼしてしまった」. The subject and
    cause differ, and there is no spill.
  - 怪しい ex1 against Soumatome's collocation 「あやしい物音がする」. It is a phrase, not a scene.
  - 刑事 ex1 against live 見当 「犯人がだれなのか、刑事には…見当がついていた」. The predicate differs.
  - 情景 ex1 against the 12/2016 読解 memory passage. That passage makes a claim about how memory records; ex1 does not.
  - 大げさ's two examples follow the 12/2016 6-31 key's sense. Their scenes (an injury, an apology) are not the key's
    scene.
- **vi notes.** Each of the 17 new examples has a new `example_notes` translation, written from the Japanese.

## 6. Prose

| # | field | finding | fix |
|---|---|---|---|
| P1 | ja ふさぐ nuance | 「上からかぶせるだけのときには使わない」 was invented from the three misuses (rule 9); 「ふたで鍋の口をふさぐ」 is fine. | Now it states what the item shows: the object of ふさぐ is a hole or gap, not the 鍋 or 皿 itself. |
| P2 | ja たまたま compare | 「「たまたま〜した」の形で使う」 was contradicted by the card's own ex2 「その日はたまたま…だった」 and its usage (rule 35). | Rewritten, and 思いがけず is added. |
| P3 | vi 偶然 compare | 「たまたま」: "chỉ làm phó từ" (only an adverb). The 7/2019 script says 「たまたまだよ」. | → "phó từ: 「たまたま会う」" |
| P4 | vi 刑事 usage | "Chỉ người làm nghề." overclaims, because 刑事 is also 刑事事件. The nuance already says "ở thẻ này". | Cut. |
| P5 | vi usage lines | 囲む, やかましい, 偶然, 世の中, もったいない, ぶつける, 悔しい, 戻す, 実践 and 一応 quoted the replaced examples. | Realigned. |
| P6 | 豊富 back-link (merge `REVIEW`) | It dropped 「豊かな自然」 from the live compare. | Restored (98 of 100). |
| P7 | 務める sources (doubt 5) | The 勤める claim had no page. | Added SK 漢字 PDF 182 No.661 勤 (出勤・通勤・勤める). |

- **Doubt 5, Vietnamese claims.**
  - 刑事's note is right. "Hình sự" is a Vietnamese word used adjectivally ("vụ án hình sự"), so rule 34 allows calling
    it a trap. The note limits itself to this card, and ex2's "phim hình sự" agrees with it.
  - 情景's note is right. "Tình cảnh" is a Vietnamese word meaning a plight, which is a real false friend.
  - 務める's three-way note is right, and it is now sourced (P7).
  - Neither word is in Hajimete, so rule 35's Hajimete-gloss test does not apply.
- **Other Hán Việt notes.** These are correct: bảo tồn (保存), phân giải (分解), mật tiếp / mật thiết (密接), thiện lương
  (善良), thực tiễn (実践), ấu trĩ, áp đảo, động tác and hạ tuần.
- **Official-distractor claims.** I checked every quoted option list and misuse fragment in both languages against the
  booklet line, and all are real. Examples: 争う 「戦って」「競って」「抗って」 and 「たたかって」「きそって」「ぶつかって」, 勧誘
  「勧遊」「観誘」「観遊」, 垂直 「乗頂」「乗直」「垂頂」, 合図's three misuses, 区切り's three misuses, 乗り継ぐ's three, and
  もったいない's 12/2016 やむをえない item.
- **Back-links.** Every contrast in the old compares is kept, in both panes, for all 31 back-links. I compared each old
  and new compare by hand.
- **vi quoting.** A script found no Japanese outside 「」 and no ruby outside 「」 in any vi field or back-link.
- **Citations in prose.** There are none: no sitting date, SK, page or 問題 number in any prose field.
- **Translation check.** vi is not a translation of ja. I wrote every new compare from the items, never from the other
  pane.
- **Bands.** Everything is within the bands. The largest fields are the ja 豊富 back-link at 98 of 100 and the vi
  あいまい back-link at 173 of 180.

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| E1, E4, E5, E6, E15 (the 漢字 card of the same kanji) | Rules 35 and 39 say to grep the whole module, but a 漢字 card's example for 囲む, 下旬, 偶然 or 実践 uses the same compound, so the frame is nearly forced. The author's table did not put the kanji's card beside the word. | LEX brief: *for each 語彙 headword, print the example of every 漢字 card for its kanji beside yours; a shared compound needs a different scene AND frame.* Gate idea: extend rule 34's example-overlap check across categories (語彙 ↔ 漢字 ↔ 文法 examples and stems sharing the headword plus ≥2 content tokens). |
| E2, E8, E9 (文法 examples and stems) | Rule 39 covers a 語彙 word with a 文法 card of its own (おそらく). 契機 is inside g-kikkake's pattern (を契機に), and もったいない / ぶつける are ordinary words in 文法 sentences. | Extend rule 39: *also grep 文法 cards whose pattern contains the word, and every 文法 example or stem that contains it.* |
| E10, E12, E14, E16 (official items and scripts) | The author's scan covered 問題1–6 items and Hajimete/SK. The 問題7–9 stems (12/2024 7-31, 12/2011 8-48) and 聴解 scripts holding the word were not compared. | Rule 21 / 39 already require it. Add to the brief: *the table rows are EVERY refs line holding the word, 問題7–9 and scripts included* (`QAV5_table.py` does this). |
| E3, E11, E13 (SK/Soumatome practice lines, incl. an uncited page) | Rule 13 compares with the cited page. 一応's SK PDF 143 was not cited at all, and the Soumatome 悔しい line sits in a drill. | Rule 13 for 語彙: *grep the SK and Soumatome extracts for the word and cite any page that treats it*, which also settles doubts like 一応's sense. |
| E17, 一応 sense (rule 27) | A second sense entered an example with no page. | Existing rule. The author flagged 一応 and did not resolve it; rule 23 says an open doubt is resolved before hand-off. |
| 4 look-alike links, 2 glosses (rule 40) | Rule 40 bans shared gloss WORDS, but nothing checks it, and the dump shows only today's pairings. | Gate: *WARN when two unrelated same-pos entries share a content word or phrase in `meaning` (ja: a kanji word or 〜がはっきりしない-type phrase; vi: a two-syllable word)*. `QAV5_glosshw.py` is a working prototype; it needs a stop list for 相手/物事/仕事. |
| P2, 敗れる fix (rule 35) | A restriction written in prose (「たまたま〜した」の形; 「試合や勝負で」) was not re-read against the card's own examples. That includes a live gloss edited to dodge a headword. | Add to rule 35: *a live gloss edited for rule 34 is re-read against that card's examples.* |
| P1, P3, P4 (unsourced generalisations) | Rule 9 is applied to register and frequency claims, and "only" or "never" usage claims slip through. | QA-only; keep. |
| 一か月 furigana | Not in `check_ruby_suspects`. | Gate: *WARN on 一《ひと》か月 / 一《ひと》ヶ月* (it is いっかげつ; ひとつき is written 一月). |
| ruby on non-word official options | Rule 34 exists. | QA-only. |

## For the coordinator

- **Merge.** Apply `V5_live_meaning_fix.json` to live `語彙.ja.json` first. It now holds **6** meanings: 敗れる is
  corrected and 評判 is added (§4). Then run `merge_batch.py 語彙 5`. It applies 31 back-links: the authors' 29, plus
  あいまい and 普及 from QA; the existing 思いがけず back-link now also adds たまたま. Then run `make knowledge`,
  `make drill LEVEL=N2` and `make check`.
- **Live files.** I did not touch them. All live changes are in the fix file and the back-link files.
- **Still open, pre-dating B5.** ふさわしい ⊃ 場面 is cross-pos (イ形容詞 / 名詞), so it is harmless today. B5 back-links
  場面, so the next 語彙 QA should look at it.
- **Not mine.** The untracked `CLAUDE_YOU_MUST_READ_THIS.md` in the repo root is out of scope for this QA, and I did not
  act on it.
