# QA report — 知識 N2 漢字 batch 10 (71 kanji, SK 301–384; 50 back-links)

**QA: PASS after fixes.** I authored none of this batch. One full round, with direct fixes. One author (Sonnet, the first Sonnet draft) wrote both panes.

Files: scratch `batches/漢字_B10.json`, `.ja.json`, `.vi.json`, `.backlinks.json`, `.backlinks.vi.json`, `K10_live_meaning_fix.json` (36 → 37 ja), `K10vi_live_meaning_fix.json` (2 vi). The originals are in `QAK10_orig/`. `QAK10_fix.py` rebuilds every fix from those originals plus the CURRENT live tree. I did not edit the live `knowledge/`.

## Checks

| area | method | result |
| - | - | - |
| ids / readings | SK 別冊 PDF 161–165, sliced with pypdf and read as images | All 71 ids match the page. The other 13 numbers in range are already live. on/kun/words match, and the (他) marks are on the page (感じる/ずる, 喜ぶ). Five rubies were wrong and 貝 needed a decision (F1, F3) |
| official_count | Parser over 問題1/2 of 31 sittings (301 items). The 9 items it misses were read by hand | 0 is right for all 71. No 問題2 key holds a B10 kanji. Every 問題1 hit is outside the underlined word. Spot-checked the cited distractor notes (育う, 加じった, 即差に, 完えず): all true |
| examples | `frames`, then every example read for frame and sense | 3 replaced (F5). The replacements were rescanned until they had 0 hits (two drafts hit an official 問題6 misuse, and one hit a 語彙 card) |
| lures | `lures` before and after | 7 GW, all judged: 帰/理, 質/本, 規/違, 接/礼, 賃/労, 賃/工 and 践/送 are not two-answer items, and all predate B10 (B9 accepted the same set). PAIR 0. HW: F4 |
| translation | vi compared with ja, field by field | `meaning` and `usage` are written for the vi reader. **`compare` mirrored the ja in 44 of 45 batch entries and in about 42 of the 50 back-link sentences** (F6) |
| back-links | `rebase`, plus a read of all 50 | 45 extend the live compare verbatim. 5 added a link with no text (F2) |
| links | each new `related` pair read against the brief's link reasons | Justified. Look-alikes, compound partners, 問題2 option sets and colliding glosses each have a reason. Same-sound-only pairs (加/可, 期/器, 決/結) are kept: 問題2 tests exactly that confusion, and the compare names it. 個/魚 is kept for the Vietnamese CÁ trap |
| gate | `batch_tool gate` | Before and after: 0 FAIL, 0 WARN, 0 REVIEW. After: +71 entries, 50 back-links, fixes ja 37, vi 2. `frames` 0 hits |

## Findings

| # | where | sev | defect → fix | root cause |
| - | - | - | - | - |
| F1 | ja usage: 位 各 角 球 港 | major (▶ speech) | The ruby in each usage row did not match the row's reading. In the on rows: 〜位《くらい》, 球《たま》, 〜港《みなと》. In the kun rows: 各《かく》, 角《かく》. Fixed to い, きゅう, こう, おのおの, かど | The same class as B9 F1, again. There is still no gate check that a ruby in the 音読み segment is an on reading. `QAK10_ruby.py` is that check (12 lines) and should move into `check_ruby_suspects` |
| F2 | back-links 係 情 務 違 調 | major (rule 28) | A link was added with no contrast text, because the live compare was near the cap. Each live compare was compressed, keeping every 「」 form and contrast, and the new contrast was added in both panes: 関係, 感, 業, 差, 査/調査 | The cap was treated as a reason to skip. The brief should say: compress, never skip |
| F3 | 貝 on/kun | minor | SK prints 「カイ」 in katakana (the on column), but かい is the kun reading of 貝. Moved to `kun ['かい']`, `on []`, with a source note. ja and vi usage rewritten | Typesetting in the source. Decided for the reading class, with a note |
| F4 | ruby 形《けい》 in 「形も似ている」 (課 議 経; back-links 憶 果 会 義 軽) | major (▶ speech) | 8 places read 形 (shape) as けい. Fixed to かたち. In the same place, rule 34: 型's live gloss 「ものの形…きまった形」 now carries the new headword 形, so a live fix was added. The K10 fix for 争 left 勝 (k-0414) in place → 「あいてにかとうとして…」 | The author's helper ruby'd 形 by its on reading. The HW sweep was run on the batch glosses only, not on its linked partners |
| F5 | examples 育 加 格 | minor | 育: one 庭師 tends the pines 「三代にわたって」 → 庭師の一家. 加速: 「急ぎのため…少しずつ加速」 contradicts itself → a ship with a new engine. 格好: 「軽い格好」 is not a natural collocation → パジャマのままの格好. vi notes rewritten | The frame scan cannot see sense. The author did not read each example once for meaning |
| F6 | vi compare (45 batch + about 42 back-link sentences) | major (brief rule 10) | Rendered from the ja sentence by sentence, for example 王 「玉とは形が似ていて…点がある」 → "「王」 và 「玉」 trông gần giống; 「玉」 có thêm một chấm". All were rewritten for the vi reader, led by Hán Việt: 絵/会 and 形/型 share HỘI and HÌNH; 差 SAI ≠ "sai" (wrong); 最 TỐI ≠ "tối" (dark); 億/憶 share ỨC | Brief rule 10 was ignored in a one-author batch. Field by field, compare is the field where translation creeps in |
| F7 | vi meaning 最 経; ja/vi usage 件 | minor | 最 "cuối cùng" was borrowed from 最後 → "nhất, hơn hết". 経 "điều hành" was borrowed from 経営, and it is 営's gloss word → "trải qua; kinh độ". 「〜件」 is not on the 件 page, so it was cut from both panes | Rule 29 (borrowed sense) and rule 27 (sense on the page) |

The six older live fixes swept in by this batch (勝 争 厚 辛 積 濃) were re-read. Five are fine. 争 is F4.

**Counts:** 7 findings (5 major, 2 minor). Edits: 13 rubies, 3 examples, 2 vi glosses, 1 reading class, 1 usage claim, 45 vi compares, 47 vi back-link sentences, 5 ja back-links rebuilt, 2 live fixes (1 added, 1 changed).

**Sonnet vs the Opus drafts:**
- Per entry, the content defect rate is about the same as B8/B9. B9 (Opus, 31 entries) had 4 rubies, 2 examples, 9 vi glosses and 22/31 mirrored compares. B10 (71 entries) has 13 rubies, 3 examples and 2 vi glosses.
- Sonnet did worse at applying the brief's written lessons. The B9 F1 ruby class came back with more instances. The vi compare mirroring that brief rule 10 names came back in about 98% of compares, against 71% in B9.
- Sonnet did better on vi gloss borrowing, and every new link had a reason.
- The B10 drafts pass the tool checks, but each one-pass lesson needs a QA round to hold.
