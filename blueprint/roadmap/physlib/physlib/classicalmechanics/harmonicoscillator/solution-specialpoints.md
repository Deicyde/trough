---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.trajectory_eq_cos, ClassicalMechanics.HarmonicOscillator.trajectory_velocity_eq_sin, ClassicalMechanics.HarmonicOscillator.trajectory_velocity_eq_zero_iff_sin_eq_zero, ClassicalMechanics.HarmonicOscillator.trajectory_velocity_eq_zero_iff_exists_int, ClassicalMechanics.HarmonicOscillator.trajectory_velocity_eq_zero_iff_norm_eq_amplitude, ClassicalMechanics.HarmonicOscillator.trajectory_eq_zero_iff_cos_eq_zero, ClassicalMechanics.HarmonicOscillator.trajectory_eq_zero_iff_exists_int
statement: formalized
proof: formalized
---

# Special conditions of the trajectory

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Solution.SpecialPoints`, [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean): 7 declarations, 7 with a docstring.

## i. Overview

> We demonstrate particular results about solution trajectories such as return times and points when
> the position or veliocity becomes zero

## ii. Key results

> - `TempDistElectromagneticPotential`: The type of electromagnetic potentials as distributions.
> - `trajectory_eq_cos` shows that on converting the initial conditions to amplitude-phase form
>   and `trajectory_velocity_eq_sin`: Similarly, the velocity is a shifted sine.
> - There are 2 results showing that the velocity vanishes when the sine has value zero.
>   `trajectory_velocity_eq_zero_iff_sin_eq_zero`: Velocity is 0 when the solution sine is zero.
>   `lemma trajectory_velocity_eq_zero_iff_exists_int`: Velocity is 0 when the phase is a multiple
>   of pi.
> - `trajectory_velocity_eq_zero_iff_norm_eq_amplitude`: The velocity vanishes when the trajectory
>   has norm equal to the amplitude, i.e. when it is at an extremum of position.
> - `trajectory_eq_zero_iff_cos_eq_zero`: The trajectory passes through zero when the
>   cosine factor in amplitude-phase form vanishes and `trajectory_eq_zero_iff_exists_int` shows that
>   the trajectory passes through zero when the phase is a half-odd-integer multiple of pi.

## iv. References

> References for the classical harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 58, section 21. [ref: landau\_mechanics]

## A. Normal form for standard initial conditions

> The amplitude-phase normal form was first proved for data already expressed as an
> `AmplitudePhase`. We now transport those identities back to ordinary `InitialConditions` using
> `AmplitudePhase.fromInitialConditions`.

**`ClassicalMechanics.HarmonicOscillator.trajectory_eq_cos`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean#L69).

> Every trajectory of the harmonic oscillator is a single shifted cosine after converting its
> initial conditions to amplitude-phase form.

```lean
lemma trajectory_eq_cos (IC : InitialConditions) (t : Time) :
    IC.trajectory S t =
      EuclideanSpace.single 0 ((AmplitudePhase.fromInitialConditions S IC).A *
        cos (S.ω * t - (AmplitudePhase.fromInitialConditions S IC).φ))
```

**`ClassicalMechanics.HarmonicOscillator.trajectory_velocity_eq_sin`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean#L79).

> The velocity of every trajectory is the corresponding shifted sine in amplitude-phase form.

```lean
lemma trajectory_velocity_eq_sin (IC : InitialConditions) (t : Time) :
    ∂ₜ (IC.trajectory S) t =
      EuclideanSpace.single 0 (-((AmplitudePhase.fromInitialConditions S IC).A * S.ω *
        sin (S.ω * t.val - (AmplitudePhase.fromInitialConditions S IC).φ)))
```

## B. Times at which the velocity is zero

> In amplitude-phase form the velocity is `v(t) = -Aω sin (ω t - φ)`. For nonzero amplitude this
> vanishes exactly when `sin (ω t - φ) = 0`, equivalently when `ω t - φ` is an
> integer multiple of `π`.

**`ClassicalMechanics.HarmonicOscillator.trajectory_velocity_eq_zero_iff_sin_eq_zero`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean#L100).

> For nonzero amplitude, the velocity vanishes exactly when the sine factor in
> amplitude-phase form vanishes.

```lean
lemma trajectory_velocity_eq_zero_iff_sin_eq_zero (IC : InitialConditions)
    (hA : (AmplitudePhase.fromInitialConditions S IC).A ≠ 0) (t : Time) :
    ∂ₜ (IC.trajectory S) t = 0 ↔
      sin (S.ω * t.val - (AmplitudePhase.fromInitialConditions S IC).φ) = 0
```

**`ClassicalMechanics.HarmonicOscillator.trajectory_velocity_eq_zero_iff_exists_int`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean#L108).

> For nonzero amplitude, the velocity is zero exactly at phase times `φ + nπ`.

```lean
lemma trajectory_velocity_eq_zero_iff_exists_int (IC : InitialConditions)
    (hA : (AmplitudePhase.fromInitialConditions S IC).A ≠ 0) (t : Time) :
    ∂ₜ (IC.trajectory S) t = 0 ↔
      ∃ n : ℤ,
        (t : ℝ) =
          ((AmplitudePhase.fromInitialConditions S IC).φ + n * π) / S.ω
```

## C. The position when the velocity is zero

> The zeros of the velocity are the turning points of the oscillator. In amplitude-phase form,
> these are the times when `sin (ω t - φ) = 0`; equivalently, `cos (ω t - φ)` is `1` or `-1`.
> At exactly those times the trajectory has maximal norm, equal to the amplitude `A`.
>
> The statement also covers the degenerate case `A = 0`: then the trajectory and its velocity are
> identically zero, so both sides of the equivalence hold at every time.

**`ClassicalMechanics.HarmonicOscillator.trajectory_velocity_eq_zero_iff_norm_eq_amplitude`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean#L141).

> The velocity vanishes exactly when the trajectory has norm equal to the amplitude.

```lean
lemma trajectory_velocity_eq_zero_iff_norm_eq_amplitude (IC : InitialConditions)
    (t : Time) :
    ∂ₜ (IC.trajectory S) t = 0 ↔
      ‖IC.trajectory S t‖ = (AmplitudePhase.fromInitialConditions S IC).A
```

## D. Times at which the trajectory passes through zero

> In amplitude-phase form the trajectory is `x(t) = A cos (ω t - φ).` For nonzero amplitude this
> vanishes exactly when `cos (ω t - φ) = 0`, equivalently when the phase is an odd multiple
> of `π / 2`.

**`ClassicalMechanics.HarmonicOscillator.trajectory_eq_zero_iff_cos_eq_zero`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean#L180).

> For nonzero amplitude, the trajectory passes through zero exactly when the cosine factor in
> amplitude-phase form vanishes.

```lean
lemma trajectory_eq_zero_iff_cos_eq_zero (IC : InitialConditions)
    (hA : (AmplitudePhase.fromInitialConditions S IC).A ≠ 0) (t : Time) :
    IC.trajectory S t = 0 ↔
      cos (S.ω * t.val - (AmplitudePhase.fromInitialConditions S IC).φ) = 0
```

**`ClassicalMechanics.HarmonicOscillator.trajectory_eq_zero_iff_exists_int`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean#L189).

> For nonzero amplitude, the trajectory passes through zero exactly at phase times
> `φ + (2n + 1)π / 2`.

```lean
lemma trajectory_eq_zero_iff_exists_int (IC : InitialConditions)
    (hA : (AmplitudePhase.fromInitialConditions S IC).A ≠ 0) (t : Time) :
    IC.trajectory S t = 0 ↔
      ∃ n : ℤ,
        (t : ℝ) =
          ((AmplitudePhase.fromInitialConditions S IC).φ + (2 * n + 1) * π / 2) / S.ω
```

## Depends on

- [Amplitude–phase parametrization](solution-amplitudephase.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/SpecialPoints.lean)
