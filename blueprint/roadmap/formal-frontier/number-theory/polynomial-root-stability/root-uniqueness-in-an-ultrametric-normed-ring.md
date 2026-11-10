---
declaration: theorem
origin: cited
lean: Polynomial.eq_of_eval_eq_zero_of_mul_norm_sub_lt_norm_derivative
statement: formalized
proof: formalized
---

# Root uniqueness in an ultrametric normed ring

Let `R` be an ultrametric normed commutative ring with multiplicative norm,
let `f : R[X]` satisfy `∀ n, ‖f.coeff n‖ ≤ M`, and let `y` be a root with
`‖y‖ ≤ 1`. Then every root `x` satisfying
`M * ‖x - y‖ < ‖f.derivative.eval y‖` equals `y`. The criterion
[`Polynomial.eq_of_eval_eq_zero_of_mul_norm_sub_lt_norm_derivative`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/RootUniqueness.lean)
requires neither division nor completeness, and does not assume `‖x‖ ≤ 1`:
the derivative bound and the strict inequality imply that bound. The local norm
scaling identity forces `‖x - y‖ = 0`, and separation gives equality.
The coefficient bound is arbitrary; it need not be one.

The [3-adic Newton example](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStabilityTest/NewtonNaturality.lean)
for `X² - 4` at `1` uses this criterion to identify every source root in the
strict radius-one ball with `-2`. The same example retains convergence under
the embedding into the 3-adic complex field and uniqueness among all target
roots in the target ball; the other root `2` lies on the excluded boundary.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results) of [FormalFrontier/polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability) at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Polynomial.eq_of_eval_eq_zero_of_mul_norm_sub_lt_norm_derivative` (theorem), declared in [PolynomialRootStability/RootUniqueness.lean, line 73](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/RootUniqueness.lean#L73).

Read from the source at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), without running Lean.

## Sources

- [polynomial-root-stability at efade497: README, headline results](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results)
- [Source of `Polynomial.eq_of_eval_eq_zero_of_mul_norm_sub_lt_norm_derivative` in PolynomialRootStability/RootUniqueness.lean](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/RootUniqueness.lean#L73)
