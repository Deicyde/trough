---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: IsRiemannianManifold
mathlib_file: Mathlib/Geometry/Manifold/Riemannian/Basic.lean
---

# Riemannian manifold

Consider a manifold in which the tangent spaces are already endowed with an inner product, and
the space is already endowed with an extended distance. We say that this is a Riemannian manifold
if the distance is given by the infimum of the lengths of `C^1` paths, measured using the norm in
the tangent spaces.

This is a `Prop`-valued typeclass, on top of existing data.

If you need to *construct* a distance using a Riemannian structure,
see `EMetricSpace.ofRiemannianMetric`.

```lean
IsRiemannianManifold.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {H : Type u_2} [TopologicalSpace H] (I : ModelWithCorners ℝ E H) (M : Type u_3)
  [TopologicalSpace M] [PseudoEMetricSpace M] [ChartedSpace H M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] : Prop
```

## Depends on

- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Integral of positive measurable functions](../../analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Norm](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/euclidean-and-hermitian-spaces/norm.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Riemannian/bundle metric](riemannian-bundle-metric.md)
- [Smooth map between manifolds](../differentiable-manifolds/part-01/smooth-map-between-manifolds.md)

## Sources

- [Mathlib documentation: `IsRiemannianManifold`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/Riemannian/Basic.html#IsRiemannianManifold)
- [Source of `IsRiemannianManifold` in Mathlib/Geometry/Manifold/Riemannian/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/Riemannian/Basic.lean#L71)
- [Mathlib overview: Geometry › Riemannian manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L478)
