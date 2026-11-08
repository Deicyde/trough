---
declaration: theorem
origin: cited
lean: TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_eq_ball, TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex, TauCeti.W1p.exists_eLpNorm_value_sub_setAverage_le_of_isCompactOperator, TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_convex, TauCeti.W1p.setIntegral_value_sub_setAverage_sq_le_of_ball_subset, TauCeti.W1p.setIntegral_abs_value_sub_setAverage_le_of_ball_subset, TauCeti.eLpNorm_sub_setAverage_le_of_convex, TauCeti.lintegral_enorm_sub_setAverage_rpow_le_of_convex, TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_of_convex, TauCeti.W1p.exists_eLpNorm_value_sub_setAverage_le_of_isLipschitzDomainWith
statement: formalized
proof: formalized
---

# The Poincaré–Wirtinger inequality on a ball

On a ball of radius `R` the constant of
`TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_convex` is `2 ^ (n + 1) * R`: the deviation of
`u ∈ W^{1,p}(B(c, R))` from its mean over the ball is at most `2 ^ (n + 1) * R` times the `Lᵖ`
norm of its weak gradient.  The constant is proportional to `R`, as the scaling of both sides
forces.

```lean
TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_eq_ball.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E}
  {p : ENNReal} [Fact (1 ≤ p)] {c : E} {R : ℝ} (hp : p ≠ ⊤) (hR : 0 < R)
  (hOmega : ↑Omega = Metric.ball c R) (u : ↥(TauCeti.W1p mu Omega p)) :
  MeasureTheory.eLpNorm
      (fun x => ↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in ↑Omega, ↑↑(TauCeti.W1p.value u) y ∂mu) p
      (mu.restrict ↑Omega) ≤
    ENNReal.ofReal (2 ^ (Module.finrank ℝ E + 1) * R) * ‖TauCeti.W1p.gradient u‖ₑ
```

## Depends on

- [TauCeti.totalVariationOn](../../../part-01/geometric-measure-theory-rectifiability-bv-and-f/tauceti-totalvariationon.md)

## Proof depends on

- [Extension theorem for bounded Lipschitz domains](../part-01/extension-theorem-for-bounded-lipschitz-domains.md)
- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set, the form that Rellich--Kondrachov for `W^{1,p}_0(Ω)` consumes](../../../../measure-theory/function/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Hölder's inequality for Young's exponents](../../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)
- [The Poincaré inequality on a ball](../part-01/the-poincare-inequality-on-a-ball.md)
- [Rademacher's theorem for locally Lipschitz functions](../../../part-01/calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)
- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)
- [Young's inequality for an `L¹` kernel](../../../../measure-theory/function/youngs-inequality-for-an-l1-kernel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/W1p.html#TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_eq_ball).

## Other forms

**The Poincaré–Wirtinger inequality for functions of bounded variation, localized to a subset.** Formalized in Tau Ceti as [`TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/Poincare.html#TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex).

```lean
TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_totalVariationOn_of_convex.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  {Ω : TopologicalSpace.Opens E} {u : E → ℝ} {S A : Set E} (hΩc : Convex ℝ ↑Ω)
  (hb : Bornology.IsBounded ↑Ω) (hu : MeasureTheory.LocallyIntegrableOn u (↑Ω) μ) (hS : S ⊆ ↑Ω)
  (hS₀ : μ S ≠ 0) (hA : A ⊆ ↑Ω) :
  ∫⁻ (x : E) in A, ‖u x - ⨍ (y : E) in S, u y ∂μ‖ₑ ∂μ ≤
    ENNReal.ofReal
          (μ.real (Metric.ball 0 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹) *
              Metric.diam ↑Ω ^ Module.finrank ℝ E /
            μ.real S) *
        μ A ^ (↑(Module.finrank ℝ E))⁻¹ *
      TauCeti.totalVariationOn μ Ω u
```

**The Poincaré–Wirtinger inequality from compactness.** Formalized in Tau Ceti as [`TauCeti.W1p.exists_eLpNorm_value_sub_setAverage_le_of_isCompactOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Compactness.html#TauCeti.W1p.exists_eLpNorm_value_sub_setAverage_le_of_isCompactOperator).

```lean
TauCeti.W1p.exists_eLpNorm_value_sub_setAverage_le_of_isCompactOperator.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {S : Set E}
  (hK : IsCompactOperator ⇑TauCeti.W1p.valueL) (hconn : IsPreconnected ↑Omega)
  (hfin : mu ↑Omega ≠ ⊤) (hS : S ⊆ ↑Omega) (hS0 : mu S ≠ 0) :
  ∃ C,
    0 ≤ C ∧
      ∀ (u : ↥(TauCeti.W1p mu Omega p)),
        MeasureTheory.eLpNorm
            (fun x => ↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in S, ↑↑(TauCeti.W1p.value u) y ∂mu) p
            (mu.restrict ↑Omega) ≤
          ENNReal.ofReal C * ‖TauCeti.W1p.gradient u‖ₑ
```

**The Poincaré–Wirtinger inequality on `W^{1,p}(Ω)`.** Formalized in Tau Ceti as [`TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/W1p.html#TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_convex).

```lean
TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_convex.{u_1} {E : Type u_1} [MeasurableSpace E]
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [BorelSpace E]
  {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure] {Omega : TopologicalSpace.Opens E}
  {p : ENNReal} [Fact (1 ≤ p)] {S : Set E} (hp : p ≠ ⊤) (hconv : Convex ℝ ↑Omega)
  (hb : Bornology.IsBounded ↑Omega) (hSm : MeasureTheory.NullMeasurableSet S mu) (hS : S ⊆ ↑Omega)
  (hS0 : mu S ≠ 0) (u : ↥(TauCeti.W1p mu Omega p)) :
  MeasureTheory.eLpNorm
      (fun x => ↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in S, ↑↑(TauCeti.W1p.value u) y ∂mu) p
      (mu.restrict ↑Omega) ≤
    ENNReal.ofReal
        (mu.real (Metric.ball 0 1) * Metric.diam ↑Omega ^ (Module.finrank ℝ E + 1) / mu.real S) *
      ‖TauCeti.W1p.gradient u‖ₑ
```

**The Poincaré–Wirtinger inequality on a ball inside the domain, in `L²`.** Formalized in Tau Ceti as [`TauCeti.W1p.setIntegral_value_sub_setAverage_sq_le_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/W1p.html#TauCeti.W1p.setIntegral_value_sub_setAverage_sq_le_of_ball_subset).

```lean
TauCeti.W1p.setIntegral_value_sub_setAverage_sq_le_of_ball_subset.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {c : E} {R : ℝ} (hR : 0 < R) (hball : Metric.ball c R ⊆ ↑Omega)
  (u : ↥(TauCeti.W1p mu Omega 2)) :
  ∫ (x : E) in Metric.ball c R,
      (↑↑(TauCeti.W1p.value u) x - ⨍ (y : E) in Metric.ball c R, ↑↑(TauCeti.W1p.value u) y ∂mu) ^
        2 ∂mu ≤
    (2 ^ (Module.finrank ℝ E + 1) * R) ^ 2 *
      ∫ (x : E) in Metric.ball c R, ‖↑↑(TauCeti.W1p.gradient u) x‖ ^ 2 ∂mu
```

**The Poincaré–Wirtinger inequality on a ball inside the domain, in `L¹`.** Formalized in Tau Ceti as [`TauCeti.W1p.setIntegral_abs_value_sub_setAverage_le_of_ball_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/W1p.html#TauCeti.W1p.setIntegral_abs_value_sub_setAverage_le_of_ball_subset).

```lean
TauCeti.W1p.setIntegral_abs_value_sub_setAverage_le_of_ball_subset.{u_1} {E : Type u_1}
  [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [BorelSpace E] {mu : MeasureTheory.Measure E} [mu.IsAddHaarMeasure]
  {Omega : TopologicalSpace.Opens E} {p : ENNReal} [Fact (1 ≤ p)] {c : E} {R : ℝ} (hR : 0 < R)
  (hball : Metric.ball c R ⊆ ↑Omega) (u : ↥(TauCeti.W1p mu Omega p)) :
  ∫ (x : E) in Metric.ball c R,
      |↑↑(TauCeti.W1p.value u) x -
          ⨍ (y : E) in Metric.ball c R, ↑↑(TauCeti.W1p.value u) y ∂mu| ∂mu ≤
    2 ^ (Module.finrank ℝ E + 1) * R *
      ∫ (x : E) in Metric.ball c R, ‖↑↑(TauCeti.W1p.gradient u) x‖ ∂mu
```

**The Poincaré–Wirtinger inequality on a convex domain.** Formalized in Tau Ceti as [`TauCeti.eLpNorm_sub_setAverage_le_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Basic.html#TauCeti.eLpNorm_sub_setAverage_le_of_convex).

```lean
TauCeti.eLpNorm_sub_setAverage_le_of_convex.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u : E → F} {Ω S : Set E} (hΩ : IsOpen Ω)
  (hΩc : Convex ℝ Ω) (hb : Bornology.IsBounded Ω) (hu : ContDiffOn ℝ 1 u Ω) (hS : S ⊆ Ω)
  (hS₀ : μ S ≠ 0) {p : ENNReal} (hp : 1 ≤ p) (hp' : p ≠ ⊤) :
  MeasureTheory.eLpNorm (fun x => u x - ⨍ (y : E) in S, u y ∂μ) p (μ.restrict Ω) ≤
    ENNReal.ofReal
        (μ.real (Metric.ball 0 1) * Metric.diam Ω ^ (Module.finrank ℝ E + 1) / μ.real S) *
      MeasureTheory.eLpNorm (fderiv ℝ u) p (μ.restrict Ω)
```

**The Poincaré–Wirtinger inequality on a convex domain, in `∫⁻` form.** Formalized in Tau Ceti as [`TauCeti.lintegral_enorm_sub_setAverage_rpow_le_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Basic.html#TauCeti.lintegral_enorm_sub_setAverage_rpow_le_of_convex).

```lean
TauCeti.lintegral_enorm_sub_setAverage_rpow_le_of_convex.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u : E → F} {Ω S : Set E} (hΩ : IsOpen Ω)
  (hΩc : Convex ℝ Ω) (hb : Bornology.IsBounded Ω) (hu : ContDiffOn ℝ 1 u Ω) (hS : S ⊆ Ω)
  (hS₀ : μ S ≠ 0) {p : ℝ} (hp : 1 ≤ p) :
  ∫⁻ (x : E) in Ω, ‖u x - ⨍ (y : E) in S, u y ∂μ‖ₑ ^ p ∂μ ≤
    ENNReal.ofReal
        ((μ.real (Metric.ball 0 1) * Metric.diam Ω ^ (Module.finrank ℝ E + 1) / μ.real S) ^ p) *
      ∫⁻ (y : E) in Ω, ‖fderiv ℝ u y‖ₑ ^ p ∂μ
```

**The Poincaré–Wirtinger inequality on a convex domain, localized to a subset.** Formalized in Tau Ceti as [`TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_of_convex`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/Basic.html#TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_of_convex).

```lean
TauCeti.setLIntegral_enorm_sub_setAverage_le_mul_measure_rpow_mul_of_convex.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {u : E → F} {Ω S : Set E} (hΩ : IsOpen Ω)
  (hΩc : Convex ℝ Ω) (hb : Bornology.IsBounded Ω) (hu : ContDiffOn ℝ 1 u Ω) (hS : S ⊆ Ω)
  (hS₀ : μ S ≠ 0) {A : Set E} (hA : A ⊆ Ω) :
  ∫⁻ (x : E) in A, ‖u x - ⨍ (y : E) in S, u y ∂μ‖ₑ ∂μ ≤
    ENNReal.ofReal
          (μ.real (Metric.ball 0 1) ^ (1 - (↑(Module.finrank ℝ E))⁻¹) *
              Metric.diam Ω ^ Module.finrank ℝ E /
            μ.real S) *
        μ A ^ (↑(Module.finrank ℝ E))⁻¹ *
      ∫⁻ (y : E) in Ω, ‖fderiv ℝ u y‖ₑ ∂μ
```

**The Poincaré–Wirtinger inequality on bounded connected Lipschitz domains.** Formalized in Tau Ceti as [`TauCeti.W1p.exists_eLpNorm_value_sub_setAverage_le_of_isLipschitzDomainWith`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/LipschitzDomain/RellichKondrachov.html#TauCeti.W1p.exists_eLpNorm_value_sub_setAverage_le_of_isLipschitzDomainWith).

```lean
TauCeti.W1p.exists_eLpNorm_value_sub_setAverage_le_of_isLipschitzDomainWith.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {p : ENNReal}
  [Fact (1 ≤ p)] (hp : p ≠ ⊤) (hΩ : (↑Ω).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑Ω)
  (hconn : IsPreconnected ↑Ω) {S : Set (WithLp 2 (ℝ × E))} (hS : S ⊆ ↑Ω)
  (hS0 : MeasureTheory.volume S ≠ 0) :
  ∃ C,
    0 ≤ C ∧
      ∀ (u : ↥(TauCeti.W1p MeasureTheory.volume Ω p)),
        MeasureTheory.eLpNorm
            (fun x =>
              ↑↑(TauCeti.W1p.value u) x - ⨍ (y : WithLp 2 (ℝ × E)) in S, ↑↑(TauCeti.W1p.value u) y)
            p (MeasureTheory.volume.restrict ↑Ω) ≤
          ENNReal.ofReal C * ‖TauCeti.W1p.gradient u‖ₑ
```

## Sources

- [Tau Ceti documentation: `TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_eq_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/W1p.html#TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_eq_ball)
- [Source of `TauCeti.W1p.eLpNorm_value_sub_setAverage_le_of_eq_ball` in TauCeti/Analysis/Sobolev/Poincare/Wirtinger/W1p.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Poincare/Wirtinger/W1p.lean#L300)
