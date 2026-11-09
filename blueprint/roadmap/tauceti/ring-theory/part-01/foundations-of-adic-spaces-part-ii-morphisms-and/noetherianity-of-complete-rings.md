---
declaration: theorem
origin: cited
lean: Ideal.isNoetherianRing_of_isAdicComplete
statement: formalized
proof: formalized
---

# Noetherianity of complete rings

A ring that is `I`-adically complete for a finitely
generated ideal `I` is Noetherian as soon as `R ⧸ I` is Noetherian.

```lean
Ideal.isNoetherianRing_of_isAdicComplete.{u_1} {R : Type u_1} [CommRing R] (I : Ideal R) (hI : I.FG)
  [IsAdicComplete I R] [IsNoetherianRing (R ⧸ I)] : IsNoetherianRing R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ideal.isNoetherianRing_of_isAdicComplete`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicCompletion/Noetherian.html#Ideal.isNoetherianRing_of_isAdicComplete).

## Sources

- [Tau Ceti documentation: `Ideal.isNoetherianRing_of_isAdicComplete`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicCompletion/Noetherian.html#Ideal.isNoetherianRing_of_isAdicComplete)
- [Source of `Ideal.isNoetherianRing_of_isAdicComplete` in TauCeti/RingTheory/AdicCompletion/Noetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/AdicCompletion/Noetherian.lean#L177)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
