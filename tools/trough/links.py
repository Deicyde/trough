"""The Mathlib chapter's facts as literature-links annotations in blueprint/links/.

AutoformBot reads an article's facts from its annotation where it has one, so the
chapter's pages have no front matter. links/mathlib/articles.jsonl holds one line per
page with facts, in the chapter's order: an authored article's id, the kind, the
Mathlib declarations as Lean ends, and AutoformBot's own keys. The folder's
_defaults.json makes each end Mathlib at the pin, so a new pin changes one line. An
article Mathlib lacks links nothing: "object": [].

    {"id": "af_...", "kind": "theorem", "subject": [{"type": "generic", "uri": "../../roadmap/mathlib/....md"}],
     "object": [{"location": {"declaration": "Subgroup.card_subgroup_dvd_card", "module": "Mathlib.GroupTheory.Coset.Card"}}],
     "extensions": {"org.autoform": {"origin": "cited", "mathlib": true}}}
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from urllib.parse import quote

from trough.vault import Container, facts, walk

MATHLIB = "https://github.com/leanprover-community/mathlib4"
# org.autoform keys, as AutoformBot reads them; the flags are JSON booleans.
OURS = ("origin", "navigation")
FLAGS = ("mathlib", "not_ready")


def annotation(fields: list[tuple[str, str]], page: Path, folder: Path) -> dict | None:
    """The annotation carrying a page's fields, or None if it has none."""
    given = dict(fields)
    unknown = given.keys() - {"article_id", "declaration", "mathlib_declaration", "mathlib_file", *OURS, *FLAGS}
    if unknown:
        raise ValueError(f"{page}: no annotation field for {', '.join(sorted(unknown))}")
    if not given:
        return None
    # AutoformBot takes mathlib_file from the first end's module, as the front matter gave it for the first name.
    module = given["mathlib_file"].removesuffix(".lean").replace("/", ".") if "mathlib_file" in given else None
    names = [name for name in given.get("mathlib_declaration", "").split(", ") if name]
    ends = [{"location": {"declaration": name, **({"module": module} if module and not i else {})}}
            for i, name in enumerate(names)] or ([{"location": {"module": module}}] if module else [])
    ours = {key: given[key] for key in OURS if key in given} | {key: True for key in FLAGS if given.get(key) == "true"}
    row = {
        "id": given.get("article_id"),
        "kind": given.get("declaration"),
        "subject": [{"type": "generic", "uri": quote(Path(os.path.relpath(page, folder)).as_posix())}],
        "object": ends,
        "extensions": {"org.autoform": ours} if ours else None,
    }
    return {key: value for key, value in row.items() if value is not None}


def files(root: Container, folder: Path, rev: str) -> dict[Path, str]:
    """The folder's defaults and annotations for every page under *root*."""
    rows = [row for node in walk(root) if (row := annotation(facts(node), node.path, folder))]
    defaults = {"object": {"type": "lean", "uri": MATHLIB, "version": rev}}
    return {
        folder / "_defaults.json": json.dumps(defaults) + "\n",
        folder / "articles.jsonl": "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
    }
