---
declaration: def
origin: cited
lean: Matrix.UnitaryGroup.maslovIndex
statement: formalized
---

# Matrix.UnitaryGroup.maslovIndex

The **Maslov index** of a path `γ` of unitary frames, relative to `ℝⁿ`: Souriau's spectral
formula `angleChange (det ∘ W ∘ γ) / (2π) - (s(W V) - s(W U))` for the Robbin–Salamon index of the
path of Lagrangians `γ t ℝⁿ`, with `W` the Souriau map and `s` the spectral angle sum.

```lean
Matrix.UnitaryGroup.maslovIndex.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n]
  {U V : ↥(Matrix.unitaryGroup n ℂ)} (γ : Path U V) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.UnitaryGroup.maslovIndex`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/Maslov.html#Matrix.UnitaryGroup.maslovIndex).

## Sources

- [Tau Ceti documentation: `Matrix.UnitaryGroup.maslovIndex`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/Maslov.html#Matrix.UnitaryGroup.maslovIndex)
- [Source of `Matrix.UnitaryGroup.maslovIndex` in TauCeti/Analysis/Matrix/UnitaryGroup/Maslov.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Matrix/UnitaryGroup/Maslov.lean#L298)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HeegaardFloer/STATUS.md)
