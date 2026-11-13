---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Manifold.RiemannianMetricExistenceWanted.riemannianMetricExistence, Manifold.AdmitsPositiveScalarCurvatureMetric
statement: formalized
proof: formalized
---

# Riemannian and Finsler geometry: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/index.html).

Manifolds with smoothly varying inner products or norms on tangent spaces: connections, curvature, geodesics, differential operators and rigidity theorems.

## Existence of Riemannian metrics

Let $E$ be a finite-dimensional real normed space and let
$M$ be a Hausdorff, second-countable $C^\infty$ manifold modeled on $E$ (possibly with boundary
or corners). Then $M$ admits a $C^\infty$ Riemannian metric on its tangent bundle.

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed. existence of Riemannian metrics via partition of unity; also Lee, Riemannian Manifolds; Lean states finite-dimensional Hausdorff second-countable specialization.

Formalized by `MathlibExt.Geometry.Manifold.RiemannianMetricExistenceWanted.riemannianMetricExistence`, a theorem declared in [MathlibExt/Geometry/Manifold/RiemannianMetricExistence.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/RiemannianMetricExistence.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/index.html#riemannian-metric-existence).

## Manifolds admitting a metric of positive scalar curvature

A smooth manifold $M$ without
boundary modeled on $\mathbb{R}^n$ admits a metric of positive scalar curvature when some
$C^\infty$ Riemannian metric $g$ on its tangent bundle has scalar curvature, computed for $g$,
strictly positive at every point of $M$.

Formalized by `Manifold.AdmitsPositiveScalarCurvatureMetric`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/PositiveScalarCurvature.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/PositiveScalarCurvature.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/index.html#admits-positive-scalar-curvature-metric).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemannian and Finsler geometry](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/riemannian-geometry)
