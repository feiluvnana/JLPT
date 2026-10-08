# Stage 3 (build + gate) — 20261008_1

Run 2026-10-08. This context **resumed** a stage-3 run that was stopped
partway, and it authored none of the exam items. The only files it wrote by
hand are the `logs/topics.json` row and this report.

> **Superseded (QA F5, 2026-10-08):** these shas predate the fixes made after hand-off: C1/C2, then QA round-1 F1/F2/F3/F6/F7. The current `言語知識・読解.md` sha256 is `e4a8f8da93a4`; the 聴解 files are unchanged. `qa/qa-report-20261008_1.md` records the shas QA read.

**Source shas at hand-off:**

| file | sha256 (12) | sha1 (12) |
|---|---|---|
| `言語知識・読解.md` | `6eaf37e06d3c` | `f13dd830d923` |
| `聴解スクリプト.txt` | `f87586531e65` | `e83e714732fc` (= chapters `script_sha`, gate `ok`) |
| `聴解.md` | — | `1aac1d3b91f4` |
| `聴解.mp3` | `0242400f2ccd` (= `logs/upload_manifest.json` `audio/20261008_1.mp3`, 44,059,052 bytes) | `3f10d46ca375` |

A build or repair that finds these moved must re-run this pass
(`jlpt-test-generation` §"One writer per test folder").

## 1. What I read, in full, from disk

- `AGENTS.md`, `CLAUDE.md`
- `.agents/jlpt-test-generation/SKILL.md`, the whole file (§Stage 3, §"One
  topic, one surface" and §Invariants included)
- `.agents/exam-app/SKILL.md`, the whole file
- `.agents/choukai-audio/SKILL.md` Part 0, the whole part
- `.agents/exam-blueprint/SKILL.md`: §"Topic themes" through §"The four theme
  rules" (rules 4b, 4c and 5 included), and §"What still governs a
  self-authored surface"
- `qa/stage3-report-20261002_1.md`, as the format model (§1–§10 and the
  round-1 rebuild section up to R.4)
- `qa/dokkai-allocation-20261008_1.md` and `qa/blueprint-rerolls-20261008_1.md`
- `tests/20261008_1/test_spec.json`: the reading-topic themes and all 12 avoid
  lists, plus the grammar draws
- the merged `言語知識・読解.md`: 問題7, 問題9 to the end of 問題14, and item 33
- the composer's `聴解スクリプト.txt`, in full, and `聴解.md`'s 問題1/2 options
  and key table
- `logs/choukai_draws.json`: the rows for this paper, 20261002_1 and 20260929_1
- `logs/topics.json`: the full rows for 20261002_1 and 20260929_1, and every
  earlier row's tag for each clip this paper drew
- `qa/qa-report-20261002_1.md`: its Q8 ruling
- In `tools/check_consistency.py`, while resolving specific lines:
  - `check_key_grammar_exposure`
  - `check_q14_apparatus_reuse` and `q14_block`
  - `check_pools_sha_replayability`
- In `tools/compose_choukai.py`: `MUTUALLY_EXCLUSIVE_CLIPS`

## 2. Commands, in order, with exit status

**Done by the stopped run.** I did not repeat these; the brief lists them.

```
make assemble 20261008_1                         # stopped run
make autofix 20261008_1                          # stopped run — BEFORE make mp3, as required
make lint-draft 20261008_1                       # stopped run
make verify-scramble 20261008_1                  # stopped run
make mp3 20261008_1 SEED=23329961                # stopped run — the 聴解 compose seed (RNG output)
python3 tools/choukai_segment.py tests/20261008_1/聴解.mp3   # stopped run — recovery
(draw audit vs 20261002_1 and 20260929_1)        # stopped run
```

**This run:**

```
python3 tools/assemble_paper.py tests/20261008_1 --check     # 0 — no layout drift
python3 tools/choukai_segment.py tests/20261008_1/聴解.mp3   # 0 — re-verify: ok 45.9 min, LUFS -14.98, 5/6/5/11/2
(draws row re-read: 20261008_1 present, seed 23329961; audit re-run, same result)
gh auth status                                   # feiluvnana active (td-nguyen-38 inactive); no switch
make upload-files TARGET=tests TEST=20261008_1   # 0 — 44.1 MB uploaded to `audio`, manifest 41 assets
make booklet 20261008_1                          # 0 — both booklets built, verify() ok
make sheet 20261008_1                            # 0 — 解答.html + 練習.html, 101 items (71 without 詳細解説 yet: stage 5)
make check                                       # 2 — run 1: 3 FAIL
  -- logs/topics.json row appended (§6) --
make check                                       # 2 — run 2 (final): 3 FAIL, same three
make choukai-wear                                # 0 — report only, under the 4.0 ceiling (§5.5)
```

- **`make autofix` was NOT run in this context**, and nothing was edited after
  the compose, so no rebuild chain was owed.
- **No `聴解.*` file was touched.** No re-compose was owed: no upstream-defect
  FAIL, no repeat against the previous paper, no errand identity (§5.5).
- The 問題14 and 「とは」 fixes I propose in §4 were simulated against copies of
  the text in scratch, with the gate's own functions. The paper on disk is
  unchanged.

## 3. Seeds

| seed | what | source |
|---|---|---|
| `24370401` | blueprint | `make sample` (stage 1), RNG; plus three stage-2 `--reroll-one` seeds `82200856`, `6943260` and `11565207` (`qa/blueprint-rerolls-20261008_1.md`) |
| `23329961` | 聴解 compose | stopped stage-3 run, RNG. **Kept.** No re-draw was needed |

## 4. `make check` — final run

`FAILED — 3 problem(s)`, with 6151 ok, 236 WARN, 10 note and 257 skip
(2026-10-08; any later paper or gate change moves these totals). Full output:
`/private/tmp/claude-501/-Users-td-nguyen-Desktop-jlpt/19cc0970-4605-4504-b822-7a343d532103/scratchpad/s3r_1008_check2.txt`.

### 4.1 FAIL (all three name this paper)

| # | line | class | disposition |
|---|---|---|---|
| F-A | `問題14 shares no run of 20+ characters with another paper — 20 chars vs 20261002_1: 「は、合わせていくらか。円円円円市内に住む」` | **CONTENT (item wording)** | Routed to the 読解 author (C1 below). Stage 3 does not edit stems |
| F-B | `no 問題7/8/9 keyed form appears more than 1× in the 問題10-14 prose … 問33「とは」×2` | **CONTENT (passage prose)**, triggered by a coarse count | Routed to the 読解 author (C2). Gate row proposed (RC-S3-1) |
| F-C | `詳細解説.json explains every keyed item (30 entries for 101 keys)` | structural | **Stage 5.** `make mp3` wrote the 30 聴解 entries. The 71 言語知識・読解 entries are prohibited before QA passes. Same as 20261002_1 and 20260929_1 |

**C1 — 問題14 stems 70/71 (F-A).**
- The run joins 70's tail 「…は、合わせていくらか。」, the four 円 options and
  71's head 「市内に住む…」. 20261002_1's 70 and 71 have exactly the same shape.
- **I read the whole 大問 against 20261002_1**, as the line asks:
  - **Document type:** a home-visit haircut service, against an
    extinguisher refill and take-back day. Different.
  - **Row structure:** a 3-row single-column fee table, against a 2×2 size ×
    service grid. Different.
  - **受付期間:** a monthly rule (前の月の20日), against two fixed Sundays with a
    2-day-prior Friday deadline. Different.
  - **Late route:** a 前日 5 p.m. change by phone and a 10-day mail lag on the
    voucher, against a weekday counter that takes only returns. Different.
  - **Stem constraint pairs:**
    - 70 here: fee − voucher + 出張料, with the voucher not usable on the
      出張料.
    - 70 there: two units + delivery.
    - 71 here: first-time application + the prior-month deadline.
    - 71 there: a missed pick-up date, so delivery.
- **Verdict:** a stem phrase is shared, not a re-skin. The shared stem
  phrasing is still a gate FAIL, and it has a one-word fix.
- **Note for QA:** both 70s use a 500円 add-on (出張料 here, delivery there).
- **Proposed fix (verified in simulation):** in 70, change
  「大川さんが払う金額は、合わせていくらか。」 to 「大川さんが払う金額は、全部でいくらか。」.
  - The longest shared run then drops to 15 characters: 「課へ電話でお申し込みください。」,
    a contact line, under the floor of 20.
  - Changing 71's opening instead would also work.
- **After the fix:** run `make assemble` → `make lint-draft` (ignore its
  CHOUKAI line) → `make booklet` → `make sheet` → `make check`. The fix must
  be made in `_sections/問10-14_読解.md` too. **NEVER run `make autofix`**: it
  corrupts the composed 聴解 script.

**C2 — 「とは」 ×2 (F-B).**
- 問33 keys 「とは」 (「再会する（とは）、思ってもみなかった」). The gate does
  `prose.count("とは")`, so it counts two 「ことは」 in the passage prose:
  - **10(3)'s FINAL:** 「…その週のうちに二度調べることはなかった。」
  - **11(4), mid-passage:** 「一時間置くことは変えられませんが、…」
- Neither is the 〜とは grammar point; the bare 「(?<!こ)とは」 count in 問題10–14 is
  **0**. So the hits are coarse, but they are a FAIL, and the rule is "rewrite
  the reading occurrence".
- **Proposed fix (verified in simulation):** in 11(4), change
  「一時間置くことは変えられませんが」 to 「一時間置くのは変えられませんが」.
  - The count goes to 1, and the line reads `ok`.
  - It touches no final, gloss or decisive detail.
- **The alternative is 10(3)'s final** (「…二度調べはしなかった。」), which also
  clears the line. It is **not** recommended: it changes an allocated final
  sentence.
- **After the fix**, the author owes the keyed-form re-grep against the
  baseline in §7, plus a re-read of 11(4)'s closing move. The final is
  unchanged: 「そこで、いちばんよく売れる食パンだけは、…遅らせました。」.

### 4.2 WARN and note lines that name this paper

| line | disposition |
|---|---|
| `every stamped spec's pools_sha matches pools.json (b8ba57b537f9) … 20261008_1 recorded 788effc61383` | **Record, not a defect, and no re-stamp.** The check's own text says "Expected after any pool repair; it is a record, not a defect". Its docstring says a hand-written stamp "would be a fabrication". `788effc61383` is the stamp of the last stage-2 `--reroll-one`, and the gate notes that it certifies that redraw's pool. `pools.json` moved after it because the stage-2 orchestrator deleted おおらか (`context_words`, `usage`), 〜ぶる and 〜めく (`word_formation`), as `qa/blueprint-rerolls-20261008_1.md` records. Replaying seed `24370401` will therefore not reproduce the draw item for item, and `--replay` is not a sampler concept. Nothing prescribes an action |
| `20261008_1: 聴解問題5 repeats a headline theme of 20261002_1 (composed paper) — ['消費・経済']` | **Draw audit; no repair exists** (seed-shopping is forbidden). 5-2番 is a bicycle sales pitch, tagged 消費・経済 as 20260928_1 tagged the same recording. 20261002_1's 消費・経済 headline is 問題12, bulk-buying daily goods. The subjects are unrelated and only the tags meet. The tag is honest, so it was not re-tagged |
| `20261008_1: no 聴解 slot repeats its own theme in the previous 2 papers (1 slot) — 聴解問題3-3番=メディア・情報 (also 20260929_1)` | **Same recording** (`archive:2020-12:問題3-3`, a one-anime-abroad talk), two papers back in the same slot. The one-paper bar allows it. It is one of the six two-back repeats (§5.5) |
| `note 20261008_1: two-back headline overlap ['旅行・観光'] sits only on the COMPOSED 聴解問題5` | Informational and correct. 5-1番 is a hotel for a conference trip; 20260929_1's 5-2番 is a group-tour course choice |
| `skip` ×4 errand-key / form-family lines; `skip` 聴解 errand vs 20261002_1 | A skip is not a pass. I read the `shapes` column by hand (§5.5) |
| `skip` セクション構成表 / 問題5 two-read-back / 問題5 options | Composed paper. These are the same skips 20261002_1 carries |
| `skip 詳細解説 carries no scaffold placeholder` | Stage 5 |

**Global WARNs that cover this paper without naming it:**
- `drill/N2: pages match the data they bake`: `drill/` is gitignored build
  output, and I did not run `make drill`.
- `問題1 reading-trap rate across generated papers`: corpus-level. Stage 1
  dispositioned it (`qa/blueprint-rerolls-20261008_1.md`).

**Lines worth knowing that read `ok`:**
- **聴解 build:**
  - `script_sha`
  - `32 exam MP3(s) are on the audio release`
  - 問題3 option-set reuse: worst 0.067 against the ceiling of 0.30
  - every 問題1/2 item re-reads its own question (11 items)
  - 問題14 × 聴解 decisive number
- **Rendering:** 14/14 passage boxes in all three HTML files.
- **Topics row:**
  - closed themes
  - rules 1–4 on the 読解 half
  - claim present
  - shapes 29/29
  - 0 「」 spans
- **Voice:** first person 6 (≥4), です・ます 3 (≥3), kanji density 29.5 %.
- **Length and load:** the length floor and ceiling, and lexical load at the
  current-era ceiling (novel 15.8 % against an author target of ≤15.8 %).
- **Glosses:** 27, at the band floor of 27. **An author edit must not drop
  one.**
- **Rhetoric instruments:**
  - not-A-but-B: 1 of 13
  - template caps and the cross-paper template bar
- **Options:** 読解 mean option length 27.54.

## 5. The whole-paper table

### 5.1 読解 + 問題9 cloze

- **"Drawn"** is the spec's `reading_topics[i].theme` plus its avoid list; the
  cloze theme was drawn by RNG at stage 1.
- **"On draw"** means three things: the shipped subject is about that theme,
  it is not on the avoid list, and it is not a re-wording of an avoid entry.
  I checked by keyword across all 450 avoid entries; §5.4 gives the hits.
- **Every final** is the sentence the allocation table records, and each
  closing, template and MOVE matches its row.

| surface | shipped subject | theme (shipped = drawn) | on draw | closing | template | MOVE | persona | 20261002_1 same seat | 20260929_1 same seat |
|---|---|---|---|---|---|---|---|---|---|
| 問題9 | 役場窓口の昼休み閉鎖と電話予約の例外 | 行政・手続き | yes | 反論応答 | unnamed 〈決まりは続けていく。ただ、Xにも、Yのための入り口を一つ開けておきたい〉 | 反論への応答 | 職業人 | 切り抜き帳と一行の理由 | やりかけで帰る |
| 10(1) | 夕焼けが赤い理由 | 科学・技術 | yes | 説明 | `〜のは B だ（分裂文）` (the one cleft) | 機構の説明 | 解説者 | 児童館の親子の時間（通知） | 開けずにすむ引っ越しの箱 |
| 10(2) | 校外学習で42人が電車に乗る前の事前連絡（メール） | 交通 | yes | 実用文 | — | （実用文） | 実務者 | 病院の案内図と予約票の番号 | 回覧板とアプリ（通知） |
| 10(3) | 一週間、スマートフォンで調べた字を数える | デジタル化 | yes | 条件提示 | unnamed 〈Xした字は、その週のうちにYすることはなかった〉 | 数えたことの報告 | 利用者 | 収納の置き場所 | 電話だけの取り決めの引き継ぎ |
| 10(4) | 俳句を散歩の途中で作る | 文化・伝統 | yes | 随筆 | unnamed 〈今のNには、どれも、Xが一つずつついてくる〉 | 一人称の前後比較 | 趣味の実践者 | インク容器の引き取り（メール） | 昔の写真と今の写真の展示 |
| 10(5) | 図書館の新聞の保存期間の短縮（お知らせ） | メディア・情報 | yes (**see Q6**) | 実用文 | — | （実用文） | 図書館（通知） | 写真の自動保存が動く条件 | 広報紙の小さな欄 |
| 11(1) | 島の船の時刻表が毎日ずれる理由 | 旅行・観光 | yes | 意外な観察 | unnamed (no のは, no foil) | **〈想定→実は〉** | 旅行者 | 冷凍食品を電子レンジで温めるむら | 着る日から買う服 |
| 11(2) | 一回の避難訓練で、両どなりに声をかけてから出た班 | 防災 | yes (**see Q5**) | 条件提示 | `A ほど B（相関）` (the one) | 数えたことの報告 | 係 | かるたの読み手 | 留守番の練習 |
| 11(3) | 友人の相談の電話で、最後まで聞く | 人間関係 | yes | 随筆 | unnamed 〈今は、Xたら、Yを置いて、Zのを待つことにしている〉 | 一人称の前後比較 | 友人 | 家で取るだしと粉のだし | 家族の書類を読み上げる |
| 11(4) | 焼いたパンを一時間置いて売る理由と客の声 | 食 | yes (**see Q4**) | 反論応答 | unnamed 〈そこで、XだけはYよう、Zを遅らせました〉 | 反論への応答 | 職業人 | 山の下りで脚が痛む仕組み | 器の大きさと食べる量 |
| 12(A) | 夏に池の水が緑になる仕組み | 環境 | yes | 説明 | unnamed 〈Xし、Yすれば、Zず、Wまま保たれる〉 | 機構の説明 (A+B one) | 解説者 | 日用品のまとめ買い | 腰を痛めない持ち上げ方 |
| 12(B) | 池に投げ入れるパンと水の色 | 環境 | yes | 主張 | `A だけではない。B こそが〜` (the one) | ″ | 論者 | まとめ買いの先払い | 軽いものの前で痛める腰 |
| 13 | 古い借家の台所の水が凍る朝を一冬数える | 住まい | yes (**see Q7**) | 主張 | unnamed prescription 〈〜方は、〜晩には、〜を、〜てから休んでください〉 | 数えたことの報告 | 住人 | 仲間内の幹事役が一人に決まる仕組み | 芝生の上で測る気温 |
| 14 | しらとり市 訪問理容・美容の案内 | 医療・福祉 | yes | — | — | （実用文） | 市（案内） | 消火器の詰め替え・引き取り | 留学生の奨学金 |

**Theme rules, on the shipped surfaces:**
- **Rule 1:** the five headline surfaces take five themes: 問題9 行政・手続き,
  12 環境, 13 住まい, 14 医療・福祉, and 聴解問題5 旅行・観光 + 消費・経済.
  Gate `ok`.
- **Rule 2:** no 読解 headline theme appears on another 読解 surface.
- **Rule 3:** 13 of 13 読解 themes are distinct. Gate `ok`.
- **Rule 4, one back:** no 読解 headline repeats 20261002_1. The composed
  5-2番 repeats 消費・経済 (a WARN, §4.2).
- **Rule 4, two back:** no 読解 headline repeats 20260929_1. The composed
  5-1番 旅行・観光 is noted by the gate and not counted.
- **Rule 4b** (headline subjects against 20261002_1's 13 読解 + 29 聴解):
  - No same-setting-same-issue match.
  - Same domain, different issue: 問題14 訪問理容 against 20261002_1
    聴解3-4番 (equipment that eases a carer's load), both elderly care.
  - 問題9's 役場 counter shares nothing with 20261002_1. The nearest is 10(2)'s
    hospital 案内台, a different institution and a different issue.
- **Rule 5 (voice):** first person 6, です・ます 3, kanji density 29.5 %. All
  `ok`.
- **Persona cap of 2:** 職業人 ×2 (問題9, 11(4)) and 解説者 ×2 (10(1), 12(A)).
  Every other token appears once.
- **問題12 cross-test column:** 池の水が緑になる (here), 日用品のまとめ買い
  (20261002_1) and 腰を痛めない持ち上げ方 (20260929_1). All three differ.

### 5.2 聴解: a draw audit (seed 23329961)

**Sources:** official 20 (one archive record, `archive:2018-07:問題5-1`, plus
`archive:2020-12:問題3-3`), soumatome 4, kanzenmoshi 3, shinkanzen 2. All
five preambles differ from 20261002_1's.

| slot | clip | shipped subject | theme | key | 20261002_1 same slot | 20260929_1 same slot |
|---|---|---|---|---|---|---|
| 1-1 | kanzenmoshi:cd1-07 | ゼミの発表の順番、まず研究室へ | 教育 | 1 | テニス合宿の確認 | シンポジウム準備 |
| 1-2 | kanzenmoshi:cd1-08 | レストランのクーポンの会計 | 消費・経済 | 1 2700円 | 喫茶店に忘れた傘 | **same recording, in its 1-4** |
| 1-3 | 2022-07:問題1-3 | パソコンのポスター、比べる図 | 働き方 | 3 | クッキーの企画書 | **same recording** |
| 1-4 | 2022-12:問題1-4 | 金魚のケースが汚れる | スポーツ・余暇 | 4 移動 | 新幹線のチケット変更 | 会計のクーポン |
| 1-5 | 2023-12:問題1-5 | 弱った植物、まず窓際へ | 住まい | 1 置き場所 | 展覧会の照明 | 説明会の封筒 |
| 2-1 | 2023-12:問題2-1 | アナウンサーの司会の進め方 | メディア・情報 | 3 | 林業センターのイベント | パン屋を始めた理由 |
| 2-2 | 2022-12:問題2-2 | 実験協力者の条件（睡眠6時間） | 教育 | 2 | 引っ越しの見積もり | 客が減ったパン屋 |
| 2-3 | soumatome:cd1-46 | 肩の具合 | 医療・福祉 | 1 | 地域の日本語教室 | シャツを編み物に |
| 2-4 | 2023-07:問題2-4 | 着物に夢中になった理由 | 文化・伝統 | 3 | 毎日同じ服 | 引退の理由 |
| 2-5 | 2024-12:問題2-5 | 5000m優勝の勝因 | スポーツ・余暇 | 1 | 工事の日の聞き間違い | 箱の中身は花 |
| 2-6 | soumatome:cd1-30 | 前の会社を辞めた理由 | 働き方 | 2 | 泥祭り | 自転車通勤、腰 |
| 3-1 | soumatome:cd2-28 | 車内販売への不満 | 交通 | 3 | 採用面接で重視すること | 市民グループの発足 |
| 3-2 | 2024-12:問題3-2 | ハチミツの歴史 | 食 | 4 | 鉄道写真家 | 子どものほめ方 |
| 3-3 | archive:2020-12:問題3-3 | アニメの世界的人気 | メディア・情報 | 4 | 留守電のプラン案内 | **same recording** |
| 3-4 | 2023-07:問題3-4 | 新校舎の寄付の依頼 | 教育 | 4 | 介護の負担を減らす技術 | 野菜を増やす食事 |
| 3-5 | 2025-12:問題3-5 | 農業体験会の目的 | 地域活性化 | 2 | 働くことの意義 | 医師確保の対策 |
| 4-1…11 | shinkanzen:cd2-74, 2022-12:4-2, soumatome:cd2-48, kanzenmoshi:cd1-29, 2023-07:4-5, **2024-12:4-6**, 2021-12:4-7, shinkanzen:cd2-75, **2025-07:4-9**, 2025-12:4-10, 2022-07:4-11 | see `shapes` | 働き方 ×5, 人間関係 ×3, 食 ×2, スポーツ・余暇 | 1,3,3,2,1,3,2,1,2,1,3 | — | 4-6 and 4-9 **same recordings** |
| 5-1 | archive:2018-07:問題5-1 | 会議の宿、温泉で安い所 | 旅行・観光 | 2 緑ホテル | 授賞式の出席者 | スポーツクラブ会員 |
| 5-2 | 2025-12:問題5-2 | 4種類の自転車から選ぶ | 消費・経済 | 3 / 2 | 健康イベントの会場 | 自由行動のコース |

**The shipped 聴解 theme tally:**

| theme | count |
|---|---|
| 働き方 | 7 |
| 人間関係 | 3 |
| 教育 | 3 |
| スポーツ・余暇 | 3 |
| 食 | 3 |
| メディア・情報 | 2 |
| 消費・経済 | 2 |
| 住まい, 医療・福祉, 文化・伝統, 交通, 地域活性化, 旅行・観光 | 1 each |

This is a draw audit, so nothing is re-angled.

### 5.3 The reads, one axis at a time

#### MOVE column, read down on its own (読解, 10 essay surfaces, 12 A+B as one)

| MOVE | surfaces | count |
|---|---|---|
| 数えたことの報告 | 10(3), 11(2), 13 | 3 (cap) |
| 機構の説明 | 10(1), 12 | 2 |
| 一人称の前後比較 | 10(4), 11(3) | 2 |
| 反論への応答 | 問題9, 11(4) | 2 |
| 〈想定→実は〉 | 11(1) | 1 |

- **This matches the allocation exactly.**
- **Per-大問 bar:** 問題11 holds 0 機構の説明, against the bar of ≤1.
- **Persona bar:** none of the three counters reads back N年分 of records.
  - 10(3) counts one week.
  - 11(2) counts one drill.
  - 13 counts one season. Its 3年前 is when the narrator moved in, not a
    counted span.
- **No count is set against an expectation.**

**The skeleton read** uses the three-beat rubric: an attributed assumption, an
explicit denial, then 実は Y.

- **Conservative count, 読解: 1**, which is 11(1).
  - The assumption: 「船を動かす人の都合に合わせて時刻をずらしているのだろうと思った」.
  - The denial: 「ところが…実はそうではなかった」.
  - Y is the tide. The deletion test collapses the passage, as allocated.
- **Borderline, not counted:**
  - **11(3).** Inside the after-state: 「上司の話をしていたはずが、本当は今の仕事を続けるかどうか迷っている」.
    That is a はずが→本当は beat about what Mika talked about. It is not the
    passage's skeleton, which is a practice before and after, and no belief of
    the narrator's is denied. Recorded as Q3.
  - **11(4).** The customer's view is conceded (「たしかに…」), then explained
    (「ただ、…」). That is 反論への応答.
  - **問題9.** 「考えが及んでいなかった」 is a concession, not a denial.
  - **12(B).** The foil 「夏の日ざしだけではありません」 is named, not
    attributed.
  - **13.** 「このあたりの古い家ではよくあることだ」 is confirmed, not denied.

#### TEMPLATE column, read down separately

- **Named templates:** 分裂文 1 (10(1)), 相関 1 (11(2)) and
  `A だけではない。B こそが〜` 1 (12(B)). Gate: not-A-but-B 1 of 13.
- **Cap-1 templates (後知れ, 不在の残り, 先回り): none.**
- **相関 appears outside 11(2) only in the body, not in a final:** 10(3)
  「よく書く字ほど、何度も出てくる。」 is in its 2nd paragraph.
- **Every pair the allocation names to read differs:**
  - 10(4) 〈今のNには…ついてくる〉 vs 11(3) 〈今は、Xたら…待つことにしている〉. Both
    are 今 after-states, but one is a state of the poems and the other a habit
    (〜ことにしている). Recorded with Q3.
  - 問題9 〈…ただ、…開けておきたい〉 vs 11(4) 〈そこで、…遅らせました〉. They differ.
  - 10(3) vs 11(2): an unnamed condition skeleton vs 相関.
  - 12(B) vs 13: only 12(B) carries a foil.
  - 10(1) (a cleft) vs 12(A) (a conditional).
  - 12(A) vs 12(B).
- **Cross-paper bar `ok`:** no 問題11 cleft.
- **Unnamed skeletons against 20261002_1, per 大問:** none reused.
- **The 〈介入 → 数字が動いた〉 axis**, the second-axis trap
  `jlpt-test-generation` names. Three surfaces close on an intervention and its
  counted outcome:
  - 10(3): copying by hand → no re-lookups.
  - 11(2): knocking → fewer no-shows.
  - 13: a trickle of water → no frozen mornings. 13 closes on the
    prescription, but its 5th paragraph carries the result.

  All three are the allocated 数えたことの報告 rows, so this is by design, but
  it is one claim family three times. Recorded as Q2.

#### 読解 and 聴解 rows, read as ONE list

- **Decisive numbers:** gate `問題14 shares no decisive number with any 聴解 item`
  is `ok`.
- **Near-shared numbers:** 聴解1-2番 prices dinner at 3000円 per person, and
  its key comes after a coupon with an exclusion: cash only, 3 per coupon,
  key 2700円. 問題14-70 prices a 3,000円 cut after a voucher with an
  exclusion: not usable on the 出張料, key **3,000円**.
  - They share an errand shape (an amount after a discount voucher with an
    exclusion), and the string 3000 appears in both.
  - No number carries from one to the other. Recorded as Q8.
- **12(A)/(B) × 聴解1-4番, the strongest cross-half adjacency:**
  - 12 explains why still water goes green: sunlight plus nutrients, with B's
    nutrients from uneaten bread.
  - 1-4 is a goldfish tank that dirties fast. Its cues are 日当たりの良い部屋
    and the line that leftover feed causes dirt (食べずに残ったものが汚れの原因).
    Its key is relocation; reducing feed is a distractor the dialogue denies.
  - **The mechanism is shared.** 12(B)'s "stop the feeding" message points at
    1-4's wrong option (えさを減らす), not its key.
  - This is a decisive-detail question for QA (Q1). If it is filed, the 読解
    side is re-angled; the 聴解 clip is banked.
- **Domain adjacencies (no shared decisive detail):**
  - 10(2) a school group on a train / 聴解3-1番 車内販売 / 4-2番 a flight.
  - 11(4) a bakery / 聴解4-10番 定食屋 / 4-4番 弁当.
  - 10(4) 俳句 / 聴解2-4番 着物: both traditional practices.
  - 問題14 elderly home visits / 聴解2-3番 a shoulder at the clinic.
  - 11(1) an island trip / 聴解5-1番 a hotel on a business trip.
- **Keyed forms spoken in 聴解:**
  - 4-5番: 「やめるべきじゃなかったんじゃない？」 and the option
    「もっと早くやめるべきだったってこと？」, the 問題9-51 key べきだった.
  - 2-4番: 「そういうわけじゃないんだけど」, the 問題8 `〜わけではない` target.
  - 4-11番: 「優勝できるとは、思わなかったよね」, 問33's own 〜とは、思わなかった
    frame.
  - 4-10番: 「安いわりに」, a 問33 distractor.
  - 4-6番: 「関わらず」.
  - 1-1番: 「ない限りは」.

  聴解 is sat after 言語知識 is collected, so there is no answer leak. Recorded.

#### The cross-half 〈想定→実は〉 cap of 2

- **読解: 1** (11(1)).
- **聴解, counted by the 2026-10-03 orchestrator ruling** (which counted
  20261002_1's 聴解3-2番, a question-presupposition case): **2-4番.**
  - 「着物って高いんだよね？」 is answered 「そんなことないよ」.
  - 「特に古い着物が好きなの？」 is answered 「そういうわけじゃない」.
  - Y is the coordination of 帯 and 小物.
- **Total: 2, at the cap. No re-angle is owed.**
- **聴解, borderline, not counted:**
  - **1-4番:** the friend's suggested causes are each ruled out; that is
    diagnostic elimination, which 20261002_1's stage-3 report did not count
    for the same clip.
  - **5-2番:** proposals are rejected (「遠いんじゃない？」「大丈夫よ」), which is
    the 問題5 format.
  - **2-1番:** 「声や雰囲気っていうよりは」 is a というより preference, not a
    denial.
- **If QA counts any of these, the paper is at 3 and 11(1) must be re-angled.**
  Its legal targets are in the allocation's §"Why 〈想定→実は〉 is at 11(1)":
  機構の説明, 一人称の前後比較 or 反論への応答, never 数えたことの報告.
  Recorded as Q3.

### 5.4 Cross-test reads, 読解 (rows read across the three columns)

No same-seat row repeats a subject (§5.1). The cross-seat and avoid-list
echoes follow. None is a string-visible repeat, and none is stage 3's to
re-author:

- **Q4: 11(4) パン屋 × 20260929_1 聴解2-1番/2-2番 (bakery founder; bakery
  losing customers) and the spec's 食 avoid list.** The avoid list holds that
  2-1 string and a 20260819_1 bakery pickup-date item. It is the same setting
  with a different issue: why loaves rest an hour before sale. Two back.
  Minor.
- **Q5: 11(2) 町内会の地震想定避難訓練.** The 防災 avoid list holds
  20260903_1 問題13 (what drills test) and 20260904_2 聴解1-5番 (drill prep).
  It also holds a 20260914_1 **pre-replacement** 12(A), which never shipped:
  a 町内会 earthquake 見回り訓練 counting four years of records. The allocation
  barred N年分 and 札, and the author complied; this is one drill, counting
  arrivals and no-shows. The setting recurs often in the record, so QA should
  read it against the 20260903_1 row.
- **Q6: 10(5) 図書館の新聞保存 × 20261002_1 問題9 新聞の切り抜き帳.** This is
  the newspaper domain, one paper back, in a different seat. The institution
  (a library's storage policy against a personal scrapbook) and the issue
  differ. The allocation barred clippings and newsletters.
- **Q7: 13 気温の予報を一冬書き写す × 20260929_1 問題13 芝生の上で測る気温.**
  Air temperature, two back, in the same seat. Here the forecast is copied and
  a threshold found; there it is where a thermometer is placed. Both are 説明
  or 主張 on 科学 vs 住まい. The allocation barred a measuring protocol, and
  no instrument is placed. Minor. It is also the same setting as the
  avoid-list 古家の玄関の引き戸 (20260911_1 10(5), a rented old house) with a
  different issue.
- **10(1) 夕焼け × 20261002_1 11(1) 電子レンジ:** both are 科学・技術
  機構の説明 physics, one back. The domains differ (atmospheric optics against
  appliance heating), and the allocation's bar was respected. Minor, not
  filed.
- **問題9 役場窓口 × 20260929_1 11(3) 家族の書類を読み上げる (行政・手続き) and
  20260929_1 10(5) 役場の広報紙:** both two back. The setting is a town hall;
  the issues differ (counter hours against reading aloud and a newsletter).
  Minor.
- **Claim read, within the paper: 問題9 × 11(4).** Both claims are "keep the
  practice for its stated reason, concede the objection's valid part, change
  one thing for the case it hurts". One is a lunch-hour closure kept with a
  phone-booked exception; the other a one-hour rest kept with the bestseller's
  bake moved. The allocation itself asked QA to read the two together. Both
  are 反論への応答 (2, inside the cap) and their skeletons differ, but the
  claim column reads as one move twice. Recorded as Q2.

**問題9's options against the previous two papers:** the gate line
`問題9 blanks reuse no option set` is `ok`.

### 5.5 Errand identity: `shapes` across three papers, by hand

**Clip repeats:**
- **Against 20261002_1:** 0 of 29 in the same slot, and 0 slot-free repeats in
  any slot. No clip appears twice within the paper. The stopped run's
  composer console output is not on record, so I cannot say whether
  `freshest()` printed a dropped bar. The draw itself shows no
  previous-paper repeat, so no bar was dropped in effect.
- **Against 20260929_1 (two back):** **six repeats**. The one-paper bar allows
  every one.

  | this paper | clip | 20260929_1 |
  |---|---|---|
  | 1-1番 | `kanzenmoshi:cd1-07` | its 1-2番 |
  | 1-2番 | `kanzenmoshi:cd1-08` | its 1-4番 |
  | 1-3番 | `2022-07:問題1-3` | its 1-3番 |
  | 3-3番 | `archive:2020-12:問題3-3` | its 3-3番 |
  | 4-6番 | `2024-12:問題4-6` | its 4-6番 |
  | 4-9番 | `2025-07:問題4-9` | its 4-9番 |

  20261002_1 carried three two-back repeats. `make choukai-wear` is under the
  4.0 ceiling in every 大問 (問題1 textbook projection 2.33, 問題2 2.62), so
  the composer is behaving as designed. A learner who sat 20260929_1, though,
  meets 6 of 29 items again one paper later. Re-seeding to escape this would
  be seed-shopping. Recorded as Q9, a process question for the owner: is a
  two-back bar wanted?

**Candidate pairs**, read side by side against the `MUTUALLY_EXCLUSIVE_CLIPS`
standard (same errand, same implicature, same key):

- **Within the paper, 1-4番 × 1-5番** (`2022-12:問題1-4` goldfish tank,
  `2023-12:問題1-5` weak plant). Both key on relocation. **This exact pair was
  judged not errand identity by qa-report-20261002_1 Q8**: different errands
  and disjoint option sets. I follow that ruling, so there is no entry and no
  re-draw.
- **2-6番 (why she quit) × 4-5番 (you shouldn't have quit so easily):** both
  are about quitting a job. The formats (interview reason against
  quick-response) and implicatures differ, and nothing carries. Not identity.
- **Against 20261002_1, by function plus form:**
  - **4-10番 `安いわりに` (evaluation against expectation) × its 4-3番
    `にしては`:** near-synonymous concessive-contrast forms, both answered
    with agreement. Different forms and different keys' functions (an inference
    against an agreement). Minor.
  - **4-7番, relayed praise (`大したもんだ`) × its 4-4番, praise answered
    modestly:** different functions.
  - **5-1番:** a hotel by onsen and price, against its award-ceremony
    attendees.
  - **5-2番:** bicycles, against its health-event rooms.
  - **問題3:** option sets are `ok` (0.067).
- **Against 20260929_1, beyond the six identical clips:**
  - **2-5番:** a winning runner's tactic, against its 2-4番 retiring
    athlete's reason. Both are athlete interviews, in different slots.
  - **2-6番:** a career-step reason, against its 2-1番 bakery founder's
    reason. This is the "reason for a career step" interview again; precedent
    Q7 on 20261002_1 noted the class.

  Neither is identity.

**No re-draw for errand identity, and nothing added to
`MUTUALLY_EXCLUSIVE_CLIPS`.**

## 6. `logs/topics.json`

I appended one row for `20261008_1`. It adds 218 lines, and the other 21
rows are byte-identical: the file was re-dumped with its own indent, and the
re-dump of the pre-run file reproduces it exactly.

It holds:
- `surfaces`, `themes` and `claim` (43 keys each)
- `shapes` (29)
- `closing_moves` (13)
- `voices` and `persona` (14 each)
- `notes`

The row contains **no 「」 span**, and non-paper strings are in backticks.
The gate after the append reads `ok` on:
- `claim per surface`
- `shapes 29/29`
- `0 spans read`
- the closed-vocabulary and rule 1–4 lines

**If C1 or C2 is applied, the row needs re-checking:**
- **C2 (11(4)):** no field quotes the changed clause.
- **C1 (問題14-70's stem):** `surfaces.問題14` describes the flyer, not the
  stem.
- **Keyed forms:** the row's `notes` sentence on the 「とは」 FAIL must be
  updated when C2 lands.

## 7. Keyed-form baseline (問題10–14 incl. options and glosses, as shipped; for the author's re-grep after C1/C2)

| form (item) | count | frame / note |
|---|---|---|
| とは, 問33 bare (?<!こ)とは | 0 | the gate's ×2 is 「ことは」 in 10(3)'s final and in 11(4) (C2). The other 5 「ことは」 are question stems, which the gate does not read |
| ものだ／ものではない (問題7) | 0 | — |
| ものである | 1 | 12(A) 「…植物の栄養になるものである。」 is formal-noun もの + である in 文末, not the 回想 ものだ. The gate is silent. This is the same class as 20261002_1 Q6, reworded there in round 1. Recorded as Q10 |
| てならない, やら, ようではないか, と思うと／と思ったら, にしたら／にすれば／にしてみれば, ございま, はともかく, といった, に即して, に違いない (問題7) | 0 each | — |
| ばかりに, わけではな／わけじゃな, に応じ, に基づ (問題8) | 0 each | — |
| として (問題8) | 0 in prose | the 5 hits are the 問題10–14 instruction lines (「答えとして」), which the gate strips |
| 耳が痛 (48), かといって (49), 休まずに (50), べき (51) | 0 each | — |
| ところが | 1 | 11(1), sentence-initial. Not keyed in this paper (49 keys かといって) |
| こそ, だけでは | 1 each | 12(B)'s final, the allocated not-A-but-B template |
| つもり | 2 | 10(2) email body. The allocation's ban on つもり was for 問題9 prose |

## 8. Content items routed to authors (NOT repaired here)

| id | file / item | gate line | proposed fix | owner |
|---|---|---|---|---|
| **C1** | `_sections/問10-14_読解.md` + `言語知識・読解.md`, 問題14 item 70 stem | FAIL `問題14 shares no run of 20+ characters … 「は、合わせていくらか。円円円円市内に住む」` | 「大川さんが払う金額は、合わせていくらか。」 → 「…、全部でいくらか。」. Simulated: longest shared run 15, line `ok` | 読解 author |
| **C2** | same files, 問題11(4) para. 4 | FAIL `問33「とは」×2` | 「一時間置くことは変えられませんが」 → 「一時間置くのは変えられませんが」. Simulated: line `ok`. Keeps 10(3)'s allocated final and all 27 glosses | 読解 author |

**After both edits, rebuild:** `make assemble 20261008_1` →
`make lint-draft 20261008_1` (ignore its CHOUKAI line) → `make booklet` →
`make sheet` → `make check`. **Never run `make autofix`.**

Then:
- re-grep every keyed form against §7;
- re-read 11(4)'s closing move;
- re-read the MOVE and TEMPLATE columns;
- re-check the `logs/topics.json` row (§6).

Neither edit changes a key, so the scoped second review is not triggered.

## 9. Questions for QA

| id | where | rule | evidence |
|---|---|---|---|
| Q1 | 問題12(A)(B) × 聴解1-4番 | one list across halves; shared decisive detail | Light plus leftover feed makes water dirty or green on both surfaces. 12(B)'s "stop feeding" points at 1-4's denied distractor (§5.3). If filed, the 読解 side is re-angled |
| Q2 | 問題9 × 11(4); 10(3) × 11(2) × 13 | `claim` column read down; the 〈介入→数字が動いた〉 axis | One claim shape twice, "keep the rule, fix the case it hurts" (the allocation asked for this read). Three counted interventions, by allocation (§5.3, §5.4) |
| Q3 | 聴解2-4番 (counted); 1-4番, 5-2番, 2-1番 (not); 11(3)'s はずが→本当は beat | cross-half 〈想定→実は〉 cap | The paper is at 2, the cap. One more counted surface means re-angling 11(1) (§5.3) |
| Q4 | 11(4) パン屋 | avoid list / two-back domain | Bakery setting against 20260929_1 聴解2-1/2-2 and a 食 avoid entry; a different issue |
| Q5 | 11(2) 町内会の避難訓練 | avoid list | A recurrent setting in the record, one drill counted; read against 20260903_1 問題13 |
| Q6 | 10(5) 図書館の新聞 | previous paper, cross-seat | The newspaper domain against 20261002_1 問題9 |
| Q7 | 13 予報の気温 | two back, same seat | Air temperature against 20260929_1 問題13; no instrument placed |
| Q8 | 問題14-70 × 聴解1-2番 | 14 × 聴解 decisive number (gate `ok`) | Both price an amount after a voucher with an exclusion, and 3000 occurs in both. Not carried |
| Q9 | 聴解 1-1, 1-2, 1-3, 3-3, 4-6, 4-9 | draw audit, two back | Six of 29 clips are the same recordings as 20260929_1, allowed. A process question for the owner: is a two-back bar wanted? |
| Q10 | 12(A) 「…ものである。」 | one grammar point, one KEY per paper | A formal-noun もの in 文末 against 問題7-34's ものだ. The gate is silent; a cheap reword exists (`…植物の栄養である。`) |
| Q11 | 問題14 overall | the C1 read | Both papers' 70s use a 500円 add-on. Different documents, rows and deadlines (§4.1) |

## 10. Root-cause row (proposed, NOT applied — gate changes are the owner's call)

| id | defect | class | proposed repair |
|---|---|---|---|
| RC-S3-1 | `check_key_grammar_exposure` counts a keyed option with `prose.count(keyed)`. A two-character key like 「とは」 is therefore matched inside 「ことは」, a different word, and 2 such hits FAIL the paper. Founding case: 20261008_1 問33 (10(3), 11(4)) | GATE-COARSE | For bare-particle keys (とは, には, では …), count only occurrences not preceded by a kana that makes them part of another word (こ+とは), or count after a tokenizer. Measure over all papers before changing (exam-qa-review §6.5). The reword is cheap, so this is low priority, and **the gate is not loosened here** |

## 11. What I skipped, and why

- **The stopped run's steps** (assemble, autofix, lint-draft, verify-scramble,
  mp3, segment, draw audit): not repeated, as instructed. I re-verified the
  segment recovery and the draws row.
- **Fixing C1/C2:** content, which is the author's job. Both fixes are
  proposed and simulated.
- **Stage 5** (`scaffold-explanations`, `model-answer`): prohibited before QA.
  It is FAIL F-C.
- **Stage 4 QA:** not started.
- **`make drill`:** a gitignored build. The global WARN is recorded.
- **Gate and composer changes:** RC-S3-1 is proposed only.
- **Listening to the MP3:** not possible here. The substitutes were the
  5/6/5/11/2 segmentation, the `script_sha` match and a full read of the
  transcript.
- **No commit**, as instructed.
