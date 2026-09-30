# QA report: knowledge/N2 文法, batch 11 (19 points, 57 examples, 38 quiz items, 31 back-links)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. The files are in the coordinator's
scratch `batches/`. The sha1 values are the first 12 characters, before review → after the fixes:

| file | pre | post |
|---|---|---|
| `文法_B11.json` | 889c18054979 | e89769e95c89 |
| `文法_B11.ja.json` | 883b9f3d4d39 | 47e510c50dd5 |
| `文法_B11.vi.json` | cc0c16ee4fdc | 91d1f3bc5227 |
| `文法_B11.backlinks.json` | 9f647b343175 | fa438e4d2158 |
| `文法_B11.backlinks.vi.json` | 568fa4c0c062 | 568fa4c0c062 (unchanged) |

All fixes are in one re-runnable script, `scratchpad/QA11_patch.py`. It always starts from `QA11_bak/`. I did not
touch the real `knowledge/` or B12 (g-fumaete).

## Verdict

`QA: FAIL → fixed (11 finding classes, 32 surfaces; 4 automatic-fail surfaces: two copies of a Shin Kanzen
example frame, one copy of a live entry's example, one official-item scene). No content findings are open.`

**Gate.** `QA11_gate.sh` copies `.agents/` and `knowledge/` into `scratchpad/QA11_repo` (the rest is symlinked) and
runs `merge_batch.py`'s own logic there (`QA11_merge.py`: REPO repointed, and the REVIEW check extended to the vi
pane). It merges the live 273 plus B11 and applies 31 back-links. Then it rebuilds with `build_knowledge.py --level N2`
and runs `check_knowledge.py`.

- **Result: 0 FAIL, 0 WARN, 292 entries.** This includes `check_ruby_suspects` (with the B10 形 rule),
  `check_meaning_lures`, `check_prose_citations` and `check_related_symmetry`.
- **REVIEW lines: none**, before or after the fixes, in the ja pane and in the vi pane. So I read all 31
  back-links by hand against the current live compare. Two had lost content that is not in 「」 (F8).
- B11 answer positions are 10/10/9/9, and the merged category is 143/149/148/144. No key moved.
- Two band overruns in my own new text (g-tte ja compare 102, meshiagaru vi quiz 157) were trimmed.

## 1. Blind solve (rule 7)

- `QA11_blind.py` wrote stems and options only, no ids, shuffled with seed 1111. I saved my answers to
  `QA11_myanswers.txt` before I opened the map.
- **38/38 agree with the keys.** As in B0–B10, agreement proved little.
- I spliced all 114 distractors, then spliced all 7 changed items again. **Eight of my own replacement drafts failed
  that re-check** and were changed a second time:
  - mono-wo Q1: くせに is natural after a ば-clause (「調べればわかるくせに」), so it was a second answer → ことに.
  - kanarazushimo ex2: 「有名な大学を出た人が…仕事ができる」 = live g-karatoitte Q1.
  - douka ex2: 「家族がみんな元気で…ますように」 = live g-you-ni ex1.
  - koto-shiji Q2, three tries:
    - 美術館の作品に触れない ≈ live g-keigo-goran Q1 (美術館, 作品を手に取って).
    - エレベーターを使わない = live g-kiwa ex3.
    - The report-deadline idea ≈ 7/2018 問題8-47.
  - koto-shiji ex3: 会議室の机といす ≈ 漢字 k-0462 ex1.
  - koto-shiji ex1: a campsite fire rule ≈ 聴解 l-sk-29 Q1.

## 2. The authors' flags, judged

| flag | verdict |
|---|---|
| vi: kanarazushimo Q1 「とても」 killed on meaning only | **Upheld.** とても is not in the PDF 159 table, and its kill rested on an unstated rule (「とても〜ない」 = impossible). → **まるで**, which PDF 159 lists as 様態 and which needs 〜ようだ. Kills now: まさか ← no 〜だろう; いったい ← no question; まるで ← no ようだ. All three are on the page. The ja explanation targets まるで, the vi one いったい |
| vi: meshiagaru Q1 「おいでになって」, a real honorific killed only on meaning | **Kept.** A meaning kill on a quoted stem clause is what rule 8 asks for: 「こちらのスープは熱いので」 makes the action eating, and おいでになる is 来る / 行く. The distractor is not a misuse natives produce, so rule 14 is satisfied. The vi explanation now targets it (before, both panes explained お食べして), and vi Q2 now targets お召し上がりしました |
| vi: mono-wo Q1 「わりに」 killed only by the counterfactual ば-clause | **Upheld.** 「すぐわかったわりに…何度も行ったり来たり」 reads as "easy, yet he wandered", so the kill was grammatical only. The stem now opens 「父は駅の地図を見ようともしなかった。」, and わりに → **ことに** (IV-D, PDF 139: it follows a feeling, such as 不思議なことに). Kills: ものだから ← cause and effect clash (「すぐわかった」 against 「何度も行ったり来たり」); ものなら ← IV-G 1a (PDF 146: needs a wish or intent after it, but the main clause is a past fact); ことに ← 「わかった」 is not a feeling. Q2 also had two syntax kills (ことに, ついでに) → ついでに → からには (IV-G 1a) |
| vi: g-dano connection vs PDF 144 notation | **Confirmed.** On PDF 144 it is 「名・普通形（ナ形 ~~だ~~・名 ~~だ~~）＋だの」, with だ struck through. So the だ of the plain form is dropped and だの is attached. The shared connection (「だ」を取る) and the vi usage (bỏ 「だ」 rồi gắn 「だの」) state this literally. The ja usage said 「だ」を付けない, which is ambiguous; it now says 「「だ」を取った形につく（「静かだの」「雨だの」）」 (rule 15) |
| vi: dokoroka back-link 「thường tệ hơn」 | **Kept.** PDF 66 ▲ says 「前件よりも悪い状況を言うことが多い」, and "thường" carries that hedge |
| vi: youyaku note on Vietnamese "cuối cùng" | **Kept.** It is true that "cuối cùng" also means "last in a list" and ようやく does not. It is not a Hán Việt claim, so rule 34 does not apply, and nothing contradicts it |
| ja: six non-existent keigo forms as distractors | **Rule 14 is satisfied.** I found four: お目にかかりになりたい, お目にかかられて, お食べして, お召し上がりしました. None is a misuse natives commonly produce. お目にかかられる (謙譲語 + られる) is the 参られる type that rule 14 itself gives as allowed |
| ja: g-dokorodehanai restricted to 18課5 | **Correct.** PDF 93 gives 「〜できる状況ではない」, 名・動辞書形, and the ▲ reasons. The 程度 sense on PDF 66 (12課2) is left to the compare. Coverage note for the coordinator: the live g-dokoroka card's headword is 〜どころか only, so 12課2's 程度 〜どころではない has no card of its own |
| ja: count calls (どうしても 2; 7/2014-48 not counted) | **Upheld.** The two cards are 12/2014 P8-49 and 7/2022 P8-45. 7/2014 P8-48 (reprinted as 7/2021 P8-44) has どうしても in B's line of the stem. 12/2024-36 is stem only. 7/2024-32, 7/2025-33, 12/2012-42 and 12/2021-42 are distractors |

## 3. official_count (rules 4, 10, 12, 37): all 19 re-verified

`QA10_hits.py` printed every 問題7–9 line in the 31 `booklet.md` files that holds any batch form. I checked each hit
against `key.md` with a new helper, `QA11_item.py`, which prints an item with its key. I also grepped for bare
option lines (`１ こと`) to catch one-mora forms.

| entry | shipped → verified | hits (excluded) |
|---|---|---|
| **koto-shiji** | **0 → 1** | **12/2015 問題7-39**: 「コート内では必ずテニスシューズを履く（こと）。」, key 1, options こと／はず／など／のみ. Added to `sources`. (12/2019-32 聞かなかったことにして is ことにする) |
| kke | 1 ✓ | 12/2022-38 何番（だっけ）. 12/2020-42 よかったっけ is a distractor |
| adv-doushitemo | 2 ✓ | §2 |
| adv-youyaku | 1 ✓ | 7/2017 P8-48 card. 12/2019-31 is stem only. 7/2022-32 and 12/2012-35 are distractors |
| ka-no-you | 0 ✓ | 12/2016-37 (key 以上), 7/2017-41 (key というように), 7/2025-39 and the 問題9 options 12/2018 / 7/2021 are all distractors |
| omenikakaru, sashiageru, mono-wo, douka, chittomo, kanarazushimo, chuushin | 0 ✓ each | distractors only: 12/2019-36, 12/2016-38 / 12/2024-35, 7/2013-38 / 12/2023-34, 12/2020-33 / 12/2019-33, 12/2011-36 / 7/2021-32, 12/2022-32 / 7/2023-32, 12/2016-36 (12/2010-37 is stem only) / 7/2025 問題9-51 |
| the other 8 | 0 ✓ each | no 問題7–9 key. 結果 in 7/2010 問題9-50 is a distractor (key もの) |

## 4. Findings

| # | class | severity | surfaces | evidence (abridged) | fix | root cause |
|---|---|---|---|---|---|---|
| F1 | official_count wrong | 要修正 | koto-shiji | §3 | 0 → 1, and the source was added | PIPELINE-GAP: a regex for 「こと」 drowns in instruction text (最もよいものを…), so a one-mora 文末 form needs a grep of the option lines (R3) |
| F2 | Shin Kanzen frame copied (rules 3, 13) | **auto** | dokorodehanai Q1, ex1 | Q1 「引っ越しで…忙しくて、お花見どころではない」 = PDF 93 ① 「仕事が忙しくて、旅行どころではない」. ex1 「…ゆっくり話すどころではなかった」 = ② 「…ゆっくり食事を楽しむどころではなかった」 | Q1 → 「来週、大事な資格の試験があるんだ。今はお花見（　）んだ」. ex1 → 台風 → 「その夜は寝るどころではなかった」 | RULE-IGNORED (rules 3, 13; B10 R1 column). Once again it is the entry's own cited page |
| F3 | official scene reused (rules 21, 33, 39) | **auto** | kanarazushimo Q2; koto-shiji ex1 | Q2 (study → 「すれば」 → pass, options 必ずしも / たとえ) ≈ 12/2016 問題7-36 (「たくさん書けば（そのうち）うまくなる」, options 必ずしも / たとえ / そのうち / さっき). ex1 「（プールの注意書き）入る前に、必ずシャワーを浴びること」 ≈ 12/2015-39 (tennis-court sign, 必ず…履くこと), the item F1 found | Q2 → 牛乳 → 背が伸びる (たとえ still dies on 「飲めば」). ex1 → 「（駅の掲示）エスカレーターでは、手すりにつかまること」 | RULE-IGNORED; F1 hid the item |
| F4 | scene + predicate shared in the module (rules 11, 35, 39) | **auto** (first) / 要修正 | kanarazushimo ex2; koto-shiji Q2, ex3; to-douji-ni ex2, ex3; meshiagaru ex1, ex2; douka ex2; towa-kagiranai ex2 | kanarazushimo ex2 「日本人だからといって…敬語を正しく使えるわけではない」 = live g-wake-dewa-nai ex3. koto-shiji Q2 (試験中 スマートフォンを使わない) = 語彙 v-o-ihan ex2. to-douji-ni ex2 (会議が終わる → 部長が部屋を出ていった) ≈ live g-to-omou-to Q1, g-mokamawazu Q1; ex3 (祖父 七十歳 → 始めた) ≈ 語彙 v-0537 ex2. meshiagaru ex1 (社長は毎朝…) ≈ g-keigo-nasaru ex2, g-keigo-irassharu ex3; ex2 「先生、お昼ご飯はもう召し上がりましたか」 = its own Q2. douka ex2 (day of an exam, 「どうか…ますように」) = its own Q1 (day of an operation). koto-shiji ex3 and Q1 both 「朝八時までに」. towa ex2 (人気の店 → 口に合う) = its own Q1's frame (ベストセラー → 面白い) | new: 料理の本を何冊も持っている人; 登山道の看板 植物を取らない; 調理室の掲示 包丁; 目覚まし時計が鳴ると同時に; 就職が決まった → 部屋を探し始めた; お客様がお茶を召し上がっている間に; 辛い料理はあまり召し上がらない; 七夕 新しいクラスで友達ができますように; 地図アプリが教える道 | RULE-IGNORED (rule 39's module-wide grep); `QA9_cross.py` reads 文法 only (R4) |
| F5 | soft or syntax-only kills (rules 8, 23, 32) | 要修正 | kanarazushimo Q1; mono-wo Q1, Q2; youyaku Q2 | §2. youyaku Q2 had two syntax kills (二度と and かりに both need a particular sentence end) | youyaku かりに → きっと (PDF 159 推量, dies on B's own 「うん…終わったよ」) | RULE-IGNORED (rule 23: two of these were flagged, and none was fixed before hand-off) |
| F6 | a form with 0 hits kept (rule 37) | 要修正 | chuushin connection, vi usage | 「を中心にして」 has 0 hits in `refs/**/*.md`. を中心に and を中心として both have hits | cut | RULE-IGNORED |
| F7 | furigana | 要修正 | kanarazushimo Q2; doushitemo ex3; back-link g-keigo-o-suru | 「｜十時《じゅうじ》｜間《あいだ》」 (十時間 read as じゅうじ + あいだ); 花畑《はなはた》 → はなばたけ; 「かえた｜形《けい》」, where 形 is a plain "form", so かたち | fixed (the Q2 stem is new) | GATE-BLIND (R1) |
| F8 | back-link dropped live content not in 「」 | 要修正 | g-keigo-o-suru, g-tte (ja) | 「お〜いたす」は「する」を「いたす」にかえた形 lost 「する」を, which leaves it unclear what was changed. 「って」 lost 「意味を聞く」, which the live usage names (〜って何？) | both restored within the band | TOOL-BLIND: REVIEW compares 「」 forms only, and in the primary pane only (R2) |
| F9 | wording widened or narrowed (rule 15) | 要修正 | dano ja usage; koto-shiji ja usage + vi compare; to-douji-ni ja compare | dano: §2. koto-shiji: 「書いて伝える指示に使う」 / "viết cho mọi người đọc". PDF 139 does not say the form is written only. to-douji-ni: 「「とともに」は、一方の変化につれて…」 narrows とともに, which also means 同時 | literal and scoped: 「みんなに向けた指示」; 「に伴って・とともに」 | RULE-IGNORED |
| F10 | vi rule 6 | note | kke vi usage | a bare 「です」 | quoted | RULE-IGNORED |
| F11 | textbook example in prose (rule 32) | note | dokorodehanai vi nuance | 「(bệnh nặng hơn mình nghĩ)」 retells PDF 66 ① (風邪 → 肺炎) | 「“đâu phải ở mức A, thực tế khác xa”」 | RULE-IGNORED |

**Explanations.** Every changed item was re-explained in both panes, the vi text written from the item. In each changed
item the vi pane now targets a different distractor from ja: meshiagaru Q1 / Q2, mono-wo Q2, kanarazushimo Q2,
youyaku Q2, dokorodehanai Q1, koto-shiji Q2. mono-wo Q1 keeps both original explanations (ja ものなら, vi ものだから),
because both are still true of the new stem. Note: in 20 of the 38 items both panes explain the same distractor. No
rule bans this, so I left those items alone.

**Checked and not findings**

- **SK pages read** (my own renders, `QA11_pages/`): PDF 66, 93, 96, 138, 139, 142, 144, 146, 159.
  - 接続 and meaning match literally: だけあって (＊名だ never, ▲ no future or conjecture after it),
    どころではない (名・動辞書形), だの (§2), こと (動辞書形／ない形).
  - つつ's 「硬い言い方」 is the inventory's SK register. あげく's 「残念な結果」 is the SK gloss (20課3).
- **Rule 38:** every distractor is a live entry or an inventory row (checked by script). たいして, 今にも, まるで and
  きっと are PDF 159 rows. お会いになる is g-keigo-o-ni-naru.
- **Rule 22:** no key is printed as a wrong option in an equivalent official frame. お目にかかる is a distractor
  where a guest or visitor comes, and 差し上げる appears in 感謝の言葉を / 注文 frames.
- **Provenance** (`QA9_prov.py` over `refs/**/*.md` including scripts, and `tests/imported-*`). Before and after the
  fixes, the hits left are stock phrases: してくれればよかった, お客様がいらっしゃっ, 気をつけてください,
  になさってください, からといって、必ずしも (Shin Kanzen 語彙, a film sentence).
- **Bigram scan** against all official 問題7–9 items (`QA9_bigram.py`, ≥2 shared bigrams, every hit read). After the
  fixes, the hits share nouns only (目覚まし時計, 会議室, 美術館 → gone).
- **Module scan** (`QA11_cross.py`: every B11 example and stem against live 文法 / 語彙 / 漢字 / 読解 / 聴解, B12, and
  B11 itself, own entry included; kanji bigrams ≥2 read). What is left shares nouns only.
- **Furigana:** I read every ruby pair in the batch (list in `QA11_dump.txt`). `check_prose_citations` is clean, and
  no metadata leaks.

## 5. Root causes and proposed edits

| findings | code | proposed edit |
|---|---|---|
| F7 | GATE-BLIND | **R1 (gate, `check_ruby_suspects`, WARN):** (a) a numeral ruby followed by 「｜間《あいだ》」 (十時《じゅうじ》｜間《あいだ》, 三年《さんねん》｜間《あいだ》): 時間 / 年間 split and read あいだ; (b) 形《けい》 right after a plain た-form verb (かえた形《けい》), the reverse of the B10 rule. **The live tree already has (a) twice**, and nobody has fixed them: g-ppanashi Q1 「｜三時《さんじ》｜間《あいだ》」 and g-ni-motozu-ite Q (shared stem and ja quiz) 「｜三年《さんねん》｜間《あいだ》」. Both came in with B10 and are for the coordinator. I did not touch `knowledge/` |
| F8 | TOOL-BLIND | **R2 (`merge_batch.py`):** run the REVIEW check on every learner pane too (`QA11_merge.py` does), and also print a clause-level diff (difflib on 「。」-split sentences) of old → new, so that unquoted losses show (「する」を, 意味を聞く). It printed 0 lines on a batch with two real losses |
| F1 | PIPELINE-GAP | **R3 (BATCH_JA_BRIEF, counting):** for a one- or two-mora 文末 form (こと, もの, わけ, の), grep the option lines (`^[1-4１-４] こと`) and the key, not the form. The form regex drowns in 「最もよいものを」-type instruction text. Founding case: 12/2015-39 |
| F4 | RULE-IGNORED + PIPELINE-GAP | **R4 (brief tool):** give authors `QA11_cross.py` in place of `QA9_cross.py`. It reads every live category, the open batches and the entry's own quiz. `QA9_cross.py` reads 文法 only, so 語彙 v-o-ihan and v-0537 were invisible to it. It caught all ten F4 surfaces, and eight of my own drafts |
| F2, F3, F5, F6, F9–F11 | RULE-IGNORED (rules 3 / 13, 21, 8 / 23, 37, 15, 6, 32) | none. The rules exist. F5's two flagged kills were handed in unfixed (rule 23) |

## 6. Coverage and skips

- Blind solve on all 38 items. I spliced all 114 distractors, and spliced all 7 changed items again.
- official_count re-verified for all 19 entries, each hit against `key.md`.
- Every SK-cited entry was compared with its page. Provenance, the official bigram scan and the module scan were each
  run before and after the fixes.
- Back-links: all 31 old → new pairs read in both languages, against the current live compare.
- Gate: live 273 + B11 merged in scratch with the back-links, rebuilt, `check_knowledge.py` → 0 FAIL, 0 WARN.
- **Skipped:**
  - `make check` / `make knowledge` on the real tree. The coordinator merges, and I must not touch `knowledge/`.
  - B12 (g-fumaete) was read only, as a scan source.
  - Speech and pitch (the 文法 pitch flag is off).
  - The untracked `CLAUDE_YOU_MUST_READ_THIS.md` asks for 語彙 / 漢字 work outside this brief. I did not act on it.
