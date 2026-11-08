"""Read a project's formalization.yaml, schema v0.4 (mathlib-initiative/formalization.yaml).

A project writes this file about itself: who made it and under which license,
its sources, how it was automated and reviewed, and its status with the main
results. The schema allows keys it does not name. Formal Frontier's libraries
add `highlights`, each a title, an informal statement and its declarations, and
a `note` on main results; those are read here, and every other key is kept as
written.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import yaml

VERSION = "v0.4"
KNOWN = ("version", "project", "sources", "automation", "review", "status", "related_formalizations", "highlights")


@dataclass
class Formalization:
    project: dict
    sources: list[dict]
    automation: dict
    review: dict
    status: dict = field(default_factory=dict)
    related: list[dict] = field(default_factory=list)
    highlights: list[dict] = field(default_factory=list)
    extra: dict = field(default_factory=dict)  # every other top-level key, as written

    @property
    def main_results(self) -> list[dict]:
        return [result for result in self.status.get("main_results") or [] if isinstance(result, dict)]


def load(text: str, where: str = "formalization.yaml") -> Formalization:
    """The file's contents; raises ValueError when a key v0.4 requires is missing or empty."""
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError(f"{where}: not a mapping")
    if str(data.get("version")) != VERSION:
        raise ValueError(f"{where}: version {data.get('version')!r}, not {VERSION}")
    project = data.get("project") or {}
    automation = data.get("automation") or {}
    review = data.get("review") or {}
    missing = [f"project.{key}" for key in ("name", "authors", "license") if not project.get(key)]
    missing += [] if data.get("sources") else ["sources"]
    missing += [] if automation.get("methods") else ["automation.methods"]
    missing += [] if review.get("status") else ["review.status"]
    if missing:
        raise ValueError(f"{where}: lacks {', '.join(missing)}")
    highlights = []
    for entry in data.get("highlights") or []:
        if isinstance(entry, dict) and entry.get("title"):
            highlights.append({
                "title": text_of(entry["title"]),
                "statement": text_of(entry.get("statement")),
                "declarations": [{"declaration": text_of(item["declaration"]), "file": str(item.get("file") or "")}
                                 for item in entry.get("declarations") or []
                                 if isinstance(item, dict) and item.get("declaration")],
            })
    return Formalization(
        project=project,
        sources=[source for source in data["sources"] if isinstance(source, dict)],
        automation=automation,
        review=review,
        status=data.get("status") or {},
        related=[item for item in data.get("related_formalizations") or [] if isinstance(item, dict)],
        highlights=highlights,
        extra={key: value for key, value in data.items() if key not in KNOWN},
    )


def text_of(value) -> str:
    """A scalar as one line of text: YAML's folded and literal blocks keep their line breaks."""
    return " ".join(str(value).split()) if value is not None else ""
