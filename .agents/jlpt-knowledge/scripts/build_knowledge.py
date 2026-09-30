#!/usr/bin/env python3
"""Build the knowledge module's pages: knowledge/<LEVEL>/<category>.html + index.html
(+ knowledge/<LEVEL>/<category>/<part>.html for a split category).

    python3 .agents/jlpt-knowledge/scripts/build_knowledge.py [--level N2]     # make knowledge [LEVEL=N2]

One page per category in references/categories.json, whether or not it has
content yet (an empty one says 準備中), and the category index. A category in the
split layout (<stem>/<part>.json) gets one card page PER PART instead, and its
category page becomes a short list of the parts — so no page has to embed the
whole category (jlpt-knowledge/SKILL.md §Page). Every page is
self-contained (inline CSS/JS; the Google Fonts link the other pages use) so the
same files work from `make serve`, the Pages build and file://.

What is rendered where (jlpt-knowledge/SKILL.md §Page):
- Cards are listed in BOOK ORDER (knowledge_data.book_sorted, SKILL §Book order),
  and nothing on the page reorders them: search and the filters only narrow the
  list, and the group filter lists its groups in the same order. The quiz alone
  shuffles.
- Python renders every card and every quiz item to HTML once — furigana through
  exam-model-answer's apply_furigana(), every language as a `.lang-pane` — and
  embeds them as data. The page inserts cards 50 at a time as the reader
  scrolls, so a 2,500-card category opens as fast as a 20-card one, and filters
  and search run over a small per-entry index instead of the DOM.
- Language: the registry (langs.order()) decides the panes; the page's top is
  lang_ui's one sticky bar (breadcrumb level › 知識 › category, and the language
  dropdown), whose choice is the site-wide LANG_STORE_KEY. No language code is
  written in this file.
- Progress (覚えた, quiz history) goes through local_store.JLPTKnowledgeStore — the
  one place its localStorage keys are spelled.

Missing prose never blanks a card: a language with no entry for an id shows the
primary language's prose under a one-line note, and a card with no prose at all
still shows its shared material. `make check` WARNs on both.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / ".agents" / "exam-model-answer" / "scripts"))
sys.path.insert(0, str(ROOT / ".agents" / "exam-app" / "scripts"))

import knowledge_data as D            # noqa: E402
import langs                      # noqa: E402
import build_model_answer as BMA  # noqa: E402  (apply_furigana, EXPLANATION_CSS)
import lang_ui                    # noqa: E402  (the one sticky bar + language dropdown)
import app_style                  # noqa: E402
import local_store                # noqa: E402
import quiz_gen                   # noqa: E402  (generated 語彙/漢字 quiz items)

# Pitch accent: an optional dataset module (references/pitch/, its own owner).
# Absent or broken -> no pitch lines at all; the page never guesses one.
try:
    import pitch as PITCH         # noqa: E402  lookup(word, reading) -> list[int] | None
except Exception:                 # noqa: BLE001 — any import failure means "no dataset"
    PITCH = None
PITCH_ATTRIBUTION = HERE.parent / "references" / "pitch" / "ATTRIBUTION.txt"

NS = "knowledge"
PAGE_SIZE = 50
RATE_SLOW = 0.7          # speechSynthesis rate of the ゆっくり setting
PRIMARY = langs.primary()
ORDER = langs.order()
UI = langs.ui_table(NS)
ITEM_PROSE = ("meaning", "usage", "nuance", "compare")

FONTS = lang_ui.FONT_TAGS   # the one font link every page loads (lang_ui owns it)


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def fu(s) -> str:
    """Escape, then turn ｜漢字《かな》 into <ruby>. The markup survives escaping."""
    return BMA.apply_furigana(esc(s or ""))


def label(key: str, tag: str = "span", **fmt) -> str:
    """A UI label in every active language, one `.lang-pane` each."""
    def one(c):
        s = UI.get(c, {}).get(key) or UI[PRIMARY].get(key, key)
        return esc(s.format(**fmt) if fmt else s)
    if len(ORDER) == 1:
        return one(ORDER[0])
    return "".join(f'<{tag} class="lang-pane" data-lang="{c}">{one(c)}</{tag}>' for c in ORDER)


# Card chrome repeats on every card (2,500 in 語彙), so a card carries a token
# where a label or the ▶ button's aria text goes, and the page expands it from
# one table on insertion — the same markup, stored once. The token characters are
# Private Use Area code points, which no authored text contains.
TOK_OPEN, TOK_CLOSE = "\ue000", "\ue001"


def tok(key: str) -> str:
    return f"{TOK_OPEN}{key}{TOK_CLOSE}"


def token_table() -> dict[str, str]:
    keys = ("learned", "field_examples", "field_sources", "field_related",
            *(k for k in UI[PRIMARY] if k.startswith("field_")))
    t = {k: label(k) for k in dict.fromkeys(keys)}
    t["say_aria"] = esc(" / ".join(dict.fromkeys(UI[c].get("speak", "") for c in ORDER
                                                  if UI[c].get("speak"))))
    return t


def panes(render, tag: str = "div") -> str:
    """`render(code)` per active language, each wrapped in a `.lang-pane`."""
    if len(ORDER) == 1:
        return render(ORDER[0])
    return "".join(f'<{tag} class="lang-pane" data-lang="{c}">{render(c)}</{tag}>' for c in ORDER)


def portal_label(key: str, **fmt) -> str:
    """A portal-namespace label (the module's own name, 知識) in every language —
    the breadcrumb names the module the way the portal's module chooser does."""
    def one(c):
        s = langs.ui(c, "portal").get(key) or langs.ui(PRIMARY, "portal").get(key, key)
        return esc(s.format(**fmt) if fmt else s)
    return "".join(f'<span class="lang-pane" data-lang="{c}">{one(c)}</span>' for c in ORDER)


def crumbs(level: str, depth: int, trail: list[tuple[str, str | None]]) -> list:
    """level › 知識 › … for a page `depth` folders below knowledge/<LEVEL>/
    (0: the index and the category pages, 1: a split category's part pages).
    Relative links, explicit index.html: `make serve`, a Pages subpath, file://."""
    up = "../" * depth
    know = [(portal_label("mod_knowledge"), None if not trail else f"{up}{D.INDEX_HTML}")]
    home = (lang_ui.pane("portal", "crumb_home"), f"{up}../../{D.INDEX_HTML}")
    return [home, (esc(level), f"{up}../../{level}/{D.INDEX_HTML}")] + know + trail


def dup_control(render) -> str:
    """A control whose own text is language-bound (a placeholder, <option> labels)
    is rendered once per language; the page keeps the copies in sync by
    `data-ctl`. The same no-text-substitution rule as every label."""
    return panes(render, tag="span")


def cite(src: dict) -> str:
    ref = str(src.get("ref", ""))
    txt = Path(ref).name
    if src.get("page"):
        txt += f" p.{src['page']}"
    if src.get("note"):
        txt += f" — {src['note']}"
    return f'<span class="cite" title="{esc(ref)}">{fu(txt)}</span>'


def fact_value(v) -> str:
    if isinstance(v, list):
        return "・".join(fu(x) for x in v)
    return fu(v)


# ------------------------------------------------------------ pronunciation
# Speech: the page speaks through the browser's speechSynthesis (no audio files).
# It is handed the READING, never the kanji, so a voice cannot misread one: the
# furigana markup is resolved to its kana here, at build time.
_RUBY_BAR = re.compile(r"｜([^《》｜]+)《([^》]*)》")
_RUBY_KANJI = re.compile(r"([一-龥々〆ヶ]+)《([^》]*)》")


def speech_text(s: str) -> str:
    s = _RUBY_BAR.sub(r"\2", s or "")
    s = _RUBY_KANJI.sub(r"\2", s)
    s = s.replace("**", "").replace("｜", "")
    return re.sub(r"[〜～]", "", s).strip()


def say_btn(text: str) -> str:
    t = speech_text(text)
    if not t:
        return ""
    return (f'<button type="button" class="say" data-say="{esc(t)}" aria-label="{tok("say_aria")}" '
            f'title="{tok("say_aria")}">&#x25B6;&#xFE0E;</button>')


_SMALL = set("ゃゅょぁぃぅぇぉゎャュョァィゥェォヮ")
_KANA = re.compile(r"^[ぁ-ゖァ-ヺー]+$")


def morae(kana: str) -> list[str]:
    out: list[str] = []
    for ch in kana:
        if ch in _SMALL and out:
            out[-1] += ch
        else:
            out.append(ch)
    return out


def pitch_html(kana: str, drops) -> str:
    """The standard high/low line over the kana, one per accent the dataset lists.

    `drops` are accent-drop positions (0 heiban, 1 atamadaka, n = drop after the
    n-th mora). The trailing half-width slot is the particle, so 平板 and 尾高
    stay distinguishable. Borders, not colour fills: it prints and survives a
    theme change. Unknown (None, or kana the line cannot be drawn over) -> "".
    """
    if not drops or not kana or not _KANA.match(kana):
        return ""
    ms = morae(kana)
    lines = []
    for n in list(dict.fromkeys(d for d in drops if isinstance(d, int) and 0 <= d <= len(ms)))[:2]:
        hi = [(i > 0) if n == 0 else (i == 0) if n == 1 else (0 < i < n) for i in range(len(ms))]
        hi.append(n == 0)                                   # the particle slot
        cells = []
        for i, h in enumerate(hi):
            cls = ["pm", "h" if h else "l"]
            if i > 0 and h and not hi[i - 1]:
                cls.append("up")
            if i + 1 < len(hi) and h and not hi[i + 1]:
                cls.append("dn")
            if i == len(ms):
                cls.append("tail")
            cells.append(f'<span class="{" ".join(cls)}">{esc(ms[i]) if i < len(ms) else ""}</span>')
        lines.append(f'<span class="pitch" data-drop="{n}">{"".join(cells)}</span>')
    return "".join(lines)


class PitchUse:
    """Whether a page drew any line from the dataset (-> print its attribution)."""
    dataset = False


def pitch_for(word: str, reading: str, override=None) -> str:
    kana = speech_text(reading)
    if override is not None:
        return pitch_html(kana, override)
    if PITCH is None or not word or not kana:
        return ""
    try:
        drops = PITCH.lookup(word, kana)
    except Exception:  # noqa: BLE001 — a lookup failure is "unknown", never a guess
        drops = None
    out = pitch_html(kana, drops)
    if out:
        PitchUse.dataset = True
    return out


def pitch_footer() -> str:
    """The dataset's attribution, on every page that drew a line from it."""
    if not (PitchUse.dataset and PITCH_ATTRIBUTION.is_file()):
        return ""
    txt = esc(PITCH_ATTRIBUTION.read_text(encoding="utf-8").strip()).replace("\n", "<br>")
    return f'<footer class="credit"><b>{label("pitch_credit")}</b><br>{txt}</footer>'


def kanji_words_html(e: dict, spec: dict) -> str:
    """漢字 `words`: each compound with its ruby, its pitch line and a ▶."""
    ov = e.get("pitch") if isinstance(e.get("pitch"), dict) else {}
    cells = []
    for w in e.get("words", []) or []:
        plain_w = D.plain(w)
        line = pitch_for(plain_w, speech_text(w), ov.get(plain_w)) if spec.get("pitch") else ""
        cells.append(f'<span class="kw">{fu(w)}{line}{say_btn(w)}</span>')
    return "".join(cells)


# ------------------------------------------------------------------ one card
def prose_for(prose: dict, eid: str, code: str) -> tuple[dict, bool]:
    """(prose, fell_back) — a language without the entry borrows the primary's."""
    own = prose.get(code, {}).get(eid)
    if own:
        return own, False
    return prose.get(PRIMARY, {}).get(eid) or {}, code != PRIMARY


def title_html(spec: dict, e: dict, prose: dict) -> str:
    if spec["kind"] == "guide":
        return panes(lambda c: f'<span class="hw">{fu(prose_for(prose, e["id"], c)[0].get("title") or e["id"])}</span>',
                     tag="span")
    word = e.get(spec["headword"], "")
    hw = f'<span class="hw">{fu(word)}</span>'
    rk = spec.get("reading")
    reading = e.get(rk, "") if rk else ""
    line = ""
    if reading and (spec.get("pitch") or isinstance(e.get("pitch"), list)):
        line = pitch_for(D.plain(word), reading,
                         e.get("pitch") if isinstance(e.get("pitch"), list) else None)
    rd = f'<span class="rd">{line or fu(reading)}</span>' if reading else ""
    say = say_btn(reading) if reading else ""
    return hw + rd + say


def headword_plain(spec: dict, e: dict, prose: dict) -> str:
    if spec["kind"] == "guide":
        return D.plain(prose_for(prose, e["id"], PRIMARY)[0].get("title") or e["id"])
    return D.plain(str(e.get(spec["headword"], "")))


def card_html(spec: dict, e: dict, prose: dict, heads: dict, level: str,
              elsewhere: dict | None = None) -> str:
    """One card. `elsewhere` maps a related id that is NOT on this page (a split
    category's other part) to the page it is on; such a link navigates there
    with the card's anchor instead of scrolling this page."""
    eid = e["id"]
    elsewhere = elsewhere or {}
    out = [f'<article class="dcard" id="e-{esc(eid)}" data-id="{esc(eid)}">',
           '<div class="dc-head"><div class="dc-title">', title_html(spec, e, prose), '</div>',
           f'<button type="button" class="learn-btn" data-id="{esc(eid)}" aria-pressed="false">'
           f'{tok("learned")}</button></div>']
    facts = spec.get("facts", []) if spec["kind"] == "item" else []
    rows = [(f, e.get(f)) for f in facts if e.get(f)]
    if rows:
        out.append('<dl class="dc-facts">' + "".join(
            f'<div><dt>{tok("field_" + f)}</dt><dd>'
            f'{kanji_words_html(e, spec) if f == "words" else fact_value(v)}</dd></div>' for f, v in rows)
            + "</dl>")
    meta = []
    if e.get("group"):
        meta.append(f'<span class="tag grp">{esc(e["group"])}</span>')
    meta += [f'<span class="tag">{esc(t)}</span>' for t in e.get("tags", []) or []]
    if meta:
        out.append('<div class="dc-meta">' + "".join(meta) + "</div>")

    def body(c):
        pr, fb = prose_for(prose, eid, c)
        parts = [f'<p class="fb-note">{esc(UI[c].get("fallback_note", ""))}</p>'] if fb and pr else []
        if spec["kind"] == "guide":
            parts += [f"<p>{fu(p)}</p>" for p in pr.get("body", []) or []]
        else:
            dl = "".join(f'<div class="pr-{k}"><dt>{esc(UI[c].get("field_" + k, k))}</dt>'
                         f'<dd>{fu(pr.get(k))}</dd></div>' for k in ITEM_PROSE if pr.get(k))
            if dl:
                parts.append(f'<dl class="dc-prose">{dl}</dl>')
        return "".join(parts)
    out.append(f'<div class="dc-body">{panes(body)}</div>')

    exs = e.get("examples", []) or []
    if exs:
        lis = []
        for i, ex in enumerate(exs):
            notes = ""
            if len(ORDER) > 1:
                def note(c, i=i):
                    pr, fb = prose_for(prose, eid, c)
                    n = (pr.get("example_notes") or [])
                    return f'<div class="ex-note">{fu(n[i])}</div>' if not fb and i < len(n) and n[i] else ""
                notes = "".join(f'<div class="lang-pane" data-lang="{c}">{note(c)}</div>'
                                for c in ORDER if c != PRIMARY)
            lis.append(f'<li><div class="ex-ja">{fu(ex)}{say_btn(ex)}</div>{notes}</li>')
        out.append(f'<div class="dc-ex"><div class="dc-lbl">{tok("field_examples")}</div>'
                   f'<ol>{"".join(lis)}</ol></div>')

    rel = [r for r in e.get("related", []) or [] if r in heads]
    if rel:
        out.append(f'<div class="dc-rel"><span class="dc-lbl">{tok("field_related")}</span> ' + "".join(
            (f'<a href="{esc(elsewhere[r])}#e-{esc(r)}">{esc(heads[r])}</a>' if r in elsewhere else
             f'<a href="#e-{esc(r)}" data-goto="{esc(r)}">{esc(heads[r])}</a>') for r in rel) + "</div>")
    srcs = e.get("sources", []) or []
    if srcs:
        out.append(f'<div class="dc-src"><span class="dc-lbl">{tok("field_sources")}</span> '
                   + "".join(cite(s) for s in srcs if isinstance(s, dict)) + "</div>")
    out.append(f'<div class="dc-hist" data-id="{esc(eid)}"></div></article>')
    return "".join(out)


def quiz_items(spec: dict, entries: list[dict], prose: dict, heads: dict) -> list[dict]:
    out = []
    for ei, e in enumerate(entries):
        for n, q in enumerate(e.get("quiz", []) or [], start=1):
            opts = q.get("options") or []
            if len(opts) != 4 or not isinstance(q.get("answer"), int):
                continue      # the gate FAILs it; the page does not ship a broken item

            def expl(c, n=n):
                pr, fb = prose_for(prose, e["id"], c)
                xs = pr.get("quiz") or []
                return fu(xs[n - 1]) if n - 1 < len(xs) and xs[n - 1] else ""
            out.append({"qid": f'{e["id"]}#{n}', "e": ei, "id": e["id"],
                        "g": e.get("group", ""), "stem": fu(q.get("stem", "")),
                        "opts": [fu(o) for o in opts], "a": q["answer"],
                        "x": panes(expl), "from": esc(heads.get(e["id"], e["id"]))})
        for it in GEN.get(e["id"], []):
            out.append(gen_quiz_item(it, e, ei, prose, heads))
    return out


# Generated 語彙/漢字 items (quiz_gen.py): computed ONCE per category over every
# part by build_category(), so each part page ships the same items the gate checks.
GEN: dict[str, list[dict]] = {}


def _fmt(c: str, key: str, **vals) -> str:
    """A knowledge.json template, escaped, with pre-rendered HTML spliced into {slots}."""
    t = esc(UI.get(c, {}).get(key) or UI[PRIMARY].get(key, key))
    for k, v in vals.items():
        t = t.replace("{" + k + "}", v)
    return t


def gen_quiz_item(it: dict, e: dict, ei: int, prose: dict, heads: dict) -> dict:
    """One generated item as the page's quiz data: stem, options and explanation are
    rendered per language (`.lang-pane`), the key position is the same in every pane."""
    reading = it.get("reading") or ""
    word = (fu(f"｜{it['word']}《{reading}》") if reading and reading != it["word"] else esc(it["word"]))
    shown = f'<b class="gen-hw">{word}</b>'
    if it["kind"] == "reading":
        stem = panes(lambda c: _fmt(c, "gen_r_stem", w=shown), tag="span")
        opts = [esc(o) for o in it["options"]]

        def expl(c):
            m = prose_for(prose, e["id"], c)[0].get("meaning") or ""
            ps = [_fmt(c, "gen_r_key", r=esc(it["key"]), w=esc(it["word"]))]
            if m:
                ps.append(_fmt(c, "gen_meaning", m=fu(m)))
            for d in it["distractors"]:
                if "kanji" in d:
                    ps.append(_fmt(c, "gen_r_fake", d=esc(d["text"]), k=esc(d["kanji"]),
                                   s=esc(d["as"]), t=esc(d["is"])))
                else:
                    ps.append(_fmt(c, "gen_r_other", d=esc(d["text"]), w=esc(d["word"])))
            return "".join(f"<p>{p}</p>" for p in ps)
    else:
        stem = panes(lambda c: _fmt(c, "gen_m_stem", w=shown), tag="span")

        def pick(text: dict, c: str) -> str:
            return text[c] if c in it["key"] else text[PRIMARY]
        opts = [panes(lambda c, o=o: fu(pick(o, c) if isinstance(o, dict) else o), tag="span")
                for o in it["options"]]

        def expl(c):
            ps = [_fmt(c, "gen_m_key", w=word, m=fu(pick(it["key"], c)))]
            for d in it["distractors"]:
                ps.append(_fmt(c, "gen_m_other", m=fu(pick(d["text"], c)), w=esc(d["word"])))
            return "".join(f"<p>{p}</p>" for p in ps)
    return {"qid": it["qid"], "e": ei, "id": e["id"], "g": e.get("group", ""), "stem": stem,
            "opts": opts, "a": it["answer"], "x": panes(expl),
            "from": esc(heads.get(e["id"], e["id"]))}


# ------------------------------------------------------------------ page chrome
CSS = r"""
*{box-sizing:border-box}
:root{--primary:#1e3a8a;--card:#ffffff;--soft:#f1f5f9}
body{margin:0;background:#f8fafc;color:var(--ink);font-family:var(--ui);line-height:1.7}
ruby rt{font-size:.58em;color:var(--muted);user-select:none}
.wrap{max-width:82em;margin:0 auto;padding:1.8em 1.5em 5em}
.lead{color:var(--muted);margin:.2rem 0 1rem;font-size:.95rem}
.tabs{display:flex;gap:.4rem;margin:.4rem 0 1rem;border-bottom:1px solid var(--line)}
.tab-btn{border:none;background:none;font:inherit;font-weight:700;color:var(--muted);
  padding:.55rem 1rem;cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-1px}
.tab-btn.active{color:var(--primary);border-bottom-color:var(--accent)}
body[data-tab="study"] #quiz, body[data-tab="quiz"] #study{display:none}
.controls{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin-bottom:.8rem}
.controls input[type=search],.controls select{font:inherit;font-size:.92rem;border:1px solid var(--line);
  border-radius:6px;padding:.45rem .6rem;background:#fff;color:var(--ink);min-height:38px}
.controls input[type=search]{flex:1 1 16rem;min-width:0}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:6px;overflow:hidden}
.seg button{border:none;background:#fff;font:inherit;font-size:.88rem;padding:.4rem .75rem;cursor:pointer;color:var(--ink)}
.seg button+button{border-left:1px solid var(--line)}
.seg button.active{background:var(--accent);color:#fff;font-weight:700}
.stat{color:var(--muted);font-size:.88rem;font-variant-numeric:tabular-nums;margin:.2rem 0 .6rem}
.dcard{scroll-margin-top:calc(var(--tb-h) + .6rem);background:var(--card);border:1px solid #e2e8f0;border-radius:10px;padding:1rem 1.1rem;margin:0 0 .9rem;
  box-shadow:0 1px 3px rgba(0,0,0,.03);scroll-margin-top:4.5rem}
.dcard.learned{border-left:4px solid #059669}
.dcard.flash{box-shadow:0 0 0 3px rgba(37,99,235,.35)}
.dc-head{display:flex;justify-content:space-between;align-items:flex-start;gap:.8rem}
.dc-title{display:flex;flex-wrap:wrap;align-items:baseline;gap:.2rem .8rem}
.hw{font-family:var(--serif);font-size:1.35rem;font-weight:700;color:#0f172a}
.rd{color:var(--muted);font-size:.95rem}
.learn-btn{flex:0 0 auto;font:inherit;font-size:.82rem;font-weight:700;border:1px solid var(--line);background:#fff;
  color:var(--muted);border-radius:9999px;padding:.25rem .8rem;cursor:pointer;min-height:32px}
.learn-btn[aria-pressed="true"]{background:#ecfdf5;border-color:#a7f3d0;color:#065f46}
.dc-facts,.dc-prose{margin:.5rem 0 0}
.dc-facts div,.dc-prose div{display:grid;grid-template-columns:6.5em 1fr;gap:.6rem;padding:.12rem 0}
.dc-facts dt,.dc-prose dt{font-size:.8rem;font-weight:700;color:var(--primary);padding-top:.2rem}
.dc-facts dd,.dc-prose dd{margin:0}
.dc-prose .pr-meaning dd{font-weight:700}
.dc-meta{display:flex;flex-wrap:wrap;gap:.3rem;margin:.45rem 0 0}
.tag{font-size:.75rem;background:var(--soft);color:#334155;border-radius:4px;padding:.05rem .45rem}
.tag.grp{background:#e0e7ff;color:#3730a3}
.tag.off{background:#fef3c7;color:#92400e}
.fb-note{font-size:.8rem;color:#92400e;background:#fffbeb;border-radius:4px;padding:.2rem .5rem;margin:.5rem 0 0}
.dc-body p{margin:.5rem 0}
.dc-lbl{font-size:.8rem;font-weight:700;color:var(--primary)}
.dc-ex{margin-top:.6rem}
.dc-ex ol{margin:.25rem 0 0;padding-left:1.4rem}
.dc-ex li{margin:.3rem 0}
.ex-ja{font-family:var(--serif)}
.ex-note{font-size:.88rem;color:#475569}
.dc-rel,.dc-src{margin-top:.5rem;font-size:.82rem}
.dc-rel a{margin-right:.6rem;color:var(--accent)}
.cite{color:var(--muted);margin-right:.7rem}
.dc-hist{font-size:.78rem;color:var(--muted);margin-top:.3rem}
.dc-hist:empty{display:none}
.more{text-align:center;margin:1rem 0}
.empty{color:var(--muted);text-align:center;padding:2rem 0}
/* pronunciation: ▶ buttons appear only once a Japanese voice is found (body.tts) */
.say,.tts-only{display:none}
body.tts .say{display:inline-flex}
body.tts .tts-only{display:inline-flex}
.say{align-items:center;justify-content:center;width:1.7em;height:1.7em;margin:0 .3em;vertical-align:middle;
  border:1px solid var(--line);border-radius:9999px;background:#fff;color:var(--accent);font-size:.7rem;cursor:pointer;padding:0}
.say:hover{border-color:var(--accent)}
.pitch{display:inline-flex;align-items:stretch;margin-right:.35em;line-height:1.35;padding:1px 0;font-size:.95rem}
.pm{border:0 solid var(--pitch,#b91c1c);padding:0 .04em}
.pm.h{border-top-width:2px}
.pm.l{border-bottom-width:2px}
.pm.up{border-left-width:2px}
.pm.dn{border-right-width:2px}
.pm.tail{min-width:.5em}
.kw{display:inline-flex;align-items:center;margin:0 .9em .2em 0;flex-wrap:wrap}
.kw .pitch{margin-left:.3em}
footer.credit{max-width:60rem;margin:0 auto;padding:0 1rem 2rem;color:var(--muted);font-size:.75rem}
/* quiz */
.qbox{background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:1.1rem 1.2rem}
.qhead{display:flex;justify-content:space-between;color:var(--muted);font-size:.85rem;font-variant-numeric:tabular-nums}
.qstem{font-family:var(--serif);font-size:1.12rem;margin:.6rem 0 .9rem}
.qopts{display:grid;gap:.5rem}
.qopt{text-align:left;font:inherit;font-family:var(--serif);border:1px solid var(--line);background:#fff;border-radius:8px;
  padding:.6rem .8rem;cursor:pointer;color:var(--ink)}
.qopt:hover:not(:disabled){border-color:var(--accent)}
.qopt:disabled{cursor:default}
.qopt.right{background:#ecfdf5;border-color:#34d399}
.qopt.wrong{background:#fef2f2;border-color:#f87171}
.qopt b{font-family:var(--ui);margin-right:.5rem;color:var(--muted)}
.verdict{margin-top:.9rem}
.verdict .v{font-weight:800}
.verdict .v.ok{color:#065f46}.verdict .v.ng{color:#991b1b}
.verdict .from{font-size:.85rem;margin-top:.4rem}
.qsetup{display:grid;gap:.7rem;background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:1.1rem 1.2rem}
.qsetup .row{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}
.qsetup .row>.k{min-width:6em;font-weight:700;font-size:.88rem;color:var(--primary)}
.qresult{text-align:center}
.qresult .big{font-size:2rem;font-weight:800;font-variant-numeric:tabular-nums}
.qactions{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:flex-end;margin-top:.9rem}
.qresult .qactions{justify-content:center}
/* index */
.cats{display:grid;grid-template-columns:repeat(auto-fill,minmax(16rem,1fr));gap:.9rem}
.cat{display:block;background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:1rem 1.1rem;color:inherit;
  text-decoration:none;transition:all .15s ease}
a.cat:hover{border-color:var(--accent);box-shadow:0 2px 8px rgba(37,99,235,.12)}
.cat.off{opacity:.6}
.cat h2{margin:0 0 .2rem;font-size:1.2rem}
.cat p{margin:0;color:var(--muted);font-size:.88rem}
.cat .n{margin-top:.6rem;font-size:.85rem;font-variant-numeric:tabular-nums}
@media (max-width:40em){
  .wrap{padding:.8rem .75rem 3rem}
  .dc-facts div,.dc-prose div{grid-template-columns:1fr;gap:0}
  .hw{font-size:1.2rem}
}
@media print{
  .tabs,.controls,.learn-btn,.more,#quiz,.say{display:none!important}
  .pm{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  body{background:#fff}
  .dcard{scroll-margin-top:calc(var(--tb-h) + .6rem);box-shadow:none;break-inside:avoid;page-break-inside:avoid}
}
"""

PAGE_JS = r"""
function ctlValue(name){ const el = document.querySelector('[data-ctl="'+name+'"]'); return el ? el.value : ''; }
function syncCtl(src){
  document.querySelectorAll('[data-ctl="'+src.dataset.ctl+'"]').forEach(el => { if (el !== src) el.value = src.value; });
}
const S = window.JLPTKnowledgeStore;
let learned = S.learned(LEVEL, CAT);
let hist = S.history(LEVEL, CAT);
const state = {status: 'all', list: [], shown: 0};

function histText(id){
  let n = 0, ok = 0;
  Q.forEach(q => { if (q.id === id && hist[q.qid]) { n += hist[q.qid].n; ok += hist[q.qid].ok; } });
  return n ? L.quiz_history + ' ' + ok + ' / ' + n : '';
}
function paintCard(el){
  const id = el.dataset.id, on = !!learned[id];
  el.classList.toggle('learned', on);
  const b = el.querySelector('.learn-btn'); if (b) b.setAttribute('aria-pressed', on ? 'true' : 'false');
  const h = el.querySelector('.dc-hist'); if (h) h.innerHTML = histText(id);
}
function learnedCount(){ return E.filter(e => learned[e.id]).length; }
function paintHeader(){
  document.querySelectorAll('.js-learned').forEach(x => x.textContent = learnedCount());
}
/* The search index is the card's own text (headword, ruby readings, examples,
   every language's prose — not its related links or citations), derived on
   first use rather than shipped twice. */
function searchText(e){
  if (e.s === undefined) e.s = e.html.replace(/<div class="dc-(rel|src)">.*?<\/div>/g, ' ')
                                     .replace(/\ue000\w+\ue001/g, ' ').replace(/<[^>]*>/g, ' ')
                                     .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
                                     .replace(/&quot;/g, '"').replace(/&#x27;/g, "'").toLowerCase();
  return e.s;
}
function matches(e, q, g, t, o){
  if (g && e.g !== g) return false;
  if (t && !(e.t || []).includes(t)) return false;
  if (o === 'yes' && !(e.oc > 0)) return false;
  if (state.status === 'todo' && learned[e.id]) return false;
  if (state.status === 'done' && !learned[e.id]) return false;
  if (q) { const s = searchText(e); for (const w of q.split(/\s+/)) if (w && s.indexOf(w) < 0) return false; }
  return true;
}
function refresh(){
  if (!document.getElementById('cards')) return;          // an empty (準備中) category
  const q = (ctlValue('q') || '').trim().toLowerCase();
  const g = ctlValue('group'), t = ctlValue('tag'), o = ctlValue('official');
  const list = E.map((e, i) => i).filter(i => matches(E[i], q, g, t, o));   // E is in book order
  state.list = list; state.shown = 0;
  document.getElementById('cards').innerHTML = '';
  more();
  document.querySelectorAll('.js-hits').forEach(x => x.textContent = list.length);
  document.getElementById('nomatch').hidden = list.length > 0 || E.length === 0;
}
function more(until){
  const box = document.getElementById('cards');
  if (!box) return;
  const end = Math.min(state.list.length, Math.max(state.shown + PAGE, until || 0));
  const frag = document.createElement('div');
  frag.innerHTML = state.list.slice(state.shown, end).map(i => E[i].html.replace(TOK, (m, k) => T[k] || '')).join('');
  Array.from(frag.children).forEach(el => { paintCard(el); box.appendChild(el); });
  state.shown = end;
  document.getElementById('more').hidden = state.shown >= state.list.length;
}
function goTo(id){
  let pos = state.list.findIndex(i => E[i].id === id);
  if (pos < 0) {
    document.querySelectorAll('[data-ctl]:not([data-ctl^="qz-"])').forEach(el => { el.value = el.tagName === 'SELECT' ? el.options[0].value : ''; });
    setStatus('all', true); refresh();
    pos = state.list.findIndex(i => E[i].id === id);
  }
  if (pos < 0) return;
  if (pos >= state.shown) more(pos + 1);
  setTab('study');
  const el = document.getElementById('e-' + id);
  if (el) { el.scrollIntoView({block: 'start'}); el.classList.add('flash'); setTimeout(() => el.classList.remove('flash'), 1400); }
}
function setStatus(s, quiet){
  state.status = s;
  document.querySelectorAll('[data-status]').forEach(b => b.classList.toggle('active', b.dataset.status === s));
  if (!quiet) refresh();
}
function setTab(t){
  document.body.dataset.tab = t;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.toggle('active', b.dataset.tab === t));
}
document.addEventListener('click', ev => {
  const lb = ev.target.closest('.learn-btn');
  if (lb) { const id = lb.dataset.id; learned = S.setLearned(LEVEL, CAT, id, !learned[id]);
            paintCard(lb.closest('.dcard')); paintHeader(); return; }
  const go = ev.target.closest('[data-goto]');
  if (go) { ev.preventDefault(); goTo(go.dataset.goto); }
});
document.addEventListener('input', ev => {
  if (ev.target.dataset && ev.target.dataset.ctl) { syncCtl(ev.target); if (!ev.target.dataset.ctl.startsWith('qz-')) refresh(); }
});
document.addEventListener('change', ev => {
  if (ev.target.dataset && ev.target.dataset.ctl) { syncCtl(ev.target); if (!ev.target.dataset.ctl.startsWith('qz-')) refresh(); }
});


/* ---- speech (browser speechSynthesis; the text is already kana) ---- */
const TTS = {voice: null, rate: 1};
function pickVoice(){
  if (!('speechSynthesis' in window)) return;
  const vs = window.speechSynthesis.getVoices() || [];
  const v = vs.find(x => /^ja[-_]JP$/i.test(x.lang)) || vs.find(x => /^ja\b/i.test(x.lang));
  if (v) { TTS.voice = v; document.body.classList.add('tts'); }
}
function say(text){
  if (!TTS.voice || !text) return;
  const s = window.speechSynthesis; s.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'ja-JP'; u.voice = TTS.voice; u.rate = TTS.rate; s.speak(u);
}
function setRate(r, persist){
  TTS.rate = r;
  document.querySelectorAll('[data-rate]').forEach(b => b.classList.toggle('active', parseFloat(b.dataset.rate) === r));
  if (persist) { const p = S.prefs(); p.rate = r; S.setPrefs(p); }
}
document.addEventListener('click', ev => {
  const b = ev.target.closest('.say'); if (b) { ev.preventDefault(); ev.stopPropagation(); say(b.dataset.say); }
}, true);
document.addEventListener('DOMContentLoaded', () => {
  const r = parseFloat(S.prefs().rate); setRate(r === RATE_SLOW ? RATE_SLOW : 1, false);
  if ('speechSynthesis' in window) {
    pickVoice();
    const s = window.speechSynthesis;
    if (s.addEventListener) s.addEventListener('voiceschanged', pickVoice); else s.onvoiceschanged = pickVoice;
  }
});

/* ---- quiz ---- */
const qz = {pool: [], i: 0, score: 0, wrong: [], answered: false, last: []};
function shuffle(a){ for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
function quizPool(){
  const g = ctlValue('qz-group'), st = ctlValue('qz-status'), n = ctlValue('qz-n');
  let p = Q.map((q, i) => i).filter(i => {
    const q = Q[i];
    if (g && q.g !== g) return false;
    if (st === 'todo' && learned[q.id]) return false;
    if (st === 'missed' && !(hist[q.qid] && hist[q.qid].last === 0)) return false;
    return true;
  });
  shuffle(p);
  if (n !== 'all') p = p.slice(0, parseInt(n, 10));
  return p;
}
function quizView(which){
  ['qz-setup', 'qz-run', 'qz-done'].forEach(id => { const el = document.getElementById(id); if (el) el.hidden = id !== which; });
}
function startQuiz(pool){
  qz.pool = pool || quizPool(); qz.i = 0; qz.score = 0; qz.wrong = [];
  document.getElementById('qz-nomatch').hidden = qz.pool.length > 0;
  if (!qz.pool.length) return;
  quizView('qz-run'); showQ();
}
function showQ(){
  const q = Q[qz.pool[qz.i]]; qz.answered = false;
  document.getElementById('qz-pos').textContent = (qz.i + 1) + ' / ' + qz.pool.length;
  document.getElementById('qz-score').textContent = qz.score;
  document.getElementById('qz-stem').innerHTML = q.stem;
  document.getElementById('qz-opts').innerHTML = q.opts.map((o, k) =>
    '<button type="button" class="qopt" data-k="' + (k + 1) + '"><b>' + (k + 1) + '</b>' + o + '</button>').join('');
  document.getElementById('qz-verdict').hidden = true;
  document.getElementById('qz-next').hidden = true;
}
function choose(k){
  if (qz.answered) return; qz.answered = true;
  const q = Q[qz.pool[qz.i]], ok = k === q.a;
  if (ok) qz.score++; else qz.wrong.push(qz.pool[qz.i]);
  hist = Object.assign({}, hist); hist[q.qid] = S.record(LEVEL, CAT, q.qid, ok);
  document.querySelectorAll('#qz-opts .qopt').forEach(b => {
    const kk = parseInt(b.dataset.k, 10); b.disabled = true;
    if (kk === q.a) b.classList.add('right'); else if (kk === k) b.classList.add('wrong');
  });
  const v = document.getElementById('qz-verdict');
  v.innerHTML = '<div class="v ' + (ok ? 'ok' : 'ng') + '">' + (ok ? L.quiz_correct : L.quiz_wrong)
    + (ok ? '' : ' — ' + L.quiz_answer_is + ' ' + q.a) + '</div>'
    + '<div class="exp-content">' + q.x + '</div>'
    + '<div class="from">' + L.quiz_from + ': <a href="#e-' + q.id + '" data-goto="' + q.id + '">' + q.from + '</a></div>';
  v.hidden = false;
  document.getElementById('qz-score').textContent = qz.score;
  const nx = document.getElementById('qz-next');
  nx.innerHTML = qz.i + 1 < qz.pool.length ? L.quiz_next : L.quiz_finish; nx.hidden = false;
  document.querySelectorAll('.dcard[data-id="' + q.id + '"]').forEach(paintCard);
}
function nextQ(){
  if (qz.i + 1 < qz.pool.length) { qz.i++; showQ(); return; }
  qz.last = qz.pool.slice();
  document.getElementById('qz-final').textContent = qz.score + ' / ' + qz.pool.length;
  document.getElementById('qz-retry-wrong').hidden = !qz.wrong.length;
  quizView('qz-done');
}
document.addEventListener('click', ev => {
  const o = ev.target.closest('.qopt'); if (o) { choose(parseInt(o.dataset.k, 10)); return; }
  const a = ev.target.closest('[data-qz]'); if (!a) return;
  const act = a.dataset.qz;
  if (act === 'start') startQuiz();
  else if (act === 'next') nextQ();
  else if (act === 'quit' || act === 'setup') quizView('qz-setup');
  else if (act === 'retry') startQuiz(shuffle(qz.last.slice()));
  else if (act === 'retry-wrong') startQuiz(shuffle(qz.wrong.slice()));
});

document.addEventListener('DOMContentLoaded', () => {
  setTab('study'); refresh(); paintHeader();
  const s = document.getElementById('sentinel');
  if (s && 'IntersectionObserver' in window) {
    new IntersectionObserver(es => { if (es.some(x => x.isIntersecting) && state.shown < state.list.length) more(); },
                             {rootMargin: '800px'}).observe(s);
  }
  if (location.hash.startsWith('#e-')) goTo(decodeURIComponent(location.hash.slice(3)));
});
"""


def js_data(obj) -> str:
    """JSON safe to embed inside <script> (no `</script>` break-out)."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def page(level: str, title: str, trail: list, body: str,
         stamps: str, scripts: str, footer: str = "") -> str:
    """`trail` = the breadcrumb (see crumbs()); the bar is lang_ui's."""
    return f"""<!DOCTYPE html>
<html lang="{esc(langs.html_lang(PRIMARY))}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
{FONTS}
<style>{app_style.APP_CSS}{BMA.EXPLANATION_CSS}
{lang_ui.head_css()}
{CSS}</style>
</head>
{lang_ui.body_open('data-tab="study"')}{stamps}
{lang_ui.topbar_html(trail)}
{body}{footer}
<script>
{local_store.KNOWLEDGE_STORE_JS}
{scripts}
</script>
</body>
</html>
"""


def seg_status() -> str:
    return ('<span class="seg">' + "".join(
        f'<button type="button" data-status="{k}" onclick="setStatus(\'{k}\')">{label(lk)}</button>'
        for k, lk in (("all", "filter_all"), ("todo", "filter_todo"), ("done", "filter_done")))
        + "</span>")


def select(ctl: str, options: list[tuple[str, str | None, str]]) -> str:
    """options: (value, label key or None, literal text). One <select> per language."""
    def one(c):
        opts = "".join(
            f'<option value="{esc(v)}">{esc((UI[c].get(k) or UI[PRIMARY].get(k, k)) if k else t)}</option>'
            for v, k, t in options)
        return f'<select data-ctl="{ctl}">{opts}</select>'
    return dup_control(one)


def part_label(part: D.Part) -> str:
    """A part's display name: the shared file's own `part` field, else its file name."""
    try:
        lab = D.read_json(part.shared).get("part")
    except (OSError, ValueError, AttributeError):
        lab = None
    return lab if isinstance(lab, str) and lab.strip() else part.name


def build_category(level: str, spec: dict) -> list[Path]:
    """Single layout: ONE page with every card. Split layout: one page per part
    (`<stem>/<part>.html`, only that part's cards and quiz items — a 2,500-word
    語彙 as one page would embed ~11 MB) plus the category page listing the parts."""
    cat = D.locate(level, spec)
    entries, prose = D.load_entries(cat)
    # Book order (SKILL §Book order): every page lists its cards in the order of the
    # book the category follows, whatever order the data files hold them in. No
    # control reorders them — search and filters only narrow the list.
    entries = D.book_sorted(spec, [e for e in entries if isinstance(e.get("id"), str)], level)
    GEN.clear()
    GEN.update(quiz_gen.generate(spec, entries, prose))   # whole category, before any part
    heads = {e["id"]: headword_plain(spec, e, prose) for e in entries}
    # Part pages are build output beside the part data: drop any whose part is gone
    # (or every one, once the category is no longer split).
    keep = {p.name for p in cat.parts} if cat.layout == "split" else set()
    sub = D.level_dir(level) / spec["stem"]
    for old in (sorted(sub.glob("*.html")) if sub.is_dir() else []):
        if old.stem not in keep:
            old.unlink()
    if cat.layout != "split":
        return [render_cards(level, spec, entries, prose, heads, D.page_path(level, spec["stem"]),
                             crumbs(level, 0, [(label(spec["label"]), None)]), cat.sources())]
    where = {e["id"]: e["_part"] for e in entries}
    outs = []
    for part in cat.parts:
        mine = [e for e in entries if e["_part"] == part.name]
        elsewhere = {i: f"{p}.html" for i, p in where.items() if p != part.name}
        trail = crumbs(level, 1, [(label(spec["label"]), f"../{D.page_path(level, spec['stem']).name}"),
                                  (fu(part_label(part)), None)])
        outs.append(render_cards(level, spec, mine, prose, heads,
                                 D.part_page_path(level, spec["stem"], part.name),
                                 trail, D.part_page_sources(cat, part), part=part_label(part),
                                 elsewhere=elsewhere))
    outs.append(build_parts_index(level, spec, cat, entries))
    return outs


PARTS_JS = r"""
document.addEventListener('DOMContentLoaded', () => {
  const got = window.JLPTKnowledgeStore.learned(LEVEL, CAT);
  let total = 0;
  document.querySelectorAll('[data-part]').forEach(el => {
    const n = (PIDS[el.dataset.part] || []).filter(id => got[id]).length; total += n;
    const x = el.querySelector('.js-learned'); if (x) x.textContent = n;
  });
  document.querySelectorAll('.js-learned-total').forEach(x => x.textContent = total);
});
"""


def build_parts_index(level: str, spec: dict, cat: D.Category, entries: list[dict]) -> Path:
    """A split category's own page: its parts, each with its entry and 覚えた counts.
    覚えた and quiz history stay keyed per CATEGORY, so every part page and this
    list read one store."""
    stem = spec["stem"]
    pids = {p.name: [e["id"] for e in entries if e["_part"] == p.name] for p in cat.parts}
    cards = []
    for p in cat.parts:
        n = len(pids[p.name])
        inner = (f'<h2>{fu(part_label(p))}</h2>'
                 f'<div class="n">{n} {label("entries")} · {label("learned")} '
                 f'<span class="js-learned">0</span> / {n}</div>')
        if n:
            cards.append(f'<a class="cat" href="{esc(stem)}/{esc(p.name)}.html" '
                         f'data-part="{esc(p.name)}">{inner}</a>')
        else:
            cards.append(f'<div class="cat off" aria-disabled="true">{inner}</div>')
    name = UI[PRIMARY].get(spec["label"], stem)
    title = f"{level} {name}"
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + label(spec["label"]), label(spec["desc"]))
            + f'<main class="wrap"><p class="lead">{label("parts_lead")}</p>'
            f'<div class="stat">{len(entries)} {label("entries")} · {label("learned")} '
            f'<span class="js-learned-total">0</span> / {len(entries)}</div>'
            f'<div class="cats">{"".join(cards)}</div></main>')
    scripts = (f"const LEVEL = {js_data(level)}, CAT = {js_data(stem)};\n"
               f"const PIDS = {js_data(pids)};\n{PARTS_JS}")
    out = D.page_path(level, stem)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(level, title, crumbs(level, 0, [(label(spec["label"]), None)]), body,
                        D.src_sha_comments(level, D.category_page_sources(cat)), scripts),
                   encoding="utf-8")
    return out


def render_cards(level: str, spec: dict, entries: list[dict], prose: dict, heads: dict,
                 out: Path, trail: list, sources: list[Path],
                 part: str | None = None, elsewhere: dict | None = None) -> Path:
    """The study + quiz page over `entries` (a whole category, or one part of it);
    `trail` is its breadcrumb (crumbs())."""
    PitchUse.dataset = False
    E = [{"id": e["id"], "g": e.get("group", ""), "t": e.get("tags", []) or [],
          "oc": int(e.get("official_count") or 0),
          "html": card_html(spec, e, prose, heads, level, elsewhere)} for e in entries]
    Q = quiz_items(spec, entries, prose, heads)
    groups = list(dict.fromkeys(e["g"] for e in E if e["g"]))
    tags = list(dict.fromkeys(t for e in E for t in e["t"]))
    has_oc = any(e["oc"] for e in E)
    L = {k: label(k) for k in ("quiz_correct", "quiz_wrong", "quiz_answer_is", "quiz_next",
                               "quiz_finish", "quiz_from", "quiz_history")}
    name = UI[PRIMARY].get(spec["label"], spec["stem"])
    title = f"{level} {name}" + (f" — {D.plain(part)}" if part else "")

    def search_box(c):
        return (f'<input type="search" data-ctl="q" placeholder="{esc(UI[c].get("search_placeholder", ""))}" '
                f'aria-label="{esc(UI[c].get("search_placeholder", ""))}">')
    ctl = [dup_control(search_box)]
    if groups:
        ctl.append(select("group", [("", "filter_group_all", "")] + [(g, None, g) for g in groups]))
    if tags:
        ctl.append(select("tag", [("", "filter_tag_all", "")] + [(t, None, t) for t in tags]))
    if has_oc:
        ctl.append(select("official", [("", "filter_official_all", ""), ("yes", "filter_official", "")]))
    ctl.append(seg_status())
    ctl.append(f'<span class="seg tts-only" role="group" aria-label="{esc(UI[PRIMARY].get("speed", ""))}">'
               + "".join(f'<button type="button" data-rate="{r}" onclick="setRate({r}, true)">{label(k)}</button>'
                         for r, k in ((1, "speed_normal"), (RATE_SLOW, "speed_slow"))) + "</span>")

    if not E:
        study = f'<p class="empty">{label("empty_category")}</p>'
    else:
        study = (f'<div class="controls">{"".join(ctl)}</div>'
                 f'<div class="stat"><span class="js-hits">{len(E)}</span> {label("shown")} · '
                 f'{label("learned")} <span class="js-learned">0</span> / {len(E)}</div>'
                 f'<div id="cards"></div><p class="empty" id="nomatch" hidden>{label("no_match")}</p>'
                 f'<div class="more"><button type="button" class="ui-btn" id="more" onclick="more()" hidden>'
                 f'{label("load_more")}</button></div><div id="sentinel"></div>')
    if not Q:
        quiz = f'<p class="empty">{label("quiz_none")}</p>'
    else:
        counts = [n for n in (10, 20, 50) if n < len(Q)]
        qopts_n = [(str(n), None, str(n)) for n in counts] + [("all", "quiz_all", "")]
        rows = []
        if groups:
            rows.append(f'<div class="row"><span class="k">{label("quiz_scope")}</span>'
                        + select("qz-group", [("", "filter_group_all", "")] + [(g, None, g) for g in groups])
                        + "</div>")
        rows.append(f'<div class="row"><span class="k">{label("quiz_which")}</span>'
                    + select("qz-status", [("", "quiz_status_all", ""), ("todo", "quiz_status_todo", ""),
                                           ("missed", "quiz_status_missed", "")]) + "</div>")
        rows.append(f'<div class="row"><span class="k">{label("quiz_n")}</span>'
                    + select("qz-n", qopts_n) + "</div>")
        quiz = (f'<div id="qz-setup" class="qsetup"><p class="lead">{label("quiz_intro")} '
                f'({len(Q)} {label("quiz_count")})</p>{"".join(rows)}'
                f'<p class="empty" id="qz-nomatch" hidden>{label("quiz_empty_selection")}</p>'
                f'<div class="qactions"><button type="button" class="ui-btn primary" data-qz="start">'
                f'{label("quiz_start")}</button></div></div>'
                f'<div id="qz-run" class="qbox" hidden><div class="qhead"><span id="qz-pos"></span>'
                f'<span>{label("quiz_score")} <b id="qz-score">0</b></span></div>'
                f'<div class="qstem" id="qz-stem"></div><div class="qopts" id="qz-opts"></div>'
                f'<div class="verdict explanation-box" id="qz-verdict" hidden></div>'
                f'<div class="qactions"><button type="button" class="ui-btn" data-qz="quit">{label("quiz_quit")}</button>'
                f'<button type="button" class="ui-btn primary" id="qz-next" data-qz="next" hidden></button></div></div>'
                f'<div id="qz-done" class="qbox qresult" hidden><div>{label("quiz_score")}</div>'
                f'<div class="big" id="qz-final"></div><div class="qactions">'
                f'<button type="button" class="ui-btn" data-qz="retry">{label("quiz_retry")}</button>'
                f'<button type="button" class="ui-btn" id="qz-retry-wrong" data-qz="retry-wrong">{label("quiz_retry_wrong")}</button>'
                f'<button type="button" class="ui-btn primary" data-qz="setup">{label("quiz_start")}</button>'
                f'</div></div>')
    head = f"JLPT {esc(level)} " + label(spec["label"]) + (f' — {fu(part)}' if part else "")
    body = (lang_ui.header_html(head, label(spec["desc"]))
            + f'<main class="wrap"><nav class="tabs"><button type="button" class="tab-btn" data-tab="study" onclick="setTab(\'study\')">'
            f'{label("tab_study")}</button><button type="button" class="tab-btn" data-tab="quiz" '
            f'onclick="setTab(\'quiz\')">{label("tab_quiz")}</button></nav>'
            f'<section id="study">{study}</section><section id="quiz">{quiz}</section></main>')
    scripts = (f"const LEVEL = {js_data(level)}, CAT = {js_data(spec['stem'])}, PAGE = {PAGE_SIZE}, "
               f"RATE_SLOW = {RATE_SLOW};\n"
               f"const E = {js_data(E)};\nconst Q = {js_data(Q)};\nconst L = {js_data(L)};\n"
               f"const T = {js_data(token_table())}, TOK = /\\ue000(\\w+)\\ue001/g;\n{PAGE_JS}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(level, title, trail, body,
                        D.src_sha_comments(level, sources), scripts, pitch_footer()),
                   encoding="utf-8")
    return out


INDEX_JS = r"""
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-cat]').forEach(el => {
    const ids = IDS[el.dataset.cat] || [], got = window.JLPTKnowledgeStore.learned(LEVEL, el.dataset.cat);
    const n = ids.filter(id => got[id]).length;
    const x = el.querySelector('.js-learned'); if (x) x.textContent = n;
  });
});
"""


def build_index(level: str) -> Path:
    cards, ids, sources = [], {}, []
    for spec in D.categories(level):
        cat = D.locate(level, spec)
        sources += [p.shared for p in cat.parts]
        entries, _ = D.load_entries(cat)
        n = len(entries)
        ids[spec["stem"]] = [e.get("id") for e in entries if isinstance(e.get("id"), str)]
        inner = (f'<h2>{label(spec["label"])}</h2><p>{label(spec["desc"])}</p>'
                 + (f'<div class="n">{n} {label("entries")} · {label("learned")} '
                    f'<span class="js-learned">0</span> / {n}</div>' if n else
                    f'<div class="n">{label("coming")}</div>'))
        if n:
            cards.append(f'<a class="cat" href="{esc(D.page_path(level, spec["stem"]).name)}" '
                         f'data-cat="{esc(spec["stem"])}">{inner}</a>')
        else:
            cards.append(f'<div class="cat off" aria-disabled="true">{inner}</div>')
    title = UI[PRIMARY]["index_title"].format(level=level)
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + portal_label("mod_knowledge"), label("index_lead"))
            + f'<main class="wrap"><div class="cats">{"".join(cards)}</div></main>')
    scripts = f"const LEVEL = {js_data(level)};\nconst IDS = {js_data(ids)};\n{INDEX_JS}"
    out = D.level_dir(level) / D.INDEX_HTML
    out.parent.mkdir(parents=True, exist_ok=True)
    # Back to the portal's module chooser for this level, as an explicit file and
    # relative, so it works from `make serve`, a Pages repo subpath and file://.
    out.write_text(page(level, title, crumbs(level, 0, []), body,
                        D.src_sha_comments(level, sources), scripts), encoding="utf-8")
    return out


def build(level: str) -> list[Path]:
    if not D.categories(level):
        return []
    outs = [p for spec in D.categories(level) for p in build_category(level, spec)]
    outs.append(build_index(level))
    return outs


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--level", default="N2")
    args = ap.parse_args()
    outs = build(args.level)
    if not outs:
        print(f"{args.level}: no knowledge categories in {D.CATEGORIES_JSON.relative_to(ROOT)} — nothing to build")
        return 0
    for p in outs:
        print(f"  wrote {p.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
