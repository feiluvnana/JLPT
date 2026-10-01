# QA — 知識 語彙 batch 13 (Hajimete No.385–479)

Fresh-eyes reviewer (wrote none of the batch). One Sonnet author wrote both panes. Checked against live at 72758f1 (B12 merged; the 漢字 B11 commit since does not touch 語彙).
75 entries. 20 numbers were dropped because they are already live cards: 389, 391, 401, 402, 406, 418, 423, 428, 431, 433, 434, 436, 438, 439, 444, 458, 461, 465, 473 and 477.
After QA: 14 back-links (the author's 4, plus 担ぐ, 用心, 油断, 訂正, 改善, 周辺, 周囲, 家屋, 年間 and 握る) and 8 live meaning fixes (3 of them revised).
Pre-review copies: `scratchpad/QAV13_bak/`. The fixes are in `QAV13_patch.py` and `QAV13_patch2.py`.
sha1 (first 12 characters), pre → post:

| file | pre | post |
| - | - | - |
| `.json` | a62a2032b667 | d290fa7bc88b |
| `.ja` | 26b660b37778 | 9bd89fff958f |
| `.vi` | d7da53e73fe9 | ed16cea44392 |
| `.backlinks` | 56b988c3cd3c | 9dcf1dc4ee40 |
| `.backlinks.vi` | 9e9fcd90a5cf | 363d1f1a47fd |
| `V13_live_meaning_fix` | 9983a1e38307 | d05655cc2a85 |

## Checks run
- `batch_tool stats / frames / lures / rebase / gate`, before and after the fixes. I read all 79 examples against the Hajimete example on the same page.
- Hajimete pp.81–96 (all 75 entries) checked through the extract: ids, readings, pos, senses and VI lines.
- Every ruby that differs from pykakasi was checked by hand.
- official_count: I grepped every 問題1–6 item for each headword, its stem and 交代.

## Findings and fixes
| # | Finding | Fix | Root cause |
| - | - | - | - |
| 1 | **The book's frame was copied in 18 examples. The tool flagged none of them.** 人通り (the 絶えた line), 辺り, 付近, 住宅, 中間 (the AとBの中間にXがある frame), 修正 (間違っているので修正), 故郷 (a parcel from mother at home), 近郊, 行き帰り (Xの行き帰りはバス), つかむ (someone grabbed my arm), つかまる (it shook, so I held on), 交替 (担当者が交替), はるか (はるか昔から続く), 間隔 (間隔をあけて走る), リニューアル (passive with a facility subject), Uターン (Uターン就職). Two more: 訓練 (a phone drill for new staff, which is really 研修) and 見回る (家中の窓を見回る, which is unnatural). In prose, 4 vi usage lines and 1 ja usage line quoted book sentences: 市民ホールがリニューアルされる, ふるさとの良さを宣伝する, 同じ道をぐるぐる回る, 故郷と東京を行き来する, and 都道府県や市町村などの自治体. | All replaced. My first replacements then hit live cards (v-0023 そば屋, v-1209 帽子, 試合/選手) and a 10-character window. Those were replaced again. Re-scan: 0 frame hits and 0 spans. | `frames` needs 2+ shared tokens. A copied frame often shares only the headword plus a predicate. Same root cause as in B12. |
| 2 | **Missed official hit.** なだらか is the key of 12/2016 問題4-20 (なだらかだった). The author had 0 and cited only a 12/2022 distractor. | official_count 1, source added, tag 問題4 文脈. The example was moved off the slope scene. | The author grepped only the cited sitting. |
| 3 | **Wrong furigana.** 通院 was given ついん (should be つういん). ページ, which is katakana, was given a ruby. | Both fixed. That example was replaced anyway. | pykakasi-diff review was not done (brief item 12). |
| 4 | **Gloss defects.** つかまる 「何かに手でしっかり持つ」 is ungrammatical. 交替 「順番を決めて」 is narrower than the page (担当者が交替した). 年度 had 学校 / năm học, which the page does not attest. エリア shared 広がり with live 空間. | Rewritten. 年度 now reads 「国や会社などが、お金の計算のために決めた一年。」 (the page gives fiscal year and năm tài khóa). | Sense was not checked against the page. |
| 5 | **Live fixes changed the sense.** かじる 「少しずつ食べる」 does not fit its own example (a dog gnawing a chair leg). 傾く 「一方へ寄って曲がる」 means bend, not tilt. 針 「数字のところに向けて動く」 is awkward. | Now 「固い物の端に、歯を立ててかむ。」, 「まっすぐだった物が、一方に寄った向きになる。」 and 「時計などで、動いて数字を教える細い部分。」 | A gloss was swapped to dodge a headword without re-reading the examples. |
| 6 | **Unlinked competing glosses (rule 40).** Known pairs: 担う/担ぐ, 慎重/用心, 気を抜く/油断, 修正/訂正 and 修正/改善, 辺り/周辺, 辺り/周囲, 付近/周辺, 住宅/家屋, 年度/年間. Found in QA: 下町/街 (家や店が多い), 地区/エリア (the book gives "khu vực" for both), 人通り/歩行者 (the book gives "người đi đường" and "người đi bộ"), つかむ/握る (しっかり持つ). The fix to つかまる's gloss created a GW with 握る, so it was re-glossed. | All linked both ways, with compares in both panes. The live compares for 用心 and 訂正 were compressed and every 「」 form was kept: `rebase` shows only 向けて, 前より, 所 and "tình trạng" dropped. 修正/改正 was not linked: the glosses share no word (直す vs 改める), and 改正 is reached through 訂正. | The author stopped "for lack of room" instead of compressing. |
| 7 | **The 見慣れる 他動詞 tag is unsourced.** | Tag removed. | — |

## Rulings
- **交替 is counted through 交代 (7/2012 問題6-31, key 2): yes, 1.** Hajimete p.87 prints "Can also be written as 交代する". It is one word (こうたい) and no other card owns 交代. The source note now says why it is counted.
- **The vi compares do not render the ja.** Each one leads with Hán Việt, a collocation or a transitivity contrast. The new ones also name real Vietnamese traps: "tu chính" means amending a law, which is closer to 改正; 用心 "dụng tâm" does not mean "cố ý"; and 担 is read かつぐ vs になう.

## Not fixed
- Four `lures` GW lines (更新/違反, 飽きる/落ち込む, フルコース/主食, 消費税/会計) are pairs between two live cards. No B13 id is involved and none competes in meaning. They predate B13.

Final gate: **0 FAIL, 0 WARN, 0 REVIEW**; 14 back-links, 8 live fixes.
