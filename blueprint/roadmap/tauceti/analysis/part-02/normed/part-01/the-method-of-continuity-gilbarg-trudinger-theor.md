---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.surjective_iff_of_forall_norm_le_lineMap
statement: formalized
proof: formalized
---

# The method of continuity (Gilbarg–Trudinger, Theorem 5.2)

Let `E` be a Banach space and
`L₀, L₁ : E →L[𝕜] F`. If the operators `L t = (1 - t) L₀ + t L₁` satisfy the a priori estimate
`‖x‖ ≤ C * ‖L t x‖` for every `t ∈ [0, 1]`, then `L₀` is surjective if and only if `L₁` is.

```lean
ContinuousLinearMap.surjective_iff_of_forall_norm_le_lineMap.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] [NormedAddCommGroup F] [NormedSpace 𝕜 F] {C : ℝ} [NormedSpace ℝ F]
  [SMulCommClass 𝕜 ℝ F] {L₀ L₁ : E →L[𝕜] F}
  (hC : ∀ t ∈ Set.Icc 0 1, ∀ (x : E), ‖x‖ ≤ C * ‖((AffineMap.lineMap L₀ L₁) t) x‖) :
  Function.Surjective ⇑L₀ ↔ Function.Surjective ⇑L₁
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.surjective_iff_of_forall_norm_le_lineMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/MethodOfContinuity.html#ContinuousLinearMap.surjective_iff_of_forall_norm_le_lineMap).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.surjective_iff_of_forall_norm_le_lineMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/MethodOfContinuity.html#ContinuousLinearMap.surjective_iff_of_forall_norm_le_lineMap)
- [Source of `ContinuousLinearMap.surjective_iff_of_forall_norm_le_lineMap` in TauCeti/Analysis/Normed/Operator/MethodOfContinuity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/MethodOfContinuity.lean#L102)
