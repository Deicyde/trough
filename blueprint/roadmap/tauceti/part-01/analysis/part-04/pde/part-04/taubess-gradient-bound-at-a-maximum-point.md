---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.norm_sq_le_of_isLocalMax, TauCeti.SeibergWitten.norm_sq_add_mul_norm_sq_le
statement: formalized
proof: formalized
---

# Taubes's gradient bound at a maximum point

Suppose that at a point `x₀` the functions
`|α|²` and `x = |∇_a α|²` are `C²` and satisfy the projected Weitzenböck inequality
`-Δ|α|² / 2 + |∇_a α|² - (r / 4)(1 - |α|²)|α|² ≤ K₁` and the bound
`-K₂ r (|∇_a α|² + 1) ≤ Δ|∇_a α|² / 2`. If `x₀` is a local maximum of
`|∇_a α|² + (K₂ + 1) r |α|²` where `(K₂ + 1) r (1 - |α|²) ≤ |∇_a α|²`, the gradient is bounded
independently of `r`: `|∇_a α(x₀)|² ≤ 4 (K₁ + K₂ + K₁ K₂) / 3`.

```lean
TauCeti.SeibergWitten.norm_sq_le_of_isLocalMax.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : Type u_4} {F : Type u_5}
  [NormedAddCommGroup A] [NormedAddCommGroup F] {α : M → A} {Dα : M → F} {r K₁ K₂ : ℝ} (hr : 0 < r)
  (hK₂ : 0 ≤ K₂) {x₀ : M} (hα : ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 2 (fun y => ‖α y‖ ^ 2) x₀)
  (hDα : ContMDiffAt I (modelWithCornersSelf ℝ ℝ) 2 (fun y => ‖Dα y‖ ^ 2) x₀)
  (hW :
    -(TauCeti.Manifold.laplaceBeltrami I (fun y => ‖α y‖ ^ 2) x₀ / 2) + ‖Dα x₀‖ ^ 2 -
        r / 4 * (1 - ‖α x₀‖ ^ 2) * ‖α x₀‖ ^ 2 ≤
      K₁)
  (hB :
    -(K₂ * r * (‖Dα x₀‖ ^ 2 + 1)) ≤ TauCeti.Manifold.laplaceBeltrami I (fun y => ‖Dα y‖ ^ 2) x₀ / 2)
  (hmax : IsLocalMax (fun y => ‖Dα y‖ ^ 2 + (K₂ + 1) * r * ‖α y‖ ^ 2) x₀)
  (hf : (K₂ + 1) * r * (1 - ‖α x₀‖ ^ 2) ≤ ‖Dα x₀‖ ^ 2) : ‖Dα x₀‖ ^ 2 ≤ 4 / 3 * (K₁ + K₂ + K₁ * K₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fermat's theorem on a manifold](../../../../geometry/part-01/morse-functions-sublevel-topology-and-morse-bott/part-01/fermats-theorem-on-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_le_of_isLocalMax`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/GradientBound.html#TauCeti.SeibergWitten.norm_sq_le_of_isLocalMax).

## Other forms

**Taubes's gradient bound `|∇_a α|² + r |∇β|² ≤ C' r w₊ + C'`.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.norm_sq_add_mul_norm_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/GradientBound.html#TauCeti.SeibergWitten.norm_sq_add_mul_norm_sq_le).

```lean
TauCeti.SeibergWitten.norm_sq_add_mul_norm_sq_le.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8, u_9}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] [CompactSpace M] {A : M → Type u_4}
  {B : M → Type u_5} {F₁ : M → Type u_6} {F₂ : M → Type u_7} {S₁ : M → Type u_8} {S₂ : M → Type u_9}
  [(x : M) → NormedAddCommGroup (A x)] [(x : M) → NormedAddCommGroup (B x)]
  [(x : M) → NormedAddCommGroup (F₁ x)] [(x : M) → NormedAddCommGroup (F₂ x)]
  [(x : M) → NormedAddCommGroup (S₁ x)] [(x : M) → NormedAddCommGroup (S₂ x)] {α : (x : M) → A x}
  {β : (x : M) → B x} {Dα : (x : M) → F₁ x} {Dβ : (x : M) → F₂ x} {D2α : (x : M) → S₁ x}
  {D2β : (x : M) → S₂ x} {c C r : ℝ} (hc : 0 ≤ c) (hr : 1 ≤ r)
  (hα₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖α x‖ ^ 2)
  (hβ₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖β x‖ ^ 2)
  (hDα₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖Dα x‖ ^ 2)
  (hDβ₂ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖Dβ x‖ ^ 2)
  (hWα :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖α x‖ ^ 2) x / 2 + ‖Dα x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 - 1) * ‖α x‖ ^ 2 ≤
        c * ‖α x‖ * (‖Dβ x‖ + ‖α x‖ + ‖β x‖))
  (hWβ :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖β x‖ ^ 2) x / 2 + ‖Dβ x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 + 1) * ‖β x‖ ^ 2 ≤
        c * ‖β x‖ * (‖Dα x‖ + ‖α x‖ + ‖β x‖))
  (hDα :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖Dα x‖ ^ 2) x / 2 + ‖D2α x‖ ^ 2 ≤
        c *
          (r * (‖Dα x‖ ^ 2 + ‖Dα x‖ * ‖Dβ x‖ + ‖Dα x‖) + (‖D2β x‖ + ‖Dα x‖ + ‖Dβ x‖ + 1) * ‖Dα x‖))
  (hDβ :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun x => ‖Dβ x‖ ^ 2) x / 2 + ‖D2β x‖ ^ 2 ≤
        c *
          (r * (‖Dβ x‖ ^ 2 + ‖β x‖ * (‖Dα x‖ + ‖Dβ x‖ + 1) * ‖Dβ x‖) +
            (‖D2α x‖ + ‖Dα x‖ + ‖Dβ x‖ + 1) * ‖Dβ x‖))
  (hs : ∀ (x : M), ‖α x‖ ^ 2 + ‖β x‖ ^ 2 ≤ 1 + C / r)
  (ht : ∀ (x : M), ‖β x‖ ^ 2 ≤ C / r * max (1 - ‖α x‖ ^ 2) 0 + C / r ^ 2) (x : M) :
  ‖Dα x‖ ^ 2 + r * ‖Dβ x‖ ^ 2 ≤
    150 * (1 + c + C) ^ 5 * r * max (1 - ‖α x‖ ^ 2) 0 + 150 * (1 + c + C) ^ 5
```

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.norm_sq_le_of_isLocalMax`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/GradientBound.html#TauCeti.SeibergWitten.norm_sq_le_of_isLocalMax)
- [Source of `TauCeti.SeibergWitten.norm_sq_le_of_isLocalMax` in TauCeti/Analysis/PDE/SeibergWitten/GradientBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/GradientBound.lean#L173)
