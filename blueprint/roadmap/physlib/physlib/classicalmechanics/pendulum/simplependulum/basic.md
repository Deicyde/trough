---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum, ClassicalMechanics.SimplePendulum.m_ne_zero, ClassicalMechanics.SimplePendulum.ℓ_ne_zero, ClassicalMechanics.SimplePendulum.g_ne_zero, ClassicalMechanics.SimplePendulum.ω, ClassicalMechanics.SimplePendulum.ω_pos, ClassicalMechanics.SimplePendulum.ω_ne_zero, ClassicalMechanics.SimplePendulum.ω_sq
statement: formalized
proof: formalized
---

# The simple gravity pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Basic`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean): 55 declarations, 55 with a docstring.

## i. Overview

> A simple gravity pendulum is a bob of mass `m` fixed to one end of a rigid massless rod of length
> `ℓ`, the other end of which is pinned at a pivot, swinging in a vertical plane under a uniform
> gravitational acceleration `g`. Its configuration is the angle `θ` of the rod from the downward
> vertical. The bob moves on the circle of radius `ℓ` about the pivot, so its moment of inertia
> about the pivot is `I = m ℓ²` and its kinetic energy is `T = ½ I θ̇²`. Swinging out to the angle
> `θ` raises the bob by `ℓ (1 - cos θ)` against gravity, so the potential energy is
> `V = m g ℓ (1 - cos θ)`, normalized to vanish at the bottom of the swing. Balancing the rate of
> change of the angular momentum about the pivot against the torque `-m g ℓ sin θ` of gravity gives
> the equation of motion `I θ̈ = -m g ℓ sin θ`, equivalently `θ̈ + (g/ℓ) sin θ = 0`. The mass drops
> out of the motion, which is governed by the single quantity `ω = √(g/ℓ)`, the angular frequency of
> the small oscillations about the bottom.
>
> The configuration of the pendulum is genuinely an angle modulo a full turn, an element of the
> circle `SimplePendulum.ConfigurationSpace`. As for the harmonic oscillator, the dynamics in this
> file are written instead on the Euclidean lift `Time → EuclideanSpace ℝ (Fin 1)`: the angle is
> carried by a real number, from which the configuration is recovered by
> `SimplePendulum.ConfigurationSpace.ofAngle`, and the one-dimensional Euclidean space stands in for
> both the configuration space and its tangent space, so that the Euler–Lagrange operator of Physlib
> applies verbatim. Two lifts differing by `2π n` describe the same motion: the invariance of the
> dynamics under such shifts is proved in the module `SimplePendulum.LiftInvariance`, and the full
> connection of the model here with the geometric configuration space is made in a later module.
> The first consequences of the dynamics — the equilibria, and the below- and above-separatrix
> energy bounds characteristic of libration and rotation — follow in `SimplePendulum.Equilibria`.

## ii. Key results

> - `SimplePendulum` contains the input data of the problem: the mass `m` of the bob, the length `ℓ`
>   of the rod and the gravitational acceleration `g`.
> - `SimplePendulum.ω` is the angular frequency `√(g/ℓ)` of the small oscillations, and
>   `SimplePendulum.inertia` is the moment of inertia `m ℓ²` of the bob about the pivot. They are
>   tied together by `SimplePendulum.ω_sq_mul_inertia`, the identity by which the mass cancels from
>   the equation of motion.
> - `SimplePendulum.kineticEnergy`, `SimplePendulum.potentialEnergy` and `SimplePendulum.energy` are
>   the energies, with the bounds `potentialEnergy_nonneg`, `potentialEnergy_le` and
>   `potentialEnergy_eq_zero_iff`, the gradient `gradient_potentialEnergy` of the potential and the
>   time derivatives `kineticEnergy_deriv`, `potentialEnergy_deriv` and `energy_deriv`.
> - `SimplePendulum.lagrangian` is the Lagrangian `T - V` of the pendulum, and
>   `SimplePendulum.torque` is the torque about the pivot, the generalized force conjugate to
>   the angle.
> - `SimplePendulum.EquationOfMotion` is the equation of motion `I θ̈ = τ(θ)`, with its scalar form
>   `equationOfMotion_iff_scalar` and its independence of the mass `equationOfMotion_iff_of_eq_ω`;
>   `SimplePendulum.IsSolution` is a smooth solution of it.
> - `SimplePendulum.gradLagrangian` is the variational derivative of the action, computed by
>   `gradLagrangian_eq_eulerLagrangeOp` and `gradLagrangian_eq_torque`.
> - `SimplePendulum.equationOfMotion_iff_gradLagrangian_zero` identifies the equation of motion,
>   for smooth lifts of the angle, with the vanishing of the variational derivative of the action,
>   and `SimplePendulum.isSolution_iff` characterizes the solutions as the smooth critical points
>   of the action.
> - `SimplePendulum.energy_conservation_of_equationOfMotion`,
>   `SimplePendulum.energy_conservation_of_equationOfMotion'` and
>   `SimplePendulum.IsSolution.energy_eq` express the conservation of energy along the motions of
>   the pendulum.

## iv. References

> References for the simple gravity pendulum include:
>
> * Landau & Lifshitz, Mechanics, 3rd ed., §5 and §21. [ref: landau\_mechanics]
> * Arnold, Mathematical Methods of Classical Mechanics, 2nd ed., §4. [ref: arnold\_mechanics]

## A. The input data

> We start by defining a structure containing the input data of the simple pendulum, and proving
> basic properties thereof. The input data consists of the mass `m` of the bob, the length `ℓ` of
> the rod, and the gravitational acceleration `g`; everything else in this file is built from these
> three numbers.

### A.1. The structure of the input data

> The three numbers are carried by a structure, together with the positivity assumptions: a
> pendulum with a massless bob, a rod of zero length or no gravity is not a pendulum.

**`ClassicalMechanics.SimplePendulum`**, a structure, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L137).

> The simple gravity pendulum is specified by the mass `m` of its bob, the length `ℓ` of its
> rod, and the gravitational acceleration `g`. All three are assumed to be positive. The
> configuration of the pendulum is the angle of the rod from the downward vertical.

```lean
structure SimplePendulum where
  /-- The mass of the bob. -/
  m : ℝ
  /-- The length of the massless rod. -/
  ℓ : ℝ
  /-- The gravitational acceleration. -/
  g : ℝ
  m_pos : 0 < m
  ℓ_pos : 0 < ℓ
  g_pos : 0 < g
```

### A.2. Simple inequalities for the input data

> The positivity of the input data is used most often through the corresponding non-vanishing
> statements, which is the form in which the field-clearing tactics consume it.

**`ClassicalMechanics.SimplePendulum.m_ne_zero`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L163).

> The mass of the bob is not equal to zero.

```lean
lemma m_ne_zero : S.m ≠ 0
```

**`ClassicalMechanics.SimplePendulum.ℓ_ne_zero`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L167).

> The length of the rod is not equal to zero.

```lean
lemma ℓ_ne_zero : S.ℓ ≠ 0
```

**`ClassicalMechanics.SimplePendulum.g_ne_zero`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L171).

> The gravitational acceleration is not equal to zero.

```lean
lemma g_ne_zero : S.g ≠ 0
```

## B. Frequency and moment of inertia

> Two derived quantities control the dynamics of the pendulum: the angular frequency `ω = √(g/ℓ)`
> of the small oscillations about the bottom of the swing, and the moment of inertia `I = m ℓ²` of
> the bob about the pivot.
>
> The mass enters the equation of motion only through `I`, where it cancels against the mass in the
> torque of gravity; what survives is `ω`. The identity performing that cancellation is
> `ω_sq_mul_inertia`.

### B.1. The angular frequency

> Linearizing `sin θ ≈ θ` about the bottom of the swing turns the equation of motion into that of a
> harmonic oscillator of angular frequency `√(g/ℓ)`. The exact motion is not harmonic, but this
> frequency is the natural time scale of the pendulum and appears throughout its analysis.

**`ClassicalMechanics.SimplePendulum.ω`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L199).

> The angular frequency of the simple pendulum, `ω`, is defined as `√(g/ℓ)`. It is the angular
> frequency of the small oscillations of the pendulum about the bottom of its swing.

```lean
noncomputable def ω : ℝ
```

**`ClassicalMechanics.SimplePendulum.ω_pos`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L203).

> The angular frequency of the simple pendulum is positive.

```lean
lemma ω_pos : 0 < S.ω
```

**`ClassicalMechanics.SimplePendulum.ω_ne_zero`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L206).

> The angular frequency of the simple pendulum is not equal to zero.

```lean
lemma ω_ne_zero : S.ω ≠ 0
```

**`ClassicalMechanics.SimplePendulum.ω_sq`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L209).

> The square of the angular frequency of the simple pendulum is equal to `g/ℓ`.

```lean
lemma ω_sq : S.ω ^ 2 = S.g / S.ℓ
```

**`ClassicalMechanics.SimplePendulum.inverse_ω_sq`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L212).

> The inverse of the square of the angular frequency of the simple pendulum is `ℓ/g`.

```lean
lemma inverse_ω_sq : (S.ω ^ 2)⁻¹ = S.ℓ / S.g
```

### B.2. The moment of inertia

> The bob is a point mass at the fixed distance `ℓ` from the pivot, so the moment of inertia of the
> pendulum about the pivot is `m ℓ²`. It is the coefficient relating the angular acceleration to
> the torque, and so plays for the angle the role that the mass plays for a position.

**`ClassicalMechanics.SimplePendulum.inertia`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L226).

> The moment of inertia of the simple pendulum about its pivot is `I = m ℓ²`, the moment of
> inertia of a point mass `m` at distance `ℓ` from the axis.

```lean
def inertia : ℝ
```

**`ClassicalMechanics.SimplePendulum.inertia_pos`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L229).

> The moment of inertia of the simple pendulum is positive.

```lean
lemma inertia_pos : 0 < S.inertia
```

**`ClassicalMechanics.SimplePendulum.inertia_ne_zero`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L233).

> The moment of inertia of the simple pendulum is not equal to zero.

```lean
lemma inertia_ne_zero : S.inertia ≠ 0
```

**`ClassicalMechanics.SimplePendulum.ω_sq_mul_inertia`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L238).

> The square of the angular frequency times the moment of inertia is `m g ℓ`, the coefficient
> appearing in the potential energy and in the torque. This is the identity by which the mass
> cancels from the equation of motion.

```lean
lemma ω_sq_mul_inertia : S.ω ^ 2 * S.inertia = S.m * S.g * S.ℓ
```

## C. The energies

> The simple pendulum has a kinetic energy determined by the rate of change of its angle, and a
> potential energy determined by the height of the bob, hence by the angle itself. These combine to
> give the total energy of the pendulum.
>
> Here we state and prove a number of properties of these energies, including the gradient of the
> potential energy, which is the object entering the equation of motion.

### C.1. The definitions of the energies

> We define the three energies; it is these energies which control the dynamics of the pendulum,
> through the Lagrangian.

**`ClassicalMechanics.SimplePendulum.kineticEnergy`**, a def, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L269).

> The kinetic energy of the simple pendulum along a lift `θ` of the angle is
> $\frac{1}{2} I ‖\dot θ‖^2$, where `I` is the moment of inertia about the pivot.

```lean
noncomputable def kineticEnergy (θ : Time → EuclideanSpace ℝ (Fin 1)) : Time → ℝ
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy`**, a def, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L275).

> The potential energy of the simple pendulum at the angle `x` is `m g ℓ (1 - cos (x 0))`, the
> work done against gravity in raising the bob from the bottom of the swing. It is normalized to
> vanish at the bottom.

```lean
noncomputable def potentialEnergy (x : EuclideanSpace ℝ (Fin 1)) : ℝ
```

**`ClassicalMechanics.SimplePendulum.energy`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L279).

> The energy of the simple pendulum is the kinetic energy plus the potential energy.

```lean
noncomputable def energy (θ : Time → EuclideanSpace ℝ (Fin 1)) : Time → ℝ
```

### C.2. Simple equalities and bounds for the energies

> Besides the definitional unfoldings, the potential energy of the pendulum is non-negative and
> vanishes exactly at the bottom of the swing, just as the potential energy of the harmonic
> oscillator is non-negative and vanishes exactly at the origin. What has no harmonic-oscillator
> analogue is the upper bound: the potential energy of the pendulum is at most `2 m g ℓ`, its
> value at the top of the swing.

**`ClassicalMechanics.SimplePendulum.kineticEnergy_eq`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L295).

> The kinetic energy of the simple pendulum, written out.

```lean
lemma kineticEnergy_eq (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.kineticEnergy θ = fun t => (1 / (2 : ℝ)) * S.inertia * ⟪∂ₜ θ t, ∂ₜ θ t⟫_ℝ
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy_eq`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L299).

> The potential energy of the simple pendulum, written out.

```lean
lemma potentialEnergy_eq (x : EuclideanSpace ℝ (Fin 1)) :
    S.potentialEnergy x = S.m * S.g * S.ℓ * (1 - Real.cos (x 0))
```

**`ClassicalMechanics.SimplePendulum.energy_eq`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L303).

> The energy of the simple pendulum, written out.

```lean
lemma energy_eq (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.energy θ = fun t => S.kineticEnergy θ t + S.potentialEnergy (θ t)
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy_nonneg`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L308).

> The potential energy of the simple pendulum is non-negative, the bottom of the swing being
> the lowest point of the circle on which the bob moves.

```lean
lemma potentialEnergy_nonneg (x : EuclideanSpace ℝ (Fin 1)) : 0 ≤ S.potentialEnergy x
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy_le`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L318).

> The potential energy of the simple pendulum is at most `2 m g ℓ`, its value at the top of the
> swing.

```lean
lemma potentialEnergy_le (x : EuclideanSpace ℝ (Fin 1)) :
    S.potentialEnergy x ≤ 2 * (S.m * S.g * S.ℓ)
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy_eq_zero_iff`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L330).

> The potential energy of the simple pendulum vanishes exactly when the cosine of the angle is
> equal to `1`, that is exactly at the bottom of the swing.

```lean
lemma potentialEnergy_eq_zero_iff (x : EuclideanSpace ℝ (Fin 1)) :
    S.potentialEnergy x = 0 ↔ Real.cos (x 0) = 1
```

### C.3. Smoothness of the energies and the gradient of the potential

> The potential energy is a smooth function of the angle, and its gradient on the one-dimensional
> Euclidean lift is `m g ℓ sin θ` times the unit vector of the angular coordinate. This gradient is
> what the equation of motion balances against the angular acceleration, so we record it here, once.
> The subsection also records that, along a smooth lift of the angle, each of the three energies is
> a differentiable function of the time — differentiability in time along the lift, as distinct
> from the differentiability in the angle of the potential energy — which is the differentiability
> that the time derivatives of section C.4 consume.

**`ClassicalMechanics.SimplePendulum.potentialEnergy_contDiff`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L351).

> The potential energy of the simple pendulum is a smooth function of the angle.

```lean
lemma potentialEnergy_contDiff (n : WithTop ℕ∞) : ContDiff ℝ n S.potentialEnergy
```

**`ClassicalMechanics.SimplePendulum.differentiable_potentialEnergy`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L359).

> The potential energy of the simple pendulum is a differentiable function of the angle. This
> is differentiability in the angle; for differentiability in time along a smooth lift of the
> angle see `potentialEnergy_differentiable`.

```lean
lemma differentiable_potentialEnergy : Differentiable ℝ S.potentialEnergy
```

**`ClassicalMechanics.SimplePendulum.gradient_potentialEnergy`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L364).

> The gradient of the potential energy of the simple pendulum is `m g ℓ sin θ` times the unit
> vector of the angular coordinate.

```lean
lemma gradient_potentialEnergy (x : EuclideanSpace ℝ (Fin 1)) :
    gradient S.potentialEnergy x =
      (S.m * S.g * S.ℓ * Real.sin (x 0)) • EuclideanSpace.single 0 1
```

**`ClassicalMechanics.SimplePendulum.kineticEnergy_differentiable`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L380).

> Along a smooth lift of the angle the kinetic energy is differentiable in time.

```lean
lemma kineticEnergy_differentiable (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ) :
    Differentiable ℝ (S.kineticEnergy θ)
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy_differentiable`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L389).

> Along a smooth lift of the angle the potential energy is a differentiable function of the
> time. This is differentiability in time along the lift; for differentiability in the angle see
> `differentiable_potentialEnergy`.

```lean
lemma potentialEnergy_differentiable (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ) :
    Differentiable ℝ (fun t => S.potentialEnergy (θ t))
```

**`ClassicalMechanics.SimplePendulum.energy_differentiable`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L396).

> Along a smooth lift of the angle the energy is differentiable in time.

```lean
lemma energy_differentiable (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ) :
    Differentiable ℝ (S.energy θ)
```

### C.4. Time derivatives of the energies

> For a general smooth lift of the angle, which need not satisfy the equation of motion, we can
> compute the time derivatives of the energies. Each is an inner product against the angular
> velocity: the equation of motion will be exactly the statement that the two contributions cancel.

**`ClassicalMechanics.SimplePendulum.kineticEnergy_deriv`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L413).

> The rate of change of the kinetic energy is the angular velocity paired with the angular
> momentum's rate of change, `I θ̈`.

```lean
lemma kineticEnergy_deriv (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ) :
    ∂ₜ (S.kineticEnergy θ) = fun t => ⟪∂ₜ θ t, S.inertia • ∂ₜ (∂ₜ θ) t⟫_ℝ
```

**`ClassicalMechanics.SimplePendulum.potentialEnergy_deriv`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L426).

> The rate of change of the potential energy is the angular velocity paired with the gradient
> of the potential.

```lean
lemma potentialEnergy_deriv (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ) :
    ∂ₜ (fun t => S.potentialEnergy (θ t)) =
      fun t => ⟪∂ₜ θ t, gradient S.potentialEnergy (θ t)⟫_ℝ
```

**`ClassicalMechanics.SimplePendulum.energy_deriv`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L440).

> The rate of change of the energy is the angular velocity paired with the sum of `I θ̈` and
> the gradient of the potential; the equation of motion is exactly the vanishing of that sum.

```lean
lemma energy_deriv (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ) :
    ∂ₜ (S.energy θ) =
      fun t => ⟪∂ₜ θ t, S.inertia • ∂ₜ (∂ₜ θ) t + gradient S.potentialEnergy (θ t)⟫_ℝ
```

## D. The Lagrangian

> The pendulum is a conservative system, so its Lagrangian is the kinetic energy minus the potential
> energy, `L = ½ I θ̇² - m g ℓ (1 - cos θ)`. As for the harmonic oscillator, it is defined as a
> function on phase space, of the time, the angle and the angular velocity separately; that it is
> `T - V` along a lift of the angle is then a lemma rather than the definition.
>
> The Lagrangian carries no explicit time dependence, the pendulum being autonomous; the time
> argument is kept because it is the type the Euler–Lagrange operator of Physlib expects.

### D.1. The definition of the Lagrangian and equalities for it

> The Lagrangian is written directly in terms of the moment of inertia and the potential energy,
> so that the equalities below are the two ways of reading it: expanded in the input data, and as
> the kinetic energy minus the potential energy along a lift of the angle.

**`ClassicalMechanics.SimplePendulum.lagrangian`**, a def, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L477).

> The Lagrangian of the simple pendulum, `L(t, θ, θ̇) = ½ I ‖θ̇‖² - V(θ)`, the kinetic energy
> minus the potential energy as a function on phase space. It does not depend on the time.

```lean
noncomputable def lagrangian (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) : ℝ
```

**`ClassicalMechanics.SimplePendulum.lagrangian_eq`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L481).

> The Lagrangian of the simple pendulum, written out in the input data.

```lean
lemma lagrangian_eq :
    S.lagrangian = fun _ x v =>
      (1 / (2 : ℝ)) * S.inertia * ⟪v, v⟫_ℝ - S.m * S.g * S.ℓ * (1 - Real.cos (x 0))
```

**`ClassicalMechanics.SimplePendulum.lagrangian_eq_kineticEnergy_sub_potentialEnergy`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L489).

> Along a lift of the angle the Lagrangian of the simple pendulum is the kinetic energy minus
> the potential energy.

```lean
lemma lagrangian_eq_kineticEnergy_sub_potentialEnergy (t : Time)
    (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.lagrangian t (θ t) (∂ₜ θ t) = S.kineticEnergy θ t - S.potentialEnergy (θ t)
```

### D.2. Smoothness of the Lagrangian

> The Lagrangian is a smooth function of all of its arguments jointly. This is the hypothesis that
> the Euler–Lagrange theorem of Physlib places on a Lagrangian, so it is recorded on the uncurried
> form `↿S.lagrangian`.

**`ClassicalMechanics.SimplePendulum.contDiff_lagrangian`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L506).

> The Lagrangian of the simple pendulum is a smooth function of the time, the angle and the
> angular velocity jointly.

```lean
lemma contDiff_lagrangian (n : WithTop ℕ∞) : ContDiff ℝ n ↿S.lagrangian
```

### D.3. Gradients of the Lagrangian

> The Euler–Lagrange operator is built from the two partial gradients of the Lagrangian. The
> gradient in the angle is minus the gradient of the potential energy, that is the torque of
> section E; the gradient in the angular velocity is the angular momentum `I θ̇`.

**`ClassicalMechanics.SimplePendulum.gradient_lagrangian_position_eq`**, a lemma, [line 522](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L522).

> The gradient of the Lagrangian of the simple pendulum in the angle is minus the gradient of
> the potential energy, `-m g ℓ sin θ` times the unit vector of the angular coordinate.

```lean
lemma gradient_lagrangian_position_eq (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) :
    gradient (fun x => S.lagrangian t x v) x =
      -((S.m * S.g * S.ℓ * Real.sin (x 0)) • EuclideanSpace.single 0 1)
```

**`ClassicalMechanics.SimplePendulum.gradient_lagrangian_velocity_eq`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L536).

> The gradient of the Lagrangian of the simple pendulum in the angular velocity is the angular
> momentum `I θ̇` about the pivot.

```lean
lemma gradient_lagrangian_velocity_eq (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) :
    gradient (S.lagrangian t x) v = S.inertia • v
```

## E. The torque and the equation of motion

> Gravity exerts on the bob a torque `-m g ℓ sin θ` about the pivot, the generalized force conjugate
> to the angle, and the equation of motion balances it against the rate of change `I θ̈` of the
> angular momentum.
>
> We take that pointwise relation as the definition of the equation of motion, rather than the
> vanishing of the variational derivative of the action, which is how the harmonic oscillator defines
> its own. The reason is that the variational derivative is defined to be `0` whenever no variational
> gradient exists, so its vanishing holds vacuously for every lift of the angle too rough to admit
> one; it says what it is meant to say only under a smoothness assumption. The pointwise equation is
> totalized too — `∂ₜ` is `fderiv`, which is `0` off differentiability — but its totalization cannot
> make the equation vacuously true: both sides remain genuine, and generally unequal, functions of
> time. A rough lift can still satisfy the equation accidentally — a discontinuous lift hopping
> between equilibrium angles solves it, as section E.3 explains — which is why the notion of a
> solution, `IsSolution`, demands smoothness as well. It is also the form in which the equation of
> motion is solved and used. The two agree for smooth lifts, by
> `equationOfMotion_iff_gradLagrangian_zero` of section G, which is one rearrangement away from
> `gradLagrangian_eq_torque` of section F.

### E.1. The torque

> The pendulum is conservative, so the generalized force conjugate to the angle is minus the
> gradient of the potential energy. It is a torque about the pivot rather than a force, the angle
> being the coordinate; this is why it is `m g ℓ sin θ` and not `m g sin θ`.

**`ClassicalMechanics.SimplePendulum.torque`**, a def, [line 582](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L582).

> The generalized force of the simple pendulum conjugate to the angle, that is the torque about
> the pivot, is minus the gradient of the potential energy, `τ = -∂V/∂θ`.

```lean
noncomputable def torque (x : EuclideanSpace ℝ (Fin 1)) : EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.SimplePendulum.torque_eq`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L588).

> The torque of the simple pendulum is `-m g ℓ sin θ` times the unit vector of the angular
> coordinate. It is restoring near the bottom of the swing: for `|θ| < π` it opposes the
> displacement, and it vanishes both at the bottom and at the inverted position.

```lean
lemma torque_eq (x : EuclideanSpace ℝ (Fin 1)) :
    S.torque x = -((S.m * S.g * S.ℓ * Real.sin (x 0)) • EuclideanSpace.single 0 1)
```

**`ClassicalMechanics.SimplePendulum.torque_apply`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L593).

> The single component of the torque of the simple pendulum is `-m g ℓ sin θ`.

```lean
lemma torque_apply (x : EuclideanSpace ℝ (Fin 1)) :
    S.torque x 0 = -(S.m * S.g * S.ℓ * Real.sin (x 0))
```

### E.2. The equation of motion

> The equation of motion of the simple pendulum equates the rate of change of the angular momentum
> about the pivot with the torque of gravity, at every instant.

**`ClassicalMechanics.SimplePendulum.EquationOfMotion`**, a def, [line 613](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L613).

> The equation of motion of the simple pendulum: at every instant the rate of change `I θ̈` of
> the angular momentum about the pivot equals the torque `τ(θ)` of gravity.
>
> This pointwise relation, and not the vanishing of the variational derivative of the action, is
> the definition of the equation of motion here; see the discussion in section E. For a smooth
> lift of the angle the two agree, by `equationOfMotion_iff_gradLagrangian_zero` of section G.

```lean
def EquationOfMotion (θ : Time → EuclideanSpace ℝ (Fin 1)) : Prop
```

**`ClassicalMechanics.SimplePendulum.equationOfMotion_iff_newtons_2nd_law`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L621).

> The equation of motion of the simple pendulum with all of its terms on one side: at every
> instant the rate of change `I θ̈` of the angular momentum plus the gradient of the potential
> energy vanishes. This is the rotational form of Newton's second law, in the shape in which
> `DampedHarmonicOscillator` states its own; the sum on the left is exactly the combination that
> `energy_deriv` pairs with the velocity `∂ₜ θ`.

```lean
lemma equationOfMotion_iff_newtons_2nd_law (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.EquationOfMotion θ ↔
      ∀ t, S.inertia • ∂ₜ (∂ₜ θ) t + gradient S.potentialEnergy (θ t) = 0
```

### E.3. Smooth solutions

> A solution of the pendulum is a smooth lift satisfying the equation of motion. Smoothness is part
> of the definition because the bare pointwise equation, being totalized, admits unphysical
> solutions: a lift jumping between the equilibrium angles `0` and `π` has zero torque everywhere,
> and — being locally constant wherever it is differentiable at all — it has `∂ₜ θ`, and hence
> `∂ₜ (∂ₜ θ)`, identically zero, so it satisfies the equation even when it is nowhere continuous.
> Demanding smoothness excludes such junk, and is the regularity under which the variational
> description of the motion agrees with the pointwise one.

**`ClassicalMechanics.SimplePendulum.IsSolution`**, a def, [line 642](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L642).

> A solution of the simple pendulum is a smooth lift of the angle satisfying the equation of
> motion.

```lean
def IsSolution (θ : Time → EuclideanSpace ℝ (Fin 1)) : Prop
```

**`ClassicalMechanics.SimplePendulum.IsSolution.contDiff`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L646).

> A solution of the simple pendulum is smooth.

```lean
lemma IsSolution.contDiff {S : SimplePendulum} {θ : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution θ) : ContDiff ℝ ∞ θ
```

**`ClassicalMechanics.SimplePendulum.IsSolution.equationOfMotion`**, a lemma, [line 650](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L650).

> A solution of the simple pendulum satisfies the equation of motion.

```lean
lemma IsSolution.equationOfMotion {S : SimplePendulum} {θ : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution θ) : S.EquationOfMotion θ
```

### E.4. The scalar equation and independence of the mass

> The angle is a single number, so the vector equation of motion is equivalent to the scalar
> equation obtained by reading off its one component. Dividing that component by the moment of
> inertia, using `ω_sq_mul_inertia`, cancels the mass and leaves `θ̈ + ω² sin θ = 0`: two pendulums
> with the same `ω = √(g/ℓ)` have exactly the same angular motions, whatever their masses.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_iff_scalar`**, a lemma, [line 666](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L666).

> The equation of motion of the simple pendulum in scalar form, `θ̈ + ω² sin θ = 0`. The mass
> has cancelled: only the angular frequency `ω = √(g/ℓ)` survives.

```lean
lemma equationOfMotion_iff_scalar (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.EquationOfMotion θ ↔ ∀ t, ∂ₜ (∂ₜ θ) t 0 + S.ω ^ 2 * Real.sin (θ t 0) = 0
```

**`ClassicalMechanics.SimplePendulum.equationOfMotion_iff_of_eq_ω`**, a lemma, [line 693](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L693).

> Two simple pendulums with the same angular frequency have the same angular equation of
> motion, and hence the same angular motions; in particular, changing only the mass does not
> affect the angular motion. An equal `ω` still permits different lengths, and so different
> trajectories of the bob in space.

```lean
lemma equationOfMotion_iff_of_eq_ω (S' : SimplePendulum) (h : S'.ω = S.ω)
    (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S'.EquationOfMotion θ ↔ S.EquationOfMotion θ
```

## F. The variational derivative of the action

> The action of the simple pendulum is the time integral of the Lagrangian along a lift of the
> angle. Its variational derivative is computed here, in two steps: it is the Euler–Lagrange
> operator of the Lagrangian, and that operator is the torque minus the rate of change of the
> angular momentum.

### F.1. The definition of the variational derivative

> The variational derivative is that of Physlib's variational calculus, applied to the action of the
> pendulum. Recall that it is defined to be `0` when no variational gradient exists, so the lemmas
> below are stated for smooth lifts of the angle.

**`ClassicalMechanics.SimplePendulum.gradLagrangian`**, a def, [line 721](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L721).

> The variational derivative of the action of the simple pendulum, the action being the time
> integral of the Lagrangian along a lift of the angle.

```lean
noncomputable def gradLagrangian (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    Time → EuclideanSpace ℝ (Fin 1)
```

### F.2. Equality with the Euler–Lagrange operator

> For a smooth lift of the angle the variational derivative of the action is the Euler–Lagrange
> operator of the Lagrangian, by the general theorem `euler_lagrange_varGradient`; the hypotheses
> of that theorem are the smoothness of the lift and `contDiff_lagrangian`.

**`ClassicalMechanics.SimplePendulum.gradLagrangian_eq_eulerLagrangeOp`**, a lemma, [line 737](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L737).

> For a smooth lift of the angle the variational derivative of the action of the simple
> pendulum is the Euler–Lagrange operator of its Lagrangian.

```lean
lemma gradLagrangian_eq_eulerLagrangeOp (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) :
    S.gradLagrangian θ = eulerLagrangeOp S.lagrangian θ
```

### F.3. The variational derivative in terms of the torque

> Evaluating the Euler–Lagrange operator with the gradients of section D.3 gives the variational
> derivative as the torque minus the rate of change of the angular momentum. Its vanishing is
> therefore the equation of motion of section E; that equivalence is
> `equationOfMotion_iff_gradLagrangian_zero` of section G.

**`ClassicalMechanics.SimplePendulum.gradLagrangian_eq_torque`**, a lemma, [line 755](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L755).

> For a smooth lift of the angle the variational derivative of the action of the simple
> pendulum is the torque minus the rate of change `I θ̈` of the angular momentum.

```lean
lemma gradLagrangian_eq_torque (θ : Time → EuclideanSpace ℝ (Fin 1)) (hθ : ContDiff ℝ ∞ θ) :
    S.gradLagrangian θ = fun t => S.torque (θ t) - S.inertia • ∂ₜ (∂ₜ θ) t
```

## G. Equation of motion and the variational principle

> Section E took the pointwise balance of the angular momentum's rate of change against the torque
> as the definition of the equation of motion, and section F computed the variational derivative of
> the action. This section proves that for smooth lifts of the angle the two agree: the pointwise
> law is exactly the Euler–Lagrange equation of the action, the statement that the motion is a
> critical point of the action. The equivalence holds only under smoothness — the variational
> derivative is `0` by convention on lifts too rough to admit a variational gradient, so on such
> lifts its vanishing says nothing — which is why section E took the pointwise form as primary.

### G.1. Equivalence with the vanishing of the variational derivative

> By `gradLagrangian_eq_torque` the variational derivative of the action along a smooth lift is
> the torque minus the rate of change of the angular momentum, so its vanishing is a rearrangement
> of the equation of motion.

**`ClassicalMechanics.SimplePendulum.equationOfMotion_iff_gradLagrangian_zero`**, a lemma, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L789).

> For a smooth lift of the angle the equation of motion of the simple pendulum holds if and
> only if the variational derivative of the action vanishes: the smooth motions of the pendulum
> are the critical points of its action.

```lean
lemma equationOfMotion_iff_gradLagrangian_zero (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) :
    S.EquationOfMotion θ ↔ S.gradLagrangian θ = 0
```

### G.2. The variational characterization of solutions

> A solution was defined in section E.3 as a smooth lift satisfying the equation of motion.
> Substituting the equivalence of G.1 for the equation of motion turns this into the variational
> characterization: the solutions of the pendulum are exactly the smooth lifts of the angle along
> which the variational derivative of the action vanishes.

**`ClassicalMechanics.SimplePendulum.isSolution_iff`**, a lemma, [line 809](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L809).

> A lift of the angle is a solution of the simple pendulum if and only if it is smooth and the
> variational derivative of the action vanishes along it.

```lean
lemma isSolution_iff (θ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.IsSolution θ ↔ ContDiff ℝ ∞ θ ∧ S.gradLagrangian θ = 0
```

## H. Energy conservation

> The pendulum is conservative: along any smooth lift of the angle satisfying the equation of
> motion the energy is constant. No computation remains to be done here: by `energy_deriv` the
> rate of change of the energy is the angular velocity paired with the sum of `I θ̈` and the
> gradient of the potential, and the equation of motion is exactly the vanishing of that sum.

### H.1. Energy conservation in terms of time derivatives

> The first form of energy conservation: the time derivative of the energy vanishes identically
> along any smooth lift of the angle satisfying the equation of motion.

**`ClassicalMechanics.SimplePendulum.energy_conservation_of_equationOfMotion`**, a lemma, [line 835](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L835).

> Along a smooth lift of the angle satisfying the equation of motion the time derivative of
> the energy of the simple pendulum vanishes.

```lean
lemma energy_conservation_of_equationOfMotion (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) (h : S.EquationOfMotion θ) : ∂ₜ (S.energy θ) = 0
```

### H.2. Energy conservation in terms of constant energy

> The second form: the energy is differentiable in time along a smooth lift of the angle, so the
> vanishing of its derivative makes it a constant function of the time, equal to its initial
> value.

**`ClassicalMechanics.SimplePendulum.energy_conservation_of_equationOfMotion'`**, a lemma, [line 854](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L854).

> Along a smooth lift of the angle satisfying the equation of motion the energy of the simple
> pendulum at any time is equal to its initial value.

```lean
lemma energy_conservation_of_equationOfMotion' (θ : Time → EuclideanSpace ℝ (Fin 1))
    (hθ : ContDiff ℝ ∞ θ) (h : S.EquationOfMotion θ) (t : Time) :
    S.energy θ t = S.energy θ 0
```

### H.3. Energy conservation for solutions

> The hypotheses of energy conservation — smoothness and the equation of motion — are exactly the
> two components of being a solution, so for solutions conservation takes its most compact form.

**`ClassicalMechanics.SimplePendulum.IsSolution.energy_eq`**, a lemma, [line 875](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean#L875).

> The energy of the simple pendulum along a solution at any time is equal to its initial
> value.

```lean
lemma IsSolution.energy_eq {S : SimplePendulum} {θ : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution θ) (t : Time) : S.energy θ t = S.energy θ 0
```

## Depends on

- [A. Euler–Lagrange equations](../../eulerlagrange.md)

## Proof depends on

- [The Classical Harmonic Oscillator](../../harmonicoscillator/basic.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Basic.lean)
