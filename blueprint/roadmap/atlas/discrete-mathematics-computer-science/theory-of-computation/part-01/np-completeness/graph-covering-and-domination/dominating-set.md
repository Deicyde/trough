---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.DominatingSet.DominatingSetInstance, MetaMathlibExt.Complexity.NPComplete.DominatingSet.Graph, MetaMathlibExt.Complexity.NPComplete.DominatingSet.WellFormed, MetaMathlibExt.Complexity.NPComplete.DominatingSet.DominatingSetFeasible, MetaMathlibExt.Complexity.NPComplete.DominatingSet.dominatingSetDec, MetaMathlibExt.Complexity.NPComplete.DominatingSet.dominatingSet_npComplete
statement: formalized
---

# Dominating set

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set/index.html).

## Instances of DOMINATING SET

An instance of DOMINATING SET is a triple $(n, E, K)$ of a
natural number $n$ (the number of vertices), a list $E$ of pairs of natural numbers (the edges)
and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.DominatingSet.DominatingSetInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/DominatingSetWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DominatingSetWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set/index.html#dominating-set-instance).

## Graph of a DOMINATING SET instance

For an instance $(n, E, K)$ of DOMINATING SET, its
graph is the simple graph on $\{0, \dots, n - 1\}$ in which distinct vertices $i$ and $j$ are
adjacent when $(i, j)$ or $(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DominatingSet.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/DominatingSetWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DominatingSetWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set/index.html#graph).

## Well-formed DOMINATING SET instances

An instance $(n, E, K)$ of DOMINATING SET is well
formed when the list $E$ has no repeated entries and every pair $(u, v) \in E$ satisfies $u < n$,
$v < n$, $u \ne v$ and $(v, u) \notin E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DominatingSet.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/DominatingSetWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DominatingSetWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set/index.html#well-formed).

## Feasibility of a DOMINATING SET instance

An instance $(n, E, K)$ of DOMINATING SET is
feasible when there is a set $S$ of at most $K$ vertices of its graph such that every vertex lies in
$S$ or is adjacent to a vertex of $S$, where the graph has vertex set $\{0, \dots, n - 1\}$ and
distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or $(j, i)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DominatingSet.DominatingSetFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/DominatingSetWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DominatingSetWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set/index.html#dominating-set-feasible).

## DOMINATING SET as a decision problem

The decision problem DOMINATING SET accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a triple
$(n, E, K)$ of a natural number $n$, a list $E$ of pairs of natural numbers and a natural number
$K$ such that $E$ has no repeated entries, every pair $(u, v) \in E$ satisfies $u < n$, $v < n$,
$u \ne v$ and $(v, u) \notin E$, and there is a set $S$ of at most $K$ vertices with every vertex
in $S$ or adjacent to a vertex of $S$, in the graph on $\{0, \dots, n - 1\}$ where distinct $i$
and $j$ are adjacent when $(i, j)$ or $(j, i)$ belongs to $E$. Bitstrings that do not decode are
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.DominatingSet.dominatingSetDec`, a definition declared in [WantedExt/Complexity/NPComplete/DominatingSetWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DominatingSetWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set/index.html#dominating-set-dec).

## DOMINATING SET is NP-complete

The decision problem DOMINATING SET belongs to NP, and
every decision problem in NP reduces to DOMINATING SET by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), DOMINATING SET.

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.DominatingSet.dominatingSet_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/DominatingSetWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/DominatingSetWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set/index.html#dominating-set-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dominating set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/dominating-set)
