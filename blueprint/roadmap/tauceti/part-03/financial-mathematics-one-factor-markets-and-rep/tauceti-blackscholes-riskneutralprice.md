---
declaration: def
origin: cited
lean: TauCeti.BlackScholes.riskNeutralPrice
statement: formalized
---

# TauCeti.BlackScholes.riskNeutralPrice

The discounted risk-neutral expectation `exp (-r τ) * E[h (S_τ)]` of a payoff `h` of the
terminal spot `S_τ = terminalSpot s r σ τ Z`, `Z ∼ N(0, 1)`. For a non-integrable payoff the
Bochner integral, and hence this value, is zero.

```lean
TauCeti.BlackScholes.riskNeutralPrice (h : ℝ → ℝ) (s r σ τ : ℝ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.riskNeutralPrice`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.riskNeutralPrice`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice)
- [Source of `TauCeti.BlackScholes.riskNeutralPrice` in TauCeti/Probability/Finance/BlackScholes/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Finance/BlackScholes/Basic.lean#L134)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FinancialMathematics/STATUS.md)
