---
declaration: theorem
origin: cited
lean: TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_hessianOperator, TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_iteratedGradient
statement: formalized
proof: formalized
---

# The Aleksandrov measure estimate (Gilbarg–Trudinger, Lemma 9.2)

Let `Ω` be bounded and
open, let `u` be continuous on `closure Ω` and `C²` in `Ω`, and let `m` bound `u` on
`frontier Ω`. For `x ∈ Ω` and every additive Haar measure `μ`,
`μ (ball 0 ((u x - m) / diam Ω)) ≤ ∫⁻ y in upperContactSet u Ω, |det D²u(y)| ∂μ`.

```lean
TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_hessianOperator.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] {u : E → ℝ} {Ω : Set E} {x : E} [CompleteSpace E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E)
  [μ.IsAddHaarMeasure] {m : ℝ} (hΩb : Bornology.IsBounded Ω) (hΩ : IsOpen Ω)
  (hcont : ContinuousOn u (closure Ω)) (hu : ContDiffOn ℝ 2 u Ω) (hm : ∀ z ∈ frontier Ω, u z ≤ m)
  (hx : x ∈ Ω) :
  μ (Metric.ball 0 ((u x - m) / Metric.diam Ω)) ≤
    ∫⁻ (y : E) in TauCeti.PDE.upperContactSet u Ω,
      ENNReal.ofReal |(TauCeti.hessianOperator u y).det| ∂μ
```

## Depends on

- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_hessianOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/ContactSet.html#TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_hessianOperator).

## Other forms

**The Aleksandrov measure estimate for `W^{2,n}` functions (Gilbarg–Trudinger, Lemma 9.2 for strong solutions).** Formalized in Tau Ceti as [`TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_iteratedGradient`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/AleksandrovBakelmanPucci/Sobolev.html#TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_iteratedGradient).

```lean
TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_iteratedGradient.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {Ω : TopologicalSpace.Opens E}
  {ū : E → ℝ} {x : E} {m : ℝ} {p : ENNReal} [Fact (1 ≤ p)] (hΩb : Bornology.IsBounded ↑Ω)
  (hp : p = ↑(Module.finrank ℝ E)) (u : TauCeti.Wkp μ Ω p 2) (hcont : ContinuousOn ū (closure ↑Ω))
  (hū : ↑↑(TauCeti.Wkp.value 2 u) =ᵐ[μ.restrict ↑Ω] ū) (hm : ∀ z ∈ frontier ↑Ω, ū z ≤ m)
  (hx : x ∈ Ω) :
  μ (Metric.ball 0 ((ū x - m) / Metric.diam ↑Ω)) ≤
    ∫⁻ (y : E) in TauCeti.PDE.upperContactSet ū ↑Ω,
      {y | ContinuousLinearMap.IsPositive (-↑↑(TauCeti.Wkp.iteratedGradient 1 u) y)}.indicator
        (fun y => ENNReal.ofReal |ContinuousLinearMap.det (↑↑(TauCeti.Wkp.iteratedGradient 1 u) y)|)
        y ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_hessianOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/ContactSet.html#TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_hessianOperator)
- [Source of `TauCeti.PDE.addHaar_ball_le_lintegral_abs_det_hessianOperator` in TauCeti/Analysis/PDE/MaximumPrinciple/ContactSet.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/MaximumPrinciple/ContactSet.lean#L248)
