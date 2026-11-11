---
declaration: theorem
origin: cited
lean: TauCeti.BlackScholes.callPrice_sub_putPrice
statement: formalized
proof: formalized
---

# Put–call parity for the closed-form prices

`C - P = s - K e^{-rτ}`.

```lean
TauCeti.BlackScholes.callPrice_sub_putPrice (s r σ K τ : ℝ) :
  TauCeti.BlackScholes.callPrice s r σ K τ - TauCeti.BlackScholes.putPrice s r σ K τ =
    s - K * Real.exp (-r * τ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.callPrice_sub_putPrice`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.callPrice_sub_putPrice).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.callPrice_sub_putPrice`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.callPrice_sub_putPrice)
- [Source of `TauCeti.BlackScholes.callPrice_sub_putPrice` in TauCeti/Probability/Finance/BlackScholes/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Finance/BlackScholes/Basic.lean#L270)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FinancialMathematics/STATUS.md)
