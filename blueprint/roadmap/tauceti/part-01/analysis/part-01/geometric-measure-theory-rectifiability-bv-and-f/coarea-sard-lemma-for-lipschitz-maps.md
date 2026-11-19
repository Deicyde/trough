---
declaration: theorem
origin: cited
lean: LipschitzWith.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero, LocallyLipschitz.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero, LocallyLipschitzOn.ae_euclideanHausdorffMeasure_inter_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero
statement: formalized
proof: formalized
---

# Coarea Sard lemma for Lipschitz maps

The set where the coarea Jacobian
`(fderiv ℝ f x)†.normDet` vanishes (including points where `f` is not differentiable) meets almost
every fibre in a `μHE[dim E - dim F]`-null set.

```lean
LipschitzWith.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero.{u_1,
    u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [NormedAddCommGroup F] [InnerProductSpace ℝ F] [FiniteDimensional ℝ F]
  [MeasurableSpace E] [BorelSpace E] [MeasurableSpace F] [BorelSpace F] {f : E → F} {K : NNReal}
  (hf : LipschitzWith K f) :
  ∀ᵐ (y : F),
    (MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ E - Module.finrank ℝ F))
        ({x | (↑(ContinuousLinearMap.adjoint (fderiv ℝ f x))).normDet = 0} ∩ f ⁻¹' {y}) =
      0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Eilenberg's inequality, integral form](../../../measure-theory/function/part-01/eilenbergs-inequality-integral-form.md)
- [Rademacher's theorem for locally Lipschitz functions](../../part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`LipschitzWith.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Lipschitz.html#LipschitzWith.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero).

## Other forms

**Coarea Sard lemma for locally Lipschitz maps.** Formalized in Tau Ceti as [`LocallyLipschitz.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Lipschitz.html#LocallyLipschitz.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero).

```lean
LocallyLipschitz.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero.{u_1,
    u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [NormedAddCommGroup F] [InnerProductSpace ℝ F] [FiniteDimensional ℝ F]
  [MeasurableSpace E] [BorelSpace E] [MeasurableSpace F] [BorelSpace F] {f : E → F}
  (hf : LocallyLipschitz f) :
  ∀ᵐ (y : F),
    (MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ E - Module.finrank ℝ F))
        ({x | (↑(ContinuousLinearMap.adjoint (fderiv ℝ f x))).normDet = 0} ∩ f ⁻¹' {y}) =
      0
```

**Coarea Sard lemma for locally Lipschitz maps on open sets.** Formalized in Tau Ceti as [`LocallyLipschitzOn.ae_euclideanHausdorffMeasure_inter_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Lipschitz.html#LocallyLipschitzOn.ae_euclideanHausdorffMeasure_inter_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero).

```lean
LocallyLipschitzOn.ae_euclideanHausdorffMeasure_inter_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero.{u_1,
    u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [NormedAddCommGroup F] [InnerProductSpace ℝ F] [FiniteDimensional ℝ F]
  [MeasurableSpace E] [BorelSpace E] [MeasurableSpace F] [BorelSpace F] {U : Set E} {f : E → F}
  (hf : LocallyLipschitzOn U f) (hU : IsOpen U) :
  ∀ᵐ (y : F),
    (MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ E - Module.finrank ℝ F))
        (U ∩ {x | (↑(ContinuousLinearMap.adjoint (fderiv ℝ f x))).normDet = 0} ∩ f ⁻¹' {y}) =
      0
```

## Sources

- [Tau Ceti documentation: `LipschitzWith.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Coarea/Lipschitz.html#LipschitzWith.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero)
- [Source of `LipschitzWith.ae_euclideanHausdorffMeasure_setOf_normDet_adjoint_fderiv_eq_zero_inter_preimage_eq_zero` in TauCeti/MeasureTheory/Function/Coarea/Lipschitz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Function/Coarea/Lipschitz.lean#L724)
