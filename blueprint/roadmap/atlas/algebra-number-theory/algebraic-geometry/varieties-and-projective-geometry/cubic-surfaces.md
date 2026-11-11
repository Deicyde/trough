---
declaration: section
origin: cited
lean: AlgebraicGeometry.CubicSurface, AlgebraicGeometry.CubicSurface.totalDegree_defining, AlgebraicGeometry.CubicSurface.isHomogeneous_pderiv, AlgebraicGeometry.CubicSurface.IsSingularPoint, AlgebraicGeometry.CubicSurface.IsSmooth, AlgebraicGeometry.CubicSurface.aeval_defining_eq_zero_of_pderiv, AlgebraicGeometry.CubicSurface.isSingularPoint_iff, AlgebraicGeometry.fermatCubicSurface
statement: formalized
proof: formalized
---

# Cubic surfaces

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html).

## Algebraic Geometry

## Cubic surface

A cubic surface over a field $k$ is a nonzero homogeneous polynomial
$f \in k[x_0, x_1, x_2, x_3]$ of degree $3$ in the four homogeneous coordinates of
$\mathbb{P}^3$, its defining equation. The surface it describes is the projective zero locus
$V(f) \subseteq \mathbb{P}^3$.

Formalized by `AlgebraicGeometry.CubicSurface`, a structure declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#cubic-surface).

## The defining cubic has total degree three

The defining cubic form of a cubic surface
over a field $k$ has total degree exactly $3$.

Formalized by `AlgebraicGeometry.CubicSurface.totalDegree_defining`, a lemma declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#total-degree-defining).

## The partial derivatives of a cubic form are quadratic

Let $S$ be a cubic surface over a
field $k$ with defining cubic form $f \in k[x_0, x_1, x_2, x_3]$. For each $i \in \{0, 1, 2, 3\}$,
the partial derivative $\partial f / \partial x_i$ is homogeneous of degree $2$.

Formalized by `AlgebraicGeometry.CubicSurface.isHomogeneous_pderiv`, a lemma declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#is-homogeneous-pderiv).

## Singular point of a cubic surface

Let $S$ be a cubic surface over a field $k$ with
defining cubic form $f \in k[x_0, x_1, x_2, x_3]$. A point $x \in k^4$ is a singular point of the
affine cone over $S$ when $f(x) = 0$ and $\partial f / \partial x_i$ vanishes at $x$ for every
$i \in \{0, 1, 2, 3\}$.

Over an algebraically closed field, $S$ is a smooth projective surface exactly when the origin is
its only such point.

Formalized by `AlgebraicGeometry.CubicSurface.IsSingularPoint`, a definition declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#is-singular-point).

## Smooth cubic surface

Let $k$ be an algebraically closed field and $S$ a cubic surface
over $k$ with defining cubic form $f \in k[x_0, x_1, x_2, x_3]$. The surface $S$ is smooth when
every point $x \in k^4$ at which $f$ and all its partial derivatives $\partial f / \partial x_i$
vanish is the origin, that is, when the origin is the only singular point of the affine cone
over $S$.

This is the Jacobian criterion for smoothness of the projective surface
$V(f) \subseteq \mathbb{P}^3$ cut out by $f$.

Formalized by `AlgebraicGeometry.CubicSurface.IsSmooth`, a definition declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#is-smooth).

## Vanishing partial derivatives force the cubic to vanish when $3 \neq 0$

Let $S$ be a
cubic surface over a field $k$ in which $3 \neq 0$, and let $f \in k[x_0, x_1, x_2, x_3]$ be its
defining cubic form. If $x \in k^4$ is a point at which every partial derivative
$\partial f / \partial x_i$ vanishes, then $f(x) = 0$.

This follows from Euler's identity $\sum_i x_i \, \partial f / \partial x_i = 3 f$.

Formalized by `AlgebraicGeometry.CubicSurface.aeval_defining_eq_zero_of_pderiv`, a lemma declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#aeval-defining-eq-zero-of-pderiv).

## Singular points via partial derivatives

Let $S$ be a cubic surface over a field $k$ in
which $3 \neq 0$, and let $f \in k[x_0, x_1, x_2, x_3]$ be its defining cubic form. A point
$x \in k^4$ is a singular point of the affine cone over $S$ if and only if every partial
derivative $\partial f / \partial x_i$ vanishes at $x$.

The condition $f(x) = 0$ in the definition of a singular point is then automatic, by Euler's
identity.

Formalized by `AlgebraicGeometry.CubicSurface.isSingularPoint_iff`, a lemma declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#is-singular-point-iff).

## Fermat cubic surface

Over a field $k$, the Fermat cubic surface is the cubic surface in
$\mathbb{P}^3$ with defining cubic form $x_0^3 + x_1^3 + x_2^3 + x_3^3$.

It is smooth when the characteristic of $k$ is not $3$.

Formalized by `AlgebraicGeometry.fermatCubicSurface`, a definition declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#fermat-cubic-surface).

## Triple plane

Over a field $k$, the triple plane is the cubic surface in $\mathbb{P}^3$
with defining cubic form $x_0^3 \in k[x_0, x_1, x_2, x_3]$, that is, the plane $x_0 = 0$
counted three times.

It is non-reduced, and every point of the plane $x_0 = 0$ is a singular point.

Formalized by `AlgebraicGeometry.triplePlane`, a definition declared in [MathlibExt/AlgebraicGeometry/CubicSurface.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/CubicSurface.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html#triple-plane).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cubic surfaces](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/cubic-surfaces)
