---
declaration: theorem
origin: cited
lean: TauCeti.GlobalNumberFields.adeleBaseChangeEquiv_tower
statement: formalized
proof: formalized
---

# TauCeti.GlobalNumberFields.adeleBaseChangeEquiv_tower

**Base change of adeles in a tower** `K ⊆ L ⊆ M`: the comparison for `M/K` factors through
the comparison for `L/K`, followed by the comparison for `M/L`.

```lean
TauCeti.GlobalNumberFields.adeleBaseChangeEquiv_tower.{u_1, u_2, u_3} (K : Type u_1) (L : Type u_2)
  [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L]
  [TopologicalSpace (TensorProduct K (NumberField.AdeleRing (NumberField.RingOfIntegers K) K) L)]
  [IsModuleTopology (NumberField.AdeleRing (NumberField.RingOfIntegers K) K)
      (TensorProduct K (NumberField.AdeleRing (NumberField.RingOfIntegers K) K) L)]
  (M : Type u_3) [Field M] [NumberField M] [Algebra K M] [Algebra L M] [IsScalarTower K L M]
  [TopologicalSpace (TensorProduct K (NumberField.AdeleRing (NumberField.RingOfIntegers K) K) M)]
  [IsModuleTopology (NumberField.AdeleRing (NumberField.RingOfIntegers K) K)
      (TensorProduct K (NumberField.AdeleRing (NumberField.RingOfIntegers K) K) M)]
  [TopologicalSpace (TensorProduct L (NumberField.AdeleRing (NumberField.RingOfIntegers L) L) M)]
  [IsModuleTopology (NumberField.AdeleRing (NumberField.RingOfIntegers L) L)
      (TensorProduct L (NumberField.AdeleRing (NumberField.RingOfIntegers L) L) M)]
  (a : NumberField.AdeleRing (NumberField.RingOfIntegers K) K) (z : M) :
  (TauCeti.GlobalNumberFields.adeleBaseChangeEquiv K M) (a ⊗ₜ[K] z) =
    (TauCeti.GlobalNumberFields.adeleBaseChangeEquiv L M)
      ((TauCeti.GlobalNumberFields.adeleBaseChangeEquiv K L) (a ⊗ₜ[K] 1) ⊗ₜ[L] z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.semilocalEquiv](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-semilocalequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.adeleBaseChangeEquiv_tower`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Adeles/BaseChange.html#TauCeti.GlobalNumberFields.adeleBaseChangeEquiv_tower).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.adeleBaseChangeEquiv_tower`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Adeles/BaseChange.html#TauCeti.GlobalNumberFields.adeleBaseChangeEquiv_tower)
- [Source of `TauCeti.GlobalNumberFields.adeleBaseChangeEquiv_tower` in TauCeti/NumberTheory/NumberField/Global/Adeles/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Global/Adeles/BaseChange.lean#L273)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/GlobalNumberFields/STATUS.md)
