# QA report — 20261008_1 (Stage 4, round 2: scoped re-review)

QA: FAIL (2 findings, 0 automatic)

Neither finding changes a key or replaces an item. Under `jlpt-test-generation` §"The fix loop" both are fixed directly and get no third review. R2-F1 is the one that blocks: the paper is at 3 against the cross-half 〈想定→実は〉 cap of 2.

- **Reviewed:** 2026-10-08 22:31–22:42 JST, by a context that wrote nothing in this paper and did not run round 1.
- **Source revision.** These shas were the same at the start (22:31) and before writing (22:40), and the mtimes did not move:
  - `言語知識・読解.md` = `3ded8d02c01d` (22:29:03). This is the post-round-1-fix revision; round 1 read `1eb4ea5ec07f`.
  - `聴解.md` = `1aac1d3b91f4` (18:41:08)
  - `聴解スクリプト.txt` = `e83e714732fc` (18:41:08), which equals `聴解_チャプター.json` `script_sha`.
- **Solved from** `qa/20261008_1/keyless.md` (`make keyless 20261008_1`, 934 lines, rebuilt at 22:31). Items 41, 63 and 64 were answered from that file, and the answers written to `<scratch>/qa2_1008_blind.txt`, before I opened any key row.
- **Scope**, per the brief and §"The fix loop":
  - 問題7-41 (rerolled 〜に即して → 〜とみえる) and the 問題7 column;
  - 問題11(4) (re-angled) with 63–64, and the 問題11 column;
  - the MOVE ruling on 11(4), and the F3 claim re-check against 問題9.
- **Entry gate.** `make check` exits 2 with exactly one FAIL, `20261008_1: 詳細解説.json explains every keyed item (30 entries for 101 keys)`. That FAIL belongs to stage 5 and is expected. The paper's three WARNs are the ones round 1 dispositioned (§6).

## 1. Blind-solve diff

**3/3 agreement. There are no mismatches.**

| item | reviewer | key | |
|---|---|---|---|
| 41 | 4 とみえる | 4 | agree |
| 63 | 4 | 4 | agree |
| 64 | 3 | 3 | agree |

**Blind strategy passes, re-run over all 18 items 52–69** (64 is new, and 67 and 69 moved in F2). Chance is 25%.

| measure | result | bar |
|---|---|---|
| Most bigrams shared with the item's own passage | 6/18 = 33.3% | ≤45% (official 32.8%) |
| Second-longest option | 4/18 = 22.2% | ≤45% (official 24.6%) |
| Uniquely longest key (gate, 52–71) | 5/20 = 25% | ≤30% |
| Tied-longest key (gate) | 7/20 = 35% | ≤35% |
| Overlap margin median (gate) | −0.080 | ≤0 |
| 64 option lengths | 33/29/31/30, ratio 1.14 | ≤1.65 |

64's key is the option with the **lowest** bigram overlap of its set (0.29), so it is a paraphrase, not a lift.

## 2. Walkthrough (scoped items)

| 項目 | 鍵 | 判定 | 決め手／どこが問題か | どう直すか |
|---|---|---|---|---|
| 問題7-41 | 4 とみえる | OK, stem 要修正 (R2-F2) | 「今朝から何度も時計を見ては、そわそわしている。午後の面接が、よほど気になる（とみえる）」. The speaker infers a third person's state from observed behaviour, and よほど pairs with an inferential ending.<br>**Two-answer hunt:**<br>• 1 限りだ attaches to emotive adjectives (うれしい限りだ), never to a verb like 気になる, and it voices the speaker's own feeling, while the experiencer here is 山田さん. Impossible on two counts.<br>• 2 おそれがある states the risk of a future bad event. 「面接が気になるおそれがある」 is nonsense, and よほど takes an inference, not a risk.<br>• 3 にすぎない ("merely") contradicts よほど (extreme degree).<br>**Band:** in band. I opened the Shin Kanzen N2文法 PDF myself. The 索引 p.209 (PDF p.218) prints 「〜とみえる 100, 136」. 実力養成編 第1部 22課-1 (book p.100, PDF p.110) heads 「〜とみえる ⇒ある根拠があって、〜らしい・〜ようだと思う」 with 普通形＋とみえる and the note 「主にほかの人の様子を見て、それを根拠に推量したことを表す文につく。推量した人は文中に表れない」. That satisfies `bunpou.md` §Inventory (1). It is not in `level_band_grammar.txt` TOO_HARD. No official key exists: the only 「と見え」 strings in the 31 booklets are literal 見える (7/2017 L474, 7/2024 L110), not the grammar form. The rerolls file's "0 hits" is right for the form. It last keyed in 20260812_2 (#32), and the gate's rotation line is `ok`. | R2-F2 |
| 問題11-63 | 4 | OK | 「焼き上がったばかりのパンの中には、まだ湯気がこもっています。このまま袋に入れると…表面がべたべたになり、切ろうとすれば中がつぶれてしまいます」.<br>• 1 (burns): not stated.<br>• 2 (aroma too strong): not stated; the passage says the aroma weakens.<br>• 3 (no staff before opening): not stated, and the bread is 「並べています」 after its hour. | — |
| 問題11-64 | 3 | OK (key); passage → R2-F1 | Concession: 「たしかに、焼きたての香りは、時間がたつと弱くなります」. Reason: 「一時間ほど置くと…ふっくらとした形のまま切れるのです」. Kept: 「棚のパンには一時間の休みを取らせています」.<br>• 1 is denied by the final: the hour is kept.<br>• 2 is denied by the たしかに line. I tested it as a second answer, because the passage does say 「店の中の焼きたての香りは消えません」. It still dies, on its own reason clause 「冷めても変わらない」.<br>• 4 (bake later, just before opening) is not stated, and 「パンは七時ごろから順に焼き上がります」 contradicts it.<br>The key survives the R2-F1 fix unchanged, because no option mentions the oven. | R2-F1 (passage) |

## 3. Column re-reads

### 問題7 (12 stems)

- **Distribution** (gate, the owner's counter): mean 46.2 (band 36–52), 3 stems under 34 (34, 36, 39; need ≥2), spread 47 (≥25). Dialogue or setting stems: 2 (35, 38).
- **Option-form reuse.** 41's four forms (限りだ, おそれがある, にすぎない, とみえる) occur in no other 問題7 option line. The nearest relative is 35-1 かねない, which shares a lesson with おそれがある (22課-2/-3) but is a different form. The gate line `no 問題7 form printed in more than 2 items' options` is `ok`, and by hand no form appears in two items, which is the official maximum of 1.
- **One key per paper.** とみえる is keyed only at 41. Over the 問題10–14 prose and the （注N） lines it occurs 0 times (grep 「とみえ|と見え」 hits only L158 and the key row L563). The gate's keyed-form exposure line is `ok`.
- **41 against 42 (R2-F2).**
  - The stems are adjacent and built on one template: 「**隣の**席の山田さんは…そわそわしている。…よほど気になる（　）」 and 「**隣の**部屋の明かりが夜中までついていた。田中さんは…書いていた（　）」. Each observes a third person's behaviour and asks for an inference about them.
  - The keys come from one Shin Kanzen lesson, 22課 「〜だろうと思う」: とみえる is 22課-1 and に違いない is 22課-5 (p.101, opened). 41's distractor おそれがある is 22課-3.
  - The gate's 目次 line is `ok` because the two keys have different section numbers. It also maps only 2 of this paper's 17 grammar draws.
  - Measured on the 10 imported sittings' 問題7 keys: **no sitting keys two inference forms**. The only ones are 2022-07 みたい, 2023-07 らしく, 2025-07 らしく and 2025-12 に違いない, one each.

### 問題11 (4 passages, 8 stems)

- **Stems.** 57 なぜか, 58 分かったこと, 59 何か, 60 どうだったか, 61 なぜか, 62 考え, 63 なぜか, 64 考え.
  - Every pair puts the 事実 stem first.
  - There are 2 考え stems (62, 64), inside the official 1–4.
  - The gate's no-pure-retrieval line is `ok`.
  - 64's stem shares the 24-character formula 「の意見について、筆者はどのように考えているか。」 with 20261002_1. That is a stem shape, not apparatus, and is not filed.
- **Keys** 1,3,1,4,3,4,4,3. The 71 positions match `answer_positions` (gate `ok`).
- **Foil reuse across the 大問.**
  - 64's distractors share no actor and reaction with any other 問題11 foil.
  - 63-2 and 64-2 are both aroma foils, but different lines kill them: 63-2 is not stated, and 64-2 dies on the たしかに line.
  - 63-1 prints 「おそれがある」, which is 41's distractor. Under `exam-qa-review` §3's exclusion 3, option strings are outside the keyed-form scan, and it is not a key, so it is not counted.
- **What 63 and 64 test.**
  - Both keys rest on the 湯気→形 paragraph. 64 discriminates on the stance (concede, then keep), so it is not a re-ask of 63.
  - In the current text, the whole post-（中略） half (the oven) decides neither item. The R2-F1 fix removes that half, which also tidies this up.
- **13-final column, 11(4)'s row.**
  - The current final 「香りは奥のオーブンにまかせて、棚のパンには一時間の休みを取らせています」 is unnamed. It is not a cleft, not 後知れ, not 不在, not 先回り, and not the not-A-but-B family.
  - It differs from 20261002_1's 11(4) skeleton (〜ので、…ままでも、…V-ていく) and from 問題9's 〈決まりは続けていく。ただ…開けておきたい〉.
  - Shape 反論応答: 2 (問題9, 11(4)), at the cap. The gate's template and reframe lines are `ok`.
- **Provenance**, re-run for the re-authored surface. I ran a 14-character shared-run scan of the whole 11(4) block (passage plus 63–64) and of item 41 against every other `tests/*` booklet and 聴解スクリプト, all 31 `booklet.md` and `script.md`, and the Shinkanzen, Soumatome, Hajimete and External extracts. The only hit is the 64 stem formula above. There is no passage lift.
- **Lengths.** The gate's 問題11 section floor and ceiling and the per-passage ≥400 line are `ok`. 11(4) body = 576 JP characters: 330 before （中略） and 244 after.

## 4. The MOVE ruling on 11(4)

**Ruling: 11(4) runs 〈想定→実は〉. The paper is at 3 (11(1), 聴解2-4番, 11(4)) against the cross-half cap of 2. Filed as R2-F1.**

I read it down the skeleton, 〈通説または自分の想定した X → 否定 → 実は Y〉, and set the 反論応答 / 反論への応答 labels aside:

1. **Attributed assumption.** The customer says 「焼きたてのほうがおいしいのに…香りも逃げてしまう」. Holding the bread costs the shop its fresh-bread aroma, and the aroma is the shelf bread's.
2. **Explicit denial.** 「棚のパンを一時間置いても、店の中の焼きたての香りは**消えません**」 directly negates the customer's 「逃げてしまう」 for the thing the customer experiences, the shop.
3. **実は Y.** It is set up by the reveal question 「では、店に入ったときの香りは、どこから来るのでしょうか」 and delivered as 「入り口で感じる香りは、ほとんどがこのオーブンから流れてきています」. The real source is elsewhere.

**The deletion test** (`dokkai.md` §MOVE allocation). Delete the denial and its 実は Y, that is, the oven paragraph. The final 「香りは奥のオーブンにまかせて」 then loses its antecedent. The recorded claim (`logs/topics.json`: 「…認めるが、店の香りは奥のオーブンが担っているので…」) loses its middle term. The whole post-（中略） half has nothing left to say. **The passage collapses, so it is on the skeleton.**

**Why the 「たしかに」 concession does not exempt it.** Conceding the literal claim and then relocating the real cause is the owner's founding case for this cap: `20260907_1`'s "the tool kept its promise; the real change was elsewhere", which `jlpt-test-generation` §"One topic, one surface" counts as this skeleton. 11(4) is "the aroma does weaken; the aroma you notice really comes from elsewhere". That is the same shape: 前提の更新 / 予想外の担い手.

**The allocation's own argument is refuted.** Its row says 「no 〈想定→実は〉 (the 「どこから来るのでしょうか」 is a question device, nothing attributed is denied)」. Something attributed IS denied: 「香りも逃げてしまう」 against 「香りは消えません」. The question device is the reveal beat, not a neutral one.

At the very least this is BORDERLINE under the three-beat rubric, and borderline resolves against the item (Ground rules: default FAIL). Precedent also counts 3 as over the cap: 20261002_1 stage-3 R-1 was re-angled from 3 to 2.

**Origin (repair collateral).** Round 1's F3 recommended exactly this landing site: 「the scent customers notice at the door comes from bread still baking in the back all morning」. The fixer then followed it. Neither the proposal nor the fix was read against the MOVE column. This is the repair-collateral class `exam-qa-review` §5 names (20260812_1, 20260903_1, 20260904_1), with a new twist: the reviewer's own proposed fix carried the collateral (RC-R2-1).

**The F3 duplicate-claim re-check against 問題9: closed.**

| beat | 問題9 | 11(4) now | same? |
|---|---|---|---|
| narrator | 職業人, first person, the clerk's own workplace rule | 職業人, first person, the baker's own practice | yes (persona 職業人 2, at the cap, allowed) |
| objection | a resident's letter | customers' remarks | yes (the MOVE 反論への応答 allows it) |
| concession | a **blind spot** 「そういう人がいることまでは、考えが及んでいなかった」 | a **cost** 「たしかに…弱くなります」 | no |
| resolution | rule kept **plus one exception channel** (phone booking) | practice kept, **no exception, no schedule change** | no |

The claim, which is what Axis 4 compares, now differs in resolution, so F3 is closed. One residue remains: both surfaces are 職業人 defending a one-hour workplace practice (正午〜一時 / 一時間置く) against a member of the public. That is legal under today's persona cap, and it is exactly what round 1's RC-F3 row ("the two rows may not share a persona token") would forbid. That row is still open and should be adopted before the next `make sample`. The R2-F1 fix below avoids 問題9's wording (決まり, これからも, 続けていく, 考えが及ぶ), so it does not re-tighten F3.

## 5. Findings

### R2-F1 — 問題11(4) runs 〈想定→実は〉: the cross-half count is 3 against the cap of 2 (要修正; key unchanged)

- **Owner.** 読解 (question-authoring/dokkai). The 読解 side is always the one re-angled; 聴解2-4番 is a banked recording.
- **Location.** `言語知識・読解.md` 問題11(4), the three paragraphs after （中略）; item 64's 解説 row (L590), which quotes the final; `logs/topics.json` 20261008_1 `surfaces` and `claim` for 問題11(4) and the 〈想定→実は〉 count in `notes`; `qa/dokkai-allocation-20261008_1.md` L45 (the 「no 〈想定→実は〉」 cell).
- **Evidence.** §4: 「香りも逃げてしまう」 → 「棚のパンを一時間置いても、店の中の焼きたての香りは消えません」 → 「入り口で感じる香りは、ほとんどがこのオーブンから流れてきています」. The deletion test collapses the passage.
- **Fix: delete the relocation, and keep 63 and 64 exactly as they are.**
  - Replace the three post-（中略） paragraphs with a hold-and-explain that answers the objection on its own terms. Suggested text, 230 JP characters against 244 today; pad by about 10 characters if the 問題11 floor line moves:

    > 　香りが弱くなる分は、私も惜しいと思っています。それでも、お客様がパンを召し上がるのは、たいてい家に帰って切ってからです。そのときに中がつぶれず、ふっくらとした形のまま切れることを、この店では大切にしてきました。
    > 　ですから、「どうして冷ますのか」と聞かれたときには、パンの中の水分について説明し、焼き上がったばかりのパンと一時間置いたパンを切って、切り口を見比べていただくようにしています。
    > 　棚のパンには、焼き上がってから一時間の休みを取らせ、それから袋に入れています。

  - Constraints, all checked against the suggested text:
    - no attributed belief is denied (the deletion test has nothing to delete);
    - no cleft, no わけではない, no 〜ていた＋のだ, no 〜ていない, no 先回り, and no foil-preference final;
    - none of 問題9's 決まり / これからも / 続けていく;
    - no new （注N）, and the paper total stays at 27;
    - （中略） is kept;
    - 0 hits for every 問題7/8/9 keyed form, とみえる included.
  - Then:
    - **64's 解説:** replace the quote 「香りは奥のオーブンにまかせて…」 with the new final, or with 「そのときに中がつぶれず…大切にしてきました」. The 1/2/4 kills are unchanged.
    - **Re-confirm 64:** 1 dies on the final, 2 on 「たしかに」 and 「惜しい」, 4 on 「七時ごろから」.
    - **`logs/topics.json` 問題11(4) `claim`:** 「焼いたパンの香りが時間とともに弱まることは惜しいと認めつつ、家で切ったときにつぶれない形を保つために、一時間置くことは続け、切り口を比べて見せて説明する。」 Re-record `surfaces` and `notes` the same way, then grep for 「オーブン」 in all four narration places (`jlpt-test-generation` §"Closing a finding includes re-grepping its notes").
    - **Allocation row L45:** strike the 「no 〈想定→実は〉 … nothing attributed is denied」 cell and the oven wording.
    - **Re-run:** `make check` (length, template, reframe and keyed-form lines), then the 13-final column and the MOVE column once each. The cross-half count must return to 2 (11(1), 聴解2-4番).
- **Not taken:** re-angling 11(1). It is the allocated, clean seat, and the defect is on the re-angled surface.
- **Root cause.** RC-R2-1 and RC-R2-2 (§7).

### R2-F2 — 問題7-41 and 42 are one stem template on adjacent items (要修正, minor; key unchanged)

- **Owner.** 文法 (question-authoring/bunpou).
- **Evidence.** Both stems open 「隣の」, observe a third person's behaviour and ask for an inference about them. The two keys come from one Shin Kanzen lesson (22課-1 とみえる and 22課-5 に違いない), and 41's distractor おそれがある is 22課-3. The 10 imported sittings key at most one inference form per 問題7 (§3). This is not a two-answer issue: とみえる would fit 42's frame, but it is not among 42's options.
- **Fix (stem only, no reroll).** 41 → 「山田さんは、今朝から何度も時計を見ては、そわそわしている。午後の面接が、よほど気になる（　）。」. This drops 「隣の席の」, which removes the shared opener.
  - Distribution after the fix: about 5 characters shorter; the mean stays inside 36–52, the under-34 count stays at 3, and the spread stays at 47 (max 68 / min 21).
  - The 41 解説 needs no change: it names 山田さん, not 隣の席.
  - Leave the shared-lesson key pair as drawn. A reroll now would put an unreviewed item into a paper that has used up its one scoped re-review. It goes to RC-R2-3.
- **Root cause.** RC-R2-3.

### Looked at, not filed

- **41 distractor 2 おそれがある** is a same-lesson competitor of the key. That makes it plausible, not weak. It shares part of speech and function (a 文末 modal) with the key.
- **63–64 both keyed on the 湯気→形 paragraph.** 64 discriminates on the stance (§3). The fix leaves this as it is.
- **The pools_sha WARN** now reads 20261008_1 recorded `b8ba57b537f9` against pools `cf187cf62829`. That stamp is the F1 reroll's. The pool moved again when 〜に即して was retired into `retired_entries.grammar_p7`. This is a record, not a defect: the spec, the ledger and `rotation.reroll_log` all name 〜とみえる at `grammar_p7[10]` with seed 48018312.

## 6. Coverage

- **Steps run, scoped:**
  - **Step 0** on 41/63/64, plus both strategy passes over all 18 items.
  - **Steps 1 and 2.** The key proof, plus one line per wrong option, for 41, 63 and 64.
  - **Step 2b** on all three option sets.
  - **Step 2.5** for 41, with the Shin Kanzen N2文法 PDF opened at PDF pp.110, 111 and 218.
  - **Step 3:**
    - the 問題7 distribution and option-form reuse;
    - the 問題11 stems, foils and lengths;
    - the keyed-form re-grep over 問題10–14 prose and glosses;
    - the 13-final read for 11(4);
    - the provenance re-scan of the re-authored surface.
  - **Step 5:** the MOVE column (§4) and the claim column against 問題9.
  - **Step 6:** the spec, ledger and reroll_log for `grammar_p7[10]`.
- **`make check` WARNs naming this paper** (all three were dispositioned in round 1 and are unchanged):
  - the composed 聴解問題5 headline repeat against 20261002_1;
  - 聴解3-3番's two-back theme;
  - pools_sha (§5).
- **Round-1 dispositions in scope:**
  - **F1** holds: rerolled, retired, recorded, in band.
  - **F3** holds on the claim, and its landing site is R2-F1.
- **Glanced, not re-passed:** F2 (paragraph 1 now reads 「昼すぎに気温が上がって管の中の氷がとけるまで」, and 69-3 matches it) and F6 (「（注2）便：ここでは、船が出る、その一回一回」).

## 7. Root-cause rows (6.5)

| id | finding | code | tests showing the class | owning file | concrete proposed edit |
|---|---|---|---|---|---|
| RC-R2-1 | R2-F1 | RULE-MISSING | Repair collateral: 20260812_1, 20260903_1, 20260904_1 and this. This is the first case where the reviewer's own proposed re-angle authored it. | `exam-qa-review/SKILL.md` §3 (beside 「A replacement option YOU propose is a new distractor」) and §5 | Add: **"A re-angle YOU propose is a new MOVE. Before writing it into the report, classify the proposed passage against the 〈想定→実は〉 skeleton and run the deletion test on it. A proposal that relocates 'the real cause' elsewhere is the skeleton (`20261008_1` F3 → round-2 R2-F1)."** Not gateable. |
| RC-R2-2 | R2-F1 (cap wording) | RULE-UNENFORCEABLE (two files disagree) | 1 file pair | `question-authoring/references/dokkai.md` §"The rhetorical-MOVE allocation table" | The table cell 「**2** — 3 is the ceiling, never the target」 and the sentence 「Plan 2, accept 3, treat 4 as a rewrite」 contradict the owner rule, 「Cap: 〈想定→実は〉 at most 2 surfaces across both halves」 (`jlpt-test-generation` §"One topic, one surface"), and the 20261002_1 precedent that re-angled 3 → 2. Replace both with 「**2 across both halves** (owner: jlpt-test-generation). The official 3–4 of 9 is why 2 is not a floor, never a licence for 3」. |
| RC-R2-3 | R2-F2 | RULE-MISSING | Measured: 0 of 10 imported sittings key two inference forms in 問題7. Not yet measured over generated papers. | `question-authoring/references/bunpou.md` §問題7; `exam-blueprint` (draw-time) | Add to §問題7: **"At most one 推量 key (らしい／みたい／に違いない／とみえる／はずだ…) per 問題7, and no two adjacent stems on one scene template."** Measure it over all generated papers before landing, and name the ids it moves. A draw-time bar would need Shin Kanzen 課 mapping, but the 目次 check maps only 2 of 17 draws here. |

Round 1's open rows (F1, F3, F4, RC-O1, RC-O2) still block the next `make sample`, and RC-R2-1 to RC-R2-3 join them.

## 8. Skips

- **Not a full re-pass.** Only 41, 63, 64 and their columns were solved. The strategy passes over 52–69 are the one exception.
- **No audio.** No 聴解 item is in scope, the 聴解 half was not re-composed, and the environment has no playback. Round 1's F4 is still open on its ear-check.
- **Shin Kanzen N1 文法 is not in `refs/`**, so the "would N1 claim it" half of step 2.5 rests on the N2 headword. That is sufficient under `bunpou.md` §Inventory (1).
- **No edits.** Only this report was written. Scratch files are `<scratch>/qa2_1008_*`, with a copy of round 1's strategy script re-run on current text.

## Dispositions (orchestrator, 2026-10-08): fixed directly, no further review (the scoped re-review runs at most once)

| finding | disposition |
|---|---|
| R2-F1 11(4) runs 〈想定→実は〉 (paper at 3) | **Fixed** by the 読解 author with this report's replacement text, plus three lexical-load swaps (帰宅, 実際に, 比べて見て). The oven passage is removed; the aroma loss is conceded twice and never denied. New final: 「棚のパンには、焼き上がってから一時間の休みを取らせ、それから袋に入れています。」 Items 63/64 are unchanged (keys 4/3); 64's 解説 is re-quoted. The paper is at 2 = cap (11(1), 聴解2-4番). The allocation row and the `logs/topics.json` surface/claim/notes are re-recorded. |
| R2-F2 stems 41/42 share one template | **Fixed** by the 文法 author: 41 is now a two-turn dialogue (駅前で, a queue at a ramen shop → 「よほど評判がいい（　）」); options and key 4 are unchanged; 解説 rewritten. The two-inference-keys-per-問題7 observation is left as this report's rule proposal, with no reroll. |

The rule proposals (deletion test for reviewers' re-angles, dokkai.md 「accept 3」 wording, an inference-key cap per 問題7) join round 1's root-cause rows. They are **not applied**, and they block the next `make sample` until each is applied or rejected with a reason.
