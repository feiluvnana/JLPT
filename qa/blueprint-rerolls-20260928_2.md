# Blueprint rerolls — 20260928_2 (why each `--reroll-one` ran)

Base draw: `make sample 20260928_2 SEED=37987317`. Every reroll below used a
fresh `secrets.randbelow(10**8)` seed, and each one was forced by a rule. None
was run to get a "nicer" item. The authoritative record is the spec's `seed`
string and `rotation.reroll_log`, which the ledger row mirrors. This file only
explains the evidence behind each reason. Count rerolls from the seed string;
this note holds no count.

| # | reroll | out → in | reason |
|---|---|---|---|
| 1 | `kanji_reading:0` seed 72408319 | 御手洗い(おてあらい) → 針(はり) | **Validity rules 2 and 4.** The key reads 御 as お, which is not a 常用音訓. Shin Kanzen 漢字 #646 gives 御 as ギョ／ゴ／おん. The spelling 御手洗い has zero hits in the Shin Kanzen, Soumatome and Hajimete extracts and in all 31 sittings. Shin Kanzen 漢字 #435 洗 prints the word as お手洗い, with a kana お. お手洗い is also an N5 core word, the class the 2026-09-28 audit removed. Replacement: 針 is 訓 and attested (SK 漢字 #797 はり), so 2 of 5 targets stay 訓. |
| 2 | `kanji_reading:3` seed 29770999 | 複製(ふくせい) → 精算(せいさん) | **Validity rule 4, removal signal.** 複製 is absent from the textbooks AND from the archive. I read Shin Kanzen 漢字 #970 複 on the page (PDF p.198): it lists only 複雑／複写／複数. There are zero hits for 複製 or ふくせい in Soumatome 語彙, Hajimete 2500 and every extract of the 31 sittings. One source is unchecked: the Soumatome 漢字 book, a scan with no text layer and no index. Replacement: 精算 is 音 on 常用音訓, and the archive corroborates it (12/2018 問題2 option set; 12/2021 読解 「レジでご精算の後」), so it satisfies rule 4. |
| 3 | `reading_topics:9` seed 57805307, `--exclude-theme` ×11 | 交通 → デジタル化 | **Theme rule 4, consecutive papers.** Index 9 is 問題12, a headline surface. 交通 is 20260928_1's 問題9 headline. The exclusions are rule-forbidden themes only. From 20260928_1 (one paper back, rule 4): headlines 交通, 人間関係, 文化・伝統, 食, plus its 聴解問題5 themes スポーツ・余暇 and 消費・経済. From 20260917_1 (two papers back): headlines 環境, メディア・情報, 働き方, 行政・手続き, plus its 聴解問題5 themes 消費・経済 and 科学・技術. The kept 問題13 行政・手続き already spends the two-back budget of one. 行政・手続き and 科学・技術 are also this paper's other headlines (rule 1). |
| 4 | `reading_topics:11` seed 91982577, `--exclude-theme` ×12 | 科学・技術 → 子育て・家族 | **Theme rule 4, two papers back, at most one repeat.** Index 11 is 問題14, a headline surface. 科学・技術 was 20260917_1's 聴解問題5-2番 headline. That made a second two-back repeat beside 問題13 行政・手続き, which was 20260917_1's 問題14. `check_theme_repeat_cross_test` counts the earlier paper's composed 聴解問題5 against this paper's 読解 headlines (the 20260928_1 F1 correction). Tie-break: the later index of the two was redrawn. Exclusions: the same 11 as row 3, plus デジタル化 (this paper's new 問題12 headline, rule 1). |

Headline set after the rerolls: 問題12 デジタル化, 問題13 行政・手続き, 問題14
子育て・家族. The 問題9 cloze is 住まい; `qa/dokkai-allocation-20260928_2.md`
records the derivation. 聴解問題5 is composed at stage 3.

- Rule 4 against 20260928_1: 0 repeats.
- Rule 4 against 20260917_1: 1 repeat (行政・手続き).

## Pool defects surfaced by this draw (not fixed here — Stage 1 writes only the spec and the ledger)

- **`kanji_reading` 御手洗い(おてあらい)** is undrawable: it needs a 表外音訓, its
  spelling is unattested, and it is N5 core. After reroll 1 no ledger row holds
  it, so by `exam-blueprint` §"Pool entries stay inside the N2 band" it should be
  **deleted**, not retired.
- **`kanji_reading` 複製(ふくせい)** meets rule 4's removal signal on the evidence
  above. No ledger row holds it either. The only check left before deleting it is
  one read of the Soumatome 漢字 page for 複.
- **`orthography` 引分け** is drawn and KEPT on this paper. Its spelling does not
  match the textbook headword 引き分け (Hajimete; SK 漢字 kanji table). There are
  zero hits for 引分け in any extract or sitting. It is not undrawable: the
  repair is to correct it in place (`exam-blueprint` §"A pool spelling must match
  its headword"), and to carry the corrected string into this spec and its ledger
  row, so `check_draw_provenance()` still resolves. The 文字・語彙 author must not
  print 引分け as the key before that is decided. Decision for the orchestrator.

## Pool corrections made by the orchestrator after the draw (2026-09-28)

- **orthography 引分け → 引き分け**, corrected in place (exam-blueprint: "a defective but fixable string is still corrected in place"). The Shin Kanzen headword is 引き分け, and the spelling 引分け has zero hits anywhere. No shipped paper drew this orthography entry. `pools.json`, this spec and this paper's ledger row were edited together, so draw provenance still resolves. The context_words entry 引き分け (drawn by 20260817_3) is a separate category and is unchanged.
- **kanji_reading 御手洗い(おてあらい): deleted.** No shipped paper drew it (rule: an entry no shipped paper drew is deleted outright). Reason: reroll 1 above.
- **kanji_reading 複製(ふくせい): left in the pool**, pending a look at the Soumatome 漢字 page for 複 (no text layer, no index).
- **usage 懸念 and context_words 懸念: both deleted** after the QA-round-1 F1 reroll (`usage:1`, seed 71464738, 懸念 → 儲かる). Band evidence: 0 hits in the Shin Kanzen, Soumatome and Hajimete extracts and in all 31 official booklets; 懸 appears only inside 一生懸命 (qa-report-20260928_2 F1). No shipped paper drew either entry.
