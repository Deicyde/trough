# Independent sigma-algebras

A family of measurable space structures (i.e. of σ-algebras) is independent with respect to a
measure `μ` (typically defined on a finer σ-algebra) if the family of sets of measurable sets they
define is independent. `m : ι → MeasurableSpace Ω` is independent with respect to measure `μ` if
for any finite set of indices `s = {i_1, ..., i_n}`, for any sets
`f i_1 ∈ m i_1, ..., f i_n ∈ m i_n`, then `μ (⋂ i in s, f i) = ∏ i ∈ s, μ (f i)`.

```lean
ProbabilityTheory.iIndep.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2} (m : ι → MeasurableSpace Ω)
  {_mΩ : MeasurableSpace Ω} (μ : MeasureTheory.Measure Ω := by volume_tac) : Prop
```

## Depends on

- [Almost sure convergence](../convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Giry monad](../../analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.iIndep`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Independence/Basic.html#ProbabilityTheory.iIndep)
- [Source of `ProbabilityTheory.iIndep` in Mathlib/Probability/Independence/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Independence/Basic.lean#L105)
- [Mathlib overview: Probability Theory › Definitions in probability theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L394)
- [Mathlib undergraduate list: Probability Theory › Definitions of a probability space](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L550)
