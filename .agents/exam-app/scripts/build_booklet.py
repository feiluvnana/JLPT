#!/usr/bin/env python3
"""
Render JLPT exam Markdown sources to booklet HTML (A4-styled, print-ready).

Usage:
    python build_booklet.py tests/1/言語知識・読解.md tests/1/聴解.md

Requires: `pip install markdown pykakasi`, Noto CJK JP fonts installed.
No PDF toolchain needed — the browser is the renderer.
"""

import hashlib
import functools
import re
import sys

from pathlib import Path

import markdown

# The level table (timing, section names) — the cover prints them, never a copy.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "jlpt-exam-structure" / "scripts"))
import level as LEVEL  # noqa: E402

# Screen-only shell. `CSS` keeps the A4 print geometry (@page etc.) untouched
# so Cmd-P still yields the booklet; this just makes the page readable on a
# monitor, where an unbounded full-width line length is unusable.
SCREEN_CSS = """
@media screen {
  :root { --gutter: 1.6em; }
  body { max-width: 60em; margin: 0 auto; padding: 2.5em var(--gutter) 6em;
         background: #fff; }
  table { max-width: 100%; }
  /* A wide 問題14 table scrolls sideways on a narrow screen. Screen only: a
     scroll container cannot break across printed pages (see .passage-box). */
  .passage-box { overflow-x: auto; }
  .bk-cover { border: 1px solid #d4d4d4; padding: 2.4em 2.6em 1.6em; margin: 0 0 3em; }
}
@media screen and (max-width: 48em) {
  :root { --gutter: 0.8em; }
  body { padding: 1.2em var(--gutter) 4em; font-size: 11pt; }
  table { display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; }
  blockquote { padding: 8px 10px; margin: 8px 0; }
  h1 { font-size: 13.5pt; margin: 22px 0 10px; }
  h2 { font-size: 11pt; margin: 18px 0 10px; }
  h2.bk-mondai-l { font-size: 15pt; }
  .passage-box { padding: 10px 12px; }
  /* Four columns do not fit a phone: halve them, never wrap mid-option. */
  .bk-opts { margin-left: .4em; }
  .bk-opts.bk-c4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .bk-opts.bk-c2 { grid-template-columns: minmax(0, 1fr); }
  .bk-ov { margin-left: .4em; }
  .bk-cover { padding: 1.2em 1em; }
  .bk-cv-level { font-size: 32pt; }
  .bk-cv-title { font-size: 15pt; }
  .bk-cv-notes { padding: .6em .9em; }
}
"""


GOTHIC = ('"YuGothic", "Yu Gothic", "Hiragino Sans", "Noto Sans JP", '
          '"Noto Sans CJK JP", sans-serif')

# The booklet stylesheet. Every layout choice below is read off the official
# 問題用紙 (refs/External/official_workbook_2018, refs/JLPT_N2_NEW/*): plain bold
# Gothic 問題 headings with a hanging instruction, boxed item numbers, tested
# words UNDERLINED in the body face, options on equal columns with no period,
# passages in a thin black rule on white, 「— N —」 page numbers.
CSS = """
@page { size: A4; margin: 18mm 16mm 20mm;
  @bottom-center { content: "— " counter(page) " —"; font-family: %(g)s;
                   font-size: 10pt; color: #1a1a1a; } }
/* The cover is not page 1: official numbering starts on the first page of
   questions. A named page is the one reset Chrome honours (counter-reset on an
   element or on @page:first is ignored). */
@page bk-cover { counter-reset: page 0; @bottom-center { content: none; }
                 @top-right { content: none; } }
body { font-family: "YuMincho", "Yu Mincho", "Hiragino Mincho ProN", "Noto Serif JP", "Noto Serif CJK JP", serif;
       font-size: 11.5pt; line-height: 1.9; color: #1a1a1a; background: #fff; }
h1, h2, h3 { font-family: %(g)s; break-after: avoid; page-break-after: avoid;
             break-inside: avoid; }
h1 { font-size: 15pt; border-bottom: 2.5px solid #1a1a1a; padding-bottom: 5px;
     margin: 30px 0 14px; }
/* 【文字・語彙】/【文法】/【読解】: official prints the part as a small boxed
   label (the tab on the page edge), not a banner. */
h1.bk-part { display: table; font-size: 10.5pt; letter-spacing: .08em;
             border: 1px solid #1a1a1a; padding: 1px 12px; margin: 22px 0 12px; }
h2 { font-size: 12pt; margin: 26px 0 12px; }
/* 「問題1　＿＿の言葉の…」: bold Gothic, the instruction hanging under itself. */
h2.bk-mondai { display: flex; align-items: baseline; gap: 0 1em; line-height: 1.75; }
h2.bk-mondai .bk-mn { flex: 0 0 auto; white-space: nowrap; }
h2.bk-mondai .bk-mi { flex: 1 1 auto; min-width: 0; }
h2.bk-mondai-l { font-size: 18pt; margin: 34px 0 8px; }
h3 { font-size: 11pt; margin: 20px 0 8px; }
p { margin: 12px 0; orphans: 2; widows: 2; }
strong { font-family: %(g)s; }
/* The item number, in a thin box (official 「[11] 9時（　）の…」). */
strong.bk-qn { display: inline-block; min-width: 1.55em; padding: 0 .28em;
               border: 1px solid #1a1a1a; line-height: 1.3; text-align: center;
               font-size: .9em; margin-right: .6em; box-sizing: border-box; }
/* The tested word / the marked span: official UNDERLINES it in the body face.
   The Markdown convention stays **word**; only its rendering changed. */
strong.bk-tw { font-family: inherit; font-weight: normal; text-decoration: underline;
               text-decoration-thickness: 1px; text-underline-offset: .24em; }
/* Options: 「1　はしら」, no period, on four equal columns — or two, or one,
   whichever the longest option fits (widen() decides). */
.bk-opts { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr));
           gap: .05em 1em; margin: .3em 0 .1em 2.1em; }
.bk-opts.bk-c2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.bk-opts.bk-c1 { grid-template-columns: minmax(0, 1fr); }
.bk-o, .bk-ov { display: flex; gap: .95em; }
.bk-ov { margin: .05em 0 0 2.1em; }
.bk-on { flex: 0 0 auto; }
.bk-ot { flex: 1 1 auto; min-width: 0; }
.bk-opts + br, .bk-ov + br { display: none; }
/* The stem hangs past its number box; its options sit on the same edge. */
p:has(> strong.bk-qn:first-child) { padding-left: 1.95em; text-indent: -1.95em; }
p:has(> strong.bk-qn:first-child) > .bk-opts,
p:has(> strong.bk-qn:first-child) > .bk-ov { margin-left: 0; }
.bk-opts, .bk-ov, strong.bk-qn, ruby { text-indent: 0; }
/* Furigana: WeasyPrint has NO ruby layout (and ignores ruby-position), so the
   reading is stacked manually. rt is taken out of flow and pinned above the
   base, which keeps the base glyphs on the text baseline and leaves line
   spacing untouched. Do NOT go back to display:inline-table -- WeasyPrint
   drops the base onto its own line under the reading. */
ruby {
  display: inline-block;
  position: relative;
  text-align: center;
  vertical-align: baseline;
  /* line-height 1 keeps the ruby box hugging its glyphs; with a taller
     inherited line-height the box grows and `bottom: 100%%` would push the
     reading far above the text. */
  line-height: 1;
}
rb { display: inline; }
rt {
  position: absolute;
  bottom: calc(100%% + 0.1em);
  left: -0.6em;
  right: -0.6em;
  font-size: 0.5em;
  line-height: 1;
  font-weight: normal;
  color: #333;
  white-space: nowrap;
  text-align: center;
}
rp { display: none; }
/* Only blocks that actually carry furigana get extra leading, so the reading
   clears the descenders of the line above without loosening plain text. */
p.furi, li.furi { line-height: 2.1; }
/* 注 glosses: body-ish size under the passage, no rule; the inline （注N）
   marker is small and raised, as printed. */
.vocab-notes { margin: 10px 0 0; font-size: 10pt; line-height: 1.75; color: #1a1a1a; }
.bk-chu { font-size: .68em; position: relative; top: -.4em; }
table { border-collapse: collapse; margin: 10px 0; width: 100%%; page-break-inside: avoid; }
th, td { border: 1px solid #888; padding: 4px 9px; font-size: 10pt;
         line-height: 1.6; }
th { background: #f0f0f0; font-family: %(g)s; }
blockquote { border: 1px solid #999; background: #fafafa; margin: 10px 0;
             padding: 10px 14px; page-break-inside: avoid; }
/* 問題9-14: the passage/notice text official booklets print inside a thin
   black rule on white, separate from the questions below it. See
   box_passages(). A box too tall for a page (問題13's essay, 問題14's flyer)
   carries the .bk-flow marker and may break; the rest stay whole. The box must
   not scroll in print: Chrome lays a scroll container out as one unbreakable
   block, which is how 問題14 once printed a blank page. */
.passage-box { border: 1px solid #1a1a1a; background: #fff; margin: 10px 0 16px;
               padding: 12px 18px; break-inside: avoid; page-break-inside: avoid; }
.passage-box:has(> .bk-flow) { break-inside: auto; page-break-inside: auto; }
.passage-box > *:first-child, .passage-box > .bk-flow + * { margin-top: 0; }
.passage-box > *:last-child { margin-bottom: 0; }
.bk-flow { display: none; }
/* 聴解: 「― メモ ―」 centred, with room to write under it. */
.bk-memo { text-align: center; letter-spacing: .25em; margin: 16px 0 72px; }
hr { border: none; border-top: 1px dashed #999; margin: 22px 0; }
/* The 問題用紙 cover (booklet HTML only — the sheet has its own gate screen). */
.bk-cover { font-family: %(g)s; }
.bk-cv-head { display: flex; justify-content: space-between; align-items: baseline; }
.bk-cv-en { font-size: 10pt; font-weight: 700; }
.bk-cv-kind { font-size: 17pt; font-weight: 700; }
.bk-cv-level { text-align: center; font-size: 46pt; font-weight: 800; line-height: 1.2;
               margin: 1.1em 0 .1em; letter-spacing: .04em; }
.bk-cv-title { text-align: center; font-size: 21pt; font-weight: 800; line-height: 1.4; }
.bk-cv-time { text-align: center; font-size: 17pt; font-weight: 700; margin: .3em 0 .9em; }
.bk-cv-notes { border: 1px solid #1a1a1a; padding: .8em 1.8em 1em; margin: 0 auto 1.4em;
               max-width: 36em; font-family: "YuMincho", "Yu Mincho", "Hiragino Mincho ProN", "Noto Serif JP", serif; }
.bk-cv-nh { text-align: center; font-family: %(g)s; font-weight: 700; font-size: 13pt;
            letter-spacing: .5em; margin-bottom: .4em; }
.bk-cv-nh small { font-size: 7.5pt; letter-spacing: 0; }
.bk-cv-item { display: flex; gap: .8em; margin: .35em 0; line-height: 1.6; }
.bk-cv-item small { display: block; font-size: 8pt; color: #333; line-height: 1.35; }
.bk-cv-box { display: inline-block; border: 1px solid #1a1a1a; min-width: 1.2em;
             line-height: 1.15; text-align: center; font-size: .85em; font-family: %(g)s; }
.bk-cv-id { max-width: 36em; margin: .7em auto; font-family: "YuMincho", "Yu Mincho", serif; }
.bk-cv-id th { width: 45%%; background: #fff; font-weight: normal; text-align: left;
               font-family: inherit; }
.bk-cv-id td { height: 2.2em; }
@media print {
  .bk-cover { page: bk-cover; break-after: page; }
  h1.bk-brk, h1.bk-key { break-before: page; page-break-before: always; }
  /* An item (stem + its options) never splits across pages. */
  p:has(> .bk-opts), p:has(> .bk-ov) { break-inside: avoid; page-break-inside: avoid; }
  /* 聴解: every 問題 opens a new page, as printed (the first follows the label). */
  h2.bk-mondai-l { break-before: page; page-break-before: always; }
  h1.bk-part + h2.bk-mondai-l { break-before: auto; page-break-before: auto; }
  /* 「右のページは…の案内である」: the flyer gets a page of its own. */
  .passage-box:has(> .bk-flyer) { break-before: page; page-break-before: always; }
}
""" % {"g": GOTHIC}


def source_sha(path: Path) -> str:
    """First 12 hex digits of sha1 over the file's raw BYTES.

    Same convention `tools/compose_choukai.py` stamps into \u8074\u89e3_\u30c1\u30e3\u30d7\u30bf\u30fc.json as
    `script_sha`. NOT an mtime: mtimes are checkout-unstable, so they cannot
    distinguish "rebuilt" from "merely re-checked-out".
    """
    return hashlib.sha1(path.read_bytes()).hexdigest()[:12]


def src_sha_comments(sources) -> str:
    """`<!-- src_sha: <file name>=<12-hex sha1> -->`, one comment per input.

    Stamped into every generated HTML so an artifact built from a superseded
    Markdown source is detectable by content, and `make check` can fail on it.
    The precedent is on the audio side: a script rewrite across several
    \u8074\u89e3\u30b9\u30af\u30ea\u30d7\u30c8.txt files once rebuilt only one MP3, and nothing could see
    the rest. The HTML deliverables had exactly the same blind spot.
    `build_interactive.py` calls this helper too, so both builders emit one
    format. Each stamp gets its own line (the rest of the document is one long
    line) so it is greppable and shows up as a one-line diff on a rebuild.
    """
    return "".join(f"\n<!-- src_sha: {p.name}={source_sha(p)} -->\n"
                   for p in sources if p.is_file())


OPT = re.compile(r"[1-4]\.\s")
# One option number inside a line: start of line or after whitespace, so a
# decimal in option text (`価格が3.5倍`) is never taken for a number.
OPT_NUM = re.compile(r"(?:^|(?<=\s))([1-4])\.\s+")
VERT_OPT = re.compile(r"^\s+([1-4])\.\s*(.+)$")
# widen()'s column choice, in em of option text at body size. A4 less 32 mm of
# margin is ~44 em at 11.5 pt; four columns leave ~8.5 em of text after the
# number and gap, two leave ~19. Anything longer is laid one per line.
COLS_4_MAX_EM = 8.5
COLS_2_MAX_EM = 19.0


@functools.lru_cache(maxsize=1)
def _kakasi():
    """One converter per process (~15 ms each; a full `make pages` built 80)."""
    try:
        import pykakasi
    except ImportError:
        return None
    return pykakasi.kakasi()


def add_choukai_furigana(md_content: str) -> str:
    """Add HTML ruby furigana to all kanji in listening test booklet text/options."""
    kks = _kakasi()
    if kks is None:
        return md_content

    def fix_hira(orig: str, hira: str, prev_orig: str = '') -> str:
        """Correct known pykakasi mis-readings before ruby conversion.

        Never trust kakasi's hira output as-is -- confirmed wrong on three
        recurring patterns: (1) 小さ+い/く conjugations (小さい, 小さく,
        小さかった, 小さすぎる, 小さくない, 小さくて) come back with a chouon
        mark, e.g. "ちーさい" instead of "ちいさい"; (2) a bare single-kanji
        人 token is always read にん by kakasi, but every genuine にん
        compound (三人, 本人, 友人, 何人, ...) is already merged into one
        multi-character token by kakasi, so a standalone 人 is always the
        word "hito" (a/the person), never にん; (3) a 方 token immediately
        following hiragana (a verb's renyoukei/stem: 伝わり方, 使い方, 考え方,
        食べ方, 話し方, ...) is the "method/way" reading かた, never ほう --
        every genuine ほう compound (一方, 先方, 双方, 四方, ...) has 方
        attached directly to a preceding KANJI, so kakasi merges it into one
        token and this rule never fires on those.
        """
        if orig.startswith('小さ') and 'ちー' in hira:
            hira = hira.replace('ちー', 'ちい')
        if orig == '人' and hira == 'にん':
            hira = 'ひと'
        if orig.startswith('方') and hira.startswith('ほう') and prev_orig \
                and '぀' <= prev_orig[-1] <= 'ゟ' \
                and (len(orig) == 1 or not ('一' <= orig[1] <= '鿿')):
            hira = 'かた' + hira[2:]
        return hira

    def token_to_ruby(orig: str, hira: str) -> str:
        if orig == '入っ' and hira == 'いっっ':
            return '<ruby>入<rt>はい</rt></ruby>っ'
        suffix = ''
        while orig and hira and orig[-1] == hira[-1] and not ('\u4e00' <= orig[-1] <= '\u9fff'):
            suffix = orig[-1] + suffix
            orig = orig[:-1]
            hira = hira[:-1]
        prefix = ''
        while orig and hira and orig[0] == hira[0] and not ('\u4e00' <= orig[0] <= '\u9fff'):
            prefix = prefix + orig[0]
            orig = orig[1:]
            hira = hira[1:]
        if orig and any('\u4e00' <= c <= '\u9fff' for c in orig):
            return f'{prefix}<ruby>{orig}<rt>{hira}</rt></ruby>{suffix}'
        return prefix + orig + suffix

    overrides = {
        '時間': '<ruby>時間<rt>じかん</rt></ruby>',
        '分': '<ruby>分<rt>ふん</rt></ruby>',
        '問題数': '<ruby>問題数<rt>もんだいすう</rt></ruby>',
        '問': '<ruby>問<rt>もん</rt></ruby>',
        '問題': '<ruby>問題<rt>もんだい</rt></ruby>',
        '例': '<ruby>例<rt>れい</rt></ruby>',
        '番': '<ruby>番<rt>ばん</rt></ruby>',
    }

    rad = re.compile(r'<div class="qa')
    out_lines = []
    in_answer_key = False
    for line in md_content.splitlines():
        if '# 【正解・解説】' in line or '# 解答用紙' in line:
            in_answer_key = True
        if in_answer_key or line.startswith('#') or line.startswith('|') or '---' in line or '<ruby>' in line:
            out_lines.append(line)
            continue

        # 解答.html's injected radio groups are HTML, never prose: the `問` in
        # `name="q_問3-1"` would be rewritten to <ruby>問<rt>もん</rt></ruby> here
        # and by fit_ruby, breaking the attribute (nested quotes) and making the
        # grader's querySelector('input[name="q_…"]') miss the group. Rubify the
        # leading markdown part of a mixed line, leave the group untouched.
        if rad.search(line):
            head, sep, tail = line.partition('<div class="qa')
            if not head:
                out_lines.append(line)
            else:
                res = kks.convert(head)
                head_out = ''
                prev_orig = ''
                for item in res:
                    orig = item['orig']
                    hira = fix_hira(orig, item['hira'], prev_orig)
                    head_out += overrides[orig] if orig in overrides \
                        else token_to_ruby(orig, hira)
                    prev_orig = orig
                out_lines.append(head_out + sep + tail)
            continue

        res = kks.convert(line)
        line_out = ''
        prev_orig = ''
        for item in res:
            orig = item['orig']
            hira = fix_hira(orig, item['hira'], prev_orig)
            if orig in overrides:
                line_out += overrides[orig]
            else:
                line_out += token_to_ruby(orig, hira)
            prev_orig = orig
        out_lines.append(line_out)

    return '\n'.join(out_lines)


RUBY_TAG = re.compile(r"<ruby>(.*?)<rt>(.*?)</rt>\s*</ruby>", re.S)
TAGS = re.compile(r"<[^>]+>")


def _em_width(text: str) -> float:
    """Approximate advance width in em: CJK/kana are full-width, ASCII half."""
    return sum(0.5 if ord(c) < 0x2E80 else 1.0 for c in text)


# How far a reading may overhang its base, per side: official booklets let
# furigana spill over neighbouring kana. The overhang may use the plain text
# up to the next ruby, minus that ruby's own overhang and a quarter-em
# clearance, and never more than half an em. The reading is centred, so the
# tighter side sets both.
RUBY_OVERHANG_EM = 0.5
_LINE_EDGE = re.compile(r"<br|<p[ >]|</p>|<li|bk-on|<strong|</strong>")


def fit_ruby(html: str) -> str:
    """Reserve room for readings wider than their base so furigana never
    collides with the neighbouring word's furigana.

    rt is absolutely positioned (see CSS), so a long reading would otherwise
    overhang its base. Widening the base box centres the kanji inside the space
    the reading needs -- the same thing furigana-heavy print books do -- less
    the overhang its neighbours leave room for (RUBY_OVERHANG_EM), which is
    what closed the visible gaps around 練習中/提出 in 聴解.html.
    """
    rubies = list(RUBY_TAG.finditer(html))
    if not rubies:
        return html
    need, have = [], []
    for m in rubies:
        need.append(_em_width(TAGS.sub("", m.group(2))) * 0.5)  # rt at 0.5em
        have.append(_em_width(TAGS.sub("", m.group(1))))
    spill = [max(0.0, (n - h) / 2) for n, h in zip(need, have)]

    def room(i: int, j: int) -> float:
        """Overhang ruby i may take toward neighbour j (j = i±1)."""
        if j < 0 or j >= len(rubies):
            return RUBY_OVERHANG_EM
        lo, hi = sorted((i, j))
        between = html[rubies[lo].end(): rubies[hi].start()]
        if _LINE_EDGE.search(between):
            return RUBY_OVERHANG_EM
        gap = _em_width(TAGS.sub("", between))
        return max(0.0, min(RUBY_OVERHANG_EM, gap - spill[j] - 0.25))

    out, last = [], 0
    for i, m in enumerate(rubies):
        want = need[i] - 2 * min(room(i, i - 1), room(i, i + 1))
        out.append(html[last: m.start()])
        if want - have[i] <= 0.05:
            out.append(m.group(0))
        else:
            out.append(f'<ruby style="min-width:{want:.2f}em">{m.group(1)}'
                       f'<rt>{m.group(2)}</rt></ruby>')
        last = m.end()
    out.append(html[last:])
    return "".join(out)


BLOCK = re.compile(r"<(p|li)>(.*?)</\1>", re.S)
NOTE_ITEM = re.compile(r"（注\d+）[^（\n]*")


def split_vocab_note_line(line: str) -> str:
    """One （注N） gloss per line in vocabulary note blocks."""
    stripped = line.strip().rstrip("\\")
    if not stripped.startswith("（注"):
        return line
    items = NOTE_ITEM.findall(stripped)
    if len(items) <= 1:
        return line
    prefix = line[: len(line) - len(line.lstrip())]
    return "\n".join(prefix + item for item in items)


def format_vocab_notes(md: str) -> str:
    return "\n".join(split_vocab_note_line(l) for l in md.splitlines())


def mark_vocab_notes(html: str) -> str:
    """Tag gloss blocks so `.vocab-notes` styling applies."""

    def sub(m: re.Match) -> str:
        tag, inner = m.group(1), m.group(2)
        text = TAGS.sub("", inner).strip()
        if text.startswith("（注"):
            return f'<{tag} class="vocab-notes">{inner}</{tag}>'
        return m.group(0)

    return BLOCK.sub(sub, html)


def mark_furigana_blocks(html: str) -> str:
    """Tag <p>/<li> holding ruby so CSS can give them furigana leading."""
    def sub(m: re.Match) -> str:
        tag, inner = m.group(1), m.group(2)
        cls = ' class="furi"' if "<ruby" in inner else ""
        return f"<{tag}{cls}>{inner}</{tag}>"

    return BLOCK.sub(sub, html)


def _plain_em(text: str) -> float:
    """Printed width of option text: readings, tags and `**` do not count."""
    text = re.sub(r"<rt>.*?</rt>", "", text, flags=re.S)
    return _em_width(TAGS.sub("", text).replace("**", "").strip())


def _opt_cell(n: str, text: str) -> str:
    return (f'<span class="bk-o"><span class="bk-on">{n}</span>'
            f'<span class="bk-ot">{text.strip()}</span></span>')


def widen(line: str) -> str:
    """Lay one Markdown option line out the way the official booklet does.

    `1. はしら  2. ゆか  3. かべ  4. たな` becomes four equal grid columns
    printing `1　はしら` — no period — or a 2x2 grid, or one option per line,
    whichever the LONGEST option fits (COLS_*_MAX_EM), so no option ever wraps
    in the middle. A vertical line (` 1. …`) keeps its own row with the same
    number/text split. Emits inline HTML the Markdown pass keeps (its `**`
    still renders); anything before the `1.` (問題9's `**48** `) stays in front.

    The sheet's parsers (build_interactive.inject_gengo/inject_choukai) read the
    Markdown BEFORE this runs, so the bubble count never depends on it.
    """
    nums = list(OPT_NUM.finditer(line))
    starts = [i for i, m in enumerate(nums) if m.group(1) == "1"]
    if starts:
        run = nums[starts[0]:]
        k = 0
        while k < len(run) and run[k].group(1) == str(k + 1):
            k += 1
        run = run[:k]
        if len(run) >= 3:
            ends = [m.start() for m in run[1:]] + [len(line)]
            texts = [line[m.end():e] for m, e in zip(run, ends)]
            w = max(_plain_em(t) for t in texts)
            cols = 4 if w <= COLS_4_MAX_EM else 2 if w <= COLS_2_MAX_EM else 1
            cells = "".join(_opt_cell(str(i), t) for i, t in enumerate(texts, 1))
            prefix = line[: run[0].start()].strip()
            prefix = prefix + " " if prefix else ""
            return f'{prefix}<span class="bk-opts bk-c{cols}">{cells}</span>'
    m = VERT_OPT.match(line)
    if m:
        return (f'<span class="bk-ov"><span class="bk-on">{m.group(1)}</span>'
                f'<span class="bk-ot">{m.group(2).strip()}</span></span>')
    return line


BOX_START = "JLPTPASSAGEBOXSTART"
BOX_END = "JLPTPASSAGEBOXEND"
KEY_SPLIT = re.compile(r"^#+\s*(?:解答|【?正解)", re.M)
# Both authored dialects must box, or the box silently disappears (see
# box_passages()): the 問題N instruction may sit on the `## 問題N` line OR in
# its own paragraph below, and 問題12's two texts may be labelled `### A` OR
# `**A**`. `[^\n]*` on the heading and SUB_MARK's two alternatives are what
# make the boxer dialect-agnostic -- narrowing either one drops boxes with no
# error (2026-08-20: `[ \t]*` here boxed nothing at all in three papers).
SECTION_RE = re.compile(r"^(## 問題(?:9|10|11|12|13|14))([^\n]*)\n(.*?)(?=^## |\Z)", re.M | re.S)
SUB_MARK = r"(?:###[ \t][^\n]*|\*\*[A-D]\*\*[ \t]*)"
SUBSECTION_RE = re.compile(rf"^({SUB_MARK}\n)(.*?)(?=^{SUB_MARK}$|\Z)", re.M | re.S)
FIRST_STEM_RE = re.compile(r"\n\*\*\d+\*\*")
FIRST_PARA_GAP_RE = re.compile(r"\n[ \t]*\n")


# 問題14's flyer box opens with this sentinel instead: it CONTAINS BOX_START,
# so every count of boxes (check_passage_boxes counts BOX_START) is unchanged.
FLYER_START = BOX_START + "FLYER"


def _box_upto_stem(body: str, start: str = BOX_START) -> str:
    """Wrap `body` up to its first **NN** question marker in BOX_START/END
    sentinels (converted to a real <div> after markdown rendering -- see
    box_passages()). A body with no marker at all (問題12's "### A") is
    boxed in full."""
    m = FIRST_STEM_RE.search(body)
    passage, rest = (body[: m.start()], body[m.start():]) if m else (body, "")
    passage = passage.strip("\n")
    if not passage:
        return body
    return f"\n\n{start}\n\n{passage}\n\n{BOX_END}\n\n{rest.strip(chr(10))}\n"


def _process_section(m: re.Match) -> str:
    number, head_tail, body = m.group(1), m.group(2), m.group(3)
    heading = f"{number}{head_tail}\n"
    start = FLYER_START if number.endswith("問題14") else BOX_START
    if SUBSECTION_RE.search(body):
        # ### (1) / ### A / **A** subsections: the box wraps each
        # subsection's own passage, so the section's instruction line (before
        # the first marker) sits outside every box, matching official layout.
        # The marker itself stays outside too -- the label prints above the
        # ruled box, as in the official booklets.
        body = SUBSECTION_RE.sub(lambda sm: sm.group(1) + _box_upto_stem(sm.group(2)), body)
    elif head_tail.strip():
        # 問題9/13/14 with the instruction already on the heading line: the
        # whole body IS the passage. Skipping a paragraph here would push the
        # passage's first paragraph out of the box.
        body = _box_upto_stem(body, start)
    else:
        # No subsections (問題9/13/14): skip the leading instruction
        # sentence -- the box starts at the next paragraph (the passage's
        # own title/text).
        pm = FIRST_PARA_GAP_RE.search(body)
        instr, passage_block = (body[: pm.start()], body[pm.start():]) if pm else ("", body)
        body = instr + _box_upto_stem(passage_block, start)
    return heading + body


def box_passages(text: str) -> str:
    """Wrap each 問題9-14 passage/notice in a BOX_START/END sentinel pair so
    it renders inside a ruled box, the way official booklets separate the
    reading text from the questions under it (`.passage-box` in CSS).
    Operates on raw markdown, before `markdown.markdown()`, so the sentinels
    -- plain text, no markdown-special characters -- become their own
    paragraph and box_passages_html() below can swap them for a real <div>
    without disturbing nl2br/tables parsing of what's inside."""
    exam_body, *rest = KEY_SPLIT.split(text, maxsplit=1)
    boxed = SECTION_RE.sub(_process_section, exam_body)
    return boxed if not rest else boxed + text[len(exam_body):]


# A box longer than this (text characters), or holding a table, may break
# across printed pages (`.bk-flow`); a shorter one is kept whole. An A4 page
# holds ~1,400 characters of passage, so 1,000 keeps every 問題10–12 text whole
# and lets 問題13's essay and 問題14's flyer flow instead of leaving a blank page.
FLOW_CHARS = 1000


def box_passages_html(html_text: str) -> str:
    """Swap box_passages()'s rendered sentinel paragraphs for the real div.

    The opening tag stays exactly `<div class="passage-box">` — `make check`
    counts that string and build_practice finds boxes by it — so a tall box is
    marked by a hidden first child instead of a second class."""
    def box(m: re.Match) -> str:
        flyer, inner = bool(m.group(1)), m.group(2)
        flow = flyer or "<table" in inner or len(TAGS.sub("", inner)) > FLOW_CHARS
        marker = ('<span class="bk-flow bk-flyer"></span>' if flyer
                  else '<span class="bk-flow"></span>' if flow else "")
        return f'<div class="passage-box">{marker}{inner}</div>'

    html_text = re.sub(rf"<p>\s*{BOX_START}(FLYER)?\s*</p>(.*?)<p>\s*{BOX_END}\s*</p>",
                       box, html_text, flags=re.S)
    html_text = re.sub(rf"<p>\s*{BOX_START}(?:FLYER)?\s*</p>", '<div class="passage-box">', html_text)
    html_text = re.sub(rf"<p>\s*{BOX_END}\s*</p>", "</div>", html_text)
    return html_text


# Python-Markdown strips a paragraph's leading whitespace, U+3000 included, so
# every passage lost the 1-字 indent of its FIRST paragraph (later lines,
# joined by nl2br, kept theirs). A placeholder rides through and is put back.
INDENT_MARK = "JLPTIDEOGRAPHICINDENT"
LEADING_IDEO = re.compile(r"^(　+)(?=\S)", re.M)


def keep_indent(md: str) -> str:
    return LEADING_IDEO.sub(lambda m: INDENT_MARK * len(m.group(1)), md)


def restore_indent(html_text: str) -> str:
    return html_text.replace(INDENT_MARK, "　")


KEY_HTML = re.compile(r"<h[1-6][^>]*>\s*(?:解答|【?正解)")
H1_RE = re.compile(r"<h1>(.*?)</h1>", re.S)
H2_MONDAI = re.compile(r"<h2>(問題\s*\d+)[ \t　]*(.*?)</h2>", re.S)
STEM_NUM = re.compile(r'(<p(?: class="[^"]*")?>|<br />\n?)<strong>(\d{1,2})'
                      r'(?:[ 　]+([^<]+))?</strong>')
TABLE_RE = re.compile(r"(<table.*?</table>)", re.S)
STRONG_RE = re.compile(r"<strong>(.*?)</strong>", re.S)
# What may sit right before a label/title that fills its own line.
LINE_HEAD = re.compile(r'(?:<p[^>]*>|<br />|<div class="passage-box">|'
                       r'<span class="bk-flow"></span>|<span class="bk-ot">|'
                       r'<strong class="bk-qn">\d+</strong>|<li[^>]*>)\s*$')
LINE_TAIL = re.compile(r"\s*(?:<br|</p>|</li>|</span>|$)|[：:　 ]")
PARA_RE = re.compile(r'<p(?: class="([^"]*)")?>(.*?)</p>', re.S)
CHU_RE = re.compile(r"（注\d+）")
MEMO_RE = re.compile(r'<p(?: class="furi")?>\s*[-ー―－]+\s*メモ\s*[-ー―－]+\s*</p>')


def _mark_tested(chunk: str) -> str:
    """`**word**` → underlined tested word, unless it is a title or label.

    A bold span that fills its own line (a notice title, 問題12's A/B, 問題6's
    headword) or opens a line as a label (`**夕食**　…`, `**申請方法**：…`) stays
    bold Gothic; every other one — the target word in a stem, a marked span in
    a passage — is what official prints underlined in the body face."""
    def sub(m: re.Match) -> str:
        head = LINE_HEAD.search(chunk, max(0, m.start() - 80), m.start())
        if head and head.end() == m.start() and LINE_TAIL.match(chunk, m.end()):
            return m.group(0)
        return f'<strong class="bk-tw">{m.group(1)}</strong>'

    return STRONG_RE.sub(sub, chunk)


def _small_chu(para: re.Match) -> str:
    cls, inner = para.group(1) or "", para.group(2)
    if "vocab-notes" in cls:
        return para.group(0)
    return para.group(0).replace(
        inner, CHU_RE.sub(lambda m: f'<span class="bk-chu">{m.group(0)}</span>', inner), 1)


def style_exam(html_text: str, is_choukai: bool) -> str:
    """The official 問題用紙 look, applied to the rendered exam part only.

    Boxed item numbers, bold-Gothic 問題 headings with a hanging instruction,
    boxed part labels (読解 opens a new printed page), underlined tested words,
    small inline （注N） markers, a centred 「― メモ ―」. The answer key after
    the key heading is left as it was, except that it starts a new page."""
    m = KEY_HTML.search(html_text)
    exam, key = (html_text[: m.start()], html_text[m.start():]) if m else (html_text, "")

    def h1(mm: re.Match) -> str:
        cls = "bk-part bk-brk" if "読解" in mm.group(1) else "bk-part"
        return f'<h1 class="{cls}">{mm.group(1)}</h1>'

    def h2(mm: re.Match) -> str:
        cls = "bk-mondai bk-mondai-l" if is_choukai else "bk-mondai"
        instr = mm.group(2).strip()
        rest = f' <span class="bk-mi">{instr}</span>' if instr else ""
        return f'<h2 class="{cls}"><span class="bk-mn">{mm.group(1)}</span>{rest}</h2>'

    def stem(mm: re.Match) -> str:
        word = mm.group(3)
        tail = f" <strong>{word.strip()}</strong>" if word else ""
        return f'{mm.group(1)}<strong class="bk-qn">{mm.group(2)}</strong>{tail}'

    exam = H2_MONDAI.sub(h2, H1_RE.sub(h1, exam))
    exam = STEM_NUM.sub(stem, exam)
    if not is_choukai:
        exam = "".join(part if part.startswith("<table") else _mark_tested(part)
                       for part in TABLE_RE.split(exam))
        exam = PARA_RE.sub(_small_chu, exam)
    exam = MEMO_RE.sub('<p class="bk-memo">― メモ ―</p>', exam)
    key = key.replace("<h1>", '<h1 class="bk-key">', 1)
    return exam + key


def render_body(md: str, is_choukai: bool) -> str:
    """One half of the paper, Markdown → body HTML. The ONE render chain.

    `build()` below and both solving pages (build_interactive.render_bodies, for
    解答.html and 練習.html) go through here, so the ruled boxes, the option
    grid, the furigana and the item-number boxes cannot differ between the
    booklet and the sheet. The sheet hands in Markdown whose radios are already
    injected and whose key is already truncated."""
    if is_choukai:
        md = add_choukai_furigana(md)
    else:
        md = box_passages(md)
    exam, *rest = KEY_SPLIT.split(md, maxsplit=1)
    md = "\n".join(widen(l) for l in exam.splitlines()) + (
        "\n" + md[len(exam):] if rest else "")
    md = keep_indent(format_vocab_notes(md))
    # nl2br is MANDATORY: keeps stacked answer options on separate lines.
    body = restore_indent(markdown.markdown(md, extensions=["tables", "nl2br"]))
    body = mark_vocab_notes(mark_furigana_blocks(fit_ruby(body)))
    if not is_choukai:
        body = box_passages_html(body)
    return style_exam(body, is_choukai)


def _cover_notes(is_choukai: bool) -> list[tuple[str, str]]:
    notes = [
        ("試験が始まるまで、この問題用紙を開けないでください。",
         "Do not open this question booklet until the test begins."),
        ("この問題用紙を持って帰ることはできません。",
         "Do not take this question booklet with you after the test."),
        ("受験番号と名前を下の欄に、受験票と同じように書いてください。",
         "Write your examinee registration number and name clearly in each box "
         "below as written on your test voucher."),
    ]
    if is_choukai:
        notes.append(("この問題用紙にメモをとってもかまいません。",
                      "You may make notes in this question booklet."))
    else:
        box = '<span class="bk-cv-box">{}</span>'
        nums = "、".join(box.format(n) for n in (1, 2, 3))
        notes.append((f"問題には解答番号の{nums} … が付いています。"
                      "解答は、解答用紙にある同じ番号のところにマークしてください。",
                      f"One of the row numbers {nums} … is given for each question. "
                      "Mark your answer in the same row of the answer sheet."))
    return notes


def cover_html(level: str, is_choukai: bool) -> str:
    """The 問題用紙 cover: level, section name and time, the 注意 box and the
    受験番号・名前 lines, as the official booklet prints them. Section names and
    minutes come from the level table (`level.py`), never from this file.
    Booklet only — 解答.html/練習.html open on their own gate screen.
    The page count (official 注意 4.) is left out: HTML has no fixed pages."""
    try:
        table = LEVEL.load(level)
        names = [s["name"] for s in table["scoring"]["sections"]]
        minutes = table["timing"]["choukai_min" if is_choukai else "gengo_min"]
    except Exception:  # a scaffold level: no cover rather than a wrong one
        return ""
    title = names[-1] if is_choukai else "・".join(names[:-1])
    en = "Listening" if is_choukai else "Language Knowledge (Vocabulary/Grammar)・Reading"
    items = "".join(
        f'<div class="bk-cv-item"><span>{i}.</span><div>{ja}<small>{en_}</small></div></div>'
        for i, (ja, en_) in enumerate(_cover_notes(is_choukai), 1))
    return (f'<section class="bk-cover">'
            f'<div class="bk-cv-head"><span class="bk-cv-en">{en}</span>'
            f'<span class="bk-cv-kind">問題用紙</span></div>'
            f'<div class="bk-cv-level">{level}</div>'
            f'<div class="bk-cv-title">{title}</div>'
            f'<div class="bk-cv-time">（{minutes}分）</div>'
            f'<div class="bk-cv-notes"><div class="bk-cv-nh">注意 <small>Notes</small></div>'
            f'{items}</div>'
            f'<table class="bk-cv-id"><tr><th>受験番号　Examinee Registration Number</th>'
            f'<td></td></tr></table>'
            f'<table class="bk-cv-id"><tr><th>名前　Name</th><td></td></tr></table>'
            f'</section>')


FONT_TAGS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Noto+Serif+JP:wght@400;700&display=swap" rel="stylesheet">'
)


def build(src: Path) -> Path:
    """Markdown source -> styled A4 HTML booklet. Returns the path written.

    No PDF toolchain — browser `@page` geometry layout renders identical A4
    and the same CSS prints correctly straight from the browser. The document
    is verified BEFORE it is written: a failing verify() must not leave a
    freshly sha-stamped file behind that `make check` would take as current."""
    md = src.read_text(encoding="utf-8")
    is_choukai = "聴解" in src.name or "choukai" in src.name.lower()
    body = render_body(md, is_choukai)
    level = LEVEL.declared_level(src.parent) or LEVEL.level_of(src.parent.name)
    cover = cover_html(level, is_choukai)
    # The official running head (「言語知識（文字・語彙・文法）・読解」 top right).
    title = re.search(r'bk-cv-title">([^<]*)<', cover) if cover else None
    running = (f'@page {{ @top-right {{ content: "{title.group(1)}"; '
               f'font-family: {GOTHIC}; font-size: 8.5pt; color: #333; }} }}'
               if title else "")
    html = (f'<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'{FONT_TAGS}'
            f"<title>{src.stem}</title>"
            f"{src_sha_comments([src])}"
            f"<style>{CSS}{running}{SCREEN_CSS}</style></head>"
            f"<body>{cover}{body}</body></html>")
    html_path = src.with_suffix(".html")
    verify_html(html, html_path, src)
    html_path.write_text(html, encoding="utf-8")
    return html_path


def verify_html(html: str, html_path: Path, src: Path):
    """The checks that used to run against the PDF, now against the HTML
    string — run before anything is written."""
    problems = []
    if "�" in html:
        problems.append("mojibake (U+FFFD) in output")
    # Question numbering must stay continuous across section boundaries. `N.`
    # list syntax makes python-markdown emit <ol> and restart at 1 in every
    # section, so question-authoring mandates bold `**N**` stems.
    if "<ol>" in html:
        problems.append("<ol> present — a stem used `N.` list syntax and will "
                        "renumber from 1; use `**N**` instead")
    if "言語知識" in src.name:
        # Rendered as the boxed number (`strong.bk-qn`); a bare `<strong>N`
        # still counts, so a stem style_exam() missed is not a false gap.
        nums = {int(m.group(1)) for m in
                re.finditer(r'<strong(?: class="bk-qn")?>(\d{1,2})(?:</strong>|\s)', html)}
        # Contiguous from 1 to the paper's own last number — not 1..71, which
        # was N2's generated shape and let a 72/75-item import drop its tail.
        missing = [n for n in range(1, max(nums, default=0) + 1) if n not in nums]
        if missing:
            problems.append(f"no bold stem found for question(s) {missing}")
    if problems:
        raise SystemExit(f"{html_path} (NOT written):\n  " + "\n  ".join(problems))
    print(f"  ok: {html_path} "
          f"({len(re.sub(r'<[^>]+>', '', html)):,} chars of text)")


def verify(html_path: Path, src: Path):
    """verify_html() on a file already on disk."""
    verify_html(html_path.read_text(encoding="utf-8"), html_path, src)


if __name__ == "__main__":
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not argv:
        sys.exit("usage: build_booklet.py tests/<id>/言語知識・読解.md "
                 "[tests/<id>/聴解.md]")
    for arg in argv:
        src = Path(arg)
        if not src.is_file():
            sys.exit(f"not found: {src}")
        out = build(src)          # verifies before writing
        print(f"built {out}")
