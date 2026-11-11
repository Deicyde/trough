---
declaration: def
origin: cited
lean: CategoryTheory.Sheaf.rightDerivedΓIsoOfIsFlasque
statement: formalized
---

# CategoryTheory.Sheaf.rightDerivedΓIsoOfIsFlasque

A functorial flasque resolution computes the native right derived functors of global
sections, naturally in the sheaf. No injectivity of the terms of the resolution is assumed.

```lean
CategoryTheory.Sheaf.rightDerivedΓIsoOfIsFlasque.{u} {X : TopCat} {R : Type u} [CommRing R]
  [(CategoryTheory.Sheaf.Γ (Opens.grothendieckTopology ↑X) (ModuleCat R)).Additive]
  (K :
    CategoryTheory.Functor (CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R))
      (CochainComplex (CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R)) ℕ))
  (ι :
    CochainComplex.single₀ (CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R)) ⟶ K)
  [∀ (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R)), QuasiIso (ι.app F)]
  (hK :
    ∀ (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R)) (n : ℕ),
      TopCat.Presheaf.IsFlasque ((K.obj F).X n).obj)
  (n : ℕ) :
  (CategoryTheory.Sheaf.Γ (Opens.grothendieckTopology ↑X) (ModuleCat R)).rightDerived n ≅
    K.comp
      (((CategoryTheory.Sheaf.Γ (Opens.grothendieckTopology ↑X) (ModuleCat R)).mapHomologicalComplex
            (ComplexShape.up ℕ)).comp
        (HomologicalComplex.homologyFunctor (ModuleCat R) (ComplexShape.up ℕ) n))
```

## Depends on

- [CategoryTheory.Functor.rightDerivedIsoOfResolution](categorytheory-functor-rightderivedisoofresoluti.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.rightDerivedΓIsoOfIsFlasque`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Flasque/Resolution.html#CategoryTheory.Sheaf.rightDerived%CE%93IsoOfIsFlasque).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.rightDerivedΓIsoOfIsFlasque`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Flasque/Resolution.html#CategoryTheory.Sheaf.rightDerived%CE%93IsoOfIsFlasque)
- [Source of `CategoryTheory.Sheaf.rightDerivedΓIsoOfIsFlasque` in TauCeti/Topology/Sheaves/Flasque/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/Flasque/Resolution.lean#L113)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
