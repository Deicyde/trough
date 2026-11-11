---
declaration: def
origin: cited
lean: TauCeti.Topology.finiteCechCohomologyIso
statement: formalized
---

# Finite covers compute Čech cohomology on a compact space

On a compact space, the colimit
of the Čech cohomologies over the finite indexed covers is canonically isomorphic to the Čech
cohomology, naturally in the presheaf. No separation axiom is assumed.

```lean
TauCeti.Topology.finiteCechCohomologyIso.{v', u, u'} (X : TopCat) (A : Type u')
  [CategoryTheory.Category.{v', u'} A] [CategoryTheory.Preadditive A]
  [CategoryTheory.Limits.HasProducts A] [CategoryTheory.CategoryWithHomology A]
  [CategoryTheory.Limits.HasColimitsOfShape (TauCeti.Topology.PointOpenCover ↑X) A] (n : ℕ)
  [CompactSpace ↑X]
  [CategoryTheory.Limits.HasColimitsOfShape (TauCeti.Topology.FiniteOpenCover ↑X) A] :
  TauCeti.CategoryTheory.cechCohomology A TauCeti.Topology.FiniteOpenCover.toFormalCoproduct ⋯ n ≅
    TauCeti.Topology.cechCohomology X A n
```

## Depends on

- [Mutually cofinal systems of families have canonically isomorphic Čech cohomology](mutually-cofinal-systems-of-families-have-canoni.md)
- [TauCeti.Topology.cechCohomology](tauceti-topology-cechcohomology.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Topology.finiteCechCohomologyIso`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cech/Cofinal.html#TauCeti.Topology.finiteCechCohomologyIso).

## Sources

- [Tau Ceti documentation: `TauCeti.Topology.finiteCechCohomologyIso`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cech/Cofinal.html#TauCeti.Topology.finiteCechCohomologyIso)
- [Source of `TauCeti.Topology.finiteCechCohomologyIso` in TauCeti/Topology/Sheaves/Cech/Cofinal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/Cech/Cofinal.lean#L103)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
