---
declaration: theorem
origin: cited
lean: TauCeti.Probability.not_logSobolevInequality_gaussianReal
statement: formalized
proof: formalized
---

# TauCeti.Probability.not_logSobolevInequality_gaussianReal

No constant smaller than `1` satisfies the standard Gaussian logarithmic Sobolev inequality.

```lean
TauCeti.Probability.not_logSobolevInequality_gaussianReal {C : ℝ} (hC : C < 1) :
  ¬(ProbabilityTheory.gaussianReal 0 1).LogSobolevInequality C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.not_logSobolevInequality_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Concentration/Poincare/Gaussian/LogSobolevSharpness.html#TauCeti.Probability.not_logSobolevInequality_gaussianReal).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.not_logSobolevInequality_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Concentration/Poincare/Gaussian/LogSobolevSharpness.html#TauCeti.Probability.not_logSobolevInequality_gaussianReal)
- [Source of `TauCeti.Probability.not_logSobolevInequality_gaussianReal` in TauCeti/Probability/Concentration/Poincare/Gaussian/LogSobolevSharpness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Concentration/Poincare/Gaussian/LogSobolevSharpness.lean#L111)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RandomMatrices/STATUS.md)
