#!/usr/bin/env python3
"""Record what trough maps of CSLib, from a checkout of it.

    python tools/refresh_cslib.py CHECKOUT

CHECKOUT is a git checkout of leanprover/cslib at the commit to pin. A sparse
checkout is enough: the .lean and README.md files under Cslib/, with README.md,
GOVERNANCE.md, LICENSE, lean-toolchain and lake-manifest.json. This writes
data/cslib/source.json, the commit, its date, toolchain and Mathlib, and
library.json: each module's title, module docstring and later `/-!` notes as written, the
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
import sys
from pathlib import Path

from trough import cslib, library

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "cslib"


def refresh(checkout: Path, out: Path) -> list[str]:
    """Write source.json and library.json under *out*, or neither when there is a problem; return the problems."""
    return library.refresh(cslib.CSLIB, checkout, out)


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
