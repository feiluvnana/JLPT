# QA — 知識 語彙 batch 12 (Hajimete No.311–384)

Fresh-eyes reviewer (wrote none of the batch). One Sonnet author wrote both panes. Checked against live at 3acc400 (B11 merged).
69 entries. 5 numbers were dropped because they are already live cards: 319 薄める, 333 もてなす, 335 ごちゃごちゃ, 341 素材, 378 さっさと.
After QA: 15 back-links (the author's 12, plus 要求, さっさと and ばらす) and 8 live meaning fixes (3 of them revised).
Pre-review copies: `scratchpad/QAV12_bak/`. `QAV12_patch.py` and `QAV12_patch2.py` hold the fixes, plus two small trims made inline.
sha1 (first 12 characters), pre → post:

| file | pre | post |
| - | - | - |
| `.json` | 00ae075c9fb7 | 7b56018981b4 |
| `.ja` | cf039b1e3796 | b0f7fd838c25 |
| `.vi` | d3fcdeab4604 | cab0b431e575 |
| `.backlinks` | 22eb4f231c58 | e0783edd79f3 |
| `.backlinks.vi` | 607b5e86ed16 | dfd0cbf2b8d8 |
| `V12_live_meaning_fix` | 7063fc9cdc70 | fa7d31909829 |

## Checks run
- `batch_tool stats / frames / lures / rebase / gate`, before and after the fixes. I also ran a relaxed scene scan (`QAV12_scene.py`) and read all 138 examples by hand.
- Hajimete PDF pp.65, 67–71 and 73–77 checked against about 45 entries: ids, readings, pos, senses and VI lines.
- Page citations for No.363–384 are correct. 363–369 are on p.73, and PDF p.74 is a duplicate scan of p.73 (confirmed). 370–375 are on p.75, 376–381 on p.76 and 382–384 on p.77.
- official_count: もれる = 1 (12/2021 問題6-28 「漏れる」, key 3). Confirmed.
  - I grepped all 954 official 問題1–9 items for every headword and stem. No keyed hit was missed.
  - Every hit that does not count (a distractor or stem-only appearance) is already in `sources` and marked 「数えない」.

## Findings and fixes
| # | Finding | Fix | Root cause |
| - | - | - | - |
| 1 | **14 wrong furigana readings.** The worst is 分別 read ふんべつ seven times (the book prints ぶんべつ). The others: 応援旗 read as はた, 模様替《もようがえ》え, 呼び鈴 read すず, ほうれん草 read くさ, 根元 split, 印 read いん, 留める read とど (ja and vi), 名 read めい, 儲け話 read はなし, 鉢植《はちうえ》え, 頃 read ごろ, やり方 read ほう (twice), 陰 read いん. | All fixed. | Sonnet guessed on-readings and okurigana spans. `check_ruby_suspects` only knows the patterns that have shipped twice. Proposal: WARN when a ruby's reading ends in the kana that follows it (`《…え》え`), and when a word's ruby reading differs from the entry's own `reading` (分別). |
| 2 | **20 example sentences in 18 entries copied a scene or frame.** The tool flagged none of them. Book copies: 元 (both examples), リクエスト, さっと, ちぎる (SM), くたびれる (SK), 甘み, 工夫. Official copies: 自動的 (12/2016 script), 一変 (7/2024 読解), 衣類 (12/2023 読解), 分別 (12/2013), しばる (12/2018 問題2-9 stem), リスト (12/2010 script). Module copies: 手作り, 粗大ごみ (live v-0123). Repeats inside the batch: the travel bag with 多めに, in three entries. | All replaced. Re-scan: 0 frame hits and 0 10-character spans. | The frames threshold needs 2+ shared tokens. A copied frame often shares only the headword plus one noun. |
| 3 | **Unsourced or misleading prose.** もれる nuance quoted official 問題6 option sentences and named 「用法問題」 (rules 18 and 32). 清掃, 手作り and 古新聞 called the book's ＋ words 「言い方もある」, but they are not synonyms. アンテナ used 「アンテナが低い」 (the page attests 「アンテナを張る」). 表示 cited 「価格表示」 (the book prints 表示価格). The リクエスト vi gloss ignored the book's VI word "yêu cầu". | Nuance blanked or reworded. Collocations and gloss now follow the page. | Brief rule 2 ("only what a cited page attests") was read as covering senses only, not nuance and usage. |
| 4 | **Known pairs left unlinked:** リクエスト↔要求 (both are "yêu cầu"), さっと↔さっさと, もれる↔ばらす. | Linked both ways. The live compares of 要求, さっさと and ばらす are compressed under the cap and keep every 「」 form and contrast. `rebase` shows only wording trims. | The author stopped at the cap instead of compressing. |
| 5 | **The vi compare mirrored the ja compare** in 21 cards and 7 back-links (the rule 10 creep). | Rewritten for the Vietnamese reader: Hán Việt traps (分別 = "phân biệt", 処理 = "xử lý", 規模 = "quy mô"), the "yêu cầu", "thà" and "nhanh" overlaps, and noun vs verb. | One author wrote both panes. |
| 6 | **Live fixes.** The 5 中身→内容 changes (粗末, 充実, 分野, 分析, 話題) all still fit their cards. 引き落とし's 「自動で」 kept the stem of the new 自動的 headword. 拡充 still carried 充実 and 組織 (HW), and its new 内容 made a PAIR with 充実. 話題 had a bare 話. | 引き落とし → 「口座から引かれて払われること」. 拡充 → 「部門や設備などを広げて、さらによくすること」. 話題 ruby added. | A fix was checked against the one word it removed, not re-run through the lures check. |

Furigana in the vi quotes: every 「」 quote the batch authored carries ruby. Japanese appears only inside 「」. The bare quotes that remain are
live text kept verbatim.

## Result
`gate 語彙 12`: **0 FAIL, 0 WARN, 21 ok, 0 REVIEW**. `frames`: 0 hits. `lures`: 0 LURE, 0 HW, 0 READ. The remaining 7 GW and 2 PAIR are
already live and pair different senses: 引き落とし/残高 on 口座, and 分析/せい on 原因.

**Defect rate vs earlier batches.** The Sonnet draft is clearly worse on furigana. B10 had 0 wrong readings and B11 had 5 broken ruby
markups. B12 has 14 wrong readings, several of them in plain N3 words. Frame copies are also up: about 20 sentences, against 6 in B10.
Ids, readings, pos, pages and official_count are as clean as earlier batches: no error. A Sonnet author needs a mandatory ruby read-back
step, or a ruby-vs-`reading` check in the gate.
