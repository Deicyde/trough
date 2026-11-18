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

- [Liouville's inequality at a finite place](../../part-03/number-field/liouvilles-inequality-at-a-finite-place.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/UnitHeight.html#TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight%E2%82%81).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight₁`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/UnitHeight.html#TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight%E2%82%81)
- [Source of `TauCeti.NumberField.Units.unitHeightLowerBound_le_logHeight₁` in TauCeti/NumberTheory/EffectiveBounds/UnitHeight.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/EffectiveBounds/UnitHeight.lean#L106)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/EffectiveBounds/STATUS.md)
