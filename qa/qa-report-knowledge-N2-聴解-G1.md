# QA report — 知識 N2 聴解 guides, batch G1 (25 entries, 28 quiz items)

Reviewer: fresh-eyes QA context, authored none of the batch. Date 2026-09-30.
Targets: scratch `batches/聴解_G1.json`, `聴解_G1.ja.json`, `聴解_G1.vi.json`.
Fixed in place, in one full round.

## What was checked

- **Owners re-read:** `jlpt-knowledge/SKILL.md` (guide schema, bands, quiz rules 1–16),
  inventory `N2.md`, `jlpt-exam-structure/SKILL.md` §聴解 / §問題1 Question Forms /
  §kana-LEANING / §問題5 prints nothing / §Announcer, `choukai-audio/SKILL.md`
  §Register and Part 3 pacing table, `references/official_register.md` §1, §2.1–2.5, §7.6.
- **`make choukai-profile BASELINE=1` re-run.** Every percentage the batch quotes
  matches it: 問題1 36.8% / 31.0% / 16% single-speaker; 問題2 37.6% / 32.6% / 5.5%;
  short reactions 16.9%; 問題4 replies opening はい/いいえ/では 3.1% (§5); ≥3-speaker
  問題5 in 31/31. The pacing numbers (12.2 s / 8.3 s answer pause, 20.22 s option
  reading, 3.10 s between spoken choices) match `choukai-audio` Part 3. The per-form
  縮約形 rates (って 92.4, てる 29.6, ちゃう 5.2, なきゃ 2.3, とく 1.8) match
  `official_register.md` §7.6(a). The profile does not print those rates, so §7.6(a)
  is their only owner.
- **Every cited page read from the scan:** SK 聴解 PDF pp. 11–21, 23, 25, 27, 28, 30–34,
  36, 39, 42, 56, 61 (rendered with pdftoppm, contrast raised); 完全模試 対策 pp. 13–14;
  7/2025 `script.md` 問題1-1, 問題2-1, 問題3-1, 問題4-4/8/10, 問題5-1/2 plus `key.md`.
  The one official line the vi pane quotes verbatim (「今加藤さんが確認してるとこ」)
  was also checked against the script PDF page, because the extract is OCR.
- **Provenance:** 10-char windows of every sample, stem and option checked against
  `refs/**/*.md` and `tests/imported-*`: 0 hits after the fixes. One of my own
  replacement samples hit and was replaced again. The samples were also compared
  by hand with each SK page's own examples.
- **Validation:** the gate's own `check_category` ran on a scratch copy of `knowledge/`
  with this batch merged. Schema, bands, related ids, source refs and answer balance
  (28 items) are all ok. A scratch `build_category` render then passed the stamp
  check. The real `knowledge/` was not touched.

## Findings

| # | Sev | Entry | Finding | Fix | Root cause |
|---|---|---|---|---|---|
| 1 | **High** | l-iikae (shared note + ja ¶2) | The note and the ja pane said the talk was 「本を作る会社に入りたい」 and the option turned it into 「出版社で働く」. The 7/2025 script has the woman say 出版社 herself (「植物専門の本を作ってる出版社があって、そこに入りたい」). The rewording is 入りたい→働く, with the kind of books dropped. The note also cited `booklet.md`, which cannot show the talk. | Source re-pointed to `script.md`, with a correct note. ja ¶2 rewritten. The vi pane was already right. | The JA author paraphrased `official_register.md` §7.6(b)'s gloss instead of reading the script it cites. Brief gap: "cite a sitting" did not require reading the script behind a quoted item. |
| 2 | **High** | l-overview (ja ¶2, vi ¶1, quiz 1 + both explanations) | The card said 「選択肢が印刷されているのは問題1と問題2だけ」 (vi: 「Chỉ Mondai 1 và 2 in…」), and the quiz explanation said 「問題1と問題2だけ」. That is false for the real exam: all 31 sittings print 問題5 2番's four names (`jlpt-exam-structure` §問題5). ja ¶2 also contradicted itself two sentences later. The vi pane never mentioned 問題5's printed names. | The stem is now scoped to 「問題1〜4のうち」 and option 4 is now 問題1と問題4. ja ¶2 says four sentence options are printed in 問題1/2 and that the real exam prints 2番's names (the site does not). vi ¶1 adds the same sentence. Both explanations rewritten. | The repo house rule (問題5 prints nothing) was written into a card about the REAL exam. Brief gap: the guide briefs never say "describe the sitting, and flag house divergences as divergences". |
| 3 | Med | l-q1-kadai quiz | The distractor 「木村さんに連絡する」 is never raised in the talk (the JA author's doubt, upheld; rule 8). | The talk now defers a task (「名簿のコピーは明日でいいから」), and option 4 is 「名簿をコピーする」. Each distractor now dies by one of three different devices (done / reassigned / deferred), matching `official_register` §2.3. Both explanations rewritten. | Rule 8 was applied to grammar items only. A listening-item quiz needs every option to be a candidate the talk kills. |
| 4 | Med | l-sk-05 quiz | 「会社の食堂」 is never raised (doubt upheld). | The talk now names 去年のレストラン, closed (「閉店しちゃったし」), and option 4 is 「去年のレストラン」. Both explanations rewritten. | Same as #3. |
| 5 | Med | l-keigo quiz | 「カード会社の人」 is never raised (doubt upheld), and 「客の家族」 did not compete either. | Added a 客 line (「このカード、家族のなんですけど」), so the family is the card's owner and a real competitor. Option 4 is now 「客と店員の二人」. Both explanations rewritten. | Same as #3. |
| 6 | Med | l-sk-10 quiz 1 and 2 (not flagged by the author) | 「資料を作った人」, 「会場の人」 and 「地図を作った人」 are not in the stems. The ja explanation even said 「資料を作った人の話は出ていない」. | Q1: 「田中さんが作った資料…」, and option 4 is 田中さん. Q2: 「会場の人からもらった地図、みんなに…」, and the options are 話し手 / 会場の人 / みんな / 聞き手. Explanations rewritten in both languages. | Same as #3. When an author's own explanation says "not in the talk", the item is not ready to hand off. |
| 7 | Med | l-q4-sokuji quiz | The kill for option 3 (「7時ならまだ開いてないよね」) rested on an unstated premise that the shop was open (doubt upheld; rule 1). | The prompt now says 「朝7時の開店と同時に行ったのに」, and both explanations say what kills option 3. | Rule 1 (write the assumption into the stem) was not applied to 問題4-style prompts. |
| 8 | Med | l-q4-sokuji vi ¶4 | Told the learner that 「lời cảm ơn, lời tạ lỗi」 (thanks AND apologies) appear in right and wrong replies. 対策 p.12 says 「お礼や感謝の言葉」, so apologies are not on the page. | Changed to 「lời cảm ơn, lời bày tỏ lòng biết ơn」. | Rule 15 (restrictions match the page's wording) was checked for grammar, not for strategy guides. |
| 9 | Med | l-q5-tougou vi ¶3 + shared note | 「Shin Kanzen (tr.12) chỉ ra 質問1 và 質問2 hỏi về hai người khác nhau」 turned one example into a rule. SK states no such rule, and 7/2025's two questions both ask about 2人 (day 1 vs day 2). | vi ¶3 now says the two questions ask different things, with SK's example (女/男) and 7/2025's (日目) as illustrations. The shared note now says 「例題では質問1が女の人、質問2が男の人」. | An example was stated as a rule, which rule 9 bans. |
| 10 | Low | l-q5-tougou ja ¶2 | 「提案が…反対で消えることが多い」 is a frequency nobody counted, and no source was cited for it. | Changed to 「ことがある」, citing SK p.20 (例題5: proposals rejected one by one), which was added to the sources. | Rule 9 (a frequency word is a countable claim). |
| 11 | Low | l-q4-sokuji ja ¶2 | 「はい」「いいえ」で始まる返事は3%ほど. The measure is はい/いいえ/**では** (3.1%). はい/いいえ alone are about 1.1% (`official_register` §2.4). | Now reads 「はい」「いいえ」「では」. | Paraphrase narrowed the measured category. |
| 12 | Low | l-q3-gaiyou (vi ¶1), l-shukuyaku (vi ¶2) | The vi author's note, upheld. The ~3 s gap between spoken choices and 縮約形 in 31/31 sittings came from `choukai-audio` / `jlpt-exam-structure` §Announcer, not from the entry's cited sources. | Cited: l-q3's exam-structure note now names §Announcer (~3 s). l-shukuyaku adds `choukai-audio/SKILL.md` §Register rule 3 (31/31). | The brief says "every fact from the owner", but did not say "…and the owner goes in `sources`". |
| 13 | Low | l-sk-04 example 1 | 「山田さん、きのうは早く帰るつもりだったじゃない。どうしたの？」 is SK 例題4(1)'s scenario (leave work vs stay late, 確認の〜じゃない) turned around. Rule 13 treats that as a copy. | Replaced with 「あれ、佐藤さん、甘いものはやめたはずじゃない。そのケーキ、どうしたの？」. My first replacement hit a 10-char window in 12/2018 and was replaced again. vi note updated. | The author changed the predicate but kept the scenario. |
| 14 | Low | l-sk-07 ja ¶3 | 「っ」「ん」が入って「元の言葉より強く聞こえる」: the 強く nuance is not on SK p.16. | Cut. The sentence now gives SK's own two forms (すっごく・あんまり). | Rule 9. |
| 15 | Low | l-sk-06 vi ¶3 | "Count the morae" was a strategy no cited page gives. | Restated as a fact about the card's own pairs (one extra mora = a different word), with no advice attached. | Rule 9, in the learner pane. |
| 16 | Low | l-sk-04 ja ¶3 | 「〜じゃない」 is used 「…予想と違っていたことを表す」: this widened SK's 「推測できます」 (said of one example). | Now reads 「…と推測できる」. | Rule 15. |
| 17 | Low | l-sk-12 ja ¶3 | 「迫る勢いだった」 was described as 「まだ起こっていない」. The race is over, so the accurate statement is that he did not become 1位. | Rewritten: 「た形でも1位にはなっていない文」. | Wording. |
| 18 | Low | l-shukuyaku ja ¶1 | 「って」 (92/10k) was listed with the verb contractions but never glossed. It is the colloquial と/という, and it is not in SK p.16's table. | Added 「（＝と・という）」. | Wording. |
| 19 | Low | l-keigo vi ¶1, ¶3 | 「hay có cảnh…」 was an uncounted frequency. The vi pane quoted 「〜させてもらえますか」, while SK p.19's table prints もらえる？/もらえない？/もらえませんか. | 「có những cảnh」; the quote now uses 「〜させてもらえませんか」 / 「〜てもらえませんか」. | Rules 9 and 15. |
| 20 | Low | l-iikae vi ¶1 | 「thường tóm」 (often): SK p.52 says 「ことがあります」. | 「có khi tóm」. | Rule 15. |
| 21 | Low | l-sk-13 vi note 3 | 「chuyển xuống Osaka」 added a direction the Japanese does not have. | 「chuyển đến Osaka」. | Translation. |

## The authors' doubts, judged

- **Weak distractors never raised in the talk** (木村さんに連絡する / 会社の食堂 / カード会社の人):
  upheld, fixed (#3–#5). The same defect in l-sk-10 was also fixed (#6).
- **l-q4 option 3's implied open shop:** upheld, fixed (#7).
- **「このサイトの模試では印刷しない」 in l-overview / l-q5:** the parenthesis is correct and
  was kept. l-q5 was never misleading, since it states the real exam first. l-overview
  was misleading, because its 「問題1と問題2だけ」 and its quiz explanation were false for
  the real exam (#2).
- **Rounded numbers:** 約17% (16.9), 約92回 (92.4), 約30 (29.6), 約5 (5.2), 約2 (2.3 / 1.8),
  約37% / 約31% / 約38% / 約33%, 約12秒 / 約8秒 / 約20秒: all match their owners.
  There was one scope error, which is #11.
- **vi author's l-iikae note:** upheld; the ja pane repeated the error (#1).
- **vi author's l-q3 ~3 s and l-shukuyaku 31/31:** upheld. Both kept and cited (#12).

## Not done / notes

- **Blind solve:** I did not re-solve the 22 unchanged items blind. I relied on the Gemini
  3.8 Flash two-run agreement on all 28 original keys. I solved each of the 6 rewritten
  items before keying it (overview Q1, q1 Q1, q4 Q1, keigo Q1, sk-05 Q1, sk-10 Q1/Q2).
  No key position changed, so answer balance is unchanged (gate ok).
- **`make check` not run.** The batch lives in scratch and `knowledge/` was not touched.
  The gate's own `check_category` plus a scratch render stand in for it. The real
  `knowledge/N2/文法` currently FAILs a band (g-nikakawarinaku `compare`), which belongs
  to another batch.
- **Owner drift found while checking. Not this batch's defect; for the doc owners:**
  1. `jlpt-exam-structure` §問題1 table: その他 is 18.1% and 条件一致 1.9%, but the profile
     now prints 15.5% / 4.5%. The rows need refreshing from `--baseline`.
  2. `official_register.md` §1 and the profile give 縮約形 as median 63.9 [29.9–89.3],
     while §7.6(a) and `choukai-audio` §Register give 37.3 [22.4–67.4]. Two regexes are
     publishing one metric under one name.
  3. The profile prints 問題4 はい/いいえ/では as 2.5% (§1) and 3.1% (§5) in the same output.
  4. `official_register.md` gives 「〜ではありません」 as 0.9 (§1) and 0.4 (§2.3).
  5. `choukai-audio` §Register still shows short reactions at 18% and filler openers at
     35%. Those are the targets; the measured values are 16.9% / 32.7%.

## Rules proposed for the briefs / SKILL

- **GUIDE_JA_BRIEF / GUIDE_VI_BRIEF:** "A card describes the real sitting. A repo house
  rule (問題5 prints nothing, no 例) appears only as a labelled aside, and never inside a
  sentence or quiz explanation about what the exam prints." (#2)
- **GUIDE_JA_BRIEF:** "When you cite an official item for how it behaves, read that
  item's `script.md` block, not a skill doc's gloss of it, and cite `script.md` (not
  `booklet.md`) for anything said in the audio." (#1)
- **Both guide briefs:** "Every number you take from an owner doc goes into `sources`
  with its §." (#12)
- **jlpt-knowledge SKILL, quiz rule 17 (guide quizzes):** "A listening-style quiz lists
  only candidates the stem raises, and each one dies by a device the stem states. If your
  own explanation has to say 「〜は話に出ていない」, replace that option." (#3–#6)
