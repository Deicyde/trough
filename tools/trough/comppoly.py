"""The CompPoly chapter: Verified-zkEVM/CompPoly, computable polynomials in Lean, an article per module.

CompPoly is a formally verified library of computable polynomial operations over finite fields and general rings,
univariate, multivariate, multilinear and bivariate, built on Mathlib, in folders under CompPoly/ (Fields,
Univariate, Bivariate, LinearAlgebra, Data, Multivariate, ToMathlib, Multilinear). tools/refresh_library.py reads a
checkout at a pinned commit into data/comppoly/ without Lean, as trough.library reads any library, with the
opening of its folders' READMEs and the README's first sentence; lean/library/LibraryDeps.lean then reads, with
Lean, the modules each module's statements and proofs use and which of the names read from the source are public.
trough.library builds the chapter; this module holds what is CompPoly's own: its README's description and the
opening of the chapter's intro.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from . import library
from .blueprints import Built
from .formal_conjectures import quote
from .library import GITHUB, Library, pinned

SCHEMA = "trough-comppoly/v1"
REPO = "Verified-zkEVM/CompPoly"
ROOT = "CompPoly"
TITLE = "CompPoly: computable polynomials in Lean"


def readme_description(readme: str) -> list[str]:
    """The first sentence of the README's first paragraph under its `# CompPoly` title: what the library is. The
    sentence after it says what the library aims to serve."""
    body = re.split(r"^# CompPoly[ \t]*\n", readme, maxsplit=1, flags=re.M)[-1]
    paragraph = " ".join(re.split(r"\n\s*\n", body.strip(), maxsplit=1)[0].split())
    return [re.split(r"(?<=[.!?])\s+", paragraph, maxsplit=1)[0]] if paragraph else []


def extras(checkout: Path) -> dict:
    """What CompPoly's record keeps besides its modules: its README's description."""
    return {"readme": readme_description((checkout / "README.md").read_text(encoding="utf-8"))}


def intro(data: dict, stats: Counter) -> str:
    return library.module_intro(COMPPOLY, data, stats, [
        f"[{REPO}]({GITHUB}/{REPO}) says in its README:",
        quote(pinned(COMPPOLY, "\n\n".join(data["readme"]), data["rev"])),
    ])


COMPPOLY = Library(id="comppoly", name="CompPoly", title=TITLE, repo=REPO, root=ROOT, schema=SCHEMA, intro=intro,
                   required=("README.md", "lean-toolchain", "lake-manifest.json"), extras=extras, list_empty=True)

LIBRARY = COMPPOLY  # as generate.py and refresh_library.py find it


def load(data: Path) -> dict | None:
    return library.load(COMPPOLY, data)


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    return library.chapter(COMPPOLY, data)
