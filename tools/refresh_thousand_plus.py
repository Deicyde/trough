#!/usr/bin/env python3
"""Refresh data/thousand-plus.json from a checkout of 1000-plus/1000-plus.github.io.

    git clone --depth 1 https://github.com/1000-plus/1000-plus.github.io.git /tmp/1000-plus
    python tools/refresh_thousand_plus.py /tmp/1000-plus

Keeps, per entry, the Mathematics Subject Classification code, the Wikipedia
pages and the provers that formalize it. The project is released into the
public domain (Unlicense).
"""

from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

OUT = Path(__file__).resolve().parent.parent / "data" / "thousand-plus.json"
PROVERS = ("isabelle", "hol_light", "coq", "rocq", "lean", "metamath", "mizar")


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---", text, re.S)
    if not match:
        raise ValueError(f"{path}: no front matter")
    return yaml.safe_load(match.group(1)) or {}


def main() -> int:
    checkout = Path(sys.argv[1])
    rev = subprocess.run(["git", "-C", str(checkout), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
    names = yaml.safe_load((checkout / "_data" / "msc.yml").read_text(encoding="utf-8"))
    entries = {}
    for path in sorted((checkout / "_thm").glob("*.md")):
        data = front_matter(path)
        key = f"{data['wikidata']}{data.get('id_suffix') or ''}"
        pages = [
            html.unescape(re.sub(r"^\[\[|\]\]$", "", str(link)).split("|")[0])
            for link in data.get("wikipedia_links") or []
        ]
        others = {
            prover: sorted({str(record.get("status", "")) for record in data[prover] if isinstance(record, dict)})
            for prover in PROVERS
            if isinstance(data.get(prover), list)
        }
        entries[key] = {"msc": str(data.get("msc_classification") or ""), "wikipedia": pages, "others": others}
    payload = {
        "source": {"repo": "1000-plus/1000-plus.github.io", "rev": rev},
        "msc_names": {str(code): name for code, name in names.items()},
        "entries": entries,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{len(entries)} entries from {rev[:8]} written to {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
