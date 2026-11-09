# Symmetric polynomials

A `MvPolynomial φ` is symmetric if it is invariant under
permutations of its variables by the `rename` operation

```lean
MvPolynomial.IsSymmetric.{u_1, u_3} {σ : Type u_1} {R : Type u_3} [CommSemiring R]
  (φ : MvPolynomial σ R) : Prop
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Polynomial in several indeterminates](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)

## Sources

- [Mathlib documentation: `MvPolynomial.IsSymmetric`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPolynomial/Symmetric/Defs.html#MvPolynomial.IsSymmetric)
- [Source of `MvPolynomial.IsSymmetric` in Mathlib/RingTheory/MvPolynomial/Symmetric/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/MvPolynomial/Symmetric/Defs.lean#L109)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L169)
