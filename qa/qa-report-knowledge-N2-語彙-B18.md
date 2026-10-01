# QA — 知識 語彙 B18 (Hajimete No.807–883, PDF 151–162)

Fresh-eyes reviewer; authored nothing. One round, fixed directly in the batch dir.
Scope: 64 entries (13 dropped numbers are all live: 812 819 820 827 831 839 842 850–854 874),
13 back-links (11 + 着々 and 続出, both added in QA), 22 ja live fixes and 1 vi live fix.
Every back-link and live fix was rebased on the live text after B17 (831376a).

## Findings and fixes

| # | Finding | Fix | Root cause |
|---|---|---|---|
| 1 | Wrong rubies: 鮮《せん》やか (華やか ja+vi compare), ページ分《ふん》, 月《がつ》に一度, 会話｜力《ちから》, 相次《あいつぎ》いで, 計画｜通《とお》り | Fixed to あざ / ぶん / つき / 会話力《かいわりょく》 / あいつ; 計画通り removed with the nuance rewrite | These readings match pykakasi, so a diff against pykakasi alone (brief item 12) does not catch them. Read rubies in context too |
| 2 | Frame and 読解 copies: 見た目 example matched the official 問題6 correct sentence (7/2010 #32 「人を外見で判断する」) and then a 2025-12 読解 claim. 続々 copied 相次ぐ's live 「電話が相次いだ」 frame. 感想 copied 批評's live new-menu feedback scene. 生地 ex1 copied 布's カーテン＋厚い scene, and ex2 shared its frame with B19 v-0915 | All five examples replaced, with notes rewritten. `frames` now shows 0 hits | `frames` does not compare an example with the examples of LINKED partner cards. The author has to read those partners' examples |
| 3 | Usage beyond the page: 利益／雇用を生み出す, 解釈が分かれる／を間違える, 人生が本になる (textbook fragment), 主人に忠実だ (textbook fragment) | Cut to what the page attests or to the entry's own example | Brief item 2 is applied to `meaning` only |
| 4 | Unsourced claims in vi.usage: spelling notes (ダサい, 今ひとつ, せりふ in both panes), "Thường…", "Trong sách…" (names the source), 一言感想, "Người lớn cũng đọc", ロマンチック (the page has ロマンティック), 古代 given as an "opposite" (the page lists it with ＋) | Cut or corrected | — |
| 5 | Long official stems quoted in nuance (4 PROV hits) | Shortened to 「栄養の（　）」 / 「（　）がつかない」 or paraphrased | — |
| 6 | vi compares and vi back-link sentences mirrored the ja (≈28 of 30) | Rewritten for the Vietnamese reader: Hán Việt first, then the trap (役者 DỊCH GIẢ ≠ "dịch giả", 主人公 ≠ "chủ nhân", 現に HIỆN ≠ "hiện nay", 生地 SINH ĐỊA, 空想 is not the adjective "không tưởng", リズム/テンポ are both called "nhịp") | The same as B17. A one-author batch still writes the vi compare from the ja |
| 7 | 感想 meaning 「見たり読んだり」 did not fit its eating example. 書物 「特に、内容のある本」 had no source. アイドル 「若い人に」 had no source | Example replaced / meaning cut to 「本のこと。」 / meaning rewritten | Rules 27/35 |
| 8 | 退屈: the page marks it 名＋ナ形 | pos changed to 名詞・ナ形容詞 | — |
| 9 | Live fixes 実現 「本当の形」 and 就く 「本当に入る」 were unnatural. 素材 swapped in 布 (now a headword) | Rewritten | The fix sweep replaced 実際 with 本当 mechanically |

## Coordinator items
1. 案の定: the back-link is the current live compare (B17 removed 果たして) plus the B18 sentence. The duplicate `v-0794` in add_related is removed. 0 REVIEW.
2. 続々 is now linked with 着々 and with 続出, both ways and in both panes. 続出's ja compare was compressed to 85 characters, 着々's vi to 157 and 続出's vi to 168, keeping every 「」 form (`rebase` lists the dropped prose, no quoted form). 12/2012 問題4-17 (着々と key, 続々と distractor) is the reason for the link.
3. Fixed (finding 3).
4. 賞 = 0 is confirmed. 12/2011 問題3-11 文学（賞） is a 語形成 key for the suffix 〜賞, the same as 〜離れ under 離れる (v-0434). The other hits in the archive are stem-only.
5. Fixed (finding 6).

official_count: ぶかぶか 2 (12/2010 #25 key 4 とても大きい; 12/2025 #25 key 3 大きすぎる) and 奇妙 1 (7/2012 #24 key 1 変な) were re-derived. A grep of 問題1–6 by word and reading found no missed keyed hit.

Gate: 0 FAIL / 0 WARN / 0 REVIEW. `frames` 0. `lures`: 2 GW hits, both between live cards outside B18, so they are pre-existing.
