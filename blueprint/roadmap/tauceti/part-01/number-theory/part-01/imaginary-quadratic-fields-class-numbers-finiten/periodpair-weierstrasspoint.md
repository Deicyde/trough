---
declaration: def
origin: cited
lean: PeriodPair.weierstrassPoint
statement: formalized
---

# PeriodPair.weierstrassPoint

The point `(℘(z), ℘'(z) / 2)` of the Weierstrass curve of `L` for `z ∉ Λ`, and the point at
infinity `0` for `z ∈ Λ`.

```lean
PeriodPair.weierstrassPoint (L : PeriodPair) (z : ℂ) : L.weierstrassCurve.toAffine.Point
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PeriodPair.weierstrassPoint`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/Uniformization.html#PeriodPair.weierstrassPoint).

## Sources

- [Tau Ceti documentation: `PeriodPair.weierstrassPoint`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/Uniformization.html#PeriodPair.weierstrassPoint)
- [Source of `PeriodPair.weierstrassPoint` in TauCeti/Analysis/SpecialFunctions/Elliptic/Uniformization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Elliptic/Uniformization.lean#L285)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
