---
declaration: module
origin: cited
lean: ClassicalMechanics.ReferenceFrame.Particle, ClassicalMechanics.ReferenceFrame.Particle.velocity, ClassicalMechanics.ReferenceFrame.Particle.acceleration, ClassicalMechanics.ReferenceFrame.Particle.pointInSpace
statement: formalized
proof: formalized
---

# Point particles

The module `Physlib.ClassicalMechanics.PointParticle.Basic`, [Physlib/ClassicalMechanics/PointParticle/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/Basic.lean): 4 declarations, 4 with a docstring.

> This module defines point particles together with their motion relative to a
> reference frame. A `Particle` has a constant positive mass and a position over
> time. Velocity and acceleration are derived from that position rather than stored
> as independent data.
>
> The trajectory is part of the particle's description, but need not be given by an
> explicit solution formula. Particle values can be considered subject to conditions
> on their positions and on the forces acting on them. A particular mechanical model
> can therefore be specified by constraints on particles, with the existence of
> particles satisfying those constraints established separately.
>
> A particle by itself carries no equation of motion or assumption about which
> forces act on it. It is a constituent from which systems can be assembled, rather
> than a specification of an isolated or unconstrained one-particle system. Newton's
> laws are imposed when particles and forces are assembled in
> `ClassicalMechanics.PointParticle.NewtonianSystem`.

**`ClassicalMechanics.ReferenceFrame.Particle`**, a structure, [line 43](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L43).

> A point particle in `frame`.

```lean
structure Particle (frame : ReferenceFrame d) where
  /-- The particle's mass. -/
  mass : ℝ+
  /-- The particle's position in frame coordinates. -/
  pos : ℝ → frame.Vector
  pos_twice_differentiable : Differentiable ℝ pos ∧ Differentiable ℝ (deriv pos)
```

**`ClassicalMechanics.ReferenceFrame.Particle.velocity`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L55).

> The particle's velocity.

```lean
def velocity : ℝ → frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Particle.acceleration`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L59).

> The particle's acceleration.

```lean
def acceleration  : ℝ → frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Particle.pointInSpace`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L63).

> The particle's position in affine space at frame time coordinate `t`.

```lean
def pointInSpace (t : ℝ) : Space d
```

## Depends on

- [Reference frames](../../spaceandtime/referenceframe.md)

## Sources

- [Physlib/ClassicalMechanics/PointParticle/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PointParticle/Basic.lean)
