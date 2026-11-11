---
declaration: def
origin: cited
lean: CategoryTheory.ShortComplex.ShortExact.cechCohomologyδ
statement: formalized
---

# The connecting map of Čech cohomology

**The connecting map of Čech cohomology** for a short exact sequence
`0 ⟶ F₁ ⟶ F₂ ⟶ F₃ ⟶ 0` of sheaves of modules on a compact normal space: the map
`Hⁿ(X, F₃) ⟶ Hⁿ⁺¹(X, F₁)`. It is characterized by
`CategoryTheory.ShortComplex.ShortExact.cechCohomologyδ_naturality_of_presheaf`.

```lean
CategoryTheory.ShortComplex.ShortExact.cechCohomologyδ.{u} {X : TopCat} {R : Type u} [Ring R]
  {S :
    CategoryTheory.ShortComplex
      (CategoryTheory.Sheaf (Opens.grothendieckTopology ↑X) (ModuleCat R))}
  [CategoryTheory.HasSheafify (Opens.grothendieckTopology ↑X) (ModuleCat R)] [CompactSpace ↑X]
  [NormalSpace ↑X] [(Opens.grothendieckTopology ↑X).WEqualsLocallyBijective (ModuleCat R)]
  (hS : S.ShortExact) (n : ℕ) :
  (TauCeti.Topology.cechCohomology X (ModuleCat R) n).obj S.X₃.obj ⟶
    (TauCeti.Topology.cechCohomology X (ModuleCat R) (n + 1)).obj S.X₁.obj
```

## Depends on

- [TauCeti.Topology.cechCohomology](tauceti-topology-cechcohomology.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.ShortComplex.ShortExact.cechCohomologyδ`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cech/LongExactSequence.html#CategoryTheory.ShortComplex.ShortExact.cechCohomology%CE%B4).

## Sources

- [Tau Ceti documentation: `CategoryTheory.ShortComplex.ShortExact.cechCohomologyδ`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/Cech/LongExactSequence.html#CategoryTheory.ShortComplex.ShortExact.cechCohomology%CE%B4)
- [Source of `CategoryTheory.ShortComplex.ShortExact.cechCohomologyδ` in TauCeti/Topology/Sheaves/Cech/LongExactSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/Cech/LongExactSequence.lean#L128)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
