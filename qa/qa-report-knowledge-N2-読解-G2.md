# QA report: knowledge/N2 読解, guide batch 2 (13 guides r-sk-13…25, 12 quiz items) + batch-1 rule-18 repair

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. Batch files are in the coordinator's
scratch `batches/`. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `読解_G2.json` | 474d95452aac | 2ef620cc1622 |
| `読解_G2.ja.json` | cb43834e40f3 | 2def5aa6e3e1 |
| `読解_G2.vi.json` | ca70b6b70db2 | 0bc2f45e4d97 |
| live `knowledge/N2/読解.ja.json` | af10f999640f | fccc76883c2d |
| live `knowledge/N2/読解.vi.json` | a028e6c8ccd9 | 07f219c1c527 |
| live `knowledge/N2/聴解.vi.json` | 005ef0127c0d | 38b94d239dd8 |
| live `knowledge/N2/聴解.ja.json` | d2798f8cc049 | unchanged |

## Verdict

`QA: FAIL → fixed. Batch 2: 11 findings across 11 entries. Batch 1 (live): 1 finding class (rule 18), 105 paragraphs
rewritten. No content finding is open.`

- **Batch 2 validation.** I merged G2 into a scratch copy (`scratchpad/QAR2_repo`: `.agents` + the fixed live `knowledge`
  copied, `refs`/`tests`/`logs`/`tools` symlinked). Then I built it with `build_knowledge.py --level N2` and ran
  `check_knowledge.py`: **0 FAIL, 0 WARN** (38 entries, 37 quiz items balanced). Batch 2 was **not** merged into the real
  `knowledge/`.
- **Batch 1 (live).** After the edit I ran `make knowledge LEVEL=N2` and `check_knowledge.py`: **0 FAIL, 0 WARN**.
- **Whole repo.** `make check` passed with 224 warnings, the same count as before. None of them comes from the knowledge
  module. All are older pool, rotation or test warnings.

## 1. Blind solve

- **My own solve.** `QAR2_blind.py` extracted stem and options only, with no ids, shuffled with seed 4127. I saved my
  answers to `QAR2_myanswers.json` before I opened the map. **12/12 agreed with the keys.**
- **Second model.** I ran `agy_blind.py` (gemini-3.8-flash-medium, 2 shuffled runs) after the fixes: **12 clean,
  0 flagged.**
- **Splices.** I spliced every distractor into its stem. Each kill is either a contradiction of quoted stem words or the
  cited page's own rule: 追加情報 after なお (p.86), part-not-whole for a 指示語 (p.138), 本文に書かれていない.
- **Answer positions.** They are balanced at 3/3/3/3.

## 2. Inputs judged

| input | verdict |
|---|---|
| ja 「2025年7月の53番」-style references | **Kept only as pointers to on-site items. Each one is now written as 「公式過去問のYYYY年M月・N番」 (F2).** On-site means the 10 `tests/imported-n2-*` papers, 7/2021–12/2025, which the portal lists as 公式過去問. r-sk-13 cited 7/2011 Q63 twice, and that paper is not on the site, so both citations are **cut (F1)**. The live 聴解.ja 「（2025年7月）」 notes point at an on-site paper, so they are kept. |
| vi: r-sk-23 option 2 「店員が、閉店の前に店の片づけを始めたこと」 is literally true and loses only as part-not-whole | **Kept.** SK PDF p.138 (例題29 解説) prints the rule: a forward-pointing 「こんな〜」 refers to the whole episode, summed up across the paragraphs that follow. Option 2 names only why the staff were busy. The customer and the not-noticing are absent from it, so it is not the event that made the writer change the shop. Its kill is distinct from the others: 1 is contradicted (尋ねた is not in the passage), 3 is the result, and 4 is the key. Official 指示語 items use the same kind of true-detail distractor. The second model did not flag it. |
| vi: r-sk-22 reads 「確かに…しかし」 as concession plus the author's view, with no cited page | **Sourced (F5).** SK 読解 PDF p.16 (book p.10, 例題3 解説) prints 「たしかに ← まず、ある意見を一部認める」 and 「しかし ← 筆者の本当に言いたいこと」, plus the note 「たしかに…。しかし〜。」「もちろん…。しかし〜。」に注意. I added that page to r-sk-22's `sources`. The prose is unchanged. |
| vi: r-sk-21 labels the older-edition figures, then gives the owner figures | **Exact, kept.** The "old" figures match SK PDF p.127 (book p.123) word for word: 中文 500字程度・問い三つ程度; 長文 900字・3問・1問は主張; 統合 二つ以上 合計600字程度; 情報検索 700字程度・問いが素材の前. The owner figures match `dokkai.md` §Length bands: 507/655/763, 814–1061, 532–592, JP-char method named; 問題14 all-char 676–793, median 707, JP-char 489–638. The JA twin is the one that was off (F6). |

## 3. Findings: batch 2

| # | sev | entry | finding | fix | root cause |
|---|---|---|---|---|---|
| F1 | med | r-sk-13 (ja) | B1 and B2 cited 「2011年7月の63番」 as evidence (「試験でも…で出ている」, 「ピアノやパーティーなどの場面だった」). The paper is not on the site, so this is a citation in prose (rule 18). | Both removed. B1 now gives the two frames only. The source stays in `sources`. | GUIDE_JA_BRIEF says to "cite a sitting when you state what the real exam does". That invites dates in prose, and nothing limits them to papers the learner can open. |
| F2 | low | r-sk-13, 14, 15, 16, 18, 24, 25 (ja) | On-site sitting references were phrased as citations (「…の形で出ている（2025年7月の53番・55番）」, 「最近の試験では…も出ている（…）」). | Rephrased as pointers: 「（公式過去問の2025年7月・53番と55番）」 and similar. | Same as F1. |
| F3 | med | r-sk-15 | **(a)** The quiz scene, a reservation rule for a shared room, is the same scene as the entry's own example 1 「会議室の予約方法変更のお知らせ」 (rule 11). **(b)** The quiz tracks SK 例題18 (PDF p.85): a management notice to residents, a title question, and a 「なお」 afterthought distractor (rule 13). | New scene: a sports-center locker notice. Key 4 kept. Both explanations rewritten. I first thought of a library notice, but 12/2021 問題12 A is a library notice, so I did not use it. | The 10-char scan cannot see a scene copy. The rule-11 check (example vs quiz inside the entry) was not run. |
| F4 | low | r-sk-16 | The quiz scene 「週末木工教室「小さな本棚を作ろう」」 overlaps 7/2016 聴解 問題1-4, a home-center furniture-making class whose options include 一日体験教室. Rule 21 applies to official listening scripts too. | The scene is now a そば打ち教室. Dates and key are unchanged. | Rule 21's script scan was not run on guide quizzes. |
| F5 | med | r-sk-22 (vi) | The 「確かに…しかし」 claim cited no page. | Sourced to SK PDF p.16 (see §2). | The VI author read only the pages the entry cites. The 確かに point is in 第1部 1-1). |
| F6 | low | r-sk-21 (ja) | 「一つは500〜750字ほど」 is below the owner's maximum of 763, and the text gave no counting method. dokkai.md: "Never quote a length without naming this method." | Changed to 「500〜760字ほど」 and 「（字数は日本語の文字だけで数えた目安）」. | Batch-1 rule (b) (copy the owner's sentence with its caveat) was not yet in GUIDE_JA_BRIEF. |
| F7 | low | r-sk-14 (ja) | 「最近の試験で10問中8問」 dropped the owner's denominator. exam-structure says "8 of 10 **apparatus** items". Read literally, the JA sentence claims 8 of every 10 問題10 stems. | Changed to 「メールやお知らせの問い10問のうち8問」. | Same as F6. |
| F8 | low | r-sk-15 (ja) | 「メールでは、「さて」の後から「〜ください」までが本題になりやすい」 widens one 例題19 observation. PDF p.88 says 本題は「さて」の後と「ください」の前 about that one mail. | Changed to 「…の後や「〜ください」の前に本題があることもある」. | Rule 15 (paraphrase that widens) was applied only to 接続 in 文法. |
| F9 | low | r-sk-15, 17, 19 (vi) | Unsourced or widened claims. **(a)** 「Lời chào… có khi dài hơn cả phần chính」 is on no page. **(b)** "chữ nhỏ… thường ghi lưu ý" widens the page's 「ことがある」. **(c)** "Hai điều hay bị hỏi" is a frequency claim with no count. **(d)** "Trong một bài mẫu về phiếu giảm giá…" points at the book's 例題20, which the learner cannot see. | (a) cut; (b) changed to "có thể ghi"; (c) changed to "Ở mỗi bước, xem…"; (d) rewritten as a general trap. | Rules 9 and 20 (frequency words need a count) were not applied to the VI pane. |
| F10 | low | r-sk-19, r-sk-25 (ja) | 「返品の手続き」 and 「備考」 appear on no cited page. The cited pages show 薬, the norimo card procedure and the 「おすすめ」 column. | Both cut. | Rule 9. |
| F11 | low | r-sk-16 (vi) | The explanation printed 「5月10日」-style dates outside 「」 (rule 6). | Changed to Vietnamese dates ("ngày 10/5"). | Rule 6 was not script-checked on the VI quiz field. |

Checked and kept (no change needed):

- **Every cited SK page read on the scan.** 読解 PDF pp.16, 75–76, 81–86, 88, 93–94, 96–97, 101–102, 105, 108, 113,
  115–116, 118, 123–125, 127–130, 136, 138–139, 152, 154, 166, 169, 172. Every other strategy sentence matches its page.
- **Cited official items read in `booklet.md` and the key.** 7/2022 Q68; 12/2022 Q55; 12/2023 Q53 (usually 経理課,
  this time 営業課, key 3); 7/2025 Q53 and Q55; 12/2021 問題12 (A 図書館の掲示, B 高校生の意見, Q65 asks A only); 12/2021
  and 7/2024 Q70 (「次の4人は…」).
- **Provenance.** The 10-char scan (`QAR2_prov.py`), run before and after the fixes, finds only stock frames. I also
  grepped the scenes against every `booklet.md` and `script.md` (マラソン, 倉庫, 入館, 加湿器, 自転車, 閉店, 体験教室, ロッカー,
  図書館). r-sk-25 (a 10 km 市民マラソン entry notice) is kept: 7/2019 Q36 is a grammar sentence about a race time, not an
  entry-conditions notice.
- **Furigana.** I read all 1,064 ruby pairs. Counters are right: 1日《ついたち》, 10日《とおか》, 20日《はつか》, 〜7日《なのか》,
  三日《みっか》, 行《ぎょう》.
- **Vietnamese pane.** Every Japanese string is inside 「」 (scripted; only the grammar label 「thể た」 is bare). The pane is
  not a translation: each card has its own structure and its own examples. example_notes are faithful.

## 4. Batch 1 (live): rule 18 repair

**F12 · high.** The live 読解 and 聴解 prose named its sources throughout:

- **読解.ja r-sk-01** opened with 『新完全マスター読解N2』の第1部, was titled 「第1部の学習の進め方」 and ended 「この本のやり方だ」.
  **r-sk-02** and **r-sk-08** began 「第1部の前半/後半では」.
- **読解.vi** used "Sách 「完全模試」 nêu…", "Theo Shin Kanzen…", "Mẹo của 「完全模試」", "ví dụ 7 của Shin Kanzen" and
  "trong ví dụ của sách" across 25 entries.
- **聴解.vi** used "Shin Kanzen (tr.19)", "Sách 『完全模試』 khuyên", "(các thẻ Shin Kanzen II)", "Trang 27" and "ví dụ 5"
  across 25 entries, with the four l-sk titles reading "Shin Kanzen: giới thiệu dạng …".

**The fix.** I rewrote 105 paragraphs (`scratchpad/QAR2_live_patch.py`; each edit asserts the old text): 6 in 読解.ja,
44 in 読解.vi and 55 in 聴解.vi.

- Every source name, page, part (第N部 / Phần N) and 例題 number is removed. The advice itself is kept, and the
  citations stay in `sources`.
- Textbook length figures (「完全模試」 ghi 200/500/600/900 chữ) are dropped. The real-exam measurement stays, now with its
  JP-char method named.
- Sitting pointers to on-site papers ("đề 7/2025", 「（2025年7月）」) and era boundaries ("từ kỳ 12/2022") are kept.
- I added no new claim. Where dropping an attribution would have left an unsourced frequency word, I softened the wording
  (for example "có thể chính là", "có khi").
- 聴解.ja needed no change. I did not touch `batches/聴解_*`.

**Root cause.** Rule 18 was written for item categories. The batch-1 guide QA looked at the VI pane's "source
attribution" structure and approved it. `check_prose_citations` (rule 30) scans item-category prose only, so no check
reads guide prose.

## 5. Rules to add

- **SKILL rule 30, extend the check to guide kinds.** `check_prose_citations` should WARN on guide prose too, on:
  Shin Kanzen, 新完全, 完全模試, 総まとめ, `tr.\d`, `ví dụ \d`, 例題, 第N部, Phần N, この本, 本のp., 「sách」 used as a
  source. It should also WARN on a sitting date that is not one of the imported (on-site) papers. (F1, F12)
- **GUIDE_JA_BRIEF / GUIDE_VI_BRIEF.**
  - (a) Replace "cite a sitting when you state what the real exam does" with: *prove it in `sources`. In prose, mention a
    sitting only as a pointer to an on-site 公式過去問 item (「公式過去問のYYYY年M月・N番」). Never name a book, a page, a
    part or a 例題.* (F1, F2, F12)
  - (b) Before hand-off, check each quiz scene against the entry's own examples (rule 11), the cited 例題, and a
    scene-keyword grep of every `booklet.md` and `script.md` (rule 21). (F3, F4)
  - (c) A 「確かに／もちろん…しかし」-type claim needs its page. For 読解 it is SK PDF p.16. (F5)
