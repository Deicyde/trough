---
declaration: module
origin: cited
lean: FluidDynamics.FluidFlow
statement: formalized
proof: formalized
---

# Basic API for fluid flows

The module `Physlib.FluidDynamics.FluidFlow.Basic`, [Physlib/FluidDynamics/FluidFlow/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Basic.lean): 1 declaration, 1 with a docstring.

## i. Overview

> This module defines `FluidFlow`, the kinematic and mass-transport layer of the fluid API.
>
> The fluid API is split according to which physical processes require which data. Density and
> velocity are sufficient at this first layer: they determine the mass flux, momentum density,
> convective momentum flux, and material derivatives used in continuity and kinematic statements.
>
> Stress, body force, and thermodynamic fields are deliberately excluded. Kinematic and
> mass-transport statements do not require them, while adding them here would force those statements
> to depend on unrelated dynamic or constitutive choices. The extension structures add such data
> only at the layer where it becomes necessary.

## ii. Key results

> - `FluidFlow` : The density and velocity fields of a fluid.

## iv. References

> * None.

## A. Fluid-flow structure

**`FluidDynamics.FluidFlow`**, a structure, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Basic.lean#L54).

> The density and velocity fields of a fluid on `d`-dimensional space.
>
> These fields are the independent data needed for kinematics and mass transport. Quantities such as
> mass flux, momentum density, and material acceleration are derived from them. Dynamic and
> thermodynamic fields are introduced only by extension structures whose statements need them.

```lean
structure FluidFlow (d : ℕ) where
  /-- The mass density field. -/
  rho : MassDensity d
  /-- The velocity field. -/
  velocity : VelocityField d
```

## Depends on

- [Basic field types for fluid dynamics](../basic.md)

## Sources

- [Physlib/FluidDynamics/FluidFlow/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Basic.lean)
