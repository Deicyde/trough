---
declaration: def
origin: cited
lean: TauCeti.NovikovSeries.completionPkg
statement: formalized
---

# TauCeti.NovikovSeries.completionPkg

The Novikov series are the completion of the group ring `H →₀ R` for the uniform structure
of its period filtration: they are complete and separated, and the inclusion `ofFinsupp` is a
uniform inducing map with dense range.

```lean
TauCeti.NovikovSeries.completionPkg.{u_1, u_2} (R : Type u_1) (H : Type u_2) [AddZeroClass H]
  (N : H →+ ℝ) [AddCommGroup R] : AbstractCompletion.{max u_2 u_1, max u_1 u_2} (H →₀ R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovSeries.completionPkg`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/Topology.html#TauCeti.NovikovSeries.completionPkg).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovSeries.completionPkg`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/Topology.html#TauCeti.NovikovSeries.completionPkg)
- [Source of `TauCeti.NovikovSeries.completionPkg` in TauCeti/RingTheory/NovikovSeries/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/NovikovSeries/Topology.lean#L345)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
