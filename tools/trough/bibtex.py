"""Read a blueprint's BibTeX: for each citation key, a short label and a link to the work.

A label is the authors' surnames and the year, "Knuth 1970", "Baader and Nipkow
1998" or "Willsey et al. 2021"; the link is the work's DOI, URL or arXiv page.
"""

from __future__ import annotations

import re
from pathlib import Path

from trough.tex import Writer, group_end

ENTRY = re.compile(r"@\s*(\w+)\s*[{(]\s*([^,\s{}()]+)\s*,")
FIELD = re.compile(r"\s*,?\s*([A-Za-z][\w:.+-]*)\s*=\s*")
BARE = re.compile(r"[^,}#)\s]*")
JOIN = re.compile(r"\s*#\s*")
SKIPPED = {"comment", "string", "preamble"}


def value(text: str, i: int) -> tuple[str, int]:
    """The field value that starts at text[i], a {group}, a "string" or a bare word, joined
    with # to more of them; and where it ends."""
    pieces = []
    while True:
        if text.startswith("{", i):
            end = group_end(text, i)
            pieces.append(text[i + 1 : end - 1])
            i = end
        elif text.startswith('"', i):
            j = i + 1
            depth = 0
            while j < len(text) and not (text[j] == '"' and depth == 0):
                depth += {"{": 1, "}": -1}.get(text[j], 0)
                j += 2 if text[j] == "\\" else 1
            pieces.append(text[i + 1 : j])
            i = j + 1
        else:
            word = BARE.match(text, i)
            pieces.append(word.group())
            i = word.end()
        join = JOIN.match(text, i)
        if not join:
            return re.sub(r"\s+", " ", "".join(pieces)).strip(), i
        i = join.end()


def entries(text: str) -> dict[str, dict[str, str]]:
    """Each entry's fields, by key; the first entry with a key wins."""
    found: dict[str, dict[str, str]] = {}
    for match in ENTRY.finditer(text):
        if match.group(1).lower() in SKIPPED:
            continue
        fields: dict[str, str] = {}
        i = match.end()
        while (name := FIELD.match(text, i)) is not None:
            fields[name.group(1).lower()], i = value(text, name.end())
        found.setdefault(match.group(2), fields)
    return found


def top_level_split(text: str, separator: str) -> list[str]:
    """text split at *separator* where it is outside braces."""
    parts, depth, start = [], 0, 0
    i = 0
    while i < len(text):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif depth == 0 and text.startswith(separator, i):
            parts.append(text[start:i])
            start = i + len(separator)
            i = start
            continue
        i += 1
    parts.append(text[start:])
    return [part.strip() for part in parts if part.strip()]


def surname(name: str) -> str:
    """The surname of a BibTeX name, "von Last, First" or "First von Last": from its first
    lowercase word, the "von" part, to the end, or else its last word."""
    pieces = top_level_split(name, ",")
    if len(pieces) > 1:
        return pieces[0]
    words = top_level_split(name, " ")
    if not words:
        return name
    particle = next((k for k, word in enumerate(words[:-1]) if k and word[:1].islower()), None)
    return " ".join(words[particle:] if particle is not None else words[-1:])


def label(fields: dict[str, str], writer: Writer) -> str | None:
    people = fields.get("author") or fields.get("editor")
    year = fields.get("year") or fields.get("date", "")[:4]
    if people:
        listed = top_level_split(people, " and ")
        names = [writer.plain(surname(name)) for name in listed if name.strip().lower() != "others"]
        names = [name for name in names if name]
        if not names:
            return None
        more = len(names) > 2 or len(names) < len(listed)  # "and others" stands for more authors
        who = f"{names[0]} et al." if more else " and ".join(names)
    elif fields.get("title"):
        who = writer.plain(fields["title"])
    else:
        return None
    return f"{who} {writer.plain(year)}".strip()


def link(fields: dict[str, str]) -> str | None:
    if fields.get("doi"):
        return "https://doi.org/" + re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", fields["doi"].strip())
    if fields.get("url", "").startswith(("http://", "https://")):
        return fields["url"].strip()
    if fields.get("eprint") and (fields.get("archiveprefix", "") + fields.get("eprinttype", "")).lower() == "arxiv":
        return f"https://arxiv.org/abs/{fields['eprint'].strip()}"
    return None


def bibliography(paths: list[Path], cited: list[str]) -> dict[str, tuple[str, str | None]]:
    """Each key of the .bib files at *paths* that the blueprint cites: its label and link.
    Works that share a label get the letters a, b, ... in the order they are first cited."""
    writer = Writer({})
    found: dict[str, tuple[str, str | None]] = {}
    for path in paths:
        for key, fields in entries(path.read_text(encoding="utf-8", errors="replace")).items():
            name = label(fields, writer)
            if name and key not in found and key in cited:
                found[key] = (name, link(fields))
    shared: dict[str, list[str]] = {}
    for key in dict.fromkeys(cited):
        if key in found:
            shared.setdefault(found[key][0], []).append(key)
    for name, keys in shared.items():
        if len(keys) > 1:
            for letter, key in zip("abcdefghijklmnopqrstuvwxyz", keys):
                found[key] = (f"{name}{letter}", found[key][1])
    return found
