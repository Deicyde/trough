---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.isGeodesicallyCompleteAt_of_compactSpace
statement: formalized
proof: formalized
---

# A compact Riemannian manifold is geodesically complete

every maximal geodesic leaving a
point `p` is defined for all time. This is do Carmo's corollary to the Hopf–Rinow theorem.

```lean
TauCeti.Manifold.isGeodesicallyCompleteAt_of_compactSpace.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [I.Boundaryless] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsManifold I (↑⊤) M] [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] [T2Space M]
  [CompactSpace M] (p : M) : TauCeti.Manifold.IsGeodesicallyCompleteAt I M p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.isGeodesicallyCompleteAt_of_compactSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Compact.html#TauCeti.Manifold.isGeodesicallyCompleteAt_of_compactSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.isGeodesicallyCompleteAt_of_compactSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Compact.html#TauCeti.Manifold.isGeodesicallyCompleteAt_of_compactSpace)
- [Source of `TauCeti.Manifold.isGeodesicallyCompleteAt_of_compactSpace` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Compact.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Compact.lean#L73)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HopfRinow/STATUS.md)
