---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.SubgraphIsomorphismInstance, MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.GraphHost, MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.WellFormed, MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.SubgraphIsomorphismFeasible, MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.subgraphIsomorphismDec, MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.subgraphIsomorphism_npComplete
statement: formalized
---

# Subgraph isomorphism

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism/index.html).

## Subgraph-isomorphism instances

A subgraph-isomorphism instance is a tuple
$(n, E_G, m, E_H)$ of a natural number $n$ (the number of host vertices), a list $E_G$ of pairs
of natural numbers (the host edges), a natural number $m$ (the number of pattern vertices) and a
list $E_H$ of pairs of natural numbers (the pattern edges).

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.SubgraphIsomorphismInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism/index.html#subgraph-isomorphism-instance).

## Host graph of a subgraph-isomorphism instance

For a subgraph-isomorphism instance
$(n, E_G, m, E_H)$, the host graph is the graph of the edge list $E_G$ on $n$ vertices: the simple
graph on $\{0, \dots, n - 1\}$ in which distinct vertices $i$ and $j$ are adjacent when $(i, j)$
or $(j, i)$ belongs to $E_G$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.GraphHost`, a definition declared in [WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism/index.html#graph-host).

## Well-formed subgraph-isomorphism instances

A subgraph-isomorphism instance
$(n, E_G, m, E_H)$ is well formed when the list $E_G$ has no repeated entries and every
$(u, v) \in E_G$ satisfies $u < n$, $v < n$, $u \ne v$ and $(v, u) \notin E_G$, and likewise the
list $E_H$ has no repeated entries and every $(u, v) \in E_H$ satisfies $u < m$, $v < m$,
$u \ne v$ and $(v, u) \notin E_H$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism/index.html#well-formed).

## Feasible subgraph-isomorphism instances

A subgraph-isomorphism instance
$(n, E_G, m, E_H)$ is feasible when there is an injective map
$f : \{0, \dots, m - 1\} \to \{0, \dots, n - 1\}$ such that for every $(u, v) \in E_H$ with
$u < m$ and $v < m$, the vertices $f(u)$ and $f(v)$ are adjacent in the host graph of the
instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.SubgraphIsomorphismFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism/index.html#subgraph-isomorphism-feasible).

## SUBGRAPH ISOMORPHISM as a decision problem

The decision problem SUBGRAPH ISOMORPHISM
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of
subgraph-isomorphism instances, to an instance that is well formed and feasible. Bitstrings that
do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.subgraphIsomorphismDec`, a definition declared in [WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism/index.html#subgraph-isomorphism-dec).

## SUBGRAPH ISOMORPHISM is NP-complete

The decision problem SUBGRAPH ISOMORPHISM belongs
to NP, and every decision problem $L$ in NP has a polynomial-time many-one reduction to
SUBGRAPH ISOMORPHISM.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), SUBGRAPH ISOMORPHISM.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.SubgraphIsomorphism.subgraphIsomorphism_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/SubgraphIsomorphismWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism/index.html#subgraph-isomorphism-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgraph isomorphism](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/paths-cycles-and-subgraphs/subgraph-isomorphism)
