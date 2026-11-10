---
declaration: def
origin: cited
lean: TauCeti.NovikovSeries.toLaurentSeries
statement: formalized
---

# TauCeti.NovikovSeries.toLaurentSeries

Novikov series on `ℤ` for the period map `k ↦ k` are the Laurent series: the ring isomorphism
which keeps every coefficient.

```lean
TauCeti.NovikovSeries.toLaurentSeries.{u_1} {R : Type u_1} [Semiring R] :
  TauCeti.NovikovSeries R ℤ (Int.castAddHom ℝ) ≃+* LaurentSeries R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovSeries.toLaurentSeries`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/LaurentSeries.html#TauCeti.NovikovSeries.toLaurentSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovSeries.toLaurentSeries`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/LaurentSeries.html#TauCeti.NovikovSeries.toLaurentSeries)
- [Source of `TauCeti.NovikovSeries.toLaurentSeries` in TauCeti/RingTheory/NovikovSeries/LaurentSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/NovikovSeries/LaurentSeries.lean#L75)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
