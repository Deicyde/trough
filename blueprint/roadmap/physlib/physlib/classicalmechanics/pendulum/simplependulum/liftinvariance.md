---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.potentialEnergy_add_int_mul_two_pi, ClassicalMechanics.SimplePendulum.torque_add_int_mul_two_pi, ClassicalMechanics.SimplePendulum.kineticEnergy_add_const, ClassicalMechanics.SimplePendulum.energy_add_int_mul_two_pi, ClassicalMechanics.SimplePendulum.equationOfMotion_add_int_mul_two_pi, ClassicalMechanics.SimplePendulum.isSolution_add_int_mul_two_pi, ClassicalMechanics.SimplePendulum.ofAngle_add_int_mul_two_pi_coord
statement: formalized
proof: formalized
---

# Independence of the lift for the simple pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.LiftInvariance`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean): 7 declarations, 7 with a docstring.

## i. Overview

> The dynamics of the simple gravity pendulum in `SimplePendulum.Basic` is written on a lift of the
> motion: the real angle `θ t 0` stands for the configuration `ConfigurationSpace.ofAngle (θ t 0)`,
> and two lifts differing by a whole number of turns carry the same configurations. For the lifted
> formulation to describe the pendulum faithfully, nothing dynamical may depend on the choice of
> the lift. This module proves that the dynamical quantities — the potential and kinetic energies,
> the torque, the energy, and the equation of motion together with its solutions — are invariant
> under the deck transformations `θ ↦ θ + 2π n` of the angular lift, and closes by making the
> starting point precise: the shifted lift describes the same configuration, by the periodicity of
> the angular lift of the geometric configuration space. The packaging of this invariance at the
> level of configuration-space trajectories comes with the geometric bridge in a later module.

## ii. Key results

> - `SimplePendulum.potentialEnergy_add_int_mul_two_pi` and
>   `SimplePendulum.torque_add_int_mul_two_pi`: the potential energy and the torque are unchanged
>   by shifting the angle by a whole number of turns.
> - `SimplePendulum.kineticEnergy_add_const` and `SimplePendulum.energy_add_int_mul_two_pi`: the
>   kinetic energy is unchanged by any constant shift of the lift, and the energy by a shift by a
>   whole number of turns.
> - `SimplePendulum.equationOfMotion_add_int_mul_two_pi` and
>   `SimplePendulum.isSolution_add_int_mul_two_pi`: the equation of motion and its solutions are
>   invariant under shifting the lift by a whole number of turns.
> - `SimplePendulum.ofAngle_add_int_mul_two_pi_coord`: the shifted lift describes the same
>   configuration.

## iv. References

> References for the simple gravity pendulum include:
>
> * Landau & Lifshitz, Mechanics, 3rd ed., §5 and §21. [ref: landau\_mechanics]
> * Arnold, Mathematical Methods of Classical Mechanics, 2nd ed., §4. [ref: arnold\_mechanics]

## A. Independence of the lift

> The dynamics of `SimplePendulum.Basic` are written on a lift of the motion: the real angle
> `θ t 0` stands for the configuration `ConfigurationSpace.ofAngle (θ t 0)`, and two lifts
> differing by a whole number of turns carry the same configurations. This section proves that the
> dynamical quantities listed below — the energies, the torque, and the equation of motion and its
> solutions — are invariant under the deck transformations `θ ↦ θ + 2π n` of the angular lift;
> the packaging of this invariance at the level of configuration-space trajectories comes with
> the geometric bridge in a later module. The section closes by making the starting point
> precise: the shifted lift does describe the same configuration, by the periodicity of the
> angular lift of the geometric configuration space.

### A.1. Invariance of the potential energy and the torque

> The potential energy and the torque depend on the angle only through its cosine and its sine,
> and both have period `2π`: neither quantity changes when the angle is shifted by a whole number
> of turns.

**`ClassicalMechanics.SimplePendulum.potentialEnergy_add_int_mul_two_pi`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean#L95).

> The potential energy of the simple pendulum is invariant under shifting the angle by a
> whole number of turns.

```lean
lemma potentialEnergy_add_int_mul_two_pi (x : EuclideanSpace ℝ (Fin 1)) (n : ℤ) :
    S.potentialEnergy (x + (n * (2 * Real.pi)) • EuclideanSpace.single 0 1) =
      S.potentialEnergy x
```

**`ClassicalMechanics.SimplePendulum.torque_add_int_mul_two_pi`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean#L105).

> The torque of the simple pendulum is invariant under shifting the angle by a whole number
> of turns.

```lean
lemma torque_add_int_mul_two_pi (x : EuclideanSpace ℝ (Fin 1)) (n : ℤ) :
    S.torque (x + (n * (2 * Real.pi)) • EuclideanSpace.single 0 1) = S.torque x
```

### A.2. Invariance of the energy

> The shift of the lift is constant in time, so it drops out of the velocity, and the kinetic
> energy is unchanged by any constant shift at all; the potential energy is unchanged by the
> invariance of A.1. Together the two give the invariance of the energy under shifting the lift
> by a whole number of turns.

**`ClassicalMechanics.SimplePendulum.kineticEnergy_add_const`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean#L125).

> The kinetic energy of the simple pendulum along a lift of the angle is invariant under
> shifting the lift by any constant: the shift drops out of the velocity.

```lean
lemma kineticEnergy_add_const (θ : Time → EuclideanSpace ℝ (Fin 1))
    (c : EuclideanSpace ℝ (Fin 1)) :
    S.kineticEnergy (fun t => θ t + c) = S.kineticEnergy θ
```

**`ClassicalMechanics.SimplePendulum.energy_add_int_mul_two_pi`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean#L137).

> The energy of the simple pendulum along a lift of the angle is invariant under shifting the
> lift by a whole number of turns: A.1 supplies the invariance of the potential energy, and the
> velocity is unchanged by a constant shift.

```lean
lemma energy_add_int_mul_two_pi (θ : Time → EuclideanSpace ℝ (Fin 1)) (n : ℤ) :
    S.energy (fun t => θ t + (n * (2 * Real.pi)) • EuclideanSpace.single 0 1) =
      S.energy θ
```

### A.3. Invariance of the equation of motion and its solutions

> Both sides of the equation of motion are invariant under the shift: the angular momentum,
> because the shift is constant in time, and the torque, by the invariance of A.1. Smoothness is
> likewise unaffected by adding a constant, so being a solution is invariant as well.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_add_int_mul_two_pi`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean#L155).

> A lift of the angle shifted by a whole number of turns satisfies the equation of motion of
> the simple pendulum if and only if the lift itself does.

```lean
lemma equationOfMotion_add_int_mul_two_pi (θ : Time → EuclideanSpace ℝ (Fin 1)) (n : ℤ) :
    S.EquationOfMotion (fun t => θ t + (n * (2 * Real.pi)) • EuclideanSpace.single 0 1) ↔
      S.EquationOfMotion θ
```

**`ClassicalMechanics.SimplePendulum.isSolution_add_int_mul_two_pi`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean#L165).

> A lift of the angle shifted by a whole number of turns is a solution of the simple pendulum
> if and only if the lift itself is.

```lean
lemma isSolution_add_int_mul_two_pi (θ : Time → EuclideanSpace ℝ (Fin 1)) (n : ℤ) :
    S.IsSolution (fun t => θ t + (n * (2 * Real.pi)) • EuclideanSpace.single 0 1) ↔
      S.IsSolution θ
```

### A.4. The shifted lift describes the same configuration

> Finally the statement giving the previous invariances their meaning: the lift and its shift by
> a whole number of turns project to the same point of the configuration space, by the
> periodicity of the angular lift `ConfigurationSpace.ofAngle` with period `2π`.

**`ClassicalMechanics.SimplePendulum.ofAngle_add_int_mul_two_pi_coord`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean#L189).

> A lift of the angle and its shift by a whole number of turns describe the same
> configuration of the simple pendulum.

```lean
lemma ofAngle_add_int_mul_two_pi_coord (x : EuclideanSpace ℝ (Fin 1)) (n : ℤ) :
    ConfigurationSpace.ofAngle
        ((x + (n * (2 * Real.pi)) • EuclideanSpace.single (0 : Fin 1) (1 : ℝ)) 0) =
      ConfigurationSpace.ofAngle (x 0)
```

## Depends on

- [The simple gravity pendulum](basic.md)
- [Configuration space of the simple pendulum](geometric-basic.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/LiftInvariance.lean)
