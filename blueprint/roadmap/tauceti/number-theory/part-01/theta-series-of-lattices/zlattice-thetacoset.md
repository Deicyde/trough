---
declaration: def
origin: cited
lean: ZLattice.thetaCoset
statement: formalized
---

# ZLattice.thetaCoset

The theta series `θ_{γ+L}(τ) = ∑_{v ∈ L} exp (π i ‖γ + v‖² τ)` of the translate `γ + L` of
`L : Submodule ℤ E`. For `γ` in the dual lattice this is the coset theta series of the coset
`γ + L`.

```lean
ZLattice.thetaCoset.{u_1} {E : Type u_1} [NormedAddCommGroup E] (L : Submodule ℤ E) (γ : E)
  (τ : UpperHalfPlane) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZLattice.thetaCoset`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Basic.html#ZLattice.thetaCoset).

## Sources

- [Tau Ceti documentation: `ZLattice.thetaCoset`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Basic.html#ZLattice.thetaCoset)
- [Source of `ZLattice.thetaCoset` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ThetaSeries/Basic.lean#L107)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
