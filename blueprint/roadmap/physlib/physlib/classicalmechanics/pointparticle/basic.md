---
declaration: module
origin: cited
lean: ClassicalMechanics.ReferenceFrame.Particle, ClassicalMechanics.ReferenceFrame.Particle.velocity, ClassicalMechanics.ReferenceFrame.Particle.acceleration, ClassicalMechanics.ReferenceFrame.Particle.pointInSpace
statement: formalized
proof: formalized
---

# Point particles

The module `Physlib.ClassicalMechanics.PointParticle.Basic`, [Physlib/ClassicalMechanics/PointParticle/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/Basic.lean): 6 declarations (2 instances with no name), 6 with a docstring.

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
>
> Position and its first time derivative are required to be differentiable when the
> frame is inertial. This ensures that the velocity and acceleration used in
> Newtonian systems are genuine derivatives. The trajectories in this definition
> are defined for all real-valued time coordinates relative to the frame's time origin.

**`ClassicalMechanics.ReferenceFrame.Particle`**, a structure, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L47).

> A point particle in `frame`.

```lean
structure Particle (frame : ReferenceFrame d) where
  /-- The particle's mass. -/
  mass : ℝ+
  /-- The particle's position in frame coordinates. -/
  pos : ℝ → frame.Vector
  pos_twice_differentiable :
    frame.IsInertial → Differentiable ℝ pos ∧ Differentiable ℝ (deriv pos)
```

**An instance with no name**, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L60).

> Position is differentiable in an inertial frame.

```lean
instance [h : Fact frame.IsInertial] : Fact (Differentiable ℝ particle.pos)
```

**`ClassicalMechanics.ReferenceFrame.Particle.velocity`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L64).

> The particle's velocity.

```lean
def velocity [_h : Fact (Differentiable ℝ particle.pos)] : ℝ → frame.Vector
```

**An instance with no name**, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L68).

> Velocity is differentiable in an inertial frame.

```lean
instance [h : Fact frame.IsInertial] : Fact (Differentiable ℝ particle.velocity)
```

**`ClassicalMechanics.ReferenceFrame.Particle.acceleration`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L72).

> The particle's acceleration.

```lean
def acceleration [Fact (Differentiable ℝ particle.pos)]
    [_h : Fact (Differentiable ℝ particle.velocity)] : ℝ → frame.Vector
```

**`ClassicalMechanics.ReferenceFrame.Particle.pointInSpace`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/Basic.lean#L77).

> The particle's position in affine space at frame time coordinate `t`.

```lean
def pointInSpace (t : ℝ) : Space d
```

## Depends on

- [Reference frames](../../spaceandtime/referenceframe.md)

## Sources

- [Physlib/ClassicalMechanics/PointParticle/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/Basic.lean)
