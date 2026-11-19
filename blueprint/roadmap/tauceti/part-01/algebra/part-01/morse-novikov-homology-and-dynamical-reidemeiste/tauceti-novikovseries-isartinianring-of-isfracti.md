---
declaration: theorem
origin: cited
lean: TauCeti.NovikovSeries.isArtinianRing_of_isFractionRing
statement: formalized
proof: formalized
---

# TauCeti.NovikovSeries.isArtinianRing_of_isFractionRing

Over a domain, the total ring of fractions of the Novikov series on a finitely generated
abelian group, with any period homomorphism, is an Artinian ring.

```lean
TauCeti.NovikovSeries.isArtinianRing_of_isFractionRing.{u_1, u_2, u_3} {H : Type u_1}
  [AddCommGroup H] (R : Type u_2) [CommRing R] [IsDomain R] [AddGroup.FG H] (N : H →+ ℝ)
  (T : Type u_3) [CommRing T] [Algebra (TauCeti.NovikovSeries R H N) T]
  [IsFractionRing (TauCeti.NovikovSeries R H N) T] : IsArtinianRing T
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovSeries.isArtinianRing_of_isFractionRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/TotalQuotient.html#TauCeti.NovikovSeries.isArtinianRing_of_isFractionRing).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovSeries.isArtinianRing_of_isFractionRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/TotalQuotient.html#TauCeti.NovikovSeries.isArtinianRing_of_isFractionRing)
- [Source of `TauCeti.NovikovSeries.isArtinianRing_of_isFractionRing` in TauCeti/RingTheory/NovikovSeries/TotalQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/NovikovSeries/TotalQuotient.lean#L93)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseNovikov/STATUS.md)
