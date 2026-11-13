---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.starLang, MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.concatLang, MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.evalPostfix, MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.regexUnivDec, MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.regex_squaring_expspace_complete
statement: formalized
---

# Regular expressions with squaring

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/regular-expressions-with-squaring/index.html).

## Kleene star of a bitstring language

For a set $S$ of bitstrings, its Kleene star is the
set of all concatenations $u_1 u_2 \cdots u_k$, for $k \ge 0$, of bitstrings
$u_1, \dots, u_k \in S$; the empty concatenation ($k = 0$) is the empty bitstring.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.starLang`, a definition declared in [WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/regular-expressions-with-squaring/index.html#star-lang).

## Concatenation of bitstring languages

For sets $S$ and $T$ of bitstrings, their
concatenation is the set of all bitstrings $uv$ with $u \in S$ and $v \in T$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.concatLang`, a definition declared in [WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/regular-expressions-with-squaring/index.html#concat-lang).

## Evaluation of postfix regular expressions with squaring

A list of natural-number tokens
is evaluated from left to right on a given stack of languages of bitstrings. Token $0$ pushes the
empty language, token $1$ pushes the language containing only the empty bitstring, and tokens $2$
and $3$ push the languages containing only the one-letter bitstring false, respectively true.
Token $4$ pops the top language $S$ and the language $T$ below it and pushes the concatenation
$TS$; token $5$ pops $S$ and $T$ in the same way and pushes $T \cup S$; token $6$ pops $S$ and
pushes its Kleene star; token $7$ pops $S$ and pushes its square $SS$. When the tokens run out,
the evaluation returns the language on the stack if the stack holds exactly one language. It
fails if the stack holds any other number of languages at the end, if a token is larger than
$7$, or if an operator token finds too few languages on the stack.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.evalPostfix`, a definition declared in [WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/regular-expressions-with-squaring/index.html#eval-postfix).

## Universality of postfix regular expressions with squaring

This is the decision problem
that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of
lists of natural numbers, to a token list whose evaluation as a postfix regular expression with
squaring, started on the empty stack, succeeds and returns the set of all bitstrings. A bitstring
that does not decode to a list of natural numbers is rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.regexUnivDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/regular-expressions-with-squaring/index.html#regex-univ-dec).

## Regular expressions with squaring: universality is EXPSPACE-complete

The universality
problem for postfix regular expressions with squaring belongs to $\mathsf{EXPSPACE}$, and every
decision problem in $\mathsf{EXPSPACE}$ reduces to it by a polynomial-time many-one reduction.
Here the universality problem accepts a bitstring exactly when it decodes to a list of
natural-number tokens whose postfix evaluation, started on the empty stack, returns the set of
all bitstrings.

## Sources

- A. R. Meyer and L. J. Stockmeyer, "The equivalence problem for regular expressions with squaring requires exponential space", Proceedings of the Thirteenth Annual Symposium on Switching and Automata Theory (1972), 125-129. (The exponential-time word problem in Stockmeyer- Meyer (STOC 1973) is membership, not universality.)

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.RegexSquaringEXPSPACEComplete.regex_squaring_expspace_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/RegexSquaringEXPSPACECompleteWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/regular-expressions-with-squaring/index.html#regex-squaring-expspace-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular expressions with squaring](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/regular-expressions-with-squaring/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/regular-expressions-with-squaring)
