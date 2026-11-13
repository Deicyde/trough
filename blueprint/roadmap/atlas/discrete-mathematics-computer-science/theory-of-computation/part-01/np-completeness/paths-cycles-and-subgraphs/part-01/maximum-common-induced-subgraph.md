---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.MaximumCommonInducedSubgraphInstance, MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.GraphFirst, MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.GraphSecond, MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.MaximumCommonInducedSubgraphFeasible, MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.maximumCommonInducedSubgraphDec, MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.maximumCommonInducedSubgraph_npComplete
statement: formalized
---

# Maximum common induced subgraph

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html).

## Instances of MAXIMUM COMMON INDUCED SUBGRAPH

An instance of MAXIMUM COMMON INDUCED
SUBGRAPH is a tuple $(n_1, E_1, n_2, E_2, K)$ in which $n_1$, $n_2$ and $K$ are natural numbers
and $E_1$, $E_2$ are finite lists of pairs of natural numbers: $n_1$ is the vertex count of the
first graph, $E_1$ its edge list, $n_2$ the vertex count of the second graph, $E_2$ its edge
list, and $K$ the bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.MaximumCommonInducedSubgraphInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html#maximum-common-induced-subgraph-instance).

## First graph of an instance

For an instance $(n_1, E_1, n_2, E_2, K)$ of MAXIMUM COMMON
INDUCED SUBGRAPH, the first graph is the graph of the edge list $E_1$ on $n_1$ vertices: the
simple graph on $\{0, \dots, n_1 - 1\}$ in which distinct vertices $i$ and $j$ are adjacent when
$(i, j)$ or $(j, i)$ belongs to $E_1$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.GraphFirst`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html#graph-first).

## Second graph of an instance

For an instance $(n_1, E_1, n_2, E_2, K)$ of MAXIMUM COMMON
INDUCED SUBGRAPH, the second graph is the graph of the edge list $E_2$ on $n_2$ vertices: the
simple graph on $\{0, \dots, n_2 - 1\}$ in which distinct vertices $i$ and $j$ are adjacent when
$(i, j)$ or $(j, i)$ belongs to $E_2$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.GraphSecond`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html#graph-second).

## Well-formed instances of MAXIMUM COMMON INDUCED SUBGRAPH

An instance
$(n_1, E_1, n_2, E_2, K)$ of MAXIMUM COMMON INDUCED SUBGRAPH is well formed when, for each
$k \in \{1, 2\}$, the list $E_k$ has no repeated entries and every pair $(u, v)$ in $E_k$ has
$u < n_k$, $v < n_k$, $u \ne v$ and $(v, u) \notin E_k$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html#well-formed).

## Feasible instances of MAXIMUM COMMON INDUCED SUBGRAPH

An instance
$(n_1, E_1, n_2, E_2, K)$ of MAXIMUM COMMON INDUCED SUBGRAPH is feasible when, writing $G_1$ and
$G_2$ for its first and second graphs, there are a set $A$ of vertices of $G_1$ and a set $B$ of
vertices of $G_2$ with $|A| \ge K$ and $|B| = |A|$, and a bijection $f : A \to B$ such that for
all $a, b \in A$, the vertices $a$ and $b$ are adjacent in $G_1$ if and only if $f(a)$ and $f(b)$
are adjacent in $G_2$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.MaximumCommonInducedSubgraphFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html#maximum-common-induced-subgraph-feasible).

## MAXIMUM COMMON INDUCED SUBGRAPH as a decision problem

The decision problem MAXIMUM
COMMON INDUCED SUBGRAPH accepts a bitstring $x$ exactly when the canonical bitstring decoding of
$x$ yields an instance of MAXIMUM COMMON INDUCED SUBGRAPH that is well formed and feasible.
Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.maximumCommonInducedSubgraphDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html#maximum-common-induced-subgraph-dec).

## MAXIMUM COMMON INDUCED SUBGRAPH is NP-complete

The decision problem MAXIMUM COMMON
INDUCED SUBGRAPH belongs to NP, and every decision problem in NP reduces to it by a
polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MAXIMUM COMMON INDUCED SUBGRAPH.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaximumCommonInducedSubgraph.maximumCommonInducedSubgraph_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MaximumCommonInducedSubgraphWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html#maximum-common-induced-subgraph-np-compl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum common induced subgraph](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/maximum-common-induced-subgraph)
