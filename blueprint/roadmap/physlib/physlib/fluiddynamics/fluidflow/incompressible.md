---
declaration: module
origin: cited
lean: FluidDynamics.FluidFlow.incompressibilityResidual, FluidDynamics.FluidFlow.ClassicalIncompressible, FluidDynamics.FluidFlow.SmoothIncompressible, FluidDynamics.FluidFlow.classicalIncompressible_of_smoothIncompressible
statement: formalized
proof: formalized
---

# Incompressible fluid flows

The module `Physlib.FluidDynamics.FluidFlow.Incompressible`, [Physlib/FluidDynamics/FluidFlow/Incompressible.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Incompressible.lean): 4 declarations, 4 with a docstring.

## i. Overview

> This module defines general incompressibility predicates for fluid flows. These predicates are
> not tied to a particular equation of motion, so they can be reused later by incompressible
> Navier-Stokes, incompressible Euler, and Bernoulli-style developments.

## ii. Key results

> - `FluidFlow.incompressibilityResidual` : The divergence of the velocity field.
> - `FluidFlow.ClassicalIncompressible` : Incompressibility guarded by velocity differentiability.
> - `FluidFlow.SmoothIncompressible` : Incompressibility with globally differentiable velocity.
> - `FluidFlow.classicalIncompressible_of_smoothIncompressible` : Smooth incompressibility implies
>   classical incompressibility.

## iv. References

> * None.

## A. Incompressibility predicates

**`FluidDynamics.FluidFlow.incompressibilityResidual`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Incompressible.lean#L52).

> The incompressibility residual, given by the divergence of the velocity field.

```lean
noncomputable def incompressibilityResidual (d : ℕ) (fluid : FluidFlow d) :
    Time → Space d → ℝ
```

**`FluidDynamics.FluidFlow.ClassicalIncompressible`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Incompressible.lean#L58).

> A classical incompressible flow has divergence-free velocity at points where the velocity
> field is differentiable.

```lean
def ClassicalIncompressible (d : ℕ) (fluid : FluidFlow d) : Prop
```

**`FluidDynamics.FluidFlow.SmoothIncompressible`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Incompressible.lean#L64).

> A smooth incompressible flow has globally differentiable velocity and vanishing
> incompressibility residual everywhere.

```lean
def SmoothIncompressible (d : ℕ) (fluid : FluidFlow d) : Prop
```

**`FluidDynamics.FluidFlow.classicalIncompressible_of_smoothIncompressible`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Incompressible.lean#L69).

> A smooth incompressible flow is classically incompressible.

```lean
lemma classicalIncompressible_of_smoothIncompressible
    (d : ℕ) (fluid : FluidFlow d) :
    SmoothIncompressible d fluid → ClassicalIncompressible d fluid
```

## Depends on

- [Basic API for fluid flows](basic.md)
- [Divergence on Space](../../spaceandtime/space/part-01/derivatives-div.md)

## Sources

- [Physlib/FluidDynamics/FluidFlow/Incompressible.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Incompressible.lean)
