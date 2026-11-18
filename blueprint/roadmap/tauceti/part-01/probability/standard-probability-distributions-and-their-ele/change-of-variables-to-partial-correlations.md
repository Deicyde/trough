---
declaration: theorem
origin: cited
lean: TauCeti.setIntegral_comp_correlationCoordinatesOfPartialCorrelation
statement: formalized
proof: formalized
---

# Change of variables to partial correlations

The integral of a function over the
positive-definite correlation region is the integral over the open cube of its composite with the
partial-correlation forward map, weighted by the Jacobian `∏ √(1 - z ij ^ 2) ^ (p - j - 2)`
(zero-based column `j`).

```lean
TauCeti.setIntegral_comp_correlationCoordinatesOfPartialCorrelation.{u_1} {p : ℕ} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] (g : (TauCeti.strictLowerTriangle p → ℝ) → E) :
  ∫ (z : TauCeti.strictLowerTriangle p → ℝ) in
      {z | ∀ (ij : TauCeti.strictLowerTriangle p), |z ij| < 1},
      (∏ ij, √(1 - z ij ^ 2) ^ (p - ↑(↑ij).2 - 2)) •
        g (TauCeti.correlationCoordinatesOfPartialCorrelation z) =
    ∫ (x : TauCeti.strictLowerTriangle p → ℝ) in TauCeti.posDefCorrelationRegion p, g x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.setIntegral_comp_correlationCoordinatesOfPartialCorrelation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/SymmetricMatrix/Correlation.html#TauCeti.setIntegral_comp_correlationCoordinatesOfPartialCorrelation).

## Sources

- [Tau Ceti documentation: `TauCeti.setIntegral_comp_correlationCoordinatesOfPartialCorrelation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/SymmetricMatrix/Correlation.html#TauCeti.setIntegral_comp_correlationCoordinatesOfPartialCorrelation)
- [Source of `TauCeti.setIntegral_comp_correlationCoordinatesOfPartialCorrelation` in TauCeti/MeasureTheory/Measure/SymmetricMatrix/Correlation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Measure/SymmetricMatrix/Correlation.lean#L1048)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StandardDistributions/STATUS.md)
