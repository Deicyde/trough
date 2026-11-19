---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_of_isLocalMax
statement: formalized
proof: formalized
---

# Taubes's `β` bound at a maximum point

Suppose that at a point `x₀` the functions
`|α|²` and `|β|²` are `C²` and satisfy the projected Weitzenböck inequalities
`-Δ|β|² / 2 + (r / 4)(|α|² + |β|² + 1)|β|² ≤ c |β| (|∇_a α| + |α| + |β|)` and
`-Δ|α|² / 2 + |∇_a α|² - (r / 4)(1 - |α|²)|α|² ≤ K₁`, with `0 < r` and `0 ≤ K₁`. If `x₀` is a
local maximum of `|β|² + (4 c² / r) |α|²`, then
`|β(x₀)|² ≤ (4 c² / r) (max (1 - |α(x₀)|²) 0 + 4 (1 + 2 K₁) / r)`.

```lean
TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_of_isLocalMax.{u_1, u_2, u_3, u_4, u_5,
    u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} {F : M → Type u_6} [(x : M) → SeminormedAddCommGroup (A x)]
  [(x : M) → SeminormedAddCommGroup (B x)] [(x : M) → SeminormedAddCommGroup (F x)]
  {α : (x : M) → A x} {β : (x : M) → B x} {Dα : (x : M) → F x} {r c K₁ : ℝ} (hr : 0 < r)
  (hK₁ : 0 ≤ K₁) {x₀ : M} (hα : ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 2 (fun y => ‖α y‖ ^ 2) x₀)
  (hβ : ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 2 (fun y => ‖β y‖ ^ 2) x₀)
  (hWβ :
    -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖β y‖ ^ 2) x₀ / 2) +
        r / 4 * (‖α x₀‖ ^ 2 + ‖β x₀‖ ^ 2 + 1) * ‖β x₀‖ ^ 2 ≤
      c * ‖β x₀‖ * (‖Dα x₀‖ + ‖α x₀‖ + ‖β x₀‖))
  (hWα :
    -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖α y‖ ^ 2) x₀ / 2) + ‖Dα x₀‖ ^ 2 -
        r / 4 * (1 - ‖α x₀‖ ^ 2) * ‖α x₀‖ ^ 2 ≤
      K₁)
  (hmax : IsLocalMax (fun y => ‖β y‖ ^ 2 + 4 * c ^ 2 / r * ‖α y‖ ^ 2) x₀) :
  ‖β x₀‖ ^ 2 ≤ 4 * c ^ 2 / r * (max (1 - ‖α x₀‖ ^ 2) 0 + 4 * (1 + 2 * K₁) / r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fermat's theorem on a manifold](../../../../geometry/part-01/morse-functions-sublevel-topology-and-morse-bott/part-01/fermats-theorem-on-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_of_isLocalMax`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/BetaBound.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_of_isLocalMax).

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_of_isLocalMax`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/BetaBound.html#TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_of_isLocalMax)
- [Source of `TauCeti.SeibergWitten.norm_sq_le_div_mul_max_one_sub_add_div_of_isLocalMax` in TauCeti/Analysis/PDE/SeibergWitten/BetaBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/BetaBound.lean#L295)
