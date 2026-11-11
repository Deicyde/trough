---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.GraphHomomorphismInstance, MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.GraphTarget, MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.WellFormed, MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.GraphHomomorphismFeasible, MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.graphHomomorphismDec, MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.graphHomomorphism_npComplete
statement: formalized
---

# Graph homomorphism

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism/index.html).

## Graph-homomorphism instances

A graph-homomorphism instance is a quadruple $(n, E, m, F)$
where $n$ is a natural number (the number of source vertices), $E$ is a list of pairs of natural
numbers (the source edges), $m$ is a natural number (the number of target vertices) and $F$ is a
list of pairs of natural numbers (the target edges).

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.GraphHomomorphismInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism/index.html#graph-homomorphism-instance).

## Target graph of a graph-homomorphism instance

The target graph of a graph-homomorphism
instance $(n, E, m, F)$ is the simple graph on $\{0, \dots, m - 1\}$ in which distinct vertices
$i$ and $j$ are adjacent when $(i, j)$ or $(j, i)$ belongs to $F$. Pairs of $F$ with an endpoint
at least $m$ contribute no edge.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.GraphTarget`, a definition declared in [WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism/index.html#graph-target).

## Well-formed graph-homomorphism instances

A graph-homomorphism instance $(n, E, m, F)$ is
well formed when $E$ has no repeated entries, every pair $(u, v)$ in $E$ satisfies $u < n$,
$v < n$, $u \ne v$ and $(v, u) \notin E$, $F$ has no repeated entries, and every pair $(u, v)$
in $F$ satisfies $u < m$, $v < m$, $u \ne v$ and $(v, u) \notin F$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism/index.html#well-formed).

## Feasible graph-homomorphism instances

A graph-homomorphism instance $(n, E, m, F)$ is
feasible when there is a map $f : \{0, \dots, n - 1\} \to \{0, \dots, m - 1\}$ such that, for
every pair $(u, v)$ in $E$ with $u < n$ and $v < n$, the vertices $f(u)$ and $f(v)$ are adjacent
in the target graph of the instance, that is, $f(u) \ne f(v)$ and $(f(u), f(v))$ or
$(f(v), f(u))$ belongs to $F$. Pairs of $E$ with an endpoint at least $n$ impose no condition.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.GraphHomomorphismFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism/index.html#graph-homomorphism-feasible).

## GRAPH HOMOMORPHISM as a decision problem

The decision problem GRAPH HOMOMORPHISM accepts
a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
graph-homomorphism instance $(n, E, m, F)$ that is well formed (neither $E$ nor $F$ has repeated
entries, every pair $(u, v)$ in $E$ has $u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E$, and
every pair $(u, v)$ in $F$ has $u < m$, $v < m$, $u \ne v$ and $(v, u) \notin F$) and for which
there is a map $f : \{0, \dots, n - 1\} \to \{0, \dots, m - 1\}$ such that, for every pair
$(u, v)$ in $E$, $f(u) \ne f(v)$ and $(f(u), f(v))$ or $(f(v), f(u))$ belongs to $F$. Bitstrings
that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.graphHomomorphismDec`, a definition declared in [WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism/index.html#graph-homomorphism-dec).

## GRAPH HOMOMORPHISM is NP-complete

The decision problem GRAPH HOMOMORPHISM belongs to NP,
and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), GRAPH HOMOMORPHISM; P. Hell and J. Nesetril, "On the complexity of H-coloring" (1990).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.GraphHomomorphism.graphHomomorphism_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/GraphHomomorphismWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism/index.html#graph-homomorphism-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph homomorphism](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-homomorphism)
