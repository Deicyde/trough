---
declaration: theorem
origin: cited
lean: TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le, TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le_of_laplaceBeltrami, TauCeti.SeibergWitten.sqrt_integral_norm_sq_add_sqrt_mul_sqrt_integral_norm_sq_le, TauCeti.SeibergWitten.integral_norm_sq_le_of_norm_le_mul_add_norm, TauCeti.SeibergWitten.sqrt_integral_norm_sq_le_of_norm_le_mul_add_norm
statement: formalized
proof: formalized
---

# Taubes's `L²` bound on `β`

Let `g` be an integrable function of integral zero, standing
for `Δ|β|²`, and suppose the projected Weitzenböck inequality
`-g / 2 + |∇β|² + (r / 4) (|α|² + |β|² + 1) |β|² ≤ c |β| (|∇_a α| + |α| + |β|)` holds almost
everywhere, with `0 < r` and `8 c ≤ r`. Then
`∫ |∇β|² + (r / 16) ∫ |β|² ≤ (8 c² / r) (∫ |∇_a α|² + ∫ |α|²)`. Here `∇_a α` and `∇β` are any
functions `Dα` and `Dβ` satisfying these hypotheses.

```lean
TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le.{u_1, u_2, u_3, u_4, u_5}
  {c r : ℝ} {X : Type u_1} {A : X → Type u_2} {B : X → Type u_3} {F₁ : X → Type u_4}
  {F₂ : X → Type u_5} [MeasurableSpace X] {μ : MeasureTheory.Measure X}
  [(x : X) → SeminormedAddCommGroup (A x)] [(x : X) → SeminormedAddCommGroup (B x)]
  [(x : X) → SeminormedAddCommGroup (F₁ x)] [(x : X) → SeminormedAddCommGroup (F₂ x)]
  {α : (x : X) → A x} {β : (x : X) → B x} {Dα : (x : X) → F₁ x} {Dβ : (x : X) → F₂ x} {g : X → ℝ}
  (hr : 0 < r) (hcr : 8 * c ≤ r) (hg : MeasureTheory.Integrable g μ) (hg0 : ∫ (x : X), g x ∂μ = 0)
  (hα : MeasureTheory.Integrable (fun x => ‖α x‖ ^ 2) μ)
  (hDα : MeasureTheory.Integrable (fun x => ‖Dα x‖ ^ 2) μ)
  (hW :
    ∀ᵐ (x : X) ∂μ,
      -g x / 2 + ‖Dβ x‖ ^ 2 + r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 + 1) * ‖β x‖ ^ 2 ≤
        c * ‖β x‖ * (‖Dα x‖ + ‖α x‖ + ‖β x‖)) :
  ∫ (x : X), ‖Dβ x‖ ^ 2 ∂μ + r / 16 * ∫ (x : X), ‖β x‖ ^ 2 ∂μ ≤
    8 * c ^ 2 / r * (∫ (x : X), ‖Dα x‖ ^ 2 ∂μ + ∫ (x : X), ‖α x‖ ^ 2 ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The divergence theorem on a manifold without boundary](../../../../geometry/part-02/manifold/part-01/the-divergence-theorem-on-a-manifold-without-bou.md)
- [The Koszul formula](../../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.html#TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le).

## Other forms

**Taubes's `L²` bound on `β` on a closed manifold.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le_of_laplaceBeltrami`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.html#TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le_of_laplaceBeltrami).

```lean
TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le_of_laplaceBeltrami.{u_1, u_2,
    u_3, u_4, u_5, u_6, u_7}
  {c r : ℝ} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [CompactSpace M] [IsManifold I (↑⊤) M]
  [MeasurableSpace M] [BorelSpace M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {A : M → Type u_4}
  {B : M → Type u_5} {F₁ : M → Type u_6} {F₂ : M → Type u_7}
  [(x : M) → SeminormedAddCommGroup (A x)] [(x : M) → SeminormedAddCommGroup (B x)]
  [(x : M) → SeminormedAddCommGroup (F₁ x)] [(x : M) → SeminormedAddCommGroup (F₂ x)]
  {α : (x : M) → A x} {β : (x : M) → B x} {Dα : (x : M) → F₁ x} {Dβ : (x : M) → F₂ x} (hr : 0 < r)
  (hcr : 8 * c ≤ r) (hα : Continuous fun x => ‖α x‖ ^ 2)
  (hβ : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 fun x => ‖β x‖ ^ 2)
  (hDα : Continuous fun x => ‖Dα x‖ ^ 2)
  (hW :
    ∀ (x : M),
      -TauCeti.Manifold.laplaceBeltrami I (fun y => ‖β y‖ ^ 2) x / 2 + ‖Dβ x‖ ^ 2 +
          r / 4 * (‖α x‖ ^ 2 + ‖β x‖ ^ 2 + 1) * ‖β x‖ ^ 2 ≤
        c * ‖β x‖ * (‖Dα x‖ + ‖α x‖ + ‖β x‖)) :
  ∫ (x : M), ‖Dβ x‖ ^ 2 ∂TauCeti.riemannianVolume I M +
      r / 16 * ∫ (x : M), ‖β x‖ ^ 2 ∂TauCeti.riemannianVolume I M ≤
    8 * c ^ 2 / r *
      (∫ (x : M), ‖Dα x‖ ^ 2 ∂TauCeti.riemannianVolume I M +
        ∫ (x : M), ‖α x‖ ^ 2 ∂TauCeti.riemannianVolume I M)
```

**Taubes's `L²` bound on `β`, in norm form.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.sqrt_integral_norm_sq_add_sqrt_mul_sqrt_integral_norm_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.html#TauCeti.SeibergWitten.sqrt_integral_norm_sq_add_sqrt_mul_sqrt_integral_norm_sq_le).

```lean
TauCeti.SeibergWitten.sqrt_integral_norm_sq_add_sqrt_mul_sqrt_integral_norm_sq_le.{u_1, u_2, u_3,
    u_4, u_5}
  {c r : ℝ} {X : Type u_1} {A : X → Type u_2} {B : X → Type u_3} {F₁ : X → Type u_4}
  {F₂ : X → Type u_5} [MeasurableSpace X] {μ : MeasureTheory.Measure X}
  [(x : X) → SeminormedAddCommGroup (A x)] [(x : X) → SeminormedAddCommGroup (B x)]
  [(x : X) → SeminormedAddCommGroup (F₁ x)] [(x : X) → SeminormedAddCommGroup (F₂ x)]
  {α : (x : X) → A x} {β : (x : X) → B x} {Dα : (x : X) → F₁ x} {Dβ : (x : X) → F₂ x} (hr : 0 < r)
  (hc : 0 ≤ c)
  (hbound :
    ∫ (x : X), ‖Dβ x‖ ^ 2 ∂μ + r / 16 * ∫ (x : X), ‖β x‖ ^ 2 ∂μ ≤
      8 * c ^ 2 / r * (∫ (x : X), ‖Dα x‖ ^ 2 ∂μ + ∫ (x : X), ‖α x‖ ^ 2 ∂μ)) :
  √(∫ (x : X), ‖Dβ x‖ ^ 2 ∂μ) + √r * √(∫ (x : X), ‖β x‖ ^ 2 ∂μ) ≤
    16 * c / √r * (√(∫ (x : X), ‖Dα x‖ ^ 2 ∂μ) + √(∫ (x : X), ‖α x‖ ^ 2 ∂μ))
```

**Taubes's `L²` bound on `∂bar_a α`.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.integral_norm_sq_le_of_norm_le_mul_add_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.html#TauCeti.SeibergWitten.integral_norm_sq_le_of_norm_le_mul_add_norm).

```lean
TauCeti.SeibergWitten.integral_norm_sq_le_of_norm_le_mul_add_norm.{u_1, u_2, u_3, u_4, u_5, u_6,
    u_7}
  {c r : ℝ} {X : Type u_1} {A : X → Type u_2} {B : X → Type u_3} {F₁ : X → Type u_4}
  {F₂ : X → Type u_5} {F₃ : X → Type u_6} {F₄ : X → Type u_7} [MeasurableSpace X]
  {μ : MeasureTheory.Measure X} [(x : X) → SeminormedAddCommGroup (A x)]
  [(x : X) → SeminormedAddCommGroup (B x)] [(x : X) → SeminormedAddCommGroup (F₁ x)]
  [(x : X) → SeminormedAddCommGroup (F₂ x)] [(x : X) → SeminormedAddCommGroup (F₃ x)]
  [(x : X) → SeminormedAddCommGroup (F₄ x)] {α : (x : X) → A x} {β : (x : X) → B x}
  {Dα : (x : X) → F₁ x} {Dβ : (x : X) → F₂ x} {Dα' : (x : X) → F₃ x} {Dbar : (x : X) → F₄ x}
  (hr16 : 16 ≤ r) (hcr : 64 * c ^ 4 ≤ r) (hβ : MeasureTheory.Integrable (fun x => ‖β x‖ ^ 2) μ)
  (hDβ : MeasureTheory.Integrable (fun x => ‖Dβ x‖ ^ 2) μ)
  (hDα' : MeasureTheory.Integrable (fun x => ‖Dα' x‖ ^ 2) μ)
  (hbound :
    ∫ (x : X), ‖Dβ x‖ ^ 2 ∂μ + r / 16 * ∫ (x : X), ‖β x‖ ^ 2 ∂μ ≤
      8 * c ^ 2 / r * (∫ (x : X), ‖Dα x‖ ^ 2 ∂μ + ∫ (x : X), ‖α x‖ ^ 2 ∂μ))
  (hsplit : ∀ᵐ (x : X) ∂μ, ‖Dα x‖ ≤ ‖Dα' x‖ + ‖Dbar x‖)
  (hdirac : ∀ᵐ (x : X) ∂μ, ‖Dbar x‖ ≤ c * (‖Dβ x‖ + ‖β x‖)) :
  ∫ (x : X), ‖Dbar x‖ ^ 2 ∂μ ≤
    64 * c ^ 4 / r * (∫ (x : X), ‖Dα' x‖ ^ 2 ∂μ + ∫ (x : X), ‖α x‖ ^ 2 ∂μ)
```

**Taubes's `L²` bound on `∂bar_a α`, in norm form.** Formalized in Tau Ceti as [`TauCeti.SeibergWitten.sqrt_integral_norm_sq_le_of_norm_le_mul_add_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.html#TauCeti.SeibergWitten.sqrt_integral_norm_sq_le_of_norm_le_mul_add_norm).

```lean
TauCeti.SeibergWitten.sqrt_integral_norm_sq_le_of_norm_le_mul_add_norm.{u_1, u_2, u_3, u_4, u_5,
    u_6, u_7}
  {c r : ℝ} {X : Type u_1} {A : X → Type u_2} {B : X → Type u_3} {F₁ : X → Type u_4}
  {F₂ : X → Type u_5} {F₃ : X → Type u_6} {F₄ : X → Type u_7} [MeasurableSpace X]
  {μ : MeasureTheory.Measure X} [(x : X) → SeminormedAddCommGroup (A x)]
  [(x : X) → SeminormedAddCommGroup (B x)] [(x : X) → SeminormedAddCommGroup (F₁ x)]
  [(x : X) → SeminormedAddCommGroup (F₂ x)] [(x : X) → SeminormedAddCommGroup (F₃ x)]
  [(x : X) → SeminormedAddCommGroup (F₄ x)] {α : (x : X) → A x} {β : (x : X) → B x}
  {Dα : (x : X) → F₁ x} {Dβ : (x : X) → F₂ x} {Dα' : (x : X) → F₃ x} {Dbar : (x : X) → F₄ x}
  (hr16 : 16 ≤ r) (hcr : 64 * c ^ 4 ≤ r) (hβ : MeasureTheory.Integrable (fun x => ‖β x‖ ^ 2) μ)
  (hDβ : MeasureTheory.Integrable (fun x => ‖Dβ x‖ ^ 2) μ)
  (hDα' : MeasureTheory.Integrable (fun x => ‖Dα' x‖ ^ 2) μ)
  (hbound :
    ∫ (x : X), ‖Dβ x‖ ^ 2 ∂μ + r / 16 * ∫ (x : X), ‖β x‖ ^ 2 ∂μ ≤
      8 * c ^ 2 / r * (∫ (x : X), ‖Dα x‖ ^ 2 ∂μ + ∫ (x : X), ‖α x‖ ^ 2 ∂μ))
  (hsplit : ∀ᵐ (x : X) ∂μ, ‖Dα x‖ ≤ ‖Dα' x‖ + ‖Dbar x‖)
  (hdirac : ∀ᵐ (x : X) ∂μ, ‖Dbar x‖ ≤ c * (‖Dβ x‖ + ‖β x‖)) :
  √(∫ (x : X), ‖Dbar x‖ ^ 2 ∂μ) ≤
    8 * c ^ 2 / √r * (√(∫ (x : X), ‖Dα' x‖ ^ 2 ∂μ) + √(∫ (x : X), ‖α x‖ ^ 2 ∂μ))
```

## Sources

- [Tau Ceti documentation: `TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.html#TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le)
- [Source of `TauCeti.SeibergWitten.integral_norm_sq_add_mul_integral_norm_sq_le` in TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/SeibergWitten/L2Bounds.lean#L117)
