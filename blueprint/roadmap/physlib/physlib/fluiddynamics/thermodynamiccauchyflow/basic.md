---
declaration: module
origin: cited
lean: FluidDynamics.ThermodynamicCauchyFlow
statement: formalized
proof: formalized
---

# Basic predicates for thermodynamic Cauchy flows

The module `Physlib.FluidDynamics.ThermodynamicCauchyFlow.Basic`, [Physlib/FluidDynamics/ThermodynamicCauchyFlow/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Basic.lean): 1 declaration, 1 with a docstring.

## i. Overview

> This module defines `ThermodynamicCauchyFlow`, the thermodynamic layer currently needed for
> isentropic and Bernoulli-type statements.
>
> This structure is intentionally the minimal carrier for the present thermodynamic API, not a claim
> that entropy and enthalpy describe every thermodynamic process. Temperature, heat flux, and other
> state data should be introduced by a further extension when an energy or heat-transport law needs
> them. Keeping those fields out here lets Bernoulli and isentropic results avoid assumptions
> unrelated to their statements.

## ii. Key results

> - `ThermodynamicCauchyFlow` : A Cauchy flow with entropy and enthalpy fields.

## iv. References

> * None.

## A. Thermodynamic Cauchy-flow structure

**`FluidDynamics.ThermodynamicCauchyFlow`**, a structure, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Basic.lean#L52).

> A Cauchy flow equipped with thermodynamic entropy and enthalpy fields.
>
> These fields are independent of the kinematic and momentum-balance data unless additional
> thermodynamic constitutive laws are imposed. They are sufficient for the current isentropic and
> Bernoulli APIs; other thermodynamic fields belong in later extensions that require them.

```lean
structure ThermodynamicCauchyFlow (d : ℕ) extends CauchyFlow d where
  /-- The specific entropy field. -/
  entropy : ScalarField d
  /-- The specific enthalpy field. -/
  enthalpy : ScalarField d
```

## Depends on

- [Basic API for Cauchy flows](../cauchyflow/basic.md)

## Sources

- [Physlib/FluidDynamics/ThermodynamicCauchyFlow/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/ThermodynamicCauchyFlow/Basic.lean)
