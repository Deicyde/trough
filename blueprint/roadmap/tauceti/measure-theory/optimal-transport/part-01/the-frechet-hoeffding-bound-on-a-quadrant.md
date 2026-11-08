---
declaration: theorem
origin: cited
lean: TauCeti.ofReal_cdf_sub_le_measure
statement: formalized
proof: formalized
---

# The Fréchet–Hoeffding bound on a quadrant

Every transport plan of two real laws gives the
quadrant `Iic a ×ˢ Ioi b` mass at least `cdf μ a - cdf ν b`: the pairs with first coordinate at most
`a` carry mass `cdf μ a`, and at most `cdf ν b` of it has second coordinate at most `b`.

```lean
TauCeti.ofReal_cdf_sub_le_measure {μ ν : MeasureTheory.Measure ℝ}
  [MeasureTheory.IsProbabilityMeasure μ] {π : MeasureTheory.Measure (ℝ × ℝ)}
  (hπ : TauCeti.IsCoupling π μ ν) (a b : ℝ) :
  ENNReal.ofReal (↑(ProbabilityTheory.cdf μ) a - ↑(ProbabilityTheory.cdf ν) b) ≤
    π (Set.Iic a ×ˢ Set.Ioi b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ofReal_cdf_sub_le_measure`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Rearrangement.html#TauCeti.ofReal_cdf_sub_le_measure).

## Sources

- [Tau Ceti documentation: `TauCeti.ofReal_cdf_sub_le_measure`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Rearrangement.html#TauCeti.ofReal_cdf_sub_le_measure)
- [Source of `TauCeti.ofReal_cdf_sub_le_measure` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Rearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Rearrangement.lean#L83)
