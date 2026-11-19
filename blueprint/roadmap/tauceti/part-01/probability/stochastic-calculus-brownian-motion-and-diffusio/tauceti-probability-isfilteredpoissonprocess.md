---
declaration: structure
origin: cited
lean: TauCeti.Probability.IsFilteredPoissonProcess
statement: formalized
---

# TauCeti.Probability.IsFilteredPoissonProcess

`N` is a **homogeneous Poisson process of rate `α` relative to the filtration `ℱ`** under
`P`: it starts at `0` almost surely, it is adapted to `ℱ`, and for `s ≤ t` the increment
`N t - N s` has the law of a Poisson variable of parameter `α * (t - s)` and is independent of
`ℱ s`.

```lean
TauCeti.Probability.IsFilteredPoissonProcess.{u_1} {Ω : Type u_1} {mΩ : MeasurableSpace Ω}
  (ℱ : MeasureTheory.Filtration NNReal mΩ) (α : NNReal) (N : NNReal → Ω → ℝ)
  (P : MeasureTheory.Measure Ω := by volume_tac) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.IsFilteredPoissonProcess`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Poisson/Filtered.html#TauCeti.Probability.IsFilteredPoissonProcess).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.IsFilteredPoissonProcess`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Poisson/Filtered.html#TauCeti.Probability.IsFilteredPoissonProcess)
- [Source of `TauCeti.Probability.IsFilteredPoissonProcess` in TauCeti/Probability/Process/Poisson/Filtered.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Process/Poisson/Filtered.lean#L68)
- [Tau Ceti roadmap status: Stochastic calculus, Brownian motion and diffusions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StochasticCalculus/STATUS.md)
