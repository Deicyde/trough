# Fubini's theorem

**Fubini's Theorem**: For integrable functions on `α × β`,
the Bochner integral of `f` is equal to the iterated Bochner integral.
`integrable_prod_iff` can be useful to show that the function in question in integrable.
`MeasureTheory.Integrable.integral_prod_right` is useful to show that the inner integral
of the right-hand side is integrable.

```lean
MeasureTheory.integral_prod.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2} {E : Type u_3}
  [MeasurableSpace α] [MeasurableSpace β] {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} [NormedAddCommGroup E] [MeasureTheory.SFinite ν] [NormedSpace ℝ E]
  [MeasureTheory.SFinite μ] (f : α × β → E) (hf : MeasureTheory.Integrable f (μ.prod ν)) :
  ∫ (z : α × β), f z ∂μ.prod ν = ∫ (x : α), ∫ (y : β), f (x, y) ∂ν ∂μ
```

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bochner integral](../part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Giry monad](../part-01/giry-monad.md)
- [Measurable function](../part-01/measurable-function.md)

## Proof depends on

- [Approximation by step functions](../../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Hausdorff space](../../../topology/general-topology/part-01/hausdorff-space.md)
- [Inner product space, over $R$ or $C$](../../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Squeeze theorem](../../../../thousand-plus/analysis/26-real-functions/part-02/squeeze-theorem.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `MeasureTheory.integral_prod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Prod.html#MeasureTheory.integral_prod)
- [Source of `MeasureTheory.integral_prod` in Mathlib/MeasureTheory/Integral/Prod.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Integral/Prod.lean#L438)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L357)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L524)
- [1000+ theorems list: Q1149022](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1443)
- [1000+ theorems project: Q1149022](https://1000-plus.github.io/all.html?length=-1#Q1149022)
- [Wikipedia: Fubini's theorem](https://en.wikipedia.org/wiki/Fubini's_theorem)
- [Wikidata: Q1149022](https://www.wikidata.org/wiki/Q1149022)
