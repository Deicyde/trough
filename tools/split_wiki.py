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
        jsonl_path = path.with_suffix(".jsonl")
        saved = (path.read_text(encoding="utf-8"), jsonl_path.read_text(encoding="utf-8") if jsonl_path.is_file() else None)
        text = saved[0]
        if not text.startswith("---\n") and saved[1] is not None:
            text = wiki.combined(path)  # split already: write its quotes again
        before = wiki.parse_text(path, text)
        markdown, rows = wiki.split(text, path.stem, modules)
        path.write_text(markdown, encoding="utf-8")
        jsonl_path.write_text(wiki.jsonl(rows), encoding="utf-8")
        (path.parent / "_defaults.json").write_text(json.dumps(wiki.DEFAULTS) + "\n", encoding="utf-8")
        # The two files must read back as the article did, up to how a citation's name is spelled.
        try:
            same = canonical(wiki.parse(path)) == canonical(before)
            problem = "does not read back as it was"
        except ValueError as error:
            same, problem = False, f"does not read back ({error})"
        if not same:
            path.write_text(saved[0], encoding="utf-8")
            if saved[1] is None:
                jsonl_path.unlink()
            else:
                jsonl_path.write_text(saved[1], encoding="utf-8")
            raise SystemExit(f"{path}: the split article {problem}; left as it was")
        print(f"{path}: {len(rows) - 1} citations", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
