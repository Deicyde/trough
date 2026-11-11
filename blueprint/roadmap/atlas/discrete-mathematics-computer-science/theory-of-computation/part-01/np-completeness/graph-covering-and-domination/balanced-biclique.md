---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.BalancedBicliqueInstance, MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.Graph, MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.WellFormed, MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.BalancedBicliqueFeasible, MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.balancedBicliqueDec, MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.balancedBiclique_npComplete
statement: formalized
---

# Balanced biclique

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique/index.html).

## Balanced biclique instances

An instance of BALANCED BICLIQUE is a triple $(n, es, K)$
consisting of a natural number $n$ (the number of vertices), a list $es$ of pairs of natural
numbers (the edges) and a natural number $K$ (the bound).

Formalized by `MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.BalancedBicliqueInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique/index.html#balanced-biclique-instance).

## Graph of a balanced biclique instance

The graph of a balanced biclique instance
$(n, es, K)$ is the simple graph on $\{0, \dots, n-1\}$ in which distinct vertices $u$ and $v$
are adjacent when $(u, v)$ or $(v, u)$ belongs to $es$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.Graph`, a definition declared in [WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique/index.html#graph).

## Well-formed balanced biclique instances

A balanced biclique instance $(n, es, K)$ is
well formed when the entries of the list $es$ are distinct and every pair $(u, v)$ in $es$
satisfies $u < n$, $v < n$, $u \neq v$ and $(v, u) \notin es$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique/index.html#well-formed).

## Feasible balanced biclique instances

A balanced biclique instance $(n, es, K)$ is
feasible when there are disjoint sets $A$ and $B$ of exactly $K$ vertices each in
$\{0, \dots, n-1\}$ such that every vertex of $A$ is adjacent to every vertex of $B$, where
distinct vertices $u$ and $v$ are adjacent when $(u, v)$ or $(v, u)$ belongs to $es$. In other
words, the graph contains a complete bipartite subgraph $K_{K,K}$, not necessarily induced.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.BalancedBicliqueFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique/index.html#balanced-biclique-feasible).

## The decision problem BALANCED BICLIQUE

BALANCED BICLIQUE is the decision problem that
accepts a bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a
balanced biclique instance $(n, es, K)$ that is well formed (the entries of $es$ are distinct,
and every pair $(u, v)$ in $es$ has $u < n$, $v < n$, $u \neq v$ and $(v, u) \notin es$) and for
which there are disjoint sets $A$ and $B$ of exactly $K$ vertices each in $\{0, \dots, n-1\}$
such that every vertex of $A$ is adjacent to every vertex of $B$, where distinct vertices $u$ and
$v$ are adjacent when $(u, v)$ or $(v, u)$ belongs to $es$. Bitstrings that do not decode are
rejected.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.balancedBicliqueDec`, a definition declared in [WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique/index.html#balanced-biclique-dec).

## BALANCED BICLIQUE is NP-complete

The decision problem BALANCED BICLIQUE belongs to NP,
and every decision problem in NP reduces to it by a polynomial-time many-one reduction.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability* (1979), BALANCED COMPLETE BIPARTITE SUBGRAPH; D. S. Johnson, "The NP- completeness column" (1987).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.BalancedBiclique.balancedBiclique_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BalancedBicliqueWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique/index.html#balanced-biclique-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Balanced biclique](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/graph-covering-and-domination/balanced-biclique)
