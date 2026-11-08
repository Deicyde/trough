---
declaration: theorem
origin: cited
lean: MvPolynomial.eval₂Hom_coefficientProduct_eq_iff
statement: formalized
proof: formalized
---

# Finite coefficient-product equations determine whole products

For independent
commutative semirings `C` and `R`, an arbitrary homomorphism `φ : C →+* R`,
nominal sizes `m,n`, seeds `g,h : Polynomial C` and arbitrary target coefficient
point, [`MvPolynomial.eval₂Hom_coefficientProduct_eq_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientProduct.lean)
identifies the finite evaluated equations with equality of the entire ordinary
perturbed product to `T`. It assumes target-side bounds
`(g.map φ).natDegree ≤ m`, `(h.map φ).natDegree ≤ n`, `T.natDegree ≤ m + n`, and
`T.coeff (m + n) = (g.map φ).coeff m * (h.map φ).coeff n`. Zero sizes, mapped
degree drops and trivial semirings are included; no source degree bound or
injectivity of `φ` is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.eval₂Hom_coefficientProduct_eq_iff` (theorem), declared in [MultivariatePolynomials/CoefficientProduct.lean, line 354](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientProduct.lean#L354).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.eval₂Hom_coefficientProduct_eq_iff` in MultivariatePolynomials/CoefficientProduct.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/CoefficientProduct.lean#L354)
