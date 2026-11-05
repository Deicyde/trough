---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.bernoulliMeasure
mathlib_file: Mathlib/Probability/Distributions/Bernoulli.lean
---

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
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.bernoulliMeasure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Bernoulli.html#ProbabilityTheory.bernoulliMeasure)
- [Source of `ProbabilityTheory.bernoulliMeasure` in Mathlib/Probability/Distributions/Bernoulli.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Distributions/Bernoulli.lean#L41)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L406)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L566)
