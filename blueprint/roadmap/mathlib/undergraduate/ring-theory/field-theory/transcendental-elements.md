# Transcendental elements

An element of an R-algebra is transcendental over R if it is not algebraic over R.

```lean
Transcendental.{u, v} (R : Type u) {A : Type v} [CommRing R] [Ring A] [Algebra R A] (x : A) : Prop
```

## Depends on

- [Algebraic elements](algebraic-elements.md)

## Sources

- [Mathlib documentation: `Transcendental`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Defs.html#Transcendental)
- [Source of `Transcendental` in Mathlib/RingTheory/Algebraic/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Algebraic/Defs.lean#L48)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L183)
