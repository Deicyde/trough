---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le
statement: formalized
proof: formalized
---

# The Hille--Yosida power bounds at a complex spectral parameter

on the half-plane of a
growth bound `(omega, M)`, `‖R(lambda, A)ⁿ‖ ≤ M / (re lambda - omega)ⁿ` for every `n`.

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℂ X] [CompleteSpace X] {omega M : ℝ}
  {lambda : ℂ} (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) (hS : S.IsComplexLinear)
  (hb : S.HasGrowthBound omega M) (hlambda : omega < lambda.re) (n : ℕ) :
  ‖(S.complexGenerator hS).resolvent lambda ^ n‖ ≤ M / (lambda.re - omega) ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hille–Yosida resolvent bound](hille-yosida-resolvent-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Complex.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Complex.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le)
- [Source of `TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_pow_le` in TauCeti/Analysis/Semigroups/Resolvent/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Resolvent/Complex.lean#L164)
