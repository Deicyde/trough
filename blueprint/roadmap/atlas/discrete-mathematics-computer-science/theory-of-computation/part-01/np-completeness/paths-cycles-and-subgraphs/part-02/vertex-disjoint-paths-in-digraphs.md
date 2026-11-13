---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.DirectedDisjointPathsInstance, MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.DAdj, MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.WellFormed, MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.DirectedDisjointPathsFeasible, MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.directedDisjointPathsDec, MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.directedDisjointPaths_npComplete
statement: formalized
---

# Vertex-disjoint paths in digraphs

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs/index.html).

## Directed disjoint paths instances

An instance of DIRECTED DISJOINT PATHS is a triple
$(n, A, P)$ consisting of a natural number $n$ (the number of vertices), a finite list $A$ of
ordered pairs of natural numbers (the arcs) and a finite list $P$ of ordered pairs of natural
numbers (the source-target pairs).

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.DirectedDisjointPathsInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs/index.html#directed-disjoint-paths-instance).

## Directed adjacency for DIRECTED DISJOINT PATHS

For a finite list $E$ of ordered pairs of
natural numbers and natural numbers $u$ and $v$, the directed adjacency of $u$ to $v$ in $E$ is
the boolean value that is true exactly when the pair $(u, v)$ occurs in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.DAdj`, a definition declared in [WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs/index.html#dadj).

## Well-formed directed disjoint paths instances

An instance $(n, A, P)$ of DIRECTED
DISJOINT PATHS is well formed when the arc list $A$ has no repeated entries, every arc $(u, v)$
in $A$ satisfies $u < n$, $v < n$ and $u \ne v$, and every source-target pair $(s, t)$ in $P$
satisfies $s < n$ and $t < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs/index.html#well-formed).

## Feasible directed disjoint paths instances

Let $(n, A, P)$ be an instance of DIRECTED
DISJOINT PATHS whose list of source-target pairs is
$P = ((s_0, t_0), \dots, (s_{k-1}, t_{k-1}))$. The instance is feasible when there are lists
$\pi_0, \dots, \pi_{k-1}$ of natural numbers such that, for every $p < k$, the list $\pi_p$ is
nonempty, has no repeated entries, has first entry $s_p$ and last entry $t_p$, has all its
entries less than $n$, and every two consecutive entries $u, v$ of $\pi_p$ form an arc $(u, v)$
occurring in $A$; and such that, for all distinct $p, q < k$, no $v < n$ is an entry of both
$\pi_p$ and $\pi_q$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.DirectedDisjointPathsFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs/index.html#directed-disjoint-paths-feasible).

## DIRECTED DISJOINT PATHS as a decision problem

The decision problem DIRECTED DISJOINT
PATHS accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding,
to an instance of DIRECTED DISJOINT PATHS that is well formed and feasible; bitstrings that do
not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.directedDisjointPathsDec`, a definition declared in [WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs/index.html#directed-disjoint-paths-dec).

## DIRECTED DISJOINT PATHS is NP-complete

The decision problem DIRECTED DISJOINT PATHS
belongs to NP, and every decision problem in NP reduces to it by a polynomial-time many-one
reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), DISJOINT PATHS; S. Fortune, J. Hopcroft, and J. Wyllie, "The directed subgraph homeomorphism problem" (1980).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.DirectedDisjointPaths.directedDisjointPaths_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DirectedDisjointPathsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs/index.html#directed-disjoint-paths-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vertex-disjoint paths in digraphs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/vertex-disjoint-paths-in-digraphs)
