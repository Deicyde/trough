---
declaration: module
origin: cited
lean: ClassicalMechanics.FreeParticle.linearMomentum_conserved, ClassicalMechanics.FreeParticle.kineticEnergy_conserved, ClassicalMechanics.FreeParticle, ClassicalMechanics.FreeParticle.Trajectory, ClassicalMechanics.FreeParticle.velocity, ClassicalMechanics.FreeParticle.linearMomentum, ClassicalMechanics.FreeParticle.kineticEnergy, ClassicalMechanics.FreeParticle.NewtonsSecondLaw
statement: formalized
proof: formalized
---

# The Free Particle

The module `Physlib.ClassicalMechanics.FreeParticle.Basic`, [Physlib/ClassicalMechanics/FreeParticle/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean): 11 declarations, 11 with a docstring, 2 listed as significant.

## i. Overview

> The free particle is one of the simplest systems in classical mechanics: a particle of mass `m`
> moving with no external forces acting on it. Physically, this means the particle just keeps moving
> at constant velocity.
>
> In this file, we work in a simple 1D coordinate system where position and velocity are functions
> of time with values in `ℝ`. This keeps things easy to reason about. A more complete treatment would
> use manifolds and tangent bundles.

## ii. Key results

> The main things we show about the free particle are:
>
> In the `Basic` module:
> - `FreeParticle` stores the mass of the particle.
> - `NewtonsSecondLaw` encodes the equation `m * q'' = 0`.
> - `accel_zero` shows that this implies `q'' = 0`.
> - `velocity_const_of_zero_acc` shows that zero acceleration means velocity is constant.
> - `linearMomentum_conserved` shows that linear momentum stays constant over time.
> - `kineticEnergy_conserved` shows that kinetic energy stays constant over time.
>
> So overall, we formalise the usual chain:
> Newton’s law → zero acceleration → constant velocity → constant momentum and energy.

## iv. References

> * None.

**`ClassicalMechanics.FreeParticle`**, a structure, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L75).

> A classical free particle with positive mass.
>
> A free particle is a mechanical system evolving in the absence of
> external forces. The dynamics are therefore entirely determined by
> Newton's second law with zero force.
>
> The only parameter of the system is the particle mass. The assumption
> that the mass is strictly positive is physically natural and is used
> throughout the development when simplifying the equation of motion.

```lean
structure FreeParticle where
  /--
  The mass of the free particle.

  This parameter determines the inertial response of the particle in
  Newton's second law.
  -/
  mass : ℝ
  mass_pos : 0 < mass
```

**`ClassicalMechanics.FreeParticle.Trajectory`**, an abbrev, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L91).

> A trajectory is a time-dependent position function describing the motion
> of the particle in one spatial dimension. Defining the trajectory.

```lean
abbrev Trajectory
```

**`ClassicalMechanics.FreeParticle.velocity`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L100).

> The velocity of a trajectory at a given time.
> This is defined as the time derivative of the position function.

```lean
def velocity (s : FreeParticle) (q : Trajectory) (t : Time) : ℝ
```

**`ClassicalMechanics.FreeParticle.linearMomentum`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L110).

> The linear momentum of the free particle along a trajectory.
>
> This is given by the classical one-dimensional expression `p = m v`,
> where `m` is the particle mass and `v` is the velocity.

```lean
def linearMomentum (s : FreeParticle) (q : Trajectory) (t : Time) : ℝ
```

**`ClassicalMechanics.FreeParticle.kineticEnergy`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L120).

> The kinetic energy of the free particle along a trajectory.
>
> This is given by the classical expression `E = (1 / 2) m v²`,
> where `m` is the particle mass and `v` is the velocity.

```lean
def kineticEnergy (s : FreeParticle) (q : Trajectory) (t : Time) : ℝ
```

**`ClassicalMechanics.FreeParticle.NewtonsSecondLaw`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L130).

> Newton's second law for the free particle.
>
> Since no external forces act on the particle, Newton's second law
> reduces to the equation `m q'' = 0`, expressing that the acceleration
> vanishes identically.

```lean
def NewtonsSecondLaw (s : FreeParticle) (q : Trajectory) (t : Time) : Prop
```

**`ClassicalMechanics.FreeParticle.accel_zero`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L141).

> Newton's second law for a free particle implies that the acceleration
> vanishes identically.
>
> Since the particle mass is strictly positive, the equation
> `m q'' = 0` can be simplified to `q'' = 0` by cancelling the mass
> factor.

```lean
lemma accel_zero (s : FreeParticle) (q : Trajectory) (h : ∀ t, s.NewtonsSecondLaw q t) :
    ∀ t, deriv (deriv q) t = 0
```

**`ClassicalMechanics.FreeParticle.velocity_const_of_zero_acc`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L157).

> If the acceleration of a trajectory vanishes everywhere, then the
> velocity is constant.
>
> More precisely, if the second derivative of the trajectory is zero
> for all times, then there exists a constant `v₀` such that the
> velocity is equal to `v₀` at every time.
>
> The second-order differentiability assumption is included to apply
> standard results from real analysis relating vanishing derivatives to
> constant functions.

```lean
lemma velocity_const_of_zero_acc (q : Time → ℝ) (h : ∀ t, deriv (deriv q) t = 0)
    (hcont : ContDiff ℝ 2 q) : ∃ v₀, ∀ t, deriv q t = v₀
```

**`ClassicalMechanics.FreeParticle.linearMomentum_conserved_of_velocity_const`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L171).

> If a free-particle trajectory has constant velocity, then its linear momentum is constant.

```lean
lemma linearMomentum_conserved_of_velocity_const (s : FreeParticle) (q : Trajectory)
    (h : ∃ v₀, ∀ t, s.velocity q t = v₀) :
    ∃ p, ∀ t, s.linearMomentum q t = p
```

**`ClassicalMechanics.FreeParticle.linearMomentum_conserved`**, a theorem, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L183). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A free particle satisfying the equation of motion conserves linear momentum.
>
> Newton's second law implies that the acceleration vanishes, so the velocity is constant.
> Since the particle mass is fixed, the linear momentum is constant in time.

```lean
theorem linearMomentum_conserved (s : FreeParticle) (q : Trajectory)
    (h : ∀ t, s.NewtonsSecondLaw q t) (hcont : ContDiff ℝ 2 q) :
    ∃ p, ∀ t, s.linearMomentum q t = p
```

**`ClassicalMechanics.FreeParticle.kineticEnergy_conserved`**, a theorem, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean#L198). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A free particle satisfying the equation of motion conserves kinetic energy.
>
> The proof follows the standard argument from classical mechanics:
> Newton's second law implies that the acceleration vanishes, which in
> turn implies that the velocity is constant. Since the kinetic energy
> depends only on the square of the velocity, it follows that the kinetic
> energy is constant in time.

```lean
theorem kineticEnergy_conserved (s : FreeParticle) (q : Trajectory)
    (h : ∀ t, s.NewtonsSecondLaw q t) (hcont : ContDiff ℝ 2 q) :
    ∃ E, ∀ t, s.kineticEnergy q t = E
```

## Depends on

- [Time Derivatives](../../spaceandtime/time/derivatives.md)

## Sources

- [Physlib/ClassicalMechanics/FreeParticle/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/FreeParticle/Basic.lean)
