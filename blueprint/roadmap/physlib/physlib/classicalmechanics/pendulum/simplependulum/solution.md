---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.phaseVectorField, ClassicalMechanics.SimplePendulum.phaseVectorField_lipschitz, ClassicalMechanics.SimplePendulum.acceleration_eq_of_equationOfMotion, ClassicalMechanics.SimplePendulum.inertia_smul_eq_torque, ClassicalMechanics.SimplePendulum.phaseCurve_hasDerivAt, ClassicalMechanics.SimplePendulum.equationOfMotion_unique, ClassicalMechanics.SimplePendulum.IsSolution.eq_of_initial, ClassicalMechanics.SimplePendulum.isSolution_comp_neg
statement: formalized
proof: formalized
---

# Existence and uniqueness of the solutions of the simple pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Solution`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean): 11 declarations, 11 with a docstring.

## i. Overview

> The equation of motion of the simple pendulum, `θ̈ + ω² sin θ = 0`, is nonlinear, and unlike the
> harmonic oscillator it has no solution in closed elementary form. Whatever is to be proved about
> "the" motion of the pendulum released with a given angle and angular velocity must therefore rest
> on the general theory of ordinary differential equations rather than on an explicit formula. This
> module supplies that foundation: two smooth solutions of the equation of motion with the same
> initial angle and the same initial angular velocity coincide for all time, and for any initial
> angle and angular velocity there is a curve with that initial data satisfying the equation of
> motion on some interval of time about the initial instant.
>
> The argument is the one used for the damped harmonic oscillator. The second-order equation is
> rewritten as the first-order system `(θ, θ̇)' = (θ̇, -ω² sin θ)` on the phase space, whose
> right-hand side, the phase-space vector field of the pendulum, is globally Lipschitz because `sin`
> is. The global uniqueness theorem for Lipschitz first-order systems, Mathlib's
> `ODE_solution_unique_univ`, then gives the uniqueness. The uniqueness is global in time and does
> not depend on the size of the motion: it holds for librations and rotations alike. Existence comes
> from the Picard–Lindelöf theorem applied to the same first-order system, the phase-space vector
> field being smooth; the theorem is local, and so is the statement proved here.
>
> The equation of motion contains no first derivative of the angle: there is no damping. Reversing
> the direction of time therefore carries solutions to solutions, and combined with uniqueness this
> shows that a pendulum released from rest retraces its path, the angle being an even function of
> the time since release.

## ii. Key results

> - `SimplePendulum.phaseVectorField` is the phase-space vector field `(θ, θ̇) ↦ (θ̇, -ω² sin θ)`,
>   and `SimplePendulum.phaseVectorField_lipschitz` proves that it is globally Lipschitz, with
>   constant `1 + ω²`.
> - `SimplePendulum.acceleration_eq_of_equationOfMotion` solves the equation of motion for the
>   angular acceleration, and `SimplePendulum.phaseCurve_hasDerivAt` shows that the phase curve
>   `(θ, θ̇)` of a smooth solution is an integral curve of the phase-space vector field.
> - `SimplePendulum.equationOfMotion_unique` proves that two smooth solutions of the equation of
>   motion with the same initial angle and angular velocity are equal, and
>   `SimplePendulum.IsSolution.eq_of_initial` is the same statement for solutions.
> - `SimplePendulum.isSolution_comp_neg` proves that the time reversal `t ↦ θ (-t)` of a solution
>   is a solution, and `SimplePendulum.releasedFromRest_even` that a solution released from rest is
>   an even function of time.
> - `SimplePendulum.exists_local_solution` proves, from the Picard–Lindelöf theorem, that for any
>   initial angle and angular velocity there is a curve with that initial data, differentiable
>   together with its velocity and satisfying the equation of motion at all times within some
>   `ε > 0` of the initial instant.

## iv. References

> References for the motion of the pendulum, its phase plane, and the existence and uniqueness
> theorem for ordinary differential equations include:
>
> * Landau & Lifshitz, Mechanics, 3rd ed., §11, for motion in one dimension. [ref: landau\_mechanics]
> * Arnold, Mathematical Methods of Classical Mechanics, 2nd ed., §4, for the phase plane of the
>   pendulum. [ref: arnold\_mechanics]
> * Arnold, Ordinary Differential Equations, Chapter 4 (Proofs of the main theorems), for the
>   existence and uniqueness theorem by Picard iteration. [ref: arnold\_ode]
>
> The reduction to a first-order system on the phase space follows
> `DampedHarmonicOscillator.equationOfMotion_unique`.

## A. The phase-space vector field

> The equation of motion `θ̈ + ω² sin θ = 0` is of second order. Taking the angular velocity as a
> second unknown turns it into the first-order system `(θ, θ̇)' = (θ̇, -ω² sin θ)` on the phase
> space, the product of two copies of the one-dimensional Euclidean space carrying the angle and its
> rate of change. The right-hand side of this system is the phase-space vector field of the
> pendulum. Its first component is the projection onto the angular velocity, and its second is `-ω²`
> times the sine of the angle; as the derivative of `sin` is bounded by one, the field is globally
> Lipschitz on the phase space. This is the hypothesis under which the general uniqueness theorem
> for first-order systems applies with no restriction on the time interval or on the size of the
> motion.

### A.1. The definition of the vector field

**`ClassicalMechanics.SimplePendulum.phaseVectorField`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L123).

> The phase-space vector field of the simple pendulum, sending `(θ, θ̇)` to
> `(θ̇, -ω² sin θ)`. It is the right-hand side of the first-order system on the phase space
> equivalent to the equation of motion `θ̈ + ω² sin θ = 0`.

```lean
noncomputable def phaseVectorField (p : EuclideanSpace ℝ (Fin 1) × EuclideanSpace ℝ (Fin 1)) :
    EuclideanSpace ℝ (Fin 1) × EuclideanSpace ℝ (Fin 1)
```

### A.2. The Lipschitz bound

**`ClassicalMechanics.SimplePendulum.phaseVectorField_lipschitz`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L136).

> The phase-space vector field of the simple pendulum is globally Lipschitz, with constant
> `1 + ω²`: the first component is the projection onto the angular velocity, and the second is
> `-ω²` times `sin` of the angle, and `sin` is Lipschitz with constant one.

```lean
lemma phaseVectorField_lipschitz :
    LipschitzWith (Real.toNNReal (1 + S.ω ^ 2)) S.phaseVectorField
```

## B. The phase curve of a solution

> A smooth lift `θ` of the angle satisfying the equation of motion determines the phase curve
> `t ↦ (θ t, θ̇ t)` in the phase space. Solving the equation of motion for the angular acceleration
> shows that this curve is an integral curve of the phase-space vector field: its velocity at every
> instant is the value of the field at its position. The curve is parametrised here by a real
> variable through the canonical equivalence `Time.toRealCLE.symm : ℝ ≃L[ℝ] Time`, as the
> uniqueness theorem of Mathlib is stated for curves on `ℝ`.

### B.1. The angular acceleration along a solution

**`ClassicalMechanics.SimplePendulum.acceleration_eq_of_equationOfMotion`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L175).

> Solving the equation of motion for the angular acceleration: along a solution the second
> derivative of the angle is `-ω² sin θ` times the unit vector of the angular coordinate, the
> mass having cancelled.

```lean
lemma acceleration_eq_of_equationOfMotion (θ : Time → EuclideanSpace ℝ (Fin 1))
    (h : S.EquationOfMotion θ) (t : Time) :
    ∂ₜ (∂ₜ θ) t = -(S.ω ^ 2 * Real.sin (θ t 0)) • EuclideanSpace.single 0 1
```

**`ClassicalMechanics.SimplePendulum.inertia_smul_eq_torque`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L185).

> The pointwise equation of motion in terms of the angular frequency: the moment of inertia
> times the acceleration `-ω² sin θ` is the torque. This reads the equation of motion back off
> the second component of the phase-space vector field.

```lean
lemma inertia_smul_eq_torque (x : EuclideanSpace ℝ (Fin 1)) :
    S.inertia • (-(S.ω ^ 2 * Real.sin (x 0)) • EuclideanSpace.single 0 1) = S.torque x
```

### B.2. The phase curve as an integral curve

**`ClassicalMechanics.SimplePendulum.phaseCurve_hasDerivAt`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L199).

> The phase curve `τ ↦ (θ t, θ̇ t)` (with `t = toRealCLE.symm τ`) of a smooth solution `θ`
> solves the first-order phase-space ODE with vector field `phaseVectorField`.

```lean
lemma phaseCurve_hasDerivAt {θ : Time → EuclideanSpace ℝ (Fin 1)}
    (hθ : ContDiff ℝ ∞ θ) (h : S.EquationOfMotion θ) (τ : ℝ) :
    HasDerivAt (fun τ : ℝ => (θ (toRealCLE.symm τ), ∂ₜ θ (toRealCLE.symm τ)))
      (S.phaseVectorField (θ (toRealCLE.symm τ), ∂ₜ θ (toRealCLE.symm τ))) τ
```

## C. Uniqueness of the solutions

> The phase curves of two smooth solutions with the same initial angle and angular velocity are two
> integral curves of the same globally Lipschitz vector field through the same point at time zero.
> By the global uniqueness theorem `ODE_solution_unique_univ` they coincide, and reading off the
> first component the two solutions are equal. The energy is conserved along a solution, but it is
> not used here: the nonlinear equation of motion is handled exactly as the linear damped one, by the
> first-order reduction alone.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_unique`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L222).

> Any two smooth solutions of the equation of motion of the simple pendulum with the same
> initial angle and angular velocity are equal.

```lean
lemma equationOfMotion_unique {x y : Time → EuclideanSpace ℝ (Fin 1)}
    (hx : ContDiff ℝ ∞ x) (hy : ContDiff ℝ ∞ y)
    (hEOMx : S.EquationOfMotion x) (hEOMy : S.EquationOfMotion y)
    (h0 : x 0 = y 0) (hv0 : ∂ₜ x 0 = ∂ₜ y 0) : x = y
```

**`ClassicalMechanics.SimplePendulum.IsSolution.eq_of_initial`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L239).

> Two solutions of the simple pendulum with the same initial angle and angular velocity are
> equal.

```lean
lemma IsSolution.eq_of_initial {S : SimplePendulum} {x y : Time → EuclideanSpace ℝ (Fin 1)}
    (hx : S.IsSolution x) (hy : S.IsSolution y) (h0 : x 0 = y 0) (hv0 : ∂ₜ x 0 = ∂ₜ y 0) :
    x = y
```

## D. Time-reversal symmetry

> The equation of motion `I θ̈ = τ(θ)` is of second order and contains no first derivative of the
> angle: there is no damping. Under the reversal of time `t ↦ -t` the angular velocity changes sign
> and the angular acceleration does not, so the reversed curve `t ↦ θ (-t)` of a solution is again a
> solution. Together with the uniqueness of section C this has a physical consequence: a pendulum
> released from rest at the instant `0` retraces its path, the angle at time `-t` being the angle at
> time `t`. The bookkeeping of the derivatives under the reflection of `Time` is done by the chain
> rule `Time.deriv_comp_neg` and its second-order form `Time.deriv_deriv_comp_neg`.

### D.1. Time reversal of solutions

**`ClassicalMechanics.SimplePendulum.isSolution_comp_neg`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L268).

> The time reversal `t ↦ θ (-t)` of a solution of the simple pendulum is a solution: the
> equation of motion has no velocity term, and the angular acceleration is unchanged by the
> reversal.

```lean
lemma isSolution_comp_neg {S : SimplePendulum} {θ : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution θ) : S.IsSolution (fun t => θ (-t))
```

### D.2. Motions released from rest

**`ClassicalMechanics.SimplePendulum.releasedFromRest_even`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L284).

> A solution of the simple pendulum released from rest at the instant `0` is an even function
> of time: it retraces its path, `θ (-t) = θ t`. The time reversal of the solution has the same
> initial angle and, the initial angular velocity being zero, the same initial angular velocity,
> so the two coincide by uniqueness.

```lean
lemma releasedFromRest_even {S : SimplePendulum} {θ : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution θ) (hv : ∂ₜ θ 0 = 0) (t : Time) : θ (-t) = θ t
```

## E. Local existence

> The uniqueness of section C says that a solution with given initial angle and angular velocity is
> unique if it exists. Existence comes from the Picard–Lindelöf theorem, in the form Mathlib states
> it for a time-independent `C¹` vector field: the field admits an integral curve through any point,
> defined on an open interval about the initial instant. Applied to the phase-space vector field of
> the pendulum, which is smooth, this gives a curve `(θ, θ̇)` in the phase space through the initial
> data, and its first component is the required angle. Mathlib's curve is parametrised by `ℝ`, so it
> is pulled back to `Time` through `Time.toRealCLE`; its derivative is read off through
> `Time.deriv_comp_toRealCLE_of_hasDerivAt`, the converse of the bridge lemma
> `Time.hasDerivAt_comp_toRealCLE_symm`.
>
> The statement is local: at the times within `ε` of the initial instant, for some `ε > 0`, the
> angle and its velocity are differentiable and the equation of motion holds, and nothing is claimed
> about the curve outside that interval. The differentiability is part of the conclusion so that
> the equation of motion there is a statement about genuine derivatives, and not about the value
> `0` that `∂ₜ` assigns to a curve where it is not differentiable. Global existence, which the
> global Lipschitz bound of section A makes true, is not proved here.

### E.1. Smoothness of the phase-space vector field

**`ClassicalMechanics.SimplePendulum.phaseVectorField_contDiff`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L322).

> The phase-space vector field of the simple pendulum is smooth: its components are the
> projection onto the angular velocity and `sin` of the angle.

```lean
lemma phaseVectorField_contDiff (n : WithTop ℕ∞) : ContDiff ℝ n S.phaseVectorField
```

### E.2. Local existence of solutions

**`ClassicalMechanics.SimplePendulum.exists_local_solution`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean#L338).

> **Local existence** of solutions of the simple pendulum: for any initial angle `x₀` and
> angular velocity `v₀` there are `ε > 0` and a curve `θ` with `θ 0 = x₀` and `∂ₜ θ 0 = v₀` which,
> at every time within `ε` of the initial instant, is differentiable together with its velocity
> `∂ₜ θ` and satisfies the equation of motion. This is the Picard–Lindelöf theorem applied to the
> phase-space vector field, the first component of the integral curve through `(x₀, v₀)` being
> the angle.

```lean
lemma exists_local_solution (x₀ v₀ : EuclideanSpace ℝ (Fin 1)) :
    ∃ ε > (0 : ℝ), ∃ θ : Time → EuclideanSpace ℝ (Fin 1), θ 0 = x₀ ∧ ∂ₜ θ 0 = v₀ ∧
      ∀ t : Time, |t.val| ≤ ε → DifferentiableAt ℝ θ t ∧ DifferentiableAt ℝ (∂ₜ θ) t ∧
        S.inertia • ∂ₜ (∂ₜ θ) t = S.torque (θ t)
```

## Depends on

- [The simple gravity pendulum](basic.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Solution.lean)
