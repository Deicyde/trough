---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: EuclideanDomain
mathlib_file: Mathlib/Algebra/EuclideanDomain/Defs.lean
---

# Euclidean domain

A `EuclideanDomain` is a non-trivial commutative ring with a division and a remainder,
satisfying `b * (a / b) + a % b = a`.
The definition of a Euclidean domain usually includes a valuation function `R → ℕ`.
This definition is slightly generalised to include a well-founded relation
`r` with the property that `r (a % b) b`, instead of a valuation.

```lean
EuclideanDomain.{u} (R : Type u) : Type u
```

## Depends on

- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `EuclideanDomain`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Defs.html#EuclideanDomain)
- [Source of `EuclideanDomain` in Mathlib/Algebra/EuclideanDomain/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/EuclideanDomain/Defs.lean#L68)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L90)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L149)
