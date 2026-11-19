---
declaration: theorem
origin: cited
lean: TauCeti.index_toeplitz_toLp
statement: formalized
proof: formalized
---

# Gohberg–Krein index theorem

The Toeplitz operator of a nowhere-zero continuous symbol
`a : C(UnitAddCircle, ℂ)` has Fredholm index equal to minus the winding number of `a` about `0`.

```lean
TauCeti.index_toeplitz_toLp (a : C(UnitAddCircle, ℂ)) (ha : ∀ (x : UnitAddCircle), a x ≠ 0) :
  (TauCeti.toeplitz ((ContinuousMap.toLp ⊤ AddCircle.haarAddCircle ℂ) a)).index =
    -a.windingNumber ha
```

## Depends on

- [ContinuousMap.windingNumber](continuousmap-windingnumber.md)

## Proof depends on

- [Atkinson's theorem](../../part-03/fredholm/atkinsons-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.index_toeplitz_toLp`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Fredholm.html#TauCeti.index_toeplitz_toLp).

## Sources

- [Tau Ceti documentation: `TauCeti.index_toeplitz_toLp`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/Fredholm.html#TauCeti.index_toeplitz_toLp)
- [Source of `TauCeti.index_toeplitz_toLp` in TauCeti/Analysis/Fourier/Hardy/Fredholm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Hardy/Fredholm.lean#L139)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorTheory/STATUS.md)
