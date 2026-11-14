---
declaration: module
origin: cited
lean: ClassicalMechanics.DampedHarmonicOscillator.InitialConditions, ClassicalMechanics.DampedHarmonicOscillator.underdampedBase, ClassicalMechanics.DampedHarmonicOscillator.criticallyDampedBase, ClassicalMechanics.DampedHarmonicOscillator.overdampedBase, ClassicalMechanics.DampedHarmonicOscillator.trajectory, ClassicalMechanics.DampedHarmonicOscillator.trajectory_eq_of_underdamped, ClassicalMechanics.DampedHarmonicOscillator.trajectory_eq_of_criticallyDamped, ClassicalMechanics.DampedHarmonicOscillator.trajectory_eq_of_overdamped
statement: formalized
proof: formalized
---

# Solutions to the damped harmonic oscillator

The module `Physlib.ClassicalMechanics.DampedHarmonicOscillator.Solution`, [Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean): 18 declarations, 18 with a docstring; 12 private, not shown.

## i. Overview

> In this module we define the solution to the damped harmonic oscillator for given initial
> conditions and prove that it satisfies the equation of motion. The solution selects the
> appropriate closed form from the sign of the discriminant: trigonometric for the underdamped
> case, polynomial for the critically damped case, and hyperbolic for the overdamped case.

## ii. Key results

> - `InitialConditions` is a structure for the initial position and velocity.
> - `trajectory` selects the appropriate regime-specific trajectory from the sign of the
>   discriminant; `trajectory_eq_of_underdamped_relaxationTime` rewrites the underdamped
>   solution with the relaxation time `τ`.
> - `trajectory_equationOfMotion_of_underdamped`,
>   `trajectory_equationOfMotion_of_criticallyDamped`, and
>   `trajectory_equationOfMotion_of_overdamped` prove the selected trajectory satisfies the
>   equation of motion in each damping regime.
> - `trajectory_equationOfMotion` proves that the selected trajectory satisfies the equation
>   of motion.
> - `equationOfMotion_unique` proves that two smooth solutions with the same initial data agree, and
>   `trajectories_unique` proves that the selected trajectory is the unique solution with the given
>   initial conditions.

## iv. References

> References for the damped harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 76, section 25. [ref: landau\_mechanics]
> * Goldstein, Classical Mechanics, Chapter 6, Section 6.5 (Forced Vibrations and the Effect of
>   Dissipative Forces). [ref: goldstein\_classicalmechanics]

## A. The initial conditions

> We define the type of initial conditions for the damped harmonic oscillator. The initial
> conditions are the position and velocity at time `0`.

**`ClassicalMechanics.DampedHarmonicOscillator.InitialConditions`**, a structure, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L82).

> The initial conditions for the damped harmonic oscillator, specified by an initial
> position and an initial velocity.

```lean
structure InitialConditions where
  /-- The initial position of the damped harmonic oscillator. -/
  x₀ : EuclideanSpace ℝ (Fin 1)
  /-- The initial velocity of the damped harmonic oscillator. -/
  v₀ : EuclideanSpace ℝ (Fin 1)
```

## B. Trajectories associated with the initial conditions

> For each damping regime, we give an explicit formula for the trajectory with the specified
> initial conditions.

### B.1. Regime-specific base trajectories

**`ClassicalMechanics.DampedHarmonicOscillator.underdampedBase`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L100).

> The oscillatory part of the underdamped trajectory before exponential decay.

```lean
noncomputable def underdampedBase
    (IC : InitialConditions) : Time → EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.DampedHarmonicOscillator.criticallyDampedBase`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L107).

> The polynomial part of the critically damped trajectory before exponential decay.

```lean
noncomputable def criticallyDampedBase
    (IC : InitialConditions) : Time → EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.DampedHarmonicOscillator.overdampedBase`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L112).

> The hyperbolic part of the overdamped trajectory before exponential decay.

```lean
noncomputable def overdampedBase
    (IC : InitialConditions) : Time → EuclideanSpace ℝ (Fin 1)
```

### B.2. The selected trajectory

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L126).

> Given initial conditions, the solution selected from the damping regime of the
> oscillator.

```lean
noncomputable def trajectory
    (IC : InitialConditions) : Time → EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_eq_of_underdamped`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L138).

> In the underdamped regime, the selected trajectory uses the trigonometric base.

```lean
lemma trajectory_eq_of_underdamped (IC : InitialConditions) (hS : S.IsUnderdamped) :
    S.trajectory IC =
      fun t : Time => exp (-S.decayRate * t) • S.underdampedBase IC t
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_eq_of_criticallyDamped`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L145).

> In the critically damped regime, the selected trajectory uses the polynomial base.

```lean
lemma trajectory_eq_of_criticallyDamped (IC : InitialConditions) (hS : S.IsCriticallyDamped) :
    S.trajectory IC =
      fun t : Time => exp (-S.decayRate * t) • S.criticallyDampedBase IC t
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_eq_of_overdamped`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L155).

> In the overdamped regime, the selected trajectory uses the hyperbolic base.

```lean
lemma trajectory_eq_of_overdamped (IC : InitialConditions) (hS : S.IsOverdamped) :
    S.trajectory IC =
      fun t : Time => exp (-S.decayRate * t) • S.overdampedBase IC t
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_eq_of_underdamped_relaxationTime`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L170).

> In the underdamped regime, the selected trajectory is `exp (-t / τ)` times the
> trigonometric base, `τ` being the relaxation time.

```lean
lemma trajectory_eq_of_underdamped_relaxationTime (IC : InitialConditions)
    (hS : S.IsUnderdamped) :
    S.trajectory IC =
      fun t : Time => exp (-(t : ℝ) / S.relaxationTime) • S.underdampedBase IC t
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_contDiff`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L179).

> The selected trajectory is smooth.

```lean
lemma trajectory_contDiff (IC : InitialConditions) :
    ContDiff ℝ ∞ (S.trajectory IC)
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_apply_zero`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L193).

> The selected trajectory has initial position `IC.x₀`.

```lean
lemma trajectory_apply_zero (IC : InitialConditions) : S.trajectory IC 0 = IC.x₀
```

### B.3. Shared calculus lemmas

> The three solution formulas all have the form `exp (-a * t) • y t`. The following private
> lemmas compute the first and second derivatives of that expression and package the common
> equation-of-motion argument.

### B.4. Derivatives of the base trajectories

> The remaining private lemmas compute the velocity and acceleration of the trigonometric,
> polynomial, and hyperbolic base trajectories before the exponential decay factor is applied.

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_velocity_at_zero`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L391).

> The selected trajectory has initial velocity `IC.v₀`.

```lean
lemma trajectory_velocity_at_zero (IC : InitialConditions) :
    ∂ₜ (S.trajectory IC) 0 = IC.v₀
```

## C. Trajectories and equation of motion

> The regime-specific trajectories satisfy the equation of motion for the damped harmonic
> oscillator.

### C.1. The selected trajectory satisfies the equation of motion

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_equationOfMotion_of_criticallyDamped`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L421).

> In the critically damped regime, the selected trajectory satisfies the damped equation
> of motion.

```lean
lemma trajectory_equationOfMotion_of_criticallyDamped (IC : InitialConditions)
    (hS : S.IsCriticallyDamped) :
    S.EquationOfMotion (S.trajectory IC)
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_equationOfMotion_of_underdamped`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L439).

> In the underdamped regime, the selected trajectory satisfies the damped equation of
> motion.

```lean
lemma trajectory_equationOfMotion_of_underdamped (IC : InitialConditions)
    (hS : S.IsUnderdamped) :
    S.EquationOfMotion (S.trajectory IC)
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_equationOfMotion_of_overdamped`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L458).

> In the overdamped regime, the selected trajectory satisfies the damped equation of
> motion.

```lean
lemma trajectory_equationOfMotion_of_overdamped (IC : InitialConditions)
    (hS : S.IsOverdamped) :
    S.EquationOfMotion (S.trajectory IC)
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectory_equationOfMotion`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L476).

> The selected trajectory satisfies the damped equation of motion.

```lean
lemma trajectory_equationOfMotion (IC : InitialConditions) :
    S.EquationOfMotion (S.trajectory IC)
```

### C.2. Uniqueness of the solutions

> Unlike the undamped oscillator, the mechanical energy is not conserved along a damped solution, so
> uniqueness cannot be read off from a conserved positive-definite energy. Instead we reduce the
> second-order equation of motion `m ẍ + γ ẋ + k x = 0` to the first-order linear system
> `(x, ẋ)' = (ẋ, (1/m)(-k x - γ ẋ))` on the phase space and invoke the global
> ODE-uniqueness theorem `ODE_solution_unique_univ` (the right-hand side is a continuous
> linear map, hence Lipschitz).

**`ClassicalMechanics.DampedHarmonicOscillator.equationOfMotion_unique`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L524).

> Any two smooth solutions of the damped equation of motion with the same initial position and
> velocity are equal.

```lean
lemma equationOfMotion_unique (x y : Time → EuclideanSpace ℝ (Fin 1))
    (hx : ContDiff ℝ ∞ x) (hy : ContDiff ℝ ∞ y)
    (hEOMx : S.EquationOfMotion x) (hEOMy : S.EquationOfMotion y)
    (h0 : x 0 = y 0) (hv0 : ∂ₜ x 0 = ∂ₜ y 0) :
    x = y
```

**`ClassicalMechanics.DampedHarmonicOscillator.trajectories_unique`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean#L548).

> The selected trajectory is the unique smooth solution of the damped equation of motion with the
> given initial conditions.

```lean
lemma trajectories_unique (IC : InitialConditions) (x : Time → EuclideanSpace ℝ (Fin 1))
    (hx : ContDiff ℝ ∞ x) (hEOM : S.EquationOfMotion x)
    (hx0 : x 0 = IC.x₀) (hv0 : ∂ₜ x 0 = IC.v₀) :
    x = S.trajectory IC
```

## Depends on

- [The damped harmonic oscillator](basic.md)

## Sources

- [Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Solution.lean)
