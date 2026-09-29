# Stage 3 (build + gate) — 20260929_1

Run 2026-09-29 in one context. This context authored no exam wording. The
files it wrote by hand are: three explanation panes in the clip-bank declaration
file (§4.4), the `logs/topics.json` row, and this report.

## 1. What I read, in full, from disk

- `AGENTS.md`, `CLAUDE.md`
- `.agents/exam-app/SKILL.md` (whole file)
- `.agents/choukai-audio/SKILL.md` Part 0 (whole)
- `.agents/jlpt-test-generation/SKILL.md` §"Stage 3 — build + gate" and
  §"One topic, one surface"
- `.agents/exam-blueprint/SKILL.md` Part II through §"What still governs a
  self-authored surface" (the near-miss rule and the `logs/topics.json` format)
- `qa/stage3-report-20260928_2.md`, as a format model
- `qa/dokkai-allocation-20260929_1.md` (final-sentence column filled in by both
  authors) and `qa/blueprint-rerolls-20260929_1.md`
- `tests/20260929_1/test_spec.json`: grammar draws, and the `reading_topics`
  avoid lists, searched by keyword for the 10(2) ruling
- `logs/topics.json`: the full rows for `20260928_2` and `20260928_1`, plus a
  keyword search of every row for 回覧/ポイントカード
- the merged `言語知識・読解.md` from 問題9 to the end of 問題14, plus its
  問題9 key rows; the composer's `聴解スクリプト.txt` and `聴解.md`, in full
- `logs/choukai_draws.json`
- While resolving specific lines I also read:
  - `tools/check_consistency.py`: `check_kaisetsu_length`/`_kaisetsu_len`,
    `THEME_TOKENS` and the headline-lexical check, `check_topics_notes_quotes`,
    `check_topics_claim_field`, `CLOSING_MOVES`
  - `tools/compose_choukai.py`: preamble choice, `previous_slot_clips()`
  - `exam-qa-review/SKILL.md` on theme-record disagreement
  - `question-authoring/references/dokkai.md` §"Option length band"

## 2. Every command I ran, in order

```
make assemble 20260929_1                       # wrote 言語知識・読解.md (N2 layout)
make autofix 20260929_1                        # clean, nothing changed
make lint-draft 20260929_1                     # clean
make verify-scramble 20260929_1                # exit 0; all five UNDECIDED (§7)
gh auth status                                 # feiluvnana active
make mp3 20260929_1 SEED=54795484              # the only seed used
python3 tools/choukai_segment.py tests/20260929_1/聴解.mp3
make upload-files TARGET=tests TEST=20260929_1 # 44.3 MB uploaded, manifest 39 assets
make booklet 20260929_1
make sheet 20260929_1
make check                                     # run 1: 3 FAIL (§6)
  -- fix: trim 3 declarations in archive_items.json (§4.4) --
make choukai-bank                              # 443 records; only those 3 changed
make mp3 20260929_1 REPLAY=1 NO_AUDIO=1        # 0 of 29 slots moved; audio kept
make sheet 20260929_1                          # 練習.html re-reads 詳細解説
  -- logs/topics.json row appended --
make check                                     # run 2: 2 FAIL (one was my row, §6)
  -- fix: one paraphrase in 「」 in the row --
make check                                     # run 3 (final): 1 FAIL, stage 5 only
```

**Seed.** Exactly one: `54795484`, verbatim from the brief. No re-draw was
needed (§4.3), so no other seed was drawn.

## 3. What I wrote

- `tests/20260929_1/言語知識・読解.md`: written by `make assemble`, not touched
  afterwards (autofix changed nothing). **No 問題7–14 wording was edited.**
- The 聴解 half, from the composer: `聴解スクリプト.txt`, `聴解.md`, `聴解.mp3`,
  `聴解_チャプター.json`, and the 30 聴解 entries in each `詳細解説` pane.
- `言語知識・読解.html`, `聴解.html`, `解答.html`, `練習.html`.
- `logs/choukai_draws.json`: one row appended by the composer. The 19 earlier
  rows are byte-identical to the pre-run copy.
- `logs/upload_manifest.json`: updated by the upload.
- `.agents/choukai-audio/references/archive_items.json` and, through
  `make choukai-bank`, `logs/choukai_bank.json`: three explanation panes (§4.4).
- `logs/topics.json`: one row appended for 20260929_1 (218 lines, no other row
  touched). It has these maps:
  - `surfaces`, `themes`, `claim` (43 keys)
  - `shapes` (29)
  - `closing_moves` (13), `voices` and `persona` (14)
  - `notes`, which include the 16 問題9 options and every stage-3 ruling

  The gate reads 6 of 6 「…」 spans as found in the paper.

**Source shas at hand-off** (sha1, first 12):

| file | sha |
|---|---|
| `言語知識・読解.md` | `686f5c0778e7` |
| `聴解.md` | `95a511336329` |
| `聴解スクリプト.txt` | `53d84554fe79` (matches the gate's `script_sha`) |
| `聴解.mp3` | `8cf3dff26924` |

## 4. Build results

### 4.1 Segmentation

`ok  20260929_1  46.2 min  LUFS -15.38  問題1:5 問題2:6 問題3:5 問題4:11 問題5:2`.
It recovers **5/6/5/11/2**, as required.

### 4.2 Upload

`make upload-files TARGET=tests TEST=20260929_1` uploaded `20260929_1.mp3`
(44.3 MB) to release `audio` and exited 0. The active gh account is
`feiluvnana`. I switched no account. The gate reads
`30 exam MP3(s) are on the audio release`. The audio did not change after the
upload: the replay used `NO_AUDIO` and the MP3 bytes are identical.

### 4.3 The composed draw

- **Composer output:** 46.2 min, 34 chapters.
  - Source mix: official 20, kanzenmoshi 6, mimikara 1, shinkanzen 1 and
    soumatome 1.
  - Of the 20 official clips, 4 are archive records: `archive:2020-12:問題3-1`,
    `3-3` and `3-4`, and `archive:2017-12:問題5-1`.
  - It draws from 10 sittings.
- **Composer notes:**
  - the standing figure exclusion (4 items)
  - ffmpeg `Invalid PNG signature` noise, which is cover art and harmless
  - **No freshness bar was dropped, and no slot starved.**
- **Diff against the previous paper by id, `20260928_2`:**
  - 0 of 29 clip ids repeat in the same slot.
  - 0 slot-free clips repeat in any slot.
  - No clip appears twice within the paper.
  - One preamble repeats: `2025-07:問題5-preamble`. The 問題5 preamble is the
    instruction alone, with no 例 (「この問題には練習はありません」). The composer
    picks preambles least-used-first, with no previous-paper bar, so this is
    allowed.
- **Two papers back (`20260928_1`):** 0 repeats in the same slot, 0 in any slot.
- **Further back:** recorded, not re-drawn, because the one-paper bar allows it.
  - Three back, `20260917_1`: 問題4-1番 is the same recording,
    `2022-07:問題4-1`.
  - Four back, `20260914_1`: `kanzenmoshi:cd1-12` and `kanzenmoshi:cd1-31`
    repeat, each in a different slot.
- **Slots moved:**
  - The seeded compose is this paper's first row.
  - The replay (§4.4) moved **0 of 29 slots** and 0 of 5 preambles.
  - `聴解.mp3`, `聴解スクリプト.txt`, `聴解.md` and `聴解_チャプター.json` are
    byte-identical before and after the replay (shasum).
  - The draws file is byte-identical too.
- **Gate:** `no 問題3 option set repeats 20260928_2's (worst 0.077, ceiling
  0.30)` is `ok`, and so is the `script_sha` stamp.

### 4.4 The one repair: three over-budget clip declarations

**The first `make check` failed on 問5-1 in both explanation panes:**
- ja: 244 against the 210-char budget, and `options_analysis[3]` 51 against a
  cap of 50.
- vi: 648 against the 380-char budget, and three options over their cap of 90.

**Cause.** Those panes are composer output. The composer copies them verbatim
from the bank declaration `archive:2017-12:問題5-1` in
`.agents/choukai-audio/references/archive_items.json`, one of three 問題5-1
declarations added (uncommitted) earlier on 2026-09-29.

**Measurement.** I measured every declaration in `archive_items.json` and
`textbook_items.json` with the gate's own `_kaisetsu_len`. Exactly those three
new items were over:

| declaration | ja before | vi before |
|---|---|---|
| `archive:2017-12:問題5-1` | 244 | 648 |
| `archive:2020-12:問題5-1` | 241 | 562 |
| `archive:2018-07:問題5-1` | in band | 539 |

Only 2017-12 is in this paper. The other two would fail the next paper that
draws them.

**Repair.**
- **Where:** at the owner of the text, the declaration. I cut every pane to band.
  No `聴解.*` file was hand-edited, and the draw did not change.
- **Fixes along the way:** two small errors in the 2020-12 ja pane.
  - 「いけない」 → 「行けない」.
  - A 打ち合わせ gloss that read 打診 → 「前もって仕事の相談をすること」.
  - The 2020-12 option 1 analysis now says what the script supports:
    「店長だけが行くという話は出ていない」.
- **Unchanged:** `script_lines`, keys, `stem`/`options` and `kaisetsu_cell`.
- **Then:**
  1. `make choukai-bank`: the diff shows only those three records changed, and
     only their explanation fields.
  2. `make mp3 20260929_1 REPLAY=1 NO_AUDIO=1`.
  3. `make sheet`.

  Both terseness lines are now `ok`.

**Why not a fresh seed:** a re-draw would have hidden the defect for this paper
and left it in the bank for the next one. The brief's "fresh seed only" rule is
for a 聴解 repeat or a composer-reported draw problem. This was a data defect in
a declaration, and the draw itself was clean.

**Root-cause row (proposed, NOT applied).** Changing the gate needs the owner's
decision.

| id | defect | class | proposed repair |
|---|---|---|---|
| RC-S3-1 | `build_textbook_bank.py`/`build_archive_bank.py` accept a declaration whose `explanation`/`explanation_vi` breach `KAISETSU_BANDS`/`KAISETSU_ITEM_BUDGET`. The breach surfaces only after a paper draws the clip, as a per-test FAIL at stage 3 | PIPELINE-GAP | Measure each declared pane with `check_consistency._kaisetsu_len` at bank-build time, and refuse it (or have `make check` FAIL it on the bank) so the error lands where the text is authored |

## 5. The whole-paper table

### 5.1 読解 + 問題9 cloze

Each `reading_topics[i]` entry gives a theme and an avoid list, with no subject
string. So "drawn" below is the theme. "On draw" means the shipped subject is
about that theme and is not on, or a re-wording of, that entry's avoid list. I
searched every avoid list by keyword, and read in full the two entries 10(2)
touches.

| surface | shipped subject | theme (shipped = drawn) | on draw | closing | template | MOVE | persona | 20260928_2 same seat | 20260928_1 same seat |
|---|---|---|---|---|---|---|---|---|---|
| 問題9 | やりかけで帰る | 働き方 (RNG pick of 4) | yes | 説明 | unnamed 「AはBになる」 | 機構の説明 | 職業人 | 家が鳴る音 | 案内板で乗り換える |
| 10(1) | 開けずにすむ引っ越しの箱 | 住まい | yes | 随筆 | unnamed 〈N〉には〈X〉が詰まっている | 一人称の前後比較 | 転勤者 | 手ぬぐいの二色染め（メール） | 杖の持ち方 |
| 10(2) | 回覧板とアプリのお知らせ（町内会） | デジタル化 | **yes, ruled (§5.4 b)** | 実用文 | — | （実用文） | 町内会（通知） | 泳ぎ始めの息の練習 | 保育園の門の暗証番号 |
| 10(3) | 電話だけの取り決めの引き継ぎ（メール） | 人間関係 | yes | 実用文 | — | （実用文） | 実務者 | 二度目のお礼 | 夕食後のうたた寝 |
| 10(4) | 昔の写真と今の写真を並べる展示 | 地域活性化 | yes | 条件提示 | unnamed 〜かどうかで〜かどうかが変わる | 数えたことの報告 | 世話役 | 見積もりと待つ時間 | 紙皿をやめる食器（メール） |
| 10(5) | 広報紙の小さな欄 | メディア・情報 | yes | 意外な観察 | unnamed 〈人〉は、〈目的〉ために〜V-ている | 数えたことの報告 | 役場職員 | 教室に置いて帰れる教科書 | 給料日の書き出し |
| 11(1) | 着る日から買う服 | 消費・経済 | yes | 随筆 | unnamed 今の〈私〉は、〈時点〉から〜ことを考えている | 一人称の前後比較 | 消費者 | 雑貨店の傘の売れ方 | ブロック塀の点検 |
| 11(2) | 留守番の練習と家の決まり | 子育て・家族 | yes | 反論応答 | unnamed 〜ていくと、X は、そのまま Y になった | 反論への応答 | 親 | 商店街の一角を貸す | 窓を開ける5分 |
| 11(3) | 家族の書類を本人の前で読み上げる | 行政・手続き | yes | 主張 | unnamed 〜べきだと思います | 一人称の前後比較 | 代わりに書く家族 | 小さなかばんの旅 | 無人駅の待合室の当番 |
| 11(4) | 器の大きさと食べる量 | 食 | yes | 主張 | `A というより B` | **〈想定→実は〉** | 論者 | 119番の質問 | ます目のノート |
| 12(A) | 腰を痛めない荷物の持ち上げ方 | 睡眠・健康 | yes (WARN §6) | 条件提示 | unnamed 〜条件は二つで、〜ことと〜ことである | 機構の説明 (A+B one) | 解説者 | 端末のメモ | 職場での呼び方 |
| 12(B) | 軽いものの前で痛める腰 | 睡眠・健康 | yes | 意外な観察 | unnamed 〜では、〜分だけ、〜てしまう | ″ | 観察者 | ″ | ″ |
| 13 | 芝生の上で測る気温 | 科学・技術 | yes (WARN §6) | 説明 | 分裂文 | 反論への応答 | 解説者 | やさしい日本語のお知らせ | 寄席と落語の筋 |
| 14 | みなみ野大学 留学生のための奨学金 | 教育 | yes | — | — | （実用文） | 大学（案内） | チャイルドシートの貸し出し | 給食センター親子見学会 |

Every final sentence is the one the author wrote into the allocation table, and
every closing, template and MOVE matches its row.

**Theme rules, counted on the shipped surfaces:**

- **Rule 1:** the five headline surfaces take five different themes: 問題9
  働き方, 12 睡眠・健康, 13 科学・技術, 14 教育, and 聴解問題5 (スポーツ・余暇 +
  旅行・観光). The gate line is `ok`.
- **Rule 2:** no 読解 headline theme appears on another 読解 surface.
- **Rule 3:** 13 of 13 読解 themes are distinct.
- **Rule 4, one back (20260928_2):** no 読解 headline repeats, and the gate line
  is `ok`. **Both 聴解問題5 themes repeat 20260928_2's 聴解問題5.** That is the
  composed half, so it is a WARN (§6), and 5-1 スポーツ・余暇 is the third paper
  running.
- **Rule 4, two back (20260928_1):** no 読解 headline repeats. The budget of one
  is unspent.
- **Rule 4b (headline subjects against 20260928_2's 13 読解 and 29 聴解
  subjects):** no match. The nearest are two:
  - 問題9 × 20260928_2 12(B): both turn on the next morning, but the subjects
    are a memo-reopening rule and stopping work mid-task.
  - 聴解5-1 × 20260928_2 5-1: both are sports facilities, but the errands are
    choosing a membership type and moving a class.
- **Rule 5 (voice):** the gate reports 8 first-person surfaces, 3 in です・ます
  throughout (11(3), 12(B), 13) and kanji density 29.9%. All three lines are
  `ok`.
- **Persona cap of 2:** 解説者 ×2 (12(A), 13). Every other token appears once.
  - I tagged 問題9 職業人: it speaks of 「わたしたち」 at work, and it describes
    a work habit rather than explaining a phenomenon.
  - I tagged 12(B) 観察者: it reports what people answer when asked
    (「腰を痛めたときの様子を尋ねると」).

**問題12 cross-test column:** 腰を痛めない持ち上げ方 (here), 端末のメモ
(20260928_2), 職場での呼び方 (20260928_1). All three differ.

### 5.2 聴解: a draw audit

Keys are from `聴解.md`.

| slot | clip | shipped subject | theme | 20260928_2 same slot | 20260928_1 same slot |
|---|---|---|---|---|---|
| 1-1 | 2024-07:問題1-1 | シンポジウム、まずスタッフ用スケジュール表 | 教育 | 出張帰りの新幹線 | ガラス体験、まずエプロン |
| 1-2 | kanzenmoshi:cd1-07 | 発表の順番、まず先生の研究室 | 教育 | 値引きシールが先 | 図書館、土曜に来る |
| 1-3 | 2022-07:問題1-3 | ポスター、前の商品と比べる図 | 働き方 | 振込先を確認 | オーケストラのパンフ |
| 1-4 | kanzenmoshi:cd1-08 | クーポンの会計、2700円 | 消費・経済 | 野球大会、まず手袋 | 文化祭の応募 |
| 1-5 | 2023-07:問題1-5 | 説明会、封筒を机に置く | 働き方 | プログラム訂正の貼り紙 | ライブの手伝い |
| 2-1 | 2024-07:問題2-1 | パン屋を始めた理由（母の夢） | 働き方 | 前の会社を辞めた理由 | 眼鏡はコンタクト切れ |
| 2-2 | 2023-07:問題2-2 | パン屋、ホームページで宣伝 | 消費・経済 | 塾からレストランへ | 親子イベント、駐車場 |
| 2-3 | 2023-12:問題2-3 | シャツを編み物の材料に | 環境 | 休暇申請を簡単に | 考察と引用の区別 |
| 2-4 | kanzenmoshi:cd1-11 | 引退の理由、気持ちの限界 | スポーツ・余暇 | 在宅で選んだ会社 | フリマ、値段順 |
| 2-5 | 2021-12:問題2-5 | 箱の中身は花 | 消費・経済 | 保育実習、目の高さ | 転職の理由 |
| 2-6 | kanzenmoshi:cd1-12 | 自転車通勤、筋肉を増やす | 睡眠・健康 | 犬は寝てばかり | 事務室へ鍵を借りに |
| 3-1 | archive:2020-12:問題3-1 | みかんの会の発足 | 地域活性化 | 歯の役割 | 仲間言葉の方言 |
| 3-2 | mimikara:cd2-15 | 子どものほめ方 | 子育て・家族 | 研修、前半期待外れ | 同じミスを繰り返さない |
| 3-3 | archive:2020-12:問題3-3 | アニメの世界的人気 | メディア・情報 | お菓子屋の喜び | 子どもの注意のしかた |
| 3-4 | archive:2020-12:問題3-4 | 野菜を増やす食事の改善 | 食 | 良い睡眠の条件 | 蜂を飼う注意 |
| 3-5 | 2022-12:問題3-5 | 医師を確保する対策 | 医療・福祉 | 先に答えてしまう学生 | 道路と橋の整備 |
| 4-1…11 | 2022-07:4-1, 2023-07:4-2, 2024-12:4-3, 2025-07:4-4, 2021-12:4-5, 2024-12:4-6, shinkanzen:cd2-70, kanzenmoshi:cd1-32, 2025-07:4-9, soumatome:cd2-49, kanzenmoshi:cd1-31 | see the `shapes` map | 働き方×3, 人間関係×3, 消費・経済×3, 教育, スポーツ・余暇, 食 | 4-1 also kanji (§5.5) | — |
| 5-1 | archive:2017-12:問題5-1 | スポーツクラブ、ブルー会員 | スポーツ・余暇 | 親子サッカー教室 | ダンスの小道具 |
| 5-2 | 2022-07:問題5-2 | 自由行動の四つのコース | 旅行・観光 | 緑市の夕日 | 四種の自転車 |

The shipped 聴解 theme tally is:

| theme | count |
|---|---|
| 働き方 | 6 |
| 消費・経済 | 6 |
| 教育 | 3 |
| 人間関係 | 3 |
| スポーツ・余暇 | 3 |
| 食 | 2 |
| 環境 | 1 |
| 睡眠・健康 | 1 |
| 地域活性化 | 1 |
| 子育て・家族 | 1 |
| メディア・情報 | 1 |
| 医療・福祉 | 1 |
| 旅行・観光 | 1 |

This is a draw audit, so nothing is re-angled.

### 5.3 The reads, one axis at a time

#### MOVE column, read down on its own (読解)

The counts match the allocation exactly:

| MOVE | surfaces | count |
|---|---|---|
| 一人称の前後比較 | 10(1), 11(1), 11(3) | 3 (at cap) |
| 機構の説明 | 問題9, 12 | 2 |
| 数えたことの報告 | 10(4), 10(5) | 2 |
| 反論への応答 | 11(2), 13 | 2 |
| 〈想定→実は〉 | 11(4) | 1 |

**The skeleton read** uses the three-beat rubric: an attributed assumption, an
explicit denial, then 実は Y. It covers the ten essay surfaces, with 12 A+B
counted as one.

- **Conservative count, 読解: 1**, which is 11(4), as planned.
  - The assumption is attributed: 「多くの人はそう考えていて」.
  - The denial is 「ところが」 plus the bowl experiment.
  - Y is the bowl size.
- **Borderline, not counted:**
  - **13.** It concedes the objection as fact (「この測り方に向けられた声が言っていることは、事実です」)
    and never denies it. It then explains what the rule protects. It stays
    反論への応答.
  - **問題9.** A described practice, its cost, then an alternative. That is a
    practice, not a held belief.
  - **12(B).** 「意外に少ないものです」 is an unexpected fact, not an attributed
    belief.
- **The before-state is a PRACTICE** in 10(1), 11(1) and 11(3): opening every
  box, buying at sales, filling in forms alone.
- **Neither count is framed against a stated expectation** (10(4), 10(5)). 10(5)'s
  「表紙の特集は、その半分にも届かない」 is a fact.
- **11(2) takes its objection seriously** (「母が挙げたことはどれもほんとうに起こりうるので」).
  It does not knock it down.
- **Gate:** `0 of 13` is its marker-bearing instrument, not this read.

#### TEMPLATE column, read down separately

- **Named templates:** `A というより B` ×1 (11(4)) and 分裂文 ×1 (13). This is
  the paper's only not-A-but-B member, and the gate agrees: 1 of 13.
- **相関 is 0, as allocated**, with one note: 12(B)'s 「〜分だけ」 is proportional.
  Read as 相関, it makes ×1, which is within the cap of 2.
- **Cap-1 templates:** none used by the gate's regex. One near-shape for QA:
  11(1) 「店を出る前から、その服を着て出かける日のことを考えている」 has the
  〈動作〉前から…V-ている shape of 先回り. Its subject is a person, not a thing
  anticipating a person, so I did not count it.
- **The unnamed finals, read as a column:**
  - 問題9 「〈N〉は…〈N〉になる」 and 11(2) 「〜ていくと、X は、そのまま Y
    になった」 share an X-becomes-Y predicate. That is 2 surfaces, at the cap if
    counted as one template. Recorded for QA.
  - 10(5) 「町の人は、…ために、…を読んでいる」 and 11(1) 「今の私は、…から、…を考えている」
    are both person-は habitual V-ている finals. Different frames; recorded.
  - Every pair the allocation named to read differs: 9 vs 13, 10(1) vs 11(1),
    10(4) vs 12(A), 10(5) vs 12(B), 11(3) vs 11(4), 12(A) vs 12(B).
- **The cross-paper bar is `ok`:** no 問題10 cleft, and no 問題11 より…ほう or
  わけではない.

#### 読解 and 聴解 rows, read as ONE list

- **No decisive number or condition is shared.** The gate line
  `問題14 shares no decisive number with any 聴解 item` is `ok`.
- **Domain adjacencies (no shared decisive detail; recorded for QA):**
  - 問題11(4) (a university canteen's 定食, bowl size) / 聴解3-4番 (a company
    canteen's 定食, vegetables) / 聴解4-4番 (「この量は食べきれないよ」).
  - 問題12 (lifting, back injury) / 聴解2-6番 (「最近、腰が痛くなることが多いから」;
    the key is the health check's advice) / 問題9 blank 49's key 腰が重く. 腰
    appears on three surfaces.
  - 問題14 (a university scholarship flyer) / 聴解3-5番 (a mayor's measures
    against the doctor shortage, including a scholarship; 「奨学金」 is spoken,
    and the key is 対策).
- **聴解-internal clusters, recorded for QA:**
  - 問題2 1番 and 2番 are both set in a パン屋, with different errands (why it
    was started; how to win customers back).
  - 聴解1-5番 and 4-9番 are both a 商品説明会.
- **Keyed forms spoken in 聴解:**
  - 聴解1-2番 and 2-6番 speak 「ない限りは」, the 問題8-45 form.
  - 4-9番 speaks 「おいでいただき」 and 「失礼いたしました」, the 問題7 敬語 keys.

  聴解 is sat after 言語知識 is collected, so there is no answer leak. Recorded.

#### The cross-half 〈想定→実は〉 cap of 2

- **聴解, conservative: 1**, which is **3-2番**. 「子どものやる気を引き出すには、
  しかるのではなくほめることが大切だとよく言われます。しかし、ただほめればいい
  というものではありません」 has all three beats: the common view, the explicit
  denial and 実は Y (specific, timely praise).
  - It is the same 「〜ばいいというものではありません」 frame as 20260928_2's
    聴解3-4番, which that paper counted.
- **聴解, borderline and not counted:**
  - **2-5番, the strongest.** The coffee guess is attributed
    (「コーヒーが入っていると思われる方も多いそうです」). The reveal
    (「私もまさかこの箱に花が入っているとは思いませんでした」) comes before it,
    and the guess is never explicitly denied.
  - **3-1番.** The naming aside 「みかんを栽培する会かなと想像するかもしれませんが」
    is a side remark, not the talk's move.
  - **2-4番.** The interviewer's guess (the medal) is half-conceded
    (「それもそうなんですが」).
  - **2-6番.** A suggestion corrected with 「というか」, the 問題2 distractor
    format.
- **Total 2 (11(4) + 聴解3-2) = the cap.** No re-angle is owed.
- **If QA counts 2-5番, the total is 3.** 問題11(4) is the surface to re-angle, to
  数えたことの報告 or 反論への応答 as the allocation pre-decided. That also
  touches its `A というより B` final and 問64's hunger-based distractors, so it
  is authoring work for the 読解 author, not a stage-3 edit.

### 5.4 Author flags and cross-test reads, 読解

**(a) 問題9 vs 問題11(4): the two no longer share a claim.**
- 問題9: stop just short of a boundary, so the next morning's first step is
  chosen the day before.
- 11(4): the amount eaten follows the bowl, not hunger.
- They share no setting, no mechanism and no move (機構の説明 / 〈想定→実は〉).
- I also read 問題9 against every other surface for a "decide the day before"
  claim:
  - 11(1) (picture the day you will wear it while buying) is anticipation, not
    a day-before decision.
  - 12(B) is about bodily preparation before a light lift.
  - Neither is the same claim.

**(b) 問題10(2) is NOT a re-wording of either avoid entry. No re-author.**
- **The デジタル化 entry** is 20260903_1 聴解問題3-3番, 「スーパーの店内アナウンスで、
  紙のポイントカードからアプリへ切りかえる案内」. The shared frame is a paper
  thing moving to an app. That frame is close to the theme's definition, not a
  subject. The institution, the object and the reader's action all differ:
  - a supermarket against a 町内会;
  - a loyalty card against the neighbourhood circular;
  - an in-store switch against registering with the 班長 by 3月20日, with the
    回覧板 kept for non-registrants.
- **The 地域活性化 entry** is 20260827_2 聴解問題2-1番, 「町内会の回覧板で、次の班へ
  回すときは判を押してから回すという説明」. It shares the institution and the
  object, but the issue is how to pass the board on, not replacing it.
- **The test** (exam-blueprint Part II): would a candidate who sat both papers
  recognise the situation? For neither pair, I judge.
- **Both sources are 8–9 papers back**, outside the two-paper columns.
- **Recorded in the row's notes** so the next blueprint sees the combination.

**(c) 読解 mean option length is 30.19 JP chars** (gate `JP_CHAR` method, 80
options), against the soft band 24–30 of `dokkai.md` §"Option length band".
**Not trimmed; deferred to QA as a note.**
- Getting to 30.00 needs at least 15 chars out of at least three items.
- I tried the cheap candidates, and each is unsafe:
  - 71: dropping 「5月20日の」 from options 1/3/4 saves only 9. Digits are not
    counted.
  - 63-2 and 59-2: shortening either distractor makes that item's key uniquely
    the longest. That pushes two gate-backed key-length shares to their limits:
    6/20 → 7/20 against ≤35%, and 5/20 → 6/20 against ≤30%.
  - 66-1 and 61-1: these are keys. Trimming 66-1 breaks the parallel
    A…し、B… form its distractors share. Trimming 61-1 turns it into a verbatim
    lift of the passage.
- 30.19 is 0.6% over a soft authoring target with no gate. The per-item ratio
  lines are `ok`.

**Cross-test, 読解 (minor, recorded; no rule broken):**
- 11(1) sits in the same slot and theme (消費・経済) as 20260928_2 11(1).
  - Here, a narrator counts her own wardrobe. There, a clerk counted umbrella
    sales.
  - Both passages count, but the subjects and claims differ, and the allocation
    already barred the shop-records narrator.
- 問題9 × 20260928_2 12(B): the next-morning hinge (§5.1 rule 4b).
- 問題9 blank 49 is a body-part idiom blank **for the third paper running**:
  20260928_1 blank 51, 20260928_2 blank 49 and 腰/顔/口 here. No idiom is shared.
- Blank 50 is again a four-way paradigm of one modal: わけ in 20260928_2, はず
  here. The gate's option-reuse line is `ok`.
- **The 16 問題9 options against the previous two papers:** 0 exact repeats.
  - `ただ` does not occur in the 読解 prose, and neither does any 問題9 key form.
  - The full list is in the row's `notes`.

### 5.5 Errand identity: `shapes` across three papers, read by hand

- **Same-clip repeats beyond one back:**
  - 4-1 = 20260917_1 4-1 (three back).
  - Two kanzenmoshi clips repeat 20260914_1 (four back).

  Allowed. Re-drawing to escape them would be seed-shopping.
- **Candidate errand pairs.** Each was read side by side. **None is identity** by
  the `MUTUALLY_EXCLUSIVE_CLIPS` standard (same errand, same implicature, same
  key):
  - **4-1番 kanji memorising, in slot 4-1 for three papers running.**
    - Here: 「全部は覚え切れてない」 → sympathise.
    - 20260928_2: 「無理に決まってる」 → encourage.
    - 20260917_1: this same recording.

    The implicature and key differ from 20260928_2. It is the closest item in
    the paper, and **QA should confirm.**
  - **5-2番 × 20260928_2 5-2番:** two people pick trip sights per time slot
    (tour courses AM/PM against sunset spots day 1/day 2). The places, the
    deciders and the keys differ, and this is the 問題5-2 format.
  - **3-2番 (how to praise a child) × 20260928_1 3-3番 (how to scold a child)**,
    two back. The same domain, parenting advice, with different claims.
  - **2-1番 (why a bakery owner started) × 20260928_2 2-1番 (why a woman left
    her job).** Both are reason-for-a-career-step interviews, with different
    errands and keys.
  - 5-1番 × 20260928_2 5-1番 / 1-5番: a sports facility, with different errands
    (choose a membership against moving a class / a printed-programme fix).
- **No re-draw, and nothing added to `MUTUALLY_EXCLUSIVE_CLIPS`.**

## 6. `make check`: every line naming 20260929_1 (final run)

The final run ends `FAILED — 1 problem(s)`, with 5447 ok, 224 WARN and 240 skip.
The full output is at
`/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/c07e9e11-12f0-4983-9c7a-66f0f23c690d/scratchpad/s3_20260929_1_check3.txt`.

### FAIL

| line | disposition |
|---|---|
| `20260929_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)` | **Structural at stage 3.** The 30 聴解 entries come from `make mp3`. The 71 言語知識・読解 entries are stage 5, which is prohibited before QA passes |

**FAILs fixed during the run:**

| run | line | disposition |
|---|---|---|
| 1 | `詳細解説.json inside the terseness bands — 問5-1(244)` | **Resolved** at the bank declaration (§4.4) |
| 1 | `詳細解説.vi.json inside the terseness bands — 問5-1(648)` | **Resolved** at the bank declaration (§4.4) |
| 2 | `every logs/topics.json 「…」 span occurs in its own paper — shapes/聴解問題4-1番「全部は覚えていない」` | **Resolved.** It was my own paraphrase in 「」; I reworded it without brackets |

### WARN

| line | disposition |
|---|---|
| `20260929_1 問題12: the shipped prose uses a 「睡眠・健康」 word` | **False positive of the token table; deferred to QA §5 with this reason.** The surface is a non-medical body-care habit (lifting without hurting the back). That is inside 睡眠・健康 as the allocation reads it. `THEME_TOKENS` lists no body or injury word. The only other candidate, 医療・福祉, has no institution, treatment or patient in the prose. Retagging would relieve no rule, since neither 睡眠・健康 nor 医療・福祉 is a 20260928_2 headline, so there is no dodge motive. I did not widen the table |
| `20260929_1 問題13: the shipped prose uses a 「科学・技術」 word` | **Same class; deferred to QA.** The surface is the measurement protocol of air temperature (温度計, 観測所, 測り方). The table has 測定 but not 測る/温度計/観測. 環境, the alternative, is not what the passage argues. Retagging would relieve no rule |
| `聴解問題5 repeats a headline theme of 20260928_2 (composed paper) — ['スポーツ・余暇', '旅行・観光']` | **Draw audit; no repair exists** (seed-shopping is forbidden). 5-1 is a sports-club membership choice against a parent–child football class moved to a smaller pitch. 5-2 is tour courses against sunset spots. The shared parts are the 問題5 format and the theme tag, not the errand (§5.5) |
| `no 聴解 slot repeats its own theme in the previous 2 papers — 5-1=スポーツ・余暇 (20260928_1, 20260928_2); 2-1=働き方 (20260928_2); 5-2=旅行・観光 (20260928_2)` | **I read the rows side by side (§5.5).** The subjects are unrelated: 2-1 a bakery owner's motive against leaving a job for more responsibility. 5-1 and 5-2 as above; 20260928_1 5-1 was dance props. Composed; no repair |
| `the 問題8 form-family check compares most of the draw (1/5 = 20% family-tagged)` | **Pool-coverage WARN, not a paper defect.** Four of the five 問題8 draws carry no `grammar_form_families` tag. By hand: the five forms (だけあって, わりに, ない限りは, したがって, をもとに) share no form core with each other or with any 問題7 draw, and 問題7 has no だけに/だけある. The repair belongs in `pools.json`, which is not stage 3's to edit |
| `問題1/2 question repeats match in PUNCTUATION too — 問題1-1番, 問題2-3番` | **Transcription noise inherited from the source script PDFs**, as the line itself says. The audio is identical and no candidate can hear it |
| `every stamped spec's pools_sha matches pools.json … 20260929_1 stamped on a REROLL` | **A record, not a defect.** The spec's sha certifies the pool of its last reroll. Nothing at stage 3 depends on replaying the seed |
| `skip no 聴解1/2/3/5 errand repeats 20260928_2's` | A skip is not a pass. I read the `shapes` column by hand (§5.5) |
| `skip` errand-key ×2, 問題7 form family, 目次 identity | No keyed draws, so there is nothing to compare. The hand reads are §5.4–5.5 |

Global WARNs that do not name this paper are not listed.

Lines that bear on this paper and are `ok`:

- **Keyed forms:** `no 問題7/8/9 keyed form appears more than 1× in the 問題10-14
  prose`.
  - My own grep finds **0 hits for all 21 forms** in the 読解 half: the 17
    問題7/8 forms, plus 問題9's keys ただ, 腰が重く, はずだ and 何から始めるかの判断.
  - The only raw matches were 「それでも、」 and 「駅前でも、」, which are not
    〜てでも.
  - No 読解 prose was edited, so this is the baseline for any QA fix.
- **Theme and topics lines:** the 5 theme-rule lines, the closing vocabulary,
  claim/persona and shapes presence, and the quote spans (6/6).
- **Passage boxes:** 14/14 in the Markdown, 言語知識・読解.html, 解答.html and
  練習.html.
- **Lengths:** the length floors and ceilings, and lexical load.
- **Rhetoric instruments:** the not-A-but-B and belief-denial instruments, and
  closing-template repeat against 20260928_2.
- **Options:** 問題9 option reuse, and option-length ratios.
- **Places and decisive numbers:** invented place names (both lines), and
  問題14 × 聴解 decisive number.
- **Build:** `script_sha`, and the audio release.

## 7. verify-scramble

All five 問題8 items (43–47) print `UNDECIDED` with `ARTIFACT: ok`, and the
command exits 0.

| item | FREE UNITS |
|---|---|
| 43 | 1 |
| 44 | 1 |
| 45 | 0 |
| 46 | 1 |
| 47 | 0 |

This is the tool's normal output, since it does not decide uniqueness. The
per-card last-slot proofs are QA's to read against the listed rival orderings.
- 46 is the したがって item (18 of 24 orderings survive).
- 47 is the をもとにして item.

Neither frame appears in the 読解 prose.

## 8. Content items for QA (NOT repaired here)

| id | where | rule | evidence | owner |
|---|---|---|---|---|
| Q1 | 聴解2-5番 vs the cross-half 〈想定→実は〉 cap | §"One topic, one surface" MOVE cap | Borderline three-beat read (§5.3). At the cap if not counted; over if counted | QA rules on it. If counted, 問題11(4) is re-angled by the 読解 author |
| Q2 | 聴解4-1番 | errand identity, three papers | Kanji memorising in slot 4-1 three papers running; the implicature and key differ from 20260928_2 (§5.5) | QA confirms. Only a confirmed identity triggers a re-seed plus `MUTUALLY_EXCLUSIVE_CLIPS` |
| Q3 | 問題12, 問題13 | headline theme lexical WARN | Token-table gap; tags honest (§6) | QA §5 verdict |
| Q4 | 読解 options | soft option-length band | 30.19 against 24–30 (§5.4 c) | QA; the 読解 author if QA wants it moved |
| Q5 | 問題9 × 11(2); 10(5) × 11(1); 11(1) near-先回り | TEMPLATE column read | Unnamed-skeleton near-pairs (§5.3) | QA reads the column |
| Q6 | 腰 ×3, 定食 ×3, 奨学金 ×2, パン屋 ×2, 商品説明会 ×2 | one topic, one surface | Adjacencies with no shared decisive detail (§5.3) | QA |

Any edit to 問題10–14 obliges the Stage-3 re-grep: every 問題7/8/9 keyed form,
with counts and frames, plus a re-read of the edited passage's closing move and
of the MOVE and TEMPLATE columns. The baseline is 0 hits for every form (§6).
After the fix, the `logs/topics.json` row's `surfaces`, `claim`, `persona` and
`notes` for the edited surfaces must be rewritten against the new bytes.

## 9. What I skipped, and why

- **Stage 5** (`scaffold-explanations`, `model-answer`): prohibited before QA.
- **Stage 4 QA:** not started, as instructed.
- **A 聴解 re-draw:** no one-back repeat, no dropped bar and no errand-identity
  pair was found. The one composer-output defect was repaired at its source
  declaration, with the draw kept (§4.4).
- **Trimming 読解 options:** not cheap and safe (§5.4 c).
- **Re-authoring 10(2):** not a re-wording (§5.4 b).
- **Gate or pool changes:** these would loosen a check or edit a pool, which is
  the user's decision.
  - RC-S3-1 is proposed, not applied.
  - `THEME_TOKENS` was not widened.
  - `grammar_form_families` was not filled.
- **Listening to the MP3:** not possible here. The substitutes were the
  segmentation round-trip, the `script_sha` match and reading the full
  transcript.
- **`refs/` binaries:** the compose read the archive MP3s from disk, and nothing
  else was needed.
- **No commit**, as instructed.

## 10. Post-QA rebuild (2026-09-29, after qa-report-20260929_1 round 1)

### 10.1 F6 deferred, F7 recorded

- **F6 (the bank):** made and then reverted, on the orchestrator's decision.
  - The upstream fixes were made in the two imports:
    - 聴解1-3番's 「全面」→「前面」 in `tests/imported-n2-2022-07/聴解スクリプト.txt` and the
      `詳細解説.json` script field;
    - 聴解2-2番's option-2 解説 in `tests/imported-n2-2023-07/聴解.md` and both
      詳細解説 panes.
  - Rebuilding those imports' booklet, sheet and model answer was refused by
    the permission classifier. I did not retry it.
  - All five import files were restored with `git checkout --`, and git
    status for both imports is clean.
  - `make choukai-bank` gives a bank identical to its pre-F6 bytes.
  - `make mp3 20260929_1 REPLAY=1 NO_AUDIO=1`: 0 of 29 slots moved, the draws
    file is unchanged, and the `聴解.mp3` shasum matches.
  - **F6 is deferred to the user:** both upstream fixes plus the rebuild of the
    two imports. 「今まで最も」 stays an ear-check note at 320.11 s.
- **F7:** added to the 20260929_1 `notes` in `logs/topics.json`, together with
  the F6 deferral and a post-QA summary.

### 10.2 Commands

```
make assemble 20260929_1        # wrote 言語知識・読解.md
make autofix 20260929_1         # "clean" — but see 10.3
make lint-draft 20260929_1      # clean
make verify-scramble 20260929_1 # exit 0; 43–47 UNDECIDED, ARTIFACT ok; FREE UNITS 1/1/0/1/0
make booklet 20260929_1 && make sheet 20260929_1
make check                      # 2 FAIL: stage-5, and a script_sha mismatch (10.3)
make mp3 20260929_1 REPLAY=1 NO_AUDIO=1   # restores the composer's script
make booklet 20260929_1 && make sheet 20260929_1
make check                      # final: 1 FAIL (stage 5), 5447 ok / 224 WARN / 240 skip
```

**問題8-46 after the re-cut:**
- The four cards: したがって、 / 早めに作って / おく / のがいいでしょう.
- `FREE UNITS: 1` = the connective card. 早めに作って→おく→のがいいでしょう is
  chained: おく needs the te-form, and の nominalises the dictionary form.
- Key ★ = card 2 (おく), position 2 kept.
- 24 of 24 orderings survive the tool's filter, so uniqueness is QA's scoped
  re-review to decide.

### 10.3 A new defect found and repaired: `make autofix` rewrites the composed transcript

- **The failure:** the first post-QA `make check` failed
  `聴解.mp3 was built from today's 聴解スクリプト.txt`. The script sha was
  `ca1207bb1abe` against the chapters' `53d84554fe79`. There was also a new WARN:
  `聴解.md: 解説 quotes trace to the passage/script`, reporting 「私は紐状に…編むのに使っています」
  and 「5つの言語に翻訳されています」 as missing.
- **Cause:** `lint_draft.py --fix` (`make autofix`) applies its contraction
  rewrite to `tests/<id>/聴解スクリプト.txt`. At the original stage 3 it ran before
  `make mp3`, when there was no script yet, so it touched nothing. In the
  post-QA chain it ran after the compose, and it rewrote 7 lines of official
  transcript (2-1, 2-3, 2-4, 2-5, 3-3, 3-5) into casual forms the audio does not
  speak:
  - 「病気になってしまいました」→「病気になっちゃった」
  - 「どうしていますか」→「どうしてるか」
  - 「翻訳されています」→「翻訳されてます」
  - …
  - and it dropped the final newline.
- **Repair:** `make mp3 20260929_1 REPLAY=1 NO_AUDIO=1`.
  - The script is back to `53d84554fe79`, byte-identical to the composer's.
  - The MP3 is untouched and 0 slots moved.
  - Then booklet and sheet were rebuilt. Both the FAIL and the WARN cleared.
- **Root-cause row (proposed, NOT applied — a tool change is the owner's call):**

| id | defect | class | proposed repair |
|---|---|---|---|
| RC-S3-2 | `lint_draft.py --fix` rewrites a COMPOSED `聴解スクリプト.txt` (official transcript) whenever `make autofix` runs after `make mp3`. That is exactly the post-QA rebuild order, so every paper whose fix loop re-runs the chain gets a transcript that disagrees with its own audio. The gate catches it only indirectly, through `script_sha` | PIPELINE-GAP | Make `lint_choukai_script(fix=True)` a no-op (lint-only) when `聴解_チャプター.json` has `"source": "composed"`, as `compose_choukai.py` refuses to be hand-edited. Until then the post-QA chain should run `make autofix` before `make mp3`, or follow it with `make mp3 <id> REPLAY=1 NO_AUDIO=1`. Founding case: 20260929_1, 2026-09-29 |

### 10.4 Reads after the author fixes

- **Keyed-form re-grep over the 読解 half:** 0 hits for all 17 問題7/8 forms, for
  問題9's keys (ただ, 腰が重く, はずだ, 何から始めるかの判断), and for the new
  問題2 key 応接. No frame to report. The gate line is `ok`.
- **The 13 finals:** none changed. The diff touches no last sentence. The
  closing, template, not-A-but-B and belief-denial lines are `ok`, and §5.3's
  column reads stand unchanged.
- **Option length:** the 読解 mean is **29.81**, inside the 24–30 band (was 30.19).
  - Key-longest shares: 4/20 uniquely longest and 5/20 longest.
  - Rank spread is 35%.
- **Glosses:** 27 in-body, and the gate reads them paired, ordered and
  orphan-free.
- **Topic table, new rows:**

| surface | new content | clash? |
|---|---|---|
| 問題2-7 | 「母は朝から客のおうせつに追われていた」 (応接) | none: no 読解 or 聴解 surface is about receiving visitors |
| 問題8-46 | （料理の本で）煮物は…冷めていく間に味がしみ込む → したがって早めに作っておくのがいい | 食 domain only, shared with 問題11(4) (bowl size) and 聴解3-4番/4-4番 (定食); no decisive detail crosses |
| 問題11(1) | adds （注2）暮れ and small wording trims | subject and claim unchanged |
| 問題13 | loses （注5）入り込む | subject and claim unchanged |

  The `logs/topics.json` surfaces and claims stay valid. 6 of 6 quote spans are
  found.

### 10.5 `make check` lines naming 20260929_1 (final)

- **FAIL:** only `詳細解説.json explains every keyed item (30 entries for 101
  keys)`, which is stage 5. **No FAIL names any other test.**
- **WARN:** the same set as §6, with the same dispositions (問題8 form-family
  coverage; the 問題12/13 theme-token gaps; the composed 聴解問題5 theme repeat;
  the 聴解 slot-theme repeats; the question punctuation noise).
- **pools_sha:** the value is new. This spec recorded `98822aa52bb9`, and
  `pools.json` is now `657affe4425a` after the F2 deletions of 基盤 and 金魚.
  That is a record, as the line says ("expected after any pool repair").
- **No new WARN names this test.**

### 10.6 Shas at hand-off (sha1, first 12)

| file | sha |
|---|---|
| `言語知識・読解.md` | `9224fc9b938d` |
| `聴解.md` | `95a511336329` (unchanged) |
| `聴解スクリプト.txt` | `53d84554fe79` (unchanged; equals the chapters' `script_sha`) |
| `聴解.mp3` | `8cf3dff26924` (unchanged; the uploaded bytes) |

### RC-S3-3 (proposed, not applied — orchestrator, 2026-09-29)

`make lint-draft` FAILs `CHOUKAI-縮約形` (21.6 per 10k chars vs floor 22.4) on the
composed `聴解スクリプト.txt`, a verbatim transcript of real recordings. The floor is a
TTS-era authoring target, and its only offered repair (`--fix`) is the RC-S3-2 rewrite
that corrupts the transcript. The post-QA chain's earlier "clean" lint was clean only
because autofix had just injected contractions. Proposal: `lint_draft.py` skips (or
reports-only) the CHOUKAI checks on a composed paper. `make check` does not gate this,
so the paper ships with the lint line recorded here as a false positive.
