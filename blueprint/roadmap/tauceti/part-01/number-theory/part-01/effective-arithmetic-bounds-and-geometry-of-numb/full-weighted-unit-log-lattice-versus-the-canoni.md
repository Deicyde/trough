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

- [Dirichlet's unit lattice theorem, with all places retained](../../part-03/number-field/dirichlets-unit-lattice-theorem-with-all-places.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Log/Covolume.html#TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume).

## Sources

- [Tau Ceti documentation: `TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Log/Covolume.html#TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume)
- [Source of `TauCeti.covolume_fullUnitLattice_fullLogEuclideanVolume` in TauCeti/NumberTheory/NumberField/Units/Log/Covolume.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/Units/Log/Covolume.lean#L220)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/EffectiveBounds/STATUS.md)
