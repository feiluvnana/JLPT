"""The learner-language registry — the ONE place a language code is listed.

Every page that prints prose for a learner (模範解答.html, 練習.html's reveals,
the knowledge module, the portal chrome) and every gate check that measures that
prose reads its languages from here, never from a literal ``["ja", "vi"]``.
Adding a third language, or replacing Vietnamese, is a data change:

    references/languages/index.json        {"primary": "ja", "order": [...]}
    references/languages/<code>/meta.json  code, name, html_lang, length_factor
    references/languages/<code>/<ns>.json  UI strings, one file per page family
                                           (model_answer, practice, portal, knowledge,
                                           exam — 解答.html's chrome, drill)

plus that language's content files (``詳細解説.<code>.json``,
``knowledge/<LEVEL>/<category>.<code>.json``). Until they exist the pages fall back
the way a paper without ``詳細解説.vi.json`` always has, and the gate WARNs.

`primary` is the exam's own language (Japanese). It is special in exactly one
way: it owns the exam wording. Where a skill stores prose for the primary
language in an unsuffixed file (``詳細解説.json``) that is that skill's
convention, reached through `content_path()`, not a rule of this module.

Dependency-free on purpose (json + pathlib): `make serve` imports it.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

LANG_DIR = Path(__file__).resolve().parents[1] / "references" / "languages"

# The UI namespaces a language folder must carry — one per page family. A
# namespace a language lacks is a FAIL in the gate (check_language_registry),
# because the page would print the primary language's label in its place.
NAMESPACES = ("model_answer", "practice", "portal", "knowledge", "exam", "drill")


@lru_cache(maxsize=None)
def _index() -> dict:
    return json.loads((LANG_DIR / "index.json").read_text(encoding="utf-8"))


def primary() -> str:
    """The exam language (ja). Owns the exam wording; always first in order()."""
    return _index()["primary"]


def order() -> list[str]:
    """Active languages, in segmented-control order. primary() is first."""
    o = list(_index()["order"])
    p = primary()
    return [p] + [c for c in o if c != p]


def learners() -> list[str]:
    """Active languages other than the primary one — the ones that translate
    passages/examples and carry the 'written, not translated' prose rule."""
    return [c for c in order() if c != primary()]


@lru_cache(maxsize=None)
def meta(code: str) -> dict:
    return json.loads((LANG_DIR / code / "meta.json").read_text(encoding="utf-8"))


def name(code: str) -> str:
    return meta(code)["name"]


def html_lang(code: str) -> str:
    return meta(code).get("html_lang", code)


def length_factor(code: str) -> float:
    """How much longer this language runs than Japanese for the same content —
    the multiplier every per-language length band is derived with."""
    return float(meta(code).get("length_factor", 1.0))


def required(code: str) -> bool:
    """Is this language's CONTENT mandatory yet? (meta.json `"required": true`)

    The primary language always is. A learner language is required once its
    content exists across the fleet — then a missing or partial content file is
    a FAIL. A language just added to `order` starts un-required (leave the key
    out), so every page falls back and the gate WARNs instead of failing every
    paper on disk; flip it to true when the content is through. Also decides
    whether a hand-declared 聴解 bank item MUST carry `explanation_<code>`.
    """
    return code == primary() or bool(meta(code).get("required", False))


def content_field(code: str, base: str = "explanation") -> str:
    """The per-language field name in a record that carries every language's
    prose side by side (the 聴解 clip bank): primary -> `explanation`,
    others -> `explanation_<code>`."""
    return base if code == primary() else f"{base}_{code}"


@lru_cache(maxsize=None)
def ui(code: str, namespace: str) -> dict:
    """UI strings for one page family. Missing file -> {} (the gate FAILs it)."""
    p = LANG_DIR / code / f"{namespace}.json"
    if not p.is_file():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def ui_table(namespace: str, codes: list[str] | None = None) -> dict:
    """{code: strings} for every active language — the shape the builders'
    old literal `UI = {"ja": {...}, "vi": {...}}` dicts had."""
    return {c: ui(c, namespace) for c in (codes or order())}


def content_path(base: Path, code: str, primary_unsuffixed: bool = True) -> Path:
    """`詳細解説.json` + 'vi' -> `詳細解説.vi.json`.

    With ``primary_unsuffixed`` (the 詳細解説 convention) the primary language
    is the base path itself; without it (the knowledge convention, where the
    unsuffixed file is the shared Japanese material) every language, primary
    included, gets its code.
    """
    if primary_unsuffixed and code == primary():
        return base
    return base.with_name(f"{base.stem}.{code}{base.suffix}")


def pane_css(root: str = "body", attr: str = "data-lang",
             pane: str = ".lang-pane") -> str:
    """CSS that shows only the active language's panes, for every active code.

    Replaces hand-written pairs like
    ``body[data-lang="ja"] .lang-pane[data-lang="vi"]{display:none}`` — which
    needed one line per ordered pair and a new line for every language added.
    """
    return "\n".join(
        f'{root}[{attr}="{c}"] {pane}:not([{attr}="{c}"]) {{ display: none !important; }}'
        for c in order())


def check() -> list[str]:
    """Registry problems, as sentences (empty = sound). The gate prints them."""
    out = []
    idx = _index()
    if idx.get("primary") not in idx.get("order", []):
        out.append(f"index.json: primary {idx.get('primary')!r} is not in order")
    if len(set(idx.get("order", []))) != len(idx.get("order", [])):
        out.append("index.json: order lists a language twice")
    for c in idx.get("order", []):
        if not (LANG_DIR / c / "meta.json").is_file():
            out.append(f"{c}: no meta.json")
            continue
        m = meta(c)
        for k in ("code", "name", "html_lang", "length_factor"):
            if k not in m:
                out.append(f"{c}/meta.json: missing {k!r}")
        if m.get("code") != c:
            out.append(f"{c}/meta.json: code {m.get('code')!r} != folder name")
    p = idx.get("primary")
    for ns in NAMESPACES:
        want = set(ui(p, ns))
        if not want:
            out.append(f"{p}/{ns}.json: missing or empty (the primary language defines the keys)")
            continue
        for c in idx.get("order", []):
            if c == p:
                continue
            have = set(ui(c, ns))
            if want - have:
                out.append(f"{c}/{ns}.json: missing {sorted(want - have)}")
            if have - want:
                out.append(f"{c}/{ns}.json: keys the primary does not define {sorted(have - want)}")
            # A value may itself be a table (exam.json `advice`, keyed by 大問
            # code): its keys are held to the primary's the same way.
            for k in sorted(want & have):
                pv, cv = ui(p, ns)[k], ui(c, ns)[k]
                if isinstance(pv, dict) or isinstance(cv, dict):
                    pk = set(pv) if isinstance(pv, dict) else set()
                    ck = set(cv) if isinstance(cv, dict) else set()
                    if pk != ck:
                        out.append(f"{c}/{ns}.json `{k}`: keys differ from the primary's "
                                   f"(missing {sorted(pk - ck)}, extra {sorted(ck - pk)})")
    return out


if __name__ == "__main__":
    probs = check()
    print(f"languages: {', '.join(f'{c} ({name(c)})' for c in order())}; primary {primary()}")
    for p in probs:
        print("  !", p)
    raise SystemExit(1 if probs else 0)
