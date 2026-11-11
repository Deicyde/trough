---
declaration: theorem
origin: cited
lean: TauCeti.IsJordanCurve.four_pi_mul_volume_real_filledHull_sdiff_eq_iff
statement: formalized
proof: formalized
---

# Equality in the isoperimetric inequality for a rectifiable Jordan curve

For a Jordan
curve `C ⊆ ℂ` of finite length `L = μHE[1] C`, the Lebesgue area `A` of its inside
`filledHull C \ C` satisfies `4π A = L²` exactly when `C` is a circle of positive radius.

```lean
TauCeti.IsJordanCurve.four_pi_mul_volume_real_filledHull_sdiff_eq_iff {C : Set ℂ}
  (hC : TauCeti.IsJordanCurve C)
  (hfin : (MeasureTheory.Measure.euclideanHausdorffMeasure 1) C ≠ ⊤) :
  4 * Real.pi * MeasureTheory.volume.real (TauCeti.filledHull C \ C) =
      ((MeasureTheory.Measure.euclideanHausdorffMeasure 1) C).toReal ^ 2 ↔
    ∃ c r, 0 < r ∧ C = Metric.sphere c r
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Banach indicatrix inequality](../../topology/e-metric-space/banach-indicatrix-inequality.md)
- [Fundamental theorem for absolutely continuous curves, integrability](../function/part-01/fundamental-theorem-for-absolutely-continuous-cu.md)
- [Generalized winding number (HW Def 2.1)](../../analysis/part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [Jordan index theorem (orientation sign dichotomy)](../../analysis/part-02/contour/jordan-index-theorem-orientation-sign-dichotomy.md)
- [Parseval's energy identity](../../analysis/part-02/fourier/parsevals-energy-identity.md)
- [TauCeti.Green.green_ac_winding](../../geometry/part-01/differential-geometry-forms-stokes-flows-de-rham/tauceti-green-green-ac-winding.md)
- [TauCeti.rectifiableSignedArea](tauceti-rectifiablesignedarea.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.four_pi_mul_volume_real_filledHull_sdiff_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Isoperimetric.html#TauCeti.IsJordanCurve.four_pi_mul_volume_real_filledHull_sdiff_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsJordanCurve.four_pi_mul_volume_real_filledHull_sdiff_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Isoperimetric.html#TauCeti.IsJordanCurve.four_pi_mul_volume_real_filledHull_sdiff_eq_iff)
- [Source of `TauCeti.IsJordanCurve.four_pi_mul_volume_real_filledHull_sdiff_eq_iff` in TauCeti/Analysis/Complex/PlaneSeparation/Isoperimetric.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/PlaneSeparation/Isoperimetric.lean#L181)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Isoperimetry/STATUS.md)
