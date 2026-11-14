---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory, ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_eq, ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_zero, ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_contDiff, ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_velocity, ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_acceleration, ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_position_at_zero, ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_velocity_at_zero
statement: formalized
proof: formalized
---

# Basic properties of trajectories

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Solution.Basic`, [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean): 9 declarations, 3 with a docstring.

## i. Overview

> To each initial condition we association a trajectory. We will prove some basic properties
> of these trajectories.
>
> …

## ii. Key results

> - `trajectory`: The trajectory has the expected sinusoidal form.
> - `trajectory_eq`: Definitonal equality for the trajectory.
> - `trajectory_zero`: For zero initial conditions, the trajectory is zero.
> - `trajectory_contDiff`: The time derivative of the trajectory exists and is smooth.
> - `trajectory_velocity`: The velocity has the expected sinusoidal form.
> - `trajectory_acceleration`: The acceleration has the expected sinusoidal form.
> - `trajectory_position_at_zero`: The trajectory has the correct position at the point the initial
>   conditions are specified.
> - `lemma trajectory_velocity_at_zero`: The trajectory has the correct velocity at the point the
>   initial conditions are specified.
> - `trajectory_equationOfMotion`: The trajectories satisfy the equation of motion.

## iv. References

> References for the classical harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 58, section 21. [ref: landau\_mechanics]

## A. The trajectory associated with the initial conditions

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L71).

> Given initial conditions, the solution to the classical harmonic oscillator.

```lean
noncomputable def trajectory (IC : InitialConditions) : Time → EuclideanSpace ℝ (Fin 1)
```

### A.1. Definitional equality for the trajectory

> We show a basic definitional equality for the trajectory.

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_eq`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L81).

```lean
lemma trajectory_eq (IC : InitialConditions) :
    IC.trajectory S = fun t : Time => cos (S.ω * t) • IC.x₀ + (sin (S.ω * t)/S.ω) • IC.v₀
```

## B. The trajectory for zero initial conditions

> The trajectory for zero initial conditions is the zero function.

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_zero`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L94).

> For zero initial conditions, the trajectory is zero.

```lean
lemma trajectory_zero : trajectory S 0 = fun _ => 0
```

## C. Smoothness of the trajectories

> The trajectories for any initial conditions are smooth functions of time.

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_contDiff`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L106).

```lean
lemma trajectory_contDiff (S : HarmonicOscillator) (IC : InitialConditions) {n : WithTop ℕ∞} :
    ContDiff ℝ n (IC.trajectory S)
```

## D. Velocity of the trajectories

> We give a simplification of the velocity of the trajectory.

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_velocity`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L120).

```lean
lemma trajectory_velocity (IC : InitialConditions) : ∂ₜ (IC.trajectory S) =
    fun t : Time => - S.ω • sin (S.ω * t.val) • IC.x₀ + cos (S.ω * t.val) • IC.v₀
```

## E. Acceleration of the trajectories

> We give a simplification of the acceleration of the trajectory.

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_acceleration`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L149).

```lean
lemma trajectory_acceleration (IC : InitialConditions) : ∂ₜ (∂ₜ (IC.trajectory S)) =
    fun t : Time => - S.ω^2 • cos (S.ω * t.val) • IC.x₀ - S.ω • sin (S.ω * t.val) • IC.v₀
```

## F. The initial conditions of the trajectories

> We show that, unsurprisingly, the trajectories have the initial conditions
> used to define them.

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_position_at_zero`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L176).

> For a set of initial conditions `IC` the position of the solution at time `0` is
> `IC.x₀`.

```lean
lemma trajectory_position_at_zero (IC : InitialConditions) : IC.trajectory S 0 = IC.x₀
```

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_velocity_at_zero`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L180).

```lean
lemma trajectory_velocity_at_zero (IC : InitialConditions) : ∂ₜ (IC.trajectory S) 0 = IC.v₀
```

## G. Trajectories and Equation of motion

> The trajectories satisfy the equation of motion for the harmonic oscillator.

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectory_equationOfMotion`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean#L191).

```lean
lemma trajectory_equationOfMotion (IC : InitialConditions) :
    EquationOfMotion S (IC.trajectory S)
```

## Depends on

- [The initial conditions](solution-initialdata.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Basic.lean)
