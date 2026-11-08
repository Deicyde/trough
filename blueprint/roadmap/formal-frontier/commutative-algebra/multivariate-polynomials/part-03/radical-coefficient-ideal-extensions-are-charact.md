---
declaration: theorem
origin: cited
lean: MvPolynomial.isRadical_map_C_iff
statement: formalized
proof: formalized
---

# Radical coefficient-ideal extensions are characterized by subtractivity

For any commutative semiring `R`, ideal `I`, and nonempty variable type `σ`,
[`MvPolynomial.isRadical_map_C_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealSubtractive.lean)
says that `I.map C` is radical exactly when `I` is radical and satisfies
`a ∈ I → a + b ∈ I → b ∈ I`. The
[sufficiency theorem](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealSubtractive.lean)
also allows empty variable types. The coefficient and variable universes are
independent; no properness, ring, domain, reducedness or finiteness hypothesis
is needed. The [examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/CoefficientIdealSubtractive.lean)
include the proper nonzero kernel of reduction `ℕ →+* ZMod 2` and the
original prime-extension and radical-extension necessity applications.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.isRadical_map_C_iff` (theorem), declared in [MultivariatePolynomials/CoefficientIdealSubtractive.lean, line 266](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealSubtractive.lean#L266).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.isRadical_map_C_iff` in MultivariatePolynomials/CoefficientIdealSubtractive.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealSubtractive.lean#L266)
