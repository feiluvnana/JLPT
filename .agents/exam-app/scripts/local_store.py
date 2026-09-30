"""The browser-side store — ONE implementation of "the disk, in localStorage".

`make serve` writes answers and results to `tests/<id>/ユーザー解答.json` and
`tests/<id>/採点結果.json`. A GitHub Pages deployment is static: there is no
server to POST to and no disk to write. This module holds the localStorage
backend that stands in for that disk, and it is the SINGLE copy of it — both
the exam sheet (screens 2–3, `build_interactive.py`) and the test list
(screen 1, `build_pages.py` via `index_view.py`) include this same snippet.

**One store per build, never two.** `exam-app/SKILL.md` forbids
a second copy of the answers, because the list and the sheet would then disagree
about what you answered. That rule is unchanged: the storage backend is chosen
at BUILD time (`build_interactive.py --storage server|local`), so a server build
touches only the JSON files on disk and a Pages build touches only localStorage.
Nothing sniffs at runtime and nothing writes to both.

The localStorage keys deliberately spell out the on-disk paths they replace —
`jlpt-mock/v1/<test_id>/ユーザー解答.json` — so what a key holds, and which file
it corresponds to when you export it, is readable in devtools.

Keep this module dependency-free: `make serve` must start without the authoring
dependencies installed.
"""

# Bump the version segment only if the stored SHAPE changes; the values are the
# same documents grade_answers.py reads, so a shape change means a grader change.
STORAGE_PREFIX = "jlpt-mock/v1"
ANSWERS_JSON = "ユーザー解答.json"
RESULT_JSON = "採点結果.json"

# `window.JLPTStore` — the localStorage half of the two storage backends.
# Pure data access: no DOM, no fetch, no rendering. Safe to include on any page.
LOCAL_STORE_JS = """
window.JLPTStore = (function(){
  var PREFIX = "%(prefix)s", ANSWERS = "%(answers)s", RESULT = "%(result)s";
  function key(id, name){ return PREFIX + '/' + id + '/' + name; }
  function read(id, name){
    try {
      var raw = localStorage.getItem(key(id, name));
      return raw ? JSON.parse(raw) : null;
    } catch (e){ return null; }          // private mode, quota, corrupt JSON
  }
  function write(id, name, obj){
    try { localStorage.setItem(key(id, name), JSON.stringify(obj)); return true; }
    catch (e){ return false; }           // quota exceeded → caller falls back
  }
  function remove(id, name){
    try { localStorage.removeItem(key(id, name)); } catch (e){}
  }
  return {
    PREFIX: PREFIX, ANSWERS: ANSWERS, RESULT: RESULT,
    key: key, read: read, write: write, remove: remove,
    answers: function(id){ return read(id, ANSWERS); },
    setAnswers: function(id, o){ return write(id, ANSWERS, o); },
    result: function(id){ return read(id, RESULT); },
    setResult: function(id, o){ return write(id, RESULT, o); },
    clear: function(id){ remove(id, ANSWERS); remove(id, RESULT); },
    // Which test ids this browser actually holds data for — the Pages test
    // list uses it so a test whose folder was renamed still shows its progress.
    ids: function(){
      var out = [];
      try {
        for (var i = 0; i < localStorage.length; i++){
          var k = localStorage.key(i);
          if (k && k.indexOf(PREFIX + '/') === 0){
            var id = k.slice(PREFIX.length + 1).split('/')[0];
            if (id && out.indexOf(id) < 0) out.push(id);
          }
        }
      } catch (e){}
      return out;
    }
  };
})();
""" % {"prefix": STORAGE_PREFIX, "answers": ANSWERS_JSON, "result": RESULT_JSON}


# `window.JLPTKnowledgeStore` — the knowledge module's per-browser progress
# (jlpt-knowledge/SKILL.md §Progress). Same rule as JLPTStore: this is the ONLY
# place its keys are spelled. It lives under its OWN prefix, not under
# STORAGE_PREFIX, so `JLPTStore.ids()` — which lists every `jlpt-mock/v1/<id>/`
# as a test — can never mistake a knowledge category for a paper. The keys again
# read like the files they would be:
#
#   jlpt-knowledge/v1/<LEVEL>/<category>/覚えた.json      {"<entry id>": 1, ...}
#   jlpt-knowledge/v1/<LEVEL>/<category>/クイズ履歴.json  {"<entry id>#<n>": {"n": tries,
#                                                      "ok": correct, "last": 0|1}}
#   jlpt-knowledge/v1/設定.json                           {"rate": 1 | 0.7}  (読み上げの速さ)
#
# `<n>` is the quiz item's 1-based index inside its entry, so the history of an
# entry's first question survives the entries around it being reordered.
KNOWLEDGE_PREFIX = "jlpt-knowledge/v1"
KNOWLEDGE_LEARNED_JSON = "覚えた.json"
KNOWLEDGE_HISTORY_JSON = "クイズ履歴.json"
KNOWLEDGE_PREFS_JSON = "設定.json"

KNOWLEDGE_STORE_JS = """
window.JLPTKnowledgeStore = (function(){
  var PREFIX = "%(prefix)s", LEARNED = "%(learned)s", HISTORY = "%(history)s", PREFS = "%(prefs)s";
  function key(level, cat, name){ return PREFIX + '/' + level + '/' + cat + '/' + name; }
  function read(level, cat, name){
    try {
      var raw = localStorage.getItem(key(level, cat, name));
      var o = raw ? JSON.parse(raw) : null;
      return (o && typeof o === 'object') ? o : {};
    } catch (e){ return {}; }
  }
  function write(level, cat, name, obj){
    try { localStorage.setItem(key(level, cat, name), JSON.stringify(obj)); return true; }
    catch (e){ return false; }
  }
  return {
    PREFIX: PREFIX, key: key,
    learned: function(level, cat){ return read(level, cat, LEARNED); },
    setLearned: function(level, cat, id, on){
      var o = read(level, cat, LEARNED);
      if (on) o[id] = 1; else delete o[id];
      write(level, cat, LEARNED, o);
      return o;
    },
    history: function(level, cat){ return read(level, cat, HISTORY); },
    // Level-independent preferences (the speech rate) — one key for the module.
    prefs: function(){
      try { var o = JSON.parse(localStorage.getItem(PREFIX + '/' + PREFS) || 'null');
            return (o && typeof o === 'object') ? o : {}; } catch (e){ return {}; }
    },
    setPrefs: function(o){
      try { localStorage.setItem(PREFIX + '/' + PREFS, JSON.stringify(o)); } catch (e){}
    },
    record: function(level, cat, qid, ok){
      var o = read(level, cat, HISTORY);
      var h = o[qid] || {n: 0, ok: 0, last: 0};
      h.n += 1; if (ok) h.ok += 1; h.last = ok ? 1 : 0;
      o[qid] = h;
      write(level, cat, HISTORY, o);
      return h;
    }
  };
})();
""" % {"prefix": KNOWLEDGE_PREFIX, "learned": KNOWLEDGE_LEARNED_JSON, "history": KNOWLEDGE_HISTORY_JSON,
       "prefs": KNOWLEDGE_PREFS_JSON}
