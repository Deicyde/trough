---
declaration: theorem
origin: cited
lean: TauCeti.Probability.setIntegral_exp_mul_gaussianReal
statement: formalized
proof: formalized
---

# TauCeti.Probability.setIntegral_exp_mul_gaussianReal

Integrating the exponential weight `exp (t * x)` against `N(m, v)` over a set `s` gives the
moment-generating function `exp (m t + v t² / 2)` times the mass of `s` under the tilted law
`N(m + v t, v)`.

```lean
TauCeti.Probability.setIntegral_exp_mul_gaussianReal (m : ℝ) (v : NNReal) (t : ℝ) (s : Set ℝ) :
  ∫ (x : ℝ) in s, Real.exp (t * x) ∂ProbabilityTheory.gaussianReal m v =
    Real.exp (m * t + ↑v * t ^ 2 / 2) * (ProbabilityTheory.gaussianReal (m + ↑v * t) v).real s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.setIntegral_exp_mul_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Tilted.html#TauCeti.Probability.setIntegral_exp_mul_gaussianReal).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.setIntegral_exp_mul_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Tilted.html#TauCeti.Probability.setIntegral_exp_mul_gaussianReal)
- [Source of `TauCeti.Probability.setIntegral_exp_mul_gaussianReal` in TauCeti/Probability/Distributions/Tilted.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Tilted.lean#L89)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FinancialMathematics/STATUS.md)
