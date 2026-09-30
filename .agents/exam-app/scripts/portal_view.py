"""The portal — level chooser and module chooser, ONE implementation for both
deployments.

Entering the site is three screens deep before a paper opens:

    /                       level chooser   N1–N5 cards: status (level.py), test
                                            count, whether a knowledge module exists
    /<LEVEL>/               module chooser  試験 (the exam list) / 知識 (knowledge)
                                            / ドリル (drill)
    /<LEVEL>/exam/          the exam list   index_view.py, filtered to that level

plus two modules built elsewhere and served as-is: 知識, built by jlpt-knowledge
into `knowledge/<LEVEL>/index.html`, and ドリル, built by jlpt-drill into
`drill/<LEVEL>/index.html` — each card stays disabled until its index exists. `serve_sheet.py` renders the first two on the fly from disk; `build_pages.py`
bakes them into `_site/index.html` and `_site/<LEVEL>/index.html`. Both call the
functions below with the SAME test objects (the list's own `{id, level, …}`
shape), so the two deployments cannot drift — the arrangement index_view.py
already has for the list, which renders its page through `page()` here too.

**Every link is relative** (`N2/index.html`, `../knowledge/N2/index.html`,
`../../tests/<id>/解答.html`): Pages serves the site from `/<repo>/`, where an
absolute `/` leaves the site. Links name `index.html` explicitly so the tree
also works opened from disk.

The chrome is bilingual through the language registry (`langs.py`, namespace
`portal`): every label ships one `.lang-pane` per active language and
`body[data-lang]` shows one. The top of every screen is lang_ui's ONE slim
sticky bar (breadcrumb + language dropdown, `lang_ui.topbar_html`), whose
switcher remembers the choice under `lang_ui.LANG_STORE_KEY` — one preference
across portal, knowledge, drill, exam, practice and model answer. The title and
subtitle below it are ordinary page content.

A level with nothing behind it is shown DISABLED (「準備中」), never hidden: the
portal covers N1–N5, and a greyed N1 says "coming" where a missing one would say
"not supported".

Dependency-free (json + pathlib + sibling modules), like index_view.py:
`make serve` must start without the authoring dependencies installed.
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
ROOT = _HERE.parents[2]
KNOWLEDGE = ROOT / "knowledge"   # the 知識 module (jlpt-knowledge; tracked)
DRILL = ROOT / "drill"           # the ドリル module (make drill)

sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(ROOT / ".agents" / "jlpt-exam-structure" / "scripts"))
sys.path.insert(0, str(ROOT / ".agents" / "exam-model-answer" / "scripts"))
import app_style                  # noqa: E402
import level as LEVEL             # noqa: E402
import langs                      # noqa: E402
import build_model_answer as ma   # noqa: E402  (EXPLANATION_CSS: .lang-pane + pane hiding)
import lang_ui                    # noqa: E402  (the one sticky bar + language dropdown)
sys.path.insert(0, str(ROOT / ".agents" / "jlpt-knowledge" / "scripts"))
import knowledge_data             # noqa: E402  (summary(level): entry counts, both layouts)

NS = "portal"
LEVELS = LEVEL.LEVEL_NAMES
EXAM_DIR = "exam"          # /<LEVEL>/exam/ — the exam module's folder name
KNOWLEDGE_DIR = KNOWLEDGE.name   # /knowledge/<LEVEL>/ — the 知識 module
DRILL_DIR = DRILL.name           # /drill/<LEVEL>/ — the ドリル module
INDEX = "index.html"

FONT_TAGS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900'
    '&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">'
)

# The page header and card chrome every portal screen shares — the exam list
# included (index_view adds only its own list CSS on top). The sticky part is
# lang_ui's topbar; the header below it scrolls away with the page.
PORTAL_CSS = """
*{box-sizing:border-box}
body{margin:0;background:#f8fafc;color:var(--ink);font-family:var(--ui);--primary:#1e3a8a}
header.app-header{
  background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color:#fff;padding:1rem 1.4rem 1.15rem;
}
.header-inner{max-width:82em;margin:0 auto;display:flex;flex-wrap:wrap;align-items:baseline;
  gap:.2rem 1rem}
.header-badge{display:inline-block;background:rgba(255,255,255,0.12);color:#93c5fd;
  font-size:0.72rem;font-weight:700;padding:0.15rem 0.6rem;border-radius:9999px;
  letter-spacing:0.04em;flex-basis:100%;max-width:max-content;margin-bottom:.35rem}
h1.title{font-size:1.4rem;font-weight:900;margin:0;color:#ffffff}
.subtitle{color:#94a3b8;font-size:0.88rem}
main{max-width:82em;margin:0 auto;padding:1.8em 1.5em 5em}
.lede{margin:0 0 1.6em;font-size:10.5pt;color:var(--muted);line-height:1.6}
h2.section{font-size:13pt;font-weight:800;color:#0f172a;margin:0 0 .4em}
.pt-grid{display:grid;gap:1em;grid-template-columns:repeat(auto-fill,minmax(14em,1fr))}
.pt-grid.mods{grid-template-columns:repeat(auto-fill,minmax(20em,1fr))}
.pt-card{display:flex;flex-direction:column;gap:.55em;background:#fff;
  border:1px solid #e2e8f0;border-radius:12px;padding:1.1em 1.2em 1.2em;
  color:inherit;text-decoration:none;box-shadow:0 1px 3px rgba(0,0,0,0.03);
  transition:all .18s ease;min-height:9.5em}
a.pt-card:hover{border-color:var(--accent);box-shadow:0 6px 18px rgba(37,99,235,0.12);
  transform:translateY(-1px)}
.pt-card.off{opacity:.55;background:#f1f5f9;cursor:default}
.pt-card .pt-name{font-size:1.9rem;font-weight:900;color:#0f172a;line-height:1.1}
.pt-card .pt-mod{font-size:1.25rem;font-weight:900;color:#0f172a}
.pt-card .pt-desc{font-size:10pt;color:#475569;line-height:1.65}
.pt-card .pt-meta{display:flex;flex-wrap:wrap;gap:.4em;font-size:9.5pt;color:#475569}
.pt-card .pt-meta span{background:#f1f5f9;border:1px solid #e2e8f0;border-radius:9999px;
  padding:.1em .65em;font-variant-numeric:tabular-nums}
.pt-card .pt-go{margin-top:auto;font-size:10pt;font-weight:700;color:var(--accent)}
.pt-card.off .pt-go{color:#64748b}
.badge.st-calibrated{background:#ecfdf5;border-color:#a7f3d0;color:#065f46}
.badge.st-structured{background:#e0f2fe;border-color:#bae6fd;color:#0369a1}
.badge.st-scaffold,.badge.st-none{background:#f8fafc;border-color:var(--line);color:#64748b}
.pt-cats{display:flex;flex-wrap:wrap;gap:.35em}
.pt-cats span{font-size:9pt;background:#eef2ff;border:1px solid #c7d2fe;color:#3730a3;
  border-radius:6px;padding:.05em .5em}
@media screen and (max-width: 54em){
  header.app-header{padding:.75rem 1rem .85rem}
  h1.title{font-size:1.15rem}
  .subtitle{font-size:.8rem}
  main{padding:1.2em 1em 4em}
  .pt-grid,.pt-grid.mods{grid-template-columns:1fr}
  .pt-card{min-height:0}
}
"""


# ------------------------------------------------------------------- strings
def _fill(s: str, kw: dict) -> str:
    for k, v in kw.items():
        s = s.replace("{" + k + "}", str(v))
    return s


def tr(code: str, key: str, **kw) -> str:
    """One language's string; the primary language's when that one lacks it
    (the gate FAILs a missing key, so this is only a render-time safety net)."""
    s = langs.ui(code, NS).get(key)
    if s is None:
        s = langs.ui(langs.primary(), NS).get(key, key)
    return _fill(s, kw)


def pane(key: str, **kw) -> str:
    """A label in every active language, one `.lang-pane` each. The strings are
    repo-authored and may carry inline markup (<b>, <br>); values are not."""
    kw = {k: html.escape(str(v)) for k, v in kw.items()}
    codes = langs.order()
    if len(codes) == 1:
        return tr(codes[0], key, **kw)
    return "".join(f'<span class="lang-pane" data-lang="{c}">{tr(c, key, **kw)}</span>'
                   for c in codes)


def i18n_attrs(attr: str, key: str, **kw) -> str:
    """An attribute (placeholder, aria-label, title) cannot hold a pane: it is
    written in the primary language and swapped on a language change from the
    per-language copies carried as `data-i18n-<attr>-<code>`."""
    p = html.escape(tr(langs.primary(), key, **kw), quote=True)
    extra = "".join(f' data-i18n-{attr}-{c}="{html.escape(tr(c, key, **kw), quote=True)}"'
                    for c in langs.order())
    return f'{attr}="{p}"{extra} data-i18n'


def js_strings(prefix: str = "") -> str:
    """{code: {key: string}} for the keys starting with `prefix`, as JSON — what
    index_view's JS builds its card labels from."""
    return json.dumps({c: {k: v for k, v in langs.ui(c, NS).items() if k.startswith(prefix)}
                       for c in langs.order()}, ensure_ascii=False)


# ------------------------------------------------------------------- the data
def level_status(lv: str) -> str:
    """calibrated / structured / scaffold from level.py; `none` for a level with
    no structure table on disk yet."""
    try:
        return LEVEL.status(lv)
    except LEVEL.LevelError:
        return "none"


def knowledge_info(lv: str, root: Path = KNOWLEDGE) -> dict:
    """What the 知識 module holds for a level. Entry counts come from
    `knowledge_data.summary()` — the module's own reader, which knows both data
    layouts (single file and split parts) — and a category counts as available
    only with at least one entry: the builder writes a page for every category,
    empty ones included. The module is available when its `index.html` exists."""
    try:
        counts = knowledge_data.summary(lv)
    except (OSError, ValueError, KeyError):
        counts = {}
    cats = [{"stem": s, "entries": n} for s, n in counts.items() if n > 0]
    return {"available": (root / lv / INDEX).is_file(), "categories": cats}


def drill_info(lv: str, root: Path = DRILL) -> dict:
    """The ドリル module: available when `drill/<LEVEL>/index.html` exists. The
    card reads 「準備中」 for a level `make drill` has not built."""
    return {"available": (root / lv / INDEX).is_file()}


def level_summaries(tests: list[dict], knowledge_root: Path = KNOWLEDGE,
                    drill_root: Path = DRILL) -> list[dict]:
    """One row per JLPT level, N1..N5, from the list's own test objects."""
    out = []
    for lv in LEVELS:
        mine = [t for t in tests if (t.get("level") or LEVEL.DEFAULT_LEVEL) == lv]
        know = knowledge_info(lv, knowledge_root)
        drill = drill_info(lv, drill_root)
        out.append({"level": lv, "status": level_status(lv), "tests": len(mine),
                    "knowledge": know, "drill": drill,
                    "enabled": bool(mine) or know["available"] or drill["available"]})
    return out


# ------------------------------------------------------------------ the shell
# Attributes cannot hold a .lang-pane, so they are swapped here on lang_ui's
# `langchange`; everything else is CSS. `onPortalLang` lets a page (the exam
# list) re-read its own.
ATTR_JS = """
var TITLES = %(titles)s;
function paintAttrs(lang){
  document.title = TITLES[lang] || document.title;
  // data-i18n-<attr>-<lang>: an element may carry several (aria-label AND
  // placeholder), so every attribute is read rather than one named by a marker.
  var tail = '-' + lang;
  document.querySelectorAll('[data-i18n]').forEach(function(el){
    Array.prototype.slice.call(el.attributes).forEach(function(at){
      var n = at.name;
      if (n.indexOf('data-i18n-') === 0 && n.slice(-tail.length) === tail)
        el.setAttribute(n.slice(10, -tail.length), at.value);
    });
  });
  if (typeof window.onPortalLang === 'function') window.onPortalLang(lang);
}
document.addEventListener('langchange', function(e){ paintAttrs(e.detail.lang); });
"""


def page(*, title_key: str, title_kw: dict, h1: str, subtitle: str, crumbs: list,
         body: str, extra_css: str = "", head_js: str = "", tail_js: str = "",
         right: str = "") -> str:
    """One portal screen. `h1`/`subtitle`/`body` are already-rendered panes;
    `crumbs` = [(label html, href or None)] for the sticky bar, `right` = the
    page's own compact read-out beside the language dropdown."""
    p = langs.primary()
    titles = {c: tr(c, title_key, **title_kw) for c in langs.order()}
    js = ATTR_JS % {"titles": json.dumps(titles, ensure_ascii=False)}
    # The root screen's bar names the site; deeper screens carry the trail
    # there and keep the site badge in the (scrolling) header instead.
    trail = crumbs or [(pane("site_badge"), None)]
    badge = f'<span class="header-badge">{pane("site_badge")}</span>' if crumbs else ""
    return (
        f'<!DOCTYPE html><html lang="{langs.html_lang(p)}"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'{FONT_TAGS}<title>{html.escape(titles[p])}</title>'
        f'<style>{app_style.APP_CSS}{ma.EXPLANATION_CSS}{lang_ui.head_css()}{PORTAL_CSS}{extra_css}</style>'
        f'</head><body data-lang="{p}">'
        f'<script>{js}</script>{head_js}'
        f'{lang_ui.topbar_html(trail, right)}'
        '<header class="app-header"><div class="header-inner">'
        f'{badge}'
        f'<h1 class="title">{h1}</h1><div class="subtitle">{subtitle}</div>'
        '</div></header>'
        f'<main>{body}</main>'
        f'<script>{tail_js}\npaintAttrs(currentLang());</script>'
        '</body></html>')


# -------------------------------------------------------------- the two screens
def _status_badge(status: str) -> str:
    return f'<span class="badge st-{status}">{pane("status_" + status)}</span>'


def portal_html(levels: list[dict]) -> str:
    """Screen 0 — `/` (`index.html`): the level chooser."""
    cards = []
    for s in levels:
        lv = s["level"]
        meta = [pane("n_tests", n=s["tests"])]
        cats = s["knowledge"]["categories"]
        meta.append(pane("n_knowledge_cats", n=len(cats)) if s["knowledge"]["available"]
                    else pane("no_knowledge"))
        inner = (f'<div class="pt-name">{lv}</div>'
                 f'<div>{_status_badge(s["status"])}</div>'
                 '<div class="pt-meta">' + "".join(f"<span>{m}</span>" for m in meta) + '</div>')
        if s["enabled"]:
            cards.append(f'<a class="pt-card" data-level="{lv}" href="{lv}/{INDEX}">{inner}'
                         f'<span class="pt-go">{pane("open")} →</span></a>')
        else:
            cards.append(f'<div class="pt-card off" data-level="{lv}" aria-disabled="true">'
                         f'{inner}<span class="pt-go">{pane("coming")}</span></div>')
    body = (f'<h2 class="section">{pane("choose_level")}</h2>'
            f'<p class="lede">{pane("choose_level_lede")}</p>'
            f'<div class="pt-grid">{"".join(cards)}</div>')
    return page(title_key="doc_title_root", title_kw={}, h1=pane("site_title"),
                subtitle=pane("site_subtitle"), crumbs=[], body=body)


def _module_card(mod: str, href: str, inner: str, on: bool) -> str:
    """A module card: a link when the module has content, else disabled 「準備中」."""
    if on:
        return (f'<a class="pt-card" data-module="{mod}" href="{href}">{inner}'
                f'<span class="pt-go">{pane("open")} →</span></a>')
    return (f'<div class="pt-card off" data-module="{mod}" aria-disabled="true">{inner}'
            f'<span class="pt-go">{pane("coming")}</span></div>')


def module_html(s: dict) -> str:
    """Screen 1 — `/<LEVEL>/` (`<LEVEL>/index.html`): 試験, 知識 or ドリル."""
    lv = s["level"]
    exam_inner = (f'<div class="pt-mod">{pane("mod_exam")}</div>'
                  f'<div class="pt-desc">{pane("mod_exam_desc")}</div>'
                  f'<div class="pt-meta"><span>{pane("n_tests", n=s["tests"])}</span></div>')
    exam = _module_card("exam", f"{EXAM_DIR}/{INDEX}", exam_inner, bool(s["tests"]))
    k = s["knowledge"]
    cats = "".join(f'<span>{html.escape(c["stem"])} · {pane("n_entries", n=c["entries"])}</span>'
                   for c in k["categories"])
    know_inner = (f'<div class="pt-mod">{pane("mod_knowledge")}</div>'
                  f'<div class="pt-desc">{pane("mod_knowledge_desc")}</div>'
                  f'<div class="pt-meta"><span>'
                  f'{pane("n_knowledge_cats", n=len(k["categories"])) if k["available"] else pane("no_knowledge")}'
                  f'</span></div>'
                  + (f'<div class="pt-cats">{cats}</div>' if cats else ""))
    know = _module_card("knowledge", f"../{KNOWLEDGE_DIR}/{lv}/{INDEX}", know_inner,
                        k["available"])
    drill_inner = (f'<div class="pt-mod">{pane("mod_drill")}</div>'
                   f'<div class="pt-desc">{pane("mod_drill_desc")}</div>')
    drill = _module_card("drill", f"../{DRILL_DIR}/{lv}/{INDEX}", drill_inner,
                         s["drill"]["available"])
    body = (f'<p class="lede">{pane("level_lede")}</p>'
            f'<div class="pt-grid mods">{exam}{know}{drill}</div>')
    return page(title_key="doc_title_level", title_kw={"level": lv},
                h1=pane("level_title", level=lv),
                subtitle=_status_badge(s["status"]),
                crumbs=[(pane("crumb_home"), f"../{INDEX}"), (lv, None)], body=body)


def exam_href(level: str, depth: int = 2) -> str:
    """Relative link to a level's exam list from `depth` folders below the site
    root — a sheet at `tests/<id>/` is depth 2: `../../N2/exam/index.html`."""
    return "../" * depth + f"{level}/{EXAM_DIR}/{INDEX}"
