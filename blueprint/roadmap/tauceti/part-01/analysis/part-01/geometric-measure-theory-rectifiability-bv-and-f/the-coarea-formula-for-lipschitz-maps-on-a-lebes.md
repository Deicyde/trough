---
declaration: theorem
origin: cited
lean: LipschitzWith.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv
statement: formalized
proof: formalized
---

# The coarea formula for Lipschitz maps on a Lebesgue-measurable set `s`

`∫⁻ y, μHE[dim E - dim F] (s ∩ f ⁻¹' {y}) = ∫⁻ x in s, (fderiv ℝ f x)†.normDet`.

```lean
LipschitzWith.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv.{u_1,
    u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [NormedAddCommGroup F] [InnerProductSpace ℝ F] [FiniteDimensional ℝ F]
  [MeasurableSpace E] [BorelSpace E] [MeasurableSpace F] [BorelSpace F] {s : Set E} {f : E → F}
  {K : NNReal} (hf : LipschitzWith K f)
  (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume) :
  ∫⁻ (y : F),
      (MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ E - Module.finrank ℝ F))
        (s ∩ f ⁻¹' {y}) =
    ∫⁻ (x : E) in s, ENNReal.ofReal (↑(ContinuousLinearMap.adjoint (fderiv ℝ f x))).normDet
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Eilenberg's inequality, integral form](../../../measure-theory/function/part-01/eilenbergs-inequality-integral-form.md)
- [Rademacher's theorem for locally Lipschitz functions](../../part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`LipschitzWith.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Lipschitz.html#LipschitzWith.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv).

## Sources

- [Tau Ceti documentation: `LipschitzWith.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Lipschitz.html#LipschitzWith.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv)
- [Source of `LipschitzWith.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv` in TauCeti/MeasureTheory/Function/Coarea/Lipschitz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Function/Coarea/Lipschitz.lean#L742)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
