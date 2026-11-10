---
declaration: def
origin: cited
lean: ZLattice.thetaSeries
statement: formalized
---

# ZLattice.thetaSeries

The theta series `Θ_L(τ) = ∑_{v ∈ L} exp (π i ‖v‖² τ)` of `L : Submodule ℤ E`. It converges
on `ℍ` when `L` is discrete and `E` is finite-dimensional (`ZLattice.summable_thetaSeries`).

```lean
ZLattice.thetaSeries.{u_1} {E : Type u_1} [NormedAddCommGroup E] (L : Submodule ℤ E)
  (τ : UpperHalfPlane) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZLattice.thetaSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Basic.html#ZLattice.thetaSeries).

## Sources

- [Tau Ceti documentation: `ZLattice.thetaSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Basic.html#ZLattice.thetaSeries)
- [Source of `ZLattice.thetaSeries` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ThetaSeries/Basic.lean#L102)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
