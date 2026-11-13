---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.MinimumEquivalentDigraphInstance, MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.DAdj, MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.Reachable, MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.WellFormed, MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.MinimumEquivalentDigraphFeasible, MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.minimumEquivalentDigraphDec, MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.minimumEquivalentDigraph_npComplete
statement: formalized
---

# Minimum equivalent digraph

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html).

## Instances of MINIMUM EQUIVALENT DIGRAPH

An instance of MINIMUM EQUIVALENT DIGRAPH is a
triple $(n, E, K)$ consisting of a natural number $n$ (the number of vertices), a finite list $E$
of ordered pairs of natural numbers (the arcs) and a natural number $K$ (the bound on the number
of arcs).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.MinimumEquivalentDigraphInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html#minimum-equivalent-digraph-instance).

## Directed adjacency for MINIMUM EQUIVALENT DIGRAPH

For a finite list $E$ of ordered pairs
of natural numbers and natural numbers $u$ and $v$, the directed adjacency test of $E$ at $(u, v)$
returns true when the pair $(u, v)$ occurs in $E$, and false otherwise.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.DAdj`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html#dadj).

## Bounded reachability in a digraph

Let $E$ be a finite list of ordered pairs of natural
numbers, read as the arcs of a directed graph, and let $n$, $u$ and $v$ be natural numbers. Then
$v$ is reachable from $u$ within $n$ steps along $E$ when there are natural numbers
$w_0, w_1, \dots, w_k$ with $k \le n$, $w_0 = u$ and $w_k = v$ such that $(w_j, w_{j+1})$ occurs
in $E$ for every $j < k$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.Reachable`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html#reachable).

## Well-formed MINIMUM EQUIVALENT DIGRAPH instances

An instance $(n, E, K)$ of MINIMUM
EQUIVALENT DIGRAPH is well formed when the list $E$ has no repeated entries and every pair
$(a, b)$ in $E$ satisfies $a < n$, $b < n$ and $a \ne b$; that is, $E$ lists distinct arcs
without loops between vertices among $0, \dots, n - 1$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html#well-formed).

## Feasible MINIMUM EQUIVALENT DIGRAPH instances

An instance $(n, E, K)$ of MINIMUM
EQUIVALENT DIGRAPH is feasible when some sublist $F$ of $E$ (obtained by deleting entries of
$E$) has at most $K$ entries and, for all vertices $u < n$ and $v < n$, $v$ is reachable from $u$
within $n$ steps along $E$ if and only if $v$ is reachable from $u$ within $n$ steps along
$F$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.MinimumEquivalentDigraphFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html#minimum-equivalent-digraph-feasible).

## MINIMUM EQUIVALENT DIGRAPH as a decision problem

The decision problem MINIMUM
EQUIVALENT DIGRAPH accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding, to an instance of MINIMUM EQUIVALENT DIGRAPH that is well formed and
feasible. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.minimumEquivalentDigraphDec`, a definition declared in [WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html#minimum-equivalent-digraph-dec).

## MINIMUM EQUIVALENT DIGRAPH is NP-complete

The decision problem MINIMUM EQUIVALENT
DIGRAPH belongs to NP, and every decision problem in NP has a polynomial-time many-one reduction
to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MINIMUM EQUIVALENT DIGRAPH; A. V. Aho, M. R. Garey, and J. D. Ullman, "The transitive reduction of a directed graph", SIAM Journal on Computing 1 (1972), 131-137 (distinguishing transitive reduction from the minimum equivalent subgraph and the hardness connection); D. M. Moyles and G. L. Thompson, "An algorithm for finding a minimum equivalent graph of a digraph", Journal of the ACM 16 (1969), 455-460.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MinimumEquivalentDigraph.minimumEquivalentDigraph_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MinimumEquivalentDigraphWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html#minimum-equivalent-digraph-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimum equivalent digraph](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/minimum-equivalent-digraph)
