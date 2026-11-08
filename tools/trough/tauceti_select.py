"""Which Tau Ceti declarations name a result, read from the library's own docstrings.

Tau Ceti opens many docstrings with a bold title ("**Burnside's pᵃqᵇ theorem**: a finite group
of order ..."). A theorem is chosen when its title's head clause, the title before its first
qualifier ("Morley's theorem (cardinal form)" has head "Morley's theorem"), names a result:

- a person's name among its first three words, then a result noun: theorem, lemma or conjecture,
  or duality, formula, inequality, criterion and the like ("Schur-Weyl duality"); "law" counts
  only after a possessive, so "the Wishart law", a distribution, does not;
- a capitalized first word that the library also uses as a possessive ("Serre's"), then a result
  noun within three words ("Serre duality");
- a phrase of at most six words ending in "theorem" ("The cellular approximation theorem");
- at most three words, pinned to a textbook theorem right after the title ("**Global existence**
  (Milne VII, Theorem 9.5)").

A head that is itself a numbered citation ("Wedhorn's Lemma 8.34") or opens with "Step",
"Proof" and the like does not count. Tau Ceti's website shows four theorems, which are always
chosen. A definition is chosen when its title names a theorem and it carries the theorem as data
(an equivalence or an isomorphism, its name in lower case); a proposition that only states a
claim ("AbcConjecture") is not. A chosen theorem stated inside such a proposition's namespace is
proved from it, so its article says what it assumes.

The rows are tools/select_tauceti.py's reading of lean/tauceti/TauCetiSurvey.lean's output:
{"n": name, "k": kind, "m": module, "d": the docstring's first characters}.
"""

from __future__ import annotations

import re

SELECTION_SCHEMA = "trough-tauceti-selection/v1"
SHOWCASE = (
    "TauCeti.isSolvable_of_card_eq_prime_pow_mul_prime_pow",
    "TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier",
    "TauCeti.centralizer_range_tensorPowerRep_asAlgebraHom_eq_range_permTensorActionAlgHom",
    "TauCeti.centralizer_range_permTensorActionAlgHom_eq_range_tensorPowerRep_asAlgebraHom",
)
# Any bold span that opens the docstring.
BOLD = re.compile(r"^\s*\*\*(?P<title>(?:[^*\n]|\n(?!\s*\n)|\*(?!\*))+?)\*\*")
# The head clause ends at the title's first qualifier.
HEAD_SPLIT = re.compile(r",\s|:\s|;\s|\s\(|\s--\s|\s—\s|\s-\s|\s–\s|\.\s")
ARTICLE = re.compile(r"^(?:The|A|An)\s+")
# A person's name: a capitalized word, perhaps after a particle ("van Kampen"), possessive
# ("Burnside's", "Cassels'"), joined to another name ("Jordan–Brouwer", "Seifert--van Kampen"), or
# bare and not the head's first word ("The Krull intersection theorem").
_NAME = r"(?:(?:van|von|de|der|du|di|da|le|la|dos|De|Van|Von)\s)?[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ]+"
_JOIN = r"(?:--|-|–|—)"
EPONYM = re.compile(
    rf"(?<![\w`])(?:{_NAME}(?:{_JOIN}{_NAME})*['’]s?(?=\s)"
    rf"|{_NAME}(?:{_JOIN}{_NAME})+(?![\w`'’])"
    rf"|(?<=\s){_NAME}(?=[\s,]|$))")
NOT_NAMES = frozenset({
    "The", "A", "An", "Every", "Each", "For", "If", "In", "On", "Over", "Any", "No", "Some", "All",
    "Lie", "Lean", "Mathlib", "Tau", "Ceti", "Lemma", "Theorem", "Proposition", "Corollary",
    "Step", "Part", "Case", "Section", "Chapter", "Example", "Definition", "Remark", "Main",
    "Gaussian", "Hessian", "Polish", "Euclidean", "Open", "Mapping", "Limit", "Fundamental",
    "Strong", "Weak", "Laplacian", "Hamiltonian", "Lagrangian", "Abelian", "Archimedean",
    "Noetherian", "Artinian", "Hermitian", "Riemannian", "Cartesian",
})
NAME_WORDS = 3  # the name is among the head's first three words, an article dropped
CORE = r"(?:theorem|lemma|conjecture)s?"
RESULT = (r"(?:theorem|lemma|conjecture|duality|reciprocity|formula|inequality|criterion|"
          r"principle|law|identity|correspondence|dichotomy|alternative|trichotomy|"
          r"classification|decomposition|isomorphism|bound|estimate|paradox|"
          r"theorems|lemmas|conjectures|formulas|inequalities|criteria|principles|laws|"
          r"identities|bounds|estimates)")
NUMBERED = re.compile(r"\b(?:Theorem|Thm\.?|Lemma|Proposition|Prop\.?|Corollary|Cor\.?|Remark|Definition)"
                      r"\s+[\dIVX]+(?:\.[\dA-Za-z]+)+")
NOT_HEADLINE = re.compile(r"^(?:Naturality|Step|Case|Part|Proof|Auxiliary|Helper|Lemma|Corollary|Technical|"
                          r"Preparation|Reduction|Ingredient)\b", re.I)
# "(Author, Theorem N)" right after the title, not "(..., proof of Theorem N)".
CITED = re.compile(r"^\s*[.:]?\s*\(([^()]{0,80}?)\b(?:Theorem|Thm\.?)\s+[\dIVX]+(?:\.[\dA-Za-z]+)*[^()]{0,40}\)")
NOT_CITED = re.compile(r"\b(?:proof|step|after|of|by|see|cf\.?|from|in)\s*$", re.I)
CITED_WORDS = 3
POSSESSIVE = re.compile(r"\b([A-ZÀ-Ö][a-zà-ÿ]+)['’]s?\s")
BARE_FIRST = re.compile(rf"^([A-ZÀ-Ö][a-zà-ÿ]+)\s+(?:[\w-]+\s+){{0,2}}?{RESULT}\b")
# A proposition that only states a claim, by its name's last component.
STATEMENT = re.compile(r"(?:Conjecture|Theorem|Hypothesis|Problem)\w*$")
DEFINITIONS = frozenset({"def", "abbrev"})


def title(doc: str | None) -> str | None:
    """The bold span that opens a docstring, as plain words."""
    match = BOLD.match(doc or "")
    return " ".join(match["title"].split()).rstrip(".:,;") if match else None


def head(text: str) -> str:
    return HEAD_SPLIT.split(text, 1)[0]


def _plain(text: str) -> str:
    return ARTICLE.sub("", re.sub(r"`[^`]*`", "X", text))


def _excluded(clause: str) -> bool:
    return bool(NUMBERED.search(clause)) or bool(NOT_HEADLINE.match(_plain(clause)))


def named_before(clause: str, end: int) -> bool:
    """Whether a person's name stands among the first words of *clause*, before offset *end*."""
    plain = _plain(clause[:end])
    if clause.startswith("The "):
        plain = " " + plain  # a capital right after "The" may be a bare name
    for match in EPONYM.finditer(plain):
        word = None if re.search(rf"['’]|{_JOIN}", match.group(0)) else match.group(0).split()[-1]
        if word in NOT_NAMES:
            continue
        if len(plain[:match.start()].split()) < NAME_WORDS:
            return True
    return False


def named_theorem(clause: str) -> bool:
    """A name, then theorem, lemma or conjecture: "Burnside's pᵃqᵇ theorem"."""
    if _excluded(clause):
        return False
    match = re.search(rf"\b{CORE}\b", clause, re.I)
    return bool(match) and named_before(clause, match.end())


def named_result(clause: str) -> bool:
    """A name, then any result noun: "Schur-Weyl duality", "Parseval's identity"."""
    if _excluded(clause):
        return False
    match = re.search(rf"\b{RESULT}\b", clause, re.I)
    if not match:
        return False
    if match.group(0).lower().startswith("law") and not re.search(r"['’]s?\s", _plain(clause[:match.start()])):
        return False
    return named_before(clause, match.end())


def bare_named_result(clause: str, possessives: set[str]) -> bool:
    """A first word the library also writes as a possessive, then a result noun: "Serre duality"."""
    if clause.startswith("The ") or NUMBERED.search(clause):
        return False
    match = BARE_FIRST.match(clause)
    return bool(match) and match.group(1) in possessives


def the_theorem(clause: str) -> bool:
    """At most six words ending in "theorem": "The prime number theorem"."""
    if NUMBERED.search(clause):
        return False
    plain = _plain(clause)
    return bool(re.match(r"(?:[^\s,]+\s+){0,5}theorems?\b", plain, re.I)) and not NOT_HEADLINE.match(plain)


def cited_theorem(doc: str, text: str) -> bool:
    """At most three words, then "(Author, Theorem N)": "**Global existence** (Milne VII, Theorem 9.5)"."""
    match = CITED.match(doc[BOLD.match(doc).end():])
    return (bool(match) and not NOT_CITED.search(match.group(1))
            and len(_plain(head(text)).split()) <= CITED_WORDS)


def possessive_names(rows) -> set[str]:
    """The capitalized words any title writes as a possessive."""
    names: set[str] = set()
    for row in rows:
        text = title(row.get("d"))
        if text:
            names.update(POSSESSIVE.findall(text))
    return names - NOT_NAMES


def theorem_test(row: dict, possessives: set[str]) -> str | None:
    """Which test chooses a theorem, or None."""
    text = title(row.get("d"))
    if not text:
        return None
    clause = head(text)
    if named_theorem(clause):
        return "named theorem"
    if named_result(clause):
        return "named result"
    if bare_named_result(clause, possessives):
        return "named result"
    if the_theorem(clause):
        return "the theorem"
    if cited_theorem(row["d"], text):
        return "cited theorem"
    return None


def definition_test(row: dict) -> str | None:
    """A definition whose title names a theorem and that carries it as data."""
    text = title(row.get("d"))
    if not text or row["n"].split(".")[-1][:1].isupper():
        return None
    clause = head(text)
    if named_theorem(clause) or the_theorem(clause) or (named_result(clause) and re.search(rf"\b{CORE}\b", clause, re.I)):
        return "theorem as data"
    return None


def select(rows: list[dict]) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    """The chosen declarations, each with the test that chose it, and for each chosen one stated in
    the namespace of a proposition that only states a claim, that proposition and its module."""
    possessives = possessive_names(rows)
    chosen: dict[str, str] = {}
    for row in rows:
        if row["k"] == "theorem":
            test = theorem_test(row, possessives)
        elif row["k"] in DEFINITIONS:
            test = definition_test(row)
        else:
            continue
        if test:
            chosen[row["n"]] = test
    names = {row["n"] for row in rows}
    for name in SHOWCASE:
        if name in names:
            chosen[name] = "showcase"
    statements = {row["n"]: row["m"] for row in rows if row["k"] in DEFINITIONS
                  and row["n"].split(".")[-1][:1].isupper() and STATEMENT.search(row["n"].split(".")[-1])}
    assuming = {name: {"statement": name.rsplit(".", 1)[0], "module": statements[name.rsplit(".", 1)[0]]}
                for name in chosen if "." in name and name.rsplit(".", 1)[0] in statements}
    return dict(sorted(chosen.items())), dict(sorted(assuming.items()))


def _normal(text: str) -> str:
    text = ARTICLE.sub("", text)
    text = re.sub(r"[–—-]+", "-", text)
    text = re.sub(r"['’]s?\b", "", text)
    return " ".join(text.split()).casefold()


def plain_title(text: str, key: str) -> bool:
    """Whether a title is its result's name and nothing more: "Menger's theorem" for "menger theorem"."""
    return _normal(text) == key


def group_key(text: str) -> str:
    """The name of the result a title states, for gathering its forms: "Menger's theorem for
    adjacent vertices" and "Menger's theorem, predicate form" both give "menger theorem". A short
    key without a name ("structure theorem") keeps the whole head clause."""
    clause = head(text)
    match = re.search(rf"\b{RESULT}\b", clause, re.I)
    key = clause[:match.end()] if match else clause
    if match and len(_plain(key).split()) <= 2 and not named_before(clause, match.end()):
        key = clause
    return _normal(key)
