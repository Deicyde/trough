---
declaration: theorem
origin: cited
lean: MvPolynomial.isMaximal_map_C_iff
statement: formalized
proof: formalized
---

# Maximal coefficient extensions over commutative semirings

For a commutative
semiring `R`, any variable type `σ` and ideal `I`,
`(I.map MvPolynomial.C).IsMaximal ↔ I.IsMaximal ∧ IsEmpty σ`, by
[`MvPolynomial.isMaximal_map_C_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealMaximal.lean).
With nonempty `σ`, no coefficient extension is maximal. For proper `I`,
the constant-coefficient preimage is a strict intermediate ideal.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.isMaximal_map_C_iff` (theorem), declared in [MultivariatePolynomials/CoefficientIdealMaximal.lean, line 61](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealMaximal.lean#L61).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.isMaximal_map_C_iff` in MultivariatePolynomials/CoefficientIdealMaximal.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdealMaximal.lean#L61)
