---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.IndependentDominatingSetInstance, MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.Graph, MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.WellFormed, MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.IndependentDominatingSetFeasible, MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.independentDominatingSetDec, MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.independentDominatingSet_npComplete
statement: formalized
---

# Independent dominating set

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set/index.html).

## Independent dominating set instances

An instance of INDEPENDENT DOMINATING SET is a
triple $(n, E, K)$ of a natural number $n$, the number of vertices, a list $E$ of pairs of
natural numbers, the edges, and a natural number $K$, the bound on the size of the set.

Formalized by `MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.IndependentDominatingSetInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set/index.html#independent-dominating-set-instance).

## Graph of an independent dominating set instance

For an independent dominating set
instance with $n$ vertices and edge list $E$, the graph of the instance is the simple graph on
$\{0, \dots, n-1\}$ in which distinct vertices $u$ and $v$ are adjacent when $(u, v)$ or
$(v, u)$ belongs to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set/index.html#graph).

## Well-formed independent dominating set instances

An independent dominating set instance
$(n, E, K)$ is well formed when the list $E$ has no repeated entries and every pair $(a, b)$ in
$E$ satisfies $a < n$, $b < n$, $a \ne b$, and $(b, a)$ does not belong to $E$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set/index.html#well-formed).

## Instances with a small independent dominating set

An independent dominating set instance
$(n, E, K)$ has a small independent dominating set when there is a set $S$ of vertices of its
graph with at most $K$ elements such that every vertex lies in $S$ or is adjacent to a vertex of
$S$, and no two distinct vertices of $S$ are adjacent.

Formalized by `MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.IndependentDominatingSetFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set/index.html#independent-dominating-set-feasible).

## INDEPENDENT DOMINATING SET as a decision problem

The decision problem INDEPENDENT
DOMINATING SET accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring
encoding, to an independent dominating set instance $(n, E, K)$ that is well formed and whose
graph has an independent dominating set of at most $K$ vertices. It rejects every bitstring
that does not decode to an instance.

Formalized by `MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.independentDominatingSetDec`, a definition declared in [WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set/index.html#independent-dominating-set-dec).

## INDEPENDENT DOMINATING SET is NP-complete

The decision problem INDEPENDENT DOMINATING
SET belongs to NP, and every decision problem in NP has a polynomial-time many-one reduction to
it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), INDEPENDENT DOMINATING SET (a small maximal independent set).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.IndependentDominatingSet.independentDominatingSet_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/IndependentDominatingSetWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set/index.html#independent-dominating-set-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Independent dominating set](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/independent-dominating-set)
