---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Units.regulatorLowerBound_le_regulator
statement: formalized
proof: formalized
---

# An explicit regulator lower bound in every unit rank

If `d = [K : ℚ]` and
`r = rank K`, then `R_K ≥ (log 2 / (unitPowerCountBound d + 1)) ^ r / r!`.
The constant depends only on the degree and unit rank and is strictly positive.

```lean
TauCeti.NumberField.Units.regulatorLowerBound_le_regulator.{u_1} (K : Type u_1) [Field K]
  [NumberField K] :
  TauCeti.NumberField.Units.regulatorLowerBound (Module.finrank ℚ K) (NumberField.Units.rank K) ≤
    NumberField.Units.regulator K
```

## Depends on

- [TauCeti.NumberField.Units.unitPowerCountBound](tauceti-numberfield-units-unitpowercountbound.md)

## Proof depends on

- [Explicit unit height gap](explicit-unit-height-gap.md)
- [Minkowski's second theorem for the unit lattice](../heights-units-and-s-units-of-number-fields/minkowskis-second-theorem-for-the-unit-lattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.regulatorLowerBound_le_regulator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/Regulator.html#TauCeti.NumberField.Units.regulatorLowerBound_le_regulator).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.regulatorLowerBound_le_regulator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/Regulator.html#TauCeti.NumberField.Units.regulatorLowerBound_le_regulator)
- [Source of `TauCeti.NumberField.Units.regulatorLowerBound_le_regulator` in TauCeti/NumberTheory/EffectiveBounds/Regulator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/EffectiveBounds/Regulator.lean#L55)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/EffectiveBounds/STATUS.md)
