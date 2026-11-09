#!/usr/bin/env python3
"""Record what trough maps of Formal Conjectures, from a checkout of it.

    python tools/refresh_formal_conjectures.py CHECKOUT

CHECKOUT is a git checkout of google-deepmind/formal-conjectures at the commit
to pin. A sparse checkout is enough: FormalConjectures/,
FormalConjecturesUtil/Attributes/AMS.lean, lean-toolchain and LICENSE. This
writes data/formal-conjectures/source.json, the commit, its date and toolchain,
and problems.json: each problem file's title and module docstring, its research
and textbook statements as trough.leansource reads them without Lean, and its
counts of test and API statements; the FC100 lists; and the names Formal
Conjectures gives the AMS subject codes.

Nothing is written when the checkout is not Apache-2.0, when it gives no subject
names, when a file it lists is not checked out, when a categorized declaration
does not read (a file whose scopes don't close counts as one), or when the
statements kept drop under half of those the last record kept.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

from trough import ff
from trough import formal_conjectures as fc

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "formal-conjectures"
AMS_FILE = "FormalConjecturesUtil/Attributes/AMS.lean"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def kept(problems: list[dict]) -> int:
    return sum(len(problem["statements"]) for problem in problems)


def refresh(checkout: Path, out: Path) -> list[str]:
    """Write source.json and problems.json under *out*, or neither when there is a problem; return the problems."""
    rev = git(checkout, "rev-parse", "HEAD")
    paths = sorted((path for path in git(checkout, "ls-tree", "-r", "--name-only", "HEAD", "--", fc.ROOT).splitlines()
                    if path.endswith(".lean")), key=fc.natural)
    problems = []
    license_file = checkout / "LICENSE"
    if not license_file.is_file() or not ff.is_apache(license_file.read_text(encoding="utf-8")):
        problems.append(f"{fc.REPO} at {rev[:8]}: its LICENSE is not Apache-2.0")
    subjects = fc.subjects((checkout / AMS_FILE).read_text(encoding="utf-8")) if (checkout / AMS_FILE).is_file() else {}
    if not subjects:
        problems.append(f"{AMS_FILE} gives no subject names")
    missing = [path for path in paths if not (checkout / path).is_file()]
    if missing:
        problems.append(f"not checked out: {missing[0]}"
                        + (f" and {len(missing) - 1:,} other files" if len(missing) > 1 else ""))
    if problems:
        return problems
    records, subsets = fc.read(checkout, paths)
    problems += [f"{record['file']}:{item['line']} {item['name'] or '(the file)'}: {item['why']}"
                 for record in records for item in record["unread"]]
    previous = out / "problems.json"
    if previous.is_file():
        before = kept(json.loads(previous.read_text(encoding="utf-8"))["problems"])
        if kept(records) * 2 < before:
            problems.append(f"keeps {kept(records)} statements, under half the {before} the last record kept")
    if problems:
        return problems
    toolchain = checkout / "lean-toolchain"
    source = {"repo": fc.REPO, "rev": rev,
              # In UTC, as git versions print %cI differently.
              "date": git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
              "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else ""}
    record = {"schema": fc.SCHEMA, "rev": rev, "subjects": subjects, "problems": records, "subsets": subsets}
    out.mkdir(parents=True, exist_ok=True)
    (out / "source.json").write_text(json.dumps(source, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    previous.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    categories = Counter(statement["category"] for problem in records for statement in problem["statements"])
    print(f"{fc.REPO} {rev[:8]}: {len(records)} problem files, {sum(1 for problem in records if problem['statements'])} "
          f"with a kept statement; {kept(records)} statements kept ("
          + ", ".join(f"{count} {category}" for category, count in sorted(categories.items()))
          + f"); {sum(problem['folded']['test'] for problem in records)} test and "
          f"{sum(problem['folded']['api'] for problem in records)} API statements counted; {len(subsets)} FC100 lists "
          f"naming {sum(len(subset['names']) for subset in subsets)} statements, "
          f"{sum(1 for subset in subsets for item in subset['names'] if not item['file'])} not found", file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of google-deepmind/formal-conjectures")
    args = parser.parse_args()
    problems = refresh(args.checkout, OUT)
    if problems:
        print("\n".join(problems) + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
