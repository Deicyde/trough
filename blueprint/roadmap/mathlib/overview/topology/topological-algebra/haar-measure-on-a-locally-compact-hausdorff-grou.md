# Haar measure on a locally compact Hausdorff group

The Haar measure on the locally compact group `G`, scaled so that `haarMeasure K₀ K₀ = 1`.

```lean
MeasureTheory.Measure.haarMeasure.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
  (K₀ : TopologicalSpace.PositiveCompacts G) : MeasureTheory.Measure G
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Closure](../general-topology/part-01/closure.md)
- [Compactness in terms of filters](../general-topology/part-01/compactness-in-terms-of-filters.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)
- [Topological group](topological-group.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Measure.haarMeasure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Haar/Basic.html#MeasureTheory.Measure.haarMeasure)
- [Source of `MeasureTheory.Measure.haarMeasure` in Mathlib/MeasureTheory/Measure/Haar/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Measure/Haar/Basic.lean#L516)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L258)
