---
declaration: theorem
origin: cited
lean: TauCeti.ofReal_mul_measure_compl_closedBall_le_wassersteinEDist
statement: formalized
proof: formalized
---

# Markov's inequality for the Wasserstein distance from a Dirac law

For a probability
measure `μ` and a radius `r`, the mass of `μ` outside the closed ball of radius `r` about `x`,
multiplied by `r`, is at most `W_p (δ_x, μ)`, for every exponent `1 ≤ p`.

```lean
TauCeti.ofReal_mul_measure_compl_closedBall_le_wassersteinEDist.{u_1} {X : Type u_1} {p : ENNReal}
  [PseudoMetricSpace X] [MeasurableSpace X] [BorelSpace X] [SecondCountableTopology X]
  [Fact (1 ≤ p)] (x : X) (μ : MeasureTheory.ProbabilityMeasure X) (r : ℝ) :
  ENNReal.ofReal r * ↑μ (Metric.closedBall x r)ᶜ ≤
    TauCeti.wassersteinEDist p (MeasureTheory.Measure.dirac x) ↑μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ofReal_mul_measure_compl_closedBall_le_wassersteinEDist`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Compactness.html#TauCeti.ofReal_mul_measure_compl_closedBall_le_wassersteinEDist).

## Sources

- [Tau Ceti documentation: `TauCeti.ofReal_mul_measure_compl_closedBall_le_wassersteinEDist`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Compactness.html#TauCeti.ofReal_mul_measure_compl_closedBall_le_wassersteinEDist)
- [Source of `TauCeti.ofReal_mul_measure_compl_closedBall_le_wassersteinEDist` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Compactness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/Compactness.lean#L89)
