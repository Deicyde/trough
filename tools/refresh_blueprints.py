#!/usr/bin/env python3
"""Refresh a library's blueprint sources in data/blueprints/<id>/ from a checkout.

    python tools/refresh_blueprints.py pfr /path/to/pfr-checkout
    python tools/refresh_blueprints.py strongpnt /path/to/checkout --repo math-inc/strongpnt \\
        --entry blueprint/src/web.tex --no-text

The first refresh of a library needs --repo and --entry; later ones read them
from its source.json. With text (the default) the TeX and BibTeX files the
blueprint reads are copied into src/, with the repository's license, which
must be one trough recognizes and the one source.json records (--license
accepts a new one). With --no-text, for a library whose text trough may not
reproduce, only structure.json is written: titles, labels, Lean names, marks
and places.

Nothing is written when the blueprint names a file the checkout lacks, has no
nodes, or has under half the nodes of the last refresh (--force writes anyway).
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from trough import blueprints, leanblueprint

DATA = Path(__file__).resolve().parent.parent / "data" / "blueprints"
LICENSE_FILE = re.compile(r"(?i)^(licen[cs]e|copying)([-._][\w.-]*)?$")
# Words each license's text carries, enough to tell the common ones apart.
LICENSES = [
    ("Apache-2.0", ["Apache License", "Version 2.0"]),
    ("MIT", ["Permission is hereby granted, free of charge"]),
    ("BSD-3-Clause", ["Redistribution and use in source and binary forms", "Neither the name"]),
    ("BSD-2-Clause", ["Redistribution and use in source and binary forms"]),
    ("LGPL-3.0", ["GNU LESSER GENERAL PUBLIC LICENSE", "Version 3"]),
    ("GPL-3.0", ["GNU GENERAL PUBLIC LICENSE", "Version 3"]),
    ("CC-BY-4.0", ["Creative Commons", "Attribution 4.0"]),
]


def git(checkout: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(checkout), *args], check=True, capture_output=True, text=True).stdout.strip()


def license_of(checkout: Path) -> tuple[str | None, str | None]:
    """The checkout's license file, and the SPDX name of the license it holds, if trough knows it."""
    files = sorted(path for path in checkout.iterdir() if path.is_file() and LICENSE_FILE.match(path.name))
    for path in files:
        text = " ".join(path.read_text(encoding="utf-8", errors="replace").split())
        for name, words in LICENSES:
            if all(word in text for word in words):
                return path.name, name
    return (files[0].name, None) if files else (None, None)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("id")
    parser.add_argument("checkout", type=Path)
    parser.add_argument("--repo", help="owner/name on GitHub")
    parser.add_argument("--entry", help="the blueprint's web entry file, as a path in the repository")
    parser.add_argument("--license", help="accept this SPDX name for the checkout's license")
    parser.add_argument("--no-text", dest="text", action="store_false", default=None)
    parser.add_argument("--text", dest="text", action="store_true")
    parser.add_argument("--force", action="store_true", help="write even when the node count halves")
    args = parser.parse_args()

    directory = DATA / args.id
    source_file = directory / "source.json"
    previous = json.loads(source_file.read_text(encoding="utf-8")) if source_file.is_file() else {}
    repo = args.repo or previous.get("repo")
    entry = args.entry or previous.get("entry")
    if not repo or not entry:
        parser.error(f"{args.id} has no source.json yet: give --repo and --entry")
    text = args.text if args.text is not None else previous.get("text", True)

    license_file, license_name = license_of(args.checkout)
    if text:
        expected = args.license or previous.get("license")
        if license_name is None:
            found = f"{license_file} holds no license trough recognizes" if license_file else "there is no license file"
            print(f"error: {args.id}: {found}; refresh with --no-text to keep only the structure", file=sys.stderr)
            return 1
        if license_name != expected:
            print(f"error: {args.id}: the license is now {license_name}, not {expected}; check it and give "
                  f"--license {license_name}", file=sys.stderr)
            return 1
    elif license_name:
        print(f"::warning::{args.id} now has a license ({license_name} in {license_file}): trough could show its "
              "text; refresh with --text to do so", file=sys.stderr)

    root = args.checkout / entry.rsplit("/", 1)[0] if "/" in entry else args.checkout
    blueprint = leanblueprint.read(root, entry.rsplit("/", 1)[-1])
    graph = blueprint.graph
    missing = [problem for problem in blueprint.problems if "names no file" in problem]
    if missing or not graph:
        for problem in missing or [f"{entry} has no nodes"]:
            print(f"error: {args.id}: {problem}", file=sys.stderr)
        return 1
    if len(graph) < previous.get("nodes", 0) / 2 and not args.force:
        print(f"error: {args.id}: {len(graph)} nodes, under half of the {previous['nodes']} last time; check the "
              "blueprint, and give --force if that is right", file=sys.stderr)
        return 1

    directory.mkdir(parents=True, exist_ok=True)
    if (directory / "src").exists():
        shutil.rmtree(directory / "src")
    for stale in ("structure.json", "LICENSE"):
        (directory / stale).unlink(missing_ok=True)
    if text:
        for name in blueprint.files + blueprint.bibliography:
            target = directory / "src" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / name, target)
        shutil.copyfile(args.checkout / license_file, directory / "LICENSE")
    else:
        payload = blueprints.structure(blueprint)
        (directory / "structure.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    source = {
        "repo": repo,
        "rev": git(args.checkout, "rev-parse", "HEAD"),
        "date": git(args.checkout, "log", "-1", "--format=%cI", "HEAD"),
        "entry": entry,
        "license": license_name if text else None,
        "text": text,
        "nodes": len(graph),
    }
    source_file.write_text(json.dumps(source, indent=1) + "\n", encoding="utf-8")
    print(f"{args.id}: {len(blueprint.files)} files, {len(graph)} nodes at {source['rev'][:8]}", file=sys.stderr)
    for problem in blueprint.problems:
        print(f"  {problem}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
