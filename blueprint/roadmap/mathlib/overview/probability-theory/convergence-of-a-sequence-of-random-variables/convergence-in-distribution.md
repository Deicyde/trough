# Convergence in distribution

The characterization of weak convergence of probability measures by the usual (defining)
condition that the integrals of every continuous bounded function converge to the integral of the
function against the limit measure.

```lean
MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.{u_1, u_2} {Ω : Type u_1}
  [MeasurableSpace Ω] [TopologicalSpace Ω] [OpensMeasurableSpace Ω] {γ : Type u_2} {F : Filter γ}
  {μs : γ → MeasureTheory.ProbabilityMeasure Ω} {μ : MeasureTheory.ProbabilityMeasure Ω} :
  Filter.Tendsto μs F (nhds μ) ↔
    ∀ (f : BoundedContinuousFunction Ω ℝ),
      Filter.Tendsto (fun i => ∫ (ω : Ω), f ω ∂↑(μs i)) F (nhds (∫ (ω : Ω), f ω ∂↑μ))
```

## Depends on

- [Bochner integral](../../analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_integral_tendsto`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/ProbabilityMeasure.html#MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_integral_tendsto)
- [Source of `MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_integral_tendsto` in Mathlib/MeasureTheory/Measure/ProbabilityMeasure.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Measure/ProbabilityMeasure.lean#L364)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L417)
