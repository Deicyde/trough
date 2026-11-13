---
declaration: module
origin: cited
lean: Electromagnetism.ElectricField, Electromagnetism.MagneticField, Electromagnetism.VectorPotential, Electromagnetism.EMSystem, Electromagnetism.ChargeDensity, Electromagnetism.CurrentDensity, Electromagnetism.EMSystem.c, Electromagnetism.EMSystem.coulombConstant
statement: formalized
proof: formalized
---

# A. Electromagnetism

The module `Physlib.Electromagnetism.Basic`, [Physlib/Electromagnetism/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean): 8 declarations, 8 with a docstring.

> Electromagnetism describes electric and magnetic fields, their potentials and sources, and the
> relations between them on space and spacetime. This module provides a compact foundational API used
> by more specialized electromagnetism modules in Physlib.

## A.1. Main definitions

> The module contains coordinate-level types for electric and magnetic fields, a spacetime vector
> potential, charge and current densities, and the constants describing an electromagnetic system.
> For an `EMSystem`, it also defines the speed of light and Coulomb's constant in terms of the vacuum
> permittivity and permeability.

## A.2. Current status

> The definitions here are intentionally lightweight. More developed APIs are organized under the
> `Kinematics`, `Dynamics`, `TemperedDistributional`, `ThreeDimension`, and `Vacuum` subdirectories.
> The abbreviations in this file remain useful as shared entry points while those APIs continue to
> converge.

…

**`Electromagnetism.ElectricField`**, an abbrev, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean#L44).

> The electric field is a map from `(d + 1)`-dimensional spacetime to `ℝ^d`.

```lean
abbrev ElectricField (d : ℕ := 3)
```

**`Electromagnetism.MagneticField`**, an abbrev, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean#L47).

> The magnetic field is a map from `(d + 1)`-dimensional spacetime to `ℝ^d`.

```lean
abbrev MagneticField (d : ℕ := 3)
```

**`Electromagnetism.VectorPotential`**, an abbrev, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean#L52).

> The vector potential of an electromagnetic field.

```lean
abbrev VectorPotential (d : ℕ := 3)
```

**`Electromagnetism.EMSystem`**, a structure, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean#L55).

> The electric permittivity and the magnetic permeability of free space.

```lean
structure EMSystem where
  /-- The permittivity of free space. -/
  ε₀ : ℝ
  /-- The permeability of free space. -/
  μ₀ : ℝ
```

**`Electromagnetism.ChargeDensity`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean#L68).

> The charge density.

```lean
abbrev ChargeDensity
```

**`Electromagnetism.CurrentDensity`**, an abbrev, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean#L71).

> The current density.

```lean
abbrev CurrentDensity
```

**`Electromagnetism.EMSystem.c`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean#L78).

> The speed of light.

```lean
noncomputable def c : ℝ
```

**`Electromagnetism.EMSystem.coulombConstant`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean#L81).

> Coulomb's constant.

```lean
noncomputable def coulombConstant : ℝ
```

## Depends on

- [Spacetime](../spaceandtime/spacetime/basic.md)

## Sources

- [Physlib/Electromagnetism/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Basic.lean)
