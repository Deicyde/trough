---
declaration: theorem
origin: cited
lean: TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo
statement: formalized
proof: formalized
---

# TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo

The call delta lies strictly between `0` and `1`.

```lean
TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo {s r σ K τ : ℝ} (hs : 0 < s) (hK : 0 < K)
  (hσ : σ ≠ 0) (hτ : 0 < τ) :
  deriv (fun x => TauCeti.BlackScholes.callPrice x r σ K τ) s ∈ Set.Ioo 0 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus](tauceti-blackscholes-mul-gaussianpdfreal-dplus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Greeks.html#TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Greeks.html#TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo)
- [Source of `TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo` in TauCeti/Probability/Finance/BlackScholes/Greeks.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Finance/BlackScholes/Greeks.lean#L114)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FinancialMathematics/STATUS.md)
