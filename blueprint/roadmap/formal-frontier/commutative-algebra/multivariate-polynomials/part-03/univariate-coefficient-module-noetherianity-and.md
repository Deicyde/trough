---
declaration: theorem
origin: cited
lean: Polynomial.isNoetherian_iff
statement: formalized
proof: formalized
---

# Univariate coefficient-module Noetherianity and Artinianity each characterize trivial coefficients

For any `R : Type u` with `[Semiring R]`,
[`Polynomial.isNoetherian_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Noetherian.lean) and
[`Polynomial.isArtinian_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Artinian.lean) give
`IsNoetherian R (Polynomial R) ↔ Subsingleton R` and
`IsArtinian R (Polynomial R) ↔ Subsingleton R`, respectively.
Both use the canonical left coefficient action
`r • p = Polynomial.C r * p`, not polynomial multiplication as a self-module.
The universe is arbitrary; no commutativity, ring, domain or field hypothesis
is required. The [coefficient-module examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/PolynomialCoefficientModules.lean)
distinguish these properties from coefficient self-Noetherianity and
self-Artinianity, even for the infinite non-ring semiring `ℝ≥0` with finitely
many ideals.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Polynomial.isNoetherian_iff` (theorem), declared in [MultivariatePolynomials/Noetherian.lean, line 202](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Noetherian.lean#L202).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Polynomial.isNoetherian_iff` in MultivariatePolynomials/Noetherian.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Noetherian.lean#L202)
