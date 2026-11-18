---
declaration: def
origin: cited
lean: TauCeti.Bigraded.eulerPowerSeries
statement: formalized
---

# TauCeti.Bigraded.eulerPowerSeries

The **Alexander-graded Euler formal power series** of `P : PowerSeries (LaurentPolynomial R)`
from a slicewise finiteness witness `hP`: its `a`-th power-series coefficient is the finite
alternating sum `∑ n, (-1)ⁿ [qᵃ][tⁿ] P`.

```lean
TauCeti.Bigraded.eulerPowerSeries.{u_1} {R : Type u_1} [Ring R]
  {P : PowerSeries (LaurentPolynomial R)} (hP : TauCeti.Bigraded.HasEulerPowerSeries P) :
  PowerSeries R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Bigraded.eulerPowerSeries`](https://taucetiproject.org/docs/TauCeti/Algebra/Bigraded/PowerSeries.html#TauCeti.Bigraded.eulerPowerSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.Bigraded.eulerPowerSeries`](https://taucetiproject.org/docs/TauCeti/Algebra/Bigraded/PowerSeries.html#TauCeti.Bigraded.eulerPowerSeries)
- [Source of `TauCeti.Bigraded.eulerPowerSeries` in TauCeti/Algebra/Bigraded/PowerSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Bigraded/PowerSeries.lean#L148)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
