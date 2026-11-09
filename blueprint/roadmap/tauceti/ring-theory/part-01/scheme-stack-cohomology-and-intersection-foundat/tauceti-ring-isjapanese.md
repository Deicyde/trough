---
declaration: class
origin: cited
lean: TauCeti.Ring.IsJapanese
statement: formalized
---

# TauCeti.Ring.IsJapanese

A domain `R` is *Japanese* (or *N-2*) if for every finite extension `L` of its fraction field,
the integral closure of `R` in `L` is a finite `R`-module; inseparable extensions are included.
Stacks, Definition 10.161.1 (032F). See `IsJapanese.finite_integralClosure` for an arbitrary model
of the fraction field and an extension in an arbitrary universe.

```lean
TauCeti.Ring.IsJapanese.{u} (R : Type u) [CommRing R] [IsDomain R] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Ring.IsJapanese`](https://taucetiproject.org/docs/TauCeti/RingTheory/Japanese.html#TauCeti.Ring.IsJapanese).

## Sources

- [Tau Ceti documentation: `TauCeti.Ring.IsJapanese`](https://taucetiproject.org/docs/TauCeti/RingTheory/Japanese.html#TauCeti.Ring.IsJapanese)
- [Source of `TauCeti.Ring.IsJapanese` in TauCeti/RingTheory/Japanese.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Japanese.lean#L121)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
