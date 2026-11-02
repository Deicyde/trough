---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_integral_tendsto
mathlib_file: Mathlib/MeasureTheory/Measure/ProbabilityMeasure.lean
---

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

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bochner integral](../../analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)

## Proof depends on

- [Approximation by step functions](../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../topology/general-topology/part-01/closed-map.md)
- [Fatou's lemma](../../analysis/measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Monotone convergence theorem (Measures and integral calculus)](../../analysis/measures-and-integral-calculus/part-01/monotone-convergence-theorem.md)
- [Pointwise convergence](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Weak-* topology for dualities](../../analysis/topological-vector-spaces/weak-topology-for-dualities.md)

## Sources

- [Mathlib documentation: `MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_integral_tendsto`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/ProbabilityMeasure.html#MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_integral_tendsto)
- [Source of `MeasureTheory.ProbabilityMeasure.tendsto_iff_forall_integral_tendsto` in Mathlib/MeasureTheory/Measure/ProbabilityMeasure.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Measure/ProbabilityMeasure.lean#L364)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L417)
