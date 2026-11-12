#!/usr/bin/env python3
"""Record what trough maps of CSLib, from a checkout of it.

    python tools/refresh_cslib.py CHECKOUT

CHECKOUT is a git checkout of leanprover/cslib at the commit to pin. A sparse
checkout is enough: the .lean and README.md files under Cslib/, with README.md,
GOVERNANCE.md, LICENSE, lean-toolchain and lake-manifest.json. This writes
data/cslib/source.json, the commit, its date, toolchain and Mathlib, and
library.json: each module's title, module docstring and later `/-!` notes, the
authors its header names, and its public declarations as trough.leansource
reads them without Lean, each with its kind, line, docstring and statement; the
area READMEs without their plans; the README's description; and the
maintainers GOVERNANCE.md names.

Nothing is written when the checkout is not Apache-2.0, when a file it lists is
not checked out, when a module's scopes don't close, or when the declarations
drop under half the last record's.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from trough import cslib

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "cslib"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def refresh(checkout: Path, out: Path) -> list[str]:
    """Write source.json and library.json under *out*, or neither when there is a problem; return the problems."""
    rev = git(checkout, "rev-parse", "HEAD")
    paths = git(checkout, "ls-tree", "-r", "--name-only", "HEAD").splitlines()
    record, problems = cslib.read(checkout, paths)
    previous = out / "library.json"
    last = json.loads(previous.read_text(encoding="utf-8")) if previous.is_file() else None
    if record and last:
        now, before = cslib.counts(record["modules"])["declarations"], cslib.counts(last["modules"])["declarations"]
        if now * 2 < before:
            problems.append(f"reads {now} declarations, under half the {before} the last record read")
    if problems:
        return problems
    manifest = json.loads((checkout / "lake-manifest.json").read_text(encoding="utf-8"))
    mathlib = next((package.get("rev", "") for package in manifest.get("packages", []) if package.get("name") == "mathlib"), "")
    source = {"repo": cslib.REPO, "rev": rev,
              # In UTC, as git versions print %cI differently.
              "date": git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
              "toolchain": (checkout / "lean-toolchain").read_text(encoding="utf-8").strip().split(":")[-1],
              "mathlib": mathlib, "license": "Apache-2.0"}
    record = {"schema": record.pop("schema"), "rev": rev, **record}
    out.mkdir(parents=True, exist_ok=True)
    (out / "source.json").write_text(json.dumps(source, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    previous.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    tally = cslib.counts(record["modules"])
    print(f"{cslib.REPO} {rev[:8]}: {len(record['modules'])} modules, {tally['declarations']} public declarations "
          f"({tally['documented']} documented, {tally['sorry']} holding sorry), "
          f"{sum(1 for module in record['modules'] if module['title'])} modules titled by their docstrings, "
          f"{len(record['folders'])} folder READMEs", file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of leanprover/cslib")
    args = parser.parse_args()
    problems = refresh(args.checkout, OUT)
    if problems:
        print("\n".join(problems) + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
