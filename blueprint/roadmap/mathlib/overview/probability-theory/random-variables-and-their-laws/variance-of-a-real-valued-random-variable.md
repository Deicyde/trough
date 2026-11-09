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
- [Source of `ProbabilityTheory.variance` in Mathlib/Probability/Moments/Variance.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Moments/Variance.lean#L61)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L401)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L563)
