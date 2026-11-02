---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun
mathlib_file: Mathlib/MeasureTheory/Measure/LevyConvergence.lean
---

# Lévy continuity theorem

The **Lévy convergence theorem**: the weak convergence of probability measures is equivalent
to the pointwise convergence of their characteristic functions.

```lean
MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ₀ : MeasureTheory.ProbabilityMeasure E}
  {μ : ℕ → MeasureTheory.ProbabilityMeasure E} :
  Filter.Tendsto μ Filter.atTop (nhds μ₀) ↔
    ∀ (t : E),
      Filter.Tendsto (fun n => MeasureTheory.charFun (↑(μ n)) t) Filter.atTop
        (nhds (MeasureTheory.charFun (↑μ₀) t))
```

## Depends on

- [Borel sigma-algebra](../../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Characteristic function](../../../../overview/probability-theory/definitions-in-probability-theory/characteristic-function.md)
- [Finite-dimensionality](../../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Lipschitz continuity](../../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Probability measure](../../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)

## Proof depends on

- [Dominated convergence theorem](../../../../overview/analysis/measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Group](../../../../overview/general-algebra/group-theory/part-01/group.md)
- [Lebesgue measure (Measures and integral calculus)](../../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Limits of sequences](../../../../undergraduate/topology/topology-and-metric-spaces/limits-of-sequences.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Prokhorov's theorem](../../../analysis/28-measure-and-integration/part-01/prokhorovs-theorem.md)
- [Squeeze theorem](../../../analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/LevyConvergence.html#MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun)
- [Source of `MeasureTheory.ProbabilityMeasure.tendsto_iff_tendsto_charFun` in Mathlib/MeasureTheory/Measure/LevyConvergence.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/LevyConvergence.lean#L212)
- [1000+ theorems list: Q1966978](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1958)
- [1000+ theorems project: Q1966978](https://1000-plus.github.io/?length=-1#Q1966978)
- [Wikipedia: Lévy continuity theorem](https://en.wikipedia.org/wiki/L%C3%A9vy_continuity_theorem)
- [Wikidata: Q1966978](https://www.wikidata.org/wiki/Q1966978)
