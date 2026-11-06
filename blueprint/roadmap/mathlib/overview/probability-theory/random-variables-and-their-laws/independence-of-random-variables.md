# Independence of random variables

A family of functions defined on the same space `Ω` and taking values in possibly different
spaces, each with a measurable space structure, is independent if the family of measurable space
structures they generate on `Ω` is independent. For a function `g` with codomain having measurable
space structure `m`, the generated measurable space structure is `MeasurableSpace.comap g m`.

```lean
ProbabilityTheory.iIndepFun.{u_1, u_2, u_6} {Ω : Type u_1} {ι : Type u_2} {_mΩ : MeasurableSpace Ω}
  {β : ι → Type u_6} [m : (x : ι) → MeasurableSpace (β x)] (f : (x : ι) → Ω → β x)
  (μ : MeasureTheory.Measure Ω := by volume_tac) : Prop
```

## Depends on

- [Almost sure convergence](../convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Giry monad](../../analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.iIndepFun`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Independence/Basic.html#ProbabilityTheory.iIndepFun)
- [Source of `ProbabilityTheory.iIndepFun` in Mathlib/Probability/Independence/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Independence/Basic.lean#L131)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L402)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L561)
