---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le, TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_le
statement: formalized
proof: formalized
---

# Hille–Yosida resolvent bound

`‖R λ‖ ≤ M/(λ-ω)` for a C₀ semigroup with
growth bound `(ω, M)` and `λ > ω` (Hille 1948, Yosida 1948; Engel–Nagel Ch. II).

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
  (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) {ω M : ℝ} (hb : S.HasGrowthBound ω M)
  (lambda : ℝ) (hlam : ω < lambda) : ‖S.resolvent hb lambda hlam‖ ≤ M / (lambda - ω)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Basic.html#TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le).

## Other forms

**Hille--Yosida resolvent bound for the resolvent of the generator.** Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Identity.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_le).

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_le.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] (S : TauCeti.Semigroups.StronglyContinuousSemigroup X)
  [CompleteSpace X] {omega M : ℝ} (hb : S.HasGrowthBound omega M) {lambda : ℝ}
  (hlambda : omega < lambda) : ‖S.generator.resolvent lambda‖ ≤ M / (lambda - omega)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/Basic.html#TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le)
- [Source of `TauCeti.Semigroups.StronglyContinuousSemigroup.resolvent_norm_le` in TauCeti/Analysis/Semigroups/Resolvent/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Semigroups/Resolvent/Basic.lean#L299)
