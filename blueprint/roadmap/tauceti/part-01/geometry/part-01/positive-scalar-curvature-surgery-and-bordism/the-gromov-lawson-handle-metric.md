---
declaration: theorem
origin: cited
lean: TauCeti.hasPositiveScalarCurvature_torpedoMetric_prodTangentSpace_sphereRoundMetricOfRadius
statement: formalized
proof: formalized
---

# The Gromov–Lawson handle metric

For `m ≥ 2` and every radius `δ > 0`, the product of the
torpedo metric on `F` with the round metric of radius `δ` on `Sᵐ` has positive scalar curvature.
With `F = ℝ^(k + 1)` and `m = q - 1`, this is the metric on the handle `D^(k + 1) × S^(q - 1)` glued
in by surgery along `S^k` in codimension `q ≥ 3`.

```lean
TauCeti.hasPositiveScalarCurvature_torpedoMetric_prodTangentSpace_sphereRoundMetricOfRadius.{u_4,
    u_5}
  {F : Type u_4} [NormedAddCommGroup F] [InnerProductSpace ℝ F] [FiniteDimensional ℝ F]
  {V : Type u_5} [NormedAddCommGroup V] [InnerProductSpace ℝ V] {m : ℕ}
  [Fact (Module.finrank ℝ V = m + 1)] (hm : 2 ≤ m) {δ : ℝ} (hδ : 0 < δ) :
  ((TauCeti.torpedoMetric F).prodTangentSpace
      (TauCeti.sphereRoundMetricOfRadius δ hδ)).HasPositiveScalarCurvature
```

## Depends on

- [TauCeti.torpedoMetric](tauceti-torpedometric.md)

## Proof depends on

- [The Christoffel formula of the first kind](../../part-02/manifold/part-01/the-christoffel-formula-of-the-first-kind.md)
- [The Gauss formula](../../part-02/manifold/part-01/the-gauss-formula.md)
- [The Koszul formula](../../part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasPositiveScalarCurvature_torpedoMetric_prodTangentSpace_sphereRoundMetricOfRadius`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Handle.html#TauCeti.hasPositiveScalarCurvature_torpedoMetric_prodTangentSpace_sphereRoundMetricOfRadius).

## Sources

- [Tau Ceti documentation: `TauCeti.hasPositiveScalarCurvature_torpedoMetric_prodTangentSpace_sphereRoundMetricOfRadius`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Handle.html#TauCeti.hasPositiveScalarCurvature_torpedoMetric_prodTangentSpace_sphereRoundMetricOfRadius)
- [Source of `TauCeti.hasPositiveScalarCurvature_torpedoMetric_prodTangentSpace_sphereRoundMetricOfRadius` in TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Handle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/PositiveScalarCurvature/Handle.lean#L72)
- [Tau Ceti roadmap status: Positive scalar curvature, surgery and bordism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PositiveScalarCurvature/STATUS.md)
