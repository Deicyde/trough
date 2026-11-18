---
declaration: theorem
origin: cited
lean: TauCeti.Probability.not_continuousAt_gaussianCondKernel_gaussianRankChangeCovariance_zero_zero
statement: formalized
proof: formalized
---

# TauCeti.Probability.not_continuousAt_gaussianCondKernel_gaussianRankChangeCovariance_zero_zero

Although the joint laws vary weakly continuously, the displayed conditional laws at
observation zero are not weakly continuous when the observed covariance drops rank.

```lean
TauCeti.Probability.not_continuousAt_gaussianCondKernel_gaussianRankChangeCovariance_zero_zero :
  ¬ContinuousAt
      (fun t =>
        ((EuclideanSpace.gaussianCondKernel 0 (TauCeti.Probability.gaussianRankChangeCovariance t))
            0).toProbabilityMeasure)
      0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.not_continuousAt_gaussianCondKernel_gaussianRankChangeCovariance_zero_zero`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Conditional/RankChange.html#TauCeti.Probability.not_continuousAt_gaussianCondKernel_gaussianRankChangeCovariance_zero_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.not_continuousAt_gaussianCondKernel_gaussianRankChangeCovariance_zero_zero`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Conditional/RankChange.html#TauCeti.Probability.not_continuousAt_gaussianCondKernel_gaussianRankChangeCovariance_zero_zero)
- [Source of `TauCeti.Probability.not_continuousAt_gaussianCondKernel_gaussianRankChangeCovariance_zero_zero` in TauCeti/Probability/Distributions/Gaussian/Conditional/RankChange.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Distributions/Gaussian/Conditional/RankChange.lean#L132)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StandardDistributions/STATUS.md)
