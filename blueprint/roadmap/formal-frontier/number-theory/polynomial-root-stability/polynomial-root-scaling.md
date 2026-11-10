---
declaration: theorem
origin: cited
lean: Polynomial.continuous_eval_scaleRoots
statement: formalized
proof: formalized
---

# Polynomial root scaling

For a fixed polynomial `p : R[X]` over a topological semiring `R`, evaluation
of Mathlib's root-scaling operation is jointly continuous by
[`Polynomial.continuous_eval_scaleRoots`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/ScaleRoots.lean):
`(t, z) ↦ (p.scaleRoots t).eval z`. The polynomial is fixed; no continuity
across changes of degree is asserted, and multiplication need not be commutative.

Over any normed field `K`, suppose `p : K[X]` satisfies
`∀ w, 1 ≤ ‖w‖ → p.eval w ≠ 0`. If `‖t‖ ≤ ‖z‖` and `z ≠ 0`, then
[`Polynomial.scaleRoots_eval_ne_zero_of_norm_le`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/ScaleRoots.lean)
gives `(p.scaleRoots t).eval z ≠ 0`. In particular this applies when `‖t‖ ≤ 1`
and `‖z‖ = 1`. The outside condition holds for `X` over every normed field
and for `X - C (1/2)` over `ℂ`; it implies `p ≠ 0` by evaluation at `1`.
At parameter zero the scaled polynomial is `p.leadingCoeff • X ^ p.natDegree`,
so nonzero constants are included without a positive-degree hypothesis.
No completeness, algebraic-closure or nontrivial-norm assumption is needed.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results) of [FormalFrontier/polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability) at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Polynomial.continuous_eval_scaleRoots` (theorem), declared in [PolynomialRootStability/ScaleRoots.lean, line 47](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/ScaleRoots.lean#L47).

Read from the source at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), without running Lean.

## Sources

- [polynomial-root-stability at efade497: README, headline results](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results)
- [Source of `Polynomial.continuous_eval_scaleRoots` in PolynomialRootStability/ScaleRoots.lean](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/ScaleRoots.lean#L47)
