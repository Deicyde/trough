---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.LongestPath.LongestPathInstance, MetaMathlibExt.Complexity.NPComplete.LongestPath.Graph, MetaMathlibExt.Complexity.NPComplete.LongestPath.WellFormed, MetaMathlibExt.Complexity.NPComplete.LongestPath.LongestPathFeasible, MetaMathlibExt.Complexity.NPComplete.LongestPath.longestPathDec, MetaMathlibExt.Complexity.NPComplete.LongestPath.longestPath_npComplete
statement: formalized
---

# Longest path

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path/index.html).

## Longest-path instances

A longest-path instance is a tuple $(n, E, K, s, t)$ consisting of
a natural number $n$, the number of vertices; a list $E$ of pairs of natural numbers, the edges;
and natural numbers $K$, the length bound, $s$, the start vertex, and $t$, the target vertex.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestPath.LongestPathInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/LongestPathWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestPathWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path/index.html#longest-path-instance).

## Graph of a longest-path instance

For a longest-path instance with vertex count $n$ and
edge list $E$, its graph is the graph of the edge list $E$ on $n$ vertices: the simple graph on
$\{0, \dots, n - 1\}$ in which distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or
$(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestPath.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/LongestPathWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestPathWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path/index.html#graph).

## Well-formed longest-path instances

A longest-path instance $(n, E, K, s, t)$ is well
formed when $s < n$, $t < n$, the list $E$ has no repeated entries, and every pair $(u, v)$ in
$E$ satisfies $u < n$, $v < n$ and $u \ne v$, and its reverse $(v, u)$ does not belong to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestPath.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/LongestPathWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestPathWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path/index.html#well-formed).

## Feasibility of a longest-path instance

A longest-path instance $(n, E, K, s, t)$ is
feasible when the graph of $E$ on $n$ vertices has a simple path from $s$ to $t$ with at least
$K$ edges, that is, a list $v_0, \dots, v_m$ of pairwise distinct vertices with $m \ge K$,
$v_0 = s$ and $v_m = t$, in which $v_j$ and $v_{j+1}$ are adjacent for every $j < m$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestPath.LongestPathFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/LongestPathWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestPathWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path/index.html#longest-path-feasible).

## The LONGEST PATH decision problem

LONGEST PATH is the decision problem that accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a longest-path
instance $(n, E, K, s, t)$ that is well formed and in which the graph of $E$ on $n$ vertices has
a simple path from $s$ to $t$ with at least $K$ edges. Bitstrings that do not decode to a
longest-path instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.LongestPath.longestPathDec`, a definition declared in [WantedExt/Complexity/NPComplete/LongestPathWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestPathWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path/index.html#longest-path-dec).

## LONGEST PATH is NP-complete

The LONGEST PATH decision problem belongs to NP, and every
decision problem in NP has a polynomial-time many-one reduction to LONGEST PATH.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), LONGEST PATH.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.LongestPath.longestPath_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/LongestPathWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/LongestPathWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path/index.html#longest-path-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Longest path](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/longest-path)
