#!/usr/bin/env python3
"""Record what trough maps of Axiom Math's CFSG, from a checkout of it.

    python tools/refresh_cfsg.py CHECKOUT

CHECKOUT is a git checkout of AxiomMath/CFSG at the commit to pin. A sparse
checkout is enough: every .lean file but those under Certificates/ and
CFSG/Certificates/, with formalization.yaml, README.md, LICENSE, lean-toolchain
and lake-manifest.json. This writes data/cfsg/source.json, the commit, its date,
toolchain, Mathlib and Tau Ceti, and proof.json: the top theorem, the reduction
and the theorem its proof gives for each case; each milestone module's
declarations as trough.leansource reads them without Lean, with their Lean
statements; for each case and milestone file, the case and milestone files it
imports, directly or not, through no other; the main results; the facts of
formalization.yaml; the README's opening; and the files and theorems of each
folder.

Nothing is written when the checkout is not Apache-2.0, when a file it lists is
not checked out, when the top theorem, the reduction, a case or a main result is
not found, when a milestone module's scopes don't close, or when the milestones
drop under half the last count.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from trough import cfsg

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "cfsg"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def refresh(checkout: Path, out: Path) -> list[str]:
    """Write source.json and proof.json under *out*, or neither when there is a problem; return the problems."""
    rev = git(checkout, "rev-parse", "HEAD")
    paths = git(checkout, "ls-tree", "-r", "--name-only", "HEAD").splitlines()
    record, problems = cfsg.read(checkout, paths)
    previous = out / "proof.json"
    last = json.loads(previous.read_text(encoding="utf-8")) if previous.is_file() else None
    if record and last and len(record["milestones"]) * 2 < len(last["milestones"]):
        problems.append(f"reads {len(record['milestones'])} milestones, under half the {len(last['milestones'])} "
                        "the last record read")
    if problems:
        return problems
    manifest = checkout / "lake-manifest.json"
    mathlib, tauceti = cfsg.mathlib_and_tauceti(json.loads(manifest.read_text(encoding="utf-8"))) if manifest.is_file() else ("", "")
    toolchain = checkout / "lean-toolchain"
    source = {"repo": cfsg.REPO, "rev": rev,
              # In UTC, as git versions print %cI differently.
              "date": git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
              "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else "",
              "mathlib": mathlib, "tauceti": tauceti}
    record = {"schema": record.pop("schema"), "rev": rev, **record}
    out.mkdir(parents=True, exist_ok=True)
    (out / "source.json").write_text(json.dumps(source, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    previous.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    milestones = record["milestones"]
    declarations = [declaration for milestone in milestones for declaration in milestone["declarations"]]
    print(f"{cfsg.REPO} {rev[:8]}: {record['files']} Lean files read, {record['certificates']} certificate files "
          f"counted; {len(record['cases'])} cases of {record['reduction']['name']}; {len(milestones)} milestone modules "
          f"({sum(milestone['indexed'] for milestone in milestones)} indexed), {len(declarations)} declarations "
          f"({sum(declaration['sorry'] for declaration in declarations)} holding sorry); "
          f"{sum(len(item['depends']) for item in [*record['cases'], *milestones])} import edges; "
          f"{sum(not milestone['cases'] for milestone in milestones)} milestones reached by no case; "
          f"{len(record['main_results'])} main results", file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of AxiomMath/CFSG")
    args = parser.parse_args()
    problems = refresh(args.checkout, OUT)
    if problems:
        print("\n".join(problems) + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
