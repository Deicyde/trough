---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.period, ClassicalMechanics.HarmonicOscillator.period_eq, ClassicalMechanics.HarmonicOscillator.period_pos, ClassicalMechanics.HarmonicOscillator.trajectory_periodic, ClassicalMechanics.HarmonicOscillator.return_time
statement: formalized
proof: formalized
---

# Periodicity and recurrence

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Solution.Periodicity`, [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean): 5 declarations, 3 with a docstring.

## i. Overview

> Every trajectory is a shifted cosine of angular frequency `ω`, so it repeats after a fixed period
> `T = 2π / ω`. We record the period, show the trajectory is periodic, and prove that — for
> non-trivial initial data — the trajectory returns to its initial position and velocity exactly at
> integer multiples of the period.

## ii. Key results

> - `period`: The oscillator period is the standard 2 pi / angular frequency.
> - `period_eq`: The notation "T" corresponds to the period defined above.
> - `period_pos`: The period is positive.
> - `trajectory_periodic`: The trajectory of the harmonic oscillator is periodic with
>   period of `2 * π / ω`.
> - `return_time`: The oscillator returns to its starting point on integer multiples of its period.

## iv. References

> References for the classical harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 58, section 21. [ref: landau\_mechanics]

## A. The period

> The period `T = 2π / ω` is the time for one complete oscillation; it is positive since `ω > 0`.

**`ClassicalMechanics.HarmonicOscillator.period`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean#L64).

> The period of a harmonic oscillator is `2 * π / ω`.

```lean
noncomputable def period (S : HarmonicOscillator) : ℝ
```

**`ClassicalMechanics.HarmonicOscillator.period_eq`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean#L69).

```lean
lemma period_eq : T S = 2 * π / S.ω
```

**`ClassicalMechanics.HarmonicOscillator.period_pos`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean#L71).

```lean
lemma period_pos : 0 < T S
```

## B. Periodicity of the trajectory

> The trajectory satisfies `x(t + T) = x(t)`: advancing time by one period shifts the phase `ω t`
> by `2π`, leaving `cos` and `sin` unchanged.

**`ClassicalMechanics.HarmonicOscillator.trajectory_periodic`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean#L85).

> The trajectory of the harmonic oscillator is periodic with period of `2 * π / ω`.

```lean
lemma trajectory_periodic (IC : InitialConditions) :
    Function.Periodic (IC.trajectory S) (T S)
```

## C. Return to the initial state

> For non-trivial initial data, the trajectory returns to its initial position and velocity only at
> integer multiples of the period.

**`ClassicalMechanics.HarmonicOscillator.return_time`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean#L107).

> Assuming that the initial coordinate and velocity are not simultaneously zero,
> the time stamps when the harmonic oscillator returns to its initial coordinate and velocity is
> a multiple of its period

```lean
lemma return_time (IC : InitialConditions) (non_trivial : IC.x₀ ≠ 0 ∨ IC.v₀ ≠ 0)
    (t : Time) (ht : IC.trajectory S t = IC.x₀ ∧ ∂ₜ (IC.trajectory S) t = IC.v₀) :
    ∃ n : ℤ,  (n : ℝ) * (T S) = t
```

## Depends on

- [Basic properties of trajectories](solution-basic.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/Periodicity.lean)
