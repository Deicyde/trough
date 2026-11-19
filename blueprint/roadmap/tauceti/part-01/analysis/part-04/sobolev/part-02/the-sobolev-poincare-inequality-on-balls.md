---
declaration: theorem
origin: cited
lean: TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eLpNorm_gradient_of_ball_subset, TauCeti.eLpNorm_sub_setAverage_le_mul_measure_rpow_of_convex, TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_measure_rpow_of_convex, TauCeti.W1p.setLAverage_rpow_enorm_value_sub_setAverage_le_of_ball_subset, TauCeti.W1p.setLAverage_rpow_enorm_value_sub_setAverage_le_of_eq_ball, TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eNorm_gradient_of_convex
statement: formalized
proof: formalized
---

# The Sobolev–Poincaré inequality on balls

Let `1 ≤ p < n`, with Sobolev conjugate `p⋆`,
`1/p⋆ + 1/n = 1/p`, where `n` is the dimension. If `u ∈ W^{1,p}(Ω)` and `B = B(c, R) ⊆ Ω`, then

`‖u - ⨍_B u‖_{L^{p⋆}(B)} ≤ 2 ^ (n + 5) p⋆ / μ(B(0, 1)) ^ (1/n) · ‖∇u‖_{Lᵖ(B)}`.

The constant depends only on `n`, `p` and the normalization of `μ`, not on the radius: `p⋆` is the
only exponent for which an inequality of this form is invariant under dilations.

```lean
TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eLpNorm_gradient_of_ball_subset.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p pstar : ENNReal} [Fact (1 ≤ p)] (hpstar : pstar ≠ ⊤)
  (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹) {c : E} {R : ℝ}
  (hball : Metric.ball c R ⊆ ↑Omega) (u : ↥(TauCeti.W1p mu Omega p)) :
  MeasureTheory.eLpNorm
      (fun x =>
        ↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in Metric.ball c R, ↑↑(TauCeti.W1p.value u) y ∂mu)
      pstar (mu.restrict (Metric.ball c R)) ≤
    ENNReal.ofReal
        (2 ^ (Module.finrank ℝ E + 5) * pstar.toReal /
          mu.real (Metric.ball 0 1) ^ (↑(Module.finrank ℝ E))⁻¹) *
      MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.gradient u)) p (mu.restrict (Metric.ball c R))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's bound on an average](../../../../measure-theory/integral/part-02/holders-bound-on-an-average.md)
- [Hölder's inequality with a bounded weight](../../../../measure-theory/integral/part-02/holders-inequality-with-a-bounded-weight.md)
- [Meyers–Serrin: `H = W` in `W^{k,p}(Ω)`](meyers-serrin-h-w-in-w-k-p.md)
- [The Poincaré–Wirtinger inequality for functions of bounded variation, localized to a subset](../../../part-03/bounded-variation/the-poincare-wirtinger-inequality-for-functions.md)
- [Young's inequality for integral kernels](../../../../measure-theory/integral/part-02/youngs-inequality-for-integral-kernels.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eLpNorm_gradient_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/CriticalSobolev.html#TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eLpNorm_gradient_of_ball_subset).

## Other forms

**The Sobolev–Poincaré inequality for `C¹` functions on a convex domain.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_sub_setAverage_le_mul_measure_rpow_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Sobolev.html#TauCeti.eLpNorm_sub_setAverage_le_mul_measure_rpow_of_convex).

```lean
TauCeti.eLpNorm_sub_setAverage_le_mul_measure_rpow_of_convex.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [Nontrivial E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u : E → F} {Ω S : Set E} (hΩ : IsOpen Ω)
  (hΩc : Convex ℝ Ω) (hb : Bornology.IsBounded Ω) (hu : ContDiffOn ℝ 1 u Ω) (hS : S ⊆ Ω)
  (hS₀ : μ S ≠ 0) {p q : NNReal} (hp : 1 ≤ p) (hpq : p ≤ q) {δ : ℝ} (hδ : (↑p)⁻¹ - (↑q)⁻¹ = δ)
  (hδn : δ < (↑(Module.finrank ℝ E))⁻¹) :
  MeasureTheory.eLpNorm (fun x => u x - ⨍ (y : E) in S, u y ∂μ) (↑q) (μ.restrict Ω) ≤
    ENNReal.ofReal
            (Metric.diam Ω ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E) *
              (((1 - δ) / ((↑(Module.finrank ℝ E))⁻¹ - δ)) ^ (1 - δ) *
                μ.real (Metric.ball 0 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹))) /
          μ S *
        μ Ω ^ ((↑(Module.finrank ℝ E))⁻¹ - δ) *
      MeasureTheory.eLpNorm (fderiv ℝ u) (↑p) (μ.restrict Ω)
```

**The Sobolev–Poincaré inequality on `W^{1,p}(Ω)`.** Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_measure_rpow_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Sobolev.html#TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_measure_rpow_of_convex).

```lean
TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_measure_rpow_of_convex.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {S : Set E} [Nontrivial E]
  (hp : p ≠ ⊤) (hconv : Convex ℝ ↑Omega) (hb : Bornology.IsBounded ↑Omega) (hS : S ⊆ ↑Omega)
  (hS0 : mu S ≠ 0) {q : NNReal} (hpq : p ≤ ↑q) {δ : ℝ} (hδ : p.toReal⁻¹ - (↑q)⁻¹ = δ)
  (hδn : δ < (↑(Module.finrank ℝ E))⁻¹) (u : ↥(TauCeti.W1p mu Omega p)) :
  MeasureTheory.eLpNorm
      (fun x => ↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in S, ↑↑(TauCeti.W1p.value u) y ∂mu) (↑q)
      (mu.restrict ↑Omega) ≤
    ENNReal.ofReal
            (Metric.diam ↑Omega ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E) *
              (((1 - δ) / ((↑(Module.finrank ℝ E))⁻¹ - δ)) ^ (1 - δ) *
                mu.real (Metric.ball 0 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹))) /
          mu S *
        mu ↑Omega ^ ((↑(Module.finrank ℝ E))⁻¹ - δ) *
      ‖TauCeti.W1p.gradient u‖ₑ
```

**The Sobolev–Poincaré inequality on a ball inside the domain, with averages.** Formalized in Tau Ceti as [`TauCeti.W1p.setLAverage_rpow_enorm_value_sub_setAverage_le_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Sobolev.html#TauCeti.W1p.setLAverage_rpow_enorm_value_sub_setAverage_le_of_ball_subset).

```lean
TauCeti.W1p.setLAverage_rpow_enorm_value_sub_setAverage_le_of_ball_subset.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] [Nontrivial E] {p₀ : ENNReal}
  [Fact (1 ≤ p₀)] (hp : p ≠ ⊤) (hpp₀ : p ≤ p₀) {c : E} {r : ℝ} (hr : 0 < r)
  (hball : Metric.ball c r ⊆ ↑Omega) {q : NNReal} (hpq : p ≤ ↑q) {δ : ℝ}
  (hδ : p.toReal⁻¹ - (↑q)⁻¹ = δ) (hδn : δ < (↑(Module.finrank ℝ E))⁻¹)
  (u : ↥(TauCeti.W1p mu Omega p₀)) :
  (⨍⁻ (x : E) in Metric.ball c r,
        ‖↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in Metric.ball c r, ↑↑(TauCeti.W1p.value u) y ∂mu‖ₑ ^
          ↑q ∂mu) ^
      (↑q)⁻¹ ≤
    ENNReal.ofReal
        (2 ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E) *
            ((1 - δ) / ((↑(Module.finrank ℝ E))⁻¹ - δ)) ^ (1 - δ) *
          r) *
      (⨍⁻ (x : E) in Metric.ball c r, ‖↑↑(TauCeti.W1p.gradient u) x‖ₑ ^ p.toReal ∂mu) ^ p.toReal⁻¹
```

**The Sobolev–Poincaré inequality on a ball, with averages.** Formalized in Tau Ceti as [`TauCeti.W1p.setLAverage_rpow_enorm_value_sub_setAverage_le_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Sobolev.html#TauCeti.W1p.setLAverage_rpow_enorm_value_sub_setAverage_le_of_eq_ball).

```lean
TauCeti.W1p.setLAverage_rpow_enorm_value_sub_setAverage_le_of_eq_ball.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] [Nontrivial E] (hp : p ≠ ⊤)
  {c : E} {r : ℝ} (hr : 0 < r) (hOmega : ↑Omega = Metric.ball c r) {q : NNReal} (hpq : p ≤ ↑q)
  {δ : ℝ} (hδ : p.toReal⁻¹ - (↑q)⁻¹ = δ) (hδn : δ < (↑(Module.finrank ℝ E))⁻¹)
  (u : ↥(TauCeti.W1p mu Omega p)) :
  (⨍⁻ (x : E) in ↑Omega,
        ‖↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in ↑Omega, ↑↑(TauCeti.W1p.value u) y ∂mu‖ₑ ^
          ↑q ∂mu) ^
      (↑q)⁻¹ ≤
    ENNReal.ofReal
        (2 ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E) *
            ((1 - δ) / ((↑(Module.finrank ℝ E))⁻¹ - δ)) ^ (1 - δ) *
          r) *
      (⨍⁻ (x : E) in ↑Omega, ‖↑↑(TauCeti.W1p.gradient u) x‖ₑ ^ p.toReal ∂mu) ^ p.toReal⁻¹
```

**The Sobolev–Poincaré inequality on a bounded convex domain.** Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eNorm_gradient_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/CriticalSobolev.html#TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eNorm_gradient_of_convex).

```lean
TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eNorm_gradient_of_convex.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p pstar : ENNReal} [Fact (1 ≤ p)] (hpstar : pstar ≠ ⊤)
  (hexp : pstar⁻¹ + (↑(Module.finrank ℝ E))⁻¹ = p⁻¹) (hconv : Convex ℝ ↑Omega)
  (hb : Bornology.IsBounded ↑Omega) (u : ↥(TauCeti.W1p mu Omega p)) :
  MeasureTheory.eLpNorm
      (fun x => ↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in ↑Omega, ↑↑(TauCeti.W1p.value u) y ∂mu)
      pstar (mu.restrict ↑Omega) ≤
    ENNReal.ofReal
        (32 * pstar.toReal * mu.real (Metric.ball 0 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹) *
            Metric.diam ↑Omega ^ Module.finrank ℝ E /
          mu.real ↑Omega) *
      ‖TauCeti.W1p.gradient u‖ₑ
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eLpNorm_gradient_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/CriticalSobolev.html#TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eLpNorm_gradient_of_ball_subset)
- [Source of `TauCeti.W1p.eLpNorm_value_sub_setAverage_le_mul_eLpNorm_gradient_of_ball_subset` in TauCeti/Analysis/Sobolev/Poincare/Wirtinger/CriticalSobolev.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/CriticalSobolev.lean#L556)
