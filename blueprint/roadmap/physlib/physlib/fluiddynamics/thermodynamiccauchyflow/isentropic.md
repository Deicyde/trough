---
declaration: module
origin: cited
lean: FluidDynamics.ThermodynamicCauchyFlow.IsIsentropic
statement: formalized
proof: formalized
---

# Isentropic thermodynamic Cauchy flows

The module `Physlib.FluidDynamics.ThermodynamicCauchyFlow.Isentropic`, [Physlib/FluidDynamics/ThermodynamicCauchyFlow/Isentropic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Isentropic.lean): 1 declaration, 1 with a docstring.

## i. Overview

> This module defines the isentropic predicate for thermodynamic Cauchy flows.

## ii. Key results

> - `ThermodynamicCauchyFlow.IsIsentropic` : A thermodynamic Cauchy flow whose entropy is
>   materially conserved.

## iv. References

> * None.

## A. Thermodynamic-flow predicates

**`FluidDynamics.ThermodynamicCauchyFlow.IsIsentropic`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Isentropic.lean#L46).

> A thermodynamic flow is isentropic when the entropy is materially conserved along the
> underlying fluid velocity field.

```lean
def IsIsentropic (d : ℕ) (flow : ThermodynamicCauchyFlow d) : Prop
```

## Depends on

- [Kinematic quantities for fluid flows](../fluidflow/kinematics.md)
- [Basic predicates for thermodynamic Cauchy flows](basic.md)

## Sources

- [Physlib/FluidDynamics/ThermodynamicCauchyFlow/Isentropic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Isentropic.lean)
