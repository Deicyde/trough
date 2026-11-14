#!/usr/bin/env python3
"""Record what trough maps of Physlib, from a checkout of it.

    python tools/refresh_physlib.py CHECKOUT

CHECKOUT is a git checkout of leanprover-community/physlib at the commit to pin. A sparse checkout is enough: the
.lean files and API-map.md files under Physlib/, PhyslibAlpha/ and QuantumInfo/, with README.md, LICENSE,
lean-toolchain, lake-manifest.json and scripts/lint/exemptions/Theorems.txt. This writes data/physlib/source.json
(the commit, its date, toolchain and Mathlib, the README's words on the project, the significant results
Theorems.txt lists and the counts), api-maps.json (each API map's title, content, Lean references and literature
references) and modules/<library>.<area>.json, the modules of each area: each module's title, module docstring and
section docstrings, and its declarations as trough.leansource reads them without Lean, with their docstrings and
Lean statements. lean/physlib/PhyslibDeps.lean, run by the data workflow, then writes deps.json.

Nothing is written when the repository is not Apache-2.0, when a file the commit lists is not checked out, when a
module's scopes don't close as they open, when the README no longer describes each library, or when the
declarations drop under half of those the last record has.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

from trough import physlib

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "physlib"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True,
                          env={**os.environ, "TZ": "UTC"}).stdout.strip()


def last_modules(out: Path) -> list[dict]:
    return [module for shard in sorted((out / "modules").glob("*.json"))
            for module in json.loads(shard.read_text(encoding="utf-8"))["modules"]]


def refresh(checkout: Path, out: Path) -> list[str]:
    """Write source.json, api-maps.json and the module records under *out*, or nothing when there is a problem;
    return the problems."""
    rev = git(checkout, "rev-parse", "HEAD")
    paths = git(checkout, "ls-tree", "-r", "--name-only", "HEAD").splitlines()
    record, problems = physlib.read(checkout, paths)
    if record:
        count, last = physlib.mapped(record["modules"]), physlib.mapped(last_modules(out)) if (out / "modules").is_dir() else 0
        if count * 2 < last:
            problems.append(f"reads {count:,} declarations, under half the {last:,} the last record read")
    if problems:
        return problems
    manifest = checkout / "lake-manifest.json"
    mathlib = next((package for package in json.loads(manifest.read_text(encoding="utf-8")).get("packages", [])
                    if package.get("name") == "mathlib"), {}) if manifest.is_file() else {}
    toolchain = checkout / "lean-toolchain"
    modules = record["modules"]
    counts: Counter = Counter()
    for module in modules:
        library = module["file"].split("/")[0]
        counts[f"files_{library}"] += 1
        counts[f"declarations_{library}"] += sum(bool(declaration["name"]) for declaration in module["declarations"])
        counts[f"instances_{library}"] += sum(not declaration["name"] for declaration in module["declarations"])
        counts[f"documented_{library}"] += sum(bool(declaration["doc"]) for declaration in module["declarations"])
        counts[f"private_{library}"] += module["private"]
    source = {
        "repo": physlib.REPO, "rev": rev,
        # In UTC, as git versions print %cI differently.
        "date": git(checkout, "log", "-1", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "--format=%cd", "HEAD"),
        "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else "",
        "mathlib": mathlib.get("rev", ""), "mathlib_version": mathlib.get("inputRev", ""),
        "license": record["license"], "readme": record["readme"], "theorems": record["theorems"],
        "counts": dict(sorted(counts.items())),
    }
    shards: dict[str, list[dict]] = {}
    for module in modules:
        shards.setdefault(physlib.shard(module["file"]), []).append(module)
    (out / "modules").mkdir(parents=True, exist_ok=True)
    for stale in (out / "modules").glob("*.json"):
        if stale.stem not in shards:
            stale.unlink()
    for name, items in shards.items():
        (out / "modules" / f"{name}.json").write_text(
            json.dumps({"schema": physlib.SCHEMA, "rev": rev, "modules": items}, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
    maps = {"schema": physlib.SCHEMA, "rev": rev, "api_maps": record["api_maps"]}
    for name, value in (("source.json", source), ("api-maps.json", maps)):
        (out / name).write_text(json.dumps(value, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    listed = {name for names in record["theorems"].values() for name in names}
    found = {declaration["name"] for module in modules for declaration in module["declarations"]} & listed
    print(f"{physlib.REPO} {rev[:8]}: {len(modules)} modules, {physlib.mapped(modules)} declarations ("
          + ", ".join(f"{count} {key}" for key, count in sorted(counts.items()))
          + f"); {len(record['api_maps'])} API maps; {len(found)} of the {len(listed)} names Theorems.txt lists found",
          file=sys.stderr)
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("checkout", type=Path, help="a checkout of leanprover-community/physlib")
    args = parser.parse_args()
    problems = refresh(args.checkout, OUT)
    if problems:
        shown = problems[:200]
        print("\n".join(shown) + (f"\n... and {len(problems) - len(shown)} more" if len(problems) > len(shown) else "")
              + "\nnothing written", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
