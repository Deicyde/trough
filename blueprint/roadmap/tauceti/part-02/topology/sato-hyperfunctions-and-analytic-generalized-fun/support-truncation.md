---
declaration: theorem
origin: cited
lean: CategoryTheory.Sheaf.subsingleton_supportedModuleH_of_isZero_supportedModuleHSheaf
statement: formalized
proof: formalized
---

# Support truncation

If the local cohomology sheaves `𝓗_S^q(F)` vanish for all `q < n`,
then the cohomology modules `H_S^q(W, F)` with supports in `S` vanish for all `q < n` and every
open `W`.

```lean
CategoryTheory.Sheaf.subsingleton_supportedModuleH_of_isZero_supportedModuleHSheaf.{u} {X : TopCat}
  {R : Type u} [CommRing R] (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R))
  (S : TopologicalSpace.Closeds ↑X) {n : ℕ}
  (h : ∀ q < n, CategoryTheory.Limits.IsZero (F.supportedModuleHSheaf S q)) {q : ℕ} (hq : q < n)
  (W : TopologicalSpace.Opens ↑X) : Subsingleton (F.supportedModuleH S W q)
```

## Depends on

- [CategoryTheory.Sheaf.supportedModuleH](categorytheory-sheaf-supportedmoduleh.md)
- [CategoryTheory.Sheaf.supportedModuleHSheaf](categorytheory-sheaf-supportedmodulehsheaf.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.subsingleton_supportedModuleH_of_isZero_supportedModuleHSheaf`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Edge.html#CategoryTheory.Sheaf.subsingleton_supportedModuleH_of_isZero_supportedModuleHSheaf).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.subsingleton_supportedModuleH_of_isZero_supportedModuleHSheaf`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Edge.html#CategoryTheory.Sheaf.subsingleton_supportedModuleH_of_isZero_supportedModuleHSheaf)
- [Source of `CategoryTheory.Sheaf.subsingleton_supportedModuleH_of_isZero_supportedModuleHSheaf` in TauCeti/Topology/Sheaves/LocalCohomology/Edge.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Sheaves/LocalCohomology/Edge.lean#L120)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Hyperfunctions/STATUS.md)
