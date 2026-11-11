---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.HoneycombVertex, MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.step, MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.step_step, MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.step_injective, MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.origin, MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.endpoint, MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.vertexAt, MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.visitedVertices
statement: formalized
---

# Self-avoiding walks on the honeycomb lattice

13 results, 12 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html).

## Vertices of the honeycomb lattice

A vertex of the honeycomb lattice is a triple
$(x, y, s)$ with $x, y \in \mathbb{Z}$ and $s$ a boolean recording which of the two classes of
the bipartition the vertex belongs to.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.HoneycombVertex`, a structure declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#honeycomb-vertex).

## Steps in the honeycomb lattice

For a vertex $v = (x, y, s)$ and a direction label
$d \in \{0, 1, 2\}$, the step from $v$ in direction $d$ is a vertex on the other side of the
bipartition. If $s$ is true, it is $(x, y, \mathrm{false})$, $(x + 1, y, \mathrm{false})$ or
$(x, y + 1, \mathrm{false})$ for $d = 0, 1, 2$ respectively. If $s$ is false, it is
$(x, y, \mathrm{true})$, $(x - 1, y, \mathrm{true})$ or $(x, y - 1, \mathrm{true})$ for
$d = 0, 1, 2$ respectively.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.step`, a definition declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#step).

## Steps are involutions

For every vertex $v$ of the honeycomb lattice and every
direction label $d \in \{0, 1, 2\}$, taking the step in direction $d$ from $v$ and then the
step in direction $d$ again returns to $v$.

In particular, the coordinate model defines an undirected graph.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.step_step`, a theorem declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#step-step).

## Distinct labels give distinct neighbors

For every vertex $v$ of the honeycomb
lattice, the steps from $v$ in the directions $0$, $1$ and $2$ are three distinct vertices.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.step_injective`, a theorem declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#step-injective).

## Origin of the honeycomb lattice

The origin is the vertex $(0, 0, \mathrm{false})$.

The honeycomb lattice is vertex-transitive, so the choice of base vertex is arbitrary.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.origin`, a definition declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#origin).

## Endpoint of a direction word

For a finite word $d_1 d_2 \cdots d_k$ of direction labels
in $\{0, 1, 2\}$, its endpoint is the vertex reached from the origin by taking the step in
direction $d_1$, then the step in direction $d_2$, and so on through $d_k$. The endpoint of the
empty word is the origin.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.endpoint`, a definition declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#endpoint).

## Vertices along a direction word

For a word $(d_1, \ldots, d_n)$ of direction labels in
$\{0, 1, 2\}$ and an integer $0 \le i \le n$, the $i$-th vertex of the word is the endpoint of
its prefix $(d_1, \ldots, d_i)$, the vertex reached from the origin after the first $i$ steps.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.vertexAt`, a definition declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#vertex-at).

## Vertices visited by a direction word

For a word $(d_1, \ldots, d_n)$ of direction
labels in $\{0, 1, 2\}$, the set of visited vertices is the finite set of its $i$-th vertices for
$0 \le i \le n$; it contains the origin (for $i = 0$) and the endpoint of the word.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.visitedVertices`, a definition declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#visited-vertices).

## Self-avoiding direction words

A word $(d_1, \ldots, d_n)$ of direction labels in
$\{0, 1, 2\}$ is self-avoiding when its set of visited vertices has exactly $n + 1$ elements,
that is, when its $n + 1$ vertices, the $i$-th vertices for $0 \le i \le n$, are pairwise
distinct.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.IsSelfAvoiding`, a definition declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#is-self-avoiding).

## Number of self-avoiding walks on the honeycomb lattice

For a natural number $n$, this
is the number of self-avoiding walks with $n$ steps on the honeycomb lattice starting at the
origin.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.walkCount`, a definition declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#walk-count).

## Three-step self-avoiding walks on the honeycomb lattice

There are exactly $12$
self-avoiding walks with $3$ steps on the honeycomb lattice starting at a fixed vertex.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.walkCount_three`, a theorem declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#walk-count-three).

## Six-step self-avoiding walks on the honeycomb lattice

There are exactly $90$
self-avoiding walks with $6$ steps on the honeycomb lattice starting at a fixed vertex.

Six is the first length at which a walk can close a hexagon.

Formalized by `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.walkCount_six`, a theorem declared in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#walk-count-six).

## The connective constant of the honeycomb lattice

Let $c_n$ be the number of $n$-step
self-avoiding walks on the honeycomb lattice starting at the origin. Then
$c_n^{1/n} \to \sqrt{2 + \sqrt{2}}$ as $n \to \infty$.

## Sources

- H. Duminil-Copin and S. Smirnov, 'The connective constant of the honeycomb lattice equals sqrt(2 + sqrt 2)', Ann. of Math. 175 (2012), 1653-1665, https://doi.org/10.4007/annals.2012.175.3.14. Problem `honeycomb_connective_constant` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.HoneycombConnectiveConstantWanted.Combinatorics.HoneycombConnectiveConstant.honeycomb_connective_constant` is written with `theorem_wanted` in [WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HoneycombConnectiveConstantWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html#honeycomb-connective-constant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Self-avoiding walks on the honeycomb lattice](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements/self-avoiding-walks-on-the-honeycomb-lattice)
