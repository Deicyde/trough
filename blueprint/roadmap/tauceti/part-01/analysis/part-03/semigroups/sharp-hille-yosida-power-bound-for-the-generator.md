---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_pow_le
statement: formalized
proof: formalized
---

# Sharp Hille--Yosida power bound for the generator resolvent

For a C₀-semigroup with
growth bound `(omega, M)` and `lambda > omega`,
`‖R(lambda, generator S) ^ n‖ ≤ M / (lambda - omega) ^ n`.

This is the necessity estimate in exactly the form consumed by the Hille--Yosida generation
theorem.

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_pow_le.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
  (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) {omega M : ℝ}
  (hb : S.HasGrowthBound omega M) {lambda : ℝ} (hlambda : omega < lambda) (n : ℕ) :
  ‖S.generator.resolvent lambda ^ n‖ ≤ M / (lambda - omega) ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hille–Yosida resolvent bound](hille-yosida-resolvent-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_pow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/PowerBounds.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_pow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_pow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/Resolvent/PowerBounds.html#TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_pow_le)
- [Source of `TauCeti.Semigroups.StronglyContinuousSemigroup.norm_generator_resolvent_pow_le` in TauCeti/Analysis/Semigroups/Resolvent/PowerBounds.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Semigroups/Resolvent/PowerBounds.lean#L277)
