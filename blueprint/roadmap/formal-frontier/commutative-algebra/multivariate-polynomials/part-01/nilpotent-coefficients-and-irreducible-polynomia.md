---
declaration: theorem
origin: cited
lean: MvPolynomial.isNilpotent_iff_coeff
statement: formalized
proof: formalized
---

# Nilpotent coefficients and irreducible polynomial spectra

For any
commutative semiring `R` and arbitrary variable type `σ`,
[`MvPolynomial.isNilpotent_iff_coeff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Nilpotent.lean)
characterizes nilpotent polynomials by nilpotence of every coefficient.
[`PrimeSpectrum.irreducibleSpace_mvPolynomial_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/PrimeSpectrum.lean)
states that `PrimeSpectrum (MvPolynomial σ R)` is irreducible exactly when
`PrimeSpectrum R` is irreducible. Coefficients and variables have independent
universes; empty or infinite variables and trivial coefficients are allowed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.isNilpotent_iff_coeff` (theorem), declared in [MultivariatePolynomials/Nilpotent.lean, line 131](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Nilpotent.lean#L131).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.isNilpotent_iff_coeff` in MultivariatePolynomials/Nilpotent.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Nilpotent.lean#L131)
