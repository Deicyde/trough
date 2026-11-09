---
declaration: theorem
origin: cited
lean: TauCeti.isZLattice_fullUnitLattice
statement: formalized
proof: formalized
---

# Dirichlet's unit lattice theorem, with all places retained

The logarithmic image of
the units is a full integral lattice in the sum-zero hyperplane.

```lean
TauCeti.isZLattice_fullUnitLattice.{u_1} (K : Type u_1) [Field K] [NumberField K] :
  IsZLattice ℝ (TauCeti.fullUnitLattice K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isZLattice_fullUnitLattice`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Log/Hyperplane.html#TauCeti.isZLattice_fullUnitLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.isZLattice_fullUnitLattice`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Log/Hyperplane.html#TauCeti.isZLattice_fullUnitLattice)
- [Source of `TauCeti.isZLattice_fullUnitLattice` in TauCeti/NumberTheory/NumberField/Units/Log/Hyperplane.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Units/Log/Hyperplane.lean#L139)
