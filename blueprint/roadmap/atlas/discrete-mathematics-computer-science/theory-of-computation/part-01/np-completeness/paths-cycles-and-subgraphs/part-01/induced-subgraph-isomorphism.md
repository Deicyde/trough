---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.InducedSubgraphIsomorphismInstance, MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.GraphHost, MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.GraphPattern, MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.WellFormed, MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.InducedSubgraphIsomorphismFeasible, MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.inducedSubgraphIsomorphismDec, MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.inducedSubgraphIsomorphism_npComplete
statement: formalized
---

# Induced subgraph isomorphism

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html).

## Induced-subgraph-isomorphism instance

An instance of INDUCED SUBGRAPH ISOMORPHISM is a
quadruple $(n, E, k, F)$ consisting of a natural number $n$ (the number of host vertices), a list
$E$ of pairs of natural numbers (the host edges), a natural number $k$ (the number of pattern
vertices) and a list $F$ of pairs of natural numbers (the pattern edges).

Formalized by `MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.InducedSubgraphIsomorphismInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html#induced-subgraph-isomorphism-instance).

## Host graph of an induced-subgraph-isomorphism instance

For an instance $(n, E, k, F)$,
the host graph is the graph of the edge list $E$ on $n$ vertices: the simple graph on
$\{0, \dots, n - 1\}$ in which distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or
$(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.GraphHost`, a definition declared in [WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html#graph-host).

## Pattern graph of an induced-subgraph-isomorphism instance

For an instance
$(n, E, k, F)$, the pattern graph is the graph of the edge list $F$ on $k$ vertices: the simple
graph on $\{0, \dots, k - 1\}$ in which distinct vertices $i$ and $j$ are adjacent when $(i, j)$
or $(j, i)$ belongs to $F$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.GraphPattern`, a definition declared in [WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html#graph-pattern).

## Well-formed induced-subgraph-isomorphism instance

An instance $(n, E, k, F)$ is
well-formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E$, and likewise the list $F$ has no repeated
entries and every pair $(u, v)$ in $F$ satisfies $u < k$, $v < k$, $u \ne v$ and
$(v, u) \notin F$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html#well-formed).

## Induced embedding of the pattern into the host

An instance $(n, E, k, F)$ is feasible
when there is an injective map $f$ from $\{0, \dots, k - 1\}$ to $\{0, \dots, n - 1\}$ such that,
for all $a, b \in \{0, \dots, k - 1\}$, the vertices $a$ and $b$ are adjacent in the pattern
graph if and only if $f(a)$ and $f(b)$ are adjacent in the host graph.

Formalized by `MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.InducedSubgraphIsomorphismFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html#induced-subgraph-isomorphism-feasible).

## INDUCED SUBGRAPH ISOMORPHISM as a decision problem

The decision problem INDUCED SUBGRAPH
ISOMORPHISM accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to an instance $(n, E, k, F)$ (host vertex count, host edge list, pattern vertex count,
pattern edge list) that is well-formed and for which there is an injective map $f$ from
$\{0, \dots, k - 1\}$ to $\{0, \dots, n - 1\}$ such that, for all $a$ and $b$, the vertices $a$
and $b$ are adjacent in the pattern graph if and only if $f(a)$ and $f(b)$ are adjacent in the
host graph. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.inducedSubgraphIsomorphismDec`, a definition declared in [WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html#induced-subgraph-isomorphism-dec).

## INDUCED SUBGRAPH ISOMORPHISM is NP-complete

The decision problem INDUCED SUBGRAPH
ISOMORPHISM is in NP, and every decision problem in NP reduces to it by a polynomial-time
many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), INDUCED SUBGRAPH ISOMORPHISM.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.InducedSubgraphIsomorphism.inducedSubgraphIsomorphism_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/InducedSubgraphIsomorphismWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html#induced-subgraph-isomorphism-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Induced subgraph isomorphism](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/induced-subgraph-isomorphism)
