#!/usr/bin/env python3
"""Build the drill module's pages: drill/<LEVEL>/index.html + one page per tool.

    python3 .agents/jlpt-drill/scripts/build_drill.py [--level N2]     # make drill [LEVEL=N2]

Tools (jlpt-drill/SKILL.md §Tools):

    大問別練習.html            hub: every 大問 with its pool; resolves ?items= deep links
    大問別練習/<code>.html     one practice page per 言語知識・読解 大問 (問1 … 問14)
    聴解トレーニング.html      one real clip at a time, played as its span of a test's 聴解.mp3
    復習ノート.html            mistakes from exams, drills and 知識 quizzes; Leitner 1/3/7/14/30
    進捗.html                  score trend, section scores vs cutoff, per-大問 accuracy, weak areas
    読解ライブラリ.html        hub: every 読解 passage, by 大問
    読解ライブラリ/<code>.html  the passages of one 大問, 原文/訳 per learner language

Nothing here authors exam content or explanation prose: stems/options/passages
and every explanation come from each test's 詳細解説 files and the clip bank,
rendered through exam-model-answer's own renderer (explanation_box_html,
apply_furigana, format_passage_text, ptext_switch_html). Chrome comes from
lang_ui (one sticky bar, one language dropdown); labels from the registry's
`drill` namespace; storage from local_store.JLPTDrillStore. Every page is
self-contained (Pages copies only *.html) and links relatively.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drill_data as D            # noqa: E402  (puts the sibling skills on sys.path)
import langs                      # noqa: E402
import lang_ui                    # noqa: E402
import level as LEVEL             # noqa: E402
import build_model_answer as BMA  # noqa: E402
import app_style                  # noqa: E402
import local_store                # noqa: E402

ROOT = D.ROOT
NS = "drill"
PRIMARY = langs.primary()
ORDER = langs.order()
UI = langs.ui_table(NS)
SPLIT_LIMIT = 3_000_000          # bytes: a single page above this is split per 大問 (SKILL.md)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700'
         '&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">')


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def fu(s) -> str:
    """Escape, then ｜漢字《かな》 -> <ruby> (exam-model-answer's own converter)."""
    return BMA.apply_furigana(esc(s or ""))


def _ui(c: str, key: str) -> str:
    return UI.get(c, {}).get(key) or UI[PRIMARY].get(key, key)


def label(key: str, tag: str = "span", **fmt) -> str:
    """A UI label in every active language, one `.lang-pane` each."""
    def one(c):
        s = _ui(c, key)
        return esc(s.format(**fmt) if fmt else s)
    if len(ORDER) == 1:
        return one(ORDER[0])
    return "".join(f'<{tag} class="lang-pane" data-lang="{c}">{one(c)}</{tag}>' for c in ORDER)


def raw_label(key: str) -> str:
    """label() keeping `{placeholders}` for the page's JS to fill."""
    if len(ORDER) == 1:
        return esc(_ui(ORDER[0], key))
    return "".join(f'<span class="lang-pane" data-lang="{c}">{esc(_ui(c, key))}</span>' for c in ORDER)


def panes(render, tag: str = "div") -> str:
    if len(ORDER) == 1:
        return render(ORDER[0])
    return "".join(f'<{tag} class="lang-pane" data-lang="{c}">{render(c)}</{tag}>' for c in ORDER)


def js_data(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def squeeze(h: str) -> str:
    """Drop the indentation between tags the shared renderer emits (size, not looks)."""
    return re.sub(r">\s+<", "><", h).strip()


def mondai_label(m: dict) -> str:
    return f'{esc(m["mondai"])} {esc(m["name"])}'


# ------------------------------------------------------------------ chrome
CSS = r"""
:root{--font-sans:"Noto Sans JP","Hiragino Sans","Yu Gothic",system-ui,sans-serif;
  --font-serif:"Noto Serif JP","Hiragino Mincho ProN","Yu Mincho",serif;--primary:#2563eb;
  --ink:#0f172a;--ink2:#475569;--muted:#64748b;--line:#e2e8f0;--card:#fff;--bg:#f5f7fa;
  --ok:#15803d;--ng:#b91c1c}
body.drill [hidden]{display:none!important}
body.drill{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font-sans);
  line-height:1.6;-webkit-text-size-adjust:100%}
.dr-wrap{max-width:82em;margin:0 auto;padding:1.8em 1.5em 5em;box-sizing:border-box}
.dr-wrap h1{font-size:1.35rem;margin:.4rem 0 .2rem}
.dr-wrap h2{font-size:1.05rem;margin:1.4rem 0 .5rem}
.dr-lead{color:var(--ink2);margin:.2rem 0 .8rem;font-size:.92rem}
.dr-note{color:var(--muted);font-size:.8rem;margin:.3rem 0 1rem}
.dr-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(15rem,1fr));gap:.7rem}
.dr-card{display:block;background:var(--card);border:1px solid var(--line);border-radius:10px;
  padding:.8rem .95rem;color:inherit;text-decoration:none;min-width:0}
a.dr-card:hover{border-color:#93c5fd;box-shadow:0 1px 4px rgba(15,23,42,.08)}
.dr-card h3{margin:0 0 .25rem;font-size:1rem}
.dr-card p{margin:0;color:var(--ink2);font-size:.85rem}
.dr-card .n{margin-top:.45rem;color:var(--muted);font-size:.8rem}
.dr-card.off{opacity:.55}
.chips{display:flex;flex-wrap:wrap;gap:.35rem;align-items:center;margin:.35rem 0}
.chips .k{font-size:.8rem;color:var(--muted);min-width:5.5em}
.chip-btn{border:1px solid #cbd5e1;background:#fff;color:var(--ink);border-radius:999px;
  padding:.22rem .7rem;font:500 .82rem/1.3 var(--font-sans);cursor:pointer}
.chip-btn[aria-pressed="true"]{background:var(--primary);border-color:var(--primary);color:#fff}
.dr-box{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:1rem;margin:.8rem 0}
.dr-actions{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.qhead{display:flex;flex-wrap:wrap;justify-content:space-between;gap:.5rem;color:var(--muted);font-size:.82rem;margin-bottom:.6rem}
.qstem{font-family:var(--font-serif);font-size:1.05rem;margin:.4rem 0 .8rem;line-height:2}
.qopts{display:grid;gap:.45rem}
.qopt{display:flex;gap:.6rem;align-items:flex-start;text-align:left;border:1px solid #cbd5e1;background:#fff;
  border-radius:8px;padding:.55rem .75rem;font:1rem/1.9 var(--font-serif);color:var(--ink);cursor:pointer;width:100%}
.qopt b{font-family:var(--font-sans);color:var(--muted);min-width:1.2em}
.qopt:disabled{cursor:default}
.qopt.right{border-color:var(--ok);background:#f0fdf4}
.qopt.wrong{border-color:var(--ng);background:#fef2f2}
.bubbles{display:flex;gap:.5rem;flex-wrap:wrap}
.bubbles .qopt{width:auto;min-width:3rem;justify-content:center}
.verdict{margin-top:.8rem}
.verdict .v{font-weight:700;margin-bottom:.3rem}
.verdict .v.ok{color:var(--ok)} .verdict .v.ng{color:var(--ng)}
.fallback-note{font-size:.78rem;color:var(--muted);margin:.4rem 0 0}
.passage-box{border:1px solid #334155;background:#fff;padding:.9rem 1rem;font-family:var(--font-serif);
  line-height:2;margin:.4rem 0 .8rem;overflow-x:auto}
.passage-box table{border-collapse:collapse;width:100%}
.passage-box td,.passage-box th{border:1px solid #94a3b8;padding:.2rem .4rem}
details.pq-passage>summary{cursor:pointer;color:var(--ink2);font-size:.85rem}
.badge-o{display:inline-block;font-size:.72rem;border-radius:4px;padding:0 .35rem;border:1px solid #cbd5e1;color:var(--ink2)}
.badge-o.official{border-color:#1d4ed8;color:#1d4ed8}
.big{font-size:2.2rem;font-weight:700;margin:.2rem 0}
.empty{color:var(--muted);font-size:.9rem}
.dr-table{width:100%;border-collapse:collapse;font-size:.85rem}
.dr-table th,.dr-table td{border-bottom:1px solid var(--line);padding:.35rem .4rem;text-align:left;vertical-align:top}
.dr-table td.n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(9rem,1fr));gap:.6rem}
.tile{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.6rem .8rem}
.tile .l{font-size:.78rem;color:var(--muted)} .tile .v{font-size:1.5rem;font-weight:700}
.row-list{list-style:none;padding:0;margin:0}
.row-list li{display:flex;flex-wrap:wrap;gap:.3rem .7rem;align-items:center;padding:.45rem 0;border-bottom:1px solid var(--line);font-size:.86rem}
.row-list li .grow{flex:1 1 12rem;min-width:0}
.src-chip{font-size:.7rem;border-radius:4px;padding:0 .35rem;background:#eef2f7;color:var(--ink2)}
.boxno{font-size:.75rem;color:var(--ink2);white-space:nowrap}
/* listening player */
.lp{background:#0f172a;color:#e2e8f0;border-radius:10px;padding:.7rem .8rem;margin:.6rem 0}
.lp-row{display:flex;flex-wrap:wrap;gap:.4rem;align-items:center}
.lp button{border:1px solid #334155;background:#1e293b;color:#e2e8f0;border-radius:6px;
  padding:.3rem .6rem;font:600 .82rem/1.2 var(--font-sans);cursor:pointer;min-height:2rem}
.lp button[aria-pressed="true"]{background:#2563eb;border-color:#2563eb}
.lp .time{font-variant-numeric:tabular-nums;font-size:.82rem;margin-left:auto}
.lp-bar{position:relative;height:10px;background:#334155;border-radius:5px;margin:.6rem 0;cursor:pointer}
.lp-bar .fill{position:absolute;left:0;top:0;bottom:0;background:#60a5fa;border-radius:5px}
.lp-bar .ab{position:absolute;top:-3px;bottom:-3px;background:rgba(250,204,21,.35);border-left:2px solid #facc15;border-right:2px solid #facc15}
.lp .msg{font-size:.78rem;color:#fca5a5;margin-top:.3rem}
.lp label.pick{font-size:.78rem;color:#cbd5e1;cursor:pointer}
.lp label.pick input{display:none}
.script-box{white-space:normal;font-family:var(--font-serif);line-height:1.9;background:#fff;border:1px solid var(--line);
  border-radius:8px;padding:.7rem .9rem;margin:.5rem 0;font-size:.95rem}
.qlabel{font-weight:700;font-size:.85rem;margin:.6rem 0 .3rem;color:var(--ink2)}
.popts{margin:.2rem 0 .5rem;padding-left:0;list-style:none;font-family:var(--font-serif)}
/* library */
.psg{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:.8rem .9rem;margin:.7rem 0}
.psg-head{display:flex;flex-wrap:wrap;gap:.3rem .8rem;align-items:center;font-size:.82rem;color:var(--ink2)}
.psg details{margin-top:.5rem}
.psg summary{cursor:pointer;font-size:.85rem;color:var(--primary)}
.lib-q{border-top:1px dashed var(--line);padding-top:.5rem;margin-top:.5rem}
.lib-q ol{margin:.3rem 0 .3rem 1.4rem;padding:0;font-family:var(--font-serif)}
/* charts */
.viz{background:#fcfcfb;border:1px solid var(--line);border-radius:10px;padding:.7rem .8rem;margin:.6rem 0}
.viz svg{display:block;width:100%;height:auto;overflow:visible}
.viz .cap{font-size:.8rem;color:#52514e;margin:.1rem 0 .3rem}
.viz text{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:11px;fill:#52514e}
.viz text.muted{fill:#898781}
#tip{position:fixed;z-index:2000;pointer-events:none;background:#0b0b0b;color:#fff;font:12px/1.4 system-ui,sans-serif;
  padding:.35rem .5rem;border-radius:6px;max-width:16rem;display:none}
@media (max-width:600px){.dr-wrap{padding-top:.6rem}.qstem{font-size:1rem}.big{font-size:1.8rem}}
@media print{body.drill{background:#fff}.chips,.dr-actions,.lp,#tip{display:none!important}
  .dr-card,.dr-box,.psg{break-inside:avoid;border-color:#999}}
"""


def page(level: str, title: str, crumbs: list, body: str, scripts: str, stamps: str,
         up: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{esc(langs.html_lang(PRIMARY))}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
{FONTS}
<style>{app_style.APP_CSS}{BMA.EXPLANATION_CSS}{BMA.PASSAGE_TOGGLE_CSS}
{lang_ui.head_css()}
{CSS}</style>
</head>
<body class="drill" data-lang="{esc(PRIMARY)}">{stamps}
{lang_ui.topbar_html(crumbs, label=_ui(PRIMARY, "lang_label"))}
{body}
<div id="tip" role="tooltip"></div>
<script>
{lang_ui.SWITCHER_JS}
{local_store.LOCAL_STORE_JS}
{local_store.KNOWLEDGE_STORE_JS}
{local_store.DRILL_STORE_JS}
const LEVEL = {js_data(level)}, UP = {js_data(up)}, RESULT_FILE = {js_data(local_store.RESULT_JSON)};
const LBL = {js_data(JS_LABELS())}, TXT = {js_data(JS_TEXTS())};
{COMMON_JS}
{scripts}
{BMA.PASSAGE_TOGGLE_JS}
</script>
</body>
</html>
"""


def crumbs(level: str, depth: int, *tail) -> list:
    """level › ドリル › …, relative from a page `depth` folders below drill/<LEVEL>/."""
    back = "../" * depth
    out = [(lang_ui.pane("portal", "crumb_home"), f"{back}../../{D.INDEX_HTML}"),
           (esc(level), f"{back}../../{level}/{D.INDEX_HTML}"),
           (label("module"), f"{back}{D.INDEX_HTML}")]
    return out + list(tail)


# JS-built text: every label the scripts print, in every language as pane markup.
# The keys are read off the scripts themselves (every `lbl('key')`), so a label
# used in JS cannot be missing from the page; `src_*` is built from a variable.
_JS_EXTRA = ("src_exam", "src_drill", "src_knowledge")


def _js_src() -> str:
    return "".join(v for k, v in globals().items() if k.endswith("_JS") and isinstance(v, str))


def JS_LABELS() -> dict:
    keys = sorted(set(re.findall(r"lbl\('(\w+)'", _js_src())) | set(_JS_EXTRA))
    return {k: raw_label(k) for k in keys}


def JS_TEXTS() -> dict:
    """Plain strings per language for text that cannot hold pane markup (SVG
    <text>, tooltips): `txt('key')` picks the language on screen, and a chart
    that prints one re-draws on `langchange`."""
    keys = sorted(set(re.findall(r"txt\('(\w+)'", _js_src())))
    return {c: {k: _ui(c, k) for k in keys} for c in ORDER}


COMMON_JS = r"""
const S = window.JLPTDrillStore, DAY = 86400000;
function lbl(k, fmt){
  let s = LBL[k] || k;
  if (fmt) for (const x in fmt) s = s.split('{' + x + '}').join(fmt[x]);
  return s;
}
function txt(k, fmt){
  const c = (window.currentLang && window.currentLang()) || Object.keys(TXT)[0];
  let s = (TXT[c] && TXT[c][k]) || (TXT[Object.keys(TXT)[0]] || {})[k] || k;
  if (fmt) for (const x in fmt) s = s.split('{' + x + '}').join(fmt[x]);
  return s;
}
function esc(s){ return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function shuffle(a){ for (let i = a.length - 1; i > 0; i--){ const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
function param(n){ try { return new URLSearchParams(location.search).get(n); } catch (e){ return null; } }
function fmtDate(t){ const d = new Date(t); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }
/* Exam results: `make serve` exposes the test list at api/tests and every graded
   test's 採点結果.json as a file under tests/; a Pages build keeps them in
   JLPTStore (localStorage). One of the two answers; nothing is copied. */
let EXAM_SOURCE = null;
async function loadExamResults(){
  try {
    const r = await fetch(UP + 'api/tests?level=' + encodeURIComponent(LEVEL), {cache: 'no-store'});
    const ct = r.headers.get('content-type') || '';
    if (r.ok && ct.indexOf('json') >= 0){
      const j = await r.json();
      if (j && Array.isArray(j.tests)){
        EXAM_SOURCE = 'server';
        const rows = j.tests.filter(t => t.result);
        const got = await Promise.all(rows.map(async t => {
          try {
            const rr = await fetch(UP + 'tests/' + encodeURIComponent(t.id) + '/' + encodeURIComponent(RESULT_FILE), {cache: 'no-store'});
            return rr.ok ? {id: t.id, result: await rr.json()} : null;
          } catch (e){ return null; }
        }));
        return got.filter(x => x && x.result && x.result.summary);
      }
    }
  } catch (e){}
  EXAM_SOURCE = 'local';
  const out = [];
  try {
    for (const id of window.JLPTStore.ids()){
      const res = window.JLPTStore.result(id);
      if (res && res.summary) out.push({id: id, result: res});
    }
  } catch (e){}
  return out;
}
/* {itemId: {ok, t}} from the exam results; 聴解 keys through ALIAS when given. */
function examMarks(results, alias){
  const out = {};
  for (const r of results){
    const t = Date.parse(r.result.graded_at) || 0;
    for (const [k, v] of Object.entries(r.result.detail_gengo || {}))
      if (v && v.user != null) out[r.id + ':' + k] = {ok: !!v.is_correct, t: t};
    for (const [k, v] of Object.entries(r.result.detail_choukai || {})){
      if (!v || v.user == null) continue;
      const id = (alias && alias[r.id + ':' + k]) || (r.id + ':' + k);
      out[id] = {ok: !!v.is_correct, t: t};
    }
  }
  return out;
}
function storeNote(){
  const el = document.getElementById('store-src');
  if (el) el.innerHTML = EXAM_SOURCE === 'server' ? lbl('store_server') : lbl('store_local');
}
/* chip groups: <div class="chips" data-f="name"><button class="chip-btn" data-v="…"> */
function chipValue(f){ const b = document.querySelector('.chips[data-f="' + f + '"] .chip-btn[aria-pressed="true"]'); return b ? b.dataset.v : ''; }
function setChip(f, v){
  const g = document.querySelector('.chips[data-f="' + f + '"]'); if (!g) return;
  const bs = g.querySelectorAll('.chip-btn');
  let hit = false;
  bs.forEach(b => { const on = b.dataset.v === v; if (on) hit = true; b.setAttribute('aria-pressed', on ? 'true' : 'false'); });
  if (!hit && bs[0]) bs[0].setAttribute('aria-pressed', 'true');
}
document.addEventListener('click', ev => {
  const b = ev.target.closest('.chips .chip-btn'); if (!b) return;
  setChip(b.closest('.chips').dataset.f, b.dataset.v);
  document.dispatchEvent(new CustomEvent('chipchange', {detail: {f: b.closest('.chips').dataset.f}}));
});
/* tooltips over [data-tip] (charts) */
(function(){
  const tip = () => document.getElementById('tip');
  function show(ev, el){ const t = tip(); if (!t) return; t.innerHTML = el.getAttribute('data-tip'); t.style.display = 'block';
    const x = Math.min(ev.clientX + 12, window.innerWidth - t.offsetWidth - 8), y = Math.max(ev.clientY - t.offsetHeight - 10, 8);
    t.style.left = x + 'px'; t.style.top = y + 'px'; }
  document.addEventListener('mousemove', ev => { const el = ev.target.closest && ev.target.closest('[data-tip]'); if (el) show(ev, el); else if (tip()) tip().style.display = 'none'; });
  document.addEventListener('touchstart', ev => { const el = ev.target.closest && ev.target.closest('[data-tip]'); if (el){ const p = ev.touches[0]; show({clientX: p.clientX, clientY: p.clientY}, el); } else if (tip()) tip().style.display = 'none'; }, {passive: true});
})();
"""


def chips(f: str, options: list[tuple[str, str]], k: str | None = None, default: str | None = None) -> str:
    """A row of toggle chips; options = [(value, label key)]."""
    default = options[0][0] if default is None else default
    bs = "".join(f'<button type="button" class="chip-btn" data-v="{esc(v)}" '
                 f'aria-pressed="{"true" if v == default else "false"}">{label(lk) if lk else esc(v)}</button>'
                 for v, lk in options)
    head = f'<span class="k">{label(k)}</span>' if k else ""
    return f'<div class="chips" data-f="{esc(f)}">{head}{bs}</div>'


def stamp_list(pool_sources: list[Path]) -> str:
    return D.src_sha_comments(pool_sources + [D.KNOWLEDGE_LINKS])


# --------------------------------------------------------------- rendering
def explanation_html(prose: dict, key: str, answer: int, choukai: bool) -> str:
    """exam-model-answer's own box, one pane per language. A language with no
    prose for the item shows the primary set under a one-line note — never blank."""
    det, missing = {}, []
    for c in ORDER:
        if c in prose:
            det[c] = {key: prose[c]}
        else:
            det[c] = {key: prose.get(PRIMARY, {})}
            missing.append(c)
    box = BMA.explanation_box_html(det, key, answer, "", ORDER, choukai=choukai)
    note = ""
    if missing and len(ORDER) > 1:
        note = "".join(f'<span class="lang-pane" data-lang="{c}"><p class="fallback-note">'
                       f'{esc(_ui(c, "fallback_note"))}</p></span>' for c in missing)
    return squeeze(note + box)


def passage_html(text: str) -> str:
    return f'<div class="passage-box">{BMA.format_passage_text(text)}</div>'


def plain_len(text: str) -> int:
    t = re.sub(r"｜?([^｜《》]+?)《[^》]*》", r"\1", text or "")
    t = re.sub(r"<[^>]+>|\*\*|[|\-\s]", "", t)
    return len(t)


# ----------------------------------------------------------- 大問別練習
PRACTICE_JS = r"""
let EXAM = {};
const st = {pool: [], i: 0, score: 0, wrong: [], answered: false, review: false, last: []};
function attempts(){ return S.attempts(); }
function seen(id, A){ const a = A[id]; return !!(a && a.length) || !!EXAM[id]; }
function missed(id, A){ const a = A[id]; if (a && a.length) return !a[a.length - 1].ok; return !!(EXAM[id] && !EXAM[id].ok); }
function filtered(){
  const o = chipValue('origin'), s = chipValue('status'), A = attempts();
  return ITEMS.map((x, i) => i).filter(i => {
    const x = ITEMS[i];
    if (o && x.o !== o) return false;
    if (s === 'unseen' && seen(x.id, A)) return false;
    if (s === 'missed' && !missed(x.id, A)) return false;
    return true;
  });
}
function view(w){ ['pq-setup', 'pq-run', 'pq-done'].forEach(id => document.getElementById(id).hidden = id !== w); }
function paintSetup(){
  const n = filtered().length, A = attempts();
  document.getElementById('pq-avail').innerHTML = lbl('items_n', {n: n});
  let tried = 0, ok = 0;
  for (const x of ITEMS){ const a = A[x.id]; if (a && a.length){ tried++; if (a[a.length - 1].ok) ok++; } }
  document.getElementById('pq-mine').innerHTML = tried ? '· ' + lbl('acc_n', {n: tried, p: Math.round(ok * 100 / tried)}) : '';
}
function start(pool, review){
  st.pool = pool; st.i = 0; st.score = 0; st.wrong = []; st.review = !!review; st.last = pool.slice();
  document.getElementById('pq-none').hidden = pool.length > 0;
  if (!pool.length){ view('pq-setup'); return; }
  view('pq-run'); show();
}
function startFromSetup(){
  let p = shuffle(filtered()); const n = chipValue('count');
  if (n !== 'all') p = p.slice(0, parseInt(n, 10));
  start(p, false);
}
function show(){
  const x = ITEMS[st.pool[st.i]]; st.answered = false;
  document.getElementById('pq-pos').innerHTML = lbl('pos_of', {i: st.i + 1, n: st.pool.length});
  document.getElementById('pq-src').innerHTML = '<span class="badge-o ' + x.o + '">' + (x.o === 'official' ? lbl('origin_official') : lbl('origin_mock')) + '</span> ' + esc(x.t) + ' · ' + esc(x.k);
  document.getElementById('pq-score').innerHTML = lbl('score_of', {s: st.score, n: st.i});
  const ps = document.getElementById('pq-passage');
  if (x.g >= 0){ ps.hidden = false; ps.querySelector('.pq-ptext').innerHTML = PASS[x.g]; ps.open = true; } else ps.hidden = true;
  document.getElementById('pq-stem').innerHTML = x.s;
  document.getElementById('pq-opts').innerHTML = x.op.map((o, k) =>
    '<button type="button" class="qopt" data-k="' + (k + 1) + '"><b>' + (k + 1) + '</b><span>' + o + '</span></button>').join('');
  document.getElementById('pq-verdict').hidden = true;
  document.getElementById('pq-next').hidden = true;
  window.scrollTo({top: 0});
}
function choose(k){
  if (st.answered) return; st.answered = true;
  const x = ITEMS[st.pool[st.i]], ok = k === x.a;
  if (ok) st.score++; else st.wrong.push(st.pool[st.i]);
  S.record(x.id, ok, k, 'practice', st.review || !!(EXAM[x.id] && !EXAM[x.id].ok));
  document.querySelectorAll('#pq-opts .qopt').forEach(b => {
    const kk = parseInt(b.dataset.k, 10); b.disabled = true;
    if (kk === x.a) b.classList.add('right'); else if (kk === k) b.classList.add('wrong');
  });
  const v = document.getElementById('pq-verdict');
  v.innerHTML = '<div class="v ' + (ok ? 'ok' : 'ng') + '">' + (ok ? lbl('verdict_ok') : lbl('verdict_ng') + ' — ' + lbl('answer_is', {n: x.a})) + '</div>' + x.x;
  v.hidden = false;
  document.getElementById('pq-score').innerHTML = lbl('score_of', {s: st.score, n: st.i + 1});
  const nx = document.getElementById('pq-next');
  nx.innerHTML = st.i + 1 < st.pool.length ? lbl('next') : lbl('finish'); nx.hidden = false;
}
function next(){
  if (st.i + 1 < st.pool.length){ st.i++; show(); return; }
  document.getElementById('pq-final').textContent = st.score + ' / ' + st.pool.length;
  document.getElementById('pq-retry-wrong').hidden = !st.wrong.length;
  view('pq-done'); paintSetup();
}
document.addEventListener('click', ev => {
  const o = ev.target.closest('#pq-opts .qopt'); if (o){ choose(parseInt(o.dataset.k, 10)); return; }
  const a = ev.target.closest('[data-act]'); if (!a) return;
  const act = a.dataset.act;
  if (act === 'start') startFromSetup();
  else if (act === 'next') next();
  else if (act === 'quit' || act === 'setup'){ view('pq-setup'); paintSetup(); }
  else if (act === 'retry') start(shuffle(st.last.slice()), st.review);
  else if (act === 'retry-wrong') start(shuffle(st.wrong.slice()), true);
});
document.addEventListener('chipchange', paintSetup);
document.addEventListener('DOMContentLoaded', () => {
  const s = param('status'); if (s) setChip('status', s);
  const o = param('origin'); if (o) setChip('origin', o);
  paintSetup();
  const want = (param('items') || '').split(',').filter(Boolean);
  if (want.length){
    const idx = {}; ITEMS.forEach((x, i) => idx[x.id] = i);
    start(want.filter(id => id in idx).map(id => idx[id]), param('review') === '1');
  }
  loadExamResults().then(rs => { EXAM = examMarks(rs); storeNote(); paintSetup(); });
});
"""


def practice_page(level: str, m: dict, items: list, passages: dict, sources: list[Path]) -> str:
    pidx, P, ITEMS = {}, [], []
    for it in items:
        g = -1
        if it.group:
            if it.group not in pidx:
                pidx[it.group] = len(P)
                P.append(passage_html(passages[it.group].text))
            g = pidx[it.group]
        ITEMS.append({"id": it.id, "t": it.test, "o": it.origin, "k": it.key, "a": it.answer, "g": g,
                      "s": BMA.apply_furigana(it.stem),
                      "op": [BMA.apply_furigana(o) for o in it.options],
                      "x": explanation_html(it.prose, it.key, it.answer, False)})
    n_off = sum(1 for i in items if i.origin == "official")
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + mondai_label(m), label("practice_page_lead"))
            + f'<main class="dr-wrap">'
            f'<p class="dr-note">{label("pool_counts", n=len(items), o=n_off, m=len(items) - n_off)} '
            f'<span id="pq-mine"></span></p>'
            f'<section id="pq-setup" class="dr-box">'
            + chips("origin", [("", "f_all"), ("official", "origin_official"), ("mock", "origin_mock")], "f_origin")
            + chips("status", [("", "f_all"), ("unseen", "f_unseen"), ("missed", "f_missed")], "f_status")
            + chips("count", [("10", None), ("20", None), ("50", None), ("all", "f_all")], "f_count")
            + f'<p class="dr-note" id="pq-avail"></p><p class="empty" id="pq-none" hidden>{label("none_match")}</p>'
            f'<div class="dr-actions"><button type="button" class="ui-btn primary" data-act="start">'
            f'{label("start")}</button></div></section>'
            f'<section id="pq-run" class="dr-box" hidden><div class="qhead"><span id="pq-pos"></span>'
            f'<span id="pq-src"></span><span id="pq-score"></span></div>'
            f'<details class="pq-passage" id="pq-passage" hidden><summary>{label("passage")}</summary>'
            f'<div class="pq-ptext"></div></details>'
            f'<div class="qstem" id="pq-stem"></div><div class="qopts" id="pq-opts"></div>'
            f'<div class="verdict" id="pq-verdict" hidden></div>'
            f'<div class="dr-actions"><button type="button" class="ui-btn" data-act="quit">{label("quit")}</button>'
            f'<button type="button" class="ui-btn primary" id="pq-next" data-act="next" hidden></button></div></section>'
            f'<section id="pq-done" class="dr-box" hidden><div>{label("session_score")}</div>'
            f'<div class="big" id="pq-final"></div><div class="dr-actions">'
            f'<button type="button" class="ui-btn" data-act="retry">{label("retry")}</button>'
            f'<button type="button" class="ui-btn" id="pq-retry-wrong" data-act="retry-wrong">{label("retry_wrong")}</button>'
            f'<button type="button" class="ui-btn primary" data-act="setup">{label("new_session")}</button>'
            f'</div></section><p class="dr-note"><span id="store-src"></span> {label("store_note")}</p></main>')
    scripts = (f"const CODE = {js_data(m['code'])};\nconst ITEMS = {js_data(ITEMS)};\n"
               f"const PASS = {js_data(P)};\n{PRACTICE_JS}")
    title = f"{level} {_ui(PRIMARY, 'tool_practice')} {m['mondai']}"
    cr = crumbs(level, 1, (label("tool_practice"), f"../{D.PRACTICE}.html"),
                (mondai_label(m), None))
    return page(level, title, cr, body, scripts, stamp_list(sources), "../../../")


HUB_JS = r"""
/* ?items=<id>,… — resolve each id to the page that holds it: a 言語知識・読解 key by
   its test's own 大問 map, a 聴解 key to 聴解トレーニング. One page → go there. */
function pageOf(id){
  const i = id.lastIndexOf(':'); if (i < 0) return null;
  const t = id.slice(0, i), k = id.slice(i + 1);
  if (/^問\d-/.test(k)) return LISTEN_PAGE;
  const q = parseInt(k, 10), r = RANGES[t]; if (!r || !q) return null;
  for (const [c, lo, hi] of r) if (q >= lo && q <= hi) return PAGES[c] || null;
  return null;
}
document.addEventListener('DOMContentLoaded', () => {
  const A = S.attempts();
  document.querySelectorAll('[data-code]').forEach(el => {
    const ids = CODE_IDS[el.dataset.code] || []; let n = 0, ok = 0;
    for (const id of ids){ const a = A[id]; if (a && a.length){ n++; if (a[a.length - 1].ok) ok++; } }
    const x = el.querySelector('.js-acc'); if (x) x.innerHTML = n ? lbl('acc_n', {n: n, p: Math.round(ok * 100 / n)}) : '';
  });
  const want = (param('items') || '').split(',').filter(Boolean);
  if (!want.length) return;
  const groups = {};
  for (const id of want){ const p = pageOf(id); if (p) (groups[p] = groups[p] || []).push(id); }
  const keys = Object.keys(groups), rv = param('review') === '1' ? '&review=1' : '';
  const box = document.getElementById('deeplink');
  const href = p => p + '?items=' + encodeURIComponent(groups[p].join(',')) + rv;
  if (keys.length === 1){ location.replace(href(keys[0])); return; }
  box.hidden = false;
  box.innerHTML = keys.length ? '<p>' + lbl('deeplink_split') + '</p><ul class="row-list">' + keys.map(p =>
    '<li><span class="grow">' + esc(decodeURIComponent(p.split('/').pop().replace('.html', ''))) + '</span><a class="ui-btn primary" href="' + href(p) + '">' + lbl('items_n', {n: groups[p].length}) + '</a></li>').join('') + '</ul>'
    : '<p>' + lbl('deeplink_none') + '</p>';
});
"""


def practice_hub(level: str, gp: D.GengoPool, cp: D.ChoukaiPool, sources: list[Path]) -> str:
    by = {}
    for it in gp.items:
        by.setdefault(it.code, []).append(it)
    cards, pages, code_ids = {}, {}, {}
    for m in D.gengo_mondai(level):
        its = by.get(m["code"], [])
        code_ids[m["code"]] = [i.id for i in its]
        off = sum(1 for i in its if i.origin == "official")
        inner = (f'<h3>{mondai_label(m)}</h3><p>{esc(m["part"])}</p>'
                 f'<div class="n">{label("pool_counts", n=len(its), o=off, m=len(its) - off)}</div>'
                 f'<div class="n js-acc"></div>')
        if its:
            pages[m["code"]] = f'{D.PRACTICE}/{m["code"]}.html'
            cards.setdefault(m["section"], []).append(
                f'<a class="dr-card" href="{esc(pages[m["code"]])}" data-code="{esc(m["code"])}">{inner}</a>')
        else:
            cards.setdefault(m["section"], []).append(f'<div class="dr-card off">{inner}</div>')
    for m in D.choukai_mondai(level):
        n = sum(1 for c in cp.clips if c.code == m["code"])
        code_ids[m["code"]] = [q.id for c in cp.clips if c.code == m["code"] for q in c.questions]
        inner = (f'<h3>{mondai_label(m)}</h3><p>{label("tool_listening")}</p>'
                 f'<div class="n">{label("clips_n", n=n)}</div><div class="n js-acc"></div>')
        cards.setdefault("聴解", []).append(
            f'<a class="dr-card" href="{esc(D.LISTENING)}.html?mondai={esc(m["code"])}" '
            f'data-code="{esc(m["code"])}">{inner}</a>' if n else f'<div class="dr-card off">{inner}</div>')
    sec_label = {"言語知識": "sec_gengo", "読解": "sec_dokkai", "聴解": "sec_choukai"}
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + label("tool_practice"), label("tool_practice_desc"))
            + f'<main class="dr-wrap">'
            f'<div class="dr-box" id="deeplink" hidden></div>'
            + "".join(f'<h2>{label(sec_label[s])}</h2><div class="dr-grid">{"".join(cs)}</div>'
                      for s, cs in cards.items())
            + f'<p class="dr-note">{label("store_note")}</p></main>')
    scripts = (f"const RANGES = {js_data(gp.ranges)};\nconst PAGES = {js_data(pages)};\n"
               f"const LISTEN_PAGE = {js_data(D.LISTENING + '.html')};\n"
               f"const CODE_IDS = {js_data(code_ids)};\n{HUB_JS}")
    title = f"{level} {_ui(PRIMARY, 'tool_practice')}"
    return page(level, title, crumbs(level, 0, (label("tool_practice"), None)), body, scripts,
                stamp_list(sources), "../../")


# ----------------------------------------------------------- 聴解トレーニング
LISTEN_JS = r"""
let EXAM = {};
const au = document.getElementById('au');
const st = {pool: [], i: 0, score: 0, wrong: [], review: false, last: [], got: {}};
let cur = null, A = null, B = null, pendingSeek = null;
function attempts(){ return S.attempts(); }
function clipSeen(c, Aa){ return c.q.some(q => (Aa[q.id] && Aa[q.id].length) || EXAM[q.id]); }
function clipMissed(c, Aa){ return c.q.some(q => { const a = Aa[q.id]; if (a && a.length) return !a[a.length - 1].ok; return !!(EXAM[q.id] && !EXAM[q.id].ok); }); }
function filtered(){
  const m = chipValue('mondai'), o = chipValue('origin'), s = chipValue('status'), Aa = attempts();
  return CLIPS.map((c, i) => i).filter(i => {
    const c = CLIPS[i];
    if (m && c.c !== m) return false;
    if (o && c.o !== o) return false;
    if (s === 'unseen' && clipSeen(c, Aa)) return false;
    if (s === 'missed' && !clipMissed(c, Aa)) return false;
    return true;
  });
}
function view(w){ ['lt-setup', 'lt-run', 'lt-done'].forEach(id => document.getElementById(id).hidden = id !== w); }
function paintSetup(){ document.getElementById('lt-avail').innerHTML = lbl('clips_n', {n: filtered().length}); }
function start(pool, review){
  st.pool = pool; st.i = 0; st.score = 0; st.wrong = []; st.review = !!review; st.last = pool.slice();
  document.getElementById('lt-none').hidden = pool.length > 0;
  if (!pool.length){ view('lt-setup'); return; }
  view('lt-run'); show();
}
function startFromSetup(){
  let p = shuffle(filtered()); const n = chipValue('count');
  if (n !== 'all') p = p.slice(0, parseInt(n, 10));
  start(p, false);
}
/* ---- the player: one clip = [s, e] of a test's 聴解.mp3 ---- */
function fmt(t){ t = Math.max(0, t); return Math.floor(t / 60) + ':' + String(Math.floor(t % 60)).padStart(2, '0'); }
function seek(t){ if (au.readyState >= 1) au.currentTime = t; else pendingSeek = t; }
au.addEventListener('loadedmetadata', () => { if (pendingSeek != null){ au.currentTime = pendingSeek; pendingSeek = null; } });
au.addEventListener('error', () => {
  if (!cur) return;
  if (!au.dataset.triedFallback && cur.fb){ au.dataset.triedFallback = '1'; pendingSeek = cur.s; au.src = cur.fb; au.load(); return; }
  document.getElementById('lt-msg').hidden = false;
});
au.addEventListener('timeupdate', () => {
  if (!cur) return;
  const t = au.currentTime;
  if (A != null && B != null && t >= B){ au.currentTime = A; return; }
  if (t >= cur.e){ au.pause(); au.currentTime = cur.e; }
  if (t < cur.s - 0.3 && !au.paused) au.currentTime = cur.s;
  paintTime();
});
au.addEventListener('play', paintPlay); au.addEventListener('pause', paintPlay);
function paintPlay(){ const b = document.getElementById('lt-play'); b.textContent = au.paused ? '▶︎' : '❚❚'; b.setAttribute('aria-pressed', au.paused ? 'false' : 'true'); }
function paintTime(){
  if (!cur) return;
  const len = cur.e - cur.s, t = Math.min(Math.max(au.currentTime - cur.s, 0), len);
  document.getElementById('lt-fill').style.width = (len ? t * 100 / len : 0) + '%';
  document.getElementById('lt-time').textContent = fmt(t) + ' / ' + fmt(len);
  const ab = document.getElementById('lt-ab');
  if (A != null){ const a = (A - cur.s) * 100 / len, b = ((B != null ? B : au.currentTime) - cur.s) * 100 / len;
    ab.hidden = false; ab.style.left = a + '%'; ab.style.width = Math.max(b - a, 0.5) + '%'; } else ab.hidden = true;
}
function loadClip(c){
  au.pause(); A = B = null; paintAB();
  document.getElementById('lt-msg').hidden = true;
  if (au.getAttribute('data-clip-src') !== c.src){
    au.dataset.triedFallback = ''; au.setAttribute('data-clip-src', c.src);
    pendingSeek = c.s; au.src = c.src; au.load();
  } else seek(c.s);
  paintTime(); paintPlay();
}
function play(){
  if (!cur) return;
  if (au.paused){ if (au.currentTime < cur.s || au.currentTime >= cur.e - 0.05) seek(A != null ? A : cur.s); au.play().catch(() => {}); }
  else au.pause();
}
function nudge(d){ if (!cur) return; seek(Math.min(Math.max(au.currentTime + d, cur.s), cur.e)); paintTime(); }
function restart(){ if (!cur) return; seek(cur.s); au.play().catch(() => {}); }
function setAB(){
  if (!cur) return;
  const t = au.currentTime;
  if (A == null || B != null){ A = t; B = null; } else if (t > A + 0.5) B = t; else { A = t; }
  paintAB(); paintTime();
}
function clearAB(){ A = B = null; paintAB(); paintTime(); }
function paintAB(){
  const b = document.getElementById('lt-abbtn');
  b.textContent = A == null ? 'A' : (B == null ? 'A→B' : 'A↔B');
  b.setAttribute('aria-pressed', B != null ? 'true' : 'false');
  document.getElementById('lt-abclear').hidden = A == null;
}
function setRate(r){ au.playbackRate = r; document.querySelectorAll('[data-rate]').forEach(b => b.setAttribute('aria-pressed', parseFloat(b.dataset.rate) === r ? 'true' : 'false')); }
document.getElementById('lt-bar').addEventListener('click', ev => {
  if (!cur) return; const r = ev.currentTarget.getBoundingClientRect();
  seek(cur.s + (cur.e - cur.s) * Math.min(Math.max((ev.clientX - r.left) / r.width, 0), 1)); paintTime();
});
function pick(inp){
  const f = inp.files && inp.files[0]; if (!f || !cur) return;
  au.dataset.triedFallback = '1'; au.setAttribute('data-clip-src', 'picked:' + cur.t);
  pendingSeek = cur.s; au.src = URL.createObjectURL(f); au.load(); document.getElementById('lt-msg').hidden = true;
}
/* ---- questions ---- */
function show(){
  cur = CLIPS[st.pool[st.i]]; st.got = {};
  document.getElementById('lt-pos').innerHTML = lbl('pos_of', {i: st.i + 1, n: st.pool.length});
  document.getElementById('lt-src').innerHTML = '<span class="badge-o ' + (cur.o === 'official' ? 'official' : '') + '">' + (cur.o === 'official' ? lbl('origin_official') : lbl('origin_textbook')) + '</span> ' + esc(cur.c) + ' · ' + esc(cur.t);
  document.getElementById('lt-score').innerHTML = lbl('score_of', {s: st.score, n: st.i});
  document.getElementById('lt-qs').innerHTML = cur.q.map((q, qi) =>
    (cur.q.length > 1 ? '<div class="qlabel">' + lbl('question_label', {n: qi + 1}) + '</div>' : '')
    + (q.op ? '<ol class="popts">' + q.op.map((o, k) => '<li>' + (k + 1) + '　' + o + '</li>').join('') + '</ol>' : '')
    + '<div class="bubbles" data-q="' + qi + '">' + Array.from({length: q.n}, (_, k) =>
        '<button type="button" class="qopt" data-k="' + (k + 1) + '"><b>' + (k + 1) + '</b></button>').join('') + '</div>'
    + '<div class="verdict" data-v="' + qi + '" hidden></div>').join('');
  document.getElementById('lt-reveal').hidden = true;
  document.getElementById('lt-next').hidden = true;
  loadClip(cur);
}
function choose(qi, k){
  if (st.got[qi] != null) return; st.got[qi] = k;
  const q = cur.q[qi], ok = k === q.a;
  if (ok) st.score++; else if (st.wrong.indexOf(st.pool[st.i]) < 0) st.wrong.push(st.pool[st.i]);
  S.record(q.id, ok, k, 'listening', st.review || !!(EXAM[q.id] && !EXAM[q.id].ok));
  document.querySelectorAll('.bubbles[data-q="' + qi + '"] .qopt').forEach(b => {
    const kk = parseInt(b.dataset.k, 10); b.disabled = true;
    if (kk === q.a) b.classList.add('right'); else if (kk === k) b.classList.add('wrong');
  });
  const v = document.querySelector('.verdict[data-v="' + qi + '"]');
  v.innerHTML = '<div class="v ' + (ok ? 'ok' : 'ng') + '">' + (ok ? lbl('verdict_ok') : lbl('verdict_ng') + ' — ' + lbl('answer_is', {n: q.a})) + '</div>' + q.x;
  v.hidden = false;
  document.getElementById('lt-score').innerHTML = lbl('score_of', {s: st.score, n: st.i + 1});
  if (Object.keys(st.got).length === cur.q.length){
    document.getElementById('lt-script').innerHTML = cur.sc;
    document.getElementById('lt-reveal').hidden = false;
    const nx = document.getElementById('lt-next');
    nx.innerHTML = st.i + 1 < st.pool.length ? lbl('next') : lbl('finish'); nx.hidden = false;
  }
}
function next(){
  au.pause();
  if (st.i + 1 < st.pool.length){ st.i++; show(); return; }
  cur = null;
  document.getElementById('lt-final').textContent = st.score + ' / ' + st.pool.reduce((n, i) => n + CLIPS[i].q.length, 0);
  document.getElementById('lt-retry-wrong').hidden = !st.wrong.length;
  view('lt-done'); paintSetup();
}
document.addEventListener('click', ev => {
  const o = ev.target.closest('#lt-qs .qopt');
  if (o){ choose(parseInt(o.closest('.bubbles').dataset.q, 10), parseInt(o.dataset.k, 10)); return; }
  const r = ev.target.closest('[data-rate]'); if (r){ setRate(parseFloat(r.dataset.rate)); return; }
  const a = ev.target.closest('[data-act]'); if (!a) return;
  const act = a.dataset.act;
  if (act === 'start') startFromSetup();
  else if (act === 'play') play();
  else if (act === 'restart') restart();
  else if (act === 'back5') nudge(-5);
  else if (act === 'fwd5') nudge(5);
  else if (act === 'ab') setAB();
  else if (act === 'abclear') clearAB();
  else if (act === 'next') next();
  else if (act === 'quit' || act === 'setup'){ au.pause(); cur = null; view('lt-setup'); paintSetup(); }
  else if (act === 'retry') start(shuffle(st.last.slice()), st.review);
  else if (act === 'retry-wrong') start(shuffle(st.wrong.slice()), true);
});
document.addEventListener('chipchange', paintSetup);
document.addEventListener('DOMContentLoaded', () => {
  const m = param('mondai'); if (m) setChip('mondai', m);
  const s = param('status'); if (s) setChip('status', s);
  setRate(1); paintSetup();
  const want = (param('items') || '').split(',').filter(Boolean);
  if (want.length){
    const idx = {}; CLIPS.forEach((c, i) => c.q.forEach(q => idx[q.id] = i));
    const seenC = new Set(), pool = [];
    for (const id of want){ const i = idx[ALIAS[id] || id]; if (i != null && !seenC.has(i)){ seenC.add(i); pool.push(i); } }
    start(pool, param('review') === '1');
  }
  loadExamResults().then(rs => { EXAM = examMarks(rs, ALIAS); storeNote(); paintSetup(); });
});
"""

# 問題1/2 print their options in the booklet; 問題3/4 speak them; 問題5's
# multi-question item prints each question's options (jlpt-exam-structure).
PRINTED_SECTIONS = ("問題1", "問題2")


def listening_page(level: str, cp: D.ChoukaiPool, sources: list[Path]) -> str:
    CL = []
    for c in cp.clips:
        printed = c.code in PRINTED_SECTIONS or (c.code == "問題5" and len(c.questions) > 1)
        qs = []
        for q in c.questions:
            n = len(q.options) or (3 if c.code == "問題4" else 4)
            qs.append({"id": q.id, "a": q.answer, "n": n,
                       "op": [BMA.apply_furigana(esc(o)) for o in q.options] if printed and q.options else None,
                       "x": explanation_html(q.prose, q.key, q.answer, True)})
        CL.append({"id": c.id, "c": c.code, "o": c.origin, "t": c.test,
                   "src": f"../../tests/{c.test}/聴解.mp3", "fb": LEVEL.audio_release_url(c.test),
                   "s": round(c.start, 2), "e": round(c.end, 2),
                   "sc": esc(c.script).replace("\n", "<br>"), "q": qs})
    alias = {k: v for k, v in cp.aliases.items() if k != v}
    mondai = [(m["code"], None) for m in D.choukai_mondai(level)]
    n_off = sum(1 for c in cp.clips if c.origin == "official")
    rates = "".join(f'<button type="button" data-rate="{r}">{r}×</button>' for r in (0.75, 0.9, 1, 1.1, 1.25))
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + label("tool_listening"), label("listening_lead"))
            + f'<main class="dr-wrap">'
            f'<p class="dr-note">{label("clip_counts", n=len(cp.clips), o=n_off, m=len(cp.clips) - n_off)}</p>'
            f'<section id="lt-setup" class="dr-box">'
            + chips("mondai", [("", "f_all")] + mondai, "f_mondai")
            + chips("origin", [("", "f_all"), ("official", "origin_official"), ("textbook", "origin_textbook")], "f_origin")
            + chips("status", [("", "f_all"), ("unseen", "f_unseen"), ("missed", "f_missed")], "f_status")
            + chips("count", [("5", None), ("10", None), ("20", None), ("all", "f_all")], "f_count")
            + f'<p class="dr-note" id="lt-avail"></p><p class="empty" id="lt-none" hidden>{label("none_match")}</p>'
            f'<div class="dr-actions"><button type="button" class="ui-btn primary" data-act="start">{label("start")}</button></div></section>'
            f'<section id="lt-run" class="dr-box" hidden><div class="qhead"><span id="lt-pos"></span>'
            f'<span id="lt-src"></span><span id="lt-score"></span></div>'
            f'<div class="lp"><audio id="au" preload="metadata"></audio>'
            f'<div class="lp-row"><button type="button" id="lt-play" data-act="play" aria-label="play">&#x25B6;&#xFE0E;</button>'
            f'<button type="button" data-act="restart" aria-label="restart">&#x21BA;</button>'
            f'<button type="button" data-act="back5">−5s</button><button type="button" data-act="fwd5">+5s</button>'
            f'<button type="button" id="lt-abbtn" data-act="ab" title="A–B">A</button>'
            f'<button type="button" id="lt-abclear" data-act="abclear" hidden>✕</button>'
            f'<span class="time" id="lt-time">0:00 / 0:00</span></div>'
            f'<div class="lp-bar" id="lt-bar"><div class="ab" id="lt-ab" hidden></div><div class="fill" id="lt-fill"></div></div>'
            f'<div class="lp-row">{rates}<label class="pick">{label("pick_mp3")}'
            f'<input type="file" accept="audio/*" onchange="pick(this)"></label></div>'
            f'<div class="msg" id="lt-msg" hidden>{label("audio_error")}</div></div>'
            f'<p class="dr-note">{label("ab_help")}</p>'
            f'<div id="lt-qs"></div>'
            f'<div id="lt-reveal" hidden><details open><summary>{label("script")}</summary>'
            f'<div class="script-box" id="lt-script"></div></details></div>'
            f'<div class="dr-actions"><button type="button" class="ui-btn" data-act="quit">{label("quit")}</button>'
            f'<button type="button" class="ui-btn primary" id="lt-next" data-act="next" hidden></button></div></section>'
            f'<section id="lt-done" class="dr-box" hidden><div>{label("session_score")}</div>'
            f'<div class="big" id="lt-final"></div><div class="dr-actions">'
            f'<button type="button" class="ui-btn" data-act="retry">{label("retry")}</button>'
            f'<button type="button" class="ui-btn" id="lt-retry-wrong" data-act="retry-wrong">{label("retry_wrong")}</button>'
            f'<button type="button" class="ui-btn primary" data-act="setup">{label("new_session")}</button>'
            f'</div></section><p class="dr-note"><span id="store-src"></span> {label("store_note")}</p></main>')
    scripts = f"const CLIPS = {js_data(CL)};\nconst ALIAS = {js_data(alias)};\n{LISTEN_JS}"
    title = f"{level} {_ui(PRIMARY, 'tool_listening')}"
    return page(level, title, crumbs(level, 0, (label("tool_listening"), None)), body, scripts,
                stamp_list(sources), "../../")


# ----------------------------------------------------------- 復習ノート
# The notebook's collection rule, shared by 復習ノート and 進捗 so both count the same due items.
REVIEW_CORE_JS = r"""
function mondaiOf(id){
  const i = id.lastIndexOf(':'), t = id.slice(0, i), k = id.slice(i + 1);
  const m = /^問(\d)-/.exec(k); if (m) return '問題' + m[1];
  const q = parseInt(k, 10), r = RANGES[t]; if (!r) return null;
  for (const [c, lo, hi] of r) if (q >= lo && q <= hi) return c;
  return null;
}
function knowParse(id){ const p = id.split(':'); return {level: p[1], cat: p[2], qid: p.slice(3).join(':'), eid: p.slice(3).join(':').split('#')[0]}; }
let NOTE = [];
function collect(results){
  const now = Date.now(), M = {}, srs = S.srs(), att = S.attempts();
  function add(id, src, t){ const e = M[id] || (M[id] = {id: id, src: {}, t: 0}); e.src[src] = 1; e.t = Math.max(e.t, t || 0); }
  const ex = examMarks(results, ALIAS);
  for (const [id, v] of Object.entries(ex)) if (!v.ok) add(id, 'exam', v.t);
  for (const [id, list] of Object.entries(att)){ const l = list[list.length - 1]; if (l && !l.ok) add(id, 'drill', l.t); }
  for (const cat of Object.keys(KQ)){
    const h = window.JLPTKnowledgeStore.history(LEVEL, cat);
    for (const [qid, v] of Object.entries(h)){
      const id = '知識:' + LEVEL + ':' + cat + ':' + qid;
      if (!KQ[cat].entries[qid.split('#')[0]]) continue;
      const s = srs[id];
      if (s && typeof s.n === 'number' && v.n > s.n){ S.review(id, v.last === 1, {n: v.n}); }
      if (v.last === 0) add(id, 'knowledge', 0);
    }
  }
  const srs2 = S.srs();
  for (const id of Object.keys(srs2)) if (!M[id]) add(id, id.indexOf('知識:') === 0 ? 'knowledge' : 'drill', 0);
  NOTE = Object.values(M).map(e => {
    const s = srs2[e.id];
    return Object.assign(e, {box: s ? s.box : 1, due: s ? s.due : (e.t || now), kind: e.id.indexOf('知識:') === 0 ? 'know' : (/:問\d-/.test(e.id) ? 'listen' : 'gengo')});
  });
}
"""

REVIEW_JS = r"""
function rowLabel(e){
  if (e.kind === 'know'){
    const k = knowParse(e.id), c = KQ[k.cat], en = c && c.entries[k.eid];
    return '<b>' + (c ? c.label : esc(k.cat)) + '</b> · ' + esc(en ? en.head : k.eid) + ' <span class="boxno">#' + esc(k.qid.split('#')[1] || '') + '</span>';
  }
  const i = e.id.lastIndexOf(':'), c = mondaiOf(e.id), m = CODES[c];
  return '<b>' + (m ? esc(m.label) : esc(c || '')) + '</b> · ' + esc(e.id.slice(0, i)) + ' · ' + esc(e.id.slice(i + 1));
}
function target(e){
  if (e.kind === 'listen') return LISTEN_PAGE;
  if (e.kind === 'gengo'){ const c = mondaiOf(e.id); return c ? PRACTICE_HUB : null; }
  return null;
}
function paint(){
  const now = Date.now(), src = chipValue('src'), when = chipValue('when');
  const all = NOTE.filter(e => !src || e.src[src]);
  const due = all.filter(e => e.due <= now);
  document.getElementById('t-due').textContent = NOTE.filter(e => e.due <= now).length;
  document.getElementById('t-all').textContent = NOTE.length;
  for (let b = 1; b <= 5; b++) document.getElementById('t-box' + b).textContent = NOTE.filter(e => e.box === b).length;
  const shown = (when === 'all' ? all : due).slice().sort((a, b) => a.due - b.due);
  const box = document.getElementById('rv-groups');
  if (!shown.length){ box.innerHTML = '<p class="empty">' + (NOTE.length ? lbl('review_done') : lbl('review_empty_none')) + '</p>'; return; }
  /* group: one group per 大問 (practice / listening) and per 知識 category */
  const groups = {};
  for (const e of shown){
    const g = e.kind === 'know' ? 'k:' + knowParse(e.id).cat : mondaiOf(e.id) || '?';
    (groups[g] = groups[g] || []).push(e);
  }
  const order = Object.keys(groups).sort((a, b) => (CODE_ORDER[a] ?? 99) - (CODE_ORDER[b] ?? 99));
  box.innerHTML = order.map(g => {
    const es = groups[g], first = es[0], dueIds = es.filter(e => e.due <= now).map(e => e.id);
    let head = '', act = '';
    if (first.kind === 'know'){ const c = KQ[g.slice(2)]; head = c ? c.label : esc(g); }
    else { const m = CODES[g]; head = m ? esc(m.label) : esc(g);
      const t = target(first);
      if (t && dueIds.length) act = '<a class="ui-btn primary" href="' + t + '?items=' + encodeURIComponent(dueIds.join(',')) + '&review=1">' + lbl('review_open') + ' (' + dueIds.length + ')</a>'; }
    const rows = es.map(e => {
      const srcs = Object.keys(e.src).map(s => '<span class="src-chip">' + lbl('src_' + s) + '</span>').join(' ');
      const dueTxt = e.due <= now ? lbl('due_today') : lbl('due_on', {d: fmtDate(e.due)});
      let extra = '';
      if (e.kind === 'know'){
        const k = knowParse(e.id), en = KQ[k.cat] && KQ[k.cat].entries[k.eid];
        if (en) extra = '<a class="ui-btn" href="' + KNOW_ROOT + en.page + '#e-' + encodeURIComponent(k.eid) + '">' + lbl('open_card') + '</a>'
          + '<button type="button" class="ui-btn" data-kr="1" data-id="' + esc(e.id) + '">' + lbl('review_ok_btn') + '</button>'
          + '<button type="button" class="ui-btn" data-kr="0" data-id="' + esc(e.id) + '">' + lbl('review_notyet') + '</button>';
      }
      return '<li><span class="grow">' + rowLabel(e) + ' ' + srcs + '</span><span class="boxno">' + lbl('box_n', {n: e.box}) + ' · ' + dueTxt + '</span>' + extra + '</li>';
    }).join('');
    return '<div class="dr-box"><div class="qhead"><b>' + head + '</b><span>' + lbl('items_n', {n: es.length}) + '</span></div>' + (act ? '<div class="dr-actions" style="margin:0 0 .5rem">' + act + '</div>' : '') + '<ul class="row-list">' + rows + '</ul></div>';
  }).join('');
}
document.addEventListener('click', ev => {
  const b = ev.target.closest('[data-kr]'); if (!b) return;
  const id = b.dataset.id, k = knowParse(id), h = window.JLPTKnowledgeStore.history(k.level, k.cat)[k.qid] || {n: 0};
  S.review(id, b.dataset.kr === '1', {n: h.n || 0});
  loadExamResults().then(rs => { collect(rs); paint(); });
});
document.addEventListener('chipchange', paint);
document.addEventListener('DOMContentLoaded', () => {
  loadExamResults().then(rs => { collect(rs); storeNote(); paint(); });
});
"""


def _full_label(m: dict) -> str:
    """「問題3 語形成」; a 聴解 大問 is prefixed with its section, since 聴解's
    問題1–5 reuse the numbers of 言語知識's (exam wording, Japanese on every pane)."""
    return (f'{m["section"]} ' if m["section"] == "聴解" else "") + f'{m["mondai"]} {m["name"]}'


def _code_maps(level: str) -> tuple[dict, dict]:
    codes, order = {}, {}
    for i, m in enumerate(D.gengo_mondai(level) + D.choukai_mondai(level)):
        codes[m["code"]] = {"label": _full_label(m), "part": m["part"], "section": m["section"]}
        order[m["code"]] = i
    return codes, order


def _knowledge_js(level: str) -> dict:
    kq = D.knowledge_quiz(level)
    out = {}
    for stem, v in kq.items():
        if not v["entries"]:
            continue
        out[stem] = {"label": "".join(f'<span class="lang-pane" data-lang="{c}">'
                                      f'{esc(langs.ui(c, "knowledge").get(v["label"]) or stem)}</span>'
                                      for c in ORDER) if len(ORDER) > 1 else esc(stem),
                     "entries": v["entries"]}
    return out


def review_page(level: str, gp: D.GengoPool, cp: D.ChoukaiPool, sources: list[Path]) -> str:
    codes, order = _code_maps(level)
    for stem in D.knowledge_quiz(level):
        order[f"k:{stem}"] = 100 + len(order)
    alias = {k: v for k, v in cp.aliases.items() if k != v}
    tiles = (f'<div class="tiles"><div class="tile"><div class="l">{label("review_due")}</div>'
             f'<div class="v" id="t-due">0</div></div><div class="tile"><div class="l">{label("review_total")}</div>'
             f'<div class="v" id="t-all">0</div></div>'
             + "".join(f'<div class="tile"><div class="l">{label("box_n", n=b)} · {label("every_days", n=d)}</div>'
                       f'<div class="v" id="t-box{b}">0</div></div>'
                       for b, d in enumerate(local_store.DRILL_INTERVALS_DAYS, 1)) + '</div>')
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + label("tool_review"), label("review_lead"))
            + f'<main class="dr-wrap">{tiles}'
            + chips("when", [("due", "review_show_due"), ("all", "review_show_all")], "f_show")
            + chips("src", [("", "f_all"), ("exam", "src_exam"), ("drill", "src_drill"), ("knowledge", "src_knowledge")], "f_source")
            + f'<div id="rv-groups"></div>'
            f'<p class="dr-note">{label("review_rule")}</p>'
            f'<p class="dr-note"><span id="store-src"></span> {label("store_note")}</p></main>')
    scripts = (f"const RANGES = {js_data(gp.ranges)};\nconst CODES = {js_data(codes)};\n"
               f"const CODE_ORDER = {js_data(order)};\nconst ALIAS = {js_data(alias)};\n"
               f"const KQ = {js_data(_knowledge_js(level))};\n"
               f"const KNOW_ROOT = {js_data(f'../../knowledge/{level}/')};\n"
               f"const PRACTICE_HUB = {js_data(D.PRACTICE + '.html')}, LISTEN_PAGE = {js_data(D.LISTENING + '.html')};\n"
               f"{REVIEW_CORE_JS}\n{REVIEW_JS}")
    title = f"{level} {_ui(PRIMARY, 'tool_review')}"
    return page(level, title, crumbs(level, 0, (label("tool_review"), None)), body, scripts,
                stamp_list(sources + D.knowledge_sources(level)), "../../")


# ----------------------------------------------------------- 進捗
# Chart tokens: the dataviz reference palette's light chrome and categorical
# slot 1 (one series per chart — no legend box; the title names it).
PROGRESS_JS = r"""
const C = {s1: '#2a78d6', grid: '#e1e0d9', axis: '#c3c2b7', muted: '#898781', ink2: '#52514e', surf: '#fcfcfb'};
function svg(w, h, inner){ return '<svg viewBox="0 0 ' + w + ' ' + h + '" role="img">' + inner + '</svg>'; }
function colTop(x, y, w, h){ const r = Math.min(4, w / 2, h); return 'M' + x + ',' + (y + h) + 'V' + (y + r) + 'Q' + x + ',' + y + ' ' + (x + r) + ',' + y + 'H' + (x + w - r) + 'Q' + (x + w) + ',' + y + ' ' + (x + w) + ',' + (y + r) + 'V' + (y + h) + 'Z'; }
function barEnd(x, y, w, h){ const r = Math.min(4, h / 2, w); return 'M' + x + ',' + y + 'H' + (x + w - r) + 'Q' + (x + w) + ',' + y + ' ' + (x + w) + ',' + (y + r) + 'V' + (y + h - r) + 'Q' + (x + w) + ',' + (y + h) + ' ' + (x + w - r) + ',' + (y + h) + 'H' + x + 'Z'; }
/* score trend: one line, the pass mark as a labelled reference */
function chartW(id){ const el = document.getElementById(id); return Math.max(300, Math.round(((el && el.clientWidth) || 660) - 26)); }
function trendChart(rs, W){
  const H = 220, L = 34, R = 12, T = 12, Bm = 34, max = SCORING.max;
  const x = i => rs.length < 2 ? L + (W - L - R) / 2 : L + i * (W - L - R) / (rs.length - 1);
  const y = v => T + (H - T - Bm) * (1 - v / max);
  let g = '';
  for (let v = 0; v <= max; v += max / 4){ g += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + y(v) + '" y2="' + y(v) + '" stroke="' + C.grid + '" stroke-width="1"/><text x="' + (L - 6) + '" y="' + (y(v) + 4) + '" text-anchor="end" class="muted">' + v + '</text>'; }
  g += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + y(SCORING.pass) + '" y2="' + y(SCORING.pass) + '" stroke="' + C.ink2 + '" stroke-width="1"/><text x="' + (W - R) + '" y="' + (y(SCORING.pass) - 4) + '" text-anchor="end">' + esc(txt('chart_pass_label', {n: SCORING.pass})) + '</text>';
  const pts = rs.map((r, i) => [x(i), y(r.result.summary.total_scaled_score)]);
  if (pts.length > 1) g += '<polyline fill="none" stroke="' + C.s1 + '" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" points="' + pts.map(p => p.join(',')).join(' ') + '"/>';
  rs.forEach((r, i) => {
    const s = r.result.summary, tip = txt('chart_score_tip', {id: esc(r.id), d: fmtDate(Date.parse(r.result.graded_at) || 0), s: s.total_scaled_score, m: s.max_scaled_score});
    g += '<circle cx="' + pts[i][0] + '" cy="' + pts[i][1] + '" r="5" fill="' + C.s1 + '" stroke="' + C.surf + '" stroke-width="2"/>'
       + '<circle cx="' + pts[i][0] + '" cy="' + pts[i][1] + '" r="14" fill="transparent" data-tip="' + esc(tip) + '"/>';
    if (rs.length <= 8 || i === 0 || i === rs.length - 1) g += '<text x="' + pts[i][0] + '" y="' + (H - Bm + 16) + '" text-anchor="middle" class="muted">' + fmtDate(Date.parse(r.result.graded_at) || 0).slice(5) + '</text>';
  });
  const last = rs[rs.length - 1].result.summary.total_scaled_score;
  g += '<text x="' + Math.min(pts[pts.length - 1][0] + 8, W - R) + '" y="' + (pts[pts.length - 1][1] - 8) + '" text-anchor="' + (rs.length > 1 ? 'end' : 'start') + '" style="font-weight:600;fill:#0b0b0b">' + last + '</text>';
  return svg(W, H, g);
}
/* section scores of one sitting: one bar per section on the 0–max scale, the cutoff as a tick */
function sectionChart(r, W){
  const secs = SCORING.sections, rowH = 34, L = Math.min(190, Math.round(W * 0.4)), R = 60, H = secs.length * rowH + 20;
  const x = v => L + (W - L - R) * v / secs[0].max;
  let g = '';
  secs.forEach((sc, i) => {
    const s = (r.result.summary.sections || {})[sc.name] || {scaled_score: 0}, y0 = 8 + i * rowH, bh = 16;
    g += '<text x="' + (L - 8) + '" y="' + (y0 + 12) + '" text-anchor="end">' + esc(SEC_LABEL[sc.name] || sc.name) + '</text>';
    g += '<rect x="' + L + '" y="' + y0 + '" width="' + (W - L - R) + '" height="' + bh + '" fill="' + C.grid + '" opacity=".45" rx="2"/>';
    const w = Math.max(x(s.scaled_score) - L, 0);
    if (w > 0) g += '<path d="' + barEnd(L, y0, w, bh) + '" fill="' + C.s1 + '"/>';
    g += '<line x1="' + x(sc.cutoff) + '" x2="' + x(sc.cutoff) + '" y1="' + (y0 - 3) + '" y2="' + (y0 + bh + 3) + '" stroke="#0b0b0b" stroke-width="2"/>';
    const below = s.scaled_score < sc.cutoff;
    g += '<text x="' + (x(s.scaled_score) + 6) + '" y="' + (y0 + 12) + '">' + s.scaled_score + ' / ' + sc.max + (below ? ' ✕' : '') + '</text>';
    g += '<rect x="' + L + '" y="' + (y0 - 4) + '" width="' + (W - L - R) + '" height="' + (bh + 8) + '" fill="transparent" data-tip="' + esc(txt('chart_section_tip', {s: SEC_LABEL[sc.name] || sc.name, v: s.scaled_score, m: sc.max, c: sc.cutoff})) + '"/>';
  });
  g += '<text x="' + x(secs[0].cutoff) + '" y="' + (H - 2) + '" text-anchor="middle" class="muted">' + esc(txt('chart_cutoff_label', {n: secs[0].cutoff})) + '</text>';
  return svg(W, H, g);
}
/* per-大問 accuracy: exams + drills, one bar per 大問 */
function mondaiStats(rs){
  const st = {}; const add = (c, ok, n, src) => { const s = st[c] || (st[c] = {ok: 0, n: 0, eOk: 0, eN: 0, dOk: 0, dN: 0}); s.ok += ok; s.n += n; if (src === 'e'){ s.eOk += ok; s.eN += n; } else { s.dOk += ok; s.dN += n; } };
  for (const r of rs) for (const [c, v] of Object.entries(r.result.taxonomy_stats || {})) if (v.total) add(c, v.correct, v.total, 'e');
  for (const [id, list] of Object.entries(S.attempts())){
    const c = mondaiOf(id); if (!c) continue;
    for (const a of list) add(c, a.ok ? 1 : 0, 1, 'd');
  }
  return st;
}
function mondaiChart(st, W){
  const rows = CODE_LIST.filter(c => st[c.code] && st[c.code].n);
  if (!rows.length) return '';
  const rowH = 24, L = Math.min(170, Math.round(W * 0.4)), R = Math.min(110, Math.round(W * 0.28)), H = rows.length * rowH + 24;
  const x = p => L + (W - L - R) * p / 100;
  let g = '';
  [0, 50, 100].forEach(p => { g += '<line x1="' + x(p) + '" x2="' + x(p) + '" y1="4" y2="' + (H - 18) + '" stroke="' + C.grid + '" stroke-width="1"/><text x="' + x(p) + '" y="' + (H - 4) + '" text-anchor="middle" class="muted">' + p + '%</text>'; });
  rows.forEach((c, i) => {
    const s = st[c.code], p = Math.round(s.ok * 100 / s.n), y0 = 6 + i * rowH, bh = 14;
    g += '<text x="' + (L - 8) + '" y="' + (y0 + 11) + '" text-anchor="end">' + esc(c.label) + '</text>';
    if (p > 0) g += '<path d="' + barEnd(L, y0, x(p) - L, bh) + '" fill="' + C.s1 + '"/>';
    g += '<text x="' + (x(p) + 6) + '" y="' + (y0 + 11) + '">' + p + '% (' + s.n + ')' + (p < WEAK && s.n >= WEAK_MIN ? ' ' + esc(txt('weak_tag')) : '') + '</text>';
    g += '<rect x="0" y="' + (y0 - 4) + '" width="' + W + '" height="' + rowH + '" fill="transparent" data-tip="' + esc(txt('chart_mondai_tip', {m: c.label, p: p, n: s.n, e: s.eN ? Math.round(s.eOk * 100 / s.eN) + '%' : '—', en: s.eN, d: s.dN ? Math.round(s.dOk * 100 / s.dN) + '%' : '—', dn: s.dN})) + '"/>';
  });
  return svg(W, H, g);
}
function tableHtml(head, rows){ return '<details><summary class="dr-note">' + lbl('table_view') + '</summary><table class="dr-table"><thead><tr>' + head.map(h => '<th>' + h + '</th>').join('') + '</tr></thead><tbody>' + rows.map(r => '<tr>' + r.map((c, i) => '<td' + (i ? ' class="n"' : '') + '>' + c + '</td>').join('') + '</tr>').join('') + '</tbody></table></details>'; }
function paint(rs){
  rs.sort((a, b) => (Date.parse(a.result.graded_at) || 0) - (Date.parse(b.result.graded_at) || 0));
  const att = S.attempts(); let dn = 0, dok = 0;
  for (const list of Object.values(att)) for (const a of list){ dn++; if (a.ok) dok++; }
  const srs = S.srs(), now = Date.now();
  document.getElementById('p-tests').textContent = rs.length;
  document.getElementById('p-best').textContent = rs.length ? Math.max(...rs.map(r => r.result.summary.total_scaled_score)) : '—';
  document.getElementById('p-drill').textContent = dn;
  document.getElementById('p-drillacc').textContent = dn ? Math.round(dok * 100 / dn) + '%' : '—';
  collect(rs); document.getElementById('p-due').textContent = NOTE.filter(e => e.due <= now).length;
  const tr = document.getElementById('p-trend'), se = document.getElementById('p-sections');
  if (!rs.length){ tr.innerHTML = '<p class="empty">' + lbl('no_results') + '</p>'; se.innerHTML = ''; }
  else {
    tr.innerHTML = trendChart(rs, chartW('p-trend')) + tableHtml([lbl('col_test'), lbl('col_date'), lbl('col_total')], rs.map(r => [esc(r.id), fmtDate(Date.parse(r.result.graded_at) || 0), r.result.summary.total_scaled_score + ' / ' + r.result.summary.max_scaled_score + ' ' + (r.result.summary.passed ? lbl('pass') : lbl('fail'))]));
    const last = rs[rs.length - 1];
    se.innerHTML = '<div class="cap">' + lbl('sections_latest', {id: esc(last.id)}) + '</div>' + sectionChart(last, chartW('p-sections'))
      + tableHtml([lbl('col_test')].concat(SCORING.sections.map(s => esc(SEC_LABEL[s.name] || s.name))), rs.map(r => [esc(r.id)].concat(SCORING.sections.map(s => { const v = ((r.result.summary.sections || {})[s.name] || {}).scaled_score; return v == null ? '—' : v + (v < s.cutoff ? ' ✕' : ''); }))));
  }
  const st = mondaiStats(rs), mc = document.getElementById('p-mondai');
  const ch = mondaiChart(st, chartW('p-mondai'));
  mc.innerHTML = ch ? ch + tableHtml([lbl('col_mondai'), lbl('col_exam'), lbl('col_drill'), lbl('col_all')], CODE_LIST.filter(c => st[c.code]).map(c => { const s = st[c.code]; return [esc(c.label), s.eN ? s.eOk + '/' + s.eN : '—', s.dN ? s.dOk + '/' + s.dN : '—', Math.round(s.ok * 100 / s.n) + '%']; })) : '<p class="empty">' + lbl('no_activity') + '</p>';
  const weak = CODE_LIST.filter(c => st[c.code] && st[c.code].n >= WEAK_MIN && st[c.code].ok * 100 / st[c.code].n < WEAK)
    .sort((a, b) => st[a.code].ok / st[a.code].n - st[b.code].ok / st[b.code].n);
  const wk = document.getElementById('p-weak');
  wk.innerHTML = weak.length ? '<ul class="row-list">' + weak.map(c => {
    const s = st[c.code], links = [];
    if (c.listen) links.push('<a class="ui-btn primary" href="' + LISTEN_PAGE + '?mondai=' + encodeURIComponent(c.code) + '&status=missed">' + lbl('weak_listen') + '</a>');
    else if (PAGES[c.code]) links.push('<a class="ui-btn primary" href="' + PAGES[c.code] + '?status=missed">' + lbl('weak_practice') + '</a>');
    for (const k of (KLINKS[c.part] || [])) links.push('<a class="ui-btn" href="' + KNOW_ROOT + k.page + '">' + lbl('weak_knowledge') + ': ' + k.label + '</a>');
    return '<li><span class="grow"><b>' + esc(c.label) + '</b> — ' + Math.round(s.ok * 100 / s.n) + '% (' + s.n + ')</span>' + links.join('') + '</li>';
  }).join('') + '</ul>' : '<p class="empty">' + lbl('weak_none', {p: WEAK, n: WEAK_MIN}) + '</p>';
}
let RS = null;
document.addEventListener('langchange', () => { if (RS) paint(RS); });
let RZ = null; window.addEventListener('resize', () => { clearTimeout(RZ); RZ = setTimeout(() => { if (RS) paint(RS); }, 200); });
document.addEventListener('DOMContentLoaded', () => { loadExamResults().then(rs => { RS = rs; storeNote(); paint(rs); }); });
"""

WEAK_PCT, WEAK_MIN_N = 60, 5     # 要強化 below 60 % — the result screen's own band (exam-app)


def progress_page(level: str, gp: D.GengoPool, cp: D.ChoukaiPool, sources: list[Path]) -> str:
    sc = LEVEL.scoring(level)
    sec_label = {}
    for s in sc["sections"]:
        sec_label[s["name"]] = re.sub(r"（.*?）", "", s["name"])   # 言語知識（文字・語彙・文法） -> 言語知識
    code_list, pages = [], {}
    have = {i.code for i in gp.items}
    for m in D.gengo_mondai(level):
        code_list.append({"code": m["code"], "label": f'{m["mondai"]} {m["name"]}', "part": m["part"], "listen": False})
        if m["code"] in have:
            pages[m["code"]] = f'{D.PRACTICE}/{m["code"]}.html'
    for m in D.choukai_mondai(level):
        code_list.append({"code": m["code"], "label": _full_label(m), "part": "聴解", "listen": True})
    kq = D.knowledge_quiz(level)
    klinks = {}
    for part, stems in D.knowledge_links(level).items():
        for s in stems:
            k = kq.get(s)
            if k and k["available"]:
                lab = ("".join(f'<span class="lang-pane" data-lang="{c}">{esc(langs.ui(c, "knowledge").get(k["label"]) or s)}</span>'
                               for c in ORDER) if len(ORDER) > 1 else esc(s))
                klinks.setdefault(part, []).append({"page": f"{s}.html", "label": lab})
    tiles = "".join(f'<div class="tile"><div class="l">{label(k)}</div><div class="v" id="{i}">—</div></div>'
                    for i, k in (("p-tests", "p_tests"), ("p-best", "p_best"), ("p-drill", "p_drill"),
                                 ("p-drillacc", "p_drillacc"), ("p-due", "p_due")))
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + label("tool_progress"), label("progress_lead"))
            + f'<main class="dr-wrap"><div class="tiles">{tiles}</div>'
            f'<h2>{label("chart_trend")}</h2><div class="viz" id="p-trend"></div>'
            f'<h2>{label("chart_sections")}</h2><div class="viz" id="p-sections"></div>'
            f'<h2>{label("chart_mondai")}</h2><div class="viz" id="p-mondai"></div>'
            f'<h2>{label("weak_title")}</h2><div id="p-weak"></div>'
            f'<p class="dr-note">{label("progress_scale_note")}</p>'
            f'<p class="dr-note"><span id="store-src"></span> {label("store_note")}</p></main>')
    scripts = (f"const SCORING = {js_data(sc)};\nconst SEC_LABEL = {js_data(sec_label)};\n"
               f"const RANGES = {js_data(gp.ranges)};\nconst CODE_LIST = {js_data(code_list)};\n"
               f"const PAGES = {js_data(pages)};\nconst KLINKS = {js_data(klinks)};\n"
               f"const KNOW_ROOT = {js_data(f'../../knowledge/{level}/')};\n"
               f"const LISTEN_PAGE = {js_data(D.LISTENING + '.html')};\n"
               f"const ALIAS = {js_data({k: v for k, v in cp.aliases.items() if k != v})};\n"
               f"const KQ = {js_data(_knowledge_js(level))};\n"
               f"const WEAK = {WEAK_PCT}, WEAK_MIN = {WEAK_MIN_N};\n{REVIEW_CORE_JS}\n{PROGRESS_JS}")
    title = f"{level} {_ui(PRIMARY, 'tool_progress')}"
    return page(level, title, crumbs(level, 0, (label("tool_progress"), None)), body, scripts,
                stamp_list(sources + D.knowledge_sources(level)), "../../")


# ----------------------------------------------------------- 読解ライブラリ
LENGTH_BINS = ((0, 400, "len_short"), (400, 800, "len_mid"), (800, 10**9, "len_long"))

LIBRARY_JS = r"""
function paint(){
  const o = chipValue('origin'), l = chipValue('len');
  let n = 0;
  document.querySelectorAll('.psg').forEach(el => {
    const on = (!o || el.dataset.o === o) && (!l || el.dataset.len === l);
    el.hidden = !on; if (on) n++;
  });
  document.getElementById('lib-n').innerHTML = lbl('passages_n', {n: n});
}
document.addEventListener('chipchange', paint);
/* A new edition starts every passage on 原文, like 練習.html (exam-app §練習モード). */
document.addEventListener('langchange', () => document.querySelectorAll('.passage-tr').forEach(b => b.dataset.ptext = 'src'));
document.addEventListener('DOMContentLoaded', () => {
  paint();
});
"""


def _len_bin(n: int) -> str:
    return next(k for lo, hi, k in LENGTH_BINS if lo <= n < hi)


def passage_block(p: D.Passage, title: str) -> str:
    """The passage with a 原文/訳 toggle in every learner pane that has a
    translation (build_model_answer's own control over `passage_translation`)."""
    src = passage_html(p.text)

    def one(c):
        tr = p.translations.get(c)
        if c == PRIMARY or not tr:
            return f'<div class="passage-head"><span class="passage-title">{title}</span></div>{src}'
        return (f'<div class="passage-tr" data-ptext="src"><div class="passage-head">'
                f'<span class="passage-title">{title}</span>{BMA.ptext_switch_html(c)}</div>'
                f'<div class="ptext-pane" data-ptext="src">{src}</div>'
                f'<div class="ptext-pane" data-ptext="tr"><div class="passage-box">'
                f'{BMA.format_passage_text(esc(tr))}</div></div></div>')
    return panes(one)


def library_page(level: str, m: dict, passages: list, items: dict, sources: list[Path]) -> str:
    blocks = []
    for p in sorted(passages, key=lambda p: (plain_len(p.text), p.id)):
        n = plain_len(p.text)
        qs = []
        for iid in p.items:
            it = items[iid]
            opts = "".join(f"<li>{BMA.apply_furigana(o)}</li>" for o in it.options)
            qs.append(f'<div class="lib-q"><div class="qstem">{esc(it.key)}　{BMA.apply_furigana(it.stem)}</div>'
                      f'<ol>{opts}</ol><details><summary>{label("show_answer")}</summary>'
                      f'<p><b>{label("answer_is", n=it.answer)}</b></p>'
                      f'{explanation_html(it.prose, it.key, it.answer, False)}</details></div>')
        prac = f'../{D.PRACTICE}.html?items={",".join(p.items)}'
        blocks.append(
            f'<article class="psg" id="{esc(p.id)}" data-o="{esc(p.origin)}" data-len="{_len_bin(n)}">'
            f'<div class="psg-head"><span class="badge-o {esc(p.origin)}">'
            f'{label("origin_official" if p.origin == "official" else "origin_mock")}</span>'
            f'<b>{esc(p.test)}</b><span>{label("chars_n", n=n)}</span>'
            f'<span>{label("q_n", n=len(p.items))}</span>'
            f'<a href="{esc(prac)}">{label("practice_these")}</a></div>'
            f'{passage_block(p, mondai_label(m))}'
            f'<details><summary>{label("show_questions")}</summary>{"".join(qs)}</details></article>')
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + mondai_label(m), label("library_page_lead"))
            + f'<main class="dr-wrap">'
            + chips("origin", [("", "f_all"), ("official", "origin_official"), ("mock", "origin_mock")], "f_origin")
            + chips("len", [("", "f_all")] + [(k, k) for _, _, k in LENGTH_BINS], "f_length")
            + f'<p class="dr-note" id="lib-n"></p>{"".join(blocks)}</main>')
    title = f"{level} {_ui(PRIMARY, 'tool_library')} {m['mondai']}"
    cr = crumbs(level, 1, (label("tool_library"), f"../{D.LIBRARY}.html"), (mondai_label(m), None))
    return page(level, title, cr, squeeze(body), LIBRARY_JS, stamp_list(sources), "../../../")


def library_hub(level: str, gp: D.GengoPool, sources: list[Path]) -> str:
    cards = []
    for m in D.gengo_mondai(level):
        if m["section"] != "読解":
            continue
        ps = [p for p in gp.passages.values() if p.code == m["code"]]
        lens = [plain_len(p.text) for p in ps]
        inner = (f'<h3>{mondai_label(m)}</h3>'
                 f'<div class="n">{label("passages_n", n=len(ps))}'
                 + (f' · {label("chars_range", a=min(lens), b=max(lens))}' if lens else "") + '</div>'
                 f'<div class="n">{label("translated_n", n=sum(1 for p in ps if p.translations))}</div>')
        cards.append(f'<a class="dr-card" href="{esc(D.LIBRARY)}/{esc(m["code"])}.html">{inner}</a>'
                     if ps else f'<div class="dr-card off">{inner}</div>')
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + label("tool_library"), label("tool_library_desc"))
            + f'<main class="dr-wrap"><div class="dr-grid">{"".join(cards)}</div></main>')
    title = f"{level} {_ui(PRIMARY, 'tool_library')}"
    return page(level, title, crumbs(level, 0, (label("tool_library"), None)), body, "",
                stamp_list(sources), "../../")


# ----------------------------------------------------------- index
INDEX_JS = r"""
document.addEventListener('DOMContentLoaded', () => {
  const att = S.attempts();
  let n = 0; for (const l of Object.values(att)) n += l.length;
  const p = document.querySelector('[data-tool="進捗"] .js-live'); if (p) p.innerHTML = lbl('attempts_n', {n: n});
});
"""


def index_page(level: str, gp: D.GengoPool, cp: D.ChoukaiPool, sources: list[Path]) -> str:
    stat = {D.PRACTICE: label("items_n", n=len(gp.items)),
            D.LISTENING: label("clips_n", n=len(cp.clips)),
            D.LIBRARY: label("passages_n", n=sum(1 for p in gp.passages.values()
                                                  if next((m for m in D.gengo_mondai(level) if m["code"] == p.code), {}).get("section") == "読解"))}
    cards = "".join(
        f'<a class="dr-card" href="{esc(stem)}.html" data-tool="{esc(stem)}"><h3>{label(lk)}</h3>'
        f'<p>{label(dk)}</p><div class="n">{stat.get(stem, "")}<span class="js-live"></span></div></a>'
        for stem, lk, dk in D.TOOLS)
    body = (lang_ui.header_html(f"JLPT {esc(level)} " + label("module"), label("index_lead"))
            + f'<main class="dr-wrap"><div class="dr-grid">{cards}</div>'
            f'<p class="dr-note">{label("store_note")}</p></main>')
    title = _ui(PRIMARY, "index_title").format(level=level)
    cr = [(lang_ui.pane("portal", "crumb_home"), f"../../{D.INDEX_HTML}"),
          (esc(level), f"../../{level}/{D.INDEX_HTML}"), (label("module"), None)]
    return page(level, title, cr, body, INDEX_JS, stamp_list(sources), "../../")



# ----------------------------------------------------------- build
def expected_pages(level: str, gp: D.GengoPool) -> list[str]:
    """Every page the builder writes for `level`, relative to drill/<LEVEL>/."""
    out = [D.INDEX_HTML] + [f"{t[0]}.html" for t in D.TOOLS]
    have = {i.code for i in gp.items}
    out += [f"{D.PRACTICE}/{m['code']}.html" for m in D.gengo_mondai(level) if m["code"] in have]
    lib = {p.code for p in gp.passages.values()}
    out += [f"{D.LIBRARY}/{m['code']}.html" for m in D.gengo_mondai(level)
            if m["section"] == "読解" and m["code"] in lib]
    return out


def build(level: str) -> list[Path]:
    if not LEVEL.has_structure(level):
        return []
    gp = D.gengo_pool(level)
    cp = D.choukai_pool(level)
    if not gp.items and not cp.clips:
        return []
    out_dir = D.level_dir(level)
    out_dir.mkdir(parents=True, exist_ok=True)
    g_src, c_src = gp.sources, cp.sources + [t / D.CHOUKAI_MD for t in D.level_tests(level)]
    written: dict[str, str] = {}
    by_code: dict[str, list] = {}
    for it in gp.items:
        by_code.setdefault(it.code, []).append(it)
    items = {i.id: i for i in gp.items}
    for m in D.gengo_mondai(level):
        its = by_code.get(m["code"])
        if its:
            written[f"{D.PRACTICE}/{m['code']}.html"] = practice_page(level, m, its, gp.passages, g_src)
        if m["section"] == "読解":
            ps = [p for p in gp.passages.values() if p.code == m["code"]]
            if ps:
                written[f"{D.LIBRARY}/{m['code']}.html"] = library_page(level, m, ps, items, g_src)
    written[f"{D.PRACTICE}.html"] = practice_hub(level, gp, cp, g_src + c_src)
    written[f"{D.LISTENING}.html"] = listening_page(level, cp, c_src)
    written[f"{D.REVIEW}.html"] = review_page(level, gp, cp, g_src + c_src)
    written[f"{D.PROGRESS}.html"] = progress_page(level, gp, cp, g_src + c_src)
    written[f"{D.LIBRARY}.html"] = library_hub(level, gp, g_src)
    written[D.INDEX_HTML] = index_page(level, gp, cp, g_src + c_src)
    assert sorted(written) == sorted(expected_pages(level, gp)), "expected_pages() drifted from build()"
    # Build output only: drop any page this build did not write (a 大問 whose pool emptied).
    for old in out_dir.rglob("*.html"):
        if old.relative_to(out_dir).as_posix() not in written:
            old.unlink()
    paths = []
    for rel, markup in written.items():
        p = out_dir / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(markup, encoding="utf-8")
        paths.append(p)
    return paths


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--level", default=LEVEL.DEFAULT_LEVEL)
    args = ap.parse_args()
    outs = build(args.level)
    if not outs:
        print(f"{args.level}: no tests with 詳細解説 and no playable clips — nothing to build")
        return 0
    gp, cp = D.gengo_pool(args.level), D.choukai_pool(args.level)
    for p in outs:
        size = p.stat().st_size
        print(f"  wrote {p.relative_to(ROOT)}  ({size / 1e6:.2f} MB)"
              + ("  ! over the split limit" if size > SPLIT_LIMIT else ""))
    print(f"  pool: {len(gp.items)} 言語知識・読解 items ({len(gp.skipped)} skipped), "
          f"{len(gp.passages)} passages, {len(cp.clips)} playable clips "
          f"({sum(len(c.questions) for c in cp.clips)} questions), {len(cp.unplayable)} bank clips unplayable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
