# Product of sigma-algebras

Mathlib states this as `MeasurableSpace.pi`.

```lean
MeasurableSpace.pi.{u_4, u_6} {δ : Type u_4} {X : δ → Type u_6}
  [m : (a : δ) → MeasurableSpace (X a)] : MeasurableSpace ((a : δ) → X a)
```

## Depends on

- [Events](../../probability-theory/definitions-of-a-probability-space/events.md)

## Sources

- [Mathlib documentation: `MeasurableSpace.pi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/MeasurableSpace/Constructions.html#MeasurableSpace.pi)
- [Source of `MeasurableSpace.pi` in Mathlib/MeasureTheory/MeasurableSpace/Constructions.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/MeasurableSpace/Constructions.lean#L580)
- [Mathlib undergraduate list: Measures and integral calculus › Measure theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L504)
- [Mathlib undergraduate list: Measures and integral calculus › Measure theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L509)
