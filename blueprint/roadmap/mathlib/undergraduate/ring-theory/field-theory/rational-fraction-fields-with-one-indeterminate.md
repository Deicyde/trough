# Rational fraction fields with one indeterminate over a field

`RatFunc K` is `K(X)`, the field of rational functions over `K`.

The inclusion of polynomials into `RatFunc` is `algebraMap K[X] K⟮X⟯`,
the maps between `K⟮X⟯` and another field of fractions of `K[X]`,
especially `FractionRing K[X]`, are given by `IsLocalization.algEquiv`.

```lean
RatFunc.{u} (K : Type u) [CommRing K] : Type u
```

## Depends on

- [Localization](../../../overview/general-algebra/rings/localization.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `RatFunc`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/RatFunc/Defs.html#RatFunc)
- [Source of `RatFunc` in Mathlib/FieldTheory/RatFunc/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/FieldTheory/RatFunc/Defs.lean#L61)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L189)
