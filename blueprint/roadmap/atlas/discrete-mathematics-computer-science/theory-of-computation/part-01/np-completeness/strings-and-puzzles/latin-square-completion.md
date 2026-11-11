---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.LatinSquareCompletionInstance, MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.WellFormed, MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.LatinSquareCompletionFeasible, MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.latinSquareCompletionDec, MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.latinSquareCompletion_npComplete
statement: formalized
---

# Latin square completion

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/latin-square-completion/index.html).

## Latin square completion instances

An instance of LATIN SQUARE COMPLETION is a pair
$(n, G)$ of a natural number $n$, the intended size, and a list $G$ of lists of natural numbers,
read as the rows of a partial grid in which the entry $0$ marks a blank cell.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.LatinSquareCompletionInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/latin-square-completion/index.html#latin-square-completion-instance).

## Well-formed Latin square completion instances

An instance $(n, G)$ of LATIN SQUARE
COMPLETION is well formed when $n > 0$, $G$ has exactly $n$ rows, every row of $G$ has length
$n$, and every entry of $G$ is at most $n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/latin-square-completion/index.html#well-formed).

## Completable partial Latin squares

An instance $(n, G)$ of LATIN SQUARE COMPLETION is
feasible when there is a grid $C$ consisting of $n$ rows of length $n$ such that for all
$r, c < n$ the entry $G_{rc}$ is either $0$ or equal to $C_{rc}$, every row of $C$ is a
permutation of $1, \dots, n$, and every column of $C$ is a permutation of $1, \dots, n$. Here
$G_{rc}$ is taken to be $0$ when $G$ has no entry in row $r$ and column $c$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.LatinSquareCompletionFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/latin-square-completion/index.html#latin-square-completion-feasible).

## LATIN SQUARE COMPLETION as a decision problem

The decision problem LATIN SQUARE
COMPLETION accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding of pairs of a natural number and a list of lists of natural numbers, to an instance
$(n, G)$ that is well formed ($n > 0$ and $G$ consists of $n$ rows of length $n$ with entries at
most $n$) and feasible ($G$ can be completed to an $n \times n$ grid whose rows and columns are
permutations of $1, \dots, n$ and which agrees with $G$ on its nonzero entries). Bitstrings that
do not decode, or that decode to a malformed instance, are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.latinSquareCompletionDec`, a definition declared in [WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/latin-square-completion/index.html#latin-square-completion-dec).

## LATIN SQUARE COMPLETION is NP-complete

The decision problem LATIN SQUARE COMPLETION on
bitstrings lies in NP, and every decision problem in NP reduces to it by a polynomial-time
many-one reduction.

## Sources

- C. J. Colbourn, "The complexity of completing partial Latin squares" (1984).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.LatinSquareCompletion.latinSquareCompletion_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LatinSquareCompletionWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/latin-square-completion/index.html#latin-square-completion-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Latin square completion](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/latin-square-completion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/strings-and-puzzles/latin-square-completion)
