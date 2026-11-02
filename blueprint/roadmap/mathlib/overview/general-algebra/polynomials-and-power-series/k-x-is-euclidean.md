---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: Polynomial.instEuclideanDomain
mathlib_file: Mathlib/Algebra/Polynomial/FieldDivision.lean
---

# $K[X]$ is Euclidean

Mathlib states this as `Polynomial.instEuclideanDomain`.

```lean
Polynomial.instEuclideanDomain.{u} {R : Type u} [Field R] : EuclideanDomain (Polynomial R)
```

## Depends on

- [Euclidean domain](../divisibility-in-integral-domains/euclidean-domain.md)
- [Field](../field-theory/field.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `Polynomial.instEuclideanDomain`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.instEuclideanDomain)
- [Source of `Polynomial.instEuclideanDomain` in Mathlib/Algebra/Polynomial/FieldDivision.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/FieldDivision.lean#L360)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L100)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L158)
