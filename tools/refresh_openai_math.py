#!/usr/bin/env python3
"""Record what trough maps of OpenAI Math, from a checkout.

    python tools/refresh_openai_math.py CHECKOUT
    python tools/refresh_openai_math.py --files CHECKOUT

CHECKOUT is a git checkout of openai/math at the commit to pin; a sparse
checkout is enough: CONTENTS.md, overview.tex, LICENSE, lean/docs/,
lean/ComparatorChallenges/, lean/formalization.yaml, lean/lean-toolchain,
lean/lake-manifest.json, and the Lean files --files prints. Those are the
solution modules the statement files' configurations name and, once those are
checked out, the OAI modules they import, so a sparse checkout adds them in two
rounds. This writes data/openai-math/source.json (the commit, its date,
toolchain, Mathlib and the counts), structure.json (the subjects and their
families in order) and families/<subject>.json, each family's description,
manuscripts and Lean page, with each formalized result's statements as the
statement file writes them and where the repository's Lean proves them.

Nothing is written when the license is not Apache-2.0, when CONTENTS.md,
overview.tex, a family's Lean page, a statement file or a configuration does
not read or does not match the others, or when the families drop under half of
those the last record has.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from trough import atlas, openai_math
from trough.vault import slugify

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "openai-math"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def last_numbers(out: Path) -> set[str]:
    return {family["number"] for shard in sorted((out / "families").glob("*.json"))
            for family in json.loads(shard.read_text(encoding="utf-8"))["families"]}


def refresh(checkout: Path, out: Path) -> list[str]:
    """Write source.json, structure.json and the family records under *out*, or nothing when there is a problem;
    return the problems."""
    rev = git(checkout, "rev-parse", "HEAD")
    license_file = checkout / "LICENSE"
    notice = atlas.license_notice(license_file.read_text(encoding="utf-8")) if license_file.is_file() else None
    if notice is None:
        return [f"{openai_math.REPO} at {rev[:8]}: its LICENSE is not Apache-2.0"]
    structure, families, counts, problems = openai_math.read(checkout)
    previous = last_numbers(out) if (out / "families").is_dir() else set()
    numbers = {family["number"] for records in families.values() for family in records}
    if not problems and not numbers:
        problems.append(f"{openai_math.REPO} at {rev[:8]}: CONTENTS.md lists no families")
    if len(numbers) * 2 < len(previous):
        problems.append(f"{len(numbers)} families, under half the {len(previous)} of the last record")
    if problems:
        return problems
    manifest = checkout / "lean" / "lake-manifest.json"
    mathlib = next((package for package in json.loads(manifest.read_text(encoding="utf-8")).get("packages", [])
                    if package.get("name") == "mathlib"), {}) if manifest.is_file() else {}
    toolchain = checkout / "lean" / "lean-toolchain"
    source = {
        "repo": openai_math.REPO, "rev": rev,
        # In UTC, as git versions print %cI differently.
        "date": git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
        "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else "",
        "mathlib": mathlib.get("rev", ""), "mathlib_version": mathlib.get("inputRev", ""),
        "license": "Apache-2.0", "counts": counts,
    }
    structure = {"schema": openai_math.SCHEMA, "repo": openai_math.REPO, "rev": rev, **structure}
    (out / "families").mkdir(parents=True, exist_ok=True)
    shards = {slugify(subject): records for subject, records in families.items()}
    for stale in (out / "families").glob("*.json"):
        if stale.stem not in shards:
            stale.unlink()
    for name, records in shards.items():
        (out / "families" / f"{name}.json").write_text(
            json.dumps({"schema": openai_math.SCHEMA, "rev": rev, "families": records}, indent=1, ensure_ascii=False)
            + "\n", encoding="utf-8")
    for name, record in (("source.json", source), ("structure.json", structure)):
        (out / name).write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{openai_math.REPO} {rev[:8]}: " + ", ".join(f"{count} {key}" for key, count in counts.items()),
          file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of openai/math")
    parser.add_argument("--files", action="store_true", help="print the Lean files to add to a sparse checkout")
    args = parser.parse_args()
    if args.files:
        print("\n".join(openai_math.solution_files(args.checkout)))
        return 0
    problems = refresh(args.checkout, OUT)
    if problems:
        shown = problems[:200]
        print("\n".join(shown) + (f"\n... and {len(problems) - len(shown)} more" if len(problems) > len(shown) else "")
              + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
