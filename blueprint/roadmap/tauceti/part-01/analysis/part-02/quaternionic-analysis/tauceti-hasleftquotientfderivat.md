---
declaration: def
origin: cited
lean: TauCeti.HasLeftQuotientFDerivAt
statement: formalized
---

# TauCeti.HasLeftQuotientFDerivAt

`f` has *left quotient derivative* `b` at `q`: the real Fréchet derivative of `f` at `q` is
right multiplication `h ↦ h * b`. Equivalently `h⁻¹ * (f (q + h) - f q) → b` as `h → 0`, see
`TauCeti.hasLeftQuotientFDerivAt_iff_tendsto_inv_mul`.

```lean
TauCeti.HasLeftQuotientFDerivAt (f : Quaternion ℝ → Quaternion ℝ) (q b : Quaternion ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasLeftQuotientFDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/QuotientDeriv.html#TauCeti.HasLeftQuotientFDerivAt).

## Sources

- [Tau Ceti documentation: `TauCeti.HasLeftQuotientFDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/QuotientDeriv.html#TauCeti.HasLeftQuotientFDerivAt)
- [Source of `TauCeti.HasLeftQuotientFDerivAt` in TauCeti/Analysis/Quaternion/QuotientDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Quaternion/QuotientDeriv.lean#L82)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
