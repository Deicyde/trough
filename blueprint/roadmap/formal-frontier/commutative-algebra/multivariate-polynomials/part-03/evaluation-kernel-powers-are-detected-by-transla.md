---
declaration: theorem
origin: cited
lean: MvPolynomial.mem_pow_ker_eval_addUnits_iff
statement: formalized
proof: formalized
---

# Evaluation-kernel powers are detected by translated coefficients

For any
commutative semiring `R` and point `a : σ → AddUnits R`,
[`MvPolynomial.mem_pow_ker_eval_addUnits_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean)
characterizes membership in every `n`th evaluation-kernel power by vanishing
of all coefficients of total degree `< n` after the translation `p(X + a)`.
Over a commutative ring,
[`MvPolynomial.mem_pow_ker_eval_iff`](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean)
allows arbitrary points `a : σ → R`. Both results allow arbitrary variable
types, independent coefficient/variable universes, and every `n : ℕ`, including zero.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results) of [FormalFrontier/multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials) at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `MvPolynomial.mem_pow_ker_eval_addUnits_iff` (theorem), declared in [MultivariatePolynomials/EvaluationIdeal.lean, line 149](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L149).

Read from the source at commit [724d9804](https://github.com/FormalFrontier/multivariate-polynomials/tree/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a), without running Lean.

## Sources

- [multivariate-polynomials at 724d9804: README, headline results](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/README.md#headline-results)
- [Source of `MvPolynomial.mem_pow_ker_eval_addUnits_iff` in MultivariatePolynomials/EvaluationIdeal.lean](https://github.com/FormalFrontier/multivariate-polynomials/blob/724d9804aa6e853d9fe34f6a35c5c0d35c7f8c6a/MultivariatePolynomials/EvaluationIdeal.lean#L149)
