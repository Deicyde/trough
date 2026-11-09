# Riemannian/bundle metric

A family of inner product space structures on the fibers of a fiber bundle, defining the same
topology as the already existing one. This family is not assumed to be continuous or smooth: to
guarantee continuity, resp. smoothness, of the inner product as a function of the base point,
use `ContinuousRiemannianMetric` or `ContMDiffRiemannianMetric`.

This structure is used through `RiemannianBundle` for typeclass inference, to register the inner
product space structure on the fibers without creating diamonds.

```lean
Bundle.RiemannianMetric.{u_4, u_6} {B : Type u_4} (E : B → Type u_6)
  [(b : B) → TopologicalSpace (E b)] [(b : B) → AddCommGroup (E b)]
  [(b : B) → _root_.Module ℝ (E b)] : Type (max u_4 u_6)
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Bundle.RiemannianMetric`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/VectorBundle/Riemannian.html#Bundle.RiemannianMetric)
- [Source of `Bundle.RiemannianMetric` in Mathlib/Topology/VectorBundle/Riemannian.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/VectorBundle/Riemannian.lean#L363)
- [Mathlib overview: Geometry › Riemannian manifolds](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L476)
