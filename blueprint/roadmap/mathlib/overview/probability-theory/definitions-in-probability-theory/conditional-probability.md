---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.cond
mathlib_file: Mathlib/Probability/ConditionalProbability.lean
---

# Conditional probability

The conditional probability measure of measure `μ` on set `s` is `μ` restricted to `s`
and scaled by the inverse of `μ s` (to make it a probability measure):
`(μ s)⁻¹ • μ.restrict s`.

```lean
ProbabilityTheory.cond.{u_1} {Ω : Type u_1} {m : MeasurableSpace Ω} (μ : MeasureTheory.Measure Ω)
  (s : Set Ω) : MeasureTheory.Measure Ω
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.cond`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/ConditionalProbability.html#ProbabilityTheory.cond)
- [Source of `ProbabilityTheory.cond` in Mathlib/Probability/ConditionalProbability.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/ConditionalProbability.lean#L71)
- [Mathlib overview: Probability Theory › Definitions in probability theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L395)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L554)
