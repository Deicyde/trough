# Hölder's inequality

Hölder's inequality for functions `α → ℝ≥0`. The integral of the product of two functions
is bounded by the product of their `ℒp` and `ℒq` seminorms when `p` and `q` are conjugate
exponents.

```lean
NNReal.lintegral_mul_le_Lp_mul_Lq.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} {p q : ℝ} (hpq : p.HolderConjugate q) {f g : α → NNReal}
  (hf : AEMeasurable f μ) (hg : AEMeasurable g μ) :
  ∫⁻ (a : α), ↑((f * g) a) ∂μ ≤
    (∫⁻ (a : α), ↑(f a) ^ p ∂μ) ^ (1 / p) * (∫⁻ (a : α), ↑(g a) ^ q ∂μ) ^ (1 / q)
```

## Depends on

- [Almost sure convergence](../../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Integral of positive measurable functions](../../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)

## Sources

- [Mathlib documentation: `NNReal.lintegral_mul_le_Lp_mul_Lq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/MeanInequalities.html#NNReal.lintegral_mul_le_Lp_mul_Lq)
- [Source of `NNReal.lintegral_mul_le_Lp_mul_Lq` in Mathlib/MeasureTheory/Integral/MeanInequalities.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Integral/MeanInequalities.lean#L479)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L523)
