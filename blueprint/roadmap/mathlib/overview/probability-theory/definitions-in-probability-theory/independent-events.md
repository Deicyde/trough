---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.iIndepSet
mathlib_file: Mathlib/Probability/Independence/Basic.lean
---

# Independent events

A family of sets is independent if the family of measurable space structures they generate is
independent. For a set `s`, the generated measurable space has measurable sets `∅, s, sᶜ, univ`.

```lean
ProbabilityTheory.iIndepSet.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2} {_mΩ : MeasurableSpace Ω}
  (s : ι → Set Ω) (μ : MeasureTheory.Measure Ω := by volume_tac) : Prop
```

## Depends on

- [Almost sure convergence](../convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Giry monad](../../analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.iIndepSet`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Independence/Basic.html#ProbabilityTheory.iIndepSet)
- [Source of `ProbabilityTheory.iIndepSet` in Mathlib/Probability/Independence/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Independence/Basic.lean#L121)
- [Mathlib overview: Probability Theory › Definitions in probability theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L393)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L548)
