---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.EdgeDominatingSetInstance, MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.Adj, MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.WellFormed, MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.EdgeDominatingSetFeasible, MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.edgeDominatingSetDec, MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.edgeDominatingSet_npComplete
statement: formalized
---

# Edge dominating set

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set/index.html).

## EDGE DOMINATING SET instances

An instance of EDGE DOMINATING SET is a triple
$(n, E, K)$ of a natural number $n$ (the vertex count), a finite list $E$ of ordered pairs of
natural numbers (the edge list) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.EdgeDominatingSetInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set/index.html#edge-dominating-set-instance).

## Edge-list adjacency for EDGE DOMINATING SET

For a list $E$ of ordered pairs of natural
numbers and natural numbers $u$ and $v$, the Boolean adjacency of $u$ and $v$ in $E$ is true
exactly when $(u, v)$ or $(v, u)$ occurs in $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.Adj`, a definition declared in [WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set/index.html#adj).

## Well-formed EDGE DOMINATING SET instances

An instance with vertex count $n$, edge list
$E$ and bound $K$ is well formed when $E$ has no repeated entries and every pair $(a, b)$ in $E$
satisfies $a < n$, $b < n$ and $a \ne b$, and $(b, a)$ does not occur in $E$. Thus $E$ lists the
edges of a simple graph on the vertices $0, \dots, n - 1$, each once and in one orientation.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set/index.html#well-formed).

## Feasible EDGE DOMINATING SET instances

An instance with vertex count $n$, edge list $E$
and bound $K$ is feasible when some sublist $D$ of $E$ (its entries taken in order) has at most
$K$ entries and dominates every edge of $E$: for every $e \in E$ there is $d \in D$ such that one
of the two entries of $d$ equals one of the two entries of $e$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.EdgeDominatingSetFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set/index.html#edge-dominating-set-feasible).

## The EDGE DOMINATING SET decision problem

EDGE DOMINATING SET is the decision problem
that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding,
to an EDGE DOMINATING SET instance $(n, E, K)$ that is well formed and feasible, that is, some
sublist of $E$ with at most $K$ entries contains, for every edge of $E$, an edge sharing an
endpoint with it. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.edgeDominatingSetDec`, a definition declared in [WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set/index.html#edge-dominating-set-dec).

## EDGE DOMINATING SET is NP-complete

The EDGE DOMINATING SET decision problem belongs to
NP, and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), EDGE DOMINATING SET; M. Yannakakis and F. Gavril, "Edge dominating sets in graphs" (1980).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.EdgeDominatingSet.edgeDominatingSet_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/EdgeDominatingSetWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set/index.html#edge-dominating-set-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Edge dominating set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/edge-dominating-set)
