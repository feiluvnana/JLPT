# QA — 知識 語彙 B23 (Hajimete No.1195–1290, PDF 218–232)

Fresh-eyes reviewer; one round, fixed directly in the batch dir. 71 entries kept. The 25
numbers not carded (1196 1208 1209 1213 1216 1236 1237 1242 1247 1248 1251 1253 1255–1258
1266 1270 1272–1274 1285–1288) are all live cards already. Every page 218–232 was read
against every entry: headword, reading, pos, ＋/↔ words, the VI gloss, the example, and the
usage line.

Final: `gate` 0 FAIL / 0 WARN / 0 REVIEW; `lures` no hits (it reported 1 PAIR before the
fixes); `frames` 0 PROV / 0 `!!` (the 3 remaining K lines share only 祖父/手紙/家族).
`rebase`: 30 back-links. 20 fill an empty live compare. 10 rewrite a live compare to fit the
cap, and every 「」 form is kept. 19 ja live fixes (16 → 19) and 3 vi live fixes (1 → 3), each diffed
against the CURRENT live text after B22 merged.

## Findings (fixed)

| # | class | count | what |
|---|---|---|---|
| F1 | usage copies the book's example or note phrase | 6 ja + 6 vi | 少なくとも五人, 仕事と育児の両立は難しい→勉強と部活の両立/両立が難しい, 納税の義務, 怒りが爆発する (the book's note), 復興支援 (＝復興をサポート), 制度を改める (＝制度の見直し). The vi usage 「ただちに報告する」 also repeated the 7/2012 問題5 stem |
| F2 | example copies a frame or scene | 6 | 爆発: a factory explosion (the book's 化学工場, 火災's 工場で爆発), then a 電子レンジで温める sentence that matched an official 問題6 misuse sentence (`!!`); 要素: 〜も…な要素だ; 支配: a country ruled by another for N years; ばく大な費用/資金が必要; 見解: 専門家の見解が分かれる (the 12/2010 問題5 stem), then 市は…計画を発表した (漢字 k-1034) and 事故の原因 (v-o-izen) |
| F3 | gloss carries another headword or verb stem (rule 34) | 9 B23 + 6 live | 言い争い (争う), 守らせる (守る B24), 飛び散る (飛ぶ), 従わせる (従う), 向かって (向く), 仕組み (組む), 物事 ×5 (B24 v-1354). Live 抜ける ×3 (パンク, 外れる, ぐったり) were not fixed for 抜く; 敗れる 負ける (負う); v-0106/v-0872 物事 |
| F4 | rule 40: shared gloss words | 5 | 約束ごと in 取り締まり/不正/制度; 導入 fix "quy chế" = 制度/改正; 個人情報's ja gloss used 情報 (its own headword; PAIR with アンテナ); 充実 "chế độ" vs 制度; もめる/争う "言い合い"/"cãi cọ" |
| F5 | links missing | 10 | 関連↔関わる, 荒っぽい↔乱暴 (荒 was a distractor in the 7/2021 問題2 item), 防止↔予防, 治める↔納める, ただちに↔たちまち, 一瞬↔とっさ, 上回る↔乗り越える/超過, 救助↔援助, もめる↔争う. The live compares of 納める, たちまち, とっさ, 予防, 援助 and 争う were compressed to fit the caps |
| F6 | vi compare mirrors ja | 17/24 | rewritten to lead with the Vietnamese trap: 災害 TAI HẠI ≠ 'tai hại', 定着 ĐỊNH TRƯỚC ≠ 'định trước', 情報 TÌNH BÁO ≠ 'tình báo', 実際 THỰC TẾ ≠ 'thực tế' (practical), 救助 CỨU TRỢ ≠ 'cứu trợ', 少年 ≠ 'thiếu niên' (both sexes), 判断 ≠ 'phán đoán' (guess) … The other 7 already carried their own trap (reading, homophone, 伸びる) |
| F7 | Hán Việt / bare Japanese | 6 | 非難 PHI NAN → PHI NẠN (×3 fields); 行方 (hành phương) → HÀNH PHƯƠNG; 予期 DỰ KÌ → DỰ KỲ; bare (ひなん), (じっせん), (こうきょう), (ます), +する, 言い換え in the vi pane |
| F8 | unsourced or contradicted claims | 3 | ただちに "used for instructions and reports" (the book's example is news spreading); もめる vi "thường"; 問題5 nuance prose → the live convention (key + options) |
| F9 | ruby and pos | 2 | ｜全社《ぜんしゃ》｜員《いん》 → ｜全社員《ぜんしゃいん》; あり得ない イ形容詞 → 連語 (the book prints 連語) |
| F10 | odd collocation or note | 2 | 「意見がもめる」 → 「会議がもめる」; 成立 note "hợp đồng được thành lập" → "được ký kết" |

Decisions: あり得ない takes the book's 連語, because pos is read off the page and only a 慣 mark
has a ruling. 非難 is PHI NẠN, because the 難 of blame (and of 困難) is NẠN. 公 reads
おおやけ (p.226, ruby checked), and its gloss was rewritten.

official_count was re-derived from the stem and the four options: 見解 1 (12/2010 問題5-26)
and ただちに 1 (7/2012 問題5-23). A grep of 問題1–6 in all 31 sittings found no keyed hit that
was missed (12/2025 問題1-2 keys 討論; the 7/2016 おさめた item is 納める; 旧/現/諸 are
affix keys), and no live `sources` note credits a B23 headword.

Open for B24/B25: B25 v-1405 洗練 「あか抜けて」 carries 抜く's stem. B24 v-1354 物事 will
need live fixes, since 物事 is common in live glosses.

## Root cause
- F1/F2: `frames` does not compare `usage` lines with the book's example, and it does not
  see a page's note phrase (怒りが爆発する). Each must be read against the page.
- F3: `lures` HW does not catch verb stems inside compounds (言い争い, 仕組み) or the
  headwords of open later batches. The author's check skipped the reverse direction (live
  glosses carrying the batch's stems: 抜ける).
- F6: brief items 10/11/15 again. The vi pane was written first, but its compare still
  restates the ja contrast after a Hán Việt label.
