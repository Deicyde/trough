---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.isEnergyCritical_iff_isGeodesicCurveOn
statement: formalized
proof: formalized
---

# The variational characterization of geodesics

On a boundaryless `C^n` manifold with
`2 ≤ n ≤ ∞`, a curve which is `C^n` near every point of `[a, b]` is a critical point of the energy
between `a` and `b` among `C^n` variations with fixed endpoints exactly when it is a geodesic on
the open interval between `a` and `b`.  For `n = ∞`: a smooth curve is critical among smooth
variations exactly when it is a geodesic.

```lean
TauCeti.Manifold.isEnergyCritical_iff_isGeodesicCurveOn.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] {γ : ℝ → M}
  {a b : ℝ} {n : ℕ∞} [I.Boundaryless] [IsManifold I 2 M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] [FiniteDimensional ℝ E]
  [ContMDiffVectorBundle 1 E (TangentSpace I) I]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] [IsManifold I (↑n) M] (hn : 2 ≤ n)
  (hγ : ∀ t ∈ Set.uIcc a b, ContMDiffAt (modelWithCornersSelf ℝ ℝ) I (↑n) γ t) :
  TauCeti.Manifold.IsEnergyCritical I (↑n) γ a b ↔
    TauCeti.Manifold.IsGeodesicCurveOn I γ (Set.uIoo a b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.isEnergyCritical_iff_isGeodesicCurveOn`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/FirstVariation.html#TauCeti.Manifold.isEnergyCritical_iff_isGeodesicCurveOn).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.isEnergyCritical_iff_isGeodesicCurveOn`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/FirstVariation.html#TauCeti.Manifold.isEnergyCritical_iff_isGeodesicCurveOn)
- [Source of `TauCeti.Manifold.isEnergyCritical_iff_isGeodesicCurveOn` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/FirstVariation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Geodesic/FirstVariation.lean#L307)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HopfRinow/STATUS.md)
