#!/usr/bin/env python3
"""Record what trough maps of Anthropic's Lean proof of Fermat's Last Theorem, from a checkout.

    python tools/refresh_anthropic_flt.py CHECKOUT [--docs URL]
    python tools/refresh_anthropic_flt.py CHECKOUT --files

CHECKOUT is a git checkout of anthropics/fermats-last-theorem at the commit to
pin. A sparse checkout is enough: PROOF-PATH.md, formalization.yaml,
html/data/meta.js and edges.js, lean-toolchain, lake-manifest.json and LICENSE,
then the files --files lists once those are checked out: the landmarks'
statement files and the main results' files. This writes
data/anthropic-flt/source.json (the commit, the formalization.yaml's facts and
PROOF-PATH.md's steps) and landmarks.json (each landmark's stage, aliases and
Lean statement, and the nearest landmarks its proof reaches). With --docs, the
record links the repository's documentation site at URL when the site serves
the landmarks' pages; when the site does not answer at all, the last record's
link is kept, so an outage does not change the data.

Nothing is written when the repository is not Apache-2.0, when a file the
refresh reads is in the commit but not in the checkout, when a landmark's
statement file states another theorem or may be cut short, or when the
landmarks drop under half of those the last record has.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

from trough import anthropic_flt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "anthropic-flt"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def fetch(url: str, method: str, attempts: int = 3, wait: float = 10.0) -> bytes | None:
    """The body of a GET, b"" for a HEAD that answers, None when the site answers that it has no such page.
    A request the site does not answer, or answers with a server error, is tried *attempts* times, then
    raises anthropic_flt.Unreachable."""
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method=method), timeout=60) as response:
                return response.read() if method == "GET" else b""
        except urllib.error.HTTPError as error:
            if error.code < 500:
                return None
        except (urllib.error.URLError, OSError):
            pass
        if attempt + 1 < attempts:
            time.sleep(wait)
    raise anthropic_flt.Unreachable(url)


def refresh(checkout: Path, out: Path, docs: str | None = None, fetcher=fetch) -> list[str]:
    """Write the two records under *out*, or none when there is a problem; return the problems."""
    try:
        rev = git(checkout, "rev-parse", "HEAD")
        # In UTC, as git versions print %cI differently.
        date = git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD")
        paths = set(git(checkout, "ls-tree", "-r", "--name-only", "HEAD").splitlines())
        source, landmarks = anthropic_flt.read_repository(checkout, rev, date, paths)
    except (ValueError, OSError, KeyError, yaml.YAMLError, subprocess.CalledProcessError) as error:
        return [str(error)]
    previous = out / "landmarks.json"
    if previous.is_file():
        before = len(json.loads(previous.read_text(encoding="utf-8"))["landmarks"])
        after = len(landmarks["landmarks"])
        if after * 2 < before:
            return [f"{after} landmarks, under half the {before} of the last record"]
    if docs:
        try:
            problem = anthropic_flt.docs_problem(docs, landmarks, fetcher)
        except anthropic_flt.Unreachable as error:
            last = out / "source.json"
            kept = json.loads(last.read_text(encoding="utf-8")).get("docs") if last.is_file() else None
            print(f"The documentation site does not answer at {error}; "
                  + ("keeping the last record's link." if kept == docs else "not linking it."), file=sys.stderr)
            if kept == docs:
                source["docs"] = docs
        else:
            if problem:
                print(f"Not linking the documentation site: {problem}", file=sys.stderr)
            else:
                source["docs"] = docs
    out.mkdir(parents=True, exist_ok=True)
    for name, record in (("source.json", source), ("landmarks.json", landmarks)):
        (out / name).write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    counts = landmarks["counts"]
    print(f"{rev[:8]}: {counts['landmarks']} landmarks of {counts['theorems']} theorems, {counts['landmark_edges']} "
          f"edges between them of {counts['edges']}" + (f"; documentation at {source['docs']}" if "docs" in source else ""),
          file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of anthropics/fermats-last-theorem")
    parser.add_argument("--docs", help="the documentation site's address, ending in /, to link when it serves the pages")
    parser.add_argument("--files", action="store_true",
                        help="list the landmarks' statement files and the main results' files, and stop")
    args = parser.parse_args()
    if args.files:
        print("\n".join(anthropic_flt.files_to_read(args.checkout)))
        return 0
    problems = refresh(args.checkout, OUT, args.docs)
    if problems:
        print("\n".join(problems) + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
