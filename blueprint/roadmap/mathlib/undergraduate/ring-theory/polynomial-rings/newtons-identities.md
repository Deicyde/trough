# Newton's identities

**Newton's identities** give a recurrence relation for the kth elementary symmetric polynomial
in terms of lower degree elementary symmetric polynomials and power sums.

```lean
MvPolynomial.mul_esymm_eq_sum.{u_1, u_2} (σ : Type u_1) [Fintype σ] (R : Type u_2) [CommRing R]
  (k : ℕ) :
  ↑k * MvPolynomial.esymm σ R k =
    (-1) ^ (k + 1) *
      ∑ a ∈ Finset.HasAntidiagonal.antidiagonal k with a.1 < k,
        (-1) ^ a.1 * MvPolynomial.esymm σ R a.1 * MvPolynomial.psum σ R a.2
```

## Depends on

- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in several indeterminates](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)

## Proof depends on

- [Formula for the Number of Combinations](../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)

## Sources

- [Mathlib documentation: `MvPolynomial.mul_esymm_eq_sum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.html#MvPolynomial.mul_esymm_eq_sum)
- [Source of `MvPolynomial.mul_esymm_eq_sum` in Mathlib/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/MvPolynomial/Symmetric/NewtonIdentities.lean#L219)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L166)
