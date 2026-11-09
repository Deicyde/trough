# Gaussian measures

A measure is Gaussian if its map by every continuous linear form is a real Gaussian measure.

```lean
ProbabilityTheory.IsGaussian.{u_1} {E : Type u_1} [TopologicalSpace E] [AddCommMonoid E]
  [_root_.Module ℝ E] {mE : MeasurableSpace E} (μ : MeasureTheory.Measure E) : Prop
```

## Depends on

- [Dual of a normed space](../../analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Gaussian law](gaussian-law.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Variance of a real-valued random variable](variance-of-a-real-valued-random-variable.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.IsGaussian`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Gaussian/Basic.html#ProbabilityTheory.IsGaussian)
- [Source of `ProbabilityTheory.IsGaussian` in Mathlib/Probability/Distributions/Gaussian/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Distributions/Gaussian/Basic.lean#L44)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L412)
