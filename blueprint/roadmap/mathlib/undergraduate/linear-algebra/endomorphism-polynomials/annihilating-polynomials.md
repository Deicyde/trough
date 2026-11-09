# Annihilating polynomials

`annIdeal R a` is the *annihilating ideal* of all `p : R[X]` such that `p(a) = 0`.

The informal notation `p(a)` stands for `Polynomial.aeval a p`.
Again informally, the annihilating ideal of `a` is
`{ p ∈ R[X] | p(a) = 0 }`. This is an ideal in `R[X]`.
The formal definition uses the kernel of the aeval map.

```lean
Polynomial.annIdeal.{u_1, u_2} (R : Type u_1) {A : Type u_2} [CommSemiring R] [Semiring A]
  [Algebra R A] (a : A) : Ideal (Polynomial R)
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Ideal of a commutative ring](../../../overview/general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `Polynomial.annIdeal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/AnnihilatingPolynomial.html#Polynomial.annIdeal)
- [Source of `Polynomial.annIdeal` in Mathlib/LinearAlgebra/AnnihilatingPolynomial.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/AnnihilatingPolynomial.lean#L48)
- [Mathlib undergraduate list: Linear algebra › Endomorphism polynomials](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L54)
