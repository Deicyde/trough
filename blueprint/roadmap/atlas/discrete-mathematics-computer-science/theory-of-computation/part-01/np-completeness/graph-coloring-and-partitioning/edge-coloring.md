---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.EdgeColoring.EdgeColoringInstance, MetaMathlibExt.Complexity.NPComplete.EdgeColoring.Adj, MetaMathlibExt.Complexity.NPComplete.EdgeColoring.WellFormed, MetaMathlibExt.Complexity.NPComplete.EdgeColoring.EdgeColoringFeasible, MetaMathlibExt.Complexity.NPComplete.EdgeColoring.edgeColoringDec, MetaMathlibExt.Complexity.NPComplete.EdgeColoring.edgeColoring_npComplete
statement: formalized
---

# Edge coloring

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring/index.html).

## Edge coloring instances

An instance of EDGE COLORING is a triple $(n, E, K)$ consisting
of a natural number $n$, the number of vertices, a finite list $E$ of ordered pairs of natural
numbers, the edges, and a natural number $K$, the bound on the number of colors.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeColoring.EdgeColoringInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring/index.html#edge-coloring-instance).

## Adjacency in an edge coloring edge list

Given a list $E$ of ordered pairs of natural
numbers and natural numbers $u$ and $v$, the boolean adjacency of $u$ and $v$ in $E$ is true
exactly when $(u, v)$ or $(v, u)$ occurs in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeColoring.Adj`, a definition declared in [WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring/index.html#adj).

## Well-formed edge coloring instances

An edge coloring instance $(n, E, K)$ is well formed
when the list $E$ has no repeated entries and every pair $(a, b)$ in $E$ satisfies $a < n$,
$b < n$ and $a \ne b$, and $(b, a)$ does not occur in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeColoring.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring/index.html#well-formed).

## Feasible edge coloring instances

Let $(n, E, K)$ be an edge coloring instance with edge
list $E = (e_0, \dots, e_{m-1})$, where the endpoints of a pair $(x, y)$ are $x$ and $y$. The
instance is feasible when there is a list $(c_0, \dots, c_{m-1})$ of natural numbers with
$c_j < K$ for every $j$ such that $c_a \ne c_b$ for all distinct $a, b < m$ for which $e_a$ and
$e_b$ share an endpoint.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeColoring.EdgeColoringFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring/index.html#edge-coloring-feasible).

## EDGE COLORING as a decision problem

The EDGE COLORING decision problem accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of edge coloring
instances, to an instance that is well formed and feasible. Bitstrings that do not decode are
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeColoring.edgeColoringDec`, a definition declared in [WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring/index.html#edge-coloring-dec).

## EDGE COLORING is NP-complete

The EDGE COLORING decision problem belongs to NP, and every
decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), EDGE COLORING; I. Holyer, "The NP-completeness of edge-coloring" (1981).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.EdgeColoring.edgeColoring_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/EdgeColoringWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring/index.html#edge-coloring-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Edge coloring](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/edge-coloring)
