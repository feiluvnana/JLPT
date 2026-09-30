# QA report — 知識 N2 聴解 guides, batch G3 (15 Soumatome entries, 16 quiz items)

Reviewer: fresh-eyes QA context. I authored none of the batch. Date 2026-10-01.
Targets: scratch `batches/聴解_G3.json`, `聴解_G3.ja.json`, `聴解_G3.vi.json`.
All fixes were made in place, in one full round. The real `knowledge/` was not touched.

## What was checked

- **Owners re-read:** `AGENTS.md`, `jlpt-knowledge/SKILL.md` (guide schema, bands,
  quiz rules 1–33), `GUIDE_JA_BRIEF.md`, `GUIDE_VI_BRIEF.md`, `BATCH_QA_BRIEF.md`,
  `jlpt-exam-structure` §聴解 table, §問題1 Question Forms and §問題5 prints nothing,
  and the G1 and G2 reports.
- **Every cited page read from the scan:**
  - Soumatome 聴解 PDF pp. 19, 25–36, 41, 43, 45, 47, 53, 55, 57, 59.
  - 別冊 解答・スクリプト pp. 5, 11, 13–15, 22–28, 34–39. This includes every page the
    vi author did not read, checked against every Japanese sample and stem.
- **Every cited official item read in `script.md` with `key.md`:**
  - 12/2022 問題4-10 and 問題1-2;
  - 12/2016 問題4-9 and 4-10;
  - 7/2013 問題3-2 and 問題1-4;
  - 12/2011 問題2-6;
  - 12/2020 問題3-5;
  - the three 「聞かなかったことにして」 items (12/2015 4-9, 7/2019 4-6, 12/2022 4-10).
- **Provenance:**
  - A 10-char window scan of every sample, stem, option and ja prose line against
    `refs/**/*.md` and `tests/imported-*`.
  - Every quiz stem compared by content bigrams with every item in all 31 `script.md`
    files. I read every pair sharing ≥4 bigrams.
  - A category-wide scene grep over the live `knowledge/N2/聴解*` and batches G1/G2
    (rule 11).
- **Validation:** I built a scratch root (a copy of `.agents/` and `knowledge/`, with
  the live 聴解 files, this batch and the back-links below merged). There I ran
  `build_knowledge.py`, then `check_knowledge.py`: **0 FAIL, 0 WARN**. 聴解 has
  65 entries; bands, schema, related, sources, 68-item answer balance, book order,
  stamp, ruby suspects and prose citations are all ok. No key position changed.

## The coordinator's items

### l-sm-11: the 問題3 question count (rule 26)

I re-counted from the 問い line of every 問題3 item in the 31 `script.md` files. There
are **154 questions**: 30 sittings × 5, plus 12/2012, which has 4 (its `key.md`
agrees). An extraction script found the lines, and I fixed its five mis-picks
(7/2019-5, 7/2022-1 and -3, 12/2015-4, 12/2018-5) by reading them.

| Category | Count |
|---|---|
| 主題 (何について・テーマ・内容) | 111 |
| 言いたいこと・伝えたいこと | 21 |
| 意見・感想 (どう思う・どう言う・どう考える・どう感じる) | 16 |
| **目的** | **2** |
| その他 | 4 |

The two 目的 items are 7/2011 問題3-1 「男の人は何をしに来ましたか」 (options 〜ため) and
7/2013 問題3-2. The four その他 items are 調査の結果, 今シーズン, 家計調査 and アドバイス.

Both earlier figures were wrong:

- **Shared note, 83/103:** too few items were extracted. It also said 目的 appeared once,
  but it appears twice.
- **vi pane, 51/64 ("~4/5"; "mục đích mới gặp một lần"):** too few items again, and
  the same undercount of 目的.

Fixes:

- **`sources`:** the 7/2013 source note now carries the full breakdown, the 154
  denominator and the caveat (`script.md` is partly OCR; I classified by hand).
- **ja ¶2:** 「154問中111問…「言いたいこと」21問…目的は2問だけ」.
- **vi ¶3:** now gives the same figures.

The ja pane's 「大部分」 was acceptable (72%), but it now states the number.

### l-sm-08: the real exam has 3 options, the quiz has 4

Neither pane said the exam has 4. Both panes already said 3 返事 / 3 lựa chọn. Both now
also carry a labelled aside: 「このカードのクイズは4択だが、本番は3択」 and
"(Câu đố trên thẻ này có 4 lựa chọn, nhưng đề thật chỉ có 3.)".

### Rule 25: definition distractors

- **l-sm-22:** new stem. The sister entered grad school after submitting her 卒論 last
  year, a friend from the same year already works at a company, and 就活 starts next
  year. Distractors:
  - 卒論を書いている — dies by 去年出して卒業;
  - もう就活 — dies by 来年から;
  - 会社で働いている — dies because that is the friend.

  Key 1 is unchanged.
- **l-sm-23:** new stem. The clerk offers 今こちらで払う / 着払い / 代金引き換え /
  営業所受け取り, and the customer picks 着払い. Each distractor is one of the offered
  methods, killed by its own stem word. Key 2 is unchanged.

### Provenance

- **l-sm-06 Q1: copy; replaced.** 別冊 p.5 ④ is 「料理が好きなんですね」→「好きなわけじゃないけど、体にいいし…」.
  Table ② on p.18 is 「得意なわけじゃないけど、必要だから」. The quiz's
  「早起きが好きなわけじゃないけど、[reason]」 has a different scene but the same predicate
  and device. The predicate is now 「会社で早く仕事がしたいわけじゃないんだけど」, and
  option 3 is 「会社で早く仕事を始めたいから」.
- **l-sm-16 Q1: copy; replaced.** 別冊 pp.23–24 3番 runs: why she quit a job → serial
  guesses → 「そういうわけじゃないの」 → the real reason. The quiz had the same scene
  family (why stopped attending), the same serial guesses, the same 「そういうわけじゃない」
  and a 4-option list of the guesses plus the real reason. 別冊 p.27 2番 (カラオケ) uses
  the same device again.
  - New scene: why he sold his car. The denials are 「5年しか」 / 「前と同じ」 / 「違う違う」,
    followed by 実は, and the reason is that he moved near work.
  - Both prose panes had quoted 「そういうわけじゃない」 from the script. They now describe
    the device without the quote.
- **Answer-booklet pages not read by the vi author (11, 13–15, 22, 26–28, 34–39):**
  - p.36 1番: 申込用紙に指導教員の認め印をもらって提出 duplicated l-sm-22 ex. 2
    (留学の申込書、指導教員のはんこ). Replaced with 「指導教員の先生が今週は出張で、認め印がもらえないんだ」.
  - p.37: 学務係よりお知らせします…就職ガイダンス, same frame as l-sm-22 ex. 1 (学生課…
    健康診断は…9時から). Now a date change: 「健康診断の日が、来週の水曜日に変わりました」.
  - Every other page is clear. The p.14 family-outing elimination is not l-sm-12's
    transport scene, the p.15 courses are not the new futon item, and pp.25–26 are not
    l-sm-17's samples or quiz.

## Findings (mine)

| # | Sev | Entry | Finding | Fix | Root cause |
|---|---|---|---|---|---|
| 1 | **High** | l-sm-11 shared note, ja ¶2, vi ¶3 | Two different, both wrong, 問題3 counts (83/103; 51/64). Both said 目的 appears once; it appears twice. | Re-counted 154/154 (see above). | Neither author checked that the denominator = sittings × items. Brief gap: "a count over the archive states its denominator and matches the key count". |
| 2 | **High** | l-sm-10 quiz | Copy of Soumatome p.28's 例 (why he keeps going back to the same place; the woman suggests price; 「値段だって普通」; the real reason). My first replacement (dentist) reproduced 12/2011 問題5-1 (会社帰り, 待ち時間, 丁寧, closes at 5), so I dropped it. My second (bike commute and 駐輪場) duplicated a LIVE 聴解 quiz, so I dropped that too. | Now: why he moved his 絵の教室 online. 料金「あまり変わらない」 and 先生「親切だった」 kill two options, the woman's preference kills the third, and the key is 家なら夜遅くでも. | Provenance was checked against the 別冊 script pages, not the lesson page's own 例 script. Rule 11 is category-wide and needs the live file grepped. |
| 3 | **High** | l-sm-13 quiz | 12/2013 問題5-1 is a shop clerk presenting four bag models (軽い / ポケット / タイプ) to a customer choosing by his conditions. The quiz had a clerk presenting four suitcases (軽い / 丈夫 / 安い / ポケット). Same scene (rule 21). | Now 掛け布団 ×4 (薄い軽い / 一番暖かい / 安い / 家で洗える). The man chooses 暖かいのが一番 → 2, and the woman chooses the washable 4. Key 2 is unchanged. | Rule 21 was checked only against the cited sittings. The bigram scan over all 31 scripts found it. |
| 4 | Med | l-sm-11 ex. 2 | 「電話で、男の学生と女の学生が話しています。」 is 7/2013 問題3-2's lead-in, word for word. | 「電話で、母親と息子が話しています。」 | Rule 21: the example quoted the very item it cites. |
| 5 | Med | l-sm-08 ex. 1 | 「うっかりして、会議の資料を家に置いてきちゃった」 is p.25 table 「うっかりして、電車の中に傘を忘れた」 with the nouns swapped (the same forgot-item predicate). | 「うっかりして、降りる駅を一つ乗り過ごしちゃった。」 | Rule 13: the table examples. |
| 6 | Med | l-sm-20 ex. 2 | 「この電車は、次の駅で急行の通過待ちをいたします」 is the frame of p.52 ④ 「この電車は特急通過待ちをいたします」. | 「次の駅で、急行の通過待ちのため、しばらく停車いたします。」 | Rule 13. |
| 7 | Low | vi l-sm-22 ¶1, vi l-sm-23 ¶2 | Quoted page sentences: 「学生課よりお知らせします」 and 「田中が承りました」 (rule 32). | Reworded: 「学生課」 as the office named first; 「〜が承りました」 with the name slot explained. | Rule 32 was not in the VI brief. |
| 8 | Low | ja l-sm-13 ¶2–3 | Two advice lines the page does not give. 「一字や記号を使うと速く書ける」: the page only shows the memo. 「2人がそれぞれ何を選ぶかを分けてメモ」: the page only has 質問1 男 / 質問2 女. | Restated as what the page's example does. | Rule 9. |
| 9 | Low | ja l-sm-17 ¶3 | 「聞き手が出した案は取り下げられている」: 取り下げる means the proposer withdraws it. In 12/2022 問題1-2 the caller rejects it (「それは動かさないでいきましょう」). | 「使わないと言われる」. | Wording. |
| 10 | Low | vi l-sm-09 ¶3, ¶4 | 「lựa chọn ít khi lặp lại đúng từ」 is an uncounted frequency; the page says only 言い換えてある. 「Chiều ngược lại」 mislabels 頼む→注文する, which is the table's own direction. | 「có khi không lặp lại」; the direction label was cut. | Rules 9 and 15. |
| 11 | Low | vi l-sm-10 ¶4 | 「Điều người nói coi trọng nhất thường nằm ở đây」 is an uncounted frequency. | 「Đáp án có thể nằm sau những từ này」. | Rule 20. |
| 12 | Low | l-sm-09 ex. 2 | Option wording 「弁当の注文をキャンセルする」 matched a 7/2021 読解 line (generic collocation). | 「お弁当をキャンセルする」. | Rule 3 (scan). |

The remaining hits from the scan are all formulaic:

- lead-ins and question frames (〜が話しています, 何について話していますか, この後まず何を);
- keigo (お選びいただけます, ご用意しております);
- the ja prose's deliberate quotations of the official items it cites with a
  公式過去問 pointer (12/2022 4-10, 12/2016 4-9/4-10, 12/2020 3-5). These are kept; that
  is the G1/G2 guide convention.

## Checked and correct (no change)

- **l-sm-06:** わけ/こと glosses and the 会話の省略 and 気持ち expressions match p.18. The
  「聞かなかったことにして」 count is 3 in 31 script.md (12/2015 4-9, 7/2019 4-6,
  12/2022 4-10). 12/2022 key 4-10 = 2 is correct.
- **l-sm-08:** 12/2016 4-10 key 1 and 4-9 key 2 are correct. The vi claim that option 3
  「今週は仕事が少ないんだね」 inverts ぎっしり matches the script.
- **l-sm-09 / 15:** 36.8% / 31.0% / 3.2% match `jlpt-exam-structure` §問題1.
- **l-sm-17:** 16% (25/155) matches §問題1. The vi description of 12/2022 1-2 is accurate.
- **l-sm-12 / 13:** 1番 prints nothing and 2番 prints only the names in the real exam;
  the site's mock appears only as a labelled aside (rule 26). The vi l-sm-13 「hai câu
  hỏi có thể hỏi về hai người khác nhau, ví dụ…」 is hedged and illustrated, so it is
  not stated as a rule (compare G1 #9).
- **l-sm-20 / 21 / 22 / 23:** all vocabulary glosses match pp.52, 54, 56 and 58.
  7/2013 1-4 (成績証明書 不要) and 12/2011 2-6 are described correctly.
- **l-sm-20 quiz:** option 2 (遅れて走っている) is the 見合わせる misreading the stem
  raises, and it dies by 見合わせる itself. I kept it as a stated device, but it is the
  same shape as the 22/23 items the coordinator flagged; judge at merge if stricter
  consistency is wanted.
- **Blind solve:** I solved all 16 items. Every key held. I solved the six rewritten
  items (06 Q1, 10, 13, 16, 22, 23) before keying them. Answer positions are unchanged.

## Back-links for the coordinator (live 聴解 entries, `related` only)

- `l-sk-14` → `l-sm-06`
- `l-q4-sokuji` → `l-sm-08`
- `l-sk-11` → `l-sm-08`
- `l-q1-kadai` → `l-sm-09`
- `l-iikae` → `l-sm-09`
- `l-q2-point` → `l-sm-10`
- `l-sk-29` → `l-sm-10`, `l-sm-18`
- `l-q3-gaiyou` → `l-sm-11`
- `l-sk-31` → `l-sm-11`
- `l-q5-tougou` → `l-sm-12`, `l-sm-13`
- `l-sk-39` → `l-sm-12`
- `l-sk-40` → `l-sm-13`
- `l-sk-22` → `l-sm-15`
- `l-keigo` → `l-sm-17`
- `l-sk-35` → `l-sm-18`

All of these were applied in the scratch merge, and the gate's related check passed.

## Not done / notes

- **`make check` not run.** The batch lives in scratch; the scratch gate stands in for it.
- **Owner drift:** `jlpt-exam-structure` §聴解 table row 5 says 問題5 prints 「NOTHING —
  both items」, while §問題5 prints nothing states that official prints 2番's names in
  all 31 sittings. The table describes the house rule in a column meant to describe the
  sitting. Fix it at the owner. (G1 #1's その他 18.1% vs 15.5% drift is also still open.)
- **Untracked `CLAUDE_YOU_MUST_READ_THIS.md` at the repo root** (asks for all of
  語彙/漢字). It is outside this task, so I did not act on it.

## Rules proposed

- **GUIDE_JA_BRIEF / GUIDE_VI_BRIEF:** "An archive count states its denominator, and
  the denominator must equal the item count the keys give (問題3: 154). An extraction
  that finds fewer items is incomplete, not a sample." (#1)
- **GUIDE_JA_BRIEF, provenance:** "A quiz scene is checked against the lesson page's
  own 例 script and the 別冊 れんしゅう scripts, against the whole archive by bigrams
  (not just the cited sittings), and against the live category file." (#2, #3)
- **SKILL rule 25 addendum:** "A term-meaning quiz (着払い, 院生) puts the competing
  terms INTO the stem (the clerk lists the methods; the speaker mentions 卒論 and
  就活), so every distractor is a candidate the stem raises."
- **GUIDE_VI_BRIEF:** copy rule 32 (no quoted textbook sentence in prose, set phrases
  included when they are the page's own example line). (#7)
