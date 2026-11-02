---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Bundle.RiemannianMetric
mathlib_file: Mathlib/Topology/VectorBundle/Riemannian.lean
---

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
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Bundle.RiemannianMetric`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/VectorBundle/Riemannian.html#Bundle.RiemannianMetric)
- [Source of `Bundle.RiemannianMetric` in Mathlib/Topology/VectorBundle/Riemannian.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/VectorBundle/Riemannian.lean#L363)
- [Mathlib overview: Geometry › Riemannian manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L476)
