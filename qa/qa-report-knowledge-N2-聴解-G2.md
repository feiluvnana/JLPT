# QA report — 知識 N2 聴解 guides, batch G2 (25 entries, 24 quiz items)

Reviewer: fresh-eyes QA context. I authored none of the batch. Date 2026-09-30.
Targets: scratch `batches/聴解_G2.json`, `聴解_G2.ja.json`, `聴解_G2.vi.json`.
All fixes were made in place, in one full round. The real `knowledge/` was not touched.

## What was checked

- **Owners re-read:** `AGENTS.md`, `jlpt-knowledge/SKILL.md` (guide schema, bands,
  quiz rules 1–30), `GUIDE_JA_BRIEF.md`, `GUIDE_VI_BRIEF.md`, `BATCH_QA_BRIEF.md`,
  `jlpt-exam-structure` §問題1 Question Forms and §問題5 prints nothing,
  `choukai-audio` Part 3 pacing table, `official_register.md` §2.5, §7.3, §7.6(c),
  and the G1 report (`qa-report-knowledge-N2-聴解-G1.md`).
- **`make choukai-profile BASELINE=1` re-run.** It confirms 問題1 まず 36.8% (57/155).
  The profile does not print three of the quoted figures, so I checked each against
  its owner:
  - 「まず」 median 5.5 /10k (0–19.1): `official_register` §7.3 table.
  - question-form replies, 13% of 973: §7.6(c).
  - 20.22 s / 12.2 s / 8.3 s / 3.10 s: `choukai-audio` Part 3.

  All match.
- **Every cited page read from the scan.** SK 聴解 PDF pp. 36–44, 46–47, 49–50, 52–54,
  56–59, 61–63, 65–66, 71–72, 76–77, 79–80, 85–86, 88–89, 91–92, 94–96, 99–100, and
  Soumatome 聴解 pp. 13, 15, 17. Pages were sliced with pypdf and rendered with the
  contrast raised.
- **Every cited official item read:**
  - 7/2025 `script.md` 問題3 1–5 and 問題4-9, with `key.md`;
  - 12/2025 `script.md` 問題3 1–5 and 問題5 1–2, with `key.md`.
- **Provenance:**
  - A 10-char window scan of every sample, stem and option against `refs/**/*.md`
    and `tests/imported-*`. After the fixes it returns 0 real hits. The remaining
    hits are ありがとうございます and one line-join artefact.
  - Every quiz stem compared by content bigrams with all 31 `script.md` files, then
    the close ones read.
  - Every sample compared by hand with each page's own examples and scripts.
- **Validation** ran on a scratch root (a copy of `.agents/` and `knowledge/` with the
  live 聴解 files plus this batch merged). The scratch `build_knowledge.py` ran, then
  the scratch `check_knowledge.py`: **0 FAIL, 0 WARN** (聴解: bands, schema, related,
  sources, 52-item answer balance, book order, stamp, ruby suspects, prose citations).
  No key position changed.

## The vi author's findings, judged

| Finding | Verdict | Fix |
|---|---|---|
| l-sk-18 option 3 (「10時より前にしたい」) dies only because the talk lacks it (rule 25) | Upheld | The stem now offers 「午後でもいいんですが」. Option 3 is now 「午後がいいとはっきり答えている」, which dies by a device the stem states (her whole line is 「そうですねえ……」 and names no time). Both explanations rewritten. |
| l-sm-04 ex. 3 copies Soumatome p.14's scene and causative (「私が試験に合格した。両親が安心した」 → 「息子は試験に受かって、親を喜ばせた」; rules 3/13) | Upheld | Now 「娘は毎日電話をかけて、遠くに住む父を喜ばせている。」 (喜ばせる is not on the page). vi note rewritten. |
| Rule 26 layout: l-sm-04 Q2, l-sk-17, l-sk-24, l-sk-35, l-sk-36 end without ［問い］; l-sk-18 runs the question onto the note line | Upheld | `\n［問い］` added in all six. |
| l-sk-15 / l-sk-16 both open on 許可求め→受け | Upheld | l-sk-15 ex. 1 is now 質問→情報提示 (「会議、何時からだっけ？」「3時からだよ。」). I avoided SK p.27's 「晩ご飯、何が食べたい？」「天ぷらがいいな」 shape. vi note rewritten. |

## The coordinator's ja-pane checks

- **l-sk-31:** The ja pane never claimed that lead-ins omit the topic. It only
  listed 7/2025 lead-ins. ¶2 now adds that 12/2025 問題3の2番 names the topic
  (「研修について」). The vi ¶4 says the same, and the script is cited in `sources`.
  The vi ¶4 had claimed that "the five lead-ins give only place and speaker". That was
  true for 7/2025 only and was scoped that way; it is now paired with the counterexample.
- **l-sk-27:** The ja pane already said けど/から can go either way (SK p.48 例4 vs 例5),
  so it was correct. The vi ¶3 now says so explicitly: 「Tự 『けど』 không mang nghĩa
  phủ định」.
- **l-sk-40:** The ja ¶3 had dodged the trap by quoting only 「安定性が高い」. It now
  quotes 「1番安定性が高いのにする」 and states that 1番 means 一番 (最も), not bike 1,
  and that the choice is bike 3. The vi was already right.
- **l-sk-38 / l-sk-40:** Both describe the real exam (2番 prints four names). The
  site's print-nothing mock appears only as a parenthesised aside. vi l-sk-40 ¶4 said
  the mock "reads the options twice"; nothing sources "twice", so it was cut.

## Findings (mine)

| # | Sev | Entry | Finding | Fix | Root cause |
|---|---|---|---|---|---|
| 1 | **High** | vi pane, 22 of 25 entries (~45 paragraphs) | Learner prose named its sources throughout: 「Shin Kanzen (tr.27–30)」, 「Soumatome (tr.12)」, 「Ví dụ của sách (tr.31)」, 「Sách nói…」 (rule 18). | Every paragraph rewritten without book or page. The book's worked examples are introduced as 「Ví dụ:」. | **Gate bug:** `GUIDE_CITES` holds `r"\\btr\\. ?[0-9]"`, which in a raw string matches the literal text `\btr\.`, so 「(tr.27)」 never matches. Only the 「Shin Kanzen」 token is caught. 「Ví dụ của sách (tr.31)」 and 「Sách nói」 pass as well. `GUIDE_VI_BRIEF` also never says rule 18. |
| 2 | Med | ja 8 entries, vi 8 entries | Sitting pointers were written 「（2025年7月）」 / 「Đề 7/2025」. | Rewritten to the coordinator's form, 「公式過去問の2025年7月・問題3の1番」 (ja inline; vi inside 「」). | The pointer format was not in either brief. |
| 3 | Med | l-sk-16 quiz | 「そのネクタイ、すてきですね。」 is SK p.27's 褒め example (「素敵な洋服ですね」) with the noun swapped (rules 3/13). | New stem: 「このケーキ、とてもおいしいですね。」. Key 「ありがとうございます。初めて焼いてみたんです。」 (お礼＋謙遜). Distractors: complaint misreading ×2, invitation acceptance. Both explanations rewritten. | Provenance was checked against the cited page's prose, not its table examples. |
| 4 | Med | l-sm-05 ex. 1 and quiz | Ex. 1 「山田様は、先ほど会議室においでになりました。」 copies Soumatome p.16 (「田中様がおいでです／おいでになりました」). The quiz stem 「お客様が2時にお見えになります」 copies p.16's 「田中様は２時に見える／お見えになるそうです」. | Ex. 1 → 「先生は来月、研究のためにアメリカへおいでになるそうです。」 (行く sense). Quiz → 「司会『講師の先生が、ただいま会場にお見えになりました。』」. vi note and both explanations rewritten. | Same as #3. |
| 5 | Med | l-sk-21 ex. 1 and quiz | Ex. 1 (牛乳が切れてる→買っとかなきゃ) reuses the SK p.35 script scene (household shopping, 電球が切れてる, 買わなくちゃ). The quiz's 「パソコンは情報課が設定」 for a newcomer echoes 7/2017 問題1-1 (a new arrival and パソコンの設定). | Ex. 1 → 「あしたの会議の資料、10部コピーしとかなきゃ。」. Quiz option 1 → 制服 (総務課が用意). vi note and explanations rewritten. | Rule 13 (the 例題 scripts on the answer page) and rule 21 (official scenes, cited or not). |
| 6 | Med | l-sk-17 quiz | Option 3 「相手の意見に反論している」: the stem has no opinion to rebut. The explanation had to say 「反論する意見も出ていない」 (rule 25). | Option 3 → 「その日の予定を相手に聞いている」, killed by the stem's 「〜んです」 statement form. This also ties to ¶3's question-form replies. Both explanations rewritten. | Rule 25 was applied to content quizzes, not to reply-classification quizzes. |
| 7 | Low | l-sk-32 ex. 2 | Vegetables as both 例 (of 食材) and まとめる言葉 cloned SK p.68's お米/主食 device in the same food domain. | Now sports/趣味. The vi ¶3 and note were updated. | Rule 3: "same scenario + new nouns". |
| 8 | Low | l-sk-34 ex. | 「駅前の本屋が次々に閉店…→理由」 is SK p.77's 車が売れない理由 shape (a business in decline plus から reasons). | Now 「週末、駅前の公園に人が集まっている。→ 花がきれいだから／屋台が出ているから」. vi note rewritten. | Same as #7. |
| 9 | Low | vi l-sk-24 ¶3 | Said the book's example has a closing-time condition. It has none; that condition is only the card's ex. 2. | Corrected. | Rule 15. |
| 10 | Low | vi l-sk-29 ¶4 | Quoted SK p.57's script sentence nearly verbatim inside 「」, and glossed it as "nói chậm" (the script says only the important parts slowly). | Paraphrased with "nói chậm ở chỗ quan trọng". | Brief: "never copy the book's sentences". |
| 11 | Low | vi l-sk-34 ¶4 | 「phóng viên」 for アナウンサー. | 「phát thanh viên」. | Translation. |
| 12 | Low | ja l-sk-16 ¶3 | 「どうぞお構いなく」: p.28 prints 「お構いなく」. | Now matches the page. | Rule 15. |
| 13 | Low | vi l-sk-21 ¶2 | 「〜たほうがいい」: p.33 prints 「〜たほうが」. | Now matches the page. | Rule 15. |
| 14 | Low | ja l-sm-05 ¶3 | 「お越しいただき」で始まるあいさつ: the 7/2025 stimulus begins 「本日は…」. | 「お越しいただき」を使ったあいさつ. | Wording. |
| 15 | Low | vi l-sk-20 quiz | 「Dạng không có câu hỏi trước bài nói là Mondai 3」 implied it was the only one. | Now "Mondai 3 và bài 1 của Mondai 5 chỉ có câu hỏi sau bài nói". | Wording. |
| 16 | Low | l-sk-32, l-sk-36, l-sk-40 explanations | One distractor each went unexplained: l-sk-32 opt. 1, l-sk-36 opt. 4 (vi), l-sk-40 opt. 1. | Added, within the bands. | "The explanation says what rules the strongest distractor out." |

## Not done / notes

- **Blind solve:** I solved all 24 items. I read the keys alongside, so the unchanged
  18 were not solved blind. I solved the 6 rewritten or changed items (l-sk-16, 17, 18,
  21, sm-05, and l-sk-24's layout) before keying them. Every key held, and no key
  position changed.
- **`make check` not run.** The batch lives in scratch. The scratch gate (see
  Validation) stands in for it.
- **Live batch 1 (`knowledge/N2/聴解.*.json`):** the 読解 G2 QA had already removed the
  book, page and 例題 names from the live vi pane, so I did not redo that. My scan finds
  none left in either pane. The live prose still carries sitting pointers in the old
  form (ja 4: l-q4-sokuji, l-iikae, l-sk-09, l-sk-12 「（2025年7月）」; vi ~9 「đề 7/2025」).
  These are allowed, but they are not in the new 「公式過去問のYYYY年M月・N番」 form.
  They are left to the coordinator.
- **Owner drift still open** (G1 #1): `jlpt-exam-structure` §問題1 prints その他 18.1%,
  while the profile now prints 15.5% (条件一致 1.9% vs 4.5%).
- **Untracked `CLAUDE_YOU_MUST_READ_THIS.md` at the repo root.** It asks the reader to
  author the whole of 語彙/漢字. It is outside this task, so I did not act on it.

## Rules proposed

- **check_knowledge `GUIDE_CITES`:** change `r"\\btr\\. ?[0-9]"` to `r"\btr\. ?[0-9]"`,
  and add `sách (?:nói|nhắc|lưu ý|giải thích)|của sách|Sách ` for the vi pane (#1).
  This is not edited here because it is gate code another agent may be touching.
- **GUIDE_VI_BRIEF and GUIDE_JA_BRIEF:** copy rule 18 in, with the pointer form:
  "Never name a book, page, part or 例題 in prose. Introduce a textbook worked example
  as 「例えば」/「Ví dụ:」. Point at an official item only as
  「公式過去問のYYYY年M月・問題N のM番」." (#1, #2)
- **GUIDE_JA_BRIEF, provenance:** "Compare every quiz stem and sample with the cited
  page's TABLE examples and the answer-page 例題 scripts, not just its prose." (#3–#5)
- **SKILL rule 25 addendum:** "A reply-classification quiz (受け/断り/謝り/反論 …)
  offers only categories the stem's line could plausibly be. Each wrong category dies
  by a stated feature of the line (its form, a missing apology word), never by 'no
  opinion was given'." (#6)
