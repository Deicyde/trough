"""The chapter on Axiom's Lean formalization of the Stacks Project: an article per Stacks section, a block per tag.

AxiomMath/Stacks formalizes the Stacks Project (stacks.math.columbia.edu) in
Lean, indexed by Stacks tag. A declaration that formalizes all or part of a tag
carries `@[stacks TAG]` (or `@[stacks_fixed TAG]`), with a comment saying which
part when it covers only part; `attribute [stacks TAG] name` tags a declaration
after the fact, and `add_to_stacks TAG name` registers one outside the
repository, in Mathlib. `@[ega "..."]`, `@[sga "..."]`, `add_to_ega` and
`add_to_sga` record the items of EGA and SGA a declaration proves. The library
has two tiers, StacksCore and StacksFrontier. tools/refresh_stacks.py reads a
checkout at a pinned commit into data/stacks/: each tag's declarations as
trough.leansource reads them without Lean, and the parts, chapters and sections
of the Stacks Project, read from its own repository, which place each tag. The
chapter has a part per Stacks Project part, a page per chapter and an article
per section with a tag that a declaration carries; an EGA page and an SGA page
index the references. The articles have no edges.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from collections.abc import Callable
from pathlib import Path

from . import ff, leansource, tex
from .blueprints import Built, escape
from .formal_conjectures import natural, plural, quote
from .mathlib import fence
from .vault import Container, Entry, Leaf, chunk, slugify

SCHEMA = "trough-stacks/v1"
REPO = "AxiomMath/Stacks"
PROJECT = "stacks/stacks-project"
GITHUB = "https://github.com"
SITE = "https://stacks.axiommath.ai/"
STACKS_SITE = "https://stacks.math.columbia.edu"
MATHLIB_DOCS = "https://leanprover-community.github.io/mathlib4_docs/find/?pattern={}#doc"
TIERS = ("StacksCore", "StacksFrontier")
STRING = r'"(?:[^"\\]|\\[\s\S])*"'  # a backslash may end a line, as a string gap does
TAG = re.compile(r"^[0-9A-Z]{4}$")
TAGGING = re.compile(rf"^(?:stacks|stacks_fixed) (\S+)(?: ({STRING}))?$", re.S)
REFERENCE = re.compile(rf"^(ega|sga) ({STRING})(?: ({STRING}))?$", re.S)
WORDS = ("stacks", "stacks_fixed", "ega", "sga")
REGISTRATION = re.compile(rf"add_to_(stacks|ega|sga)[ \t]+({STRING}|[^\s\"]+)(?:\s+({STRING}))?\s+({leansource.NAME})")
# Where a command starts, found in the text with strings blanked: a line of a multi-line string may start
# with the same word.
REGISTRATION_START = re.compile(r"^[ \t]*add_to_(?:stacks|ega|sga)\b", re.M)
ATTRIBUTE_START = re.compile(r"^[ \t]*attribute[ \t]*\[", re.M)
EGA_VOLUMES = ("0", "I", "II", "III", "IV")
SGA_VOLUMES = ("1", "2", "3", "4", "4½", "5", "6", "7")
NUMBER = re.compile(r"^\d+(?:\.\d+)+$")
SGA_NUMBER = re.compile(r"^(?=.*\d)[A-Za-z0-9()]+(?:\.[A-Za-z0-9()]+)*$")
EXPOSE = re.compile(r"^(?:0|[IVX][A-Za-z]*)$")
ESCAPES = {"n": "\n", "t": "\t", "r": "\r", "\\": "\\", '"': '"', "'": "'"}


def lean_string(literal: str) -> str:
    """The value of a Lean string literal, written with its quotes: escapes decoded, and a gap (a backslash
    ending a line, with the next line's leading space) taken out. An attribute list comes with its whitespace
    collapsed, so a gap there reads as a backslash and one space."""
    body, out, i = literal[1:-1], [], 0
    while i < len(body):
        if body[i] == "\\" and i + 1 < len(body):
            following = body[i + 1]
            if following in " \t\n":
                i += 1
                while i < len(body) and body[i] in " \t\n":
                    i += 1
                continue
            if following in ESCAPES:
                out.append(ESCAPES[following])
                i += 2
                continue
            if (match := re.match(r"x([0-9a-fA-F]{2})|u([0-9a-fA-F]{4})", body[i + 1:])):
                out.append(chr(int(match.group(1) or match.group(2), 16)))
                i += 1 + match.end()
                continue
        out.append(body[i])
        i += 1
    return "".join(out)


def ega(ref: str) -> tuple[str, str] | None:
    """An EGA reference's volume and printed number, "IV 7.8.3" giving ("IV", "7.8.3"); None when it is not one."""
    parts = ref.split()
    if len(parts) == 2 and parts[0] in EGA_VOLUMES and NUMBER.match(parts[1]):
        return parts[0], parts[1]
    return None


def sga(ref: str) -> tuple[str, str, str] | None:
    """An SGA reference's volume, exposé and number, "4 IV 4.9.4" giving ("4", "IV", "4.9.4"); None when it is
    not one. SGA 4½ names its parts in words joined by underscores, which read as spaces."""
    parts = ref.split()
    if len(parts) != 3 or parts[0] not in SGA_VOLUMES or not SGA_NUMBER.match(parts[2]):
        return None
    if parts[0] != "4½" and not EXPOSE.match(parts[1]):
        return None
    return parts[0], parts[1].replace("_", " ") if parts[0] == "4½" else parts[1], parts[2]


def read_attributes(attributes: tuple[str, ...] | list[str]) -> tuple[list[dict], dict[str, list[dict]], list[str]]:
    """The tags and the EGA and SGA references an attribute list gives, and its attributes of these kinds that
    do not read."""
    tags, references, unread = [], {"ega": [], "sga": []}, []
    for attribute in attributes:
        word = attribute.split(" ", 1)[0]
        if word not in WORDS:
            continue
        if word in ("stacks", "stacks_fixed"):
            match = TAGGING.match(attribute)
            if not match or not TAG.match(match.group(1)):
                unread.append(attribute)
                continue
            tags.append({"tag": match.group(1), "comment": lean_string(match.group(2)) if match.group(2) else ""})
            continue
        match = REFERENCE.match(attribute)
        ref = " ".join(lean_string(match.group(2)).split()) if match else ""
        if not match or not (ega(ref) if word == "ega" else sga(ref)):
            unread.append(attribute)
            continue
        references[word].append({"ref": ref, "comment": lean_string(match.group(3)) if match.group(3) else ""})
    return tags, references, unread


def line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def closing(code: str, opening: int) -> int:
    """Where the bracket opened at code[opening] closes, in text whose strings and comments are blanked."""
    depth = 0
    for i in range(opening, len(code)):
        if code[i] == "[":
            depth += 1
        elif code[i] == "]":
            depth -= 1
            if not depth:
                return i
    return len(code)


def header(text: str, line: int) -> str:
    """A declaration's text from its keyword's line, while lines stay indented and do not start a `|` case:
    the statement of a definition by cases, or the whole of a structure written without `where`."""
    lines = leansource.blank_attributes(leansource.blank(text)).split("\n")
    source = text.split("\n")
    column = len(lines[line - 1]) - len(lines[line - 1].lstrip())
    kept = [source[line - 1][column:]]
    for number in range(line, len(lines)):
        code = lines[number]
        if not code.strip() or not code[:1].isspace() or code.strip().startswith("|"):
            break
        kept.append(source[number])
    return leansource.dedent("\n".join(kept).rstrip(), column)


def read_file(text: str, path: str) -> dict:
    """What a file writes about tags and references: the declarations that carry one, with their docstrings,
    statements and lines; the public names it declares, with their lines; its registrations (`add_to_stacks`,
    `add_to_ega`, `add_to_sga`) and the `attribute` commands that name a declaration it does not; and what of
    these does not read."""
    record = {"declarations": [], "names": {}, "registrations": [], "commands": [], "unread": []}
    found = leansource.declarations(text, relaxed=True)
    if found is None:
        record["unread"].append({"line": 0, "why": "its scopes do not close as they open"})
        return record
    spans = leansource.spans(text)
    code = leansource.clear(text, spans)
    plain = leansource.clear(text, [span for span in spans if span[2] != "string"])
    for declaration in found:
        if declaration.name and not declaration.private:
            record["names"].setdefault(declaration.name, declaration.line)

    def entry(declaration: leansource.Declaration) -> dict:
        return {"name": declaration.name, "kind": declaration.kind, "line": declaration.line,
                "private": declaration.private, "doc": declaration.doc,
                "statement": declaration.statement if declaration.statement is not None else header(text, declaration.line),
                "sorry": declaration.proof_sorry, "tags": [], "ega": [], "sga": []}

    entries: dict[int, dict] = {}  # by position in found
    attached: Counter = Counter()
    for index, declaration in enumerate(found):
        tags, references, unread = read_attributes(declaration.attributes)
        attached.update(attribute for attribute in declaration.attributes if attribute.split(" ", 1)[0] in WORDS)
        record["unread"] += [{"line": declaration.line, "why": f"an attribute that does not read: {attribute}"}
                             for attribute in unread]
        if tags or references["ega"] or references["sga"]:
            entries[index] = entry(declaration)
            entries[index]["tags"] += tags
            entries[index]["ega"] += references["ega"]
            entries[index]["sga"] += references["sga"]

    # Every attribute of these kinds that an `@[...]` list writes sits on a declaration read above.
    written: dict[str, list[int]] = {}
    i = code.find("@[")
    while i >= 0:
        end = closing(code, i + 1)
        for attribute in leansource.split_attributes(plain[i + 2:end]):
            if attribute.split(" ", 1)[0] in WORDS:
                written.setdefault(attribute, []).append(line_of(code, i))
        i = code.find("@[", end + 1)
    for attribute, lines in written.items():
        for line in lines[attached[attribute]:]:
            record["unread"].append({"line": line, "why": f"an attribute on no declaration the reading finds: {attribute}"})

    for match in REGISTRATION_START.finditer(code):
        start = code.index("add_to_", match.start())
        line = line_of(code, start)
        command = REGISTRATION.match(plain, start)
        what, ref = (command.group(1), command.group(2)) if command else ("", "")
        if not command or not leansource.is_name(command.group(4)):
            value = ""
        elif what == "stacks" and TAG.match(ref):
            value = ref
        elif what in ("ega", "sga") and ref.startswith('"'):
            value = " ".join(lean_string(ref).split())
            value = value if (ega(value) if what == "ega" else sga(value)) else ""
        else:
            value = ""
        if not value:
            first = plain[start:].split("\n", 1)[0].strip()
            record["unread"].append({"line": line, "why": f"a registration that does not read: {first}"})
            continue
        record["registrations"].append({"what": what, "ref": value, "line": line, "name": command.group(4),
                                        "comment": lean_string(command.group(3)) if command.group(3) else ""})

    for match in ATTRIBUTE_START.finditer(code):
        opening = match.end() - 1
        end = closing(code, opening)
        attributes = leansource.split_attributes(plain[opening + 1:end])
        if not any(attribute.split(" ", 1)[0] in WORDS for attribute in attributes):
            continue
        line = line_of(code, match.start())
        # The names run to the next line that starts a command at column 0.
        rest = re.split(r"\n(?=\S)", code[end + 1:], maxsplit=1)[0]
        names = rest.split()
        tags, references, unread = read_attributes(attributes)
        record["unread"] += [{"line": line, "why": f"an attribute that does not read: {attribute}"} for attribute in unread]
        if not names or not all(leansource.is_name(name) for name in names):
            record["unread"].append({"line": line, "why": f"an `attribute` command whose names do not read: {rest.strip()}"})
            continue
        for name in names:
            # A name the file declares, written in full or under the namespaces it sits in.
            here = [index for index, declaration in enumerate(found) if declaration.name and not declaration.private
                    and (declaration.name == name or declaration.name.endswith("." + name))]
            if len(here) == 1:
                index = here[0]
                entries.setdefault(index, entry(found[index]))
                entries[index]["tags"] += [tag | {"attribute_line": line} for tag in tags]
                entries[index]["ega"] += references["ega"]
                entries[index]["sga"] += references["sga"]
            else:
                record["commands"].append({"line": line, "name": name, "tags": tags, **references})
    record["declarations"] = [entries[index] for index in sorted(entries)]
    return record


def tier(path: str) -> str:
    return path.split("/", 1)[0]


def read(checkout: Path, paths: list[str]) -> tuple[list[dict], dict, list[str]]:
    """Every tag's record, sorted by tag, the counts the intro gives, and what does not read, from the .lean files
    of both tiers. A tag's record lists the repository's declarations that carry it and the declarations
    registered for it, each with its EGA and SGA references."""
    files: dict[str, dict] = {}
    names: dict[str, tuple[str, int]] = {}
    unread: list[str] = []
    for path in paths:
        record = read_file((checkout / path).read_text(encoding="utf-8"), path)
        for name, line in record.pop("names").items():
            names.setdefault(name, (path, line))
        unread += [f"{path}:{item['line']} {item['why']}" for item in record["unread"]]
        if record["declarations"] or record["registrations"] or record["commands"]:
            files[path] = record
    # An `attribute` command naming a declaration of another file of the repository tags it there.
    for path, record in list(files.items()):
        for command in record["commands"]:
            if command["name"] not in names:
                continue
            target, line = names[command["name"]]
            other = files.setdefault(target, {"declarations": [], "registrations": [], "commands": []})
            found = next((item for item in other["declarations"] if item["name"] == command["name"]), None)
            if found is None:
                text = (checkout / target).read_text(encoding="utf-8")
                declaration = next(item for item in leansource.declarations(text, relaxed=True) or []
                                   if item.name == command["name"] and not item.private)
                found = {"name": declaration.name, "kind": declaration.kind, "line": declaration.line,
                         "private": False, "doc": declaration.doc,
                         "statement": declaration.statement if declaration.statement is not None else header(text, line),
                         "sorry": declaration.proof_sorry, "tags": [], "ega": [], "sga": []}
                other["declarations"].append(found)
            found["tags"] += [tag | {"attribute_file": path, "attribute_line": command["line"]} for tag in command["tags"]]
            found["ega"] += command["ega"]
            found["sga"] += command["sga"]
            command["resolved"] = True
    # References registered on a name, which its declaration's block and its registrations show.
    registered: dict[str, dict[str, list[dict]]] = {}
    for record in files.values():
        for item in record["registrations"]:
            if item["what"] != "stacks":
                registered.setdefault(item["name"], {"ega": [], "sga": []})[item["what"]].append(
                    {"ref": item["ref"], "comment": item["comment"]})
        for command in record["commands"]:
            if not command.get("resolved"):
                for work in ("ega", "sga"):
                    registered.setdefault(command["name"], {"ega": [], "sga": []})[work] += command[work]
    tags: dict[str, dict] = {}
    counts: Counter = Counter()
    items: dict[str, set[str]] = {"ega": set(), "sga": set()}
    for path in paths:
        if path not in files:
            continue
        record, where = files[path], tier(path)
        for declaration in record["declarations"]:
            extra = registered.get(declaration["name"], {"ega": [], "sga": []}) if declaration["name"] else {}
            for work in ("ega", "sga"):
                declaration[work] += extra.get(work, [])
                items[work] |= {reference["ref"] for reference in declaration[work]}
                counts[f"{work}_attributes"] += len(declaration[work])
            if not declaration["tags"]:
                continue
            counts[f"declarations_{where}"] += 1
            counts["sorry"] += declaration["sorry"]
            for tagging in declaration["tags"]:
                block = {key: value for key, value in declaration.items() if key != "tags"}
                block |= {"file": path, "tier": where, "comment": tagging["comment"]}
                for key in ("attribute_file", "attribute_line"):
                    if key in tagging:
                        block[key] = tagging[key]
                tags.setdefault(tagging["tag"], {"tag": tagging["tag"], "declarations": [], "registrations": []})[
                    "declarations"].append(block)
        external = [item for item in record["registrations"] if item["what"] == "stacks"] + [
            {"what": "stacks", "ref": tagging["tag"], "line": command["line"], "name": command["name"],
             "comment": tagging["comment"], "attribute": True}
            for command in record["commands"] if not command.get("resolved") for tagging in command["tags"]]
        for item in record["registrations"]:
            if item["what"] != "stacks":
                counts[f"{item['what']}_registrations_{where}"] += 1
                items[item["what"]].add(item["ref"])
        for item in external:
            counts[f"registrations_{where}"] += 1
            references = registered.get(item["name"], {"ega": [], "sga": []})
            entry = {"name": item["name"], "file": path, "line": item["line"], "tier": where, "comment": item["comment"],
                     "ega": references["ega"], "sga": references["sga"]}
            if item.get("attribute"):
                entry["attribute"] = True
            if item["name"] in names:
                entry["declared"] = {"file": names[item["name"]][0], "line": names[item["name"]][1]}
            tags.setdefault(item["ref"], {"tag": item["ref"], "declarations": [], "registrations": []})[
                "registrations"].append(entry)
    for record in tags.values():
        for tier_name in TIERS:
            if any(block["tier"] == tier_name for block in record["declarations"] + record["registrations"]):
                counts[f"tags_{tier_name}"] += 1
    counts["files_StacksCore"] = sum(1 for path in paths if tier(path) == "StacksCore")
    counts["files_StacksFrontier"] = sum(1 for path in paths if tier(path) == "StacksFrontier")
    counts["ega_items"], counts["sga_items"] = len(items["ega"]), len(items["sga"])
    return [tags[tag] for tag in sorted(tags)], dict(sorted(counts.items())), unread


# The Stacks Project's structure.

ITEM = re.compile(r"^\\item\s*\\hyperref\[(.+?)-section-phantom\]\{(.*)\}\s*$")
SECTION_OR_LABEL = re.compile(r"\\section\*?\s*\{|\\label\s*\{([^}]*)\}")


def read_project(checkout: Path, used: set[str]) -> tuple[dict, list[str]]:
    """The Stacks Project's parts, chapters and sections, titled as it titles them, and the place of each tag of
    *used*: its chapter, its section (0 before the chapter's first section), the kind of item its label names and
    its position in the chapter; with what does not read."""
    problems = []
    labels: dict[str, str] = {}
    tags_file = checkout / "tags" / "tags"
    for line in (tags_file.read_text(encoding="utf-8").splitlines() if tags_file.is_file() else []):
        if line.strip() and not line.startswith("#"):
            tag, _, label = line.strip().partition(",")
            labels[tag] = label
    if not labels:
        problems.append("the Stacks Project's tags/tags lists no tags")
    preamble = checkout / "preamble.tex"
    writer = tex.Writer(tex.definitions(preamble.read_text(encoding="utf-8")) if preamble.is_file() else {})
    tag_of = {label: tag for tag, label in labels.items()}
    parts: list[dict] = []
    contents = checkout / "chapters.tex"
    number = 0
    for line in (contents.read_text(encoding="utf-8").splitlines() if contents.is_file() else []):
        line = tex.strip_comment(line).strip()
        if not line:
            continue
        if not line.startswith("\\"):
            parts.append({"title": writer.plain(line), "chapters": []})
            continue
        if (match := ITEM.match(line)) and parts:
            number += 1
            parts[-1]["chapters"].append({"number": number, "file": match.group(1), "title": writer.plain(match.group(2)),
                                          "tag": tag_of.get(f"{match.group(1)}-section-phantom")})
    if not parts:
        problems.append("the Stacks Project's chapters.tex lists no parts")
    places: dict[str, dict] = {}
    for part in parts:
        for chapter in part["chapters"]:
            source = checkout / f"{chapter['file']}.tex"
            chapter["sections"] = []
            if not source.is_file():
                continue
            text = "\n".join(tex.strip_comment(line) for line in source.read_text(encoding="utf-8").split("\n"))
            section, pending, order = 0, None, 0
            for match in SECTION_OR_LABEL.finditer(text):
                if match.group(1) is None:
                    end = tex.group_end(text, match.end() - 1)
                    section += 1
                    pending = {"number": section, "title": writer.plain(text[match.end():end - 1]), "tag": None}
                    chapter["sections"].append(pending)
                    continue
                label = f"{chapter['file']}-{match.group(1).strip()}"
                order += 1
                if pending is not None and match.group(1).strip().startswith("section-"):
                    pending["tag"] = tag_of.get(label)
                    pending = None
                tag = tag_of.get(label)
                if tag in used:
                    kind = label[len(chapter["file"]) + 1:].split("-", 1)[0]
                    places[tag] = {"chapter": chapter["file"], "section": section, "order": order,
                                   "kind": "chapter" if label.endswith("-section-phantom") else kind}
            # The chapter's own tag, whose label is no \label in its file.
            if chapter["tag"] in used:
                places.setdefault(chapter["tag"], {"chapter": chapter["file"], "section": 0, "order": 0, "kind": "chapter"})
    if writer.unknown:
        print("unknown TeX in the Stacks Project's titles: " + ", ".join(f"\\{name}" for name, _ in writer.unknown.most_common(8)))
    return {"parts": parts, "tags": dict(sorted(places.items()))}, problems


# The site.

class Unreachable(Exception):
    """The site did not answer at all: a network failure, which says nothing about its pages."""


def site_problem(url: str, tags: list[str], fetch: Callable[[str, str], bytes | None]) -> str | None:
    """Why the site at *url* does not serve the tags' pages, or None when it does: its tag page answers for the
    first of *tags*, and its data, at the address its home page names, has an entry for each of them. fetch(url,
    method) gives the body of a GET, None when the site answers that it has no such page; it raises Unreachable
    when the site does not answer."""
    home = fetch(url, "GET")
    base = re.search(rb'data-base="([^"]+)"', home or b"")
    if not base:
        return f"{url} does not name its data"
    if fetch(f"{url}library?tag={tags[0]}", "GET") is None:
        return f"{url}library?tag={tags[0]} answers that it has no such page"
    for tag in tags:
        data = fetch(f"{base.group(1).decode()}api/entity/{tag}.json", "GET")
        try:
            entity = json.loads(data or b"null")
        except ValueError:
            entity = None
        if not isinstance(entity, dict) or (entity.get("entity") or {}).get("tag") != tag:
            return f"its data has no entry for tag {tag}"
    return None


def sample(tags: list[str], size: int = 30) -> list[str]:
    """*size* tags spread evenly over the sorted list, the same for the same list."""
    ordered = sorted(tags)
    if len(ordered) <= size:
        return ordered
    return [ordered[index * len(ordered) // size] for index in range(size)]


# The chapter, from the data.

# What each tier is, in the words of the repository's formalization.yaml.
TIER_WORDS = {"StacksCore": "StacksCore (human-reviewed)", "StacksFrontier": "StacksFrontier (drafted, not yet reviewed)"}
KIND_WORDS = {"chapter": "the chapter", "section": "the section", "subsection": "a subsection", "item": "an item",
              "equation": "an equation", "exercise": "an exercise", "example": "an example", "remarks": "remarks"}
NO_DEPENDS = ("No dependencies are recorded: this chapter reads the repository's source text without running Lean, "
              "which edges between declarations need.")
LEAN_NAMES = 8  # the names a card's Lean row shows


def load(data: Path) -> dict | None:
    """data/stacks/'s source, structure and tag records, when they are there."""
    directory = data / "stacks"
    shards = sorted((directory / "tags").glob("*.json"))
    if not ((directory / "source.json").is_file() and (directory / "structure.json").is_file() and shards):
        return None
    tags = [record for shard in shards for record in json.loads(shard.read_text(encoding="utf-8"))["tags"]]
    return {"source": json.loads((directory / "source.json").read_text(encoding="utf-8")),
            "structure": json.loads((directory / "structure.json").read_text(encoding="utf-8")), "tags": tags}


def blob(source: dict, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{source['repo']}/blob/{source['rev']}/{path}" + (f"#L{line}" if line else "")


def at(rev: str, repo: str = REPO) -> str:
    return f"[{rev[:8]}]({GITHUB}/{repo}/tree/{rev})"


def tag_url(tag: str) -> str:
    return f"{STACKS_SITE}/tag/{tag}"


def comment(text: str) -> str:
    """An attribute's comment, on one line, as the page quotes it."""
    return ff.safe(" ".join(text.split()))


def reference(work: str, item: dict) -> str:
    """An EGA or SGA reference as the block names it, with its comment quoted."""
    if work == "ega":
        volume, number = ega(item["ref"])
        text = f"EGA {volume} ({number})"
    else:
        volume, exposé, number = sga(item["ref"])
        text = f"SGA {volume} {exposé} ({number})"
    return text + (f", “{comment(item['comment'])}”" if item["comment"] else "")


def references(block: dict) -> str:
    named = [reference(work, item) for work in ("ega", "sga") for item in block[work]]
    return ("References: " + "; ".join(named) + ".") if named else ""


def indefinite(words: str) -> str:
    return ("an " if words[:1] in "aeiou" else "a ") + words


def declaration_block(block: dict, source: dict) -> str:
    """A declaration's part of its tag's block: its name, kind, tier and line, its attribute's comment, its EGA
    and SGA references, its docstring and its Lean statement."""
    if block["name"]:
        name = f"**`{block['name']}`**, " + indefinite(("private " if block["private"] else "") + block["kind"])
    else:
        name = "**An instance with no name**"
    head = (f"{name} in {TIER_WORDS[block['tier']]}, declared in "
            f"[{block['file']}, line {block['line']}]({blob(source, block['file'], block['line'])}).")
    if "attribute_line" in block:
        where = block.get("attribute_file", block["file"])
        head += (f" The tag is given by the `attribute` command at [{where}, line {block['attribute_line']}]"
                 f"({blob(source, where, block['attribute_line'])}).")
    if block["sorry"]:
        head += " Its value contains `sorry`."
    if block["comment"]:
        head += f" The attribute's comment: “{comment(block['comment'])}”."
    parts = [" ".join(filter(None, [head, references(block)]))]
    if block["doc"]:
        parts.append(quote(block["doc"]))
    parts.append(fence(block["statement"]))
    return "\n\n".join(parts)


def registration_line(item: dict, source: dict) -> str:
    """A declaration registered for the tag, linked to Mathlib's documentation, or to its line when the repository
    declares it."""
    name = item["name"]
    if "declared" in item:
        target = f"[`{name}`]({blob(source, item['declared']['file'], item['declared']['line'])}), declared in the repository,"
    else:
        target = f"[`{name}`]({MATHLIB_DOCS.format(name)})"
    how = "an `attribute` command" if item.get("attribute") else "`add_to_stacks`"
    line = (f"- {target} registered with {how} in [{item['file']}, line {item['line']}]"
            f"({blob(source, item['file'], item['line'])}) ({item['tier']})")
    if item["comment"]:
        line += f": “{comment(item['comment'])}”"
    return line + "." + (f" {references(item)}" if references(item) else "")


def ordered(blocks: list[dict]) -> list[dict]:
    """A tag's declarations, StacksCore's first, each tier's by file and line."""
    return sorted(blocks, key=lambda block: (TIERS.index(block["tier"]), natural(block["file"]), block["line"]))


def tag_block(record: dict, place: dict, source: dict, site: bool) -> str:
    tag = record["tag"]
    kind = KIND_WORDS.get(place["kind"], f"a {place['kind']}") if place else ""
    lines = [f"## Tag {tag}" + (f", {kind}" if kind else ""), ""]
    links = f"[Tag {tag}]({tag_url(tag)}) in the Stacks Project"
    if site:
        links += f"; [its page]({SITE}library?tag={tag}) on the repository's site"
    lines.append(links + ".")
    for block in ordered(record["declarations"]):
        lines += ["", declaration_block(block, source)]
    if record["registrations"]:
        lines += ["", "Declarations registered for the tag:", ""]
        lines += [registration_line(item, source)
                  for item in sorted(record["registrations"], key=lambda item: (natural(item["file"]), item["line"]))]
    return "\n".join(lines)


def names_of(records: list[dict]) -> list[tuple[str, str]]:
    """The names an article's blocks give, in order, each once, with what a Lean row should link it to."""
    seen: dict[str, str] = {}
    for record in records:
        for block in ordered(record["declarations"]):
            if block["name"]:
                seen.setdefault(block["name"], f"{block['file']}#L{block['line']}")
        for item in record["registrations"]:
            seen.setdefault(item["name"], "")
    return list(seen.items())


def tally(records: list[dict]) -> Counter:
    counts: Counter = Counter()
    for record in records:
        counts["tags"] += 1
        for block in record["declarations"]:
            counts[block["tier"]] += 1
            counts["sorry"] += block["sorry"]
        counts["registrations"] += len(record["registrations"])
        counts["registered_here"] += sum("declared" in item for item in record["registrations"])
    return counts


def carried(counts: Counter) -> str:
    """What carries an article's or a chapter's tags, in words."""
    parts = []
    declarations = counts["StacksCore"] + counts["StacksFrontier"]
    if declarations:
        tiers = [f"{counts[name]:,} in {name}" for name in TIERS if counts[name]]
        parts.append(plural(declarations, "declaration") + " of the repository"
                     + (f" ({' and '.join(tiers)})" if len(tiers) > 1 else f", in {TIERS[0] if counts[TIERS[0]] else TIERS[1]}"))
    if counts["registrations"]:
        parts.append(plural(counts["registrations"], "registered declaration"))
    return " and ".join(parts)


def article(chapter: dict, section: dict | None, records: list[dict], places: dict, data: dict,
            links: dict[str, str]) -> Leaf:
    """A section's article: a line placing it, then a block per tag in the Stacks Project's order."""
    source = data["source"]
    site = bool(source.get("site", {}).get("tags"))
    counts = tally(records)
    if section:
        title = f"{chapter['number']}.{section['number']} {section['title']}"
        where = f"Section {chapter['number']}.{section['number']} of the Stacks Project" + (
            f", [Tag {section['tag']}]({tag_url(section['tag'])})" if section.get("tag") else "")
    else:
        title = f"{chapter['number']} {chapter['title']}: the chapter's own tag"
        where = f"The tag of Chapter {chapter['number']} of the Stacks Project as a whole"
    opening = (f"{where}. {plural(counts['tags'], 'tag')} here {'is' if counts['tags'] == 1 else 'are'} carried by "
               f"{carried(counts)}, quoted below from [{REPO}]({GITHUB}/{REPO}) at commit {at(source['rev'])}.")
    body = "\n\n".join([opening] + [tag_block(record, places.get(record["tag"]), source, site) for record in records])
    names = names_of(records)
    fields = [("declaration", "section"), ("origin", "cited")]
    if names:
        shown = names[:LEAN_NAMES]
        fields += [("lean", ", ".join(name for name, _ in shown)), ("statement", "formalized")]
        if not counts["sorry"]:
            fields.append(("proof", "formalized"))
        for name, line in shown:
            path, _, number = line.partition("#L")
            links[name] = blob(source, path, int(number)) if line else MATHLIB_DOCS.format(name)
    slug = slugify(f"{chapter['number']}-{section['number']} {section['title']}" if section else f"{chapter['number']}-0 chapter")
    leaf = Leaf(escape(title), slug, fields, body, no_depends=NO_DEPENDS)
    leaf.sources = ([(f"Section {chapter['number']}.{section['number']}, Tag {section['tag']}", tag_url(section["tag"]))]
                    if section and section.get("tag") else
                    [(f"Chapter {chapter['number']}, Tag {chapter['tag']}", tag_url(chapter["tag"]))] if chapter.get("tag") else [])
    leaf.sources.append((f"{REPO} at {source['rev'][:8]}", f"{GITHUB}/{REPO}/tree/{source['rev']}"))
    return leaf


def credit(source: dict) -> str:
    return (f"The docstrings and Lean statements are quoted from [{REPO}]({GITHUB}/{REPO}) at commit {at(source['rev'])}, "
            "under its Apache-2.0 license.")


def index_pages(work: str, articles: dict[str, tuple[str, Leaf]], tags: list[dict], total: int) -> tuple[Container, int]:
    """The EGA or SGA index, with the number of items it lists: a page per volume listing each item that a block's
    declaration carries, with the articles it is in and the comments it is carried with."""
    found: dict[str, dict[str, set[str]]] = {}  # ref -> article key -> comments
    for record in tags:
        if record["tag"] not in articles:
            continue
        key = articles[record["tag"]][0]
        for block in record["declarations"] + record["registrations"]:
            for item in block[work]:
                found.setdefault(item["ref"], {}).setdefault(key, set()).add(" ".join(item["comment"].split()))
    titles = {key: leaf.title for key, leaf in articles.values()}
    title = work.upper()
    pages = []
    for volume in EGA_VOLUMES if work == "ega" else SGA_VOLUMES:
        refs = sorted((ref for ref in found if ref.split()[0] == volume), key=natural)
        if not refs:
            continue
        lines, group = [], None
        for ref in refs:
            parsed = ega(ref) if work == "ega" else sga(ref)
            heading = (f"§{parsed[1].split('.')[0]}" if work == "ega" else
                       parsed[1] if volume == "4½" else f"Exposé {parsed[1]}")
            if heading != group:
                lines += ([""] if lines else []) + [f"### {heading}", ""]
                group = heading
            cited = ", ".join(
                f"[{titles[key]}](trough:{key})"
                + (" (" + "; ".join(f"“{ff.safe(text)}”" for text in sorted(comments) if text) + ")" if any(comments) else "")
                for key, comments in sorted(found[ref].items(), key=lambda pair: natural(pair[0])))
            lines.append(f"- ({parsed[-1]}): {cited}")
        page = Container(f"{title} {volume}", slugify(f"{work} {volume}"))
        page.prose = (f"The items of {title} {volume} that a declaration of an article carries, numbered as printed, "
                      "each with the articles it is in and the attribute's comments where there are any.\n\n"
                      + "\n".join(lines))
        pages.append(Entry(page))
    index = Container(title, work, pages)
    name = "Éléments de géométrie algébrique" if work == "ega" else "Séminaire de géométrie algébrique"
    index.prose = (f"The items of Grothendieck's *{name}* ({title}) that the declarations of this chapter's articles "
                   f"carry, {plural(len(found), 'item')}, on a page per volume. "
                   + (f"The repository carries {total - len(found):,} more on declarations without a Stacks tag, which "
                      "have no article here. " if total > len(found) else "")
                   + "The index links the articles, which live in their chapters.")
    return index, len(found)


def chapter(data: dict) -> tuple[Built, dict[str, str]]:
    """The chapter's root, with its articles and counts, and the links of the names its cards' Lean rows show (for
    hooks/lean-links.json). A part per Stacks Project part, a page per chapter, an article per section."""
    source, structure = data["source"], data["structure"]
    places = structure["tags"]
    by_section: dict[tuple[str, int], list[dict]] = {}
    unplaced = []
    for record in data["tags"]:
        place = places.get(record["tag"])
        if place is None:
            unplaced.append(record)
            continue
        by_section.setdefault((place["chapter"], place["section"]), []).append(record)
    for records in by_section.values():
        records.sort(key=lambda record: places[record["tag"]]["order"])
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    links: dict[str, str] = {}
    articles: dict[str, tuple[str, Leaf]] = {}  # by tag: its article's key and the article
    parts = []
    for part in structure["parts"]:
        pages = []
        for chap in part["chapters"]:
            sections = [(None, by_section[(chap["file"], 0)])] if (chap["file"], 0) in by_section else []
            sections += [(section, by_section[(chap["file"], section["number"])]) for section in chap["sections"]
                         if (chap["file"], section["number"]) in by_section]
            if not sections:
                continue
            page = Container(escape(f"{chap['number']} {chap['title']}"), slugify(f"{chap['number']} {chap['title']}"))
            counts: Counter = Counter()
            for section, records in sections:
                leaf = article(chap, section, records, places, data, links)
                key = f"stacks-{chap['file']}-{section['number'] if section else 0}"
                page.entries.append(Entry(leaf))
                targets[key] = leaf
                for record in records:
                    articles[record["tag"]] = (key, leaf)
                counts += tally(records)
            stats["articles"] += len(sections)
            stats.update(counts)
            named = f", [Tag {chap['tag']}]({tag_url(chap['tag'])})" if chap.get("tag") else ""
            if len(sections) > 1:
                which = (f"the {len(sections):,} sections of its {len(chap['sections']):,} with a tag that a declaration "
                         "carries, one article each, in the Stacks Project's order")
            else:
                which = f"{'its one section' if sections[0][0] else 'the chapter'} with a tag that a declaration carries"
            page.prose = (f"Chapter {chap['number']} of the Stacks Project, *{escape(chap['title'])}*{named}: {which}. "
                          f"Their {plural(counts['tags'], 'tag')} {'is' if counts['tags'] == 1 else 'are'} carried by "
                          f"{carried(counts)}.")
            chunk(page)
            pages.append(Entry(page))
            stats["chapters"] += 1
        if not pages:
            continue
        container = Container(escape(part["title"]), slugify(part["title"]), pages)
        container.prose = "\n\n".join([
            f"The {plural(len(pages), 'chapter')} of the Stacks Project's part *{escape(part['title'])}* with a tag that "
            f"a declaration carries, {'a page each, ' if len(pages) > 1 else ''}numbered as the Stacks Project numbers "
            "them.", credit(source)])
        chunk(container)
        parts.append(Entry(container))
        stats["parts"] += 1
    indexes = []
    for work in ("ega", "sga"):
        index, shown = index_pages(work, articles, data["tags"], source["counts"].get(f"{work}_items", 0))
        targets[f"stacks-{work}"] = index
        indexes.append(Entry(index))
        stats[f"{work}_indexed"] = shown
    stats["unplaced"] = len(unplaced)
    root = Container("The Stacks Project in Lean (Axiom)", "stacks", parts + indexes)
    root.prose = intro(data, stats)
    if unplaced:
        def carriers(record: dict) -> str:
            named = [f"[`{block['name']}`]({blob(source, block['file'], block['line'])})" if block["name"] else
                     f"[an instance with no name]({blob(source, block['file'], block['line'])})"
                     for block in ordered(record["declarations"])]
            return ", ".join(named + [f"`{item['name']}` (registered)" for item in record["registrations"]])

        root.tail = (f"Tags that the Stacks Project does not list at commit {at(structure['rev'], PROJECT)}, so with no "
                     "article: " + "; ".join(f"{record['tag']}, carried by {carriers(record)}" for record in unplaced) + ".")
    return Built(root, targets, {}, dict(stats), Counter()), dict(sorted(links.items()))


def without_invitations(text: str) -> str:
    """A description without its sentences that invite contributions, the cut marked with …."""
    sentences = re.split(r"(?<=[.!?])\s+", " ".join(text.split()))
    kept = [sentence for sentence in sentences if not re.search(r"\bwelcome\b|\bcontribut", sentence, re.I)]
    return " ".join(kept) + (" …" if len(kept) < len(sentences) else "")


def intro(data: dict, stats: Counter) -> str:
    source, structure = data["source"], data["structure"]
    counts = source["counts"]
    readme = source.get("readme", {})
    described = [f"{name} as “{ff.safe(readme['tiers'][name])}”" for name in TIERS if readme.get("tiers", {}).get(name)]
    tiers = f" It describes {' and '.join(described)}" if described else ""
    declarations = stats["StacksCore"] + stats["StacksFrontier"]
    here = (f", {stats['registered_here']:,} of them declared in the repository itself" if stats["registered_here"] else
            "")
    site = source.get("site", {})
    site_line = (f"The repository's site, {SITE}, links each tag to its Lean code; each block links the tag's page there."
                 if site.get("tags") else
                 f"The repository's site, {SITE}, links each tag to its Lean code, but its tag pages answer as missing "
                 "pages when fetched, so the blocks do not link them.")
    sorry = ("No declaration's value read here contains `sorry`, as the README says."
             if not counts.get("sorry") else
             f"{plural(counts['sorry'], 'declaration')} carrying a tag {'has' if counts['sorry'] == 1 else 'have'} a value "
             "that contains `sorry`; each block says so.")
    return "\n\n".join([
        f"[The Stacks Project in Lean]({GITHUB}/{REPO}), from Axiom Math, formalizes "
        f"[the Stacks Project]({STACKS_SITE}) in Lean on top of Mathlib, indexed by Stacks tag, with a site at {SITE}. "
        f"This chapter maps it as read at commit {at(source['rev'])} ({source['date'][:10]}), Lean toolchain "
        f"{source['toolchain']}, Mathlib {source.get('mathlib_version') or source['mathlib'][:8]}. The "
        "repository runs no continuous integration, so the commit is the newest of its main branch, not one a build "
        "is known to pass.",
        f"Its formalization.yaml describes it: “{ff.safe(without_invitations(source['project']['description']))}”"
        + (f" Its README: “{ff.safe(readme['structure'])}”" if readme.get("structure") else "") + tiers,
        ff.facts(source),
        f"There are {plural(stats['articles'], 'article')}, one for each section of the Stacks Project with a tag that a "
        f"declaration carries, in {plural(stats['chapters'], 'chapter')} and {plural(stats['parts'], 'part')} as the "
        f"Stacks Project orders them. They hold {plural(stats['tags'], 'tag')}, each a block listing the "
        f"{plural(declarations, 'declaration')} of the repository that carry it ({stats['StacksCore']:,} in StacksCore, "
        f"{stats['StacksFrontier']:,} in StacksFrontier) and the {plural(stats['registrations'], 'declaration')} "
        f"registered for it with `add_to_stacks` or an `attribute` command{here}. The README describes `add_to_stacks` as "
        "registering a tag that Mathlib already covers on the Mathlib declaration, and the blocks link the others to "
        "Mathlib's documentation. A declaration carrying several tags is in each tag's block. The repository "
        f"has {counts.get('files_StacksCore', 0):,} Lean files in StacksCore and {counts.get('files_StacksFrontier', 0):,} "
        "in StacksFrontier.",
        "No Lean is run for this chapter. Tags are read from the source text, as the attributes are written: a "
        "declaration carries a tag when the `@[...]` list right before it has `stacks TAG` or `stacks_fixed TAG`, or an "
        "`attribute [stacks TAG]` command names it; `add_to_stacks TAG name` registers a declaration outside the "
        "repository, which the block links to Mathlib's documentation. A declaration's name is read under the "
        "namespaces it sits in; an instance with no name is shown without one, and a `private` declaration under the "
        "name it is written with. Its Lean statement runs to the `:=` or `where` that starts its value, and its line "
        f"is the line its keyword is on. {sorry} The articles have no dependencies: edges between declarations need "
        "Lean.",
        f"The parts, chapters and sections, their numbers and titles, are the Stacks Project's, read from "
        f"[its repository]({GITHUB}/{PROJECT}) at commit {at(structure['rev'], PROJECT)}, and each tag is placed in the "
        "section its label is in there. The Stacks Project is under the GNU Free Documentation License, so its text is "
        "not quoted: each block links its tag's page at stacks.math.columbia.edu. " + site_line,
        f"Declarations also carry the items of EGA and SGA they prove, which the blocks note with the attribute's "
        f"comment as written; two indexes list them, [EGA](trough:stacks-ega) ({plural(stats['ega_indexed'], 'item')}) "
        f"and [SGA](trough:stacks-sga) ({plural(stats['sga_indexed'], 'item')}), of the {counts.get('ega_items', 0):,} "
        f"and {counts.get('sga_items', 0):,} the repository carries.",
        credit(source) + " Each declaration's line is linked.",
    ])
