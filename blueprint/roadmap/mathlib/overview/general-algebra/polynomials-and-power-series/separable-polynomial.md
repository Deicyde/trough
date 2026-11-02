---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Polynomial.Separable
mathlib_file: Mathlib/FieldTheory/Separable.lean
---

# Separable polynomial

A polynomial is separable iff it is coprime with its derivative.

```lean
Polynomial.Separable.{u} {R : Type u} [CommSemiring R] (f : Polynomial R) : Prop
```

## Depends on

- [Coprime element](../divisibility-in-integral-domains/coprime-element.md)
- [Polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)

## Sources

- [Mathlib documentation: `Polynomial.Separable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.Separable)
- [Source of `Polynomial.Separable` in Mathlib/FieldTheory/Separable.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/Separable.lean#L41)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L99)
