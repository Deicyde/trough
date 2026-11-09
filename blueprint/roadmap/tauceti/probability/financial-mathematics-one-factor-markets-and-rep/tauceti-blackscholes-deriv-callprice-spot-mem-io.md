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
- [Source of `TauCeti.BlackScholes.deriv_callPrice_spot_mem_Ioo` in TauCeti/Probability/Finance/BlackScholes/Greeks.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Finance/BlackScholes/Greeks.lean#L114)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FinancialMathematics/STATUS.md)
