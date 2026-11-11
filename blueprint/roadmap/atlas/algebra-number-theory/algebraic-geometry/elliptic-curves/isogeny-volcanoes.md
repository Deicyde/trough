---
declaration: section
origin: cited
lean: Multigraph, Multigraph.Adj, Multigraph.degree, Multigraph.degreeOn, Multigraph.Connected, Multigraph.IsConnected, Multigraph.adj_comm, Multigraph.connected_refl
statement: formalized
proof: formalized
---

# Isogeny volcanoes

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html).

## Multigraph

A multigraph on a vertex set $V$ is given by an edge multiplicity function $m$
that assigns to every two vertices $v, w \in V$ a natural number $m(v, w)$ and is symmetric:
$m(v, w) = m(w, v)$ for all $v, w \in V$. Loops are permitted: $m(v, v)$ may be positive.

Formalized by `Multigraph`, a structure declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#multigraph).

## Adjacency in a multigraph

Two vertices $v$ and $w$ of a multigraph $G$ are adjacent when
the edge multiplicity between $v$ and $w$ is positive.

Formalized by `Multigraph.Adj`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#adj).

## Degree of a vertex in a multigraph

For a multigraph $G$ on a finite vertex set $V$ with edge
multiplicity $m$, the degree of a vertex $v$ is $\sum_{w \in V} m(v, w)$. A loop at $v$
contributes its multiplicity once, matching the outgoing-isogeny convention.

Formalized by `Multigraph.degree`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#degree).

## Degree restricted to a predicate

Let $G$ be a multigraph on a finite vertex set $V$ with
edge multiplicity $m$, let $v \in V$ and let $P$ be a decidable predicate on $V$. The degree of
$v$ restricted to $P$ is $\sum_{w \in V,\, P(w)} m(v, w)$.

Formalized by `Multigraph.degreeOn`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#degree-on).

## Connectivity of vertices in a multigraph

Two vertices $v$ and $w$ of a multigraph $G$ are
connected when they are related by the reflexive-transitive closure of adjacency, that is, when
there is a finite sequence of vertices $v = u_0, u_1, \dots, u_k = w$ with $k \ge 0$ and $u_i$
adjacent to $u_{i+1}$ for each $i < k$.

Formalized by `Multigraph.Connected`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#connected).

## Connected multigraph

A multigraph $G$ is connected when every two vertices $v$ and $w$
of $G$ are joined by a walk, that is, $w$ is reachable from $v$ by a finite (possibly empty)
sequence of steps along edges of positive multiplicity.

Formalized by `Multigraph.IsConnected`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-connected).

## Symmetry of adjacency in a multigraph

In a multigraph $G$, a vertex $v$ is adjacent to a
vertex $w$ if and only if $w$ is adjacent to $v$.

Formalized by `Multigraph.adj_comm`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#adj-comm).

## Every vertex is connected to itself

In a multigraph $G$, every vertex $v$ is connected to
$v$.

Formalized by `Multigraph.connected_refl`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#connected-refl).

## Degree splits over a predicate and its complement

Let $G$ be a multigraph on a finite
vertex set $V$, let $v \in V$ and let $P$ be a decidable predicate on $V$. Then the degree of $v$
equals the degree of $v$ restricted to $P$ plus the degree of $v$ restricted to $\neg P$.

Formalized by `Multigraph.degreeOn_compl`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#degree-on-compl).

## Restricted degree depends only on the neighbours

Let $G$ be a multigraph on a finite
vertex set $V$, let $v \in V$ and let $P$ and $Q$ be decidable predicates on $V$. If
$P(w) \iff Q(w)$ for every vertex $w$ whose edge multiplicity with $v$ is positive, then the
degree of $v$ restricted to $P$ equals the degree of $v$ restricted to $Q$.

Formalized by `Multigraph.degreeOn_congr`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#degree-on-congr).

## Isogeny volcano

Let $\ell$ be a prime. An $\ell$-isogeny volcano consists of a finite
vertex set $V$, a multigraph on $V$ with edge multiplicities $m(v, w)$, a depth $d \in \mathbb{N}$,
a surjective level map $\mathrm{lev} : V \to \{0, 1, \dots, d\}$ and a surface degree
$s \in \mathbb{N}$ with $s \le 2$, subject to the following conditions, where the surface is the
set of vertices of level $0$. Every surface vertex $v$ satisfies
$\sum_{w \in V,\ \mathrm{lev}(w) = 0} m(v, w) = s$. Every vertex $v$ of positive level has a
unique parent: $\sum_{w \in V,\ \mathrm{lev}(w) + 1 = \mathrm{lev}(v)} m(v, w) = 1$. Whenever
$m(v, w) > 0$, either $v$ and $w$ both lie on the surface or their levels differ by exactly one.
Every vertex $v$ with $\mathrm{lev}(v) < d$ has degree $\sum_{w \in V} m(v, w) = \ell + 1$, where a
loop at $v$ contributes its multiplicity once. Finally, the multigraph is connected: any two
vertices are joined by a path along which consecutive vertices have positive edge multiplicity.

Formalized by `IsogenyVolcano`, a structure declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#isogeny-volcano).

## Surface of a volcano

A vertex $v$ of an $\ell$-isogeny volcano $C$ lies on the surface
of $C$ when its level is $0$.

Formalized by `IsogenyVolcano.isSurface`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-surface).

## Floor of a volcano

A vertex $v$ of an $\ell$-isogeny volcano $C$ of depth $d$ lies on
the floor of $C$ when its level is $d$, the last of the levels $0, 1, \dots, d$.

Formalized by `IsogenyVolcano.isFloor`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-floor).

## Depth of an isogeny volcano

The depth of an $\ell$-isogeny volcano $C$ is the natural
number $d$ recorded in $C$: the levels of the vertices of $C$ are exactly $0, 1, \dots, d$, with
level $0$ the surface and level $d$ the floor.

Formalized by `IsogenyVolcano.volcanoDepth`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#volcano-depth).

## Horizontal edge

In an $\ell$-isogeny volcano $C$, the pair $(v, w)$ of vertices is a
horizontal edge when the edge multiplicity between $v$ and $w$ is positive and both $v$ and $w$
lie on the surface, that is, both have level $0$.

Formalized by `IsogenyVolcano.IsHorizontalEdge`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-horizontal-edge).

## Descending edge

In an $\ell$-isogeny volcano $C$, the pair $(v, w)$ of vertices is a
descending edge when the edge multiplicity between $v$ and $w$ is positive and $w$ lies one level
below $v$, that is, the level of $v$ plus one equals the level of $w$ (level $0$ being the
surface).

Formalized by `IsogenyVolcano.IsDescendingEdge`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-descending-edge).

## Ascending edge

In an $\ell$-isogeny volcano $C$, the pair $(v, w)$ of vertices is an
ascending edge when the edge multiplicity between $v$ and $w$ is positive and $w$ lies one level
above $v$, that is, the level of $w$ plus one equals the level of $v$ (level $0$ being the
surface).

Formalized by `IsogenyVolcano.IsAscendingEdge`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-ascending-edge).

## Vertical edge

In an $\ell$-isogeny volcano $C$, the pair $(v, w)$ of vertices is a
vertical edge when it is a descending edge or an ascending edge, that is, when the edge
multiplicity between $v$ and $w$ is positive and the levels of $v$ and $w$ differ by exactly
one.

Formalized by `IsogenyVolcano.IsVerticalEdge`, a definition declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-vertical-edge).

## Reversing a descending edge gives an ascending edge

In an $\ell$-isogeny volcano, for
vertices $v$ and $w$, $(v, w)$ is a descending edge if and only if $(w, v)$ is an ascending
edge.

Formalized by `IsogenyVolcano.descending_iff_ascending_symm`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#descending-iff-ascending-symm).

## Reversing an ascending edge gives a descending edge

In an $\ell$-isogeny volcano, for
vertices $v$ and $w$, $(v, w)$ is an ascending edge if and only if $(w, v)$ is a descending
edge.

Formalized by `IsogenyVolcano.ascending_iff_descending_symm`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#ascending-iff-descending-symm).

## Every edge of an isogeny volcano is horizontal, descending or ascending

Let $C$ be an $\ell$-isogeny volcano, with levels numbered from $0$ at the surface, and let $v, w$
be vertices of $C$ whose edge multiplicity is positive. Then $(v, w)$ is a horizontal edge (both
$v$ and $w$ have level $0$), a descending edge (the level of $w$ is the level of $v$ plus one) or
an ascending edge (the level of $v$ is the level of $w$ plus one).

Formalized by `IsogenyVolcano.edge_direction`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#edge-direction).

## Surface vertices are those of level zero

A vertex $v$ of an $\ell$-isogeny volcano $C$
lies on the surface of $C$ if and only if the level of $v$, as a natural number, is $0$.

Formalized by `IsogenyVolcano.isSurface_iff`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-surface-iff).

## Floor vertices are those whose level equals the depth

A vertex $v$ of an
$\ell$-isogeny volcano $C$ lies on the floor of $C$ if and only if the level of $v$, as a natural
number, equals the depth of $C$.

Formalized by `IsogenyVolcano.isFloor_iff`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#is-floor-iff).

## Surface regularity of an isogeny volcano

Let $C$ be an $\ell$-isogeny volcano with edge
multiplicities $m$ and surface degree $s$. For every surface vertex $v$ of $C$, that is, every
vertex of level $0$, the sum of $m(v, w)$ over all surface vertices $w$ of $C$ equals $s$.

This restates the surface-regularity condition of an isogeny volcano in terms of the surface
predicate.

Formalized by `IsogenyVolcano.surface_degreeOn`, a theorem declared in [MathlibExt/Combinatorics/IsogenyVolcano.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/IsogenyVolcano.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html#surface-degree-on).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Isogeny volcanoes](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/elliptic-curves/isogeny-volcanoes)
