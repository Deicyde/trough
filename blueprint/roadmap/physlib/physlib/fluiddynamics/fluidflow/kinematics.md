---
declaration: module
origin: cited
lean: FluidDynamics.FluidFlow.materialDerivative, FluidDynamics.FluidFlow.specificKineticEnergy
statement: formalized
proof: formalized
---

# Kinematic quantities for fluid flows

The module `Physlib.FluidDynamics.FluidFlow.Kinematics`, [Physlib/FluidDynamics/FluidFlow/Kinematics.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Kinematics.lean): 2 declarations, 2 with a docstring.

## i. Overview

> This module defines basic kinematic scalar quantities associated to `FluidFlow`.

## ii. Key results

> - `FluidFlow.materialDerivative` : The material derivative along a fluid velocity field.
> - `FluidFlow.specificKineticEnergy` : The specific kinetic energy `|u|^2 / 2`.

## iv. References

> * None.

## A. Flow-derived scalar quantities

**`FluidDynamics.FluidFlow.materialDerivative`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Kinematics.lean#L50).

> The material derivative `D_t f = partial_t f + u · grad f` of a scalar field.

```lean
noncomputable def materialDerivative (d : ℕ) (fluid : FluidFlow d)
    (field : ScalarField d) : ScalarField d
```

**`FluidDynamics.FluidFlow.specificKineticEnergy`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Kinematics.lean#L55).

> The specific kinetic energy `|u|^2 / 2` of a fluid flow.

```lean
noncomputable def specificKineticEnergy (d : ℕ) (fluid : FluidFlow d) : ScalarField d
```

## Depends on

- [Basic API for fluid flows](basic.md)
- [Gradient of functions and distributions on `Space d`](../../spaceandtime/space/part-01/derivatives-grad.md)
- [Time Derivatives](../../spaceandtime/time/derivatives.md)

## Sources

- [Physlib/FluidDynamics/FluidFlow/Kinematics.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Kinematics.lean)
