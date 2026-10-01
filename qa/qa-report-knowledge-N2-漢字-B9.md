# QA report — 知識 N2 漢字 batch 9 (31 kanji, SK 267–300; 37 → 52 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes.

One author wrote both panes (SKILL §"Written, not translated", 2026-10-01). I checked whether the vi fields were written from the SK page or rendered from the ja.

Files: scratch `batches/漢字_B9.json`, `.ja.json`, `.vi.json`, `.backlinks.json`, `.backlinks.vi.json`, `K9_live_meaning_fix.json` (51 ja), `K9vi_live_meaning_fix.json` (3 → 4 vi).
- The originals are in `QAK9_orig/`.
- `QAK9_fix.py` rebuilds every fix from those originals and the CURRENT live tree (post 211fdcc), so the round can be re-run.
- I did not edit the live `knowledge/`.

## Checks

| area | method | result |
| - | - | - |
| ids / readings | SK 別冊 PDF 158–160, rendered and read | All 31 ids match the page, including 北 268, 木 269 and 用 287 (the OCR missed these three). on/kun match. 部門, 約束 and 予約 are not on the page; each is cited to an official sentence. Four rubies were wrong (F1) |
| official_count | Listed every 問題1/2 item in the 31 booklets whose sentence holds a B9 kanji (97 lines) and read the underlined word and options | 0 is right for all 31. The only option hits are 管利 and 官利 (12/2023 2-6, 12/2011 2-7). They are distractors, and the key 管理 holds no B9 kanji |
| examples | `batch_tool frames` plus hand greps of each scene (refs, tests, module, open batches) | 2 replaced (F2) |
| gloss lures | `batch_tool lures` before and after; rule-40 check on every K9 fix | F3, F4, F7. What is left is outside B9: HW items on 下, 実, 相, 調, 登, 等, 景, 濃, 批, 視, 践; GW items 帰/理, 規/違, 接/礼, 養/田; the 質/本 Hán Việt label lure, accepted as in B6–B8 |
| translation | Compared vi and ja field by field | vi `meaning` and `usage` are written for the vi reader (Hán Việt and glosses). **`compare` was mirrored sentence by sentence in ~22 of 31 entries** (F5). `nuance` is a one-line reading fact in both languages and is accepted |
| rebase onto B8 | `batch_tool rebase`, plus a diff of every back-link against the 1446b8b base and the live text | F6 |
| gate | `batch_tool gate` (CURRENT live → merge → build → check_knowledge) | Before: 0 FAIL, 0 WARN, **8 REVIEW** (dropped B8 forms). After: **0 FAIL, 0 WARN, 0 REVIEW**; 52 back-links; fixes ja 51, vi 4 |

## Findings

| # | where | sev | defect → fix | root cause |
| - | - | - | - | - |
| F1 | ja usage of 夜, 様, 力, 六 | major (▶ speech) | In the on-reading row, the ruby was the kun reading: 「〜夜《よる》」, 「様《さま》」 and 「〜力《ちから》」 (PDF 159/160 print や, よう and りょく). 「六《む》つ」 is also wrong. Fixed to 〜夜《や》, 様《よう》, 〜力《りょく》 and 六《むっ》つ | The usage rows were not read against the page row by row (B8 F2, again). `check_ruby_suspects` has no check that a ruby in the 音読み segment is an on-reading |
| F2 | examples 有, 夜 | minor | 有: a museum audio guide with a fee, which is the 7/2023 問題8-46 scene. 夜: 「この道は、夜間は…」 reuses the 12/2020 問題5-24 frame (この道は… with 夜間 as an option). Replaced with a coin locker fee and night roadwork at a 交差点. The drafts rejected along the way: a park boat fee (7/2023 読解 「ボート代は別に」), a library open at night (saturated: 4 cards), レジ袋 (SK 聴解) and 駅前の工事 (3 cards). Both vi notes were rewritten | The scene scan did not cover official claims or 問題5 frames (rule 39) |
| F3 | vi `meaning` of 本, 名, 目, 約, 有, 曜, 来, 力; 様 | major | Eight glosses quoted a compound that holds another entry's headword: 「本部」→部, 「名物」→物, 「科目」→科, 「約束」→束, 「有料」→料, 「月曜」→月, 「来年」→年, 「学力」→学. 様's "gắn vào" was 付's gloss word. All rewritten without the compounds | Rule 34 was applied to the ja gloss only. The vi gloss template "(「compound」)" reintroduces the kanji |
| F4 | links (B8 "link at merge") | major (two-answer risk) | Linked both ways, with a compare in both languages for each: 北↔南, 夜↔晩 and 夜↔朝 (よる), 問↔答 and 問↔聞 (きく), 郵↔便 (てがみ), 利↔便, 洋↔服 (服's gloss prints ようふく), 料↔費, 無↔非 and 無↔不 (ない), and the look-alikes 門↔聞, 旅↔族, 来↔米, 本↔体. Also 果↔実, live to live: the K9 fix 「くだものなどの、み」 collides with 実 「しょくぶつのみ」. 15 new live targets. 服's live compare (92/100) was compressed and keeps every quoted form | The author listed the pairs as "link at merge" instead of linking them. B8 R2 (compound partners and gloss words go in `related`) is still not a hand-off check |
| F5 | vi `compare` | major (rule) | Mirrored the ja sentence by sentence, for example 様 「氏とは…同じ。洋とは形が似ていて…」 → "「〜様」 và 「〜氏」… 「様」 và 「洋」…". 22 vi compares were rewritten for the vi reader, led by the Hán Việt reading. Examples: 友/有 share the HV reading HỮU; 「訪問」 reads "phỏng vấn" but means to visit (a rule-34 false friend); 万/方 is VẠN/PHƯƠNG | The one-author rule allows both panes in one context. Writing them in one pass made the shared-fact `compare` field come out as a rendering |
| F6 | back-links rebased onto B8 | major | ja 親 and 金 dropped B8's 父親/母親 and 費用 sentences. vi 間, 親, 使, 賃, 金, 語 and 損 were built on pre-B8 text and dropped 聞/耳, 父母, 便/吏/更, 貸/費/運貸/運費, 費用 and 文体. All 37 are now the CURRENT live text plus the B9 sentence. Three vi texts went over 180 after the rebuild: 間 and 賃 were compressed, and for 損 the author's own trim ("đi", "ghép thành") was kept. No 「」 form or contrast was lost | B8 merged after B9 was written. The vi pane was not rebased with the ja pane |
| F7 | live fixes | minor | ja 才: 「すぐれたせいしつ」 is not 才 (talent) → 「うまれつきそなわった、すぐれたもの。さいのう。」. vi 置: "vị trí (「位置」)" collided with 点 "vị trí" → "sắp đặt, bố trí". Added vi 材: "(như gỗ)" named 木 (B8 note) → "vật liệu, nguyên liệu để làm ra đồ vật". The other 50 ja and 2 vi fixes match the current live text: each keeps the B8 kana and removes only the kanji. That includes 疲, 果, 実, 能, 講, 象, 損, 編 and 養 | Rule 40 was re-run on kanji, not on the gloss words a fix introduces. The B8 vi note for 材 was missed |

**Counts:** 7 findings (5 major, 2 minor).
- Edits: 4 rubies, 2 examples, 9 vi glosses, 22 vi compares, 13 B9 ja compares.
- Back-links: 52 (37 rebuilt, 15 new).
- Fixes: 1 ja changed, 1 vi changed, 1 vi added.

The vi text of the new links, notes and compares was written in this QA context, which had read the ja pane. As in B2–B8, a vi-only pass may re-author them.

## Proposed rules

- **R1:** `check_ruby_suspects` should WARN on a single-kanji ruby inside a 「音読みX…」 segment whose reading is not X.
- **R2:** In the brief, rebasing means BOTH panes: rebuild every vi back-link from the live vi text, not only the ja.
- **R3:** In the brief, a learner-pane `compare` must lead with what that reader uses (Hán Việt, false friends). A sentence-for-sentence restatement of the primary pane is a translation finding.
- **R4:** Lures already flags vi glosses with quoted compounds (HW). Make it a hand-off requirement: no 「compound」 inside a vi `meaning`.

## Merge steps

1. Start from the CURRENT live tree (211fdcc or later; `knowledge/N2/語彙*` had uncommitted changes from another session, which this round did not touch).
2. Run `python3 .agents/jlpt-knowledge/scripts/batch_tool.py merge 漢字 9`. It applies `K9_live_meaning_fix.json` (51) and `K9vi_live_meaning_fix.json` (4), adds 31 entries and applies back-links to 52 live entries. There should be no REVIEW line.
3. Run `make knowledge`, then `make check`, and read every line.
