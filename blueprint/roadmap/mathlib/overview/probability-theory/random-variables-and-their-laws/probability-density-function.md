---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.HasPDF
mathlib_file: Mathlib/Probability/Density.lean
---

# Probability density function

A random variable `X : Ω → E` is said to have a probability density function (`HasPDF`)
with respect to the measure `ℙ` on `Ω` and `μ` on `E`
if the push-forward measure of `ℙ` along `X` is absolutely continuous with respect to `μ`
and they have a Lebesgue decomposition (`HaveLebesgueDecomposition`).

```lean
MeasureTheory.HasPDF.{u_1, u_2} {Ω : Type u_1} {E : Type u_2} [MeasurableSpace E]
  {m : MeasurableSpace Ω} (X : Ω → E) (ℙ : MeasureTheory.Measure Ω)
  (μ : MeasureTheory.Measure E := by volume_tac) : Prop
```

## Depends on

- [Almost sure convergence](../convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Integral of positive measurable functions](../../analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Sources

- [Mathlib documentation: `MeasureTheory.HasPDF`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Density.html#MeasureTheory.HasPDF)
- [Source of `MeasureTheory.HasPDF` in Mathlib/Probability/Density.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Density.lean#L61)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L400)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L559)
