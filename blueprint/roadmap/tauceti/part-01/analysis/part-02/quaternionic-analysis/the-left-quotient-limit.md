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
- [Source of `TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul` in TauCeti/Analysis/Quaternion/QuotientDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Quaternion/QuotientDeriv.lean#L371)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
