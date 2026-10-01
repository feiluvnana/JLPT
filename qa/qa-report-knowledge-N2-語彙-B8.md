# QA report: knowledge/N2 語彙, batch 8 (62 words, Hajimete No.1–75; 7 → 11 live back-links; 4 → 7 ja + 1 vi live gloss fixes)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. Both panes were written by Claude authors
working separately. B7 was merged live (cfa3518) after B8 was written. Files are in the coordinator's scratch `batches/`.
The pre-review copies are in `scratchpad/QAV8_bak/`, and `QAV8_patch.py` rebuilds every batch fix from them.
`QAV8_livepatch.py <dir>` applies the one direct live fix. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B8.json` | dd660f3c443b | 8edc2cdbc585 |
| `語彙_B8.ja.json` | 4fbcc5ef860e | a4c5faa0fc77 |
| `語彙_B8.vi.json` | 08c446e3a7ab | 4283f412f5ca |
| `語彙_B8.backlinks.json` | 4466ebaf5fe7 | 9e1dc018e922 |
| `語彙_B8.backlinks.vi.json` | 7d9cfaf36ab4 | 7d096fc4adf6 |
| `V8_live_meaning_fix.json` | 9034eebb1ac2 | 513c262fbf3f |
| `V8vi_live_meaning_fix.json` | — (new) | 3d09fa1ec1b9 |

## Verdict

`QA: FAIL → fixed (6 finding classes: 1 wrong group label (35 cards), 9 example frame/scene copies, 4 unlinked look-alike pairs, 9 gloss lures (5 of them live), 2 prose fields that quote or overreach, 1 example that its vi note mistranslated). 0 content findings are open after the fixes.`

**No id, headword, reading, pos or official count in the batch is wrong.**

**Validation.** `QAV8_gate.py` copies `.agents/` and the CURRENT live `knowledge/` (B7 included) into `scratchpad/QAV8_root`.
It applies `V8_live_meaning_fix.json` (ja), `V8vi_live_meaning_fix.json` (vi) and `QAV8_livepatch.py`, then runs
`merge_batch.py`'s own code (REPO set to the scratch root) for 語彙 B8. That merges the batch, applies both back-link files
and checks book order. It then builds `語彙.html` and runs `check_knowledge.check_category`. Result: **17 of 17 ok, 0 FAIL,
0 WARN**: 478 entries, 869 generated items (391 reading, 478 meaning), 11 live entries back-linked, cards in book order, and
**no `REVIEW` line in either pane**. The first post-fix run failed the たちまち back-link bands (ja 103/100, vi 199/180).
I trimmed both without dropping a quoted form and re-ran.

**Live files.** I applied `QAV8_livepatch.py` to the real `knowledge/N2/語彙.json`; it relabels 3 groups (§1). I then ran
`make knowledge` and `make drill LEVEL=N2`. `make check` printed "All checks passed (239 skipped), 224 warning(s)". None of
the warnings is on a knowledge or drill line. Nothing is committed. All other live changes are in the fix files and the
back-link files, which the coordinator applies at merge.

## 1. Range, ids, headwords, readings, group

- **Every number 1–75 is now a card.** I opened Hajimete PDF pp.11–21 (printed 12–22). The 62 B8 cards plus the 13 live
  cards (5 6 14 17 18 20 22 32 33 34 36 68 74) cover 1–75 exactly. Every id, headword, reading and pos matches the page.
  Every cited `page` is the right PDF page: 1–7 → 11, 8–16 → 12, 17–22 → 13, 23–26 → 14, 27–33 → 15, 34–41 → 16,
  42–49 → 17, 50–57 → 18, 58–65 → 19, 66–71 → 20, 72–75 → 21. The 思い込み ＋ word is on 20 and 愛を込めて is No.77 on 22.
- **Group label (author doubt 1): wrong in live as well as in the batch.** PDF 18 prints Section 3 as 「知人・付き合い」
  (ちじん つきあい). 「知り合い・付き合い」 came from the inventory OCR and was copied from live v-0068 直接, v-0074 ぐち and
  v-o-kioku 記憶. All 32 B8 cards and those 3 live cards are now `第1章 人と人との関係／知人・付き合い`. This does not change
  the order, since the label sorts by its first numbered word. `references/inventory/N2.json` still carries the OCR label.
  I did not touch the inventory; that is for the coordinator.
- **Readings.** All 62 are as printed (いっか, せけんしらず, いいつける, ほうっておく, かんじ, おおや, かいぬし, かわす,
  きくばり, …). No reading distractor is a valid reading of its headword.
- **Furigana.** I read all 500 distinct ruby pairs. They include 世間知《せけんし》らず, 友達付《ともだちづ》き, 付《づ》き合い,
  離《ばな》れ, 気配《きくば》り, 一家団《いっかだん》らん, 出産祝《しゅっさんいわ》い, 家族連《づ》れ, 二《ふた》つ and 五《いつ》つ.
  None is wrong.

## 2. official_count, hit by hit (rule 35)

`QAV8_find.py` printed every parsed 問題1–6 item holding each form (`QAV8_find.txt`). I grepped the merged 12/2010
booklet by hand. It has only 読解 hits, among them うろ覚え, which is cited.

- **All 62 counts are right.** The three 1s are 呼び止める (7/2013 4-16 key), 思い込む (12/2024 4-17 key) and 招く
  (12/2016 2-6 key まねいた).
- **Excluded hits, confirmed on the booklet line.** Distractors only: 招いて (7/2012 2-6, 12/2014 4-20), 招った
  (7/2011 2-9), 納得 (7/2019 4-18), 結びついて (7/2024 4-19), 込めた (7/2012 4-18). Stems only: 慰められた (7/2019 1-4,
  where the target is 恥), 等しく接する (12/2019 1-1, where the target is 等しく), 再会する (12/2012 4-20), 友人 (many).
  Misuse lines of other words: 手軽な自己紹介 (12/2014 6-32). Key sentences of other words: 話が盛り上がった (7/2022 6-28 世代).
  覚え: 12/2017 5-23's key is the verb 覚えて, credited to live 記憶, so it is not the noun.
- **Rule 35, part 1.** I intersected every item B8 cites with every live citation: 6 shared items, each credited to the
  right side (蓄える, 問い合わせる, 握る, 油断, 場面/名所). No live `sources` note counts a B8 word's hit.

## 3. Author doubts

| doubt | verdict |
|---|---|
| 「知り合い・付き合い」 vs 「知人・付き合い」 | **Book wins.** Fixed in the batch and in 3 live cards (§1). |
| Link 覚え↔記憶 | **Linked.** Hajimete prints 記憶 as No.60's ＋ word. Both are 名詞 with no shared kanji, so the generator can pair them, and the glosses (前に…心に残る / 心にとどめる) are near-synonyms. Compares in both panes and back-links. |
| Link 甘える↔甘やかす | **Linked** as a 自他 pair (Hajimete No.7 ＋ word). The shared 甘 already keeps them off each other's quizzes. |
| Live 垂直 「直角に交わる」 vs B8 交わす | **Fixed.** The gloss printed 交わ, the kanji and okurigana of a new same-category headword. → 「…線や面が直角になっていること。」 (fix file). |
| とっさ vs たちまち/途端 | **Linked both.** Hajimete glosses とっさ "instant / 刹那间 / ngay lập tức". The ja glosses (考える時間もないほど短い間 / とても短い時間のうちに / まさにその瞬間) read as one another. The たちまち back-link was at its band, so it is rewritten with every quoted form kept. |
| 幹事, 察する vi | **Sourced; kept.** 幹事 "Người lo liệu mọi việc cho buổi tiệc…" follows the EN "organizer", the ZH 负责人 and the page example (飲み会の幹事), and the Hán Việt note does not contradict "cán sự". 察する "Đoán ra, cảm nhận được" follows the EN "infer" and the ZH 揣测/察知; "đồng cảm" is still covered by "cảm nhận… tâm trạng". |
| 意思/意志 | **Rewritten.** The ja nuance quoted the PDF 101 example frame (「強い意志で〜を決める」 ← 弟は強い意志で留学を決めた; rule 32). The ja gloss 「何かをしよう、こうしたいと思う考え」 also shared 「こうしたい」 with live 願望 (same pos, no shared kanji). Now: 「自分がこれからどうするつもりかという考え。」 (EN "intention", ZH 打算) and 「…意志は目的に向かってやりとげようとする心の強さで、「強い意志」のように言う」 (EN "will"). The vi meaning and nuance were rewritten separately. |
| Official options quoted without ruby | **Correct as written.** The ja pane rubies real-word options (聞き取られて, 思い起こして, 考え抜いて). Non-words (伯いた, 泊いた, 召いた) have none (rule 34). The vi pane follows the live convention (引き止める, 頼る): no ruby on options. |

## 4. Examples: frame and scene (rules 21, 35, 39)

The 10-char window scan (`QAV8_prov.py`) found only boilerplate and one trivial 「コミュニケーションが」. `QAV8_frame.py`
sets every example beside every sentence sharing 2+ content tokens with it. The corpus was all refs extracts, every
`knowledge/N2/*.json` (文法 stems included), every open batch (文法_B8–B11, 漢字_B7/B8; 語彙_B9 does not exist yet) and
tests/imported-*. I also compared every example with its Hajimete page example and the cited official items, including
問題6 misuse lines. I grepped each replacement's scene nouns over the same corpus before keeping it.

| # | entry | finding | fix |
|---|---|---|---|
| E1 | 接する ex1 「祖父は、孫に接するときだけは、別人のように優しくなる」 | 7/2016 問題7-41 「どんな人が相手でも厳しく接する森先輩だが、なぜか私（には）そうではない」: the same "one way to all, different to one person" frame. 12/2019 1-1 等しく接する also prints やさしく as an option. | → 「サークルに入って留学生と接する機会が増え、英語で話すことにも慣れてきた。」 |
| E2 | 察する ex | The live 読解 guide passage (年配の客が困っている様子…店員は気づかなかった) has the same scene reversed. A first replacement (inferring illness from a voice on the phone) was the 文法 stem 「…母は体の具合が悪いのではないかと心配した」, so I discarded it. | → 「部長の短い返事から、計画にあまり乗り気でないことを察した。」 |
| E3 | 近所付き合い ex | 文法 stem 「祖母は…自分の畑でとれた野菜を（差し上げた）」: grandmother, field vegetables, giving. A first replacement was the 文法 example 「…隣の人の名前すら知らない」, so I discarded it. | → 「祖母の住む村では今も近所付き合いが盛んで、祭りの準備は村じゅうで行う。」 (the usage now shows 〜が盛んだ in both panes) |
| E4 | あえて ex 「楽な方法もあったが、彼はあえて時間のかかる手作業を選んだ」 | The claim of the cited 7/2021 読解 (「時間のかかることをあえてする」). The scan missed it because 時間 is a stop token. I rejected candidates matching 12/2018 読解 (新人が意見を言う), 7/2010 2-8 (伝統の味を守る) and the 読解 guide (反対の意見を言い出しにくい). | → 「人気が出ても、店主はあえて店を広げず、今も一人で料理を作っている。」 The gloss drops わざわざ: 「ふつうはしないことや難しいことを、わかっていて進んでする様子。」 |
| E5 | 見習う ex 「先輩の電話の受け答えを見習って」 | Hajimete No.71's example 「アルバイト先の先輩の気配りを見習いたい」 (先輩's manner at work). A first replacement (a boss's time management) was a 聴解 guide quiz option (朝の時間の使い方), so I discarded it. | → 「祖父を見習って、毎朝近所の公園を掃除するようになった。」 |
| E6 | あきれる ex (a husband who never picks up his socks) | The Hajimete p.17 frame 「彼はいつも遅刻するので、あきれてしまう」: a habitual misdeed, then あきれてしまう. | → 「自分から頼んできた仕事なのに、もう忘れている上司にはあきれた。」 |
| E7 | 説得 ex 「反対していた祖父を説得して…」 | Hajimete p.12 「父は私の留学に反対だったが、母が説得してくれた」 (the OCR mangles it, so only the page shows it). A first replacement 「家族で何度も話して…」 was the 文法 example 「家族で何度も話し合った結果、祖母と…」, so I discarded it. | → 「時間をかけて祖父を説得し、やっと車の運転をやめてもらった。」 |
| E8 | 招く ex1 「結婚二十年の記念に、両親を…」 | Whose anniversary was unclear, and the vi note (ngày cưới của bố mẹ) said something the Japanese did not. | → 「両親の結婚二十年の記念に、二人をレストランの食事に招いた。」 |
| E9 | 大家 vi note | 「bà chủ nhà」 adds a gender the Japanese does not have. | → 「chủ nhà」 |

- **Checked without change.** These were kept because the scene differs and the sense forces the frame:
  - 振り返る ex1 (a noise behind → turned round) against Hajimete ① (name called from behind) and 7/2015 6-29.
  - 呼び止める (police at a crossing) against Hajimete (管理人) and 7/2013 4-16 (reporter).
  - 言い出す (son says he doesn't want to go) against Hajimete (sister wants to study abroad).
  - つくづく (watching parents work → business is hard) against SK 語彙 PDF 150 (seeing her cry → I was wrong, a different predicate and claim).
  - 招く ex2 against Hajimete ② 混乱を招いた.
  - 込める against live 願望 (a painting).
  - 盛り上がる against 7/2022 6-28.
  - 大家 against SK (家賃をせまられた).
  - あきれる (new) against the 12/2010 読解 on 上司's unreasonable requests (a different claim).

## 5. Generated quizzes and glosses (rules 28, 34, 40)

`QAV8_dump.py` dumped all 869 items before the fixes (`QAV8_quiz.txt`) and after them (`QAV8_quiz2.txt`). I read all 210
meaning items that involve a B8 word (`QAV8_mq.txt`). `QAV8_glosshw.py` (headword/stem containment and shared gloss words,
both panes) and `QAV8_kcheck.py` (vetting every new gloss) found these lures:

| gloss | lure | fix |
|---|---|---|
| B8 てっきり 「…迷わずに信じていた」 | prints 迷 (live 迷う). As 案の定's distractor it also read as "as expected". | 「疑わずにそうだと信じていたが、実は違っていた様子。」 (the nuance is now in the gloss, so ja nuance → "") |
| B8 縁 「人と人などをつなぐ…つながり」 | reads as 仲 「人と人との関係」 (same pos); vi "mối gắn bó" ≈ "quan hệ" | 「人と人、人と場所などの間にある、ふしぎなめぐりあわせ。」 (Hajimete "fate / 缘分") / vi "Duyên, cơ duyên gặp gỡ…" |
| B8 大家 「…持ち主」 | 主 of 飼い主 (same pos) | 「家やアパートを人に貸している人。」 |
| B8 振り返る 「…思い出して考える」 | 思い (思い込む, 思いやり; the B7 苦情 precedent) | 「…過去のことをもう一度考える。」 |
| live 反省 (fix file) 「…思い返し…」 | the author's fix removed 振り返 but brought in 思い | 「自分のしたことをもう一度よく考えて、悪かった点に気づくこと。」 |
| live 受け入れる (fix file) 「…グループや組織の中に…」 | still printed the headword 組織; a 引き取る draft would print 引き (引き止める) | 「やって来た人を、自分たちのところに迎え入れる。」 |
| live 伝統 「昔から受け継がれてきた…」 | 継 of B8 継ぐ | 「昔から伝えられてきた…」 (added to the fix file) |
| live もてなす 「心をこめて迎え…」 | こめ of B8 込める (same pos) | 「心を尽くして迎え…」 (added) |
| live 充実 vi "(thiết bị, chế độ) chu đáo" | B8 気配り's key "Sự chu đáo…" (same pos) | "…đầy đủ" (new `V8vi_live_meaning_fix.json`) |

- **The author's four live fixes.** 触れる and 模範 are kept: both fit their cards' examples, and neither brings in a
  headword. 反省 and 受け入れる are re-fixed (table). The fix file now holds **7** ja meanings.
- **Left as residual.** All are cross-pos, so the same-pos generator does not pair them today:
  - 大いに/相当: vi both "rất" (副詞 vs 副詞・ナ形容詞).
  - 久しい/とっくに: vi "Đã lâu" / "Đã từ lâu rồi" (イ形容詞 vs 副詞).
  - 意思 vi "ý định" against 願望 "mong ước": distinct after the fix.

## 6. Prose

- **ja.** 大半 「半分よりずっと多い」 overstated "most" (Hajimete "hơn nửa, phần lớn"), so it is now 「半分より多い」.
  「つくづく反省する」 is sourced (SK 語彙 PDF 150 example), and 「あえて〜必要はない」 is sourced (12/2019 読解 「夢なんかあえて
  もつ必要はない」). Every quoted official distractor list matches its booklet line. No prose names a source.
- **vi.** It is not a translation of ja: the Hán Việt notes and the example-led usage lines are its own. No Japanese
  stands outside 「」. Every example_note is faithful except E8/E9, and the 7 replaced examples have new notes written from
  the Japanese. 同期 usage dropped 「同期と仲がいい」, which rebuilt Hajimete's example sentence with the 「会社の同期」 beside it
  (rule 32). 察する, 接する and 近所付き合い usage lines follow the new examples.
- **Back-links.** The 7 author back-links sit on the CURRENT live text: none of their targets was touched by B7. Quote by
  quote, old → new, nothing is lost in either pane. QA adds 甘やかす, 記憶, たちまち and 途端 (11 in all), each with a complete
  ja and vi compare.

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| Group label | The inventory's B8–27 OCR rows carried the label, and the author matched the live cards instead of the page. N2.md says "rows are a number range only" but not "labels too". | N2.md: *a B8–27 row's `group` is OCR as well: read the Section title off the page; live cards inherit the error, so fix them too.* Coordinator: patch `inventory/N2.json` (知り合い→知人). |
| E1 (official 問題7 frame), E4 (cited 読解 claim) | The author's scan compared nouns, and 時間 is a stop token in a typical frame scan. 問題7 stems were not in its view for a 語彙 card. | Existing rules 21/39. LEX brief: *grep the example's predicate over every official 問題7–9 stem, not only 問題1–6, and print each cited 読解 line's claim before writing.* |
| E2, E3 (knowledge-module scenes), and three QA first drafts that hit 文法 stems/examples | The module now holds ~1,500 example/stem sentences; scene reuse is near-certain without a grep. | Gate idea (B7's, now more urgent): WARN when an example shares 3+ content tokens with any knowledge sentence. `QAV8_frame.py` is a working prototype. |
| E5–E7 (Hajimete page frames) | The Hajimete OCR mangles some example lines (説得's is unreadable), so a scan of `vocab_reference.md` cannot see them. | LEX brief: *open the Hajimete PDF page for every card (not only for doubtful readings) and compare each example with the printed one.* |
| Gloss lures (てっきり 迷, 伝統 継, もてなす こめ, 大家 主, 充実 vi) | Rule 40's gloss check was run for B8 glosses against live headwords, but not for **live glosses against B8's new headwords**, and not for kana spellings (こめ). | LEX brief: *when a batch adds headwords, grep every live gloss (both panes) for each new headword's kanji, stem and kana form.* |
| Fix-file re-fixes (反省, 受け入れる) | B7's rule (*a live fix is itself grepped*) was not applied to this batch's own fix file. | Existing B7 LEX rule; keep. |
| 4 unlinked pairs | 記憶 and 甘やかす landed in B7 after B8 was written; とっさ's partners were in another chapter. | QA-only; keep. |

## For the coordinator — merge steps

1. Already applied to the real `knowledge/N2/語彙.json` by `QAV8_livepatch.py`: 3 group labels (v-0068, v-0074,
   v-o-kioku). `make knowledge` and `make drill LEVEL=N2` have been run. The script is idempotent; do not re-run it.
2. Apply `V8_live_meaning_fix.json` (7 ja meanings: 触れる, 模範, 反省 (re-fixed), 受け入れる (re-fixed), 伝統, 垂直, もてなす)
   to `語彙.ja.json`, and `V8vi_live_meaning_fix.json` (充実) to `語彙.vi.json`.
3. Run `merge_batch.py 語彙 8`. It applies **11** back-links: the authors' 7 plus 甘やかす, 記憶, たちまち and 途端.
4. `make knowledge`, `make drill LEVEL=N2`, `make check`.
5. Patch `.agents/jlpt-knowledge/references/inventory/N2.json`: 「知り合い・付き合い」 → 「知人・付き合い」.
