---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.isMedian_quantile_half
statement: formalized
proof: formalized
---

# The quantile at level `1 / 2` is a median

This holds for every probability measure on
`ℝ`, including laws with atoms.

```lean
MeasureTheory.Measure.isMedian_quantile_half (μ : MeasureTheory.Measure ℝ)
  [MeasureTheory.IsProbabilityMeasure μ] : μ.IsMedian (μ.quantile 2⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.isMedian_quantile_half`](https://taucetiproject.org/docs/TauCeti/Probability/Quantile/Median.html#MeasureTheory.Measure.isMedian_quantile_half).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.isMedian_quantile_half`](https://taucetiproject.org/docs/TauCeti/Probability/Quantile/Median.html#MeasureTheory.Measure.isMedian_quantile_half)
- [Source of `MeasureTheory.Measure.isMedian_quantile_half` in TauCeti/Probability/Quantile/Median.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Quantile/Median.lean#L69)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StandardDistributions/STATUS.md)
