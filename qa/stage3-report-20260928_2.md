# Stage 3 (build + gate) — 20260928_2

Run 2026-09-28 in one context. This context authored nothing and changed no
authored wording. The only file it wrote by hand is the `logs/topics.json` row.

## 1. What I read, in full, from disk

- `AGENTS.md`, `CLAUDE.md`
- `.agents/exam-app/SKILL.md` (whole file)
- `.agents/choukai-audio/SKILL.md` (whole file, Part 0 first)
- `.agents/jlpt-test-generation/SKILL.md` (whole file: the pipeline table, the
  reading map, §"Stage 3 — build + gate", §"One topic, one surface",
  §Invariants)
- `.agents/exam-blueprint/SKILL.md` §"Topic themes", §"The four theme rules"
  (rules 1–5, 4b, 4c) and Part II through §"What still governs a self-authored
  surface"
- `qa/dokkai-allocation-20260928_2.md`, with its final-sentence column filled in
  by both authors
- `qa/stage3-report-20260928_1.md`, as a format model only
- `logs/topics.json`: the rows for `20260928_1` and `20260917_1`, all fields,
  plus a keyword search of every earlier row (§5.4)
- While resolving specific lines I also read:
  - `question-authoring/references/bunpou.md` §"問題9 options" (the 16-option
    comparison)
  - `tools/check_consistency.py`: `check_invented_proper_nouns`,
    `PLACE_STOP`, `check_p14_choukai_shared_decider`, `check_topics_claim_field`
  - `tools/compose_choukai.py`: `MUTUALLY_EXCLUSIVE_CLIPS` and its comment
- Inputs:
  - the three `tests/20260928_2/_sections/*.md` fragments, read through the
    merged `言語知識・読解.md`, from 問題7 to the end of 問題14 plus the 読解 key
  - `tests/20260928_2/test_spec.json`, including all 12 `reading_topics` avoid
    lists
  - the composer's `聴解スクリプト.txt` and `聴解.md`, read in full
  - `logs/choukai_draws.json`

## 2. Every command I ran, in order

```
make assemble 20260928_2
make autofix 20260928_2                  # clean, nothing changed
make lint-draft 20260928_2               # clean
make verify-scramble 20260928_2          # exit 0; all five UNDECIDED (see §7)
make mp3 20260928_2 SEED=99207311        # the only seed used
python3 tools/choukai_segment.py tests/20260928_2/聴解.mp3
make upload-files TARGET=tests TEST=20260928_2
make booklet 20260928_2
make sheet 20260928_2
make check                               # run 1: 3 FAIL (no topics row yet)
make findings                            # to attribute WARNs to test ids
make check                               # run 2, after the topics.json row: 4 FAIL (my empty 問題14 closing_moves entry)
make check                               # run 3, entry removed (final, §6)
```

**Seed.** Exactly one: `99207311`, verbatim from the brief. No re-draw was
needed (§4.3), so no other seed was drawn.

## 3. What I wrote

- `tests/20260928_2/言語知識・読解.md`: written by `make assemble`, not touched
  afterwards (autofix changed nothing).
- The whole 聴解 half, written by the composer: `聴解スクリプト.txt`, `聴解.md`,
  `聴解.mp3`, `聴解_チャプター.json`, and the 30 聴解 entries in each
  `詳細解説` pane.
- `言語知識・読解.html`, `聴解.html`, `解答.html`, `練習.html`, from
  `make booklet` and `make sheet`.
- `logs/choukai_draws.json`: one row appended by the composer. The 18 earlier
  rows are byte-identical to the pre-run copy.
- `logs/upload_manifest.json`: updated by the upload (38 assets).
- `logs/topics.json`: one row appended for 20260928_2 (218 added lines, no
  other row touched). It has these maps:
  - `surfaces`, `themes`, `claim` (43 keys: 13 読解 + 問題14 + 29 聴解)
  - `shapes` (29 聴解)
  - `closing_moves`, `voices`, `persona` (the 読解 keys)
  - `notes`, which include the 16 問題9 options and the open stage-3 findings

  The gate reads 5 of 5 「…」 spans as found in the paper.

**Source shas at hand-off** (sha1, first 12):

| file | sha |
|---|---|
| `言語知識・読解.md` | `48072951e7cb` |
| `聴解.md` | `cb28c3866e56` |
| `聴解スクリプト.txt` | `d80f64cc678a` (matches the chapters' `script_sha`) |
| `聴解.mp3` | `976c80a6e2e5` |

## 4. Build results

### 4.1 Segmentation

`ok  20260928_2  45.3 min  LUFS -15.14  問題1:5 問題2:6 問題3:5 問題4:11 問題5:2`.
It recovers **5/6/5/11/2**, as required.

### 4.2 Upload

`make upload-files TARGET=tests TEST=20260928_2` uploaded `20260928_2.mp3`
(43.5 MB) to release `audio`, exit 0. The active gh account is `feiluvnana`. I
switched no account. The gate reads `29 exam MP3(s) are on the audio release`
with no mismatch.

### 4.3 The composed draw

- **Composer output:** 45.3 min, 34 chapters. The source mix is official 20,
  soumatome 7, shinkanzen 1 and kanzenmoshi 1. It draws from 8 sittings.
- **Composer notes:**
  - the standing figure exclusion (4 items)
  - ffmpeg `Invalid PNG signature` noise, which is cover art in source MP3s and
    harmless
  - **No freshness bar was dropped, and no slot starved.**
- **Diff against the previous row, `20260928_1`:**
  - 0 of 29 clip ids repeat in the same slot.
  - 0 slot-free clips repeat in any slot.
  - 0 of 5 preambles repeat.
  - No clip appears twice within the paper.
- **Slots moved:** none. This is the paper's first composition, so there is no
  earlier row of its own to diff. The 18 earlier rows are unchanged.
- **Two papers back (`20260917_1`):** two slot-free clips repeat, each in a
  different slot. The composer's one-paper bar allows this. I recorded it and
  did not re-draw.
  - `soumatome:cd2-5` (the sick dog at the vet) was 2-5番 there and is 2-6番
    here.
  - `kanzenmoshi:cd1-37` (「ないなあ、この辺にしまったはずなんだけど…。」) was
    4-6番 there and is 4-11番 here.
- **Gate:** `no 問題3 option set repeats 20260928_1's (worst 0.125, ceiling
  0.30)` is `ok`, and the `script_sha` stamp matches.

## 5. The whole-paper table

### 5.1 読解 + 問題9 cloze

Each `reading_topics[i]` entry gives a theme and an avoid list, with no subject
string. So "drawn" below is the theme. "On draw" means the shipped subject is
about that theme and is not on, or a re-wording of, that entry's avoid list. I
searched every avoid list by keyword.

| surface | shipped subject | theme (shipped = drawn) | on draw | closing | template | MOVE | persona | 20260928_1 same seat | 20260917_1 same seat |
|---|---|---|---|---|---|---|---|---|---|
| 問題9 | 家が鳴る音 (drying wood releases stored stress at joints) | 住まい (author-composed, RNG pick) | yes | 意外な観察 | unnamed (`…には、もう、…ほどの（力がたまらない）`) | 機構の説明 | 観察者 | 案内板で乗り換える | 緑のカーテン |
| 10(1) | 記念品の手ぬぐいを二色で染められるか（メール） | 文化・伝統 | yes | 実用文 | — | （実用文） | 実務者 | 杖の持ち方 | 窓口の開く時間帯 |
| 10(2) | 将棋教室の受付表：同期と指した人ほど残る | スポーツ・余暇 | **NO: near-miss (F4)** | 条件提示 | 相関 (`ほど…割合が高い`) | 数えたことの報告 | 受付係 | 保育園の門の暗証番号 | 旅の絵はがき |
| 10(3) | 二度目のお礼 | 人間関係 | yes | 随筆 | unnamed (`…のもとへ…を運んでいく`) | 一人称の前後比較 | 生活者 | 夕食後のうたた寝 | 弁当屋へのメール |
| 10(4) | 見積もりと待つ時間 | 働き方 | yes | 説明 | 分裂文 | 機構の説明 | 解説者 | 食器を洗って返すかのメール | 屋上駐車場のお知らせ |
| 10(5) | 教科書を教室に置いて帰れる（中学校のお知らせ） | 教育 | yes | 実用文 | — | （実用文） | 学校（通知） | 給料日の書き出し | 古道具の直した跡 |
| 11(1) | 雑貨店の傘は晴れた朝のあとの雨で売れる | 消費・経済 | yes | 意外な観察 | unnamed (`…を片手に…開けるのだ`) | 数えたことの報告 | 店員 | ブロック塀の点検 | 紹介のしかた |
| 11(2) | 商店街：呼び込みより一角を貸す | 地域活性化 | yes | 主張 | `AよりBのほうが` | **〈想定→実は〉** | 住民 | 窓を開ける5分 | 教室の30分宿題 |
| 11(3) | 小さなかばんの旅 | 旅行・観光 | yes (family note, §5.4) | 随筆 | unnamed (`…たびに…一つ増えます`) | 一人称の前後比較 | 旅行者 | 無人駅の待合室の当番 | 通路の私物 |
| 11(4) | 消防団の昼の団員 | 防災 | on theme, **but a re-skin of 20260928_1 11(1) (F3)** | 反論応答 | `わけではない` | 反論への応答 | 消防団員 | ます目のノート | 眠れない夜 |
| 12(A) | 端末のメモが見返されない仕組み | デジタル化 | yes | 説明 | unnamed (`…あいだだけ…呼び出される`) | 機構の説明 (A+B one) | 解説者 | 職場での呼び方 | 会報の事実確認 |
| 12(B) | 翌朝に開き直す決まり | デジタル化 | yes | 条件提示 | unnamed (`…と決めておけば…読み返される`) | ″ | 実践者 | ″ | ″ |
| 13 | やさしい日本語のお知らせ | 行政・手続き | yes | 反論応答 | unnamed (`AとBは…並び立ちます`) | 反論への応答 | 市職員 | 寄席と落語の筋 | 引き継ぎ |
| 14 | みずほ市チャイルドシートの貸し出し | 子育て・家族 | yes | — | — | （実用文） | 市（案内） | 給食センター親子見学会 | 犬の登録と予防注射 |

**Theme rules, counted on the shipped surfaces:**

- **Rule 1:** the five headline surfaces take five different themes: 問題9
  住まい, 12 デジタル化, 13 行政・手続き, 14 子育て・家族, and 聴解問題5
  (スポーツ・余暇 + 旅行・観光). The gate line is `ok`.
  - My tag for 5-1 is a judgement call. It is a sports centre's staff moving a
    parent–child football class to a smaller pitch, and I tagged it
    スポーツ・余暇 from the prose. 子育て・家族 would collide with 問題14, and
    rule 4c forbids retagging to dodge a rule. I read 親子 as the audience, not
    the subject.
- **Rule 2:** no 読解 headline theme appears on another 読解 surface. Under the
  lenient reading, 聴解問題5's スポーツ・余暇 and 旅行・観光 tag 10(2) and 11(3),
  which is allowed.
- **Rule 3:** 13 of 13 読解 themes are distinct.
- **Rule 4, one paper back:** no 読解 headline repeats 20260928_1 (`ok`).
  聴解問題5-1 スポーツ・余暇 repeats 20260928_1 聴解問題5-1. That is the composed
  half, so it is a WARN only (§6).
- **Rule 4, two papers back:** one repeat, 問題13 行政・手続き against
  20260917_1 問題14 (the dog-registration notice, a different subject). That
  spends the budget of one (`ok`).
- **Rule 4b (headline subjects against 20260928_1's 13 読解 and 29 聴解
  subjects):** no match.
  - Same setting, different issue: 聴解問題5-1 (a parent–child football class
    with low sign-ups; the venue moves) against 20260928_1 聴解問題2-2 (a
    parent–child event plan with no parking).
- **Rule 5 (voice):** 9 first-person surfaces, 3 in です・ます throughout, and
  kanji density 30.0%. The gate's three lines are `ok`.
- **Persona cap of 2:** 解説者 ×2 (10(4), 12(A)). Every other token appears
  once.
  - I tagged 問題9 観察者, not 解説者. It starts from an observed phenomenon and
    then gives the mechanism, as 20260928_1 10(3) did under 観察者.
  - All 11 proposed personas match the prose: 受付係 「初心者の受付を八年」; 店員
    「雑貨店で働いて」 (not the 店主); 消防団員 「私たちの団」; 実践者 (the 7 a.m.
    rule); 市職員 「私は市役所で」.

**問題12 cross-test column:** 端末のメモ (here), 職場での呼び方 (20260928_1),
会報の事実確認 (20260917_1). All three differ.

### 5.2 聴解: a draw audit

Keys are from `聴解.md`.

| slot | clip | shipped subject | theme | 20260928_1 same slot | 20260917_1 same slot |
|---|---|---|---|---|---|
| 1-1 | soumatome:cd1-44 | 出張帰りの新幹線を先に変更 | 働き方 | ガラス体験、まずエプロン | 携帯店の留守電 |
| 1-2 | 2024-07:問題1-2 | 値引きシールが先、豆は後 | 働き方 | 図書館、土曜に来る | 説明会の作業分け |
| 1-3 | 2023-07:問題1-3 | 振込で払える、振込先を確認 | 消費・経済 | オーケストラのパンフ | 家具の寄付 |
| 1-4 | 2025-07:問題1-4 | 野球大会の片付け、まず手袋 | スポーツ・余暇 | 市民文化祭の応募 | レストランの追加注文 |
| 1-5 | soumatome:cd2-2 | プログラム訂正の貼り紙 | スポーツ・余暇 | 文化祭ライブの手伝い | 学生証の再発行 |
| 2-1 | soumatome:cd1-30 | 前の会社を辞めた理由（責任ある仕事） | 働き方 | 眼鏡はコンタクトを切らした | 郵便局の配達 |
| 2-2 | 2021-12:問題2-2 | 塾からレストランへバイトを換えた理由 | 働き方 | 親子イベント、駐車場がない | 企業実習の期待 |
| 2-3 | 2024-07:問題2-3 | 社内アンケート、休暇申請を簡単に | 働き方 | 考察と引用の区別 | 課長が問題にした報告 |
| 2-4 | 2025-12:問題2-4 | 先輩が会社を選んだ点（在宅） | 働き方 | フリマ、値段順 | 家具作りの魅力 |
| 2-5 | 2022-12:問題2-5 | 保育実習、目の高さで話す | 教育 | 転職の理由 | 犬の容体 (**this paper's 2-6 clip**) |
| 2-6 | soumatome:cd2-5 | 犬は寝てばかり | 医療・福祉 | 事務室へ鍵を借りに | 就職先の理由 |
| 3-1 | 2024-07:問題3-1 | 歯の役割 | 睡眠・健康 | 仲間言葉の方言 | リーダーを断る |
| 3-2 | 2025-12:問題3-2 | 研修、前半期待外れ・後半満足 | 働き方 | 同じミスを繰り返さない | 夏の体調不良 |
| 3-3 | 2025-07:問題3-3 | お菓子屋の喜び | 人間関係 | 子どもの注意のしかた | 高齢者の社会貢献 |
| 3-4 | 2025-07:問題3-4 | 良い睡眠の条件 | 睡眠・健康 | 蜂を飼う注意 | 通販の利用理由 |
| 3-5 | soumatome:cd2-29 | 先に答えてしまう学生 | 教育 | 道路と橋の整備 | 雲の発生 |
| 4-1…11 | 2024-07:4-1, 2025-07:4-2, 2024-07:4-3, 2025-12:4-4, shinkanzen:cd2-66, soumatome:cd2-47, 2025-07:4-7, 2024-12:4-8, 2023-12:4-9, soumatome:cd1-40, kanzenmoshi:cd1-37 | see the `shapes` map | 働き方×4, 人間関係×3, 教育, 旅行・観光, 消費・経済, スポーツ・余暇 | — | 4-11's clip was 20260917_1 4-6 |
| 5-1 | 2025-07:問題5-1 | 親子サッカー教室、会場を小さく | スポーツ・余暇 | ダンスの小道具 | 和菓子店の貼紙 |
| 5-2 | 2025-07:問題5-2 | 緑市の夕日、夕日通りと西が丘 | 旅行・観光 | 四種の自転車 | 科学イベント |

The shipped 聴解 theme tally is 働き方 11, スポーツ・余暇 4, 人間関係 4, 教育 3,
消費・経済 2, 睡眠・健康 2, 旅行・観光 2 and 医療・福祉 1. This is a draw audit,
so nothing is re-angled (exam-blueprint rule 3).

## 5.3 The reads, one axis at a time

### MOVE column, read down on its own (読解)

The counts match the allocation exactly:

| MOVE | surfaces | count |
|---|---|---|
| 機構の説明 | 問題9, 10(4), 12 | 3 (at its ceiling) |
| 数えたことの報告 | 10(2), 11(1) | 2 |
| 一人称の前後比較 | 10(3), 11(3) | 2 |
| 反論への応答 | 11(4), 13 | 2 |
| 〈想定→実は〉 | 11(2) | 1 |

**The skeleton read** uses the three-beat rubric: an attributed assumption, an
explicit denial, then 実は Y. It covers the ten essay surfaces, with 12 A+B
counted as one.

- **Conservative count, 読解: 1**, which is 11(2).
  - The assumption is attributed: 「多くの町がそう考え」.
  - The denial is 「ところが…三軒しかない」.
  - Y is the 一角 shops.
  - Deletion test: without the denial, the final's comparison has nothing to
    stand on. It is genuinely on the skeleton, as planned.
- **Borderline, not counted:**
  - **13.** It concedes the objection's claim that easy words drop conditions.
    Then 「抜けが生まれていたのは、一つの文に条件をいくつも詰め込んだときでした」
    moves the cause to sentence structure, and 「…減らす必要はありません」 denies
    it. That is close to 〈原因 X → 実は Y〉. The allocation labels it
    反論への応答, and the objection is answered on its own terms. **QA should
    rule on it.**
  - **11(1).** 「雨の強さと売れた数とは、ほとんど結びついていなかった」 runs
    against an unattributed natural expectation. It is a fact, not a held
    belief, which is what the allocation asked for.
- **The other checks:**
  - 問題9 and 11(1) mismatches are facts.
  - The "before" in 10(3) and in 11(3) is a PRACTICE.
  - Neither count (10(2), 11(1)) is framed against a stated expectation.
  - 11(4) and 13 both concede the objection (「もっともな」) and answer it.
- **Gate:** `0 of 13` is its marker-bearing instrument, not this read.

### TEMPLATE column, read down separately

- **Named templates:**
  - 相関 ×1 (10(2)). It becomes ×2 if 11(3)'s proportional
    「…たびに…一つ増えます」 is read as 相関. Either way it is within the cap of 2.
  - 分裂文 ×1 (10(4))
  - `AよりBのほうが` ×1 (11(2))
  - `わけではない` ×1 (11(4))
- **Cap-1 templates:** none used.
  - 11(1) ends 〜るのだ, not 〜ていたのだ.
  - 問題9 ends 〜ない, not 〜ていない.
  - No surface ends 先回り.
- **The not-A-but-B family** has 2 members, 11(2) and 11(4), as allocated.
  - 12(B) carries the foil-denial 「だからといって、紙の手帳に戻ることはないと私は思う」
    in a non-final sentence.
  - Its final names no foil, so I did not count it. I recorded it for QA.
- **The unnamed finals, read as a column:** no two share a skeleton.
  - 問題9 is a degree-negation; 11(1) is an affirmative scene plus のだ.
  - 10(3) is a motion metaphor; 11(3) is 比例 たびに.
  - 12(A) is the あいだだけ limitation; 12(B) is a ば-condition.
- **The skeleton read below the final line** is not clean. 11(4) and 13 run the
  **same body scaffolding** (F3b):
  1. 「〜には、〈団／市役所〉の中からも…反対の声があ（っ）た」
  2. the objection
  3. 「〜というの（である／です）」
  4. 「この心配（には／は）、もっとも…」

  That concession sentence is also the third consecutive paper's:
  20260917_1 11(2) 「この心配にはもっともな（注2）ところがあり」 and 20260928_1
  12(B) 「この声はもっともだ」.

### 読解 and 聴解 rows, read as ONE list

- **F1 (the gate): 問題14 × 聴解問題1-3番 share 2週間, and it is decisive on
  both sides.**
  - The flyer's short-rental cap 「2週間まで」 decides 問71: 10 days counts as
    the short rental.
  - 1-3番's 「クレジットカードは自宅に届くまで2週間くらいはかかるかも」 is what
    kills option 4.
  - The regex does not normalise numerals, so it misses the flyer's
    「1週間前までに」 against 聴解2-2番's 「一週間ごとに」. That pair is not
    decisive on the 聴解 side (2-2 keys on schedule flexibility) and is not a
    finding.
- **Domain adjacencies, with no shared decisive detail:**
  - 問題14 (child seats) / 聴解2-5 (a nursery practicum)
  - 11(4) (a fire brigade) / none
  - 13 (municipal notices) / none
  - 10(4) (waiting time at work) / 聴解2-3 (a work-conditions survey)
- **聴解-internal clusters, recorded for QA:**
  - 問題2 1-4番 are all job or work items.
  - 在宅勤務 is 2-3番's distractor (the man's wish) and 2-4番's key.
  - The surname 山下 appears in 聴解1-5番, 聴解2-5番 and 問題14-70. Different
    大問, so it is not a defect under choukai-audio rule 4.
- **The cross-half 〈想定→実は〉 cap of 2:**
  - 聴解, conservative: **1**, which is 3-4番. 「睡眠時間は長ければいいという
    ものではありません。睡眠によって十分な休養が取れたと感じられることが大切です」
    has all three beats: the common view, the denial and 実は Y.
  - 聴解, borderline and not counted: 3-2番 (「…楽しみにしていたんですが、時間の
    関係でだいぶ削られたんですよ」). This is an expectation disappointed, with no
    reinterpretation Y. 2-2番's 「塾のシフト、減らしてもらえばよかったんじゃない?」
    is a suggestion turned down, not a belief denied.
  - **Total 2 (11(2) + 聴解3-4) = the cap.** No re-angle is owed. The one
    headroom slot the allocation planned is spent by 聴解3-4.
  - If QA counts 13 (above), the total is 3 and 13 is the surface to re-angle,
    since 11(2) is the planned member.

### 5.4 Cross-test, 読解

- **F3: 11(4) re-runs 20260928_1 11(1).** One paper back, and the same kind of
  surface. The two share all of these:
  - the theme, 防災
  - the closing shape 反論応答 and the template `わけではない`
  - the claim: lay residents are objected to as unqualified, and the answer is
    that they are not being asked to do the experts' job
  - the apparatus:
    - 「私の住む町内会では…」 against 「私の住む町の消防団（注1）では…」
    - 「反対の意見があります…という意見です。この心配には、うなずける（注4）点があり」
      against 「反対の声があった…というのである。この心配には、もっともなところがある」
    - 「…わけではないのです」 against 「…わけではない」

  The subjects differ (checking block walls, a daytime fire-brigade role). But
  §"One topic, one surface" says a shared domain in one row is a finding even
  when theme tags differ, and here even the tag matches. A candidate who sat both
  papers would recognise the essay.
- **F4: 10(2) is a near-miss of an avoid entry.**
  - The entry is スポーツ・余暇 `reading_topics[1].avoid`, 20260910_1 11(1):
    `市の体育館の卓球開放日で、四年分の帳面の欄を並べ替えても…帳面になかった初日の帰り際の五分が分かれ目だった（受付台の手伝いを四年続けて記録してきた人）`.
  - It matches 10(2) on setting (a public hobby session), narrator (a reception
    volunteer of N years), method (reading back sign-in sheets) and question
    (who keeps coming). Only the answer differs.
  - exam-blueprint Part II: "A near-miss counts as used."
  - Its claim also echoes 20260928_1 11(3) (a rota stays when paired with last
    year's member). That makes "records show continuation depends on who you
    were paired with" three papers running, counting 20260914_1 11(1).
  - The 「N年分の記録を読み返して数える」 crutch that 20260928_1's stage 3 flagged
    for the next allocation is back on two surfaces here, 10(2) and 11(1). That
    is the allocation's choice; the authors followed it.
- **Minor findings (recorded; no rule broken):**
  - 10(1) is the **third consecutive** 問題10 business email in which a company
    総務課 asks an outside supplier whether an order for a company event can be
    varied and still delivered in time. Its letterhead `みなと電機総務課` is one
    word off 20260917_1 10(3)'s `あおば電機総務課`.
  - `あおば` also names this paper's school in 10(5), as 「あおば市立ひがし中学校」.
    Apparatus near-verbatim from two back.
  - 10(5) is a school-to-parents notice, one paper after 20260928_1 10(2)'s
    nursery-to-parents notice. The document type repeats; the institution and
    the errand differ.
  - 11(3) belongs to the same family as 20260827_2 11(4) `地図を持たない旅` and
    20260904_2 11(3) (asking locals is what creates the encounter). I judge it a
    different subject: packing light, and asking for missing things.
  - 11(1) and 20260917_1 10(5), two back: in both, a shop's own records reveal
    what customers actually do.
  - 問題9 blank 49 is a body-part idiom blank (口に合う/目を引く/耳につく/胸を打つ),
    as 20260928_1 blank 51 was (…/目についた). No idiom is shared.
  - 問題9 blank 50's distractor わけではない is 11(4)'s final template.
- **The 16 問題9 options against the previous two papers and this spec:** 0
  exact repeats. `すると` matches the spec only inside the 問題8 key `からすると`.
  The list is in the `notes` field.

### 5.5 Errand identity: `shapes` across three papers, read by hand

- **Same-clip repeats two back:** `soumatome:cd2-5` and `kanzenmoshi:cd1-37`
  (§4.3). Recorded, not re-drawn: a re-draw to escape a repeat the policy allows
  would be seed-shopping.
- **Candidate errand pairs.** Each was read side by side. **None is identity**
  by the standard `MUTUALLY_EXCLUSIVE_CLIPS` was built on (same errand, same
  implicature, same key):
  - **2-1番 × 20260928_1 2-5番** (one back). A woman explains why she left her
    previous job. The keys differ (責任のある仕事をさせてもらえない against
    新しい分野の仕事をしてみたかった), and so do the options and the format (a
    job-interview monologue against an interview dialogue). This is the
    closest pair in the paper, and QA should confirm it.
  - 2-4番 × 20260917_1 2-6番 (two back): why this company (在宅 against
    本音で話せた).
  - 1-4番 × 20260928_1 1-1番: the first step is putting on protective gear
    (gloves before a tent teardown; an apron at a glass workshop). The errands
    differ.
  - 4-1番 × 20260917_1 4-1番: a complaint about memorising kanji. One reply
    encourages and the other sympathises.
  - 5-1番 × 20260928_1 5-1番: a group picks one fix for an event. That is the
    format of 問題5-1.
  - Gate slot-theme WARN pairs: 2-2 (changing part-time jobs) against
    20260917_1 2-2 (internship expectations) and 20260928_1 2-2 (an event
    plan's problem); 2-3 (what to write in a survey) against 20260917_1 2-3
    (what the section chief faulted). All have different errands.
- **No re-draw, and nothing added to `MUTUALLY_EXCLUSIVE_CLIPS`.**

## 6. `make check`: every line naming 20260928_2 (final run)

The final run ends `FAILED — 3 problem(s)`. The whole gate prints 5235 ok,
214 WARN and 231 skip. The full output is at
`/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/72237c98-7f53-47d8-ba10-9abc5cd01c31/scratchpad/s3_20260928_2_check3.txt`.

### FAIL

| line | disposition |
|---|---|
| `20260928_2: 問題14 shares no decisive number with any 聴解 item — both surfaces turn on ['2週間']` | **Content (F1), routed to the 読解 author.** The 聴解 side is a banked clip, so the flyer's number moves. `3週間` is not in the script, so 「3週間まで」 is free, for example. Then 問71's stem and 解説 must be re-derived. |
| `20260928_2: no invented place name repeats the previous 2 papers — 「私の住む町」 (also 20260928_1); 「私は市」 (also 20260928_1)` | **Both hits are generic phrases, not invented names**, and so gate false positives of the class `PLACE_STOP` exists for: 「私の住む町」 in 11(2) and 11(4), against 20260928_1's `私の住む町内会`; `私は市` from 13's `私は市役所で`, against 20260928_1 10(5)'s `私は市の相談窓口で`. I did **not** edit the gate, because adding stop-list entries loosens it and needs the user's OK (memory). But the 11(4) half is a real apparatus echo, part of F3, and re-authoring 11(4) clears it. The rest clears either by the stop-list decision or by rewording 11(2)'s and 13's openings. **For the orchestrator.** |
| `20260928_2: 詳細解説.json explains every keyed item (30 entries for 101 keys)` | **Structural at stage 3.** The 30 聴解 entries come from `make mp3`. The 71 言語知識・読解 entries are stage 5, which is prohibited before QA passes. |

### WARN

| line | disposition |
|---|---|
| `聴解問題5 repeats a headline theme of 20260928_1 (composed paper) — ['スポーツ・余暇']` | **Draw audit; no repair exists** (seed-shopping is forbidden). 5-1 (a class moved to a smaller pitch) against 20260928_1 5-1 (dance props). They share the 問題5 "pick one fix" format and nothing else. |
| `no 聴解 slot repeats its own theme in the previous 2 papers — 2-2=働き方 (20260917_1, 20260928_1); 2-3=働き方 (20260917_1); 5-1=スポーツ・余暇 (20260928_1)` | **I read the rows side by side (§5.5).** The errands differ in every pair. The tag is 働き方 because 聴解 is majority work-register by format (exam-blueprint rule 3). |
| `every stamped spec's pools_sha matches pools.json (3ba4426adfc8) … 20260928_2 recorded 40bb1a12448e` | **A record, not a defect.** `pools.json` has uncommitted working-tree edits made after this spec's last reroll. The gate says this is expected after a pool repair. Replaying the seed would not reproduce the draw item for item, and nothing at stage 3 depends on that. |
| `skip no 聴解1/2/3/5 errand repeats 20260928_1's` | A skip is not a pass. I read the `shapes` column by hand (§5.5). |

Global WARNs that do not name this paper are not listed.

Lines that bear on this paper and are `ok`:

- keyed-form re-grep (`no 問題7/8/9 keyed form appears…`): my own grep finds 0
  hits for all 17 keyed forms in 問題10–14, including こそ, なお, に限り,
  とのことだ and からすると
- the 5 theme-rule lines
- closing vocabulary, claim/persona and shapes presence
- the quote spans, 5/5
- passage boxes 14/14 in the Markdown, 言語知識・読解.html, 解答.html and
  練習.html
- lexical load (novel 14.6%)
- the not-A-but-B and belief-denial instruments
- 問題9 option reuse
- `script_sha`

## 7. verify-scramble

All five 問題8 items (43–47) print `UNDECIDED` with `ARTIFACT: ok` and
`FREE UNITS: 1`, and the command exits 0. This is the tool's normal output,
since it does not decide uniqueness. The per-card last-slot proofs are QA's to
read against the listed rival orderings.

47 is the 補足追加 (なお、) item. Its frame appears nowhere in the 読解 prose,
where 「なお」 has 0 hits.

## 8. Content defects for routing (NOT repaired here)

| id | where | rule | gate message / evidence | owner |
|---|---|---|---|---|
| **F1** | 問題14 table cell `2週間まで`, which decides 問71 | §"One topic, one surface": no decisive detail shared with a 聴解 item | FAIL `問題14 shares no decisive number with any 聴解 item — ['2週間']` (聴解1-3番) | 読解 author: move the flyer's interval and re-derive 71 |
| **F2** | 11(2) and 11(4) 「私の住む町」, 13 `私は市役所で` | invented-apparatus reuse (exam-qa-review Ground rules) | FAIL `no invented place name repeats the previous 2 papers` | orchestrator (stop-list, or reword); the 11(4) half is cleared by F3 |
| **F3** | 問題11(4) | §"One topic, one surface": no 読解 topic or domain repeats the previous test | 20260928_1 11(1): same theme, closing shape, template, claim and apparatus (§5.4). Hand read, no gate line | 読解 author: re-author 11(4) on another subject and claim. If its 反論への応答 MOVE is kept, it needs a different objection domain and must not use `わけではない` + the 町内の住民 frame |
| **F3b** | 11(4) × 13 in this paper | TEMPLATE column read | the shared objection-and-concession scaffolding (§5.3). Hand read | 読解 author, in the same pass. If 11(4) is re-authored, check 13's concession sentence is not the only survivor of a three-paper crutch |
| **F4** | 問題10(2) | exam-blueprint Part II: "A near-miss counts as used" | avoid entry from 20260910_1 11(1) (卓球の帳面), plus a claim echo of 20260928_1 11(3). Hand read | 読解 author: re-subject 10(2) inside スポーツ・余暇, off the "records show who stays" family |
| QA check | 問題13 | cross-half 〈想定→実は〉 cap | borderline three-beat read (§5.3). At the cap if not counted, over if counted | QA rules on it; if counted, 13 is the one re-angled |

Any edit to 問題10–14 obliges the Stage-3 re-grep: every 問題7/8/9 keyed form,
with counts and frames, plus a re-read of the edited passage's closing move and
of the MOVE and TEMPLATE columns. The baseline is 0 hits for every form (§6).
After the fix, the `logs/topics.json` row's `surfaces`, `claim`, `persona` and
`notes` for the edited surfaces must be rewritten against the new bytes.

## 9. What I skipped, and why

- **Stage 5** (`scaffold-explanations`, `model-answer`): prohibited before QA.
- **Every F1–F4 repair:** each is authored 読解 content. I edited no prose.
- **The gate's place-name stop list:** it would loosen the gate, which needs the
  user's decision.
- **A 聴解 re-draw:** no one-back repeat and no errand-identity pair was found,
  so a fresh seed was not warranted. Re-drawing for the two-back repeats would
  be seed-shopping.
- **Listening to the MP3:** not possible here. The substitutes were the
  segmentation round-trip, the `script_sha` match and reading the full
  transcript.
- **`refs/` binaries:** not needed for any question this pass asked.
