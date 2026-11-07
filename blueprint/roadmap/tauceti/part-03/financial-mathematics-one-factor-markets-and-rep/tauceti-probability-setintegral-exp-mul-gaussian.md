---
declaration: theorem
origin: cited
lean: TauCeti.Probability.setIntegral_exp_mul_gaussianReal
statement: formalized
proof: formalized
---

# TauCeti.Probability.setIntegral\_exp\_mul\_gaussianReal

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
- [Source of `TauCeti.Probability.setIntegral_exp_mul_gaussianReal` in TauCeti/Probability/Distributions/Tilted.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/Tilted.lean#L89)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FinancialMathematics/STATUS.md)
