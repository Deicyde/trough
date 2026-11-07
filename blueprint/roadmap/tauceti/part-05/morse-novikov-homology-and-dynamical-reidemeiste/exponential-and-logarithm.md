---
declaration: def
origin: cited
lean: TauCeti.NovikovSeries.expMulEquiv
statement: formalized
---

# Exponential and logarithm

of Novikov series: over a `ℚ`-algebra `K`, the exponential is
an isomorphism from the additive group of the positive ideal onto its principal unit group in the
nonnegative subring, with inverse the logarithm. This is `Ideal.expMulEquiv` for the positive
ideal, whose series are topologically nilpotent.

```lean
TauCeti.NovikovSeries.expMulEquiv.{u_1, u_2} {H : Type u_1} (K : Type u_2) [AddCommMonoid H]
  (N : H →+ ℝ) [CommRing K] [Algebra ℚ K] :
  Multiplicative ↥(TauCeti.NovikovSeries.posIdeal K N) ≃*
    ↥(TauCeti.NovikovSeries.posIdeal K N).principalUnitGroup
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovSeries.expMulEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/ExpLog.html#TauCeti.NovikovSeries.expMulEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovSeries.expMulEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/ExpLog.html#TauCeti.NovikovSeries.expMulEquiv)
- [Source of `TauCeti.NovikovSeries.expMulEquiv` in TauCeti/RingTheory/NovikovSeries/ExpLog.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/NovikovSeries/ExpLog.lean#L66)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
