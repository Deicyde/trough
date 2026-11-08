---
declaration: theorem
origin: cited
lean: Finsupp.mapDomain_degree_support_hasLeftInverse_iff
statement: formalized
proof: formalized
---

# Joint degree-and-support profiles recover bivariate coefficients only for trivial coefficients

For any additive commutative monoid `M` in an arbitrary universe,
[`Finsupp.mapDomain_degree_support_hasLeftInverse_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FiniteSupport.lean)
proves that pushing coefficients along
`d ↦ (d.degree, d.support.card)`, for `d : Fin 2 →₀ ℕ`, admits a total left
inverse exactly when `M` is subsingleton. The profile groups coefficients
jointly by total degree and the number of variables with positive exponent.
The decoder may be **any total function**: no additive, multiplicative or
linear structure is required. The
[applications](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/FiniteSupport.lean) exclude every
decoder over `ℕ` and obtain recovery over the zero ring `ZMod 1`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Finsupp.mapDomain_degree_support_hasLeftInverse_iff` (theorem), declared in [MultivariatePolynomials/FiniteSupport.lean, line 74](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FiniteSupport.lean#L74).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `Finsupp.mapDomain_degree_support_hasLeftInverse_iff` in MultivariatePolynomials/FiniteSupport.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/FiniteSupport.lean#L74)
