---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral
statement: formalized
proof: formalized
---

# The Duhamel identity for the exponential of a bounded operator

For `B : X →L[ℝ] X`,
`exp (t B) x - x = ∫₀ᵗ exp (u B) (B x) du`.

This is the fundamental theorem of calculus applied to the differentiable orbit
`u ↦ exp (u B) x`, whose derivative is the continuous function `u ↦ exp (u B) (B x)`.

```lean
ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral.{u_1} {X : Type u_1}
  [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] (B : X →L[ℝ] X) (t : ℝ) (x : X) :
  (NormedSpace.exp (t • B)) x - x = ∫ (u : ℝ) in 0..t, (NormedSpace.exp (u • B)) (B x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Exponential.html#ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Exponential.html#ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral)
- [Source of `ContinuousLinearMap.exp_smul_apply_sub_eq_intervalIntegral` in TauCeti/Analysis/Normed/Operator/Exponential.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Exponential.lean#L114)
