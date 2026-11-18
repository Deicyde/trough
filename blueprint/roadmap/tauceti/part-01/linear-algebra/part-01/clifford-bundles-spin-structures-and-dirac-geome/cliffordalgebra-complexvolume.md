---
declaration: def
origin: cited
lean: CliffordAlgebra.complexVolume
statement: formalized
---

# CliffordAlgebra.complexVolume

The normalized complex volume element `Γ = i ^ ⌊(n + 1) / 2⌋ c(e₁) ⋯ c(eₙ)` of the
complexified Clifford algebra of an oriented real inner product space of dimension `n`, for any
positively oriented orthonormal basis `e` that is orthogonal for `Q`
(`CliffordAlgebra.complexVolume_eq`). It is fixed by `CliffordAlgebra.conjStar`; in even
dimension it anticommutes with every vector, and in odd dimension it is central. For
`Q v = -‖v‖²` it squares to `1`, so in even dimension it is the chirality operator.

```lean
CliffordAlgebra.complexVolume.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] {n : ℕ} [Fact (Module.finrank ℝ V = n)] (Q : QuadraticForm ℝ V)
  (o : Orientation ℝ V (Fin n)) : CliffordAlgebra (QuadraticForm.baseChange ℂ Q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.complexVolume`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Complex.html#CliffordAlgebra.complexVolume).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.complexVolume`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Complex.html#CliffordAlgebra.complexVolume)
- [Source of `CliffordAlgebra.complexVolume` in TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Complex.lean#L98)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpinGeometry/STATUS.md)
