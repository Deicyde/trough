---
declaration: module
origin: cited
lean: DimEnergy, DimEnergy.joule, DimEnergy.electronVolt, DimEnergy.calorie, DimEnergy.kilowattHour
statement: formalized
proof: formalized
---

# Energy

The module `Physlib.Units.WithDim.Energy`, [Physlib/Units/WithDim/Energy.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Energy.lean): 5 declarations, 5 with a docstring.

> In this module we define the dimensionful type corresponding to an energy.
> We define specific instances of energy.

**`DimEnergy`**, an abbrev, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Energy.lean#L24).

> Energy as a dimensional quantity with dimension `MLT⁻2`..

```lean
abbrev DimEnergy : Type
```

**`DimEnergy.joule`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Energy.lean#L30).

> The dimensional energy corresponding to 1 joule, J.

```lean
noncomputable def joule : DimEnergy
```

**`DimEnergy.electronVolt`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Energy.lean#L33).

> The dimensional energy corresponding to 1 electron volt, 1.602176634×10−19 J.

```lean
noncomputable def electronVolt : DimEnergy
```

**`DimEnergy.calorie`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Energy.lean#L36).

> The dimensional energy corresponding to 1 calorie, 4.184 J.

```lean
noncomputable def calorie : DimEnergy
```

**`DimEnergy.kilowattHour`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Energy.lean#L39).

> The dimensional energy corresponding to 1 kilowatt-hours, (3,600,000 J).

```lean
noncomputable def kilowattHour : DimEnergy
```

## Depends on

- [Physlib.Units.WithDim.Basic](basic.md)

## Sources

- [Physlib/Units/WithDim/Energy.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Energy.lean)
