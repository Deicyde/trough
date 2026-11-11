---
declaration: theorem
origin: cited
lean: OpenSubgroup.exact_cor_cup_of_index_two
statement: formalized
proof: formalized
---

# The index-two corestriction--cup sequence is exact in every degree

The kernel of
cupping with the subgroup character consists exactly of the corestrictions from `U`.

```lean
OpenSubgroup.exact_cor_cup_of_index_two.{u} {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] (U : OpenSubgroup G)
  (hU : (↑U).index = 2) (n : ℕ) :
  Function.Exact ⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.trivialF2CorMap G ↑U ⋯ n)) fun x =>
    (((TauCeti.trivialF2TopPairing G).cup n 1) x) (U.indexTwoCharacterClass hU)
```

## Depends on

- [Shapiro's lemma in degree one](../homological/shapiros-lemma-in-degree-one.md)

## Lean

Formalized in Tau Ceti as [`OpenSubgroup.exact_cor_cup_of_index_two`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/IndexTwo/CupExact.html#OpenSubgroup.exact_cor_cup_of_index_two).

## Sources

- [Tau Ceti documentation: `OpenSubgroup.exact_cor_cup_of_index_two`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/IndexTwo/CupExact.html#OpenSubgroup.exact_cor_cup_of_index_two)
- [Source of `OpenSubgroup.exact_cor_cup_of_index_two` in TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/IndexTwo/CupExact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/ContCohomology/Corestriction/IndexTwo/CupExact.lean#L305)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
