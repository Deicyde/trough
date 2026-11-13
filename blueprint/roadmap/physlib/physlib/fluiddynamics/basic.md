---
declaration: module
origin: cited
lean: FluidDynamics.ScalarField, FluidDynamics.VectorField, FluidDynamics.MassDensity, FluidDynamics.VelocityField, FluidDynamics.MomentumDensityField, FluidDynamics.StressTensor
statement: formalized
proof: formalized
---

# Basic field types for fluid dynamics

The module `Physlib.FluidDynamics.Basic`, [Physlib/FluidDynamics/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Basic.lean): 6 declarations, 6 with a docstring.

## i. Overview

> This module defines the basic field types used to describe a fluid on `d`-dimensional space.
> The structure-specific APIs are organized in the corresponding `FluidFlow`, `CauchyFlow`, and
> `ThermodynamicCauchyFlow` subdirectories.

## ii. Key results

> - `ScalarField` : A time-dependent scalar field on space.
> - `VectorField` : A time-dependent vector field on space.
> - `MassDensity` : A time-dependent scalar density field.
> - `VelocityField` : A time-dependent vector velocity field.
> - `MomentumDensityField` : A time-dependent vector momentum density field.
> - `StressTensor` : A time-dependent matrix-valued stress field.

## iv. References

> * None.

## A. Field types

**`FluidDynamics.ScalarField`**, an abbrev, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Basic.lean#L52).

> A scalar field on `d`-dimensional space, depending on time.

```lean
abbrev ScalarField (d : ℕ)
```

**`FluidDynamics.VectorField`**, an abbrev, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Basic.lean#L55).

> A vector field on `d`-dimensional space, depending on time.

```lean
abbrev VectorField (d : ℕ)
```

**`FluidDynamics.MassDensity`**, an abbrev, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Basic.lean#L58).

> A mass density field on `d`-dimensional space.

```lean
abbrev MassDensity (d : ℕ)
```

**`FluidDynamics.VelocityField`**, an abbrev, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Basic.lean#L61).

> A velocity field on `d`-dimensional space.

```lean
abbrev VelocityField (d : ℕ)
```

**`FluidDynamics.MomentumDensityField`**, an abbrev, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Basic.lean#L64).

> A momentum density field on `d`-dimensional space.

```lean
abbrev MomentumDensityField (d : ℕ)
```

**`FluidDynamics.StressTensor`**, an abbrev, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Basic.lean#L67).

> A matrix-valued stress tensor field on `d`-dimensional space.

```lean
abbrev StressTensor (d : ℕ)
```

## Depends on

- [Space](../spaceandtime/space/part-01/basic.md)
- [Time](../spaceandtime/time/basic.md)

## Sources

- [Physlib/FluidDynamics/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Basic.lean)
