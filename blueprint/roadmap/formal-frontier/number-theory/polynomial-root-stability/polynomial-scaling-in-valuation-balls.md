---
declaration: theorem
origin: cited
lean: Valuation.map_eval_sub_eq_of_mul_map_sub_lt_map_derivative
statement: formalized
proof: formalized
---

# Polynomial scaling in valuation balls

Let `R : Type u` be a commutative ring and `Γ₀ : Type w` a
`LinearOrderedCommMonoidWithZero`, with independent universes, and let `v : Valuation R Γ₀`.
For `f : R[X]`, `M : Γ₀` and `a : R`, assume `∀ n > 0, v (f.coeff n) ≤ M` and `v a ≤ 1`; the constant coefficient is unrestricted.
Set `D = v (f.derivative.eval a)` and `B = {b | M * v (b - a) < D}`.
[`Valuation.map_eval_sub_eq_of_mul_map_sub_lt_map_derivative`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Valuation.lean) gives
`v (f.eval b - f.eval a) = D * v (b - a)` for `b ∈ B`, and
[`Valuation.map_derivative_eval_eq_of_mul_map_sub_lt_map_derivative`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Valuation.lean)
gives `v (f.derivative.eval b) = D` there. For `b, c ∈ B`,
[`Valuation.map_eval_sub_eval_eq_of_mul_map_sub_lt_map_derivative`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Valuation.lean)
gives `v (f.eval c - f.eval b) = D * v (c - b)`.
Only [`Valuation.injOn_eval_of_mul_map_sub_lt_map_derivative`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Valuation.lean)
additionally assumes `v.supp = ⊥` to conclude `Set.InjOn` on `B`; value-zero displacement alone need not identify points.
These estimates need no root, domain, field, Henselianity, completeness, rank-one or real-valued realization,
normalization, uniformizer, value-one derivative or separate `0 < M` assumption. Value inverses are not required;
multiplication in `Γ₀` by positive elements is strict and cancellative. No arbitrary-rank root-existence theorem is asserted.
The estimates reuse Mathlib's valuation, Taylor and geometric-sum APIs.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results) of [FormalFrontier/polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability) at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Valuation.map_eval_sub_eq_of_mul_map_sub_lt_map_derivative` (theorem), declared in [PolynomialRootStability/Valuation.lean, line 163](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Valuation.lean#L163).

Read from the source at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), without running Lean.

## Sources

- [polynomial-root-stability at efade497: README, headline results](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results)
- [Source of `Valuation.map_eval_sub_eq_of_mul_map_sub_lt_map_derivative` in PolynomialRootStability/Valuation.lean](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Valuation.lean#L163)
