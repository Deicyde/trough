---
declaration: theorem
origin: cited
lean: MvPolynomial.surjective_eval_family_iff
statement: formalized
proof: formalized
---

# Finite simultaneous polynomial evaluation has an exact surjectivity criterion

For any commutative ring `R`, arbitrary variable type `σ`, finite point-index
type `ι` and family `a : ι → σ → R`,
[`MvPolynomial.surjective_eval_family_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean)
states that `p ↦ (i ↦ MvPolynomial.eval (a i) p)` is surjective exactly when
the coordinate differences `a i s - a j s`, for all `s : σ`, generate the
unit ideal for every pair of distinct indices `i ≠ j`. The three types have
independent universes. Empty families, empty or infinite variable types,
repeated points and the zero ring are included; no field hypothesis is needed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.surjective_eval_family_iff` (theorem), declared in [MultivariatePolynomials/EvaluationIdeal.lean, line 325](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L325).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.surjective_eval_family_iff` in MultivariatePolynomials/EvaluationIdeal.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L325)
