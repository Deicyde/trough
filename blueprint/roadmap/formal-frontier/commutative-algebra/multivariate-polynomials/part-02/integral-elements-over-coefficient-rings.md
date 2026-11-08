---
declaration: theorem
origin: cited
lean: MvPolynomial.isIntegral_iff_coeff_isNilpotent
statement: formalized
proof: formalized
---

# Integral elements over coefficient rings

For any commutative ring `R`
and arbitrary variable type `σ`,
[`MvPolynomial.isIntegral_iff_coeff_isNilpotent`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IntegralCoefficients.lean)
characterizes `IsIntegral R p` by nilpotence of every nonconstant coefficient.
For reduced `R`,
[`MvPolynomial.isIntegral_iff_eq_C_coeff_zero`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IntegralCoefficients.lean)
specializes this to `p = C (p.coeff 0)`.
The coefficient and variable universes are independent; trivial coefficient
rings and empty or infinite variable types are allowed. Over `ZMod 4`,
`C 2 * X ()` is a nonconstant square-zero integral polynomial.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.isIntegral_iff_coeff_isNilpotent` (theorem), declared in [MultivariatePolynomials/IntegralCoefficients.lean, line 110](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IntegralCoefficients.lean#L110).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.isIntegral_iff_coeff_isNilpotent` in MultivariatePolynomials/IntegralCoefficients.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/IntegralCoefficients.lean#L110)
