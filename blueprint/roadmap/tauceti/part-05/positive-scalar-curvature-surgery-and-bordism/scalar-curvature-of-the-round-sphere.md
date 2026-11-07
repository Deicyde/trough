---
declaration: theorem
origin: cited
lean: TauCeti.scalarCurvature_sphereRoundMetricOfRadius
statement: formalized
proof: formalized
---

# Scalar curvature of the round sphere

The round `n`-sphere of radius `r` has scalar
curvature `n (n - 1) / r²`.

```lean
TauCeti.scalarCurvature_sphereRoundMetricOfRadius.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {n : ℕ} [Fact (Module.finrank ℝ E = n + 1)] {r : ℝ} (hr : 0 < r)
  (p : ↑(Metric.sphere 0 1)) :
  (TauCeti.sphereRoundMetricOfRadius r hr).scalarCurvature p = ↑n * (↑n - 1) / r ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.scalarCurvature_sphereRoundMetricOfRadius`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sphere/Radius.html#TauCeti.scalarCurvature_sphereRoundMetricOfRadius).

## Sources

- [Tau Ceti documentation: `TauCeti.scalarCurvature_sphereRoundMetricOfRadius`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sphere/Radius.html#TauCeti.scalarCurvature_sphereRoundMetricOfRadius)
- [Source of `TauCeti.scalarCurvature_sphereRoundMetricOfRadius` in TauCeti/Geometry/Manifold/Riemannian/Sphere/Radius.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Sphere/Radius.lean#L116)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
