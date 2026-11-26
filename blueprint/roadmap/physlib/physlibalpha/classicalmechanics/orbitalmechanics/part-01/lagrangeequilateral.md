---
declaration: module
origin: cited
lean: ClassicalMechanics.LagrangeOrbit.exists_lagrange_equilateral_solution
statement: formalized
proof: formalized
---

# Lagrange's circular equilateral solution

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.LagrangeEquilateral`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/LagrangeEquilateral.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/LagrangeEquilateral.lean): 1 declaration, 1 with a docstring; 22 private, not shown.

> Three positive masses form a rotating equilateral triangle in a Newtonian gravitational system.

## i. Overview

> A triangle of side length `ℓ` is translated to its mass barycentre. Rotating it with angular
> speed `√(G * M / ℓ ^ 3)`, where `M` is the total mass, preserves the separation of each pair.
> The gravitational acceleration of each particle is therefore the centripetal acceleration
> of its rotation. The rotating trajectories define particles in an arbitrary planar inertial
> reference frame, and `NewtonianSystem.ofGravity` supplies the system and both Newton laws.

## ii. Key results

> - `exists_lagrange_equilateral_solution` gives the three labelled particles, their equilateral
>   distances, uniform circular motion about the barycentre, and Kepler's third law.

## iv. References

> * [ref: chenciner\_fejoz\_2008], §8, for the reduction of the equilateral force sum.
> * R5 Lean formalization.
>   https://github.com/hkjtsgmc79-boop/lagrange-three-body-lean/releases/tag/v0.5.1

## A. The rotating configuration

## B. Particles in the inertial frame

## C. The Lagrange solution

**`ClassicalMechanics.LagrangeOrbit.exists_lagrange_equilateral_solution`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/LagrangeEquilateral.lean#L277).

> The Lagrange relative equilibrium for three positive masses in a planar inertial frame.
> The labelled particles move on a rigid equilateral triangle about their mass barycentre,
> with a positive common period obeying Kepler's third law.

```lean
public lemma exists_lagrange_equilateral_solution (frame : ReferenceFrame 2)
    (hframe : frame.IsInertial) (hG : 0 < G) (hℓ : 0 < ℓ) :
    ∃ (system : NewtonianSystem 2) (e : Fin 3 ≃ system.Particle) (T : ℝ),
      system.frame = frame ∧
      system.internalForces = gravityForces G system.particles ∧
      system.externalForces = 0 ∧
      (∀ i, (e i).mass = m i) ∧
      (∀ t, ∑ i, (m i).val • (e i).pos t = 0) ∧
      (∀ t i j, i ≠ j → ‖(e i).pos t - (e j).pos t‖ = ℓ) ∧
      (∀ i, Function.Periodic (e i).pos T) ∧
      (∃ plane : ℂ ≃ₗᵢ[ℝ] system.frame.Vector, ∀ t i,
        (e i).pos t = plane (rotation (Circle.exp (2 * Real.pi / T * t))
          (plane.symm ((e i).pos 0)))) ∧
      0 < T ∧ T ^ 2 * (G * ∑ i, (m i).val) = 4 * Real.pi ^ 2 * ℓ ^ 3
```

## Depends on

- [Pairwise Newtonian gravitation](newtoniangravity.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/LagrangeEquilateral.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/LagrangeEquilateral.lean)
