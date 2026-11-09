# Conditional expectation

Conditional expectation of a function, with notation `μ[f | m]`.

It is defined as 0 if any one of the following conditions is true:
- `m` is not a sub-σ-algebra of `m₀`,
- `μ` is not σ-finite with respect to `m`,
- `f` is not integrable.

```lean
MeasureTheory.condExp.{u_1, u_3} {α : Type u_1} {E : Type u_3} (m : MeasurableSpace α)
  {m₀ : MeasurableSpace α} [NormedAddCommGroup E] [NormedSpace ℝ E] (μ : MeasureTheory.Measure α)
  (f : α → E) : α → E
```

## Depends on

- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Extension by continuity](../../topology/general-topology/part-01/extension-by-continuity.md)
- [Inner product space $L^2$](../../../undergraduate/topology/hilbert-spaces/inner-product-space-l-2-2.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Orthogonal projection](../../analysis/hilbert-spaces/orthogonal-projection.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Vector-valued integrable function (Bochner integral)](../../analysis/measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)

## Sources

- [Mathlib documentation: `MeasureTheory.condExp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/ConditionalExpectation/Basic.html#MeasureTheory.condExp)
- [Source of `MeasureTheory.condExp` in Mathlib/MeasureTheory/Function/ConditionalExpectation/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Function/ConditionalExpectation/Basic.lean#L94)
- [Mathlib overview: Probability Theory › Definitions in probability theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L396)
