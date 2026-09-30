#!/usr/bin/env python3
"""Build the STATIC deployment of the exam app — the GitHub Pages version.

    python3 .agents/exam-app/scripts/build_pages.py
    # or: make pages          (preview it with: make preview-pages)

`make serve` and GitHub Pages are the same three screens; only the storage
differs. There is no server on Pages to POST to and no disk to write, so the
sheets are rebuilt with `--storage local` and the answers and results live in
the browser's localStorage under keys that spell out the very files they stand
in for — local_store.py owns that key schema and is the only place it is
written down.

Everything else is shared, not copied: the level and module choosers are
`portal_view.py` and the test list is `index_view.py` (the same pages `make
serve` renders, the list fed from localStorage instead of `/api/tests`), and
the sheets come from `build_interactive.build()`.

Output tree (default `_site/`, gitignored — CI builds it, nothing commits it).
It is `make serve`'s URL tree, file for file:

    _site/.nojekyll                    Pages must not run Jekyll over this
    _site/index.html                   level chooser (N1–N5)
    _site/<LEVEL>/index.html           module chooser (試験 / 知識 / ドリル), every level
    _site/<LEVEL>/exam/index.html      that level's test list + its manifest
    _site/knowledge/<LEVEL>/**/*.html  the built 知識 pages, copied (no JSON)
    _site/drill/<LEVEL>/**/*.html      the built ドリル pages (reserved; none yet)
    _site/tests/<id>/解答.html         screens 2 and 3, storage=local
    _site/tests/<id>/聴解.mp3          the audio the player streams

An LFS-tracked 聴解.mp3 that was never fetched (CI checks out with `lfs: false`)
is a text stub, not audio: it is detected and the paper deploys without a player
instead of with a silent one.

Nothing under `tests/` on disk is written or modified.
"""
import argparse
import contextlib
import io
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TESTS = ROOT / "tests"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_interactive  # noqa: E402
import index_view         # noqa: E402
import portal_view        # noqa: E402
import serve_sheet        # noqa: E402

MARKER = ".nojekyll"      # also our "this directory is a build output" flag
AUDIO = "聴解.mp3"

# The first bytes of a Git LFS pointer file — see is_lfs_pointer().
LFS_POINTER = b"version https://git-lfs.github.com/spec/v1"


def deployable(test_id: str | None = None) -> list[Path]:
    """Test folders that can be built into the site, in the list's own order."""
    if not TESTS.is_dir():
        return []
    dirs = [d for d in TESTS.iterdir()
            if d.is_dir() and (d / "言語知識・読解.md").is_file()
            and (d / "聴解.md").is_file()]
    if test_id:
        dirs = [d for d in dirs if d.name == test_id]
    return sorted(dirs, key=lambda p: serve_sheet.natural_key(p.name))


def prepare_out(out: Path, force: bool) -> None:
    """Make `out` an empty build directory, refusing to eat anything else.

    A stale sheet from a deleted test would otherwise stay deployed, so the
    directory is emptied — but only when it is recognisably one of ours (it has
    the .nojekyll marker) or it is empty. Anything else needs --force, because
    `--out docs` pointed at a real folder must not silently delete it.
    """
    if out.exists():
        if not out.is_dir():
            sys.exit(f"--out {out} exists and is not a directory")
        entries = list(out.iterdir())
        if entries and not (out / MARKER).exists() and not force:
            sys.exit(f"{out} is not empty and was not built by this script "
                     f"(no {MARKER}). Pass --force to overwrite it, or pick "
                     f"another --out.")
        for p in entries:
            shutil.rmtree(p) if p.is_dir() else p.unlink()
    out.mkdir(parents=True, exist_ok=True)
    (out / MARKER).write_text("", encoding="utf-8")


def is_lfs_pointer(p: Path) -> bool:
    """True when `p` is an UNFETCHED Git LFS pointer rather than the real file.

    `*.mp3` is LFS-tracked, and CI checks out with `lfs: false` on purpose (the
    refs/ archive makes a full smudge ~3 GB per run and blew the account's LFS
    budget — .github/workflows/pages.yml carries the whole story). So in CI every
    聴解.mp3 arrives as a ~130-byte text stub. Copying one to _site/ deploys a
    player that plays nothing and a test card that claims audio it does not have,
    with every step green — so the stub is DETECTED and treated as no audio at
    all. Never "fix" this by copying it anyway.
    """
    try:
        if p.stat().st_size > 1024:      # a real MP3 is ~30 MB; a pointer ~130 B
            return False
        with p.open("rb") as fh:
            return fh.read(len(LFS_POINTER)) == LFS_POINTER
    except OSError:
        return False


def copy_audio(src: Path, dst: Path) -> int:
    """Copy the ~30 MB MP3, skipping it when the destination is already it."""
    if dst.is_file() and dst.stat().st_size == src.stat().st_size \
            and dst.stat().st_mtime >= src.stat().st_mtime:
        return 0
    shutil.copy2(src, dst)
    return src.stat().st_size


def _build_one(job: tuple[Path, Path, bool]) -> tuple[dict, int, str]:
    """Build one test into the site; returns (manifest entry, audio bytes
    copied, captured stdout). Top-level so a worker process can pickle it."""
    d, out, with_audio = job
    buf = io.StringIO()
    copied = 0
    with contextlib.redirect_stdout(buf):
        dest = out / "tests" / d.name
        # The sheet is REBUILT, never copied from tests/<id>/: that one is the
        # server build and would POST to an /api/ that does not exist on Pages.
        build_interactive.build(d, storage="local", out_dir=dest)

        model_ans = d / "模範解答.html"
        has_explanation = model_ans.is_file()
        if has_explanation:
            shutil.copy2(model_ans, dest / "模範解答.html")

        mp3 = d / AUDIO
        pointer = mp3.is_file() and is_lfs_pointer(mp3)
        has_local_audio = mp3.is_file() and not pointer
        has_audio = has_local_audio or (d / "聴解_チャプター.json").is_file()
        if has_local_audio and with_audio:
            copied += copy_audio(mp3, dest / AUDIO)
        elif has_local_audio:
            print(f"  ! {d.name}: --no-audio, local 聴解.mp3 not copied (will use remote release audio)")
        elif pointer:
            print(f"  ! {d.name}: 聴解.mp3 is an unfetched Git LFS pointer — will fallback to remote release audio")
        elif (d / "聴解_チャプター.json").is_file():
            print(f"  ! {d.name}: local 聴解.mp3 absent — will stream from GitHub Release")
        else:
            print(f"  ! {d.name}: no 聴解 audio/chapters (run make mp3 {d.name})")

    # The static half of what the list needs; the progress half comes from
    # localStorage in the page. Same field names as serve_sheet.progress_of.
    entry = {
        "id": d.name,
        "origin": serve_sheet.test_origin(d.name),
        "level": serve_sheet.level_of(d),
        "has_sheet": True,
        "has_audio": has_audio and with_audio,
        "has_explanation": has_explanation,
        # Per-test, not the era constant: an imported past paper can key a
        # different number of items (7/2021 is 72 + 30), and the static list
        # has no server to ask.
        "total": serve_sheet.question_count_of(d),
    }
    return entry, copied, buf.getvalue()


def build_site(out: Path, test_id: str | None = None, with_audio: bool = True,
               force: bool = False) -> list[dict]:
    dirs = deployable(test_id)
    if not dirs:
        sys.exit(f"no deployable tests in {TESTS}"
                 + (f" matching {test_id!r}" if test_id else "")
                 + " (each needs 言語知識・読解.md and 聴解.md)")

    prepare_out(out, force)
    # Each test is independent (its own dest folder), so they build in worker
    # processes — 40 tests took ~13 s serially, ~5 s this way. Results are
    # collected in `dirs` order, so the manifest and the log read as before.
    jobs = [(d, out, with_audio) for d in dirs]
    if len(jobs) > 1:
        with ProcessPoolExecutor() as pool:
            results = list(pool.map(_build_one, jobs))
    else:
        results = [_build_one(j) for j in jobs]
    manifest, copied = [], 0
    for entry, n_bytes, log in results:
        if log:
            print(log, end="")
        manifest.append(entry)
        copied += n_bytes

    write_portal(out, manifest)
    if copied:
        print(f"  copied {copied / 1e6:.0f} MB of audio")
    return manifest


def copy_module(out: Path, src: Path) -> int:
    """A module's built pages, `<module>/<LEVEL>/**/*.html` → `_site/<module>/…`.

    Used for the 知識 module (`knowledge/`) and the reserved ドリル module
    (`drill/`, absent until its builder lands). Only the HTML, sub-folders
    included (a split 知識 category builds one page per part under
    `<stem>/`): the pages are self-contained (their builder bakes the data in),
    and the JSON beside them is authoring source, not a deliverable."""
    n = 0
    for lv in portal_view.LEVELS:
        base = src / lv
        pages = sorted(base.rglob("*.html")) if base.is_dir() else []
        for p in pages:
            dest = out / src.name / lv / p.relative_to(base)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dest)
            n += 1
    return n


def write_portal(out: Path, manifest: list[dict]) -> None:
    """The portal's three levels of index pages — the same views `make serve`
    renders per request, baked once. Every level gets its module chooser and
    exam list, including a level with nothing yet: its cards say 準備中."""
    n_know = copy_module(out, portal_view.KNOWLEDGE)
    n_drill = copy_module(out, portal_view.DRILL)
    summaries = portal_view.level_summaries(manifest, portal_view.KNOWLEDGE, portal_view.DRILL)
    (out / portal_view.INDEX).write_text(portal_view.portal_html(summaries),
                                         encoding="utf-8")
    for s in summaries:
        lv = s["level"]
        (out / lv / portal_view.EXAM_DIR).mkdir(parents=True, exist_ok=True)
        (out / lv / portal_view.INDEX).write_text(portal_view.module_html(s),
                                                  encoding="utf-8")
        (out / lv / portal_view.EXAM_DIR / portal_view.INDEX).write_text(
            index_view.index_html("local", manifest, level=lv), encoding="utf-8")
    counts = ", ".join(f"{s['level']} {s['tests']}" for s in summaries)
    print(f"  {out / portal_view.INDEX}  (portal; tests per level: {counts}; "
          f"{n_know} knowledge page(s), {n_drill} drill page(s))")


def main():
    ap = argparse.ArgumentParser(
        description="Build the static GitHub Pages deployment of the exam app.")
    ap.add_argument("test_id", nargs="?", default=None,
                    help="deploy only this test (default: every test in tests/)")
    ap.add_argument("--out", type=Path, default=ROOT / "_site",
                    help="output directory (default: _site/)")
    ap.add_argument("--no-audio", action="store_true",
                    help="skip the 聴解.mp3 copies (fast rebuilds; player will 404)")
    ap.add_argument("--force", action="store_true",
                    help="overwrite --out even if this script did not create it")
    args = ap.parse_args()

    tests = build_site(args.out, test_id=args.test_id,
                       with_audio=not args.no_audio, force=args.force)
    size = sum(f.stat().st_size for f in args.out.rglob("*") if f.is_file())
    print(f"\nStatic site: {args.out}  ({len(tests)} test(s), {size / 1e6:.0f} MB)")
    print("Answers and results are stored in the browser (localStorage), not on disk.")
    print(f"Preview: python3 -m http.server -d {args.out} 8766   # or: make preview-pages")


if __name__ == "__main__":
    main()
