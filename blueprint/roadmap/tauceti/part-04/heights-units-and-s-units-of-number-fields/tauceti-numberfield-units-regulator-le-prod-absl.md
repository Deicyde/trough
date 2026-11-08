---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Units.regulator_le_prod_absLogHeight₁
statement: formalized
proof: formalized
---

# TauCeti.NumberField.Units.regulator_le_prod_absLogHeight₁

Every fundamental system bounds the field regulator by `(2d) ^ r` times the product
of its absolute logarithmic heights, where `d` is the degree and `r` the unit rank.

```lean
TauCeti.NumberField.Units.regulator_le_prod_absLogHeight₁.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {ε : Fin (NumberField.Units.rank K) → (NumberField.RingOfIntegers K)ˣ}
  (hε : Subgroup.closure (Set.range ε) ⊔ NumberField.Units.torsion K = ⊤) :
  NumberField.Units.regulator K ≤
    (2 * ↑(Module.finrank ℚ K)) ^ NumberField.Units.rank K *
      ∏ i, NumberField.absLogHeight₁ ((algebraMap (NumberField.RingOfIntegers K) K) ↑(ε i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.regulator_le_prod_absLogHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Regulator/Height.html#TauCeti.NumberField.Units.regulator_le_prod_absLogHeight%E2%82%81).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.regulator_le_prod_absLogHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Regulator/Height.html#TauCeti.NumberField.Units.regulator_le_prod_absLogHeight%E2%82%81)
- [Source of `TauCeti.NumberField.Units.regulator_le_prod_absLogHeight₁` in TauCeti/NumberTheory/NumberField/Units/Regulator/Height.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Units/Regulator/Height.lean#L80)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HeightsAndUnits/STATUS.md)
