#!/usr/bin/env python3
"""Record what trough maps of Lean Pool, from a checkout of it.

    python tools/refresh_lean_pool.py CHECKOUT

CHECKOUT is a git checkout of LeanPool/lean-pool at the commit to pin. A sparse
checkout is enough: the cards in LeanPool/projects/, NOTICE.extra.yml, LICENSE,
lean-toolchain, lake-manifest.json and the .lean files under LeanPool/. This
writes data/lean-pool/source.json (the commit, its date, the Lean toolchain and
Mathlib's commit) and data/lean-pool/projects.json: each card's title, summary,
authors, sources, license, provenance and MSC2020 codes, the note (its copyright
line, or a remark about it) NOTICE.extra.yml keeps for a project published under
MIT, and each main result with the module, line and kind of its declaration as
trough.leansource reads the project's files without Lean.

Nothing is written when the repository is not Apache-2.0, a card is not as the
chapter reads it or names an entry module the checkout lacks, or the main
results the scan places drop under half of those the last record placed.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

import yaml

from trough import lean_pool

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "lean-pool"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def refresh(checkout: Path, out: Path) -> list[str]:
    """Write the two records under *out*, or neither when there is a problem; return the problems."""
    try:
        rev = git(checkout, "rev-parse", "HEAD")
        # In UTC, as git versions print %cI differently.
        date = git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD")
        source, record, counts = lean_pool.read_pool(checkout, rev, date)
    except (ValueError, OSError, yaml.YAMLError, subprocess.CalledProcessError) as error:
        return [str(error)]
    previous = out / "projects.json"
    if previous.is_file():
        try:
            before = lean_pool.found_count(json.loads(previous.read_text(encoding="utf-8")))
        except (ValueError, KeyError, TypeError) as error:
            return [f"{previous.name}, the last record, does not read: {error!r}"]
        after = lean_pool.found_count(record)
        if after * 2 < before:
            return [f"places {after} main results, under half the {before} the last record placed"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "source.json").write_text(json.dumps(source, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "projects.json").write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    results = [(project["slug"], result) for project in record["projects"] for result in project["main_results"]]
    main = [(slug, result) for slug, result in results if result["main"]]
    print(f"lean-pool {rev[:8]}: {len(record['projects'])} cards; {lean_pool.found_count(record)} of {len(results)} "
          f"main results placed, {sum(1 for _, result in main if result['module'])} of {len(main)} main declarations; "
          f"{counts['files_read']} files read, {counts['files_unclosed']} with scopes that don't close, "
          f"{counts['declared_twice']} names declared in two files", file=sys.stderr)
    for slug, result in main:
        if not result["module"]:
            print(f"  main declaration not placed: {slug}: {result['declaration']}", file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of LeanPool/lean-pool")
    args = parser.parse_args()
    problems = refresh(args.checkout, OUT)
    if problems:
        print("\n".join(problems) + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
