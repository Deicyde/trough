---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat.weylTensor_eq_zero
statement: formalized
proof: formalized
---

# Local conformal flatness forces the Weyl tensor to vanish

Away from dimension `2`, the
Weyl tensor of a locally conformally flat metric vanishes at every point. This is the easy half of
the Weyl–Schouten theorem.

```lean
Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat.weylTensor_eq_zero.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  {g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x}
  (hg : g.IsLocallyConformallyFlat) (hn : Module.finrank ℝ E ≠ 2) (x : M) :
  (CovariantDerivative.leviCivitaConnection I M).weylTensor x = 0
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat](bundle-contmdiffriemannianmetric-islocallyconfor.md)

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)
- [Weyl tensor under conformal change](weyl-tensor-under-conformal-change.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat.weylTensor_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/Basic.html#Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat.weylTensor_eq_zero).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat.weylTensor_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/Basic.html#Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat.weylTensor_eq_zero)
- [Source of `Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat.weylTensor_eq_zero` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/Basic.lean#L168)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Yamabe/STATUS.md)
