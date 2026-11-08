---
declaration: theorem
origin: cited
lean: MvPolynomial.ideal_map_C_sup_span_X_image_fg_iff
statement: formalized
proof: formalized
---

# Coefficient-and-variable ideals have an exact finite-generation criterion

For any commutative semiring `R`, coefficient ideal `I`, and variable subset `S`,
[`MvPolynomial.ideal_map_C_sup_span_X_image_fg_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IdealOfVars.lean)
characterizes finite generation of `Ideal.map C I ⊔ Ideal.span (X '' S)`:
`I` must be finitely generated, and either `S` is finite or `I` is the unit ideal.
The coefficient and variable universes are independent; no ring, domain,
subtractivity or finite-ambient-variable hypothesis is required. The
[examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/CoefficientVariableIdeal.lean) include
a proper nonsubtractive ideal over `ℕ`, coefficient zero divisors, and the
zero-ring boundary.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.ideal_map_C_sup_span_X_image_fg_iff` (theorem), declared in [MultivariatePolynomials/IdealOfVars.lean, line 201](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IdealOfVars.lean#L201).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.ideal_map_C_sup_span_X_image_fg_iff` in MultivariatePolynomials/IdealOfVars.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IdealOfVars.lean#L201)
