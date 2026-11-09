---
declaration: def
origin: cited
lean: TauCeti.NovikovSeries.mapRingHom
statement: formalized
---

# TauCeti.NovikovSeries.mapRingHom

The pushforward `P_(ρ,φ)` of Novikov series along a ring homomorphism `ρ` of coefficients and
an exponent homomorphism `φ` rescaling periods by a positive constant, as a ring homomorphism: the
coefficient at `h'` is the sum of the images under `ρ` of the coefficients at the exponents `h`
with `φ h = h'`.

```lean
TauCeti.NovikovSeries.mapRingHom.{u_1, u_2, u_4, u_5} {R : Type u_1} {S : Type u_2} {H : Type u_4}
  {H' : Type u_5} [AddMonoid H] [AddMonoid H'] {N : H →+ ℝ} {N' : H' →+ ℝ} [Semiring R] [Semiring S]
  (ρ : R →+* S) (φ : H →+ H') (hφ : ∃ c > 0, ∀ (h : H), N' (φ h) = c * N h) :
  TauCeti.NovikovSeries R H N →+* TauCeti.NovikovSeries S H' N'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovSeries.mapRingHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/Functoriality.html#TauCeti.NovikovSeries.mapRingHom).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovSeries.mapRingHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovSeries/Functoriality.html#TauCeti.NovikovSeries.mapRingHom)
- [Source of `TauCeti.NovikovSeries.mapRingHom` in TauCeti/RingTheory/NovikovSeries/Functoriality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/NovikovSeries/Functoriality.lean#L190)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseNovikov/STATUS.md)
