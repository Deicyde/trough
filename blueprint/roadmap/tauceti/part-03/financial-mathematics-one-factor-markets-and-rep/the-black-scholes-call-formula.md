---
declaration: theorem
origin: cited
lean: TauCeti.BlackScholes.riskNeutralPrice_call
statement: formalized
proof: formalized
---

# The Black–Scholes call formula

The discounted risk-neutral expectation of the call payoff
`(S_τ - K)⁺` is `s Φ(d₊) - K e^{-rτ} Φ(d₋)`.

```lean
TauCeti.BlackScholes.riskNeutralPrice_call {s r σ K τ : ℝ} (hs : 0 < s) (hσ : 0 < σ) (hK : 0 < K)
  (hτ : 0 < τ) :
  TauCeti.BlackScholes.riskNeutralPrice (fun x => (x - K)⁺) s r σ τ =
    TauCeti.BlackScholes.callPrice s r σ K τ
```

## Depends on

- [TauCeti.BlackScholes.riskNeutralPrice](tauceti-blackscholes-riskneutralprice.md)

## Proof depends on

- [TauCeti.Probability.setIntegral\_exp\_mul\_gaussianReal](tauceti-probability-setintegral-exp-mul-gaussian.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.riskNeutralPrice_call`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice_call).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.riskNeutralPrice_call`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice_call)
- [Source of `TauCeti.BlackScholes.riskNeutralPrice_call` in TauCeti/Probability/Finance/BlackScholes/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Finance/BlackScholes/Basic.lean#L312)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FinancialMathematics/STATUS.md)
