---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: IsMIntegralCurve
mathlib_file: Mathlib/Geometry/Manifold/IntegralCurve/Basic.lean
---

# Integral curves

If `v : M → TM` is a vector field on `M`, `IsMIntegralCurve γ v` means `γ : ℝ → M` is a global
integral curve of `v`. That is, `γ t` is tangent to `v (γ t)` for all `t : ℝ`.

```lean
IsMIntegralCurve.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] (γ : ℝ → M) (v : (x : M) → TangentSpace I x) : Prop
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Continuous linear map](../../../topology/topological-algebra/continuous-linear-map.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Field $\R$ of real numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../../general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `IsMIntegralCurve`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IntegralCurve/Basic.html#IsMIntegralCurve)
- [Source of `IsMIntegralCurve` in Mathlib/Geometry/Manifold/IntegralCurve/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IntegralCurve/Basic.lean#L74)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L453)
