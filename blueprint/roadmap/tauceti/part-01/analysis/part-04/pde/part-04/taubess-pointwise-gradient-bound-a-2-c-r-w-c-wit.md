---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.norm_sq_le_mul_max_one_sub_add
statement: formalized
proof: formalized
---

# Taubes's pointwise gradient bound `|∇_a α|² ≤ C r w₊ + C`, with `w₊ = max (1 - |α|²) 0`

On a compact boundaryless Riemannian manifold, suppose `|α|²` and `|∇_a α|²` are `C²` and satisfy
the projected Weitzenböck inequality
`-Δ|α|² / 2 + |∇_a α|² - (r / 4)(1 - |α|²)|α|² ≤ K₁`, the bound
`-K₂ r (|∇_a α|² + 1) ≤ Δ|∇_a α|² / 2` and the coarse bound `|α|² ≤ 1 + K₃ / r`. Then everywhere

`|∇_a α|² ≤ (K₂ + 1) r w₊ + 4 (K₁ + K₂ + K₁ K₂) / 3 + (K₂ + 1) K₃`.

```lean
TauCeti.SeibergWitten.norm_sq_le_mul_max_one_sub_add.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : Type u_4} {F : Type u_5}
  [NormedAddCommGroup A] [NormedAddCommGroup F] {α : M → A} {Dα : M → F} {r K₁ K₂ : ℝ}
  [CompactSpace M] {K₃ : ℝ} (hr : 0 < r) (hK₁ : 0 ≤ K₁) (hK₂ : 0 ≤ K₂) (hK₃ : 0 ≤ K₃)
  (hα : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun y => ‖α y‖ ^ 2)
  (hDα : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun y => ‖Dα y‖ ^ 2)
  (hW :
    ∀ (y : M),
      -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖α y‖ ^ 2) y / 2) + ‖Dα y‖ ^ 2 -
          r / 4 * (1 - ‖α y‖ ^ 2) * ‖α y‖ ^ 2 ≤
        K₁)
  (hB :
    ∀ (y : M),
      -(K₂ * r * (‖Dα y‖ ^ 2 + 1)) ≤ TauCeti.Manifold.laplaceBeltrami I (fun y => ‖Dα y‖ ^ 2) y / 2)
  (hC : ∀ (y : M), ‖α y‖ ^ 2 ≤ 1 + K₃ / r) (y : M) :
  ‖Dα y‖ ^ 2 ≤ (K₂ + 1) * r * max (1 - ‖α y‖ ^ 2) 0 + (4 / 3 * (K₁ + K₂ + K₁ * K₂) + (K₂ + 1) * K₃)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taubes's gradient bound at a maximum point](taubess-gradient-bound-at-a-maximum-point.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_mul_max_one_sub_add`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/GradientBound.html#TauCeti.SeibergWitten.norm_sq_le_mul_max_one_sub_add).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.norm_sq_le_mul_max_one_sub_add`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/GradientBound.html#TauCeti.SeibergWitten.norm_sq_le_mul_max_one_sub_add)
- [Source of `TauCeti.SeibergWitten.norm_sq_le_mul_max_one_sub_add` in TauCeti/Analysis/PDE/SeibergWitten/GradientBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/GradientBound.lean#L192)
