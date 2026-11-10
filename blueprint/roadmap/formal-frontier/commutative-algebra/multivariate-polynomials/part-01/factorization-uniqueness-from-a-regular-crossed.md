---
declaration: theorem
origin: cited
lean: Polynomial.eq_and_eq_of_mul_eq_mul_of_isRegular_resultant
statement: formalized
proof: formalized
---

# Factorization uniqueness from a regular crossed resultant

Over any commutative
ring, let `G,G'` have degree at most `m` and `H,H'` degree at most `n`, with
`G.coeff m = G'.coeff m` and `H.coeff n = H'.coeff n`. If `G * H = G' * H'`
and `Polynomial.resultant G' H m n` is regular, then `G = G'` and `H = H'`, by
[`Polynomial.eq_and_eq_of_mul_eq_mul_of_isRegular_resultant`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/ResultantFactorization.lean).
Neither monicity nor positive nominal degrees are required, and the ring may have
zero divisors.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Polynomial.eq_and_eq_of_mul_eq_mul_of_isRegular_resultant` (theorem), declared in [MultivariatePolynomials/ResultantFactorization.lean, line 62](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/ResultantFactorization.lean#L62).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Polynomial.eq_and_eq_of_mul_eq_mul_of_isRegular_resultant` in MultivariatePolynomials/ResultantFactorization.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/ResultantFactorization.lean#L62)
