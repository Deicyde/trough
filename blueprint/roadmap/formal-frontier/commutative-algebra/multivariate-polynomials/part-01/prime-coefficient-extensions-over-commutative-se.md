---
declaration: theorem
origin: cited
lean: MvPolynomial.isPrime_map_C_of_subtractive
statement: formalized
proof: formalized
---

# Prime coefficient extensions over commutative semirings

For a commutative
semiring `R`, any variable type `σ` and ideal `I`, primality of `I` together
with `∀ a b : R, a ∈ I → a + b ∈ I → b ∈ I` implies primality of
`I.map MvPolynomial.C`,
by [`MvPolynomial.isPrime_map_C_of_subtractive`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealPrime.lean).
For nonempty `σ`, these conditions are also necessary, by
[`MvPolynomial.isPrime_map_C_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealPrime.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.isPrime_map_C_of_subtractive` (theorem), declared in [MultivariatePolynomials/CoefficientIdealPrime.lean, line 34](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealPrime.lean#L34).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.isPrime_map_C_of_subtractive` in MultivariatePolynomials/CoefficientIdealPrime.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealPrime.lean#L34)
