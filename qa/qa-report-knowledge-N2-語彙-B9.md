# QA report: knowledge/N2 語彙, batch 9 (76 words, Hajimete No.76–158; 14 → 17 live back-links; 10 → 11 ja live gloss fixes)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. Both panes were written by Claude authors
working separately. 漢字 B7 and 語彙 B8 were merged live before this review, and every fix and back-link below was diffed
against that CURRENT live text. Files are in the coordinator's scratch `batches/`. The pre-review copies are in
`scratchpad/QAV9_bak/`, and `QAV9_patch.py` rebuilds every fix from them (it always starts from the backup). No live file was
edited directly. sha1 values are the first 12 characters, pre-review → post-fix:

| file | pre | post |
|---|---|---|
| `語彙_B9.json` | 069855278318 | 90a8b6923db4 |
| `語彙_B9.ja.json` | e68029080e77 | 685f4b5ced94 |
| `語彙_B9.vi.json` | 1bd6c655b854 | 002f7a3c12cd |
| `語彙_B9.backlinks.json` | 6bf4a116719a | b5ac2ea84ea9 |
| `語彙_B9.backlinks.vi.json` | 135ce6bc36c8 | 6c6711c041e4 |
| `V9_live_meaning_fix.json` | a0bd85954201 | e512cdca3012 |

## Verdict

`QA: FAIL → fixed (7 finding classes: 5 example scene/claim copies, 8 unlinked near-synonym pairs, 2 gloss lures (1 of them live), 2 vi glosses that mirror a 文法 card, 4 unsourced or overreaching prose claims, 9 vi usage lines that rebuild a Hajimete or official sentence, 1 official-numbering ambiguity in a source note). 0 content findings are open after the fixes.`

**No id, headword, reading, page or official count in the batch is wrong.** There is one doubtful `pos`. Hajimete marks
ばかにする 慣 (慣用句). The card keeps 動詞, because the category has no 慣用句 pos and 他動詞 describes how it is used.

**Validation.** `QAV9_gate.py` copies `.agents/` and the CURRENT live `knowledge/` into `scratchpad/QAV9_root`. It applies
`V9_live_meaning_fix.json` and then runs `merge_batch.py`'s own code (REPO set to the scratch root) for 語彙 B9. That merges the
batch, applies both back-link files and checks book order. It then builds `語彙.html` and runs
`check_knowledge.check_category`. Result: **17 of 17 ok, 0 FAIL, 0 WARN**: 554 entries, 997 generated items, 17 live entries
back-linked, cards in book order, and **no `REVIEW` line in either pane**. The first post-fix run failed two bands
(ばらす ja compare 101/100, 勘違い vi compare 185/180). I trimmed both without dropping a quoted form and re-ran.

## 1. Range, ids, headwords, readings, group

- **No.76–158 are all cards.** I opened Hajimete PDF pp.22–38. The 76 B9 cards plus the 7 live cards (92 105 107 108 111 151
  157) cover the range exactly.
- **Page map.** 76–82 → 22, 83–88 → 23, 89–95 → 24, 96–102 → 25, 26 is これも覚えよう③, 103–110 → 27 (= 28, a duplicate scan),
  111–119 → 29, 120–127 → 30, 128–131 → 31, 32 is これも覚えよう④, 33 is the 第2章 title page, 132–138 → 34, 139–146 → 35,
  147–153 → 36 (= 37), 154–158 → 38. Every cited `page` matches this map, including the ＋ words うらみ (31) and 一軒家 (35).
- **Groups.** The page section titles are Section 4 恋人, Section 5 関係悪化 and 第2章 Section 1 住まい. All 76 labels match.
- **Readings and headwords.** Every one is as printed. Hajimete's 「［お］互い［に］」 is the card お互い (名詞・副詞).
- **ナ形容詞 headwords (B10 author's flag).** B9 already follows the live convention. The `word` fields are ささい and いやみ,
  without な. 「ささいな」 and 「いやみ〈な〉」 appear only in source notes, as the book prints them.
- **Furigana.** I read all 586 distinct ruby pairs. Every kanji in examples and ja prose is rubied, and none is wrong. Checked
  in context: 一人住《ず》まい, 合《ごう》コン, 我《わ》が家《や》, 六十歳《ろくじゅっさい》, 行《ゆ》く先, 者《もの》, 落ち着《つ》かない.

## 2. official_count, hit by hit (rule 35)

`QAV9_find2.py` printed every parsed 問題1–6 item holding each form (`QAV9_find2.txt`). The 12/2010 booklet does not parse,
so I read its 問題1–6 by hand. It has no B9 hit.

- **The four counted words are right.**
  - **うつむく 3.** The underlined word in 12/2011 5-26, 12/2018 5-22 and 12/2023 5-25. The key is 「下を向いて」 each time.
  - **ささやく 1.** The 12/2015 5-26 underlined word; the key is 「小声で」.
  - **誓う 1.** The 7/2025 4-14 key.
  - **点検 1.** The 12/2018 item-15 key.
- Both nuances' quoted distractor lists match the booklet lines.
- **Excluded hits, confirmed on the booklet line.**
  - Official distractors: 視線 (12/2011 4-20), アプローチ (7/2010 4-17), 決意 (7/2023 4-14), 避けて (12/2022 2-8),
    さぐった (7/2017 1-4), うらんで (7/2019 1-1), 停止 (12/2011 4-16), ぞっとした (7/2021 5-21), にらむ (12/2019 4-19),
    ゆるす (7/2024 4-14) and とうとう許された (7/2018 5-26).
  - Stems only: 黙って (12/2018 5-22), 決意を (7/2021 4-20) and 互い (12/2023 4-20).
  - 問題6 lines of other words: 点検 (7/2014 6-30, 7/2017 6-30, 12/2023 6-26), 奥 (12/2016 6-30), 手前 (12/2019 6-30),
    お互い (12/2014 6-32), 互いに (12/2012 6-28), 同士 (7/2025 6-29) and 防犯 (7/2016 6-29).
- **Rule 35, part 1.** No live `sources` note credits a B9 form. The only substring hits are 思いがけない, 相互 and ふさぐ,
  which are other words.

## 3. Author doubts

| doubt | verdict |
|---|---|
| 1 あいつ | **Kept.** It is numbered headword No.130 on PDF 31. The register claim (目下の人やとても親しい人) is on the page, in the 👉 note: EN "used when you are in a superior position … or very familiar", ZH 看低对方或者是和对方非常亲近时使用. The ja usage line also said 「話し言葉で使う」, which no page says ("informal" ≠ spoken). It is cut. |
| 2 点検 「問題4 文脈」 | **The tag is kept; the note is fixed.** The 12/2018 PDF (p.2) prints items 11–15 under 問題3. Items 14 and 15 are （　） context items (スペース…, 参観/検診/観測/点検), and that sitting's 問題4 has only items 16–20. The note now says 「12/2018 問題3-15 の正解（この回の冊子は（　）に入れる語を選ぶ文脈の問題を問題3の14・15番に置いている。「問題4 文脈」の型として扱う）」. 「問題3 語形成」 would be false. |
| 3 ばらす / 言いつける | **Linked** both ways, with a back-link. ばらす① 「人に知られたくないことを、ほかの人に話す」 and 言いつける 「人のよくない行いを、親や先生などに知らせる」 are both 動詞 and share no kanji, so the generator can pair them. B9's own example 「弟がうっかり母にばらしてしまった」 shows the overlap. |
| 4 勘違い / 誤る | **Linked** both ways, with a back-link. Neither shares a kanji with the other, and the vi glosses both say "nhầm … phán đoán". |
| 5 合コン 「男女が集まって」 | **The ja is kept; the vi is narrowed.** The word sits in Section 4 恋人, whose example is 「二人は合コンで知り合ったそうだ」. With the VI gloss "tiệc gặp mặt làm quen" and the ＋ word コンパ, that supports a men-and-women mixer. The vi "giữa một nhóm nam và một nhóm nữ" added groups and is now "Tiệc gặp mặt để nam nữ làm quen với nhau". The vi usage's 「Từ gốc: コンパ」 was an etymology claim with no page; it is now "Liên quan". |
| 6 もしかすると / おそらく | **Linked**, with a back-link. SK 語彙 PDF 138 (推量) prints ② もしかすると〜かもしれない and ③ 恐らく〜だろう／と思う／に違いない. Both compares rest on that contrast. |
| 6 避ける / そらす | **Linked.** Hajimete prints the same VI gloss for both, "lảng tránh". |
| 6 一戸建て / マイホーム / 家屋 | **Linked:** 家屋↔一戸建て and 家屋↔マイホーム. 家屋's gloss 「人が住むための建物」 is a superset of the other two, so it is defensible on either one's meaning item. 一戸建て↔マイホーム is **declined**: the glosses name different properties (structure, ownership). |
| 6 同士 / お互い | **Linked.** Hajimete's EN gloss for both is "each other", and both vi glosses say "với nhau / nhau". |
| 7 いやみ ex2 | **Kept.** The ナ形 gloss on PDF 27 includes ZH 令人不愉快的 (unpleasant to others), and the ja meaning names 態度. |
| 8 許す "hứa" | **Kept.** 許's Hán Việt is "hứa". The note does not contradict Hajimete's VI "tha thứ, cho phép" (rule 35). "hứa" (promise) is itself a Vietnamese word with another meaning (rule 34). |

**Coordinator item 2.** The ばかにする gloss 「…軽く扱う」 printed 扱, the kanji of B10's new 動詞 扱う. It is now
「相手を自分より下の者とみなして、軽く見る。」. Its own compare, けなす's compare and the からかう back-link were aligned to the
same wording. The two pairs left for after B9 goes live (スペース↔空間, 返済↔ローン) are not in the batch.

## 4. Examples: frame, scene and claim (rules 21, 35, 39)

`QAV9_frame.py` sets every example beside every sentence sharing 2+ content tokens with it. The corpus covered:

- all refs extracts and tests/imported-*;
- every `knowledge/N2/*.json`, with 文法 stems;
- every open batch, 語彙_B10 and 漢字_B8 included.

I also compared every example with its Hajimete page example and with the 問題6 lines of §2. The 10-char window scan
(`QAV9_prov.py`) found only the convention of quoting official options in nuance fields, plus one vi prose hit (P1).

| # | entry | finding | fix |
|---|---|---|---|
| E1 | お互い ex2 「試合が終わると、両チームの選手はお互いに握手をした」 | The 文法 stem 「試合の開始（　）、両チームの選手が並んで記念撮影をした」 has the same scene (both teams' players, a joint act at the match). | → 「引っ越した友達とは、今もお互いに写真を送り合っている。」 |
| E2 | 示す ex2 「地図の赤い線は、駅から会場までの道を示している」 | The 文法 example 「会場までの道は、こちらの地図をご覧ください」 has the same scene (a map, the way to the venue). | → 「この標識は、ここから先は自転車で通れないことを示している。」 |
| E3 | 許す ex2 「この公園では、決められた場所のほかでバーベキューをすることは許されていない」 | 7/2015 問題14 is a park barbecue notice with a rules section: the same scene. | → 「この島では、観光客が車を持ち込むことは許されていない。」 |
| E4 | 決まり ex 「クラスで話し合って、掃除当番の決まりを作った」 | This is the claim of the 7/2017 問題11-60 key: 「クラスの問題について話し合い、必要なルールを決めること」. | → 「小学生の息子は、ゲームは一日一時間という家の決まりをきちんと守っている。」 It keeps the gloss's 「みんなが守るように」; a self-made rule was rejected because it would contradict the gloss. |
| E5 | 物音 ex 「誰もいないはずの二階から物音が聞こえて…」 | Live 怪しい's 「夜中に、隣の空き家から怪しい物音が聞こえた」 has the same frame (noise from a place where nobody should be). | → 「台所で大きな物音がしたので行ってみると、棚から鍋が落ちていた。」 |

The vi example_notes of all five were rewritten from the Japanese. Every other note is faithful. I scanned each replacement
over the same corpus; the only hits are the generic 「お互いに〜合う」 pattern.

**Checked without change.** In each case the scene or the predicate differs, and the word forces the setting.

| example | compared with | why it stays |
|---|---|---|
| 花嫁 (entering with her father) | live 衣装 (a bride changing kimono) | different event |
| 間取り 「狭いが…気に入っている」 | 12/2016 script 「この間取りと設備でこの家賃、言うことなし」 | different frame |
| 今さら (タグ, too late to return) | 文法 stem (タグ kept on for a trip) | different claim |
| 決意 「〜しようと決意した」 | SK 語彙's 医学 sentence | canonical frame; different scene |
| 点検 (消防署, 火災報知器) | the elevator scenes in Hajimete, 12/2018 and 12/2023 6-26 | different scene |
| 停止 (ベルトコンベア) | Hajimete's elevator | different scene |
| 奥, 手前 | the 12/2016 and 12/2019 問題6 misuse lines | no right word was restored |

## 5. Generated quizzes and glosses (rules 28, 34, 40)

`QAV9_dump.py` dumped all 997 items before the fixes (`QAV9_quiz.txt`) and after them (`QAV9_quiz2.txt`). I read all 52 B9
reading items and all 241 meaning items that involve a B9 word, in both languages (`QAV9_mqja.txt`, `QAV9_mqvi.txt`). The
pairings that exist today hold no second answer. Three scans looked for lures the generator could still draw:

- `QAV9_lure2.py`: every B9 headword's kanji, stem and kana form, against every live ja gloss;
- `QAV9_glosshw.py`: shared gloss words, both panes;
- a vi key-head containment scan.

| gloss | lure | fix |
|---|---|---|
| B9 ばかにする 「…軽く扱う」 | 扱 of B10 扱う (動詞) | 「相手を自分より下の者とみなして、軽く見る。」 |
| live 乱れる 「…崩れて、ばらばらになる」 | the kana ばら of B9 ばらす; both are 動詞 | 「…崩れて、整わなくなる。」 (fits 息が乱れる and 列が乱れた). Added to the fix file, now **11** entries. |
| B9 敷金 「…持ち主に預けておくお金」 | 主 (飼い主, same pos; B8 fixed 大家 for the same kanji) | 「部屋を借りるときに、前もって預けておくお金。」 |

- **The author's 10 live fixes, against the live text.** All are correct, and each removes a B9 form:
  - お互い: 交わす, 競う;
  - どうし: ニックネーム, 打ち合わせ;
  - きまり: しつけ;
  - 探: 求人, 刑事;
  - 許: 憎い, 憎む;
  - 屋根: 柱.
- **The fixes bring in no new lure.** 刑事's 「捕まえる」, 憎い's 「がまん」 and 柱's 「建物の上の部分」 add no headword. 憎む's
  思 was already in the old text.
- **Left as residual.** All are cross-pos or a different sense:
  - live 柱 vi "đỡ mái nhà" (not 屋根's whole key text);
  - いやみ against 苦情's 「いやなこと」;
  - 一戸建て against 特定 ("riêng biệt");
  - 点検 against 装置 ("thiết bị").

## 6. Prose

- **Rule 39: the 語彙 cards whose word also has a 文法 card.**
  - **むしろ.** The vi gloss "Thà… còn hơn; so ra thì…" nearly repeated g-adv-mushiro's "Đúng hơn là…, thà… còn hơn (so ra
    thì B hơn A)". It is now "Nếu phải chọn giữa hai bên thì nghiêng về bên sau".
  - **せい.** The vi gloss "Tại, do (nguyên nhân gây ra kết quả xấu)" repeated half of g-okageda's. It is now "Nguyên nhân của
    chuyện không hay; lỗi, trách nhiệm", the nominal sense of the ja gloss.
- **Unsourced claims (rules 9, 27).**
  - 見つめる compare: 「気持ちに関係なく」 is cut; the compare now restates the gloss.
  - あいつ usage: 「話し言葉で」 is cut (§3).
  - 誓う vi gloss: "(trước mọi người)" restricted the sense to an audience, which only the examples have. It is now "…sẽ làm
    (hay không làm) điều gì".
  - 合コン vi: see §3.
- **Sense attestation.** つり合う ex 「収入につり合わない高い車」 uses the "commensurate" sense. It now cites the 12/2014 読解
  note 「見合う：釣り合う」 (「その大きい夢に見合うだけの大きい人間」). Every other sense is on its cited Hajimete or SK page.
- **P1: vi usage lines that rebuilt a source sentence (rule 32; the B8 同期 precedent).** Each was replaced with a
  collocation the ja pane already uses:
  - 「似合いのカップル」 → 「若いカップル」;
  - 「他人のような態度」 → 「他人のこと」;
  - 「ふるさとの我が家」 → 「我が家に帰る」;
  - 「空間を広く見せる」 → 「空間を生かす」;
  - 「敷金が必要だ」 → 「敷金を払う」;
  - 「青い屋根」 → 「赤い屋根の家」;
  - 「木の温もり」「温もりが感じられる」, which together rebuilt Hajimete's whole sentence → 「手の温もり」;
  - 「エレベーターが停止する」 (in 停止 and in the 中断 back-link) → 「機械が停止する」;
  - 「手前に引く」, Hajimete's sentence and the right word restored into the 12/2019 6-30 misuse, → 「手前に置く」 and 「棚の手前」;
  - つり合う compare 「リーダーにふさわしい」, a 12/2010 6-31 key-sentence window, → 「〜にふさわしい人」.
- **The vi pane is not a translation.** Its Hán Việt notes and ①/② structures are its own. No Japanese stands outside 「」
  except the label ナ形容詞, and no prose names a source or a sitting date.

## 7. Back-links (rule 28)

- **The authors' 14 back-links.** I compared each with the current live compare, quote by quote, in both panes. Nothing is
  lost. The live 分解 vi text carried a garbled sentence, "Đề đọc từng gài 「ぶんかい」 cho 「分析」". The back-link
  rewrites it as "Đề từng gài cách đọc …".
- **QA adds 3 back-links:**
  - おそらく (v-o-osoraku), ← もしかすると;
  - 誤る (v-1213), ← 勘違い;
  - 言いつける (v-0010), ← ばらす.

  Each has a complete ja and vi compare that keeps every old quoted form.
- **Batch-internal links.** 避ける↔そらす, 同士↔お互い, 家屋↔一戸建て and 家屋↔マイホーム are within the batch and need no
  back-link. Each has compares in both panes.
- Both files now hold **17** targets.

## Root causes

| finding | let through by | proposed rule |
|---|---|---|
| E1, E2, E5 (knowledge-module scenes) | The module holds ~1,600 example/stem sentences, and the author's scan compared nouns, not scenes. The 文法 stems were outside the 語彙 author's view. | **Gate:** WARN when an example shares 3+ content tokens with any knowledge sentence (`QAV9_frame.py` prototype). B8 proposed this too, and B9 shows it again. |
| E3, E4 (official 読解 claims) | 問題11/14 passages and their keys were not read as claims. A key option (7/2017 60-4) is a claim too. | **LEX brief:** *grep each example's scene nouns over every 問題10–14 passage AND its four options; a key option is the passage's claim.* |
| 8 unlinked pairs | The authors linked within sections. Hajimete's identical EN/VI glosses across sections ("each other", "lảng tránh", "excuse") were not compared, and nobody checked superset glosses (家屋). | **LEX brief:** *list every pair whose Hajimete EN or VI gloss is identical, and every gloss that names a superset of another same-pos entry; link or justify each one.* |
| ばかにする 扱, 乱れる ばら | Rule 40's gloss check runs against merged headwords only. B10's headwords were open but not yet merged. The live-gloss grep used kanji, not new kana stems. | **LEX brief:** *run the gloss-headword check against the open next batch's headwords as well, and against each new kana headword's first two morae.* |
| むしろ, せい vi (rule 39) | The vi author never saw the 文法 cards' vi glosses, because rule 39 names scenes and gloss but the brief lists only examples. | **VI brief:** *for a word with a 文法 card, read that card's vi meaning first and write a gloss that shares no clause with it.* |
| P1 (vi usage rebuilding a source sentence) | The B8 同期 lesson was recorded in the B8 report but in no brief. | **VI brief:** *a usage collocation never reproduces the predicate of the Hajimete example or an official key sentence; prefer the ja pane's collocations.* |
| 点検 numbering | Some booklets (12/2018) print 文脈 items under 問題3. key.md copies the booklet numbering. | **N2.md:** note that 12/2018 問題3 holds 文脈 items at 14–15; cite the booklet number and tag the type. |
| 見つめる, あいつ, 誓う vi claims | Rule 9 was applied to compare/nuance, not to usage lines or to parentheticals in a gloss. | Existing rule 9; the brief should say *usage lines and gloss parentheticals too*. |

## For the coordinator — merge steps

1. No live file was changed by QA. `git status` is clean.
2. Apply `V9_live_meaning_fix.json` to `knowledge/N2/語彙.ja.json` (as `meaning`). It now holds **11** entries: the authors'
   10 plus 乱れる (v-0465). There is no vi fix file.
3. Run `merge_batch.py 語彙 9`. It merges 76 entries and applies **17** back-links in both panes. It prints no `REVIEW` line.
4. Run `make knowledge`, then `make drill LEVEL=N2`, then `make check`.
5. After merge, link スペース↔空間 and 返済↔ローン from B10, as the coordinator already planned.
