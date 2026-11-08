"""Read Lean 4 source without Lean: the declarations a file makes, by full name.

Comments, docstrings, strings and attributes are blanked first, so a name inside
them is never read as a declaration. Scopes follow `namespace`, `section`,
`mutual` and `end`, and `_root_` puts a name at the top level. The reading is
conservative, because a declaration it wrongly reports is worse than one it
misses: a file whose scopes do not close as they open declares nothing, a
declaration counts only when its command names it on the keyword's line, and
names Lean makes itself (constructors, fields, `ext` lemmas) are not read.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

KINDS = {"theorem": "theorem", "lemma": "lemma", "def": "def", "abbrev": "abbrev", "instance": "instance",
         "structure": "structure", "class": "class", "inductive": "inductive", "opaque": "opaque",
         "axiom": "axiom", "irreducible_def": "def"}
COMPONENT = r"(?:«[^»\n]*»|[^\s.:()\[\]{}⟨⟩,«»@]+)"
NAME = rf"{COMPONENT}(?:\.{COMPONENT})*"
MODIFIERS = r"(?:(?:private|protected|noncomputable|partial|unsafe|nonrec|public|meta|scoped|local)\s+)*"
# "open Foo in", "set_option x y in": a prefix that scopes one command.
IN_PREFIX = r"(?:(?:open|set_option|omit|include)\b[^\n]*?\bin\s+)*"
DECLARATION = re.compile(
    rf"^[ \t]*{IN_PREFIX}{MODIFIERS}(?:class\s+(?=inductive\b))?(?P<kind>{'|'.join(KINDS)})\b[ \t]*"
    rf"(?:\(priority\s*:=[^)\n]*\)[ \t]*)?(?P<name>{NAME})?",
    re.M,
)
NAMESPACE = re.compile(rf"^[ \t]*namespace[ \t]+(?P<name>{NAME})[ \t]*$")
SECTION = re.compile(rf"^[ \t]*(?:(?:noncomputable|public)[ \t]+)*section(?:[ \t]+(?P<name>{NAME}))?[ \t]*$")
MUTUAL = re.compile(r"^[ \t]*mutual[ \t]*$")
END = re.compile(rf"^[ \t]*end(?:[ \t]+(?P<name>{NAME}))?[ \t]*$")
# A line at column 0 that starts a command ends the declaration before it.
COMMAND = re.compile(
    rf"^(?:{IN_PREFIX}{MODIFIERS}(?:{'|'.join(KINDS)}|example|namespace|section|end|open|variable|universe|"
    r"set_option|attribute|mutual|notation|infix|infixl|infixr|prefix|postfix|macro|macro_rules|syntax|elab|"
    r"elab_rules|alias|export|initialize|omit|include|deriving|#\w+)\b)"
)
SORRY = re.compile(r"(?<![\w.'])(?:sorry|admit)(?![\w'!?])")
NOT_NAMES = {"where", "extends", "deriving"}


@dataclass(frozen=True)
class Declaration:
    name: str
    kind: str
    line: int
    sorry: bool  # its text in the file holds `sorry` or `admit`


def blank(text: str) -> str:
    """The text with comments, docstrings, strings and character literals turned to spaces, keeping
    every newline, so line numbers and columns stay where they were."""
    out = list(text)
    i, n = 0, len(text)

    def clear(start: int, end: int) -> None:
        for k in range(start, min(end, n)):
            if out[k] != "\n":
                out[k] = " "

    while i < n:
        c = text[i]
        if text.startswith("--", i):
            end = text.find("\n", i)
            end = n if end < 0 else end
            clear(i, end)
            i = end
        elif text.startswith("/-", i):
            depth, j = 1, i + 2
            while j < n and depth:
                if text.startswith("/-", j):
                    depth += 1
                    j += 2
                elif text.startswith("-/", j):
                    depth -= 1
                    j += 2
                else:
                    j += 1
            clear(i, j)
            i = j
        elif c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == "\\" else 1
            clear(i, j + 1)
            i = j + 1
        elif c == "«":
            j = text.find("»", i)
            i = n if j < 0 else j + 1
        elif c == "'" and (i == 0 or not (text[i - 1].isalnum() or text[i - 1] in "_'!?.")):
            literal = re.compile(r"'(?:\\[^\n]|\\u\{[0-9a-fA-F]+\}|[^\\'\n])'").match(text, i)
            if literal:
                clear(i, literal.end())
                i = literal.end()
            else:
                i += 1
        else:
            i += 1
    return "".join(out)


def blank_attributes(text: str) -> str:
    """Blank each `@[...]` attribute list, which may span lines and nest brackets."""
    out = list(text)
    i = text.find("@[")
    while i >= 0:
        depth, j = 0, i + 1
        while j < len(text):
            if text[j] == "[":
                depth += 1
            elif text[j] == "]":
                depth -= 1
                if not depth:
                    break
            j += 1
        for k in range(i, min(j + 1, len(text))):
            if out[k] != "\n":
                out[k] = " "
        i = text.find("@[", j + 1)
    return "".join(out)


def scan(text: str) -> dict[str, Declaration] | None:
    """Each declaration the file makes, by full name; None when its scopes don't close as they open."""
    lines = blank_attributes(blank(text)).split("\n")
    scopes: list[tuple[str, str]] = []  # (kind, the header's last component or "")
    found: dict[str, Declaration] = {}
    open_decl: tuple[str, str, int, list[str]] | None = None  # name, kind, line, its lines

    def close() -> None:
        nonlocal open_decl
        if open_decl:
            name, kind, line, body = open_decl
            found.setdefault(name, Declaration(name, kind, line, bool(SORRY.search("\n".join(body)))))
        open_decl = None

    for number, line in enumerate(lines, 1):
        if open_decl and line[:1].strip() and COMMAND.match(line):
            close()
        if match := NAMESPACE.match(line):
            close()
            scopes += [("namespace", part) for part in split(match["name"])]
            continue
        if match := SECTION.match(line):
            close()
            scopes.append(("section", match["name"] or ""))
            continue
        if MUTUAL.match(line):
            close()
            scopes.append(("mutual", ""))
            continue
        if match := END.match(line):
            close()
            if match["name"]:
                parts = split(match["name"])
                if len(scopes) < len(parts):
                    return None
                # `end A.B` closes namespaces A and B, or a section named A.B.
                if scopes[-1] == ("section", match["name"]):
                    scopes.pop()
                    continue
                for part in reversed(parts):
                    if scopes.pop() != ("namespace", part):
                        return None
            elif not scopes or scopes.pop()[1]:
                return None
            continue
        if match := DECLARATION.match(line):
            close()
            name = match["name"]
            if not name or name in NOT_NAMES:
                continue
            if name.startswith("_root_."):
                full = name[len("_root_."):]
            else:
                full = ".".join([part for kind, part in scopes if kind == "namespace"] + [name])
            open_decl = (full, KINDS[match["kind"]], number, [line[match.end():]])
            continue
        if open_decl:
            open_decl[3].append(line)
    close()
    return found


def split(name: str) -> list[str]:
    return re.findall(COMPONENT, name)


IDENTIFIER = re.compile(rf"^{NAME}$")


def is_name(text: str) -> bool:
    """Whether text reads as one Lean name, not several names or a signature."""
    return bool(IDENTIFIER.match(text)) and not text.startswith(".") and not text[:1].isdigit()
