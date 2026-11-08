---
declaration: def
origin: cited
lean: ContinuousLinearMap.charPowerSeries
statement: formalized
---

# ContinuousLinearMap.charPowerSeries

The **Fredholm series** `det (1 - T u)` of an endomorphism `u` of a module `M` with property
(Pr): the principal-minor series of the extension `i ∘ u ∘ r` of `u` through a retract
presentation `r ∘ i = id` of `M` by a model space `C₀(J, R)`, fixed by choice. If `u` is row
compact, it does not depend on the presentation
(`ContinuousLinearMap.IsPrCompact.charPowerSeries_eq`). If `M` does not have property (Pr) the
series is `1`.

```lean
ContinuousLinearMap.charPowerSeries.{u, w} {R : Type w} [SeminormedCommRing R] {M : Type u}
  [SeminormedAddCommGroup M] [_root_.Module R M] (u : M →L[R] M) : PowerSeries R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.charPowerSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Basic.html#ContinuousLinearMap.charPowerSeries).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.charPowerSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Basic.html#ContinuousLinearMap.charPowerSeries)
- [Source of `ContinuousLinearMap.charPowerSeries` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/PrModule/Basic.lean#L85)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CompactOperators/STATUS.md)
