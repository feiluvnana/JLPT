"""The exam list — `/<LEVEL>/exam/`, ONE implementation for both deployments.

The list exists twice over: `serve_sheet.py` serves it from disk (`make serve`),
and `build_pages.py` bakes it into a static `<LEVEL>/exam/index.html` for GitHub
Pages, where progress lives in localStorage instead. Rendering it twice in two
languages is exactly how "the same" screen drifts, so the markup lives here
once, in JS, and both deployments feed it the SAME array of test objects:

    {id, origin, level, answered, total, has_sheet, has_audio,
     result: {passed, total_scaled_score, max_scaled_score, graded_at} | null}

`serve_sheet.py` produces that array in Python (`progress_of()`) and hands it
over `GET /api/tests?level=`; the Pages build bakes a manifest of the static half
(`id/origin/level/has_sheet/has_audio`) and the page fills in the progress half
from localStorage. Only the *source* differs — the cards, the CSS and the actions
are this file.

The level is chosen upstream, on the portal's level chooser (portal_view.py);
this page shows one level and a breadcrumb back to that level's module chooser.
It renders through `portal_view.page()`, so header, breadcrumb and language
switch are the portal's own, and its labels are the portal namespace's `list_*`
strings (langs.py) — both languages in the markup, `body[data-lang]` picks one.

The cards hang under two collapsible `<details>` groups keyed on `origin`
(imported past papers vs generated mocks), both shut on load, plus a search box
that filters on id/origin and force-opens whichever group holds a hit.

Every link out of the page is relative (`../../tests/<id>/解答.html`): the page
sits two folders below the site root in both deployments.

Keep it dependency-free (see app_style.py): `make serve` must start without the
authoring dependencies installed.
"""

import json
import sys
from pathlib import Path

# These scripts are run by path (`python3 .agents/…/index_view.py`) from the repo
# root, not as a package, so the sibling modules are only importable once their
# directory is on the path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import local_store    # noqa: E402
import portal_view    # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "jlpt-exam-structure" / "scripts"))
import level as LEVEL  # noqa: E402

# A generated N2 paper's item count (71 言語知識・読解 + 30 聴解), from the level
# table — only the fallback denominator; every row carries its own `total`.
QUESTION_COUNT = LEVEL.total_items()

SHEET = "解答.html"

INDEX_CSS = """
/* Header, breadcrumb, <main> and .lede are portal_view.PORTAL_CSS — the list
   renders through portal_view.page() like every portal screen. */
/* Equal card height. Meter uses display:contents so the track shares a row with
   the status chip (left-aligned); the lbl sits on the row under the track —
   flex + align-items:center was optically centering the whole meter block and
   made the bar look offset from the chip. */
.card{display:grid;grid-template-columns:16em auto minmax(9em,1fr) auto auto;
  grid-template-rows:1fr auto;column-gap:1em;row-gap:.2em;align-items:center;
  background:#fff;border:1px solid #e2e8f0;border-radius:10px;padding:.65em 1.2em;
  margin-bottom:1em;box-sizing:border-box;height:5.4em;min-height:5.4em;
  max-height:5.4em;overflow:hidden;
  box-shadow:0 1px 3px rgba(0,0,0,0.03);
  transition:all .18s ease}
.card:hover{border-color:#cbd5e1;box-shadow:0 4px 14px rgba(0,0,0,0.06)}
.card h2{grid-column:1;grid-row:1/-1;margin:0;font-size:13pt;font-weight:800;min-width:0;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;align-self:center;color:#0f172a}
.card .origin{grid-column:2;grid-row:1/-1;align-self:center}
.card .meter{display:contents}
.card .meter .track{grid-column:3;grid-row:1;align-self:center;width:100%;min-width:0}
.card .meter .lbl{grid-column:3;grid-row:2;text-align:left;margin:0;line-height:1.2;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:9.5pt}
.card .status{grid-column:4;grid-row:1/-1;align-self:center}
.acts{grid-column:5;grid-row:1/-1;display:flex;flex-wrap:nowrap;gap:.5em;
  align-self:center}
.acts .ui-btn{padding:.4em .85em;font-size:10pt;white-space:nowrap}
.empty{background:#fff;border:1px dashed var(--line);border-radius:10px;padding:3em 2em;
  text-align:center;color:var(--muted)}
code{background:#f1f5f9;padding:.15em .45em;border-radius:4px;font-size:9.5pt;border:1px solid #e2e8f0}
.badge.origin-imp{background:#e0f2fe;color:#0369a1;border:1px solid #bae6fd}
.badge.origin-gen{background:#f1f5f9;color:#475569;border:1px solid #e2e8f0}
/* Pages-only: localStorage is the only copy of your answers, so the list owns
   the way to get them off this browser and back onto another one. */
.tools{display:flex;flex-wrap:wrap;gap:.6em;align-items:center;margin:0 0 1.6em}
.tools .note{font-size:9.5pt;color:var(--muted)}
.tools input[type=file]{display:none}
/* Search box + the two origin groups. A group is a <details>: shut until it is
   clicked, so the list opens as two lines instead of twenty cards. A live query
   force-opens whichever group holds a hit — a match hidden inside a collapsed
   group reads as "no results". */
.searchbar{display:flex;flex-wrap:wrap;gap:.6em;align-items:center;margin:0 0 1.3em}
.searchbar input{flex:1 1 18em;min-width:0;font-family:var(--ui);font-size:11pt;
  padding:.6em .9em;border:1px solid #cbd5e1;border-radius:8px;background:#fff;
  color:var(--ink);box-shadow:0 1px 3px rgba(0,0,0,0.03)}
.searchbar input:focus{outline:none;border-color:var(--accent);
  box-shadow:0 0 0 3px rgba(37,99,235,.15)}
.searchbar .hits{font-size:9.5pt;color:var(--muted);white-space:nowrap;
  font-variant-numeric:tabular-nums}
.group{background:#fff;border:1px solid #e2e8f0;border-radius:10px;margin-bottom:1em;
  box-shadow:0 1px 3px rgba(0,0,0,0.03);overflow:hidden}
.group>summary{display:flex;align-items:center;gap:.75em;cursor:pointer;
  padding:.9em 1.2em;font-size:12pt;font-weight:800;color:#0f172a;
  list-style:none;-webkit-user-select:none;user-select:none}
.group>summary::-webkit-details-marker{display:none}
.group>summary::before{content:"▶";flex:0 0 auto;font-size:8.5pt;color:var(--muted);
  transition:transform .15s ease}
.group[open]>summary::before{transform:rotate(90deg)}
.group>summary:hover{background:#f8fafc}
.group .g-count{font-size:9.5pt;font-weight:700;color:#475569;background:#f1f5f9;
  border:1px solid #e2e8f0;border-radius:9999px;padding:.15em .7em;
  font-variant-numeric:tabular-nums}
.group .g-sub{margin-left:auto;font-size:9.5pt;font-weight:500;color:var(--muted);
  font-variant-numeric:tabular-nums}
.group .g-body{padding:.9em 1.2em 1.1em;border-top:1px solid #f1f5f9}
.group .g-body .card{margin-bottom:.8em}
.group .g-body .card:last-child{margin-bottom:0}
.group .g-empty{padding:.4em .2em;color:var(--muted);font-size:10pt}
@media screen and (max-width: 54em){
  .card{grid-template-columns:1fr auto;grid-template-rows:auto auto auto auto auto;
    column-gap:.8em;row-gap:.45em;height:auto;min-height:auto;max-height:none;
    padding:1em 1.1em;overflow:visible}
  .card h2{grid-column:1;grid-row:1;font-size:12.5pt;white-space:normal;overflow:visible}
  .card .origin{grid-column:2;grid-row:1;justify-self:end}
  .card .status{grid-column:1 / -1;grid-row:2;justify-self:start}
  .card .meter .track{grid-column:1 / -1;grid-row:3}
  .card .meter .lbl{grid-column:1 / -1;grid-row:4}
  .acts{grid-column:1 / -1;grid-row:5;justify-self:start;flex-wrap:wrap;
    margin-top:.4em;width:100%}
  .acts .ui-btn{padding:.45em .9em;font-size:10pt;min-height:38px}
  .tools{gap:.7em}
  .tools .ui-btn{width:100%;justify-content:center}
  .searchbar .ui-btn{min-height:38px}
  .group>summary{padding:.85em .95em;font-size:11.5pt;flex-wrap:wrap}
  .group .g-sub{margin-left:0;width:100%}
  .group .g-body{padding:.8em .95em 1em}
}
"""


# --------------------------------------------------------------- the shared view
# Labels come from the language registry (portal namespace, `list_*` keys):
# T() returns one `.lang-pane` per language for markup, so switching language is
# CSS alone; T1() is the current language, for what cannot hold markup
# (title=, confirm(), alert()).
INDEX_JS = """
var MODE = window.LIST_MODE || 'server';
var LEVEL = %(level)s;
var TOTAL = %(total)d, SHEET = %(sheet)s;
var STR = %(strings)s, STR_ORDER = %(order)s;

function esc(s){
  return String(s).replace(/[&<>"']/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
  });
}
function fill(s, vars){
  return String(s).replace(/\\{(\\w+)\\}/g, function(m, k){
    return vars && vars[k] !== undefined ? vars[k] : m;
  });
}
function str(lang, key){
  var t = STR[lang] || {};
  return t[key] !== undefined ? t[key] : (STR[STR_ORDER[0]] || {})[key] || key;
}
function T(key, vars){           // markup: one pane per language (vars are escaped)
  var ev = {};
  for (var k in (vars || {})) ev[k] = esc(vars[k]);
  if (STR_ORDER.length < 2) return fill(str(STR_ORDER[0], key), ev);
  return STR_ORDER.map(function(c){
    return '<span class="lang-pane" data-lang="' + c + '">' + fill(str(c, key), ev) + '</span>';
  }).join('');
}
function T1(key, vars){          // plain text in the language on screen now
  var lang = document.body.dataset.lang || STR_ORDER[0];
  return fill(str(lang, key), vars);
}

/* -------------------------------------------------------------- the two sources
   Server: the same disk read screen 1 always did, over GET /api/tests.
   Local:  the baked manifest of what was deployed + this browser's localStorage.
   Both return the SAME array shape, so everything below is source-agnostic. */
function countAnswered(saved){
  if (!saved || typeof saved !== 'object') return 0;
  var n = 0;
  ['言語知識_読解', '聴解'].forEach(function(half){
    var o = saved[half] || {};
    for (var k in o){ if (o[k] !== null && o[k] !== undefined) n++; }
  });
  return n;
}

function localTests(){
  // Mirrors serve_sheet.progress_of(): same fields, read out of localStorage.
  return (window.PAGES_TESTS || []).map(function(t){
    var res = window.JLPTStore.result(t.id), summary = res && res.summary;
    return {
      id: t.id, origin: t.origin, level: t.level, total: t.total || TOTAL,
      has_sheet: t.has_sheet, has_audio: t.has_audio,
      has_explanation: t.has_explanation,
      answered: countAnswered(window.JLPTStore.answers(t.id)),
      result: summary ? {
        passed: !!summary.passed,
        total_scaled_score: summary.total_scaled_score,
        max_scaled_score: summary.max_scaled_score === undefined ? 180
                          : summary.max_scaled_score,
        graded_at: res.graded_at
      } : null
    };
  });
}

// The page is /<LEVEL>/exam/, two folders below the site root, in BOTH
// deployments — every link out of it is relative, so Pages' /<repo>/ subpath
// and a server root resolve the same way.
var ROOT_REL = '../../';

async function loadTests(){
  if (MODE === 'local') return localTests();
  var r = await fetch(ROOT_REL + 'api/tests?level=' + encodeURIComponent(LEVEL),
                      {cache: 'no-store'});   // never a stale list
  return (await r.json()).tests || [];
}

function sheetHref(id){
  return ROOT_REL + 'tests/' + encodeURIComponent(id) + '/' + encodeURIComponent(SHEET);
}

function explanationHref(id){
  return ROOT_REL + 'tests/' + encodeURIComponent(id) + '/模範解答.html';
}

/* ------------------------------------------------------------------- the cards */
function meterHtml(t){
  var ratio = !t.total ? 0 : Math.min(100, Math.round(t.answered / t.total * 100));
  var fill = t.answered >= t.total ? 'fill done' : 'fill';
  return '<div class="meter"><div class="track">'
       + '<div class="' + fill + '" style="width:' + ratio + '%%"></div></div>'
       + '<div class="lbl">' + T('list_answered', {a: t.answered, t: t.total, p: ratio})
       + '</div></div>';
}

function originBadgeHtml(t){
  var lv = t.level ? esc(t.level) + ' · ' : '';   // a restored backup is user data
  return t.origin === 'imported'
    ? '<span class="badge origin-imp">' + lv + 'imported</span>'
    : '<span class="badge origin-gen">' + lv + 'generated</span>';
}

function badgeHtml(t){
  if (!t.has_sheet) return '<span class="badge warn">' + T('list_no_sheet') + '</span>';
  if (!t.result) return '<span class="badge none">' + T('list_ungraded') + '</span>';
  var cls = t.result.passed ? 'pass' : 'fail';
  var label = T(t.result.passed ? 'list_pass' : 'list_fail');
  return '<span class="badge ' + cls + '">' + label + '&nbsp;'
       + esc(t.result.total_scaled_score) + ' / ' + esc(t.result.max_scaled_score) + '</span>';
}

function cardHtml(t){
  var id = esc(t.id), base = sheetHref(t.id), expHref = explanationHref(t.id), acts = [];
  if (!t.has_sheet){
    acts.push('<a class="ui-btn" href="#" onclick="return false" '
            + 'title="' + esc(T1('list_run_sheet', {id: t.id})) + '">' + T('list_take') + '</a>');
  } else if (t.result){
    // Already graded: the result view is the default destination, but the exam
    // is one click away and keeps the saved answers, so it can be redone.
    acts.push('<a class="ui-btn primary" href="' + base + '?screen=result">'
            + T('list_view_result') + '</a>');
    acts.push('<a class="ui-btn" href="' + base + '">' + T('list_retry') + '</a>');
  } else {
    acts.push('<a class="ui-btn primary" href="' + base + '">'
            + T(t.answered ? 'list_resume' : 'list_take') + '</a>');
  }
  if (t.has_explanation){
    acts.push('<a class="ui-btn" href="' + expHref + '">' + T('list_explanation') + '</a>');
  }
  // Clear progress whenever either store holds something — graded or mid-exam.
  if (t.result || t.answered){
    acts.push('<button type="button" class="ui-btn danger" data-clear="' + id
            + '">' + T('list_clear') + '</button>');
  }
  return '<div class="card"><h2 title="' + id + '">' + T('list_test', {id: t.id}) + '</h2>'
       + '<span class="origin">' + originBadgeHtml(t) + '</span>'
       + meterHtml(t)
       + '<span class="status">' + badgeHtml(t) + '</span>'
       + '<div class="acts">' + acts.join('') + '</div></div>';
}

/* ------------------------------------------------------- groups and search
   Origin already decides the badge, so it decides the grouping too — the two
   halves of tests/ (imported past papers, generated mocks) are what a reader
   actually picks between. Each group is a <details>, shut on load: twenty cards
   opened flat is a scroll, two summary lines is a choice. The level is chosen
   upstream (the portal's level chooser), so this list only ever holds one. */
var GROUPS = [
  {key: 'imported',  label: 'list_group_imported',
   test: function(t){ return t.origin === 'imported'; }},
  {key: 'generated', label: 'list_group_generated',
   test: function(t){ return t.origin !== 'imported'; }}
];
var TESTS = [];            // last rendered list, kept by render() itself
var QUERY = '';
/* Open/shut has to survive a re-render: refreshList() runs on every pageshow,
   so a group must not snap shut on the way back from a graded exam. Only a real
   click writes here — innerHTML builds an already-open <details>, which fires
   no toggle event. */
var OPEN = {imported: false, generated: false};

function matchesLevel(t){ return (t.level || 'N2') === LEVEL; }

function matchesQuery(t){
  if (!QUERY) return true;
  var hay = (t.id + ' ' + (t.origin || '') + ' ' + (t.level || '')).toLowerCase();
  return QUERY.split(/\\s+/).every(function(w){ return !w || hay.indexOf(w) >= 0; });
}

function groupHtml(g, tests){
  var graded = tests.filter(function(t){ return t.result; }).length;
  // A live query force-opens the groups holding its hits — a match left inside
  // a collapsed group reads as "nothing found".
  var open = ((QUERY && tests.length) || OPEN[g.key]) ? ' open' : '';
  var body = tests.length
    ? tests.map(cardHtml).join('')
    : '<div class="g-empty">' + T('list_g_empty') + '</div>';
  return '<details class="group" data-group="' + g.key + '"' + open + '>'
       + '<summary><span class="g-name">' + T(g.label) + '</span>'
       + '<span class="g-count">' + T('list_g_count', {n: tests.length}) + '</span>'
       + '<span class="g-sub">' + T('list_g_graded', {n: graded}) + '</span></summary>'
       + '<div class="g-body">' + body + '</div></details>';
}

function render(tests){
  tests = tests.filter(matchesLevel);
  TESTS = tests;     // the search re-renders from here — one assignment, one place
  var shown = tests.filter(matchesQuery);
  var body = tests.length
    ? GROUPS.map(function(g){ return groupHtml(g, shown.filter(g.test)); }).join('')
    : '<div class="empty">' + T('list_empty')
      + (MODE === 'local' ? '' : '<br><code>make sheet &lt;test_id&gt;</code>') + '</div>';
  document.getElementById('cards').innerHTML = body;
  var graded = tests.filter(function(t){ return t.result; }).length;
  document.getElementById('counts').innerHTML =
    T('list_counts', {n: tests.length, g: graded});
  var hits = document.getElementById('hits');
  if (hits) hits.innerHTML = QUERY ? T('list_hits', {n: shown.length}) : '';
}

function setQuery(v){
  QUERY = String(v || '').trim().toLowerCase();
  render(TESTS);
}

async function refreshList(){
  try { render(await loadTests()); }
  catch (e){
    document.getElementById('cards').innerHTML =
      '<div class="empty">' + T('list_load_fail', {e: String(e)}) + '</div>';
  }
}

/* ------------------------------------------------------------------- actions */
async function clearTestProgress(id){
  if (!confirm(T1('list_confirm_clear', {id: id}))) return;
  if (MODE === 'local'){
    window.JLPTStore.clear(id);
    return refreshList();
  }
  try {
    var r = await fetch(ROOT_REL + 'api/tests/' + encodeURIComponent(id) + '/clear', {
      method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'
    });
    var data = await r.json();
    if (!r.ok || !data.success){
      alert((data && data.error) || T1('list_clear_failed'));
      return;
    }
    refreshList();
  } catch (e){
    alert(T1('list_clear_failed') + ' ' + e);
  }
}

/* Pages has no disk, so the list is where answers leave and re-enter the
   browser: one JSON holding every test's 解答 and 採点結果 — every test this
   browser holds, whatever its level, so one backup still restores everything. */
function exportAll(){
  var out = {};
  (window.PAGES_TESTS || []).map(function(t){ return t.id; })
    .concat(window.JLPTStore.ids())
    .forEach(function(id){
      if (out[id]) return;
      var a = window.JLPTStore.answers(id), r = window.JLPTStore.result(id);
      if (a || r) out[id] = {"ユーザー解答.json": a, "採点結果.json": r};
    });
  if (!Object.keys(out).length){ alert(T1('list_nothing_saved')); return; }
  var a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([JSON.stringify(out, null, 2)],
                                        {type: 'application/json'}));
  a.download = 'jlpt-解答バックアップ.json';
  a.click();
}

function importAll(input){
  var f = input.files && input.files[0];
  if (!f) return;
  var reader = new FileReader();
  reader.onload = function(){
    var data;
    try { data = JSON.parse(reader.result); }
    catch (e){ alert(T1('list_json_fail', {e: String(e)})); return; }
    var n = 0;
    for (var id in data){
      var rec = data[id] || {};
      if (rec['ユーザー解答.json']) window.JLPTStore.setAnswers(id, rec['ユーザー解答.json']);
      if (rec['採点結果.json']) window.JLPTStore.setResult(id, rec['採点結果.json']);
      n++;
    }
    input.value = '';
    alert(T1('list_imported_n', {n: n}));
    refreshList();
  };
  reader.readAsText(f);
}

document.addEventListener('click', function(ev){
  var el = ev.target;
  if (!el || !el.closest) return;
  var btn = el.closest('[data-clear]');
  if (btn){ clearTestProgress(btn.getAttribute('data-clear')); return; }
  if (el.closest('#q-clear')){
    var box = document.getElementById('q');
    if (box){ box.value = ''; box.focus(); }
    setQuery('');
  }
});
document.addEventListener('input', function(ev){
  if (ev.target && ev.target.id === 'q') setQuery(ev.target.value);
});
// `toggle` does not bubble — capture it, and record only what the user clicked.
document.addEventListener('toggle', function(ev){
  var d = ev.target;
  if (d && d.classList && d.classList.contains('group')){
    OPEN[d.getAttribute('data-group')] = d.open;
  }
}, true);
// The list must be live: coming back from a graded exam has to show the score.
window.addEventListener('pageshow', refreshList);
"""


def index_js(level: str) -> str:
    return INDEX_JS % {"total": QUESTION_COUNT,
                       "sheet": json.dumps(SHEET, ensure_ascii=False),
                       "level": json.dumps(level),
                       "strings": portal_view.js_strings("list_"),
                       "order": json.dumps(portal_view.langs.order())}


P = portal_view.pane


def _lede(local: bool) -> str:
    return (f'<p class="lede">{P("list_lede_local" if local else "list_lede_server")}'
            f'<br>{P("list_group_note")}</p>')


def _searchbar() -> str:
    # Static shell, outside #cards: re-rendering the list must not blow away the
    # box the user is typing in (or its focus and caret).
    return ('<div class="searchbar">'
            '<input id="q" type="search" autocomplete="off" spellcheck="false" '
            f'{portal_view.i18n_attrs("aria-label", "list_search_label")} '
            f'{portal_view.i18n_attrs("placeholder", "list_search_placeholder")}>'
            f'<button type="button" class="ui-btn" id="q-clear">{P("list_search_clear")}</button>'
            '<span class="hits" id="hits"></span>'
            '</div>')


def _tools_local() -> str:
    return ('<div class="tools">'
            f'<button type="button" class="ui-btn" onclick="exportAll()">{P("list_backup_save")}</button>'
            f'<label class="ui-btn">{P("list_backup_load")}'
            '<input type="file" accept="application/json,.json" '
            'onchange="importAll(this)"></label>'
            f'<span class="note">{P("list_backup_note")}</span>'
            '</div>')


def index_html(mode: str = "server", tests: list | None = None,
               level: str = LEVEL.DEFAULT_LEVEL) -> str:
    """The exam list of ONE level, `/<LEVEL>/exam/` in either deployment.

    ``mode='server'``: an empty shell that fetches ``/api/tests?level=`` — the
    disk stays the source of truth and the list is never cached.
    ``mode='local'``: the same shell plus a baked manifest (this level's tests),
    filled in from localStorage by the same JS.
    """
    if mode not in ("server", "local"):
        raise ValueError(f"unknown list mode: {mode}")
    level = LEVEL.normalize(level)
    local = mode == "local"
    mine = [t for t in (tests or []) if (t.get("level") or LEVEL.DEFAULT_LEVEL) == level]
    boot = (f'<script>{local_store.LOCAL_STORE_JS}\n'
            f'window.PAGES_TESTS = {json.dumps(mine, ensure_ascii=False)};</script>'
            if local else '')
    body = (f'{_lede(local)}{_tools_local() if local else ""}{_searchbar()}'
            '<div id="cards"></div>')
    return portal_view.page(
        title_key="doc_title_exam", title_kw={"level": level},
        h1=P("exam_title", level=level), subtitle=P("exam_subtitle"),
        crumbs=[(P("crumb_home"), f"../../{portal_view.INDEX}"),
                (level, f"../{portal_view.INDEX}"), (P("crumb_exam"), None)],
        body=body, extra_css=INDEX_CSS,
        head_js=f'<script>window.LIST_MODE = "{mode}";</script>{boot}',
        right=f'<span class="sub" id="counts">{P("list_loading")}</span>',
        tail_js=index_js(level) + "\nrefreshList();")
