---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.IsJacobiFieldOn.exists_geodesicVariation_of_isCompact
statement: formalized
proof: formalized
---

# TauCeti.Manifold.IsJacobiFieldOn.exists_geodesicVariation_of_isCompact

A Jacobi field along a maximal geodesic is realized by a smooth geodesic variation
on a common open time domain around every prescribed compact subset. The central curve
and variation field agree with the original ones throughout `s`, not only on the compact
subset. The nearby curves are not asserted to have fixed endpoints.

```lean
TauCeti.Manifold.IsJacobiFieldOn.exists_geodesicVariation_of_isCompact.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {p : M} {v : TangentSpace I p}
  {s : Set ℝ} {J : (t : ℝ) → TangentSpace I (TauCeti.Manifold.maximalGeodesic I M p v t)}
  (hJ : TauCeti.Manifold.IsJacobiFieldOn I (TauCeti.Manifold.maximalGeodesic I M p v) J s)
  (hs : IsPreconnected s) (h0 : 0 ∈ s) (hsub : s ⊆ TauCeti.Manifold.geodesicInterval I M p v)
  {K : Set ℝ} (hK : IsCompact K) (hKs : K ⊆ s) :
  ∃ F U V,
    IsOpen U ∧
      IsOpen V ∧
        0 ∈ U ∧
          K ⊆ V ∧
            ContMDiffOn (modelWithCornersSelf ℝ (ℝ × ℝ)) I (↑⊤) (fun z => F z.1 z.2) (U ×ˢ V) ∧
              (∀ q ∈ U, TauCeti.Manifold.IsGeodesicCurveOn I (F q) V) ∧
                F 0 = TauCeti.Manifold.maximalGeodesic I M p v ∧
                  ∀ t ∈ s, TauCeti.Manifold.variationField I F t = J t
```

## Depends on

- [TauCeti.Manifold.IsJacobiFieldOn](tauceti-manifold-isjacobifieldon.md)

## Proof depends on

- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.IsJacobiFieldOn.exists_geodesicVariation_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Realization.html#TauCeti.Manifold.IsJacobiFieldOn.exists_geodesicVariation_of_isCompact).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.IsJacobiFieldOn.exists_geodesicVariation_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Realization.html#TauCeti.Manifold.IsJacobiFieldOn.exists_geodesicVariation_of_isCompact)
- [Source of `TauCeti.Manifold.IsJacobiFieldOn.exists_geodesicVariation_of_isCompact` in TauCeti/Geometry/Manifold/Riemannian/Jacobi/Realization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Jacobi/Realization.lean#L84)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
