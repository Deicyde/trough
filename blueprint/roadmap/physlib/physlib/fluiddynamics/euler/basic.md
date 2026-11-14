---
declaration: module
origin: cited
lean: FluidDynamics.euler_iff_convectiveEuler, FluidDynamics.Euler, FluidDynamics.ConvectiveEuler
statement: formalized
proof: formalized
---

# Euler equation for fluid flows

The module `Physlib.FluidDynamics.Euler.Basic`, [Physlib/FluidDynamics/Euler/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Euler/Basic.lean): 3 declarations, 3 with a docstring, 1 listed as significant.

## i. Overview

> This module defines the Euler equations for inviscid fluid flow as continuity, Cauchy momentum,
> and an inviscid stress law. The pressure field appears through the constitutive relation for
> the Cauchy stress tensor rather than as a field of the flow data.

## ii. Key results

> - `Euler` : Classical continuity, Cauchy momentum, and inviscid stress together.
> - `ConvectiveEuler` : Classical continuity, convective Cauchy momentum, and inviscid stress.
> - `euler_iff_convectiveEuler` : Equivalence of the conservative and convective forms when the
>   fields are differentiable.

## iv. References

> * None.

## A. Euler equations

**`FluidDynamics.Euler`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Euler/Basic.lean#L48).

> The conservative Euler equations: continuity, Cauchy momentum, and inviscid stress.

```lean
def Euler (d : ℕ) (flow : CauchyFlow d) (pressure : ScalarField d) : Prop
```

**`FluidDynamics.ConvectiveEuler`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Euler/Basic.lean#L54).

> The convective Euler equations: continuity, convective Cauchy momentum, and inviscid
> stress.

```lean
def ConvectiveEuler (d : ℕ) (flow : CauchyFlow d) (pressure : ScalarField d) : Prop
```

## B. Equivalence of conservative and convective Euler forms

**`FluidDynamics.euler_iff_convectiveEuler`**, a theorem, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Euler/Basic.lean#L66). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The conservative and convective Euler forms are equivalent when the fields are
> differentiable enough for the product rules.

```lean
theorem euler_iff_convectiveEuler
    (d : ℕ) (flow : CauchyFlow d) (pressure : ScalarField d)
    (hRhoTime : ∀ t x, DifferentiableAt ℝ (flow.rho · x) t)
    (hVelocityTime : ∀ t x, DifferentiableAt ℝ (flow.velocity · x) t)
    (hMomentumDensity : ∀ t,
      Differentiable ℝ (FluidFlow.momentumDensity d flow.toFluidFlow t))
    (hVelocitySpace : ∀ t, Differentiable ℝ (flow.velocity t)) :
    Euler d flow pressure ↔ ConvectiveEuler d flow pressure
```

## Depends on

- [Inviscid stress laws for Cauchy flows](../cauchyflow/inviscid.md)
- [Cauchy momentum equations](../cauchyflow/momentum.md)

## Sources

- [Physlib/FluidDynamics/Euler/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/Euler/Basic.lean)
