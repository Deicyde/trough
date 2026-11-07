"""The Tau Ceti chapter: one article per declaration a roadmap's status names, as Tau Ceti has it.

Tau Ceti's roadmaps (TauCetiRoadmap) each carry a generated STATUS.md whose
"Named results" and "Notable definitions and infrastructure" link declarations
in Tau Ceti's documentation. Those links pick what the chapter maps; the rest of
the roadmap, its plan, its suggested signatures and its frontier, is what the
library may add, so it is left out. Each article's text is its declaration's
docstring and signature, read at the pinned Tau Ceti commit by
lean/tauceti/TauCetiDeps.lean, which also gives the edges.
"""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROADMAPS_SCHEMA = "trough-tauceti-roadmaps/v1"
ROADMAP_REPO = "TauCetiProject/TauCetiRoadmap"
SECTIONS = ("Named results", "Notable definitions and infrastructure")
# Tau Ceti's documentation has lived at both hosts; a declaration's anchor is its full name.
DOC_LINK = re.compile(
    r"\]\(https://(?:taucetiproject\.org|taucetiproject\.github\.io/TauCeti)/docs/[^)#\s]*\.html#([^)\s]+)\)"
)
TITLE = re.compile(r"^# +(?:Roadmap: *)?(.+?)\s*$", re.M)


def status_names(status: str) -> list[str]:
    """The declarations a STATUS.md links under its named results and notable definitions, in order."""
    names: list[str] = []
    for section in re.split(r"(?m)^(?=#{2,3} )", status):
        heading = section.split("\n", 1)[0].lstrip("#").strip()
        if heading in SECTIONS:
            names += [unquote(anchor) for anchor in DOC_LINK.findall(section)]
    return list(dict.fromkeys(names))


def roadmap_title(readme: str, fallback: str) -> str:
    match = TITLE.search(readme)
    if not match:
        return fallback
    title = match.group(1)
    return title[:1].upper() + title[1:]


def read_roadmaps(checkout: Path) -> list[dict]:
    """Each roadmap with a STATUS.md that names a declaration, by path in the checkout."""
    roadmaps = []
    for status in sorted(checkout.glob("*/*/STATUS.md")):
        directory = status.parent
        names = status_names(status.read_text(encoding="utf-8"))
        if not names:
            continue
        readme = directory / "README.md"
        text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
        roadmaps.append({
            "id": directory.name,
            "path": directory.relative_to(checkout).as_posix(),
            "title": roadmap_title(text, directory.name),
            "names": names,
        })
    return roadmaps
