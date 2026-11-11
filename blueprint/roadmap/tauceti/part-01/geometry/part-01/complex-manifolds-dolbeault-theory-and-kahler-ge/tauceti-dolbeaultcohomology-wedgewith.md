---
declaration: def
origin: cited
lean: TauCeti.dolbeaultCohomology.wedgeWith
statement: formalized
---

# TauCeti.dolbeaultCohomology.wedgeWith

A continuous complex-bilinear coefficient pairing induces a product on Dolbeault cohomology,
adding both holomorphic and antiholomorphic degrees.

```lean
TauCeti.dolbeaultCohomology.wedgeWith.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {M : Type u_2} [TopologicalSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] {F : Type u_3} {G : Type u_4} {H : Type u_5}
  [NormedAddCommGroup F] [NormedSpace ℂ F] [NormedAddCommGroup G] [NormedSpace ℂ G]
  [NormedAddCommGroup H] [NormedSpace ℂ H] (μ : F →L[ℂ] G →L[ℂ] H) (p q r s : ℕ) :
  TauCeti.dolbeaultCohomology E M F p q →ₗ[ℂ]
    TauCeti.dolbeaultCohomology E M G r s →ₗ[ℂ] TauCeti.dolbeaultCohomology E M H (p + r) (q + s)
```

## Depends on

- [TauCeti.dolbeaultCohomology](tauceti-dolbeaultcohomology.md)

## Proof depends on

- [`∂bar² = 0` on a complex manifold](bar2-0-on-a-complex-manifold.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dolbeaultCohomology.wedgeWith`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Wedge.html#TauCeti.dolbeaultCohomology.wedgeWith).

## Sources

- [Tau Ceti documentation: `TauCeti.dolbeaultCohomology.wedgeWith`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Wedge.html#TauCeti.dolbeaultCohomology.wedgeWith)
- [Source of `TauCeti.dolbeaultCohomology.wedgeWith` in TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Wedge.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Wedge.lean#L134)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
