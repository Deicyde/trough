---
declaration: theorem
origin: cited
lean: maximalIntegralCurveInterval_eq_univ_of_isCompact_of_mapsTo
statement: formalized
proof: formalized
---

# A maximal integral curve confined to a compact set is defined for all time

Neither
endpoint of the maximal interval can be finite, since the escape lemma would force the curve out of
the compact set there.

```lean
maximalIntegralCurveInterval_eq_univ_of_isCompact_of_mapsTo.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  {v : (x : M) → TangentSpace I x} {x : M} [T2Space M] [IsManifold I 1 M] [BoundarylessManifold I M]
  [CompleteSpace E] (hv : ContMDiff I I.tangent 1 fun y => ⟨y, v y⟩) {K : Set M} (hK : IsCompact K)
  (hmem : Set.MapsTo (maximalIntegralCurve v x) (maximalIntegralCurveInterval v x) K) :
  maximalIntegralCurveInterval v x = Set.univ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`maximalIntegralCurveInterval_eq_univ_of_isCompact_of_mapsTo`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/IntegralCurve/Maximal.html#maximalIntegralCurveInterval_eq_univ_of_isCompact_of_mapsTo).

## Sources

- [Tau Ceti documentation: `maximalIntegralCurveInterval_eq_univ_of_isCompact_of_mapsTo`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/IntegralCurve/Maximal.html#maximalIntegralCurveInterval_eq_univ_of_isCompact_of_mapsTo)
- [Source of `maximalIntegralCurveInterval_eq_univ_of_isCompact_of_mapsTo` in TauCeti/Geometry/Manifold/IntegralCurve/Maximal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/IntegralCurve/Maximal.lean#L535)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HopfRinow/STATUS.md)
