---
declaration: module
origin: cited
lean: ClassicalMechanics.ReferenceFrame.pairGravityAcceleration, ClassicalMechanics.ReferenceFrame.gravityAcceleration, ClassicalMechanics.ReferenceFrame.pairGravity, ClassicalMechanics.ReferenceFrame.pairGravity_reverse, ClassicalMechanics.ReferenceFrame.GravityPairs, ClassicalMechanics.ReferenceFrame.gravityForces, ClassicalMechanics.ReferenceFrame.gravityForces_reverse, ClassicalMechanics.ReferenceFrame.netForce_gravity
statement: formalized
proof: formalized
---

# Pairwise Newtonian gravitation

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.NewtonianGravity`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean): 10 declarations, 10 with a docstring.

> Pair forces for a finite collection of point particles in a reference frame.

## i. Overview

> For a source of mass `m`, the gravitational acceleration of a target is proportional to
> `G * m` times the displacement towards the source divided by the cube of the separation.
> Here `G` is the gravitational constant in the frame's units. The force multiplies the
> acceleration by the target mass. Each ordered pair of distinct particle occurrences supplies
> one internal force, preserving multiplicities in the particle multiset.
>
> The formulas use the frame's physical norm. They model Newtonian gravity at collision-free
> times. At coincidence the Lean expression has value zero by totalized division.

## ii. Key results

> - `ReferenceFrame.gravityForces_reverse` proves Newton's third law for the force multiset.
> - `ReferenceFrame.netForce_gravity` expresses the net force as mass times acceleration.
> - `PointParticle.NewtonianSystem.ofGravity` bundles a solution of the acceleration equations
>   as a Newtonian system in an inertial frame.

## iv. References

> * [ref: goldstein\_classicalmechanics], Chapter 3, for the inverse-square gravitational force.

## A. Gravitational forces and acceleration

**`ClassicalMechanics.ReferenceFrame.pairGravityAcceleration`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L59).

> The contribution of the source to the target's gravitational acceleration.

```lean
def pairGravityAcceleration (source target : particles) (t : ℝ) : frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.gravityAcceleration`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L64).

> The target's gravitational acceleration from all other particle occurrences.

```lean
def gravityAcceleration (target : particles) (t : ℝ) : frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.pairGravity`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L69).

> The Newtonian force exerted by one particle on another in the given frame.

```lean
def pairGravity (source target : particles) (hne : source ≠ target) :
    frame.InternalForce particles
```

**`ClassicalMechanics.ReferenceFrame.pairGravity_reverse`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L77).

> Exchanging source and target gives the equal and opposite force.

```lean
lemma pairGravity_reverse (source target : particles) (hne : source ≠ target) :
    (pairGravity G particles source target hne).reverse =
      pairGravity G particles target source hne.symm
```

**`ClassicalMechanics.ReferenceFrame.GravityPairs`**, an abbrev, [line 96](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L96).

> All ordered pairs of distinct particle occurrences, grouped by target.

```lean
abbrev GravityPairs
```

**`ClassicalMechanics.ReferenceFrame.gravityForces`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L99).

> The internal gravitational forces, with each ordered pair occurring once.

```lean
def gravityForces : Multiset (frame.InternalForce particles)
```

**`ClassicalMechanics.ReferenceFrame.gravityForces_reverse`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L104).

> Newton's third law for the collection of pairwise gravitational forces.

```lean
lemma gravityForces_reverse :
    (gravityForces G particles).map InternalForce.reverse = gravityForces G particles
```

**`ClassicalMechanics.ReferenceFrame.netForce_gravity`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L120).

> The net internal force is the target mass times its gravitational acceleration.

```lean
lemma netForce_gravity (target : particles) (t : ℝ) :
    netForce target (gravityForces G particles) 0 t =
      target.1.mass • gravityAcceleration G particles target t
```

**`ClassicalMechanics.ReferenceFrame.acceleration_eq_gravity_iff`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L145).

> In an inertial frame, the gravitational acceleration equation is equivalent to Newton's
> second law for the constructed internal forces.

```lean
lemma acceleration_eq_gravity_iff [Fact frame.IsInertial]
    (target : particles) (t : ℝ) :
    target.1.acceleration t = gravityAcceleration G particles target t ↔
      netForce target (gravityForces G particles) 0 t =
        target.1.mass • target.1.acceleration t
```

## B. Newtonian systems under gravity

**`ClassicalMechanics.PointParticle.NewtonianSystem.ofGravity`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean#L170).

> Bundle particles that follow the gravitational equations of motion as a Newtonian system
> with no external forces. The inverse-square law describes the motion at collision-free times.

```lean
def ofGravity (G : ℝ) (particles : Multiset frame.Particle)
    (motion : ∀ (target : particles) (t : ℝ),
      target.1.acceleration t = gravityAcceleration G particles target t) :
    NewtonianSystem d
```

## Depends on

- [Newtonian point-particle systems](../../../../physlib/classicalmechanics/pointparticle/newtoniansystem-basic.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/NewtonianGravity.lean)
