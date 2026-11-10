#!/usr/bin/env python3
"""Record what trough maps of the Formal Frontier libraries, from a checkout of each.

    python tools/refresh_ff.py CHECKOUTS

CHECKOUTS holds a git checkout of every Formal Frontier library in the catalog,
each in a directory named after its repository, at the commit to pin. A sparse
checkout is enough: the README, formalization.yaml, lake-manifest.json,
lean-toolchain, LICENSE and the .lean files. For each library this writes
data/ff/<name>.json: the commit, the yaml's facts, highlights and main results,
the README's headline results, and for each declaration they name the line,
kind and whether its text in the file holds `sorry`, as trough.leansource reads
the file without Lean.

Nothing is written when a library is not Apache-2.0, or when the declarations
a library's record finds drop under half of those its last record found.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

import yaml

from trough import catalog, ff

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "ff"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def refresh(checkouts: Path, libraries: list[dict], out: Path) -> list[str]:
    """Write a record for each library under *out*, or none when any library has a problem; return the problems."""
    records, problems = {}, []
    for library in libraries:
        name = library["repo"].split("/")[1]
        checkout = checkouts / name
        if not checkout.is_dir():
            problems.append(f"{name}: no checkout at {checkout}")
            continue
        try:
            rev = git(checkout, "rev-parse", "HEAD")
            # In UTC, as git versions print %cI differently.
            date = git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD")
            paths = set(git(checkout, "ls-tree", "-r", "--name-only", "HEAD").splitlines())
            record = ff.read_library(checkout, name, rev, date, paths)
        except (ValueError, OSError, yaml.YAMLError, subprocess.CalledProcessError) as error:
            problems.append(f"{name}: {error}")
            continue
        previous = out / f"{name}.json"
        if previous.is_file():
            before = len(ff.found_names(json.loads(previous.read_text(encoding="utf-8"))))
            after = len(ff.found_names(record))
            if after * 2 < before:
                problems.append(f"{name}: finds {after} declarations, under half the {before} its last record found")
        records[name] = record
    if problems:
        return problems
    out.mkdir(parents=True, exist_ok=True)
    for name, record in records.items():
        (out / f"{name}.json").write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        named = [item for highlight in record["highlights"] for item in highlight["declarations"]]
        named += [item["declaration"] for item in record["headlines"] if item.get("declaration")]
        named += record["main_results"]
        found = sum(1 for item in named if item["found"])
        print(f"{name} {record['rev'][:8]}: {len(record['highlights'])} highlights, "
              f"{sum(item['kind'] == 'item' for item in record['headlines'])} headline items, "
              f"{len(record['main_results'])} main results; {found} of {len(named)} named declarations found",
              file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkouts", type=Path, help="a directory with a checkout of each library")
    args = parser.parse_args()
    libraries = [library for library in catalog.load(ROOT / "catalog" / "libraries.toml")
                 if library["group"] == "formal-frontier"]
    problems = refresh(args.checkouts, libraries, OUT)
    if problems:
        print("\n".join(problems) + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
