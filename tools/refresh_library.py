#!/usr/bin/env python3
"""Record what trough maps of a Lean library, from a checkout of it.

    python tools/refresh_library.py LIBRARY CHECKOUT

LIBRARY is the id of a library trough.library reads (aesop, batteries, cedar, comppoly, cslib); CHECKOUT is a git checkout of its
repository at the commit to pin. This writes data/LIBRARY/source.json, the commit, its date, toolchain and
Mathlib, and library.json: each module's title, module docstring and later `/-!` notes as written, the authors its
header names, and its declarations as trough.leansource reads them without Lean, each with its kind, line,
docstring and statement; the opening paragraphs of the READMEs in its folders; and what the library's own module
records besides. The data workflow then runs lean/library/LibraryDeps.lean, or the library's own dump, for
deps.json.

Nothing is written when the checkout is not Apache-2.0, when a file it lists is not checked out, when a module's
scopes don't close, or when the declarations drop under half the last record's.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from trough import aesop, batteries, cedar, comppoly, cslib, library

ROOT = Path(__file__).resolve().parent.parent
LIBRARIES = {value.id: value for value in (aesop.AESOP, batteries.BATTERIES, cedar.CEDAR, comppoly.COMPPOLY, cslib.CSLIB)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("library", choices=sorted(LIBRARIES), help="the library to read")
    parser.add_argument("checkout", type=Path, help="a checkout of its repository")
    args = parser.parse_args()
    problems = library.refresh(LIBRARIES[args.library], args.checkout, ROOT / "data" / args.library)
    if problems:
        print("\n".join(problems) + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
