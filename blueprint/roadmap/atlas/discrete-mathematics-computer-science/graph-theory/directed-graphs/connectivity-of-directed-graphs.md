---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.IsDirectedPath, MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.internalVertices, MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.HasInternallyDisjointPaths, MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.hamidouneSomeRAtLeastThree, MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.hamidouneSomeRAtLeastThree_refuted
statement: formalized
---

# Connectivity of directed graphs

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/connectivity-of-directed-graphs/index.html).

## Directed paths

A directed path in a digraph $D$ is a finite, possibly empty, sequence of
vertices of $D$ with no vertex repeated in which each vertex is joined to the next by an arc of
$D$.

Formalized by `MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.IsDirectedPath`, a definition declared in [WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/connectivity-of-directed-graphs/index.html#is-directed-path).

## Internal vertices of a path

The internal vertices of a path given as a vertex list (all but the first and the last).

Formalized by `MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.internalVertices`, a definition declared in [WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/connectivity-of-directed-graphs/index.html#internal-vertices).

## Internally disjoint directed paths

Let $D$ be a digraph, $r$ a natural number and $y$, $x$
vertices of $D$. We write $\kappa(y, x) \ge r$ when there are $r$ pairwise distinct directed paths
in $D$ from $y$ to $x$, no two of which share an internal vertex. Here a directed path from $y$ to
$x$ is a sequence of distinct vertices starting at $y$ and ending at $x$ in which each vertex is
joined to the next by an arc of $D$, and its internal vertices are all its vertices except the
first and the last.

Formalized by `MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.HasInternallyDisjointPaths`, a definition declared in [WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/connectivity-of-directed-graphs/index.html#has-internally-disjoint-paths).

## Hamidoune's reverse-connectivity conjecture for some $r \ge 3$

The statement that there
is a natural number $r \ge 3$ such that every digraph $D$ without loops or parallel arcs on a
finite nonempty vertex set, in which every vertex has at least $r$ out-neighbours and at least
$r$ in-neighbours, has an arc $(x, y)$ from $x$ to $y$ with $\kappa(y, x) \ge r$, that is, with
$r$ pairwise distinct directed paths from $y$ to $x$, no two of which share an internal vertex.
Here a directed path is a sequence of distinct vertices in which each vertex is joined to the
next by an arc, and its internal vertices are all its vertices except the first and the last.

Formalized by `MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.hamidouneSomeRAtLeastThree`, a definition declared in [WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/connectivity-of-directed-graphs/index.html#hamidoune-some-rat-least-three).

## Hamidoune's reverse-connectivity conjecture fails for every $r \ge 3$

For no natural
number $r \ge 3$ does the following hold: every digraph $D$ without loops or parallel arcs on a
finite nonempty vertex set, in which every vertex has at least $r$ out-neighbours and at least
$r$ in-neighbours, has an arc $(x, y)$ from $x$ to $y$ with $\kappa(y, x) \ge r$, that is, with
$r$ pairwise distinct directed paths from $y$ to $x$, no two of which share an internal vertex.
Here a directed path is a sequence of distinct vertices in which each vertex is joined to the
next by an arc, and its internal vertices are all its vertices except the first and the last.

Thomassen constructed, for every positive integer $r$, a digraph without digons with minimum
out-degree and minimum in-degree at least $r$ in which no arc $(x, y)$ has $\kappa(y, x) \ge 3$;
the report notes after Conjecture 6.21 that this is a counterexample for all $r \ge 3$.

## Sources

- B. D. Sullivan, A Summary of Problems and Results related to the Caccetta-Haggkvist Conjecture, arXiv:math/0605646, Conjecture 6.21; resolution: C. Thomassen, Even cycles in directed graphs, European J. Combin. 6 (1985) 85-89, as stated in the report's Theorem 5.2 (part ii) and the note after Conjecture 6.21, https://doi.org/10.1016/S0195-6698(85)80025-1.

Stated but not proved: `MathlibExt.Combinatorics.HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.hamidouneSomeRAtLeastThree_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HamidouneReverseConnectivityAIMCombinatoricsProblem191Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/connectivity-of-directed-graphs/index.html#hamidoune-some-rat-least-three-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Connectivity of directed graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/connectivity-of-directed-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/directed-graphs/connectivity-of-directed-graphs)
