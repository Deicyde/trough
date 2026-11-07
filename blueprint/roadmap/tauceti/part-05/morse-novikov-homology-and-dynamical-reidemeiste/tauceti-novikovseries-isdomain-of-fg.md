---
declaration: theorem
origin: cited
lean: TauCeti.NovikovSeries.isDomain_of_fg
statement: formalized
proof: formalized
---

# TauCeti.NovikovSeries.isDomain\_of\_fg

Over a domain, the Novikov ring of a finitely generated cancellative torsion-free commutative
monoid, for instance of a finitely generated torsion-free abelian group, is a domain for every
period homomorphism.

```lean
TauCeti.NovikovSeries.isDomain_of_fg.{u_1, u_2} {R : Type u_1} {H : Type u_2} [Ring R] [IsDomain R]
  [AddCancelCommMonoid H] [AddMonoid.FG H] [HasUniqueDiv H] (N : H →+ ℝ) :
  IsDomain (TauCeti.NovikovSeries R H N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovSeries.isDomain_of_fg`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/LeadingTerm.html#TauCeti.NovikovSeries.isDomain_of_fg).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovSeries.isDomain_of_fg`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/LeadingTerm.html#TauCeti.NovikovSeries.isDomain_of_fg)
- [Source of `TauCeti.NovikovSeries.isDomain_of_fg` in TauCeti/RingTheory/NovikovSeries/LeadingTerm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/NovikovSeries/LeadingTerm.lean#L263)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
