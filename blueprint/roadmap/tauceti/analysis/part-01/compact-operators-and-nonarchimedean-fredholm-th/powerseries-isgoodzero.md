---
declaration: def
origin: cited
lean: PowerSeries.IsGoodZero
statement: formalized
---

# PowerSeries.IsGoodZero

A power series `f` has a **good zero of order `h`** at `a` if its Hasse derivatives of order
less than `h` vanish at `a` and its Hasse derivative of order `h` is a unit at `a`. For `h = 0`
this says that `f(a)` is a unit. Values at `a` are the infinite sums `PowerSeries.evalAt`, so the
notion is meaningful for entire series over a complete normed ring.

```lean
PowerSeries.IsGoodZero.{u_1} {R : Type u_1} [CommRing R] [TopologicalSpace R] (f : PowerSeries R)
  (a : R) (h : ℕ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsGoodZero`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/GoodZero.html#PowerSeries.IsGoodZero).

## Sources

- [Tau Ceti documentation: `PowerSeries.IsGoodZero`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/GoodZero.html#PowerSeries.IsGoodZero)
- [Source of `PowerSeries.IsGoodZero` in TauCeti/RingTheory/PowerSeries/Entire/GoodZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Entire/GoodZero.lean#L80)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
