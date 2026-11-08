---
declaration: theorem
origin: cited
lean: MvPolynomial.mem_range_eval_prod_iff
statement: formalized
proof: formalized
---

# The image of evaluating one polynomial at two points

Over any commutative ring `R`, for assignments `a b : σ → R` with independent
coefficient and variable universes,
[`MvPolynomial.mem_range_eval_prod_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean)
characterizes value pairs `(r, s) : R × R` of one common polynomial by
`r - s ∈ Ideal.span (Set.range (fun i => a i - b i))`, without a
finite-variable, field or comaximality assumption. The
[examples](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomialsTests/EvaluationIdealImage.lean)
contrast same-parity pairs at the one-variable integer points `0` and `2`
with all pairs at the two-variable points `(0, 0)` and `(2, 3)` despite
nonunit coordinate differences, and include empty-variable diagonal and
zero-ring boundaries.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.mem_range_eval_prod_iff` (theorem), declared in [MultivariatePolynomials/EvaluationIdeal.lean, line 279](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L279).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.mem_range_eval_prod_iff` in MultivariatePolynomials/EvaluationIdeal.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L279)
