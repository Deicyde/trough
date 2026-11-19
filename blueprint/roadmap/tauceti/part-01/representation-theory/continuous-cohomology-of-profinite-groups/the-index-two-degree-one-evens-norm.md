---
declaration: def
origin: cited
lean: TauCeti.ContCohomology.evensNormIndexTwo
statement: formalized
---

# The index-two degree-one Evens norm

**The index-two degree-one Evens norm** `Nᴱᵛ : H¹(U, 𝔽₂) → H²(G, 𝔽₂)` for an open subgroup
`U` of index two: the graph class of a continuous homomorphism representing the class, which
`homClass_surjective` provides and `graphClass_representative_independent` makes irrelevant. On
the class of `α` it is `graphClass U hU α` (`evensNormIndexTwo_homClass`). It is a function and not
an additive map.

```lean
TauCeti.ContCohomology.evensNormIndexTwo.{u} {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [LocallyCompactSpace G] (U : OpenSubgroup G) (hU : (↑U).index = 2)
  (x : ↑(continuousCohomology 1 (TauCeti.trivialF2 ↥↑U)).toModuleCat) :
  ↑(continuousCohomology 2 (TauCeti.trivialF2 G)).toModuleCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.evensNormIndexTwo`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/IndexTwoNorm.html#TauCeti.ContCohomology.evensNormIndexTwo).

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.evensNormIndexTwo`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/IndexTwoNorm.html#TauCeti.ContCohomology.evensNormIndexTwo)
- [Source of `TauCeti.ContCohomology.evensNormIndexTwo` in TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/IndexTwoNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/IndexTwoNorm.lean#L75)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
