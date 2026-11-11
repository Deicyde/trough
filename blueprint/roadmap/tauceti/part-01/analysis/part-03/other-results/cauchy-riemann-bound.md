---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.norm_le_of_apply_I_eq
statement: formalized
proof: formalized
---

# Cauchy--Riemann bound

If a real-linear map `f : K → V` out of an `RCLike` field satisfies
`f I = L (f 1)` with `‖L‖ ≤ M`, and `‖f 1‖ ≤ B`, then `‖f‖ ≤ (1 + M) * B`.

```lean
ContinuousLinearMap.norm_le_of_apply_I_eq.{u_1, u_2} {K : Type u_1} {V : Type u_2} [RCLike K]
  [SeminormedAddCommGroup V] [NormedSpace ℝ V] (f : K →L[ℝ] V) {L : V →L[ℝ] V} {M B : ℝ}
  (hCR : f RCLike.I = L (f 1)) (hL : ‖L‖ ≤ M) (hreal : ‖f 1‖ ≤ B) : ‖f‖ ≤ (1 + M) * B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.norm_le_of_apply_I_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/RCLike/OperatorNorm.html#ContinuousLinearMap.norm_le_of_apply_I_eq).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.norm_le_of_apply_I_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/RCLike/OperatorNorm.html#ContinuousLinearMap.norm_le_of_apply_I_eq)
- [Source of `ContinuousLinearMap.norm_le_of_apply_I_eq` in TauCeti/Analysis/RCLike/OperatorNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/RCLike/OperatorNorm.lean#L50)
