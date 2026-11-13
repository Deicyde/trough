---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.AmplitudePhase, ClassicalMechanics.HarmonicOscillator.AmplitudePhase.toInitialConditions, ClassicalMechanics.HarmonicOscillator.AmplitudePhase.toInitialConditions_trajectory_eq_cos, ClassicalMechanics.HarmonicOscillator.AmplitudePhase.toInitialConditions_velocity_eq_sin, ClassicalMechanics.HarmonicOscillator.AmplitudePhase.fromInitialConditions, ClassicalMechanics.HarmonicOscillator.AmplitudePhase.toInitialConditions_fromInitialConditions
statement: formalized
proof: formalized
---

# Amplitude–phase parametrization

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Solution.AmplitudePhase`, [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean): 6 declarations, 6 with a docstring.

## i. Overview

> The state of the harmonic oscillator at `t = 0` is captured by `InitialConditions` as a position
> `x₀` and a velocity `v₀`. An equivalent and often more physical description writes the solution as
> a single shifted cosine of amplitude `A` and phase `φ`:
>   `x(t) = A cos (ω t - φ)`.
>
> Expanding with the angle-subtraction identity,
>   `A cos (ω t - φ) = (A cos φ) cos (ω t) + (A sin φ) sin (ω t)`,
> and matching coefficients against the standard solution
>   `x(t) = cos (ω t) x₀ + (sin (ω t) / ω) v₀`
> gives the change of coordinates
>   `x₀ = A cos φ`,   `v₀ = A ω sin φ`.
>
> We implement the forward map `(A, φ) ↦ (x₀, v₀)` as `toInitialConditions`, prove the resulting
> trajectory is the cosine normal form above (with velocity `-A ω sin (ω t - φ)`), and implement the
> inverse map `(x₀, v₀) ↦ (A, φ)` as `fromInitialConditions`, recovering `A` and `φ` as the polar
> coordinates of the phase vector `(x₀, v₀ / ω)`.

## ii. Key results

> - `toInitialConditions`: Amplitude–phase initial conditions converted to standard
>   initial conditions.
> - `toInitialConditions_trajectory_eq_cos`: The trajectory of amplitude–phase initial conditions is
>   the cosine normal form.
> - `toInitialConditions_velocity_eq_sin`: The trajectory of amplitude–phase initial conditions is
>   the sine normal form.
> - `fromInitialConditions`: Amplitude–phase initial conditions from standard initial conditions.
> - `toInitialConditions_fromInitialConditions`: Right inverse of `fromInitialConditions`.

## iv. References

> References for the classical harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 58, section 21. [ref: landau\_mechanics]

## A. The amplitude–phase initial conditions

> We define a type for initial conditions specified by an amplitude `A` and a phase angle `φ`. Being
> an amplitude and an angle, these are stored as scalars, rather than as vectors as for the other
> initial-condition types.

**`ClassicalMechanics.HarmonicOscillator.AmplitudePhase`**, a structure, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean#L79).

> Initial conditions for the harmonic oscillator specified by an amplitude `A` and a phase
> offset `φ`, describing the solution `x(t) = A cos (ω t - φ)`.
>
> The conditions can be converted to the standard `InitialConditions` format using the
> `toInitialConditions` function.

```lean
@[ext] structure AmplitudePhase where
  /-- The amplitude of the oscillation. -/
  A : ℝ
  /-- The phase offset of the oscillation. -/
  φ : ℝ
```

## B. Conversion to standard initial conditions

> Using `x₀ = A cos φ` and `v₀ = A ω sin φ`, we convert amplitude–phase data to the standard initial
> position and velocity at `t = 0`.

**`ClassicalMechanics.HarmonicOscillator.AmplitudePhase.toInitialConditions`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean#L101).

> Convert amplitude–phase initial conditions to standard initial conditions at `t = 0`, via
> `x₀ = A cos φ` and `v₀ = A ω sin φ`.
>
> See `toInitialConditions_trajectory_eq_cos` and `toInitialConditions_velocity_eq_sin` in
> section E.3 for the correctness proofs.

```lean
noncomputable def toInitialConditions (S : HarmonicOscillator) (IC : AmplitudePhase) :
    InitialConditions
```

## C. The trajectory in normal form

> The trajectory built from amplitude–phase data is exactly the single cosine
> `x(t) = A cos (ω t - φ)`, with velocity `v(t) = -A ω sin (ω t - φ)`. In the position identity the
> factor `1 / ω` of the standard solution cancels the `ω` in `v₀ = A ω sin φ`, which uses `ω ≠ 0`.

**`ClassicalMechanics.HarmonicOscillator.AmplitudePhase.toInitialConditions_trajectory_eq_cos`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean#L118).

> The trajectory of amplitude–phase initial conditions is the cosine normal form
> `x(t) = A cos (ω t - φ)`.

```lean
lemma toInitialConditions_trajectory_eq_cos (S : HarmonicOscillator) (IC : AmplitudePhase)
    (t : Time) :
    (IC.toInitialConditions S).trajectory S t
      = EuclideanSpace.single 0 (IC.A * cos (S.ω * t - IC.φ))
```

**`ClassicalMechanics.HarmonicOscillator.AmplitudePhase.toInitialConditions_velocity_eq_sin`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean#L129).

> The velocity of the amplitude–phase trajectory is `v(t) = -A ω sin (ω t - φ)`.

```lean
lemma toInitialConditions_velocity_eq_sin (S : HarmonicOscillator) (IC : AmplitudePhase)
    (t : Time) :
    ∂ₜ ((IC.toInitialConditions S).trajectory S) t
      = EuclideanSpace.single 0 (-(IC.A * S.ω * sin (S.ω * t.val - IC.φ)))
```

## D. Recovering the amplitude and phase

> The inverse map `(x₀, v₀) ↦ (A, φ)` must solve `x₀ = A cos φ` and `v₀ / ω = A sin φ`. Recovering
> the angle with the real `arctan` covers only `(-π/2, π/2)` and forces a case split at `x₀ = 0`; we
> instead embed the phase vector as the complex number `z = x₀ + (v₀ / ω) i` and read off `A = ‖z‖`
> and `φ = Complex.arg z`, with `arg` in the canonical range `(-π, π]`. The degenerate state
> `x₀ = v₀ = 0` is covered by the convention `arg 0 = 0`, so no case split is needed.
>
> We prove that converting initial conditions to amplitude–phase form and back returns the original
> initial conditions.

**`ClassicalMechanics.HarmonicOscillator.AmplitudePhase.fromInitialConditions`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean#L159).

> Recover amplitude–phase data from standard initial conditions, as the polar coordinates of the
> phase vector `(x₀, v₀ / ω)` embedded as `z = x₀ + (v₀ / ω) i`: the amplitude is `‖z‖` and the
> phase is `Complex.arg z`.
>
> See `toInitialConditions_fromInitialConditions` for the right-inverse identity.

```lean
noncomputable def fromInitialConditions (S : HarmonicOscillator) (IC : InitialConditions) :
    AmplitudePhase
```

**`ClassicalMechanics.HarmonicOscillator.AmplitudePhase.toInitialConditions_fromInitialConditions`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean#L166).

> `fromInitialConditions` is a right inverse of `toInitialConditions`: converting initial
> conditions to amplitude–phase form and back recovers them exactly.

```lean
lemma toInitialConditions_fromInitialConditions (S : HarmonicOscillator)
    (IC : InitialConditions) :
    (fromInitialConditions S IC).toInitialConditions S = IC
```

## Depends on

- [Basic properties of trajectories](solution-basic.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Solution/AmplitudePhase.lean)
