---
declaration: theorem
origin: cited
lean: IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm, TauCeti.CircleSobolev.exists_norm_inclusion_le
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

## Other forms

**Ehrling's inequality on the circle.** Formalized in Tau Ceti as [`TauCeti.CircleSobolev.exists_norm_inclusion_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.exists_norm_inclusion_le).

```lean
TauCeti.CircleSobolev.exists_norm_inclusion_le.{u_1} {s t : ℝ} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {r : ℝ} (hrt : r ≤ t) (hts : t < s) {ε : ℝ} (hε : 0 < ε) :
  ∃ C,
    0 ≤ C ∧
      ∀ (a : TauCeti.CircleSobolev s E),
        ‖(TauCeti.CircleSobolev.inclusion ⋯) a‖ ≤
          ε * ‖a‖ + C * ‖(TauCeti.CircleSobolev.inclusion ⋯) a‖
```

## Sources

- [Tau Ceti documentation: `IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Compact/Ehrling.html#IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm)
- [Source of `IsCompactOperator.exists_norm_le_mul_norm_add_mul_norm` in TauCeti/Analysis/Normed/Operator/Compact/Ehrling.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Compact/Ehrling.lean#L66)
