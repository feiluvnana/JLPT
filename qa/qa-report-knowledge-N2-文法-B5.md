# QA report: knowledge/N2 文法, batch 5 (25 points, 75 examples, 50 quiz items)

Reviewed 2026-09-30 by a fresh-eyes context that authored none of the batch. The files are in scratch `batches/`. The sha1 values below are the first 12 characters, before review → after the fixes:

| file | pre | post |
|---|---|---|
| `文法_B5.json` | dae5123eb7a8 | c6b78f71e12c |
| `文法_B5.ja.json` | 2da71a81c6d7 | af5e9b590f4f |
| `文法_B5.vi.json` | d2620d1b79f7 | 6f8e7c700765 |

## Verdict

`QA: FAIL → fixed (15 findings, 4 automatic-fail class covering 10 items). No content findings remain open after the fixes.`

I merged B5 onto the current `knowledge/N2/文法*.json` (B0–B3, 97 entries) in a scratch copy (`scratchpad/QA5_repo`, script `QA5_gate.sh`). I rebuilt the pages there and ran `check_knowledge.py`: **0 FAIL, 0 WARN, 122 entries**. The real `knowledge/` was not touched. Every `related` id in B5 resolves inside B0–B3 or B5 itself, so **B5 can merge on its own, without B4 or B6.**

**One id was renamed before merge:** `g-ni-tomonatsu-te` → `g-ni-tomonatte`, a typo. No other batch or file referenced it (checked by grep).

## 1. Blind solve

- **Extraction:** `scratchpad/QA5_blind.py` wrote `QA5_blind.txt` with stems and options only, no ids, shuffled with seed 55. I solved all 50 items there and saved my answers to `QA5_myanswers.txt` before I opened the keys.
- **Result: 50/50 agree with the keys.** Agreement is only the floor here, as in B0–B3. The splice pass below found one second defensible answer, eight weak or form-only kills, and ten items that copy an official item's or Shin Kanzen's apparatus.
- **Position balance:** 12/13/12/13 before and after. Every re-authored item kept its key position.

## 2. Per-entry walkthrough

I read these SK pages on the scan: PDF pages 23, 27, 31, 34, 40, 52, 53, 75, 100, 101, 110, 139, 159, 204 and 205. I re-verified `official_count` for **all 25 entries**, hit by hit. That covered 問題7 keyed options (`B1_p7.json`), 問題8 **cards** (`QA3_p8.py`) and 問題9 keyed options (`QA1_hits.py … 9`), each read against the key.

| entry | SK page / 接続 | official_count (verified) | verdict |
|---|---|---|---|
| g-keigo-irassharu | 敬語; p.194 note ✓ (読む人を意識した敬語は使わない) | 1 ✓ (7/2022-38) | Q2 furigana 六時《ろくとき》 fixed (F10); vi nuance heuristic fixed (F9) |
| g-keigo-nasaru | 敬語 | 1 ✓ (12/2023-37. 7/2018-42 しておきなさい is imperative and not counted) | OK: 「ご出発は何日になさいますか」. Every distractor is humble or 申す on the customer's act |
| g-keigo-o-suru | 敬語 | 1 ✓ (7/2016-44. 12/2010-39 おわび申し上げます is お〜申し上げる and not counted) | Q2 replaced (F1) |
| g-chau | p.194 ✓ (縮約形は硬い文章で使わない) | 2 ✓ (7/2017-43; 7/2012 問題8-46 card 行っちゃった. 12/2011-41 しとかなくちゃ is なくちゃ) | OK. Q1 has one form kill (なくし＋なくちゃ); とく attaches (なくしとく) |
| g-adv-sonouchi | SK外 | 2 ✓ (7/2022-32, 12/2016-36) | OK. The official distractors いまにも/さっき/たとえ recur, but in different scenes |
| g-tsutsuaru | p.13 ✓ (動ます; ▲ 変化動詞); p.195 ✓ | 1 ✓ (12/2014-44) | furigana 表《おもて》→《ひょう》 fixed (F10) |
| g-tsutsu | p.13 ✓ (▲ 時間の幅・同じ主語); p.17 次第 ▲ ✓ | **1 → 0**: the cited 12/2019 問題8-44 card 「寝ようと思いつつ…見続けてしまい」 is 14課4 つつ（も）, p.65 (F7) | Q1 fixed (F3); Q2 fixed (F5); vi nuance no longer quotes SK p.65 ② |
| g-bakarika | p.30 ✓ (literal 接続, ▲ も／働きかけ×) | 0 ✓ (7/2024-34 is a distractor) | Q2 fixed (F3) |
| g-ni-tomonatte | p.42 ✓ once the 接続 was fixed (F8) | 1 ✓ (7/2022-35) | Q1 fixed (F3); id renamed (F12) |
| g-ni-ouji-te | p.43 ✓ | 1 ✓ (7/2010-33) | Q2 fixed (F3); vi nuance fixed (F9) |
| g-ageku | p.90 ✓ once あげくに was removed (F8); p.91 末(に) ✓ | 0 ✓ (12/2010-33 is a distractor) | Q2 re-keyed (F5) |
| g-osoregaaru | p.100 ✓ (▲ マイナス・ニュース; かねない「原因がはっきり」) | 1 ✓ (7/2017-37) | Q1 fixed (F2) |
| g-koto-wa-ga | p.129 IV-D ✓ (literal, incl. 名 だ→な) | 0 ✓ (every ことは hit is ことはない or a noun こと) | Q1 fixed (F3); ex2 fixed (F4) |
| g-ni-tsuide | SK外 | 2 ✓ (7/2016-33; 7/2013 問題8-45 card) | Q1 fixed (F2) |
| g-mama | p.90 〔復習〕 only | 3 ✓ (7/2014-44, 12/2018-40, 12/2021 問題8-45 card. 7/2010-44 このまま is not counted) | note fixed (F11) |
| g-okini | SK外 | 2 ✓ (12/2015-33, 7/2017-33) | Q2 fixed (F5); ja furigana 水《みず》 and 二十分《にじゅうふん》 fixed (F10) |
| g-katei | SK外 | 1 ✓ (12/2016-39) | Q2 fixed (F2) |
| g-hodo-wa-nai | SK外 | 2 ✓ (12/2022-42; 7/2023 問題8-44 cards ほどの＋重さはない. The degree ほど of 7/2015-36, 12/2013-49 and 7/2018-48 is not counted) | Q1 wording and 入《いっ》 fixed (F10, F13); ex3 fixed (F4) |
| g-ba-yokatta | SK外 | 2 ✓ (7/2024-40; 12/2025 問題8-44 cards. ばいい of 7/2021-42, 7/2015-42 and 12/2019-45 is advice or permission) | Q2 fixed (F2) |
| g-keigo-o-desu | 敬語 | 2 ✓ (7/2017-38, 12/2018-37) | Q1 fixed (F2, F5); Q2 fixed (F6) |
| g-keigo-gozaimasu | 敬語 | 1 ✓ (12/2017-39) | Q1 and Q2 fixed (F2, F5); ex2 fixed (F4) |
| g-adv-doumo | p.151 ✓ (どうも・どうやら＝推量) | 2 ✓ (12/2011-36 推量; 7/2021-32 なんとなく) | pattern label fixed (F11) |
| g-adv-karini | not on p.151 (cited 比較用 only) | 1 ✓ (12/2012-35) | Q1 and Q2 fixed (F5); ex1 fixed (F4) |
| g-kagiri | p.21 ✓ | 0 ✓ (12/2025-33 に限り is 5課1, B6's g-ni-kagiri) | ex1, ex2 and Q1 fixed (F3, F5); ja nuance and compare fixed (F9) |
| g-kagiri-5-2 | p.24 ✓ (literal, ▲ 過去×) | 0 ✓ | OK |

## 3. Findings

| # | item | class | evidence | fix |
|---|---|---|---|---|
| F1 | g-keigo-o-suru Q2 | **verbatim official copy (auto)** | 「…お調べしますので、少々お待ちください」 (18 chars) is a line from 7/2022 聴解 script.md:171 (係員, phone, checking something for a caller). Same scene | new stem: 会議で「私から簡単に（ご説明します）」 with ご説明になります / 説明してくださいます / 説明していらっしゃいます. Both panes rewritten |
| F2 | 7 quiz items | **official item's apparatus reused (auto; rule 13 / B3 R2)** | gozaimasu Q1 = 12/2017-39 (a clerk says where an item is, plus distractors おります and なさい(ます)). gozaimasu Q2 = 7/2024-42's printed stem (phone 「クロカワ建設営業課でございます」). katei Q2 = 12/2016-39 「仮に…（とします）。すると…計算」. tsuide Q1 = 7/2016-33 (ranking in a country, plus distractor に代わって). o-desu Q1 = 7/2017-38 (staff offer help 「何か＋お〜」, plus an お〜する distractor). osore Q1 = 7/2017-37 (weather news 「明日の…降るおそれ」, also SK ①). ba-yokatta Q2 = 12/2025 問題8-44 (someone in pain → 〜ばいいのに). Every one of these officials is cited in the entry's own `sources` | gozaimasu Q1 → out of stock (在庫がございません). gozaimasu Q2 → museum 作品でございます. katei Q2 → 「世界中の時計が止まってしまう（とします）。そのとき…」. tsuide Q1 にかわって → にわたって. o-desu Q1 → 部長「お疲れ（です）ね」. osore Q1 → a depopulating area's school closing in 二十年後. ba-yokatta Q2 → a crowded train → 一本早い電車に乗ればいいのに. All explanations rewritten in both panes |
| F3 | 7 surfaces | SK copy (rule 3/13) | koto-wa-ga Q1 「説明書を読んだことは読んだが、まだよくわからない」 = SK IV-D ② 「見たことは見たが、内容がよくわからなかった」. kagiri ex1 体力の限り走り続けた ≈ SK 4課5 ③ 力の限り頑張ろう. kagiri ex2 知っている限りの知識を…伝えた ≈ ② 知っている限りのことを…話して. tsutsu Q1 意見も聞きつつ…決めた ≈ 2課6 ① 住民と話し合いつつ計画を立てて. bakarika Q2 電気…水道 = 6課2 ① 電気代のみならず…水道代 (same page). ouji Q2 体の状態に応じた治療 ≈ 9課4 ④ 体力に応じた運動. tomonatte Q1 売り上げも伸びていく ≈ 9課2 ⑤ 売れ行きが伸びる | new scenes: 風邪薬を飲んだことは飲んだが; 作れる限りのたこ焼き; 冷蔵庫にある限りの材料; 祖母が写真を見つつ昔話; 電車ばかりか飛行機まで; 気温に応じた服装; アイスクリームがよく売れるようになる |
| F4 | 4 examples | rule 11 / official echo | koto-wa-ga ex2 (homework done, answers not confident) had the scene and predicate of its own Q2 (exam written, not confident). karini ex1 (宝くじが当たったら何に使う) had the scene of Q2 (百万円あったら何をしたい). gozaimasu ex2 (こちらが…でございます) had the frame of the new Q2. hodo ex3 (ramen good but not worth queueing) = 12/2022-42's restaurant 「期待していたほどではなかった」 | new examples (ジムに入会したことは入会したが / 今の仕事を辞めたら / 担当の田中でございます / ドラマ…録画してまで見るほどではない); vi notes rewritten |
| F5 | 8 quiz items | second answer (auto) or weak / form-only kill (rules 2, 8, 14) | **karini Q1** 「ついに合格できなかったとしても」 is defensible (ついに〜なかった is standard). karini Q2 has three distractors dead on one axis (けっして/まさか/めったに all need 否定). okini Q2 以内に/までに die on feel (「二十分以内に出ています」 can read as "one leaves within 20 min"); a first repair's ずつ replaced 以内に. tsutsu Q2 きって dies on feel. kagiri Q1 has three form-only kills (ばかり/うち/まま＋の). gozaimasu Q2 と申し上げます is borderline (と申します is the natural form). ageku Q2 keyed 末に and killed あげく only on SK's 「あまり来ない」. o-desu Q1 (first repair) had お読みします, a real humble form natives misapply to a superior | karini Q1 → めったに/いまにも/せっかく. karini Q2 → たとえ/まさか/さすがに. okini Q2 adds 「朝六時から夜十時まで」, options ぶりに/ずつ/も前に/おきに. tsutsu Q2 きって → に (purpose に needs 行く・来る). kagiri Q1 → 友人は持っている（限り）の段ボール箱, options 以上/以外/ついで. gozaimasu Q2 → でおります (a non-form). ageku Q2 → key あげく (一時間も歩き回った…結局タクシー). o-desu Q1 → お疲れ (お疲れする does not exist) |
| F6 | g-keigo-o-desu Q2 | key contradicted by the archive | the key was 「ポイントカードは（お持ちです）か」. **12/2011 問題7-44 prints 「お持ちですか」 as a WRONG option** in 「資格は（　）」 (key 3 お持ちになりますか, `key.md` line 23). Standard usage accepts お持ちですか, but a card that keys it trains the learner to lose that official item | new Q2: ホテル 「どちらまで（お出かけです）か」. The usage examples 「お持ちですか」 in both panes → 「お探しですか」 (officially keyed 7/2017-38). vi nuance now contrasts お待ちします / お待ちです |
| F7 | g-tsutsu official_count | wrong count (rule 12: a look-alike that is another SK point) | 12/2019 問題8-44 「寝ようと思いつつ、つい…見続けてしまい」 is 14課4 つつ（も） (心の動きと行動が違う), not 同時 | count 1 → 0; the source note says why. The ja nuance now cites that official item as the つつ（も） reading |
| F8 | g-ni-tomonatte, g-ageku 接続 | not literal (rules 5, 15) | SK p.42 prints 名(する)・動辞書形 and 名(する)+に伴う+名; the entry said 名詞. SK p.90 prints 名-の・動た形+あげく; the entry added （あげくに） | connection plus ja/vi usage now 「〜する」の名詞; あげくに dropped in shared and vi |
| F9 | 4 prose fields | unsourced or wrong claim (rules 9, 15) | vi irassharu 「に → ở, へ → đi, から → đến」 is false (会議にいらっしゃる = đi). ja kagiri nuance 「決まった言い方が多い…強い気持ち」 and compare 「限りのほうが硬く、強い」 are on no page. vi ouji 「phải có nhiều mức」 narrows SK's 一定でなく変化が予想されるもの | rewritten from p.21 (だけ ▲) and p.43; the vi irassharu readings are now decided by context |
| F10 | 6 furigana | wrong reading (pronunciation) | 六｜時《とき》 (irassharu Q2; B3 F11's class again); 二十｜分《ふん》 ×2 (→ にじゅっぷん); ja okini 月・｜水《みず》・金 ×2 (→ すい); 九月に｜入《いっ》っても (→ はいっても); ja tsutsuaru 本のp.195の｜表《おもて》 (→ ひょう) | all fixed |
| F11 | 3 labels | metadata | SK notes read 「目次 2課5（本のp.13）」, but the cited PDF page is the lesson page, not the 目次 (14 notes). mama's note said SK treats まま 「N3の形として」; SK prints only 〔復習〕. doumo's pattern said （推量）, but ex2, ex3 and the counted 7/2021-32 are the なんとなく reading (rule 5) | notes fixed; pattern → 「どうも（推量・はっきりしない気持ち）」 |
| F12 | g-ni-tomonatsu-te | id typo | "tomonatsu" | renamed g-ni-tomonatte before merge |
| F13 | g-hodo-wa-nai Q1 | awkward Japanese | 「八月の真夏」 is redundant | → 「八月の暑さ（ほどではない）」 |
| F14 | 7 ja + 29 vi prose fields | source tags inside prose (from the B4 reviewer, via the coordinator) | 「（本のp.43）」「（14課）」「12/2019の」 in ja. 「SK:」「SK p.91」「(SK cùng trang)」「bài 5, mục 2」「(đề 7/2021)」「(A)」 in vi. B0–B3 prose never names its source; citations live in `sources` | all stripped and the sentences rewritten. A regex over both panes now finds 0 tagged fields. The つつ（も） illustration no longer quotes official 12/2019 wording (it is now 「無理だとわかりつつ、引き受けた」) |
| F15 | 5 quiz items | one kill reason shared by three options (coordinator clarification: at most two options may share one reason) | irassharu Q1: 参りました / 伺いました / おりました, all humble. nasaru Q1: いたします / 申します / まいります, all humble. o-desu Q1: お疲れ＋します / いたします / 申します, all humble non-forms. o-suru Q2: ご説明になります / 説明してくださいます / 説明していらっしゃいます, all honorific on the speaker's own act. mama Q1: 消したまま / つけないまま / 消してから, all "TV off" | おりました → ございました (ある only); 申します → くださいます (＝give); 申します → ください (a request); 説明していらっしゃいます → ご説明ください (a request, which contradicts 私から); 消してから → つけるために (a purpose). vi o-suru Q2 was rewritten for the new option. I spliced every もの/こと distractor in both readings: osore Q1 ものです (本質 / 忠告) and mama Q2 ことには (unless / 言うことには) are dead in both |

**Provenance scan** (`QA5_prov.py`: 10-char windows, markup stripped, key spliced into each stem, over `refs/**/*.md` + `tests/imported-*`). I ran it before and after the fixes. Before, it found F1. After, the only hits are stock phrases: いらっしゃいますか。, 、どうしたの？」B「, は見つからなかった。, しておけばよかった。, どうぞよろしくお願いいたします, かったとしても、この, るおそれがあります。. Each hit's context was read; none shares a scene.

**Official-apparatus pass:** every official item cited in any B5 `sources` was printed with its options (§2) and compared with that entry's two quiz stems. This found F2.

**vi rule 6:** there are no unquoted kana or kanji outside 「」 except grammar labels (thể ます/た/ない/ば/て, ナ形容詞). **Independence:** the vi explanations have their own frame (fact → key, one glossed distractor). About half target a different distractor from ja: for example koto-wa-ga Q1 だけに (ja) vs からには (vi), karini Q1 いまにも vs せっかく, okini Q2 も前に vs ぶりに. I found no mirrored sentences. **Leaks:** none.

## 4. The authors' flagged doubts, judged

**Japanese author**

- **tsutsu and the 次第 rule:** verified on PDF p.27 (本のp.17) ▲: 「後には、話者の希望・意向を表す文や働きかけの文が来る」. 聞き次第／眺め次第＋past narrative is a printed-rule kill, so it holds. Both tsutsu items changed for other reasons (F3, F5).
- **mama and the SK p.100 〔復習〕:** the page prints only the 〔復習〕 line 「子供が朝家を出たまま、まだ帰ってこない」. SK does not say "N3", so the note was reworded (F11). The entry itself stands on three official keys.
- **hodo Q1, two options killed by one 「が」:** acceptable. ほどだ and 以上だ are both degree competitors, and the contrastive が kills each one. にすぎない dies on meaning. The wording was fixed (F13).
- **okini Q2 以内に/までに:** the doubt is upheld and the item was replaced (F5).
- **敬語 in-group/out-group from the 7/2021-40 stem only:** kept. The official line 受付「中西はただいま外出しております」 said to an outside caller shows the practice itself. The claim adds no strength or frequency, and the note says it is a stem, not a key.
- **g-dokoroka / g-gurai / g-ippou-da left unlinked:** correct. Linking forces a non-empty `compare`, and SK p.30 and p.13 print no contrast with ばかりか or つつある.
- **限り (4課5) vs 限り（は） (5課2) as two entries:** genuine. PDF 31 and 34 are separate headwords with cross-refs (→5課2 / →4課5), and they differ in 接続 (名の・辞書形/ている形 vs 普通形現在, ナ形な/である) and in meaning (範囲のすべて vs 状態が続く間).

**Vietnamese author**

- **tsutsu Q2 きって:** replaced (F5).
- **gozaimasu Q2 「と申し上げます」:** replaced with the non-form でおります, and the scene changed as well (F2).
- **ageku Q2, あげく vs 末に resting on 「あまり来ない」:** upheld. The item was re-keyed to あげく with a clearly bad result (F5).
- **okini Q2 以内に:** replaced (F5).
- **kagiri Q1 「うち」:** upheld. The whole item had three form-only kills and was replaced (F5).
- **tomonatte 接続:** fixed (F8).
- **かりに and そのうち on no SK page:** correct and acceptable. Both are official-only entries (12/2012-35; 7/2022-32, 12/2016-36), like g-keigo-okoshi. karini's p.151 citation is labelled 比較用 (for comparison).

## 5. Root causes

| finding(s) | code | recurrence | proposed edit |
|---|---|---|---|
| F2 (7 items), F1 | RULE-UNENFORCEABLE | B3 F5 (1 item) → B5 (7 items + 1 script copy): systemic | **R1** below. Rule 13's official clause ("a quiz may not reuse its scenario together with one of its distractors") was read as *scenario AND distractor*. Four of the seven shared no distractor, and every one reused the scene of the item the author cited. Nothing tells the author to look at 聴解 `script.md`, which is where F1 came from |
| F6 | RULE-MISSING | first instance | **R2**: grep your KEY string among the archive's official *distractors* |
| F3, F4 | RULE-IGNORED | B0/B1/B3 | rules 3, 11 and 13 name exactly these (other headwords on the same page, the example ↔ own quiz echo). Nothing to change beyond R1's procedure |
| F5 | RULE-IGNORED, now systemic | B3 F1/F2/F7/F8 and B5 (8 items; both authors flagged 5 of them themselves) | **R3**: turn "a flagged doubt means replace" into a hand-off block |
| F7 | RULE-IGNORED | B1 F10 | rule 12 names "a look-alike that is a separate SK point". The cited card's form was never read in context |
| F8, F9 | RULE-IGNORED | B1 F12–F14, B3 F13 | rules 5, 9 and 15 |
| F14 | RULE-MISSING | B5 only (B0–B3 have none) | **R5**: add to both briefs: "Prose never names its source: no 『SK』, page, 課/bài, sitting or sub-sense label (A/B). Citations go in `sources`, and the reader sees them there." |
| F15 | RULE-UNENFORCEABLE | B5 (5 items) | **R6**: the coordinator's clarification as rule text: "Write one kill reason per distractor. No reason may appear three times. A register or direction cluster (three humble forms, three adversatives, three restrictives) is one reason." |
| F10 | GATE-BLIND, **second occurrence** (B3 F11 proposed the 時《とき》 WARN; not built) | B3, B5 | **R4** (the gate) |
| F11, F12, F13 | authoring slips | — | none |

### Proposed additions

**`BATCH_JA_BRIEF.md`**

- **R1:** "For every official item in your `sources`, print it with its options (`QA1_hits.py <form> 9`) and write its SCENE in one line: who speaks to whom, and about what. Your two quiz stems must not share that scene, even with different distractors. B5 reused 12/2017-39 (a clerk says where an item is), 7/2024-42 (a phone self-ID), 12/2016-39 (仮に…とします。すると…計算) and 7/2016-33 (a ranking 'この国で'). Also run the 10-char provenance scan (`scratchpad/QA5_prov.py`, key spliced into the stem) over `refs/**/script.md` too. B5's 「お調べしますので、少々お待ちください」 came from a 聴解 script."
- **R2:** "Grep your key string (and its dictionary form) among the options of every official 問題7 item (`B1_p7.json` `opts`). If an official item prints it as a WRONG option in an equivalent frame, do not key it, even if you think the official key is debatable. (12/2011-44 marks 「資格はお持ちですか」 wrong.)"
- **R3 (tightens B3 R4):** "Your hand-off report may list NO open doubt about a kill. A distractor you would defend with 'sounds odd', 'barely grammatical', 'rarely' (SK's あまり/ことが多い), or 'the other form is more natural' is replaced before hand-off. 'Doubts for QA' is for sourcing questions only."

**`BATCH_VI_BRIEF.md`**

- Same R3. Also: "A reading heuristic ('に → ở…') is a claim. Keep one only if it has no counterexample (会議にいらっしゃる)."

**`check_knowledge.py` (R4, GATE-BLIND, not applied: reviewers do not edit the gate)**

- WARN on `N(?:《[^》]*》)?｜?時《とき》`, where N = `[0-9０-９一二三四五六七八九十百]`. The optional ruby group matters: a first draft without it missed `｜六《ろく》｜時《とき》`. Founding strings: B3 `午後２｜時《とき》` and B5 pre-fix `｜六《ろく》｜時《とき》`.
- WARN on `[一三四六八十](?:《[^》]*》)?｜?分《ふん》` and on `十(?:《[^》]*》)?｜?分《じゅうふん》`. Founding string: B5 `｜二十《にじゅう》｜分《ふん》` (×2).
- WARN on `｜入《いっ》`. Founding string: B5 `｜入《いっ》っても`.
- **I ran all three on the incidents:** 5 hits on pre-fix B5 + B3 (`QA5_bak/`, `QA3_bak/`), every one a founding string. There are 0 hits on post-fix B5, on merged B0–B3 (`knowledge/N2/文法*.json`) and on the B4/B6 batch files.

**`jlpt-knowledge/SKILL.md` §Quiz integrity, rule 13:** replace "(a quiz may not reuse its scenario together with one of its distractors)" with "(a quiz may not reuse its SCENE, whatever its distractors; search the 聴解 `script.md` extracts too)". Add rule 16 = R2.

## 6. Coverage

- Blind solve on all 50 items, then a splice of every distractor on all 50, repeated on every re-authored item.
- SK page read for all 16 SK-cited entries (15 PDF pages). Official-only entries were read in booklet.md and key.md.
- official_count re-verified for all 25 entries across 問題7 keys, 問題8 cards and 問題9 keys in the 31 sittings.
- Provenance: 10-char scan over all 75 examples and 50 key-spliced stems, before and after the fixes. Each example and stem was also read by hand against every SK page that treats the point.
- Furigana: all 605 `漢字《よみ》` pairs were listed and read. Six were wrong (F10).
- Bands, via `knowledge_data.plain()`. ja maxima: meaning 31, usage 93, nuance 70, compare 84, quiz 78. vi maxima: 63/155/178/147/≤137 (cap 144).
- Gate: merged B0–B3 + B5 into a scratch copy, rebuilt, ran `check_knowledge.py` after each of the three fix passes. Final: 0 FAIL, 0 WARN (122 entries, 244 quiz items).

## 7. Skips

- `make check` on the real tree was not run, because the batch is not merged. The scratch-copy gate run stands in for it.
- Pitch and speech were not ear-checked (the 文法 pitch flag is off).
