---
declaration: module
origin: cited
lean: FluidDynamics.CauchyFlow.IsNewtonian
statement: formalized
proof: formalized
---

# Newtonian stress law for Cauchy flows

The module `Physlib.FluidDynamics.CauchyFlow.Newtonian`, [Physlib/FluidDynamics/CauchyFlow/Newtonian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Newtonian.lean): 1 declaration, 1 with a docstring.

## i. Overview

> This module defines the Newtonian constitutive stress law for `CauchyFlow`.

## ii. Key results

> - `CauchyFlow.IsNewtonian` : Predicate saying the Cauchy stress has Newtonian constitutive form.

## iv. References

> * None.

## A. Newtonian Cauchy flows

**`FluidDynamics.CauchyFlow.IsNewtonian`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Newtonian.lean#L44).

> A Cauchy flow is Newtonian when its stress tensor has the Newtonian constitutive form.

```lean
def IsNewtonian
    (d : ℕ) (flow : CauchyFlow d)
    (pressure shearViscosity secondViscosity : ScalarField d) : Prop
```

## Depends on

- [Basic API for Cauchy flows](basic.md)
- [Newtonian stress tensors for fluid flows](../fluidflow/newtonian.md)

## Sources

- [Physlib/FluidDynamics/CauchyFlow/Newtonian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Newtonian.lean)
