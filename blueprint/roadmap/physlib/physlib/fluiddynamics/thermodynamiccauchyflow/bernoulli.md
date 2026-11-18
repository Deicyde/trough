---
declaration: module
origin: cited
lean: FluidDynamics.bernoulliFunction, FluidDynamics.LocalBernoulliLaw, FluidDynamics.BernoulliLaw
statement: formalized
proof: formalized
---

# Bernoulli theory for thermodynamic Cauchy flows

The module `Physlib.FluidDynamics.ThermodynamicCauchyFlow.Bernoulli`, [Physlib/FluidDynamics/ThermodynamicCauchyFlow/Bernoulli.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Bernoulli.lean): 3 declarations, 3 with a docstring.

## i. Overview

> This module is reserved for Bernoulli definitions and results based on the shared
> `ThermodynamicCauchyFlow` data together with an explicit external potential parameter, rather
> than defining a separate Bernoulli-flow structure.

## ii. Key results

> - `bernoulliFunction` : The Bernoulli function `|u|^2 / 2 + h + Phi`.
> - `LocalBernoulliLaw` : Vanishing spatial gradient of the Bernoulli function.
> - `BernoulliLaw` : Spatial constancy of the Bernoulli function at each time.

## iv. References

> * None.

## A. Bernoulli function

**`FluidDynamics.bernoulliFunction`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Bernoulli.lean#L49).

> The Bernoulli function `|u|^2 / 2 + h + Phi`.

```lean
noncomputable def bernoulliFunction
    (d : ℕ) (flow : ThermodynamicCauchyFlow d) (potential : Space d → ℝ) : ScalarField d
```

## B. Bernoulli-law predicates

**`FluidDynamics.LocalBernoulliLaw`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Bernoulli.lean#L61).

> A local Bernoulli law: the Bernoulli function has zero spatial gradient.

```lean
def LocalBernoulliLaw
    (d : ℕ) (flow : ThermodynamicCauchyFlow d) (potential : Space d → ℝ) : Prop
```

**`FluidDynamics.BernoulliLaw`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Bernoulli.lean#L66).

> A global Bernoulli law: the Bernoulli function is spatially constant at each time.

```lean
def BernoulliLaw
    (d : ℕ) (flow : ThermodynamicCauchyFlow d) (potential : Space d → ℝ) : Prop
```

## Depends on

- [Kinematic quantities for fluid flows](../fluidflow/kinematics.md)
- [Basic predicates for thermodynamic Cauchy flows](basic.md)

## Sources

- [Physlib/FluidDynamics/ThermodynamicCauchyFlow/Bernoulli.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Bernoulli.lean)
