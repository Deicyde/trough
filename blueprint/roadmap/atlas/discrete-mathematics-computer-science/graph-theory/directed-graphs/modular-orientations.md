---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.JaegerModularOrientationWanted.CrossesCut, MathlibExt.Combinatorics.JaegerModularOrientationWanted.cutSize, MathlibExt.Combinatorics.JaegerModularOrientationWanted.IsFourKEdgeConnected, MathlibExt.Combinatorics.JaegerModularOrientationWanted.orientedTail, MathlibExt.Combinatorics.JaegerModularOrientationWanted.orientedHead, MathlibExt.Combinatorics.JaegerModularOrientationWanted.indegree, MathlibExt.Combinatorics.JaegerModularOrientationWanted.outdegree, MathlibExt.Combinatorics.JaegerModularOrientationWanted.IsModularOrientation
statement: formalized
---

# Modular orientations

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html).

## Edges crossing a cut

Consider a multigraph with vertex set $V$ and edge set $E$ in which
each edge has a first and a second endpoint. For a set $S \subseteq V$, an edge crosses the cut at
$S$ when exactly one of its two endpoints lies in $S$.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.CrossesCut`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#crosses-cut).

## Size of a cut

Consider a multigraph with finitely many edges in which each edge has a
first and a second endpoint. For a set $S$ of vertices, the size of the cut at $S$ is the number
of edges crossing it, that is, having exactly one endpoint in $S$. Distinct parallel edges are
counted separately.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.cutSize`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#cut-size).

## 4k-edge-connected multigraphs

For a natural number $k$, a finite multigraph is
$4k$-edge-connected when it has at least two vertices and, for every set $S$ of vertices such that
both $S$ and its complement are nonempty, at least $4k$ edges cross the cut at $S$, that is, have
exactly one endpoint in $S$. Parallel edges are counted separately. For $k \ge 1$ the condition
implies that the multigraph is connected.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.IsFourKEdgeConnected`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#is-four-kedge-connected).

## Tail of an oriented edge

Each edge $e$ of the multigraph has a reference direction from
its first endpoint to its second endpoint, and an orientation chooses for each edge whether to
reverse it. The tail of $e$ is its first endpoint if $e$ is not reversed and its second endpoint
if $e$ is reversed.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.orientedTail`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#oriented-tail).

## Head of an oriented edge

Each edge $e$ of the multigraph has a reference direction from
its first endpoint to its second endpoint, and an orientation chooses for each edge whether to
reverse it. The head of $e$ is its second endpoint if $e$ is not reversed and its first endpoint
if $e$ is reversed.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.orientedHead`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#oriented-head).

## Indegree

In a multigraph with finitely many edges and a chosen orientation, the
indegree of a vertex $v$ is the number of edges whose head is $v$, parallel edges counted
separately.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.indegree`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#indegree).

## Outdegree

In a multigraph with finitely many edges and a chosen orientation, the
outdegree of a vertex $v$ is the number of edges whose tail is $v$, parallel edges counted
separately.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.outdegree`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#outdegree).

## Modular orientations

For a natural number $k$, an orientation of a multigraph with
finitely many edges is a modulo $(2k+1)$ orientation when at every vertex the indegree minus the
outdegree is congruent to $0$ modulo $2k + 1$.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.IsModularOrientation`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#is-modular-orientation).

## Jaeger's modular orientation conjecture

This is the statement that for every integer
$k \ge 1$, every finite multigraph (loops and parallel edges allowed) that has at least two
vertices, and in which every partition of the vertices into two nonempty sets is crossed by at
least $4k$ edges, admits an orientation of its edges in which, at every vertex, the indegree minus
the outdegree is divisible by $2k + 1$.

The parameter $k$ is positive, as in the source discussion of $(2 + 1/k)$-flows and its
specializations at $k = 1$ and $k = 2$.

Formalized by `MathlibExt.Combinatorics.JaegerModularOrientationWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#conjecture).

## Jaeger's modular orientation conjecture is false

There exist an integer $k \ge 1$ and a
finite multigraph (loops and parallel edges allowed) with at least two vertices, in which every
partition of the vertices into two nonempty sets is crossed by at least $4k$ edges, such that no
orientation of the edges makes the indegree minus the outdegree of every vertex divisible by
$2k + 1$.

Han, Li, Wu and Zhang (J. Combin. Theory Ser. B 131 (2018) 1-11) construct, for every $k \ge 3$,
a $4k$-edge-connected graph with no circular $(2+1/k)$-flow, equivalently no modulo $(2k+1)$
orientation; the cases $k = 1$ (Tutte's 3-flow conjecture) and $k = 2$ remain open.

## Sources

- Daniel W. Cranston and Jiaao Li, Circular flows in planar graphs, SIAM J. Discrete Math. (2020), arXiv:1812.09833, https://arxiv.org/abs/1812.09833.

Stated but not proved: `MathlibExt.Combinatorics.JaegerModularOrientationWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/JaegerModularOrientationWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/JaegerModularOrientationWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modular orientations](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/modular-orientations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/directed-graphs/modular-orientations)
