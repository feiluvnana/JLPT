"""The site chrome every page shares: ONE sticky top bar, ONE language dropdown,
ONE page header, ONE font link.

Every page that shows interface text (portal, exam list, 解答.html, 練習.html,
模範解答.html, the 知識 and ドリル pages) is built as `head_html()` in <head>,
`head_css()` in its <style>, then `body_open()` → `topbar_html()` →
`header_html()` → content, and switches language through the bar's dropdown —
no page writes its own switch, header or font link. The two printed booklets are the exception: they are
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


# The ONE web-font request every page makes (the booklets included), so the
# browser's cache holds exactly one stylesheet and one set of font files across
# the site. `display=optional`, not `swap`: a face that is not ready within the
# first ~100 ms is skipped for that page view instead of swapping in late, so a
# navigation never re-lays the bar and header out mid-view (the "flash" the owner
# saw between screens, 2026-09-30); once cached it is used from the first paint.
FONT_TAGS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900'
    '&family=Noto+Serif+JP:wght@400;600;700&display=optional" rel="stylesheet">'
)

EARLY_MARK = "/* lang_ui: early language */"


def head_html() -> str:
    """What every page's <head> carries for the chrome: the one font link. Put
    it before the page's own <style>."""
    return FONT_TAGS


def body_open(attrs: str = "", codes: list[str] | None = None) -> str:
    """`<body data-lang=…>` plus the script that applies the SAVED language
    before anything under it is parsed. Without it the page paints in the
    primary language and switches when the bar's script runs — on a large page
    (解答.html, 模範解答.html) the parser yields in between and the reader sees
    the Japanese chrome flash first. `codes` = the languages this page offers
    (default: every active one); `attrs` = the page's other body attributes."""
    codes = codes or langs.order()
    hl = {c: langs.html_lang(c) for c in codes}
    js = (f"{EARLY_MARK}(function(){{var L={json.dumps(codes)},H={json.dumps(hl)},v=null;"
          f"try{{v=localStorage.getItem({json.dumps(LANG_STORE_KEY)})}}catch(e){{}}"
          "if(v&&L.indexOf(v)>=0){document.body.dataset.lang=v;"
          "document.documentElement.lang=H[v]||v;}})();")
    extra = f" {attrs.strip()}" if attrs.strip() else ""
    return f'<body data-lang="{codes[0]}"{extra}><script>{js}</script>'


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
            f'</nav><script>{SWITCHER_JS}{OVERLAY_SCROLL_JS}</script>')


TOPBAR_CSS = """
/* lang_ui: the one sticky bar. Sized like the exam sheet's original #bar
   (min-height 3.4em at 11pt ≈ 50px, 1.8em side padding, gradient + shadow) —
   the owner's call on 2026-09-30, after a 40px slim bar read as too small.
   --tb-h is its height, for anything that sticks under it (players). */
/* Site base, identical on every page so moving between them cannot shift or
   repaint: the page scrollbar never takes layout width — the native one is
   hidden and OVERLAY_SCROLL_JS draws a thin thumb OVER the content (the owner's
   call, 2026-09-30: a reserved gutter still read as a jitter between pages with
   and without a scrollbar), the canvas is the pages' own background (no
   white frame before the body paints), and the chrome uses ONE font stack of
   its own, whatever --ui a page defines. */
:root{--tb-h:50px;--tb-font:"Noto Sans JP",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Hiragino Sans","Yu Gothic",sans-serif}
@media screen{html{scrollbar-width:none;background:#f8fafc}
  html::-webkit-scrollbar{width:0;height:0;display:none}}
/* The overlay page scrollbar (OVERLAY_SCROLL_JS): fixed over the right edge,
   visible while scrolling or when the pointer nears the edge, never in layout. */
.ov-sb{position:fixed;top:0;right:0;bottom:0;width:14px;z-index:2000;pointer-events:none}
.ov-sb .ov-th{position:absolute;top:0;right:3px;width:6px;border-radius:4px;
  background:rgba(15,23,42,.38);opacity:0;transition:opacity .35s,width .12s,right .12s;
  pointer-events:auto;cursor:default;touch-action:none}
.ov-sb.on .ov-th{opacity:1}
.ov-sb .ov-th:hover,.ov-sb.drag .ov-th{width:9px;right:2px;background:rgba(15,23,42,.55)}
@media print{.ov-sb{display:none}}
.topbar{position:sticky;top:0;z-index:1000;display:flex;align-items:center;
  height:var(--tb-h);padding:0 max(1.8em,env(safe-area-inset-right)) 0 max(1.8em,env(safe-area-inset-left));gap:.6em 1.2em;
  box-sizing:border-box;width:100%;max-width:100%;overflow:hidden;margin:0;
  background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%);color:#e2e8f0;
  font:500 11pt/1 var(--tb-font);
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
  font:700 10pt/1 var(--tb-font);text-decoration:none;white-space:nowrap;
  cursor:pointer;box-shadow:none}
.topbar .tb-link:hover,.topbar .tb-btn:hover{background:rgba(255,255,255,.18);color:#fff}
.topbar .tb-btn.primary{background:#2563eb;border-color:#2563eb;color:#fff}
.topbar .tb-btn.primary:hover{background:#1d4ed8;border-color:#1d4ed8}
.topbar .tb-btn:disabled,.topbar .tb-btn:disabled:hover{opacity:.45;cursor:not-allowed}
.topbar .tb-btn.primary:disabled:hover{background:#2563eb}
.topbar .tb-sub{color:#94a3b8;font-variant-numeric:tabular-nums;white-space:nowrap}
.topbar .tb-short{display:none}
.lang-select{font:600 10pt/1 var(--tb-font);color:#0f172a;background:#f8fafc;
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


def header_html(title: str, subtitle: str = "") -> str:
    """The page header under the bar — the same block on EVERY page but the
    booklets (portal, exam list, 解答.html, 練習.html, 模範解答.html, 知識,
    ドリル): the site badge, the title (「JLPT N2 …」; the portal root's is the
    site name), the subtitle, on one 82em column. `title`/`subtitle` are
    already-rendered (pane) markup. It scrolls away; only the bar sticks. No
    options on purpose: a per-page width or a missing badge is exactly the
    difference the owner saw between screens (2026-09-30)."""
    b = f'<span class="header-badge">{_pane("portal", "site_badge")}</span>'
    sub = f'<div class="subtitle">{subtitle}</div>' if subtitle else ""
    return (f'<header class="app-header"><div class="header-inner">{b}'
            f'<h1 class="title">{title}</h1>{sub}</div></header>')


HEADER_CSS = """
/* lang_ui: the page header (scrolls away; only the bar sticks). Every property
   the host page could otherwise leak in (the booklet's bare h1 rule, a body
   line-height, a global reset) is set here, so it measures the same everywhere. */
header.app-header{display:block;box-sizing:border-box;margin:0;border:0;
  background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%);color:#fff;
  padding:1rem 1.4rem 1.15rem;font:400 16px/1.5 var(--tb-font);text-align:left}
header.app-header .header-inner{box-sizing:border-box;max-width:82em;margin:0 auto;
  display:flex;flex-wrap:wrap;align-items:baseline;gap:.2rem 1rem}
header.app-header .header-badge{display:inline-block;background:rgba(255,255,255,0.12);
  color:#93c5fd;font:700 0.72rem/1.4 var(--tb-font);padding:0.15rem 0.6rem;border-radius:9999px;
  letter-spacing:0.04em;margin:0}
header.app-header h1.title{font:900 1.4rem/1.35 var(--tb-font);margin:0;padding:0;border:0;
  background:none;color:#ffffff;letter-spacing:normal;text-align:left}
/* Badge + title on the first row, the subtitle always on its own row: a long
   subtitle then wraps within its row instead of changing the layout. */
header.app-header .subtitle{color:#94a3b8;font:400 0.88rem/1.6 var(--tb-font);margin:0;
  flex:1 1 100%;min-width:0}
@media screen and (max-width: 54em){
  header.app-header{padding:.75rem 1rem .85rem}
  /* A phone stacks badge / title / subtitle on every page, never "title
     beside the badge when it happens to fit". */
  header.app-header .header-inner{display:block}
  header.app-header h1.title{font-size:1.15rem;margin-top:.3rem}
  header.app-header .subtitle{font-size:.8rem}
}
@media print{header.app-header{background:none;color:#000}
  header.app-header h1.title{color:#000}}
"""


OVERLAY_SCROLL_JS = """
/* lang_ui: a page scrollbar that floats over the content instead of taking a
   gutter. Scrolling stays native (wheel, trackpad, keys, touch); this only
   draws and drags the thumb. Loaded once per page, from topbar_html(). */
(function(){
  if (window.__ovsb) return; window.__ovsb = 1;
  var d = document.documentElement, bar = document.createElement('div'),
      th = document.createElement('div'), hide = 0, drag = null;
  bar.className = 'ov-sb'; bar.setAttribute('aria-hidden', 'true');
  th.className = 'ov-th'; bar.appendChild(th);
  function geo(){
    var vh = window.innerHeight, sh = d.scrollHeight;
    return {vh: vh, sh: sh, h: Math.max(32, vh * vh / Math.max(sh, 1))};
  }
  function show(){
    bar.classList.add('on'); clearTimeout(hide);
    hide = setTimeout(function(){ if (!drag) bar.classList.remove('on'); }, 1000);
  }
  function upd(reveal){
    var g = geo();
    if (g.sh <= g.vh + 1){ bar.style.display = 'none'; return; }
    bar.style.display = '';
    var st = window.scrollY || d.scrollTop || 0;
    th.style.height = g.h + 'px';
    th.style.transform = 'translateY(' + ((g.vh - g.h) * st / (g.sh - g.vh)) + 'px)';
    if (reveal) show();
  }
  th.addEventListener('pointerdown', function(e){
    drag = {y: e.clientY, st: window.scrollY || 0};
    try { th.setPointerCapture(e.pointerId); } catch (x) {}
    bar.classList.add('drag'); show(); e.preventDefault();
  });
  th.addEventListener('pointermove', function(e){
    if (!drag) return;
    var g = geo();
    window.scrollTo(0, drag.st + (e.clientY - drag.y) * (g.sh - g.vh) / Math.max(g.vh - g.h, 1));
  });
  function end(){ if (drag){ drag = null; bar.classList.remove('drag'); show(); } }
  th.addEventListener('pointerup', end); th.addEventListener('pointercancel', end);
  window.addEventListener('scroll', function(){ upd(true); }, {passive: true});
  window.addEventListener('resize', function(){ upd(false); });
  /* Long pages render their content after first paint (知識 cards, 模範解答):
     re-measure once everything is in, and once more after late layout. */
  window.addEventListener('load', function(){ upd(false); setTimeout(function(){ upd(false); }, 600); });
  document.addEventListener('mousemove', function(e){
    if (e.clientX >= window.innerWidth - 18) upd(true);
  }, {passive: true});
  function mount(){
    document.body.appendChild(bar); upd(false);
    if (window.ResizeObserver) new ResizeObserver(function(){ upd(false); }).observe(document.body);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount);
  else mount();
})();
"""


def head_css() -> str:
    """Everything a page's <style> needs for the chrome: site base, the bar, the
    header and pane hiding."""
    return TOPBAR_CSS + HEADER_CSS + "\n.lang-pane{display:contents}\n" + langs.pane_css()
