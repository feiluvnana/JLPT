# Stage 3 (build + gate) — 20260917_1

Run 2026-09-17. One context, no authoring done here.

## 1. What I read, in full, from disk

- `.agents/exam-app/SKILL.md`
- `.agents/choukai-audio/SKILL.md` (whole file; Part 0 first)
- `.agents/jlpt-test-generation/SKILL.md` — Stage 3 and §"One topic, one surface
  (whole-paper pass, stage 3)"
- `qa/dokkai-allocation-20260917_1.md` (binding allocation table)
- `qa/stage2-notes-20260917_1.md` (verified notes + the two OPEN hand-off flags)
- `qa/open-items-20260914_1-dispositions.md` (rows 7a and 7b in particular)
- Read while resolving specific lines: `exam-blueprint/SKILL.md` §"The four theme
  rules", §"logs/topics.json", rule 4b/R2 and rule 5; `tools/check_consistency.py`
  docstrings for `check_key_grammar_exposure`, `check_choukai_option_set_reuse`,
  `check_topics_claim_field`, `check_headline_theme_lexical_support`;
  `tools/compose_choukai.py` `previous_slot_clips` / `draw` / `freshest`.
- Inputs: the three `tests/20260917_1/_sections/*.md` fragments,
  `tests/20260917_1/test_spec.json`, `logs/ledger.json`, `logs/topics.json`,
  `logs/choukai_draws.json`, `logs/choukai_bank.json`.

## 2. Every command I ran, verbatim

```
make autofix 20260917_1
make lint-draft 20260917_1
make verify-scramble 20260917_1
make mp3 20260917_1 SEED=56017719
make booklet 20260917_1                      # FAILED: <ol> present — see §3
make sheet 20260917_1
make check                                    # 3 FAIL
make upload-files TARGET=tests TEST=20260917_1
make booklet 20260917_1                       # after the two repairs in §3
make sheet 20260917_1
make check                                    # 1 FAIL (stage 5's)
make choukai-wear                             # exits non-zero, known (row 7a)
```

Plus three one-off python reads (no writes): the mechanical merge, the two
mechanical repairs in §3, and the `logs/topics.json` row append.

## 3. What I wrote

1. **`tests/20260917_1/言語知識・読解.md`** — merged MECHANICALLY from the three
   fragments: bodies in booklet order (問1–6, 問7–9, 問10–14), then ONE
   `# 解答(言語知識・読解)` heading followed by the three key tables in the same
   order. No authored wording was changed by the merge itself.

   Two **non-content** repairs were then needed, both forced by a gate:

   - **20 blank lines removed**, each sitting between a `**N**` stem and its
     ` 1. …` option run in 問題10–14. Markdown turned every one of those option
     runs into a real `<ol>`, and `build_booklet.verify()` aborts the build on an
     `<ol>` (option numbering restarts from 1). Every other paper on disk writes
     the stem and the options with no blank line between them; the fix deletes
     whitespace only and changes no character of authored text. Applied to the
     merged file and mirrored into `_sections/問10-14_読解.md` so a re-merge
     cannot reintroduce it.
   - **問題13, one connective: 「しかし、同じ机で半月を過ごすと…」 → 「それでも、…」**.
     `check_key_grammar_exposure` FAILed `問48「しかし」×2` — the 問題9 cloze keys
     しかし and the 読解 prose printed it twice (問題12(B) and 問題13).
     `KEY_EXPOSURE_MAX` is 1. I changed the 問題13 occurrence because it is a
     secondary contrast; the passage's 〈想定→実は〉 pivot is the 「ところが」 in the
     second paragraph and is untouched, as is the closing sentence. The
     re-grep this repair obliges is in §6.
2. **The whole 聴解 half**, written by `make mp3 20260917_1 SEED=56017719`:
   `聴解スクリプト.txt`, `聴解.md`, `聴解.mp3` (45.0 min, 34 chapters),
   `聴解_チャプター.json`, and the 30 choukai entries in both `詳細解説` panes.
3. **Built artifacts**: `言語知識・読解.html`, `聴解.html`, `解答.html`, `練習.html`.
4. **`logs/choukai_draws.json`** — one new row (written by the composer).
5. **`logs/upload_manifest.json`** — `20260917_1.mp3` (43.2 MB) pushed to the
   `audio` release, which is what cleared the third FAIL.
6. **`logs/topics.json`** — one new row: `surfaces`, `themes`, `shapes`,
   `closing_moves`, `voices`, `persona`, `claim`, `notes`.
7. **This report.**

## 4. The whole-paper table

Theme column is filled from the SHIPPED surface. `drawn` is the
`test_spec.json` `reading_topics` entry for that seat (問題9 has no seat — its
theme is author-composed and stage 1 fixed the legal set to 環境 / 子育て・家族 /
文化・伝統).

### 4.1 読解 + 問題9 cloze

| surface | shipped subject | theme (shipped) | drawn | = | closing | final-sentence template | MOVE | 20260914_1 same seat | 20260911_1 same seat |
|---|---|---|---|---|---|---|---|---|---|
| 問題9 | 緑のカーテンの涼しさは遮蔽と蒸散の二つの働きで、二つ目は水やり次第 | 環境 | (author-composed) | legal | 説明 | T0 `Aであると同時にBでもある` | 機構の説明 | デジタル化 (同じ一枚を直す) | 食 (金曜の汁) |
| 問題10(1) | 窓口の開く時間帯と相談者の顔ぶれ（県の五年分の記録） | 医療・福祉 | 医療・福祉 | ✓ | 条件提示 | `AほどBが多い（相関）` | 数えたことの報告 | 文化・伝統 (祭りの笛) | 文化・伝統 (石段) |
| 問題10(2) | 旅の二日目の夕方、宿の机で書く絵はがきの十分 | 旅行・観光 | 旅行・観光 | ✓ | 随筆 | T0 `〈その十分〉がXを〜してくれる` | 一人称の前後比較 | 医療・福祉 (手話通訳の立ち位置) | メディア・情報 (会報の部数) |
| 問題10(3) | 社員研修の昼食を四十食ずつ二回に分ける依頼メール | 食 | 食 | ✓ | 実用文・分類外 | T0 `〜いただけますと助かります` | （実用文） | メディア・情報 (件名20字) | 教育 (分かるとできる) |
| 問題10(4) | 大雨のとき店の屋上駐車場へ車を移せるお知らせ | 防災 | 防災 | ✓ | 実用文・分類外 | T0 `〜お出しください` | （実用文） | 交通 (踏切の遮断時間) | 地域活性化 (駅前広場) |
| 問題10(5) | 直した跡を札で示したら売れ方が変わった古道具店 | 消費・経済 | 消費・経済 | ✓ | 意外な観察 | `〜のはBだ（分裂文）` | **〈想定→実は〉** | 消費・経済 (値札改定) | 住まい (古家の引き戸) |
| 問題11(1) | 初対面の二人を引き合わせる順序と、半歩引くこと | 人間関係 | 人間関係 | ✓ | 説明 | T0 `Aで終わらずBまで含んでいる` | 機構の説明 | 行政・手続き (届け出の期限) | 防災 (堤防へ上がる人) |
| 問題11(2) | 放課後三十分の教室での宿題時間への批判と応答 | 教育 | 教育 | ✓ | 反論応答 | `Aだけではない。Bこそが〜` | 反論への応答 | 環境 (斜面に木を植える) | スポーツ・余暇 (笛を持つ資格者) |
| 問題11(3) | 集合住宅の通路の私物と、片づけた日を書く欄 | 住まい | 住まい | ✓ | 条件提示 | T0 `AのほかにBが必ずあった` | 数えたことの報告 | 子育て・家族 (洗濯物をたたまない) | 医療・福祉 (横に傾いた道) |
| 問題11(4) | 眠れない夜に一度起きて薄い本を二、三ページ読む | 睡眠・健康 | 睡眠・健康 | ✓ | 随筆 | `〜のはBだ（分裂文）` | 一人称の前後比較 | 住まい (外壁修繕の順) | 睡眠・健康 (寝る前一時間の記録) |
| 問題12(A) | 問い合わせ先は字を大きくするより通じる時間帯を書け | メディア・情報 | メディア・情報 | ✓ | 主張 | `〜のは、AではなくBだ` | 反論への応答 (A+B = one surface) | 教育 (答案返却の速さ) | 働き方 (窓口の二人制) |
| 問題12(B) | 問い合わせ先を末尾でなく二行目へ | メディア・情報 | ″ | ✓ | 反論応答 | T0 `〜であれば、〜していく` | ″ | 教育 (一行そえて返す) | 働き方 (二人制の手間) |
| 問題13 | 引き継ぎは書類の厚さではなく机を並べる十日間 | 働き方 | 働き方 | ✓ | 主張 | T0 `〜書き入れておきたい` | **〈想定→実は〉** | 人間関係 (頼みの大きさ) | 交通 (歩行者信号の青) |
| 問題14 | あさひ野市 犬の登録と春の予防注射の案内 | 行政・手続き | 行政・手続き | ✓ | （axis 2 外） | — | （実用文） | 旅行・観光 (舟下り案内) | 科学・技術 (実験の日) |

**Every one of the thirteen shipped surfaces sits on the theme it was drawn
with.** No surface moved, so nothing is stamped `"origin": "reauthored"` and no
spec/ledger annotation was needed.

### 4.2 聴解 — a DRAW audit (see §5 for the clip-id half)

> **INVALIDATED 2026-09-21 — do not diff against this table.** It describes the
> superseded seed-56017719 draw. The listening half has been re-drawn FOUR times
> since: 3187623 and 49804919 (both rejected — neither could clear F2, which was
> pinned by the pool, not the seed), 48767419 (QA round 1), 79644767 (rejected —
> reproduced F1 and added a second duplicate pair), and finally **80324117, the
> shipped draw**, composed after the within-大問 duplicate-question bar landed in
> `compose_choukai.draw()`. The live 聴解 rows are `logs/topics.json` for
> `20260917_1`; the verdict on the shipped draw is
> `qa/qa-report-20260917_1-round2.md`. The table is left unrewritten on purpose,
> as the record of what stage 3 audited.
>
> (This notice was itself stale for one generation — it named 79644767 as the
> shipped seed. Fixed 2026-09-21. A superseding notice needs re-checking every
> time the thing it supersedes moves again, which is the same NF-5 class it
> exists to prevent.)

| slot | shipped subject | theme | 20260914_1 same slot | 20260911_1 same slot |
|---|---|---|---|---|
| 問題1-1番 | 携帯電話店の留守番電話 → 貸出機を持って来店 | 消費・経済 | 合唱サークルのポスター案 | 学部選びの資料請求 |
| 問題1-2番 | 印刷済みプログラムの誤り → 貼り紙で訂正 | 働き方 | 就職活動の問い合わせ | 講演会の当日配付資料 |
| 問題1-3番 | 先輩の不要家具 → ボランティア団体に寄付 | 住まい | パンフレットの原稿依頼 | 日本語授業の申し込み |
| 問題1-4番 | 照明設計の素材をガラス→和紙に変更 | 住まい | 一行で美術館へ | 卒業パーティの名札貼り |
| 問題1-5番 | 学生証再発行 → まず申込書を書く | 教育 | 説明動画を短くまとめる | ロビー企画案を三つ |
| 問題2-1番 | 薬の心配の理由＝以前の同種の薬で吐き気 | 医療・福祉 | 絵画教室講師の条件 | 映画の終わり方 |
| 問題2-2番 | 会社に決めた理由＝本音で話せた | 働き方 | 前髪を切りすぎた | 歌手がプロになった道筋 |
| 問題2-3番 | プレゼン資料＝聞き手の立場 | 働き方 | 自転車通勤の理由 | 専門学校を選んだ理由 |
| 問題2-4番 | 着物に夢中＝合わせ方で印象が変わる | 文化・伝統 | 退職後は高校のコーチ | 今日眼鏡な理由 |
| 問題2-5番 | 店の箱の中身＝花 | 消費・経済 | ビーチコーミングの目的 | 薬の心配の理由 |
| 問題2-6番 | 猫を選んだ理由＝顔の見た目 | メディア・情報 | 防災グッズは使ってみる | 映画の一番の魅力 |
| 問題3-1番 | 学校事務室 — 授業の日程の変更 | 教育 | 片付けの効果 | 犬の健康に必要なこと |
| 問題3-2番 | 電子書籍の調査 — 利用する理由 | メディア・情報 | 海岸のごみは地元の川から | 通信販売の調査 — 利用する理由 |
| 問題3-3番 | 通信販売の調査 — 利用する理由 | 消費・経済 | 留守番電話の忘れ物確認 | 移動スーパーの見守り |
| 問題3-4番 | 男の人にとって車はかっこいいもの | 交通 | 館内放送の催し物案内 | 子どものほめ方 |
| 問題3-5番 | 人工知能の利点を活用すべきだ | 科学・技術 | 大切な話にメールを使う理由 | 通信教育には向いていない |
| 問題4-1番 | 締切に間に合うか → 徹夜で頑張るしかない | 教育 | 音を小さくしてほしい | 弁当に箸を付けるか |
| 問題4-2番 | 企画書を見てほしい → いつまでに | 働き方 | もっと早く教えてほしかった | 泣かずにはいられなかった |
| 問題4-3番 | 断るつもりが覆った → では受けるのか | 働き方 | テストが来週なら | 迷惑をかけた詫び |
| 問題4-4番 | 打ち消しだけ → 真意を尋ねる | 人間関係 | 研修が物足りなかった | 負けるに決まっている |
| 問題4-5番 | 親と相談して決めよ → そうします | 教育 | ここで待たせてほしい | 代表に選ばれたからには |
| 問題4-6番 | 来られたらよかったのに → 行きたかった | 人間関係 | 遅刻はありえない | パンフレットに沿って話す |
| 問題4-7番 | 今日は休みだったか → 午後から出勤 | 働き方 | 会計は一緒か | 卒論の締め切り |
| 問題4-8番 | しまった場所が分からない → またか | 住まい | 一日で回り切れるか | コートも預かる申し出 |
| 問題4-9番 | 取っておこう → もう使わない | 住まい | けがは大したことない | 今手が空いているか |
| 問題4-10番 | 返事が曖昧 → 代わりに聞こうか | 働き方 | 予想に反して多かった | まずまずという自己評価 |
| 問題4-11番 | 各年代に受けている → 意外だ | 消費・経済 | 申し込みは来月から | 初めの考えどおりにした |
| 問題5-1番 | ダンスコンテスト → 手に持つ小道具 | スポーツ・余暇 | 演劇部の汚れた衣装 → 飾りで隠す | 図書館の利用者を増やす案 |
| 問題5-2番 | 自転車四種 → 質問1は三番、質問2は二番 | 消費・経済 | 防災フェア四会場 | 桜映画祭の四本 |

### 4.3 The 11 drawn `quick_response` phrases

**None of them reaches a surface.** Since 2026-09-08 問題4 is composed from
banked clips, so the 11 draws in `test_spec.json` are spent by the sampler and
no setting was invented for any of them. Listed here because the pass requires
every one to be read, and because two of them WOULD have been findings had the
listening half been authored:

| # | drawn phrase | invented setting | read against 問題9 (緑のカーテン) | read against the 読解 half |
|---|---|---|---|---|
| 1 | 気が進まない | — (not shipped) | no overlap | — |
| 2 | 会場までは駅から歩いて15分ほどかかりますが、よろしいでしょうか。 | — | no overlap | would have brushed 問題14's 「③の会場には駐車場がありません。歩いてお越しください」 |
| 3 | こちらこそ、いつもお世話になっております。 | — | no overlap | **would have collided** — 問題10(3) opens 「いつもお世話になっております。」 |
| 4 | 〜に決まってる | — | no overlap | — |
| 5 | 二の足を踏む | — | no overlap | — |
| 6 | 骨が折れる | — | no overlap | — |
| 7 | 駅前のカフェ、今日はもう閉まってるんじゃない？ | — | no overlap | — |
| 8 | 気が置けない | — | no overlap | — |
| 9 | 避難経路は、各階の掲示をご確認ください。 | — | no overlap | **would have brushed** 問題10(4), the 大雨の避難 notice |
| 10 | 今日、鍵をうっかり忘れて、家に入れないんだ。 | — | no overlap | — |
| 11 | 明日の現場、朝早いけど集合時間は大丈夫そう？ | — | no overlap | — |

No action: an unshipped draw cannot collide with anything. Recorded so the next
paper's blueprint does not read this as a clean 問題9/問題4 separation earned by
authoring.

## 5. The reads, one axis at a time

### 5.1 MOVE column, read down on its own

Ten essay surfaces, 問題12 A+B as ONE (問題10(3)/(4) and 問題14 are 実用文):

| MOVE | surfaces | count | cap |
|---|---|---|---|
| 機構の説明 | 問題9, 問題11(1) | 2 | 2 |
| 数えたことの報告 | 問題10(1), 問題11(3) | 2 | 2 |
| 一人称の前後比較 | 問題10(2), 問題11(4) | 2 | 2 |
| 〈想定→実は〉 | 問題10(5), 問題13 | 2 | 2 (plan target, 3 ceiling) |
| 反論への応答 | 問題11(2), 問題12(A+B) | 2 | 2 |

Matches the binding allocation exactly. **No row over cap.**

**Then the SKELETON read, which is the read that matters** — 〈通説/想定 X →
否認 → 実は Y〉 counted by structure, not by label, essay surfaces only,
問題12 A+B as one:

- **Conservative** (all three beats: attributed assumption + explicit denial +
  実は Y): **4 of 10** — 問題10(5) (店主は…と思っていた／ところが／札が答えている),
  問題13 (長く言われてきた／ところが／机を並べる十日間), 問題12(A+B)
  (字を大きくせよという直し方が広まった／それで届くのは昼間の人だけ／時間帯),
  問題11(2) (…という批判がある／心がけで決まっているわけではない／三十分こそが).
- **With BORDERLINE counted**: **7 of 10** — adds 問題9 (すだれと同じ／はっきり
  ちがうところが一つ), 問題11(1) (紹介は済んだように見える／そのあと二人は黙る),
  問題11(4) (眠りが深くなったかは分からない／変わったのは時計との付き合い方).

Official, hand-measured on the same rubric over 9 surfaces, is **3–4 of 9**
conservative and **6–8 of 9** with borderline — the three sittings and the
numbers are owned by `qa-report-20260911_1` §"F3 の根拠 — 公式を同一ルーブリック
で実測"; I cite it rather than restating it. This paper sits **inside the band on
both rubrics**, and well clear of the four monoculture papers that made this a
mandatory read (`20260904_3` 8, `20260907_1` 7, `20260910_1` 7, `20260911_1`
10 of 10). The gate's own instrument, a different denominator, prints
`at most 3 読解 surfaces run the 〈通説→否認→実は〉 skeleton (2 of 13 surfaces)`.

The deletion test, applied only to the two rows the allocation assigns
〈想定→実は〉 and required to FAIL everywhere else: 問題10(5) and 問題13 both
collapse when their denial sentence is deleted (they were genuinely on the
skeleton). The two at risk of a re-skin, 問題10(2) and 問題11(4), both have a
**practice** as their "before" — 「旅から帰ると、私は決まって絵はがきを書きました」
and 「若いころの私は、眠れないと感じても布団から出ず」 — not a belief, which is
exactly what the allocation asked to be checked.

### 5.2 TEMPLATE column, read down SEPARATELY (second pass, after the §3 repair)

| template | surfaces | count | cap |
|---|---|---|---|
| `〜のはBだ（分裂文）` | 問題10(5), 問題11(4) | 2 | 2 |
| `AほどBが多い（相関）` | 問題10(1) | 1 | 2 |
| `Aだけではない。Bこそが〜` | 問題11(2) | 1 | 2 |
| `〜のは、AではなくBだ` | 問題12(A) | 1 | 2 |
| T0 (unnamed) | 問題9, 10(2), 10(3), 10(4), 11(1), 11(3), 12(B), 13 | 8 | — |

The eight T0 finals read down as a column — the check the allocation says is
done by hand:

1. 問題9 — `Aであると同時にBでもある`（二重機能の要約）
2. 問題10(2) — `〈その十分〉がXを〜してくれる`（時間を行為主体に立てる）
3. 問題10(3) — `〜いただけますと助かります`（依頼の定型）
4. 問題10(4) — `〜お出しください`（指示の定型）
5. 問題11(1) — `Aで終わらずBまで含んでいる`（範囲の拡張）
6. 問題11(3) — `AのほかにBが必ずあった`（共通項の報告）
7. 問題12(B) — `〜であれば、〜していく`（条件→結果）
8. 問題13 — `〜書き入れておきたい`（意志・提案）

Eight distinct skeletons; no home-grown pattern carries more than one. **The one
near-pair is 1 and 5** — 問題9's `Aであると同時にBでもある` and 問題11(1)'s
`Aで終わらずBまで含んでいる` are both "not only A, also B" in function. Neither
is one of the five grammars in the not-A-but-B reframe family
(`AではなくB`/`というより`/`よりも`/`だけではなく`/`わけではない`), so the family
count stays at the allocated 2 (問題11(2), 問題12(A)) and the gate agrees
(`1 of 13 surfaces close on the reframe`, `1 matched` on the whole-passage net).
Both surfaces carry MOVE 機構の説明, and a mechanism with two parts genuinely has
two parts. **Recorded for QA as a watch item, not a repair** — four of thirteen
surfaces close on some "A plus B" shape, which is under every written cap but is
the axis that would tip first if 問題12 is ever re-angled.

**Both columns were re-read after the 問題13 connective repair** (§3). The repair
changed a paragraph-opening 逆接 and touched neither the closing sentence nor the
denial pivot, so neither column moved.

### 5.3 Persona — the open flag from the 読解 author, resolved

The author measured its own column as `職業人 ×3` against `PERSONA_CAP = 2` and
handed it here to re-label or re-read. **Resolved as a label-granularity
artefact: the four work-adjacent narrators are four different people, and only
one of them is a 職業人 in the sense the token means.**

| surface | author's label | recorded | why |
|---|---|---|---|
| 問題10(3) | 職業人・総務 | **実務者** | a 総務課 staffer sending a transactional request; the surface is a メール, not a narrator's account |
| 問題11(1) | 職業人・進行役 | **世話役** | the surface's own subject is 「紹介する役を頼まれる」 at a 会合 — a social role anyone can be asked to play, not an occupation |
| 問題11(3) | 職業人・建物点検 | **調査者** | 「私はこの十二年、五十ほどの建物を回って…数えてきました」 — a counter reporting a six-year ledger |
| 問題13 | 職業人・元部署員 | **職業人** | the only workplace-professional narrator: a former department member reflecting on handovers |

Final tally, all 14 読解 keys, every token at or under 2:
`観察者 2` (10(1), 10(5)), `実務者 2` (10(3), 12(B)), `論者 2` (11(2), 12(A)),
`解説者 1`, `趣味の実践者 1`, `町（お知らせ）1`, `世話役 1`, `調査者 1`,
`生活者 1`, `職業人 1`, `市（案内）1`. **No passage needed re-angling**, and
`check_topics_claim_field` is `ok`. 問題12(A)/(B) are split 論者 / 実務者 on a
real difference of vantage: A argues from the reader's side (「読む人が、最後に目
で探すのは」), B from the writer's (「案内文を書くとき」).

### 5.4 Errand identity — BY HAND (dispositions row 7b)

Both spec-time checks `skip` on this paper (`0 of 44 draws keyed`), and
`no 聴解1/2/3/5 errand repeats 20260914_1's` also `skip`s, so this is the only
place the rule is applied. I read the `shapes` column of this row against
`20260914_1`'s and `20260911_1`'s, row by row across §4.2.

**Result: no 聴解 errand of this paper repeats either of the two previous
papers.** The closest rows, all recorded rather than repaired (a composed half
has nothing to re-angle):

- **問題5-1番** — both this paper and `20260914_1` put a student club choosing
  among four options for a performance in the same slot (ダンスコンテストの小道具
  ／演劇部の汚れた衣装). Different errand (what to add vs how to hide damage), same
  shape. This is the `check_slot_theme_repeat` WARN in §7 wearing its content
  face.
- **問題1-1番 留守番電話** — `20260914_1` had a 留守番電話 item too, but in
  問題3-3番: a different 大問, a different slot and a different errand (confirm a
  lost umbrella vs collect a loaner phone).
- **問題1-5番 大学の事務室の手続き** — `20260911_1` 問題1-3番 was also a university
  office counter, two papers back, different slot. The 2-back minor-finding
  column.

**One WITHIN-paper finding, and it is the biggest thing in this report — see
§6, F2**: 問題3-2番 and 問題3-3番 run the same errand (an announcer reporting a
survey), on the same option SET, with the same keyed category.

### 5.5 Grammar form families — BY HAND (dispositions row 7b)

`grammar_form_families` covers 1/5 of 問題8 and 2/12 of 問題7, so the two
`draws at most one entry per form family` lines are nearly blind. I read all 16
keyed forms by hand:

問題7 限りでは・に対して・からには・を通じて・ばかりだ・だけのことはある・
あり得る・にかけては・ほしいものだ・てしかたがない・お目にかかります・ものの;
問題8 〜などあろうはずがない・〜に限らず・〜つつ…する・〜としても…ない・
〜ばかりか…も; 問題9 しかし・上がりようがない・次第だ・すだれと同じ働きだけ.

Two surface-token adjacencies, both checked against the archive (the primary
authority) and both cleared:

- **「〜限りでは」(問31) vs 「〜に限らず」(問題8-44)** — share the verb 限る. Not
  interchangeable in any sense, and no official item offers them as rivals:
  「に限らず」 occurs in 7 of the 31 `booklet.md` extracts, always against
  unrelated forms; 「限りでは」 occurs in none. Two grammar points.
- **「〜ばかりだ」(問35) vs 「〜ばかりか…も」(問題8-47)** — share ばかり, different
  connection (辞書形＋だ vs 名詞/普通形＋か requiring a 〜も clause) and different
  meaning (一方向の変化 vs 添加). Official sets ばかりか against からには／わりには／
  どころか, never against ばかりだ.

The one real collision on this seed (媒介: 〜を通じて / 〜を通して) was found and
rerolled in stage 2; `〜にかけては` (問38) and `〜を通じて` (問34) print none of
each other's forms, as stage 2's note records.

### 5.6 The 読解 and 聴解 rows read as ONE list

`check_surface_subjects()` cannot see two names for one subject, so I read all
13 読解 rows and all 29 聴解 rows together. Two hits, both in §6 (F1 within the
読解 half, F3 across the two halves). Everything else separates: the nearest
non-findings are 問題14 (犬の登録の手続き) beside 聴解問題1-5番 (学生証の再発行) —
both counter procedures, no shared decisive number or condition — and 問題10(5)
(古道具の値打ち) beside 聴解問題3-3番 (通信販売の利用理由), which share only the
domain 買い物, explicitly allowed since nobody here chose the 聴解 item's domain.
`no 問題14 decisive number is shared with any 聴解 item` is `ok`.

## 6. Findings — as written at stage 3, with 2026-09-21 dispositions

**Status as of 2026-09-21: F1 CLOSED, F2 CLOSED, F3 CLOSED, F4 CLOSED, F5 open
(minor, cross-test column).** The findings below are left EXACTLY as stage 3
wrote them — they describe the paper as it then stood, and rewriting them would
destroy the record of what was found. Each carries a `DISPOSITION (2026-09-21)`
line stating how it was closed and against what measurement. The same
dispositions are in `logs/topics.json` `notes` for this test.

None of the four was repairable by the stage-3 build context: three needed 読解
re-authoring and one needed a new RNG seed the brief made binding. All four were
closed later — three by the 問題12 (A+B) re-angle authored as a stage-2 pass, and
F2 by `TEXTBOOK_SLOTS["問題3"]` dropping to 1 plus the 2026-09-21 re-composition.

**F2 (highest) — 聴解問題3-2番 and 問題3-3番 are one item.**
Measured within this paper: spoken option-set Jaccard **0.571** (shared tokens
利用 / 利用方法 / 利用者数 / 理由), adjacent slots, both an announcer reporting a
調査結果, both keyed to the `〜を利用する理由` category.

```
問題3-2番 (mimikara:cd2-14)      1、電子書籍の利用者数。2、電子書籍で読める本。
                                 3、電子書籍を利用する理由。4、電子書籍の利用方法。  key 3
問題3-3番 (mondaireishuu:問3-1)  1、利用者数 2、買える品物の種類 3、利用方法
                                 4、利用する理由                                      key 4
```

These are **the exact two items whose CROSS-paper pairing founded
`check_choukai_option_set_reuse`** (`20260910_1` 問題3-3番 against `20260909_1`
問題3-3番, qa-report-20260910_1 F4), and 0.571 is the same number that founding
case scored. **Root cause:** both the gate line and its mirror in
`compose_choukai.draw()` compare a candidate only against `avoid_slot`, i.e. the
PREVIOUS paper — the source comment says so in as many words ("Hard bars…Both are
cross-paper"). Nothing in the repo compares two 問題3 clips of the SAME paper, so
this shipped green with 0 same-slot repeats and 0 any-slot repeats.
**Prescribed repair** (`check_choukai_option_set_reuse`'s own docstring): a
re-draw, `make mp3 20260917_1 SEED=<fresh rng>`. I did not substitute a seed —
the stage-3 brief makes `56017719` binding. **Root-cause row for the next run:**
extend the within-paper case into `draw()` and into the gate; that is a composer
change, which re-draws every paper's half at one seed, so it is an owner ruling,
not a stage-3 edit.

> **DISPOSITION (2026-09-21) — CLOSED, by pool shape rather than by seed.**
> `TEXTBOOK_SLOTS["問題3"]` is now **1** (RC-1's addendum: 2 would have made the
> collision deterministic, because the two colliding clips were the unique 2-use
> pair and 2 slots take exactly them), so only one 問題3 textbook clip can enter a
> paper and `mimikara:cd2-14` + `mondaireishuu:問3-1` cannot co-occur. The paper
> was re-composed by `make mp3 20260917_1 SEED=48767419`; its 問題3 textbook clip
> is `mondaireishuu:問3-1` alone, the other four 問題3 slots are official archive
> clips. **Measured on the shipped paper, not assumed:** within-paper spoken
> option-set Jaccard over all 435 pairs of the 30 items runs **max 0.143**
> (問4-3 × 問4-8), then 0.125 and 0.111 — nothing reaches 0.30, against the 0.571
> this finding recorded. The one 1.000 pair, 問5-2-1 × 問5-2-2, is structural
> (問題5-2番's two 質問 share one option list by format) and is excluded.
> The ROOT-CAUSE row above stays OPEN and is not closed by this: nothing in the
> repo still compares two 聴解 clips of the same paper, and the within-paper read
> remains a by-hand step (`qa/root-cause-20260917_1.md` RC-1).

**F1 — 問題10(1) and 問題12(A): one subject, two 読解 surfaces.**
Both argue that **daytime-only availability is what decides who reaches a public
channel**. 問題10(1): 五時で閉める市の相談者は昼間に家にいる人が多く、夕方まで開けた
市ほど働きながら親の世話をする人の相談が多い。問題12(A): 字を大きくしても届くのは
もともと昼間に電話をかけられる人で、夜しか時間の取れない人は切れる音を聞く。Both
even use 届く in the same sense. Two theme tags (医療・福祉 / メディア・情報) hide
it from every check; this is the class §"One topic, one surface" exists for.
**Repair: re-angle 問題12 (A+B) onto a fresh subject** — stage-2 work.

> **DISPOSITION (2026-09-21) — CLOSED by the prescribed repair.** 問題12 (A+B) was
> re-angled onto 「取材した相手に、記事を出す前に原稿を見せるかどうか（会報・広報の
> 書き手）」 in `_sections/問10-14_読解.md`, and `言語知識・読解.md` was re-merged
> mechanically from the three fragments. The shared subject is gone: 問題12 no
> longer raises 届く, 問い合わせ先, 昼間, 電話が通じる or 字を大きく at all, and its
> claim is now 「相手に確かめてもらうべきは、書き手の見方ではなく、調べれば答えの
> 決まることである。」 問題10(1) is untouched. `logs/topics.json` `surfaces` and
> `claim` for 問題12(A)/(B) were refreshed to the shipped wording the same day.

**F3 — 問題12(A) and 聴解問題2-3番 share a decisive detail across the halves.**
聴解2-3's talk opens 「資料を作る時は大きめの文字にするとか…とよく言われますが、まずは
聞き手の立場に意識を向けましょう」 and is keyed on 聞き手の立場; 問題12(A) raises
「だから字を大きくせよ、という直し方が広まった」 and supersedes it with the
receiver's circumstances. Same received prescription, same supersession. 読解 is
read before 聴解 in the sitting, so the priming runs 読解 → 聴解. At most two
surfaces may share a move across the halves, so this is AT the cap, not over it;
the finding is the shared decisive detail, not the count. **The 読解 side is
always the one re-angled** — the clip is lifted from a real sitting.

> **DISPOSITION (2026-09-21) — CLOSED on the 読解 side, as this finding prescribes.**
> The clip `2024-12:問題2-3` is in fact BACK in the 2026-09-21 draw, at 問題2-3番
> again — so this was closed by the re-angle, not by the clip's absence, which is
> the right way round. 問題12(A) no longer raises 「字を大きくせよ」 and no longer
> supersedes a received prescription about how to lay out a text; its subject is
> what a writer may ask an interviewee to check. Read against the shipped clip:
> the two share the formal 「AではなくB」 shape (which stage 3 itself made a binding
> constraint on 問題12(A), see the constraints paragraph below), but not the
> subject, not the artefact (プレゼン資料 vs 記事の原稿) and no carryable decisive
> detail — an adjacency, not a finding. Measured on the shipped script:
> 取材・記事・原稿・会報・広報・新聞・インタビュー・編集 occur ZERO times in
> `tests/20260917_1/聴解スクリプト.txt`.

**F4/F5 (minor, the cross-test column).**
F4: 問題12(B)'s mechanism — a reader takes in only the top of a notice — is one
paper back from `20260914_1` 問題10(3) (「一覧画面に出るのは初めの二十字ほど」),
under the same メディア・情報 tag; the artefacts differ (件名 vs 問い合わせ先) and
the prescriptions differ, so it is an adjacency, not a repeat.
F5: 問題13's claim that two people at one desk transfer what documents cannot
sits two papers back from `20260911_1` 問題12(A/B) on 窓口の二人制. Noted so the
domain does not become a crutch one skip apart.

> **DISPOSITION (2026-09-21) — F4 CLOSED, F5 still open (and still minor).**
> F4 named 問題12(B)'s old mechanism (a reader takes in only the top of a notice).
> That mechanism is gone: 問題12(B) now argues that the whole draft should be
> handed to the interviewee and that only writing-style demands are refused, which
> shares nothing with `20260914_1` 問題10(3)'s 件名 observation. F5 is untouched by
> the re-angle — it is about 問題13, which did not move — and stays recorded so the
> domain does not become a crutch one skip apart.

**Re-angling 問題12 (A+B) onto a fresh subject closes F1, F3 and F4 together.**
Its constraints if that is done: keep 問題12(A) 主張 + `〜のは、AではなくBだ` +
MOVE 反論への応答 and 問題12(B) 反論応答 + T0; `answer_positions.問題12 = [2, 3]`;
section length 510–600 JP chars; personas 論者 / 実務者; a theme free of this
paper's other twelve and absent from `20260914_1`'s and `20260911_1`'s headline
sets; and the draw replaced by `--reroll-one reading_topics:9`, never
hand-substituted.

## 7. `make check` — every line naming this test

Final run: **1 FAIL, 278 warnings repo-wide, five of which name `20260917_1`**
(plus one repo-wide WARN that mentions it in a note). 142 `ok` lines name it.

### FAIL

| line | disposition |
|---|---|
| `20260917_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)` — missing 1–71 | **Structural at this point in the pipeline, not repaired.** The 30 聴解 entries were written by `make mp3`; the 71 言語知識・読解 entries are stage 5's and authoring them before QA passes is prohibited. `20260910_1`, `20260911_1` and `20260914_1` all ended stage 3 in exactly this state. Clears when stage 5 runs. |

Two FAILs the first run opened are **gone**: `no 問題7/8/9 keyed form appears more
than 1× in the 問題10-14 prose` (repaired, §3) and `39 exam MP3(s) are on the
audio release` (`make upload-files TARGET=tests TEST=20260917_1`, 43.2 MB, the
manifest is committed with the test).

### WARN

| # | line | resolution |
|---|---|---|
| 1 | `the 問題8 form-family check compares most of the draw (1/5 = 20% family-tagged)` | **Dispositioned before this run** — `qa/stage2-notes-20260917_1.md` §"Standing pool debt that WARNs on this paper" and `qa/open-items-20260914_1-dispositions.md` row 7b. Repo-wide `pools.json` metadata debt, not a property of this draw; the substantive line beside it is `ok`. The floor is never lowered to green it. Compensating action done: §5.5. |
| 2 | `the 問題7 form-family check compares most of the draw (2/12 = 17% family-tagged)` | Same disposition. Coverage rose 1/12 → 2/12 from the 媒介 family stage 2 added. |
| 3 | `20260917_1 問題12: the shipped prose uses a 「メディア・情報」 word` | **Resolved as a token-list limitation, not a moved tag.** 問題12's own vocabulary is 広報 / 会報 / 案内文 / 問い合わせ先 / 読む人 / 読み手 — none of which is in `THEME_TOKENS["メディア・情報"]`, whose 13 words are all mass-media nouns (新聞/記事/放送/番組/記者/広告/紙面/読者…). The check's founding incident is an un-moved tag CONCEALING a rule-4 repeat; that mechanism is absent here — re-tagging 問題12 to the only other defensible value, 行政・手続き, would collide with 問題14 inside this paper (rule 3) and still clear rule 4, so the tag hides nothing. Widening `THEME_TOKENS` is forbidden by the docstring and was not done. Left as a known false positive for QA to confirm. |
| 4 | `聴解問題5 repeats a headline theme of 20260914_1 (composed paper) — ['スポーツ・余暇']` | **WARN by design and no repair exists** (`exam-blueprint` rule 4, split 2026-09-09). The only surface carrying スポーツ・余暇 is the composed 聴解問題5-1番; the 読解 half has nothing to re-angle and the only other lever is seed-shopping, which this repo forbids. Content read in §5.4. |
| 5 | `no 聴解 slot repeats its own theme in the previous 2 papers (2 slots)` — 聴解問題2-2番=働き方 (20260911_1); 聴解問題5-1番=スポーツ・余暇 (20260914_1) | **Rows read side by side, as the message asks.** 問題2-2番: 会社に決めた理由（本音で話せた） vs `20260911_1` 歌手がプロになった道筋 — different errand, the tag is the tagger. 問題5-1番: ダンスコンテストの小道具 vs `20260914_1` 演劇部の汚れた衣装 — same shape (a student club picking one of four for a performance), different errand; a real adjacency, recorded, and **not repairable** — both are lifted clips (§5.4). |
| — | `every stamped spec's pools_sha matches pools.json` | Repo-wide, and it names `20260917_1` only in its closing note about specs stamped on a REROLL. This paper's `pools_sha` is `c41a9d3182f6`, which IS the current `pools.json` — the note records that the sha certifies the `--reroll-one grammar_p7:7` redraw's pool. Not a defect; the check says so. |

`make check-tests` for this paper is otherwise all `ok` plus the six documented
composed/pre-stage-5 `skip`s (no セクション構成表, `validate_script` skipped for a
composed script, 問題5 2番's markers and printed options, the 聴解 authoring/
register/pacing band family, and the pacing sha).

## 8. `make choukai-wear` — what this paper's draw did

`make choukai-wear` exits non-zero. **This is the known, accepted, pre-existing
breach of `qa/open-items-20260914_1-dispositions.md` row 7a; I did not try to fix
it, did not grow `TEXTBOOK_SLOTS`, and did not let it block.**

| 大問 | slots | tb pool | projected before | projected now | measured tb (min/mean/max) |
|---|---|---|---|---|---|
| 問題1 | 2 | 15 | 3.60 | 3.73 | 3 / 3.73 / 4 |
| 問題2 | 2 | 15 | 3.60 | 3.73 | 2 / 2.33 / 3 |
| 問題3 | 3 | 19 | **4.26** | **4.42** | 3 / 3.32 / 4 |
| 問題4 | 4 | 36 | 3.00 | 3.11 | 2 / 2.53 / 4 |

The mixed-paper count went 27 → 28, which is the whole of the movement: 問題3's
projection is `3 slots × 28 papers ÷ 19 items`. Official clips are unaffected
(1.22–2.90 per slot). This paper spent 11 slot-free clips and pushed three of
them to 4 uses — `soumatome:cd1-60` (問題1-1), `soumatome:cd2-2` (問題1-2) and
`soumatome:cd1-33` (問題3-4) — so the MEASURED maximum is still exactly the 4.0
ceiling, with the projection over it. 19 問題3 slot-free clips now sit at 4 uses.
The prescribed fix is pool growth (the user's 2026-09-14 directive to bank all 31
archive sittings), not a slot change; row 7a raises it to the user.

## 9. The two stage-2 hand-off flags

**Flag 1 — 問32's distractor 「に加えて」 beside 問題6-30's drawn headword 「加える」.
Ruled ALLOWED; no change made.**

The question the pass has to answer is "does a candidate meet the tested 問題6
headword as printed text elsewhere in the paper", and the answer is: it meets a
different grammar point built on the same verb, in a direction that gives nothing
away.

- **No rule is breached.** Item-integrity #15 governs KEYS. 問題6-30's key is a
  usage sentence (「会議の資料に、昨日調べた数字を新しく加えました。」); 問32's key
  is 「に対して」. Neither item keys the other's form, and 「に加えて」 is 問32's
  option 2, a distractor.
- **Nothing transfers in either direction.** 問題6-30 discriminates on which
  OBJECT 加える takes — 数字を加える ✓ against スピードを加え ✗ / 見学会に加え ✗ /
  苦情を加え ✗. 問32 exposes only the compound particle's additive sense, which
  does not decide any of those four. Conversely, knowing that 問題6-30's key is
  sentence 4 says nothing about whether 問32 wants a contrast particle.
- **No 問題6-30 option prints the compound particle**, so the 問題6 item cannot be
  solved by pattern-matching the 問32 option either.
- Ordering also runs the harmless way: 問題6 is answered before 問題7.

Recorded rather than silently passed, because the class (a 問題7 option meeting a
tested item one surface over) is the `20260907_1` mechanism and the next paper
should be read for it.

**Flag 2 — the 職業人 ×3 persona reading. Resolved by re-labelling, not
re-angling; full table and reasoning in §5.3.** Every token now sits at or under
`PERSONA_CAP = 2` and `check_topics_claim_field` is `ok`.

## 10. 聴解 draw audit — result

- **0 of 29 clip ids and 0 of 5 preambles repeat `20260914_1`** — in the same
  slot, and (the 2026-09-10 half of the rule) for a slot-free clip in ANY slot.
  Verified directly against `logs/choukai_draws.json`, not re-derived from the
  bank.
- **The composer printed no starvation note.** Its only note was the standing
  exclusion of two figure items whose options are picture regions
  (`2021-12:問題1-5`, `2022-12:問題1-2`). No slot was exhausted and no bar was
  dropped.
- **No within-大問 personal-name clash** in this paper. One name carries over to
  `20260914_1`'s 問題4 (`佐藤`) on a different errand — `choukai-audio` Part 0
  rule 4 says explicitly that a shared surname on a different errand is not a
  defect and must not be "repaired".
- **Two-and-three-papers-back repeats, all slot-free and all in a different
  slot** (the minor-finding column, and a direct consequence of the row 7a wear
  breach): `kanzenmoshi:cd1-14` (問題2-1 here, 問題2-5 of `20260911_1`),
  `mondaireishuu:問3-1` (問題3-3 here, 問題3-2 of `20260911_1`),
  `kanzenmoshi:cd1-15` (問題2-2 here, 問題2-3 of `20260910_1`),
  `kanzenmoshi:cd1-30` (問題4-9 here, 問題4-6 of `20260910_1`).
- Source mix: official 18, kanzenmoshi 4, soumatome 3, mimikara 2,
  mondaireishuu 2; drawn from 8 sittings (2021-07 ×1, 2021-12 ×4, 2022-07 ×1,
  2022-12 ×3, 2023-07 ×2, 2024-12 ×2, 2025-07 ×2, 2025-12 ×3).
- **No slots "moved"**: this was the paper's FIRST composition, so there is no
  previous `logs/choukai_draws.json` row for it to be diffed against. `make mp3`
  was run exactly once.

## 11. What I skipped, and why

- **`make model-answer` / `make scaffold-explanations`** — stage 5, prohibited
  before QA passes. This is why the one remaining FAIL is open.
- **The three 読解 re-angles F1/F3/F4 imply, and the F2 re-draw** — all four are
  authoring or seed decisions. A build context that authors a surface and then
  audits it breaks both context-isolation rules, and the MP3 seed was made
  binding by the brief. Handed to stage 4 / the orchestrator.
- **`refs/` binaries** — not needed. The one archive question this pass asked
  (do official items ever pair 限りでは/に限らず, or ばかりだ/ばかりか, in one
  option set?) was answered from the tracked `booklet.md` extracts, which §3 of
  `AGENTS.md` names as exact.
- **`make pages`** — not part of stage 3.
- **Nothing in any other test's folder was touched**, no `make sample` was run,
  and neither `.agents/` nor `pools.json` was edited.
