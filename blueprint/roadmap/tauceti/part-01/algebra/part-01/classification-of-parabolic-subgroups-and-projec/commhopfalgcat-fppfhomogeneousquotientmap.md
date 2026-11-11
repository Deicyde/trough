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
- [Source of `CommHopfAlgCat.fppfHomogeneousQuotientMap` in TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Map.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Map.lean#L98)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FlagVarieties/STATUS.md)
