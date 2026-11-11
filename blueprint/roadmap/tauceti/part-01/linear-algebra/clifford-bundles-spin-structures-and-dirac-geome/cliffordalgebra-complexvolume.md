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
- [Source of `CliffordAlgebra.complexVolume` in TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/VolumeElement/Complex.lean#L93)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpinGeometry/STATUS.md)
