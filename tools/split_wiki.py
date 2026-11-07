#!/usr/bin/env python3
"""Split wiki articles written in one file into their Markdown and their annotations.

    python tools/split_wiki.py wiki/mathlib/lagranges-theorem.md ...

Each file named holds front matter (article_id, concept) and [words](lean:Name) citations,
as the article pipeline drafts an article; a file split already has its quotes written again. It is rewritten as its Markdown alone, and its id,
concept and citations go to the .jsonl beside it, in the form tools/trough/wiki.py reads. The
folder gets the _defaults.json those annotations need. A concept key that names a Mathlib module
in data/mathlib/concept-deps.json becomes a module end.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import unquote

from trough import wiki

ROOT = Path(__file__).resolve().parent.parent


def canonical(article: wiki.Authored) -> wiki.Authored:
    article.body = wiki.LEAN_LINK.sub(lambda link: f"](lean:{unquote(link.group(1) or link.group(2))})", article.body)
    return article


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    deps = ROOT / "data" / "mathlib" / "concept-deps.json"
    modules = frozenset(json.loads(deps.read_text(encoding="utf-8")).get("modules", {})) if deps.is_file() else frozenset()
    for path in args.files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") and path.with_suffix(".jsonl").is_file():
            text = wiki.combined(path)  # split already: write its quotes again
        before = wiki.parse_text(path, text)
        markdown, rows = wiki.split(text, path.stem, modules)
        path.write_text(markdown, encoding="utf-8")
        path.with_suffix(".jsonl").write_text(wiki.jsonl(rows), encoding="utf-8")
        (path.parent / "_defaults.json").write_text(json.dumps(wiki.DEFAULTS) + "\n", encoding="utf-8")
        # The two files must read back as the article did, up to how a citation's name is spelled.
        if canonical(wiki.parse(path)) != canonical(before):
            original = text if text.startswith("---\n") else None
            if original is not None:
                path.write_text(original, encoding="utf-8")
                path.with_suffix(".jsonl").unlink()
            raise SystemExit(f"{path}: the split article does not read back as it was; left as it was")
        print(f"{path}: {len(rows) - 1} citations", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
