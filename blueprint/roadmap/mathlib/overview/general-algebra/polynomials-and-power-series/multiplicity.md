---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Polynomial.rootMultiplicity
mathlib_file: Mathlib/Algebra/Polynomial/Div.lean
---

# Multiplicity

The largest power of `X - C a` which divides `p`.

```lean
Polynomial.rootMultiplicity.{u} {R : Type u} [Ring R] (a : R) (p : Polynomial R) : ℕ
```

## Depends on

- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)
- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `Polynomial.rootMultiplicity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.rootMultiplicity)
- [Source of `Polynomial.rootMultiplicity` in Mathlib/Algebra/Polynomial/Div.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/Div.lean#L501)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L98)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L164)
