---
declaration: def
origin: cited
lean: IsQuotientCoveringMap.cohomologyIsoGroupCohomology
statement: formalized
---

# The local-coefficient cohomology of the base of a contractible free cover is group cohomology

for the quotient covering map `p : E ⟶ B` of an action of `G` with contractible total
space and a representation `A` of `G`, the direct cohomology `Hⁿ(B; L_A)` with values in the
associated local system is Mathlib's `groupCohomology A n`.

```lean
IsQuotientCoveringMap.cohomologyIsoGroupCohomology.{u} {E B : TopCat} {p : E ⟶ B} {G : Type u}
  [Group G] [MulAction G ↑E]
  (hG : IsQuotientCoveringMap (⇑(CategoryTheory.ConcreteCategory.hom p)) G) (k : Type u)
  [CommRing k] (A : Rep.{u, u, u} k G) [ContractibleSpace ↑E] (n : ℕ) :
  (hG.associatedLocalSystem k A).cohomology n ≅ groupCohomology A n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsQuotientCoveringMap.cohomologyIsoGroupCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Twisted/Direct/GroupCohomology.html#IsQuotientCoveringMap.cohomologyIsoGroupCohomology).

## Sources

- [Tau Ceti documentation: `IsQuotientCoveringMap.cohomologyIsoGroupCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Twisted/Direct/GroupCohomology.html#IsQuotientCoveringMap.cohomologyIsoGroupCohomology)
- [Source of `IsQuotientCoveringMap.cohomologyIsoGroupCohomology` in TauCeti/AlgebraicTopology/Cohomology/Twisted/Direct/GroupCohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/Twisted/Direct/GroupCohomology.lean#L491)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
