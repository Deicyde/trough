---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_cottonTensor_eq_zero_model_space, Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space
statement: formalized
proof: formalized
---

# Weyl–Schouten in dimension three, on a model space

An arbitrary smooth Riemannian
metric is locally conformally flat if and only if its Cotton tensor vanishes.

```lean
Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_cottonTensor_eq_zero_model_space.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  (g :
    Bundle.ContMDiffRiemannianMetric (modelWithCornersSelf ℝ E) (↑⊤) E fun x =>
      TangentSpace (modelWithCornersSelf ℝ E) x)
  (hn : Module.finrank ℝ E = 3) :
  g.IsLocallyConformallyFlat ↔
    ∀ (x : E),
      (CovariantDerivative.leviCivitaConnection (modelWithCornersSelf ℝ E) E).cottonTensor x = 0
```

## Depends on

- [Bundle.ContMDiffRiemannianMetric.IsLocallyConformallyFlat](bundle-contmdiffriemannianmetric-islocallyconfor.md)
- [CovariantDerivative.cottonTensor](covariantderivative-cottontensor.md)

## Proof depends on

- [The Christoffel formula of the first kind](../manifold/part-01/the-christoffel-formula-of-the-first-kind.md)
- [Curvature under conformal change](../curvature-jacobi-fields-submanifolds-and-bochner/curvature-under-conformal-change.md)
- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)
- [Local conformal flatness forces the Weyl tensor to vanish](local-conformal-flatness-forces-the-weyl-tensor.md)
- [The Ricci identity](../manifold/part-02/the-ricci-identity.md)
- [The second Bianchi identity](../curvature-jacobi-fields-submanifolds-and-bochner/the-second-bianchi-identity.md)
- [Weyl tensor under conformal change](weyl-tensor-under-conformal-change.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_cottonTensor_eq_zero_model_space`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.html#Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_cottonTensor_eq_zero_model_space).

## Other forms

**Weyl–Schouten in dimension at least four, on a model space.** Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.html#Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space).

```lean
Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  (g :
    Bundle.ContMDiffRiemannianMetric (modelWithCornersSelf ℝ E) (↑⊤) E fun x =>
      TangentSpace (modelWithCornersSelf ℝ E) x)
  (hn : 4 ≤ Module.finrank ℝ E) :
  g.IsLocallyConformallyFlat ↔
    ∀ (x : E),
      (CovariantDerivative.leviCivitaConnection (modelWithCornersSelf ℝ E) E).weylTensor x = 0
```

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_cottonTensor_eq_zero_model_space`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.html#Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_cottonTensor_eq_zero_model_space)
- [Source of `Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_cottonTensor_eq_zero_model_space` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.lean#L116)
