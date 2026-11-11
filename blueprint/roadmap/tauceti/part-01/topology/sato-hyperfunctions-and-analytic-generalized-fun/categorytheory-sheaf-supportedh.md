---
declaration: abbrev
origin: cited
lean: CategoryTheory.Sheaf.supportedH
statement: formalized
---

# CategoryTheory.Sheaf.supportedH

The cohomology `H_Sⁿ(W, F)` of `F` on `W` with supports in the closed subset `S`: the relative
cohomology of the inclusion `W ∖ S ⟶ W`.

```lean
CategoryTheory.Sheaf.supportedH.{u} {X : TopCat}
  (F : CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) AddCommGrpCat)
  (S : TopologicalSpace.Closeds ↑X) (W : TopologicalSpace.Opens ↑X) (n : ℕ) : Type u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.supportedH`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/SupportedCohomology.html#CategoryTheory.Sheaf.supportedH).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.supportedH`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/SupportedCohomology.html#CategoryTheory.Sheaf.supportedH)
- [Source of `CategoryTheory.Sheaf.supportedH` in TauCeti/Topology/Sheaves/SupportedCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/SupportedCohomology.lean#L144)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Hyperfunctions/STATUS.md)
