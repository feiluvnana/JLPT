# Stage 3 (build + gate) — 20261102_1

Run 2026-11-02. This context authored none of the exam items. The files it
wrote by hand are the `logs/topics.json` row, the two 問題9 AUTHOR FILLS cells
in `qa/dokkai-allocation-20261102_1.md` (the 文法 author left them empty), and
this report. Everything else was written by the pipeline commands below.

**Source shas at hand-off** (the build was made from these bytes):

| file | sha256 (12) | sha1 (12) |
|---|---|---|
| `_sections/問1-6_文字語彙.md` | `b77486409931` | `242d6663c4db` |
| `_sections/問7-9_文法.md` | `0b4871c7ac62` | `b9843d6f4d19` |
| `_sections/問10-14_読解.md` | `f31da74654e1` | `a3a9f57a6b54` |
| `test_spec.json` | `0b9cf0e1b7be` | `04077385fda4` |
| `言語知識・読解.md` (assembled) | `f5247817c175` | `38d804de707d` |
| `聴解スクリプト.txt` | `f98e77d1cc88` | `a2b4a179d009` (= chapters `script_sha`) |
| `聴解.md` | `038b57805f3a` | `215002704be0` |
| `聴解.mp3` | `b497e9bae931` (= `logs/upload_manifest.json` `audio/20261102_1.mp3`, 42,903,212 bytes) | `06c47f096302` |

Repo HEAD at start: `e6e7bf0`. A build or repair that finds these moved must
re-run this pass (`jlpt-test-generation` §"One writer per test folder").

## 1. What I read, in full, from disk

- `AGENTS.md`, `CLAUDE.md`
- `.agents/jlpt-test-generation/SKILL.md`, the whole file
- `.agents/exam-app/SKILL.md`, the whole file
- `.agents/choukai-audio/SKILL.md` Part 0, the whole part
- `.agents/exam-blueprint/SKILL.md` §"What still governs a self-authored
  surface" and §"The four theme rules"
- `.agents/question-authoring/SKILL.md` Item integrity #15 (scope of the
  keyed-form rule)
- all three `_sections/` fragments in full; `qa/dokkai-allocation-20261102_1.md`
  in full
- `聴解スクリプト.txt` in full and `聴解.md`'s key table
- `logs/choukai_draws.json` rows for this paper, 20261008_1, 20261002_1
- `logs/topics.json` rows 20261008_1 and 20261002_1 (surfaces, themes,
  closing_moves, persona, claim, shapes, notes), and every earlier row's tags
  for each clip this paper drew
- `qa/stage3-report-20261008_1.md` (format model; its 〈想定→実は〉 counting
  under the 2026-10-03 ruling)

## 2. Commands, in order, with exit status

```
gh auth status                                   # feiluvnana active
make assemble 20261102_1                         # 0 — N2 layout
make autofix 20261102_1                          # 0 — ALL CHECKS CLEAN (nothing changed); run BEFORE make mp3
make lint-draft 20261102_1                       # 0 — ALL CHECKS CLEAN
make verify-scramble 20261102_1                  # 0 — 43–47: keyed ★ survives, 解説 last-slot proof ok, 1 free unit each; UNDECIDED (the tool's ceiling, not a failure)
make mp3 20261102_1 SEED=28944768                # 0 — 44.7 min, 34 chapters; no dropped/soft bar printed
python3 tools/choukai_segment.py tests/20261102_1/聴解.mp3   # ok 5/6/5/11/2, LUFS -15.28
make upload-files TARGET=tests TEST=20261102_1   # 0 — 20261102_1.mp3 (42.9 MB) uploaded to release 'audio'; manifest updated
make booklet 20261102_1                          # 0 — both booklets
make sheet 20261102_1                            # 0 — 解答.html + 練習.html, 101 items (71 without 詳細解説 yet: stage 5)
make check                                       # 2 — run 1 (before the topics row): 1 FAIL
(logs/topics.json row appended)
make check                                       # 2 — run 2: 1 FAIL (same), 242 WARN (+2, both from the new row)
(notes field edited to list those two WARNs)
make check                                       # 2 — run 3 (final): identical to run 2 — 1 FAIL, 242 WARN, 6372 ok
```

`make autofix` was NOT run after `make mp3`.

## 3. 聴解 compose and draw audit

- Source mix: official ×20, kanzenmoshi ×3, shinkanzen ×2, soumatome ×2,
  mimikara ×1, mondaireishuu ×1. Drew from 8 sittings.
- Segment recovery: **5/6/5/11/2**.
- **vs 20261008_1 (previous):** 0 clip ids repeat in the same slot; 0 slot-free
  clips repeat in any slot; 0 ids in common at all.
- **vs 20261002_1 (two back, soft bar):** 0 same-slot repeats, 0 slot-free
  repeats. The composer printed no "soft bar dropped" line, consistent with 0.
- No clip appears twice inside the paper.
- `check_choukai_option_set_reuse`: worst 問題3 Jaccard vs 20261008_1 = 0.067
  (ceiling 0.30).

## 4. Gate (`make check`)

Final run (run 2, after the `logs/topics.json` row): `FAILED — 1 problem(s)`,
with 6372 ok, 242 WARN, 10 note, 265 skip. Run 1 (before the row) had the
same FAIL and 240 WARN; the two added WARNs are W4/W5 below, both produced by
the new row. (Totals are true for this run only; they move with any test on
disk.)

### 4.1 FAIL (names this paper)

| id | line | class | disposition |
|---|---|---|---|
| F-A | `詳細解説.json explains every keyed item (30 entries for 101 keys)` | structural | **Stage 5.** `make mp3` wrote the 30 聴解 entries; the 71 言語知識・読解 entries are prohibited before QA passes. Same as 20261008_1 F-C |

### 4.2 Every WARN naming this paper, with disposition

| id | line | disposition |
|---|---|---|
| W1 | `20261102_1: the 問題8 form-family check compares most of the draw (1/5 = 20% family-tagged)` | Pool-map coverage, not this paper's content: 4 of 5 drawn 問題8 entries carry no `grammar_form_families` tag. Read by hand: the five 問題8 forms (つつ, たびに, において, をきっかけに, ほど〜はない) share no family with each other or with the twelve 問題7 keys; the pool-level candidate pair 「〜つつも」+「経過状況(〜つつ…する)」 is not drawn here (問題7 draws no つつも). The repair is a pools.json tagging pass, not this paper. Deferred to the pool owner; not a QA blocker |
| W2 | `every stamped spec's pools_sha matches pools.json (cf187cf62829)` | Suite-wide record (names every test). This paper was stamped on its reroll, so the sha certifies the redraw's pool. Expected; not a defect |
| W3 | `20261102_1: 問題1/2 question repeats match in PUNCTUATION too — 問題2-3番` | Composed-half transcription noise inherited from the source script (「、」 placement in the head/tail question). The audio is identical; the line says it never blocks. Not a defect |
| W4 | `20261102_1 問題9: the shipped prose uses a 「スポーツ・余暇」 word` | The tag is honest: the cloze is about indoor climbing (クライミング場, 登る, コース, 突起), which is スポーツ・余暇, but none of the 11 representative tokens (スポーツ, 練習, 趣味, 運動, …) occurs. This is NOT the F1 shape: there is no truer tag to move to (rule-4 is clean under any sports/leisure reading, and no other theme fits). THEME_TOKENS must not be widened for a live paper. **Optional C2 for the 文法 author** (below): one word such as 「趣味で」 in paragraph 1 would give the record lexical support. Otherwise false positive; deferred to QA with this reason |
| W5 | `20261102_1: no 聴解 slot repeats its own theme in the previous 2 papers — 聴解問題3-1番=交通 (also 20261008_1)` | Composed half (draw audit). Read side by side: 20261008_1 3-1番 is a complaint about on-board sales announcements; this 3-1番 is a man's view of car design (cars as cool objects vs boxes). Shared domain tag, different subject, no decisive detail. Nothing to re-angle; recorded |

No other WARN names 20261102_1. Skips naming it: errand-key checks (no keyed
draws — the topic pass covers it), 問題7 form-family (0 tagged), the 問題5
imported-shape lines, セクション構成表 (none in a composed paper), and the
詳細解説 placeholder check (stage 5).

## 5. Keyed-form re-grep, 読解 half (問題10–14 body + （注N） glosses, key table excluded)

Forms verified against `_sections/問7-9_文法.md` (authoritative). Patterns
included kana/kanji variants (抜き/ぬき, 関わ/かかわ, 初め/はじめ, たび, にお
いて/における, ほど…はない).

| 大問 | keyed form | count | frame / disposition |
|---|---|---|---|
| 問題7-31 | 存じております (存じ) | 0 | — |
| 問題7-32 | たとたん | 0 | — |
| 問題7-33 | ことになっている | 0 | — |
| 問題7-34 | ご覧いただけます | 0 | — |
| 問題7-35 | ないものか | 0 | — |
| 問題7-36 | (は)ぬきにして | 0 | — |
| 問題7-37 | にかかわらず | 0 | — |
| 問題7-38 | ことか | 1 | 問題13 item 68 stem 「…とあるが、どういうことか。」 — 文末, interrogative どういう＋こと＋か, the standard 傍線部 question frame, NOT the exclamatory 〜ことか. Not a finding |
| 問題7-39 | (て)はじめて | 0 | — |
| 問題7-40 | (信じ)がたい | 0 | (ありがたい also 0) |
| 問題7-41 | あげく | 0 | — |
| 問題7-42 | ないことには | 0 | — |
| 問題8-43 | つつ | 0 | — |
| 問題8-44 | たびに | 0 | — |
| 問題8-45 | において | 0 | — |
| 問題8-46 | をきっかけに | 0 | — |
| 問題8-47 | ほど〜はない | 0 | (「十分ほど」「三日ほど」 are quantity ほど, no comparative) |
| 問題9-48 | ところ | 0 | 「所」 ×2 as a place noun (10(5) 「気にならなかった所で」, 11(4) 「届く所」); not the 「というところで」 frame |
| 問題9-49 | 〜のは…からだ | 0 | — (「からだ」 0) |
| 問題9-50 | そのため | **1** | **問題14 item 71 stem: 「そのために、山田さんは何をする必要があるか。」 — 文頭, 連用 (目的 「そのために」).** Sentence-initial use counts under the brief / qa-report-20261002_1 F10. The sense is purpose, not 問題9-50's 因果, but the surface string is 問題9-50's keyed connector opening a sentence. **Routed to the 読解 author (C1 below)** |
| 問題9-51 | その日の後半に | 0 | (後半/前半 0) |

## 6. Content items for the section authors (not fixed here)

| id | file / line | check | message | proposed fix | owner |
|---|---|---|---|---|---|
| **C1** | `_sections/問10-14_読解.md` line 287 (merged `言語知識・読解.md`, 問題14 item 71 stem) | Stage-3 keyed-form re-grep (not a gate line) | 問題9-50's keyed 「そのため」 opens a sentence in printed 読解 text: 「そのために、山田さんは何をする必要があるか。」 | e.g. 「ベビーカーを出すために、山田さんは何をする必要があるか。」 or 「山田さんは、何をする必要があるか。」. Then assemble → lint-draft → booklet → sheet (NOT autofix) and re-grep | 読解 author |
| **C2 (optional)** | `_sections/問7-9_文法.md` line 71 (問題9 paragraph 1) | WARN W4 `問題9: the shipped prose uses a 「スポーツ・余暇」 word` | no representative theme word in the cloze prose | e.g. 「三年前から、週に二回、仕事帰りに趣味で駅前の…」; any edit to 問題9 re-runs assemble → lint-draft → booklet → sheet and the keyed-form re-grep. Leaving it is defensible (the tag is honest) | 文法 author |

No other substantive content issue was found at stage 3. No mechanical edit
was made to any fragment.

## 7. Whole-paper topic pass (§"One topic, one surface")

### 7.1 The table

Themes are read from the SHIPPED surfaces. "Draw" is the spec `theme`
(subjects are authored, `origin: authored`). Prev = 20261008_1, two back =
20261002_1, both from `logs/topics.json`.

| surface | this paper: subject (shipped) | theme | on its draw? | closing shape / final template | MOVE | persona | 20261008_1 same seat | 20261002_1 same seat |
|---|---|---|---|---|---|---|---|---|
| 問題9 | indoor climbing: days that start on the hardest course had more first-try completions (one month, 9 visits) | スポーツ・余暇 | yes (author-composed, RNG) | 条件提示 / 相関 with では | 数えたことの報告 | 趣味の実践者 | 行政・手続き 役場窓口の昼休み (反論応答) | メディア・情報 新聞の切り抜き帳 (随筆, 趣味の実践者) |
| 10(1) | why ice is slippery: a never-fully-frozen surface layer, thinner with cold | 科学・技術 | yes | 意外な観察 / unnamed (雪国では…用心するそうだ) | 〈想定→実は〉 | 研究者 | **科学・技術** 夕焼けが赤い理由 (説明) | 子育て・家族 児童館 notice |
| 10(2) | thickened drinks (とろみ) and the slowed epiglottis, care home | 医療・福祉 | yes | 説明 / unnamed | 機構の説明 | 職業人 | 交通 校外学習 rail email | **医療・福祉** 病院の案内図 (意外な観察) |
| 10(3) | notice: deadline mail in orange envelopes from 4/1 | 行政・手続き | yes | 実用文 | （実用文） | 市（通知） | デジタル化 字を調べる | 住まい 収納 |
| 10(4) | email: print shop asks for original photo files, pasted photos shrink | デジタル化 | yes | 実用文 | （実用文） | 実務者 | 文化・伝統 俳句 | 環境 インク容器 email (printing supplies) |
| 10(5) | editor reads drafts aloud; red lines now split overlong sentences | 働き方 | yes | 随筆 / unnamed | 一人称の前後比較 | 職業人 | メディア・情報 library notice | デジタル化 写真の自動保存 |
| 11(1) | 和傘 craftsman keeps 48 ribs despite the weight complaint | 文化・伝統 | yes | 反論応答 / unnamed | 反論への応答 「理由を示して変えない」 | 職人 | 旅行・観光 島の船の時刻 | 科学・技術 電子レンジ |
| 11(2) | how a disaster helmet works (shell / strap gap / liner) | 防災 | yes | 説明 / unnamed | 機構の説明 | 解説者 | **防災** 避難訓練の声かけ (条件提示) | 文化・伝統 かるた |
| 11(3) | lent items come back unprompted when the borrower names the return day (6 weeks, 12 cases) | 人間関係 | yes | 条件提示 / unnamed (〜れば) | 数えたことの報告 | 観察者 | **人間関係** 友人の相談 (随筆) | 食 だし |
| 11(4) | dorm student moves one alarm across the room | 睡眠・健康 | yes | 随筆 / unnamed | 一人称の前後比較 | 学生 | 食 パンを一時間置く (反論応答) | スポーツ・余暇 山の下り |
| 12(A) | bus on-board falls happen when riders walk at the stop instant | 交通 | yes | 主張 / `A わけではない` | 反論への応答 (A+B one) | 論者 | 環境 池の水が緑 | 消費・経済 まとめ買い |
| 12(B) | a rider now stands only after the stop, prepares seated | 交通 | yes | 反論応答 / unnamed | ″ 「譲歩して一部を変える」 | 利用者 | 環境 池にパン | 消費・経済 先払い |
| 13 | sharpening the knife stopped onion tears (cells not crushed) | 食 | yes | 意外な観察 / unnamed | 一人称の前後比較 | 趣味の実践者 | 住まい 水道凍結 | 人間関係 幹事 |
| 14 | 子育てひろば hand-me-down exchange: tickets, 50円 over-ticket, big items by phone | 子育て・家族 | yes | (flyer) | （実用文） | 子育てひろば（案内） | 医療・福祉 訪問理容 | 防災 消火器 |

聴解 rows (all composed; DRAW audit, not topic audit — nothing here can be
re-angled). Full surfaces/shapes are in the `logs/topics.json` row.

| item | subject | theme | 〈想定→実は〉? | clip |
|---|---|---|---|---|
| 1-1 | choir concert prep, she takes the poster draft | スポーツ・余暇 | no | 2024-12:問題1-1 |
| 1-2 | homework after absence: the board outside the lab | 教育 | no | mondaireishuu:問1-1 |
| 1-3 | volunteer tutoring: first contact the city's 国際課 | 教育 | no | 2024-12:問題1-3 |
| 1-4 | café lighting design: change material glass → 和紙 | 働き方 | no | 2023-07:問題1-4 |
| 1-5 | phone-shop voicemail: bring the loaner phone in | 消費・経済 | no | soumatome:cd1-60 |
| 2-1 | interview nerves: new advice is to smile | 働き方 | no | 2022-07:問題2-1 |
| 2-2 | athlete's retirement: mental limit, not medal/injury | スポーツ・余暇 | **borderline** (host's guess partly conceded, not denied) | kanzenmoshi:cd1-11 |
| 2-3 | old shirts cut into yarn for knitting | 環境 | no | 2023-12:問題2-3 |
| 2-4 | senior chose her firm for work-from-home days | 働き方 | no | 2025-12:問題2-4 |
| 2-5 | medicine worry: past nausea from the same cough syrup | 医療・福祉 | no | kanzenmoshi:cd1-14 |
| 2-6 | study session: the start time was the bad point | 教育 | **borderline, closest case** (partner's worries denied 「そんなことなかったよ」, then the real problem) | 2024-12:問題2-6 |
| 3-1 | cars: to him still a cool thing, not a box | 交通 | no | soumatome:cd1-33 |
| 3-2 | retiree: planned fishing, found housework rewarding | 住まい | **YES** (「思ってたんです。ところが」→ 家事) | 2021-07:問題3-2 |
| 3-3 | designer: how design first interested him | 文化・伝統 | no | 2024-07:問題3-3 |
| 3-4 | how plants' seeds are carried | 環境 | no | 2021-07:問題3-4 |
| 3-5 | crow calls carry meaning | 科学・技術 | **borderline** (attributed view, no explicit denial) | 2023-07:問題3-5 |
| 4-1 … 4-11 | quick responses (see row) | 働き方×4, 人間関係×2, 教育, 旅行・観光×2, メディア・情報, 食 | n/a | — |
| 5-1 | park litter: repaint the benches | 地域活性化 | no (問題5 elimination format) | 2024-07:問題5-1 |
| 5-2 | summer science events: 南大学 / ちゅうおう図書館 | 科学・技術 | no | 2021-07:問題5-2 |

### 7.2 Reads and findings

**Four theme rules (counts).**
- Rule 1: headlines 問題9 スポーツ・余暇, 問題12 交通, 問題13 食, 問題14 子育て・家族,
  聴解問題5 地域活性化 + 科学・技術 — distinct.
- Rule 2 (lenient, the four 読解 headlines only): none of the four appears in
  another 読解 surface. 聴解5-2 科学・技術 also tags 10(1), which rule 2's
  2026-09-03 reading permits.
- Rule 3: all 13 読解 themes distinct (13 of 13).
- Rule 4: no 読解 headline repeats 20261008_1 (行政・手続き/環境/住まい/医療・福祉)
  or 20261002_1 (メディア・情報/消費・経済/人間関係/防災). 聴解問題5 地域活性化 /
  科学・技術 headline neither previous paper. (5-1 is tagged 地域活性化, the tag
  20260910_1 gave the same recording; it would also read as 環境, which
  headlined 20261008_1's 問題12 — composed half, WARN-only either way.)

**Each surface against its own draw.** All 13 読解 surfaces sit on their
drawn theme and match the allocation's subject/shape/template/MOVE row; every
allocation final sentence occurs verbatim in the merged paper (checked by
script).

**Rows read across the three columns (same seat).**
- **T1 (minor, sampler-level): three seats carry the same theme as 20261008_1's
  same seat** — 10(1) 科学・技術, 11(2) 防災, 11(3) 人間関係 — and 10(2)
  医療・福祉 matches 20261002_1's 10(2). The subjects, domains and MOVEs differ
  in every case (ice-surface physics vs sky optics; helmet mechanism vs
  evacuation-drill count; lending vs listening to a friend; swallowing
  mechanism vs hospital wayfinding), and the allocation checked the
  (seat, theme, MOVE) triples. Not a repeat of topic; noted so the seat/theme
  pairing does not become a crutch. Root cause is in the theme-to-seat draw,
  not the authoring.
- **T2 (moderate, claim-level — question for the orchestrator/QA):
  11(1) and 20261008_1 11(4) run one claim on different subjects, in the same
  大問, one paper apart.** 20261008_1 11(4): a baker concedes the customer's
  complaint (aroma lost), explains the reason (shape, the customer cuts at
  home), shows a physical comparison (cut faces) and keeps the practice. This
  paper's 11(1): a 和傘 maker concedes the customer's complaint (weight; tried
  it himself), explains the reason (wet 和紙 tears between wide ribs), shows a
  physical exhibit (the torn 30-rib umbrella) and keeps the practice. Seat
  differs (11(4)→11(1)) so the seat bar passes, and the allocation's
  claim-family list did not name this family for 11(1). If judged one claim,
  the repair is a 読解 re-angle of 11(1)'s resolution (it is the allocated
  「理由を示して変えない」, so the allocation row changes too), e.g. drop the
  demonstration-to-the-customer beat or move to a resolution that is not a
  shop keeping its practice against a customer.
- **T3 (minor, two back):** 10(4)'s email (print shop ↔ choir) shares the
  printing/supplies domain with 20261002_1 10(4) (office ↔ supplier, copier ink
  containers). Different errand; noted.
- **T4 (minor, two back):** 13 (home cooking hobbyist, knife sharpening) shares
  the home-cooking domain with 20261002_1 11(3) (home dashi vs powder). Noted.
- **T5 (minor):** 11(3) and 20261008_1 10(3) both run 〈keep a notebook for N
  weeks → count → split into two groups → the condition that differs〉. The
  claims differ (borrower names the date vs writing a kanji once stops a
  re-look-up), and 11(3) does not report that the note prevented a repeat
  (the allocation's bar). Noted for the MOVE/template read.
- 問題12 cross-test column: 交通 bus falls vs 環境 pond vs 消費・経済 bulk buying — no
  relation.

**Within this paper, 読解 ↔ 聴解 as one list.**
- **T6 (minor, domain only):** 問題14 (exchange of outgrown children's clothes)
  and 聴解問題2-3番 (re-using old shirts; 知り合いにゆずる is a distractor) share
  the clothing-reuse domain. No decisive detail (number, condition) can be
  carried between them; the 聴解 item was not chosen here. Per §"A 読解 passage
  may share a domain with a 聴解 item", not a finding; recorded in case QA reads
  it as one topic (then 問題14 is the side re-angled).
- 11(1) 和紙 umbrella and 聴解1-4 (lighting material changed to 和紙): shared
  word, not a decisive detail (11(1) does not bear on 1-4's key). Not a finding.
- 10(2) care home and 聴解2-5 (medicine worry): medical domain only.
- No other 読解 subject recurs in 聴解.

**Within the 読解 half.** 問題9 (own climbing log, one month) and 11(3) (own
lending log, six weeks) are the two allocated 数えたことの報告 rows; they differ in
what was counted, what it showed, persona and final template (相関 では vs
〜れば), as the allocation requires.

**MOVE column, read down the skeleton.** Deletion test on every row except
10(1): no other 読解 row carries attributed assumption → denial → 実は Y.
Closest: 12(B) (her old practice of standing early is replaced after hearing
about the stop jolt — a practice update, the allocated 「譲歩して一部を変える」,
no belief denied), 13 (window/fan tried and failed — no belief stated). 

**TEMPLATE column, read separately.** Named: 相関 1 (問題9), `A わけではない` 1
(12(A)); 分裂文 0; not-A-but-B family 1 (12(A)); no 後知れ/不在/先回り final.
The gate's `check_dokkai_template_repeat_prev_paper` is ok. Unnamed pairs at
risk (10(5)/11(4), 11(1)/12(B), 10(1)/13, 10(2)/11(2)) end on different
skeletons: 赤線が…線になった / 頭は…起きている; 作り続けてまいります / 降車口へ向かいます;
…用心するそうだ / …残らなくなっている; …調整しています / …守れない.

**〈想定→実は〉 cap of 2 across both halves.**
- 読解: **1** (10(1), allocated).
- 聴解, counted: **3-2番** (own plan to fish → ところが → housework).
- **Total 2, at the cap.**
- **Q1 (question for the orchestrator):** 聴解問題2-6番 is the nearest case to
  the 2026-10-03 ruling that counted 20261008_1's 聴解2-4番: the woman's two
  worries (more lecturers? the room too big?) are each explicitly denied
  (「いや」「そんなことなかったよ」), then the real bad point is given. I read it
  as 問題2's elimination format (as 20261008_1's stage 3 read its 1-4番) and do
  not count it; 2-2番 (host's medal guess met with 「それもそうなんですが」, a
  concession) and 3-5番 (crows thought a nuisance, no explicit denial) are
  borderline and not counted. **If 2-6番 is counted, the paper is at 3 and 10(1)
  must be re-angled** to its allocation's legal targets (機構の説明 → 問題10 would
  hold it twice, or 反論への応答); never 一人称の前後比較 (at cap 3).

**聴解 errand identity (shapes across three papers).**
- No clip-id repeat (§3).
- 1-4番 (boss reviews a design, praises most, one element to change) runs the
  same errand genre as 20261008_1 1-3番 (poster) and 20261002_1 1-3番 (cookie
  box). Different clips, products and changed element; this is a standard
  official 問題1 genre, not one item heard twice. Not proposed for
  `MUTUALLY_EXCLUSIVE_CLIPS`.
- 1-1番 (choir prep: pick own task among the remaining) vs 20261002_1 1-1番
  (tennis camp: pick own task) — two back, same genre, different errands. Noted.
- 2-1番 (interview advice) and 2-4番 (company choice) are two 就職 items in one
  paper; 20261008_1 2-6番 and 20261002_1 3-1番 also ran interviews. Domain only.
- No pair judged one item.

**Keyed grammar spoken in the composed 聴解 (observation, no repair made).**
- **Q2:** 聴解問題4-9番's key turns on 〜つつ (逆接 「知りつつ…やめられない」) and
  4-4番 speaks 〜つつある, while 問題8-43 keys 〜つつ (同時). 聴解問題4-8番's three
  options are 拝見しました／ご覧くださいました／お見えになりました — the 敬語 set
  問題7-34 prints (拝見できます／お見えになります／ご覧いただけます). Item integrity
  #15 ("one grammar point may be the KEY only once per paper") does not say
  whether a composed 聴解 key counts; 聴解 is sat after 言語知識 is collected, so
  there is no answer leak, and 20261008_1's stage 3 recorded the same class
  without repair. The only lever is a fresh SEED (whole-half re-draw) before QA;
  I did not seed-shop. **Root-cause row proposed:** `compose_choukai.py` draws
  blind to the paper's keyed 問題7/8 forms; a penalty (not a ban) on 問題4 clips
  whose key turns on a form keyed in 問題7/8 would remove the class without
  seed-shopping.

## 8. Allocation file

The two 問題9 AUTHOR FILLS cells were empty; filled from the fragment (final
sentence verified verbatim; subject, 条件提示 / 相関 with では / 数えたことの報告,
persona 趣味の実践者, and which 20261008_1 claims it is not).

## 9. `logs/topics.json`

Row `20261102_1` appended (`surfaces` 43, `themes`, `shapes` 29,
`closing_moves` 13, `voices` 14, `persona` 14, `claim` 43, `notes`). Notes
record that 問題9's 16 options were compared against the previous two papers'
問題9 options with zero repeats (measured by the 文法 author), the keyed-form
grep result, the draw audit, the 〈想定→実は〉 count with the open Q1, and the
cross-half observations. No repo-wide number is pinned. 「」 is used in the row
only for strings in the paper.

## 10. Skipped, and why

- `make model-answer` / 詳細解説 (the one FAIL): stage 5, prohibited before QA.
- No 聴解 re-draw: no clip repeat, no dropped bar; Q1/Q2 are decisions for the
  orchestrator, not seed-shopping.
- C1 not edited: it is an item-stem rewording, routed to the 読解 author.

## Orchestrator dispositions (2026-11-02), before QA

| item | disposition |
|---|---|
| C1 item 71 stem 「そのために」 | **Fixed** by the 読解 author: 「ベビーカーを出すために、山田さんは何をする必要があるか。」. Re-grep over 問題10–14: 9-50 そのため 0. |
| C2 / W4 問題9 no スポーツ・余暇 word | **Fixed** by the 文法 author: 「三年前から、趣味で、週に二回、…」. W4 no longer fires. |
| T2 11(1) repeats 20261008_1 11(4)'s claim | **Re-angled** by the 読解 author onto 「反論の前提を問い直す」: new subject 和ろうそく (was 和傘); keys 57=2, 58=2 unchanged; allocation row + logs/topics.json 11(1) surface/claim re-recorded. Pre-QA, so QA reads it in its single round. |
| Q1 聴解2-6番 and 〈想定→実は〉 | **Not counted** (a denied worry in a 問題2 dialogue, not an attributed belief + 実は Y). The paper stays at 2 (10(1), 聴解3-2番). QA may overrule. |
| Q2 keyed grammar spoken in 聴解 (4-9 つつ, 4-8 敬語 set) | **No re-draw.** No answer leaks, since 聴解 is sat after 言語知識. Carried to QA as a root-cause proposal (composer unaware of 問題7/8 keys). |

Rebuilt assemble → lint-draft → booklet → sheet (no autofix after compose). `言語知識・読解.md` sha now 3cd5ebc15c58. `make check`: the only FAIL is the stage-5 詳細解説 coverage line. WARNs naming this test: W1 (問題8 family tags), W2 (pools_sha record), W3 (2-3番 punctuation), W5 (3-1番 交通 theme) — dispositions as above in this report.
