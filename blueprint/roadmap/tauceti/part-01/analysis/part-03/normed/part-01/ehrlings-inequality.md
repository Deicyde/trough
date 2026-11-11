---
declaration: theorem
origin: cited
lean: IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm
statement: formalized
proof: formalized
---

# Ehrling's inequality

If `i : X → Y` is a compact operator and `j : Y → Z` is an injective
continuous linear map, then for every `ε > 0` there is `C ≥ 0` with
`‖i x‖ ≤ ε * ‖x‖ + C * ‖j (i x)‖` for all `x`.

```lean
IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  {X : Type u_2} {Y : Type u_3} {Z : Type u_4} [NontriviallyNormedField 𝕜]
  [SeminormedAddCommGroup X] [NormedSpace 𝕜 X] [SeminormedAddCommGroup Y] [NormedSpace 𝕜 Y]
  [NormedAddCommGroup Z] [NormedSpace 𝕜 Z] {i : X →ₗ[𝕜] Y} {j : Y →L[𝕜] Z}
  (hi : IsCompactOperator ⇑i) (hj : Function.Injective ⇑j) {ε : ℝ} (hε : 0 < ε) :
  ∃ C, 0 ≤ C ∧ ∀ (x : X), ‖i x‖ ≤ ε * ‖x‖ + C * ‖j (i x)‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Ehrling.html#IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm).

## Sources

- [Tau Ceti documentation: `IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Ehrling.html#IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm)
- [Source of `IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm` in TauCeti/Analysis/Normed/Operator/Compact/Ehrling.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/Compact/Ehrling.lean#L66)
