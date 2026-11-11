---
declaration: theorem
origin: cited
lean: TauCeti.SmoothAlmostComplexStructure.mextDerivₗ_eq_del_add_delBar_ofComplexManifold
statement: formalized
proof: formalized
---

# `d = ∂ + ∂bar` on a complex manifold

On the complex-valued smooth forms of every degree
on a complex manifold, the exterior derivative is the sum of `∂` and `∂bar`.

```lean
TauCeti.SmoothAlmostComplexStructure.mextDerivₗ_eq_del_add_delBar_ofComplexManifold.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] {M : Type u_2} [TopologicalSpace M]
  [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace ℂ F] {k : ℕ}
  (φ : TauCeti.SmoothForm (modelWithCornersSelf ℝ E) M F k) :
  (TauCeti.mextDerivₗ (modelWithCornersSelf ℝ E) k) φ =
    (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold E M).del φ +
      (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold E M).delBar φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [TauCeti.ContMDiffAlmostComplexStructure](../../../analysis/part-01/elliptic-analysis-of-pseudoholomorphic-curves/tauceti-contmdiffalmostcomplexstructure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothAlmostComplexStructure.mextDerivₗ_eq_del_add_delBar_ofComplexManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/ComplexManifold.html#TauCeti.SmoothAlmostComplexStructure.mextDeriv%E2%82%97_eq_del_add_delBar_ofComplexManifold).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothAlmostComplexStructure.mextDerivₗ_eq_del_add_delBar_ofComplexManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/ComplexManifold.html#TauCeti.SmoothAlmostComplexStructure.mextDeriv%E2%82%97_eq_del_add_delBar_ofComplexManifold)
- [Source of `TauCeti.SmoothAlmostComplexStructure.mextDerivₗ_eq_del_add_delBar_ofComplexManifold` in TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/ComplexManifold.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/ComplexManifold.lean#L148)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
