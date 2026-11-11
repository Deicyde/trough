---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MinBisection.MinBisectionInstance, MetaMathlibExt.Complexity.NPComplete.MinBisection.WellFormed, MetaMathlibExt.Complexity.NPComplete.MinBisection.MinBisectionFeasible, MetaMathlibExt.Complexity.NPComplete.MinBisection.minBisectionDec, MetaMathlibExt.Complexity.NPComplete.MinBisection.minBisection_npComplete
statement: formalized
---

# Minimum bisection

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-bisection/index.html).

## Instances of MINIMUM BISECTION

An instance of MINIMUM BISECTION is a triple
$(n, es, K)$ of a natural number $n$ (the number of vertices), a list $es$ of pairs of natural
numbers (the edge list) and a natural number $K$ (the bound on the number of crossing edges).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinBisection.MinBisectionInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MinBisectionWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinBisectionWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-bisection/index.html#min-bisection-instance).

## Well-formed MINIMUM BISECTION instances

An instance $(n, es, K)$ of MINIMUM BISECTION is
well formed when $n$ is even, the list $es$ has no repeated entries, and every entry $(u, v)$ of
$es$ satisfies $u < n$, $v < n$ and $u \ne v$, and $(v, u)$ is not an entry of $es$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinBisection.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MinBisectionWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinBisectionWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-bisection/index.html#well-formed).

## Feasible MINIMUM BISECTION instances

An instance $(n, es, K)$ of MINIMUM BISECTION is
feasible when there is a set $S \subseteq \{0, \dots, n - 1\}$ with $\lfloor n / 2 \rfloor$
elements such that no sublist of $es$ (a list obtained from $es$ by deleting entries) with
$K + 1$ entries consists only of entries $(u, v)$ with exactly one of $u$ and $v$ in $S$; that
is, at most $K$ entries of $es$ have exactly one endpoint in $S$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinBisection.MinBisectionFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MinBisectionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinBisectionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-bisection/index.html#min-bisection-feasible).

## The decision problem MINIMUM BISECTION

The decision problem MINIMUM BISECTION accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of instances, to an
instance $(n, es, K)$ of MINIMUM BISECTION that is well formed and feasible (its vertices split
into two sets of $n / 2$ vertices with at most $K$ entries of $es$ between them). Bitstrings that
do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinBisection.minBisectionDec`, a definition declared in [WantedExt/Complexity/NPComplete/MinBisectionWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinBisectionWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-bisection/index.html#min-bisection-dec).

## MINIMUM BISECTION is NP-complete

The decision problem MINIMUM BISECTION belongs to NP,
and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MINIMUM BISECTION.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MinBisection.minBisection_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MinBisectionWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinBisectionWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-bisection/index.html#min-bisection-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum bisection](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-bisection/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/minimum-bisection)
