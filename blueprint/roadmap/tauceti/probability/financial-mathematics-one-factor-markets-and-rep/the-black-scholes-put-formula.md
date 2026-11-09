---
declaration: theorem
origin: cited
lean: TauCeti.BlackScholes.riskNeutralPrice_put
statement: formalized
proof: formalized
---

# The Black–Scholes put formula

The discounted risk-neutral expectation of the put payoff
`(K - S_τ)⁺` is `K e^{-rτ} Φ(-d₋) - s Φ(-d₊)`.

```lean
TauCeti.BlackScholes.riskNeutralPrice_put {s r σ K τ : ℝ} (hs : 0 < s) (hσ : 0 < σ) (hK : 0 < K)
  (hτ : 0 < τ) :
  TauCeti.BlackScholes.riskNeutralPrice (fun x => (K - x)⁺) s r σ τ =
    TauCeti.BlackScholes.putPrice s r σ K τ
```

## Depends on

- [TauCeti.BlackScholes.riskNeutralPrice](tauceti-blackscholes-riskneutralprice.md)

## Proof depends on

- [The Black–Scholes call formula](the-black-scholes-call-formula.md)
- [Put–call parity for the closed-form prices](put-call-parity-for-the-closed-form-prices.md)
- [TauCeti.Probability.setIntegral_exp_mul_gaussianReal](tauceti-probability-setintegral-exp-mul-gaussian.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.riskNeutralPrice_put`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice_put).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.riskNeutralPrice_put`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice_put)
- [Source of `TauCeti.BlackScholes.riskNeutralPrice_put` in TauCeti/Probability/Finance/BlackScholes/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Finance/BlackScholes/Basic.lean#L333)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FinancialMathematics/STATUS.md)
