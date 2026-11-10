---
declaration: theorem
origin: cited
lean: MvPolynomial.exists_eval_eq_totalDegree_le_of_pairwise_span_eq_top
statement: formalized
proof: formalized
---

# Degree-controlled finite interpolation

Over any commutative ring `R`,
let `s : Finset ι` select points `a : ι → σ → R`. If, for every distinct
`i, j ∈ s`, the coordinate differences `a i x - a j x` span the unit ideal,
then any prescribed values `v : ι → R` are attained on `s` by a polynomial
of total degree at most `s.card - 1`
([`MvPolynomial.exists_eval_eq_totalDegree_le_of_pairwise_span_eq_top`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Interpolation.lean)).
Both the variable type and ambient label type may be infinite; no field or
domain hypothesis is needed. The theorem asserts existence, not uniqueness.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.exists_eval_eq_totalDegree_le_of_pairwise_span_eq_top` (theorem), declared in [MultivariatePolynomials/Interpolation.lean, line 75](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Interpolation.lean#L75).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.exists_eval_eq_totalDegree_le_of_pairwise_span_eq_top` in MultivariatePolynomials/Interpolation.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/Interpolation.lean#L75)
