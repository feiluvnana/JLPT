"""Generated quiz items for the 語彙 / 漢字 categories — ONE generator for the
builder, the gate and the drill's 復習ノート (jlpt-knowledge/SKILL.md §Quiz integrity).

A category whose spec in references/categories.json carries `quiz_gen` gets, per
entry, the item types it lists, built from the data at build time:

    reading   `<id>#r`  the headword (語彙 `word`; 漢字 one of its `words`, markup
                        stripped) + 4 hiragana readings: the entry's own and 3
                        distractors — other entries' readings (same mora count and
                        first mora preferred) and, for 漢字, the compound read with
                        another 音/訓 of one of its kanji that is a batch entry.
    meaning   `<id>#m`  the headword + 4 `meaning`s in the reader's language: the
                        entry's own and 3 other entries' (same `pos` preferred).
                        Distractor ENTRIES are chosen once, so every language pane
                        has the same key position.

Integrity (the reason generation is safe — check_knowledge re-verifies it):
- a reading distractor is never the entry's reading, never a reading the vendored
  dataset lists for the headword (`pitch.readings(word)`), and never the reading
  of another entry with the same headword. No dataset -> no reading items.
- a meaning distractor never comes from an entry in this entry's `related` (or one
  that relates to it), never shares the headword, never has the same meaning text
  in any language and, in 語彙, never shares a kanji with the headword (a shared
  kanji is where near-synonyms hide).
- too few candidates -> the item is skipped, never padded.

Deterministic: every choice is ranked by a sha1 of the qid and the candidate, and
key positions are dealt 1,2,3,4 over the category's items in qid-hash order, so a
rebuild over the same data is byte-identical and positions are balanced.

Stdlib only (gzip through pitch.py), no page code.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import knowledge_data as D   # noqa: E402
import langs                 # noqa: E402  (knowledge_data put its folder on sys.path)

try:
    import pitch as PITCH    # noqa: E402
    PITCH.readings("日本")   # loads the dataset now: a broken one means "no reading items"
except Exception:            # noqa: BLE001
    PITCH = None

KINDS = {"reading": "r", "meaning": "m"}
_RUBY = re.compile(r"｜([^《》｜]+)《([^》]*)》|([一-龥々〆ヶ]+)《([^》]*)》")
_HIRA = re.compile(r"^[ぁ-ゖー]+$")
_KANJI = re.compile(r"[一-龥々〆ヶ]")
_SMALL = set("ゃゅょぁぃぅぇぉゎ")
_GEMINATE = {"つ", "く", "ち", "き"}


def types(spec: dict) -> list[str]:
    """The generated item types a category's spec asks for (categories.json `quiz_gen`)."""
    return [t for t in spec.get("quiz_gen") or [] if t in KINDS]


def qid(eid: str, kind: str) -> str:
    return f"{eid}#{KINDS[kind]}"


def dataset_ok() -> bool:
    return PITCH is not None


def to_hira(s: str) -> str:
    return "".join(chr(ord(c) - 0x60) if 0x30A1 <= ord(c) <= 0x30F6 else c for c in s)


def morae(kana: str) -> list[str]:
    out: list[str] = []
    for ch in kana:
        if ch in _SMALL and out:
            out[-1] += ch
        else:
            out.append(ch)
    return out


def segments(text: str) -> list[tuple[str, str | None]]:
    """｜漢字《かんじ》 / 漢字《かんじ》 / plain kana -> [(base, ruby or None)]."""
    out, pos = [], 0
    s = (text or "").replace("**", "")
    for m in _RUBY.finditer(s):
        if m.start() > pos:
            out.append((s[pos:m.start()].replace("｜", ""), None))
        base, rb = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
        out.append((base, rb))
        pos = m.end()
    if pos < len(s):
        out.append((s[pos:].replace("｜", ""), None))
    return out


def clean(s: str) -> str:
    return re.sub(r"[〜～\s]", "", s or "")


def kana_of(text: str) -> str | None:
    """The whole hiragana reading of a furigana'd word, or None if any kanji is unread."""
    r = clean(to_hira("".join(rb if rb is not None else b for b, rb in segments(text))))
    return r if r and _HIRA.match(r) else None


def headword(e: dict, spec: dict) -> str:
    return clean(D.plain(str(e.get(spec["headword"], ""))))


def _h(*parts) -> str:
    return hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()


def _kanji_readings(e: dict) -> list[str]:
    """A 漢字 entry's readings as hiragana stems: 音 folded, 訓 cut at the okurigana dot."""
    out = [to_hira(x) for x in e.get("on") or []] + [x.split(".")[0] for x in e.get("kun") or []]
    return list(dict.fromkeys(clean(x) for x in out if clean(x) and _HIRA.match(clean(x))))


def reading_target(e: dict, spec: dict) -> tuple[str, str, str] | None:
    """(word shown, its reading, markup source) — or None when a reading item makes no sense
    (a kana-only word shows its own answer)."""
    if spec["headword"] == "kanji":
        k = str(e.get("kanji", ""))
        ws = []
        for w in e.get("words") or []:
            pw, r = clean(D.plain(w)), kana_of(w)
            if k and k in pw and r and _KANJI.search(pw):
                ws.append((pw, r, w))
        if not ws:
            return None
        return min(ws, key=lambda t: _h(e["id"], "word", t[0]))
    word, r = headword(e, spec), clean(to_hira(str(e.get(spec.get("reading") or "", ""))))
    if not (_KANJI.search(word) and r and _HIRA.match(r)):
        return None
    return word, r, word


def _pairs(entries: list[dict], spec: dict) -> list[tuple[str, str, str]]:
    """Every (word, reading, owner id) the category holds: 語彙 headwords, 漢字 compounds."""
    out = []
    for e in entries:
        if spec["headword"] == "kanji":
            for w in e.get("words") or []:
                r = kana_of(w)
                if r:
                    out.append((clean(D.plain(w)), r, e["id"]))
        else:
            word = headword(e, spec)
            r = clean(to_hira(str(e.get(spec.get("reading") or "", ""))))
            if word and r and _HIRA.match(r):
                out.append((word, r, e["id"]))
    return out


def invalid_readings(word: str, key: str, pairs) -> set[str]:
    """Readings a distractor may never be: the key, every reading the dataset lists for
    the word, and every reading another entry gives the same headword."""
    bad = {key} | {r for w, r, _ in pairs if w == word}
    if PITCH is not None:
        bad |= {to_hira(r) for r in PITCH.readings(word)}
    return bad


def _fabricated(src: str, key: str, by_kanji: dict) -> list[tuple[str, dict]]:
    """The compound read with another 音/訓 of one of its kanji that is a category entry."""
    segs = segments(src)
    out = []
    for i, (base, rb) in enumerate(segs):
        if rb is None:
            continue
        rb = to_hira(rb)
        spots = []                                     # (char, its reading here, prefix?, suffix?)
        if len(base) == 1:
            spots.append((base, rb, "", ""))
        else:
            for ch, edge in ((base[0], "head"), (base[-1], "tail")):
                for r in by_kanji.get(ch, {}).get("readings", []):
                    forms = {r} | ({r[:-1] + "っ"} if r[-1:] in _GEMINATE and edge == "head" else set())
                    for f in forms:
                        if edge == "head" and rb.startswith(f) and len(rb) > len(f):
                            spots.append((ch, f, "", rb[len(f):]))
                        if edge == "tail" and rb.endswith(f) and len(rb) > len(f):
                            spots.append((ch, f, rb[:-len(f)], ""))
        for ch, here, pre, post in spots:
            ent = by_kanji.get(ch)
            if not ent:
                continue
            for alt in ent["readings"]:
                if alt == here:
                    continue
                new = [to_hira(r if r is not None else b) for b, r in segs]
                new[i] = pre + alt + post
                cand = clean("".join(new))
                if cand != key and _HIRA.match(cand):
                    out.append((cand, {"kanji": ch, "as": alt, "is": here}))
    return out


def _rank(q: str, key: str, cands):
    km = morae(key)

    def score(c):
        cm = morae(c)
        return (-(2 * (len(cm) == len(km)) + (cm[:1] == km[:1])), _h(q, c))
    return sorted(cands, key=lambda t: score(t[0]))


def _reading_item(e, spec, pairs, by_kanji):
    tgt = reading_target(e, spec)
    if not tgt or PITCH is None:
        return None
    word, key, src = tgt
    q = qid(e["id"], "reading")
    bad = invalid_readings(word, key, pairs)
    pool, seen = [], set()
    for w, r, owner in pairs:
        if owner != e["id"] and r not in bad and r not in seen:
            seen.add(r)
            pool.append((r, {"word": w, "owner": owner}))
    fake = []
    if spec["headword"] == "kanji":
        for r, why in _fabricated(src, key, by_kanji):
            if r not in bad and r not in seen:
                seen.add(r)
                fake.append((r, why))
    fake, pool = _rank(q, key, fake), _rank(q, key, pool)
    pick = fake[:2]
    pick += pool[:3 - len(pick)]
    pick += fake[2:2 + 3 - len(pick)]
    if len(pick) < 3:
        return None
    return {"qid": q, "id": e["id"], "kind": "reading", "word": word, "key": key,
            "distractors": [{"text": r, **why} for r, why in pick]}


def meanings(prose: dict, eid: str) -> dict[str, str]:
    """{code: meaning} for every active language that has a non-empty one."""
    out = {}
    for c in langs.order():
        m = (prose.get(c, {}).get(eid) or {}).get("meaning")
        if isinstance(m, str) and D.plain(m).strip():
            out[c] = m
    return out


def excluded_meaning_sources(e: dict, entries: list[dict], spec: dict) -> set[str]:
    """Entry ids a meaning distractor may never come from: this entry, its `related`, entries
    that relate to it, same-headword entries and (語彙) headwords sharing a kanji."""
    hw = headword(e, spec)
    ks = set(_KANJI.findall(hw)) if spec["headword"] != "kanji" else set()
    out = {e["id"]} | set(e.get("related") or [])
    for x in entries:
        xh = headword(x, spec)
        if (e["id"] in (x.get("related") or []) or xh == hw
                or (ks and ks & set(_KANJI.findall(xh)))):
            out.add(x["id"])
    return out


def _meaning_item(e, spec, entries, prose):
    mine = meanings(prose, e["id"])
    prim = langs.primary()
    if prim not in mine:
        return None
    q = qid(e["id"], "meaning")
    skip = excluded_meaning_sources(e, entries, spec)
    cands = []
    for x in entries:
        if x["id"] in skip:
            continue
        theirs = meanings(prose, x["id"])
        if not all(c in theirs and D.plain(theirs[c]).strip() != D.plain(mine[c]).strip() for c in mine):
            continue
        same_pos = bool(e.get("pos")) and x.get("pos") == e.get("pos")
        cands.append((not same_pos, _h(q, x["id"]), x, theirs))
    cands.sort(key=lambda t: t[:2])
    pick, texts = [], {c: {D.plain(mine[c]).strip()} for c in mine}
    for _, _, x, theirs in cands:
        if any(D.plain(theirs[c]).strip() in texts[c] for c in mine):
            continue
        for c in mine:
            texts[c].add(D.plain(theirs[c]).strip())
        pick.append({"owner": x["id"], "word": headword(x, spec), "text": {c: theirs[c] for c in mine}})
        if len(pick) == 3:
            break
    if len(pick) < 3:
        return None
    return {"qid": q, "id": e["id"], "kind": "meaning", "word": headword(e, spec),
            "reading": clean(to_hira(str(e.get(spec.get("reading") or "", "")))) if spec.get("reading") else "",
            "key": {c: mine[c] for c in mine}, "distractors": pick}


def generate(spec: dict, entries: list[dict], prose: dict) -> dict[str, list[dict]]:
    """{entry id: [generated items]} over the WHOLE category (every part), so a part page
    and the gate see the same items. An item: {qid, id, kind, word, key, options,
    answer (1-based), distractors: [{text, owner?/word? | kanji/as/is}]}."""
    kinds = types(spec)
    entries = [e for e in entries if isinstance(e, dict) and isinstance(e.get("id"), str)]
    if not kinds or spec.get("kind") != "item":
        return {}
    pairs = _pairs(entries, spec)
    by_kanji = {}
    if spec["headword"] == "kanji":
        for e in entries:
            k = str(e.get("kanji", ""))
            if len(k) == 1:
                by_kanji.setdefault(k, {"id": e["id"], "readings": _kanji_readings(e)})
    items = {k: [] for k in kinds}
    for e in entries:
        if "reading" in kinds:
            it = _reading_item(e, spec, pairs, by_kanji)
            if it:
                items["reading"].append(it)
        if "meaning" in kinds:
            it = _meaning_item(e, spec, entries, prose)
            if it:
                items["meaning"].append(it)
    out: dict[str, list[dict]] = {}
    for kind in kinds:
        for n, it in enumerate(sorted(items[kind], key=lambda t: _h(t["qid"]))):
            a = n % 4 + 1
            ds = [d["text"] for d in it["distractors"]]
            it["options"] = ds[:a - 1] + [it["key"]] + ds[a - 1:]
            it["answer"] = a
        for it in items[kind]:
            out.setdefault(it["id"], []).append(it)
    for eid in out:
        out[eid].sort(key=lambda t: list(KINDS).index(t["kind"]))
    return out

