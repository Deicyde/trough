---
declaration: abbrev
origin: cited
lean: TauCeti.Topology.cechCohomology
statement: formalized
---

# TauCeti.Topology.cechCohomology

The degree `n` Čech cohomology of presheaves on `X` with values in `A`: the colimit over the
point-neighborhood covers `U`, ordered by refinement, of the degree `n` cohomology of the Čech
complexes `Č(U, P)`. The transition maps are induced by refinement maps
(`TauCeti.CategoryTheory.cechCohomologyDiagram_map`).

```lean
TauCeti.Topology.cechCohomology.{v', u, u'} (X : TopCat) (A : Type u')
  [CategoryTheory.Category.{v', u'} A] [CategoryTheory.Preadditive A]
  [CategoryTheory.Limits.HasProducts A] [CategoryTheory.CategoryWithHomology A]
  [CategoryTheory.Limits.HasColimitsOfShape (TauCeti.Topology.PointOpenCover ↑X) A] (n : ℕ) :
  CategoryTheory.Functor (CategoryTheory.Functor (TopologicalSpace.Opens ↑X)ᵒᵖ A) A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Topology.cechCohomology`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cech/Colimit.html#TauCeti.Topology.cechCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.Topology.cechCohomology`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cech/Colimit.html#TauCeti.Topology.cechCohomology)
- [Source of `TauCeti.Topology.cechCohomology` in TauCeti/Topology/Sheaves/Cech/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/Cech/Colimit.lean#L66)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
