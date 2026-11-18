---
declaration: module
origin: cited
lean: FluidDynamics.FluidFlow.momentumDensity, FluidDynamics.FluidFlow.momentumFlux, FluidDynamics.FluidFlow.convectiveTerm, FluidDynamics.FluidFlow.materialAcceleration, FluidDynamics.FluidFlow.timeDeriv_smul_velocity, FluidDynamics.FluidFlow.timeDeriv_momentumDensity, FluidDynamics.FluidFlow.spaceDeriv_momentumFlux_component, FluidDynamics.FluidFlow.matrixDiv_momentumFlux
statement: formalized
proof: formalized
---

# Momentum fields for fluid flows

The module `Physlib.FluidDynamics.FluidFlow.Momentum`, [Physlib/FluidDynamics/FluidFlow/Momentum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean): 9 declarations, 9 with a docstring.

## i. Overview

> This module defines generic momentum fields for fluid flow and relates conservative momentum
> transport to mass density times material acceleration. The definitions do not choose a particular
> force law or stress model, so they can be reused by Navier-Stokes, Euler, and related systems.

## ii. Key results

> - `FluidFlow.momentumDensity` : The vector momentum density `rho u`.
> - `FluidFlow.momentumFlux` : The convective momentum flux `rho u ⊗ u`.
> - `FluidFlow.convectiveTerm` : The nonlinear transport term `(u · ∇)u`.
> - `FluidFlow.materialAcceleration` : The material acceleration `∂ₜ u + (u · ∇)u`.
> - `FluidFlow.momentumTransport_eq_materialAcceleration_add_continuityResidual` :
>   The momentum-transport identity relating conservative and convective quantities.

## iv. References

> * None.

## A. Momentum fields

**`FluidDynamics.FluidFlow.momentumDensity`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L55).

> The momentum density `rho u`.

```lean
def momentumDensity (d : ℕ) (fluid : FluidFlow d) : MomentumDensityField d
```

**`FluidDynamics.FluidFlow.momentumFlux`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L59).

> The convective momentum flux `rho u ⊗ u`.

```lean
def momentumFlux (d : ℕ) (fluid : FluidFlow d) : Time → Space d → Matrix (Fin d) (Fin d) ℝ
```

**`FluidDynamics.FluidFlow.convectiveTerm`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L65).

> The nonlinear transport term `(u · ∇)u`.

```lean
noncomputable def convectiveTerm (d : ℕ) (fluid : FluidFlow d) : VectorField d
```

**`FluidDynamics.FluidFlow.materialAcceleration`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L69).

> The material acceleration `∂ₜ u + (u · ∇)u`.

```lean
noncomputable def materialAcceleration (d : ℕ) (fluid : FluidFlow d) : VectorField d
```

## B. Momentum transport identity

**`FluidDynamics.FluidFlow.timeDeriv_smul_velocity`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L79).

> Product rule for the time derivative of a scalar field times a velocity field.

```lean
lemma timeDeriv_smul_velocity (d : ℕ) (rhoAtPosition : Time → ℝ)
    (velocityAtPosition : Time → EuclideanSpace ℝ (Fin d)) (t : Time)
    (hRho : DifferentiableAt ℝ rhoAtPosition t)
    (hVelocity : DifferentiableAt ℝ velocityAtPosition t) :
    ∂ₜ (fun t' => rhoAtPosition t' • velocityAtPosition t') t =
      rhoAtPosition t • ∂ₜ velocityAtPosition t + ∂ₜ rhoAtPosition t • velocityAtPosition t
```

**`FluidDynamics.FluidFlow.timeDeriv_momentumDensity`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L93).

> Product rule for the time derivative of the momentum density `rho u`.

```lean
lemma timeDeriv_momentumDensity (d : ℕ) (fluid : FluidFlow d)
    (t : Time) (x : Space d)
    (hRho : DifferentiableAt ℝ (fluid.rho · x) t)
    (hVelocity : DifferentiableAt ℝ (fluid.velocity · x) t) :
    ∂ₜ (momentumDensity d fluid · x) t =
      fluid.rho t x • ∂ₜ (fluid.velocity · x) t + ∂ₜ (fluid.rho · x) t • fluid.velocity t x
```

**`FluidDynamics.FluidFlow.spaceDeriv_momentumFlux_component`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L103).

> Product rule for one spatial derivative of one component of `rho u ⊗ u`.

```lean
lemma spaceDeriv_momentumFlux_component (d : ℕ) (fluid : FluidFlow d)
    (t : Time) (x : Space d) (i j : Fin d)
    (hMomentumDensity : Differentiable ℝ (momentumDensity d fluid t))
    (hVelocity : Differentiable ℝ (fluid.velocity t)) :
    ∂[j] (fun x' => momentumFlux d fluid t x' i j) x =
      fluid.velocity t x i • ∂[j] (fun x' => momentumDensity d fluid t x' j) x +
      ∂[j] (fun x' => fluid.velocity t x' i) x • momentumDensity d fluid t x j
```

**`FluidDynamics.FluidFlow.matrixDiv_momentumFlux`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L121).

> The matrix divergence of `rho u ⊗ u` split into continuity and convective parts.

```lean
lemma matrixDiv_momentumFlux (d : ℕ) (fluid : FluidFlow d)
    (t : Time) (x : Space d)
    (hMomentumDensity : Differentiable ℝ (momentumDensity d fluid t))
    (hVelocity : Differentiable ℝ (fluid.velocity t)) :
    matrixDiv d (momentumFlux d fluid t) x =
      (∇ ⬝ momentumDensity d fluid t) x • fluid.velocity t x +
        fluid.rho t x • convectiveTerm d fluid t x
```

**`FluidDynamics.FluidFlow.momentumTransport_eq_materialAcceleration_add_continuityResidual`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean#L161).

> The conservative momentum transport terms equal mass density times material acceleration plus
> the continuity residual times velocity.

```lean
lemma momentumTransport_eq_materialAcceleration_add_continuityResidual
    (d : ℕ) (fluid : FluidFlow d)
    (t : Time) (x : Space d)
    (hRhoTime : DifferentiableAt ℝ (fluid.rho · x) t)
    (hVelocityTime : DifferentiableAt ℝ (fluid.velocity · x) t)
    (hMomentumDensity : Differentiable ℝ (momentumDensity d fluid t))
    (hVelocitySpace : Differentiable ℝ (fluid.velocity t)) :
    ∂ₜ (momentumDensity d fluid · x) t + matrixDiv d (momentumFlux d fluid t) x =
      fluid.rho t x • materialAcceleration d fluid t x +
        continuityResidual d fluid t x • fluid.velocity t x
```

## Depends on

- [Continuity equation for fluid flows](continuity.md)
- [Matrix divergence on Space](../../spaceandtime/space/part-01/derivatives-matrixdiv.md)

## Sources

- [Physlib/FluidDynamics/FluidFlow/Momentum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/FluidFlow/Momentum.lean)
