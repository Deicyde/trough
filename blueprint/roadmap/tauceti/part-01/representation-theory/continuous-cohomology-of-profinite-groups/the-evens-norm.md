---
declaration: def
origin: cited
lean: OpenSubgroup.evensNorm
statement: formalized
---

# The Evens norm

**The Evens norm** `N_U^G : Hⁿ(U, 𝔽₂) → H^{l n}(G, 𝔽₂)`, for `l` the index of `U`: the
tensor norm of a homogeneous cocycle representing the class, computed with the default
transversal. By `evensNorm_cochainClass` neither the representative nor the transversal matters.
It is a function and not an additive map.

```lean
OpenSubgroup.evensNorm.{u} {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  (U : OpenSubgroup G) [(↑U).FiniteIndex] [CompactSpace ↥↑U] [Fintype (G ⧸ ↑U)] {n : ℕ}
  (x : ↑(continuousCohomology n (TauCeti.trivialF2 ↥↑U)).toModuleCat) :
  ↑(continuousCohomology (Fintype.card (G ⧸ ↑U) * n) (TauCeti.trivialF2 G)).toModuleCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`OpenSubgroup.evensNorm`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/Basic.html#OpenSubgroup.evensNorm).

## Sources

- [Tau Ceti documentation: `OpenSubgroup.evensNorm`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/Basic.html#OpenSubgroup.evensNorm)
- [Source of `OpenSubgroup.evensNorm` in TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/Basic.lean#L53)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
