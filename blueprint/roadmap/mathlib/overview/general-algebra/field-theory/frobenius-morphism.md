---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: frobenius
mathlib_file: Mathlib/Algebra/CharP/Lemmas.lean
---

# Frobenius morphism

The Frobenius map `x ↦ x ^ p`.

```lean
frobenius.{u_2} (R : Type u_2) [CommSemiring R] (p : ℕ) [ExpChar R p] : R →+* R
```

## Depends on

- [Characteristic p](characteristic-p.md)
- [Characteristic zero](characteristic-zero.md)
- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)
- [Ring morphism](../rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `frobenius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#frobenius)
- [Source of `frobenius` in Mathlib/Algebra/CharP/Lemmas.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/CharP/Lemmas.lean#L324)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L125)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L176)
