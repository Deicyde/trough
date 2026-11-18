---
declaration: theorem
origin: cited
lean: TauCeti.Probability.poincareInequality_stdGaussian_iff
statement: formalized
proof: formalized
---

# TauCeti.Probability.poincareInequality_stdGaussian_iff

On a nontrivial finite-dimensional real inner product space, the standard Gaussian has
Poincaré constant `C` exactly when `1 ≤ C`.

```lean
TauCeti.Probability.poincareInequality_stdGaussian_iff.{u_1} (E : Type u_1) [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] [Nontrivial E]
  {C : ℝ} : (ProbabilityTheory.stdGaussian E).PoincareInequality C ↔ 1 ≤ C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Efron–Stein inequality on `Measure.pi` over a finite index type](../other-results/the-efron-stein-inequality-on-measure-pi-over-a.md)
- [The Gaussian Poincaré inequality on `ℝ`](../distributions/the-gaussian-poincare-inequality-on-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.poincareInequality_stdGaussian_iff`](https://taucetiproject.org/docs/TauCeti/Probability/Concentration/Poincare/Gaussian/Basic.html#TauCeti.Probability.poincareInequality_stdGaussian_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.poincareInequality_stdGaussian_iff`](https://taucetiproject.org/docs/TauCeti/Probability/Concentration/Poincare/Gaussian/Basic.html#TauCeti.Probability.poincareInequality_stdGaussian_iff)
- [Source of `TauCeti.Probability.poincareInequality_stdGaussian_iff` in TauCeti/Probability/Concentration/Poincare/Gaussian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Concentration/Poincare/Gaussian/Basic.lean#L68)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RandomMatrices/STATUS.md)
