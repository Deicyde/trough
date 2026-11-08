---
declaration: theorem
origin: cited
lean: MaximalSpectrum.infinite_polynomial
statement: formalized
proof: formalized
---

# Infinitely many maximal ideals of polynomial rings

Every nontrivial
commutative ring `R` has infinitely many maximal ideals in `R[X]`, including
when `R` is a finite field, by
[`MaximalSpectrum.infinite_polynomial`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimeSpectrum.lean).
For any commutative ring `R` and arbitrary variable type `σ`, the maximal
spectrum of `MvPolynomial σ R` is infinite exactly when `R` is nontrivial
and either `σ` is nonempty or the maximal spectrum of `R` is infinite, by
[`MaximalSpectrum.infinite_mvPolynomial_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimeSpectrum.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MaximalSpectrum.infinite_polynomial` (theorem), declared in [MultivariatePolynomials/PrimeSpectrum.lean, line 190](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimeSpectrum.lean#L190).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MaximalSpectrum.infinite_polynomial` in MultivariatePolynomials/PrimeSpectrum.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimeSpectrum.lean#L190)
