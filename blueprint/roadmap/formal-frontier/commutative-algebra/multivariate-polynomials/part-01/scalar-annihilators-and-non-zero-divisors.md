---
declaration: theorem
origin: cited
lean: MvPolynomial.mem_nonZeroDivisors_iff
statement: formalized
proof: formalized
---

# Scalar annihilators and non-zero-divisors

For any commutative semiring
`R` and arbitrary variable type `σ`,
[`MvPolynomial.mem_nonZeroDivisors_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Regularity.lean)
characterizes non-zero-divisors by the absence of a nonzero scalar in the
original coefficient semiring annihilating every coefficient. No individual
coefficient need be a non-zero-divisor.
[`MvPolynomial.eq_zero_of_mul_eq_zero_of_smul`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Regularity.lean)
shows that a polynomial with no nonzero scalar annihilator has no nonzero
polynomial annihilator. The results allow empty or infinite variable types,
independent universes and trivial coefficient semirings. The interpretation
in terms of `IsRegular` is asserted only over commutative rings.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.mem_nonZeroDivisors_iff` (theorem), declared in [MultivariatePolynomials/Regularity.lean, line 172](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Regularity.lean#L172).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.mem_nonZeroDivisors_iff` in MultivariatePolynomials/Regularity.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Regularity.lean#L172)
