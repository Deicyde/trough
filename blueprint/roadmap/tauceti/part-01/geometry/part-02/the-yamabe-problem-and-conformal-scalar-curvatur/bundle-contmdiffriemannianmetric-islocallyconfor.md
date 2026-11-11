---
declaration: def
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat
statement: formalized
---

# Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat

A smooth Riemannian metric `g` is **locally conformally flat** if every point `x` has a
neighbourhood on which a conformal rescaling `f g`, by a smooth positive function `f`, is flat:
the curvature tensor of the Levi-Civita connection of `f g` vanishes at every point near `x`.

```lean
Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/Basic.html#Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/Basic.html#Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat)
- [Source of `Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/Basic.lean#L97)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Yamabe/STATUS.md)
