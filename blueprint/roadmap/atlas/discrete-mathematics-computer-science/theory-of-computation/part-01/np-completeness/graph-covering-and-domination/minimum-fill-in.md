---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.MinimumFillInInstance, MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.GraphAug, MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.WellFormed, MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.MinimumFillInFeasible, MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.minimumFillInDec, MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.minimumFillIn_npComplete
statement: formalized
---

# Minimum fill-in

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in/index.html).

## Instances of MINIMUM FILL-IN

An instance of MINIMUM FILL-IN is a triple $(n, E, K)$
consisting of a natural number $n$ (the number of vertices), a list $E$ of pairs of natural
numbers (the edge list) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.MinimumFillInInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in/index.html#minimum-fill-in-instance).

## Graph augmented by added edges

For an instance $(n, E, K)$ of MINIMUM FILL-IN and a
list $A$ of pairs of natural numbers, the augmented graph is the graph of the edge list $E$
followed by $A$ on $n$ vertices: the simple graph on $\{0, \dots, n - 1\}$ in which distinct
vertices $i$ and $j$ are adjacent when $(i, j)$ or $(j, i)$ belongs to $E$ or to $A$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.GraphAug`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in/index.html#graph-aug).

## Well-formed MINIMUM FILL-IN instances

An instance $(n, E, K)$ of MINIMUM FILL-IN is well
formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$ and $u \ne v$, and its reverse $(v, u)$ does not belong to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in/index.html#well-formed).

## Feasible MINIMUM FILL-IN instances

An instance $(n, E, K)$ of MINIMUM FILL-IN is
feasible when there are an ordering $\sigma$ of the vertices $0, \dots, n - 1$ (a list that
contains each of them exactly once) and a list $A$ of pairs of natural numbers, with no repeated
entries and at most $K$ entries, such that every pair $(u, v)$ in $A$ satisfies $u < n$, $v < n$
and $u \ne v$, neither $(u, v)$ nor $(v, u)$ belongs to $E$, and $(v, u)$ does not belong to $A$,
and such that, in the graph augmented by $A$, any two distinct vertices $a$ and $b$ that are both
adjacent to a vertex $v$ and both come after $v$ in $\sigma$ are adjacent to each other.

The ordering $\sigma$ is thus a perfect elimination ordering of the augmented graph, so adding
the at most $K$ edges of $A$ to the graph makes it chordal.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.MinimumFillInFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in/index.html#minimum-fill-in-feasible).

## The MINIMUM FILL-IN (CHORDAL COMPLETION) problem

The decision problem MINIMUM FILL-IN
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to an
instance $(n, E, K)$ of MINIMUM FILL-IN that is well formed and feasible.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.minimumFillInDec`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in/index.html#minimum-fill-in-dec).

## MINIMUM FILL-IN (CHORDAL COMPLETION) is NP-complete

The decision problem
MINIMUM FILL-IN lies in NP, and every decision problem in NP has a polynomial-time many-one
reduction to MINIMUM FILL-IN.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MINIMUM FILL-IN; M. Yannakakis, "Computing the minimum fill-in is NP-complete" (1981).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MinimumFillIn.minimumFillIn_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MinimumFillInWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in/index.html#minimum-fill-in-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum fill-in](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/minimum-fill-in)
