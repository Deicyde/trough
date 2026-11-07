---
declaration: theorem
origin: cited
lean: TauCeti.Probability.map_orderStatistic_pi_uniformMeasure
statement: formalized
proof: formalized
---

# Order statistics of uniform samples are beta distributed

The `k`-th order statistic
(counted from `0`) of `n` independent uniform variables on the unit interval has the beta law
with parameters `k + 1` and `n - k`.

```lean
TauCeti.Probability.map_orderStatistic_pi_uniformMeasure {n : ℕ} (k : Fin n) :
  MeasureTheory.Measure.map (TauCeti.orderStatistic k)
      (MeasureTheory.Measure.pi fun x => TauCeti.Probability.uniformMeasure 0 1) =
    ProbabilityTheory.betaMeasure (↑↑k + 1) (↑n - ↑↑k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.map_orderStatistic_pi_uniformMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/OrderStatistic/Basic.html#TauCeti.Probability.map_orderStatistic_pi_uniformMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.map_orderStatistic_pi_uniformMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/OrderStatistic/Basic.html#TauCeti.Probability.map_orderStatistic_pi_uniformMeasure)
- [Source of `TauCeti.Probability.map_orderStatistic_pi_uniformMeasure` in TauCeti/Probability/Distributions/OrderStatistic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/OrderStatistic/Basic.lean#L114)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StandardDistributions/STATUS.md)
