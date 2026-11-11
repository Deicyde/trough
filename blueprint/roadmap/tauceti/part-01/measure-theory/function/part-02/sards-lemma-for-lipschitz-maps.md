---
declaration: theorem
origin: cited
lean: LipschitzWith.euclideanHausdorffMeasure_image_setOf_normDet_fderiv_eq_zero
statement: formalized
proof: formalized
---

# Sard's lemma for Lipschitz maps

The image of the set where the `dim U`-dimensional
Jacobian of a Lipschitz map `f : U → V` vanishes is null for the `dim U`-dimensional Euclidean
Hausdorff measure.

```lean
LipschitzWith.euclideanHausdorffMeasure_image_setOf_normDet_fderiv_eq_zero.{u_1, u_2} {U : Type u_1}
  {V : Type u_2} [NormedAddCommGroup U] [InnerProductSpace ℝ U] [FiniteDimensional ℝ U]
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace U]
  [BorelSpace U] [MeasurableSpace V] [BorelSpace V] {f : U → V} {K : NNReal}
  (hf : LipschitzWith K f) :
  (MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ U))
      (f '' {x | (↑(fderiv ℝ f x)).normDet = 0}) =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LipschitzWith.euclideanHausdorffMeasure_image_setOf_normDet_fderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/AreaFormula/Lipschitz.html#LipschitzWith.euclideanHausdorffMeasure_image_setOf_normDet_fderiv_eq_zero).

## Sources

- [Tau Ceti documentation: `LipschitzWith.euclideanHausdorffMeasure_image_setOf_normDet_fderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/AreaFormula/Lipschitz.html#LipschitzWith.euclideanHausdorffMeasure_image_setOf_normDet_fderiv_eq_zero)
- [Source of `LipschitzWith.euclideanHausdorffMeasure_image_setOf_normDet_fderiv_eq_zero` in TauCeti/MeasureTheory/Function/AreaFormula/Lipschitz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/AreaFormula/Lipschitz.lean#L247)
