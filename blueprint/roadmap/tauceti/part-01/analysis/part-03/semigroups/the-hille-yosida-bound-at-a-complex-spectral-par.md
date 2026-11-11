---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le
statement: formalized
proof: formalized
---

# The Hille--Yosida bound at a complex spectral parameter

on the half-plane of a growth
bound `(omega, M)`, `‖R(lambda, A)‖ ≤ M / (re lambda - omega)`.

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℂ X] [CompleteSpace X] {omega M : ℝ}
  {lambda : ℂ} (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) (hS : S.IsComplexLinear)
  (hb : S.HasGrowthBound omega M) (hlambda : omega < lambda.re) :
  ‖(S.complexGenerator hS).resolvent lambda‖ ≤ M / (lambda.re - omega)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hille–Yosida resolvent bound](hille-yosida-resolvent-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Complex.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Complex.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le)
- [Source of `TauCeti.Semigroups.StronglyContinuousSemigroup.norm_resolvent_complexGenerator_le` in TauCeti/Analysis/Semigroups/Resolvent/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Semigroups/Resolvent/Complex.lean#L153)
