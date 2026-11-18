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
- [Source of `MeasurableSpace.pi` in Mathlib/MeasureTheory/MeasurableSpace/Constructions.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/MeasureTheory/MeasurableSpace/Constructions.lean#L598)
- [Mathlib undergraduate list: Measures and integral calculus › Measure theory](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L504)
- [Mathlib undergraduate list: Measures and integral calculus › Measure theory](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L509)
