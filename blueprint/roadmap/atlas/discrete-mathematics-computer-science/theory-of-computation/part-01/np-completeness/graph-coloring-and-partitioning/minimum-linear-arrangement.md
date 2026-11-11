---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.MinimumLinearArrangementInstance, MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.WellFormed, MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.MinimumLinearArrangementFeasible, MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.minimumLinearArrangementDec, MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.minimumLinearArrangement_npComplete
statement: formalized
---

# Minimum linear arrangement

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-linear-arrangement/index.html).

## Minimum linear arrangement instance

An instance of MINIMUM LINEAR ARRANGEMENT is a triple
$(n, E, K)$ of a natural number $n$ (the number of vertices), a finite list $E$ of ordered pairs
of natural numbers (the edges) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.MinimumLinearArrangementInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-linear-arrangement/index.html#minimum-linear-arrangement-instance).

## Well-formed minimum linear arrangement instance

An instance $(n, E, K)$ of MINIMUM LINEAR
ARRANGEMENT is well formed when the list $E$ has no repeated entries and every pair $(u, v)$ in
$E$ satisfies $u < n$, $v < n$ and $u \ne v$, while the reversed pair $(v, u)$ does not occur in
$E$. Thus $E$ lists the edges of a simple graph on the vertices $0, \dots, n-1$, each edge once and
in one orientation.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-linear-arrangement/index.html#well-formed).

## Feasible minimum linear arrangement instance

An instance $(n, E, K)$ of MINIMUM LINEAR
ARRANGEMENT is feasible when there is an ordering $\pi$ of $0, 1, \dots, n-1$ (a list containing
each of these numbers exactly once) such that $\sum_{(u, v) \in E} |\pi(u) - \pi(v)| \le K$. Here
$\pi(v)$ is the position of $v$ in $\pi$, counted from $0$, and is $n$ when $v \ge n$; the sum
runs over the list $E$, so a repeated pair is counted once for each occurrence.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.MinimumLinearArrangementFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-linear-arrangement/index.html#minimum-linear-arrangement-feasible).

## The MINIMUM LINEAR ARRANGEMENT decision problem

It accepts a bitstring $x$ exactly when
$x$ decodes, under the canonical bitstring encoding, to a triple $(n, E, K)$ of a natural number
$n$, a list $E$ of pairs of natural numbers and a natural number $K$ with the following
properties: every entry of $E$ is a pair $(u, v)$ of distinct numbers below $n$, the list $E$ has
no repeated entries and never contains both $(u, v)$ and $(v, u)$, and there is an ordering of
$0, 1, \dots, n-1$ in which, writing $p(v)$ for the position of $v$, the sum of $|p(u) - p(v)|$
over all pairs $(u, v)$ in $E$ is at most $K$. Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.minimumLinearArrangementDec`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-linear-arrangement/index.html#minimum-linear-arrangement-dec).

## MINIMUM LINEAR ARRANGEMENT is NP-complete

The MINIMUM LINEAR ARRANGEMENT decision problem
lies in NP, and every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MINIMUM LINEAR ARRANGEMENT.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MinimumLinearArrangement.minimumLinearArrangement_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumLinearArrangementWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-linear-arrangement/index.html#minimum-linear-arrangement-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum linear arrangement](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-linear-arrangement/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-linear-arrangement)
