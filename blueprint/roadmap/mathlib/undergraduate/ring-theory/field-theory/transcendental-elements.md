# Transcendental elements

An element of an R-algebra is transcendental over R if it is not algebraic over R.

```lean
Transcendental.{u, v} (R : Type u) {A : Type v} [CommRing R] [Ring A] [Algebra R A] (x : A) : Prop
```

## Depends on

- [Algebraic elements](algebraic-elements.md)

## Sources

- [Mathlib documentation: `Transcendental`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Defs.html#Transcendental)
- [Source of `Transcendental` in Mathlib/RingTheory/Algebraic/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/RingTheory/Algebraic/Defs.lean#L48)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L183)
