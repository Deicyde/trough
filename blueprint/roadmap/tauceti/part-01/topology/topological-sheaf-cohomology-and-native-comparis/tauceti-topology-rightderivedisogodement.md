---
declaration: def
origin: cited
lean: TauCeti.Topology.rightDerivedΓIsoGodement
statement: formalized
---

# TauCeti.Topology.rightDerivedΓIsoGodement

Native derived global sections are computed by the global sections of the Godement
resolution, naturally in the module sheaf.

```lean
TauCeti.Topology.rightDerivedΓIsoGodement.{u} {X : TopCat} {R : Type u} [CommRing R]
  [(CategoryTheory.Sheaf.Γ (Opens.grothendieckTopology ↑X) (ModuleCat R)).Additive] (n : ℕ) :
  (CategoryTheory.Sheaf.Γ (Opens.grothendieckTopology ↑X) (ModuleCat R)).rightDerived n ≅
    (TauCeti.Topology.godementResolution (ModuleCat R) X).comp
      (((CategoryTheory.Sheaf.Γ (Opens.grothendieckTopology ↑X) (ModuleCat R)).mapHomologicalComplex
            (ComplexShape.up ℕ)).comp
        (HomologicalComplex.homologyFunctor (ModuleCat R) (ComplexShape.up ℕ) n))
```

## Depends on

- [CategoryTheory.Sheaf.rightDerivedΓIsoOfIsFlasque](categorytheory-sheaf-rightderivedisoofisflasque.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Topology.rightDerivedΓIsoGodement`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cohomology/Godement.html#TauCeti.Topology.rightDerived%CE%93IsoGodement).

## Sources

- [Tau Ceti documentation: `TauCeti.Topology.rightDerivedΓIsoGodement`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cohomology/Godement.html#TauCeti.Topology.rightDerived%CE%93IsoGodement)
- [Source of `TauCeti.Topology.rightDerivedΓIsoGodement` in TauCeti/Topology/Sheaves/Cohomology/Godement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/Cohomology/Godement.lean#L45)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
