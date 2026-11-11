---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.MaximumInducedMatchingInstance, MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.MaximumInducedMatchingFeasible, MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.maximumInducedMatchingDec, MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.maximumInducedMatching_npComplete
statement: formalized
---

# Maximum induced matching

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/maximum-induced-matching/index.html).

## Maximum-induced-matching instances

A maximum-induced-matching instance is a triple
$(n, E, K)$ of a natural number $n$ (the vertex count), a list $E$ of pairs of natural numbers
(the edges) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.MaximumInducedMatchingInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/maximum-induced-matching/index.html#maximum-induced-matching-instance).

## Well-formed maximum-induced-matching instances

A maximum-induced-matching instance
$(n, E, K)$ is well formed when the edge list $E$ has no repeated entries and every pair $(u, v)$
in $E$ satisfies $u < n$, $v < n$ and $u \ne v$, with the reverse pair $(v, u)$ not in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/maximum-induced-matching/index.html#well-formed).

## Feasible maximum-induced-matching instances

A maximum-induced-matching instance
$(n, E, K)$, with vertex count $n$, edge list $E$ of pairs of natural numbers and bound $K$, is
feasible when there is a sublist $M$ of $E$ of length at least $K$ such that any two distinct
pairs in $M$ share no endpoint, and no pair in $E$ joins an endpoint of one pair in $M$ to an
endpoint of a different pair in $M$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.MaximumInducedMatchingFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/maximum-induced-matching/index.html#maximum-induced-matching-feasible).

## The MAXIMUM INDUCED MATCHING decision problem

MAXIMUM INDUCED MATCHING is the decision
problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to a maximum-induced-matching instance $(n, E, K)$ that is well formed and feasible:
the edge list $E$ has no repeated entries, every pair $(u, v)$ in $E$ satisfies $u < n$, $v < n$
and $u \ne v$ with $(v, u)$ not in $E$, and some sublist $M$ of $E$ of length at least $K$ is an
induced matching, meaning that any two distinct pairs in $M$ share no endpoint and no pair in $E$
joins an endpoint of one pair in $M$ to an endpoint of a different pair in $M$. Bitstrings that
do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.maximumInducedMatchingDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/maximum-induced-matching/index.html#maximum-induced-matching-dec).

## MAXIMUM INDUCED MATCHING is NP-complete

The MAXIMUM INDUCED MATCHING decision problem
belongs to NP, and every decision problem in NP reduces to it by a polynomial-time many-one
reduction.

## Sources

- L. J. Stockmeyer and V. V. Vazirani, "NP-completeness of some generalizations of the maximum matching problem", Information Processing Letters 15 (1982), 14-19; K. Cameron, "Induced matchings", Discrete Applied Mathematics 24 (1989), 97-102 (NP-completeness for bipartite graphs, polynomial for chordal graphs).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaximumInducedMatching.maximumInducedMatching_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaximumInducedMatchingWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/maximum-induced-matching/index.html#maximum-induced-matching-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum induced matching](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/maximum-induced-matching/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/maximum-induced-matching)
