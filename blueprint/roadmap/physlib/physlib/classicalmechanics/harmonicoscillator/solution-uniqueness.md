---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectories_unique
statement: formalized
proof: formalized
---

# Uniqueness

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Solution.Uniqueness`, [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Uniqueness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Uniqueness.lean): 1 declaration, 1 with a docstring.

## i. Overview

> We show that the trajectories are the unique solutions to the equation of motion
> for the given initial conditions.

## ii. Key results

> - `trajectories_unique`: The soluition trajectory is unique given a set of initial conditions.

## iv. References

> * Landau and Lifshitz, Mechanics, Section 32. [ref: landau\_mechanics]

## A. Uniqueness

> We show that the trajectories are the unique solutions to the equation of motion
> for the given initial conditions.

**`ClassicalMechanics.HarmonicOscillator.InitialConditions.trajectories_unique`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Uniqueness.lean#L56).

> The trajectories to the equation of motion for a given set of initial conditions
> are unique.
>
> Given any smooth `x` satisfying the equation of motion with the same initial
> position and velocity, the difference `y = x - IC.trajectory S` also solves the
> equation of motion with zero initial conditions; energy conservation then forces
> its energy, and hence `y`, to vanish identically, so `x = IC.trajectory S`.

```lean
lemma trajectories_unique (IC : InitialConditions) (x : Time → EuclideanSpace ℝ (Fin 1))
    (hx : ContDiff ℝ ∞ x) :
    S.EquationOfMotion x ∧ x 0 = IC.x₀ ∧ ∂ₜ x 0 = IC.v₀ →
    x = IC.trajectory S
```

## Depends on

- [Basic properties of trajectories](solution-basic.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Uniqueness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Uniqueness.lean)
