---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.DirectedPathCoverInstance, MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.DAdj, MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.WellFormed, MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.DirectedPathCoverFeasible, MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.directedPathCoverDec, MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.directedPathCover_npComplete
statement: formalized
---

# Path cover of a digraph

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph/index.html).

## Instances of DIRECTED PATH COVER

An instance of DIRECTED PATH COVER is a triple
$(n, E, K)$, where the natural number $n$ is the number of vertices, the list $E$ of ordered
pairs of natural numbers lists the directed edges, and the natural number $K$ bounds the number
of paths.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.DirectedPathCoverInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph/index.html#directed-path-cover-instance).

## Directed adjacency in an edge list

For a list $E$ of ordered pairs of natural numbers
and natural numbers $u$ and $v$, the directed adjacency test of $E$ at $(u, v)$ is the boolean
that is true exactly when the pair $(u, v)$ occurs in $E$, that is, when $E$ contains an edge
from $u$ to $v$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.DAdj`, a definition declared in [WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph/index.html#dadj).

## Well-formed DIRECTED PATH COVER instances

An instance $(n, E, K)$ of
DIRECTED PATH COVER is well formed when the edge list $E$ has no repeated entries and every
edge $(a, b)$ in $E$ satisfies $a < n$, $b < n$ and $a \ne b$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph/index.html#well-formed).

## Feasible DIRECTED PATH COVER instances

An instance $(n, E, K)$ of DIRECTED PATH
COVER is feasible when there is a list of at most $K$ paths, each a list of natural numbers,
such that every path has no repeated vertex, every vertex on a path is less than $n$, and
whenever $v$ immediately follows $u$ on a path the pair $(u, v)$ occurs in $E$; and such that
every vertex $v < n$ lies on some path, and all paths containing $v$ are equal.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.DirectedPathCoverFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph/index.html#directed-path-cover-feasible).

## DIRECTED PATH COVER as a decision problem

DIRECTED PATH COVER is the decision problem
that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding,
to an instance $(n, E, K)$ of DIRECTED PATH COVER that is well formed and feasible; bitstrings
that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.directedPathCoverDec`, a definition declared in [WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph/index.html#directed-path-cover-dec).

## DIRECTED PATH COVER is NP-complete

The decision problem DIRECTED PATH COVER is in NP,
and every decision problem in NP has a polynomial-time many-one reduction to
DIRECTED PATH COVER.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), PATH COVER (the `K = 1` slice is Hamiltonian path).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.DirectedPathCover.directedPathCover_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DirectedPathCoverWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph/index.html#directed-path-cover-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Path cover of a digraph](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/path-cover-of-a-digraph)
