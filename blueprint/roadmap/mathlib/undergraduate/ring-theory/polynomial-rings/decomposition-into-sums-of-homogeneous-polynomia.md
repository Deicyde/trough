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
- [Source of `MvPolynomial.sum_homogeneousComponent` in Mathlib/RingTheory/MvPolynomial/Homogeneous.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/MvPolynomial/Homogeneous.lean#L581)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L168)
