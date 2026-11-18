---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.toHarmonicOscillator, ClassicalMechanics.SimplePendulum.toHarmonicOscillator_m, ClassicalMechanics.SimplePendulum.toHarmonicOscillator_k, ClassicalMechanics.SimplePendulum.toHarmonicOscillator_ω, ClassicalMechanics.SimplePendulum.LinearizedEquationOfMotion, ClassicalMechanics.SimplePendulum.linearizedEquationOfMotion_iff_newton, ClassicalMechanics.SimplePendulum.linearizedEquationOfMotion_iff, ClassicalMechanics.SimplePendulum.fderiv_torque_zero_apply
statement: formalized
proof: formalized
---

# Small-angle motion of the simple gravity pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.SmallAngle`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean): 29 declarations, 29 with a docstring.

## i. Overview

> Near the bottom of its swing the torque of the simple gravity pendulum is
> `-m g ℓ sin θ ≈ -m g ℓ θ`, so for small angles the equation of motion `I θ̈ = -m g ℓ sin θ`
> linearizes to `I θ̈ = -m g ℓ θ`: the equation of a harmonic oscillator whose mass is the moment
> of inertia `I = m ℓ²` of the pendulum and whose spring constant is the coefficient `m g ℓ` of
> the linearized torque. The angular frequency `√(k/m)` of this oscillator is `√(g/ℓ)`, which is
> exactly the constant `ω` of `SimplePendulum.Basic`, there described as the frequency of the
> small oscillations.
>
> This module packages the oscillator of the small oscillations as
> `SimplePendulum.toHarmonicOscillator`, defines the linearized equation of motion
> `θ̈ + ω² θ = 0` on the same Euclidean lift of the angle as the nonlinear equation, and proves
> that for smooth lifts of the angle it is the equation of motion of the associated harmonic
> oscillator, so that the solution theory of the harmonic oscillator applies verbatim to the
> small oscillations of the pendulum.
>
> The equivalence carries the whole solution theory of the oscillator over to the small
> oscillations. Every choice of initial angle and initial angular velocity determines a smooth
> small-angle motion, unique among the smooth solutions of the linearized equation of motion,
> with the closed form `cos (ω t) x₀ + (sin (ω t)/ω) v₀`. Every small-angle motion is periodic
> with the small-angle period `2π √(ℓ/g)`, in which neither the mass of the bob nor the amplitude
> of the swing appears: within the linearization the pendulum is isochronous. The small-angle
> motion released from rest at a given angle, the cosine `θ₀ cos (ω t)`, and its properties are
> recorded in the companion module `SimplePendulum/ReleasedFromRest.lean`. The linearization is
> not exact, and the final section measures what it discards: the torque differs from its
> linearization `-m g ℓ θ` by exactly `m g ℓ (θ - sin θ)`, of norm at most `m g ℓ ‖θ‖³/6`, so every
> small-angle motion solves the equation of motion of the pendulum itself up to a residual
> cubically small in the angle.

## ii. Key results

> - `SimplePendulum.toHarmonicOscillator` is the harmonic oscillator to which the pendulum
>   linearizes, of mass `I = m ℓ²` and spring constant `m g ℓ`. The simp lemmas
>   `toHarmonicOscillator_m` and `toHarmonicOscillator_k` record its data, and
>   `toHarmonicOscillator_ω` identifies its angular frequency with the constant
>   `SimplePendulum.ω` of the pendulum.
> - `SimplePendulum.LinearizedEquationOfMotion` is the small-angle equation of motion
>   `θ̈ + ω² θ = 0`. Its rotational Newton form is `linearizedEquationOfMotion_iff_newton`, and
>   `linearizedEquationOfMotion_iff` identifies it, for smooth lifts of the angle, with the
>   equation of motion of the associated harmonic oscillator. The linearization is literally
>   differentiation: `fderiv_torque_zero_apply` identifies the derivative of the torque at the
>   hanging equilibrium with the force of the oscillator, and
>   `linearizedEquationOfMotion_iff_fderiv_torque` restates the linearized equation as the
>   equation of motion with the torque replaced by that derivative.
> - `SimplePendulum.smallAngleTrajectory` is the small-angle motion determined by a choice of
>   initial conditions, the trajectory of the associated harmonic oscillator: it has the closed
>   form `cos (ω t) x₀ + (sin (ω t)/ω) v₀` (`smallAngleTrajectory_eq`), it is smooth
>   (`smallAngleTrajectory_contDiff`), it assumes its initial data at time `0`
>   (`smallAngleTrajectory_at_zero`, `smallAngleTrajectory_velocity_at_zero`), and it satisfies
>   the linearized equation of motion (`smallAngleTrajectory_linearizedEquationOfMotion`).
> - `SimplePendulum.linearized_unique`: a smooth solution of the linearized equation of motion
>   with the initial data of `IC` is `smallAngleTrajectory IC`. Together with the previous point,
>   this is the existence and uniqueness of the small-angle motions.
> - `SimplePendulum.smallAnglePeriod` is the period of the small oscillations, the period of the
>   associated harmonic oscillator: `2π/ω` (`smallAnglePeriod_eq_two_pi_div_ω`), with closed
>   form `2π √(ℓ/g)` (`smallAnglePeriod_eq`). Every small-angle trajectory is periodic with this
>   period (`smallAngleTrajectory_periodic`), and along each the energy of the associated
>   oscillator is the constant fixed by the initial data (`smallAngleTrajectory_energy`).
> - `SimplePendulum.torque_sub_toHarmonicOscillator_force` computes the exact difference between
>   the torque and the force of the associated oscillator: the term `m g ℓ (θ - sin θ)` the
>   linearization discards. Its norm is at most `m g ℓ ‖θ‖³/6`
>   (`norm_torque_sub_toHarmonicOscillator_force_le`), in coordinates `abs_torque_add_linear_le`,
>   and `gradLagrangian_sub_toHarmonicOscillator` identifies the difference of the variational
>   gradients of the two actions with the difference of torque and linearized force, with the
>   norm bound `norm_gradLagrangian_sub_toHarmonicOscillator_le`.
> - `SimplePendulum.norm_equationOfMotion_residual_le`: a small-angle motion nearly solves the
>   equation of motion of the pendulum itself, leaving at every instant a residual of norm at
>   most `m g ℓ ‖θ‖³/6` — the sense in which the small-angle theory approximates the pendulum;
>   in variational form, `norm_gradLagrangian_le_of_linearizedEquationOfMotion` makes it a
>   near-critical point of the pendulum's action.

## iv. References

> References for the small-angle motion of the simple pendulum include:
>
> * Huygens, Horologium Oscillatorium (1673). [ref: huygens\_1673]
> * Landau & Lifshitz, Mechanics, 3rd ed., §21. [ref: landau\_mechanics]
> * The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Basic`, whose equation of motion
>   this module linearizes.

## A. The harmonic oscillator of small oscillations

> Replacing `sin θ` by `θ` in the equation of motion `I θ̈ = -m g ℓ sin θ` produces the equation
> of a harmonic oscillator: the moment of inertia plays the role of the mass, and the coefficient
> `m g ℓ` of the linearized torque plays the role of the spring constant. We record this
> oscillator once and for all; its solution theory is the solution theory of the small
> oscillations of the pendulum.

### A.1. The associated harmonic oscillator

> The data of the associated oscillator: the mass `I = m ℓ²` and the spring constant `m g ℓ`,
> both positive because the data of the pendulum is.

**`ClassicalMechanics.SimplePendulum.toHarmonicOscillator`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L152).

> The harmonic oscillator to which the pendulum linearizes: mass `I = m ℓ²`, spring
> constant `m g ℓ`.

```lean
noncomputable def toHarmonicOscillator : HarmonicOscillator
```

**`ClassicalMechanics.SimplePendulum.toHarmonicOscillator_m`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L161).

> The mass of the harmonic oscillator associated to the simple pendulum is the moment of
> inertia `I = m ℓ²` of the pendulum about its pivot.

```lean
lemma toHarmonicOscillator_m : S.toHarmonicOscillator.m = S.inertia
```

**`ClassicalMechanics.SimplePendulum.toHarmonicOscillator_k`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L166).

> The spring constant of the harmonic oscillator associated to the simple pendulum is
> `m g ℓ`, the coefficient of the linearized torque.

```lean
lemma toHarmonicOscillator_k : S.toHarmonicOscillator.k = S.m * S.g * S.ℓ
```

### A.2. The frequency of the associated oscillator

> The angular frequency `√(k/m) = √(m g ℓ / m ℓ²)` of the associated oscillator collapses, the
> mass cancelling, to `√(g/ℓ)`: the constant `ω` of the pendulum, as promised by its description
> in `SimplePendulum.Basic` as the frequency of the small oscillations.

**`ClassicalMechanics.SimplePendulum.toHarmonicOscillator_ω`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L180).

> The angular frequency of the harmonic oscillator associated to the simple pendulum is the
> angular frequency `ω = √(g/ℓ)` of the small oscillations of the pendulum.

```lean
lemma toHarmonicOscillator_ω : S.toHarmonicOscillator.ω = S.ω
```

## B. The linearized equation of motion

> The linearized equation of motion is the equation `θ̈ + ω² θ = 0` obtained from the scalar form
> `θ̈ + ω² sin θ = 0` of the equation of motion by replacing `sin θ` with `θ`. It is stated, like
> the nonlinear equation, on the Euclidean lift of the angle, and it is exactly the associated
> harmonic oscillator's form of Newton's second law: multiplying by the moment of inertia converts
> one pointwise equation into the other.

### B.1. The linearized equation

> The equation `θ̈ + ω² θ = 0`, together with its rotational Newton form `I θ̈ = -m g ℓ θ`, in
> which the right-hand side is the force of the associated harmonic oscillator.

**`ClassicalMechanics.SimplePendulum.LinearizedEquationOfMotion`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L210).

> The linearized equation of motion `θ̈ + ω² θ = 0` of the simple pendulum, the small-angle
> form of the equation of motion, in which the torque is replaced by its linearization at the
> bottom of the swing.

```lean
def LinearizedEquationOfMotion (θ : Time → EuclideanSpace ℝ (Fin 1)) : Prop
```

**`ClassicalMechanics.SimplePendulum.linearizedEquationOfMotion_iff_newton`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L217).

> The linearized equation of motion in the rotational form of Newton's second law: at every
> instant the rate of change `I θ̈` of the angular momentum equals the force `-m g ℓ θ` of the
> associated harmonic oscillator. No smoothness is required: the two pointwise equations differ
> by the nonzero factor `I`.

```lean
lemma linearizedEquationOfMotion_iff_newton (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.LinearizedEquationOfMotion θ ↔
      ∀ t, S.inertia • ∂ₜ (∂ₜ θ) t = S.toHarmonicOscillator.force (θ t)
```

### B.2. Equivalence with the equation of motion of the oscillator

> For a smooth lift of the angle, the linearized equation of motion is the equation of motion of
> the associated harmonic oscillator, through the latter's own form of Newton's second law. The
> solution theory of the harmonic oscillator thereby becomes available to the small oscillations
> of the pendulum.

**`ClassicalMechanics.SimplePendulum.linearizedEquationOfMotion_iff`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L242).

> For a smooth lift of the angle, the linearized equation of motion of the simple pendulum is
> the equation of motion of the associated harmonic oscillator. The oscillator's equation of
> motion is the vanishing of the variational gradient of its action, which is totalized;
> smoothness is the regularity under which that variational description agrees with the pointwise
> one. The smoothness-free pointwise content is `linearizedEquationOfMotion_iff_newton`.

```lean
lemma linearizedEquationOfMotion_iff (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) :
    S.LinearizedEquationOfMotion θ ↔ S.toHarmonicOscillator.EquationOfMotion θ
```

### B.3. Linearization as differentiation of the torque

> The linearized force is not an ansatz: it is the derivative of the pendulum's torque at the
> hanging equilibrium. The torque vanishes at the equilibrium, so its best linear approximation
> there is the derivative alone, and that derivative is exactly the force of the associated
> harmonic oscillator. The linearized equation of motion is therefore the equation of motion
> with the torque replaced by its derivative at the equilibrium — linearizing the pendulum is
> differentiating its torque.

**`ClassicalMechanics.SimplePendulum.fderiv_torque_zero_apply`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L264).

> The derivative of the torque at the hanging equilibrium is the force of the associated
> harmonic oscillator: `(Dτ)(0) v = -m g ℓ v`. Linearizing the pendulum is differentiating
> its torque at the equilibrium.

```lean
lemma fderiv_torque_zero_apply (v : EuclideanSpace ℝ (Fin 1)) :
    fderiv ℝ S.torque 0 v = S.toHarmonicOscillator.force v
```

**`ClassicalMechanics.SimplePendulum.linearizedEquationOfMotion_iff_fderiv_torque`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L286).

> The linearized equation of motion is the equation of motion with the torque replaced by
> its derivative at the hanging equilibrium.

```lean
lemma linearizedEquationOfMotion_iff_fderiv_torque (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.LinearizedEquationOfMotion θ ↔
      ∀ t, S.inertia • ∂ₜ (∂ₜ θ) t = fderiv ℝ S.torque 0 (θ t)
```

## C. Small-angle trajectories

> For small angles the pendulum is approximated by its associated harmonic oscillator, and the
> solution theory of the oscillator transfers verbatim: every choice of initial angle and
> initial angular velocity determines a smooth motion, unique among the smooth solutions of the
> linearized equation of motion. This section performs the transfer, and specializes it to the
> classical motion released from rest at a given angle.

### C.1. The trajectory of given initial conditions

> The small-angle motion determined by an initial angle `IC.x₀` and an initial angular velocity
> `IC.v₀` is the trajectory of the associated harmonic oscillator for the same initial
> conditions. It is smooth in time, it assumes the prescribed initial data at time `0`, and
> written out it is the familiar `cos (ω t) x₀ + (sin (ω t)/ω) v₀`, with the frequency of the
> oscillator read as the `ω` of the pendulum.

**`ClassicalMechanics.SimplePendulum.smallAngleTrajectory`**, a def, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L319).

> The small-angle motion of the simple pendulum with initial angle `IC.x₀` and initial
> angular velocity `IC.v₀`: the trajectory of the associated harmonic oscillator with the same
> initial conditions.

```lean
noncomputable def smallAngleTrajectory (IC : HarmonicOscillator.InitialConditions) :
    Time → EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.SimplePendulum.smallAngleTrajectory_contDiff`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L325).

> The small-angle trajectories of the simple pendulum are smooth in time.

```lean
lemma smallAngleTrajectory_contDiff (IC : HarmonicOscillator.InitialConditions)
    {n : WithTop ℕ∞} : ContDiff ℝ n (S.smallAngleTrajectory IC)
```

**`ClassicalMechanics.SimplePendulum.smallAngleTrajectory_at_zero`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L331).

> At time `0` the small-angle trajectory passes through its initial angle.

```lean
lemma smallAngleTrajectory_at_zero (IC : HarmonicOscillator.InitialConditions) :
    S.smallAngleTrajectory IC 0 = IC.x₀
```

**`ClassicalMechanics.SimplePendulum.smallAngleTrajectory_velocity_at_zero`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L337).

> At time `0` the small-angle trajectory moves with its initial angular velocity.

```lean
lemma smallAngleTrajectory_velocity_at_zero (IC : HarmonicOscillator.InitialConditions) :
    ∂ₜ (S.smallAngleTrajectory IC) 0 = IC.v₀
```

**`ClassicalMechanics.SimplePendulum.smallAngleTrajectory_eq`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L344).

> The closed form of the small-angle motion: `cos (ω t) x₀ + (sin (ω t)/ω) v₀`, the
> trajectory of the associated harmonic oscillator with its frequency read as the `ω` of the
> pendulum.

```lean
lemma smallAngleTrajectory_eq (IC : HarmonicOscillator.InitialConditions) :
    S.smallAngleTrajectory IC = fun t : Time =>
      Real.cos (S.ω * t.val) • IC.x₀ + (Real.sin (S.ω * t.val) / S.ω) • IC.v₀
```

### C.2. Existence and uniqueness

> The small-angle trajectories solve the linearized equation of motion, and they are the only
> smooth solutions: a smooth solution with the initial data of `IC` is the small-angle
> trajectory of `IC`. Both statements are the corresponding statements for the associated
> harmonic oscillator, read through the equivalence `linearizedEquationOfMotion_iff` of the two
> equations of motion.

**`ClassicalMechanics.SimplePendulum.smallAngleTrajectory_linearizedEquationOfMotion`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L364).

> The small-angle trajectories satisfy the linearized equation of motion: for every choice
> of initial conditions the linearized equation has a smooth solution assuming them.

```lean
lemma smallAngleTrajectory_linearizedEquationOfMotion
    (IC : HarmonicOscillator.InitialConditions) :
    S.LinearizedEquationOfMotion (S.smallAngleTrajectory IC)
```

**`ClassicalMechanics.SimplePendulum.linearized_unique`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L374).

> Uniqueness of the small-angle motions: a smooth solution of the linearized equation of
> motion is determined by its initial angle and initial angular velocity, being the
> small-angle trajectory of those initial conditions. This is the uniqueness theorem for the
> associated harmonic oscillator, transferred through `linearizedEquationOfMotion_iff`.

```lean
lemma linearized_unique (IC : HarmonicOscillator.InitialConditions)
    (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ)
    (h : S.LinearizedEquationOfMotion θ) (h0 : θ 0 = IC.x₀) (hv : ∂ₜ θ 0 = IC.v₀) :
    θ = S.smallAngleTrajectory IC
```

## D. The small-angle period

> The associated harmonic oscillator completes one oscillation in the time `2π/ω`, and its
> angular frequency is the `ω = √(g/ℓ)` of the pendulum: the small oscillations have period
> `2π √(ℓ/g)`, independent of both the mass of the bob and the amplitude of the swing. Within
> the linearization the pendulum is isochronous; the dependence of the true period on the
> amplitude is invisible at this order.

### D.1. The period and its closed form

> The period of the small oscillations is the period of the associated harmonic oscillator. Its
> closed form `2π √(ℓ/g)` involves only the length of the rod and the strength of gravity: the
> mass of the bob cancelled from the frequency, and the amplitude never entered.

**`ClassicalMechanics.SimplePendulum.smallAnglePeriod`**, a def, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L406).

> The period `2π √(ℓ/g)` of the small oscillations of the simple pendulum: the period of the
> associated harmonic oscillator. Within the linearization it does not depend on the
> amplitude — the small oscillations are isochronous, as derived by Huygens (1673).

```lean
noncomputable def smallAnglePeriod : ℝ
```

**`ClassicalMechanics.SimplePendulum.smallAnglePeriod_eq_two_pi_div_ω`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L410).

> The period of the small oscillations is `2π/ω`, one full circle of phase at the angular
> frequency `ω` of the small oscillations.

```lean
lemma smallAnglePeriod_eq_two_pi_div_ω : S.smallAnglePeriod = 2 * Real.pi / S.ω
```

**`ClassicalMechanics.SimplePendulum.smallAnglePeriod_eq`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L416).

> The closed form of the small-angle period: `2π √(ℓ/g)`. Neither the mass of the bob nor
> the amplitude of the swing appears.

```lean
lemma smallAnglePeriod_eq : S.smallAnglePeriod = 2 * Real.pi * √(S.ℓ / S.g)
```

**`ClassicalMechanics.SimplePendulum.smallAnglePeriod_pos`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L422).

> The period of the small oscillations is positive.

```lean
lemma smallAnglePeriod_pos : 0 < S.smallAnglePeriod
```

### D.2. Periodicity and the energy of the small-angle motions

> Advancing time by one period shifts the phase `ω t` by `2π` and so returns every small-angle
> motion to its state: the small-angle trajectories are periodic with the small-angle period.
> Along each of them the energy of the associated harmonic oscillator is constant, equal to the
> value fixed by the initial data.

**`ClassicalMechanics.SimplePendulum.smallAngleTrajectory_periodic`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L438).

> The small-angle trajectories of the simple pendulum are periodic with the small-angle
> period `2π √(ℓ/g)`.

```lean
lemma smallAngleTrajectory_periodic (IC : HarmonicOscillator.InitialConditions) :
    Function.Periodic (S.smallAngleTrajectory IC) (S.smallAnglePeriod : Time)
```

**`ClassicalMechanics.SimplePendulum.smallAngleTrajectory_energy`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L445).

> Along a small-angle trajectory the energy of the associated harmonic oscillator is the
> constant `½ (I ‖v₀‖² + m g ℓ ‖IC.x₀‖²)` fixed by the initial data: the rotational kinetic term
> of the initial angular velocity plus the potential term of the initial angle.

```lean
lemma smallAngleTrajectory_energy (IC : HarmonicOscillator.InitialConditions) :
    S.toHarmonicOscillator.energy (S.smallAngleTrajectory IC) =
      fun _ => 1 / 2 * (S.inertia * ‖IC.v₀‖ ^ 2 + S.m * S.g * S.ℓ * ‖IC.x₀‖ ^ 2)
```

## E. The error of the linearization

> The linearization replaces the torque `-m g ℓ sin θ` by `-m g ℓ θ`. The replacement is not
> exact, and this section measures what it discards: pointwise the two differ by
> `m g ℓ (θ - sin θ)`, which the Taylor estimate for the sine bounds by `m g ℓ |θ|³/6`; the
> difference of the variational gradients of the two actions is exactly this difference of the
> torques, the inertial terms cancelling; and every small-angle motion solves the equation of
> motion of the pendulum itself up to a residual of the same cubic size.

### E.1. The cubic bound on the torque

> The difference between the torque of the pendulum and the force of the associated oscillator
> is exactly `m g ℓ (θ - sin θ)` times the unit vector of the angular direction, which the
> Taylor estimate for the sine bounds in norm by `m g ℓ ‖θ‖³/6`: for small angles the discarded
> term is cubically small. In the single coordinate of the angle the same bound reads
> `m g ℓ |θ|³/6`.

**`ClassicalMechanics.SimplePendulum.torque_sub_toHarmonicOscillator_force`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L478).

> The difference between the torque of the simple pendulum and the force of its associated
> harmonic oscillator is `m g ℓ (θ - sin θ)` times the unit vector of the angular direction:
> exactly the term the linearization discards.

```lean
lemma torque_sub_toHarmonicOscillator_force (x : EuclideanSpace ℝ (Fin 1)) :
    S.torque x - S.toHarmonicOscillator.force x =
      (S.m * S.g * S.ℓ * (x 0 - Real.sin (x 0))) • EuclideanSpace.single 0 1
```

**`ClassicalMechanics.SimplePendulum.norm_torque_sub_toHarmonicOscillator_force_le`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L490).

> The normed form of the cubic bound: the torque of the simple pendulum differs from the
> force of its associated harmonic oscillator by at most `m g ℓ ‖θ‖³ / 6` in norm.

```lean
lemma norm_torque_sub_toHarmonicOscillator_force_le (x : EuclideanSpace ℝ (Fin 1)) :
    ‖S.torque x - S.toHarmonicOscillator.force x‖ ≤ S.m * S.g * S.ℓ * ‖x‖ ^ 3 / 6
```

**`ClassicalMechanics.SimplePendulum.abs_torque_add_linear_le`**, a lemma, [line 503](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L503).

> The torque of the simple pendulum differs from its linearization `-m g ℓ θ` by at most
> `m g ℓ |θ|³ / 6`: the error of the small-angle approximation is cubic in the angle.

```lean
lemma abs_torque_add_linear_le (x : EuclideanSpace ℝ (Fin 1)) :
    |S.torque x 0 + S.m * S.g * S.ℓ * x 0| ≤ S.m * S.g * S.ℓ * |x 0| ^ 3 / 6
```

### E.2. The variational gradients

> The actions of the pendulum and of its associated oscillator have the same kinetic term, the
> moment of inertia being the mass of the oscillator, so along a smooth lift of the angle the
> difference of their variational gradients is the difference of torque and linearized force at
> each instant: the linearization error of the dynamics is the linearization error of the
> torque.

**`ClassicalMechanics.SimplePendulum.gradLagrangian_sub_toHarmonicOscillator`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L534).

> Along a smooth lift of the angle, the variational gradients of the actions of the simple
> pendulum and of its associated harmonic oscillator differ exactly by the difference between
> the torque and the linearized force: the inertial terms cancel.

```lean
lemma gradLagrangian_sub_toHarmonicOscillator (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) :
    S.gradLagrangian θ - S.toHarmonicOscillator.gradLagrangian θ =
      fun t => S.torque (θ t) - S.toHarmonicOscillator.force (θ t)
```

**`ClassicalMechanics.SimplePendulum.norm_gradLagrangian_sub_toHarmonicOscillator_le`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L547).

> The normed form: along a smooth lift of the angle the variational gradients of the two
> actions differ at every instant by at most `m g ℓ ‖θ t‖³ / 6` — the two actions have the
> same critical-point equation to cubic accuracy in the angle.

```lean
lemma norm_gradLagrangian_sub_toHarmonicOscillator_le (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) (t : Time) :
    ‖S.gradLagrangian θ t - S.toHarmonicOscillator.gradLagrangian θ t‖ ≤
      S.m * S.g * S.ℓ * ‖θ t‖ ^ 3 / 6
```

### E.3. The residual of the small-angle motions

> Combining the linearized dynamics with the cubic bound: a small-angle motion does not solve
> the equation of motion of the pendulum exactly, but the residual it leaves in it is cubically
> small in the angle — the small-angle theory solves the pendulum's own equation up to an error
> of at most `m g ℓ ‖θ‖³/6` at every instant.

**`ClassicalMechanics.SimplePendulum.norm_equationOfMotion_residual_le`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L570).

> A motion satisfying the linearized equation of motion nearly solves the equation of motion
> of the pendulum itself: at every instant the residual `I θ̈ - τ(θ)` has norm at most
> `m g ℓ ‖θ‖³ / 6`, cubically small for small angles.

```lean
lemma norm_equationOfMotion_residual_le (θ : Time → EuclideanSpace ℝ (Fin 1))
    (h : S.LinearizedEquationOfMotion θ) (t : Time) :
    ‖S.inertia • ∂ₜ (∂ₜ θ) t - S.torque (θ t)‖ ≤ S.m * S.g * S.ℓ * ‖θ t‖ ^ 3 / 6
```

**`ClassicalMechanics.SimplePendulum.norm_gradLagrangian_le_of_linearizedEquationOfMotion`**, a lemma, [line 580](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean#L580).

> The variational form of the residual: a smooth motion of the linearized dynamics is a
> near-critical point of the pendulum's own action — along it the variational gradient of the
> pendulum's action is cubically small in the angle.

```lean
lemma norm_gradLagrangian_le_of_linearizedEquationOfMotion
    (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ)
    (h : S.LinearizedEquationOfMotion θ) (t : Time) :
    ‖S.gradLagrangian θ t‖ ≤ S.m * S.g * S.ℓ * ‖θ t‖ ^ 3 / 6
```

## Depends on

- [Periodicity and recurrence](../../harmonicoscillator/solution-periodicity.md)
- [The simple gravity pendulum](basic.md)

## Proof depends on

- [The energy of the trajectories](../../harmonicoscillator/solution-energy.md)
- [Uniqueness](../../harmonicoscillator/solution-uniqueness.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/SmallAngle.lean)
