#!/usr/bin/env python3
"""Record which Tau Ceti declarations trough maps, from a TauCetiRoadmap checkout.

    python tools/refresh_tauceti.py /path/to/TauCetiRoadmap-checkout

writes data/tauceti/roadmaps.json: each roadmap with a STATUS.md, its title from
its README, and the declarations its STATUS.md links under "Named results" and
"Notable definitions and infrastructure". Nothing else is kept. STATUS.md is
written by a model, and TauCetiProgress says its prose is not validated, so it
only picks the declarations; the Tau Ceti data workflow then reads each one at
the pinned Tau Ceti commit, and a name that does not resolve there has no
article.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from trough import tauceti

OUT = Path(__file__).resolve().parent.parent / "data" / "tauceti" / "roadmaps.json"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True).stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a TauCetiRoadmap checkout")
    args = parser.parse_args()
    roadmaps = tauceti.read_roadmaps(args.checkout)
    if not roadmaps:
        print(f"{args.checkout} has no roadmap with a STATUS.md; nothing written", file=sys.stderr)
        return 1
    data = {
        "schema": tauceti.ROADMAPS_SCHEMA,
        "repo": tauceti.ROADMAP_REPO,
        "rev": git(args.checkout, "rev-parse", "HEAD"),
        "date": git(args.checkout, "log", "-1", "--format=%cI", "HEAD"),
        "roadmaps": roadmaps,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    names = {name for roadmap in roadmaps for name in roadmap["names"]}
    print(f"{len(roadmaps)} roadmaps name {len(names)} declarations", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
