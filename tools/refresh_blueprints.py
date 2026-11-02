#!/usr/bin/env python3
"""Refresh a library's blueprint sources in data/blueprints/<id>/ from a checkout.

    python tools/refresh_blueprints.py pfr /path/to/pfr-checkout
    python tools/refresh_blueprints.py strongpnt /path/to/checkout --repo math-inc/strongpnt \\
        --entry blueprint/src/web.tex --no-text

The first refresh of a library needs --repo and --entry; later ones read them
from its source.json. With text (the default) the TeX files the blueprint
reads are copied into src/, with the repository's LICENSE. With --no-text, for
a library whose text trough may not reproduce, only structure.json is written:
titles, labels, Lean names, marks and places.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from trough import blueprints, leanblueprint

DATA = Path(__file__).resolve().parent.parent / "data" / "blueprints"


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True).stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("id")
    parser.add_argument("checkout", type=Path)
    parser.add_argument("--repo", help="owner/name on GitHub")
    parser.add_argument("--entry", help="the blueprint's web entry file, as a path in the repository")
    parser.add_argument("--license", help="the license's SPDX name, or none")
    parser.add_argument("--no-text", dest="text", action="store_false", default=None)
    parser.add_argument("--text", dest="text", action="store_true")
    args = parser.parse_args()

    directory = DATA / args.id
    source_file = directory / "source.json"
    previous = json.loads(source_file.read_text(encoding="utf-8")) if source_file.is_file() else {}
    repo = args.repo or previous.get("repo")
    entry = args.entry or previous.get("entry")
    if not repo or not entry:
        parser.error(f"{args.id} has no source.json yet: give --repo and --entry")
    text = args.text if args.text is not None else previous.get("text", True)
    license_name = args.license if args.license is not None else previous.get("license")
    if license_name in ("", "none", "None"):
        license_name = None

    root = args.checkout / entry.rsplit("/", 1)[0] if "/" in entry else args.checkout
    blueprint = leanblueprint.read(root, entry.rsplit("/", 1)[-1])
    directory.mkdir(parents=True, exist_ok=True)
    if (directory / "src").exists():
        shutil.rmtree(directory / "src")
    for stale in ("structure.json", "LICENSE"):
        (directory / stale).unlink(missing_ok=True)
    if text:
        for name in blueprint.files:
            target = directory / "src" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / name, target)
        for candidate in ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"):
            if (args.checkout / candidate).is_file():
                shutil.copyfile(args.checkout / candidate, directory / "LICENSE")
                break
    else:
        payload = blueprints.structure(blueprint)
        (directory / "structure.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    source = {
        "repo": repo,
        "rev": git(args.checkout, "rev-parse", "HEAD"),
        "date": git(args.checkout, "log", "-1", "--format=%cI", "HEAD"),
        "entry": entry,
        "license": license_name,
        "text": text,
    }
    source_file.write_text(json.dumps(source, indent=1) + "\n", encoding="utf-8")
    graph = blueprint.graph
    print(f"{args.id}: {len(blueprint.files)} files, {len(graph)} nodes at {source['rev'][:8]}", file=sys.stderr)
    for problem in blueprint.problems:
        print(f"  {problem}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
