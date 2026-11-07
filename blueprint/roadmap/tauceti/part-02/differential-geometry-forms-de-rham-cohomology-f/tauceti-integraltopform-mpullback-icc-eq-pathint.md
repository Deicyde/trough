---
declaration: theorem
origin: cited
lean: TauCeti.integralTopForm_mpullback_Icc_eq_pathIntegral
statement: formalized
proof: formalized
---

# TauCeti.integralTopForm\_mpullback\_Icc\_eq\_pathIntegral

For `a < b`, the line integral of a continuous real `1`-form along a `C¹` curve is the
canonical oriented integral over `[a, b]` of the pullback of the form along the curve.

```lean
TauCeti.integralTopForm_mpullback_Icc_eq_pathIntegral.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] {a b : ℝ}
  [Fact (a < b)] {φ : TauCeti.RoughForm I M ℝ 1} (hφ : TauCeti.IsSmoothForm I 0 φ) {γ : ℝ → M}
  (hγ : ContMDiff (modelWithCornersSelf ℝ ℝ) I 1 γ) :
  TauCeti.integralTopForm (TauCeti.Manifold.Orientation.interval a b)
      (TauCeti.mpullback (modelWithCornersEuclideanHalfSpace 1) I (fun t => γ ↑t) φ) =
    TauCeti.pathIntegral φ γ a b
```

## Depends on

- [TauCeti.pathIntegral](tauceti-pathintegral.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integralTopForm_mpullback_Icc_eq_pathIntegral`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.integralTopForm_mpullback_Icc_eq_pathIntegral).

## Sources

- [Tau Ceti documentation: `TauCeti.integralTopForm_mpullback_Icc_eq_pathIntegral`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.integralTopForm_mpullback_Icc_eq_pathIntegral)
- [Source of `TauCeti.integralTopForm_mpullback_Icc_eq_pathIntegral` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean#L394)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
