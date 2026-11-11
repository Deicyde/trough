---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.DegreeConstrainedSpanningTreeInstance, MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.WellFormed, MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.DegreeConstrainedSpanningTreeFeasible, MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.degreeConstrainedSpanningTreeDec, MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.degreeConstrainedSpanningTree_npComplete
statement: formalized
---

# Degree-constrained spanning tree

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/degree-constrained-spanning-tree/index.html).

## Instances of DEGREE-CONSTRAINED SPANNING TREE

An instance of DEGREE-CONSTRAINED SPANNING
TREE is a triple $(n, E, K)$ consisting of a natural number $n$ (the number of vertices), a list
$E$ of pairs of natural numbers (the edges) and a natural number $K$ (the degree bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.DegreeConstrainedSpanningTreeInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/degree-constrained-spanning-tree/index.html#degree-constrained-spanning-tree-instanc).

## Well-formed DEGREE-CONSTRAINED SPANNING TREE instances

An instance $(n, E, K)$ of
DEGREE-CONSTRAINED SPANNING TREE is well formed when $n > 0$, the list $E$ has no repeated
entries, and every pair $(u, v)$ in $E$ satisfies $u < n$, $v < n$ and $u \ne v$, with the
reversed pair $(v, u)$ not in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/degree-constrained-spanning-tree/index.html#well-formed).

## Feasibility for DEGREE-CONSTRAINED SPANNING TREE

An instance $(n, E, K)$ of
DEGREE-CONSTRAINED SPANNING TREE is feasible when there is a list $T$ of pairs of natural numbers
such that $T$ is a sublist of $E$ (obtained by deleting entries and keeping the order), $T$ has no
repeated entries, $T$ has exactly $n - 1$ entries, the graph of $T$ on $n$ vertices is connected,
and for every vertex $v < n$ there is no sublist of $T$ with $K + 1$ entries each of which has $v$
as one of its two components.

For a well-formed instance this says that the graph of $E$ on $n$ vertices has a spanning tree in
which every vertex has degree at most $K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.DegreeConstrainedSpanningTreeFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/degree-constrained-spanning-tree/index.html#degree-constrained-spanning-tree-feasibl).

## DEGREE-CONSTRAINED SPANNING TREE as a decision problem

The decision problem
DEGREE-CONSTRAINED SPANNING TREE accepts a bitstring $x$ exactly when bitstring decoding of $x$ as
a triple $(n, E, K)$ succeeds and returns an instance of DEGREE-CONSTRAINED SPANNING TREE that is
both well formed and feasible; every bitstring that does not decode is rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.degreeConstrainedSpanningTreeDec`, a definition declared in [WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/degree-constrained-spanning-tree/index.html#degree-constrained-spanning-tree-dec).

## DEGREE-CONSTRAINED SPANNING TREE is NP-complete

The decision problem
DEGREE-CONSTRAINED SPANNING TREE belongs to the class NP, and every decision problem in NP has a
polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), DEGREE-CONSTRAINED SPANNING TREE (the `K = 2` slice is Hamiltonian path).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.DegreeConstrainedSpanningTree.degreeConstrainedSpanningTree_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DegreeConstrainedSpanningTreeWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/degree-constrained-spanning-tree/index.html#degree-constrained-spanning-tree-np-comp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Degree-constrained spanning tree](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/degree-constrained-spanning-tree/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/degree-constrained-spanning-tree)
