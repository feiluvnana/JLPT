# QA report — 知識 N2 漢字 batch 5 (59 kanji: 10 `k-NNNN`, 49 `kx-<kanji>`; 45→46 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes.

The shared file and the ja pane came from a Claude author. The vi pane and the vi back-links
were drafted by Gemini through agy, with no file access.

Files reviewed (scratch `batches/`):
- `漢字_B5.json`, `.ja.json`, `.vi.json`
- `.backlinks.json`, `.backlinks.vi.json`
- `K5_live_meaning_fix.json` (7 ja edits to live glosses)

The originals are kept in `QAK5_orig/`.

Validation ran on a scratch root, `QAK5_root`:
- `.agents/` and `knowledge/` were copied fresh; everything else is symlinked.
- `QAK5_run.sh` applies the live fix file to the copied `漢字.ja.json`.
- It then runs `merge_batch.py`, re-pointed as `QAK5_merge.py`.
- Last, it runs the builder and `check_knowledge.py`.

The real `knowledge/` was not edited.

## What was checked, and how

| area | method | result |
| - | - | - |
| SK numbers / `group` | SK 漢字 目次 PDF 134–139 (all six pages, 1–1046), read as images | 一 4, 帰 44, 待 188, 伝 473, 警 673, 材 724, 柔 762, 憎 833, 統 902, 判 937, all correct. Every `group` (第1回〜第14回, 第22/34/36/38/41/44/45回) matches. None of the 49 `kx-` kanji is on the 目次 |
| `on` / `kun` / `words` (k-) | SK 別冊 list pages PDF 141, 143, 153, 171, 183, 185, 187, 191, 195, 197 | 10/10 match the page. Compounds the page lacks (統一, 帰省, 招待, 伝統, 素材, 柔軟, 系統, 批判) are each an official key |
| readings (kx-) | the cited official item, Hajimete page, or Soumatome 漢字 page, one by one | All attested. ス in 素直/素晴らしい: Soumatome 漢字 PDF 151, checked. 反抗心 はんこうしん: Hajimete PDF 119. 大抵: official 7/2013 読解 text (F6). Prose rubies that gave readings the entry does not list (劣《れつ》, 伴《はん》, 納《のう》) are rewritten (F3) |
| `official_count` (rule 40) | Parser over all 問題1 sentences and 問題2 keys of 31 sittings (302 items). The 10 items it misses were read by hand. All four options of every cited item were printed | 59/59 correct. 帰 0 (帰勢/帰斉/帰省/帰成) and 伝 0 (伝授/伝承/伝統/伝達) are right: the kanji is printed in all four options. 投票 (12/2023 2-9) sits in a missed item and was confirmed by hand. Two reprints lacked 「（再掲）」 (乏 12/2021 1-2, 祉 12/2017 2-8); the live convention was added. The rule-35 cross-check is clean: all 49 live partners credit the shared items |
| prose option claims | every 「…」 option list in the ja and vi panes, checked against the printed options | All true after the fixes, including 違判 (12/2019 2-6), 激く (12/2017 2-10), 縮して (12/2025 2-6), 絞って/握って (7/2025 2-9), 伴いて (7/2012 2-6), 避けて (12/2022 2-8) |
| invented Japanese (vi) | every 「…」 in the vi pane and the vi back-links, matched against refs/, the shared file and the ja files | None invented. The 「戻品」 tail on 返 is a printed option, not an invention: 7/2021 2-7 へんぴん lists 返品 変品 逆品 戻品, and the live compare already quoted it. The only non-string was the broken 「勢i」 (F2) |
| generated quizzes | All `#r` and `#m` items touching the batch were dumped, before and after the fixes. The meaning items were dumped in both languages. Gloss-word overlap was scanned against all 319 entries (ja substrings, vi words and bigrams), as was headword kanji inside glosses | No fabricated reading is a real one: だいてい, じつし, ふんせき, ようす and あくる are words or near-words, but not readings of their compounds. Collisions: F4, F5. Duplicate reading item: F6. Rule 34 is clean |
| live fix file | 7 ja glosses (色 組 極 混 触 片 優) | Accepted. Each removed a batch-5 headword kanji (一, 徴) or 優's 「役者」, which collided with 俳. The vi glosses of the same 7 contain no kanji and no actor sense, so they need no fix |
| examples | 10-char windows and a ≥2-shared-token lister over refs/**/*.md, tests/imported-*, every `knowledge/N2/*.json` (quiz stems included), `漢字_B18.json` and `語彙_B6.json`. Every hit was read; replacements were rescanned in 5 rounds | F1 |
| furigana | every example and every changed prose field, by hand | F3. No rendaku compound (〜作り etc.) occurs |
| rule 6 / example_notes | script | clean after F2a |
| gate | scratch merge | before: **1 FAIL** (vi kx-即 unknown key `example\n_notes`). After: **0 FAIL, 0 WARN**; merge prints no REVIEW line; 59 entries; back-links on 46 live entries |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | 29 examples | major | Scene and frame copies. Four kinds: (1) 語彙 cards; (2) 文法 examples and stems; (3) live 漢字; (4) official items, including cited ones. Worst cases: 端 「家を出た途端に、かさを忘れたことに気がついた」 = 文法 g-tatotan (10-char hit) and 語彙 v-0199 (exactly the B4 F1 scene); 継 (親から子へ味を受け継ぐ) = 7/2010 2-8 「この店はでんとうの味を守り続けている」; 柔 (焼きたてのパン、ふわふわ) = 文法 g-ta-bakari; 判 (少し熱がある → 行っても大丈夫) = 文法 g-hodo-wa-nai; 劣 = cited 7/2016 1-5 frame; 鮮 (絵の具・空) = cited 12/2015 2-10; 憶 = cited 7/2022 1-1; 摘 = cited 12/2015 2-9; 籍 = Hajimete No.1293's own sentence; 析 = 7/2021 読解 (POS data); 施 = 文法 g-toitta; 援 = 語彙 v-0180; 祉 = 語彙 v-0418 / 語彙_B6 v-o-ikiiki; 剣 = 文法 g-nitsukete; 距 = 文法 g-katei + 12/2024 読解; 従 and 避 = 文法 g-towa-kagiranai; 典 = live 造 k-0831; 警 = cited 7/2018 2-9 and the 7/2012 問題8 concert-guard sentence; 践, 扱, 穫, 激, 儀 (= 7/2010 2-6 礼儀正しい), 徴 (= 7/2011 2-6), 票 (= 12/2023 2-9), 診 (= 12/2022 2-9) | 29 new sentences (待 only retimed). Rescans caught copies in my own replacements: 語彙 v-0589 twice, live 続 k-0446, 語彙 v-o-kakujuu and v-o-shindan, 7/2016 読解 「生中継」, 7/2011 「データを分析…事故の原因」, 7/2013/7/2016 「試験が近い→勉強」, 7/2018 「高熱→病院」, and a 10-char SK 語彙 window. All were replaced. vi example_notes were rewritten from each new sentence. Final scan: no window hit; no ≥2-token hit shares a frame | B4 R1 (read every ≥2-token hit, and frame not nouns) did not reach this author. The author's `K5_prov.py` listed hits but did not compare frames, and did not compare against the entry's own cited items. Rule 13's cited-item check does not reach 漢字 examples |
| F2 | vi pane (agy) | major | (a) schema break: kx-即 key `example\n_notes` (the gate's only FAIL). (b) broken furigana: 「｜柔軟《じゅうnan》」, and back-link 荒 「｜勢《いきお》i」. (c) the false friend as the gloss: 指摘 "(chỉ trích …)" is the very trap B2 F6 lists; 招待 "chiêu đãi"; 趣味 unmarked. (d) unattested senses (rule 27): 鮮 "tài nghệ điêu luyện / ký ức" (the 語彙 B1 precedent), 旬 "thời điểm tươi ngon" plus "tháng âm", 納 "tâm phục", 徴 "điềm báo", 施 "ban cấp, ban bố", 摘 "ngắt hái", 剣 "hai lưỡi", 刑 "tù đày", 抗 "bất khuất", 絞 "thắt chặt", 憶 "hoài niệm". There are also etymology and radical stories (籍 thẻ tre, 穫, 織, 憶, 剣 真剣 = real sword) and a non-note on 践 tiễn/tiễn đưa. (e) unsourced contrasts (rule 9): 柔/軟 (in the entry and in the 軟 back-link), 帰 "không dùng cho đồ vật", 乏 "không dùng cho người nghèo", 荒 "gồ ghề", 即/直, 援 and 施 "quy mô", 材料 "đã dùng". (f) compares that replaced the real shape contrast with filler: 詳↔討 "khi bàn bạc cần 討…", and 討↔詳. (g) gloss-word collisions: 討/析 "mổ xẻ", 典/儀 "chuẩn mực", 絞/握 "chặt", 抵/触 "va chạm", 援/救 "cứu trợ", 伴/付, 劣/敗 "thua". (h) garbled Vietnamese: 象 "biểu tượng trưng", 極 "chót vót", 逃 "không chạy tán loạn". (i) 縮 usage omitted 縮まる, which its own example used | ~75 vi prose fields rewritten (32 meanings, 13 usages, 21 nuances, 20 compares; this includes the vi side of F4/F5), 1 key repaired, and 8 back-link compares rewritten. The nuances now state the printed options instead of folk claims. 判 "con dấu" is KEPT: SK PDF 197 prints 判こ | No vi check reads a sense against refs; agy could not open any file |
| F3 | ja furigana / rubies | minor | 警 compare 「｜見《けん》はって」 (みはって); 帰 nuance 「｜帰《かえ》の字」. The prose rubies 劣《れつ》, 伴《はん》, 納《のう》 give 音 readings the card's own `on` list does not have | → 《み》, 《き》. The three are rewritten as 「｜劣《おと》る」「｜伴《ともな》う」「｜納《おさ》める」 in 乏/伴/従/縮 and in the 負/収 back-links | `check_ruby_suspects` does not see 見《けん》+kana; nothing compares a prose ruby with the entry's readings |
| F4 | ja glosses, rule 27 (author's doubt) | major | 刑 「ばつ」, 剣 「かたな」, 織 「ぬのにする」 and 旬 「月を三つにわけた十日」 rest on no ref. The refs give only 刑事, 真剣, 組織 (Soumatome 漢字 too) and 下旬. 垂 「うえからしたへ…さがる」 is also unattested (only 垂直 is), and it competes with live 下 「上から移る」 and 降. The 織↔布 link existed only because of the weaving sense | Glossed from the attested compound, in kana: 「「けいじ」のかたちで、つみをおかしたことにかかわること」, 「「しんけん」のかたちで、ほんきでとりくむようす」, 「「そしき」のかたちで、やくめをわけあってはたらく、ひとのあつまり」, 「「げじゅん」のかたちで、つきのおわりのころ」, 「「すいちょく」のかたちで、たてにまっすぐなこと」. vi to match. 織↔布 is unlinked and the 布 back-link removed. **絞** keeps the wring sense, now sourced to SK 語彙 PDF 96 (タオル／知恵／テーマ／音を絞る) | Rule 27 is read for 語彙, but a `kx-` kanji has no SK page, so the author filled the kanji's sense from memory |
| F5 | gloss collisions the generator cannot see | major (抗/反, 視/見) | ja 抗 「…さからうこと」 = live 反 「そむくこと、さからうこと」. ja 視 「目をむけて、よくみること」 ≈ live 見 「目でものをとらえること」 (vi "nhìn" in both after the first fix). ja 摘 「だいじなところを…」 shares 要's 「だいじなところ」 | 抗↔反 linked with 「反抗心」 (Hajimete PDF 119, added to 抗's words and sources). 視↔見 linked. Both get back-links in both languages, so the live targets go 45 → 46 (+反 +見 −布). 摘 reglossed 「もんだいになるところを、とりあげてしめすこと」, and the 指 back-link was updated | B4 R2 covers compound partners in `words`, not semantic twins that share no compound in the batch |
| F6 | 抵/抗 reading quiz (author's doubt) | minor | Both cards' only word was 抵抗. 抗 sorts first and takes it, so 抵 fell back to the same 抵抗 item. Rule 30 says this cannot happen; it does whenever a card has no other word | 抵 gets 「｜大抵《たいてい》」 (official 7/2013 読解 text, cited with 「数えない」); 抗 gets 「反抗心」. Now 抗→抵抗 and 抵→大抵 | `reading_target` falls back silently, and the gate does not WARN on two identical `#r` items |
| F7 | back-links 負, 反 | minor | 負's new compare dropped the B4 F3 link 「背負う」, which merge flagged as REVIEW. The first repair dropped 「まける」「かつ」「失敗」, and the new 反 compare dropped 「ちがう」 | Both are rewritten inside the 100 cap, with every old quoted form kept; merge now prints no REVIEW | The author fitted the band by cutting the oldest sentence |

## Author items, judged

1. **抵/抗 share one reading quiz.** Real (F6), and rule 30's claim is false in this case. Fixed in data.
2. **Glosses resting on general knowledge (刑, 剣, 織, 旬).** All four had no source, so each was cut to the attested compound sense (F4). 垂 was added to the list. 絞 was sourced, not cut. 端 「もののへり…いちばんさき」 is kept: it is the compositional sense of the attested 極端, and the vi gloss matches it. A stricter owner ruling could cut it too.
3. **SK-number mapping (一 帰 待 伝 警 材 柔 憎 統 判).** Correct on the 目次, the list pages and the 回 groups.
4. **帰 and 伝 counted 0.** Correct under rule 40.

**agy vi defect rate.** About 75 of the 236 vi prose fields (≈ 1 in 3) needed a fix for their own sake; that excludes fields rewritten only because a ja example or link changed. Also 8 of 45 back-link compares, and 1 schema-breaking key that made the gate FAIL. The defects are mostly unattested senses, folk etymology and unsourced contrasts. One false friend (指摘 = chỉ trích) was used as the gloss itself. Quoting was clean: agy invented no Japanese word.

**Counts:** 7 findings: 4 major (F1, F2, F4, F5), 3 minor. Edits:
- 29 examples, each with its vi example_note
- 7 ja meanings, 6 usages, 2 nuances and 10 compares
- ~86 vi fields (75 for agy defects)
- shared data: 2 words added (大抵, 反抗心), 4 sources added, 2 「（再掲）」 notes; related +抗↔反, +視↔見, −織↔布
- back-links: 3 changed in ja, 8 in vi; 2 added, 1 removed

The vi text of the new compares and glosses was written in this QA context, which had also read the ja pane. As in B2–B4, this breaks the "written, not translated" split for those fields. They were written from the kanji facts and the printed options. A vi-only pass may re-author them.

## Root causes and proposed rules

- **R1 (F1) — RULE-UNENFORCED.** B4 R1 is still not in LEX_JA_BRIEF. Add: "Read EVERY ≥2-token overlap hit against `knowledge/<LEVEL>/*.json` (quiz stems included), the open `batches/*.json`, every refs extract AND the entry's own cited official items, and compare the FRAME. A cited official sentence's frame with a new subject is a copy." The module is now saturated for the common scenes (shop, hospital, exam, grandparent, PC, map app, sports, weather). Authors should start from an uncommon setting.
- **R2 (F2) — PROCESS.** A no-file-access drafter cannot satisfy rules 9 and 27. Either give the vi drafter the refs lines for each entry (cited item + options + the textbook line), or budget a full vi rewrite in QA. The prompt should also forbid etymology, radical stories and 「thường/hay」 claims outright. It should require that a "trong đề" claim quote options the prompt supplied.
- **R3 (F4) — RULE-MISSING.** SKILL rule 27, for `kx-`: "A kanji SK does not number is glossed from its attested compounds only (「「X」のかたちで…」). A free-standing sense needs a page."
- **R4 (F6) — GATE-BLIND.** `check_knowledge` should WARN when two entries' `#r` items show the same compound. Or the coordinator should give each `kx-` card a second attested word.
- **R5 (F3) — GATE-BLIND.** WARN on a single-kanji ruby in prose whose reading is not in that entry's `on`/`kun`. Also add 見《けん》+kana to `check_ruby_suspects`.
- Housekeeping: `CLAUDE_YOU_MUST_READ_THIS.md` is still untracked at the repo root. It is outside this review and was left alone.

## Merge steps for the coordinator

1. Apply `batches/K5_live_meaning_fix.json` unchanged, as `meaning` overwrites in `knowledge/N2/漢字.ja.json`. No vi fix file is needed.
2. Run `python3 merge_batch.py 漢字 5`. It should print +59 entries and back-links applied to 46 live entries, with no REVIEW lines.
3. Run `make knowledge`, then `make check`. Read every line.
