---
declaration: abbrev
origin: cited
lean: CategoryTheory.Sheaf.supportedModuleH
statement: formalized
---

# CategoryTheory.Sheaf.supportedModuleH

The cohomology `H_Sⁿ(W, F)` of a sheaf of `R`-modules `F` on `W` with supports in the closed
subset `S`: the `R`-module `Extⁿ(Q_S(W), F)`.

```lean
CategoryTheory.Sheaf.supportedModuleH.{u} {X : TopCat} {R : Type u} [CommRing R]
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R))
  (S : TopologicalSpace.Closeds ↑X) (W : TopologicalSpace.Opens ↑X) (n : ℕ) : Type u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.supportedModuleH`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/SupportedCohomology/Module.html#CategoryTheory.Sheaf.supportedModuleH).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.supportedModuleH`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/SupportedCohomology/Module.html#CategoryTheory.Sheaf.supportedModuleH)
- [Source of `CategoryTheory.Sheaf.supportedModuleH` in TauCeti/Topology/Sheaves/SupportedCohomology/Module.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Sheaves/SupportedCohomology/Module.lean#L217)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Hyperfunctions/STATUS.md)
