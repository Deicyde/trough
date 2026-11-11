---
declaration: def
origin: cited
lean: TauCeti.torpedoMetric
statement: formalized
---

# TauCeti.torpedoMetric

The **torpedo metric** on a real inner product space `F`: the Euclidean metric multiplied by
the conformal factor `e^(2 Φ(‖y‖))`. It is the round metric of radius `torpedoCapRadius` in
stereographic coordinates on the ball of radius `e⁻²`, and the cylinder metric `‖y‖⁻² ⟪ξ, η⟫` of
`ℝ × S^(n - 1)` outside the ball of radius `e⁻¹`.

```lean
TauCeti.torpedoMetric.{u_1} (F : Type u_1) [NormedAddCommGroup F] [InnerProductSpace ℝ F] :
  Bundle.ContMDiffRiemannianMetric (modelWithCornersSelf ℝ F) (↑⊤) F fun y =>
    TangentSpace (modelWithCornersSelf ℝ F) y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.torpedoMetric`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Torpedo.html#TauCeti.torpedoMetric).

## Sources

- [Tau Ceti documentation: `TauCeti.torpedoMetric`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Torpedo.html#TauCeti.torpedoMetric)
- [Source of `TauCeti.torpedoMetric` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Torpedo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Torpedo.lean#L294)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
