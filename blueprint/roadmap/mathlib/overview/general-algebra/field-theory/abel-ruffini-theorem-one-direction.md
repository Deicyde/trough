---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: isSolvable_gal_minpoly
mathlib_file: Mathlib/FieldTheory/AbelRuffini.lean
---

# Abel-Ruffini theorem (one direction)

Mathlib states this as `isSolvable_gal_minpoly`.

```lean
isSolvable_gal_minpoly.{u_1, u_2} {F : Type u_1} {E : Type u_2} [Field F] [Field E] [Algebra F E]
  {x : E} (hx : x ∈ solvableByRad F E) : Group.IsSolvable (minpoly F x).Gal
```

## Depends on

- [Minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Splitting field](splitting-field.md)
- [Subgroup](../group-theory/part-01/subgroup.md)

## Proof depends on

- [Algebraic extension](algebraic-extension.md)
- [Direct product of groups](../../../undergraduate/group-theory/basic-definitions/direct-product-of-groups.md)
- [Local ring](../rings/local-ring.md)
- [Roots of a polynomial](../polynomials-and-power-series/roots-of-a-polynomial.md)
- [Subfield](subfield.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)

## Sources

- [Mathlib documentation: `isSolvable_gal_minpoly`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#isSolvable_gal_minpoly)
- [Source of `isSolvable_gal_minpoly` in Mathlib/FieldTheory/AbelRuffini.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/AbelRuffini.lean#L304)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L135)
