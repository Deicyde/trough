# Measurable function

A function `f` between measurable spaces is measurable if the preimage of every
measurable set is measurable.

```lean
Measurable.{u_1, u_2} {α : Type u_1} {β : Type u_2} [MeasurableSpace α] [MeasurableSpace β]
  (f : α → β) : Prop
```

## Depends on

- [Events](../../../../undergraduate/probability-theory/definitions-of-a-probability-space/events.md)

## Sources

- [Mathlib documentation: `Measurable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/MeasurableSpace/Defs.html#Measurable)
- [Source of `Measurable` in Mathlib/MeasureTheory/MeasurableSpace/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/MeasurableSpace/Defs.lean#L489)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L338)
- [Mathlib undergraduate list: Measures and integral calculus › Measure theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L510)
