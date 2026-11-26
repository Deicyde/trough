---
declaration: module
origin: cited
lean: ClassicalMechanics.PointParticle.NewtonianSystem.centerOfMass_eq_of_two_particles, ClassicalMechanics.PointParticle.NewtonianSystem.positions_eq_centerOfMass_relativePosition, ClassicalMechanics.PointParticle.NewtonianSystem.hasDerivAt_deriv_relativePosition_of_gravity, ClassicalMechanics.PointParticle.NewtonianSystem.binarySpecificAngularMomentum, ClassicalMechanics.PointParticle.NewtonianSystem.binarySignedSweptArea, ClassicalMechanics.PointParticle.NewtonianSystem.binarySpecificAngularMomentum_eq_of_gravity, ClassicalMechanics.PointParticle.NewtonianSystem.binarySignedSweptArea_eq_of_gravity, ClassicalMechanics.PointParticle.NewtonianSystem.binarySignedSweptArea_eq_of_eq_duration
statement: formalized
proof: formalized
---

# The Newtonian two-body reduction

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.BinaryStar`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean): 8 declarations, 8 with a docstring; 2 private, not shown.

> The center of mass and relative displacement of two stars in an inertial frame.

## i. Overview

> An equivalence with `Fin 2` labels the two particle occurrences. Their center of mass moves
> uniformly in the absence of external forces. Together with the relative displacement, the center
> of mass determines both positions. If their internal forces are the pairwise Newtonian
> forces, the relative displacement from star zero to star one satisfies the Kepler equation at
> each time of positive separation. The gravitational parameter is `G` times the sum of the masses.
> For positive `G` the relative acceleration points towards zero displacement.
> In two dimensions the signed specific angular momentum remains constant on collision-free
> intervals. The relative position then sweeps out equal signed areas in equal times.

## ii. Key results

> - `centerOfMass_eq_of_two_particles` gives the mass-weighted position of the binary.
> - `positions_eq_centerOfMass_relativePosition` recovers both positions from the center of mass
>   and the displacement from the first particle to the second.
> - `hasDerivAt_deriv_relativePosition_of_gravity` gives the relative acceleration.
> - `binarySignedSweptArea_eq_of_eq_duration` gives Kepler's second law for a planar binary.

## iv. References

> * [ref: goldstein\_classicalmechanics], Chapter 3.

## A. The center of mass of a binary

**`ClassicalMechanics.PointParticle.NewtonianSystem.centerOfMass_eq_of_two_particles`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean#L65).

> The center of mass of two labelled particles, in the system's frame coordinates.

```lean
lemma centerOfMass_eq_of_two_particles (t : ℝ) :
    system.centerOfMass t = ((e 0).mass.val + (e 1).mass.val)⁻¹ •
      ((e 0).mass.val • (e 0).pos t + (e 1).mass.val • (e 1).pos t)
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.positions_eq_centerOfMass_relativePosition`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean#L74).

> The two positions are recovered from their center of mass and relative displacement.
> Each offset from the center of mass is weighted by the other particle's mass.

```lean
lemma positions_eq_centerOfMass_relativePosition (t : ℝ) :
    let r := (e 1).pos t - (e 0).pos t
    let M := (e 0).mass.val + (e 1).mass.val
    (e 0).pos t = system.centerOfMass t - ((e 1).mass.val / M) • r ∧
      (e 1).pos t = system.centerOfMass t + ((e 0).mass.val / M) • r
```

## B. Relative motion under gravity

**`ClassicalMechanics.PointParticle.NewtonianSystem.hasDerivAt_deriv_relativePosition_of_gravity`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean#L110).

> At a collision-free time the relative displacement of two mutually gravitating particles
> satisfies the Kepler equation with gravitational parameter `G` times their total mass.

```lean
lemma hasDerivAt_deriv_relativePosition_of_gravity
    (hi : system.internalForces = gravityForces G system.particles)
    (he : system.externalForces = 0) {t : ℝ} (hne : (e 1).pos t ≠ (e 0).pos t) :
    let r := fun s => (e 1).pos s - (e 0).pos s
    HasDerivAt (deriv r)
      (-(G * ((e 0).mass.val + (e 1).mass.val) / ‖r t‖ ^ 3) • r t) t
```

## C. Kepler's second law

**`ClassicalMechanics.PointParticle.NewtonianSystem.binarySpecificAngularMomentum`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean#L151).

> The signed angular momentum per unit reduced mass of the relative motion.

```lean
def binarySpecificAngularMomentum (t : ℝ) : ℝ
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.binarySignedSweptArea`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean#L159).

> The signed area swept by the relative displacement over the oriented time interval.

```lean
def binarySignedSweptArea (u v : ℝ) : ℝ
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.binarySpecificAngularMomentum_eq_of_gravity`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean#L194).

> The signed specific angular momentum is constant on a collision-free interval.

```lean
lemma binarySpecificAngularMomentum_eq_of_gravity {a b t : ℝ}
    (hsep : ∀ s ∈ Icc a b, (e 1).pos s ≠ (e 0).pos s) (ht : t ∈ Icc a b) :
    system.binarySpecificAngularMomentum e t = system.binarySpecificAngularMomentum e a
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.binarySignedSweptArea_eq_of_gravity`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean#L206).

> On a collision-free interval, the area swept per unit time is half the signed specific
> angular momentum.

```lean
lemma binarySignedSweptArea_eq_of_gravity {a b u v : ℝ}
    (hsep : ∀ t ∈ Icc a b, (e 1).pos t ≠ (e 0).pos t) (hu : u ∈ Icc a b) (hv : v ∈ Icc a b) :
    system.binarySignedSweptArea e u v =
      (v - u) * (system.binarySpecificAngularMomentum e a / 2)
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.binarySignedSweptArea_eq_of_eq_duration`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean#L222).

> Kepler's second law for a binary. Equal time intervals of the same collision-free motion
> sweep out equal signed areas.

```lean
lemma binarySignedSweptArea_eq_of_eq_duration {a b u v u' v' : ℝ}
    (hsep : ∀ t ∈ Icc a b, (e 1).pos t ≠ (e 0).pos t)
    (hu : u ∈ Icc a b) (hv : v ∈ Icc a b) (hu' : u' ∈ Icc a b) (hv' : v' ∈ Icc a b)
    (hduration : v - u = v' - u') :
    system.binarySignedSweptArea e u v = system.binarySignedSweptArea e u' v'
```

## Depends on

- [Center of mass of a Newtonian system](../../../../physlib/classicalmechanics/pointparticle/newtoniansystem/centerofmass.md)
- [Pairwise Newtonian gravitation](newtoniangravity.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/BinaryStar.lean)
