---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.trajectory_energy
statement: formalized
proof: formalized
---

# The energy of the trajectories

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Solution.Energy`, [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Energy.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Energy.lean): 1 declaration, none with a docstring.

## i. Overview

> Show that the energy is a conserved quantity, i.e. a constant of motion.

## ii. Key results

> - `trajectory_energy`: The energy is conserved along any trajectory.

## iv. References

> References for the classical harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 58, section 21. [ref: landau\_mechanics]

## A. Conservation of energy

> For a given set of initial conditions, the energy of the trajectory is constant,
> due to the conservation of energy. Here we show it's value.

**`ClassicalMechanics.HarmonicOscillator.trajectory_energy`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Energy.lean#L50).

```lean
lemma trajectory_energy (IC : InitialConditions) : S.energy (IC.trajectory S) =
    fun _ => 1/2 * (S.m * ‖IC.v₀‖ ^2 + S.k * ‖IC.x₀‖ ^ 2)
```

## Depends on

- [Basic properties of trajectories](solution-basic.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Energy.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Energy.lean)
