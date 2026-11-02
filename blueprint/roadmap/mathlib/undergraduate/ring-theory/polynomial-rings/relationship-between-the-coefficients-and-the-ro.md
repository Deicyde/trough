---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Polynomial.coeff_eq_esymm_roots_of_card
mathlib_file: Mathlib/RingTheory/Polynomial/Vieta.lean
---

# Relationship between the coefficients and the roots of a split polynomial

Vieta's formula for the coefficients and the roots of a polynomial over an integral domain
with as many roots as its degree.

```lean
Polynomial.coeff_eq_esymm_roots_of_card.{u_1} {R : Type u_1} [CommRing R] [IsDomain R]
  {p : Polynomial R} (hroots : p.roots.card = p.natDegree) {k : ℕ} (h : k ≤ p.natDegree) :
  p.coeff k = p.leadingCoeff * (-1) ^ (p.natDegree - k) * p.roots.esymm (p.natDegree - k)
```

## Depends on

- [Roots of a polynomial](../../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)

## Proof depends on

- [Vieta's formulas](../../../thousand-plus/algebra/13-commutative-algebra/vietas-formulas.md)

## Sources

- [Mathlib documentation: `Polynomial.coeff_eq_esymm_roots_of_card`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Vieta.html#Polynomial.coeff_eq_esymm_roots_of_card)
- [Source of `Polynomial.coeff_eq_esymm_roots_of_card` in Mathlib/RingTheory/Polynomial/Vieta.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Polynomial/Vieta.lean#L114)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L165)
