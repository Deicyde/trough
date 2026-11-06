# Vector-valued integrable function (Bochner integral)

`Integrable f μ` means that `f` is measurable and that the integral `∫⁻ a, ‖f a‖ ∂μ` is finite.
`Integrable f` means `Integrable f volume`.

```lean
MeasureTheory.Integrable.{u_5, u_7} {ε : Type u_5} [TopologicalSpace ε] [ContinuousENorm ε]
  {α : Type u_7} {x✝ : MeasurableSpace α} (f : α → ε)
  (μ : MeasureTheory.Measure α := by volume_tac) : Prop
```

## Depends on

- [Almost sure convergence](../../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Continuous function](../../../topology/general-topology/part-01/continuous-function.md)
- [Integral of positive measurable functions](integral-of-positive-measurable-functions.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Integrable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/L1Space/Integrable.html#MeasureTheory.Integrable)
- [Source of `MeasureTheory.Integrable` in Mathlib/MeasureTheory/Function/L1Space/Integrable.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/L1Space/Integrable.lean#L55)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L350)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L516)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L518)
