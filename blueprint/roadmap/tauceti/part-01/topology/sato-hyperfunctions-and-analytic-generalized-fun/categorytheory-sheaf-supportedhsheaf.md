---
declaration: abbrev
origin: cited
lean: CategoryTheory.Sheaf.supportedHSheaf
statement: formalized
---

# CategoryTheory.Sheaf.supportedHSheaf

The local cohomology sheaf `𝓗_Sⁿ(F)` of `F` with supports in the closed subset `S`: the
sheafification of the presheaf `W ↦ H_Sⁿ(W, F)` of cohomology with supports in `S`.

```lean
CategoryTheory.Sheaf.supportedHSheaf.{u} {X : TopCat}
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) AddCommGrpCat)
  (S : TopologicalSpace.Closeds ↑X) (n : ℕ) :
  CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) AddCommGrpCat
```

## Depends on

- [CategoryTheory.Sheaf.supportedH](categorytheory-sheaf-supportedh.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.supportedHSheaf`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Basic.html#CategoryTheory.Sheaf.supportedHSheaf).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.supportedHSheaf`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/LocalCohomology/Basic.html#CategoryTheory.Sheaf.supportedHSheaf)
- [Source of `CategoryTheory.Sheaf.supportedHSheaf` in TauCeti/Topology/Sheaves/LocalCohomology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/LocalCohomology/Basic.lean#L274)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Hyperfunctions/STATUS.md)
