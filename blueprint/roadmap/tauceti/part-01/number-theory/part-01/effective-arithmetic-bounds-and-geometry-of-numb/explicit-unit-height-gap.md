---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight₁
statement: formalized
proof: formalized
---

# Explicit unit height gap

Every nontorsion unit of a degree-`d` number field has
relative logarithmic height at least `log 2 / (unitPowerCountBound d + 1)`.

```lean
TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight₁.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {u : (NumberField.RingOfIntegers K)ˣ} (hu : u ∉ NumberField.Units.torsion K) :
  TauCeti.NumberField.Units.unitHeightLowerBound (Module.finrank ℚ K) ≤
    Height.logHeight₁ ((algebraMap (NumberField.RingOfIntegers K) K) ↑u)
```

## Depends on

- [TauCeti.NumberField.Units.unitPowerCountBound](tauceti-numberfield-units-unitpowercountbound.md)

## Proof depends on

- [Liouville's inequality at a finite place](../../part-02/number-field/liouvilles-inequality-at-a-finite-place.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/UnitHeight.html#TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight%E2%82%81).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/UnitHeight.html#TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight%E2%82%81)
- [Source of `TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight₁` in TauCeti/NumberTheory/EffectiveBounds/UnitHeight.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/EffectiveBounds/UnitHeight.lean#L106)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/EffectiveBounds/STATUS.md)
