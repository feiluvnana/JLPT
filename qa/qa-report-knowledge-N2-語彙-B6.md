# QA report: knowledge/N2 語彙, batch 6 (65 words, 130 examples, 20 → 25 live back-links)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. The Japanese pane and the shared file
were written by a Claude author. The **Vietnamese pane and the vi back-links were drafted by a weaker model (Gemini, via
the agy CLI)** with no file access, working only from the shared fields and the current live vi compares. Files are in
the coordinator's scratch `batches/`. The pre-review copies are in `scratchpad/QAV6_bak/`, and `QAV6_patch.py` rebuilds
every fix from them. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B6.json` | dbdc91ba8ea9 | b962c842b8fb |
| `語彙_B6.ja.json` | 7cfd96df2a15 | fdc3ca07f085 |
| `語彙_B6.vi.json` | bb359ab1422f | 0cff5a56c98d |
| `語彙_B6.backlinks.json` | 960389786c8c | ce763bb04196 |
| `語彙_B6.backlinks.vi.json` | 18085a48ee8f | b94c490fb550 |
| `V6_live_meaning_fix.json` | 257ad493f7a8 | a177cc04b5a9 |

## Verdict

`QA: FAIL → fixed (6 finding classes: about 80 Vietnamese field defects in 50 entries, 15 of 20 drafted vi back-links, 14 examples in 13 entries, 7 unlinked look-alike pairs, 1 furigana span, 1 pos, 2 more live glosses). 0 content findings are open after the fixes.`

**Validation.** `QAV6_gate.py` copies `.agents/` and `knowledge/` into `scratchpad/QAV6_root`. It applies the six
meanings in `V6_live_meaning_fix.json` there, then runs `merge_batch.py`'s own code with REPO set to the scratch root.
That code merges B6, applies both back-link files and checks book order. The script then rebuilds `語彙.html` with
`build_knowledge.build_category` and runs `check_knowledge.check_category`. The result is **0 FAIL, 0 WARN**: 366
entries, 665 generated items (299 reading and 366 meaning), 25 live entries back-linked, cards in book order, and no
`REVIEW` line from the merge. The first post-fix run failed three vi back-link bands (189, 183 and 181 of 180
characters). I trimmed them and re-ran.

**Live files.** I edited no file under `knowledge/`. All live changes are in the fix file and the back-link files.
`make check` on the repo exits 0 ("All checks passed (239 skipped), 224 warning(s)"). None of those warnings is on a
knowledge or drill line.

**No reading, Hajimete number or official count is wrong.**

## 1. Readings, ids, groups, pos, the author's doubts

- **Readings.** I checked all 65 by hand. Every one has a kanji headword and gets a generated reading item. 44 are
  confirmed by an official 問題1 key or 問題2 kana stem that I read in `booklet.md` and the key (e.g. 7/2025 1-1 さいのう,
  12/2015 1-1 きょひ, 7/2010 1-3 けしき, 12/2025 1-1 はしら, 7/2015 1-3 ゆだん, 12/2021 1-5 さんぴ). Of the other 21,
  にごる and そうとう are printed in kana in their own items (12/2015 4-17, 12/2012 5-24), 打ち合わせ and 粗末 carry Hajimete
  furigana (PDF 132, 47), and the rest are standard readings (しだいに, きがる, けはい, ちゅうもく, りゅうこう, てんぷ, …). No
  reading distractor is a valid reading of its headword.
- **Ids (doubt 6).** I opened Hajimete PDF 47, 132 and 213. No.209 is 粗末な (p.47, ① 品質がよくない ② 大切にしない),
  No.702 is 打ち合わせ〈する〉 with ＋打ち合わせる (p.132), and No.1167 is 拒否〈する〉 (p.213). The inventory OCR had them as
  「そらす」, 「切ち合わせ」 and 「拒香」. A fuzzy match of all 65 headwords against the 1,536 OCR'd numbered rows found no
  other numbered word, so the 62 `v-o-*` ids are right. Groups match the section labels already live (会社で／仕事,
  ニュース／トラブル・事件, 暮らし／食事, 健康のために／症状 for 抽象的 as the ↔ word of No.1092, 病気と治療 for 軽傷 as the
  ＋ word of No.1116).
- **Dropped words.** The plan had 70; 活発, 深刻, 清潔 and 貴重 are live (B4), and 相次いで is the live 相次ぐ. Correct.
- **Doubt 1, 系統 has one example.** The schema allows 1–3. The example (warm-系統 clothes) does not share the 12/2018
  2-8 scene (matching tableware). Kept.
- **Doubt 2, 触れる "mention".** Sourced: SK 語彙 PDF 102 prints ④ 「彼女と話すときは、年齢には触れないほうがいい」
  ［話題、問題に〜］, and ① ③ for the other two senses. The ja usage line covers ④, so ex3 satisfies the prose. The vi
  meaning now says "nhắc đến", not the drafted "đề cập lướt qua" (in passing), which ex3 contradicts.
- **Doubt 3, pos.** **相当 fixed** to 副詞・ナ形容詞: ex2 is 「相当な被害」, the usage lists 相当な／相当に, and SK PDF 136's
  用法 drill prints 「相当な割合」. 詳細 名詞・ナ形容詞 is right. 気軽 without に is right: SK PDF 125 heads 「気軽（な）」, and
  the live convention heads ナ形容詞 bare (鮮やか, 温厚).
- **Doubt 4, 腕 vs the future idiom cards.** Hajimete PDF 269 numbers 1495 腕がいい, 1496 腕を磨く, 1497 腕が上がる (VI
  "có tay nghề"). 腕 alone is unnumbered, so `v-o-ude` is right. No gate collision: those cards will have other
  headwords, and the shared kanji keeps them out of each other's meaning items. When 1495–1497 are authored, link them to
  v-o-ude and give them the idiom, not the noun.
- **Doubt 5, 流行 for 流行る.** Correct. The only 問題1–6 hit is 7/2011 5-23, whose key is the noun 流行 (ブーム).
  流行る has no 問題1–6 hit. 流行 is not a Hajimete headword; it appears in No.248 年代's example on p.53. Soumatome PDF 93
  (はやる) and 102 (インフルエンザが流行し) are as cited.
- **Furigana.** I read all 927 distinct ruby pairs in the six files. **One fix**: the ja 相当 usage put one ruby over two
  words, 「｜相当難《むずか》しい」, which renders むずか over 相当難. It is now 「相当｜難《むずか》しい」. Checked in context:
  けが人《にん》, 十《じゅっ》軒, 九時《くじ》, 一《いち》ページ, 気配《きくば》り, 流行《はや》る, 否《ぴ》 and 抱《だ》いて.

## 2. official_count: hit by hit for all 65 (rule 35)

`QAV6_find.py` prints every parsed 問題1–6 item whose stem or options contain the word's kanji or kana form (dump in
`QAV6_find.txt`). I grepped the merged 12/2010 booklet by hand. It adds 規模 1-1, 触れる 1-2 and the 注目 6-30
headword, which are all already cited, plus 腕時計, a different word.

- **All 65 counts are correct**, including every count above 1: 油断 3 (7/2015 1-3, 7/2019 4-18, 7/2023 5-25), 湿る 3
  (7/2012 5-27, 7/2018 1-4, 7/2025 2-6), 略す 3 (7/2012 1-5, 7/2017 6-31, 12/2025 2-6), 破片 3 (12/2012 1-5, 7/2018 2-8,
  7/2021 1-5, a reprint counted once per sitting), 討論 3, 注目 2, 濁る 2, 焦る 2, 相当 2, 省略 2 and 腕 2.
- **Excluded hits, confirmed on the booklet line.** These include 才能 (12/2011 4-22 option, 7/2015 6-30 misuse), 握る
  (five distractors, including 握えて and 握って in 問題2), 機嫌 7/2022 1-3 (stem), 湿っぽい 7/2014 2-6 (another word),
  積もる 12/2021 2-9 (another word), 振り向いた 7/2025 5-25 (stem), 略きます 7/2018 2-10, 簡略 12/2012 4-22, 研修 7/2015
  1-2 and 7/2022 2-8 (stem), 触れ合う 7/2023 4-18 and 7/2024 4-19, and 触って 12/2020 5-25 (触る).
- **Rule 35, part 1.** I intersected every official item cited by a live entry with every item cited by B6. There are
  22 shared items, and each is credited to the right side. 依然 and 相変わらず both count 12/2013 5-25, and 徐々に and 次第に
  both count 12/2024 5-23, under the live 問題5 convention: underlined word plus key. No live entry counts a hit that
  belongs to a B6 word.

## 3. Generated quizzes in both languages (rule 28, rule 40)

`QAV6_dump.py` runs `quiz_gen.generate()` over the merged 366 entries. The dumps are `QAV6_quiz.txt` (pre-fix) and
`QAV6_quiz2.txt` (post-fix). `QAV6_mq.txt` holds the 186 meaning items that have a B6 key or a B6 distractor, and I read
every one. `QAV6_glosshw.py` checks every gloss for another headword and for gloss words it shares with an unrelated
same-pos entry, in both languages.

- **No current distractor glosses its key.** The links below are preventive.

| pair | verdict |
|---|---|
| 積む / 蓄える | **Link.** Both are 動詞. 経験を積む and 知識を蓄える are near-synonyms, and the vi glosses shared "tích lũy". |
| 打ち合わせ / 討論 | **Link.** Both are 名詞, and the vi glosses ("bàn bạc", "thảo luận") read as synonyms. |
| 衣装 / 格好 (live) | **Link.** 格好's 「特に、服装や身なり」 reads as a gloss of 衣装. |
| 装置 / 施設 (live) | **Link.** 施設's 「建物や設備」: 設備 is close to 装置. |
| 発達 / 展開 (live) | **Link.** The official 12/2012 4-21 contrasts them, and 展開's vi "sự phát triển tiếp theo" reads as 発達. |
| 景色 / 名所 (live) | **Link.** The V6 live fix gives 名所 「眺めのよさ」, which shares 眺め with 景色's gloss. |
| 握る / 抱える (live) | **Link.** Both glosses end 「…持つ」, and 12/2023 2-10 prints 握えて as a distractor for 抱えて. |
| 焦点 / 注目 | **Gloss fixed, no link.** Both ja glosses had 関心. 焦点 → 「話し合いや問題の中で、いちばん中心になる大事な点。」 |
| 景色 / 現象 | **Gloss fixed.** The shared word was 自然. 景色 → 「山や川、町など、目の前に広がる眺め。」 |
| 次第に / 着々, 拒否 / 要求, 系統 / 装置・導入, 解消 / 削除, 診断 / 特定, 流行 / 話題 | **vi glosses fixed** (shared "từng bước", "yêu cầu", "hệ thống", "xóa bỏ", "xác định", "nhiều người"). |

- **The four live ja fixes (名所, 抱える, 離れる, ベテラン).** Each removes a B6 headword's kanji from a live gloss (景色,
  腕, 距離, 積). I keep all four and re-read each against its card's own examples (rule 35). **ベテラン is re-fixed**: 「そ
  の仕事や分野で…」 still contained the headword 分野 (same pos, 名詞), so it is now 「ある仕事や物事を長く続けてきて、経験の多い
  人。」. **Added**: 意欲 v-0586 「…積極的な気持ち」 contained 積 (積む) → 「自分から進んで何かをしようとする気持ち。」. The
  fix file now holds **6** meanings.
- **Do the vi meanings of the four need the same fix? No.** The ja edits remove a kanji, and a Vietnamese gloss holds
  none. I ran the vi gloss-word check on all four. 名所 now shares no word with 景色 and is linked to it anyway. 抱える
  shares only "tay" with 握る and 腕, a single syllable, and is linked to 握る. 離れる "cách xa" and 距離 "khoảng cách" share
  no bigram. ベテラン shares "kinh nghiệm" with 積む, but the two have different pos and are never paired today.

## 4. The Vietnamese pane (drafted by agy)

I checked every vi line against the shared file, the cited pages (Hajimete VI glosses on PDF 47, 132, 213 and 269; SK
語彙 PDF 96, 101, 102, 113 and 114) and the official items. **50 of 65 entries and 15 of the 20 drafted back-links
needed a rewrite.**

| class | count | examples (draft → fix) |
|---|---|---|
| Sense or shade on no page (rule 27) | ~21 fields | 才能 "thiên bẩm, bẩm sinh"; 拒否 "thẳng thừng" (Hajimete: phủ nhận, bác bỏ, từ chối); 批評 "chuyên môn (văn học, nghệ thuật)" while ex2 is a customer's critique; 柱 "trụ cột gia đình" + 「大黒柱」; 相当 "tương đương với" + 「給料に相当する」; 濁る "khàn đục (giọng)" + 「声が濁る」; 解散 "giải thể tổ chức" + 「国会を解散する」; 振り向く "nghĩa bóng: đoái hoài"; 握る 「おにぎりを握る」; 蓄える 「ひげを蓄える」; 気配 「秋の気配」「逃げる気配」; 距離 "tình cảm" + 「距離を置く」; 衣装 "đồ dạ hội lộng lẫy"; 診断 "thẩm định hiện trạng"; 軽傷 "vết thương ngoài da" |
| Contradicts the card | 2 | 解消 "(…hợp đồng)" + 「契約を解消する」: the card's own official item keys 解約 over 解消 for an insurance contract. 景色 "thiên nhiên" only, while the ja card and ex2 include towns. |
| Unsourced contrast, register or frequency claim (rule 9) | ~20 | 案の定 "thường là chuyện xấu" + a やはり contrast (SK PDF 114 ㉝ lists 案の定・やはり・予想通り with no such note); 次第に vs 徐々に and 相変わらず vs 依然として invented differences, where the official 言い換え items treat them as equal; 略す/省略; 流行 vs 普及 "lâu bền"; 湿る vs 濡れる "ướt sũng"; 背骨 「脊椎」 "y khoa"; 装置 vs 「部品」; 討論 vs 「相談」; 詳細 "văn bản trang trọng"; 講義 "chỉ dùng… khác 授業"; 貿易 vs 「売買」; 添付 "chủ yếu"; 打ち合わせ vs 会/会議 "quy mô"; 景色 vs 風景/場面 |
| Factual or language error | ~10 | 焦点 "tiêu cự kính quang học" (focal length, not focal point); 流行 "đọc là はやる khi là động từ" (流行 is never はやる); 系統 「暖色系の系統」 (not Japanese) and 「系統立てて」; 絞る 搾る "ép dầu thảo mộc" (SK PDF 96: 果実、ジュース、牛乳); 腕 「腕前を披露する」 and 上達 「腕前が上達する」 (another word); 積む 「雪が積もる」 listed as a usage of 積む; 足が絡まる; 機嫌 "sắc khí" |
| example_notes | 3 | 極端 "lớn đến mức cùng cực", 相当 "vô cùng khó khăn", 解消 "giải quyết triệt để" (all overstate) |
| Gloss words shared with an unrelated entry (rule 40) | 9 | listed in §3 |
| Japanese outside 「」 (rule 6) | 0 | A script over every vi field, note and back-link found none. |

- **Kept after checking.** Hán Việt: chú mục, thiêm phó, nghiên tu, đặc định, khí phối, tiêu, tường tế. 批評's
  "phê bình" note is a real false friend under rule 34. The homophone notes 期限, 賞状 and 軽症 are kept.
- **Not a translation.** The vi pane is not a translation of the ja pane. Its fault runs the other way: it was written
  from general knowledge, not from the pages.

### vi back-links

Each old and new compare was compared quote by quote. **7 drafted vi back-links dropped contrasts the live card had**:
徐々に (「準備が着々と進む」), 依然 (「絶えず変わる」 and the past/future framing), 活気 (「活発な議論」), 活発 (「活気のある町」
and the noun-vs-ナ形容詞 point), 備える (「火の元に用心する」「あらかじめ予約する」), 評価 (the 「〜と評判だ」 frame note) and
あいまい (「かすかに見える」). 安易's added a word with no card and no link (「気兼ね」). わりと's "gây ấn tượng mạnh", 辞退's
"áp đặt", 受講's "đăng ký" and 講師's "thuật lại" were unsourced or wrong. All 15 are rewritten with every old contrast kept.
A re-check finds no quoted form lost in either pane for any of the 25 back-links. `merge_batch.py` printed no `REVIEW`,
because it compares only the primary pane (root causes).

## 5. Examples: provenance, frame, scene

The 10-char scan (`QAV6_prov.py`, over `refs/**/*.md`, `tests/imported-*`, every scratch batch and `knowledge/**`)
found only function-word overlaps. The frame table (`QAV6_table.py`, `QAV6_table.txt`) sets each example beside every
refs line holding the word (Hajimete, SK/Soumatome, all booklets and scripts) and every knowledge card, stem and open
batch (漢字 B4/B5/B18 included). I grepped each replacement's scene nouns over the same corpus before keeping it.

| # | entry | finding | fix |
|---|---|---|---|
| E1 | 極端 ex2 「この地方は、夏と冬の気温の差が極端に大きい」 | Open 漢字_B5 「最近は、夏と冬の気温の差が激しい」: same scene and predicate. | → 「兄は考え方が極端で、少しでも失敗すると、すべてをやめてしまう」 (the 考え方 sense of the gloss) |
| E2 | 解散 ex1 「…子どもたちはそれぞれ家に帰った」 | 文法 「五時のチャイムが鳴ると、子どもたちはそれぞれの家へ帰っていった」. I rejected 「午後三時に…解散」, which is the 7/2013 4-17 frame. | → 「遠足は学校の門の前で解散となり、迎えに来た親と帰る子もいた」 |
| E3 | 解散 ex2 「雨が強くなってきたので、写生会は昼で解散」 | The 12/2022 中断 key 「雨が強くなってきたので、やむまで試合を中断した」: same cause and the same cut-short frame. | → 「歓迎会は九時に終わり、店の前でそのまま解散した」 |
| E4 | 景色 ex1 (inn chosen for the view from the room) | 文法 「このホテルは景色のよさで有名なだけあって、どの部屋からも海がよく見える」. | → 「向かいに高いビルが建ち、ベランダから山の景色が見えなくなった」 |
| E5 | 次第に ex1 (children in the park thin out at dusk) | The same 文法 dusk scene as E2. | → 「日が昇るにつれて、山にかかっていた霧は次第に晴れていった」 |
| E6 | 流行 ex2 「冬になり、学校ではかぜが流行し始めている」 | Soumatome PDF 102 frame (illness spreads). My first rewrite (five absent from class) was 漢字's 「クラスの五人がかぜで休んだ」, so I discarded it. | → 「今年の冬は、流行しているかぜに家族全員がかかってしまった」 |
| E7 | 添付 ex1 (application form, attach a photo) | The application-instruction frame of 7/2016 「画像データを添付してください」, 12/2013 and the 7/2023 script. | → 「旅行で撮った写真を何枚か、メールに添付して友人に送った」 |
| E8 | 焦点 ex2 「もう一度焦点を一つに絞って話し合おう」 | SK PDF 96 絞る④ 「テーマを一つに絞ってレポートを書く」［焦点…を〜］ with the bracket noun swapped in. | → 「この特集は、地方で働く若者の暮らしに焦点を当てている」. The ja usage adds 「焦点を当てる」. |
| E9 | 略す ex2 (ceremony greetings shortened) | SK Dokkai line 「初めと終わりのあいさつは略されることがある」. | → 「この地図は細かい道を略してあるので、駅までの行き方がわかりにくい」 |
| E10 | 発達 ex1 (a book on a child's body and mind development) | The 12/2019 読解 lead 「以下は、幼児の心の発達について述べた文章である」. | → 「水泳を長く続けてきた彼女は、肩の筋肉がよく発達している」 |
| E11 | 確保 ex1 (city keeps three days of water for disasters) | The SK 備える① scene (地震に備えて水を), already removed from B1, and the 12/2019 option 「食べ物と飲み物を十分にたくわえる」. | → 「新しい研究所は、実験に必要な予算を国から確保した」 |
| E12 | 詳しい ex2 「兄は鉄道に詳しく…」 | Hajimete 「弟は世界の国旗に、とても詳しい」: a sibling who is 詳しい about a collection-type hobby. | → 「近所の酒屋の主人は日本酒に詳しく、料理に合う一本を選んでくれる」 |
| E13 | 距離 ex2 「毎朝走る距離を、少しずつ伸ばしている」 | The claim of the 7/2014 読解 on running (build distance step by step, rule 39). | → 「地図で見ると近そうだったが、実際に歩いてみると、思ったより距離があった」 |
| E14 | 農薬 ex2 (strong pesticide harms fish) | The claim of the 12/2018 script option 「環境に害のない農薬の使用法」. | → 「農薬を使ったあとは、手をよく洗うように言われている」 |

- **Checked without change.** 握る ex2 (who really holds the decision) against SK ③ 「我が家は母が財布を握っている」: the
  sense forces the frame, and the scene differs. 絞る ex1 (wringing a dishcloth to wipe a table) against SK ② (hang a
  towel). 触れる ex1 against SK ① 「…人の髪が顔に触れる」: a different subject and cause. 総額 and 背骨 against their
  official stems. 賛否 against 12/2021. 現象 ex2 (heat island) and 症状 ex2 (medicine only eases symptoms): no 読解 or
  script line makes either claim.
- **vi notes.** All 14 replaced examples have a new vi `example_notes` translation, written from the Japanese.

## 6. Japanese prose

The ja pane was sound: no unsourced claim, no citation in prose, and every quoted official distractor list matched the
booklet. The fixes were the two glosses in §3, the 相当 furigana in §1, and the nine compares rewritten for the new links
(each within the band; the largest is the ja 備える back-link at 97 of 100). Kept after checking: 打ち合わせ's 「これから
行うことを決めておくときに使う」, which follows from all three official misuses and Hajimete's gloss; and 振り向く's
「横や上下ではなく」, 濁る's 曇る/汚れる and 発達's 伸びる/育つ, which each name the right word for an official misuse.

## 7. The agy draft vs the Claude-written vi panes of B1–B5

| | entries | vi-originated defects found by QA | per entry |
|---|---|---|---|
| B1–B5 (Claude vi author) | 301 | about 11: B1 格好 misquote; B2 反省 misquote; B3 展開 false-friend framing, せめて and あいまい usage; B4 プラン/深刻 usage, おそらく gloss; B5 偶然 "chỉ phó từ", 刑事 overclaim, 分担 gloss | ≈ 0.04 |
| B6 (agy draft) | 65 | about 80 field defects in 50 entries, plus 15 of 20 back-links | ≈ 1.2 |

That is roughly **30 times the defect rate**. The difference is in kind as well as number. The Claude panes' defects were
misquotes and one-word overreaches. The agy draft adds dictionary senses, register and frequency claims and invented
contrasts throughout, because it could not see a single cited page. The one rule it kept perfectly is the mechanical one
(Japanese inside 「」). Repairing it took longer than writing the pane from the pages would have.

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| §4, all classes | The vi author had no file access. Rules 9 and 27 can only be kept by a context that can open the cited pages and Hajimete's printed VI gloss (rule 35). | BATCH_VI_BRIEF: *the learner-language author must be a context with read access to the batch's cited pages and the Hajimete VI gloss; a draft from a context without refs is not a vi pane and goes through QA as a rewrite.* Do not use agy for learner panes. |
| vi back-links dropping contrasts | `merge_batch.py` prints `REVIEW` only for the primary pane (`_q(old) - _q(new)` on `langs.primary()`). | `merge_batch.py`: *run the same dropped-quote check for every learner pane* (a three-line loop over `per_lang`). |
| E1–E5, E10–E14 (module, official 読解/script, SK frames) | Same classes as B3–B5 (rules 35, 39, 13). The author's scan did not include the open 漢字_B5 batch or the SK bracket lists, and checked nouns, not the frame. | Existing rules. Add to LEX brief: *an SK bracket list ［焦点、的…を〜］ is a frame source: putting a bracket noun into the printed sentence is a copy.* |
| 相当難《むずか》 | No check sees a ruby span that swallows the headword. | Gate idea: WARN when a ruby base in an entry's prose contains that entry's headword plus extra kanji. |
| 7 look-alike pairs, 2 ja glosses | Rule 40 needs a gloss-word check across pos and the live file; the author's dump showed only today's pairings. | Existing B5 gate proposal (`QAV6_glosshw.py` is the working prototype). |
| ベテラン fix kept 分野, 意欲 ⊃ 積 | The live fix file targeted only the four glosses holding a B6 headword word, not every B6 verb stem (積む → 積). | Add to LEX brief: *when a batch adds a verb or adjective, grep live glosses for its stem as well as the full word.* |
| 相当 pos | The author tagged the tested use (adverb) and ignored the ex2 form. | QA-only; keep. |

## For the coordinator

- **Merge.** First apply `V6_live_meaning_fix.json` to live `語彙.ja.json`. It now holds **6** meanings: 名所, 抱える, 離れる,
  ベテラン (re-fixed), and 意欲 (added). Then run `merge_batch.py 語彙 6`. It applies **25** back-links: the authors' 20 plus
  格好, 施設, 展開, 名所 and 抱える from QA, each with complete ja and vi compares. Then run `make knowledge`,
  `make drill LEVEL=N2` and `make check`.
- **Live files.** I did not touch them.
- **Next 語彙 QA.** When Hajimete 1495–1497 (腕がいい/腕を磨く/腕が上がる) are authored, link them to v-o-ude.
- **Not mine.** The untracked `CLAUDE_YOU_MUST_READ_THIS.md` in the repo root asks for the full 語彙/漢字 lists. It is
  out of scope for this QA, and I did not act on it.
