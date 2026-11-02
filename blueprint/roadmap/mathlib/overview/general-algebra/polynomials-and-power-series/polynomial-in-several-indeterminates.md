---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: MvPolynomial
mathlib_file: Mathlib/Algebra/MvPolynomial/Basic.lean
---

# Polynomial in several indeterminates

Multivariate polynomial, where `σ` is the index set of the variables and
`R` is the coefficient ring

```lean
MvPolynomial.{u_1, u_2} (σ : Type u_1) (R : Type u_2) [CommSemiring R] : Type (max u_2 u_1)
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Finitely supported function](../../data-structures/maps/finitely-supported-function.md)

## Sources

- [Mathlib documentation: `MvPolynomial`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial)
- [Source of `MvPolynomial` in Mathlib/Algebra/MvPolynomial/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/MvPolynomial/Basic.lean#L78)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L106)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L162)
