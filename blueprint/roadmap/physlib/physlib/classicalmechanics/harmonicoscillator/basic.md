---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator, ClassicalMechanics.HarmonicOscillator.k_ne_zero, ClassicalMechanics.HarmonicOscillator.m_ne_zero, ClassicalMechanics.HarmonicOscillator.ω, ClassicalMechanics.HarmonicOscillator.ω_pos, ClassicalMechanics.HarmonicOscillator.ω_sq, ClassicalMechanics.HarmonicOscillator.ω_ne_zero, ClassicalMechanics.HarmonicOscillator.inverse_ω_sq
statement: formalized
proof: formalized
---

# The Classical Harmonic Oscillator

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Basic`, [Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean): 51 declarations, 22 with a docstring.

## i. Overview

> The classical harmonic oscillator is a classical mechanical system corresponding to a
> mass `m` under a force `- k x` where `k` is the spring constant and `x` is the position.
>
> In this file, a coordinate system is assumed where position and velocity both have type
> `EuclideanSpace ℝ (Fin 1)`. This is a simpler model often used for pedagogical purpose,
> but only works because both the configuration space (position) and its tangent space (velocity)
> are isomorphic to Euclidean Space. A proper formalisation should include the geometric properties
> of the state space via manifolds and tangent bundles.

## ii. Key results

> The key results in the study of the classical harmonic oscillator are the follows:
>
> In the `Basic` module:
> - `HarmonicOscillator` contains the input data to the problem.
> - `EquationOfMotion` defines the equation of motion for the harmonic oscillator.
> - `energy_conservation_of_equationOfMotion` proves that a trajectory satisfying the
>   equation of motion conserves energy.
> - `equationOfMotion_tfae` proves that the equation of motion of motion is equivalent to
>   - Newton's second law,
>   - Hamilton's equations,
>   - the variational principal for the action,
>   - the Hamilton variation principal.
>
> In the `Solution` module:
> - `InitialConditions` is a structure for the initial conditions for the harmonic oscillator.
> - `trajectories` is the trajectories to the harmonic oscillator for given initial conditions.
> - `trajectories_equationOfMotion` proves that the solution satisfies the equation of motion.

## iv. References

> References for the classical harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 58, section 21. [ref: landau\_mechanics]
>
> …
>
> * https://web.williams.edu/Mathematics/it3/texts/var\_noether.pdf.
>   [ref: terek\_variational\_manifolds]

## A. The input data

> We start by defining a structure containing the input data of the harmonic oscillator, and
> proving basic properties thereof. The input data consists of the mass `m`
> of the particle and the spring constant `k`.

**`ClassicalMechanics.HarmonicOscillator`**, a structure, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L122).

> The classical harmonic oscillator is specified by a mass `m`, and a spring constant `k`.
> Both the mass and the string constant are assumed to be positive.

```lean
structure HarmonicOscillator where
  /-- The mass of the harmonic Oscillator. -/
  m : ℝ
  /-- The spring constant of the harmonic oscillator. -/
  k : ℝ
  m_pos : 0 < m
  k_pos : 0 < k
```

**`ClassicalMechanics.HarmonicOscillator.k_ne_zero`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L135).

```lean
lemma k_ne_zero : S.k ≠ 0
```

**`ClassicalMechanics.HarmonicOscillator.m_ne_zero`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L138).

```lean
lemma m_ne_zero : S.m ≠ 0
```

## B. The angular frequency

> From the input data, it is possible to define the angular frequency `ω` of the harmonic oscillator,
> as `√(k/m)`.
>
> The angular frequency appears in the solutions to the equations of motion of the harmonic
> oscillator.
>
> Here we both define and prove properties related to the angular frequency.

**`ClassicalMechanics.HarmonicOscillator.ω`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L156).

> The angular frequency of the classical harmonic oscillator, `ω`, is defined
> as `√(k/m)`.

```lean
noncomputable def ω : ℝ
```

**`ClassicalMechanics.HarmonicOscillator.ω_pos`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L160).

> The angular frequency of the classical harmonic oscillator is positive.

```lean
lemma ω_pos : 0 < S.ω
```

**`ClassicalMechanics.HarmonicOscillator.ω_sq`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L163).

> The square of the angular frequency of the classical harmonic oscillator is equal to `k/m`.

```lean
lemma ω_sq : S.ω^2 = S.k / S.m
```

**`ClassicalMechanics.HarmonicOscillator.ω_ne_zero`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L166).

> The angular frequency of the classical harmonic oscillator is not equal to zero.

```lean
lemma ω_ne_zero : S.ω ≠ 0
```

**`ClassicalMechanics.HarmonicOscillator.inverse_ω_sq`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L170).

> The inverse of the square of the angular frequency of the classical harmonic oscillator
> is `m/k`.

```lean
lemma inverse_ω_sq : (S.ω ^ 2)⁻¹ = S.m/S.k
```

## C. The energies

> The harmonic oscillator has a kinetic energy determined by it's velocity and
> a potential energy determined by it's position.
> These combine to give the total energy of the harmonic oscillator.
>
> Here we state and prove a number of properties of these energies.

### C.1. The definitions of the energies

> We define the three energies, it is these energies which will control the dynamics
> of the harmonic oscillator, through the lagrangian.

**`ClassicalMechanics.HarmonicOscillator.kineticEnergy`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L196).

> The kinetic energy of the harmonic oscillator is $\frac{1}{2} m ‖\dot x‖^2$.

```lean
noncomputable def kineticEnergy (xₜ : Time → EuclideanSpace ℝ (Fin 1)) : Time → ℝ
```

**`ClassicalMechanics.HarmonicOscillator.potentialEnergy`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L200).

> The potential energy of the harmonic oscillator is `1/2 k x ^ 2`

```lean
noncomputable def potentialEnergy (x : EuclideanSpace ℝ (Fin 1)) : ℝ
```

**`ClassicalMechanics.HarmonicOscillator.energy`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L204).

> The energy of the harmonic oscillator is the kinetic energy plus the potential energy.

```lean
noncomputable def energy (xₜ : Time → EuclideanSpace ℝ (Fin 1)) : Time → ℝ
```

### C.2. Simple equalities for the energies

**`ClassicalMechanics.HarmonicOscillator.kineticEnergy_eq`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L213).

```lean
lemma kineticEnergy_eq (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    kineticEnergy S xₜ = fun t => (1 / (2 : ℝ)) * S.m * ⟪∂ₜ xₜ t, ∂ₜ xₜ t⟫_ℝ
```

**`ClassicalMechanics.HarmonicOscillator.potentialEnergy_eq`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L216).

```lean
lemma potentialEnergy_eq (x : EuclideanSpace ℝ (Fin 1)) :
    potentialEnergy S x = (1 / (2 : ℝ)) • S.k • ⟪x, x⟫_ℝ
```

**`ClassicalMechanics.HarmonicOscillator.energy_eq`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L219).

```lean
lemma energy_eq (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    energy S xₜ = fun t => kineticEnergy S xₜ t + potentialEnergy S (xₜ t)
```

**`ClassicalMechanics.HarmonicOscillator.energy_eq_norm_sq`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L224).

> Mechanical energy is the mass-weighted velocity square plus the spring-weighted
> position square, divided by two.

```lean
lemma energy_eq_norm_sq (x : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.energy x t = (S.m * ‖∂ₜ x t‖ ^ 2 + S.k * ‖x t‖ ^ 2) / 2
```

**`ClassicalMechanics.HarmonicOscillator.energy_nonneg`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L231).

> Mechanical energy is nonnegative for every trajectory.

```lean
lemma energy_nonneg (x : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    0 ≤ S.energy x t
```

**`ClassicalMechanics.HarmonicOscillator.position_sq_le_energy`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L238).

> Potential energy controls the square of the displacement.

```lean
lemma position_sq_le_energy (x : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.k * ‖x t‖ ^ 2 ≤ 2 * S.energy x t
```

**`ClassicalMechanics.HarmonicOscillator.velocity_sq_le_energy`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L244).

> Kinetic energy controls the square of the velocity.

```lean
lemma velocity_sq_le_energy (x : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    S.m * ‖∂ₜ x t‖ ^ 2 ≤ 2 * S.energy x t
```

### C.3. Differentiability of the energies

> On smooth trajectories the energies are differentiable.

**`ClassicalMechanics.HarmonicOscillator.kineticEnergy_differentiable`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L257).

```lean
lemma kineticEnergy_differentiable (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    Differentiable ℝ (kineticEnergy S xₜ)
```

**`ClassicalMechanics.HarmonicOscillator.potentialEnergy_differentiable`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L263).

```lean
lemma potentialEnergy_differentiable (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    Differentiable ℝ (fun t => potentialEnergy S (xₜ t))
```

**`ClassicalMechanics.HarmonicOscillator.energy_differentiable`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L270).

```lean
lemma energy_differentiable (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    Differentiable ℝ (energy S xₜ)
```

### C.4. Time derivatives of the energies

> For a general smooth trajectory (which may not satisfy the equations of motion) we can compute
> the time derivatives of the energies.

**`ClassicalMechanics.HarmonicOscillator.kineticEnergy_deriv`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L284).

```lean
lemma kineticEnergy_deriv (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    ∂ₜ (kineticEnergy S xₜ) = fun t => ⟪∂ₜ xₜ t, S.m • ∂ₜ (∂ₜ xₜ) t⟫_ℝ
```

**`ClassicalMechanics.HarmonicOscillator.potentialEnergy_deriv`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L295).

```lean
lemma potentialEnergy_deriv (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    ∂ₜ (fun t => potentialEnergy S (xₜ t)) = fun t => ⟪∂ₜ xₜ t, S.k • xₜ t⟫_ℝ
```

**`ClassicalMechanics.HarmonicOscillator.energy_deriv`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L305).

```lean
lemma energy_deriv (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    ∂ₜ (energy S xₜ) = fun t => ⟪∂ₜ xₜ t, S.m • ∂ₜ (∂ₜ xₜ) t + S.k • xₜ t⟫_ℝ
```

## D. Lagrangian and the equation of motion

> We state the lagrangian, and derive from that the equation of motion for the harmonic oscillator.

### D.1. The Lagrangian

> We define the lagrangian of the harmonic oscillator, as a function of phase-space. It is given by
>
> $$L(t, x, v) := \frac{1}{2} m ‖v‖^2 - \frac{1}{2} k ‖x‖^2$$
>
> In theory this definition is the kinetic energy minus the potential energy, however
> to make the lagrangian a function on phase-space we reserve this result for a lemma.

**`ClassicalMechanics.HarmonicOscillator.lagrangian`**, a def, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L336).

> The lagrangian of the harmonic oscillator is the kinetic energy minus the potential energy.

```lean
noncomputable def lagrangian (t : Time) (x : EuclideanSpace ℝ (Fin 1))
    (v : EuclideanSpace ℝ (Fin 1)) : ℝ
```

#### D.1.1. Equalities for the lagrangian

> Equalities for the lagrangian. We prove some simple equalities for the lagrangian,
> in particular that when applied to a trajectory it is the kinetic energy minus the potential energy.

**`ClassicalMechanics.HarmonicOscillator.lagrangian_eq`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L351).

```lean
lemma lagrangian_eq : lagrangian S = fun t x v =>
    1 / (2 : ℝ) * S.m * ⟪v, v⟫_ℝ - 1 / (2 : ℝ) * S.k * ⟪x, x⟫_ℝ
```

**`ClassicalMechanics.HarmonicOscillator.lagrangian_eq_kineticEnergy_sub_potentialEnergy`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L356).

```lean
lemma lagrangian_eq_kineticEnergy_sub_potentialEnergy (t : Time)
    (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    lagrangian S t (xₜ t) (∂ₜ xₜ t) = kineticEnergy S xₜ t - potentialEnergy S (xₜ t)
```

#### D.1.2. Smoothness of the lagrangian

> The lagrangian is smooth in all its arguments.

**`ClassicalMechanics.HarmonicOscillator.contDiff_lagrangian`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L370).

```lean
lemma contDiff_lagrangian (n : WithTop ℕ∞) : ContDiff ℝ n ↿S.lagrangian
```

#### D.1.3. Gradients of the lagrangian

> We now show results related to the gradients of the lagrangian with respect to the
> position and velocity.

**`ClassicalMechanics.HarmonicOscillator.gradient_lagrangian_position_eq`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L383).

```lean
lemma gradient_lagrangian_position_eq (t : Time) (x : EuclideanSpace ℝ (Fin 1))
    (v : EuclideanSpace ℝ (Fin 1)) :
    gradient (fun x => lagrangian S t x v) x = - S.k • x
```

**`ClassicalMechanics.HarmonicOscillator.gradient_lagrangian_velocity_eq`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L392).

```lean
lemma gradient_lagrangian_velocity_eq (t : Time) (x : EuclideanSpace ℝ (Fin 1))
    (v : EuclideanSpace ℝ (Fin 1)) :
    gradient (lagrangian S t x) v = S.m • v
```

### D.2. The variational derivative of the action

> We now write down the variational derivative for the harmonic oscillator, for
> a trajectory $x(t)$ this is equal to
>
> $$t\mapsto \left.\frac{\partial L(t, \dot x (t), q)}{\partial q}\right|_{q = x(t)} -
>   \frac{d}{dt} \left.\frac{\partial L(t, v, x(t))}{\partial v}\right|_{v = \dot x (t)}$$
>
> Setting this equal to zero corresponds to the Euler-Lagrange equations, and thereby the
> equation of motion.

**`ClassicalMechanics.HarmonicOscillator.gradLagrangian`**, a def, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L418).

> The Euler-Lagrange operator for the classical harmonic oscillator.

```lean
noncomputable def gradLagrangian (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    Time → EuclideanSpace ℝ (Fin 1)
```

#### D.2.1. Equality for the variational derivative

> Basic equalities for the variational derivative of the action.

**`ClassicalMechanics.HarmonicOscillator.gradLagrangian_eq_eulerLagrangeOp`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L430).

```lean
lemma gradLagrangian_eq_eulerLagrangeOp (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hq : ContDiff ℝ ∞ xₜ) :
    gradLagrangian S xₜ = eulerLagrangeOp S.lagrangian xₜ
```

### D.3. The equation of motion

> The equation of motion for the harmonic oscillator is given by setting the
> variational derivative of the action equal to zero.

**`ClassicalMechanics.HarmonicOscillator.EquationOfMotion`**, a def, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L445).

> The equation of motion for the Harmonic oscillator.

```lean
def EquationOfMotion (xₜ : Time → EuclideanSpace ℝ (Fin 1)) : Prop
```

#### D.3.1. Equation of motion if and only if variational-gradient of Lagrangian is zero

> We write a simple iff statement for the definition of the equation of motions.

**`ClassicalMechanics.HarmonicOscillator.equationOfMotion_iff_gradLagrangian_zero`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L456).

```lean
lemma equationOfMotion_iff_gradLagrangian_zero (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.EquationOfMotion xₜ ↔ S.gradLagrangian xₜ = 0
```

## E. Newton's second law

> We define the force of the harmonic oscillator, and show that the equation of
> motion is equivalent to Newton's second law.

### E.1. The force

> We define the force of the harmonic oscillator as the negative gradient of the potential energy,
> and show that this is equal to `- k x`.

**`ClassicalMechanics.HarmonicOscillator.force`**, a def, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L479).

> The force of the classical harmonic oscillator defined as `- dU(x)/dx` where `U(x)`
> is the potential energy.

```lean
noncomputable def force (S : HarmonicOscillator) (x : EuclideanSpace ℝ (Fin 1)) :
    EuclideanSpace ℝ (Fin 1)
```

#### E.1.1. The force is equal to `- k x`

> We now show that the force is equal to `- k x`.

**`ClassicalMechanics.HarmonicOscillator.force_eq_linear`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L492).

> The force on the classical harmonic oscillator is `- k x`.

```lean
lemma force_eq_linear (x : EuclideanSpace ℝ (Fin 1)) : force S x = - S.k • x
```

### E.2. Variational derivative of lagrangian and force

> We relate the variational derivative of lagrangian to the force, and show the relation
> to Newton's second law.

**`ClassicalMechanics.HarmonicOscillator.gradLagrangian_eq_force`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L511).

> The Euler lagrange operator corresponds to Newton's second law.

```lean
lemma gradLagrangian_eq_force (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    S.gradLagrangian xₜ = fun t => force S (xₜ t) - S.m • ∂ₜ (∂ₜ xₜ) t
```

### E.3. Equation of motion if and only if Newton's second law

> We show that the equation of motion is equivalent to Newton's second law.

**`ClassicalMechanics.HarmonicOscillator.equationOfMotion_iff_newtons_2nd_law`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L526).

```lean
lemma equationOfMotion_iff_newtons_2nd_law (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hx : ContDiff ℝ ∞ xₜ) :
    S.EquationOfMotion xₜ ↔
    (∀ t, S.m • ∂ₜ (∂ₜ xₜ) t = force S (xₜ t))
```

## F. Energy conservation

> In this section we show that any trajectory satisfying the equation of motion
> conserves energy. This result simply follows from the definition of the energies,
> and their derivatives, as well as the statement that the equations of motion are equivalent
> to Newton's second law.

### F.1. Energy conservation in terms of time derivatives

> We prove that the time derivative of the energy is zero for any trajectory satisfying
> the equation of motion.

**`ClassicalMechanics.HarmonicOscillator.energy_conservation_of_equationOfMotion`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L554).

```lean
lemma energy_conservation_of_equationOfMotion (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hx : ContDiff ℝ ∞ xₜ)
    (h : S.EquationOfMotion xₜ) : ∂ₜ (S.energy xₜ) = 0
```

### F.2. Energy conservation in terms of constant energy

> We prove that the energy is constant for any trajectory satisfying the equation of motion.

**`ClassicalMechanics.HarmonicOscillator.energy_conservation_of_equationOfMotion'`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L570).

```lean
lemma energy_conservation_of_equationOfMotion' (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hx : ContDiff ℝ ∞ xₜ)
    (h : S.EquationOfMotion xₜ) (t : Time) : S.energy xₜ t = S.energy xₜ 0
```

## G. Hamiltonian formulation

> We now turn to the Hamiltonian formulation of the harmonic oscillator.
> We define the canonical momentum, the Hamiltonian, and show that the equations of
> motion are equivalent to Hamilton's equations.

### G.1. The canonical momentum

> We define the canonical momentum as the gradient of the lagrangian with respect to
> the velocity.

**`ClassicalMechanics.HarmonicOscillator.toCanonicalMomentum`**, a def, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L600).

> The equivalence between velocity and canonical momentum.

```lean
noncomputable def toCanonicalMomentum (t : Time) (x : EuclideanSpace ℝ (Fin 1)) :
    EuclideanSpace ℝ (Fin 1) ≃ₗ[ℝ] EuclideanSpace ℝ (Fin 1)
```

#### G.1.1. Equality for the canonical momentum

> An simple equality for the canonical momentum.

**`ClassicalMechanics.HarmonicOscillator.toCanonicalMomentum_eq`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L622).

```lean
lemma toCanonicalMomentum_eq (t : Time) (x : EuclideanSpace ℝ (Fin 1))
    (v : EuclideanSpace ℝ (Fin 1)) :
    toCanonicalMomentum S t x v = S.m • v
```

### G.2. The Hamiltonian

> The hamiltonian is defined as a function of time, canonical momentum and position, as
> ```
> H = ⟪p, v⟫ - L(t, x, v)
> ```
> where `v` is a function of `p` and `x` through the canonical momentum.

**`ClassicalMechanics.HarmonicOscillator.hamiltonian`**, a def, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L640).

> The hamiltonian as a function of time, momentum and position.

```lean
noncomputable def hamiltonian (t : Time) (p : EuclideanSpace ℝ (Fin 1))
    (x : EuclideanSpace ℝ (Fin 1)) : ℝ
```

#### G.2.1. Equality for the Hamiltonian

> We prove a simple equality for the Hamiltonian, to help in computations.

**`ClassicalMechanics.HarmonicOscillator.hamiltonian_eq`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L652).

```lean
lemma hamiltonian_eq :
    hamiltonian S = fun _ p x => (1 / (2 : ℝ)) * (1 / S.m) * ⟪p, p⟫_ℝ +
      (1 / (2 : ℝ)) * S.k * ⟪x, x⟫_ℝ
```

#### G.2.2. Smoothness of the Hamiltonian

> We show that the Hamiltonian is smooth in all its arguments.

**`ClassicalMechanics.HarmonicOscillator.hamiltonian_contDiff`**, a lemma, [line 670](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L670).

```lean
lemma hamiltonian_contDiff (n : WithTop ℕ∞) : ContDiff ℝ n ↿S.hamiltonian
```

#### G.2.3. Gradients of the Hamiltonian

> We now write down the gradients of the Hamiltonian with respect to the momentum and position.

**`ClassicalMechanics.HarmonicOscillator.gradient_hamiltonian_position_eq`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L682).

```lean
lemma gradient_hamiltonian_position_eq (t : Time) (x : EuclideanSpace ℝ (Fin 1))
    (p : EuclideanSpace ℝ (Fin 1)) :
    gradient (hamiltonian S t p) x = S.k • x
```

**`ClassicalMechanics.HarmonicOscillator.gradient_hamiltonian_momentum_eq`**, a lemma, [line 695](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L695).

```lean
lemma gradient_hamiltonian_momentum_eq (t : Time) (x : EuclideanSpace ℝ (Fin 1))
    (p : EuclideanSpace ℝ (Fin 1)) :
    gradient (hamiltonian S t · x) p = (1 / S.m) • p
```

### G.3. Relation between Hamiltonian and energy

> We show that the Hamiltonian, when evaluated on any trajectory, is equal to the energy.
> This is independent of whether the trajectory satisfies the equations of motion or not.

**`ClassicalMechanics.HarmonicOscillator.hamiltonian_eq_energy`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L716).

```lean
lemma hamiltonian_eq_energy (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    (fun t => hamiltonian S t (toCanonicalMomentum S t (xₜ t) (∂ₜ xₜ t)) (xₜ t)) = energy S xₜ
```

### G.4. Hamilton equation operator

> We define the operator on momentum-position phase-space whose vanishing is equivalent
> to Hamilton's equations.

**`ClassicalMechanics.HarmonicOscillator.hamiltonEqOp`**, a def, [line 735](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L735).

> The operator on the momentum-position phase-space whose vanishing is equivalent to the
> hamilton's equations between the momentum and position.

```lean
noncomputable def hamiltonEqOp (p : Time → EuclideanSpace ℝ (Fin 1))
    (q : Time → EuclideanSpace ℝ (Fin 1))
```

### G.5. Equation of motion if and only if Hamilton's equations

> We show that the equation of motion is equivalent to Hamilton's equations, that is
> to the vanishing of the Hamilton equation operator.

**`ClassicalMechanics.HarmonicOscillator.equationOfMotion_iff_hamiltonEqOp_eq_zero`**, a lemma, [line 748](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L748).

```lean
lemma equationOfMotion_iff_hamiltonEqOp_eq_zero (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hx : ContDiff ℝ ∞ xₜ) : S.EquationOfMotion xₜ ↔
    hamiltonEqOp S (fun t => S.toCanonicalMomentum t (xₜ t) (∂ₜ xₜ t)) xₜ = 0
```

## H. Equivalences between the different formulations of the equations of motion

> We show that the following are equivalent statements for a smooth trajectory `xₜ`:
> - The equation of motion holds. (aka the Euler-Lagrange equations hold.)
> - Newton's second law holds.
> - Hamilton's equations hold.
> - The variational principle for the action holds.
> - The Hamilton variational principle holds.

**`ClassicalMechanics.HarmonicOscillator.equationOfMotion_tfae`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean#L769).

```lean
lemma equationOfMotion_tfae (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    List.TFAE [S.EquationOfMotion xₜ,
      (∀ t, S.m • ∂ₜ (∂ₜ xₜ) t = force S (xₜ t)),
      hamiltonEqOp S (fun t => S.toCanonicalMomentum t (xₜ t) (∂ₜ xₜ t)) xₜ = 0,
      (δ (q':=xₜ), ∫ t, lagrangian S t (q' t) (fderiv ℝ q' t 1)) = 0,
      (δ (pq':= fun t => (S.toCanonicalMomentum t (xₜ t) (∂ₜ xₜ t), xₜ t)),
        ∫ t, ⟪(pq' t).1, ∂ₜ (Prod.snd ∘ pq') t⟫_ℝ - S.hamiltonian t (pq' t).1 (pq' t).2) = 0]
```

## Depends on

- [A. Euler–Lagrange equations](../eulerlagrange.md)
- [Hamilton's equations](../hamiltonianmechanics/hamiltonsequations.md)

## Proof depends on

- [Elementary rules for the gradient](../../mathematics/calculus/gradient.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Basic.lean)
