---
declaration: theorem
origin: cited
lean: TauCeti.OrientedConnectedSum.nonempty_diffeomorph_sphere
statement: formalized
proof: formalized
---

# `X # Sⁿ ≃ X`

the oriented connected sum of a connected, Hausdorff smooth
`n`-manifold `X`, for `n ≥ 1`, with the unit sphere `Sⁿ`, is diffeomorphic to `X`, for all
orientations of `X` and of the sphere. The sphere is nonempty because `F` has dimension `n + 1`,
so this needs no nonemptiness hypothesis.

```lean
TauCeti.OrientedConnectedSum.nonempty_diffeomorph_sphere.{u_4, u_5, u_6} {ι : Type u_4} [Fintype ι]
  {F : Type u_5} [NormedAddCommGroup F] [InnerProductSpace ℝ F] {n : ℕ} [NeZero n]
  [Fact (Module.finrank ℝ F = n + 1)] {X : Type u_6} [TopologicalSpace X] [T2Space X]
  [PreconnectedSpace X] [Nonempty X] [ChartedSpace (EuclideanSpace ℝ (Fin n)) X]
  [IsManifold (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))) (↑⊤) X]
  (oX : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))) X ι)
  (oS :
    TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n)))
      (↑(Metric.sphere 0 1)) ι) :
  Nonempty
    (Diffeomorph (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n)))
      (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))) (TauCeti.OrientedConnectedSum oX oS) X ↑⊤)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The connected sum of oriented manifolds is well defined](the-connected-sum-of-oriented-manifolds-is-well.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedConnectedSum.nonempty_diffeomorph_sphere`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ConnectedSum/Oriented.html#TauCeti.OrientedConnectedSum.nonempty_diffeomorph_sphere).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedConnectedSum.nonempty_diffeomorph_sphere`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ConnectedSum/Oriented.html#TauCeti.OrientedConnectedSum.nonempty_diffeomorph_sphere)
- [Source of `TauCeti.OrientedConnectedSum.nonempty_diffeomorph_sphere` in TauCeti/Geometry/Manifold/ConnectedSum/Oriented.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/ConnectedSum/Oriented.lean#L291)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricTopology/STATUS.md)
