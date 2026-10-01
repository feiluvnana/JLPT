# QA report — 知識 N2 漢字 batch 8 (73 kanji, SK 183–266; 73→83 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes.

Both panes were written by Claude authors, kept apart from each other. The ja side was rebased onto live after B7 merged (1446b8b).

Files reviewed (scratch `batches/`):
- `漢字_B8.json`, `.ja.json`, `.vi.json`
- `.backlinks.json`, `.backlinks.vi.json`
- `K8_live_meaning_fix.json` (66 ja edits) and `K8vi_live_meaning_fix.json` (8 vi edits)

The originals are kept in `QAK8_orig/`. `QAK8_fix.py` applies every fix to those originals, so the round can be re-run.

Validation ran on a scratch root, `QAK8_root`:
- `.agents/` and the CURRENT live `knowledge/` (post 1446b8b) were copied fresh; everything else is symlinked.
- `QAK8_run.sh` applies both fix files to the copied `漢字.{ja,vi}.json`.
- It then runs `merge_batch.py`, re-pointed as `QAK8_merge.py`.
- Last, it runs the builder and `check_knowledge.py`.

The real `knowledge/` was not edited. Every live-entry fix goes through the two fix files or the back-link files.

## What was checked, and how

| area | method | result |
| - | - | - |
| ids / coverage | SK 別冊 list pages PDF 153–158, sliced with pypdf and read as images | All 73 ids match the page, including the 3 numbers the OCR missed: 代191 痛206 都216. Together with the 11 live ids (待 大 短 地 中 度 疲 品 分 閉 返), 183–266 is complete. `group` 「ステップ1 第1回〜第14回」 is right |
| on / kun / words | the same pages | 73/73 readings match, okurigana and (他) marks included. 代わる/転がる are 自 by the page convention (unmarked). Four words are not on the page, and each is cited from an official sentence: 毎朝 (7/2025 1-4), 予定 (12/2019 1-5), 進歩 (7/2021 1-2). 台風 in 風's usage is on 台's page. F2 covers 都 |
| `official_count` (rule 40) | Parser over the 問題1/2 sections of 31 sittings (301 items). The 9 items it misses were read by hand (7/2019 1-4; 12/2023 1-2, 1-3, 2-9, 2-10; 7/2023 1-4, 2-10; 12/2013 1-4; 7/2018 2-8). All 79 問題1 sentences holding a B8 kanji were checked against their keys | 0 is right for all 73. No 問題2 key holds a B8 kanji. Every 問題1 hit lies outside the underlined word (世の中 よのなか, 下旬 げじゅん, 補い おぎない, 衣装 いしょう …) |
| prose option claims | All four options of every cited item printed: 12/2011 2-10, 7/2014 2-7 and 2-9, 12/2010 2-9, 12/2019 2-10, 12/2021 2-8, 12/2015 2-7, 7/2017 2-9, 7/2021 2-10, 7/2011 2-8, 12/2022 2-7 and 2-8, 7/2024 2-10 | All true. That includes the back-link claims 運貨/運貸/運費, 悪点/低点, 病労/病老 and 非憂/非優 |
| back-link base text | All 73 ja and 73 vi back-links diffed against the CURRENT live compare | 73/73 ja back-links extend the live text verbatim, and the B6 and B7 link sentences are kept. **17** vi back-links are not prefixes, not 7: 分 調 登 永 貨 賃 容, plus 一 学 区 弱 属 否 暮 療 任 持, which insert or merge sentences. All 17 were read sentence by sentence. Only 貨 drops a contrast (F5). The other drops are parenthetical glosses or a mnemonic ("trau dồi", "điều tra", "tính cả", "Mẹo: 'thuộc' là 「属」"), and they are accepted |
| generated quizzes | All 562 `#r` / `#m` items dumped before and after the fixes. All 73 B8 reading items and all 73 meaning items read in both languages. Gloss scans: ja substrings, vi words, bigrams, Hán Việt labels and a tail-word scan. They ran over every unlinked pair that touches B8 or a fixed gloss | F3, F6. Single-kanji words get the fabricated other reading (男 だん/なん, 田 でん, 店 てん, 飯 はん, 母 ぼ). B7 accepted the same class |
| live fix files | Each of the 74 edits read against its card and the CURRENT live text. Every removed kanji was checked against B8 | All 66 ja edits remove only B8 kanji. 22 of them turn the whole compound into kana (物事→ものごと, 部分→ぶぶん, 病気→びょうき, 道具→どうぐ, 植物→しょくぶつ), and that is accepted. No edit brings back a word B6 or B7 QA removed (管 keeps B6's からっぽ). Rule-40 gloss-word re-check: F6 |
| examples | Scans over refs/**/*.md, tests/imported-*, every `knowledge/N2/*.json` (quiz stems included) and the open batches 語彙_B10, 語彙_B11 and 漢字_B9: 10-char windows, a ≥2-token lister, and a separate lister over all 709 official 問題6 option sentences. Every hit was read for scene and frame. Replacements were rescanned over 3 rounds | F1 |
| furigana | All 1,173 distinct ruby pairs in examples, words, prose, back-links and fixes, read in a dump | F2 |
| rule 6 / rule 18 | script; gate | clean |
| gate | scratch merge, before and after | Before: 0 FAIL, 0 WARN, back-links on 73 live entries, no REVIEW line. After: **0 FAIL, 0 WARN**; 562 entries; back-links on 83 live entries; no REVIEW line in either language |

## Findings

| # | where | severity | defect | fix | root cause |
| - | - | - | - | - | - |
| F1 | 8 examples | major (弟 答 電 父), minor (朝 費 風 歩) | Scene and frame copies. **弟**: 「…｜小《ちい》さいころはよくけんかをした」 is a 10-char hit on 語彙 v-0028 仲 (siblings, fought a lot when small). **答**: a questionnaire answer requested by a deadline, the scene of the 7/2016 読解 notice (「6月24日を締め切り日として回答をお願い…」) and of 12/2021. **電**: summer power use rises → the city calls for 節電. That is the claim of the 12/2016 読解 notice (暖房の使用が増加 → 節電). **父**: a meeting decides the roles for a school event, the 12/2024 聴解 問題1 scene (「当日の係の分担を決める」). It also had a ruby bug (F2). **朝**: this morning, everything white = Hajimete 「あくる朝、外は真っ白だった」. **費**: saving money for a trip = SK 語彙 「旅行のためにお金をためているので…」. **風**: laundry on a windy day. 洗濯物を干す is on B7's saturated list (7/2025 問題8-44, 語彙_B11 物干し). **歩**: 「雨の日になると」 repeats 痛's frame word for word. The batch has 4 rain scenes in all | All 8 rewritten (弟 dormitory; 答 quiz answer at the end of a show; 電 island grid on wind power; 朝 朝顔 blooms; 費 car with low fuel 消費; 父 a new 父親 showing photos; 風 wind turns, campfire smoke; 歩 benches on a 歩道). Each vi example_note was rewritten from the new sentence. Rejected drafts: 引っ越しの費用は、会社が半分 (10-char hit on 語彙 v-1123), 将棋の腕が進歩 (saturated), メーカー/市役所 + 回答 (official 読解 mail headers), 車道より歩道が広い (文法 g-okageda). Final scan: no window hit; no ≥2-token hit shares scene and predicate; no 問題6 sentence restored | The author's `K8_prov.py` window corpus covered refs and tests only. It left out `knowledge/*.json`, so v-0028 was missed. The module was scanned only by tokens with a STOP list. Official 読解 claims (rule 31) and textbook 語彙 lines were not read for scene |
| F2 | furigana | minor (pronunciation) | 父: 「｜係《かか》を」 makes ▶ speech read かかを. 都 usage: 「｜都《みやこ》」 is listed under 音読みト. The page prints 都 with と there | 父's sentence was replaced. 都 → 「｜都《と》」 under ト | `check_ruby_suspects` has no rule for a truncated okurigana-less ruby. The usage line was not read against the page row by row |
| F3 | gloss collisions the generator cannot see | major (知/絡, 半/部, 実/真, 便/運), minor (rest) | **知** 「…また、ひとにしらせること」 = **絡** 「…また、ひとにしらせること」, the same clause. **半** 「ふたつにわけたうちの、ひとつ」 vs **部** 「ぜんたいを、いくつかにわけた、ひとつ」. **実** 「本当のこと」 vs **真** 「ほんとうであること」, and vi "thật" in both (pre-existing). **便** 「てがみなどをはこぶこと」 glosses 運 「ものをはこぶ」. **院** 「びょういんや…」 names 病院, whose other kanji 病 is now an entry (B6 R2). **父/母** 「おとこ/おんなのおや」 print 親's gloss 「おや」 (vi "cha mẹ" vs "cha", "mẹ"). **堂** 「…おおきなへやや、たてもの」 vs **室** 「たてもののなかの、へや」. **体** 「からだ」 vs **姿** 「からだのかたち」 (co-occurs in today's dump). **勉** 「はげむ」 vs **努** 「がんばる」. **聞** 「みみで、おとやこえをきくこと」 prints 耳's みみ, and 音 「きこえてくるもの」 glosses 聞こえる. **費** 「つかうおかね」 on 金's item (賃 and 貨 are already linked to 金) | 11 pairs linked both ways, each with a compare in both languages: 院↔病, 父↔親, 母↔親, 半↔部, 堂↔室, 体↔姿, 知↔絡, 勉↔努, 聞↔音, 費↔金, 実↔真. New live back-link targets: 院 親 室 姿 絡 努 実 真 音 金 (73 → 83). Every new live compare extends the CURRENT text verbatim. 便 → 「つごうがよいこと。また、のりもののびんや、てがみ。」 聞 → 「おとやこえを、きくこと。」 (みみ dropped) | B6 R2 / B7 R3 (compound partners; "every flagged link candidate is linked or the report says why") are still not in the vi or ja brief. The ja author ran no kana tail-word scan |
| F4 | vi 非 nuance | minor | 「非常」 is called a false friend of "phi thường (xuất chúng)". 「非常な」 does mean extraordinary, so rule 34 does not allow the trap label | → 「非常」 đứng riêng là tình trạng khẩn cấp; 「非常に」 là trạng từ: rất, vô cùng. | Rule 34 was checked against the commonest sense only |
| F5 | back-link base text | minor | vi 貨 (cap rewrite) drops 「額」 "…, không phải đồng tiền", the 貨/額 contrast. ja 離: the ADD 「｜別《べつ》の「別れて」も並んだ。」 follows the 距 sentence, so it has no item to refer to | 貨: the clause is restored (176/180). 離: 「別れて」 is folded into the first sentence (「…に「逃れて」「別れて」が並んだ」) and every old element is kept | merge's REVIEW checks only quoted forms (B6 R6). A cap rewrite drops a contrast that has no 「」 |
| F6 | live fix files | minor | ja 農 「たや畑で」 reads as たや. vi 親 "song thân" is a literary workaround, and the 父/母 links now make it unneeded. vi 院 "VIỆN — viện" is a bare label. Pre-existing vi collisions in two touched areas: 介 "ở giữa" = 中 "ở giữa"; 理 "xử lý" = 扱 "xử lý" | 農 → 「たんぼや畑で」. vi: 親 withdrawn; 院 → "VIỆN — viện; bệnh viện" (the 病 link covers it); added 介 → "GIỚI — làm trung gian, môi giới" and 理 → "LÝ — lý lẽ, quy luật; sắp xếp cho có trật tự". The other 65 ja and 6 vi edits are accepted | Kana substitution was checked for kanji (rule 34), not for how the result reads. The vi author removed collisions where a link was the better remedy (B7 withdrew 漢/間 the same way) |
| F7 | 服 ja compare | minor | 「｜持《じ》とも｜意味《いみ》が｜近《ちか》い。」 claims 服 and 持 are near in meaning | → 「｜持《じ》の「みにつける」とも｜意味《いみ》が｜近《ちか》い。」 | rule 9 wording |

## Author doubts, judged

- **Link candidates**:
  - 院↔病: linked (F3).
  - 院↔入: not linked. No gloss names 入院 once the vi fix drops "nằm viện".
  - 父↔親, 母↔親: linked. The vi 親 fix is withdrawn.
  - 物↔質: not linked. No gloss names 物質, and the vi fix removes "vật".
  - 電↔線: not linked. The vi fix removes "(điện)", a 電線 sense borrowed from 電 (rule 29).
  - 代↔変: not linked. The glosses do not compete (ja 「ほかのもののかわり」 / 「まえとちがうようす」; vi "thế chỗ" / "đổi khác"). 代's ja compare already contrasts the two かわる, and 変's ja compare is at 95/100.
  - 勉↔努: linked.
- **Hán Việt label lures** (着 TRƯỚC / 前 "trước", 半 BÁN / 売 "bán", 堂 ĐƯỜNG / 道 途 "đường", 湿 THẤP / 低 "thấp", 長 TRƯỜNG / 校, 通 "xuyên" / 川): lures, not second answers. This follows B6 (省) and B7 (車 場 前 秋). Every option leads with its own label, and the definition after the dash cannot gloss the asked kanji. None of these pairs co-occurs in today's dump. The sharpest are 低/湿 and 売/半, where a distractor's label is the key's own definition word (R5).
- **Why 着↔持 and 服↔持**: justified. 持's gloss 「てにもったり、みにつけたりしていること」 overlaps 着 (着ける = 身につける, 「からだにまとう」) and 服 (「からだにまとうもの」). Without the links, 持 could come up as a near-answer on either item. Both are kept; 服's wording is tightened (F7).
- **入/人 shape note**: correct and kept. The strokes of 入 meet at the top; those of 八 stay apart. 人 and 入 are a standard look-alike pair.

**Counts:** 7 findings: 2 major (F1, F3), 5 minor. Edits:
- 8 examples rewritten, each with its vi note; 2 rubies fixed
- 3 B8 glosses (便 ja, 聞 ja, 非 vi nuance), 1 B8 compare reworded (服)
- 11 related pairs, with compares in both languages; 10 new back-link targets, 2 back-link texts repaired (貨 vi, 離 ja)
- ja fix: 1 changed (農); vi fix: 1 withdrawn (親), 1 changed (院), 2 added (介 理). Final sizes: 66 ja, 9 vi

The vi text of the new compares, notes and fixes was written in this QA context, which had also read the ja pane. As in B2–B7, this breaks the "written, not translated" split for those fields. They were written from the kanji facts and the Japanese sentences, not from the ja prose. A vi-only pass may re-author them.

## Residual (pre-existing, outside this batch's scope)

These live glosses still print another entry's headword kanji (rule 34). The brief limits a fix to the B8 kanji, so they are reported, not fixed:
- 果 「木の実」 (実)
- 管 (中, 細)
- 厚 (大)
- 介 (間)
- 永 (続)
- 等 (順)
- 手 / 情 / 講 (人)

The gate's `check_meaning_lures` WARNs if any of them co-occurs with the kanji it prints.

## Root causes and proposed rules

- **R1 (F1) — RULE-UNENFORCED, fourth time.** LEX_JA_BRIEF's frame-scan rule is in place, but the author's window scan still covered refs only. Put this in the brief: "the 10-char window corpus = refs + tests/imported-* + every `knowledge/<LEVEL>/*.json` + open batches". A shared `prov_scan.py` in the skill's scripts would end the per-author drift. Add to the saturated list: questionnaire answer by a deadline, 節電 calls, saving money for a trip, deciding 係 at a meeting, a white morning landscape, and laundry on a windy day.
- **R2 (F3) — RULE-MISSING in the briefs (third time).** Add B6 R2 and B7 R3 verbatim to both author briefs. Also add: "run the kana tail-word scan (another entry's final gloss word inside your gloss: おや, みみ, おかね, しらせる) and link or reword each real hit".
- **R3 (F5) — GATE-BLIND.** `merge_batch.py` should print every non-prefix back-link with both texts, as B7 R1 proposed. This batch had 17 such back-links, while its hand-off listed 7.
- **R4 (F2) — GATE-BLIND, third time.** `check_ruby_suspects` should WARN on a single-kanji ruby whose reading is a strict prefix of the kanji's only dictionary reading (係《かか》 vs かかり).
- **R5 (lures) — OWNER DECISION.** Consider a gate WARN when a meaning distractor's vi Hán Việt label is a whole word of the key's vi definition (低 "thấp" / 湿 THẤP, 売 "bán" / 半 BÁN). A WARN would flag these the day they co-occur.

## Merge steps for the coordinator

1. Apply `batches/K8_live_meaning_fix.json` (66 entries; 農 changed by QA) and `batches/K8vi_live_meaning_fix.json` (9 entries: 親 withdrawn, 院 changed, 介 and 理 added) as `meaning` overwrites in `knowledge/N2/漢字.ja.json` and `漢字.vi.json`. Apply them to the CURRENT live files (post 1446b8b).
2. Run `python3 merge_batch.py 漢字 8`. It should print +73 entries and back-links applied to 83 live entries, with no REVIEW line.
3. Run `make knowledge`, then `make check`. Read every line.
4. Open-batch notes for 漢字_B9 (方 … 話):
   - 木 k-0269: 材's live gloss 「ものをつくるのにつかう、木などのもの」 prints 木, and its vi "(như gỗ)" names 木材. Both need the B9 kanji check.
   - 夜 k-0281: B8 晩 「ひがくれてからの、よる」 will collide with 夜 unless the two are linked.
   - 力 k-0297, 目 k-0278, 本 k-0270, 名 k-0276, 明 k-0277: many live glosses print these kanji (疲 「…の力」, 能 「…できる力」, 強 「力が大きい」).
