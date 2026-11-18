---
declaration: def
origin: cited
lean: CommHopfAlgCat.fppfHomogeneousQuotientMap
statement: formalized
---

# CommHopfAlgCat.fppfHomogeneousQuotientMap

The projection `G/P ⟶ G/Q` for `P ⊆ Q`, as a morphism of fppf sheaves.
Here `I` defines `P` and `J` defines `Q`, so its hypothesis is `J ≤ I`.

```lean
CommHopfAlgCat.fppfHomogeneousQuotientMap.{u} {R : Type u} [CommRing R] (H : CommHopfAlgCat R)
  {I J : TauCeti.HopfIdeal R ↑H} (hJI : J ≤ I) :
  H.fppfHomogeneousQuotient I ⟶ H.fppfHomogeneousQuotient J
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CommHopfAlgCat.fppfHomogeneousQuotientMap`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Map.html#CommHopfAlgCat.fppfHomogeneousQuotientMap).

## Sources

- [Tau Ceti documentation: `CommHopfAlgCat.fppfHomogeneousQuotientMap`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Map.html#CommHopfAlgCat.fppfHomogeneousQuotientMap)
- [Source of `CommHopfAlgCat.fppfHomogeneousQuotientMap` in TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Map.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Map.lean#L99)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FlagVarieties/STATUS.md)
