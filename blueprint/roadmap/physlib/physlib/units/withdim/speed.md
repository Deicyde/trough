---
declaration: module
origin: cited
lean: DimSpeed, DimSpeed.oneMeterPerSecond, DimSpeed.oneMilePerHour, DimSpeed.oneKilometerPerHour, DimSpeed.oneKnot, DimSpeed.oneMeterPerSecond_in_SI, DimSpeed.oneMilePerHour_in_SI, DimSpeed.oneKilometerPerHour_in_SI
statement: formalized
proof: formalized
---

# Speed

The module `Physlib.Units.WithDim.Speed`, [Physlib/Units/WithDim/Speed.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean): 12 declarations, 5 with a docstring.

> In this module we define the dimensionful type corresponding to an speed.
> We define specific instances of speed, such as miles per hour, kilometers per hour, etc.

**`DimSpeed`**, an abbrev, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L24).

> The type of speeds in the absence of a choice of unit.

```lean
abbrev DimSpeed : Type
```

## Basic speeds

**`DimSpeed.oneMeterPerSecond`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L38).

> The dimensional speed corresponding to 1 meter per second.

```lean
noncomputable def oneMeterPerSecond : DimSpeed
```

**`DimSpeed.oneMilePerHour`**, a def, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L41).

> The dimensional speed corresponding to 1 mile per hour.

```lean
noncomputable def oneMilePerHour : DimSpeed
```

**`DimSpeed.oneKilometerPerHour`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L45).

> The dimensional speed corresponding to 1 kilometer per hour.

```lean
noncomputable def oneKilometerPerHour : DimSpeed
```

**`DimSpeed.oneKnot`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L49).

> The dimensional speed corresponding to 1 knot, aka, one nautical mile per hour.

```lean
noncomputable def oneKnot : DimSpeed
```

## Speed in SI units

**`DimSpeed.oneMeterPerSecond_in_SI`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L59).

```lean
lemma oneMeterPerSecond_in_SI : oneMeterPerSecond SI = ⟨1⟩
```

**`DimSpeed.oneMilePerHour_in_SI`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L64).

```lean
lemma oneMilePerHour_in_SI : oneMilePerHour SI = ⟨0.44704⟩
```

**`DimSpeed.oneKilometerPerHour_in_SI`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L72).

```lean
lemma oneKilometerPerHour_in_SI :
    oneKilometerPerHour SI = ⟨5/18⟩
```

**`DimSpeed.oneKnot_in_SI`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L83).

```lean
lemma oneKnot_in_SI : oneKnot SI = ⟨463/900⟩
```

## Relations between speeds

**`DimSpeed.oneKnot_eq_mul_oneKilometerPerHour`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L97).

```lean
lemma oneKnot_eq_mul_oneKilometerPerHour :
    oneKnot = (1.852 : ℝ≥0) • oneKilometerPerHour
```

**`DimSpeed.oneKilometerPerHour_eq_mul_oneKnot`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L104).

```lean
lemma oneKilometerPerHour_eq_mul_oneKnot:
    oneKilometerPerHour = (250/463 : ℝ≥0) • oneKnot
```

**`DimSpeed.oneMeterPerSecond_eq_mul_oneMilePerHour`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean#L111).

```lean
lemma oneMeterPerSecond_eq_mul_oneMilePerHour :
    oneMeterPerSecond = (3125/1397 : ℝ≥0) • oneMilePerHour
```

## Depends on

- [Physlib.Units.WithDim.Basic](basic.md)

## Sources

- [Physlib/Units/WithDim/Speed.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Speed.lean)
