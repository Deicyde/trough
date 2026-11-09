#!/usr/bin/env python3
"""Choose the Tau Ceti declarations whose docstrings name a result, from a survey of the library.

    python tools/select_tauceti.py survey.jsonl

reads lean/tauceti/TauCetiSurvey.lean's output, one declaration per line, and writes
data/tauceti/selection.json: each chosen declaration with the test that chose it, and the
propositions some of them are stated from (tools/trough/tauceti_select.py has the rules). The Tau
Ceti data workflow runs it at the pinned commit, then reads the chosen declarations together with
those the roadmaps' statuses name.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from trough import tauceti_select

DATA = Path(__file__).resolve().parent.parent / "data" / "tauceti"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("survey", type=Path, help="lean/tauceti/TauCetiSurvey.lean's output")
    args = parser.parse_args()
    with args.survey.open(encoding="utf-8") as lines:
        rows = [json.loads(line) for line in lines if line.strip()]
    if not rows:
        print(f"{args.survey} holds no declarations; nothing written", file=sys.stderr)
        return 1
    chosen, assuming = tauceti_select.select(rows)
    source = json.loads((DATA / "source.json").read_text(encoding="utf-8"))
    data = {
        "schema": tauceti_select.SELECTION_SCHEMA,
        "tauceti_rev": source["rev"],
        "surveyed": len(rows),
        "chosen": chosen,
        "assuming": assuming,
    }
    (DATA / "selection.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    tests = ", ".join(f"{count} {test}" for test, count in Counter(chosen.values()).most_common())
    print(f"{len(chosen)} of {len(rows)} declarations chosen: {tests}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
