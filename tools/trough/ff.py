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

    def file(self, url: str) -> str | None:
        """The repository path a resolved link names at this commit, if it names one."""
        prefix = f"{GITHUB}/{ORG}/{self.name}/blob/{self.rev}/"
        return url[len(prefix):].partition("#")[0] if url.startswith(prefix) else None

    def text(self, markdown: str) -> str:
        """The Markdown with each relative link made absolute."""
        def link(match: re.Match) -> str:
            return f"[{match.group(1)}]({self.resolve(match.group(2))}{match.group(3)})"

        return LINK.sub(link, markdown)


def first_sentence(text: str, limit: int = 140) -> str:
    """The first sentence of Markdown text, cut at a word outside code spans."""
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
    sentence = flat[:end]
    if len(sentence) > limit and cut:
        sentence = flat[:cut].rstrip(",;:") + " …"
    return re.sub(r"(?<!\.)[.:;]$", "", sentence)


def capitalize(text: str) -> str:
    return text[:1].upper() + text[1:] if text[:1].islower() else text


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


def headline_item(markdown: str, links: Links, title: str | None = None) -> dict:
    """One headline result: its title, its text (Markdown, links absolute) and its declaration link.
    A bold lead or a leading file link is the title; after a leading declaration link, the name is."""
    paragraph = markdown.split("\n\n", 1)[0]
    link = item_link(paragraph, links)
    text = markdown
    in_text = False  # the title is the text's first sentence, so a page shows the text alone
    if title is None:
        if bold := BOLD_LEAD.match(markdown):
            title = re.sub(r"(?<!\.)[.:;]$", "", " ".join(bold.group(1).split()))
            text = markdown[bold.end():].lstrip(" :;,.—–-\n")
        elif (lead := LEADING_LINK.match(markdown)) and not lead.group(1).startswith("`"):
            title = " ".join(lead.group(1).split())
            text = markdown[lead.end():].lstrip(" :;,.—–-\n")
        elif lead and link and link["code"] and lead.group(1) == f"`{link['text']}`":
            title = lead.group(1)
            text = capitalize(markdown[lead.end():].lstrip(" :;,.—–-\n"))
        else:
            title, in_text = first_sentence(markdown), True
    title = LINK.sub(lambda match: match.group(1), title)  # a title is a link's label elsewhere
    declaration = None
    if link and link["code"] and leansource.is_name(link["text"]):
        file = links.file(link["url"])
        if file and file.endswith(".lean"):
            declaration = {"name": link["text"], "file": file}
    return {"kind": "item", "title": title, "text": links.text(text.strip()), "link": link,
            "declaration": declaration} | ({"title_in_text": True} if in_text else {})


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
            out.append(headline_item(text, links) if kind == "item" else {"kind": "prose", "text": links.text(text)})
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
    head = " ".join(license_text.split()[:12])
    return "Apache License" in head and "Version 2.0" in head


def read_library(checkout: Path, name: str, rev: str, date: str, paths: set[str]) -> dict:
    """A library's record at its commit: *paths* are every file the commit has. Raises ValueError when
    the library is not Apache-2.0, so none of its text is quoted."""
    config = formalization.load((checkout / "formalization.yaml").read_text(encoding="utf-8"),
                                f"{name}/formalization.yaml")
    license_name = formalization.text_of(config.project.get("license"))
    license_file = checkout / "LICENSE"
    if license_name != "Apache-2.0" or not license_file.is_file() or not is_apache(license_file.read_text(encoding="utf-8")):
        raise ValueError(f"{name}: not Apache-2.0 (formalization.yaml says {license_name!r})")
    manifest = checkout / "lake-manifest.json"
    deps, mathlib = depends(json.loads(manifest.read_text(encoding="utf-8"))) if manifest.is_file() else ([], "")
    toolchain = checkout / "lean-toolchain"
    links = Links(name, rev, paths)
    scans: dict[str, dict | None] = {}

    def named(declaration: str, file: str) -> dict:
        file = posixpath.normpath(file.lstrip("/"))
        if file not in scans:
            path = checkout / file
            scans[file] = leansource.scan(path.read_text(encoding="utf-8")) if file.endswith(".lean") and path.is_file() else None
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
        "project": {"name": text(config.project.get("name")), "description": text(config.project.get("description")),
                    "authors": [text(author) for author in config.project.get("authors") or []]},
        "review": {"status": text(config.review.get("status")), "notes": text(config.review.get("notes"))},
        "automation": {
            "methods": [{key: text(method.get(key)) for key in ("method", "framework", "tool_setup") if method.get(key)}
                        | ({"models": [text(model) for model in method["models"]]} if method.get("models") else {})
                        for method in config.automation.get("methods") or [] if isinstance(method, dict)],
            "notes": text(config.automation.get("notes")),
        },
        "scope": text(config.status.get("scope")),
        "sources": [{key: value for key, value in {
            "title": text(source.get("title")),
            "authors": [text(author) for author in source.get("authors") or []],
            "type": text(source.get("type")),
            "relationship": text(source.get("relationship")),
            "location": text(source.get("location")),
            "url": text(source.get("id")) if re.match(r"https?://", str(source.get("id") or "")) else "",
        }.items() if value} for source in config.sources],
        "depends": deps,
        "related": [{"name": match.group(1), "relationship": text(item.get("relationship"))}
                    for item in config.related
                    if (match := re.match(rf"https://github\.com/{ORG}/([^/]+?)(?:\.git)?/?$", str(item.get("id") or "")))],
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
    """A headline result with no article, quoted as its README gives it."""
    if item.get("title_in_text"):
        return safe(item["text"])
    title = item["title"] if re.search(r"[.?!]$", item["title"]) else f"{item['title']}."
    return safe(f"**{title}** {item['text']}".strip())


def cell(text: str) -> str:
    out, last = [], 0
    text = " ".join(text.split())
    for match in CODE.finditer(text):
        out += [text[last:match.start()].replace("|", "\\|"), match.group()]
        last = match.end()
    return safe("".join(out) + text[last:].replace("|", "\\|"))


def main_results(record: dict) -> str:
    """The yaml's main results as a table, with those the scan does not find named after it."""
    results = record["main_results"]
    if not results:
        return ""
    found = [result for result in results if result["found"]]
    missing = [result for result in results if not result["found"]]
    lines = ["## Main results", "",
             f"The {len(results):,} main results its formalization.yaml lists (`status.main_results`). They are "
             "listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API."]
    if found:
        lines += ["", "| Declaration | Kind | Where | Note |", "| --- | --- | --- | --- |"]
        for result in found:
            note = [result.get("note", "")]
            if "sorry_count" in result:
                note.append(f"Sorry count {result['sorry_count']}.")
            if result.get("axioms"):
                note.append("Axioms: " + ", ".join(f"`{axiom}`" for axiom in result["axioms"]) + ".")
            where = f"[{result['file']}, line {result['found']['line']}]({blob(record, result['file'], result['found']['line'])})"
            lines.append(f"| `{result['name']}` | {result['found']['kind']} | {where} | {cell(' '.join(filter(None, note)))} |")
    if missing:
        lines += ["", f"The scan does not find {len(missing)} of them declared in the file the yaml gives: "
                  + ", ".join(f"`{result['name']}` ([{result['file']}]({blob(record, result['file'])}))" for result in missing)
                  + "."]
    return "\n".join(lines)


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
            f"- Review status: “{safe(record['review']['status'])}”"]
    if record["review"]["notes"]:
        rows.append(f"- Review notes: “{safe(record['review']['notes'])}”")
    for method in record["automation"]["methods"]:
        parts = [f"- Automation: {method.get('method', '')}"]
        if method.get("framework"):
            parts.append(f"framework “{safe(method['framework'])}”")
        if method.get("models"):
            parts.append("models " + ", ".join(f"“{safe(model)}”" for model in method["models"]))
        if method.get("tool_setup"):
            parts.append(f"tool setup “{safe(method['tool_setup'])}”")
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
        details = [", ".join(source.get("authors", [])), source.get("location", "")]
        kind = "; ".join(filter(None, [source.get("type", ""), source.get("relationship", "")]))
        lines.append(f"- {head}" + "".join(f", {safe(detail)}" for detail in details if detail)
                     + (f" ({kind})" if kind else "") + ".")
    return "\n".join(["## Literature", "", "The sources its formalization.yaml names, with their relationship to it.",
                      "", *lines]) if lines else ""


def library_section(record: dict, chapter: set[str], titles: dict[str, str],
                    used_by: list[str]) -> tuple[Container, dict[str, str], Counter]:
    """A library's page and articles, the source links of its articles' declarations, and its counts."""
    name = record["repo"].split("/")[1]
    section = Container(escape(titles[name]), name)
    stats: Counter = Counter()
    leaves: dict[str, Leaf] = {}
    links: dict[str, str] = {}
    pending: list[str] = []

    def add(leaf: Leaf | None, declarations: list[dict], label: str | None = None) -> None:
        nonlocal pending
        if leaf is None:
            leaf = leaves[declarations[0]["name"]]
            section.entries.append(Entry(leaf, owned=False, label=label, before="\n\n".join(pending)))
        else:
            section.entries.append(Entry(leaf, before="\n\n".join(pending)))
            for item in declarations:
                leaves.setdefault(item["name"], leaf)
                links[item["name"]] = blob(record, item["file"], item["found"]["line"])
        pending = []

    if record["highlights"]:
        pending.append("## Highlights")
    for highlight in record["highlights"]:
        found = [item for item in highlight["declarations"] if item["found"]]
        missing = [item for item in highlight["declarations"] if not item["found"]]
        if not found:
            stats["highlights_not_found"] += 1
            pending.append(text_item({"title": escape(highlight["title"]), "text": highlight["statement"]}))
            continue
        stats["highlight_articles"] += 1
        add(article(record, escape(highlight["title"]), highlight["statement"],
                    quoted(record, "the highlights", "formalization.yaml"), found, missing,
                    (f"{name} at {record['rev'][:8]}: formalization.yaml", blob(record, "formalization.yaml"))), found)
    if record["headlines"]:
        pending.append("## Headline results")
    readme = "README.md", "#headline-results"
    for item in record["headlines"]:
        if item["kind"] == "heading":
            pending.append(f"### {safe(item['title'])}")
        elif item["kind"] == "prose":
            pending.append(safe(item["text"]))
        else:
            stats["headline_items"] += 1
            declaration = item.get("declaration")
            if not declaration:
                stats["headline_unnamed"] += 1
                pending.append(text_item(item))
            elif not declaration["found"]:
                stats["headline_not_found"] += 1
                pending.append(text_item(item))
            elif declaration["name"] in leaves:
                stats["headline_duplicates"] += 1
                add(None, [declaration], label=item["title"])
            else:
                stats["headline_articles"] += 1
                add(article(record, item["title"] or f"`{declaration['name']}`", item["text"],
                            quoted(record, "the headline results", *readme), [declaration], [],
                            (f"{name} at {record['rev'][:8]}: README, headline results", blob(record, readme[0]) + readme[1])),
                    [declaration])
    articles = stats["highlight_articles"] + stats["headline_articles"]
    stats["articles"] = articles
    stats["libraries_without_articles"] = int(not articles)
    stats["main_results"] = len(record["main_results"])
    stats["main_results_found"] = sum(1 for result in record["main_results"] if result["found"])
    if articles:
        kinds = [f"{number} {what}" for number, what in (
            (stats["highlight_articles"], "for highlights of its formalization.yaml"),
            (stats["headline_articles"], "for headline results in its README whose declaration link names a "
                                         "declaration the linked file declares")) if number]
        count = (f"{articles} {'article' if articles == 1 else 'articles'}"
                 + (f": {' and '.join(kinds)}." if len(kinds) > 1 else f", {kinds[0].split(' ', 1)[1]}.")
                 + ("" if not stats["headline_unnamed"] + stats["headline_not_found"] else
                    " Its other headline results are quoted where they stand." if stats["headline_articles"] else
                    " The headline results in its README are quoted where they stand."))
    else:
        count = ("No articles: " + ("its formalization.yaml lists no highlights, and " if not record["highlights"] else "")
                 + f"none of the {stats['headline_items']} headline results in its README names a declaration that the "
                 "linked file declares at this commit, so they are quoted below.")
    builds = builds_on(record)
    graph = ["## Builds on", "", *(f"- {library_link(other, chapter, titles)} ({note})" for other, note in sorted(builds.items()))
             ] if builds else ["## Builds on", "", "No other Formal Frontier library."]
    if used_by:
        graph += ["", "## Used by", "", *(f"- {library_link(other, chapter, titles)}" for other in sorted(used_by))]
    scope = ["## Scope", "", safe(record["scope"]), "", quoted(record, "the status", "formalization.yaml")] if record["scope"] else []
    section.prose = "\n\n".join(part for part in [
        f"> {safe(record['project']['description'])}",
        quoted(record, "the project description", "formalization.yaml"),
        count,
        facts(record),
        "\n".join(scope),
        literature(record),
        "\n".join(graph),
    ] if part)
    section.tail = "\n\n".join(pending)
    chunk(section)
    section.tail = "\n\n".join(part for part in (section.tail, main_results(record)) if part)
    return section, links, stats


def chapter(pairs: list[tuple[dict, dict]]) -> tuple[Built, list[tuple[Container, dict[str, str]]]]:
    """The chapter's root, with its articles and counts, and each library's page with the source links of its
    declarations (for hooks/lean-links.json). A part per subject, a section per library."""
    names = {record["repo"].split("/")[1]: (library, record) for library, record in pairs}
    titles = {name: library["name"] for name, (library, _) in names.items()}
    used_by: dict[str, list[str]] = {name: [] for name in names}
    for name, (_, record) in names.items():
        for other in builds_on(record):
            used_by.setdefault(other, []).append(name)
    stats: Counter = Counter()
    targets: dict[str, Leaf | Container] = {}
    built: list[tuple[Container, dict[str, str]]] = []
    by_subject: dict[str, list[Container]] = {subject: [] for subject in catalog.SUBJECTS}
    for name, (library, record) in names.items():
        section, links, counts = library_section(record, set(names), titles, used_by[name])
        stats.update(counts)
        stats["libraries"] += 1
        targets[library["id"]] = section
        built.append((section, links))
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
    overview = ["## The libraries"]
    for subject, sections in by_subject.items():
        if sections:
            overview += ["", f"### {subject}", ""]
            for section in sections:
                library, record = names[section.slug]
                articles = sum(isinstance(node, Leaf) for node in walk(section))
                overview.append(f"- [{section.title}](trough:{library['id']}) ({articles} "
                                f"{'article' if articles == 1 else 'articles'}): {safe(record['project']['description'])}")
    root.tail = "\n".join(overview)
    return Built(root, targets, {}, dict(stats), Counter()), built


def intro(stats: Counter) -> str:
    unnamed, not_found, duplicates = stats["headline_unnamed"], stats["headline_not_found"], stats["headline_duplicates"]
    return "\n\n".join([
        f"[Formal Frontier]({REPO_URL}) publishes Lean libraries written by AI agents (“Formal Frontier Agents”, as "
        f"their formalization.yaml files name the authors), with a dashboard at {DASHBOARD}. This chapter maps the "
        f"{stats['libraries']} libraries in trough's catalog, each read at a pinned commit: a part per subject and a "
        "section per library. A library's page quotes its formalization.yaml (its description, scope, review and "
        "automation statements), links the Formal Frontier libraries it builds on and those that build on it, quotes "
        "the headline results of its README, and lists the main results its formalization.yaml declares.",
        f"There are {stats['articles']} articles: one for each highlight in a library's formalization.yaml "
        f"({stats['highlight_articles']}), and one for each headline result in its README whose declaration link names a "
        f"declaration that the linked file declares at the pinned commit ({stats['headline_articles']}). Of the "
        f"{stats['headline_items']} headline results, {unnamed} link no declaration, {not_found} link one the linked file "
        f"is not found to declare, and {duplicates} link one that already has an article, which the library's page "
        "links in their place. The first two kinds have no article and stay as quoted text on the library's page. "
        f"{stats['libraries_without_articles']} libraries have no articles. The main results are listed on the library's page, not made articles: in several libraries they are "
        "close to the whole API.",
        "No Lean is run for this chapter. Whether a file declares a name is read from its source text, following "
        "`namespace`, `section` and `end`; a name counts only when a declaration command in that file names it in full "
        "under the right namespace, so a name given relative to an open namespace, or one Lean generates (an additive "
        "version, a constructor), is left out rather than guessed. Articles have no dependencies: edges between "
        "declarations need Lean. A declaration whose text in the file contains `sorry` is marked as stated without proof; "
        "a dependency on an unproved declaration elsewhere is not checked.",
        "The quoted text is the libraries', under their Apache-2.0 license, with the repository and commit named where "
        "it is quoted.",
    ])
