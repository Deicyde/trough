---
declaration: def
origin: cited
lean: ContinuousMap.windingNumber
statement: formalized
---

# ContinuousMap.windingNumber

The **winding number** of a nowhere-zero continuous circle function `f : C(AddCircle T, ℂ)`
about `0`, defined as `Circle.degree (f.normalizedLoop hf)`.

```lean
ContinuousMap.windingNumber {T : ℝ} (f : C(AddCircle T, ℂ)) (hf : ∀ (x : AddCircle T), f x ≠ 0) : ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousMap.windingNumber`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Winding.html#ContinuousMap.windingNumber).

## Sources

- [Tau Ceti documentation: `ContinuousMap.windingNumber`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Winding.html#ContinuousMap.windingNumber)
- [Source of `ContinuousMap.windingNumber` in TauCeti/Analysis/Fourier/Winding.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Winding.lean#L116)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorTheory/STATUS.md)
