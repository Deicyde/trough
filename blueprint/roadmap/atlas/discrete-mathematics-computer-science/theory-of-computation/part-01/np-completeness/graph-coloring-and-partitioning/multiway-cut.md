---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MultiwayCut.MultiwayCutInstance, MetaMathlibExt.Complexity.NPComplete.MultiwayCut.WellFormed, MetaMathlibExt.Complexity.NPComplete.MultiwayCut.MultiwayCutFeasible, MetaMathlibExt.Complexity.NPComplete.MultiwayCut.multiwayCutDec, MetaMathlibExt.Complexity.NPComplete.MultiwayCut.multiwayCut_npComplete
statement: formalized
---

# Multiway cut

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/multiway-cut/index.html).

## Multiway cut instances

A multiway cut instance is a tuple $(n, E, T, K)$ consisting of a
natural number $n$ (the number of vertices), a list $E$ of pairs of natural numbers (the edges), a
list $T$ of natural numbers (the terminals) and a natural number $K$ (the bound on the number of
cut edges).

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultiwayCut.MultiwayCutInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/multiway-cut/index.html#multiway-cut-instance).

## Well-formed multiway cut instances

A multiway cut instance $(n, E, T, K)$ is well-formed
when the entries of $E$ are pairwise distinct; every entry $(u, v)$ of $E$ satisfies $u < n$,
$v < n$ and $u \ne v$, and $(v, u)$ is not an entry of $E$; the entries of $T$ are pairwise
distinct; and every entry $t$ of $T$ satisfies $t < n$. Thus $E$ lists each edge of a simple
undirected graph on the vertices $0, \dots, n-1$ exactly once, in one orientation, and $T$ is a
list of distinct vertices. No condition is imposed on $K$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultiwayCut.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/multiway-cut/index.html#well-formed).

## Feasible multiway cut instances

Let $(n, E, T, K)$ be a multiway cut instance with
terminal list $T = (t_0, \dots, t_{k-1})$. It is feasible when there is a labelling $f$ of the
vertices $0, \dots, n-1$ by labels in $\{0, \dots, \max(k, 1) - 1\}$ such that $f(t_j) = j$ for
every $j < k$, and at most $K$ entries $(u, v)$ of $E$, counted with repetition, satisfy
$f(u) \ne f(v)$. Here every number $v \ge n$ counts as a vertex with label $0$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultiwayCut.MultiwayCutFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/multiway-cut/index.html#multiway-cut-feasible).

## The MULTIWAY CUT decision problem

MULTIWAY CUT is the decision problem on bitstrings that
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
multiway cut instance $(n, E, T, K)$ that is well-formed and feasible. Bitstrings that do not
decode to a multiway cut instance are rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MultiwayCut.multiwayCutDec`, a definition declared in [WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/multiway-cut/index.html#multiway-cut-dec).

## MULTIWAY CUT is NP-complete

Let MULTIWAY CUT be the decision problem that accepts exactly
the bitstrings decoding to a well-formed, feasible multiway cut instance: a simple undirected graph
on the vertices $0, \dots, n-1$, a list of distinct terminal vertices and a bound $K$ such that
deleting at most $K$ edges of the graph leaves no two terminals connected. Then MULTIWAY CUT is in
NP, and every decision problem in NP reduces to MULTIWAY CUT by a polynomial-time many-one
reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), MULTIWAY CUT; E. Dahlhaus et al., "The complexity of multiterminal cuts" (1994).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MultiwayCut.multiwayCut_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/NPComplete/MultiwayCutWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/multiway-cut/index.html#multiway-cut-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiway cut](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/multiway-cut/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-coloring-and-partitioning/multiway-cut)
