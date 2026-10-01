# QA report: knowledge/N2 語彙, batch 10 (72 words, Hajimete No.159–241; 10 → 14 live back-links; 12 → 13 ja live gloss fixes)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. B9 went live (82dd8f4) after B10 was written,
so every back-link and live fix was diffed against the CURRENT live text (`batch_tool.py rebase`). The pre-review copies are in
`scratchpad/QAV10_bak/`. `scratchpad/QAV10_patch.py` rebuilds every fix from that backup. No live file was edited.
sha1 (12 chars), pre → post: `語彙_B10.json` c9b9e410de08 → 685be6bc8e84 · `.ja` db0591e61bca → 8323b925a2ac ·
`.vi` b9a75419bb80 → e640070f0cba · `.backlinks` 6e9f7cf8c120 → ae84fd8f28fb · `.backlinks.vi` cdfae789abb1 → 87ea65b3ab13 ·
`V10_live_meaning_fix.json` a90c33cafccf → ac322d701589.

## Verdict

`QA: FAIL → fixed. 6 finding classes: 4 gloss lures, 6 example frame copies, 5 unlinked near-synonym pairs, 2 overstated or unsourced senses, 1 pos, 1 source note. No content finding is open.`

**Validation.** `batch_tool.py gate 語彙 10` merges the CURRENT live tree with `V10_live_meaning_fix.json` applied, then B10 and both
back-link files. It builds the page and runs check_knowledge. Result: **0 FAIL, 0 WARN, 21 ok, 0 REVIEW** (626 entries, 14 back-links,
13 live fixes). The first post-fix run failed one band: the 相当 vi compare was 192/180. I rewrote it, keeping every quoted form.
`lures` after the fixes: 0 LURE, 0 HW, 0 READ. The 12 GW and 5 PAIR hits that remain pair different senses.

## Checked without change

- **Range.** The 72 B10 cards plus the 11 live cards (166 167 174 178 180 194 198 199 209 215 238) cover No.159–241 exactly.
- **Pages and readings.** I opened PDF pp.41, 46 and 52. Headwords, readings, numbers and pages match, including 慣 on 高くつく and
  Hajimete's ② gloss for 重ねる, "repeating something".
- **Furigana.** I read all distinct ruby pairs. None is wrong.
- **official_count, hit by hit.** I scanned every 問題1–6 line in the 31 booklets for every form and checked each against answer_keys.json.
  - 物足りない 1 (12/2013 6-32 key 1).
  - 価値 1 (12/2022 5-25 key 4).
  - 扱う 1 (7/2012 2-7 key 3).
  - スペース 1 (12/2018 3-14 key 1).
  - Not counted:
    - スペース is a wrong option in 12/2025 4-15 (key ステージ) and 7/2015 4-21 (key デザイン).
    - 渋い is a fake reading for 辛い (7/2010 1-2, 7/2025 1-2).
    - 差し引く is a distractor in 12/2017 4-21.
    - あつかう is a fake reading for 伴う (12/2016 1-4).
    - 大まか is a distractor (12/2020 4-20, 7/2024 4-18).
    - 「（ ）収入」 and 「（ ）価格」 are prefix items.
    - The remaining hits are words in a stem or a 問題6 line.
  - All other counts are 0, which is correct.
- **vi pane.** It is written, not translated. It has its own Hán Việt notes (the 実物 "thực vật" false friend is valid under rule 34) and
  its own example scenes. Every Japanese word is inside 「」.

## Findings and fixes

| # | finding | fix | root cause |
|---|---|---|---|
| G1 | 重ねる gloss and compare 「同じことを何度もする」 contained B11's headword 何度も. So did the 積む back-link. | Changed to 「同じことをくり返す」 in all three places. This is Hajimete's own ② gloss. | Rule 40's check only covers merged headwords. The B9 report's proposal ("check against the open next batch too") is not in LEX_JA_BRIEF yet. |
| G2 | 価格 「売り買いするときの値段」 contained B11's headword 売り買い. 立て替える 「あとで返して…」 contained B11's あと. | 価格 → 「品物を売るときにつける値段。」 立て替える → 「…返してもらう約束で、代わりに先に払う。」 | Same as G1. |
| G3 | 扱う 「…使ったり接したりする」 contained live 接する (same pos). `lures` missed it because the form is inflected (接し). | Gloss → 「…使ったり相手にしたりする」. Also **linked 扱う↔接する** (Hajimete ② 「立場を考えて接する」 overlaps 接する's 「相手をする」), with compares in both panes and a back-link. | The HW scan matches dictionary forms only. **Tool:** match stems (語幹) of verb headwords. |
| G4 | Live 総額 「全部を合わせた金額」 contained B10's headword 金額 (HW). | Added to the fix file: 「全部を合わせたお金の額。」 The fix file now has **13** entries. | The authors' live-gloss grep did not cover new headwords used as whole words. |
| E1 | 払い込む 「入学金は…払い込まなければならない」 is Soumatome p.121's object (入学金). The first replacement repeated 7/2013's 読解 notice (指定口座, deadline). The second shared 漢字 k-0056's 町内会費 scene. | → 「祖父は毎年、郵便局の窓口で雑誌の年間購読料を払い込んでいる。」 | Provenance covered Hajimete, not the Soumatome page cited in `sources`. |
| E2 | 出費が多かった and 好き嫌いが多く repeat Hajimete's predicates (出費が多くて, 好き嫌いが多かった). | → 出費がかさんだ, 好き嫌いが激しく. Both collocations are already in the usage lines. | The scene changed but the predicate was kept. Rule 3 needs both changed. |
| E3 | 赤字 ex2 (the teacher's red marks on a returned essay) repeats Hajimete ② (a returned report with red corrections). | → 「この資料は、部長の赤字のとおりに直してから配ってください。」 | Same as E2. |
| E4 | 生 「とれたての貝を生のまま食べる」 repeats Hajimete's scene 「この魚は新鮮なので、生で食べられる」 (fresh seafood eaten raw). | → 「このトマトは甘いので、焼かずに生のままサラダにしよう。」 | Same as E2. |
| E5 | 買い換える (moving house, old furniture) has the same scene as 文法 g-ni-atatte 「引っ越しにあたって…家具を処分した」. A スマホ replacement hit 文法 g-to-omou-to. | → 「十五年使った冷蔵庫を、電気代の安い新しいものに買い換えた。」 | Rule 35's whole-module scene check. Frames flagged it, but the authors did not act on it. |
| — | ずらり (cars in a parking lot) and the 赤字 ex1 / 高くつく / おまけ / いける / 扱う frames | **Kept.** ずらりと並ぶ is the word's only collocation, and the scene differs from Hajimete's. The others differ in scene. | — |
| L1 | スペース↔空間 (Hajimete EN "space / 空间 / không gian"). | Linked, with compares in both panes. Back-link to v-0146, whose compare was empty. | The B9 deferral, now done. |
| L2 | 返済↔ローン (ローン 「借りて少しずつ返していく」). | Linked. 返済's compare now names ローン. Back-link to v-0136. | The B9 deferral. |
| L3 | わりあい↔相当 (B7 precedent 比較的↔相当). | Linked. Back-link to v-o-soutou, whose compare was rewritten to name わりあい. That replaced the old 「わりあいに」, which used the new headword as a gloss word. | The authors linked わりと and 比較的 but not the third member of the B7 triangle. |
| S1 | ごく 「程度がこれ以上ないほど」 overstates the word (Hajimete: "very / 很、非常 / cực kỳ"). | → 「程度を強めて言う言葉。非常に。」 | Rule 27. The sense must match the page. |
| S2 | 飽きる nuance: あきらめる 「望んでいたことを途中でやめること」 is 中断's definition (the frames tool found it word for word in an imported 詳細解説). 収入 vi "(chưa trừ các chi phí)" is unsourced. | あきらめる → 「…無理だと思ってやめること」. The vi parenthetical is cut. | Rule 9 applied to compare but not to nuance lines or gloss parentheticals. The B9 report raised the same point. |
| P1 | 高くつく pos 慣用句 is used by no other card, so the generator has no same-pos pool for it. | → 動詞 / 自動詞 (B9 ばかにする precedent). The source note still says 慣用表現. | The LEX brief lists no pos value for 慣 headwords. **Brief:** state that 慣 → the pos of the head word. |
| N1 | The スペース note said 「問題3-14」 under the tag 問題4 文脈 without explaining why. | Uses the B9 点検 wording, which explains that this sitting's 文脈 items are 問題3-14/15. | The N2.md numbering note was proposed in B9 and has not been written yet. |

**Coordinator items.**
- 生 is a one-kanji headword. That is fine; 仲, 縁 and 柱 are live. Its examples all print なま.
- 器 needed no change.
- The authors' 12 live fixes are each correct against the live text. Each one removes a B10 form: 価値, 大切, 扱, 品質, 金額, 出し入れ or 税金. None of them adds a lure.

## Merge steps (coordinator)

1. Apply `V10_live_meaning_fix.json` (13 ja `meaning`s, including 総額 v-o-sougaku) to `knowledge/N2/語彙.ja.json`.
2. `batch_tool.py merge 語彙 10` (or `merge_batch.py 語彙 10`): 72 entries and **14** back-links in both panes (new targets: v-0146 空間,
   v-0136 ローン, v-o-soutou 相当, v-0069 接する).
3. `make knowledge`, `make drill LEVEL=N2`, `make check`.
4. B11 is open and was written on top of B10. Re-run its `lures` after B10 merges. The B10 glosses it flagged (価格, 重ねる) are already fixed.
