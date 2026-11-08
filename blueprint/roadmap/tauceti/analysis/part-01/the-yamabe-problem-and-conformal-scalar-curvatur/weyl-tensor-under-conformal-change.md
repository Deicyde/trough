---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.weylTensor_leviCivitaConnection_rescale
statement: formalized
proof: formalized
---

# Weyl tensor under conformal change

Away from dimension `2`, the fully covariant Weyl
tensor of a conformally rescaled smooth metric `f g` is `f` times that of `g`:
`W^(f g)(u, v, w, z) = f W^g(u, v, w, z)`. Equivalently, the Weyl tensor of type `(1, 3)` is
conformally invariant.

```lean
Bundle.ContMDiffRiemannianMetric.weylTensor_leviCivitaConnection_rescale.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I (↑⊤) M]
  (g : Bundle.ContMDiffRiemannianMetric I (↑⊤) E fun x => TangentSpace I x) {f : M → ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) (hf_pos : ∀ (x : M), 0 < f x)
  (hn : Module.finrank ℝ E ≠ 2) (x : M) (u v w z : TangentSpace I x) :
  (((((CovariantDerivative.leviCivitaConnection I M).weylTensor x) u) v) w) z =
    f x * (((((CovariantDerivative.leviCivitaConnection I M).weylTensor x) u) v) w) z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Curvature under conformal change](../../../geometry/part-01/curvature-jacobi-fields-submanifolds-and-bochner/curvature-under-conformal-change.md)
- [The Koszul formula](../../../geometry/part-01/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.weylTensor_leviCivitaConnection_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Conformal/Basic.html#Bundle.ContMDiffRiemannianMetric.weylTensor_leviCivitaConnection_rescale).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.weylTensor_leviCivitaConnection_rescale`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Conformal/Basic.html#Bundle.ContMDiffRiemannianMetric.weylTensor_leviCivitaConnection_rescale)
- [Source of `Bundle.ContMDiffRiemannianMetric.weylTensor_leviCivitaConnection_rescale` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Conformal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Conformal/Basic.lean#L603)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Yamabe/STATUS.md)
