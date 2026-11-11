---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.LongestCycle.LongestCycleInstance, MetaMathlibExt.Complexity.NPComplete.LongestCycle.Graph, MetaMathlibExt.Complexity.NPComplete.LongestCycle.WellFormed, MetaMathlibExt.Complexity.NPComplete.LongestCycle.LongestCycleFeasible, MetaMathlibExt.Complexity.NPComplete.LongestCycle.longestCycleDec, MetaMathlibExt.Complexity.NPComplete.LongestCycle.longestCycle_npComplete
statement: formalized
---

# Longest cycle

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle/index.html).

## Instances of LONGEST CYCLE

An instance of LONGEST CYCLE is a triple $(n, E, K)$ of a
natural number $n$ (the number of vertices), a list $E$ of pairs of natural numbers (the edges),
and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestCycle.LongestCycleInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/LongestCycleWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LongestCycleWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle/index.html#longest-cycle-instance).

## Graph of a LONGEST CYCLE instance

For an instance $(n, E, K)$ of LONGEST CYCLE, its graph
is the simple graph on $\{0, \dots, n-1\}$ in which distinct vertices $i$ and $j$ are adjacent
when $(i, j)$ or $(j, i)$ belongs to $E$. Loops are dropped, and pairs with an endpoint at least
$n$ contribute no edge.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestCycle.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/LongestCycleWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LongestCycleWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle/index.html#graph).

## Well-formed LONGEST CYCLE instances

An instance $(n, E, K)$ of LONGEST CYCLE is well
formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestCycle.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/LongestCycleWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LongestCycleWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle/index.html#well-formed).

## Feasible LONGEST CYCLE instances

An instance $(n, E, K)$ of LONGEST CYCLE is feasible when
there are pairwise distinct vertices $v_1, \dots, v_m$ of the graph of the instance, with $m \ge K$
and $m \ge 3$, such that $v_j$ is adjacent to $v_{j+1}$ for every $1 \le j < m$ and $v_m$ is
adjacent to $v_1$. That is, the graph has a simple cycle with at least $K$ edges and at least
three vertices.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestCycle.LongestCycleFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/LongestCycleWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LongestCycleWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle/index.html#longest-cycle-feasible).

## The decision problem LONGEST CYCLE

LONGEST CYCLE accepts a bitstring $x$ exactly when $x$
decodes, under the canonical bitstring encoding of instances, to an instance of LONGEST CYCLE that
is well formed and feasible. Bitstrings that do not decode, and bitstrings that decode to
instances that are not well formed, are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestCycle.longestCycleDec`, a definition declared in [WantedExt/Complexity/NPComplete/LongestCycleWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LongestCycleWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle/index.html#longest-cycle-dec).

## LONGEST CYCLE is NP-complete

The decision problem LONGEST CYCLE belongs to NP, and every
decision problem in NP has a polynomial-time many-one reduction to LONGEST CYCLE.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), LONGEST CYCLE.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.LongestCycle.longestCycle_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/LongestCycleWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/LongestCycleWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle/index.html#longest-cycle-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Longest cycle](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-cycle)
