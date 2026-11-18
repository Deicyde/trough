---
declaration: module
origin: cited
lean: FluidDynamics.CauchyFlow
statement: formalized
proof: formalized
---

# Basic API for Cauchy flows

The module `Physlib.FluidDynamics.CauchyFlow.Basic`, [Physlib/FluidDynamics/CauchyFlow/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Basic.lean): 1 declaration, 1 with a docstring.

## i. Overview

> This module defines `CauchyFlow`, the momentum-balance layer of the fluid API.
> Specialized predicates and equations for Cauchy flows are organized in sibling modules.
>
> A local Cauchy momentum balance needs two kinds of force data beyond density and velocity. The
> stress tensor encodes contact forces through its divergence, while the specific body force encodes
> volumetric forces per unit mass and therefore contributes mass density times specific body force.
> Together these fields are sufficient to state the balance without choosing a material model.
>
> The momentum equation constrains the flow and forces but does not define a constitutive relation
> between them. Pressure and viscosity are therefore not stored as additional fields.
> They enter through constitutive stress laws, such as the inviscid and Newtonian predicates,
> which avoids duplicating data and imposing consistency conditions inside the carrier.
> Thermodynamic data is deferred to `ThermodynamicCauchyFlow` because it is not needed
> for momentum balance alone.

## ii. Key results

> - `CauchyFlow` : A fluid flow with Cauchy stress and specific body force.

## iv. References

> * None.

## A. Cauchy-flow structure

**`FluidDynamics.CauchyFlow`**, a structure, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Basic.lean#L59).

> A fluid flow equipped with Cauchy stress and specific body-force fields.
>
> These are the additional independent fields needed to state a local momentum balance. The Cauchy
> stress represents contact forces, and the specific body force represents volumetric force per unit
> mass. Pressure and viscosity enter through stress laws rather than as redundant fields of
> `CauchyFlow` itself.

```lean
structure CauchyFlow (d : ℕ) extends FluidFlow d where
  /-- The Cauchy stress tensor field. -/
  stress : StressTensor d
  /-- The specific body-force field, i.e. force per unit mass. -/
  specificBodyForce : VectorField d
```

## Depends on

- [Basic API for fluid flows](../fluidflow/basic.md)

## Sources

- [Physlib/FluidDynamics/CauchyFlow/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Basic.lean)
