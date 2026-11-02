---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Polynomial
mathlib_file: Mathlib/Algebra/Polynomial/Basic.lean
---

# Polynomial in one indeterminate

`Polynomial R` is the type of univariate polynomials over `R`,
denoted as `R[X]` within the `Polynomial` namespace.

Polynomials should be seen as (semi-)rings with the additional constructor `X`.
The embedding from `R` is called `C`.

```lean
Polynomial.{u_1} (R : Type u_1) [Semiring R] : Type u_1
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Finitely supported function](../../data-structures/maps/finitely-supported-function.md)

## Sources

- [Mathlib documentation: `Polynomial`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Basic.html#Polynomial)
- [Source of `Polynomial` in Mathlib/Algebra/Polynomial/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/Basic.lean#L63)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L96)
