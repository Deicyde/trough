---
declaration: theorem
origin: cited
lean: TauCeti.Finance.vectorMeasureIcc_bondPrice
statement: formalized
proof: formalized
---

# TauCeti.Finance.vectorMeasureIcc_bondPrice

The bond's Stieltjes measure on `(0,T]` is the signed measure with density `r β`.
In particular this identification does not require the interest rate to be nonnegative.

```lean
TauCeti.Finance.vectorMeasureIcc_bondPrice {r : ℝ → ℝ} {T : ℝ} (hr : ContinuousOn r (Set.Icc 0 T))
  (hT : 0 ≤ T) (β₀ : ℝ) :
  ⋯.vectorMeasureIcc hT =
    (MeasureTheory.volume.restrict (Set.Ioc 0 T)).withDensityᵥ fun t =>
      r t * TauCeti.Finance.bondPrice r β₀ t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Finance.vectorMeasureIcc_bondPrice`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/Bond/Trading.html#TauCeti.Finance.vectorMeasureIcc_bondPrice).

## Sources

- [Tau Ceti documentation: `TauCeti.Finance.vectorMeasureIcc_bondPrice`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/Bond/Trading.html#TauCeti.Finance.vectorMeasureIcc_bondPrice)
- [Source of `TauCeti.Finance.vectorMeasureIcc_bondPrice` in TauCeti/Probability/Finance/Bond/Trading.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/Bond/Trading.lean#L65)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
