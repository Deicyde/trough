---
declaration: module
origin: cited
lean: FluidDynamics.FluidFlow.ClassicalContinuityEquation, FluidDynamics.FluidFlow.continuityResidual, FluidDynamics.FluidFlow.SmoothContinuityEquation, FluidDynamics.FluidFlow.classicalContinuityEquation_of_smoothContinuityEquation
statement: formalized
proof: formalized
---

# Continuity equation for fluid flows

The module `Physlib.FluidDynamics.FluidFlow.Continuity`, [Physlib/FluidDynamics/FluidFlow/Continuity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Continuity.lean): 4 declarations, 4 with a docstring.

## i. Overview

> This module defines the classical conservative mass-balance equation for a fluid flow and the
> corresponding continuity residual. These definitions are independent of a particular momentum
> equation, so they can be reused by Navier-Stokes, Euler, and other fluid models.

## ii. Key results

> - `FluidFlow.ClassicalContinuityEquation` : Classical conservation of mass in conservative form.
> - `FluidFlow.continuityResidual` : The scalar residual `partial_t rho + div (rho u)`.
> - `FluidFlow.SmoothContinuityEquation` : Continuity for globally differentiable fields.
> - `FluidFlow.classicalContinuityEquation_of_smoothContinuityEquation` : A smooth continuity
>   equation implies the classical continuity equation.

## iv. References

> * None.

## A. Continuity equations

**`FluidDynamics.FluidFlow.ClassicalContinuityEquation`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Continuity.lean#L58).

> Classical conservation of mass in conservative form, `partial_t rho + div (rho u) = 0`.
>
> The equation is asserted at points where the time derivative of `rho` and the spatial
> divergence of `rho u` are classical derivatives.

```lean
def ClassicalContinuityEquation (d : ℕ) (fluid : FluidFlow d) : Prop
```

**`FluidDynamics.FluidFlow.continuityResidual`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Continuity.lean#L65).

> The scalar continuity-equation residual
> `partial_t rho + div (rho u)`.

```lean
noncomputable def continuityResidual (d : ℕ) (fluid : FluidFlow d) : Time → Space d → ℝ
```

**`FluidDynamics.FluidFlow.SmoothContinuityEquation`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Continuity.lean#L74).

> A stronger continuity equation for globally differentiable fields.
>
> This version records the first-order regularity needed by the classical continuity equation:
> the density is differentiable in time, the mass flux `rho u` is differentiable in space, and
> the continuity residual vanishes everywhere.

```lean
def SmoothContinuityEquation (d : ℕ) (fluid : FluidFlow d) : Prop
```

**`FluidDynamics.FluidFlow.classicalContinuityEquation_of_smoothContinuityEquation`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Continuity.lean#L80).

> A smooth continuity equation satisfies the guarded classical continuity equation.

```lean
lemma classicalContinuityEquation_of_smoothContinuityEquation
    (d : ℕ) (fluid : FluidFlow d) :
    SmoothContinuityEquation d fluid → ClassicalContinuityEquation d fluid
```

## Depends on

- [Basic API for fluid flows](basic.md)
- [Divergence on Space](../../spaceandtime/space/part-01/derivatives-div.md)
- [Time Derivatives](../../spaceandtime/time/derivatives.md)

## Sources

- [Physlib/FluidDynamics/FluidFlow/Continuity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Continuity.lean)
