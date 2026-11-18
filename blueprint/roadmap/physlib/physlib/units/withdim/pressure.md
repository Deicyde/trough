---
declaration: module
origin: cited
lean: DimPressure, DimPressure.pascal, DimPressure.millimeterOfMercury, DimPressure.bar, DimPressure.standardAtmosphere, DimPressure.torr, DimPressure.psi
statement: formalized
proof: formalized
---

# Pressure

The module `Physlib.Units.WithDim.Pressure`, [Physlib/Units/WithDim/Pressure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean): 7 declarations, 7 with a docstring.

> In this module we define the dimensionful type corresponding to an pressure.
> We define specific instances of pressure.

**`DimPressure`**, an abbrev, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean#L24).

> Pressure as a dimensional quantity with dimension `ML⁻¹T⁻2`..

```lean
abbrev DimPressure : Type
```

**`DimPressure.pascal`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean#L30).

> The dimensional pressure corresponding to 1 pascal, Pa.

```lean
noncomputable def pascal : DimPressure
```

**`DimPressure.millimeterOfMercury`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean#L33).

> The dimensional pressure corresponding to 1 millimeter of mercury (133.322387415 pascals).

```lean
noncomputable def millimeterOfMercury : DimPressure
```

**`DimPressure.bar`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean#L36).

> The dimensional pressure corresponding to 1 bar (100,000 pascals).

```lean
noncomputable def bar : DimPressure
```

**`DimPressure.standardAtmosphere`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean#L39).

> The dimensional pressure corresponding to 1 standard atmosphere (101,325 pascals).

```lean
noncomputable def standardAtmosphere : DimPressure
```

**`DimPressure.torr`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean#L42).

> The dimensional pressure corresponding to 1 torr (1/760 of standard atmosphere pressure).

```lean
noncomputable def torr : DimPressure
```

**`DimPressure.psi`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean#L45).

> The dimensional pressure corresponding to 1 pound per square inch.

```lean
noncomputable def psi : DimPressure
```

## Depends on

- [Physlib.Units.WithDim.Basic](basic.md)

## Sources

- [Physlib/Units/WithDim/Pressure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/WithDim/Pressure.lean)
