---
declaration: section
origin: cited
lean: DehnInvariant.DehnGroup, DehnInvariant.Edge, DehnInvariant.dehnInvariant, DehnInvariant.tetrahedralAngle, DehnInvariant.cubeEdges, DehnInvariant.tetrahedronEdges, DehnInvariant.dehnInvariant_nil, DehnInvariant.dehnInvariant_cons
statement: formalized
proof: formalized
---

# Dehn invariant

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html).

## Dehn group

The Dehn group is the tensor product
$\mathbb{R} \otimes_{\mathbb{Z}} (\mathbb{R} / 2\pi\mathbb{Z})$ of abelian groups; it is the target
of the Dehn invariant.

Formalized by `DehnInvariant.DehnGroup`, an abbreviation declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-group).

## Edge of a polyhedron

An edge, as recorded for the Dehn invariant, is a pair of real
numbers: its length and its dihedral angle in radians. No positivity or range condition is
imposed on either.

Formalized by `DehnInvariant.Edge`, a structure declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#edge).

## Dehn invariant

The Dehn invariant of a list of edges is the sum, over the edges, of
$\ell \otimes \theta$ in the Dehn group, where $\ell$ is the length of the edge and $\theta$ its
dihedral angle taken modulo $2\pi$.

Formalized by `DehnInvariant.dehnInvariant`, a definition declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-invariant).

## Dihedral angle of the regular tetrahedron

The real number $\arccos(1/3)$, the dihedral
angle of a regular tetrahedron in radians.

Formalized by `DehnInvariant.tetrahedralAngle`, a definition declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#tetrahedral-angle).

## Edge list of a cube

For a real number $\ell$, the edge list of a cube of side $\ell$
consists of $12$ edges, each of length $\ell$ with dihedral angle $\pi / 2$.

Formalized by `DehnInvariant.cubeEdges`, a definition declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#cube-edges).

## Edge list of the regular tetrahedron

For a real number $\ell$, the edge list of a
regular tetrahedron with edge length $\ell$ is the list of $6$ edges, each of length $\ell$ and
dihedral angle $\arccos(1/3)$.

Formalized by `DehnInvariant.tetrahedronEdges`, a definition declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#tetrahedron-edges).

## Dehn invariant of the empty edge list

The empty list of edges has Dehn invariant $0$.

Formalized by `DehnInvariant.dehnInvariant_nil`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-invariant-nil).

## The Dehn invariant splits off the first edge

Let $e$ be an edge of length $\ell$ and
dihedral angle $\theta$, and let $L$ be a list of edges. Then the Dehn invariant of the list
obtained by putting $e$ in front of $L$ equals $\ell \otimes \theta$ plus the Dehn invariant of
$L$, where $\theta$ is taken modulo $2\pi$.

Formalized by `DehnInvariant.dehnInvariant_cons`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-invariant-cons).

## Additivity of the Dehn invariant under concatenation

For lists of edges $L_1$ and $L_2$,
the Dehn invariant of the concatenation of $L_1$ and $L_2$ is the sum of the Dehn invariants of
$L_1$ and $L_2$.

Formalized by `DehnInvariant.dehnInvariant_append`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-invariant-append).

## Dehn invariant of a repeated edge

For a natural number $n$ and an edge of length $\ell$
and dihedral angle $\theta$, the Dehn invariant of the list consisting of $n$ copies of that edge
is $n \cdot (\ell \otimes \theta)$ in the Dehn group, where $\theta$ is taken modulo $2\pi$.

Formalized by `DehnInvariant.dehnInvariant_replicate`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-invariant-replicate).

## A $\mathbb{Q}$-linear functional separating $\alpha$ from $\pi$

Let $\alpha$ be a real
number such that $\alpha / \pi$ is irrational. Then there is a $\mathbb{Q}$-linear map
$f : \mathbb{R} \to \mathbb{R}$ with $f(\pi) = 0$ and $f(\alpha) \neq 0$.

The idea of the proof: $\alpha$ lies outside the $\mathbb{Q}$-span of $\pi$, and a linear
functional on the quotient separates it.

Formalized by `DehnInvariant.exists_linearMap_of_irrational`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#exists-linear-map-of-irrational).

## Nonvanishing of an edge term in the Dehn group

Let $\ell$ and $\alpha$ be real numbers
with $\ell \neq 0$ and $\alpha / \pi$ irrational. Then the pure tensor $\ell \otimes [\alpha]$ is
nonzero in the Dehn group $\mathbb{R} \otimes_{\mathbb{Z}} (\mathbb{R} / 2\pi\mathbb{Z})$, where
$[\alpha]$ is the class of $\alpha$ modulo $2\pi$.

The proof applies a $\mathbb{Q}$-linear functional that vanishes at $\pi$ but not at $\alpha$.

Formalized by `DehnInvariant.tmul_ne_zero_of_irrational`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#tmul-ne-zero-of-irrational).

## The Dehn invariant of the cube is zero

For every real number $\ell$, the edge list of a
cube of side $\ell$ (twelve edges of length $\ell$, each with dihedral angle $\pi / 2$) has Dehn
invariant $0$.

The reason is that $12 \cdot (\pi / 2) = 3 \cdot 2\pi$ vanishes in $\mathbb{R} / 2\pi\mathbb{Z}$.

Formalized by `DehnInvariant.dehnInvariant_cubeEdges`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-invariant-cube-edges).

## Nonzero Dehn invariant of the regular tetrahedron, conditional on irrationality

Suppose
that $\arccos(1/3) / \pi$ is irrational. Then for every nonzero real number $\ell$, the edge list
of a regular tetrahedron of side $\ell$ (six edges of length $\ell$, each with dihedral angle
$\arccos(1/3)$) has nonzero Dehn invariant.

Formalized by `DehnInvariant.dehnInvariant_tetrahedronEdges_ne_zero`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-invariant-tetrahedron-edges-ne-zero).

## Conditionally, the cube and the regular tetrahedron have different Dehn invariants

Suppose that $\arccos(1/3) / \pi$ is irrational. Then for all real numbers $\ell$ and $\ell'$ with
$\ell' \ne 0$, the edge list of a cube of side $\ell$ and the edge list of a regular tetrahedron
of side $\ell'$ have different Dehn invariants.

Since scissors-congruent polyhedra have equal Dehn invariants, under this hypothesis a cube and a
regular tetrahedron of equal volume are not scissors-congruent.

Formalized by `DehnInvariant.dehnInvariant_cube_ne_dehnInvariant_tetrahedron`, a theorem declared in [MathlibExt/Geometry/Dissections/DehnInvariant.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Dissections/DehnInvariant.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html#dehn-invariant-cube-ne-dehn-invariant-te).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dehn invariant](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/dehn-invariant)
