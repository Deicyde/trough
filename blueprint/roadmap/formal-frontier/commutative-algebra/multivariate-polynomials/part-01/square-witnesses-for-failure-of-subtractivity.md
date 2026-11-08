---
declaration: def
origin: cited
lean: MvPolynomial.subtractiveWitness
statement: formalized
---

# Square witnesses for failure of subtractivity

Over any commutative
semiring `R`, for `i : σ` and `a b : R`,
[`MvPolynomial.subtractiveWitness`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealSubtractive.lean)
is `C a + C b * X i + C (a + b) * X i ^ 2`, with linear coefficient `b`.
Its square belongs to `I.map C` if `a ∈ I` and `a + b ∈ I`, while
`b ∉ I` excludes the witness itself. Thus a radical (in particular prime)
extension over nonempty variables forces subtractivity. Coefficient and
variable universes are independent; no finiteness or nontriviality is needed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.subtractiveWitness` (def), declared in [MultivariatePolynomials/CoefficientIdealSubtractive.lean, line 79](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealSubtractive.lean#L79).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.subtractiveWitness` in MultivariatePolynomials/CoefficientIdealSubtractive.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealSubtractive.lean#L79)
