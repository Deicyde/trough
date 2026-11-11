---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.DensestKSubgraphInstance, MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.WellFormed, MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.DensestKSubgraphFeasible, MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.densestKSubgraphDec, MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.densestKSubgraph_npComplete
statement: formalized
---

# Densest k-subgraph

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/densest-k-subgraph/index.html).

## Instances of DENSEST k-SUBGRAPH

An instance of DENSEST k-SUBGRAPH is a quadruple
$(n, E, k, m)$ consisting of a natural number $n$ (the number of vertices), a list $E$ of pairs
of natural numbers (the edges), a natural number $k$ (the size of the vertex set sought) and a
natural number $m$ (the edge threshold).

Formalized by `MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.DensestKSubgraphInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/densest-k-subgraph/index.html#densest-ksubgraph-instance).

## Well-formed DENSEST k-SUBGRAPH instances

An instance $(n, E, k, m)$ of DENSEST
k-SUBGRAPH is well formed when the list $E$ has no repeated entries and every pair $(u, v)$ in
$E$ satisfies $u < n$, $v < n$ and $u \ne v$, with the reversed pair $(v, u)$ not in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/densest-k-subgraph/index.html#well-formed).

## Feasibility for DENSEST k-SUBGRAPH

An instance $(n, E, k, m)$ of DENSEST k-SUBGRAPH is
feasible when there are a finite set $S$ of exactly $k$ natural numbers, each less than $n$, and
a sublist $E'$ of $E$ (obtained by deleting entries and keeping the order) with at least $m$
entries such that both components of every pair in $E'$ lie in $S$.

For a well-formed instance this says that some $k$ vertices of the graph of $E$ on $n$ vertices
induce at least $m$ edges.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.DensestKSubgraphFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/densest-k-subgraph/index.html#densest-ksubgraph-feasible).

## DENSEST k-SUBGRAPH as a decision problem

The decision problem DENSEST k-SUBGRAPH accepts
a bitstring $x$ exactly when bitstring decoding of $x$ as a quadruple $(n, E, k, m)$ succeeds and
returns an instance of DENSEST k-SUBGRAPH that is both well formed and feasible; every bitstring
that does not decode is rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.densestKSubgraphDec`, a definition declared in [WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/densest-k-subgraph/index.html#densest-ksubgraph-dec).

## DENSEST k-SUBGRAPH is NP-complete

The decision problem DENSEST k-SUBGRAPH belongs to the
class NP, and every decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- U. Feige, G. Kortsarz, and D. Peleg, "The dense k-subgraph problem" (2001); M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), DENSEST k-SUBGRAPH.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.DensestKSubgraph.densestKSubgraph_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/DensestKSubgraphWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/densest-k-subgraph/index.html#densest-ksubgraph-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Densest k-subgraph](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/densest-k-subgraph/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/densest-k-subgraph)
