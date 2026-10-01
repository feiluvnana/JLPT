# QA report: knowledge/N2 語彙, batch 7 (50 words, 96 examples, 19 → 22 live back-links, 10 → 12 live gloss fixes)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. Both panes were written by Claude authors
working separately. The files are in the coordinator's scratch `batches/`. The pre-review copies are in
`scratchpad/QAV7_bak/`. `QAV7_patch.py` rebuilds every batch fix from those copies, and `QAV7_livepatch.py <dir>` applies
the two live-entry fixes. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B7.json` | d53c086c28f6 | 6796cd4a72fe |
| `語彙_B7.ja.json` | 6c7312249521 | 01e5c276e3e8 |
| `語彙_B7.vi.json` | ac1de1a6c001 | 131b36eebd02 |
| `語彙_B7.backlinks.json` | 17252798662d | f896b0a3e0c9 |
| `語彙_B7.backlinks.vi.json` | 407dfd0f1059 | 2657b429a210 |
| `V7_live_meaning_fix.json` | d7cff9a98863 | 2ee726f81dbc |
| `V7vi_live_meaning_fix.json` | e47ab43b319f | 138c95d460d1 |

## Verdict

`QA: FAIL → fixed (6 finding classes: 5 examples, 2 live-entry defects, 3 unsourced senses, 10 gloss lures, 3 unlinked look-alike pairs, 3 prose fields). 0 content findings are open after the fixes.`

**No reading, Hajimete number or official count in the batch is wrong.** The one wrong count was live 頼る (known issue 2).

**Validation.** `QAV7_gate.py` copies `.agents/` and `knowledge/` into `scratchpad/QAV7_root`. It applies both live fix
files and `QAV7_livepatch.py`, then runs `merge_batch.py`'s own code (REPO set to the scratch root) for 語彙 B7. That
code merges the batch, applies both back-link files and checks book order. The script then builds `語彙.html` and runs
`check_knowledge.check_category`. The result is **17 of 17 ok, 0 FAIL, 0 WARN**: 416 entries, 760 generated items (344
reading and 416 meaning), 22 live entries back-linked, cards in book order, and **no `REVIEW` line in either pane**. A
script also checked every back-link against the current live compare, quote by quote, in both panes. None drops a quoted
form, and every one is within the band (the largest is ja 99 of 100 and vi 178 of 180).

**Live files.** I applied `QAV7_livepatch.py` to the real `knowledge/N2/語彙*.json` (頼る and 容姿 only) and ran
`make knowledge`. On the first run, `make check` printed "All checks passed (239 skipped), 225 warning(s)". The one
extra warning against B6's 224 is the expected drill staleness (`make drill LEVEL=N2` after the merge). A second run
showed 漢字.html and index.html as stale. My edits touched no 漢字 file and git shows none changed, so another context
was writing 漢字 at the same time. I did not touch it. Nothing is committed.

## Known issues from the coordinator

1. **Back-link count.** At review time both files had **19** targets, and they matched the shared `related` lists
   exactly. A script compared every live id named in a B7 `related` with each file's keys, and the two sets were equal.
   No extra id remained to find; the 18 count predates the vi author's last write (13:02). QA adds three targets, 返品,
   略す and 相当 (§4), each with a complete ja and vi compare, so both files now hold **22**.
2. **頼る (v-0033), live.** official_count 1 → **0**. The 12/2010 source note is now 「12/2010 問題2-7：「頼り」が正解の表記問題（「たよりになる」）。名詞「頼り」の項目で数えるので、official_count には数えない」.
   The 問題2 表記 tag is dropped. The card's examples (頼らず, 頼りすぎて) and prose still fit.
3. **The ja author's doubts.**
   - **針's sewing sense.** It is sourced after all. SK 漢字 PDF 86 (第39回 IV⑩) prints 「針で指を刺してしまった。」, and
     that page is now cited. The same check showed that **ex2 「洋服のすそを縫っていたら、針で指を刺してしまった」 is that
     drill sentence with a clause added**, so it is replaced (E1).
   - **さっぱり ex2.** A copy of the frame. The 12/2011 4-21 key is 「シャワーを浴びたら、体も気分も（さっぱり）した」, and ex2
     was sweat → change shirt → たらさっぱりした. My first replacement (a haircut) was the scene of a 文法 example,
     「半年ぶりに髪を切ったら、頭がずいぶん軽くなった」, so I discarded it (E3).
   - **鈍い nuance.** Kept. The three misuses and the key 「動きが鈍い」 are quoted correctly. SK PDF 108 lists
     ②［感覚、勘、運動神経］ ③［光、音］ ④［反応、動作］ and 「頭の回転が鈍い」, and the nuance's 「計算や仕事の速さ」 does
     not contradict any of them.
   - **Possible links.** 比較的–相当: **linked**, because the vi glosses both read "khá" and both are 副詞 (§4).
     交渉–打ち合わせ/討論: declined. 交渉's vi "Đàm phán, thương lượng" shares no gloss word with them, and neither gloss
     reads as negotiation. 迷う–焦る: declined. They are each other's official reading distractors (12/2021 1-4, 12/2024
     1-2), not near-synonyms, and both nuances already name the item.
4. **The vi author's doubts.**
   - **取れる/外れる, 含む/含める, 比較的/わりと.** Kept. Each side restates its own card's sourced gloss: Hajimete p.153
     and 280 for 取れる, ↔当たる for 外れる, 「消費税を含む」 for 含む, and every archive 含める (7/2015 1-2 and the scripts'
     「〜を含めて」) is someone counting something in. None is a pragmatic claim.
   - **映る 「ニュースに映る」.** Weakly sourced, and the example's scene was a copy. 映る ex1 (shop staff on the news) is the
     7/2017 script (a TV crew at a cake shop: 「お店のスタッフの方も映りますけど」), so it is replaced (E2). The screen sense is
     now cited to the 12/2023 script line 「今テレビに映ってるアナウンサー」. The vi usage now says 「テレビに映る」.
   - **縮める 「記録を縮める」.** Kept. Hajimete p.215 glosses 縮める 缩短/缩小 and prints 縮まる 「命が縮まった」, so the time
     sense has a page.
   - **返却/返品.** **Linked** both ways (§4).
   - **Live 容姿 ex1** 「人を容姿だけで判断してはいけない」 is the 7/2010 6-32 key 「人を外見で判断するのはよくないことだ」 with
     the word swapped. It is replaced in the live file by 「祖母は若いころ、容姿のよさで近所でも評判だったそうだ。」. The
     usage collocation 「容姿で判断する」 (the same frame) is out of both panes, and the vi note is new.
5. **Live fixes against their own cards (rule 35).** All 9 ja fixes fit their cards' examples. ふきん is covered by
   「タオルなど」, and 映画の撮影 by 「ビデオ」. **苦情 is re-fixed.** The author's 「いやな思い」 brought in 思, which is
   the kanji of 思いつく, 思いがけず and 思いがけない. It is now 「受けたいやなことや不満を…」. 極端's 違 (違反) is
   cross-pos and kept. The vi fix to はきはき is right: SK PDF 150 prints きっぱり ⑧ next to はきはき ⑨. **Added: live
   尊重 vi** "(ý kiến, cá tính, truyền thống)" held 伝統's whole vi key "Truyền thống" (both are 名詞). It is now
   "Tôn trọng, coi trọng như điều có giá trị (ý kiến, cá tính)", which fits both examples.

## 1. Readings, ids, official counts

- **Readings and numbers.** I checked all 50 by hand. 41 readings are confirmed by an official 問題1 key or 問題2 kana stem
  in `booklet.md`, and the other 9 are standard (やしなう, あまやかす, いいわけ, ざんだか, こつこつ, しょほ, ちょくぜん,
  おーばー, おちこむ). All 18 `v-NNNN` ids match the Hajimete index (5, 36, 107, 108, 167, 174, 335, 438, 444, 538, 569,
  827, 902, 1161, 1237, 1255, 1307, 1379). The index prints the 22 Hajimete ＋/同義 sub-words (甘やかす 7, 含める 167,
  映る 1161, 縮む/縮める 1181, …) under their parent's number, so `v-o-*` is right for them. 返却, 迷う, 逃亡, 途端,
  重大, 針, 鈍い, 鋭い, 防災, 隣 and 願望 have no Hajimete number. No reading distractor is a valid reading of its
  headword.
- **official_count, hit by hit (rule 35).** `QAV7_find.py` printed every parsed 問題1–6 item holding each form
  (`QAV7_find.txt`), and I grepped the merged 12/2010 booklet by hand (頼り 2-7, 隣 1-5, 保つ 6-32, 含まれて 4-22). All
  50 counts are right, including 記憶 2 (7/2022 1-1, 12/2017 5-23), 縮む 2 (7/2014 6-32, 7/2011 5-25) and 鋭い 2 (7/2024
  6-27, 7/2015 4-20). Every excluded hit is confirmed on its booklet line. They include distractors only (ふくめて 7/2013
  1-3, 映して 12/2023 4-19, 鈍感 7/2019 4-16, 隣 7/2018 3-12), stems only (改善 7/2022 4-14, 迷っている 7/2025 5-22,
  逃亡 12/2025 2-10, とたん 12/2012 2-8) and other words (補足, 縮小, 文法 7/2010 6-41 「水面に映して」).
- **Rule 35, part 1.** I intersected every item cited by B7 with every item cited by a live card. There are 26 shared
  items. Only 頼る/頼り was miscredited. 計画/プラン, オーバー/大げさ and 重大/深刻 share their 問題5 items under the live
  convention (underlined word plus key).

## 2. Examples

The 10-char scan (`QAV7_prov.py`) found only quoted official misuse fragments in nuance fields, which is the existing
convention. The frame table (`QAV7_table.txt`) sets each example beside every refs line holding the word (Hajimete,
SK/Soumatome, all booklets and scripts, External, KanzenMoshi) and every knowledge card and open batch (語彙_B8,
漢字_B6/B7 included). I read every pair that shares 2 or more tokens. I grepped each replacement's scene over the same
corpus.

| # | entry | finding | fix |
|---|---|---|---|
| E1 | 針 ex2 | SK 漢字 PDF 86 drill sentence 「針で指を刺してしまった」 with a clause added. | → 「体重計に乗ると、針が思っていたより右のほうまで動いた。」 (the 数字を指す部分 sense) |
| E2 | 映る ex1 | The 7/2017 script frame (TV, shop staff appear). I rejected zoo, marathon and soccer-broadcast scenes, which are in scripts or 読解. | → 「父が撮った運動会のビデオには、転んで泣いている幼い私も映っていた。」 |
| E3 | さっぱり ex2 | The 12/2011 4-21 key frame. The haircut alternative is a 文法 example. | → 「歯医者で歯をきれいにしてもらうと、口の中がさっぱりする。」 |
| E4 | 含める ex1 | 「…も含めて、全部で二時間」 has the frame of live 総額 「家具も含めて総額で…」 and of its own ex2. | → 「駅まで歩く時間を含めると、会社まで一時間近くかかる。」 (the usage's 〜を含めると) |
| E5 | 作成 ex1 | 「〜を作成しておいた」 echoes the 12/2015 6-28 key 「資料を作成しておいてください」. | → 「…チェック表を作成して、かばんのポケットに入れた。」 |
| E6 | live 容姿 ex1 | Copy of the frame of 外見's official key (known issue 4). | Replaced in the live file. |

- **Checked without change.** 後悔 ex1 「〜たことを…後悔していた」 against the 12/2023 4-15 key: it is the canonical frame,
  the scene differs, and the act is a positive one (selling a house, not failing to apologise). 迷う ex2 (lost in a
  forest) against the 文法 霧の日 stem: the predicate and claim differ. 打ち明ける ex1 against Hajimete and the official
  key: the diary scene differs. 固める ex2 「方針を固めた」 against SK PDF 185 「砂糖が固まって…」［方針］: SK's sentence is
  not reproduced. 補う ex2 (a nap) has no claim match in any 読解 or script. 途端 ex2 has no scene match.
- **Sources added.** 外見's "things" sense (ex2 りんご) had no page; it now cites the 7/2019 script 「（車の）外見も中も」.
  針 cites SK 漢字 PDF 86. 映る cites the 12/2023 script.

## 3. Generated quizzes (rules 28, 34, 40)

`QAV7_dump.py` dumped all 760 items before the fixes (`QAV7_quiz.txt`) and after them (`QAV7_quiz2.txt`). I read all 159
meaning items that involve B7 (`QAV7_mq.txt`). **No current distractor glosses its key.** The gloss checks
(`QAV7_glosshw.py` plus a key-text containment scan and a same-pos kana-phrase scan, both languages) found lures for
pairings the generator can draw:

| gloss | lure | fix |
|---|---|---|
| 布 「…服などの材料になるもの」 | 素材's gloss is 「材料」 (same pos); 織 is the kanji of 組織 | 「糸から作った、服やカーテンなどにするもの。」 |
| 支持 「…に賛成して…」 | puts 賛 on 賛否's quiz | 「ある人や考えをよいと認めて、後ろから支えること。」 |
| 重大 「…大切で…」 | 貴重 / 粗末 (same pos) | 「そのことの影響がとても大きく、ふつうでは済まない様子。」 |
| 鋭い 「…細かいところまで届く」 | 詳しい's 「細かいところまで」 (same pos) | 「…感覚や見方がすぐれている。」 (SK PDF 108 ②④) |
| 途端 「ちょうどその時…」 | たまたま's 「ちょうどその時」 | 「あることが起こった、まさにその瞬間。また、そのすぐあと。」 |
| きっぱり 「態度をはっきりと…」 | はきはき's 「はっきり」 (same pos, the SK ⑧⑨ pair) | 「少しもためらわずに、自分の態度を決める様子。」 |
| vi 重大 "thiệt hại" | 損害's key | "…(lỗi lầm, tổn thất, sự việc)" |
| vi 保つ "bình tĩnh" | 冷静's key | "…sự điềm tĩnh…" |
| live 尊重 vi / live 苦情 ja | §Known issue 5 | in the fix files |

- **Left as residual.** All are cross-pos with a different main sense. きっぱり "dứt khoát" appears in 拒否 (名詞) and
  あいまい ("không dứt khoát"), 保つ "duy trì" in 継続 (名詞), and 極端 「違」 in 違反. 直前/途端 share
  「あることが起こ…」, but the pair is just before / just after, an opposition, not a second answer.

## 4. Links and back-links

| pair | why | done |
|---|---|---|
| 返却 ↔ 返品 (live v-0215) | Same kanji; the vi glosses share "trả lại". | `related` both ways; new compares; back-link |
| 縮める ↔ 略す (live v-o-ryakusu) | 12/2025 2-6 puts 縮して beside 略して; vi "thu gọn" / "cắt ngắn" read alike. | `related` both ways; 縮める compare rewritten; back-link keeps 「省略」「省略する」 |
| 比較的 ↔ 相当 (live v-o-soutou) | Both 副詞; vi "Tương đối, khá" / "Khá, rất". | `related` both ways; compares keep わりと and every old quote |

I compared all 22 back-links, old compare against new, in both panes. Every old quoted form survives.

## 5. Prose

- **ja.** 支持 nuance: 「応援や許可、歓迎の意味では使わない」 overreached, since 支持 is backing. It now names what the item
  shows: 「試合の応援や撮影の許可、歓迎の意味では…」. 映る usage gets 「テレビ・ビデオに映る」. Every quoted official
  distractor list matches its booklet line. No prose names a source.
- **vi.** 抵抗 nuance "rồi có thể quen dần" generalised from one official stem, so it is cut. The usage lines of 針,
  映る, さっぱり and 含める are realigned to the new examples (含める's 「日程も含めて」 was the official stem). I checked
  the Hán Việt notes (dưỡng, ký ức, giao thiệp, phòng tai, lân, nguyện vọng) and the "ủng hộ" false friend, and all are
  right. No Japanese stands outside 「」 except the grammar labels する動詞 and ナ形容詞. The pane is not a translation of
  ja (its structure and Hán Việt notes are its own). Every example_note is faithful, and all 7 new ones are written from
  the Japanese.
- **Furigana.** I read all 1,156 distinct ruby pairs. No span swallows a headword plus another word. The compound rubies
  (防災訓練, 記憶力, 返却期限) are single words. 十《じゅっ》キロ, 10分《ぷん》, 話し声《ごえ》, 一人暮《ぐ》らし and
  二重《にじゅう》 are right in context.

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| 針 ex2 (SK 漢字 drill) | The author searched the 語彙 refs and `kanji_tables.md` (the 別冊 list), not the SK 漢字 lesson pages, which are not extracted. | LEX brief: *for a word that is also a 漢字 entry, open its SK 漢字 回 page (別冊 目次 → 回 → PDF) and compare every drill sentence; it is also where a missing sense is often printed.* |
| 映る ex1, 作成 ex1 (scripts / official key) | The frame was compared by nouns. A script dialogue about the same situation (a TV crew filming a shop) was not read as a scene. | Existing rules 21 and 39. Add: *for a 画面/TV sense, read every script line holding the verb.* |
| さっぱり ex2, 含める ex1, 容姿 ex1 | The official key's frame was reused with a new noun (rule 35's FRAME), and live 容姿 predates rule 35. | Gate idea: WARN when an example shares the cited official key's predicate plus ≥2 content tokens, across live cards too. |
| 頼る count, 苦情 re-fix, 尊重 vi | Rule 35's grep of live `sources` and glosses was run for headword forms, not for the kanji a FIX introduces or for vi key texts. | LEX brief: *a live gloss fix is itself grepped: no new kanji from any headword, and in vi no other entry's whole key text.* |
| 10 gloss lures | The author's dump shows today's pairings only, and rule 40's gloss-word check covers 2+ kanji words, not kana phrases (はっきり, ちょうどその時) or substring containment of a vi key. | `QAV7_glosshw.py` + the containment scan are the prototype for the proposed rule-40 gate check. |
| 3 unlinked pairs | 返品 and 略す are live cards in other chapters; the author linked within the batch's own topic. | QA-only; keep. |

## For the coordinator — merge steps

1. Live fixes not covered by the fix files are already applied to the real `knowledge/N2/語彙*.json` by
   `QAV7_livepatch.py`: 頼る (count 0, note, tag) and 容姿 (ex1, ja/vi usage, vi note). Do not re-run it; it is
   idempotent, so it would do no harm.
2. Apply `V7_live_meaning_fix.json` (9 ja meanings, 苦情 re-fixed) to `語彙.ja.json`, and
   `V7vi_live_meaning_fix.json` (はきはき, plus 尊重 added) to `語彙.vi.json`.
3. `merge_batch.py 語彙 7`. It applies **22** back-links: the authors' 19 plus 返品, 略す and 相当.
4. `make knowledge`, `make drill LEVEL=N2`, `make check`.
