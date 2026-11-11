---
declaration: theorem
origin: cited
lean: TauCeti.Probability.mgf_intCast_discreteGaussianMeasure
statement: formalized
proof: formalized
---

# TauCeti.Probability.mgf_intCast_discreteGaussianMeasure

The discrete Gaussian mgf is a Gaussian exponential times a ratio of lattice sums.

```lean
TauCeti.Probability.mgf_intCast_discreteGaussianMeasure (c : ℝ) {s : ℝ} (hs : 0 < s) (t : ℝ) :
  ProbabilityTheory.mgf Int.cast (TauCeti.Probability.discreteGaussianMeasure c s) t =
    Real.exp (c * t + s ^ 2 * t ^ 2 / 2) * (c + s ^ 2 * t).gaussianLatticeSum s /
      c.gaussianLatticeSum s
```

## Depends on

- [TauCeti.Probability.discreteGaussianMeasure](tauceti-probability-discretegaussianmeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.mgf_intCast_discreteGaussianMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/DiscreteGaussian/Transforms.html#TauCeti.Probability.mgf_intCast_discreteGaussianMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.mgf_intCast_discreteGaussianMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/DiscreteGaussian/Transforms.html#TauCeti.Probability.mgf_intCast_discreteGaussianMeasure)
- [Source of `TauCeti.Probability.mgf_intCast_discreteGaussianMeasure` in TauCeti/Probability/Distributions/DiscreteGaussian/Transforms.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/DiscreteGaussian/Transforms.lean#L70)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StandardDistributions/STATUS.md)
