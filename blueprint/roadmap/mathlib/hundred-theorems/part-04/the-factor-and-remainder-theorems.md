---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Polynomial.dvd_iff_isRoot, Polynomial.mod_X_sub_C_eq_C_eval
mathlib_file: Mathlib/Algebra/Polynomial/Div.lean
---

# The Factor and Remainder Theorems

Mathlib records this with 2 declarations.

`Polynomial.dvd_iff_isRoot`.

```lean
Polynomial.dvd_iff_isRoot.{u} {R : Type u} {a : R} [CommRing R] {p : Polynomial R} :
  Polynomial.X - Polynomial.C a ∣ p ↔ p.IsRoot a
```

`Polynomial.mod_X_sub_C_eq_C_eval`.

```lean
Polynomial.mod_X_sub_C_eq_C_eval.{u} {R : Type u} [Field R] (p : Polynomial R) (a : R) :
  p % (Polynomial.X - Polynomial.C a) = Polynomial.C (Polynomial.eval a p)
```

## Depends on

- [Field](../../overview/general-algebra/field-theory/field.md)
- [Linear map](../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Rational number](../../overview/general-algebra/numbers/rational-number.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)

## Sources

- [Mathlib documentation: `Polynomial.dvd_iff_isRoot`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.dvd_iff_isRoot)
- [Source of `Polynomial.dvd_iff_isRoot` in Mathlib/Algebra/Polynomial/Div.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/Div.lean#L627)
- [Mathlib documentation: `Polynomial.mod_X_sub_C_eq_C_eval`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.mod_X_sub_C_eq_C_eval)
- [Source of `Polynomial.mod_X_sub_C_eq_C_eval` in Mathlib/Algebra/Polynomial/FieldDivision.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/FieldDivision.lean#L352)
- [Freek Wiedijk's 100 theorems, no. 89](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L457)
