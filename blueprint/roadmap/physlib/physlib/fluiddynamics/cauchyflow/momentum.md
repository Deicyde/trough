---
declaration: module
origin: cited
lean: FluidDynamics.CauchyFlow.CauchyMomentumEquation, FluidDynamics.CauchyFlow.ConvectiveCauchyMomentumEquation, FluidDynamics.CauchyFlow.cauchyMomentumEquation_iff_convectiveCauchyMomentumEquation
statement: formalized
proof: formalized
---

# Cauchy momentum equations

The module `Physlib.FluidDynamics.CauchyFlow.Momentum`, [Physlib/FluidDynamics/CauchyFlow/Momentum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Momentum.lean): 3 declarations, 3 with a docstring.

## i. Overview

> This module defines the conservative and convective Cauchy momentum equations for a fluid flow
> with stress and specific body-force fields. The stress tensor is left as an input field, so this
> is the balance-law layer before specializing to a constitutive law, such as Euler or
> Navier-Stokes.

## ii. Key results

> - `CauchyFlow.CauchyMomentumEquation` : Conservation of momentum using `Space.matrixDiv`.
> - `CauchyFlow.ConvectiveCauchyMomentumEquation` : The Cauchy momentum equation in convective
>   form.
> - `CauchyFlow.cauchyMomentumEquation_iff_convectiveCauchyMomentumEquation` : Equivalence of the
>   two Cauchy momentum equations when continuity holds and the fields are differentiable.

## iv. References

> * None.

## A. Cauchy momentum equations

**`FluidDynamics.CauchyFlow.CauchyMomentumEquation`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Momentum.lean#L62).

> Conservation of momentum in conservative matrix-divergence form.
>
> The equation is
>
> `partial_t (rho u) + matrixDiv (rho u ⊗ u) = matrixDiv sigma + rho f`.
>
> Here `stress` is intentionally not yet specialized to a constitutive law.

```lean
def CauchyMomentumEquation (d : ℕ) (flow : CauchyFlow d) : Prop
```

**`FluidDynamics.CauchyFlow.ConvectiveCauchyMomentumEquation`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Momentum.lean#L76).

> Conservation of momentum in convective form.
>
> The equation is
>
> `rho (partial_t u + (u · ∇)u) = matrixDiv sigma + rho f`.
>
> Here `stress` is intentionally not yet specialized to a constitutive law.

```lean
def ConvectiveCauchyMomentumEquation (d : ℕ) (flow : CauchyFlow d) : Prop
```

## B. Equivalence of conservative and convective Cauchy momentum

**`FluidDynamics.CauchyFlow.cauchyMomentumEquation_iff_convectiveCauchyMomentumEquation`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Momentum.lean#L93).

> The conservative and convective Cauchy momentum equations are equivalent when the classical
> continuity equation holds.
>
> The differentiability assumptions are exactly the product-rule assumptions used to rewrite
> `partial_t (rho u)` and `matrixDiv (rho u ⊗ u)`.

```lean
lemma cauchyMomentumEquation_iff_convectiveCauchyMomentumEquation
    (d : ℕ) (flow : CauchyFlow d)
    (hContinuity : FluidFlow.ClassicalContinuityEquation d flow.toFluidFlow)
    (hRhoTime : ∀ t x, DifferentiableAt ℝ (flow.rho · x) t)
    (hVelocityTime : ∀ t x, DifferentiableAt ℝ (flow.velocity · x) t)
    (hMomentumDensity : ∀ t, Differentiable ℝ (FluidFlow.momentumDensity d flow.toFluidFlow t))
    (hVelocitySpace : ∀ t, Differentiable ℝ (flow.velocity t)) :
    CauchyMomentumEquation d flow ↔ ConvectiveCauchyMomentumEquation d flow
```

## Depends on

- [Basic API for Cauchy flows](basic.md)
- [Momentum fields for fluid flows](../fluidflow/momentum.md)

## Sources

- [Physlib/FluidDynamics/CauchyFlow/Momentum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Momentum.lean)
