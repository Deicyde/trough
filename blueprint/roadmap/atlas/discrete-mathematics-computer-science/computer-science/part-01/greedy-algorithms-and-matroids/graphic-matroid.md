---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.GraphicMatroid.card_connectedComponent_deleteEdges_of_not_reachable, Cslib.Algorithms.Lean.GraphicMatroid.ncard_edgeSet_add_card_connectedComponent, Cslib.Algorithms.Lean.GraphicMatroid.exists_insert_isAcyclic, Cslib.Algorithms.Lean.GraphicMatroid.IsForestSet, Cslib.Algorithms.Lean.GraphicMatroid.graphicMatroid, Cslib.Algorithms.Lean.GraphicMatroid.chosen, Cslib.Algorithms.Lean.GraphicMatroid.bridgeIn, Cslib.Algorithms.Lean.GraphicMatroid.bridgeIn_iff
statement: formalized
proof: formalized
---

# Graphic matroid

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html).

## Deleting a bridge adds one component

## Deleting a bridge adds one component

Let $H$ be a simple graph on a finite vertex set
and let $ab$ be an edge of $H$. If $a$ and $b$ are not connected in the graph obtained from $H$
by deleting the edge $ab$, then that graph has exactly one more connected component than $H$.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.card_connectedComponent_deleteEdges_of_not_reachable`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#card-connected-component-delete-edges-of).

## Edges plus components of a forest

Let $V$ be a finite vertex set. For every natural
number $n$ and every forest (acyclic simple graph) $F$ on $V$ with exactly $n$ edges, the number
of edges of $F$ plus the number of connected components of $F$ equals $|V|$. So a forest on $V$
with $e$ edges has $|V| - e$ connected components.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.ncard_edgeSet_add_card_connectedComponent`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#ncard-edge-set-add-card-connected-compon).

## Augmentation property of forests

Let $G$ be a simple graph on a finite vertex set, and
let $I$ and $J$ be sets of edges of $G$ that each form an acyclic graph. If $|I| < |J|$, then there
is an edge $e \in J$ with $e \notin I$ such that $I \cup \{e\}$ still forms an acyclic graph.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.exists_insert_isAcyclic`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#exists-insert-is-acyclic).

## Forests of a graph

A set $I$ of unordered pairs of vertices is a forest of a simple graph
$G$ when every element of $I$ is an edge of $G$ and the graph with edge set $I$ has no cycles.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.IsForestSet`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#is-forest-set).

## Graphic matroid

For a simple graph $G$ on a finite vertex set, the graphic matroid of $G$
is the matroid on unordered pairs of vertices whose ground set is the edge set of $G$ and whose
independent sets are the forests of $G$, that is, the sets of edges of $G$ that form an acyclic
graph.

That these sets form a matroid is CLRS Theorem 16.5.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.graphicMatroid`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#graphic-matroid).

## Graph of a finite edge set

The graph of a finite edge set, with decidable adjacency.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.chosen`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#chosen).

## Bridge test for an edge set

On a finite vertex set, for a finite set $S$ of unordered
pairs of vertices and a pair $e = \{u, v\}$, the bridge test returns true exactly when $u$ and $v$
are not connected by a path in the graph whose edges are the non-loop pairs of $S \setminus \{e\}$.
When $e \in S$ is not a loop, this says that $e$ is a bridge of $S$: deleting it disconnects its
endpoints.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.bridgeIn`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#bridge-in).

## Characterization of the bridge test

On a finite vertex set, let $S$ be a finite set of
unordered pairs of vertices and let $u$, $v$ be vertices. The bridge test of $S$ on the pair
$\{u, v\}$ returns true if and only if $u$ and $v$ are not connected by a path in the graph whose
edges are the non-loop pairs of $S \setminus \{\{u, v\}\}$.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.bridgeIn_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#bridge-in-iff).

## Forest oracle

For a simple graph $G$ on a finite vertex set, the forest oracle accepts a
finite set $S$ of unordered pairs of vertices exactly when every $e \in S$ is an edge of $G$ and
passes the bridge test in $S$: its endpoints are not connected in the graph formed by the other
pairs of $S$. It serves as the independence oracle of the graphic matroid of $G$, since a graph
is a forest if and only if every edge is a bridge.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.forestOracle`, a definition declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#forest-oracle).

## The forest oracle decides graphic-matroid independence

For a simple graph $G$ on a
finite vertex set and a finite set $S$ of unordered pairs of vertices, the forest oracle of $G$
accepts $S$ if and only if $S$ is independent in the graphic matroid of $G$.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.forestOracle_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#forest-oracle-iff).

## Kruskal's algorithm returns a forest

Let $G$ be a simple graph on a finite vertex type
$V$. For every list $L$ of unordered pairs of vertices, the matroid greedy algorithm run on $L$
with the forest oracle of $G$ returns a forest of $G$: a set of edges of $G$ without cycles.

This is Kruskal's algorithm in the form of CLRS Section 16.4, the greedy algorithm on the graphic
matroid.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.kruskal_isForest`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#kruskal-is-forest).

## Optimality of Kruskal's algorithm

Let $G$ be a simple graph on a finite vertex type
$V$, let $w$ assign a natural number to each unordered pair of vertices, and let $L$ be a list
of unordered pairs of vertices in nonincreasing order of $w$ (each entry weighs at least as much
as every later one). Let $T$ be the set returned by the matroid greedy algorithm run on $L$ with
the forest oracle of $G$. Then every forest $I$ of $G$ all of whose edges occur in $L$ satisfies
$\sum_{x \in I} w(x) \le \sum_{x \in T} w(x)$.

This is CLRS Theorem 16.11 on the graphic matroid.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.kruskal_optimal`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#kruskal-optimal).

## Kruskal's algorithm returns a maximal forest

Let $G$ be a simple graph on a finite vertex
set and let $L$ be a list of unordered pairs of vertices such that a pair is an edge of $G$ if and
only if it occurs in $L$. Then the matroid greedy algorithm run with the forest oracle of $G$ on
$L$ returns a base of the graphic matroid of $G$, that is, a maximal forest of $G$.

Formalized by `Cslib.Algorithms.Lean.GraphicMatroid.kruskal_isBase`, a theorem declared in [CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Greedy/GraphicMatroid.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html#kruskal-is-base).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graphic matroid](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/greedy-algorithms-and-matroids/graphic-matroid)
