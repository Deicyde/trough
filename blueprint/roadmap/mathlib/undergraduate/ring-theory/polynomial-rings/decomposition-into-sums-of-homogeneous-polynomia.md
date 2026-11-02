---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MvPolynomial.sum_homogeneousComponent
mathlib_file: Mathlib/RingTheory/MvPolynomial/Homogeneous.lean
---

# Decomposition into sums of homogeneous polynomials

Mathlib states this as `MvPolynomial.sum_homogeneousComponent`.

```lean
MvPolynomial.sum_homogeneousComponent.{u_1, u_3} {σ : Type u_1} {R : Type u_3} [CommSemiring R]
  (φ : MvPolynomial σ R) :
  ∑ i ∈ Finset.range (φ.totalDegree + 1), (MvPolynomial.homogeneousComponent i) φ = φ
```

## Depends on

- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in several indeterminates](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)

## Sources

- [Mathlib documentation: `MvPolynomial.sum_homogeneousComponent`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPolynomial/Homogeneous.html#MvPolynomial.sum_homogeneousComponent)
- [Source of `MvPolynomial.sum_homogeneousComponent` in Mathlib/RingTheory/MvPolynomial/Homogeneous.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/MvPolynomial/Homogeneous.lean#L558)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L168)
