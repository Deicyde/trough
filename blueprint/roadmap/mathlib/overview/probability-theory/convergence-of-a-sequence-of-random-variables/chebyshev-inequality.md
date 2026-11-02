---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.meas_ge_le_variance_div_sq
mathlib_file: Mathlib/Probability/Moments/Variance.lean
---

# Chebyshev inequality

**Chebyshev's inequality**: one can control the deviation probability of a real random variable
from its expectation in terms of the variance.

```lean
ProbabilityTheory.meas_ge_le_variance_div_sq.{u_1} {Ω : Type u_1} {mΩ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsFiniteMeasure μ] {X : Ω → ℝ}
  (hX : MeasureTheory.MemLp X 2 μ) {c : ℝ} (hc : 0 < c) :
  μ {ω | c ≤ |X ω - ∫ (x : Ω), X x ∂μ|} ≤ ENNReal.ofReal (ProbabilityTheory.variance X μ / c ^ 2)
```

## Depends on

- [Variance of a real-valued random variable](../random-variables-and-their-laws/variance-of-a-real-valued-random-variable.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.meas_ge_le_variance_div_sq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Moments/Variance.html#ProbabilityTheory.meas_ge_le_variance_div_sq)
- [Source of `ProbabilityTheory.meas_ge_le_variance_div_sq` in Mathlib/Probability/Moments/Variance.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Moments/Variance.lean#L396)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L419)
- [Mathlib undergraduate list: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L581)
