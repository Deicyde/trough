---
declaration: module
origin: cited
lean: FluidDynamics.FluidFlow.velocityGradient, FluidDynamics.FluidFlow.newtonianStressTensor
statement: formalized
proof: formalized
---

# Newtonian stress tensors for fluid flows

The module `Physlib.FluidDynamics.FluidFlow.Newtonian`, [Physlib/FluidDynamics/FluidFlow/Newtonian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Newtonian.lean): 2 declarations, 2 with a docstring.

## i. Overview

> This module defines the velocity gradient and Newtonian stress tensor associated to a
> `FluidFlow`.

## ii. Key results

> - `FluidFlow.velocityGradient` : The spatial velocity-gradient matrix.
> - `FluidFlow.newtonianStressTensor` : The Newtonian stress tensor determined by pressure and
>   viscosity.

## iv. References

> * None.

## A. Newtonian stress tensor

**`FluidDynamics.FluidFlow.velocityGradient`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Newtonian.lean#L49).

> The spatial velocity-gradient matrix, with entries `partial_j u_i`.

```lean
noncomputable def velocityGradient (d : ℕ) (flow : FluidFlow d) :
    Time → Space d → Matrix (Fin d) (Fin d) ℝ
```

**`FluidDynamics.FluidFlow.newtonianStressTensor`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Newtonian.lean#L58).

> The Newtonian stress tensor
> `-p I + mu (grad u + grad u^T) + lambda (div u) I`.
>
> The scalar fields are pressure, shear viscosity, and second viscosity.

```lean
noncomputable def newtonianStressTensor (d : ℕ) (flow : FluidFlow d)
    (pressure shearViscosity secondViscosity : ScalarField d) : StressTensor d
```

## Depends on

- [Basic API for fluid flows](basic.md)
- [Divergence on Space](../../spaceandtime/space/part-01/derivatives-div.md)

## Sources

- [Physlib/FluidDynamics/FluidFlow/Newtonian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Newtonian.lean)
