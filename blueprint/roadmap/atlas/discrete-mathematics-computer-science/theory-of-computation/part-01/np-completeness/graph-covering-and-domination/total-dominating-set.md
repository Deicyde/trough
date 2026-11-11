---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.TotalDominatingSetInstance, MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.Graph, MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.WellFormed, MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.TotalDominatingSetFeasible, MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.totalDominatingSetDec, MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.totalDominatingSet_npComplete
statement: formalized
---

# Total dominating set

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set/index.html).

## Instances of TOTAL DOMINATING SET

An instance of TOTAL DOMINATING SET is a triple
$(n, E, K)$ consisting of a natural number $n$, the number of vertices, a list $E$ of pairs of
natural numbers, the edges, and a natural number $K$, the bound.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.TotalDominatingSetInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set/index.html#total-dominating-set-instance).

## Graph of a total dominating set instance

The graph of an instance $(n, E, K)$ of TOTAL
DOMINATING SET is the simple graph on $\{0, \dots, n-1\}$ in which distinct vertices $i$ and $j$
are adjacent when $(i, j)$ or $(j, i)$ belongs to $E$. Loops are dropped, and pairs with an
endpoint at least $n$ contribute no edge.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set/index.html#graph).

## Well-formed total dominating set instances

An instance $(n, E, K)$ of TOTAL DOMINATING
SET is well formed when the list $E$ has no repeated entries and every pair $(u, v)$ in $E$
satisfies $u < n$, $v < n$ and $u \ne v$, and its reversal $(v, u)$ does not belong to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set/index.html#well-formed).

## Feasibility of a total dominating set instance

An instance $(n, E, K)$ of TOTAL
DOMINATING SET is feasible when there is a set $S$ of at most $K$ vertices of its graph such that
every vertex $v$ of the graph, including the vertices of $S$, is adjacent to some vertex
$u \in S$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.TotalDominatingSetFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set/index.html#total-dominating-set-feasible).

## The decision problem TOTAL DOMINATING SET

TOTAL DOMINATING SET accepts a bitstring $x$
exactly when $x$ decodes, under the canonical bitstring encoding of triples of a natural number,
a list of pairs of natural numbers and a natural number, to an instance $(n, E, K)$ that is well
formed and feasible: some set of at most $K$ vertices of the graph of the instance contains a
neighbor of every vertex. Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.totalDominatingSetDec`, a definition declared in [WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set/index.html#total-dominating-set-dec).

## TOTAL DOMINATING SET is NP-complete

The decision problem TOTAL DOMINATING SET belongs to
NP, and every decision problem in NP reduces to TOTAL DOMINATING SET by a polynomial-time
many-one reduction.

## Sources

- E. J. Cockayne, R. M. Dawes, and S. T. Hedetniemi, "Total domination in graphs", Networks 10 (1980), 211-219; R. Laskar, J. Pfaff, S. M. Hedetniemi, and S. T. Hedetniemi, "On the algorithmic complexity of total domination", SIAM Journal on Algebraic and Discrete Methods 5 (1984), 420-425.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.TotalDominatingSet.totalDominatingSet_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/TotalDominatingSetWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set/index.html#total-dominating-set-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Total dominating set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/total-dominating-set)
