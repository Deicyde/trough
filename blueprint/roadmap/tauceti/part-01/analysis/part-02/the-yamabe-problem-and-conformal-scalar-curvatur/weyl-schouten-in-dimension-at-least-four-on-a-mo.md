---
declaration: theorem
origin: cited
lean: Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space
statement: formalized
proof: formalized
---

# Weyl–Schouten in dimension at least four, on a model space

An arbitrary smooth
Riemannian metric is locally conformally flat if and only if its Weyl tensor vanishes.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Christoffel formula of the first kind](../../../geometry/part-02/manifold/part-01/the-christoffel-formula-of-the-first-kind.md)
- [CovariantDerivative.conformalFlatteningForm](covariantderivative-conformalflatteningform.md)
- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)
- [The Ricci identity](../../../geometry/part-02/manifold/part-04/the-ricci-identity.md)
- [The second Bianchi identity](../../../geometry/part-02/manifold/part-04/the-second-bianchi-identity.md)

## Lean

Formalized in Tau Ceti as [`Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.html#Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space).

## Sources

- [Tau Ceti documentation: `Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.html#Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space)
- [Source of `Bundle.ContMDiffRiemannianMetric.isLocallyConformallyFlat_iff_weylTensor_eq_zero_model_space` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature/ConformallyFlat/ModelSpace.lean#L99)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Yamabe/STATUS.md)
