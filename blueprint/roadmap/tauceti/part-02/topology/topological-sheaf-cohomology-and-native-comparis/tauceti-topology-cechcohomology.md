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
- [Source of `TauCeti.Topology.cechCohomology` in TauCeti/Topology/Sheaves/Cech/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Sheaves/Cech/Colimit.lean#L68)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
