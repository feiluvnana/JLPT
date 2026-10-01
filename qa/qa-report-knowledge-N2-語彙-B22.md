# QA — 知識 語彙 B22 (Hajimete No.1114–1194, PDF 204–217)

Fresh-eyes reviewer; one round, fixed directly in the batch dir. 69 entries kept. The 12
numbers not carded (1123 1133 1141 1147 1151 1155 1158 1161 1163 1167 1191 1193) are
all live cards already. Headwords match the pages: 1131 余計［に］ (副) and 1132 余計な
(ナ形) are two book entries, so two cards; 1159 is the book's（医者に）かかる.

Final: `gate` 0 FAIL / 0 WARN / 0 REVIEW; `lures --with 23` clean (its one PAIR is
B23's 個人情報); `frames` 0 PROV, apart from the 1174 nuance, which quotes the
official option list as live cards do.

## Findings (fixed)

| # | class | count | what |
|---|---|---|---|
| F1 | usage copies the book's example phrase | 43 ja + 42 vi usage fields | 医療が進む, 高度な医療, 保険が適用される, 最悪の場合を覚悟する, 機能が回復/低下する, 居場所がわかる, あくまでも目安だ … |
| F2 | example copies the book's frame | 14 | 負傷→病院, かえって…増やす, 一方の話だけで, 相手を訴えた, 関わらない/命に関わる, 近所で犯罪, おどかす（〜ないと）, 見知らぬ人に…, 命が縮まる (ex removed), 〜ことは明らかだ, 居場所がわかった, 持ち主を探す, あくまで…続ける, あくまで案で |
| F3 | example copies another sentence | 3 | 1185 = a 7/2011 問題 stem; 1188 = B23 v-1209 frame; 1172 = a 12/2015 script window |
| F4 | ruby | 4 | 応急手当《おうきゅう》て, 余分の 分《ふん》→ぶん (×2), ドアの 陰《いん》→かげ, live fix ｜人《ひと》｜々《々》 |
| F5 | gloss carries another headword (rule 34) | 13 | B23: 水準 (1121, 1149), 事実 (1122), 判断 (1168, 1169); live: 示す (1122), 元 (1140), 差 (1181), 争い (1168, 1169), 許し (1177), 荒 / あらあらしい (1174, 1175, blurred with 荒れる); a live fix put 肌 into v-0231 |
| F6 | live glosses carrying B22 headwords that had not been fixed | 6 | 治療 (手当て), 努める (つくす), 接する / 密接 / 軽傷 (かかわる), 抵抗 (はね返す): live fixes added → 17 |
| F7 | prose quotes official stems (rule 32) | 8 nuance × 2 panes | 1119, 1145, 1148, 1154, 1174, 1185, 1186, 1187: now the live convention (key + options only) |
| F8 | unsourced claims | 4 | ケア etymology in ja and vi; 縮まる/縮む contrast where the book prints ＝; vi 余計に "tệ hơn nữa" (the page says "more than before / more than normal" → "hơn trước (ngoài mong muốn)"); あくまで "hay dùng" |
| F9 | vi compare mirrors ja | 24/28 entries, 14/14 back-links | rewritten to lead with Hán Việt + the Vietnamese trap (刑事 HÌNH SỰ, 負 PHỤ, 機能 CƠ NĂNG, 余 DƯ …); 3 left near-mirror but carry their own collocations (1142, 1144, 1146) |
| F10 | links missing | 9 | 医療↔通院/医師, 作用↔反応, 克服↔乗り越える, 配慮↔気配り, 一向に↔さっぱり, 明らか↔明確, 低下↔衰える, くっきり↔ぼんやり. Live compares were compressed to fit the caps, every 「」 form kept → 23 back-links |
| F11 | back-link drops live text | 1 | v-o-chiryou vi (治療 dropped): now the live text plus an appended sentence |

official_count re-derived hit by hit (key.md + options): 1119, 1145, 1174, 1185, 1186 and
1187 at 1; 1148 at 2. Grep of 問題1–6 in all 31 sittings: no missed keyed hit (のぞいて
in 12/2014 is 除く; ようやく / 乱暴 / 明らか appear only in stems or as distractors).

## Root cause
- F1/F2: the author checked `frames` (tokens) but did not read each line against the page;
  the book's own example phrase slips into `usage` as the "natural" collocation. Brief item
  16 says this; it needs a tool check (usage vs the page's example).
- F5: the author ran `lures` before B23 existed and does not check single-kanji or
  verb-stem headwords (争い, 許し, 元, 差); `lures` HW misses these too.
- F9: brief items 10/11/15 again — the vi pane was written first, but its compare still
  restates the ja contrast.
