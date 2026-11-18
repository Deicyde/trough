---
declaration: theorem
origin: cited
lean: LipschitzWith.lintegral_normDet_fderiv_mul_eq_lintegral_tsum
statement: formalized
proof: formalized
---

# The weighted area formula with multiplicity

Integrating the geometric Jacobian
of a Lipschitz map against a nonnegative measurable weight equals the normalized Hausdorff
integral of the sum of the weights over each fiber. The parameter set may be Lebesgue
measurable rather than Borel, and infinite fibers use extended sums.

```lean
LipschitzWith.lintegral_normDet_fderiv_mul_eq_lintegral_tsum.{u_1, u_2} {U : Type u_1}
  {V : Type u_2} [NormedAddCommGroup U] [InnerProductSpace ℝ U] [FiniteDimensional ℝ U]
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace U]
  [BorelSpace U] [MeasurableSpace V] [BorelSpace V] {f : U → V} {s : Set U} {g : U → ENNReal}
  {K : NNReal} (hf : LipschitzWith K f)
  (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume) (hg : Measurable g) :
  ∫⁻ (x : U) in s, ENNReal.ofReal (↑(fderiv ℝ f x)).normDet * g x =
    ∫⁻ (y : V),
      ∑' (x : ↑(s ∩ f ⁻¹' {y})),
        g ↑x ∂MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ U)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LipschitzWith.lintegral_normDet_fderiv_mul_eq_lintegral_tsum`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/AreaFormula/Multiplicity.html#LipschitzWith.lintegral_normDet_fderiv_mul_eq_lintegral_tsum).

## Sources

- [Tau Ceti documentation: `LipschitzWith.lintegral_normDet_fderiv_mul_eq_lintegral_tsum`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/AreaFormula/Multiplicity.html#LipschitzWith.lintegral_normDet_fderiv_mul_eq_lintegral_tsum)
- [Source of `LipschitzWith.lintegral_normDet_fderiv_mul_eq_lintegral_tsum` in TauCeti/MeasureTheory/Function/AreaFormula/Multiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Function/AreaFormula/Multiplicity.lean#L231)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
