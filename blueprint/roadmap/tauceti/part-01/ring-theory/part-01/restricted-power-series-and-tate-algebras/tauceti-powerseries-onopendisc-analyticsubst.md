---
declaration: def
origin: cited
lean: TauCeti.PowerSeries.OnOpenDisc.analyticSubst
statement: formalized
---

# TauCeti.PowerSeries.OnOpenDisc.analyticSubst

Substitution by an open-disc series whose Gauss norm on each smaller closed disc is
strictly less than the source radius. It is defined by a convergent sum and permits a nonzero
constant coefficient in the inner series.

```lean
TauCeti.PowerSeries.OnOpenDisc.analyticSubst.{u_1} {R : Type u_1} [NormedCommRing R]
  [IsUltrametricDist R] [CompleteSpace R] {R₀ S₀ : ℝ} [Fact (0 < S₀)]
  (g : ↥(PowerSeries.OnOpenDisc.subring R S₀))
  (hg : ∀ (s : ↑(Set.Ioo 0 S₀)), ‖(TauCeti.PowerSeries.OnOpenDisc.restrict s) g‖ < R₀) :
  ↥(PowerSeries.OnOpenDisc.subring R R₀) →+* ↥(PowerSeries.OnOpenDisc.subring R S₀)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.OnOpenDisc.analyticSubst`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/OpenDisc/AnalyticSubst.html#TauCeti.PowerSeries.OnOpenDisc.analyticSubst).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.OnOpenDisc.analyticSubst`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/OpenDisc/AnalyticSubst.html#TauCeti.PowerSeries.OnOpenDisc.analyticSubst)
- [Source of `TauCeti.PowerSeries.OnOpenDisc.analyticSubst` in TauCeti/RingTheory/PowerSeries/OpenDisc/AnalyticSubst.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/PowerSeries/OpenDisc/AnalyticSubst.lean#L77)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
