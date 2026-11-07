---
declaration: def
origin: cited
lean: TauCeti.continuousDerivationsEquiv
statement: formalized
---

# TauCeti.continuousDerivationsEquiv

**The continuous derivations of `K⸨X⸩` form a free module of rank one** with basis the formal
derivative `D`: the equivalence sends `a` to `a • D`, and its inverse evaluates a derivation at the
parameter `X`.

```lean
TauCeti.continuousDerivationsEquiv.{u_1} (K : Type u_1) [Field K] :
  LaurentSeries K ≃ₗ[LaurentSeries K] ↥(TauCeti.continuousDerivations K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuousDerivationsEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/ContinuousDerivation.html#TauCeti.continuousDerivationsEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.continuousDerivationsEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/ContinuousDerivation.html#TauCeti.continuousDerivationsEquiv)
- [Source of `TauCeti.continuousDerivationsEquiv` in TauCeti/RingTheory/LaurentSeries/ContinuousDerivation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/ContinuousDerivation.lean#L199)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
