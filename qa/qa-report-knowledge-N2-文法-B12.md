# QA report: knowledge/N2 文法, batch 12 (1 point: g-fumaete 〜を踏まえ, 3 examples, 2 quiz items, 2 back-links)

Reviewed 2026-10-01 by a fresh-eyes context that authored none of the batch. The files are in the coordinator's
scratch `batches/`. sha1 (first 12) before review → after the fixes:

| file | pre | post |
|---|---|---|
| `文法_B12.json` | 38bd1ffacae9 | 70fbe58bda9f |
| `文法_B12.ja.json` | be8c8f6f0aeb | c8df64901d11 |
| `文法_B12.vi.json` | ff4cb24fa61a | cff278ee2a21 |
| `文法_B12.backlinks.json` | e986ca373395 | 97004715082a |
| `文法_B12.backlinks.vi.json` | 768d14dd53b8 | fb471eda6e19 |

All fixes are in one script you can re-run, `scratchpad/QA12_patch.py`. It always starts from `QA12_bak/`. I did not
touch the real `knowledge/` tree or any B11 file.

## Verdict

`QA: FAIL → fixed (6 findings: 2 要修正, 4 軽微). No content findings are open.`

**Gate.** I copied `.agents/` and `knowledge/` into `scratchpad/QA12_repo` and symlinked the rest of the repo. There I
ran `merge_batch.py`'s own logic (`QA12_merge.py`, with only REPO repointed) as `文法 11 12`, so B11 merges first,
then B12, back-links included. After that I ran `build_knowledge.py --level N2` and `check_knowledge.py`. The whole
run is in `QA12_gate.sh`.

- **Result: 0 FAIL, 0 WARN, 293 entries.** B11 back-links reached 31 live entries and B12 back-links reached 2.
- The merge printed no `REVIEW` line, so neither B12 back-link drops a quoted form.
- The merged 文法 answer positions are 144/149/148/145 (the gate says "balanced"). B12's keys stay at 1 and 4.

## 1. Blind solve (rule 7), splices (rules 1, 2, 8, 16)

**Process deviation, stated plainly:** I first opened the shared file whole, so the keys were in view before I
extracted anything. After that I wrote `QA12_blind.txt` with `QA12_blind.py` (stem and options only, no ids,
seed 1212), solved each item by splicing, and saved `QA12_myanswers.txt` (Q1 → 1, Q2 → 4). My agreement with the
keys proves nothing. The verdicts below rest on the splice of every distractor.

| item | option | spliced | kill | killing words or page |
|---|---|---|---|---|
| Q1 | を踏まえ ✓ | 知らせを踏まえ、…書き加えた | — | — |
| Q1 | に反して | 知らせに反して、…「電車やバスで」 | meaning: the added line agrees with the notice, it does not go against it | 「駐車場が…使えなくなる」 vs 「電車やバスで」 |
| Q1 | にかけては | 知らせにかけては、… | meaning: needs a skill or superiority predicate (live g-nikaketeha: 〜のことでは、だれよりも上手だ) | 「書き加えた」 |
| Q1 | をめぐって | 知らせをめぐって、…書き加えた | page: the predicate must be a dispute or discussion (SK PDF 44, live g-womegutte) | 「書き加えた」 |
| Q2 (new) | をめぐる | 結果をめぐる対策 | page: the modified noun must be a dispute or discussion noun (PDF 44) | 「対策」 |
| Q2 (new) | に先立つ | 結果に先立つ対策 | meaning: a measure taken before the result contradicts 「そこで」 (after the result was known) | 「わかった。そこで」 |
| Q2 (new) | に反する | 結果に反する対策 | meaning: posting staff only in the morning follows the result | 「朝の通学の時間に事故が多い」 vs 「朝だけ」 |
| Q2 (new) | を踏まえた ✓ | 結果を踏まえた対策 | — | — |

- All four options attach to the noun before the blank in both items, so no item is decided by form alone (rule 2).
- Polarity is mixed, with one opposite-polarity option per item. No two options share a kill clause (rule 16).
- Every distractor has a live entry (rule 38): g-ni-hanshite, g-nikaketeha, g-womegutte, g-ni-sakidatte.
- The tested form is not printed in all four options (rule 37).
- No option set shares 3 of its 4 options with an official 問題7 set (rule 33). I grepped every booklet.md for
  をめぐ, にかけては, に反, に先立 and read each hit.
- **Coordinator point 2 (に基づいて and をもとに kept out):** confirmed. With those two forms out, neither item has a
  second defensible option.
  - I also checked the forms a learner would bring to each stem unprompted: に応えて (Q2 old stem) and
    に基づいた / をもとにした (Q2 new stem). None of them is an option. So the only two-answer risk is one the
    options do not raise.

## 2. Coordinator's points, judged

| # | point | verdict |
|---|---|---|
| 1 | `connection` leaves out をふまえて (rule 37) | **The connection is right, but the entry still taught the form (F1).** I read all four cited pages in the PDFs: Mimikara 聴解 PDF 12 「聞くべきことをふまえ、」 and PDF 130 「それをふまえた提案」; Soumatome 聴解 PDF 8 「聞くべきことをふまえ、」; Soumatome 漢字 PDF 10 「試験の形式をふまえた実戦問題」. They attest exactly 「をふまえ、」 and 「をふまえた＋名詞」. **But** `pattern` 「〜を踏まえて」, `reading` 「をふまえて」, the ja `compare` and both ja back-link compares printed the て-form, which has 0 hits in refs. The vi pane quoted only 「を踏まえ」 / 「を踏まえた」 and was clean. Fixed per the B9 に至っては precedent |
| 2 | blind solve with に基づいて / をもとに excluded | **One key, one defensible answer in each item** (§1). Q2 had a separate scene defect (F2) and was replaced |
| 3 | vi 「踏」 = “đạp” clause (rule 9 vs rule 34) | **Kept; not a rule-9 breach.** Rule 9 covers contrastive or pragmatic *usage* claims (register, modesty, "most formal"). This clause is a kanji gloss plus a false-friend warning, and that is rule 34's territory. Rule 34 allows calling a Hán Việt reading a trap only when the reading is itself a Vietnamese word with another meaning. “Đạp” is one, and “chà đạp” (trample, disregard) is close to the opposite of 踏まえる, so the warning is a real trap. The image "đứng trên A mà bước tiếp" matches the verb's literal sense (to plant one's feet on). The clause read 「Chữ 踏 là “đạp”」, which a learner can take as a gloss of the pattern, so I relabelled it as the Hán Việt reading (F5). Residual: no refs page prints 踏's Hán Việt. It is dictionary-level, as in the live vi pane's 一方/通/応/拝/承 notes |
| 4 | vi Q1 "bãi xe sắp đóng" vs 工事で使えなくなる | **Loose enough to fix (F3), minor.** It dropped 来月から and the cause 工事, and "đóng" alone suggests a permanent closure. Now: "Tháng sau bãi xe đóng để thi công" |
| 5 | back-links vs B11 pending (g-womotoni) and live (g-ni-motozu-ite) | **Every quoted form is kept in both languages** (the merge printed no REVIEW line). Two contrasts were thinned (F6). g-womotoni ja had cut B11's 「を中心に」は｜真ん中や主になる部分 down to 主になる部分: **restored** (97/100). In both vi back-links, 「に基づいて」 lost "quyết định" (the 判断 facet). Putting it back pushes them to 185 and 183 of 180, so I **left them as written** (173/180, 171/180); ja still carries 判断. Both ja are inside the band (97, 93 / 100) |
| 6 | provenance, scene clash, balance, gate | **The 10-char scan found 0 windows** across examples, stems, ja prose and the vi-quoted Japanese, against `refs/**/*.md` and `tests/imported-*/**/*.{md,txt}` (`QA12_prov.py`). **The scene check found F2.** Balance and gate: see above |

## 3. official_count (rules 4, 12, 37)

It stays **0**, confirmed. A grep of every `refs/JLPT_N2_NEW/*/{booklet,key,script}.md` for 踏まえ / ふまえ finds only
7/2018 booklet 「足を踏まれた」, which is the verb 踏む and not this point. There is no official item keying the form,
so the required one-line scene column is empty. Every source is a textbook's own prose (Mimikara, Soumatome), which
is what the inventory note of 2026-10-01 says.

## 4. Examples: provenance, frames, furigana

| cited-page sentence | nearest B12 sentence | differs by |
|---|---|---|
| Mimikara PDF 130 「河合さんが遅れることがわかったので、それをふまえた提案を述べる」 | Q1: news that the parking closes → the organiser adds a line to the notice | different scene; the predicate is a written notice, not a spoken proposal |
| Mimikara PDF 12 / Soumatome 聴解 PDF 8 「事前に示されている聞くべきことをふまえ、ポイントを絞って聞く」 | none (no listening or exam scene) | — |
| Soumatome 漢字 PDF 10 「試験の形式をふまえた実戦問題」 | none (no exam or test-format scene) | — |

- The kanji-bigram scans (category-wide `QA12_cross1.py`; module-wide plus every official booklet.md and script.md
  line in `QA12_cross2.py`, all 68 hits read) found no frame copies for ex1–ex3 or Q1:
  - 文化祭 hits 12/2019 問題14 and the 語彙/漢字 cards, but none of them has a reflection → change frame.
  - 7/2019 script 「駐車場が使えない」 is a bicycle-shed repaint, a different claim.
- Readings checked by hand: 反省《はんせい》, 受付《うけつけ》, 仕入《しい》れ, 見直《みなお》す, 主催者《しゅさいしゃ》,
  越《こ》し, 交差点《こうさてん》, 係員《かかりいん》, 通学《つうがく》, 対策《たいさく》. No `check_ruby_suspects` pattern.
- ex3 「法律ができたことを踏まえ」 is a 形式名詞 こと ＋ を踏まえ, so it is within 「名詞 ＋」.

## 5. Findings

| # | class | sev | surface | what | fix | ROOT CAUSE |
|---|---|---|---|---|---|---|
| F1 | unattested form taught (rule 37) | 要修正 | shared `pattern`, `reading`; ja `compare`; ja back-links g-womotoni, g-ni-motozu-ite | The headword 「〜を踏まえて」 / 「をふまえて」 and three ja compares quoted a form with 0 refs hits. Only `connection` had been narrowed | pattern 「〜を踏まえ」, reading 「をふまえ」, the three ja quotes 「を踏まえ」. id and book key unchanged | **RULE-GAP (rule 37).** The rule says "every form an entry keeps", but the author treated `pattern`/`reading` as the inventory's fixed `printed` label and applied the rule to `connection` only. The B9 fix (に至っては) narrowed the pattern, but rule 37 never says the headword is included |
| F2 | quiz scene = an official item's frame (rules 21, 35) + a kill resting on an unstated order (rule 1) | 要修正 | Q2 (stem, both explanations) | 「読者から…という声が多く届いた。その声（ ）改訂版では…」 reused the frame of 12/2011 問題7-37 「この美術館では、利用者の声に（こたえて）…延長することにします」 (users' 声 → the provider changes its product) and of live g-nikotaete ex2 「読者の要望にこたえて…出版される」. The に先立つ kill also relied on sentence order alone | new stem: 市の調査 finds morning school-time accidents at a crossing → 「そこで」 a measure, staff in the mornings only. 「そこで」 puts the time order into the stem. ja and vi explanations rewritten from the new item, each on its own distractor (ja に先立つ, vi に反する). My own first redraft (a museum visitor survey → bigger caption text) hit 12/2011-37 head-on and was discarded | **CHECK-GAP (rules 21/35).** Both scans key on 2-kanji bigrams. The shared key noun here is the single kanji 声, and the scene is the canonical frame of a *neighbouring* form (に応えて) that is not among the options, so neither scan nor rule points at it |
| F3 | vi explanation unfaithful to the stem | 軽微 | vi Q1 | "bãi xe sắp đóng" dropped 来月から / 工事 | "Tháng sau bãi xe đóng để thi công" | **RULE-GAP.** VI brief requires faithful `example_notes`, not faithful restatement of the stem inside quiz explanations |
| F4 | ja explanation overstates the stem | 軽微 | ja Q1 | 「知らせどおりの対応」: the notice prescribes nothing | 「知らせに合う対応」 (and 「逆のことになる」 → 「逆になる」 to stay under 80) | one-off wording; covered by the general "explanation argues from stem words" rule |
| F5 | Hán Việt label | 軽微 | vi nuance | 「Chữ 踏 là “đạp”」 can read as a gloss of the pattern | "Hán Việt 「踏」 là “đạp”" | one-off; rule 34 wording is satisfied |
| F6 | back-link thinned a live contrast | 軽微 | ja back-link g-womotoni; vi back-links (both) | ja dropped 「真ん中」 from を中心に (B11 pending text); vi dropped "quyết định" from に基づいて | ja restored; vi left (band), stated in §2 | **CHECK-GAP.** merge_batch.py's REVIEW diff compares quoted forms only, not the gloss attached to each form |

## 6. Rules proposed

- **SKILL rule 37 (and BATCH_JA_BRIEF "ADDED after batch-9"):** add "`pattern` and `reading` included. The
  inventory's `printed` headword is a label too. If it has 0 hits, the headword is narrowed to the attested form, as
  B9 did with に至っては and B12 with を踏まえ."
- **SKILL rule 21/35:** add "For each stem, list the forms a learner would bring to the blank unprompted (に応えて,
  に基づいて, をもとに…), grep the official items keying THOSE forms, and read their scenes. A frame is the
  cause → provider-response shape, even when only one kanji (声) is shared." Better still, add a 1-kanji head-noun
  pass to `QA9_cross.py`.
- **BATCH_VI_BRIEF:** "A quiz explanation restates the stem's facts faithfully (time, cause, agent). It may shorten
  them but never swap them."
- **QA brief, step 1:** the coordinator should hand the reviewer a keyless extract first. The reviewer is told to
  read the shared file, which carries the keys, so rule 7's order can only be kept by discipline.

## 7. Side observation (out of scope, not fixed)

`tools/scaffold_explanations.py:149` builds 問題9 explanation scaffolds with 「文章全体の趣旨を踏まえて」, which is the N1
instruction. Every official N2 booklet prints 「文章全体の内容を考えて」 (e.g. 12/2021, 7/2025). The gitignored
`tests/*/_sections/問7-9_文法.md` fragments also carry it. The assembled `言語知識・読解.md` files do not.
