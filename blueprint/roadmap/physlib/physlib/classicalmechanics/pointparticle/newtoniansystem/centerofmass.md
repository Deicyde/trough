---
declaration: module
origin: cited
lean: ClassicalMechanics.PointParticle.NewtonianSystem.centerOfMass, ClassicalMechanics.PointParticle.NewtonianSystem.hasDerivAt_centerOfMass, ClassicalMechanics.PointParticle.NewtonianSystem.hasDerivAt_centerOfMass_of_noExternalForces, ClassicalMechanics.PointParticle.NewtonianSystem.centerOfMass_eq_of_noExternalForces
statement: formalized
proof: formalized
---

# Center of mass of a Newtonian system

The module `Physlib.ClassicalMechanics.PointParticle.NewtonianSystem.CenterOfMass`, [Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/CenterOfMass.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/CenterOfMass.lean): 4 declarations, 4 with a docstring.

> Motion of the mass-weighted average of the particle positions in an inertial frame.

## i. Overview

> The center of mass is the mass-weighted average of the particle positions. Its velocity is
> the total momentum divided by the total mass. When there are no external forces,
> `sum_mass_acceleration_eq_zero` from `NewtonianSystem.Basic` gives a zero derivative for
> the total momentum. The center of mass then moves with constant velocity, so its position
> at any time is determined by its position and the total momentum at a reference time.

## ii. Key results

> - `hasDerivAt_centerOfMass` expresses the center-of-mass velocity in terms of total momentum.
> - `centerOfMass_eq_of_noExternalForces` gives the center-of-mass position at any time from
>   its position and the total momentum at a reference time.

## iv. References

> * [ref: goldstein\_classicalmechanics], Chapter 1.

## A. Motion of the center of mass

**`ClassicalMechanics.PointParticle.NewtonianSystem.centerOfMass`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/CenterOfMass.lean#L53).

> The center of mass in the system's frame coordinates.

```lean
def centerOfMass (t : ℝ) : S.Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.hasDerivAt_centerOfMass`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/CenterOfMass.lean#L57).

> The center-of-mass velocity is the total momentum divided by the total mass.

```lean
lemma hasDerivAt_centerOfMass (t : ℝ) :
    HasDerivAt S.centerOfMass (S.mass⁻¹ • S.momentum t) t
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.hasDerivAt_centerOfMass_of_noExternalForces`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/CenterOfMass.lean#L66).

> In the absence of external forces, the center of mass moves with a constant velocity.

```lean
lemma hasDerivAt_centerOfMass_of_noExternalForces (hExt : S.externalForces = 0) (t₀ t : ℝ) :
    HasDerivAt S.centerOfMass (S.mass⁻¹ • S.momentum t₀) t
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.centerOfMass_eq_of_noExternalForces`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/CenterOfMass.lean#L79).

> The center of mass follows the straight line fixed by its initial position and momentum.

```lean
lemma centerOfMass_eq_of_noExternalForces (hExt : S.externalForces = 0) (t₀ t : ℝ) :
    S.centerOfMass t = S.centerOfMass t₀ + (t - t₀) • (S.mass⁻¹ • S.momentum t₀)
```

## Depends on

- [Newtonian point-particle systems](basic.md)

## Sources

- [Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/CenterOfMass.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/CenterOfMass.lean)
