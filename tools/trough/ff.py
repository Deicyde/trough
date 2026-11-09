"""The Formal Frontier chapter: one article per headline result that names a declaration the library has.

Formal Frontier publishes agent-written Lean libraries under
github.com/FormalFrontier, each with a formalization.yaml and a README whose
"Headline results" section lists what it proves. tools/refresh_ff.py reads each
library at a pinned commit into data/ff/<name>.json: the yaml's facts, its
`highlights` and `status.main_results`, and the README's headline results, and
for each named declaration whether the linked file declares it
(trough.leansource, which reads the source without Lean). The chapter has a part
per subject and a section per library; an article is a yaml highlight, or a
README item whose declaration link names a declaration its file has. The main
results are listed on the library's page, not made articles: in several
libraries they are close to the whole API.
"""

from __future__ import annotations

import json
import posixpath
import re
from collections import Counter
from pathlib import Path

from . import catalog, formalization, leansource
from .blueprints import Built, escape
from .mathlib import title_key
from .vault import Container, Entry, Leaf, chunk, safe_math_markdown, slugify, walk

SCHEMA = "trough-ff/v1"
ORG = "FormalFrontier"
GITHUB = "https://github.com"
HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
ITEM = re.compile(r"^(\s{0,3})([-*+]|\d{1,9}[.)])(\s+)(.*)$")
ANCHOR = re.compile(r'^\s*(<a id="[^"]*"></a>\s*)+$')
LINK = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*<?([^()\s<>]*(?:\([^()\s]*\)[^()\s<>]*)*)>?((?:\s+\"[^\"]*\")?)\s*\)")
CODE_LINK = re.compile(r"\[`([^`\]]+)`\]\(([^)\s]+)\)")
BOLD_LEAD = re.compile(r"^\s*\*\*(.+?)\*\*", re.S)
LEADING_LINK = re.compile(r"^\s*\[([^\]]+)\]\(([^)\s]+)\)")
ABBREVIATIONS = {"e.g.", "i.e.", "cf.", "resp.", "vs."}
# A related formalization's id: the repository, or a commit of it.
RELATED = re.compile(rf"https://github\.com/{ORG}/([^/]+?)(?:\.git)?(?:/(?:tree|commit)/[0-9a-f]+)?/?$")
# The automation statements of a method, quoted on the library's page.
AUTOMATION = ("method", "framework", "tool_setup", "prompting_notes", "notes")


def section(readme: str, title: str = "Headline results") -> list[str]:
    """The lines of the README's `## title` section, which ends at the next heading of level one or two."""
    out, inside, fence = [], False, None
    for line in readme.split("\n"):
        match = FENCE.match(line)
        if fence:
            if match and match.group(1)[0] == fence:
                fence = None
        elif match:
            fence = match.group(1)[0]
        elif (heading := HEADING.match(line)) and len(heading.group(1)) <= 2:
            if inside:
                break
            if heading.group(2).strip().lower() == title.lower():
                inside = True
                continue
        if inside:
            out.append(line)
    return out


def indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def blocks(lines: list[str]) -> list[tuple[str, str]]:
    """The section as ("heading", title), ("item", Markdown) and ("prose", Markdown) blocks, in order.
    An item is a top-level list entry with all its lines, dedented; prose is a paragraph, table or
    code block outside the lists."""
    out: list[tuple[str, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or ANCHOR.match(line):
            i += 1
            continue
        if (heading := HEADING.match(line)) and not FENCE.match(line):
            out.append(("heading", heading.group(2)))
            i += 1
            continue
        if item := ITEM.match(line):
            width = len(item.group(1)) + len(item.group(2)) + len(item.group(3))
            content = [item.group(4)]
            i += 1
            fence = None
            while i < len(lines):
                nxt = lines[i]
                if fence:
                    content.append(nxt[min(width, indent(nxt)):])
                    if FENCE.match(nxt) and FENCE.match(nxt).group(1)[0] == fence:
                        fence = None
                    i += 1
                    continue
                if not nxt.strip():
                    following = next((later for later in lines[i + 1:] if later.strip()), "")
                    if following and indent(following) >= 2:
                        content.append("")
                        i += 1
                        continue
                    break
                if indent(nxt) >= 2:
                    content.append(nxt[min(width, indent(nxt)):])
                elif ITEM.match(nxt) or HEADING.match(nxt) or FENCE.match(nxt) or ANCHOR.match(nxt):
                    break
                else:
                    content.append(nxt)  # a lazy continuation of the paragraph
                if FENCE.match(nxt):
                    fence = FENCE.match(nxt).group(1)[0]
                i += 1
            out.append(("item", "\n".join(content).strip()))
            continue
        paragraph = []
        fence = None
        while i < len(lines):
            nxt = lines[i]
            if fence:
                paragraph.append(nxt)
                if FENCE.match(nxt) and FENCE.match(nxt).group(1)[0] == fence:
                    fence = None
                i += 1
                continue
            if not nxt.strip() or ANCHOR.match(nxt) or (paragraph and (ITEM.match(nxt) or HEADING.match(nxt))):
                break
            if FENCE.match(nxt):
                fence = FENCE.match(nxt).group(1)[0]
            paragraph.append(nxt)
            i += 1
        out.append(("prose", "\n".join(paragraph).strip()))
    return out


class Links:
    """Resolves a README's links against one commit of one Formal Frontier repository."""

    def __init__(self, name: str, rev: str, paths: set[str]):
        self.name, self.rev = name, rev
        self.dirs = {"/".join(path.split("/")[:k]) for path in paths for k in range(1, path.count("/") + 1)}

    def resolve(self, url: str) -> str:
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("//"):
            return url
        root = f"{GITHUB}/{ORG}/{self.name}"
        path, _, fragment = url.partition("#")
        fragment = f"#{fragment}" if fragment else ""
        if not path:
            return f"{root}/blob/{self.rev}/README.md{fragment}"
        path = posixpath.normpath(path.lstrip("/"))
        if path.startswith(".."):
            return url
        if path == ".":
            return f"{root}/tree/{self.rev}{fragment}"
        return f"{root}/{'tree' if path in self.dirs else 'blob'}/{self.rev}/{path}{fragment}"

    def contents(self, url: str) -> bool:
        """Whether a link points into the README or docs/, as a table of contents' entries do."""
        resolved = self.resolve(url)
        for kind in ("blob", "tree"):
            prefix = f"{GITHUB}/{ORG}/{self.name}/{kind}/{self.rev}/"
            if resolved.startswith(prefix):
                path = resolved[len(prefix):].partition("#")[0]
                return path in ("README.md", "docs") or path.startswith("docs/")
        return False

    def file(self, url: str) -> str | None:
        """The repository path a resolved link names at this commit, if it names one."""
        prefix = f"{GITHUB}/{ORG}/{self.name}/blob/{self.rev}/"
        return url[len(prefix):].partition("#")[0] if url.startswith(prefix) else None

    def text(self, markdown: str) -> str:
        """The Markdown with each relative link made absolute."""
        def link(match: re.Match) -> str:
            return f"[{match.group(1)}]({self.resolve(match.group(2))}{match.group(3)})"

        return LINK.sub(link, markdown)


def sentence(text: str, limit: int = 140) -> tuple[str, bool, bool]:
    """The first sentence of Markdown text with its closing mark, cut at a word outside code spans when longer
    than *limit*; whether it was cut there; and whether any of the text is left out."""
    flat = " ".join(text.split())
    in_code, end, cut = False, len(flat), None
    for i, char in enumerate(flat):
        if char == "`":
            in_code = not in_code
        elif in_code:
            continue
        elif char == " " and i <= limit:
            cut = i
        elif char in ".:;" and (i + 1 == len(flat) or flat[i + 1] == " "):
            if flat[: i + 1].rsplit(" ", 1)[-1].lower() not in ABBREVIATIONS:
                end = i + 1
                break
    if end > limit and cut:
        return flat[:cut].rstrip(",;:"), True, True
    return flat[:end], False, end < len(flat)


def first_sentence(text: str, limit: int = 140) -> str:
    """The first sentence of Markdown text as a title: cut with " …" when long, and without its closing mark."""
    words, cut, _ = sentence(text, limit)
    return words + " …" if cut else re.sub(r"(?<!\.)[.:;]$", "", words)


def opening(text: str, limit: int = 140) -> str:
    """The first sentence of Markdown text as written, with " …" where the text goes on."""
    words, _, more = sentence(text, limit)
    return words + " …" if more else words


def item_link(paragraph: str, links: Links) -> dict | None:
    """The item's declaration link, the first code link in its first paragraph; else its last link
    into the repository."""
    if code := CODE_LINK.search(paragraph):
        return {"text": code.group(1), "url": links.resolve(code.group(2)), "code": True}
    local = [match for match in LINK.finditer(paragraph) if not re.match(r"[a-z][a-z0-9+.-]*:", match.group(2), re.I)]
    for match in reversed(local):
        if match.group(1).strip("`"):
            return {"text": match.group(1).strip("`"), "url": links.resolve(match.group(2)),
                    "code": match.group(1).startswith("`")}
    return None


def headline_item(markdown: str, links: Links, title: str | None = None) -> dict | None:
    """One headline result: its title, its text as written (Markdown, links absolute) and its declaration
    link; None for a table of contents' entry. The title is a bold lead, a leading link's label, a leading
    declaration link's name, or else the first sentence; `title_from` says which."""
    paragraph = markdown.split("\n\n", 1)[0]
    link = item_link(paragraph, links)
    title_from = "heading"
    if title is None:
        if bold := BOLD_LEAD.match(markdown):
            title, title_from = re.sub(r"(?<!\.)[.:;]$", "", " ".join(bold.group(1).split())), "bold"
        elif (lead := LEADING_LINK.match(markdown)) and not lead.group(1).startswith("`"):
            if lead.end() == len(markdown) and links.contents(lead.group(2)):
                return None  # only a link into the README or docs/, as a table of contents' entry is
            title, title_from = " ".join(lead.group(1).split()), "link"
        elif lead and link and link["code"] and lead.group(1) == f"`{link['text']}`":
            title, title_from = lead.group(1), "declaration"
        else:
            title, title_from = first_sentence(markdown), "sentence"
    title = LINK.sub(lambda match: match.group(1), title)  # a title is a link's label elsewhere
    declaration = None
    if link and link["code"] and leansource.is_name(link["text"]):
        file = links.file(link["url"])
        if file and file.endswith(".lean"):
            declaration = {"name": link["text"], "file": file}
    return {"kind": "item", "title": title, "title_from": title_from, "text": links.text(markdown.strip()),
            "link": link, "declaration": declaration}


def headlines(readme: str, links: Links) -> list[dict]:
    """The README's headline results in order: group headings, prose, and items. A heading with no
    list entries under it stands for one result, its prose the result's text, as on Formal Frontier's
    own dashboard."""
    parsed = blocks(section(readme))
    groups: list[tuple[str | None, list[tuple[str, str]]]] = [(None, [])]
    for kind, text in parsed:
        if kind == "heading":
            groups.append((text, []))
        else:
            groups[-1][1].append((kind, text))
    out: list[dict] = []
    for heading, members in groups:
        if heading is not None and not any(kind == "item" for kind, _ in members):
            if members:
                out.append(headline_item("\n\n".join(text for _, text in members), links, title=heading))
            continue
        if heading is not None:
            out.append({"kind": "heading", "title": heading})
        for kind, text in members:
            item = headline_item(text, links) if kind == "item" else {"kind": "prose", "text": links.text(text)}
            if item:
                out.append(item)
    return out


def depends(manifest: dict) -> tuple[list[dict], str]:
    """The Formal Frontier libraries the Lake manifest names directly, with their pinned commits, and
    Mathlib's commit."""
    libraries, mathlib = [], ""
    for package in manifest.get("packages", []):
        url = package.get("url", "")
        if package.get("name") == "mathlib":
            mathlib = package.get("rev", "")
        if package.get("inherited", False):
            continue
        if match := re.match(rf"https://github\.com/{ORG}/([^/]+?)(?:\.git)?/?$", url):
            libraries.append({"name": match.group(1), "rev": package.get("rev", "")})
    return sorted(libraries, key=lambda library: library["name"]), mathlib


def is_apache(license_text: str) -> bool:
    """Whether the text opens as the Apache License 2.0 does."""
    return " ".join(license_text.split()).startswith("Apache License Version 2.0, January 2004")


def facts_of(config: formalization.Formalization) -> dict:
    """What a formalization.yaml states about its project, as a record keeps it for facts() and literature():
    the project, review, automation and sources, each text on one line."""
    text = formalization.text_of
    return {
        "project": {"name": text(config.project.get("name")), "description": text(config.project.get("description")),
                    "authors": [text(author) for author in config.project.get("authors") or []]},
        "review": {"status": text(config.review.get("status")), "notes": text(config.review.get("notes")),
                   "reviewers": [text(reviewer) for reviewer in config.review.get("reviewers") or []]},
        "automation": {
            "methods": [{key: text(method.get(key)) for key in AUTOMATION if method.get(key)}
                        | ({"models": [text(model) for model in method["models"]]} if method.get("models") else {})
                        for method in config.automation.get("methods") or [] if isinstance(method, dict)],
            "notes": text(config.automation.get("notes")),
        },
        "sources": [{key: value for key, value in {
            "title": text(source.get("title")),
            "authors": [text(author) for author in source.get("authors") or []],
            "type": text(source.get("type")),
            "relationship": text(source.get("relationship")),
            "location": text(source.get("location")),
            "url": text(source.get("id")) if re.match(r"https?://", str(source.get("id") or "")) else "",
        }.items() if value} for source in config.sources],
    }


def read_library(checkout: Path, name: str, rev: str, date: str, paths: set[str]) -> dict:
    """A library's record at its commit: *paths* are every file the commit has. Raises ValueError when
    the library is not Apache-2.0, so none of its text is quoted."""
    config = formalization.load((checkout / "formalization.yaml").read_text(encoding="utf-8"),
                                f"{name}/formalization.yaml")
    license_name = formalization.text_of(config.project.get("license"))
    license_file = checkout / "LICENSE"
    if license_name != "Apache-2.0" or not license_file.is_file() or not is_apache(license_file.read_text(encoding="utf-8")):
        raise ValueError(f"not Apache-2.0 (formalization.yaml says {license_name!r})")
    manifest = checkout / "lake-manifest.json"
    deps, mathlib = depends(json.loads(manifest.read_text(encoding="utf-8"))) if manifest.is_file() else ([], "")
    toolchain = checkout / "lean-toolchain"
    links = Links(name, rev, paths)
    scans: dict[str, dict | None] = {}

    def named(declaration: str, file: str) -> dict:
        file = posixpath.normpath(file.lstrip("/"))
        if file not in scans:
            # Only a .lean file the commit has: a path out of the repository, or one it lacks, declares nothing.
            readable = file.endswith(".lean") and file in paths and (checkout / file).is_file()
            scans[file] = leansource.scan((checkout / file).read_text(encoding="utf-8")) if readable else None
        found = (scans[file] or {}).get(declaration)
        return {"name": declaration, "file": file,
                "found": {"line": found.line, "kind": found.kind, "stated": found.sorry} if found else None}

    readme = checkout / "README.md"
    items = headlines(readme.read_text(encoding="utf-8"), links) if readme.is_file() else []
    for item in items:
        if item.get("declaration"):
            item["declaration"] = named(item["declaration"]["name"], item["declaration"]["file"])
    text = formalization.text_of
    return {
        "schema": SCHEMA,
        "id": f"ff-{name}",
        "repo": f"{ORG}/{name}",
        "rev": rev,
        "date": date,
        "toolchain": toolchain.read_text(encoding="utf-8").strip().split(":")[-1] if toolchain.is_file() else "",
        "mathlib": mathlib,
        "license": license_name,
        **facts_of(config),
        "depends": deps,
        "related": [{"name": match.group(1), "relationship": text(item.get("relationship"))}
                    for item in config.related
                    if (match := RELATED.match(str(item.get("id") or "")))],
        "highlights": [{"title": highlight["title"], "statement": highlight["statement"],
                        "declarations": [named(item["declaration"], item["file"]) for item in highlight["declarations"]]}
                       for highlight in config.highlights],
        "headlines": items,
        "main_results": [named(text(result.get("declaration")), str(result.get("file") or ""))
                         | {key: value for key, value in {
                             "note": text(result.get("note")),
                             "sorry_count": result.get("sorry_count"),
                             "axioms": [text(axiom) for axiom in result.get("axioms") or []],
                         }.items() if value not in ("", None, [])}
                         for result in config.main_results if result.get("declaration")],
    }


def found_names(record: dict) -> set[str]:
    """The declaration names a library's record finds, for the refresh's drop check."""
    names = {item["name"] for highlight in record["highlights"] for item in highlight["declarations"] if item["found"]}
    names |= {item["declaration"]["name"] for item in record["headlines"]
              if item.get("declaration") and item["declaration"]["found"]}
    return names | {result["name"] for result in record["main_results"] if result["found"]}



# The chapter, from the records.

MATHLIB_REPO = "https://github.com/leanprover-community/mathlib4"
REPO_URL = f"{GITHUB}/{ORG}"
DASHBOARD = "https://formalfrontier.github.io"
CODE = re.compile(r"(?s)(`{3,}).*?\1|`[^`\n]*`")
# Past this much quoted README text, a library's headline results move to a page of their own.
QUOTE_LIMIT = 40_000
# Rows of the main-results table on one page.
TABLE_ROWS = 100
NO_DEPENDS = ("No dependencies are recorded: this chapter reads the libraries' source text without running Lean, "
              "which edges between declarations need.")


def load_libraries(data: Path, libraries: list[dict]) -> list[tuple[dict, dict]]:
    """Each Formal Frontier library of the catalog that has a record under data/ff/, with it."""
    out = []
    for library in libraries:
        path = data / "ff" / f"{library['repo'].split('/')[1]}.json"
        if library["group"] == "formal-frontier" and path.is_file():
            out.append((library, json.loads(path.read_text(encoding="utf-8"))))
    return out


def safe(markdown: str) -> str:
    """Quoted Markdown as a page can show it: a `<` outside code and formulas opens no HTML."""
    markdown = safe_math_markdown(markdown)
    out, last = [], 0
    for match in CODE.finditer(markdown):
        out += [re.sub(r"<(?=[A-Za-z/!?])", "&lt;", markdown[last:match.start()]), match.group()]
        last = match.end()
    return "".join(out) + re.sub(r"<(?=[A-Za-z/!?])", "&lt;", markdown[last:])


def blob(record: dict, path: str, line: int | None = None) -> str:
    return f"{GITHUB}/{record['repo']}/blob/{record['rev']}/{path}" + (f"#L{line}" if line else "")


def at(record: dict) -> str:
    return f"[{record['rev'][:8]}]({GITHUB}/{record['repo']}/tree/{record['rev']})"


def quoted(record: dict, what: str, file: str, anchor: str = "") -> str:
    return (f"*Quoted from {what} in [{file}]({blob(record, file)}{anchor}) of "
            f"[{record['repo']}]({GITHUB}/{record['repo']}) at commit {at(record)}, Apache-2.0.*")


def lean_note(record: dict, declarations: list[dict], missing: list[dict]) -> str:
    lines = []
    for item in declarations:
        found = item["found"]
        lines.append(f"- `{item['name']}` ({found['kind']}), declared in "
                     f"[{item['file']}, line {found['line']}]({blob(record, item['file'], found['line'])})"
                     + ("; its text there contains `sorry`, so it is stated without proof." if found["stated"] else "."))
    lines += [f"- `{item['name']}`, which it also names, is not found declared in [{item['file']}]"
              f"({blob(record, item['file'])})." for item in missing]
    return "\n".join(lines) + f"\n\nRead from the source at commit {at(record)}, without running Lean."


def article(record: dict, title: str, text: str, attribution: str, declarations: list[dict], missing: list[dict],
            source: tuple[str, str]) -> Leaf:
    """An article quoting a headline result, for its declarations the scan found."""
    fields = [("declaration", declarations[0]["found"]["kind"]), ("origin", "cited"),
              ("lean", ", ".join(item["name"] for item in declarations)), ("statement", "formalized")]
    if all(item["found"]["kind"] in ("theorem", "lemma") and not item["found"]["stated"] for item in declarations):
        fields.append(("proof", "formalized"))
    body = "\n\n".join(part for part in (safe(text), attribution) if part)
    leaf = Leaf(title, slugify(title), fields, body, notes=[("Lean", lean_note(record, declarations, missing))],
                no_depends=NO_DEPENDS)
    leaf.sources = [source] + [(f"Source of `{item['name']}` in {item['file']}",
                                blob(record, item["file"], item["found"]["line"])) for item in declarations]
    return leaf


def text_item(item: dict) -> str:
    """A headline result with no article, quoted as its README gives it; a heading that stands for a
    result keeps its heading."""
    if item.get("title_from") == "heading":
        return f"### {safe(item['title'])}\n\n{safe(item['text'])}"
    return safe(item["text"])


def article_text(item: dict) -> str:
    """The quoted text an article shows under its title: the item as written, less a bold lead that is the
    title and a link to its own declaration right after it, which the Lean section shows."""
    text = item["text"]
    if item.get("title_from") == "bold":
        text = BOLD_LEAD.sub("", text, count=1).lstrip(" :;,.—–-\n")
        text = without_lead_link(text, item["declaration"]["name"])
    return text


def cell(text: str) -> str:
    out, last = [], 0
    text = " ".join(text.split())
    for match in CODE.finditer(text):
        out += [text[last:match.start()].replace("|", "\\|"), match.group()]
        last = match.end()
    return safe("".join(out) + text[last:].replace("|", "\\|"))


def main_results_page(record: dict) -> Container | None:
    """The yaml's main results, each the scan finds with its line, on a page of their own, split into pages of
    TABLE_ROWS rows when longer."""
    results = record["main_results"]
    if not results:
        return None
    rows = []
    for result in results:
        if not result["found"]:
            continue
        note = [result.get("note", "")]
        if "sorry_count" in result:
            note.append(f"Sorry count {result['sorry_count']}.")
        if result.get("axioms"):
            note.append("Axioms: " + ", ".join(f"`{axiom}`" for axiom in result["axioms"]) + ".")
        where = f"[{result['file']}, line {result['found']['line']}]({blob(record, result['file'], result['found']['line'])})"
        rows.append(f"| `{result['name']}` | {result['found']['kind']} | {where} | {cell(' '.join(filter(None, note)))} |")
    header = ["| Declaration | Kind | Where | Note |", "| --- | --- | --- | --- |"]
    credit = quoted(record, "the main results", "formalization.yaml")
    missing = len(results) - len(rows)
    lines = [f"The main results that the formalization.yaml of [{record['repo']}]({GITHUB}/{record['repo']}) lists "
             f"under `status.main_results` at commit {at(record)}, each that the scan finds declared in the file the "
             "yaml gives, with its line. They are listed here, not made articles: in several Formal Frontier libraries "
             "this list is close to the whole API. The notes are the yaml's."]
    if missing:
        lines += ["", f"The scan does not find {missing} of them; [the library's page](../README.md) names "
                  f"{'it' if missing == 1 else 'them'}."]
    page = Container("Main results", "main-results")
    if len(rows) <= TABLE_ROWS:
        page.prose = "\n".join(lines + ([""] + header + rows if rows else []) + ["", credit])
        return page
    page.prose = "\n".join(lines + ["", credit])
    for number, start in enumerate(range(0, len(rows), TABLE_ROWS), 1):
        part = Container(f"Main results {start + 1} to {min(start + TABLE_ROWS, len(rows))}", f"part-{number:02d}")
        part.prose = "\n".join(header + rows[start:start + TABLE_ROWS] + ["", credit])
        page.entries.append(Entry(part))
    return page


def main_results_summary(record: dict) -> str:
    results = record["main_results"]
    missing = [result for result in results if not result["found"]]
    text = (f"Its formalization.yaml lists {len(results):,} main {'result' if len(results) == 1 else 'results'}, and "
            f"the scan finds {len(results) - len(missing):,} of them declared in the file the yaml gives; they are on "
            "their own page, not made articles.")
    if missing:
        text += (" The scan does not find " + ", ".join(
            f"`{result['name']}` ([{result['file']}]({blob(record, result['file'])}))" for result in missing) + ".")
    return f"## Main results\n\n{text}"


def builds_on(record: dict) -> dict[str, str]:
    """The Formal Frontier libraries this one builds on, each with where that is recorded."""
    out = {dep["name"]: f"a Lake dependency, pinned at {dep['rev'][:8]}" for dep in record["depends"]}
    for item in record["related"]:
        if item["relationship"] == "builds-on":
            out.setdefault(item["name"], "named in its formalization.yaml")
    return out


def library_link(name: str, chapter: set[str], titles: dict[str, str]) -> str:
    if name in chapter:
        return f"[{escape(titles[name])}](trough:ff-{name})"
    return f"[{ORG}/{name}]({REPO_URL}/{name})"


def facts(record: dict) -> str:
    rows = [f"- Repository: [{record['repo']}]({GITHUB}/{record['repo']}), read at commit {at(record)}"
            + (f" ({record['date'][:10]})." if record["date"] else "."),
            f"- Lean toolchain {record['toolchain']}"
            + (f", Mathlib at [{record['mathlib'][:8]}]({MATHLIB_REPO}/tree/{record['mathlib']})." if record["mathlib"] else "."),
            f"- License: {record['license']}.",
            f"- Authors: {', '.join(record['project']['authors'])}.",
            f"- Review status: “{safe(record['review']['status'])}”."]
    if record["review"]["notes"]:
        rows.append(f"- Review notes: “{safe(record['review']['notes'])}”")
    if record["review"].get("reviewers"):
        rows.append("- Reviewers: " + ", ".join(f"“{safe(reviewer)}”" for reviewer in record["review"]["reviewers"]) + ".")
    for method in record["automation"]["methods"]:
        parts = [f"- Automation: {method.get('method', '')}"]
        for key, label in (("framework", "framework"), ("models", "models"), ("tool_setup", "tool setup"),
                           ("prompting_notes", "prompting notes"), ("notes", "notes")):
            if method.get(key):
                values = method[key] if isinstance(method[key], list) else [method[key]]
                parts.append(f"{label} " + ", ".join(f"“{safe(value)}”" for value in values))
        rows.append("; ".join(parts))
    if record["automation"]["notes"]:
        rows.append(f"- Automation notes: “{safe(record['automation']['notes'])}”")
    return "\n".join(["## Facts", "", "From the repository and its formalization.yaml; the review and automation "
                      "statements are quoted as written.", "", *rows])


def literature(record: dict) -> str:
    lines = []
    for source in record["sources"]:
        title = escape(source.get("title") or "Untitled")
        head = f"[{title}]({source['url']})" if source.get("url") else f"*{title}*"
        details = [", ".join(source.get("authors", [])), source.get("location", "").rstrip(".")]
        kind = "; ".join(filter(None, [source.get("type", ""), source.get("relationship", "")]))
        lines.append(f"- {head}" + "".join(f", {safe(detail)}" for detail in details if detail)
                     + (f" ({kind})" if kind else "") + ".")
    return "\n".join(["## Literature", "", "The sources its formalization.yaml names, with their relationship to it.",
                      "", *lines]) if lines else ""


def names_module(declaration: dict) -> bool:
    """Whether a declaration link names its file's module, or the module's last components, as many do."""
    module = declaration["file"].removesuffix(".lean").replace("/", ".")
    return module == declaration["name"] or module.endswith("." + declaration["name"])


def without_lead_link(text: str, name: str) -> str:
    """An item's text without a leading link to its declaration, which the article shows anyway."""
    return re.sub(rf"^\(\[`{re.escape(name)}`\]\([^)\s]+\)\)\.?\s*", "", text)


def plural(number: int, word: str) -> str:
    return f"{number} {word}" if number == 1 else f"{number} {word}s"


def credit_parts(container: Container, carries: dict[int, str], tail_kind: str, line: str) -> None:
    """Put *line* on each part page of *container* that holds quoted README text but not the heading crediting it."""
    for part in walk(container):
        if isinstance(part, Container) and part is not container and part.navigation == "transparent":
            kinds = {carries.get(id(entry)) for entry in part.entries}
            if part.tail:
                kinds.add(tail_kind)
            if "text" in kinds and "heading" not in kinds:
                part.prose = line


def library_section(record: dict, chapter: set[str], titles: dict[str, str],
                    used_by: list[str]) -> tuple[Container, dict[str, str], Counter]:
    """A library's page and articles, the source links of its articles' declarations, and its counts."""
    name = record["repo"].split("/")[1]
    section = Container(escape(titles[name]), name)
    headlines = Container("Headline results", "headline-results")
    stats: Counter = Counter()
    leaves: dict[str, Leaf] = {}
    links: dict[str, str] = {}
    readme = "README.md", "#headline-results"
    readme_quoted = quoted(record, "the headline results", *readme)
    # Which entries carry quoted README text before them, and whether that text opens with the heading that
    # credits it: a part page holding such text without the heading credits it again.
    carries: dict[int, str] = {}
    pending: list[str] = []
    pending_kind = ""

    def mark(kind: str) -> None:
        nonlocal pending_kind
        pending_kind = "heading" if "heading" in (kind, pending_kind) else kind

    def add(target: Container, leaf: Leaf | None, declarations: list[dict], label: str | None = None) -> None:
        nonlocal pending, pending_kind
        if leaf is None:
            entry = Entry(leaves[declarations[0]["name"]], owned=False, label=label, before="\n\n".join(pending))
        else:
            entry = Entry(leaf, before="\n\n".join(pending))
            for item in declarations:
                leaves.setdefault(item["name"], leaf)
                links[item["name"]] = blob(record, item["file"], item["found"]["line"])
        target.entries.append(entry)
        if pending_kind:
            carries[id(entry)] = pending_kind
        pending, pending_kind = [], ""

    if record["highlights"]:
        pending.append("## Highlights")
    for highlight in record["highlights"]:
        found = [item for item in highlight["declarations"] if item["found"]]
        missing = [item for item in highlight["declarations"] if not item["found"]]
        if not found:
            stats["highlights_not_found"] += 1
            pending += [f"**{escape(highlight['title'])}.** {safe(highlight['statement'])}",
                        quoted(record, "the highlights", "formalization.yaml")]
            continue
        stats["highlight_articles"] += 1
        add(section, article(record, escape(highlight["title"]), highlight["statement"],
                             quoted(record, "the highlights", "formalization.yaml"), found, missing,
                             (f"{name} at {record['rev'][:8]}: formalization.yaml", blob(record, "formalization.yaml"))),
            found)
    highlight_text, pending = pending, []
    for item in record["headlines"]:
        if item["kind"] == "heading":
            pending.append(f"### {safe(item['title'])}")
            mark("text")
        elif item["kind"] == "prose":
            pending.append(safe(item["text"]))
            mark("text")
        else:
            stats["headline_items"] += 1
            declaration = item.get("declaration")
            if not declaration or not declaration["found"]:
                stats["headline_unnamed" if not declaration else "headline_not_found"] += 1
                stats["headline_module_links"] += bool(declaration) and names_module(declaration)
                pending.append(text_item(item))
                mark("text")
            elif declaration["name"] in leaves:
                stats["headline_duplicates"] += 1
                add(headlines, None, [declaration], label=item["title"])
            else:
                stats["headline_articles"] += 1
                add(headlines, article(record, item["title"] or f"`{declaration['name']}`",
                                       article_text(item), readme_quoted,
                                       [declaration], [],
                                       (f"{name} at {record['rev'][:8]}: README, headline results",
                                        blob(record, readme[0]) + readme[1])),
                    [declaration])
    tail, tail_kind = pending, pending_kind
    articles = stats["highlight_articles"] + stats["headline_articles"]
    stats["articles"] = articles
    stats["libraries_without_articles"] = int(not articles)
    stats["main_results"] = len(record["main_results"])
    stats["main_results_found"] = sum(1 for result in record["main_results"] if result["found"])
    quoted_items = stats["headline_unnamed"] + stats["headline_not_found"]
    own_page = sum(len(entry.before) for entry in headlines.entries) + sum(map(len, tail)) > QUOTE_LIMIT
    if own_page:
        # A long README's headline results get a page of their own, which chunk() splits as it needs.
        headlines.prose, headlines.tail = readme_quoted, "\n\n".join(tail)
        chunk(headlines)
        credit_parts(headlines, carries, tail_kind, readme_quoted)
        section.entries.append(Entry(headlines, before="\n\n".join(highlight_text + [
            "## Headline results",
            f"The {plural(stats['headline_items'], 'headline result')} of its README are on a page of their own: "
            f"{plural(stats['headline_articles'], 'article')}, {quoted_items} quoted as text"
            + (f", and {stats['headline_duplicates']} that {'links' if stats['headline_duplicates'] == 1 else 'link'} "
               "an article above." if stats["headline_duplicates"] else ".")])))
    else:
        lead = highlight_text + (["## Headline results", readme_quoted] if record["headlines"] else [])
        if headlines.entries:
            first = headlines.entries[0]
            first.before = "\n\n".join(lead + ([first.before] if first.before else []))
            if record["headlines"]:
                carries[id(first)] = "heading"
            section.entries += headlines.entries
        else:
            tail = lead + tail
            tail_kind = "heading" if record["headlines"] else tail_kind
        section.tail = "\n\n".join(tail)
    if articles:
        kinds = [text for number, text in (
            (stats["highlight_articles"], f"{stats['highlight_articles']} for highlights of its formalization.yaml "
                                          "whose declarations the scan finds"),
            (stats["headline_articles"], f"{stats['headline_articles']} for headline results in its README whose "
                                         "declaration link names a declaration the scan finds in the linked file")) if number]
        count = (f"{plural(articles, 'article')}: {' and '.join(kinds)}."
                 + ("" if not quoted_items else
                    " Its other headline results are quoted where they stand." if stats["headline_articles"] else
                    " The headline results in its README are quoted where they stand."))
    else:
        absent = []
        if stats["highlights_not_found"]:
            absent.append(f"none of the {plural(stats['highlights_not_found'], 'highlight')} of its formalization.yaml "
                          "names a declaration the scan finds")
        elif not record["highlights"]:
            absent.append("its formalization.yaml lists no highlights")
        absent.append(f"none of its {plural(stats['headline_items'], 'headline result')} links a declaration that "
                      "the scan finds in the linked file at this commit")
        count = (f"No articles: {', and '.join(absent)}, so they are quoted "
                 + ("on a page of their own." if own_page else "below."))
    builds = builds_on(record)
    graph = ["## Builds on", "", *(f"- {library_link(other, chapter, titles)} ({how})" for other, how in sorted(builds.items()))
             ] if builds else ["## Builds on", "", "No other Formal Frontier library."]
    if used_by:
        graph += ["", "## Used by", "", *(f"- {library_link(other, chapter, titles)}" for other in sorted(used_by))]
    section.prose = "\n\n".join(part for part in [
        f"> {safe(record['project']['description'])}",
        quoted(record, "the project description", "formalization.yaml"),
        count,
        facts(record),
        literature(record),
        "\n".join(graph),
    ] if part)
    chunk(section)
    credit_parts(section, carries, tail_kind, readme_quoted)
    page = main_results_page(record)
    if page:
        # After the README text a short library keeps below its articles, or after the parts of a long one.
        section.entries.append(Entry(page, before="\n\n".join(
            part for part in (section.tail, main_results_summary(record)) if part)))
        section.tail = ""
    return section, links, stats


def chapter(pairs: list[tuple[dict, dict]]) -> tuple[Built, list[tuple[Container, dict[str, str], Counter]]]:
    """The chapter's root, with its articles and counts, and each library's page with the source links of its
    articles' declarations (for hooks/lean-links.json) and its counts. A part per subject, a section per library."""
    names = {record["repo"].split("/")[1]: (library, record) for library, record in pairs}
    titles = {name: library["name"] for name, (library, _) in names.items()}
    used_by: dict[str, list[str]] = {name: [] for name in names}
    for name, (_, record) in names.items():
        for other in builds_on(record):
            used_by.setdefault(other, []).append(name)
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    built: list[tuple[Container, dict[str, str], Counter]] = []
    by_subject: dict[str, list[Container]] = {subject: [] for subject in catalog.SUBJECTS}
    for name, (library, record) in names.items():
        section, links, counts = library_section(record, set(names), titles, used_by[name])
        stats.update(counts)
        stats["libraries"] += 1
        targets[library["id"]] = section
        built.append((section, links, counts))
        by_subject[library["subject"]].append(section)
    parts = []
    for subject, sections in by_subject.items():
        if not sections:
            continue
        sections.sort(key=lambda section: title_key(section.title))
        part = Container(subject, slugify(subject), [Entry(section) for section in sections])
        part.prose = f"The Formal Frontier libraries on {subject[:1].lower() + subject[1:]}, one section each."
        parts.append(Entry(part))
    root = Container("Formal Frontier", "formal-frontier", parts)
    root.prose = intro(stats)
    overview = ["## The libraries", "", "Each with its number of articles and the opening of its description, quoted "
                "from its formalization.yaml at its pinned commit, shortened with … where it is cut."]
    counts_of = {id(section): counts for section, _, counts in built}
    for subject, sections in by_subject.items():
        if sections:
            overview += ["", f"### {subject}", ""]
            for section in sections:
                library, record = names[section.slug]
                lead = opening(record["project"]["description"])
                overview.append(f"- [{section.title}](trough:{library['id']}) "
                                f"({plural(counts_of[id(section)]['articles'], 'article')}): {safe(lead)}")
    root.tail = "\n".join(overview)
    return Built(root, targets, {}, dict(stats), Counter()), built


def intro(stats: Counter) -> str:
    unnamed, not_found, duplicates = stats["headline_unnamed"], stats["headline_not_found"], stats["headline_duplicates"]
    highlights = f"one for each highlight in a library's formalization.yaml whose declarations the scan finds " \
                 f"({stats['highlight_articles']})"
    if stats["highlights_not_found"]:
        highlights += f"; {plural(stats['highlights_not_found'], 'highlight')} name no declaration it finds"
    return "\n\n".join([
        f"[Formal Frontier]({REPO_URL}) publishes Lean libraries written by AI agents (“Formal Frontier Agents”, as "
        f"their formalization.yaml files name the authors), with a dashboard at {DASHBOARD}. This chapter maps the "
        f"{stats['libraries']} libraries in trough's catalog, each read at a pinned commit: a part per subject and a "
        "section per library. A library's page quotes its formalization.yaml (its description, review and automation "
        "statements), links the Formal Frontier libraries it builds on and those that build on it, quotes the headline "
        "results of its README, and links a page listing the main results its formalization.yaml declares.",
        f"There are {stats['articles']} articles: {highlights}, and one for each headline result in its README whose "
        "declaration link names a declaration that the scan finds in the linked file at the pinned commit "
        f"({stats['headline_articles']}). Of the {stats['headline_items']} headline results, {unnamed} link no "
        f"declaration; {not_found} link a name the scan does not find in the linked file, {stats['headline_module_links']} "
        f"of them the file's module rather than a declaration; and {duplicates} link a declaration that already has an "
        "article, which the library's page links in their place. The first two kinds have no article and stay as "
        f"quoted text on the library's page. {stats['libraries_without_articles']} libraries have no articles. The main "
        "results are not made articles: in several libraries they are close to the whole API.",
        "No Lean is run for this chapter. Whether a file declares a name is read from its source text, following "
        "`namespace`, `section` and `end`; a name counts only when a declaration command in that file names it in full "
        "under the right namespace, so a name given relative to an open namespace, or one Lean generates (an additive "
        "version, a constructor), is left out rather than guessed, and so is a `private` declaration. Articles have no "
        "dependencies: edges between declarations need Lean. A declaration whose text in the file contains `sorry` is "
        "marked as stated without proof; a dependency on an unproved declaration elsewhere is not checked.",
        "The quoted text is the libraries', under their Apache-2.0 license, with the repository and commit named where "
        "it is quoted.",
    ])
