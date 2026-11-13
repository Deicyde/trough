---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.GraphColoring.GraphColoringInstance, MetaMathlibExt.Complexity.NPComplete.GraphColoring.Graph, MetaMathlibExt.Complexity.NPComplete.GraphColoring.WellFormed, MetaMathlibExt.Complexity.NPComplete.GraphColoring.GraphColoringFeasible, MetaMathlibExt.Complexity.NPComplete.GraphColoring.graphColoringDec, MetaMathlibExt.Complexity.NPComplete.GraphColoring.graphColoring_npComplete
statement: formalized
---

# Graph coloring

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring/index.html).

## Instances of GRAPH COLORING

An instance of GRAPH COLORING is a triple $(n, E, K)$
consisting of a natural number $n$, the number of vertices, a list $E$ of pairs of natural
numbers, the edges, and a natural number $K$, the bound on the number of colors.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphColoring.GraphColoringInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/GraphColoringWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GraphColoringWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring/index.html#graph-coloring-instance).

## Graph of a GRAPH COLORING instance

The graph of an instance $(n, E, K)$ of GRAPH
COLORING is the simple graph on $\{0, \dots, n - 1\}$ in which distinct vertices $i$ and $j$ are
adjacent when $(i, j)$ or $(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphColoring.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/GraphColoringWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GraphColoringWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring/index.html#graph).

## Well-formed GRAPH COLORING instances

An instance $(n, E, K)$ of GRAPH COLORING is well
formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$ satisfies
$u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphColoring.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/GraphColoringWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GraphColoringWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring/index.html#well-formed).

## Feasible GRAPH COLORING instances

An instance $(n, E, K)$ of GRAPH COLORING is
feasible when its graph is $K$-colorable, that is, when its vertices can be assigned colors from
$\{0, \dots, K - 1\}$ so that adjacent vertices receive different colors.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphColoring.GraphColoringFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/GraphColoringWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GraphColoringWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring/index.html#graph-coloring-feasible).

## GRAPH COLORING as a decision problem

The decision problem GRAPH COLORING accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to an instance
of GRAPH COLORING that is well formed and feasible. Bitstrings that do not decode to an instance
are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.GraphColoring.graphColoringDec`, a definition declared in [WantedExt/Complexity/NPComplete/GraphColoringWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GraphColoringWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring/index.html#graph-coloring-dec).

## GRAPH COLORING is NP-complete

The decision problem GRAPH COLORING belongs to NP, and
every decision problem $L$ in NP has a polynomial-time many-one reduction to GRAPH COLORING.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), GRAPH COLORING (chromatic number); R. M. Karp, "Reducibility among combinatorial problems" (1972).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.GraphColoring.graphColoring_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/GraphColoringWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/GraphColoringWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring/index.html#graph-coloring-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph coloring](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/graph-coloring)
