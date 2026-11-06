# Smooth bundle metric

A family of inner product space structures on the fibers of a fiber bundle, defining the same
topology as the already existing one, and varying continuously with the base point. See also
`ContinuousRiemannianMetric` for a continuous version.

This structure is used through `RiemannianBundle` for typeclass inference, to register the inner
product space structure on the fibers without creating diamonds.

```lean
Bundle.ContMDiffRiemannianMetric.{u_1, u_2, u_3, u_4, u_5} {EB : Type u_1} [NormedAddCommGroup EB]
  [NormedSpace ℝ EB] {HB : Type u_2} [TopologicalSpace HB] (IB : ModelWithCorners ℝ EB HB)
  (n : WithTop ℕ∞) {B : Type u_3} [TopologicalSpace B] [ChartedSpace HB B] (F : Type u_4)
  [NormedAddCommGroup F] [NormedSpace ℝ F] (E : B → Type u_5)
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → TopologicalSpace (E b)]
  [(b : B) → AddCommGroup (E b)] [(b : B) → _root_.Module ℝ (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] : Type (max u_3 u_5)
```

## Depends on

- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Smooth map between manifolds](../differentiable-manifolds/part-01/smooth-map-between-manifolds.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topological vector bundle](../../topology/general-topology/part-01/topological-vector-bundle.md)

## Sources

- [Mathlib documentation: `Bundle.ContMDiffRiemannianMetric`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Riemannian.html#Bundle.ContMDiffRiemannianMetric)
- [Source of `Bundle.ContMDiffRiemannianMetric` in Mathlib/Geometry/Manifold/VectorBundle/Riemannian.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorBundle/Riemannian.lean#L239)
- [Mathlib overview: Geometry › Riemannian manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L477)
