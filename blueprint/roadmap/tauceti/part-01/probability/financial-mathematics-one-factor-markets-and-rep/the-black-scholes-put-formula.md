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

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Black–Scholes call formula](the-black-scholes-call-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.riskNeutralPrice_put`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice_put).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.riskNeutralPrice_put`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.riskNeutralPrice_put)
- [Source of `TauCeti.BlackScholes.riskNeutralPrice_put` in TauCeti/Probability/Finance/BlackScholes/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/BlackScholes/Basic.lean#L366)
