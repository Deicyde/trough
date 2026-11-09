# Transcendental elements

An element of an R-algebra is transcendental over R if it is not algebraic over R.

```lean
Transcendental.{u, v} (R : Type u) {A : Type v} [CommRing R] [Ring A] [Algebra R A] (x : A) : Prop
```

## Depends on

- [Algebraic elements](algebraic-elements.md)

## Sources

- [Mathlib documentation: `Transcendental`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Defs.html#Transcendental)
- [Source of `Transcendental` in Mathlib/RingTheory/Algebraic/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/Algebraic/Defs.lean#L48)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L183)
