---
declaration: def
origin: cited
lean: TauCeti.Dagger.Omega
statement: formalized
---

# TauCeti.Dagger.Omega

The **universally finite module of differentials** `Ω¹_{A/K}`: the quotient of the Kähler
differentials `Ω[A⁄K]` by the intersection of all submodules with finite quotient. For a dagger
algebra this is Grosse-Klönne's module of differentials.

```lean
TauCeti.Dagger.Omega.{u_1, u_2} (K : Type u_1) (A : Type u_2) [CommRing K] [CommRing A]
  [Algebra K A] : Type u_2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.Omega`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Omega/Basic.html#TauCeti.Dagger.Omega).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.Omega`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Omega/Basic.html#TauCeti.Dagger.Omega)
- [Source of `TauCeti.Dagger.Omega` in TauCeti/RingTheory/Dagger/Omega/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/Omega/Basic.lean#L76)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
