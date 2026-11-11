---
declaration: theorem
origin: cited
lean: TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus
statement: formalized
proof: formalized
---

# TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus

The Black–Scholes density identity `s φ(d₊) = K e^{-rτ} φ(d₋)`, where `φ` is the standard
Gaussian density. It expresses that `d₊² - d₋² = 2 (log (s / K) + r τ)`.

```lean
TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus {s r σ K τ : ℝ} (hs : 0 < s) (hK : 0 < K)
  (hσ : σ ≠ 0) (hτ : 0 < τ) :
  s * ProbabilityTheory.gaussianPDFReal 0 1 (TauCeti.BlackScholes.dPlus s r σ K τ) =
    K * Real.exp (-r * τ) *
      ProbabilityTheory.gaussianPDFReal 0 1 (TauCeti.BlackScholes.dMinus s r σ K τ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Basic.html#TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus)
- [Source of `TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus` in TauCeti/Probability/Finance/BlackScholes/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Finance/BlackScholes/Basic.lean#L238)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FinancialMathematics/STATUS.md)
