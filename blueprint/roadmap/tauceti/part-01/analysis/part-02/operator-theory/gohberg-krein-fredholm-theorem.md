---
declaration: theorem
origin: cited
lean: TauCeti.isFredholm_toeplitz_toLp_iff
statement: formalized
proof: formalized
---

# Gohberg–Krein Fredholm theorem

For a continuous symbol `a : C(UnitAddCircle, ℂ)`, the
Toeplitz operator `T_a` on `HardySpace` is Fredholm if and only if `a` vanishes nowhere on the unit
circle.

```lean
TauCeti.isFredholm_toeplitz_toLp_iff (a : C(UnitAddCircle, ℂ)) :
  (TauCeti.toeplitz ((ContinuousMap.toLp ⊤ AddCircle.haarAddCircle ℂ) a)).IsFredholm ↔
    ∀ (x : UnitAddCircle), a x ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Atkinson's theorem](../../part-03/fredholm/atkinsons-theorem.md)
- [ContinuousMap.windingNumber](continuousmap-windingnumber.md)
- [Gohberg–Krein index theorem](gohberg-krein-index-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isFredholm_toeplitz_toLp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Fredholm.html#TauCeti.isFredholm_toeplitz_toLp_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.isFredholm_toeplitz_toLp_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Fredholm.html#TauCeti.isFredholm_toeplitz_toLp_iff)
- [Source of `TauCeti.isFredholm_toeplitz_toLp_iff` in TauCeti/Analysis/Fourier/Hardy/Fredholm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Hardy/Fredholm.lean#L149)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorTheory/STATUS.md)
