# QA — 知識 語彙 B21 (Hajimete No.1048–1113, 体と健康・病気になる前に・症状)

Fresh-eyes reviewer; authored nothing. One round, direct fixes. Final tool state: gate 0 FAIL /
0 WARN / 0 REVIEW; frames 0 hits, 10-char 0; lures 2 GW, both live↔live false positives
(察する/誓う share 「っきり」 from はっきり; 世の中/ニーズ share 社会, not synonyms).

Scope: all 60 entries read against PDF 192–203 (ids, readings, pos, ＋/↔/＝ words, VI line). The 6
numbers not carded (1070, 1073, 1080, 1082, 1098, 1110) are live. official_count: かたよる (12/2012
問題4-16), 小柄 (7/2015 問題5-26), 〜気味 (7/2013 問題3-14) and はれる (12/2023 問題6-27) are
confirmed against key.md. I grepped 問題1–6 of all 31 sittings by kanji, reading and stem.

## Findings and fixes

| # | Finding | Fix | Root cause |
| - | - | - | - |
| 1 | Missed keyed hit: 7/2011 問題4-19 「コピー機に紙が（ ）」, key 2 つまって | 詰まる official_count 0→1, source and nuance (paraphrased, no stem quote) | grep was by kanji 詰, so the kana key was missed (brief 13) |
| 2 | Uncounted distractor hits missing from sources | 測定 (12/2020 #14), 体力 (12/2022 #21), 体調 (7/2021 #23), all marked 「数えない」 | same grep |
| 3 | 5 wrong rubies: 何｜人《ひと》 (なんにん), 管理｜人《ひと》 (かんりにん), 戸締《とじま》まり (とじ), 計画｜通《とお》り (どお), 通院 gloss 通《とお》って (かよ) | corrected | split rubies hide the reading from a whole-word diff (B20 #1 again) |
| 4 | 44 usage lines copied the Hajimete example phrase (血圧が高い, 血管が弱くなる, 健康を取り戻す, 保険に加入する, 体調を崩す …); one replacement (よろしくお伝えください) then hit SK goi | all replaced in both panes; book ＋ words now say 関連語 / "Từ liên quan" (いびき, 便秘, 寒気, 体力) | brief 16 not applied |
| 5 | Example frame copies: 体が持つ (overwork → 体が持たない = the book's frame); 一般に stated a checkable fact (美術館は月曜休み) | both rewritten with their notes | — |
| 6 | vi names the source: 障がい "(sách viết がい…)"; the CHƯỚNG note claimed a misreading risk it did not show | rewritten: CHƯỚNG HẠI; 'chướng ngại' is an obstacle, this card is disability | `check_prose_citations` reads ja only |
| 7 | Mirror rate: 15/29 vi compares and 18/18 vi back-link sentences restated the ja | all rewritten around the Vietnamese trap (mạch = 脈, not 血管; 'thọ' suggests long life; DỤNG TÂM ≠ 'dụng tâm'; TRÌNH ĐỘ; 手首 reverses 'cổ tay' …); 1 left borderline (医師) | brief 10/11/15 not applied |
| 8 | Glosses colliding across batches | linked both ways: さらに↔いっそう/一段と, 測定↔観測, 反応↔応答, 休養↔休息/疲労, しきりに↔しばしば/絶えず, ぼうっと↔ぼんやり, 予防↔用心 (identical glosses), いびき↔ぐうぐう, 寒気↔冷え込む | link-at-merge pairs |
| 9 | B19 glosses carrying B21 headwords: いっそう (程度, さらに), 一段と, あまりに (程度) | live fixes (no 程度/さらに) | — |
| 10 | 念のため vi "đề phòng" = 予防 vi; 通院/医師 glosses carry B22 headword 手当て; 休養 gloss printed its own 休 | reworded | — |
| 11 | Bare kana outside 「」 in vi (ごこち, ぎみ, さむけ) | removed | — |

Not linked: 万一↔念のため and 用心↔念のため. After fix 10 their glosses share no word (万一 "lỡ ra";
念のため "để cho chắc chắn").

Rebase: all 30 back-links sit on the CURRENT live text (B19 and B20 included). 4 live compares were
shortened on purpose (疲労, 絶えず, 用心, ぼんやり, ja and vi), and every 「」 form is still there.
21 live fixes (18 + いっそう, 一段と, あまりに).
