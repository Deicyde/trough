---
declaration: abbrev
origin: cited
lean: CategoryTheory.Sheaf.supportedModuleHSheaf
statement: formalized
---

# CategoryTheory.Sheaf.supportedModuleHSheaf

The local cohomology sheaf `𝓗_Sⁿ(F)`, defined by sheafifying the module-valued supported
cohomology presheaf.

```lean
CategoryTheory.Sheaf.supportedModuleHSheaf.{u} {X : TopCat} {R : Type u} [CommRing R]
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R))
  (S : TopologicalSpace.Closeds ↑X) (n : ℕ) :
  CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.supportedModuleHSheaf`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Module.html#CategoryTheory.Sheaf.supportedModuleHSheaf).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.supportedModuleHSheaf`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Module.html#CategoryTheory.Sheaf.supportedModuleHSheaf)
- [Source of `CategoryTheory.Sheaf.supportedModuleHSheaf` in TauCeti/Topology/Sheaves/LocalCohomology/Module.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Sheaves/LocalCohomology/Module.lean#L39)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Hyperfunctions/STATUS.md)
