---
declaration: theorem
origin: cited
lean: MvPolynomial.coeffsIn_eq_restrictScalars_map_C
statement: formalized
proof: formalized
---

# Coefficient ideals over commutative semirings

For any commutative
semiring `R`, ideal `I` and arbitrary variable type `σ`,
[`MvPolynomial.coeffsIn_eq_restrictScalars_map_C`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdeal.lean)
identifies the extension `Ideal.map C I`, restricted to the canonical
coefficient action, with Mathlib's coefficient submodule `coeffsIn σ I`.
Polynomial membership is therefore coefficientwise membership, and
contraction along `C` recovers `I`.
[`MvPolynomial.ker_map_eq_map_C`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdeal.lean)
identifies the kernel of a coefficient map with the extension of its kernel.
Coefficients, target coefficients and variables have independent universes;
no ring, finiteness or nontriviality hypothesis is needed. The
[natural-number example](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/CoefficientIdeal.lean)
separates `2 * X` from `X` for the proper extended ideal `(2)` and for
coefficient reduction modulo two.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.coeffsIn_eq_restrictScalars_map_C` (theorem), declared in [MultivariatePolynomials/CoefficientIdeal.lean, line 75](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdeal.lean#L75).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.coeffsIn_eq_restrictScalars_map_C` in MultivariatePolynomials/CoefficientIdeal.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientIdeal.lean#L75)
