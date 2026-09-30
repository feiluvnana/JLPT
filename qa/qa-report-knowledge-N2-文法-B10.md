# QA report: knowledge/N2 文法, batch 10 (25 points, 75 examples, 50 quiz items, 27 back-links)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. The files are in the coordinator's
scratch `batches/`. The sha1 values are the first 12 characters, before review → after the fixes:

| file | pre | post |
|---|---|---|
| `文法_B10.json` | b0cfbda39694 | c9ab230082fb |
| `文法_B10.ja.json` | a840fd7f46ec | fc25b2ecbe6c |
| `文法_B10.vi.json` | 50dc8afd3d49 | 70a6bd09300e |
| `文法_B10.backlinks.json` | ed4ff724a63d | e2bb623429a5 |
| `文法_B10.backlinks.vi.json` | 00e917ca80a9 | ece362785192 |

All fixes are in one re-runnable script, `scratchpad/QA10_patch.py`. It always starts from `QA10_bak/`. I did not
touch the real `knowledge/` or B11.

## Verdict

`QA: FAIL → fixed (14 finding classes, about 70 surfaces; 20 automatic-fail surfaces in F1 and F2: scenes copied
from a Shin Kanzen example or an official item). No content findings are open after the fixes.`

**Gate.** I copied `.agents/` and `knowledge/` into `scratchpad/QA10_repo` and symlinked the rest of the repo. I ran
`merge_batch.py`'s own logic there (`QA10_merge.py`, with REPO and SCR repointed; `QA10_gate.sh` is the whole run).
It merged the live 248 entries plus B10 and applied the back-links to 27 live entries. I then rebuilt with
`build_knowledge.py --level N2` and ran `check_knowledge.py`.

- **Result: 0 FAIL, 0 WARN, 273 entries.** `check_related_symmetry` reports nothing.
- B10 answer positions are 12/13/13/12, and the merged category is 133/139/139/135. No key position moved.
- The first gate runs FAILed on 12 band overruns, all in my own new text. I trimmed them.

## 1. Blind solve (rule 7)

- `QA10_blind.py` wrote `QA10_blind.txt`: stems and options only, no ids, shuffled with seed 1010. I saved my answers
  to `QA10_myanswers.txt` before I opened `QA10_map.json`.
- **50/50 agree with the keys.** As in B0–B9, agreement proved little. Every finding came from the splice pass, the
  page reads and the scene comparisons.
- I spliced all 150 distractors, then spliced every changed item again after the fixes. Four of my own drafts failed
  that re-check and were changed a second time:
  - nokotodakara Q2 (a manager reading meeting papers) ≈ official 12/2022 問題7-35. Then a friend packing for a move
    ≈ live g-te-ageru Q1. Now it is a report handed in early.
  - kotodashi Q1 (a trip to a hot spring after work) ≈ official 12/2013 問題7-35. Then dinner with the family
    ≈ live g-gurai ex3. Now it is "stay in bed all day tomorrow".
  - koto-naku Q2 (use a camera without reading the manual) ≈ live g-koto-wa-nai ex2. Now it is cooking without
    fire, microwave only.
  - bakarini ex3 (a younger brother saving for a new game) ≈ live g-teshikataganai ex3 and g-tai-garu Q1. Now it is
    a player who hides an injury so he can play the match.

## 2. The authors' flags, judged

| flag | verdict |
|---|---|
| ja: はもちろん 問題8 split cards not counted (7/2025 P8-43, 7/2018 P8-45) | **Upheld (rule 37).** In 7/2025 P8-43, 「小麦粉は」 and 「もちろん」 are two separate cards, so the form has to be assembled. 7/2018 P8-45's card is 「もちろんだが」 after 「日々の練習が」. That is Nがもちろんだ, not はもちろん, so it does not count either way. official_count stays 0 |
| ja: g-koto-naku has no related / compare | **Acceptable.** The schema allows `compare: ""` when `related` is empty. The IV-D row (PDF 139) has no look-alike, and no distractor in the batch glosses ことなく. No change |
| vi: g-ppoi colour sense (白っぽい / 黒っぽい) unattested | **Upheld (rule 27).** A grep of every `refs/**/*.md` finds 0 hits for 白っぽ / 黒っぽ / っぽい色. ex3 is now 「三十歳なのに…どこか子どもっぽい」 (SK 聴解 script 「ちょっと子供っぽいな」). Q2 is now 「中学生だが…大人（っぽく）見える」 (SK 語彙 PDF 133 「大人っぽくなった」). Both sources were added. The ja nuance 「名詞や色につくと」 was rewritten |
| vi: g-gimi Q1 疲れがち killed only by 「今日は朝から少し」 | **Upheld.** The stem now opens 「ふだんはあまり疲れないのに」, which kills the がち (tendency) reading on its own. 向け was replaced by だらけ, which 「少し」 kills (live g-darake). Each option now has its own kill |
| vi: g-ni-koshi Q1 ことはない is a pragmatic kill | **Upheld, and the item also broke rule 16.** ことはない and わけにはいかない both died on 「天気がよくても」. New stem: 「山の天気は変わりやすい。山に登るときは、晴れていても雨具を持っていく（　）」. ことはない ← 「変わりやすい」; ところだった ← 「登るときは」 (a general rule, not a past near-miss, PDF 101); 一方だ ← not a change verb |
| vi: g-ppoi Q1 and Q2 both use だらけ | **Upheld.** Q2 is new (気味に / っぽく / がちに / 向けに). Q1 keeps だらけ, which 「少し」 kills |
| vi: distractor meanings not on a read page (にかわって, かけ, だらけ, に反して, に比べて, につれて) | **4 confirmed, 2 replaced.** Each of these has a live entry that states the meaning the kill needs: かけ = g-fukugou (かける 途中), だらけ = g-darake, に反して = g-ni-hanshite, につれて = g-ni-tsurete. **にかわって and に比べて are in no inventory row and on no page read** → mochiron Q1 にかわって → を問わず (PDF 62 ▲, now in `sources`); mochiron Q2 に比べて → にしては (PDF 96) |

## 3. official_count (rules 4, 10, 12, 19, 37): all 25 re-verified hit by hit

`QA10_hits.py` prints every line of 問題2–9 in all 31 `booklet.md` files that holds any of the batch's forms. Each hit
was then checked against `key.md`. I also grepped every `script.md`, because scripts are sources for scenes.

| entry | shipped → verified | hits (excluded) |
|---|---|---|
| tsutsu-14-4 | 1 ✓ | 12/2019 P8-44 card 「思いつつ」. Excluded: 12/2012-37 「発表しつつ」 is a distractor (key 2) and a 同時 sense; 12/2017-38, 7/2017, 12/2014 and 12/2025 are つつある |
| taimonoda | 0 ✓ | 12/2016 問題9-53 「使用したいものだ」 is a distractor (key 1) |
| kikkake | 0 ✓ | 12/2022 P8-43 「…がきっかけだった」 (a different frame, assembled from cards); 7/2021 問題3 and 7/2010 / 7/2016 問題6 are vocabulary items; 7/2023 and 12/2016 問題9 use it in the passage text only |
| mochiron | 0 ✓ | §2 |
| gimi, ppoi, ppanashi | 0 ✓ each | only 問題2 / 3 / 6 items and 問題9 passage text (7/2013 問題3-14 気味, 7/2014 問題2-6 湿っぽい, 12/2011 問題6 鳴りっぱなし, 12/2022 問題9 座りっぱなし) |
| the other 18 | 0 ✓ each | no 問題7–9 key. The hits are in 読解 or 聴解 text only (に基づく, というものではない, ことなく, に越した, はともかく and ことだし in scripts) |

## 4. Findings

| # | class | severity | surfaces | evidence (abridged) | fix | root cause |
|---|---|---|---|---|---|---|
| F1 | Shin Kanzen example copied with new nouns (rules 3, 13) | **auto** | hatomokaku Q1; kotodashi Q1, ex3; nokotodakara Q2; zujimaida Q2; yarayara Q2; tsutsu ex1, Q1, ex2, Q2; toiumonodehanai Q1, Q2; bakarini ex2, ex3; toiukatoiuka ex1, ex3; mokamawazu ex2; koto-naku Q2 | hatomokaku Q1 「この映画は、話の内容はともかく、音楽が本当にすばらしい」 = PDF 63 ① 「この店は、店の雰囲気はともかく、料理の味は最高だ」. kotodashi Q1 「仕事も早く終わったことだし、…見ていこうかな」 = PDF 88 ② 「雨もやんだことだし、ちょっとジョギングしてこようかな」, and ex3 「給料日のことだし、みんなで…行きませんか」 = ④. nokotodakara Q2 (someone is late → guess where they are) = PDF 88 ③ (太郎の帰りが遅い → 本屋). zujimaida Q2 (moved away before visiting the café) = PDF 101 ③ (went home without travelling). yarayara Q2 「…には、AやらBやら、さまざまな品物が並んでいた」 = PDF 56 ④. tsutsu ex1 / Q1 「〜なければと思いつつ、まだ〜」 = PDF 75 ①, and ex2 / Q2 (says no sweets / on a diet → eats) = ③. toiumonodehanai Q1 「〜ば〜というものではない。…練習が大切だ」 = PDF 67 ③. bakarini ex2 (went out without an umbrella) = PDF 89 ②, and ex3 (travelled far because he wanted to) = ⑤. toiukatoiuka ex1 (a person's good/bad trait pair) = PDF 56 ①. mokamawazu ex2 (children playing outside, ignoring the cold) = PDF 65 練習. koto-naku Q2 「一度も休むことなく…続けている」 = PDF 139 ① | new scenes: ほかの人はともかく、君だけは時間を守って; 仕事も片づいたことだし、明日は寝ていたい; 娘ももう大学生のことだし; 何でも早めにやる田中さん → レポート; 限定ケーキ、販売終了; 娘の部屋 → 足の踏み場もない; 課長「残業を減らそう」; 悪いとは思いつつ日記を; 無駄づかい → セール; 夜ふかし; 有名な先生に習えば; 新しいパソコン; 駅の階段で急いだ; 試合に出たい → けがを隠す; 明るいというか派手; 懐かしいというか落ち着く; 歌手 → 薄いドレス; 火を使うことなく | RULE-IGNORED (rules 3, 13). The provenance scan is by 10-char windows, so it cannot see a frame. The page compare the rules ask for was not done (R1) |
| F2 | official scene reused (rule 21) | **auto** | kotodashi Q2; hatomokaku Q1 | kotodashi Q2 (「みんな疲れていることだし、片づけは明日にしよう」) = 12/2014 script 「明日も早いことだし、今日の作業はこれで切り上げよう」. The entry cites this line in its own `sources`. hatomokaku Q1 ≈ 12/2020 script 「歌うまかったよ。ダンスはともかくとして」, 12/2015 script 「サービスはともかく店の雰囲気はいい」 and 7/2018 script (設備 / サービス) | kotodashi Q2 → 「荷物も多いことだし、タクシーで行こうよ」; hatomokaku Q1 → F1 | RULE-IGNORED (rule 21 names `script.md`). Again the entry's **own cited** line |
| F3 | example ↔ quiz, same scene + predicate (rule 11) | 要修正 | yarayara ex1 / Q1; tsutsu ex2 / Q2 (and Q2 ≈ live g-towa-iinagara ex2 「ダイエット中とはいいながら、甘いもの…」); umononara ex1 / Q1; dakearu ex2 / Q2; zujimaida ex2 / Q1; taimonoda ex3 / Q2; koto-naku ex2 / Q2; ppoi ex2 / Q1; ni-motozu-ite ex1 / Q1 | busy → 暇もない / 時間もなかった; diet → sweets ×2; a family elder angered over food ×2; 「さすが…店だけある」 about the food ×2; an unread book ×2; 「子どもたちには〜てほしいものだ」 ×2; non-stop operation ×2; watery soup ×2; 「に基づいて〜が決められている」 ×2 | new examples (せきやら熱やら; 居眠り → 宿題を倍; 「星の村」; カメラを一度も使わず; 古い映画館を残して; 手紙が五十年; 押し入れが湿っぽい; 献立が作られている) | RULE-IGNORED (rule 11). `QA9_cross.py` compares a batch only with *other* entries, not an entry's examples with its own quiz (R2) |
| F4 | one kill clause shared (rules 16, 33) | 要修正 | kotodashi Q1, Q2; ni-koshi Q1; ppanashi Q1; zujimaida Q2 | kotodashi Q1: ばかりに and ものの are both on PDF 146 IV-G 1b (no 希望・意向 after), and both died on 「見ていこうかな」. Q2: おかげで and とたん are both in 1b and both died on 「しようよ」. ni-koshi Q1: §2. ppanashi Q1: 気味 and がち both died on 「三時間ずっと」. zujimaida Q2: 済んだ and までもなかった both died on 「残念」 | kotodashi Q1 → ばかりに / わりに (PDF 96 ▲) / くせに; Q2 → おかげで / ついでに / 一方で; ppanashi Q1 気味 → かけ (dies on 「ずっと」), and がち now dies on 「コンサートの間」; zujimaida Q2 → 食べるわけがなかった (dies on 「食べようと思っていた」) | RULE-IGNORED (rule 33 names this exact shape). No tally was handed in (R3) |
| F5 | two syntax kills in one item (rule 8) | 要修正 | gimi Q2 | がたい＋で and ます形＋次第＋で are both ungrammatical | 次第 → 向け (a meaning kill: live g-muke-da) | RULE-IGNORED |
| F6 | sense on no cited page (rule 27) | 要修正 | ppoi ex3, Q2, ja nuance | §2 | §2 | RULE-IGNORED (the vi author flagged it, but it was not fixed before hand-off: rule 23) |
| F7 | distractor whose kill is on no page (rules 8, 9) | 要修正 | mochiron Q1, Q2 | §2 | §2 | RULE-MISSING: nothing says a distractor must be an inventoried form (R4) |
| F8 | meaning not copied literally (rule 5) | 要修正 | ja meaning of toiumonodehanai, tsutsu-14-4, nokotodakara, bakarini, zujimaida | e.g. tsutsu 「〜と思ったり言ったりしているのに」 against PDF 75 「〜という心の動きとは、行動が違っている」; nokotodakara 「様子」 against the page's 「態度」; bakarini 「ただ…思ってもいなかった」 against 「予期しない」 | copied from the page (bakarini keeps the first half, and its usage carries the たいばかりに sense) | RULE-IGNORED |
| F9 | restriction widened (rule 15) | 要修正 | ja dakearu nuance; ja umononara compare + back-link g-mononara | PDF 96's ▲ 「未来や推量を表す文は来ない」 applies to 「〜だけあって」 only, but the nuance applied it to the whole pattern. PDF 78 says ものなら takes 「可能の意味を表す動詞」, but the prose said 「辞書形（多くは可能形）」 | the nuance now scopes the ▲ to だけあって; both compares now say 「可能の意味の動詞の辞書形」 | RULE-IGNORED |
| F10 | textbook sentence in prose (rule 32) | note | ja udehanaika nuance | it copied PDF 118's ▲ word for word (「強く誘いかける男性的な言い方で、政治家の演説などに見られる。日常の会話ではあまり使わない」) | reworded; the same facts, still sourced | RULE-IGNORED |
| F11 | furigana | 要修正 | ja umononara compare; back-link g-mononara | 「｜可能《かのう》｜形《かたち》」: in 可能形, 形 is read けい | 「可能の意味の動詞の辞書形」 (F9) | GATE-BLIND (R5) |
| F12 | back-link dropped a live contrast | 要修正 | g-rashii (ja: どうも〜らしい, そうだ（様態）); g-ni-chigai-nai (ja: まさか); g-wake-dewa-nai (ja: わけにはいかない, からといって; vi: からといって); g-nagara-mo (ja: ながら's connection); g-nimokakawarazu (ja: 「にも」がない形); g-bekida (vi: べきだった ↔ ことだ has no past form) | the back-link value replaces the live compare wholesale, so each of these contrasts would have disappeared at merge | restored within the band. The four entries the brief named were checked against the CURRENT live text: g-ni-sotte, g-zu-ni-sumu and g-monoka keep every live contrast; g-rashii did not, and is fixed | RULE-MISSING (R6) |
| F13 | vi rule 6 | note | vi ni-motozu-ite nuance | a bare 「基」 | quoted | RULE-IGNORED |
| F14 | explanation targets | — | all 21 changed items | — | both panes rewritten per item, the vi one from the item. In all 21, vi targets a different distractor from ja | — |

**Checked and not findings**

- **SK pages read** (my own renders, `QA10_pages/`): PDF 48, 56, 62, 63, 65, 67, 75, 78, 79, 88, 89, 96, 101, 110,
  115, 118, 126, 127, 139, 146.
  - 接続 matches the page literally for all 19 SK entries, (な)/である included. This covers ことだし (名 の / である),
    ばかりに (名 である), だけ（のことは）ある (＊名だ never) and はともかく (普通形現在 ＋ の).
  - The ▲ restrictions quoted in the prose match the page: もかまわず 1b, とみえる 2b, たいものだ 2a, ずじまい 3a and
    だけある 3b (all on PDF 146), and PDF 118 for (よ)うではないか.
- **Rule 22:** no key is printed as a wrong option in an equivalent official frame.
- **Provenance** (`QA9_prov.py`, 10-char windows with the key spliced in, over `refs/**/*.md` including every
  `script.md`, and `tests/imported-*`). I ran it before and after the fixes. The hits left are stock phrases:
  というものではない。, とてもわかりやすい。, どのくらいいるのか、, 落ち着いているので、.
- **Bigram scan against every official 問題7–9 item** (`QA9_bigram.py`). I read every hit at ≥2 shared bigrams for the
  changed texts. The two real hits were my own drafts (§1) and were changed. What is left shares nouns only
  (天気予報, 就職活動, 高校時代).
- **Category- and module-wide scene scan** (`QA10_cross.py` / `QA10_cross2.py`: B10 against live 文法, 語彙, 漢字 and
  the open B11, ≥2 bigrams, read-only for B11). After the fixes, the hits share nouns only (パソコン, タクシー, 約束の時間).
- **Furigana:** I hand-read every new string (e.g. 夜《よ》ふかし, 雨具《あまぐ》, 三十分《さんじゅっぷん》,
  三十歳《さんじゅっさい》, 五十年間《ごじゅうねんかん》). The gate's `check_ruby_suspects` and
  `check_prose_citations` are clean.
- **Headwords and ids:** no B10 headword duplicates a live entry or B11. Every `related` id resolves at merge. The
  `book` keys match the inventory.

## 5. Root causes and proposed edits

| findings | code | recurrence | proposed edit |
|---|---|---|---|
| F1 | RULE-IGNORED + a procedure gap | B4, B8, B9, B10. B10 has 19 surfaces | **R1 (BATCH_JA_BRIEF, required hand-off column):** "For every example and every stem, write the closest numbered example on the cited SK page (and its 練習 items) as '① scene → predicate', and one line saying how yours differs. A frame shared with ① is a copy even when every noun is new." This is the 'scene of every official item' column rule 37 already requires, applied to the SK page. B10's 19 copies all sat on a page the entry cites |
| F2 | RULE-IGNORED | B5, B9, B10: each time a line from the entry's **own** `sources` | **R1 (same column):** list the entry's own cited script / 読解 lines too. Rule 21 is specific, and the column makes it checkable |
| F3 | RULE-IGNORED + PIPELINE-GAP | B4, B5, B8, B9, B10 | **R2 (tool, `QA9_cross.py`):** also compare each entry's examples with its **own** quiz stems (the script skips the entry's own batch). Founding cases: the 9 F3 pairs, e.g. yarayara ex1 / Q1 and ppoi ex2 / Q1. It should also scan 語彙 / 漢字 (rule 35 is module-wide), as `QA10_cross2.py` does |
| F4 | RULE-IGNORED | B6, B8, B9, B10 | **R3 (BATCH_JA_BRIEF):** "Before you put two conjunctions in one option set, look them up on PDF 146 (IV-G). Two from the same row (1a / 1b / 1c / 3a …) share one kill clause whenever the main clause is the thing that row restricts." kotodashi Q1 and Q2 each paired two 1b forms |
| F7 | RULE-MISSING | first recorded instance | **R4 (SKILL §Quiz integrity, rule 38):** "Every 文法 distractor is a form with a live entry or an inventory row, so its meaning is on a page. A form with neither is replaced (B10 mochiron: にかわって, に比べて)." |
| F11 | GATE-BLIND | first instance | **R5 (gate, `check_ruby_suspects`, WARN):** 「形《かたち》」 directly after a ruby'd grammar term (可能 / 意向 / 辞書 / ない / て / 連用 …). Founding string: `｜可能《かのう》｜形《かたち》` in B10 umononara compare. I did not build it (reviewers do not edit the gate) |
| F12 | RULE-MISSING | B9 and B10 back-link passes | **R6 (merge_batch.py, review aid):** before applying a back-link, print every 「…」-quoted form in the old live compare that is missing from the new one. I ran this predicate on B10: before the fixes it flagged 15 targets and caught all 6 real losses. The other 9 were wording trims or examples that were dropped on purpose. So make it a printed list the reviewer must answer, not a FAIL |
| F5, F6, F8, F9, F10, F13 | RULE-IGNORED (rules 8, 27, 5, 15, 32, 6) | B2–B10 | none. F6 was flagged by its author and still handed in (rule 23) |

## 6. Coverage and skips

- Blind solve on all 50 items. I spliced all 150 distractors, and spliced all 21 changed items again after the fixes.
- official_count re-verified for all 25 entries.
- SK pages: 20 read. The 接続 and meaning of all 19 SK entries were compared with the page.
- Provenance, the official bigram scan and the category-wide scene scan were each run before and after the fixes.
- Back-links: all 27 old → new pairs read in both languages, each against the current live compare.
- Gate: live 248 + B10 merged in scratch with the back-links, rebuilt, `check_knowledge.py` → 0 FAIL, 0 WARN.
- **Skipped:**
  - `make check` / `make knowledge` on the real tree. The coordinator merges, and I must not touch `knowledge/`.
  - B11 was read only, for the scene scan.
  - Speech and pitch (the 文法 pitch flag is off).
  - The untracked `CLAUDE_YOU_MUST_READ_THIS.md` asks for 語彙 / 漢字 work outside this brief. I did not act on it.
- **For the coordinator:**
  - B11 has `related` links into B10: g-dake-atte → g-dakearu, g-dano → g-yarayara, g-dano → g-toiukatoiuka. Its
    back-link compares for those three must be written from the **post-QA** B10 prose, because the back-link value
    replaces the compare wholesale.
  - g-dakearu's nuance now scopes the PDF 96 ▲ to 「〜だけあって」, which B11 makes its own entry.
