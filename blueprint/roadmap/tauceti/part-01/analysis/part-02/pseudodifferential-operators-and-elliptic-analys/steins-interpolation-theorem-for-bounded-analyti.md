---
declaration: theorem
origin: cited
lean: TauCeti.CompatibleCouple.ComplexMethodSpace.norm_analyticFamilyMap_le
statement: formalized
proof: formalized
---

# Stein's interpolation theorem for bounded analytic families

If the boundary operators of a
bounded analytic family `T` satisfy `‖T₀ t x‖ ≤ M₀ ‖x‖` and `‖T₁ t x‖ ≤ M₁ ‖x‖` with
`M₀, M₁ ≥ 0`, then `T θ` maps `[X₀, X₁]_θ` to `[Y₀, Y₁]_θ` with
`‖T θ u‖_θ ≤ M₀ ^ (1 - θ) * M₁ ^ θ * ‖u‖_θ` for `0 ≤ θ ≤ 1`.

```lean
TauCeti.CompatibleCouple.ComplexMethodSpace.norm_analyticFamilyMap_le.{u_1, u_2, u_3, u_4, u_5, u_6}
  {X₀ : Type u_1} {X₁ : Type u_2} {V : Type u_3} [NormedAddCommGroup X₀] [NormedSpace ℂ X₀]
  [NormedAddCommGroup X₁] [NormedSpace ℂ X₁] [AddCommGroup V] [_root_.Module ℂ V]
  [TopologicalSpace V] [ContinuousAdd V] [T1Space V] {C : TauCeti.CompatibleCouple ℂ X₀ X₁ V}
  {Y₀ : Type u_4} {Y₁ : Type u_5} {W : Type u_6} [NormedAddCommGroup Y₀] [NormedSpace ℂ Y₀]
  [NormedAddCommGroup Y₁] [NormedSpace ℂ Y₁] [AddCommGroup W] [_root_.Module ℂ W]
  [TopologicalSpace W] [ContinuousAdd W] [T1Space W] {D : TauCeti.CompatibleCouple ℂ Y₀ Y₁ W}
  {θ : ℝ} {T : ℂ → C.SumSpace →L[ℂ] D.SumSpace} {T₀ : ℝ → X₀ →L[ℂ] Y₀} {T₁ : ℝ → X₁ →L[ℂ] Y₁}
  (hT : TauCeti.CompatibleCouple.IsBoundedAnalyticFamily T T₀ T₁) (hθ : θ ∈ Set.Icc 0 1) {M₀ M₁ : ℝ}
  (hM₀ : 0 ≤ M₀) (hM₁ : 0 ≤ M₁) (h₀ : ∀ (t : ℝ) (x : X₀), ‖(T₀ t) x‖ ≤ M₀ * ‖x‖)
  (h₁ : ∀ (t : ℝ) (x : X₁), ‖(T₁ t) x‖ ≤ M₁ * ‖x‖) (u : C.ComplexMethodSpace θ) :
  ‖(TauCeti.CompatibleCouple.ComplexMethodSpace.analyticFamilyMap θ hT) u‖ ≤
    M₀ ^ (1 - θ) * M₁ ^ θ * ‖u‖
```

## Depends on

- [TauCeti.CompatibleCouple.ComplexMethodSpace](tauceti-compatiblecouple-complexmethodspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CompatibleCouple.ComplexMethodSpace.norm_analyticFamilyMap_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/ComplexMethod/Basic.html#TauCeti.CompatibleCouple.ComplexMethodSpace.norm_analyticFamilyMap_le).

## Sources

- [Tau Ceti documentation: `TauCeti.CompatibleCouple.ComplexMethodSpace.norm_analyticFamilyMap_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/ComplexMethod/Basic.html#TauCeti.CompatibleCouple.ComplexMethodSpace.norm_analyticFamilyMap_le)
- [Source of `TauCeti.CompatibleCouple.ComplexMethodSpace.norm_analyticFamilyMap_le` in TauCeti/Analysis/Normed/Interpolation/ComplexMethod/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Interpolation/ComplexMethod/Basic.lean#L994)
