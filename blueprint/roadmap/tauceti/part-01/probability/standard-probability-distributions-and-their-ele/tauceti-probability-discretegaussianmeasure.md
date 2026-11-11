---
declaration: def
origin: cited
lean: TauCeti.Probability.discreteGaussianMeasure
statement: formalized
---

# TauCeti.Probability.discreteGaussianMeasure

The discrete Gaussian law on `ℤ` with real center `c` and width `s`.

At positive width it is the weighted Dirac sum normalized by `Real.gaussianLatticeSum c s`.
At nonpositive width it is the zero measure.

```lean
TauCeti.Probability.discreteGaussianMeasure (c s : ℝ) : MeasureTheory.Measure ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.discreteGaussianMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/DiscreteGaussian/Basic.html#TauCeti.Probability.discreteGaussianMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.discreteGaussianMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/DiscreteGaussian/Basic.html#TauCeti.Probability.discreteGaussianMeasure)
- [Source of `TauCeti.Probability.discreteGaussianMeasure` in TauCeti/Probability/Distributions/DiscreteGaussian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/DiscreteGaussian/Basic.lean#L75)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StandardDistributions/STATUS.md)
