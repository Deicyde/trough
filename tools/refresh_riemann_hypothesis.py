#!/usr/bin/env python3
"""Record what trough maps of leanprover-community/riemann-hypothesis, from a checkout of it.

    python tools/refresh_riemann_hypothesis.py CHECKOUT [--evidence FILE] [--changes FILE]

CHECKOUT is a git checkout of the repository at the commit to pin. This writes data/riemann-hypothesis/: source.json,
folders.json, scan.json and verification.json (see trough.riemann_hypothesis). When verification.json records a
passing Comparator run, FILE is the file it names, as fetched at the commit it names; the refresh checks it.

When the verification folder gains or loses a file, or its notes' Results section changes, the refresh still writes
the data, keeps Comparator's status, and writes what changed to the --changes file, one line each.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from trough import riemann_hypothesis

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of the repository")
    parser.add_argument("--evidence", type=Path, help="the file a recorded passing run names, at its commit")
    parser.add_argument("--changes", type=Path, help="where to write how the verification folder changed")
    args = parser.parse_args()
    problems, changes = riemann_hypothesis.refresh(args.checkout, ROOT / "data" / riemann_hypothesis.ID, args.evidence)
    if problems:
        print("\n".join(problems) + "\nnothing written", file=sys.stderr)
        return 1
    if args.changes and changes:
        args.changes.write_text("".join(f"{line}\n" for line in changes), encoding="utf-8")
    for line in changes:
        print(f"verification folder: {line}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
