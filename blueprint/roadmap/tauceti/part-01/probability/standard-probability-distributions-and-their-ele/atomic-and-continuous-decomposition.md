---
declaration: theorem
origin: cited
lean: TauCeti.Probability.gaussianMixtureMeasure_eq_sum_dirac_add_withDensity
statement: formalized
proof: formalized
---

# Atomic and continuous decomposition

A Gaussian mixture is the sum of the weighted
Dirac masses of its zero-variance components and of Lebesgue measure weighted by the mixture
density.

```lean
TauCeti.Probability.gaussianMixtureMeasure_eq_sum_dirac_add_withDensity.{u_1} {ι : Type u_1}
  [Fintype ι] {v : ι → NNReal} [DecidablePred fun i => v i = 0] (p : Convexity.StdSimplex NNReal ι)
  (m : ι → ℝ) :
  TauCeti.Probability.gaussianMixtureMeasure p m v =
    ∑ i with v i = 0, ↑(p.weights i) • MeasureTheory.Measure.dirac (m i) +
      MeasureTheory.volume.withDensity (TauCeti.Probability.gaussianMixturePDF p m v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.gaussianMixtureMeasure_eq_sum_dirac_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Mixture/Basic.html#TauCeti.Probability.gaussianMixtureMeasure_eq_sum_dirac_add_withDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.gaussianMixtureMeasure_eq_sum_dirac_add_withDensity`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Mixture/Basic.html#TauCeti.Probability.gaussianMixtureMeasure_eq_sum_dirac_add_withDensity)
- [Source of `TauCeti.Probability.gaussianMixtureMeasure_eq_sum_dirac_add_withDensity` in TauCeti/Probability/Distributions/Gaussian/Mixture/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Gaussian/Mixture/Basic.lean#L160)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StandardDistributions/STATUS.md)
