#!/usr/bin/env python3
"""Record what trough maps of the Analysis I companion, from a checkout of it.

    python tools/refresh_analysis.py CHECKOUT

CHECKOUT is a git checkout of teorth/analysis at the commit to pin. A sparse
checkout is enough: Analysis/ (its .lean files and the measure theory README),
literate.toml, README.md, LICENSE, lean-toolchain and the lake files. This
writes data/analysis/source.json, the commit, its date, toolchain and Mathlib,
and sections.json: each section module of the two books, Analysis I in
literate.toml's order and the measure theory book in its numbering, with its
title, module docstring and the section modules it imports, and its labelled
items in file order, each with the declarations carrying its label as
trough.leansource reads them without Lean; the chapter titles the READMEs give;
and the repository's other modules, by title.

Nothing is written when the checkout is not Apache-2.0, when literate.toml
names a module the checkout lacks, or when the labelled declarations drop
under half of those the last record kept.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from trough import analysis, ff

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "analysis"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True).stdout.strip()


def kept(sections: list[dict]) -> int:
    return sum(len(item["declarations"]) for section in sections for item in section["items"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of teorth/analysis")
    args = parser.parse_args()
    checkout = args.checkout
    rev = git(checkout, "rev-parse", "HEAD")
    paths = sorted(path for path in git(checkout, "ls-tree", "-r", "--name-only", "HEAD", "--", "Analysis").splitlines()
                   if path.endswith(".lean"))
    license_file = checkout / "LICENSE"
    refusals = []
    if not license_file.is_file() or not ff.is_apache(license_file.read_text(encoding="utf-8")):
        refusals.append(f"{analysis.REPO} at {rev[:8]}: its LICENSE is not Apache-2.0")
    for name in (analysis.LITERATE, analysis.README, analysis.MT_README, "lake-manifest.json"):
        if not (checkout / name).is_file():
            refusals.append(f"{name} is not checked out")
    missing = [path for path in paths if not (checkout / path).is_file()]
    if missing:
        refusals.append(f"{len(missing)} files are not checked out, such as {missing[0]}")
    if refusals:
        print("\n".join(refusals) + "\nnothing written", file=sys.stderr)
        return 1
    record = analysis.read(checkout, paths)
    if record["missing"]:
        print(f"literate.toml names {len(record['missing'])} modules with no file, such as {record['missing'][0]}\n"
              "nothing written", file=sys.stderr)
        return 1
    del record["missing"]
    previous = OUT / "sections.json"
    if previous.is_file():
        before = kept(json.loads(previous.read_text(encoding="utf-8"))["sections"])
        if kept(record["sections"]) * 2 < before:
            print(f"keeps {kept(record['sections'])} labelled declarations, under half the {before} the last record "
                  "kept\nnothing written", file=sys.stderr)
            return 1
    manifest = json.loads((checkout / "lake-manifest.json").read_text(encoding="utf-8"))
    mathlib = next((package["rev"] for package in manifest.get("packages", []) if package.get("name") == "mathlib"), "")
    toolchain = checkout / "lean-toolchain"
    source = {"repo": analysis.REPO, "rev": rev, "date": git(checkout, "log", "-1", "--format=%cI", "HEAD"),
              "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else "",
              "mathlib": mathlib}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "source.json").write_text(json.dumps(source, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    previous.write_text(json.dumps({"schema": analysis.SCHEMA, "rev": rev, **record}, indent=1, ensure_ascii=False)
                        + "\n", encoding="utf-8")
    tally = analysis.counts(record["sections"])
    print(f"{analysis.REPO} {rev[:8]}: " + "; ".join(
        f"{analysis.BOOKS[book]}: {tally[f'{book} sections']} sections, {tally[f'{book} items']} labelled items, "
        f"{tally[f'{book} declarations']} declarations" for book in analysis.BOOKS)
        + f"; {len(record['others'])} other modules", file=sys.stderr)
    for key in sorted(key for key in tally if key.count(" ") >= 2 and not key.endswith(("sections", "items", "declarations"))):
        print(f"  {key}: {tally[key]}", file=sys.stderr)
    for section in record["sections"]:
        for unread in section["unread"]:
            print(f"  not read: {section['file']}:{unread['line']} {unread['label']}: {unread['why']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
