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
- [Source of `TauCeti.HasLeftQuotientFDerivAt` in TauCeti/Analysis/Quaternion/QuotientDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Quaternion/QuotientDeriv.lean#L82)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
