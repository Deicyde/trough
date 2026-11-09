# Gaussian processes

A stochastic process is a Gaussian process if all its finite dimensional distributions are
Gaussian.

```lean
ProbabilityTheory.IsGaussianProcess.{u_1, u_2, u_3} {Ω : Type u_1} {E : Type u_2} {T : Type u_3}
  {mΩ : MeasurableSpace Ω} [MeasurableSpace E] [TopologicalSpace E] [AddCommMonoid E]
  [_root_.Module ℝ E] (X : T → Ω → E) (P : MeasureTheory.Measure Ω := by volume_tac) : Prop
```

## Depends on

- [Gaussian measures](../random-variables-and-their-laws/gaussian-measures.md)
- [Product of sigma-algebras](../../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.IsGaussianProcess`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Gaussian/IsGaussianProcess/Def.html#ProbabilityTheory.IsGaussianProcess)
- [Source of `ProbabilityTheory.IsGaussianProcess` in Mathlib/Probability/Distributions/Gaussian/IsGaussianProcess/Def.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Distributions/Gaussian/IsGaussianProcess/Def.lean#L27)
- [Mathlib overview: Probability Theory › Stochastic Processes](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L427)
