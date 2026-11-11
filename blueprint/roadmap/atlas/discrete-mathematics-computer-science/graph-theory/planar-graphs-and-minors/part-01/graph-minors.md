---
declaration: section
origin: cited
lean: MetaMathlibExt.FinGraph, MetaMathlibExt.cliqueFinGraph, MetaMathlibExt.cliqueFinGraph_adj, MetaMathlibExt.MinorStep, MetaMathlibExt.IsMinor, MetaMathlibExt.IsMinor.refl, MetaMathlibExt.IsMinor.trans, MetaMathlibExt.IsMinor.of_step
statement: formalized
---

# Graph minors

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html).

## Finite simple graph

A finite graph consists of a finite vertex set $V$ together with a
simple graph on $V$, that is, a symmetric and irreflexive adjacency relation on $V$.

Stable source: https://en.wikipedia.org/wiki/Robertson%E2%80%93Seymour_theorem.

Formalized by `MetaMathlibExt.FinGraph`, a structure declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#fin-graph).

## Complete graph as a finite graph

For a natural number $n$, $K_n$ is the finite graph whose
vertices are the natural numbers less than $n$, in which any two distinct vertices are adjacent.

Formalized by `MetaMathlibExt.cliqueFinGraph`, an abbreviation declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#clique-fin-graph).

## Adjacency in the complete graph

For every natural number $n$ and all vertices $x$ and $y$
of the complete graph $K_n$, whose vertices are the natural numbers less than $n$, $x$ and $y$ are
adjacent if and only if $x \ne y$.

Formalized by `MetaMathlibExt.cliqueFinGraph_adj`, a theorem declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#clique-fin-graph-adj).

## One-step graph minor

For finite graphs $H$ and $G$, $H$ arises from $G$ by one minor step
when one of the following holds. Isomorphism: $H$ is isomorphic to $G$. Vertex deletion: for some
vertex $a$ of $G$ there is an injective map $f$ from the vertices of $H$ to the vertices of $G$
whose image consists of all vertices other than $a$, such that vertices $u, v$ of $H$ are adjacent
exactly when $f(u), f(v)$ are adjacent in $G$. Edge deletion: for some edge $xy$ of $G$ there is a
bijection $e$ from the vertices of $H$ to the vertices of $G$ such that, for all vertices $u, v$ of
$H$, the vertices $e(u), e(v)$ are adjacent in $G$ whenever $u, v$ are adjacent in $H$, and if
$e(u), e(v)$ are adjacent in $G$, then either $u, v$ are adjacent in $H$ or the pair $(e(u), e(v))$
is $(x, y)$ or $(y, x)$; moreover, $e^{-1}(x), e^{-1}(y)$ are not adjacent in $H$. Edge
contraction: for some edge $ab$ of $G$ there is a surjective map $f$ from the vertices of $G$ to
the vertices of $H$ with $f(a) = f(b)$ such that, for all vertices $x, y$ of $G$, $f(x) = f(y)$
implies $x = y$ or $(x, y)$ is $(a, b)$ or $(b, a)$, and vertices $u, v$ of $H$ are adjacent
exactly when $u \ne v$ and there are adjacent vertices $u', v'$ of $G$ with $f(u') = u$ and
$f(v') = v$.

Stable source: https://en.wikipedia.org/wiki/Robertson%E2%80%93Seymour_theorem.

Formalized by `MetaMathlibExt.MinorStep`, an inductive type declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#minor-step).

## Graph minor relation

For finite graphs $H$ and $G$, $H$ is a minor of $G$ when there is a
finite sequence $H = G_0, G_1, \dots, G_k = G$ of finite graphs, with $k \ge 0$, such that for
each $i < k$, $G_i$ arises from $G_{i+1}$ by one minor step: an isomorphism, the deletion of one
vertex, the deletion of one edge, or the contraction of one edge.

Stable source: https://en.wikipedia.org/wiki/Robertson%E2%80%93Seymour_theorem.

Formalized by `MetaMathlibExt.IsMinor`, a definition declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#is-minor).

## Reflexivity of the graph minor relation

Every finite graph $G$ is a minor of itself.

Formalized by `MetaMathlibExt.IsMinor.refl`, a theorem declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#refl).

## Transitivity of the graph minor relation

For finite graphs $H$, $K$ and $G$, if $H$ is a
minor of $K$ and $K$ is a minor of $G$, then $H$ is a minor of $G$.

Formalized by `MetaMathlibExt.IsMinor.trans`, a theorem declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#trans).

## A single minor step gives a minor

For finite graphs $H$ and $G$, if $H$ arises from $G$ by
one minor step, then $H$ is a minor of $G$.

Formalized by `MetaMathlibExt.IsMinor.of_step`, a theorem declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#of-step).

## An isomorphic copy is a minor

For finite graphs $H$ and $G$, if $H$ is isomorphic to $G$,
then $H$ is a minor of $G$.

Formalized by `MetaMathlibExt.IsMinor.of_iso`, a theorem declared in [MathlibExt/Combinatorics/Graph/GraphMinor.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Graph/GraphMinor.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#of-iso).

## Robertson–Seymour theorem

Let $F$ be a family of finite simple graphs that is closed
under taking minors: whenever $G \in F$ and $H$ is a minor of $G$, also $H \in F$. Then any two
finite graphs that are minors of each other are isomorphic, and there is a finite set $O$ of
finite graphs such that a finite graph $G$ belongs to $F$ if and only if no graph in $O$ is a
minor of $G$.

Stable source: https://en.wikipedia.org/wiki/Robertson%E2%80%93Seymour_theorem.

Stated but not proved: `MetaMathlibExt.robertson_seymour` is written with `theorem_wanted` in [WantedExt/Combinatorics/Graph/RobertsonSeymourWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Graph/RobertsonSeymourWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html#robertson-seymour).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph minors](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/graph-minors)
