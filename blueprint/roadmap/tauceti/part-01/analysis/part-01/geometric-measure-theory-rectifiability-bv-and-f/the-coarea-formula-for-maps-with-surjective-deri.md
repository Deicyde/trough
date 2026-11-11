---
declaration: theorem
origin: cited
lean: MeasureTheory.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv
statement: formalized
proof: formalized
---

# The coarea formula for maps with surjective derivative

Let `E` and `F` be
finite-dimensional real inner product spaces and let `f : E → F` be differentiable at every point
of a Lebesgue-measurable set `s`, with surjective derivative. Then integrating over `F` the
`(dim E - dim F)`-dimensional Euclidean Hausdorff measures of the fibres `s ∩ f ⁻¹' {y}` gives the
integral over `s` of the coarea Jacobian, the norm determinant of the adjoint of
`fderiv ℝ f x`.

```lean
MeasureTheory.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv.{u_1,
    u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [NormedAddCommGroup F] [InnerProductSpace ℝ F] {f : E → F} {s : Set E} [FiniteDimensional ℝ E]
  [FiniteDimensional ℝ F] [MeasurableSpace E] [BorelSpace E] [MeasurableSpace F] [BorelSpace F]
  (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume)
  (hd : ∀ x ∈ s, DifferentiableAt ℝ f x) (hsurj : ∀ x ∈ s, Function.Surjective ⇑(fderiv ℝ f x)) :
  ∫⁻ (y : F),
      (MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ E - Module.finrank ℝ F))
        (s ∩ f ⁻¹' {y}) =
    ∫⁻ (x : E) in s, ENNReal.ofReal (↑(ContinuousLinearMap.adjoint (fderiv ℝ f x))).normDet
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Eilenberg's inequality, integral form](../../../measure-theory/function/part-01/eilenbergs-inequality-integral-form.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Basic.html#MeasureTheory.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv).

## Sources

- [Tau Ceti documentation: `MeasureTheory.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Basic.html#MeasureTheory.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv)
- [Source of `MeasureTheory.lintegral_euclideanHausdorffMeasure_inter_preimage_eq_lintegral_normDet_adjoint_fderiv` in TauCeti/MeasureTheory/Function/Coarea/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Coarea/Basic.lean#L447)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
