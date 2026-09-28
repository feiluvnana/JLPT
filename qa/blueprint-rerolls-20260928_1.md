# Blueprint rerolls — 20260928_1 (why each `--reroll-one` ran)

Base draw: `make sample 20260928_1 SEED=47119433`. Every reroll below used a
fresh `secrets.randbelow(10**8)` seed, and each was forced by a rule. None was
run to get a "nicer" item. The ledger seed string records the seeds; this file
records the reasons (qa-report-20260928_1 F1 / RC-2: the pipeline has no place
to write them).

| # | reroll | out → in | reason |
|---|---|---|---|
| 1 | `reading_topics:11` seed 23975609 | 働き方 → 食 | rule 4: 働き方 headlined 20260917_1 (問題13); index 11 is 問題14, a headline |
| 2 | `kanji_reading:1` seed 26220605 | 匹敵する(ひってき) → 五重の塔 | the 文字・語彙 author found 匹敵する is 音 + する; `is_kun_target` mis-scored a reading with the する left off as 訓. Once the classifier was fixed, the paper held 1 true 訓 target against `KUN_FLOOR` 2 |
| 3 | `kanji_reading:1` seed 42706298 | 五重の塔(ごじゅうのとう) → 捕らえる | 五重の塔 is 音 throughout; the classifier read the particle の as okurigana. Fixed, then the floor was still unmet |
| 4 | `kanji_reading:1` seed 63171527 | 捕らえる(とらえる) → 略す | **undrawable, not mis-classified**: 捕らえる IS 訓, but moji-goi's "build the set BEFORE you accept the target" found no three real same-field 〜らえる distractors (branch (a) empty, branch (b) only こらえる) |
| 5 | `kanji_reading:1` seed 7021088 | 略す(りゃくす) → 最も | 略す is 略(リャク) + す; the classifier judged a bare す tail 訓. Fixed (the stem must be on-shaped and one of the kanji's pykakasi readings) |
| 6 | `reading_topics:9` seed 39520803 | スポーツ・余暇 → 科学・技術 | stage-3 F1, rule 1: the composed 聴解問題5-1番 is スポーツ・余暇 |
| 7 | `reading_topics:9` seed 6670416 | 科学・技術 → 交通 | rule 4 FAIL: 科学・技術 was 20260917_1's (composed) 聴解問題5-2 headline, carried here by a 読解 headline |
| 8 | `reading_topics:9` seed 43431270 | 交通 → 行政・手続き | rule 1: 交通 is the 問題9 cloze's composed theme |
| 9 | `reading_topics:9` seed 89576765 + `--exclude-theme` ×10 | 行政・手続き → 人間関係 | rule 4: 行政・手続き headlined 20260917_1 (問題14). Exclusions (rule-forbidden only): 環境 メディア・情報 働き方 行政・手続き 消費・経済 科学・技術 (20260917_1 headlines) + 交通 文化・伝統 食 スポーツ・余暇 (this paper's other headlines) |
| 10 | `grammar_p7:5` seed 85597537 | 〜を通して → 〜にあたって | QA F2: 20260917_1 keyed 〜を通じて; Shin Kanzen and the 媒介 family treat them as one point, inside the grammar cooldown |

Pipeline changes these forced (`sample_items.py`): `is_kun_target` now handles
a する reading with the する left off, a particle の, and a bare す tail. It
moves exactly 匹敵する, 五重の塔, 気の毒 and 略す to 音, and no shipped paper's
count changes. A new `--exclude-theme` flag was also added to `--reroll-one`.
