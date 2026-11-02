---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Polynomial.roots
mathlib_file: Mathlib/Algebra/Polynomial/Roots.lean
---

# Roots of a polynomial

`roots p` noncomputably gives a multiset containing all the roots of `p`,
including their multiplicities.

```lean
Polynomial.roots.{u} {R : Type u} [CommRing R] [IsDomain R] (p : Polynomial R) : Multiset R
```

## Depends on

- [Multiplicity](multiplicity.md)

## Sources

- [Mathlib documentation: `Polynomial.roots`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots)
- [Source of `Polynomial.roots` in Mathlib/Algebra/Polynomial/Roots.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/Roots.lean#L54)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L97)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L163)
