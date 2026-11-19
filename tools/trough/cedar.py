"""The Cedar chapter: cedar-policy/cedar-spec, the Lean formalization of the Cedar policy language, an article per module.

cedar-spec holds the formalization of Cedar, with proofs about it, and tooling for differential randomized testing
between the formalization and Cedar's Rust implementation. The Lean is the Lake project in cedar-lean/, and this
chapter maps its Cedar library: the modules under cedar-lean/Cedar/ (Data, Spec, Validation, TPE, SymCC, SymCCOpt and
Thm, the proofs). The project's other libraries, for Protobuf serialization, the foreign function interface and
tests, are left out. tools/refresh_library.py reads a checkout at a pinned commit into data/cedar/ without Lean, as
trough.library reads any library, with the opening of the repository's README; lean/library/LibraryDeps.lean then
reads, with Lean, the modules each module's statements and proofs use and which of the names read from the source
are public. trough.library builds the chapter; this module holds what is Cedar's own: its README's description and
the opening of the chapter's intro.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from . import library
from .blueprints import Built
from .formal_conjectures import quote
from .library import GITHUB, Library, pinned

SCHEMA = "trough-cedar/v1"
REPO = "cedar-policy/cedar-spec"
SUBDIR = "cedar-lean"
ROOT = "Cedar"
TITLE = "Cedar: the Lean formalization of the Cedar policy language"


def readme_description(readme: str) -> list[str]:
    """The repository README's first paragraph under its `# Cedar Specification` title: what the repository holds."""
    body = re.split(r"^# Cedar Specification[ \t]*\n", readme, maxsplit=1, flags=re.M)[-1]
    paragraph = " ".join(re.split(r"\n\s*\n", body.strip(), maxsplit=1)[0].split())
    return [paragraph] if paragraph else []


def extras(project: Path) -> dict:
    """What Cedar's record keeps besides its modules: the description in the README at the repository's top, above
    the Lake project's folder."""
    return {"readme": readme_description((project / ".." / "README.md").read_text(encoding="utf-8"))}


def intro(data: dict, stats: Counter) -> str:
    return library.module_intro(CEDAR, data, stats, [
        f"[{REPO}]({GITHUB}/{REPO}) says in its README:",
        quote(pinned(CEDAR, "\n\n".join(data["readme"]), data["rev"])),
        f"Its Lean is the Lake project in `{SUBDIR}/`, and this chapter maps that project's `{ROOT}` library. The "
        "project's other libraries, for Protobuf serialization, the foreign function interface and tests, are left out.",
    ])


CEDAR = Library(id="cedar", name="Cedar", title=TITLE, repo=REPO, root=ROOT, schema=SCHEMA, intro=intro,
                required=("../README.md", "lean-toolchain", "lake-manifest.json"), extras=extras, list_empty=True,
                subdir=SUBDIR)

LIBRARY = CEDAR  # as generate.py and refresh_library.py find it


def load(data: Path) -> dict | None:
    return library.load(CEDAR, data)


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    return library.chapter(CEDAR, data)
