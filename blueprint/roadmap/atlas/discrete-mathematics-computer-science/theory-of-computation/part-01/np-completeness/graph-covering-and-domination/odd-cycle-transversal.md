---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.OddCycleTransversalInstance, MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.Graph, MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.WellFormed, MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.OddCycleTransversalFeasible, MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.oddCycleTransversalDec, MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.oddCycleTransversal_npComplete
statement: formalized
---

# Odd cycle transversal

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal/index.html).

## Odd cycle transversal instances

An odd cycle transversal instance is a triple
$(n, es, K)$ of a natural number $n$ (the number of vertices), a list $es$ of pairs of natural
numbers (the edges) and a natural number $K$ (the bound on the number of removed vertices).

Formalized by `MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.OddCycleTransversalInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal/index.html#odd-cycle-transversal-instance).

## Graph of an odd cycle transversal instance

For an odd cycle transversal instance
$(n, es, K)$, its graph is the graph of the edge list $es$ on $n$ vertices: the simple graph on
$\{0, \dots, n-1\}$ in which distinct vertices $i$ and $j$ are adjacent when $(i, j)$ or $(j, i)$
belongs to $es$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal/index.html#graph).

## Well-formed odd cycle transversal instances

An odd cycle transversal instance
$(n, es, K)$ is well formed when the list $es$ has no repeated entries and every pair $(u, v)$ in
$es$ satisfies $u < n$, $v < n$ and $u \ne v$, and $(v, u)$ does not belong to $es$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal/index.html#well-formed).

## Feasible odd cycle transversal instances

An odd cycle transversal instance $(n, es, K)$
is feasible when there is a set $S$ of at most $K$ vertices of its graph such that the subgraph
induced on the vertices outside $S$ is bipartite.

Formalized by `MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.OddCycleTransversalFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal/index.html#odd-cycle-transversal-feasible).

## ODD CYCLE TRANSVERSAL as a decision problem

The decision problem ODD CYCLE TRANSVERSAL
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to an
odd cycle transversal instance $(n, es, K)$ that is well formed and feasible. Well formed means
that $es$ has no repeated entries and every pair $(u, v)$ in $es$ satisfies $u < n$, $v < n$,
$u \ne v$ and $(v, u) \notin es$; feasible means that some set of at most $K$ vertices can be
removed from the graph of the instance so that the remaining induced subgraph is bipartite.
Bitstrings that do not decode to an instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.oddCycleTransversalDec`, a definition declared in [WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal/index.html#odd-cycle-transversal-dec).

## ODD CYCLE TRANSVERSAL is NP-complete

The decision problem ODD CYCLE TRANSVERSAL, which
accepts a bitstring exactly when it decodes to a well-formed instance $(n, es, K)$ whose graph
becomes bipartite after removing some set of at most $K$ vertices, belongs to NP, and every
decision problem in NP has a polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), ODD CYCLE TRANSVERSAL (vertex deletion to a bipartite graph).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.OddCycleTransversal.oddCycleTransversal_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/OddCycleTransversalWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal/index.html#odd-cycle-transversal-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Odd cycle transversal](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/odd-cycle-transversal)
