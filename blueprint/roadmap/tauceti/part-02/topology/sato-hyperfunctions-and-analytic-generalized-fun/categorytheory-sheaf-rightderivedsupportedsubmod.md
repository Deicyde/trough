---
declaration: def
origin: cited
lean: CategoryTheory.Sheaf.rightDerivedSupportedSubmoduleSectionsIso
statement: formalized
---

# CategoryTheory.Sheaf.rightDerivedSupportedSubmoduleSectionsIso

Right derived supported sections are the supported Ext groups, naturally in the
coefficient sheaf. The target evaluates the existing supported cohomology presheaf on `W`.

```lean
CategoryTheory.Sheaf.rightDerivedSupportedSubmoduleSectionsIso.{u} {X : TopCat} {R : Type u}
  [CommRing R] (S : TopologicalSpace.Closeds ↑X) (W : TopologicalSpace.Opens ↑X) (n : ℕ) :
  (CategoryTheory.Sheaf.supportedSubmoduleSectionsFunctor S W).rightDerived n ≅
    (CategoryTheory.Sheaf.supportedModuleHPresheafFunctor S n).comp
      ((CategoryTheory.evaluation (TopologicalSpace.Opens ↑X)ᵒᵖ (ModuleCat R)).obj (Opposite.op W))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.rightDerivedSupportedSubmoduleSectionsIso`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/SupportedCohomology/Derived.html#CategoryTheory.Sheaf.rightDerivedSupportedSubmoduleSectionsIso).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.rightDerivedSupportedSubmoduleSectionsIso`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/SupportedCohomology/Derived.html#CategoryTheory.Sheaf.rightDerivedSupportedSubmoduleSectionsIso)
- [Source of `CategoryTheory.Sheaf.rightDerivedSupportedSubmoduleSectionsIso` in TauCeti/Topology/Sheaves/SupportedCohomology/Derived.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Sheaves/SupportedCohomology/Derived.lean#L108)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Hyperfunctions/STATUS.md)
