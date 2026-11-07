---
declaration: theorem
origin: cited
lean: TauCeti.F4ShortRoot.PrimeField.specialIsogeny_specialIsogeny
statement: formalized
proof: formalized
---

# TauCeti.F4ShortRoot.PrimeField.specialIsogeny\_specialIsogeny

Squaring the special endomorphism gives the prime-field Frobenius on all carrier points.

```lean
TauCeti.F4ShortRoot.PrimeField.specialIsogeny_specialIsogeny.{u_1} (A : Type u_1) [CommRing A]
  [Algebra (ZMod 2) A] (g : ↥(TauCeti.F4ShortRoot.PrimeField.points A)) :
  (TauCeti.F4ShortRoot.PrimeField.specialIsogeny A)
      ((TauCeti.F4ShortRoot.PrimeField.specialIsogeny A) g) =
    (TauCeti.F4ShortRoot.PrimeField.frobenius 1 A) g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.F4ShortRoot.PrimeField.specialIsogeny_specialIsogeny`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/F4/ShortRoot/PrimeField/QuotientSpecialIsogeny.html#TauCeti.F4ShortRoot.PrimeField.specialIsogeny_specialIsogeny).

## Sources

- [Tau Ceti documentation: `TauCeti.F4ShortRoot.PrimeField.specialIsogeny_specialIsogeny`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/F4/ShortRoot/PrimeField/QuotientSpecialIsogeny.html#TauCeti.F4ShortRoot.PrimeField.specialIsogeny_specialIsogeny)
- [Source of `TauCeti.F4ShortRoot.PrimeField.specialIsogeny_specialIsogeny` in TauCeti/Algebra/Lie/F4/ShortRoot/PrimeField/QuotientSpecialIsogeny.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/F4/ShortRoot/PrimeField/QuotientSpecialIsogeny.lean#L394)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CFSGStatement/STATUS.md)
