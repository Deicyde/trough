---
declaration: section
origin: cited
lean: MathlibExt.Geometry.SphereTheoremWanted.Geometry.SphereTheorem.curv, MathlibExt.Geometry.SphereTheoremWanted.Geometry.SphereTheorem.QuarterPinched, MathlibExt.Geometry.SphereTheoremWanted.Geometry.SphereTheorem.sphere_theorem, MathlibExt.Geometry.SphereTheoremWanted.Geometry.SphereTheorem.differentiable_sphere_theorem
statement: formalized
---

# Sphere theorem

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/sphere-theorem/index.html).

## Riemann curvature of a covariant derivative

Let $\nabla$ be a covariant derivative on the
tangent bundle of a smooth manifold $M$. For vector fields $X, Y, Z$ on $M$, the curvature of
$\nabla$ is the vector field
$R(X,Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]} Z$, where $[X,Y]$ is the Lie
bracket of $X$ and $Y$.

Formalized by `MathlibExt.Geometry.SphereTheoremWanted.Geometry.SphereTheorem.curv`, a definition declared in [WantedExt/Geometry/SphereTheoremWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SphereTheoremWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/sphere-theorem/index.html#curv).

## Strictly quarter-pinched curvature

Let $\nabla$ be a covariant derivative on the tangent
bundle of a Riemannian manifold $M$, with curvature $R$. Then $\nabla$ is strictly quarter-pinched
when, for all smooth vector fields $X, Y$ on $M$ and every point $x \in M$ at which $X(x)$ and
$Y(x)$ are orthonormal, the sectional curvature $K = \langle R(X,Y)Y(x), X(x) \rangle$ satisfies
$1 < K \le 4$. The interval $(1, 4]$ is Knill's normalization of strict quarter pinching.

Formalized by `MathlibExt.Geometry.SphereTheoremWanted.Geometry.SphereTheorem.QuarterPinched`, a definition declared in [WantedExt/Geometry/SphereTheoremWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SphereTheoremWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/sphere-theorem/index.html#quarter-pinched).

## Topological sphere theorem

Let $M$ be a compact, Hausdorff, simply connected smooth
manifold without boundary, of dimension $d \ge 2$, with a smooth Riemannian metric. Suppose $M$
carries a smooth covariant derivative $\nabla$ on its tangent bundle that is torsion-free,
compatible with the metric and strictly quarter-pinched (every sectional curvature at an
orthonormal pair lies in $(1, 4]$). Then $M$ is homeomorphic to the unit sphere
$S^d \subset \mathbb{R}^{d+1}$.

## Sources

- M. Berger; W. Klingenberg; H. E. Rauch (topological sphere theorem, 1951–1961). Knill, *Some fundamental theorems in mathematics*, §121. Problem `sphere_theorem_topological` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.SphereTheoremWanted.Geometry.SphereTheorem.sphere_theorem` is written with `theorem_wanted` in [WantedExt/Geometry/SphereTheoremWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SphereTheoremWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/sphere-theorem/index.html#sphere-theorem).

## Differentiable sphere theorem

Let $M$ be a compact, Hausdorff, simply connected smooth
manifold without boundary, of dimension $d \ge 2$, with a smooth Riemannian metric. Suppose $M$
carries a smooth covariant derivative $\nabla$ on its tangent bundle that is torsion-free,
compatible with the metric and strictly quarter-pinched (every sectional curvature at an
orthonormal pair lies in $(1, 4]$). Then $M$ is diffeomorphic to the unit sphere
$S^d \subset \mathbb{R}^{d+1}$ with its standard smooth structure.

## Sources

- S. Brendle & R. Schoen, *Manifolds with 1/4-pinched curvature are space forms*, J. AMS 22 (2009). Knill, *Some fundamental theorems in mathematics*, §121. Problem `sphere_theorem_differentiable` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.SphereTheoremWanted.Geometry.SphereTheorem.differentiable_sphere_theorem` is written with `theorem_wanted` in [WantedExt/Geometry/SphereTheoremWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SphereTheoremWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/sphere-theorem/index.html#differentiable-sphere-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sphere theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/sphere-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/sphere-theorem)
