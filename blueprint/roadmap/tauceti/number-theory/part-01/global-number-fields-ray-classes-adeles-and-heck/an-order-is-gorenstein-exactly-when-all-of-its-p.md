---
declaration: theorem
origin: cited
lean: TauCeti.GlobalNumberFields.NumberFieldOrder.isGorenstein_iff_forall_isUnit
statement: formalized
proof: formalized
---

# An order is Gorenstein exactly when all of its proper fractional ideals are invertible

```lean
TauCeti.GlobalNumberFields.NumberFieldOrder.isGorenstein_iff_forall_isUnit.{u} {K : Type u}
  [Field K] [NumberField K] (O : TauCeti.GlobalNumberFields.NumberFieldOrder K) :
  O.IsGorenstein ↔
    ∀ (I : FractionalIdeal (nonZeroDivisors ↥O.toSubalgebra) K),
      O.IsProperFractionalIdeal I → IsUnit I
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.NumberFieldOrder.isGorenstein_iff_forall_isUnit`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Orders/Gorenstein.html#TauCeti.GlobalNumberFields.NumberFieldOrder.isGorenstein_iff_forall_isUnit).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.NumberFieldOrder.isGorenstein_iff_forall_isUnit`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Orders/Gorenstein.html#TauCeti.GlobalNumberFields.NumberFieldOrder.isGorenstein_iff_forall_isUnit)
- [Source of `TauCeti.GlobalNumberFields.NumberFieldOrder.isGorenstein_iff_forall_isUnit` in TauCeti/NumberTheory/NumberField/Global/Orders/Gorenstein.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Global/Orders/Gorenstein.lean#L353)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/GlobalNumberFields/STATUS.md)
