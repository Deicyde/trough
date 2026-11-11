---
declaration: def
origin: cited
lean: TauCeti.bigradedExtPoincarePowerSeries
statement: formalized
---

# TauCeti.bigradedExtPoincarePowerSeries

The full bigraded Ext Poincaré series, as a formal power series in cohomological degree
with Laurent-polynomial internal coefficients. No cohomological bound is required.

```lean
TauCeti.bigradedExtPoincarePowerSeries.{w, v, u, t} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] (k : Type t) [Field k] [CategoryTheory.Linear k C]
  [CategoryTheory.HasExt C] (e : C ≌ C) {X Y : C}
  (h : TauCeti.IsGradedExtInternallyFinite k e X Y) : PowerSeries (LaurentPolynomial ℤ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.bigradedExtPoincarePowerSeries`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/ExtEuler/Graded/Poincare/PowerSeries.html#TauCeti.bigradedExtPoincarePowerSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.bigradedExtPoincarePowerSeries`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/ExtEuler/Graded/Poincare/PowerSeries.html#TauCeti.bigradedExtPoincarePowerSeries)
- [Source of `TauCeti.bigradedExtPoincarePowerSeries` in TauCeti/Algebra/Homology/EulerCharacteristic/ExtEuler/Graded/Poincare/PowerSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/EulerCharacteristic/ExtEuler/Graded/Poincare/PowerSeries.lean#L50)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
