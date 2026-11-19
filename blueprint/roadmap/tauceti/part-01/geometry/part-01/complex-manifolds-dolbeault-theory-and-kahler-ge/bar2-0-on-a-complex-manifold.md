---
declaration: theorem
origin: cited
lean: TauCeti.SmoothAlmostComplexStructure.delBar_delBar_ofComplexManifold
statement: formalized
proof: formalized
---

# `∂bar² = 0` on a complex manifold

This is the identity making the forms of types `(p,•)`
with the operator `∂bar` the Dolbeault complex.

```lean
TauCeti.SmoothAlmostComplexStructure.delBar_delBar_ofComplexManifold.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {M : Type u_2} [TopologicalSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℂ F] {k : ℕ} (φ : TauCeti.SmoothForm (modelWithCornersSelf ℝ E) M F k) :
  (TauCeti.SmoothAlmostComplexStructure.ofComplexManifold E M).delBar
      ((TauCeti.SmoothAlmostComplexStructure.ofComplexManifold E M).delBar φ) =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [`d = ∂ + ∂bar` on a complex manifold](d-bar-on-a-complex-manifold.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothAlmostComplexStructure.delBar_delBar_ofComplexManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/ComplexManifold.html#TauCeti.SmoothAlmostComplexStructure.delBar_delBar_ofComplexManifold).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothAlmostComplexStructure.delBar_delBar_ofComplexManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/ComplexManifold.html#TauCeti.SmoothAlmostComplexStructure.delBar_delBar_ofComplexManifold)
- [Source of `TauCeti.SmoothAlmostComplexStructure.delBar_delBar_ofComplexManifold` in TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/ComplexManifold.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/ComplexManifold.lean#L148)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
