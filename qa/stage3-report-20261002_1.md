# Stage 3 (build + gate) — 20261002_1

Run 2026-10-02 in one context, which authored none of the exam items. The
files it wrote by hand are:
- the three 読解 apparatus edits in §4.4, made in both the fragment and the
  merged paper;
- the `logs/topics.json` row;
- this report.

## 1. What I read, in full, from disk

- `AGENTS.md`, `CLAUDE.md`
- `.agents/exam-app/SKILL.md`, the whole file
- `.agents/choukai-audio/SKILL.md` Part 0, the whole part
- `.agents/jlpt-test-generation/SKILL.md`: §"Stage 3 — build + gate",
  §"One topic, one surface" and §"Invariants"
- `.agents/exam-blueprint/SKILL.md`: §"Topic themes" through §"The four theme
  rules" (rule 5 and 4b/4c included), and §"What still governs a self-authored
  surface" (the `topics.json` row format, `claim`/`persona`, the 「」 convention)
- `qa/stage3-report-20260929_1.md`, as the format model
- `qa/dokkai-allocation-20261002_1.md`
- `tests/20261002_1/test_spec.json`
- the merged `言語知識・読解.md`, 問題7 to the end of 問題14, with its 文法 key
  rows
- the composer's `聴解スクリプト.txt` and `聴解.md`, in full
- `logs/choukai_draws.json`: the last three rows
- `logs/topics.json`: the full rows for `20260929_1` and `20260928_2`
- While resolving specific lines, in `tools/check_consistency.py`:
  - `check_choukai_question_repeat` and `CHOUKAI_QUESTION_REPEAT_GRANDFATHERED`
  - the keyed-form exposure/frame check
  - `check_invented_proper_nouns`
- Also the 7/2022 archive `script.md` lines for 問題2-4番

## 2. Every command, in order, with exit status

```
gh auth status                                   # feiluvnana active (td-nguyen-38 inactive)
make assemble 20261002_1                         # 0 — wrote 言語知識・読解.md (N2 layout)
make autofix 20261002_1                          # 0 — clean; diff vs pre-autofix copy: none
make lint-draft 20261002_1                       # 0 — clean
make verify-scramble 20261002_1                  # 0 — 43–47 all UNDECIDED, ARTIFACT ok (§7)
make mp3 20261002_1 SEED=85360207                # 0 — 46.0 min, 34 chapters
python3 tools/choukai_segment.py tests/20261002_1/聴解.mp3   # ok 5/6/5/11/2
make upload-files TARGET=tests TEST=20261002_1   # 0 — 44.2 MB uploaded
make booklet 20261002_1                          # 0
make sheet 20261002_1                            # 0 (71 items without 詳細解説 yet: stage 5)
make check                                       # 2 — run 1: 3 FAIL (§6)
  -- fix A: fresh-seed re-draw (§4.3) --
make mp3 20261002_1 SEED=51233600                # 0 — 46.3 min, 34 chapters
python3 tools/choukai_segment.py tests/20261002_1/聴解.mp3   # ok 5/6/5/11/2, LUFS -15.74
  -- fix B: two 問題11 glosses; fix C: 問題14 letterhead (§4.4), both files --
python3 tools/assemble_paper.py tests/20261002_1 --check   # 0
python3 tools/assemble_paper.py tests/20261002_1  # re-assembled output byte-identical to the edited merge
make upload-files TARGET=tests TEST=20261002_1   # 0 — 44.5 MB re-uploaded, manifest 40 assets
make booklet 20261002_1 && make sheet 20261002_1 # 0
make check                                       # 2 — run 2: 1 FAIL (stage 5 only)
  -- logs/topics.json row appended --
make check                                       # 2 — run 3 (final): 1 FAIL (stage 5 only)
```

`make autofix` ran **before** `make mp3`, as required, and never ran again
after either compose.

**Seeds.** I used two seeds.
- `85360207` came from the brief, verbatim.
- `51233600` is a fresh `secrets.randbelow(10**8)` re-draw. §4.3 gives the
  reason.

## 3. What I wrote

- `tests/20261002_1/言語知識・読解.md`: written by `make assemble`, then three
  apparatus edits (§4.4). I made the same edits in
  `_sections/問10-14_読解.md`, and re-assembling reproduces the merged file
  byte for byte. **No item stem, option, key or 解説 was edited.**
- The 聴解 half comes from the composer, at seed `51233600`: `聴解スクリプト.txt`,
  `聴解.md`, `聴解.mp3`, `聴解_チャプター.json`, and the 30 聴解 entries in each
  `詳細解説` pane.
- `言語知識・読解.html`, `聴解.html`, `解答.html`, `練習.html`.
- `logs/choukai_draws.json`: one row for 20261002_1. The second compose
  replaced the first row in place, and the 20 earlier rows are identical to the
  pre-run copy.
- `logs/upload_manifest.json`: updated by the two uploads.
- `logs/topics.json`: one row appended, 218 lines, with no other row touched.
  It holds:
  - `surfaces`, `themes` and `claim` (43 keys each)
  - `shapes` (29)
  - `closing_moves` (13)
  - `voices` and `persona` (14 each)
  - `notes`

  It contains no 「」 span; non-paper strings are in backticks.

**Source shas at hand-off** (sha1, first 12):

| file | sha |
|---|---|
| `言語知識・読解.md` | `10590f1af4e1` |
| `聴解.md` | `840087f32dc2` |
| `聴解スクリプト.txt` | `ab8c7404e029` (matches the chapters' `script_sha`; gate `ok`) |
| `聴解.mp3` | `80011ffb494d` (the uploaded bytes) |

## 4. Build results

### 4.1 Segmentation

`ok  20261002_1  46.3 min  LUFS -15.74  問題1:5 問題2:6 問題3:5 問題4:11 問題5:2`
recovers **5/6/5/11/2**. The first compose also recovered 5/6/5/11/2, at
LUFS -15.95.

### 4.2 Upload

- The active `gh` account is `feiluvnana`. I switched no account.
- Both uploads exited 0: the seed-1 audio at 44.2 MB, then the seed-2 audio at
  44.5 MB.
- The gate reads `31 exam MP3(s) are on the audio release` and raises no
  manifest-mismatch FAIL. The audio did not change after the second upload.

### 4.3 The composed draw, and the re-draw

**Seed 1 (`85360207`)** drew `2022-07:問題2-4` into 問題2-4番. `make check`
then FAILed:
`every 問題1/2 item re-reads its own question — 問題2-4番: 頭「…何だと言っていますか。」/ 尾「…何と言っていますか。」`.

- This is a known upstream transcription defect.
  `tests/imported-n2-2022-07/聴解スクリプト.txt` took the tail from the script
  PDF's 解説欄 line 「問い …？（正解:２）」, as `refs/JLPT_N2_NEW/13. N2 7-2022/script.md`
  l.164 shows.
- `CHOUKAI_QUESTION_REPEAT_GRANDFATHERED` names it for the import and for
  20260819_1, and says the repair was deferred because "the 7/2022 audio has
  not been listened to".
- The gate's repair is upstream: fix the import, run `make choukai-bank`, then
  re-compose 20260810_1 and 20260819_1. That needs the audio heard to know which
  wording is spoken, and I cannot listen here. It also re-composes two other
  papers. **So I took the brief's route for a 聴解 problem: a fresh-seed
  re-draw, with no hand edit.**

**Seed 2 (`51233600`):**
- **Composer output:** 46.3 min, 34 chapters.
  - Source mix: official 20, soumatome 5, kanzenmoshi 2, mimikara 1 and
    shinkanzen 1.
  - Of the official clips, `archive:2018-07:問題5-1` is the one archive record.
  - It draws from 10 sittings.
- **Composer notes:** only the standing figure exclusion (4 items) and ffmpeg's
  `Invalid PNG signature` cover-art noise. **No freshness bar was dropped and no
  slot starved.**
- **Against seed 1:** 18 of 29 slots moved.
- **Against 20260929_1 (previous paper):**
  - 0 of 29 clip ids repeat in the same slot.
  - 0 slot-free clips repeat in any slot.
  - No clip appears twice within the paper.
  - All 5 preambles differ.
- **Against 20260928_2 (two back):** one repeat, `soumatome:cd1-30` in the same
  slot, 問題2-1番 (§5.5). The one-paper bar allows it.
- **Neither problem clip was drawn.** `2022-07:問題2-4` is gone, and
  `2021-07:問題2-5` (the other grandfathered upstream defect, which would also
  FAIL here) was not drawn.
- **Gate lines:**
  - `every 問題1/2 item re-reads its own question (11 items compared)`: `ok`
  - `no 問題3 option set repeats 20260929_1's (worst 0.071, ceiling 0.30)`: `ok`
  - `script_sha`: `ok`

### 4.4 The 読解 repairs (apparatus only)

| # | gate line | edit | why this edit |
|---|---|---|---|
| B | FAIL `問31「ところ」 in the same 文末 frame as the stem: 「…草の、ほかの部分とつながっているところ…」` | 問題11(1) （注1） `根元：葉や草の、ほかの部分とつながっているところ` → 「根元：葉や草が、茎や地面とつながっている部分」. 問題11(4) （注5） `段差：道などで、高さが急に変わっているところ` → 「段差：道などで、高さが急に変わっている場所」. The second was not printed, because the gate prints one hit per item, but it is the same frame, so I fixed both | The gloss stays, as the gate asks. Only its last noun changed, and the meaning is unchanged |
| C | WARN `「みずき市」 ~ 「みずほ市」 (20260928_2)` | 問題14 letterhead `みずき市` → かわせ市 (3 occurrences: instruction line, title, contact line) | かわせ市 has no name on disk within edit distance 1, and it is not a real municipality |

**After the edits:**
- **Option and key text:** no option, key, item number or decisive number
  changed.
- **Length:** the 読解 length lines are `ok`.
- **Glosses:** the gloss lines are `ok`; there are 26 glosses.

**Keyed-form re-grep of the whole 読解 half (問題10–14), after the edits** —
every 問題7/8/9 keyed form, with counts and frames:

| form (item) | count | frame / note |
|---|---|---|
| ところだった (31) | 0 | — |
| ところ (core of 31) | 2 | 「ところが、」 in 10(3), a sentence-initial connective; 「一人のところに」 in 13, 連用. Neither is 文末 |
| っぱなし (32), ざるを得ない (33), といっても／と言っても (34), 申し上げ (35), ことなく (36), ものがある (37), と言っても過言ではない (38), といい (39), はさておき (40), にわたって／にわたり (41), にしたがって／に従って (42) | 0 each | — |
| のみならず (43), に先立って／先立 (44), にしては (45), ことから (46), どころか (47) | 0 each | — |
| ものだ (48) | 1 | 10(2) 「…と聞くものだった。」. This is 文末, but it is the formal-noun predicate ("29 of the questions were ones that asked…"), not the 回想 ものだ that 48 keys. The gate's 文末モーダル line is silent on it. **Recorded for QA (Q6)** |
| ところが (49) | 1 | 10(3), sentence-initial. 49 is [論理接続], which the frame rule exempts, and the count is within the max of 1. Recorded |
| 目を通す (50), 切り抜いた理由 (51) | 0 | — |

The gate line `no 問題7/8/9 keyed form appears more than 1× … or even once in
the same frame` is `ok`.

**Closing moves after the edits:** 11(1) and 11(4) still close on their
allocated finals. 11(1) closes on 「同じものを何度も測るときに大切なのは…ことです。」;
11(4) closes on 「下りでは、筋肉が伸ばされながら…傷がついていく。」. The
glosses sit below the passage, so no final changed.

## 5. The whole-paper table

### 5.1 読解 + 問題9 cloze

"Drawn" is the spec `reading_topics[i]` theme, plus its avoid list. 問題9's
theme was picked by RNG at blueprint time; see the allocation. "On draw" means
the shipped subject is about that theme and is not on its avoid list, or a
re-wording of it.

| surface | shipped subject | theme (shipped = drawn) | on draw | closing | template | MOVE | persona | 20260929_1 same seat | 20260928_2 same seat |
|---|---|---|---|---|---|---|---|---|---|
| 問題9 | 切り抜き帳と一行の理由 | メディア・情報 | yes | 随筆 | unnamed 〈〜ても、〜があれば、〜ことができる〉 | 一人称の前後比較 | 趣味の実践者 | やりかけで帰る | 家が鳴る音 |
| 10(1) | 児童館の平日午前の親子の時間（お知らせ） | 子育て・家族 | yes | 実用文 | — | （実用文） | 児童館（通知） | 開けずにすむ引っ越しの箱 | 手ぬぐいの二色染め（メール） |
| 10(2) | 病院の案内図と予約票の番号のずれ | 医療・福祉 | yes | 意外な観察 | unnamed 〜ない以上、…ことになる | 数えたことの報告 | ボランティア | 回覧板とアプリ | 泳ぎ始めの息の練習 |
| 10(3) | 収納の置き場所 | 住まい | yes | 主張 | `A だけではない。B こそが〜` | **〈想定→実は〉** | 借り手 | 電話だけの取り決めの引き継ぎ | 二度目のお礼 |
| 10(4) | インク容器の引き取りの問い合わせ（メール） | 環境 | yes | 実用文 | — | （実用文） | 実務者 | 昔の写真と今の写真の展示 | 見積もりと待つ時間 |
| 10(5) | 写真の自動保存が動く条件 | デジタル化 | yes | 条件提示 | unnamed 〈条件〉が来るまで、〈物〉は…待っている | 機構の説明 | 店員 | 広報紙の小さな欄 | 教室に置いて帰れる教科書 |
| 11(1) | 同じ葉を三回測る理由 | 科学・技術 | yes, but **see Q1** | 説明 | 分裂文 (大切なのは…ことです) | 反論への応答 | 研究者 | 着る日から買う服 | 雑貨店の傘の売れ方 |
| 11(2) | かるたの読み手と取り方の変化 | 文化・伝統 | yes | 随筆 | unnamed 〈前のN〉は、今では〜として…残っている | 一人称の前後比較 | 趣味の実践者 | 留守番の練習と家の決まり | 商店街の一角を貸す |
| 11(3) | 家で取るだしと粉のだし | 食 | yes | 反論応答 | unnamed それで今は、…に回している | 反論への応答 | 家庭の料理人 | 家族の書類を読み上げる | 小さなかばんの旅 |
| 11(4) | 山の下りで脚が痛む仕組み | スポーツ・余暇 | yes | 意外な観察 | unnamed 〜ので、…ままでも、…V-ていく | 機構の説明 | 解説者 | 器の大きさと食べる量 | 119番の質問 |
| 12(A) | 日用品のまとめ買い | 消費・経済 | yes | 主張 | unnamed 〜のが、…賢いやり方である | 反論への応答 (A+B one) | 論者 | 腰を痛めない持ち上げ方 | 端末のメモ |
| 12(B) | 買い置きが見えると増える使う量 | 消費・経済 | yes, but **see Q2** | 説明 | unnamed 〜と、…は…に戻っていく | ″ | 助言者 | 軽いものの前で痛める腰 | 翌朝に開き直す決まり |
| 13 | 仲間内の幹事役が一人に決まる仕組み | 人間関係 | yes | 条件提示 | unnamed 〜ている〈集団〉では、Xは…として受け取られる | 機構の説明 | 解説者 | 芝生の上で測る気温 | やさしい日本語のお知らせ |
| 14 | かわせ市 家庭の消火器の詰め替え・引き取り | 防災 | yes | — | — | （実用文） | 市（案内） | 留学生の奨学金 | チャイルドシートの貸し出し |

Every final sentence is the one its author wrote into the allocation table,
and every closing, template and MOVE matches its row.

**問題9 vs 11(2), the pair the brief named.**
- **The finals:**
  - 問題9: 「何年かたって開いても、その一行があれば、はさみを手にした日の自分に会うことができる。」,
    skeleton **〈〜ても、〜があれば、〜ことができる〉**: a concessive plus a
    conditional, then a possibility predicate.
  - 11(2): 「子どものころ初めの音で覚えた札は、今では一つの歌として、読む人の声と一緒に耳に残っている。」,
    skeleton **〈前の実践のN は、今では〜として…残っている〉**: a then/now
    topic plus a state V-ている.
  - They share no connective, no predicate class and no frame. **Confirmed
    different.**
- **The claims differ:** writing why you kept something keeps its meaning,
  against reading aloud changing how you listen.
- **The befores are both PRACTICES, not beliefs:** pasting clippings with
  date and paper only, and memorising first sounds.

**Theme rules, on the shipped surfaces:**
- **Rule 1:** the headline themes are distinct: 問題9 メディア・情報, 12
  消費・経済, 13 人間関係, 14 防災, and 聴解問題5 旅行・観光 + 睡眠・健康.
  Gate `ok`.
- **Rule 2:** no 読解 headline theme appears on another 読解 surface.
- **Rule 3:** 13 of 13 読解 themes are distinct. Gate `ok`.
- **Rule 4, one back:** no 読解 headline repeats 20260929_1 (gate `ok`).
  Both 聴解問題5 themes repeat 20260929_1 headlines:
  - 5-1 旅行・観光 against its 5-2;
  - 5-2 睡眠・健康 against its 問題12.

  These are composed, so the line is a WARN (§6).
- **Rule 4, two back:** no 読解 headline repeats 20260928_2. The gate notes
  that 旅行・観光 sits only on the composed 5-1 and is not counted.
- **Rule 4b (headline subjects against 20260929_1's 13 読解 and 29 聴解):** no
  match. The nearest is 問題9 切り抜き帳 against 20260929_1 10(5) 広報紙の小さな欄.
  Both are print media, but one is a personal scrapbook of newspaper articles
  and the other is a town newsletter and its readers' postcards: a different
  institution and a different issue. The allocation barred exactly the
  newsletter/postcard subject, and the cloze stayed off it.
- **Rule 5 (voice):** gate reads 5 first-person essay surfaces (≥4), 3 in
  です・ます (11(1), 12(B), 13; ≥3), and kanji density 29.8%. All `ok`.
- **Persona cap of 2:**
  - 趣味の実践者 ×2 (問題9, 11(2)) and 解説者 ×2 (11(4), 13). Both are at the cap.
  - Every other token appears once.
  - 12(B) is tagged 助言者, because its move is a recommendation
    (「…しまっておくことをお勧めします」), not an explanation.

**問題12 cross-test column:** 日用品のまとめ買い (here), 腰を痛めない持ち上げ方
(20260929_1) and 端末のメモ (20260928_2). All three differ in topic.

### 5.2 聴解: a draw audit (seed 51233600)

| slot | clip | shipped subject | theme | key | 20260929_1 same slot | 20260928_2 same slot |
|---|---|---|---|---|---|---|
| 1-1 | kanzenmoshi:cd1-04 | 就職セミナー前に出すもの | 教育 | 3 メール | シンポジウム、スケジュール表 | 新幹線のチケット変更 |
| 1-2 | kanzenmoshi:cd1-06 | 忘れた傘、友人が預かる | 人間関係 | 1 電車に乗る | 発表の順番、研究室 | 値引きシール |
| 1-3 | 2022-12:問題1-3 | クッキーの箱のデザイン | 働き方 | 2 | 比べる図を入れる | 振込先の確認 |
| 1-4 | 2022-12:問題1-4 | 金魚のケースが汚れる | スポーツ・余暇 | 4 ケースを移動 | クーポンの会計 | テント片付け、手袋 |
| 1-5 | 2023-12:問題1-5 | 弱った植物、まず置き場所 | 住まい | 1 置く場所を変える | 封筒を机に置く | 訂正の貼り紙 |
| 2-1 | soumatome:cd1-30 | 前の会社を辞めた理由 | 働き方 | 2 | パン屋を始めた理由 | **same recording** |
| 2-2 | 2024-07:問題2-2 | 引っ越しを安く、家具のもらい手 | 住まい | 1 | パン屋、ホームページ | 塾からレストランへ |
| 2-3 | 2021-07:問題2-3 | 地域の日本語教室のよさ | 教育 | 3 | シャツを編み物に | 休暇申請を簡単に |
| 2-4 | 2024-12:問題2-4 | 俳優の家具作りの魅力 | スポーツ・余暇 | 2 | 引退の理由 | 在宅で選んだ会社 |
| 2-5 | 2024-12:問題2-5 | 5000m優勝の勝因 | スポーツ・余暇 | 1 | 箱の中身は花 | 目の高さを合わせる |
| 2-6 | soumatome:cd1-46 | 肩の具合 | 医療・福祉 | 1 | 自転車通勤、腰 | 犬は寝てばかり |
| 3-1 | 2024-12:問題3-1 | 採用面接で重視すること | 働き方 | 1 | みかんの会 | 歯の役割 |
| 3-2 | soumatome:cd1-33 | 車はかっこいいもの | 交通 | 2 | 子どものほめ方 | 研修の感想 |
| 3-3 | 2023-07:問題3-3 | 宇宙での体の変化 | 科学・技術 | 4 | アニメの人気 | お菓子屋の喜び |
| 3-4 | 2021-07:問題3-4 | 植物の種の運ばれ方 | 環境 | 1 | 野菜を増やす食事 | 良い睡眠の条件 |
| 3-5 | 2025-12:問題3-5 | 農業体験会の目的 | 地域活性化 | 2 | 医師確保の対策 | 先に答える学生 |
| 4-1…11 | soumatome:cd2-46, shinkanzen:cd2-75, 2022-07:4-3, soumatome:cd2-48, 2023-12:4-5, 2023-12:4-6, 2024-12:4-7, 2021-12:4-8, 2021-07:4-9, 2025-12:4-10, mimikara:cd2-19 | see `shapes` | 人間関係×4, 働き方×4, スポーツ・余暇×2, 食 | 3,1,2,3,3,1,2,1,1,1,3 | — | — |
| 5-1 | archive:2018-07:問題5-1 | 会議の宿、温泉で最安 | 旅行・観光 | 2 緑ホテル | スポーツクラブ会員 | 親子サッカー教室 |
| 5-2 | 2024-12:問題5-2 | 健康イベントの会場 | 睡眠・健康 | 1 / 4 | 自由行動のコース | 夕日の名所 |

The shipped 聴解 theme tally is:

| theme | count |
|---|---|
| 働き方 | 7 |
| 人間関係 | 5 |
| スポーツ・余暇 | 5 |
| 教育 | 2 |
| 住まい | 2 |
| 医療・福祉, 交通, 科学・技術, 環境, 地域活性化, 食, 旅行・観光, 睡眠・健康 | 1 each |

This is a draw audit, so nothing is re-angled.

### 5.3 The reads, one axis at a time

#### MOVE column, read down on its own (読解, 10 essay surfaces, 12 A+B as one)

| MOVE | surfaces | count |
|---|---|---|
| 機構の説明 | 10(5), 11(4), 13 | 3 (cap) |
| 反論への応答 | 11(1), 11(3), 12 | 3 (cap) |
| 一人称の前後比較 | 問題9, 11(2) | 2 |
| 数えたことの報告 | 10(2) | 1 |
| 〈想定→実は〉 | 10(3) | 1 |

This matches the allocation exactly.

**The skeleton read** uses the three-beat rubric: an attributed assumption, an
explicit denial, then 実は Y.

- **Conservative count, 読解: 1**, which is 10(3).
  - The assumption is attributed: 「不動産屋にも友人にも、『収納は多いほどいい』と言われた」.
  - The denial is 「ところが、半年もすると…」.
  - Y is the placement.
- **Borderline, not counted:**
  - **11(4).** 「なぜ、息の楽な下りのほうが、脚に疲れを残すのだろうか」 poses a
    puzzle from a reported fact. No belief is attributed or denied.
  - **11(3).** The husband's view is tested and half-conceded
    (「夫の言うとおり、味噌汁なら」). That is 反論への応答.
  - **12(B).** 「たしかに安くなります。けれども…」 concedes A's fact and adds a
    second fact. Nothing is denied as a held belief.
  - **11(1).** The objection is conceded (「時間の使い方としては正しいと思います」).
  - **問題9 and 11(2):** the befores are practices.

#### TEMPLATE column, read down separately

- **Named templates:** `A だけではない…こそ` ×1 (10(3)) and 分裂文 ×1 (11(1)).
  Gate: not-A-but-B 1 of 13, and no template over its cap.
- **相関 is 0.** 12(B)'s 「使う量は、目に入る残りの多さによって変わる」 is
  proportional, but it is in the body, not the final.
- **Cap-1 templates (後知れ, 不在の残り, 先回り): none.** 10(5)'s 「写真は…順番を待っている」
  has a thing waiting on a condition, not anticipating a person's action, so it
  is not 先回り. Recorded.
- **Every pair the allocation named to read differs:** 9 vs 11(2) (above), 10(2)
  vs 11(4), 10(5) vs 13, 11(1) vs 12(B), and 12(A) vs 12(B).
- **Near-pairs the gate cannot see (recorded for QA, Q5):**
  - **11(2) and 11(3)** are both in 問題11, and both end on a 今(では) + V-ている
    after-state: 「今では…残っている」 and 「それで今は…回している」. The topic
    framing differs (a 〈N〉は topic against a それで connective).
  - **11(4) and 12(B)** both end on a V-ていく gradual-change predicate: 「傷がついていく」
    and 「戻っていきます」. They are in different 大問.
- **Cross-paper bar `ok`:** no 問題11 `A というより B` and no 問題13 分裂文.

#### 読解 and 聴解 rows, read as ONE list

- **No decisive number or condition is shared.** Gate:
  `問題14 shares no decisive number with any 聴解 item` is `ok`. The flyer's
  500円, 3本 and 10年 appear in no 聴解 item.
- **Domain adjacencies (no shared decisive detail; recorded for QA, Q4):**
  - 10(3) 部屋の収納 / 聴解2-2 引っ越しで大きい家具を減らす. Both are 住まい;
    the issues differ.
  - 11(1) 葉の成長を測る / 聴解1-5 弱った植物 / 3-4 種の運ばれ方. All are plants.
  - 11(4) 下りで脚が痛む / 聴解2-6 肩の具合 / 2-5 陸上の勝因.
  - 10(2) 病院の案内図 / 聴解2-6 病院.
  - 13 幹事 / 聴解4-7 セミナーの弁当予約.
- **Keyed forms spoken in 聴解:**
  - 4-5番 「つけっぱなし」, the 問32 form.
  - 4-3番 「平日の昼にしては」, the 問題8-45 form.
  - 4-9番 「揃ったところで」.
  - 4-11番 「わけじゃない」.

  聴解 is sat after 言語知識 is collected, so there is no answer leak. Recorded.

#### The cross-half 〈想定→実は〉 cap of 2

- **聴解, conservative: 0.**
- **聴解, borderline, the strongest: 2-3番.** The friend's guess
  (「先生、教え方うまいの」) is denied (「先生に日本語の文法とか言葉とかを習うんじゃないんだ」),
  then Y follows (event planning). The guess is a question, though, not an
  attributed belief.
- **聴解, not counted:**
  - **3-2番:** 「確かにそれもそうなんですが、昔は」 is a concession.
  - **2-5番:** 「…自信がなくて」 is a narrated tactic.
- **Total:** 1 conservative (10(3)), and 2 if 2-3番 is counted. Either way
  this is within the cap, so **no re-angle is owed.** If QA counts 2-3番, the
  paper sits at the cap.

### 5.4 Cross-test reads, 読解 (rows read across the three columns)

No same-seat row repeats a subject (§5.1). Three cross-seat echoes are findings
for QA. None is a subject repeat a string check can see, and none is stage 3's
to re-author:

- **Q1, the strongest: 問題11(1) × 20260929_1 問題13.** Both are 科学・技術
  反論への応答 passages that justify a measurement protocol against a lay
  objection:
  - 20260929_1 問題13: why air temperature is measured on grass, in shade, at
    1.5 m;
  - here: why the same leaf is measured three times.

  The allocation barred thermometer placement and official temperatures, and
  the author complied literally. What survives is the domain (measurement
  method) and the MOVE (an objection conceded, then the method explained).
  This is one paper back, in a different seat.
- **Q2: 問題12(B) × 20260929_1 問題11(4), a claim-level echo.**
  - There: the amount eaten follows the bowl, not hunger, so use a smaller bowl.
  - Here: the amount used follows the visible stock, not need, so hide the
    stock.

  The mechanism is the same: consumption is set by an environmental cue, so
  change the cue. The subjects differ (food portion against household
  consumables) and so do the themes (食 against 消費・経済). This is the
  "two surfaces asserting the same move on different subjects" case the
  `claim` column exists for, read across papers. One paper back.
- **Q3: 問題11(4) × 20260929_1 問題12(A)(B).** Both explain musculoskeletal
  strain: the lower back when lifting there, the thigh muscles downhill here.
  The themes (睡眠・健康 against スポーツ・余暇), subject and claim differ;
  the domain repeats. Minor.
- **Two back (20260928_2):** no domain repeat worth filing. 11(4)'s 息が上がる
  appears near 20260928_2 10(2) (breathing in swimming), as a word only.
- **10(3) 収納の置き場所 × 20260929_1 10(1) 開けずにすむ引っ越しの箱:** both are
  household possessions, but the issues (storage placement against unpacked
  boxes) and claims differ. The allocation's explicit bar (moving boxes) was
  respected. Minor.

**問題9's 16 options against the previous two papers:** the gate line
`問題9 blanks reuse no option set` is `ok`. 49 is a [論理接続] blank again
(20260929_1's 48 was a connective blank too); its options share no member with
20260929_1's.

### 5.5 Errand identity: `shapes` across three papers, by hand

**Same-clip repeats beyond one back:**
- **2-1番 `soumatome:cd1-30` = 20260928_2 2-1番:** the same recording in the same
  slot, two back. Allowed by the one-paper bar. Re-drawing to escape it would be
  seed-shopping.
- **Seed 1 had two different two-back repeats**, `shinkanzen:cd2-66` and
  `2025-07:問題4-7`. Both are gone.
- **2-1番 is the third reason-for-a-career-step interview in 2-1 running:**
  - 20260929_1: why the bakery was started;
  - 20260928_2: this same recording.

  Recorded as Q7.

**Candidate pairs.** I read each side by side, against the
`MUTUALLY_EXCLUSIVE_CLIPS` standard (same errand, same implicature, same key):

- **Within this paper, 1-4番 × 1-5番, the closest.** Both are a 相談 about a
  living thing kept at home that is not doing well (a fish tank that dirties
  fast, a plant that weakens). Each walks past feed/water/cut/clean options,
  and both key on **relocation**: ケースを移動する and 置く場所を変える. The
  objects, the advisers and the rejected options differ, so I judge this not
  identity, but it is the same key shape in adjacent slots. **QA should
  confirm (Q8).** A confirmed pair means a fresh-SEED re-draw plus a
  `MUTUALLY_EXCLUSIVE_CLIPS` entry, never a hand re-slot.
- **5-1番 × 20260929_1 5-1番:** both choose one of four options under
  conditions. One is a hotel by onsen and price; the other a sports-club
  membership by days and budget. This is the 問題5-1 format; the errands
  differ.
- **5-2番 × 20260929_1 5-2番:** two people each pick a first stop (health-event
  rooms against tour courses). The format again; the errands differ.
- **2-6番 (shoulder after treatment) × 20260929_1 2-6番 (bike commute for back
  pain) × 20260928_2 2-6番 (sick dog):** not identity.
- **問題4:** none of the 11 exchanges repeats an exchange from 20260929_1 or
  20260928_2 by function plus form. The nearest are:
  - 4-5 (指摘→謝罪) against 20260929_1 4-11 (不満→謝罪): a different trigger;
  - 4-3 `にしては` against 20260928_2 4-7 `だけに`: a different form.

**No re-draw for errand identity, and nothing added to
`MUTUALLY_EXCLUSIVE_CLIPS`.**

## 6. `make check`: every line naming 20261002_1 (final run)

The final run ends `FAILED — 1 problem(s)`, with 5928 ok, 233 WARN and 249 skip
(2026-10-02; any later paper or gate change moves these totals). The full output
is at
`/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/94f049d6-6faa-4a1f-aacd-dfe4f50c2707/scratchpad/s3-check3.txt`.

### FAIL

| line | disposition |
|---|---|
| `20261002_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)` | **Structural at stage 3.** The 30 聴解 entries come from `make mp3`. The 71 言語知識・読解 entries are stage 5, which is prohibited before QA passes (same as 20260929_1) |

**FAILs fixed during the run:**

| run | line | disposition |
|---|---|---|
| 1 | `every 問題1/2 item re-reads its own question — 問題2-4番 …何だと… / …何と…` | **Resolved** by the fresh-seed re-draw (§4.3). The upstream defect is untouched and still grandfathered (RC-S3-1) |
| 1 | `no 問題7/8/9 keyed form … 問31「ところ」 in the same 文末 frame` | **Resolved** by the two gloss rewrites (§4.4 B) |

### WARN

| line | disposition |
|---|---|
| `20261002_1: no invented place name is one character off — 「みずき市」 ~ 「みずほ市」` (run 1) | **Resolved** by renaming the city to かわせ市 (§4.4 C). The line is now `ok` |
| `20261002_1: 聴解問題5 repeats a headline theme of 20260929_1 (composed paper) — ['旅行・観光', '睡眠・健康']` | **Draw audit; no repair exists** (seed-shopping is forbidden). 5-1 is booking a business-trip hotel against 20260929_1 5-2's tour courses. 5-2 is a health event's rooms against 20260929_1 問題12's lifting technique. The subjects are unrelated; only the tags meet. Both tags are honest, so neither was re-tagged |
| `20261002_1: no 聴解 slot repeats its own theme in the previous 2 papers (4 slots)` | Read side by side (§5.2/5.5). **2-1=働き方 × 20260928_2** is the same recording, two back: a real repeat the one-paper bar allows, recorded (Q7). **2-1=働き方 × 20260929_1** is a bakery founder's motive, a different subject. **2-6=医療・福祉 × 20260928_2** is a human shoulder check-up against a sick dog: unrelated. **2-4=スポーツ・余暇 × 20260929_1** is hobby furniture-making against an athlete's retirement: unrelated. Composed; no repair |
| `drill/N2: pages match the data they bake` (global; lists this test's sources) | `drill/` is gitignored build output that `make drill` / `make pages` / CI rebuild. It does not name this paper as defective. I did not run it, because there is no reason to bake a pre-QA paper into a local build |
| `skip` ×4 errand-key / form-family lines | No keyed or family-tagged draws, so there is nothing to compare. The hand reads are in §5.4–5.5 |
| `skip no 聴解1/2/3/5 errand repeats 20260929_1's` | A skip is not a pass. I read the `shapes` column by hand (§5.5) |
| `note 20261002_1: two-back headline overlap ['旅行・観光'] sits only on the COMPOSED 聴解問題5` | Informational, and correct |

The paper's lines that matter here and are `ok`:
- **Keyed forms:** the keyed-form exposure/frame line and the 問題9 文末モーダル
  line.
- **Topics row:** themes, closing vocabulary, claim, shapes (29/29) and quote
  spans (0 read).
- **Theme rules:** rules 1 to 4.
- **Places and decisive numbers:** both invented-place lines, and 問題14 × 聴解
  decisive number.
- **Passage boxes:** 14/14 in the Markdown, 言語知識・読解.html, 解答.html and
  練習.html.
- **Length and load:** length floor and ceiling, and lexical load (3 lines).
- **Voice and density:** voice quotas, kanji density 29.8%, and median
  sentence 34.0.
- **Options:** 読解 mean option length 27.34, and the ratio lines.
- **Rhetoric instruments:** the not-A-but-B and template caps, and the
  cross-paper template bar.
- **聴解 build:** 問題3 option-set reuse (0.071), question re-read (11/11),
  `script_sha`, and the audio release (31 MP3s).

## 7. verify-scramble

All five 問題8 items (43–47) print `UNDECIDED` with `ARTIFACT: ok`, and the
command exits 0. Of the 24 orderings, 24 survive the tool's 4-junction filter
for each item. That is the tool's normal output, since it does not decide
uniqueness. The per-card last-slot proofs in the 解説 are QA's to read against
the rival orderings.

| item | FREE UNITS |
|---|---|
| 43 | 1 |
| 44 | 0 |
| 45 | 1 |
| 46 | 1 |
| 47 | 0 |

## 8. Content items for QA (NOT repaired here)

| id | where | rule | evidence | owner |
|---|---|---|---|---|
| Q1 | 問題11(1) × 20260929_1 問題13 | §"One topic, one surface", no 読解 topic repeats the previous test (domain read) | Same theme, same MOVE, same measurement-protocol domain, one paper back (§5.4) | QA rules on it. If filed, the 読解 author re-angles 11(1) (stage 3 authors nothing) |
| Q2 | 問題12(B) × 20260929_1 問題11(4) | `claim` column read across papers | Consumption set by a cue, not need, so change the cue (§5.4) | QA. If filed, re-angle 12(B) within 反論への応答 for the A+B pair |
| Q3 | 問題11(4) × 20260929_1 問題12 | domain repeat, one back | Musculoskeletal strain mechanism (§5.4) | QA, minor |
| Q4 | 住まい ×3 (10(3), 聴解1-5, 2-2), plants ×3, body pain ×3 | one topic, one surface | Adjacencies with no shared decisive detail (§5.3) | QA |
| Q5 | 11(2) × 11(3), 11(4) × 12(B) | TEMPLATE column | Unnamed near-skeletons (§5.3) | QA reads the column |
| Q6 | 10(2) 「…と聞くものだった。」 vs 問題9-48 ものだ | keyed form, one per paper | A formal-noun ものだ in 文末 position; the gate is silent (§4.4) | QA. A cheap reword exists (`…と聞く質問だった`) if it is judged a hint |
| Q7 | 聴解2-1番 | errand identity, three papers | Same recording as 20260928_2 2-1 (two back), and a third career-step reason in 2-1 running (§5.5) | QA. Composed; only a re-seed could move it |
| Q8 | 聴解1-4番 × 1-5番 | errand identity within paper | Both are 相談 about a living thing at home and key on relocation (§5.5) | QA confirms. A confirmed pair means a fresh SEED plus `MUTUALLY_EXCLUSIVE_CLIPS` |
| Q9 | 聴解2-3番 | cross-half 〈想定→実は〉 cap | Borderline three-beat. Counted, the total is 2, at the cap (§5.3) | QA |

Any edit to 問題10–14 obliges the Stage-3 re-grep: every 問題7/8/9 keyed form,
with counts and frames, against the §4.4 baseline, plus a re-read of the edited
passage's closing move and of the MOVE and TEMPLATE columns. After that edit,
rewrite the `logs/topics.json` row's `surfaces`, `claim`, `persona` and `notes`
for the edited surfaces against the new bytes.

## 9. Root-cause rows (proposed, NOT applied — gate, composer and pool changes are the owner's call)

| id | defect | class | proposed repair |
|---|---|---|---|
| RC-S3-1 | `compose_choukai.draw()` can draw a clip that `check_consistency.CHOUKAI_QUESTION_REPEAT_GRANDFATHERED` already names as an upstream defect (`imported-n2-2022-07:問題2-4番`, `imported-n2-2021-07:問題2-5番`). Every new paper that draws one FAILs at stage 3, and the only repair available without listening to the audio is a re-seed, which the brief allows but which spends a draw. Founding case: 20261002_1 seed 85360207 | PIPELINE-GAP | Exclude those upstream clip ids in `draw()`, the way the figure items are excluded (and print the note), until each is ear-checked and repaired upstream with `make choukai-bank` + re-compose of its holders. The real fix is to listen to 7/2022 問題2-4番 (and 7/2021 2-5番) once and repair the import |
| RC-S3-2 | The keyed-form frame check takes 〜ところだった's core as bare 「ところ」 and classifies a noun-final （注N） gloss 「…ところ」 as 文末. So any 「…するところ」 place-definition gloss trips the ところだった key, although the noun is not the grammar point (two such glosses were here; the gate printed one) | GATE-COARSE | Either include the copula in the core for 文末 modal keys (ところだ／ところだった), or treat a gloss DEFINITION line (`（注N）X：…`) as a noun frame. Measure over all papers before changing. Rewording was cheap, so this is low priority |
| RC-S3-3 | The blueprint's avoid lists are SUBJECT-level, so a surface can stay off every listed subject and still restate the previous paper's domain + MOVE (Q1) or its claim (Q2). Nothing at stage 1 reads the previous row's `claim` column | PIPELINE-GAP | Stage 1 lists the previous paper's 13 `claim` sentences (plus its domain per 科学・技術/消費・経済 surface) beside each theme's avoid list in the allocation table, so the author avoids a claim, not only a subject string |

## 10. What I skipped, and why

- **Stage 5** (`scaffold-explanations`, `model-answer`): prohibited before QA.
  This is the one remaining FAIL.
- **Stage 4 QA:** not started, as instructed.
- **The upstream repair of `imported-n2-2022-07` 問題2-4番:** it needs the
  audio heard, and it re-composes two other papers. I re-drew instead
  (RC-S3-1).
- **Re-angling Q1/Q2:** this is authoring work, and stage 3 authors no items.
  It is filed for QA.
- **`make drill`:** a gitignored build. The global WARN is recorded, not
  cleared.
- **Gate, composer or pool changes:** RC-S3-1..3 are proposed, not applied.
- **Listening to the MP3:** not possible here. The substitutes were the
  segmentation round-trip (5/6/5/11/2), the `script_sha` match and reading the
  full transcript.
- **No commit**, as instructed. No `git stash` or reset was used.

## Round-1 fix rebuild

Done 2026-10-05 by a context that authored nothing in this paper. The agent
that ran assemble/booklet/sheet after the round-1 fixes stalled without
recording anything, so this section records that rebuild after the fact. It
also re-records the 聴解 half and the topic table. §1–§10 above describe the
paper QA saw: seed `51233600`, sha `10590f1af4e1`. They are history, and
this section supersedes them wherever the two disagree.

**Read in full for this pass:**
- `AGENTS.md`
- `jlpt-test-generation` §Stage 3, §"One topic, one surface" and §"Closing a
  finding…"
- `exam-blueprint` §"The four theme rules" and §"What still governs a
  self-authored surface"
- `qa/qa-report-20261002_1.md`, this report, `qa/blueprint-rerolls-20261002_1.md`
  and `qa/dokkai-allocation-20261002_1.md`
- the merged 問題7–14
- the whole `聴解スクリプト.txt`
- the `logs/choukai_draws.json` and `logs/topics.json` rows for this paper,
  20260929_1 and 20260928_2

**Edited:** only the `logs/topics.json` row (R.3) and this section.

### R.1 Sources, freshness and the re-draw

| file | sha1 (12) |
|---|---|
| `言語知識・読解.md` | `1b77661c9e98` |
| `聴解.md` | `3eef7acf4224` |
| `聴解スクリプト.txt` | `1997305f7a72` (= chapters `script_sha`, gate `ok`) |
| `聴解.mp3` | `f15790511758`. Its sha256 `0da86ab9a969…` and size 44227245 match `logs/upload_manifest.json` `audio/20261002_1.mp3`. Gate: `31 exam MP3(s) are on the audio release` |

**Freshness checks:**
- `python3 tools/assemble_paper.py tests/20261002_1 --check` exits 0, with no
  drift.
- `言語知識・読解.html`, `解答.html` and `練習.html` (18:48:04–05) are newer
  than `言語知識・読解.md` (18:47:58). `聴解.html` is newer than `聴解.md`.
- Gate lines are `ok`:
  - `built HTML matches the Markdown it stamps`
  - `built HTML records its source sha`
  - 14/14 passage boxes in each of the three HTML files
- Spot-check: all three HTML files carry the new strings for 11(1), 問題14 F12
  and 10(1). None carries `さくら台`. 解答/練習 carry the new 聴解1-1番.

**聴解 re-draw history.** Each seed came fresh from RNG, and no hand edit was
made to any 聴解 file.

| seed | outcome |
|---|---|
| `85360207` | stage 3. Drew `2022-07:問題2-4`, so FAIL (§4.3) |
| `51233600` | the paper QA reviewed. Superseded: QA F1 refused `kanzenmoshi:cd1-04` in `textbook_items.json` |
| `54137854` | rejected. It drew the grandfathered-defective `2022-07:問題2-4` (RC-S3-1) |
| `64787247` | rejected, for the same reason |
| **`63138204`** | **final.** Sources: official 20, soumatome 6, kanzenmoshi 1, mimikara 1, shinkanzen 1. The archive records are `archive:2014-12:問題3-5` and `archive:2020-12:問題5-1` |

The composer's console output for the last seed was not saved by the stalled
agent, so whether it dropped a freshness bar is read from the draw instead.
`kanzenmoshi:cd1-04` is not drawn, and neither is `2022-07:問題2-4` or
`2021-07:問題2-5`.

**Clip repeats** (`logs/choukai_draws.json`):
- **Against 20260929_1:** 0/29 in the same slot, and 0 slot-free repeats in
  any slot. 29 distinct clips.
- **Against 20260928_2 (two back):** 3 textbook clips repeat, all allowed by
  the one-paper bar.

  | this paper | clip | 20260928_2 |
  |---|---|---|
  | 1-4番 | `soumatome:cd1-44` | its 1-1番 |
  | 4-1番 | `soumatome:cd2-47` | its 4-6番 |
  | 4-2番 | `shinkanzen:cd2-66` | its 4-5番 |

  This makes the round-1 open process note (two-back bar, a `make choukai-wear`
  question) three items deep on this paper.
- **F14 is still open.** `2022-12:問題1-3` (「書いていておいて」) survived the
  re-draw, so 20261002_1 is again a holder of that clip.

### R.2 Keyed-form re-grep (whole 読解 half, 問題10–14 incl. options and glosses), after every round-1 edit

| form (item) | count | frame |
|---|---|---|
| ところだった (31) | 0 | — |
| ところ (core of 31) | 2 | 12(B) 「四百円のところを」 (連用, noun) and 13 「一人のところに」 (連用, noun). Neither is 文末 |
| っぱなし 32, ざるを得 33, といっても／と言っても 34, 申し上げ 35, ことなく 36, ものがある 37, 過言 38, といい 39, さておき 40, にわた 41, にしたが／に従／したがって 42 | 0 each | — |
| のみならず 43, 先立 44, にしては 45, ことから 46, どころか 47 | 0 each | — |
| ものだ／ものである (48) | 0 | 10(2) now reads 「…と聞く質問だった。」 (F10) |
| ところが (49) | 0 | 10(3) now opens 「けれども、」 (F10) |
| 目を通 (50), 切り抜 (51) | 0 | — |
| new 文字・語彙 keys: 実績 (1-1), しつこい (4-20), 身につ (6-29) | 0 each | — |

**Sentence-initial connectives in the 読解 prose:**

| connective | count |
|---|---|
| ただ | 3 |
| そのため | 3 |
| また | 2 |
| そこで | 2 |
| ですから | 2 |
| それでも, けれども, たしかに, すると, 一方, たとえば | 1 each |

- No keyed connective appears.
- そこで is a 問題9-49 *distractor*, which is not exposure.
- ただ is no longer keyed, because 4-20 was rerolled.
- Gate: `no 問題7/8/9 keyed form appears more than 1× … or even once in the
  same frame` is `ok`.

**聴解 speaks keyed forms**, but it is sat after 言語知識 is collected, so
there is no leak:
- にしては: 1-1番 「この時期にしては」 and 4-3番, the 問題8-45 form
- つけっぱなし: 4-5番, the 問32 form
- 揃ったところで: 4-9番
- わけじゃない: 4-11番

**Each edited passage's closing move, re-read:**

| passage | edit | final now | matches allocation |
|---|---|---|---|
| 10(1) | apparatus | 「ご協力をお願いいたします。」 | 実用文 |
| 10(2) | F13 | 「…案内台まで来て番号を見せることになる。」 | the 〜ない以上、…ことになる skeleton, unchanged |
| 10(3) | F10 | unchanged: 「収納は、量だけではない。…こそが…」 | 主張 / `だけではない…こそ` / 〈想定→実は〉 |
| 10(5) | re-angle | unchanged: 「…時間が来るまで、写真は電話の中で順番を待っている。」 | 条件提示, now under 反論への応答. The complaint is conceded (「たしかに、設定しただけでは…」), not denied |
| 11(1) | replaced | 「凍った物を電子レンジで温めるときに大切なのは、…時間をとることです。」 | 説明 / 分裂文 (the paper's only cleft) / 機構の説明 |
| 11(2) | F11 (gloss removed) | unchanged | — |
| 11(4) | F8, F11 (gloss removed) | unchanged | — |
| 12(B) | re-angled | 「まとめ買いの安さは、…という仕組みの上に成り立っています。」 | 説明, unnamed, not a cleft. It differs from 12(A) 「〜のが、…賢いやり方である」 and from 11(1) |
| 14 | F12 | 「受付日の2日前の金曜日（6月7日の分は6月5日、…）」 | the key, 6月5日, is now decided by the flyer's own wording |

- The Q5 pair 11(4)×12(B) (〜ていく) is gone, because the old 12(B) final was
  replaced.
- Glosses: the gate reads 25 （注N） markers, at the floor of ≥25.

### R.3 `logs/topics.json` row: checked against disk, and what changed

The stalled agent had already rewritten the row (18:56, after the final
compose at 18:37). I re-checked every field against the current 言語知識・読解.md,
`聴解スクリプト.txt` and `choukai_draws.json`:

- **All 29 聴解 entries** (`surfaces`, `themes`, `shapes`, `claim`) describe
  the seed-63138204 draw, line by line against the script. That includes the
  three same-recording notes on 1-4, 4-1 and 4-2.
- **The four 読解 surfaces** (10(1), 10(5), 11(1), 12(B)) and their `claim`
  and `persona` (11(1) 職業人) match the passages.
- **No removed string remains.** I grepped for the leaf protocol, 戸棚,
  残りの多さ, さくら台, 受付まで, ものだった, 畳, `kanzenmoshi:cd1-04`, and
  every old-seed subject.

**Changed by this pass:**
1. **`surfaces.問題14`.** It still described the pre-F12 deadline, `前の週の金曜日までに`
   (not in the paper; it sat outside 「」, so the quote gate could not see
   it). It now reads 受付日の2日前の金曜日までに.
2. **`notes`.**
   - Added the two rejected round-1 seeds (54137854, 64787247) and why they
     were rejected.
   - Replaced the 〈想定→実は〉 sentence. It had counted 10(3) + 聴解3-2番 = 2
     and silently dropped 聴解2-3番, which QA round 1 counted. It now states
     both counts (R.4) and leaves the cap open.
   - Added the rule-4b same-setting/different-issue note for 聴解問題5.

Every other row in the file is byte-identical. The gate after the edit reads
`every logs/topics.json 「…」 span occurs in its own paper (0 spans read)`
`ok`, plus `claim`, `shapes 29/29` and the theme lines `ok`.

### R.4 Whole-paper topic table: changed surfaces and all 聴解 rows

**読解, the changed surfaces.** Each is on its drawn theme, off that theme's
spec `avoid` list (checked by keyword over all 28/24/60/26 entries), and new
against every row of `logs/topics.json`.

| surface | shipped subject (drawn = theme only) | theme | closing | template | MOVE | 20260929_1 same seat | 20260928_2 same seat |
|---|---|---|---|---|---|---|---|
| 10(1) | けやき通り児童館の平日午前の親子の時間（お知らせ） | 子育て・家族 | 実用文 | — | 実用文 | 開けずにすむ引っ越しの箱 (住まい) | 手ぬぐいの二色染め（メール） |
| 10(5) | 写真の自動保存が動く条件 | デジタル化 | 条件提示 | unnamed 〈条件〉が来るまで…待っている | 反論への応答 | 広報紙の小さな欄 | 教室に置いて帰れる教科書 |
| 11(1) | 冷凍食品を電子レンジで温めるむらの仕組み | 科学・技術 | 説明 | 分裂文 | 機構の説明 | 着る日から買う服 | 雑貨店の傘の売れ方 |
| 12(B) | まとめ買いの先払い (A+B: 日用品のまとめ買い) | 消費・経済 | 説明 | unnamed …という仕組みの上に成り立っている | 反論への応答 (A+B) | 軽いものの前で痛める腰 | 翌朝に開き直す決まり |

- **F2 is cleared.** 10(1) no longer shares a place name, a 4月 start, a title
  shape or an option-1 opening with 20260929_1 10(2). The place-name gate
  lines are `ok`.
- **F3 is cleared.** 11(1) is a heating mechanism, not a measurement protocol,
  and not 20260929_1 問題13's 気温 domain or its conceded-objection move.
- **F4 is cleared.** 12(B) now argues cash paid up front. It has no cue,
  visibility or storage claim, so 20260929_1 11(4)'s claim and 10(3)'s
  placement subject are gone.

**MOVE column**, read down on its own (10 essay surfaces):

| MOVE | surfaces | count |
|---|---|---|
| 機構の説明 | 11(1), 11(4), 13 | 3 (cap) |
| 反論への応答 | 10(5), 11(3), 12 | 3 (cap) |
| 一人称の前後比較 | 問題9, 11(2) | 2 |
| 数えたことの報告 | 10(2) | 1 |
| 〈想定→実は〉 | 10(3) | 1 |

This matches the updated allocation.

**TEMPLATE column**, read down separately:
- **Named:** `だけではない…こそ` ×1 (10(3)) and 分裂文 ×1 (11(1)).
- **相関:** 0.
- **Cap-1 templates:** 後知れ, 不在の残り and 先回り are all 0.
- **Every named pair differs:** 9/11(2), 10(2)/11(4), 10(5)/13, 11(1)/12(B)
  and 12(A)/12(B).
- **Cross-paper bars hold:** 問題11 has no `A というより B`, and 問題13 is no
  cleft.

**Theme rules:**
- 13/13 読解 themes are distinct.
- The five headline themes are distinct: 9 メディア・情報, 12 消費・経済,
  13 人間関係, 14 防災, and 聴解5 働き方 + 睡眠・健康.
- No 読解 headline repeats either previous paper.

**Persona:**

| persona | surfaces | count |
|---|---|---|
| 趣味の実践者 | 9, 11(2) | 2 |
| 解説者 | 11(4), 13 | 2 |
| 店員 | 10(5) | 1 |
| 職業人 | 11(1) | 1 |

**〈想定→実は〉 across both halves (cap 2): OPEN, needs a ruling.**

| surface | how it reads | counted |
|---|---|---|
| 読解 10(3) | full three-beat | **1** |
| 読解 10(5) | conceded complaint, then a mechanism | not counted, borderline (same convention as old 11(1)/12(B)) |
| 聴解2-3番 | the friend's guess at the cause (「先生、教え方うまいの」), denied (「…習うんじゃないんだ」), then the real cause (events). QA round 1 counted it | 1 if counted |
| 聴解3-2番 (new draw) | the fans' question presupposes technique, which is dismissed (「少しぐらい下手でも構わないんです」, introduced by 「私は反対に」), then Y (what to express) | 1 if counted. As strong as 2-3番 or stronger |
| 聴解3-5番 | 「…だけではありません」 adds rather than denies, and the view is unattributed | not counted |

- **Counted the way round 1 counted, the total is 3: one over the cap.**
- **Under the strict rubric, the total is 1,** because a question is not an
  attributed belief.
- The rule says the 読解 side is the one re-angled. The allocation's only
  legal target is 10(3) → 一人称の前後比較 (2 → 3), written on a practice.
  That is authored work, so it is **reported here, not done**.

**聴解, a draw audit of all 29 rows.** Shipped themes and subjects are in the
topics row. Theme tally:

| theme | count |
|---|---|
| 働き方 | 10 |
| スポーツ・余暇 | 5 |
| 人間関係 | 4 |
| 住まい | 2 |
| 文化・伝統 | 2 |
| 消費・経済 | 2 |
| 環境, 教育, 医療・福祉, 睡眠・健康 | 1 each |

It is not re-angled.

Errand identity across three papers (`shapes`), read against the
`MUTUALLY_EXCLUSIVE_CLIPS` standard (same errand, same implicature, same key):

- **Same recordings two back:** 1-4, 4-1 and 4-2 (above). This is identity by
  construction, and allowed.
- **1-3番 × 20260929_1 1-3番, the closest cross-paper pair, in the same
  slot.** Both revise a sales visual after one critique from a superior:
  - here, a cookie box: 目に止まりにくい → 目立つ色 → change the box design;
  - there, a PC poster: 数字だけでは分かりにくい → add a comparison chart.

  The object, the fix and the key differ, and knowing one key gives nothing
  for the other. So this is **not identity**. It is recorded as a near-pair
  for the scoped re-review.
- **Within the paper:** 1-1 (合宿 checklist), 1-3 (critique → box) and 1-5
  (展覧会 final check → lighting) are all "pick the one remaining fix/task".
  That is the 問題1 format. The keys are disjoint, so this is not identity.
- **Not identity:**
  - 3-2番 × 20260929_1 3-2番 (praising children specifically). Both are "not
    X but Y" talks in one slot: a shared shape, with different subjects.
  - 5-1 (who attends an award ceremony) × 20260929_1 5-1 (a gym membership)
    × 20260928_2 5-1 (a 親子サッカー plan).
  - 5-2 (health-event rooms) × 20260929_1 5-2 (tour courses) × 20260928_2 5-2
    (sunset spots). This is the 5-2 format.
  - No 問題4 exchange repeats 20260929_1 by function plus form.

**No `MUTUALLY_EXCLUSIVE_CLIPS` entry and no re-draw for errand identity.**

**読解 and 聴解, read as one list.**
- **Decisive numbers.** The gate reads `問題14 shares no decisive number with
  any 聴解 item` as `ok`. 12(B)'s 四百円/千円/六百円 appear in no 聴解 item.
- **Domain adjacencies with no shared decisive detail:**
  - 10(5) home wireless / 聴解3-3 internet plan;
  - 10(2) hospital / 聴解3-4 care equipment;
  - 10(3) storage / 聴解2-2 moving furniture;
  - 12 bulk-buy saving / 聴解2-2 cheaper move / 3-3 cheaper plan.
- **Inside 読解, for the scoped re-review (minor, not filed here):**
  - **10(5) × 11(1)** are both a worker explaining a household device's
    hidden mechanism to lay users: 店員 on phone backup, 職業人 on the
    microwave. The MOVE, theme and claim differ.
  - **11(1) × 11(3)** are both kitchen settings in 問題11: microwave physics
    and a dashi tasting. The subject and claim differ.

### R.5 `make check` lines naming 20261002_1 (rerun after the R.3 edit)

The run exits 2: `FAILED — 1 problem(s)`, with 5929 ok, 232 WARN and 249 skip
(2026-10-05; any later paper or gate change moves these totals). Output is in
the session scratchpad as `s3b-check.txt`.

| line | disposition |
|---|---|
| FAIL `詳細解説.json explains every keyed item (30 entries for 101 keys)` | **Expected; stage 5.** The 30 聴解 entries come from the composer. The 71 言語知識・読解 entries are prohibited before QA closes |
| WARN `聴解問題5 repeats a headline theme of 20260929_1 (composed paper) — ['働き方','睡眠・健康']` | **Draw audit; no repair** (seed-shopping is forbidden). 5-1 (働き方, restaurant staff choosing who attends an award ceremony) against 20260929_1 問題9 (働き方, leaving work at a half-finished point): unrelated subjects. 5-2 (睡眠・健康, health-event rooms; the woman's sleep complaint) against 20260929_1 問題12 (lifting and back strain): only the health domain is shared. Both tags are honest and neither was re-tagged. Rule 4 two back: 20260928_2 headlined neither theme, and the gate line is `ok`. The round-1 tags were 旅行・観光 + 睡眠・健康; 旅行・観光 left with the re-draw |
| (resolved) `no 聴解 slot repeats its own theme in the previous 2 papers` | **Now `ok` (0 slots).** The round-1 WARN (4 slots, including 2-1 `soumatome:cd1-30`) is cleared by the re-draw |
| WARN `every stamped spec's pools_sha matches pools.json` (lists 20261002_1 as stamped on a REROLL) | **A record, not a defect.** It follows from the three 文字・語彙 rerolls in `qa/blueprint-rerolls-20261002_1.md`. Separately, that file's pool follow-up is still unapplied: 中級, 切実 (two entries) and connective ただ stay drawable. That needs the owner |
| WARN `drill/N2: pages match the data they bake` (lists `tests/20261002_1/*` as not in the build) | **Global, gitignored build output.** `make drill` / `make pages` / CI rebuild it. It names no defect of this paper, and there is no reason to bake a pre-QA paper into a local build |
| skip ×4 errand-key / form-family lines; skip `no 聴解1/2/3/5 errand repeats 20260929_1's` | No keyed or family-tagged draws. A skip is not a pass; the hand read is R.4 |

### R.6 Authored-content items found (reported, NOT fixed: this pass edits no exam text)

| id | where | evidence | owner |
|---|---|---|---|
| R-1 | cross-half 〈想定→実は〉 cap | 3 under round-1 counting (10(3) + 聴解2-3番 + 聴解3-2番), or 1 under the strict rubric (R.4). Needs an orchestrator/QA ruling. If 3 stands, re-angle 10(3) to 一人称の前後比較 and re-run R.2 | orchestrator → 読解 author |
| R-2 | 12(B) ¶2 | 「一つあたりで見れば二百円ほど得をしています」. 200円 is the whole-pack saving (4×300円=1,200円 against 1,000円). Per unit, the saving is about 17円 (100円 against about 83円), so the per-unit frame misstates the figure. No key depends on it (65 key 1 is 「一つあたりにすると割安」). A wording fix such as 「全部で二百円ほど得をしています」 would need the 読解 author and a re-check of 65/66 | 読解 author (minor) |
| R-3 | 10(5) × 11(1); 11(1) × 11(3) | Near-pairs (R.4), not findings | scoped re-review reads them |

Not done in this pass, with the reason:
- Stage 5: prohibited before QA closes.
- Any edit to `_sections/`, `言語知識・読解.md` or 聴解.*: out of scope by
  brief.
- No `make mp3`, `make autofix`, commit, stash or reset was run.
