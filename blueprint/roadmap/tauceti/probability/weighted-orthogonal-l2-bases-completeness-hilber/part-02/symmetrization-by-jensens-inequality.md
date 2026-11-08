---
declaration: theorem
origin: cited
lean: TauCeti.ofReal_mgf_sub_integral_le_lintegral
statement: formalized
proof: formalized
---

# Symmetrization by Jensen's inequality

For a probability measure `μ`, the moment
generating function of `f - 𝔼 f` at `t` is at most `∫∫ exp (t (f x - f y)) dμ(x) dμ(y)`.

```lean
TauCeti.ofReal_mgf_sub_integral_le_lintegral.{u_1} {Ω : Type u_1} {mΩ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} {f : Ω → ℝ} [MeasureTheory.IsProbabilityMeasure μ]
  (hfm : Measurable f) (hfi : MeasureTheory.Integrable f μ) {t : ℝ}
  (hint : MeasureTheory.Integrable (fun x => Real.exp (t * (f x - ∫ (y : Ω), f y ∂μ))) μ)
  (hneg : MeasureTheory.Integrable (fun x => Real.exp (-t * f x)) μ) :
  ENNReal.ofReal (ProbabilityTheory.mgf (fun x => f x - ∫ (y : Ω), f y ∂μ) μ t) ≤
    ∫⁻ (p : Ω × Ω), ENNReal.ofReal (Real.exp (t * (f p.1 - f p.2))) ∂μ.prod μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ofReal_mgf_sub_integral_le_lintegral`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Basic.html#TauCeti.ofReal_mgf_sub_integral_le_lintegral).

## Sources

- [Tau Ceti documentation: `TauCeti.ofReal_mgf_sub_integral_le_lintegral`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Basic.html#TauCeti.ofReal_mgf_sub_integral_le_lintegral)
- [Source of `TauCeti.ofReal_mgf_sub_integral_le_lintegral` in TauCeti/Probability/Moments/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Moments/Basic.lean#L120)
