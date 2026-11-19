---
declaration: def
origin: cited
lean: IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles
statement: formalized
---

# IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles

The **`S`-integral finite adeles** `∏_{v ∈ S} K_v × ∏_{v ∉ S} 𝒪_v`: the finite adeles that are
integral at every finite place outside `S`, as an `R`-subalgebra of the finite adele ring. For
`S = ∅` these are the integral finite adeles, and every finite adele is `S`-integral for some
finite `S`.

```lean
IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles.{u_1, u_2} (R : Type u_1) [CommRing R]
  [IsDedekindDomain R] (K : Type u_2) [Field K] [Algebra R K] [IsFractionRing R K]
  (S : Set (IsDedekindDomain.HeightOneSpectrum R)) :
  Subalgebra R (IsDedekindDomain.FiniteAdeleRing R K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/FiniteAdeleRing/Basic.html#IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles).

## Sources

- [Tau Ceti documentation: `IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/FiniteAdeleRing/Basic.html#IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles)
- [Source of `IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles` in TauCeti/RingTheory/DedekindDomain/FiniteAdeleRing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/DedekindDomain/FiniteAdeleRing/Basic.lean#L215)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/GlobalNumberFields/STATUS.md)
