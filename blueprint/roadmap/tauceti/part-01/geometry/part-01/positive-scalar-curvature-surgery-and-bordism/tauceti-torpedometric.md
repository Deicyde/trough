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
- [Source of `TauCeti.torpedoMetric` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Torpedo.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Torpedo.lean#L294)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
