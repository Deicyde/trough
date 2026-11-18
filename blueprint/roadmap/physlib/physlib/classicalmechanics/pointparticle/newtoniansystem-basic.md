---
declaration: module
origin: cited
lean: ClassicalMechanics.PointParticle.NewtonianSystem, ClassicalMechanics.PointParticle.NewtonianSystem.Vector, ClassicalMechanics.PointParticle.NewtonianSystem.Particle, ClassicalMechanics.PointParticle.NewtonianSystem.Particle.mass, ClassicalMechanics.PointParticle.NewtonianSystem.Particle.pos, ClassicalMechanics.PointParticle.NewtonianSystem.Particle.velocity, ClassicalMechanics.PointParticle.NewtonianSystem.Particle.acceleration, ClassicalMechanics.PointParticle.NewtonianSystem.Particle.momentum
statement: formalized
proof: formalized
---

# Newtonian point-particle systems

The module `Physlib.ClassicalMechanics.PointParticle.NewtonianSystem.Basic`, [Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean): 30 declarations (4 instances with no name), 27 with a docstring.

> This module defines `NewtonianSystem`, consisting of an inertial reference frame, a finite
> collection of point particles, and the internal and external forces acting on
> them. Particles carry masses and positions over time; forces carry vector values
> over time and identify the particles they act on.
>
> Newton's second law requires the net force on each particle to equal its mass
> times its acceleration. Newton's third law requires the multiset of internal
> forces to be invariant under equal-and-opposite reversal.
>
> Particles and forces are stored in multisets. For example, if two identical springs
> connect the same pair of particles, the net force on either particle must count
> both spring forces, even though they are equal.
>
> Many classical systems are specified by constraints rather than explicit position
> and force functions. Such models can be formalized as conditions on `NewtonianSystem`
> values: which particles and forces are present, geometric constraints such as
> fixed distances, and restrictions on the forces such as centrality.
>
> Results can be proved for arbitrary systems satisfying these conditions. An
> existence proof establishes that a satisfying system exists for given parameters
> and initial conditions; choice can then be used to select one. Explicit formulas
> for the positions and forces are not required to state the conditions or to
> reason about systems satisfying them.

## A. Systems

**`ClassicalMechanics.PointParticle.NewtonianSystem`**, a structure, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L53).

> A finite system of point particles satisfying Newton's laws.

```lean
structure NewtonianSystem (d : ℕ) where
  /-- The system's reference frame. -/
  frame : ReferenceFrame d
  [isInertial : Fact frame.IsInertial]
  /-- The particles in the system. -/
  particles : Multiset frame.Particle
  /-- Forces between particles in the system. -/
  internalForces : Multiset (frame.InternalForce particles)
  /-- Forces on the system from external sources. -/
  externalForces : Multiset (frame.Force particles)
  /-- Newton's second law: the net force on each particle equals its mass times its acceleration. -/
  newton_second_law : ∀ particle : particles,
    netForce particle internalForces externalForces = particle.1.mass • particle.1.acceleration
  /-- Newton's third law: internal forces and their reverses occur with equal multiplicities. -/
  newton_third_law : internalForces.map .reverse = internalForces
```

**An instance with no name**, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L73).

```lean
instance : Fact system.frame.IsInertial
```

## B. System particles

**`ClassicalMechanics.PointParticle.NewtonianSystem.Vector`**, an abbrev, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L81).

> Vectors in the system's frame.

```lean
abbrev Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Particle`**, an abbrev, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L84).

> A particle in `system`.

```lean
abbrev Particle : Type
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Particle.mass`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L91).

> The particle's mass.

```lean
def mass : ℝ+
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Particle.pos`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L94).

> The particle's position at `t`.

```lean
def pos : system.Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Particle.velocity`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L97).

> The particle's velocity at `t`.

```lean
def velocity : system.Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Particle.acceleration`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L100).

> The particle's acceleration at `t`.

```lean
def acceleration : system.Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Particle.momentum`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L103).

> The particle's momentum at `t`.

```lean
def momentum : system.Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Particle.kineticEnergy`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L106).

> The particle's kinetic energy at `t`.

```lean
def kineticEnergy : ℝ
```

## C. System forces

**`ClassicalMechanics.PointParticle.NewtonianSystem.Force`**, an abbrev, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L115).

> A force in `system`.

```lean
abbrev Force : Type
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Force.inner`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L123).

> The underlying force.

```lean
def inner : system.frame.Force system.Particle
```

**An instance with no name**, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L126).

```lean
instance : Coe system.Force (system.frame.Force system.Particle)
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Force.value`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L129).

> The force at `t`.

```lean
def value (t : ℝ) : system.Vector
```

**An instance with no name**, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L131).

```lean
instance : CoeFun system.Force (fun _ => ℝ → system.Vector)
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Force.target`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L135).

> The force's target.

```lean
def target : system.Particle
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Force.Internal`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L138).

> Whether `force` is internal.

```lean
def Internal : Prop
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.Force.External`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L141).

> Whether `force` is external.

```lean
def External : Prop
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.InternalForce`**, an abbrev, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L146).

> An internal force in `system`.

```lean
abbrev InternalForce : Type
```

**An instance with no name**, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L153).

> View an internal force as a system force.

```lean
instance : Coe system.InternalForce system.Force
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.InternalForce.value`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L156).

> The force at `t`.

```lean
def value (t : ℝ) : system.Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.InternalForce.target`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L159).

> The force's target.

```lean
def target : system.Particle
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.InternalForce.source`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L162).

> The force's source.

```lean
def source : system.Particle
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.InternalForce.reverse_count_eq`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L165).

> A force and its reverse have the same multiplicity.

```lean
lemma reverse_count_eq :
    system.internalForces.count force.1.reverse = system.internalForces.count force.1
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.InternalForce.reverse`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L174).

> The reverse force.

```lean
def reverse : system.InternalForce
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.InternalForce.Central`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L178).

> Whether the force lies along the line joining its source and target.

```lean
def Central : Prop
```

## D. Aggregate quantities

**`ClassicalMechanics.PointParticle.NewtonianSystem.mass`**, a def, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L190).

> Total mass.

```lean
def mass : ℝ
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.momentum`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L194).

> Total momentum at `t`.

```lean
def momentum : system.Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.netExternalForce`**, a def, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L198).

> Net external force at `t`.

```lean
def netExternalForce : system.Vector
```

**`ClassicalMechanics.PointParticle.NewtonianSystem.kineticEnergy`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean#L202).

> Total kinetic energy at `t`.

```lean
def kineticEnergy : ℝ
```

## Depends on

- [Forces](../force.md)
- [Point particles](basic.md)

## Sources

- [Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/PointParticle/NewtonianSystem/Basic.lean)
