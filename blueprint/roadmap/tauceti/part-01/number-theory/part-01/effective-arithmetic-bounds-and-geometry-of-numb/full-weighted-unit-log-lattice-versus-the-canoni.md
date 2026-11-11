---
declaration: theorem
origin: cited
lean: TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume
statement: formalized
proof: formalized
---

# Full weighted unit-log lattice versus the canonical regulator

For the induced
Euclidean Haar measure, the covolume of the existing full logarithmic unit lattice is
`sqrt (rank K + 1) * regulator K`.

```lean
TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume.{u_1} (K : Type u_1) [Field K]
  [NumberField K] :
  ZLattice.covolume (TauCeti.fullUnitLattice K) (TauCeti.fullLogEuclideanVolume K) =
    √(↑(NumberField.Units.rank K) + 1) * NumberField.Units.regulator K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dirichlet's unit lattice theorem, with all places retained](../../part-02/number-field/dirichlets-unit-lattice-theorem-with-all-places.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Log/Covolume.html#TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume).

## Sources

- [Tau Ceti documentation: `TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Log/Covolume.html#TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume)
- [Source of `TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume` in TauCeti/NumberTheory/NumberField/Units/Log/Covolume.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Units/Log/Covolume.lean#L220)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/EffectiveBounds/STATUS.md)
