# Bernoulli law

The **Bernoulli distribution** over an arbitrary measurable space `X`.
Given `x y : X` and `p : I` (`I` is the `unitInterval`),
it is the measure which gives mass `p` to `{x}` and `1 - p` to `{y}`.

```lean
ProbabilityTheory.bernoulliMeasure.{u_1} {X : Type u_1} [MeasurableSpace X] (x y : X)
  (p : ↑unitInterval) : MeasureTheory.Measure X
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.bernoulliMeasure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Bernoulli.html#ProbabilityTheory.bernoulliMeasure)
- [Source of `ProbabilityTheory.bernoulliMeasure` in Mathlib/Probability/Distributions/Bernoulli.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Distributions/Bernoulli.lean#L41)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L406)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L566)
