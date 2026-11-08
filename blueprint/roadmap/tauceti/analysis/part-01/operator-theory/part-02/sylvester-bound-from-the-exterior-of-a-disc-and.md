---
declaration: theorem
origin: cited
lean: TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_le_norm_sub_smul_of_norm_sub_smul_le
statement: formalized
proof: formalized
---

# Sylvester bound from the exterior of a disc and a smaller disc

If
`(r + δ) ‖x‖ ≤ ‖A x - c x‖` for every `x` and `‖B y - c y‖ ≤ r ‖y‖` for every `y`, then
`δ N(X) ≤ N(A X - X B)` for every unitarily invariant seminorm `N`.

```lean
TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_le_norm_sub_smul_of_norm_sub_smul_le.{u_1,
    u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F]
  [FiniteDimensional 𝕜 F] {A : E →L[𝕜] E} {B : F →L[𝕜] F} {c : 𝕜} {r δ : ℝ}
  (N : TauCeti.UnitarilyInvariantSeminorm 𝕜 F E) (hA : ∀ (x : E), (r + δ) * ‖x‖ ≤ ‖A x - c • x‖)
  (hB : ∀ (y : F), ‖B y - c • y‖ ≤ r * ‖y‖) (X : F →L[𝕜] E) : δ * N ↑X ≤ N ↑((A.sylvester B) X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fan dominance](../part-01/fan-dominance.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_le_norm_sub_smul_of_norm_sub_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_le_norm_sub_smul_of_norm_sub_smul_le).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_le_norm_sub_smul_of_norm_sub_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.html#TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_le_norm_sub_smul_of_norm_sub_smul_le)
- [Source of `TauCeti.UnitarilyInvariantSeminorm.mul_map_le_map_sylvester_apply_of_le_norm_sub_smul_of_norm_sub_smul_le` in TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/UnitarilyInvariantSeminorm/Sylvester/Basic.lean#L192)
