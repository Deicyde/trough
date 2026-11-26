---
declaration: module
origin: cited
lean: FluidDynamics.CauchyFlow.HasBodyForcePotential, FluidDynamics.CauchyFlow.HasConservativeBodyForce
statement: formalized
proof: formalized
---

# Body-force predicates for Cauchy flows

The module `Physlib.FluidDynamics.CauchyFlow.BodyForce`, [Physlib/FluidDynamics/CauchyFlow/BodyForce.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/FluidDynamics/CauchyFlow/BodyForce.lean): 2 declarations, 2 with a docstring.

## i. Overview

> This module defines predicates for conservative specific body forces on `CauchyFlow`.

## ii. Key results

> - `CauchyFlow.HasBodyForcePotential` : Predicate encoding the convention
>   `specificBodyForce = -grad Phi`.
> - `CauchyFlow.HasConservativeBodyForce` : Predicate saying the specific body force has some
>   potential.

## iv. References

> * None.

## A. Conservative-force convention

**`FluidDynamics.CauchyFlow.HasBodyForcePotential`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/FluidDynamics/CauchyFlow/BodyForce.lean#L50).

> A flow has body-force potential `Phi` when its specific body force is minus the gradient of
> `Phi`.

```lean
def HasBodyForcePotential (d : ℕ) (flow : CauchyFlow d) (potential : Space d → ℝ) : Prop
```

**`FluidDynamics.CauchyFlow.HasConservativeBodyForce`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/FluidDynamics/CauchyFlow/BodyForce.lean#L54).

> A flow has conservative body force when its specific body force has some potential.

```lean
def HasConservativeBodyForce (d : ℕ) (flow : CauchyFlow d) : Prop
```

## Depends on

- [Basic API for Cauchy flows](basic.md)
- [Gradient of functions and distributions on `Space d`](../../spaceandtime/space/part-01/derivatives-grad.md)

## Sources

- [Physlib/FluidDynamics/CauchyFlow/BodyForce.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/FluidDynamics/CauchyFlow/BodyForce.lean)
