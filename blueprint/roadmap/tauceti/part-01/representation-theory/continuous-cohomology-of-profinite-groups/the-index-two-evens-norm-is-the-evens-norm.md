---
declaration: theorem
origin: cited
lean: OpenSubgroup.evensNormIndexTwo_eq
statement: formalized
proof: formalized
---

# The index-two Evens norm is the Evens norm

for `U` of index two, the explicit index-two
norm `evensNormIndexTwo U hU`, defined by the graph cocycle, is the general Evens norm `N_U^G` on
`H¹(U, 𝔽₂)`, up to the transport of degrees from `Fintype.card (G ⧸ U) * 1` to `2`. As in
`evensNorm_eq_graphClass`, finite index and local compactness are derived from the other
assumptions.

```lean
OpenSubgroup.evensNormIndexTwo_eq.{u} {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] (U : OpenSubgroup G) [CompactSpace ↥↑U] [Fintype (G ⧸ ↑U)]
  (hU : (↑U).index = 2) (x : ↑(continuousCohomology 1 (TauCeti.trivialF2 ↥↑U)).toModuleCat) :
  TauCeti.ContCohomology.evensNormIndexTwo U hU x =
    (CategoryTheory.ConcreteCategory.hom
        (TauCeti.ContinuousCohomology.degreeCast (TauCeti.trivialF2 G) ⋯).hom)
      (U.evensNorm x)
```

## Depends on

- [The Evens norm](the-evens-norm.md)
- [The index-two degree-one Evens norm](the-index-two-degree-one-evens-norm.md)

## Proof depends on

- [Frobenius reciprocity for `coind₁`, uniqueness](../other-results/frobenius-reciprocity-for-coind1-uniqueness.md)

## Lean

Formalized in Tau Ceti as [`OpenSubgroup.evensNormIndexTwo_eq`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/IndexTwo.html#OpenSubgroup.evensNormIndexTwo_eq).

## Sources

- [Tau Ceti documentation: `OpenSubgroup.evensNormIndexTwo_eq`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/IndexTwo.html#OpenSubgroup.evensNormIndexTwo_eq)
- [Source of `OpenSubgroup.evensNormIndexTwo_eq` in TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/IndexTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/IndexTwo.lean#L98)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
