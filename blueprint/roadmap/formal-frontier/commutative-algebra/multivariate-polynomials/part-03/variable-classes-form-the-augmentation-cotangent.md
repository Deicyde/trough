---
declaration: def
origin: cited
lean: MvPolynomial.idealOfVarsCotangentBasis
statement: formalized
---

# Variable classes form the augmentation cotangent basis

For any
`(σ : Type u)` and `(R : Type v) [CommRing R]`,
[`MvPolynomial.idealOfVarsCotangentBasis`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Cotangent.lean)
is a `σ`-indexed `R`-basis of the stock variable-ideal cotangent `I/I²`.
Its vectors are the classes of `X i`, with inherited coefficient action
`r • [p] = [C r * p]`. The `_apply` and `_repr_X` lemmas characterize those
vectors, and `idealOfVarsCotangentBasis_repr_toCotangent` computes each
coordinate as `(x : MvPolynomial σ R).coeff (Finsupp.single i 1)` for any
representative `x` in the variable ideal. Quadratic and higher terms do not
contribute. The variable and coefficient universes are independent; empty
or infinite variable types, zero rings and nilpotent coefficients are allowed.
This is an indexed basis, not a numerical rank assertion over the zero ring.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.idealOfVarsCotangentBasis` (def), declared in [MultivariatePolynomials/Cotangent.lean, line 131](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Cotangent.lean#L131).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.idealOfVarsCotangentBasis` in MultivariatePolynomials/Cotangent.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Cotangent.lean#L131)
