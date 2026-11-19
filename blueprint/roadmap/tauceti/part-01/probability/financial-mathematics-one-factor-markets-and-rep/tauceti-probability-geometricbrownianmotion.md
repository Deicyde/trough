---
declaration: def
origin: cited
lean: TauCeti.Probability.geometricBrownianMotion
statement: formalized
---

# TauCeti.Probability.geometricBrownianMotion

The **geometric Brownian motion** `s * exp ((μ - σ² / 2) t + σ W_t)` driven by `W`, with
initial value `s`, drift `μ` and volatility `σ`.

```lean
TauCeti.Probability.geometricBrownianMotion.{u_1} {Ω : Type u_1} (s μ σ : ℝ) (W : NNReal → Ω → ℝ)
  (t : NNReal) (ω : Ω) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.geometricBrownianMotion`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Geometric/Basic.html#TauCeti.Probability.geometricBrownianMotion).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.geometricBrownianMotion`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Geometric/Basic.html#TauCeti.Probability.geometricBrownianMotion)
- [Source of `TauCeti.Probability.geometricBrownianMotion` in TauCeti/Probability/BrownianMotion/Geometric/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/BrownianMotion/Geometric/Basic.lean#L75)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
