# Stage 3 (build + gate) — 20261102_2

Run 2026-11-02. This context authored none of the exam items. The only things
it wrote by hand are the `logs/topics.json` row and this report. The pipeline
commands below wrote everything else. No fragment was edited, and the
allocation file was not touched (both authors had filled their AUTHOR FILLS
cells).

**Source shas at hand-off** (the build was made from these bytes):

| file | sha256 (12) | sha1 (12) |
|---|---|---|
| `_sections/問1-6_文字語彙.md` | `e8a5ae40b231` | `e13b3e428f87` |
| `_sections/問7-9_文法.md` | `7e5960a99e1c` | `3bc83fad4ec9` |
| `_sections/問10-14_読解.md` | `6422ab026ae4` | `91673b72db6e` |
| `test_spec.json` | `01236b460eba` | `c5df6c43545a` |
| `言語知識・読解.md` (assembled) | `27825d85c6f7` | `9ef3eb1a028c` |
| `聴解スクリプト.txt` | `833e87c67c9e` | `04f2f9dcff6f` (= chapters `script_sha`) |
| `聴解.md` | `0d7b5334da95` | `b3f27a901759` |
| `聴解.mp3` | `88d42e6716c5` (= `logs/upload_manifest.json` `audio/20261102_2.mp3`, 44,775,596 bytes) | `9c94a3ade16c` |

Repo HEAD at start: `aa025ac`. If a later build or repair finds these shas
changed, it must re-run this pass (`jlpt-test-generation` §"One writer per
test folder").

## 1. What I read, in full, from disk

- `AGENTS.md` and `CLAUDE.md`.
- `.agents/jlpt-test-generation/SKILL.md` (the whole file).
- `.agents/exam-app/SKILL.md` (the whole file).
- `.agents/choukai-audio/SKILL.md` Part 0 (the whole part).
- `.agents/exam-blueprint/SKILL.md`: §"Topic themes" through §"The four theme
  rules" (incl. rules 4b/4c/5), and §"What still governs a self-authored
  surface".
- `qa/stage3-report-20261102_1.md` (precedent for this report's format).
- `qa/dokkai-allocation-20261102_2.md` and `qa/blueprint-rerolls-20261102_2.md`.
  I read the reroll note's 問題12 section, which is the part this pass uses.
- The `問7-9_文法.md` and `問10-14_読解.md` fragments in full. Of
  `問1-6_文字語彙.md` I read only its gate and lint lines: no topic-table
  surface or keyed form lives in it.
- `聴解スクリプト.txt` in full and `聴解.md`'s options and key table.
- From `logs/choukai_draws.json`: the rows for this paper, 20261102_1 and
  20261008_1, plus every earlier row that drew one of this paper's clips (to
  see how those clips were tagged before).
- From `logs/topics.json`: the full 20261102_1 and 20261008_1 rows.
- From `tools/`: `compose_choukai.py` (`previous_slot_clips`, `two_back_clips`,
  `MUTUALLY_EXCLUSIVE_CLIPS`) and `check_consistency.py`
  (`check_choukai_script_reads`, plus `check_key_grammar_exposure`'s messages).

## 2. Commands, in order, with exit status

```
gh auth status                                   # feiluvnana active (release write)
make assemble 20261102_2                         # 0 — N2 layout
make autofix 20261102_2                          # 0 — ALL CHECKS CLEAN (nothing changed); run BEFORE make mp3
make lint-draft 20261102_2                       # 0 — ALL CHECKS CLEAN
make verify-scramble 20261102_2                  # 0 — 43–47: keyed ★ survives, 解説 last-slot proof ok, FREE UNITS 1 each; UNDECIDED (the tool's ceiling, not a failure)
make mp3 20261102_2 SEED=14231493                # 0 — 46.6 min, 34 chapters; no dropped / soft-bar line printed
python3 tools/choukai_segment.py tests/20261102_2/聴解.mp3   # ok 5/6/5/11/2, LUFS -15.59
make upload-files TARGET=tests TEST=20261102_2   # 0 — 20261102_2.mp3 (44.8 MB) to release 'audio'; manifest updated
make booklet 20261102_2                          # 0 — both booklets
make sheet 20261102_2                            # 0 — 解答.html + 練習.html, 101 items (71 without 詳細解説 yet: stage 5)
make check                                       # 2 — run 1 (before the topics row): 1 FAIL, 244 WARN
(logs/topics.json row appended)
make check                                       # 2 — run 2: same FAIL, 245 WARN (+1, W5, from the new row)
(notes field: voice counts changed to the gate's numbers; gate gap named)
make check                                       # 2 — run 3 (final): WARN/FAIL set identical to run 2 — 1 FAIL, 245 WARN, 11 note, 6602 ok, 273 skip
```

Seed `14231493` was the orchestrator's RNG output. It had 0 hits in
`logs/choukai_draws.json` and `logs/ledger.json` before the draw, and I used
it verbatim. `make autofix` was **not** run after `make mp3`. The compose also
printed its standard exclusion notes: 4 figure items, and 6
`UPSTREAM_DEFECT_CLIPS`, including `soumatome:cd1-60` from qa-report-20261102_1
F5.

## 3. 聴解 compose and draw audit

- **Source mix:** official ×20 (two of them archive clips, `archive:2020-12:問題3-4`
  and `archive:2020-12:問題5-1`), kanzenmoshi ×5, shinkanzen ×2, soumatome ×2.
  Drawn from 11 sittings.
- **Segment recovery:** **5/6/5/11/2**.
- **vs 20261102_1 (previous paper):** 0 same-slot repeats, 0 slot-free clips in
  any slot, 0 clip ids in common.
- **vs 20261008_1 (two back, soft bar):** 0 same-slot repeats, 0 slot-free
  repeats, 0 ids in common. The composer printed no "soft bar dropped" line,
  which matches the 0.
- **Composer's notion of "previous":** it picks the previous paper by test id,
  not by row order. The history's last row before this one is a replay of
  `20260904_2`, and the composer correctly took 20261102_1 and 20261008_1.
- No clip appears twice inside the paper.
- `check_choukai_option_set_reuse`: the worst 問題3 Jaccard against 20261102_1
  is 0.111 (ceiling 0.30).

## 4. Gate (`make check`)

The final run (run 3) reads `FAILED — 1 problem(s)`, with 6602 ok, 245 WARN,
11 note and 273 skip. These totals are true for this run only and move with
any test on disk.

### 4.1 FAIL (names this paper)

| id | line | disposition |
|---|---|---|
| F-A | `詳細解説.json explains every keyed item (30 entries for 101 keys)` | **Stage 5.** `make mp3` wrote the 30 聴解 entries. The 71 言語知識・読解 entries are prohibited before QA passes. Same as 20261102_1 F-A |

### 4.2 Every WARN naming this paper, with disposition

| id | line | disposition |
|---|---|---|
| W1 | `20261102_2: every drawn 聴解 clip carries a QA script-read record (29 of 29 unread)` | **Deferred to stage 4. This is QA's own work item.** `check_choukai_script_reads` (qa-report-20261102_1 RC-5) WARNs until `exam-qa-review` §4 check 6 reads each drawn clip as Japanese and writes one `logs/choukai_script_reads.json` row per clip. No other context can clear it honestly |
| W2 | `every stamped spec's pools_sha matches pools.json (cf187cf62829)` | Suite-wide record that names every test. This paper's spec was stamped against the current pool. Expected; not a defect |
| W3 | `drill/N2: pages match the data they bake — … 4 source(s) not in the build (['tests/20261102_2/聴解_チャプター.json', 'tests/20261102_2/言語知識・読解.md', 'tests/20261102_2/詳細解説.json'])` | **Deferred to after stage 5.** `drill/` is gitignored build output (`jlpt-drill`). Two of this paper's sources are still moving: 詳細解説.json is completed at stage 5, and the paper text changes with any QA fix. A `make drill` now would go stale again at the next fix. Run `make drill` (or `make pages`) once stage 5 is green. Not a QA blocker. This write also falls outside my brief's write list |
| W4 | `20261102_2: 問題1/2 question repeats match in PUNCTUATION too — 問題1-1番` | The 「、」 placement in the head/tail question is transcription noise inherited from the source script. The audio is identical, and the line itself says it never blocks. Not a defect |
| W5 | `20261102_2: no 聴解 slot repeats its own theme in the previous 2 papers — 聴解問題2-2番=教育 (also 20261008_1)` | Composed half, so this is a draw audit. Read side by side, the subjects are unrelated. 20261008_1 2-2番 is a professor recruiting sleep-experiment subjects. This 2-2番 is a student going to the office to borrow the venue key while preparing a research presentation. They share no decisive detail, and nothing can be re-angled. Recorded |

The one `note` naming the paper says the two-back headline overlap 旅行・観光
sits only on the composed 聴解問題5-2番 and is not counted against rule 4's
budget (see §7.2).

No other WARN names 20261102_2. These skips name it:
- errand-key rotation (no keyed draws; the topic pass covers it);
- 問題7/問題8 form-family (0 of 17 grammar draws tagged);
- the 聴解1/2/3/5 errand line (it points at this pass);
- セクション構成表 (none in a composed paper);
- the imported-shape 問題5 lines;
- the 詳細解説 placeholder line (stage 5).

## 5. Keyed-form re-grep, 読解 half (問題10–14 body + （注N） glosses, key table excluded)

Keyed forms were read from the two fragments, which are authoritative. The
patterns include kana and kanji variants, plus keigo and humble variants of the
modal keys.

| 大問 | keyed form | count | frame / disposition |
|---|---|---|---|
| 問題7-31 | つつも | 0 | (pattern hit 11(2) 「一つつけて」 = 一つ＋つけて, not the form) |
| 問題7-32 | を踏まえて | 0 | — |
| 問題7-33 | （よ）うものなら | 0 | — |
| 問題7-34 | はずがない | 0 | — |
| 問題7-35 | と同時に | 0 | — |
| 問題7-36 | ことだし | 0 | — |
| 問題7-37 | かねない | 0 | — |
| 問題7-38 | ないわけにはいかない | 0 | — |
| 問題7-39 | のもとで | 0 | — |
| 問題7-40 | としたら | 0 | (pattern hit item 63 stem 「早く寝ようとすると」 = 〜ようとする＋と, not the hypothetical) |
| 問題7-41 | だらけ | 0 | — |
| 問題7-42 | いらっしゃる | 0 | none in 10(1), 10(2), 14 |
| 問題8-43 | に伴って | 0 | (pattern hits 「もっともな」 ×3 in 11(2) and item 60, not the form) |
| 問題8-44 | とはいえ | 0 | — |
| 問題8-45 | 一方 | 0 | — |
| 問題8-46 | てたまらない | 0 | — |
| 問題8-47 | をはじめ | 0 | 11(1) 「付けはじめた」, 13 「読み始めた」, item 68 「読み始めに」 = V-はじめる compounds, not N＋をはじめ |
| 問題9-48 | なにしろ | 0 | — |
| 問題9-49 | どうしようもなく | 0 | — |
| 問題9-50 | 〜ことにした | **1** | **10(2) notice: 「6月1日から、使ったおむつは園でまとめて捨てることにいたしました。」 — 文末, the humble form of 〜ことにした in the same decision sense as the key (問題9 blank 50 is also 文末).** The fragment is out of line with 問題9-50's key. **Routed to the 読解 author (C1)** |
| 問題9-51 | 先に家に着いた者 | 0 | — |

The 問題9 prose has no 問題7/8 keyed form. 「始めた小さな備え」 is
V-始める, not をはじめ.

**The gate is green on this hit.** `check_key_grammar_exposure`'s lines
「no 問題7/8/9 keyed form appears … in the same 文末/連用/連体 frame as its
stem」 and 「no 問題9 文末モーダル key is also a 文末モーダル in the 問題10-14
prose」 both read `ok`. The matcher does not see the humble spelling
〜ことにいたしました. See root-cause proposal RC-S3-1.

**Composed 聴解 (observation; outside Item integrity #15's scope, RC-8):**
- 問題9-50's 〜ことにした is spoken 3×:
  - 2-4番 「母にお金借りることにしたんですけど」;
  - 3-4番 「野菜ジュースを作って飲むことにしたの」 (the key evidence for 3-4);
  - 5-1番's question 「出席することにしましたか」.
- 問題7-42's いらっしゃる is spoken once: 3-3番 「お店をやっていらっしゃる橋本さん」.
- 聴解 is sat after 言語知識 is collected, so nothing leaks. No repair; same
  class as 20261102_1 Q2.

## 6. Content items for the section authors (not fixed here)

| id | file / line | check | message | proposed fix | owner |
|---|---|---|---|---|---|
| **C1** | `_sections/問10-14_読解.md` line 30 (問題10(2), second paragraph) | Stage-3 keyed-form re-grep (the gate line is blind to it, RC-S3-1) | 問題9-50's key 〜ことにした sits sentence-final in printed 読解 text as 「捨てることにいたしました」, in the same decision sense | e.g. 「そこで、6月1日からは、使ったおむつを園でまとめて捨てます。」 (or 「…処分いたします。」). Any form other than こと＋に＋する/いたす. **Item 53's 解説 cell quotes the old sentence verbatim and must be re-derived in the same edit.** Then: assemble → lint-draft → booklet → sheet (NOT autofix) → keyed-form re-grep → re-read 10(2)'s closing pair (unchanged) | 読解 author |

**C1 disposition (読解 author, fix pass 2026-11-02): FIXED.** 10(2) line 30 now reads 「そこで、6月1日からは、使ったおむつを園でまとめて処分いたします。」 (notice register kept; no こと＋に＋する/いたす). Item 53's 解説 re-derived to quote the new sentence; no other 解説 cell quoted it. Options of 53 unchanged (key 1 still 「…持ち帰らなくてよいこと」). 10(2)'s closing pair is untouched (two instructions: bring new nappies / label each). Widened re-grep of the assembled 問題10–14 body + glosses, with ことにし／ことにいたし／ことになっ／ことにする variants, humble/polite spellings and every 問題7/8/9 keyed form: 0 hits each (non-keyed surface 「進むことになる」 in 11(4) is ことになる, not the decision form). Rebuilt with assemble → lint-draft (clean) → booklet → sheet, no autofix; `logs/topics.json` notes sentence rewritten from 'open' to 'fixed'.

There are no other content items at stage 3. The minor reads in §7.2 (T1–T4)
go to QA, not to a repair.

## 7. Whole-paper topic pass (§"One topic, one surface")

### 7.1 The table

Themes are read from the SHIPPED surfaces. "Draw" is the spec `theme`
(`origin: authored`; 問題9 is author-composed by RNG). Prev = 20261102_1 and
two back = 20261008_1, both from `logs/topics.json`.

| surface | this paper: subject (shipped) | theme | on its draw? | closing shape / final template | MOVE | persona | 20261102_1 same seat | 20261008_1 same seat |
|---|---|---|---|---|---|---|---|---|
| 問題9 | 残り湯: after a half-day water outage, the bath is drained only just before the next evening's fill; tub-washing moves to whoever is home first | 防災 | yes (RNG over 防災/文化・伝統) | 随筆 / unnamed 〜こともある | 一人称の前後比較 | 生活者 | スポーツ・余暇 climbing log (数えた, 相関) | 行政・手続き 窓口の昼休み (反論応答) |
| 10(1) | email, shop → supplier: packing filler from air bags to crumpled paper, fragile goods excepted; will price or date change? | 環境 | yes | 実用文 | （実用文） | 実務者 | 科学・技術 ice physics | 科学・技術 sky optics |
| 10(2) | nursery notice: used nappies discarded at the nursery from 6/1; bring new ones each morning, each named | 子育て・家族 | yes | 実用文 | （実用文） | 保育園（通知） | 医療・福祉 thickened drinks | 交通 school-trip rail email |
| 10(3) | bike-class instructor: rear gear size vs pedal weight and distance per stroke | スポーツ・余暇 | yes | 説明 / unnamed trade-off 〜が、…てすみます | 機構の説明 | 職業人 | 行政・手続き envelope colour | デジタル化 kanji lookup |
| 10(4) | receptionist's month count: days staff wrote a return time had fewer 「少々お待ちください」 | 働き方 | yes | 条件提示 / 相関 with ほど | 数えたことの報告 | 観察者 | デジタル化 photo files email | 文化・伝統 haiku |
| 10(5) | traveller who always takes local trains; friend's objection granted, way kept (work empties from the head) | 旅行・観光 | yes | 反論応答 / unnamed 〜てある | 反論への応答 「理由を示して変えない」 | 旅行者 | 働き方 reading drafts aloud | メディア・情報 library newspapers |
| 11(1) | gyoza log, 8 sessions: squeezed cabbage → zero torn skins | 食 | yes | 条件提示 / unnamed 〜た日には…一つも…なかった | 数えたことの報告 | 趣味の実践者 | 文化・伝統 和ろうそく | 旅行・観光 island ferry |
| 11(2) | teacher doesn't red-correct diaries; parent's worry conceded; pencil circle on 3× repeated errors | 教育 | yes | 反論応答 / unnamed | 反論への応答 「譲歩して一部を変える」 | 職業人 | 防災 helmets | 防災 evacuation drill |
| 11(3) | student: 1.5× with stop/rewind → normal speed, mark and review after; 90 min now ~100 | デジタル化 | yes | 随筆 / unnamed 〜ようになった | 一人称の前後比較 | 学生 | 人間関係 lending log | 人間関係 friend's consultation |
| 11(4) | why moving bedtime earlier is hard: body clock runs a bit over 24 h | 睡眠・健康 | yes | 意外な観察 / unnamed 〜が、…しか…ない | 機構の説明 | 解説者 | 睡眠・健康 alarm across room | 食 bread rested an hour |
| 12(A) | souvenir custom persists by reciprocity; a burdened group should agree to stop | 人間関係 | yes (reroll 地域活性化 → 人間関係) | 説明 / unnamed 〜のが早い | 機構の説明 (A+B one) | 論者 | 交通 bus falls | 環境 green pond |
| 12(B) | craft club: newcomers give sweets as a pretext to talk; narrator talks to them first | 人間関係 | ″ | 意外な観察 / unnamed 〜ています | ″ | 生活者 | 交通 bus rider | 環境 bread in pond |
| 13 | 「長い記事は…読んでもらえない」 belief vs read-through articles that show the route first | メディア・情報 | yes | 主張 / `A だけではない。B こそが〜` | 〈想定→実は〉 | 利用者 | 食 knife and onions | 住まい frozen pipes |
| 14 | silver centre: screen/shoji re-covering (size table, 300円 pattern, pickup 500円 waived ≥5, pay on receipt, weekdays) | 住まい | yes | (flyer) | （実用文） | シルバー人材センター（案内） | 子育て・家族 clothes exchange | 医療・福祉 visiting barber |

聴解 rows (all composed). These are a DRAW audit, not a topic audit; nothing
here can be re-angled. Full surfaces, shapes and claims are in the
`logs/topics.json` row.

| item | subject | theme | 〈想定→実は〉? | clip |
|---|---|---|---|---|
| 1-1 | presentation practice: senior says speak slower (not add, not memorise) | 教育 | no | 2023-12:問題1-1 |
| 1-2 | farm part-timer: weed the leek field first | 食 | no | 2023-07:問題1-2 |
| 1-3 | umbrella left at café: friend keeps it, she takes the train | 人間関係 | no | kanzenmoshi:cd1-06 |
| 1-4 | boss's late shinkansen: rebook the next-morning train before the hotel | 働き方 | no | soumatome:cd1-44 |
| 1-5 | product-briefing prep: put the envelopes on the desks | 働き方 | no | 2023-07:問題1-5 |
| 2-1 | pocket projector went viral after a singer's TV mention | 消費・経済 | no | 2024-12:問題2-1 |
| 2-2 | goes to the office to borrow the venue key (pin mic only asked) | 教育 | no | kanzenmoshi:cd1-16 |
| 2-3 | staff survey: easier leave applications | 働き方 | no | 2024-07:問題2-3 |
| 2-4 | new car not to his taste: his mother chose it | 交通 | **YES** (「高かったでしょう」→「いや、安かったんですよ」, her assumption he is pleased denied → 母の好み) | soumatome:cd2-37 |
| 2-5 | radio: café-like shop's gift boxes hold flowers | 消費・経済 | **borderline, closest case** (attributed 通説 coffee + announcer's own 「まさか」; but X are candidate answers) | 2021-12:問題2-5 |
| 2-6 | fish shop: stock regional fish (price/deli/delivery ruled out) | 食 | no (proposal elimination) | 2022-12:問題2-6 |
| 3-1 | school office: Friday class rescheduled | 教育 | no | 2021-12:問題3-1 |
| 3-2 | rail photographer: what you want to convey > technique | スポーツ・余暇 | **borderline** (technique conceded, not denied; X = option 4) | 2024-07:問題3-2 |
| 3-3 | 50-year sweet shop owner: joy of the shop | 人間関係 | no | 2025-07:問題3-3 |
| 3-4 | canteen: woman improved her diet (350 g vegetables) | 食 | no | archive:2020-12:問題3-4 |
| 3-5 | supermarket job: cashier work means minding customers | 働き方 | no (man's guess = option 1, ruled out) | kanzenmoshi:cd1-21 |
| 4-1 … 4-11 | quick responses (see row) | 働き方×3, 人間関係×2, 教育×2, 食×2, スポーツ・余暇, 交通 | n/a | — |
| 5-1 | restaurant prize: manager + male clerk attend the ceremony | 働き方 | no (elimination) | archive:2020-12:問題5-1 |
| 5-2 | group tour: author's-places cycling AM, brush-making PM | 旅行・観光 | no | 2022-07:問題5-2 |

### 7.2 Reads and findings

**Four theme rules (counts).**
- **Rule 1.** Headlines: 問題9 防災, 問題12 人間関係, 問題13 メディア・情報,
  問題14 住まい, 聴解問題5 働き方 + 旅行・観光. All distinct.
- **Rule 2 (lenient: the four 読解 headlines only).** None of the four appears
  on another 読解 surface. 聴解5-1 働き方 also tags 10(4), and 5-2 旅行・観光
  also tags 10(5); rule 2's 2026-09-03 reading permits both.
- **Rule 3.** All 13 読解 themes are distinct (13 of 13).
- **Rule 4.** No 読解 headline repeats 20261102_1 (スポーツ・余暇, 交通, 食,
  子育て・家族, 地域活性化, 科学・技術).
  - Against 20261008_1, exactly one repeat: 住まい (問題14 here; 問題13
    there). That is the two-back budget of one.
  - The composed 聴解問題5-2番 旅行・観光 repeats 20261008_1's 聴解問題5-1番.
    The gate prints this as a `note`; it is not counted, being the composed
    half.
  - This is the same recording 20260929_1 spent as 5-2番, three papers back.
- **Rule 4b (headline subjects against 20261102_1's 13 + 21 subjects).** No
  match on same setting plus same issue.
  - 問題13 (articles read to the end) vs 4-4 (a forgotten singer): different.
  - 問題14 (screen/shoji re-covering) vs 3-2 (a retiree finds housework):
    different.
  - 聴解5-2 (tour courses) vs 20261008_1 5-1 (hotel booking): travel setting,
    different issue.

**Each surface against its own draw.**
- All 13 読解 surfaces sit on their drawn theme.
- Every surface matches its allocation row for subject, shape, template, MOVE
  and persona.
- Every allocation final and penultimate sentence occurs verbatim in the
  merged paper (checked by script). Three of them carry an inline （注N）
  marker in print: 11(1) もみこみ, 11(4) 宵の口, 13 道筋.
- The spec `avoid` keyword hits are word collisions on different subjects:
  - 10(1) vs a paper-container sorting notice and a reusable-tableware email;
  - 10(2) vs three nursery notices on other issues;
  - 10(4) vs a lecture-reception staffing call;
  - 12 vs a gift-choice errand;
  - 13 vs AI summaries, local papers, a newsletter column and a clippings
    book;
  - 14 vs an essay whose sliding door sets the order of re-papering windows.
  None is the same institution plus the same issue.

**Rows read across the three columns (same seat).**
- **T1 (minor, seat-level): 11(4) 睡眠・健康 sits in the seat where
  20261102_1 also put 睡眠・健康** (11(4), the alarm moved across the room).
  The subject, MOVE and persona all differ:
  - here: the body clock's >24 h period, 機構の説明, 解説者;
  - there: moving the alarm, 一人称の前後比較, 学生.
  The allocation barred exactly the (theme, MOVE) pair and the alarm/waking
  subject. 20261102_1's stage 3 recorded the same class (its T1). The root
  cause is the theme-to-seat draw, not the authoring. No other seat repeats
  either previous paper's theme.
- **T2 (minor, claim-level, 読解-internal):** 10(3) and 11(4) are both 機構の説明.
  They close on the same contrastive two-clause skeleton: 10(3) 「…回数は増えますが、
  一回ごとに足にかかる力は小さくてすみます」 and 11(4) 「…遅らせる向きには一晩でも合わ
  せられるが、早める向きには少しずつしか合わせられない」. Both are 〈one direction
  costs X, the other Y〉, in different 大問 (10 vs 11), and neither is a named
  template. The allocation's at-risk list paired 10(3) with 12(A) and 11(4)
  with 12(B), not these two with each other. Not a cap breach. **For QA's
  template-column read.**
- **T3 (minor, two back):** 10(5) (local trains) and 20261008_1 11(1) (island
  ferry times) share the slow-transport-travel domain. Different claim (keep
  the slow way for one's head vs times set by the tide). Noted.
- 問題12 cross-test column: 人間関係 souvenirs vs 交通 bus falls vs 環境 pond.
  No relation.

**Within this paper, 読解 ↔ 聴解 read as one list.**
- **T4 (minor, domain only):** 12(B) (newcomers hand out sweets at a craft
  club) and 聴解3-3番 (a sweet shop's joy) share sweets. 12(A)/(B) gifts and
  聴解2-5番 (gift boxes of flowers) share gifts. No decisive detail can be
  carried between them. Not a finding.
- 10(5) local trains and 聴解1-4番 (rebooking a shinkansen) / 4-9番 (nearly
  boarded the usual train): rail domain only.
- 11(3) recorded lectures and 聴解3-1番 (a rescheduled class): university
  domain only.
- 11(1) gyoza and 聴解3-4番 (vegetables in the diet) / 2-6番 (fish shop): food
  domain only.
- 13 (writer and reader) and 聴解1-1番 (presentation pacing): both about
  helping an audience follow. Different subjects, no shared detail.
- `check_* 問題14 shares no decisive number with any 聴解 item` is ok.

**MOVE column, read down the skeleton.** I ran the deletion test on every row
except 13. No other 読解 row carries attributed assumption → denial → 実は Y.
Nearest cases:
- **11(1):** pleats and extra water were tried and failed. But no belief is
  stated, and 「自分では見当がつかなかった」 disclaims a hypothesis. Same call as
  20261102_1 13.
- **11(3):** the result runs against intuition (90 min now takes ~100). But no
  expectation is written, as the allocation designed.
- **12(B):** 「会になじむための手がかりでもあった」 adds a cause; it does not deny A
  with 実は.

The gate's marker count is 0 of 13. It does not see 13's unmarked 通説, which is
why this column is read by hand.

**TEMPLATE column, read separately.**
- Named: 相関 1 (10(4), with ほど, not に伴って), `A だけではない。B こそが〜` 1
  (13). 分裂文 0; 後知れ / 不在 / 先回り 0.
- not-A-but-B family: 1 (13).
- `check_dokkai_template_repeat_prev_paper`: ok (問題9 is not 相関; 12 is not
  わけではない).
- Unnamed pairs at risk:
  - 問題9 / 11(3): 〜こともある vs 〜ようになった, different.
  - 10(3) / 12(A): 〜てすみます vs 〜のが早い, different.
  - 11(4) / 12(B): 〜しか…ない vs 〜ています, different.
  - 10(4) / 11(1): ほど＋数量 vs 〜た日には…一つも…なかった, different.
  - 10(5) / 11(2): 〜てある vs 〜てきます, different.
  - 12(A) / 12(B): different.
  - The one echo is T2 above.

**〈想定→実は〉 cap of 2 across both halves.**
- 読解: **1** (13, allocated).
- 聴解, counted: **2-4番**.
  - The woman's presupposition 「高かったでしょう」 is explicitly denied
    (「いや、安かったんですよ」).
  - Her assumption that he is pleased (「よかったですねえ」) is denied by his
    reaction; the real reason is 「母の好み」.
  - This is the 20261008_1 2-4番 kimono shape, which the 2026-10-03 ruling
    counted. "Expensive" is not one of the item's four candidate reasons.
- **Total 2, at the cap.**
- **Q1 (question for the orchestrator):** 聴解問題2-5番 is the nearest case.
  - It carries an attributed 通説 (「箱にはコーヒーが入っていると思われる方も多い
    そうです」) and the announcer's own denied presumption (「まさかこの箱に花が
    入っているとは思いませんでした」).
  - I do not count it. Coffee, sweets and jewels are each a printed option to
    the item's own question 「何が入っていますか」, which is RC-7's exclusion.
  - 3-2番 (technique conceded, it is option 4) and 3-5番 (the man's guess is
    option 1) are borderline and also not counted.
  - **If 2-5番 is counted, the paper is at 3 and 13 must be re-angled** to the
    allocation's legal targets: 数えたことの報告, 一人称の前後比較 or
    反論への応答 (each 2→3); never 機構の説明, which is at cap 3.

**聴解 errand identity (shapes across three papers).**
- No clip-id repeat (§3).
- **Q2 (question for the orchestrator/QA): 聴解問題4-4番
  (`2025-12:問題4-4`) runs the same errand as 20261102_1's 4-1番
  (`shinkanzen:cd2-65`).** Both are a request to consult a colleague, granted
  with かまいません. The keys are 「構いませんよ。いつがいいですか？」 here and
  「ええ、かまいませんよ。何でしょう？」 there.
  - The tested form differs. Here it is 〜ていただけるとありがたい as a request,
    and the distractors invert the benefactive direction. There it is
    よろしいでしょうか, against おかまいなく and どういたしまして.
  - My read: same situation, different item. Not proposed for
    `MUTUALLY_EXCLUSIVE_CLIPS`.
  - If QA judges them one item, the repair is a composer re-draw with a fresh
    orchestrator SEED before QA, plus the pair added to
    `MUTUALLY_EXCLUSIVE_CLIPS`. I did not re-draw.
- 1-1番 (a senior approves most of a presentation and changes one point,
  speed) is the third paper running with this 問題1 genre: 20261102_1 1-4番
  (lighting material) and 20261008_1 1-3番 (poster figure). The clips,
  products and changed element all differ. It is a standard official genre.
  Noted; not one item.
- Within the paper, three items are on seminars or presentations: 1-1番
  (practice), 2-2番 (prep, borrowing a key) and 4-2番 (consolation after a bad
  one). Different errands. Two are on umbrellas: 1-3番 (left at a café) and
  4-3番 (should have brought one). Different errands. Domain only.
- 4-10番 (have you been to the new restaurant) vs 20261008_1 4-10番 (the cheap
  set-meal shop was good): same slot and restaurant domain, different exchange
  (asking about experience vs agreeing with a verdict). Not one item.

## 8. Root-cause row proposed (for QA's table)

| id | finding | where it slipped | proposed repair |
|---|---|---|---|
| RC-S3-1 | C1: 問題9-50's key 〜ことにした sits 文末 in 10(2) as 「捨てることにいたしました」, and `make check` printed `ok` on both keyed-form lines | `check_key_grammar_exposure` matches the keyed surface string, and the humble/polite spellings of a modal key (〜ことにいたしました / 〜ことにしました) do not contain 「ことにした」 | Normalise a 〜ことにした / 〜ことになった key to a stem (ことに＋{し,いたし,なっ,なり}) before matching, the same way kana/kanji variants are folded. Then re-run the gate across all papers on disk and record any newly surfaced hits before treating them as regressions |

## 9. `logs/topics.json`

Row `20261102_2` appended. It holds:
- `surfaces` 43, `themes` 43, `shapes` 29, `claim` 43;
- `closing_moves` 13, `voices` 14, `persona` 14;
- `notes`.

The notes record:
- the draw;
- the allocation match and the MOVE / template / persona tallies;
- the gate's voice counts;
- the theme rules;
- the keyed-form grep with C1 still open (the fix pass must update that
  sentence);
- the draw audit;
- the 〈想定→実は〉 count with Q1's borderline cases;
- the cross-paper 聴解 observations (Q2).

「」 is used only for strings in the paper: 3 spans, all verified by
`check_topics_notes_quotes`. No repo-wide number is pinned.

## 10. Skipped, and why

- `make model-answer` / 詳細解説 (the one FAIL): stage 5, prohibited before QA.
- `make drill` (W3): it bakes stage-5 data. Run it after stage 5, and it is
  outside this brief's write list.
- No 聴解 re-draw: no clip repeat and no dropped bar. Q1 and Q2 are decisions
  for the orchestrator, not seed-shopping.
- C1 not edited: it is a passage rewording plus a 解説 cell, routed to the 読解
  author.
- The 文字・語彙 fragment was not read line by line. It feeds neither the topic
  table nor the keyed-form grep, and its gate and lint lines are all ok.

## 11. Orchestrator rulings (2026-11-02)

| item | ruling |
|---|---|
| Q1 聴解2-5番 and the 〈想定→実は〉 cap | **Not counted.** The guesses it denies (coffee, sweets, jewels) are the item's own printed options, raised and ruled out. That is the "does NOT count" case of the RC-7 rule now in `jlpt-test-generation` §"One topic, one surface" (applied in aa025ac). The cap reads 2 of 2: 問題13 and 聴解2-4番. 問題13 is not re-angled. |
| Q2 聴解4-4番 vs 20261102_1 4-1番 | **Not one item.** The two are different clips with different tested forms. "Asking permission, answered with かまいません" is a stock 問題4 situation, not an errand identity. No re-draw, and no `MUTUALLY_EXCLUSIVE_CLIPS` entry. QA may overrule with a reason. |
| C1 | Closed by the 読解 author (§6): 「処分いたします」, and 53 解説 re-derived. |
| W1 (29 unread clip script records) | Deferred to stage 4 QA, which writes `logs/choukai_script_reads.json` rows (exam-qa-review §4 check 6). |
| W3 (stale `drill/N2`) | Deferred until after stage 5. `drill/` is gitignored build output. |

## Addendum — QA F3 applied (bank repair, 2026-11-02)

- **What changed.** In `.agents/choukai-audio/references/textbook_items.json`,
  `kanzenmoshi:cd1-21`'s last 女 line now reads
  「女:だといいんだけどね。とにかく、なるべく疲れないのがいいのよ。」, matching
  完全模試 解答 p.31.
  - `make choukai-bank` accepted it. The window is unchanged (4.10–100.28 s).
    `measured.rate` moved 0.1826 → 0.1738, inside the official band.
- **Audibility, decided by measurement, so no ear-check was queued.**
  - The window ends after the spoken options, so any spoken last line lies
    inside it.
  - Track21's speech runs (`choukai_segment.measure` + `find_pauses`,
    min 0.25 s) align turn by turn at 0.10–0.18 s/char. The woman's last turn
    is the 4.02 s run at 61.80–65.82 s.
  - With the printed 29 characters that turn runs at 0.139 s/char, matching
    the surrounding turns (T4 0.137, T9 0.13). The banked 10 characters would
    imply 0.40 s/char.
  - The lone 1.04 s run at 67.88 s, flanked by pauses of 2 s or more, is this
    book's structural beat before the question. The same beat shows in
    Track20 (46.00–47.06 s) and Track23 (52.76–53.78 s).
  - So the line is spoken, and the transcript now matches the audio.
- **Holders**, from `logs/choukai_draws.json`: 20260910_1 (問題3-3) and
  20261102_2 (問題3-5). Both were replayed with `make mp3 <id> REPLAY=1
  NO_AUDIO=1`.
  - **0 of 29 slots moved** on each, preambles and seed are the same, and both
    `聴解.mp3` sha1s are unchanged.
  - 20260910_1's replay also refreshed two pieces of stale composer output.
    The opening line of 聴解スクリプト.txt had been corrupted to 「Nに聴解」 and
    is now 「N2聴解」. The 問3 `script` fields now carry the spoken options,
    as the current composer writes them.
  - 20260910_1 then got `make sheet` and `make model-answer`, and is clean in
    `make check`.
  - 20261102_2's booklet and sheet were deliberately NOT rebuilt (the
    orchestrator does it after the section fixes). Until then `make check`
    FAILs `20261102_2: built HTML matches the Markdown it stamps`.
- `logs/choukai_script_reads.json` keeps `kanzenmoshi:cd1-21` → `F3`, the way
  F6/F7 kept theirs after the 20261102_1 repair.
