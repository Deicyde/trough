---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.InitialConditionsAtTime.toInitialConditions_trajectory_at_t₀, ClassicalMechanics.HarmonicOscillator.InitialConditionsAtTime.toInitialConditions_velocity_at_t₀, ClassicalMechanics.HarmonicOscillator.InitialConditionsAtTime.toInitialConditions_energy_at_t₀, ClassicalMechanics.HarmonicOscillator.InitialConditionsFromTwoPositions.toInitialConditions_trajectory_at_t₁, ClassicalMechanics.HarmonicOscillator.InitialConditionsFromTwoPositions.toInitialConditions_trajectory_at_t₂, ClassicalMechanics.HarmonicOscillator.InitialConditionsFromTwoVelocities.toInitialConditions_velocity_at_t₁, ClassicalMechanics.HarmonicOscillator.InitialConditionsFromTwoVelocities.toInitialConditions_velocity_at_t₂
statement: formalized
proof: formalized
---

# Consistency of the initial conditions

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Solution.Consistency`, [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean): 7 declarations, 7 with a docstring.

## i. Overview

> Demonstrate that the different choices of initial conditions are self-consistent

## ii. Key results

> - `InitialConditionsAtTime.toInitialConditions_trajectory_at_t₀`: The initial conditions specified
>   at a point in time create trajectories that pass through the correct point.
>   `InitialConditionsAtTime.toInitialConditions_velocity_at_t₀`: The initial conditions specified
>   at a point in time create trajectories that pass through the initial point with the correct
>   velocity.
>   `InitialConditionsAtTime.toInitialConditions_energy_at_t₀`: The initial conditions specified
>   at a point in time create trajectories that pass through the initial point with the correct
>   energy.
> - `InitialConditionsFromTwoPositions.toInitialConditions_trajectory_at_t₁`: Check that when the
>   initial conditions are specified with two (time, position) pairs that the resulting
>   trajectory has the correct position at the first of the two specified points.
>   `InitialConditionsFromTwoPositions.toInitialConditions_trajectory_at_t₂`: As above for the
>   second specified point.
> - `InitialConditionsFromTwoVelocities.toInitialConditions_velocity_at_t₁`: Check that when the
>   initial conditions are specified with two (time, velocity) pairs that the resulting
>   trajectory has the correct velocity at the first of the two specified points.
>   `InitialConditionsFromTwoVelocities.toInitialConditions_velocity_at_t₂`: As above for the
>   second specified point.

## iv. References

> References for the classical harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 58, section 21. [ref: landau\_mechanics]

## A. Correctness of Initial Conditions

> We now prove the correctness lemmas for the `InitialConditionsAtTime.toInitialConditions`
> conversion function. These show that the conversion produces a trajectory that passes through
> the specified position and velocity at the specified time.

### A.1. Correctness of InitialConditionsAtTime conversion

**`ClassicalMechanics.HarmonicOscillator.InitialConditionsAtTime.toInitialConditions_trajectory_at_t₀`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean#L88).

> The trajectory resulting from `toInitialConditions` passes through the specified
> position `xT₀` at time `t₀`.

```lean
lemma toInitialConditions_trajectory_at_t₀ (S : HarmonicOscillator)
    (IC : InitialConditionsAtTime) :
    (IC.toInitialConditions S).trajectory S IC.t₀ = IC.xT₀
```

**`ClassicalMechanics.HarmonicOscillator.InitialConditionsAtTime.toInitialConditions_velocity_at_t₀`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean#L100).

> The trajectory resulting from `toInitialConditions` has the specified
> velocity `vT₀` at time `t₀`.

```lean
lemma toInitialConditions_velocity_at_t₀ (S : HarmonicOscillator)
    (IC : InitialConditionsAtTime) :
    ∂ₜ ((IC.toInitialConditions S).trajectory S) IC.t₀ = IC.vT₀
```

**`ClassicalMechanics.HarmonicOscillator.InitialConditionsAtTime.toInitialConditions_energy_at_t₀`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean#L112).

> The energy of the trajectory at time `t₀` equals the energy computed from the
> initial conditions at `t₀`.

```lean
lemma toInitialConditions_energy_at_t₀ (S : HarmonicOscillator)
    (IC : InitialConditionsAtTime) :
    S.energy ((IC.toInitialConditions S).trajectory S) IC.t₀ =
    1/2 * (S.m * ‖IC.vT₀‖^2 + S.k * ‖IC.xT₀‖^2)
```

### A.2. Correctness of InitialConditionsFromTwoPositions conversion

> The conversion recovers the initial conditions only when `sin (S.ω * (t₂ - t₁)) ≠ 0`. This
> condition fails exactly when `ω·(t₂ - t₁) = n·π` for some integer `n`, i.e. when `t₂ - t₁` is an
> integer multiple of half a period; in that case `x(t₂) = (-1)^n · x(t₁)` for every trajectory,
> independent of `v₀`, so the two positions do not determine the initial conditions.
>
> Under this nondegeneracy condition, we prove that the resulting trajectory passes through `xT₁`
> at `t₁` and `xT₂` at `t₂`.

**`ClassicalMechanics.HarmonicOscillator.InitialConditionsFromTwoPositions.toInitialConditions_trajectory_at_t₁`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean#L141).

> The trajectory from `toInitialConditions` passes through `xT₁` at time `t₁`,
> provided `sin (S.ω * (t₂ - t₁)) ≠ 0`.

```lean
lemma toInitialConditions_trajectory_at_t₁ (S : HarmonicOscillator)
    (IC : InitialConditionsFromTwoPositions)
    (hΔ : sin (S.ω * (IC.t₂ - IC.t₁)) ≠ 0) :
    (IC.toInitialConditions S).trajectory S IC.t₁ = IC.xT₁
```

**`ClassicalMechanics.HarmonicOscillator.InitialConditionsFromTwoPositions.toInitialConditions_trajectory_at_t₂`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean#L153).

> The trajectory from `toInitialConditions` passes through `xT₂` at time `t₂`,
> provided `sin (S.ω * (t₂ - t₁)) ≠ 0`.

```lean
lemma toInitialConditions_trajectory_at_t₂ (S : HarmonicOscillator)
    (IC : InitialConditionsFromTwoPositions)
    (hΔ : sin (S.ω * (IC.t₂ - IC.t₁)) ≠ 0) :
    (IC.toInitialConditions S).trajectory S IC.t₂ = IC.xT₂
```

### A.3. Correctness of InitialConditionsFromTwoVelocities conversion

> The conversion recovers the initial conditions only when `sin (S.ω * (t₂ - t₁)) ≠ 0`. Under this
> nondegeneracy condition, we prove that the resulting trajectory has velocity `vT₁` at `t₁` and
> `vT₂` at `t₂`.

**`ClassicalMechanics.HarmonicOscillator.InitialConditionsFromTwoVelocities.toInitialConditions_velocity_at_t₁`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean#L179).

> The trajectory from `toInitialConditions` has velocity `vT₁` at time `t₁`,
> provided `sin (S.ω * (t₂ - t₁)) ≠ 0`.

```lean
lemma toInitialConditions_velocity_at_t₁ (S : HarmonicOscillator)
    (IC : InitialConditionsFromTwoVelocities)
    (hΔ : sin (S.ω * (IC.t₂ - IC.t₁)) ≠ 0) :
    ∂ₜ ((IC.toInitialConditions S).trajectory S) IC.t₁ = IC.vT₁
```

**`ClassicalMechanics.HarmonicOscillator.InitialConditionsFromTwoVelocities.toInitialConditions_velocity_at_t₂`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean#L192).

> The trajectory from `toInitialConditions` has velocity `vT₂` at time `t₂`,
> provided `sin (S.ω * (t₂ - t₁)) ≠ 0`.

```lean
lemma toInitialConditions_velocity_at_t₂ (S : HarmonicOscillator)
    (IC : InitialConditionsFromTwoVelocities)
    (hΔ : sin (S.ω * (IC.t₂ - IC.t₁)) ≠ 0) :
    ∂ₜ ((IC.toInitialConditions S).trajectory S) IC.t₂ = IC.vT₂
```

## Depends on

- [Basic properties of trajectories](solution-basic.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Consistency.lean)
