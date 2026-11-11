---
declaration: def
origin: cited
lean: IsDedekindDomain.FiniteAdeleRing.principalParts
statement: formalized
---

# IsDedekindDomain.FiniteAdeleRing.principalParts

The **principal parts** of a finite adele `a`: the family of classes of its components `a v`
in `K_v ⧸ 𝒪_v`. All but finitely many of them vanish, because `a` is integral at all but finitely
many places, so this is an `R`-linear map to the direct sum of the local quotients.

```lean
IsDedekindDomain.FiniteAdeleRing.principalParts.{u_1, u_2} (R : Type u_1) [CommRing R]
  [IsDedekindDomain R] (K : Type u_2) [Field K] [Algebra R K] [IsFractionRing R K] :
  IsDedekindDomain.FiniteAdeleRing R K →ₗ[R]
    DirectSum (IsDedekindDomain.HeightOneSpectrum R) fun v =>
      IsDedekindDomain.HeightOneSpectrum.adicCompletion K v ⧸
        IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegersSubmodule K v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsDedekindDomain.FiniteAdeleRing.principalParts`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/FiniteAdeleRing/PrincipalParts.html#IsDedekindDomain.FiniteAdeleRing.principalParts).

## Sources

- [Tau Ceti documentation: `IsDedekindDomain.FiniteAdeleRing.principalParts`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/FiniteAdeleRing/PrincipalParts.html#IsDedekindDomain.FiniteAdeleRing.principalParts)
- [Source of `IsDedekindDomain.FiniteAdeleRing.principalParts` in TauCeti/RingTheory/DedekindDomain/FiniteAdeleRing/PrincipalParts.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DedekindDomain/FiniteAdeleRing/PrincipalParts.lean#L77)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/GlobalNumberFields/STATUS.md)
