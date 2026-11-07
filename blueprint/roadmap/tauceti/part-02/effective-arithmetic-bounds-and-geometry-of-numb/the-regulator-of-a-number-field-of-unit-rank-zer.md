---
declaration: theorem
origin: cited
lean: NumberField.Units.regulator_eq_one_of_rank_eq_zero
statement: formalized
proof: formalized
---

# The regulator of a number field of unit rank zero is `1`

When the unit rank is zero,
the unit lattice sits inside the zero-dimensional log space, and the regulator — its covolume,
computed by `NumberField.Units.regulator_eq_det'` as a determinant indexed by the infinite
places other than the distinguished one — is the determinant of the empty matrix, `1`.

```lean
NumberField.Units.regulator_eq_one_of_rank_eq_zero.{u_1} (K : Type u_1) [Field K] [NumberField K]
  (h : NumberField.Units.rank K = 0) : NumberField.Units.regulator K = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.Units.regulator_eq_one_of_rank_eq_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/Regulator.html#NumberField.Units.regulator_eq_one_of_rank_eq_zero).

## Sources

- [Tau Ceti documentation: `NumberField.Units.regulator_eq_one_of_rank_eq_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/Regulator.html#NumberField.Units.regulator_eq_one_of_rank_eq_zero)
- [Source of `NumberField.Units.regulator_eq_one_of_rank_eq_zero` in TauCeti/NumberTheory/EffectiveBounds/Regulator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/EffectiveBounds/Regulator.lean#L58)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/EffectiveBounds/STATUS.md)
