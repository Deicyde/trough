---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.variance
mathlib_file: Mathlib/Probability/Moments/Variance.lean
---

# Variance of a real-valued random variable

The `ℝ`-valued variance of a real-valued random variable defined by applying `ENNReal.toReal`
to `evariance`.

```lean
ProbabilityTheory.variance.{u_1} {Ω : Type u_1} {mΩ : MeasurableSpace Ω} (X : Ω → ℝ)
  (μ : MeasureTheory.Measure Ω) : ℝ
```

## Depends on

- [Bochner integral](../../analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.variance`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Moments/Variance.html#ProbabilityTheory.variance)
- [Source of `ProbabilityTheory.variance` in Mathlib/Probability/Moments/Variance.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Moments/Variance.lean#L61)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L401)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L563)
