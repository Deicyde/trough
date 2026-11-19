---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_sq, TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div
statement: formalized
proof: formalized
---

# Taubes's pointwise bound

**Taubes's pointwise bound** `|β|² ≤ (C / r) w₊ + C / r²`, with `w₊ = max (1 - |α|²) 0` and
`C = 32 c² (K₁ + 3 K₃ + 2)`. On a compact boundaryless Riemannian manifold, suppose `|α|²` and
`|β|²` are `C²` and satisfy the projected Weitzenböck inequalities
`-Δ|α|² / 2 + |∇_a α|² - (r / 4)(1 - |α|²)|α|² ≤ K₁` and
`-Δ|β|² / 2 + (r / 4)(|α|² + 1)|β|² ≤ c |β| (|∇_a α| + |α| + |β|)`, and the coarse bound
`|α|² + |β|² ≤ 1 + K₃ / r`, with `r ≥ 1`. Then the bound holds everywhere.

```lean
TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_sq.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} {F : M → Type u_6} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (B x)] [(x : M) → SeminormedAddCommGroup (F x)]
  {α : (x : M) → A x} {β : (x : M) → B x} {Dα : (x : M) → F x} {r c K₁ K₃ : ℝ} [CompactSpace M]
  (hr : 1 ≤ r) (hK₁ : 0 ≤ K₁) (hK₃ : 0 ≤ K₃)
  (hα : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun y => ‖α y‖ ^ 2)
  (hβ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun y => ‖β y‖ ^ 2)
  (hWα :
    ∀ (y : M),
      -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖α y‖ ^ 2) y / 2) + ‖Dα y‖ ^ 2 -
          r / 4 * (1 - ‖α y‖ ^ 2) * ‖α y‖ ^ 2 ≤
        K₁)
  (hWβ :
    ∀ (y : M),
      -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖β y‖ ^ 2) y / 2) +
          r / 4 * (‖α y‖ ^ 2 + 1) * ‖β y‖ ^ 2 ≤
        c * ‖β y‖ * (‖Dα y‖ + ‖α y‖ + ‖β y‖))
  (hC : ∀ (y : M), ‖α y‖ ^ 2 + ‖β y‖ ^ 2 ≤ 1 + K₃ / r) (y : M) :
  ‖β y‖ ^ 2 ≤
    32 * c ^ 2 * (K₁ + 3 * K₃ + 2) / r * max (1 - ‖α y‖ ^ 2) 0 +
      32 * c ^ 2 * (K₁ + 3 * K₃ + 2) / r ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taubes's `β` bound at a maximum point](taubess-bound-at-a-maximum-point.md)
- [Taubes's bound on `β`](taubess-bound-on.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/BetaBound.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_sq).

## Other forms

**Taubes's pointwise bound `|β|² ≤ (C / r) w₊ + C / r²`, with `w₊ = max (1 - |α|²) 0`.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/BetaBound.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div).

```lean
TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} {F : M → Type u_6} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (B x)] [(x : M) → SeminormedAddCommGroup (F x)]
  {α : (x : M) → A x} {β : (x : M) → B x} {Dα : (x : M) → F x} {r c K₁ K₃ : ℝ} [CompactSpace M]
  (hr : 0 < r) (hK₁ : 0 ≤ K₁) (hK₃ : 0 ≤ K₃)
  (hα : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun y => ‖α y‖ ^ 2)
  (hβ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun y => ‖β y‖ ^ 2)
  (hWβ :
    ∀ (y : M),
      -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖β y‖ ^ 2) y / 2) +
          r / 4 * (‖α y‖ ^ 2 + ‖β y‖ ^ 2 + 1) * ‖β y‖ ^ 2 ≤
        c * ‖β y‖ * (‖Dα y‖ + ‖α y‖ + ‖β y‖))
  (hWα :
    ∀ (y : M),
      -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖α y‖ ^ 2) y / 2) + ‖Dα y‖ ^ 2 -
          r / 4 * (1 - ‖α y‖ ^ 2) * ‖α y‖ ^ 2 ≤
        K₁)
  (hC : ∀ (y : M), ‖α y‖ ^ 2 ≤ 1 + K₃ / r) (y : M) :
  ‖β y‖ ^ 2 ≤ 4 * c ^ 2 / r * (max (1 - ‖α y‖ ^ 2) 0 + (4 + 8 * K₁ + K₃) / r)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/BetaBound.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_sq)
- [Source of `TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_sq` in TauCeti/Analysis/PDE/SeibergWitten/BetaBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/BetaBound.lean#L249)
