---
declaration: def
origin: cited
lean: CovariantDerivative.cottonTensor
statement: formalized
---

# CovariantDerivative.cottonTensor

The Cotton tensor `C(u, v, w) = (∇_w P)(u, v) - (∇_v P)(u, w)` of a smooth connection, where
`P` is the Schouten tensor and `∇P` is `CovariantDerivative.derivSchoutenTensor`. The usual
formula on vector fields holds for a smooth metric (see
`CovariantDerivative.cottonTensor_apply_of_mdifferentiableAt`); otherwise `∇P`, and hence the
Cotton tensor, may be `0`.

```lean
CovariantDerivative.cottonTensor.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I (↑⊤) M] [Bundle.RiemannianBundle (TangentSpace I)]
  (cov : CovariantDerivative I E (TangentSpace I)) [cov.ContMDiffCovariantDerivative ↑⊤] (x : M) :
  TangentSpace I x →ₗ[ℝ] TangentSpace I x →ₗ[ℝ] TangentSpace I x →ₗ[ℝ] ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CovariantDerivative.cottonTensor`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Cotton.html#CovariantDerivative.cottonTensor).

## Sources

- [Tau Ceti documentation: `CovariantDerivative.cottonTensor`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Cotton.html#CovariantDerivative.cottonTensor)
- [Source of `CovariantDerivative.cottonTensor` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Cotton.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/Cotton.lean#L109)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Yamabe/STATUS.md)
