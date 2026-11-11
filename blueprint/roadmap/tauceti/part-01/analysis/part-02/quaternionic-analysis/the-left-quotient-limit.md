---
declaration: theorem
origin: cited
lean: TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul
statement: formalized
proof: formalized
---

# The left quotient limit

`f` has left slope `b` at `q` exactly when
`h⁻¹ * (f (q + h) - f q) → b` as `h → 0`, `h ≠ 0`. The increment stands on the left of the
difference quotient.

```lean
TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul {f : Quaternion ℝ → Quaternion ℝ}
  {q b : Quaternion ℝ} :
  TauCeti.HasLeftQuotientFDerivAt f q b ↔
    Filter.Tendsto (fun h => h⁻¹ * (f (q + h) - f q)) (nhdsWithin 0 {0}ᶜ) (nhds b)
```

## Depends on

- [TauCeti.HasLeftQuotientFDerivAt](tauceti-hasleftquotientfderivat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/QuotientDeriv.html#TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/QuotientDeriv.html#TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul)
- [Source of `TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul` in TauCeti/Analysis/Quaternion/QuotientDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Quaternion/QuotientDeriv.lean#L371)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
