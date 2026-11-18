---
declaration: module
origin: cited
lean: FluidDynamics.navier_stokes_iff_convective_navier_stokes, FluidDynamics.NavierStokes, FluidDynamics.ConvectiveNavierStokes
statement: formalized
proof: formalized
---

# The Navier-Stokes equations

The module `Physlib.FluidDynamics.CauchyFlow.NavierStokes`, [Physlib/FluidDynamics/CauchyFlow/NavierStokes.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/NavierStokes.lean): 3 declarations, 3 with a docstring, 1 listed as significant.

## i. Overview

> The Navier-Stokes equations are a set of partial differential equations that describe
> the motion of viscous fluid substances. They are fundamental in fluid dynamics and are
> used to model the behavior of fluids in various contexts, including gas flow and water flow.
>
> This file defines the Navier-Stokes equations as continuity, Cauchy momentum, and a Newtonian
> stress law. The Cauchy momentum equation supplies the balance-law layer, while
> `CauchyFlow.IsNewtonian` specializes the stress tensor through pressure and viscosity fields.

## ii. Key results

> - `NavierStokes` : Classical continuity, Cauchy momentum, and Newtonian stress together.
> - `ConvectiveNavierStokes` : Classical continuity, convective Cauchy momentum, and Newtonian
>   stress together.
> - `navier_stokes_iff_convective_navier_stokes` : Equivalence of the two forms when the fields
>   are differentiable.

## iv. References

> * None.

## A. Navier-Stokes equations

**`FluidDynamics.NavierStokes`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/NavierStokes.lean#L54).

> The conservative Navier-Stokes equations: continuity, Cauchy momentum, and Newtonian
> stress.

```lean
def NavierStokes
    (d : ℕ) (flow : CauchyFlow d)
    (pressure shearViscosity secondViscosity : ScalarField d) : Prop
```

**`FluidDynamics.ConvectiveNavierStokes`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/NavierStokes.lean#L63).

> The convective Navier-Stokes equations: continuity, convective Cauchy momentum, and
> Newtonian stress.

```lean
def ConvectiveNavierStokes
    (d : ℕ) (flow : CauchyFlow d)
    (pressure shearViscosity secondViscosity : ScalarField d) : Prop
```

## B. Equivalence of conservative and convective Navier-Stokes forms

**`FluidDynamics.navier_stokes_iff_convective_navier_stokes`**, a theorem, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/NavierStokes.lean#L78). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The conservative and convective Navier-Stokes forms are equivalent when the fields are
> differentiable enough for the product rules.

```lean
theorem navier_stokes_iff_convective_navier_stokes
    (d : ℕ) (flow : CauchyFlow d)
    (pressure shearViscosity secondViscosity : ScalarField d)
    (hRhoTime : ∀ t x, DifferentiableAt ℝ (flow.rho · x) t)
    (hVelocityTime : ∀ t x, DifferentiableAt ℝ (flow.velocity · x) t)
    (hMomentumDensity : ∀ t,
      Differentiable ℝ (FluidFlow.momentumDensity d flow.toFluidFlow t))
    (hVelocitySpace : ∀ t, Differentiable ℝ (flow.velocity t)) :
    NavierStokes d flow pressure shearViscosity secondViscosity ↔
      ConvectiveNavierStokes d flow pressure shearViscosity secondViscosity
```

## Depends on

- [Cauchy momentum equations](momentum.md)
- [Newtonian stress law for Cauchy flows](newtonian.md)

## Sources

- [Physlib/FluidDynamics/CauchyFlow/NavierStokes.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/NavierStokes.lean)
