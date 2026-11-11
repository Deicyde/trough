---
declaration: def
origin: cited
lean: TauCeti.dolbeaultCohomology.mkZeroEquiv
statement: formalized
---

# `H^(p,0)` is the space of holomorphic `p`-forms

The class map identifies the
`∂bar`-closed forms of type `(p,0)` with the Dolbeault cohomology `H^(p,0)_∂bar(M; F)`.

```lean
TauCeti.dolbeaultCohomology.mkZeroEquiv.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {M : Type u_2} [TopologicalSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℂ E) (↑⊤) M] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℂ F] (p : ℕ) :
  ↥(TauCeti.Dolbeault.closedForms E M F p 0) ≃ₗ[ℂ] TauCeti.dolbeaultCohomology E M F p 0
```

## Depends on

- [TauCeti.dolbeaultCohomology](tauceti-dolbeaultcohomology.md)

## Proof depends on

- [`∂bar² = 0` on a complex manifold](bar2-0-on-a-complex-manifold.md)
- [ModelWithCorners.restrictScalars](../complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dolbeaultCohomology.mkZeroEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Cohomology.html#TauCeti.dolbeaultCohomology.mkZeroEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.dolbeaultCohomology.mkZeroEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Cohomology.html#TauCeti.dolbeaultCohomology.mkZeroEquiv)
- [Source of `TauCeti.dolbeaultCohomology.mkZeroEquiv` in TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialForm/Dolbeault/Cohomology.lean#L79)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
