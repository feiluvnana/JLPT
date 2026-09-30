# QA report: knowledge/N2 読解, guide batch 1 (25 guides, 25 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. Files are in the coordinator's
scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `読解_G1.json` | 90b4bd3d7335 | 4943f2e52c7c |
| `読解_G1.ja.json` | 2c37d79bb1b9 | 23c54d474368 |
| `読解_G1.vi.json` | bba6cb24fb20 | 6d29d1d53cb0 |

## Verdict

`QA: FAIL → fixed (13 findings across 11 entries). 0 content findings are open.`

I merged G1 into a scratch copy of the repo (`scratchpad/QAR1_repo`: `.agents` + `knowledge` copied, `refs`/`tests`/`logs`/`tools`
symlinked), rebuilt it with `build_knowledge.py --level N2` and ran `check_knowledge.py`: **0 FAIL, 0 WARN** (25 entries, positions
balanced at 7/6/6/6). The real `knowledge/` and the real builder were not touched. `make check` on the real repo is green (0 FAIL,
224 WARN). None of those warnings comes from the knowledge module. All of them are older pool, rotation or test warnings.

## 1. Blind solve

- `QAR1_blind.py` wrote stem and options only, with no ids, shuffled with seed 9311. I saved my answers to `QAR1_myanswers.json`
  before I opened the map. **24/24 agreed with the keys.** I did not answer one item, r-overview #0, because it depends on the
  card's own time table (see F2).
- After the fixes I re-ran the second-model solve (`scratchpad/agy_blind.py`, gemini-3.8-flash-medium, 2 shuffled runs): **25 clean,
  0 flagged.** The r-sk-01 disagreement it had reported earlier is gone.
- **Every distractor spliced.** All 読解 kills are either a contradiction of quoted passage words or 本文に書かれていない. The
  second is the same kill the cited Shin Kanzen pages use in their own explanations (p.23, p.53, p.59: 「〜とは書かれていない」).

## 2. Inputs judged

| input | verdict |
|---|---|
| Gemini: r-sk-01 #0 「この本の第1部の方法で…最初にすることはどれか」 (key 4, model 2) | **Upheld (F1).** The item depends on the textbook, and the quiz tab shows it without the card. It is also a two-answer item for a general reader: this batch's own r-q12 and r-q14 cards say "read the question first", so option 1 is defensible. I rewrote it as an ア/イ/ウ ordering item that the card's three steps answer. ア cannot come first because it compares 「わかったこと」. Key kept at 4. |
| Same dependency in other quizzes | **r-overview #0 「時間配分の目安で…」 had it (F2).** Its answer depended on the card's time table, which is repo guidance and not an official figure. I rewrote it on the question count, an official fact: 問題11 has 8 questions, the most of any 読解 問題. No other stem depends on the book or the card. |
| ja: r-sk-09 opt 4 「母が妹のすることをまねすること」 killed only by 家族みんなの習慣 | **Kept.** The kill is a real contradiction: one person's imitation cannot be the whole family's habit. It is the strongest distractor, which is good. But the JA explanation never killed it, so I added that kill (F5). |
| ja: r-sk-12 opt 3 and r-sk-11 opts 1–2 die only because the passage does not say them | **Kept.** 「本文に書かれていない」 is the official 読解 kill and the kill SK uses on the cited pages. Each item also has a contradiction-killed distractor (r-sk-12 opt 1 vs 「本の数は少ない」, opt 4 vs 長居). The second-model solve found them single-answer. |
| ja: r-chuu's last sentence is the author's own inference | **Upheld, cut (F8).** 「省かれた部分があっても…読めばよい」 is on no cited page. |
| ja: stems use 「［文章］…［問い］…」 on one line | **Fixed with data only (F10).** Line breaks now go before each ［問い］/［B］/ア/イ/ウ. `apply_furigana` already turns `\n` into `<br>`, and the page sets `#qz-stem` with innerHTML, so the breaks render **with no builder change**. I checked this with a headless screenshot of the scratch page's quiz view (`scratchpad/QAR1_quiz.png`, r-q12). |
| ja: the inventory cited 対策 p.9 but the 読解 tips are PDF 11–12 | **Not a defect in the batch.** Every entry cites `page: 11/12` (PDF) with the note 「本のp.9/p.10」, which matches the scan. The inventory's "p.9" is the book page. |
| vi: pre-2022 SK/完全模試 figures (中文 ~3問, ~500/~700字) labelled "older" | **Mostly fine.** r-q11 VI says 「完全模試」's 500字 is the old-era figure. The JA card states only current-era facts. **But r-q14 was misleading in both languages (F9, F8).** VI set "đề thật 489–638 chữ" against 完全模試's 700, and JA said 600字. dokkai.md itself warns that 問題14 "misleads in JP chars": counted with all characters it is 676–793, median 707, so 700字 is right. Both now say about 700 including the table and figures. |
| vi: r-chuu's 「ここでは」 point rests on the 7/2025 booklet | **Kept.** The 7/2025 glosses print 「ここでは、…」 (概念, 成す, メディア, 進化, 機動性に優れた, そそる, いざとなれば), and 対策 p.9 lists 「（ここでの）〇〇〇とは何か」 as a 問題11 frame. The reading "the meaning in this text" is the literal sense of ここでは, not an inference. |
| vi: r-sk-04 option 2 weak | **Upheld (F3).** 「自分の意見を大切にすること」 died only by a vague meaning mismatch. I replaced it with 「相手より先に自分の意見を言うこと」, which contradicts the quoted 「話が終わるまでとっておく」. |

## 3. Findings

| # | sev | entry | finding | fix | root cause |
|---|---|---|---|---|---|
| F1 | high | r-sk-01 | The quiz depended on the textbook ("この本の第1部の方法で") and had two answers for a reader without the card. Gemini picked 2. The batch's own r-q12/r-q14 support opt 1. | Rewritten as an ordering item; key 4; both explanations rewritten. | GUIDE_JA_BRIEF says "quiz items test the strategy on a tiny original sample" but never says the item must stand alone in the quiz tab. For guide kinds, no SKILL quiz rule covers "answerable without the card or the book". |
| F2 | med | r-overview | 「時間配分の目安で」 depends on the repo's own guidance table. The answer is not derivable from official facts alone. | The stem now rests on the question count (official); explanations rewritten. | Same as F1. |
| F3 | low | r-sk-04 | Option 2 was a non-competitor (a vague "meaning differs" kill). | Replaced with a contradiction of a quoted phrase; both explanations name it. | Rule 8's "competes on the tested meaning" was not applied to guide items. |
| F4 | med | r-sk-10 | The quiz tracked SK 例題11 (p.46): a topic-marked subject lists event-staff actions (set up the venue, 案内 guests, 片づける) and then asks だれか about the last one. Same scenario and predicate, so a copy (rules 3/13). The 10-char scan cannot see it. | New scene: a household morning, 兄 as the hidden subject; key 1; both explanations rewritten. | Rule 13 names the cited page's example as a provenance source, but GUIDE_JA_BRIEF lists only the 10-char scan. For guides, every quiz passage is a paraphrase target of the cited 例題. |
| F5 | low | r-sk-09 | The JA explanation did not kill the strongest distractor (opt 4). | Added the 「家族みんなの習慣」 kill. | The SKILL's quiz-integrity paragraph ("what rules the strongest distractor out") was not checked for ja. |
| F6 | low | r-shijigo | Example 2 「会員の六割…。この数字は、去年より大きく増えた。」 mirrors Bunpou p.178 B-1 「自給率は約12%である。この数字はさらに低くなる」 (percentage, then この数字は, then a change predicate). | Changed to 「これを受けて、来月から夜の講座を二つ増やすことにした」; VI note updated. | Rule 13 (every page that treats the point). |
| F7 | med | r-q13, r-q12, r-chuu (ja) | Furigana errors: 「7｜回《まわ》」 ×2 (reads かい) and 「2〜5か｜所《ところ》」 (reads しょ). | Fixed. | Hand furigana was not re-read. Counter + 回/所 is a known pykakasi-style failure (exam-model-answer lists the class). |
| F8 | med | r-chuu, r-q11, r-q13, r-q14 (ja) | Unsourced or overstated claims: r-chuu's 中略 inference; 「筆者の考えを問う問いも…必ず出る」 (7/7 measured, stated as a law); 「文化」 is not in 対策 p.10's list (社会・人生・文明・歴史・芸術); 「素材は600字ほど」 (the JP-char median, which dokkai.md says misleads for 問題14). | Cut; changed to 「最近の試験では毎回」; 歴史; 「表や数字も含めて700字ほど」. | Rule 9 (no unsourced claim). The 問題14 counting caveat sits in dokkai.md prose, not in the numbers authors copy. |
| F9 | med | r-q10-tanbun, r-q11, r-q14, r-sentakushi (vi) | Measured facts misstated: "gần một nửa" for 考え frames (exam-structure: about 29%; the author had added the 17% 述べている frames); 「26/28 cặp: câu hỏi sự việc đứng trước câu hỏi ý kiến」 (13 of the 28 pairs are two-事実 pairs with no 考え item; the fact is "the 事実 stem comes first"); 問題14 length (as F8); overlap margin stated per item, not as a per-paper median. | Each sentence corrected against the owner file. | The VI brief says "every exam fact comes from jlpt-exam-structure/dokkai.md", but a figure can be copied from the owner and still paraphrased wrongly. No check compares the paraphrase with the owner's wording. |
| F10 | low | 21 stems | Passage and question ran on one line, so the stem read as one block. | Line breaks in the data; they render as `<br>` (verified). | Neither the brief nor the SKILL says how a guide stem carries a passage. |
| F11 | info | — | `jlpt-knowledge/SKILL.md` §Batch workflow step 5 names `.agents/jlpt-knowledge/scripts/second_model_solve.py`, which does not exist. The working tool is `scratchpad/agy_blind.py`. | Not fixed (it is outside the batch). | The doc landed before the script. Move the script into the skill or change the path. |

The facts I verified and kept (no change needed):

- Counts, timings and question numbers against `jlpt-exam-structure`: 20 items, 52–71, 15/25/9/15/9 min (73 min in all), 4×2 from
  12/2022, 28 pairs with the 事実 stem first in 26, 82% name 筆者, 69 is 考え in 7/7, the 問題12 65/66 frames, 問題14 value/action/option.
- Measurements against `dokkai.md`: 157/241/334, 507/655/763, 551, 904, （中略） 2–5, 指示語 1.57, span median 8, 0–3 spans per
  paper, （注） ~5/~7 and 0 in 12/14, apparatus intent in 8 of 10, both 問題14 items person-scenario in 7/7.
- 7/2025 citations against `booklet.md`: Q53 (thanks, then report, then 「ご対応いただけるでしょうか」), Q59, Q65 (opt 1 is A-only,
  opt 4 is B's), Q67 (reason), Q68 (「②これとは何か」), Q69, and the 「概念：ここでは、意味内容」 gloss.
- Every strategy sentence against the scan I read: SK 読解 PDF pp.6, 9–13, 21–22, 29–30, 33–34, 39–40, 45–46, 53–54, 59–60, 65–67,
  81–82, 84, 127, 152, 166; 対策 PDF pp.11–12; SK 文法 PDF pp.188–189, 196–197.
- The 10-char provenance scan (`QAR1_prov.py`, before and after the fixes): the only hits are stock frames (筆者の考えに合うのはどれか,
  ありがとうございました, いただけないでしょうか, 参加したいと思っている). Every quiz passage was also compared with the cited
  page's 例題 (F4, F6).
- Vietnamese pane: every Japanese string is inside 「」 (scripted check). It is not a translation: VI organises each card by source
  attribution and adds exam figures in its own order. No mirrored framing was found. example_notes are faithful.

## 4. Rules to add

- **SKILL §Quiz integrity, new rule 17 (guide kinds):** a guide quiz item is answered from its own stem plus official exam facts. It
  never depends on "this book", "this card" or a repo guidance table, because the quiz tab shows it without the card. If a card
  recommends a method, the item must make every other option wrong on facts in the stem, not on "the book says so". (F1, F2)
- **GUIDE_JA_BRIEF / GUIDE_VI_BRIEF:** (a) write every quiz passage on a scene the cited 例題 does not use, and check the page's 例題
  and 例 lines as well as the 10-char scan (F4, F6); (b) when you quote a measured figure, copy the owner's own sentence, including
  its denominator and its method caveat (問題14's all-character count, "the 事実 stem comes first" and not "事実 before 考え"),
  and do not summarise it (F8, F9); (c) break a stem with `\n` before ［問い］ and before each passage part (F10).
- **SKILL §Batch workflow step 5:** fix the missing `second_model_solve.py` path (F11).
