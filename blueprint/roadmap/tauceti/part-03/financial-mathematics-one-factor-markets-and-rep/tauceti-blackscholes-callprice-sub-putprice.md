---
declaration: theorem
origin: cited
lean: TauCeti.BlackScholes.callPrice_sub_putPrice
statement: formalized
proof: formalized
---

# TauCeti.BlackScholes.callPrice_sub_putPrice

**Put–call parity** for the closed-form prices: `C - P = s - K e^{-rτ}`.

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
- [Source of `TauCeti.BlackScholes.callPrice_sub_putPrice` in TauCeti/Probability/Finance/BlackScholes/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Finance/BlackScholes/Basic.lean#L270)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FinancialMathematics/STATUS.md)
