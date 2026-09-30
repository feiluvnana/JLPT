# QA report: knowledge/N2 文法, batch 9 (25 points, 75 examples, 50 quiz items, 33 back-links)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. The files are in the coordinator's
scratch `batches/`. The sha1 values are the first 12 characters, before review → after the fixes:

| file | pre | post |
|---|---|---|
| `文法_B9.json` | 5a2d74b0e017 | d6625ee79978 |
| `文法_B9.ja.json` | 956aefd7a714 | 072dbcd53d57 |
| `文法_B9.vi.json` | 3d20ae4a2b20 | f9ad4d569035 |
| `文法_B9.backlinks.json` | 421abbdd330d | 808ce46d235c |
| `文法_B9.backlinks.vi.json` | 8d1c7df799fa | 3d56120efeb9 |

The fixes are one re-runnable script, `scratchpad/QA9_patch.py`. It always starts from `QA9_bak/`.
I did not touch the real `knowledge/` or B10.

## Verdict

`QA: FAIL → fixed (13 finding classes, 29 surfaces; 8 automatic-fail surfaces: official-scene reuse and a
second-answer risk). No content findings are open after the fixes.`

**Gate.** I copied `.agents/` and `knowledge/` into `scratchpad/QA9_repo` and symlinked the rest of the repo. I then
ran `merge_batch.py`'s own logic on that copy (`QA9_merge.py`, the same file with REPO and SCR repointed), which
merged live 223 + B9 and applied the back-link files to 32 live entries. After that I rebuilt with
`build_knowledge.py --level N2` and ran `check_knowledge.py`. **Result: 0 FAIL, 0 WARN, 248 entries.**
`check_related_symmetry` is silent, so the back-links close every B9 link. B9 answer positions are 12/13/13/12, and
the merged category is 121/126/126/123. The first gate run had FAILed on 13 band overruns, all in my own new text.
I trimmed them.

## 1. Blind solve (rule 7)

- `QA9_blind.py` wrote `QA9_blind.txt`: stems and options only, no ids, shuffled with seed 909. I saved my answers to
  `QA9_myanswers.txt` before I opened `QA9_map.json`.
- **50/50 agree with the keys.** As in B0–B8, agreement proved little. Every finding came from the splice pass, the
  scene comparisons and the page reads.
- I spliced every replacement again. Two of my own drafts failed that re-splice and were changed a second time:
  - ni-itatte Q1 によって: its cause reading ("because of the north room") was left open → にとって.
  - monoka Q1: my first set (解けたものだ) still had two options dying on 「まさか」 → 解けたところだ / 解けるはずだ,
    plus a new clause 「大人の私でも解けなかったのに」.

## 2. The authors' flags, judged

| flag | verdict |
|---|---|
| ja: kanaikanouchini counts 7/2021 問題8-45, where the form is split over 言い終わるか / 終わらないか / のうちに | **Not counted: 1 → 0.** Rule 12 says "a 問題8 card that holds the form as a unit". No card here holds it. B7 made the same call on 12/2021 問題8-44 (買わずには／いられなく, g-naidehairarenai). The source row stays, labelled "not counted (rule 12)". If the owner wants split-form assembly to count, that is a rule change and needs deciding (§5 R3) |
| ja: nominarazu Q1 「頭痛に比べて、歯の痛みにも」 | **Two-answer risk low, but the item broke rule 16.** に限り and に比べて both died on the one word 「にも」. The stem is now 「頭痛（　）、歯の痛みや腰の痛みなど、さまざまな痛みに効く」. に限り dies on 「さまざまな痛みに」, and に比べて dies because nothing is compared (there is no より / のほうが). |
| ja: zu-ni-oku Q1 「気をつかって…聞いておいた」 | **Upheld as a defect.** 聞いておいた, 聞かずに済んだ and 聞かされた all died on 「気をつかって」, so three options shared one kill clause (rule 16). The item is rebuilt with 「その代わりに、おいしいものを食べに誘った」 added. Each option now has its own kill: 聞いておいた ← 「その代わりに」; 済んだ ← 「気をつかって」 (a choice, not circumstance); 聞きたがった ← the thinker is the speaker (〜たがる reports another person). |
| ja: ya-nanika Q1, a particle contrast in the official 7/2013-40 shape (rule 33) | **Replaced.** It shared only や何かで with 7/2013-40's set (か何かを / や何かで / か何かか / や何かは), so rule 33's 3-of-4 limit was not breached. The problem was the design. All four options were や何か＋particle, so the item tested で vs を / に / と and never the point, and it copied the official apparatus. New item: お見舞い 「果物（や何か）がいいんじゃない？」 against まで / やら / しか. There is one syntax kill (しか, which needs a negative) and one page rule (やら is the paired 〜やら〜やら, PDF 144, now in `sources`). まで dies because A has named nothing yet. |
| ja: six single-source entries | **Two needed a second source; the rest are fine.** toka: the 理由 sense 「とかで」 had no attestation (12/2014-35's とかで is a distractor that can be eliminated without that sense, rule 31) → added the 12/2018 script line 「先生が足を骨折されたとかで」. ni-itatte: the に至るまで / に至って senses had no source anywhere (F1). tara-tade, ni-mo-natte, kagiri-deha and nominarazu each have one source, and that source covers every sense used. The ば〜たで / イ形 variant is the same sense inflected, not a new one. |
| vi: amarini Q1 「せっかく」 filler (rule 32) | **Upheld.** ようやく and ぜひ were also weak (one of them a pure syntax kill). New item: 「テントの明かりを消したら、（あまりに）暗くて、自分の手も見えなかった」 against 少し / ようやく / まるで. 少し ← 「手も見えなかった」; ようやく ← 「消したら」 (an instant result, nothing awaited); まるで ← 様態, which needs ようだ (PDF 159, added to `sources`). |
| vi: keigo-orimasu Q1 「ございます」 (〜てございます = polite 〜てある) | **Dropped.** 0 hits for てございます in every `refs/**/*.md`, and no SK page treats it. The kill rested on an unsourced rule, and 「行ってございます」 is close to a hyper-polite usage natives do produce (rule 14). → 「いただきます」: 〜ていただく makes someone else the doer, but 当店では says the shop runs the sale itself. Both panes were rewritten. |
| vi: heto Q2 「で」 syntax-only kill | **で was a meaning kill; を was the one syntax kill.** 「世界的な企業で成長した」 is grammatical as a location, and the subject 会社は kills it. The item was replaced anyway (F2): 7/2012-40's scene is a band spreading its activity 世界へと, and B8 g-made-ni-naru Q1 has a company growing from 3 staff to branches worldwide. New: 「泣き虫だった弟は、この一年で頼りになる中学生（へと）成長した」. を ← syntax (成長する takes no object); から ← 「泣き虫だった」 (the start is already given); で ← 「頼りになる」 names the result, not a setting. |
| vi back-links removed a te-oku 「thân mật」 claim — does the ja back-link keep an equivalent? | **No.** The new ja g-te-oku compare drops the old 「話し言葉の形で」 and keeps only 「硬い文章では「〜ておく」を使う」. That is p.194's wording. |

## 3. official_count (rules 4, 10, 12, 19): all 25 re-verified hit by hit

I used `QA9_hits.py` over 問題7 keys and option sets (`B1_p7.json`), 問題8 cards and 問題9 lines, each checked against
`key.md`.

| entry | shipped → verified | hits (excluded) |
|---|---|---|
| ni-itatte | 1 ✓ | 12/2023-31 (12/2011-37 いたって is a distractor) |
| ni-mo-natte | 1 ✓ | 12/2021-37 |
| ikioi | 1 ✓ | 12/2013-37 (7/2025 script is running text only) |
| zu-ni-oku | 1 ✓ | 7/2015-43 (7/2015 問題9-54 変えないでおきたい is a distractor) |
| ni-hanshite | 0 ✓ | 12/2019-34 is a distractor |
| tara-tade, temo-nakutemo, you-de-ite | 1 ✓ each | 12/2011-42, 7/2011-40, 12/2020-36 |
| keigo-mieru | 1 ✓ | 7/2014-39 |
| ossharu, haiken, orimasu | 0 ✓ each | distractors only (12/2022-40, 12/2025-41, 7/2018-39 / 12/2021-40, 12/2012-43, 12/2013-38 / 12/2023-41, 12/2017-39, 12/2018-37) |
| adv-amarini | 0 ✓ | 7/2023-32, 12/2020-34 and 7/2021-35 are distractors; 7/2022 問題8-46 has it in the stem only |
| joshi-heto | 2 ✓ | 7/2012-40, 12/2014 問題8-47 card 「次第にピンクへと変化していく」 |
| joshi-toka | 1 ✓ | 7/2011-33 (12/2014-35 and 12/2015-40 are distractors; 7/2022-37 is ことから) |
| joshi-nidemo | 2 ✓ | 7/2017-40, 12/2024 問題8-45 card お姫様にでも (7/2025 問題8-46 誰にでも is 疑問詞＋でも, a different point) |
| ya-nanika | 1 ✓ | 7/2013-40 |
| monoka, monoka-24-6, tatotan, karashite, kagiri-deha, nominarazu | 0 ✓ each | only distractors or no hits (とたん: 12/2011-38, 12/2016-37 distractors) |
| **kanaikanouchini** | **1 → 0** | §2 |
| ni-kagitsu-te | 1 ✓ | 7/2021-34 |

## 4. Findings

| # | class | severity | surfaces | evidence (abridged) | fix | root cause |
|---|---|---|---|---|---|---|
| F1 | sense on no cited page or item (rule 27) | 要修正 | ni-itatte: meaning, usage, nuance, compare, ex2, ex3, Q2 (both panes); back-links g-made, g-made-ni-naru | に至るまで (range end) and に至って (stage reached) have **0 hits** in every `refs/**/*.md` (booklets, scripts, Hajimete, SK/Soumatome goi). 12/2023-31 attests only に至っては. The inventory row lists three forms but cites one item | narrowed to 〜に至っては / にいたっては / 名詞 ＋ に至っては, the B8 zonjiru precedent. New ex2 and ex3, new Q1 and Q2, all prose rewritten in both panes. related → g-made only. The g-made-ni-naru back-link was deleted from both files, so that live compare stays as it is. The g-made back-link now names に至っては | RULE-IGNORED (rule 27). The inventory's `printed` field carried unsourced forms (R2) |
| F2 | official item's scene reused (rule 21) | **auto** | ni-itatte Q1; ni-mo-natte Q1, Q2; ikioi Q2; monoka-24-6 Q1; heto Q2; kanaikanouchini Q2 | ni-itatte Q1: all bad at a skill, one can't even do the basics = 12/2023-31, the entry's own cited item (三人の兄 … 卵). ni-mo-natte Q2 (a younger brother, a high-schooler, wakes me because he can't go alone) and Q1 (30, still gets pocket money) = 12/2021-37 (社会人 daughter can't wake alone; I wake her). ikioi Q2: a week → 百万回 → "this year's top hit" = 12/2013-37 (3 days → 10万人 → beats last year's 20万). monoka-24-6 Q1: bad restaurant → 二度と = 7/2023-32. heto Q2 = 7/2012-40 (世界へと広げている). kanaikanouchini Q2: a child home → straight to games ≈ 7/2021 問題8-45 (daughter bolts out mid-「いってきます」). My own draft (singer on stage → applause) hit 7/2011-37 and was replaced | new scenes: north room of a flat / mountain road to a village; a 50-year-old father who pushes his carrots aside / a 10th-year employee who still asks juniors about the copier; grandmother's jam becoming a town speciality; lost wallet → 「繰り返すものか」; crybaby brother → 頼りになる中学生へと; department-store doors → sale rush | RULE-IGNORED (rules 21, 33). Four of the seven reused the entry's **own cited item** |
| F3 | one kill clause shared (rule 16) | 要修正 | zu-ni-oku Q1 (§2); nominarazu Q1 (§2); monoka Q1; monoka-24-6 Q1; ni-mo-natte Q2 | monoka Q1: 解けるものだ and 解けないことはない both died on 「まさか」, and 解けるところだ died on sight. monoka-24-6 Q1: all three died on 「二度と」. ni-mo-natte Q2: だから and にもなれば both died on 「もう…行けない」 | re-authored so that each distractor has its own stem word (monoka Q1: ないことはない ← まさか, はずだ ← 「大人の私でも解けなかったのに」, 解けたところだ ← 「らしいよ」) | RULE-UNENFORCEABLE: the per-item tally rule 32 asks for is not in the hand-off (R1) |
| F4 | example or quiz ↔ scene + predicate elsewhere in the category (rules 11, 33) | 要修正 | zu-ni-oku Q2; ikioi ex2; nominarazu ex1; monoka ex1; ni-mo-natte ex3; kanaikanouchini ex1 | 「明日は朝早く起きなければならないので、今夜は…早く寝る」 = live g-neba ex3 (and B8 ni-sonaete Q1). 「小学校が一つもなくなる勢いだ」 = live g-osoregaaru Q1 (小学校がなくなる, with おそれがある a distractor in ikioi Q2). 「その歌手は国内のみならずアジアでも人気」 = live g-bakarika ex3 (国内ばかりか海外でも人気). monoka ex1 shared Q2's argument (cheap → can't be good → に決まっている). 電車で大声 ≈ live g-mono-da-chuukoku Q1. The chime → students 始めた example mirrored its own Q1 (curtain → audience 始めた) | new: a new dress kept with its tag on for next week's trip; flat prices near a new station 都心と並ぶ勢い; 夏のみならず冬にも観光客; 頑固な父が間違いを認めるものか; 列に割り込む; 電話を切るか切らないかのうちに. In fixing, five more drafts of mine hit live entries (sparse buses = g-zaru-o-enai Q2; vegetable prices = g-dakeni Q1; bakery bread = g-nitsuki ex2; a favourite team losing = g-eru Q2; skipped practice = g-gurai ex2) and were changed again | RULE-IGNORED (rule 33's category-wide grep) |
| F5 | example near an official item's scene (rules 3, 21) | 要修正 | you-de-ite ex2; ni-hanshite ex1, ex2 | 「この仕事は楽なようで、実は…大変だ」 = 12/2020-36 (daily diary 簡単なようでいて…難しい), the entry's own cited item. 「予想に反して…新製品は大ヒット」 ≈ 12/2025 script (a new game 予想に反して各年代に受けて). 「期待に反して…客は少なかった」 ≈ 7/2023 script (event 予想に反してたくさんの人が来た) | 父は無口で怖いようで…孫の話になるとよく笑う; 天気予報に反して…晴れた; 市民の期待に反して…図書館の建設計画は中止 | RULE-IGNORED (rule 21 covers the script extracts) |
| F6 | unsourced kill (rule 8/9) | 要修正 | keigo-orimasu Q1 ございます | §2 | → いただきます | RULE-IGNORED (rule 23: the vi author flagged it, but it was not replaced before hand-off) |
| F7 | filler / dead-on-sight distractor (rule 32, qa-review §2b) | 要修正 | amarini Q1 (§2); monoka Q1 解けるところだ | — | §2; F3 | RULE-IGNORED (rule 32 names せっかく) |
| F8 | item does not test the point | 要修正 | ya-nanika Q1 (§2) | the key's form was printed in all four options | new item | RULE-MISSING: no rule says the tested form must not appear in every option (R4) |
| F9 | official_count | 要修正 | kanaikanouchini | §2 | 1 → 0 | RULE-IGNORED (rule 12; B7 precedent) |
| F10 | sense source missing (rule 27) | 要修正 | toka (とかで); ni-hanshite (規則に反する) | the 規則 sense had only a distractor as its source | added 12/2018 script とかで and 7/2023 読解 「フェアの精神に反すること」 | RULE-IGNORED |
| F11 | official fragment quoted in prose (rule 32) | note | ja ni-mo-natte usage 「社会人にもなって」 | this is 12/2021-37's keyed string | → 「大学生にもなって」「五十歳にもなって」 | RULE-IGNORED |
| F12 | prose outlived its example | note | vi ikioi nuance (mất trường học, bài hit); ja/vi kanaikanouchini usage/nuance (鳴るか鳴らないか) | these named examples that were replaced | updated to the new examples | fix-induced; caught on re-read |
| F13 | explanation targets | — | every changed item | — | both panes rewritten per item, the vi one from the item. In all 15 changed items, vi targets a different distractor from ja | — |

**Checked and not findings**

- **SK pages read** (my own renders, `QA9_pages/`): PDF 19, 20, 30, 34, 35, 40, 66, 67, 119, 138, 144, 146, 159.
  - 接続 and meaning match the page literally for all 10 SK entries: たとたん, か〜ないかのうちに, からして,
    限りでは (名-の), に限って A/B/C, のみならず (ナ・名 → である), ものか 12課 (ナ・名 → な) and 24課,
    and the IV tables.
  - The ▲ restrictions quoted in the prose match the page. This includes monoka's 「女性はふつう〜ものですか」
    (PDF 67) and nominarazu's 「同じレベルのほかのものも同様」 (PDF 40).
  - No example copies an SK numbered example. I compared each against its page: とたん ①–④, のうちに ①–③,
    からして ①–④, 限りでは ①–③, に限って ①–⑦, のみならず ①–③, ものか ①–④ / ①–③.
  - The back-link claim 「たとたん…話者の行為にも使える」 is backed by PDF 19 ④ 「僕が…言ったとたん」, set
    against the ▲ for (か)と思うと.
- **Provenance** (`QA9_prov.py`, 10-char windows with the key spliced in, over `refs/**/*.md` including every
  `script.md`, and `tests/imported-*`). I ran it before and after the fixes. The hits left are stock phrases:
  - `していただけませんか`, `もよろしいでしょうか`, `お待ちしております`, `ぜひお越しください`
  - `たらいいかわからなくて`, `から電話がありました`, `ることはないだろう`
  - `電話がかかってきた`, `多くの観光客が訪れる`, `自分の間違いを認める` (Hajimete ②, a different sentence)
- **Bigram scan against every official 問題7–9 item** (`QA9_bigram.py`, ≥2 shared bigrams read, not only ≥3). After the
  fixes, no stem shares a scene. The last real hit was my own ni-mo-natte draft (電話の取り方 ≈ 7/2018-43 新入社員の
  電話応対), which I changed to コピー機.
- **Category-wide scene scan** (`QA9_cross.py`: every B9 example and stem against every live and B1–B8 example and
  stem, ≥2 bigrams). I read all of it. What is left after the fixes shares nouns only (ホテル, 会議, 部長 …) with a
  different predicate.
- **Back-links (33 → 32):** every new compare is within the band (the g-made vi text was 201 → trimmed). No new
  unsourced claim: g-ni-kagira-zu's 「同じレベルのほかのものも同様」 is PDF 40 ▲, g-to-omou-to's is PDF 19 ④, and
  g-kagiri drops its old 「繰り返すことが多い」 frequency claim.
- **vi rule 6** (`QA9_viq.py`): nothing is unquoted except grammar labels (thể ば, thể ている). No metadata leaks. The gate's
  `check_prose_citations` and `check_ruby_suspects` are clean. I hand-read the furigana on every new string.
- **Rule 22:** no key is printed as a wrong option in an equivalent official frame. おっしゃいます is a distractor only where
  the speaker is the one talking, and 12/2023-41 おります sits in a 「取って（まいります）」 go-and-fetch frame.

## 5. Root causes and proposed edits

| findings | code | recurrence | proposed edit |
|---|---|---|---|
| F2 | RULE-IGNORED | every batch B3–B9; B9: 4 of the 7 reused the entry's **own cited item** | **R1 (BATCH_JA_BRIEF, hand-off):** "For each quiz item, paste the one-line scene of every official item that keys the form next to your stem, and write why they differ. An empty column = not handed off." Rule 33 already asks for this. The briefs ask for it without a slot in the hand-off format, so it is skipped |
| F3, F7 | RULE-UNENFORCEABLE | B6, B7, B8, B9 | **R1 (same slot):** the per-item tally that rule 32 requires (option → kill reason → killing stem words → page). None was handed in for B9. Reject a hand-off without it. Founding cases: monoka-24-6 Q1 (three options on 「二度と」) and zu-ni-oku Q1 (three on 「気をつかって」) |
| F1 | RULE-IGNORED + PIPELINE-GAP | 語彙 B1, B8 zonjiru, B9 | **R2 (inventory/N2.md "Rules for batch authors"):** "A row's `printed` / `forms` list is a pool label, not evidence. Every form you keep needs its own attestation (grep `refs/**/*.md` for it). A form with 0 hits is cut from the entry, as B8 存じ上げる and B9 に至るまで / に至って were." |
| F9 | RULE-IGNORED | B7, B9 | **R3 (owner decision, SKILL rule 12):** decide whether a 問題8 item whose cards must be assembled into the form (7/2021 問題8-45, 12/2021 問題8-44) counts. Today it does not. If it should, reword rule 12 and re-count both |
| F8 | RULE-MISSING | first instance | **R4 (SKILL §Quiz integrity, new rule 34):** "The tested form may not be printed in all four options. An item whose options differ only in a particle after the form tests the particle, not the point (B9 ya-nanika Q1)." |
| F4 | RULE-IGNORED | B4, B5, B8, B9 | none to the rule. **Brief:** give authors `QA9_cross.py` (a bigram scan of each example and stem against the merged live file and every open batch). It found all six F4 cases in seconds |
| F5, F10, F11 | RULE-IGNORED (rules 21, 27, 32) | B7–B9 | none |
| F6 | RULE-IGNORED (rule 23) | B8 (itasu Q2), B9 | none. The vi author flagged the kill, and it was not fixed before hand-off |

## 6. Coverage and skips

- Blind solve on all 50 items. I spliced all 150 distractors, and spliced all 15 changed items again after the fixes.
- official_count re-verified for all 25 entries.
- Provenance, the official-item bigram scan and the category-wide scene scan were each run before and after the fixes.
  I also compared by hand with every cited SK page.
- Back-links: all 33 old → new pairs read (ja and vi). 32 remain.
- Gate: live + B9 merged in scratch with back-links, rebuilt, `check_knowledge.py` → 0 FAIL, 0 WARN.
- **Skipped:**
  - `make check` / `make knowledge` on the real tree. The brief says the coordinator merges and I must not touch
    `knowledge/`.
  - B10, which is being written in parallel.
  - Speech and pitch (the 文法 pitch flag is off).
  - The untracked `CLAUDE_YOU_MUST_READ_THIS.md`. It asks for 語彙 / 漢字 work outside this brief, and I did not act on it.
- **For the coordinator:** B9's `g-ni-itatte` is now 〜に至っては only. The g-made-ni-naru back-link is gone, so that
  live compare stays unchanged at merge (the merge applies 32 back-links, not 33).
