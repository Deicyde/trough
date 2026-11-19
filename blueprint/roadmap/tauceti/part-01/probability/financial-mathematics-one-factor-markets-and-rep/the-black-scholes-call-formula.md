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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.riskNeutralPrice_call`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice_call).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.riskNeutralPrice_call`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice_call)
- [Source of `TauCeti.BlackScholes.riskNeutralPrice_call` in TauCeti/Probability/Finance/BlackScholes/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/BlackScholes/Basic.lean#L345)
