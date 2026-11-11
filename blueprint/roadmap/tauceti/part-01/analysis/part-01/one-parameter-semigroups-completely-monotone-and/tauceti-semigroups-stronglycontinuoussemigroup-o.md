---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded_resolvent_eq_inv_smul_tsum_pow
statement: formalized
proof: formalized
---

# TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded_resolvent_eq_inv_smul_tsum_pow

For `λ > ‖A‖`, the Laplace-transform resolvent of `t ↦ exp (tA)` is the Neumann series
`λ⁻¹ ∑' n, (λ⁻¹ A)ⁿ`.

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded_resolvent_eq_inv_smul_tsum_pow.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (A : X →L[ℝ] X)
  {lambda : ℝ} (hlambda : ‖A‖ < lambda) :
  (TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded A).resolvent ⋯ lambda hlambda =
    lambda⁻¹ • ∑' (n : ℕ), (lambda⁻¹ • A) ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded_resolvent_eq_inv_smul_tsum_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/BoundedGenerator/Resolvent.html#TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded_resolvent_eq_inv_smul_tsum_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded_resolvent_eq_inv_smul_tsum_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/BoundedGenerator/Resolvent.html#TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded_resolvent_eq_inv_smul_tsum_pow)
- [Source of `TauCeti.Semigroups.StronglyContinuousSemigroup.ofBounded_resolvent_eq_inv_smul_tsum_pow` in TauCeti/Analysis/Semigroups/BoundedGenerator/Resolvent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Semigroups/BoundedGenerator/Resolvent.lean#L68)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OneParameterSemigroups/STATUS.md)
