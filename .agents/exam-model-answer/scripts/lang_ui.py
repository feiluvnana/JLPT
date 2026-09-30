"""The site chrome every page shares: ONE sticky top bar, ONE language dropdown.

Every page that shows interface text (portal, exam list, 解答.html, 練習.html,
模範解答.html, the 知識 and ドリル pages) renders its top of screen through
`topbar_html()` and switches language through the dropdown it contains — no page
writes its own switch. The two printed booklets are the exception: they are
official-paper replicas, and the exam's wording is Japanese on every page.

Mechanism (unchanged from the segmented control it replaces): every translatable
label is printed once per language as `<span class="lang-pane" data-lang=…>`,
`langs.pane_css()` hides the panes that are not `body[data-lang]`, and the
dropdown only flips that attribute. Text a page builds in JS listens for the
`langchange` event on `document`.

The chosen language is remembered under LANG_STORE_KEY — one preference for the
whole site.

Dependency-free (langs.py + stdlib): `make serve` imports it.
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import langs  # noqa: E402

# The one localStorage key for the reader's language (was
# build_model_answer.LANG_STORE_KEY, which now re-exports this).
LANG_STORE_KEY = "kaisetsuLang"


def default_label() -> str:
    """The dropdown's aria-label: every active language's own word for
    "language" (portal namespace `lang_label`), so a screen reader announces it
    in whichever language the reader understands. An attribute cannot hold a
    `.lang-pane`, hence the joined form."""
    words = [langs.ui(c, "portal").get("lang_label") for c in langs.order()]
    return " / ".join(dict.fromkeys(w for w in words if w)) or "Language"


def switcher_html(codes: list[str] | None = None, label: str | None = None) -> str:
    """The dropdown. `codes` narrows it to the languages this page has content
    for (default: every active language). A single option renders disabled —
    the control is always present, so it never moves between pages."""
    codes = codes or langs.order()
    label = label or default_label()
    opts = "".join(f'<option value="{c}" lang="{langs.html_lang(c)}">'
                   f'{html.escape(langs.name(c))}</option>' for c in codes)
    dis = " disabled" if len(codes) < 2 else ""
    return (f'<select class="lang-select" aria-label="{html.escape(label)}"'
            f' data-langs="{html.escape(json.dumps(codes))}"{dis}>{opts}</select>')


def topbar_html(crumbs: list[tuple[str, str | None]], right_html: str = "",
                codes: list[str] | None = None, label: str | None = None) -> str:
    """The sticky bar, followed by the switcher's script (it must run right
    after the dropdown exists, so the page's first paint is already in the
    reader's language). `crumbs` = [(label_html, href_or_None), …], left to
    right; labels may already be `.lang-pane` markup, and the last one is where
    you are. `right_html` sits before the dropdown — a page's own compact
    controls (timer, counters, actions); give an element `tb-wide` to drop it
    on a phone, `tb-shrink` to let it ellipsize."""
    parts = []
    for i, (text, href) in enumerate(crumbs):
        if i:
            parts.append('<span class="tb-sep" aria-hidden="true">›</span>')
        last = " tb-last" if i == len(crumbs) - 1 else ""
        parts.append(f'<a class="tb-crumb{last}" href="{href}">{text}</a>' if href
                     else f'<span class="tb-crumb tb-here{last}">{text}</span>')
    return ('<nav class="topbar" id="topbar" aria-label="breadcrumb">'
            f'<div class="tb-crumbs">{"".join(parts)}</div>'
            f'<div class="tb-right">{right_html}{switcher_html(codes, label)}</div>'
            f'</nav><script>{SWITCHER_JS}</script>')


TOPBAR_CSS = """
/* lang_ui: the one sticky bar. Sized like the exam sheet's original #bar
   (min-height 3.4em at 11pt ≈ 50px, 1.8em side padding, gradient + shadow) —
   the owner's call on 2026-09-30, after a 40px slim bar read as too small.
   --tb-h is its height, for anything that sticks under it (players). */
:root{--tb-h:50px}
.topbar{position:sticky;top:0;z-index:1000;display:flex;align-items:center;
  height:var(--tb-h);padding:0 max(1.8em,env(safe-area-inset-right)) 0 max(1.8em,env(safe-area-inset-left));gap:.6em 1.2em;
  box-sizing:border-box;width:100%;max-width:100%;overflow:hidden;margin:0;
  background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%);color:#e2e8f0;
  font:500 11pt/1 var(--ui,system-ui,sans-serif);
  box-shadow:0 4px 14px rgba(0,0,0,.08);border-bottom:1px solid rgba(255,255,255,.08)}
.topbar .tb-crumbs{flex:1 1 0;min-width:2.5em;display:flex;align-items:center;gap:.45em;
  white-space:nowrap;overflow:hidden}
.topbar .tb-crumb{color:#cbd5e1;text-decoration:none;overflow:hidden;text-overflow:ellipsis;
  min-width:0;flex:0 1 auto;line-height:1.5}
.topbar a.tb-crumb:hover{color:#fff;text-decoration:underline}
.topbar .tb-here{color:#fff;font-weight:800;font-size:12.5pt;flex:0 1 auto}
.topbar .tb-sep{color:#64748b;flex:0 0 auto}
.topbar .tb-right{flex:0 0 auto;max-width:calc(100% - 2.5em);min-width:0;justify-content:flex-end;display:flex;align-items:center;gap:.5em}
.topbar .tb-right>*{flex:0 0 auto}
.topbar .tb-right>.tb-shrink{flex:0 1 auto;min-width:0;overflow:hidden;text-overflow:ellipsis;
  white-space:nowrap}
.topbar .tb-last{flex:0 1 auto}
/* A page's own compact controls in the bar (right_html): links, buttons, read-outs. */
.topbar .tb-link,.topbar .tb-btn{display:inline-flex;align-items:center;justify-content:center;
  box-sizing:border-box;height:32px;min-height:0;padding:0 .85em;margin:0;border-radius:6px;
  border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.08);color:#e2e8f0;
  font:700 10pt/1 var(--ui,system-ui,sans-serif);text-decoration:none;white-space:nowrap;
  cursor:pointer;box-shadow:none}
.topbar .tb-link:hover,.topbar .tb-btn:hover{background:rgba(255,255,255,.18);color:#fff}
.topbar .tb-btn.primary{background:#2563eb;border-color:#2563eb;color:#fff}
.topbar .tb-btn.primary:hover{background:#1d4ed8;border-color:#1d4ed8}
.topbar .tb-btn:disabled,.topbar .tb-btn:disabled:hover{opacity:.45;cursor:not-allowed}
.topbar .tb-btn.primary:disabled:hover{background:#2563eb}
.topbar .tb-sub{color:#94a3b8;font-variant-numeric:tabular-nums;white-space:nowrap}
.topbar .tb-short{display:none}
.lang-select{font:600 10pt/1 var(--ui,system-ui,sans-serif);color:#0f172a;background:#f8fafc;
  border:1px solid #cbd5e1;border-radius:6px;height:32px;padding:0 1.6em 0 .6em;cursor:pointer;
  max-width:9.5em}
.lang-select:focus-visible{outline:2px solid #60a5fa;outline-offset:1px}
.lang-select[disabled]{opacity:.6;cursor:default}
@media (max-width:600px){
  :root{--tb-h:44px}
  .topbar{gap:.4em .8em;font-size:10pt;padding:0 .9em}
  .topbar .tb-here{font-size:11.5pt}
  .topbar .tb-wide{display:none!important}
  /* On a phone only the page you are on is spelled out; the crumbs before it
     stay reachable as a short trail that gives way first. */
  /* On a phone the trail collapses to one 「‹」 back link to the parent page
     plus the page you are on — squeezed crumbs read as bare 「› ›」. */
  .topbar .tb-crumbs>.tb-crumb:not(.tb-last),.topbar .tb-crumbs>.tb-sep{display:none}
  .topbar .tb-crumbs>a.tb-crumb:nth-last-child(3){display:inline-flex;flex:0 0 auto;
    font-size:0;width:22px;justify-content:center;text-decoration:none}
  .topbar .tb-crumbs>a.tb-crumb:nth-last-child(3)::before{content:"‹";font-size:20px;
    line-height:1;color:#e2e8f0}
  .topbar .tb-right{gap:.35em}
  .lang-select{height:30px;font-size:10pt;max-width:6.5em;padding:0 1.1em 0 .4em}
  .topbar .tb-link,.topbar .tb-btn{height:30px;padding:0 .6em;font-size:10pt}
  .topbar .tb-long{display:none}
  .topbar .tb-short{display:inline}
}
@media print{.topbar{display:none!important}}
"""

SWITCHER_JS = """
/* lang_ui: apply / remember / restore the reader's language. */
(function(){
  var KEY = %(key)s;
  function offered(sel){
    try { return JSON.parse(sel.getAttribute('data-langs')) || []; } catch (e) { return []; }
  }
  function applyLang(lang, persist){
    var sel = document.querySelector('.lang-select');
    var list = sel ? offered(sel) : %(order)s;
    if (list.indexOf(lang) < 0) lang = list[0];
    document.body.dataset.lang = lang;
    document.documentElement.lang = %(html_langs)s[lang] || lang;
    document.querySelectorAll('.lang-select').forEach(function(s){ s.value = lang; });
    if (persist){ try { localStorage.setItem(KEY, lang); } catch (e) {} }
    try { document.dispatchEvent(new CustomEvent('langchange', {detail: {lang: lang}})); } catch (e) {}
    return lang;
  }
  function savedLang(){
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  if (window.applyLang) return;          /* one switcher per page */
  window.applyLang = applyLang;
  window.currentLang = function(){ return document.body.dataset.lang || %(primary)s; };
  document.addEventListener('change', function(ev){
    if (ev.target && ev.target.classList && ev.target.classList.contains('lang-select'))
      applyLang(ev.target.value, true);
  });
  function boot(){ return applyLang(savedLang() || document.body.dataset.lang || %(primary)s, false); }
  /* This script sits right after the dropdown (topbar_html), so the language is
     applied before the rest of the page paints; DOMContentLoaded fires the
     event once more for listeners registered further down the page. */
  if (document.querySelector('.lang-select')) boot();
  document.addEventListener('DOMContentLoaded', boot);
  /* Coming back through the history cache must show the language chosen since. */
  window.addEventListener('pageshow', function(e){ if (e.persisted) boot(); });
})();
""" % {"key": json.dumps(LANG_STORE_KEY), "order": json.dumps(langs.order()),
       "html_langs": json.dumps({c: langs.html_lang(c) for c in langs.order()}),
       "primary": json.dumps(langs.primary())}


def pane(ns: str, key: str, **kw) -> str:
    """One label from namespace `ns`, in every active language, as `.lang-pane`
    spans (`kw` fills its {placeholders})."""
    return "".join(f'<span class="lang-pane" data-lang="{c}">'
                   f'{langs.ui(c, ns).get(key, "").format(**kw)}</span>' for c in langs.order())


_pane = pane


def header_html(title: str, subtitle: str = "", badge: bool = True,
                width: str | None = None) -> str:
    """The module header under the bar — the exam list's gradient block (site
    badge, title, subtitle), shared so 試験, 知識 and ドリル open the same way.
    `title`/`subtitle` are already-rendered (pane) markup. `width` aligns the
    header's content with the page column below it (e.g. "60rem"); it scrolls
    away with the page, only the bar sticks."""
    style = f' style="max-width:{html.escape(width)}"' if width else ""
    b = f'<span class="header-badge">{_pane("portal", "site_badge")}</span>' if badge else ""
    sub = f'<div class="subtitle">{subtitle}</div>' if subtitle else ""
    return (f'<header class="app-header"><div class="header-inner"{style}>{b}'
            f'<h1 class="title">{title}</h1>{sub}</div></header>')


HEADER_CSS = """
/* lang_ui: the module header (scrolls away; only the bar sticks). */
header.app-header{background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%);
  color:#fff;padding:1rem 1.4rem 1.15rem}
header.app-header .header-inner{max-width:82em;margin:0 auto;display:flex;flex-wrap:wrap;
  align-items:baseline;gap:.2rem 1rem}
header.app-header .header-badge{display:inline-block;background:rgba(255,255,255,0.12);
  color:#93c5fd;font-size:0.72rem;font-weight:700;padding:0.15rem 0.6rem;border-radius:9999px;
  letter-spacing:0.04em;flex-basis:100%;max-width:max-content;margin-bottom:.35rem}
header.app-header h1.title{font-size:1.4rem;font-weight:900;margin:0;color:#ffffff;
  font-family:var(--ui,system-ui,sans-serif)}
header.app-header .subtitle{color:#94a3b8;font-size:0.88rem;line-height:1.6}
@media screen and (max-width: 54em){
  header.app-header{padding:.75rem 1rem .85rem}
  header.app-header h1.title{font-size:1.15rem}
  header.app-header .subtitle{font-size:.8rem}
}
@media print{header.app-header{background:none;color:#000}
  header.app-header h1.title{color:#000}}
"""


def head_css() -> str:
    """Everything a page's <style> needs for the chrome: the bar + pane hiding."""
    return TOPBAR_CSS + HEADER_CSS + "\n.lang-pane{display:contents}\n" + langs.pane_css()
