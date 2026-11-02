---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: RatFunc
mathlib_file: Mathlib/FieldTheory/RatFunc/Defs.lean
---

# Rational fraction fields with one indeterminate over a field

`RatFunc K` is `K(X)`, the field of rational functions over `K`.

The inclusion of polynomials into `RatFunc` is `algebraMap K[X] K⟮X⟯`,
the maps between `K⟮X⟯` and another field of fractions of `K[X]`,
especially `FractionRing K[X]`, are given by `IsLocalization.algEquiv`.

```lean
RatFunc.{u} (K : Type u) [CommRing K] : Type u
```

## Depends on

- [Localization](../../../../overview/general-algebra/rings/localization.md)
- [Polynomial in one indeterminate](../../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Ring](../../../../overview/general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `RatFunc`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/RatFunc/Defs.html#RatFunc)
- [Source of `RatFunc` in Mathlib/FieldTheory/RatFunc/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/RatFunc/Defs.lean#L61)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L189)
