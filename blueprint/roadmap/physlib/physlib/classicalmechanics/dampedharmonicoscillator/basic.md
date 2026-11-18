---
declaration: module
origin: cited
lean: ClassicalMechanics.DampedHarmonicOscillator, ClassicalMechanics.DampedHarmonicOscillator.EquationOfMotion, ClassicalMechanics.DampedHarmonicOscillator.acceleration_eq_of_equationOfMotion, ClassicalMechanics.DampedHarmonicOscillator.energy_dissipation_rate, ClassicalMechanics.DampedHarmonicOscillator.energy_not_conserved, ClassicalMechanics.DampedHarmonicOscillator.energy_balance, ClassicalMechanics.DampedHarmonicOscillator.energy_antitone, ClassicalMechanics.DampedHarmonicOscillator.energy_le_initial
statement: formalized
proof: formalized
---

# The damped harmonic oscillator

The module `Physlib.ClassicalMechanics.DampedHarmonicOscillator.Basic`, [Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean): 69 declarations, 61 with a docstring; 1 private, not shown.

> The equation of motion, energy dissipation, damping regimes and variational formulation.

## i. Overview

> The damped harmonic oscillator is a classical mechanical system consisting of a mass `m`
> under a restoring force `- k x` and a damping force `- γ ẋ`, where `k` is the spring
> constant, `γ` is the damping coefficient, `x` is the position, and `ẋ` is the velocity.
>
> The equation of motion for the damped harmonic oscillator is:
> ```
> m ẍ + γ ẋ + k x = 0
> ```
>
> Depending on the relationship between the damping coefficient and the natural frequency,
> the system exhibits three different behaviors:
> - **Underdamped** (`γ^2 < 4 * m * k`) : oscillatory motion with exponentially decaying
>   amplitude.
> - **Critically damped** (`γ^2 = 4 * m * k`) : fastest return to equilibrium without
>   oscillation.
> - **Overdamped** (`4 * m * k < γ^2`) : slow return to equilibrium without oscillation.
>
> In this file, the position and velocity both have type `EuclideanSpace ℝ (Fin 1)`. This
> coordinate model is useful for a first formalization, but it works only because the
> one-dimensional configuration space and its tangent space are both isomorphic to
> one-dimensional Euclidean space. A more geometric formalization should represent the
> configuration space and its tangent bundle directly.

## ii. Key results

> The key results in the study of the classical damped harmonic oscillator are the following:
>
> In the `Basic` module:
> - `DampedHarmonicOscillator` contains the input data to the problem.
> - `EquationOfMotion` defines the damped oscillator equation `m ẍ + γ ẋ + k x = 0`.
> - `energy_dissipation_rate` computes the rate at which damping removes mechanical energy.
> - `energy_balance` gives the mechanical energy change over a finite time interval.
> - `energy_antitone` shows that mechanical energy is nonincreasing along a solution.
> - `IsUnderdamped`, `IsCriticallyDamped`, and `IsOverdamped` define the three damping
>   regimes from the discriminant `γ^2 - 4 * m * k`.
> - `angularFrequency` selects the real frequency parameter from the damping regime.
> - `qualityFactor` and `relaxationTime` define the quality factor `Q = ω / (2 β)` and the
>   amplitude relaxation time `τ = 1 / β` from the decay rate `β = γ / (2 m)`;
>   `isUnderdamped_iff_half_lt_qualityFactor` and its companions characterise the three damping
>   regimes by `Q`.
> - `toUndamped_equationOfMotion` relates the damped and undamped equations of motion when
>   the damping coefficient is zero.
> - `lagrangian` defines the Caldirola–Kanai lagrangian `exp (γ/m * t) * (T - V)`.
> - `gradLagrangian` defines the variational gradient of the corresponding action, and
>   `equationOfMotion_iff_gradLagrangian_zero` shows that its vanishing is equivalent to
>   the equation of motion.
>
> In the `Solution` module:
> - `InitialConditions` contains the initial position and velocity.
> - `trajectory` gives the explicit solution selected from the damping regime.

## iv. References

> References for the damped harmonic oscillator include:
>
> * Landau & Lifshitz, Mechanics, page 76, section 25. [ref: landau\_mechanics]
> * Goldstein, Classical Mechanics, Chapter 6, Section 6.5 (Forced Vibrations and the Effect of
>   Dissipative Forces). [ref: goldstein\_classicalmechanics]
>
> References for the Caldirola–Kanai lagrangian include:
>
> * Caldirola, Nuovo Cimento 18 (1941) 393. [ref: caldirola\_1941]
> * Kanai, Progress of Theoretical Physics 3 (1948) 440. [ref: kanai\_1948]

## A. The input data

> We start by defining a structure containing the input data of the damped harmonic oscillator.
> The mass `m` and spring constant `k` are inherited from `HarmonicOscillator`; this file adds
> the damping coefficient `γ`.

**`ClassicalMechanics.DampedHarmonicOscillator`**, a structure, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L134).

> The classical damped harmonic oscillator is specified by a mass `m`, a spring
> constant `k`, and a damping coefficient `γ`.
>
> The mass and spring constant are inherited from `HarmonicOscillator` and are positive.
> The damping coefficient is assumed to be nonnegative.

```lean
structure DampedHarmonicOscillator extends HarmonicOscillator where
  /-- The damping coefficient of the oscillator. -/
  γ : ℝ
  /-- The damping coefficient is nonnegative. -/
  γ_nonneg : 0 ≤ γ
```

> The mass/spring nonzero lemmas, the natural angular frequency, and the undamped energy API
> are inherited from `HarmonicOscillator`.

## B. The equation of motion and energy dissipation

### B.1. The equation of motion

**`ClassicalMechanics.DampedHarmonicOscillator.EquationOfMotion`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L159).

> The equation of motion for the damped harmonic oscillator:
> `m ẍ + γ ẋ + k x = 0`.

```lean
noncomputable def EquationOfMotion (xₜ : Time → EuclideanSpace ℝ (Fin 1)) : Prop
```

**`ClassicalMechanics.DampedHarmonicOscillator.acceleration_eq_of_equationOfMotion`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L164).

> Solving the equation of motion for the acceleration: along a solution the second derivative
> is `-(k/m) x - (γ/m) ẋ`.

```lean
lemma acceleration_eq_of_equationOfMotion (z : Time → EuclideanSpace ℝ (Fin 1))
    (hEOM : S.EquationOfMotion z) (t : Time) :
    ∂ₜ (∂ₜ z) t = (-(S.m⁻¹ * S.k)) • z t + (-(S.m⁻¹ * S.γ)) • ∂ₜ z t
```

### B.2. Energy dissipation

> The damped oscillator inherits the mechanical energy from the undamped harmonic oscillator.
> Along a solution of the damped equation of motion, that energy decreases at a rate
> proportional to `-γ ‖ẋ‖^2`.

**`ClassicalMechanics.DampedHarmonicOscillator.energy_dissipation_rate`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L189).

> Along a smooth solution of the damped equation of motion, the derivative of the
> mechanical energy is `-γ ‖ẋ‖^2`.

```lean
lemma energy_dissipation_rate (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time)
    (h1 : S.EquationOfMotion xₜ)
    (hx : ContDiff ℝ ∞ xₜ) :
    ∂ₜ (S.energy xₜ) t = - S.γ * ⟪∂ₜ xₜ t, ∂ₜ xₜ t⟫_ℝ
```

**`ClassicalMechanics.DampedHarmonicOscillator.energy_not_conserved`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L200).

> If `0 < γ` and the velocity is nonzero at a time, the mechanical energy is strictly
> decreasing at that time.

```lean
lemma energy_not_conserved (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time)
    (h1 : S.EquationOfMotion xₜ) (hx : ContDiff ℝ ∞ xₜ) (hdx : ∂ₜ xₜ t ≠ 0) (hγ : 0 < S.γ) :
    ∂ₜ (S.energy xₜ) t < 0
```

**`ClassicalMechanics.DampedHarmonicOscillator.energy_balance`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L208).

> The mechanical energy change between two times equals the work done by damping.
> The interval integral is oriented, so the identity holds in either time order.

```lean
lemma energy_balance (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hEOM : S.EquationOfMotion xₜ) (hx : ContDiff ℝ ∞ xₜ) (a b : ℝ) :
    S.energy xₜ ⟨b⟩ - S.energy xₜ ⟨a⟩ =
      -S.γ * ∫ t in a..b, ‖∂ₜ xₜ ⟨t⟩‖ ^ 2
```

**`ClassicalMechanics.DampedHarmonicOscillator.energy_antitone`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L225).

> Mechanical energy is nonincreasing along every smooth solution, including zero damping.

```lean
lemma energy_antitone (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hEOM : S.EquationOfMotion xₜ) (hx : ContDiff ℝ ∞ xₜ) :
    Antitone (fun t : ℝ => S.energy xₜ ⟨t⟩)
```

**`ClassicalMechanics.DampedHarmonicOscillator.energy_le_initial`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L238).

> At nonnegative times the mechanical energy is bounded by its initial value.

```lean
lemma energy_le_initial (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hEOM : S.EquationOfMotion xₜ) (hx : ContDiff ℝ ∞ xₜ) (t : Time) (ht : 0 ≤ t.val) :
    S.energy xₜ t ≤ S.energy xₜ 0
```

## C. Newton's second law

> We define the force of the damped oscillator, and show that the equation of
> motion is equivalent to Newton's second law.

### C.1. The force

> We define the force of the damped oscillator as `- k x - γ v`.

**`ClassicalMechanics.DampedHarmonicOscillator.force`**, a def, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L261).

> The force of the damped harmonic oscillator at a given position and time.

```lean
noncomputable def force (S : DampedHarmonicOscillator)
    (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (t : Time) :
    EuclideanSpace ℝ (Fin 1)
```

### C.2. Equation of motion if and only if Newton's second law

> We show that the equation of motion is equivalent to Newton's second law.

**`ClassicalMechanics.DampedHarmonicOscillator.equationOfMotion_iff_newtons_2nd_law`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L273).

```lean
lemma equationOfMotion_iff_newtons_2nd_law (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.EquationOfMotion xₜ ↔
    (∀ t : Time, S.m • ∂ₜ (∂ₜ xₜ) t = force S xₜ t)
```

## D. Damping regimes

> The sign of the discriminant `γ^2 - 4 * m * k` separates the underdamped, critically
> damped, and overdamped regimes. We also define the decay rate and the regime-selected
> real frequency that appears in the explicit solution formulas.

### D.1. The discriminant, the decay rate and the angular frequency

**`ClassicalMechanics.DampedHarmonicOscillator.discriminant`**, a def, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L299).

> The discriminant that determines the damping regime.

```lean
noncomputable def discriminant : ℝ
```

**`ClassicalMechanics.DampedHarmonicOscillator.decayRate`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L302).

> The exponential decay rate `γ / (2 * m)`.

```lean
noncomputable def decayRate : ℝ
```

**`ClassicalMechanics.DampedHarmonicOscillator.IsUnderdamped`**, a def, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L305).

> The system is underdamped when γ² < 4mk.

```lean
def IsUnderdamped : Prop
```

**`ClassicalMechanics.DampedHarmonicOscillator.IsCriticallyDamped`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L308).

> The system is critically damped when γ² = 4mk.

```lean
def IsCriticallyDamped : Prop
```

**`ClassicalMechanics.DampedHarmonicOscillator.IsOverdamped`**, a def, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L311).

> The system is overdamped when 4mk < γ².

```lean
def IsOverdamped : Prop
```

**`ClassicalMechanics.DampedHarmonicOscillator.isUnderdamped_or_isCriticallyDamped_or_isOverdamped`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L314).

> Every damped oscillator is underdamped, critically damped, or overdamped.

```lean
lemma isUnderdamped_or_isCriticallyDamped_or_isOverdamped :
    S.IsUnderdamped ∨ S.IsCriticallyDamped ∨ S.IsOverdamped
```

**`ClassicalMechanics.DampedHarmonicOscillator.IsUndamped`**, a def, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L319).

> The system is undamped when γ = 0.

```lean
def IsUndamped : Prop
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency`**, a def, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L326).

> The real frequency selected by the damping regime.
>
> In the underdamped regime this is the oscillation frequency. In the critically damped
> regime it is `0`. In the overdamped regime this is the real split rate between the two
> roots.

```lean
noncomputable def angularFrequency : ℝ
```

**`ClassicalMechanics.DampedHarmonicOscillator.discriminant_eq_four_mul_m_sq_mul_decayRate_sq_sub_ω_sq`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L337).

> The relationship between the discriminant, decay rate, and natural angular frequency.

```lean
lemma discriminant_eq_four_mul_m_sq_mul_decayRate_sq_sub_ω_sq :
    S.discriminant = 4 * S.m^2 * (S.decayRate^2 - S.ω^2)
```

**`ClassicalMechanics.DampedHarmonicOscillator.decayRate_nonneg`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L344).

> The decay rate is nonnegative.

```lean
lemma decayRate_nonneg : 0 ≤ S.decayRate
```

**`ClassicalMechanics.DampedHarmonicOscillator.decayRate_pos`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L348).

> The decay rate is positive when the damping coefficient is positive.

```lean
lemma decayRate_pos (hγ : 0 < S.γ) : 0 < S.decayRate
```

**`ClassicalMechanics.DampedHarmonicOscillator.isUnderdamped_of_gamma_eq_zero`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L352).

> An undamped oscillator lies in the underdamped regime.

```lean
lemma isUnderdamped_of_gamma_eq_zero (hγ : S.γ = 0) : S.IsUnderdamped
```

**`ClassicalMechanics.DampedHarmonicOscillator.isUnderdamped_decayRate`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L357).

> An underdamped system has decay rate less than the natural frequency.

```lean
lemma isUnderdamped_decayRate (hS : S.IsUnderdamped) : S.decayRate < S.ω
```

**`ClassicalMechanics.DampedHarmonicOscillator.isCriticallyDamped_decayRate`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L363).

> A critically damped system has decay rate equal to the natural frequency.

```lean
lemma isCriticallyDamped_decayRate (hS : S.IsCriticallyDamped) : S.ω = S.decayRate
```

**`ClassicalMechanics.DampedHarmonicOscillator.gamma_eq_two_mul_m_mul_decayRate`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L369).

> The damping coefficient is twice mass times the decay rate.

```lean
lemma gamma_eq_two_mul_m_mul_decayRate : S.γ = 2 * S.m * S.decayRate
```

**`ClassicalMechanics.DampedHarmonicOscillator.k_eq_m_mul_ω_sq`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L374).

> The spring constant is `m * ω^2`.

```lean
lemma k_eq_m_mul_ω_sq : S.k = S.m * S.ω^2
```

**`ClassicalMechanics.DampedHarmonicOscillator.k_eq_m_mul_decayRate_sq_of_criticallyDamped`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L379).

> In the critically damped regime, `k = m * decayRate^2`.

```lean
lemma k_eq_m_mul_decayRate_sq_of_criticallyDamped (hS : S.IsCriticallyDamped) :
    S.k = S.m * S.decayRate^2
```

**`ClassicalMechanics.DampedHarmonicOscillator.isOverdamped_decayRate`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L384).

> An overdamped system has decay rate greater than the natural frequency.

```lean
lemma isOverdamped_decayRate (hS : S.IsOverdamped) : S.ω < S.decayRate
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_eq_underdamped`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L390).

> In the underdamped regime, the selected frequency uses the oscillation frequency.

```lean
lemma angularFrequency_eq_underdamped (hS : S.IsUnderdamped) :
    S.angularFrequency = sqrt (- S.discriminant) / (2 * S.m)
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_eq_criticallyDamped`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L395).

> In the critically damped regime, the selected frequency is zero.

```lean
lemma angularFrequency_eq_criticallyDamped (hS : S.IsCriticallyDamped) :
    S.angularFrequency = 0
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_eq_overdamped`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L401).

> In the overdamped regime, the selected frequency uses the real split rate.

```lean
lemma angularFrequency_eq_overdamped (hS : S.IsOverdamped) :
    S.angularFrequency = sqrt S.discriminant / (2 * S.m)
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_sq_of_underdamped`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L408).

> In the underdamped regime, the selected angular frequency squares to
> `ω^2 - decayRate^2`.

```lean
lemma angularFrequency_sq_of_underdamped (hS : S.IsUnderdamped) :
    S.angularFrequency^2 = S.ω^2 - S.decayRate^2
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_pos_of_underdamped`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L417).

> The selected angular frequency is positive in the underdamped regime.

```lean
lemma angularFrequency_pos_of_underdamped (hS : S.IsUnderdamped) :
    0 < S.angularFrequency
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_ne_zero_of_underdamped`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L423).

> The selected angular frequency is nonzero in the underdamped regime.

```lean
lemma angularFrequency_ne_zero_of_underdamped (hS : S.IsUnderdamped) :
    S.angularFrequency ≠ 0
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_sq_of_overdamped`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L429).

> In the overdamped regime, the selected angular frequency squares to
> `decayRate^2 - ω^2`.

```lean
lemma angularFrequency_sq_of_overdamped (hS : S.IsOverdamped) :
    S.angularFrequency^2 = S.decayRate^2 - S.ω^2
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_pos_of_overdamped`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L438).

> The selected angular frequency is positive in the overdamped regime.

```lean
lemma angularFrequency_pos_of_overdamped (hS : S.IsOverdamped) :
    0 < S.angularFrequency
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_ne_zero_of_overdamped`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L444).

> The selected angular frequency is nonzero in the overdamped regime.

```lean
lemma angularFrequency_ne_zero_of_overdamped (hS : S.IsOverdamped) :
    S.angularFrequency ≠ 0
```

**`ClassicalMechanics.DampedHarmonicOscillator.isUnderdamped_iff_decayRate_lt`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L449).

> The underdamped regime is characterised by `β < ω`.

```lean
lemma isUnderdamped_iff_decayRate_lt : S.IsUnderdamped ↔ S.decayRate < S.ω
```

**`ClassicalMechanics.DampedHarmonicOscillator.isCriticallyDamped_iff_eq_decayRate`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L457).

> The critically damped regime is characterised by `ω = β`.

```lean
lemma isCriticallyDamped_iff_eq_decayRate : S.IsCriticallyDamped ↔ S.ω = S.decayRate
```

**`ClassicalMechanics.DampedHarmonicOscillator.isOverdamped_iff_lt_decayRate`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L465).

> The overdamped regime is characterised by `ω < β`.

```lean
lemma isOverdamped_iff_lt_decayRate : S.IsOverdamped ↔ S.ω < S.decayRate
```

### D.2. The quality factor and the relaxation time

> The quality factor `Q = ω / (2 β)` and the amplitude relaxation time `τ = 1 / β` are the
> usual dimensionless and dimensionful measures of the damping, both expressed through the
> decay rate `β = γ / (2 m)`. When `γ = 0` both are `0` by the convention `x / 0 = 0` of Lean,
> so the lemmas below assume `0 < γ` whenever the value matters.

**`ClassicalMechanics.DampedHarmonicOscillator.qualityFactor`**, a def, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L487).

> The quality factor `Q = ω / (2 β)`, equal to `m ω / γ` and to `√(m k) / γ`: the ratio of
> the natural angular frequency to the width `γ / m` of the resonance.
>
> When `γ = 0` the value is `0` by the convention `x / 0 = 0`.

```lean
noncomputable def qualityFactor : ℝ
```

**`ClassicalMechanics.DampedHarmonicOscillator.relaxationTime`**, a def, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L493).

> The relaxation time `τ = 1 / β` of the amplitude, equal to `2 m / γ`; the exponential
> factor of the solutions is `exp (-t / τ)` (see `exp_neg_decayRate_mul`).
>
> When `γ = 0` the value is `0` by the convention `0⁻¹ = 0`.

```lean
noncomputable def relaxationTime : ℝ
```

**`ClassicalMechanics.DampedHarmonicOscillator.qualityFactor_eq_m_mul_ω_div_γ`**, a lemma, [line 496](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L496).

> The quality factor equals `m ω / γ`.

```lean
lemma qualityFactor_eq_m_mul_ω_div_γ : S.qualityFactor = S.m * S.ω / S.γ
```

**`ClassicalMechanics.DampedHarmonicOscillator.qualityFactor_eq_sqrt_div`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L501).

> The quality factor equals `√(m k) / γ`.

```lean
lemma qualityFactor_eq_sqrt_div : S.qualityFactor = √(S.m * S.k) / S.γ
```

**`ClassicalMechanics.DampedHarmonicOscillator.qualityFactor_pos`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L507).

> The quality factor is positive when the damping coefficient is positive.

```lean
lemma qualityFactor_pos (hγ : 0 < S.γ) : 0 < S.qualityFactor
```

**`ClassicalMechanics.DampedHarmonicOscillator.qualityFactor_sq`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L512).

> The square of the quality factor equals `m k / γ ^ 2`.

```lean
lemma qualityFactor_sq : S.qualityFactor ^ 2 = S.m * S.k / S.γ ^ 2
```

**`ClassicalMechanics.DampedHarmonicOscillator.discriminant_eq_mul_qualityFactor`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L517).

> The discriminant in terms of the quality factor: `γ ^ 2 - 4 m k = 4 m k (1 / (4 Q ^ 2) - 1)`;
> for `γ = 0` both sides equal `-4 m k`.

```lean
lemma discriminant_eq_mul_qualityFactor :
    S.discriminant = 4 * S.m * S.k * (1 / (4 * S.qualityFactor ^ 2) - 1)
```

**`ClassicalMechanics.DampedHarmonicOscillator.isUnderdamped_iff_half_lt_qualityFactor`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L525).

> The underdamped regime is characterised by `1 / 2 < Q` when `0 < γ`.

```lean
lemma isUnderdamped_iff_half_lt_qualityFactor (hγ : 0 < S.γ) :
    S.IsUnderdamped ↔ 1 / 2 < S.qualityFactor
```

**`ClassicalMechanics.DampedHarmonicOscillator.isCriticallyDamped_iff_qualityFactor_eq_half`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L532).

> The critically damped regime is characterised by `Q = 1 / 2` when `0 < γ`.

```lean
lemma isCriticallyDamped_iff_qualityFactor_eq_half (hγ : 0 < S.γ) :
    S.IsCriticallyDamped ↔ S.qualityFactor = 1 / 2
```

**`ClassicalMechanics.DampedHarmonicOscillator.isOverdamped_iff_qualityFactor_lt_half`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L539).

> The overdamped regime is characterised by `Q < 1 / 2` when `0 < γ`.

```lean
lemma isOverdamped_iff_qualityFactor_lt_half (hγ : 0 < S.γ) :
    S.IsOverdamped ↔ S.qualityFactor < 1 / 2
```

**`ClassicalMechanics.DampedHarmonicOscillator.angularFrequency_sq_eq_mul_qualityFactor`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L547).

> In the underdamped regime the selected angular frequency satisfies
> `ω_d ^ 2 = ω ^ 2 (1 - 1 / (4 Q ^ 2))` when `0 < γ`.

```lean
lemma angularFrequency_sq_eq_mul_qualityFactor (hγ : 0 < S.γ) (hS : S.IsUnderdamped) :
    S.angularFrequency ^ 2 = S.ω ^ 2 * (1 - 1 / (4 * S.qualityFactor ^ 2))
```

**`ClassicalMechanics.DampedHarmonicOscillator.relaxationTime_eq`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L555).

> The relaxation time equals `2 m / γ`.

```lean
lemma relaxationTime_eq : S.relaxationTime = 2 * S.m / S.γ
```

**`ClassicalMechanics.DampedHarmonicOscillator.decayRate_mul_relaxationTime`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L559).

> The decay rate and the relaxation time are inverse to each other when `0 < γ`.

```lean
lemma decayRate_mul_relaxationTime (hγ : 0 < S.γ) : S.decayRate * S.relaxationTime = 1
```

**`ClassicalMechanics.DampedHarmonicOscillator.relaxationTime_pos`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L563).

> The relaxation time is positive when the damping coefficient is positive.

```lean
lemma relaxationTime_pos (hγ : 0 < S.γ) : 0 < S.relaxationTime
```

**`ClassicalMechanics.DampedHarmonicOscillator.qualityFactor_eq_ω_mul_relaxationTime`**, a lemma, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L567).

> The quality factor equals `ω τ / 2`; this holds for `γ = 0` as well, both sides being `0`.

```lean
lemma qualityFactor_eq_ω_mul_relaxationTime : S.qualityFactor = S.ω * S.relaxationTime / 2
```

**`ClassicalMechanics.DampedHarmonicOscillator.exp_neg_decayRate_mul`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L573).

> The exponential factor `exp (-β t)` of the solutions equals `exp (-t / τ)`; for `γ = 0`
> both sides equal `1`.

```lean
lemma exp_neg_decayRate_mul (t : Time) :
    exp (-S.decayRate * t) = exp (-(t : ℝ) / S.relaxationTime)
```

## E. To undamped oscillator

> We show that the damped harmonic oscillator reduces to the undamped harmonic oscillator when the
> damping coefficient is zero. The underlying mass and spring data are already inherited from
> `HarmonicOscillator`; the proof argument records that this conversion is being used only in
> the zero-damping case.
>
> We also show that the equations of motion are equivalent in this case.

**`ClassicalMechanics.DampedHarmonicOscillator.toUndamped`**, a def, [line 592](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L592).

> Convert a damped oscillator to its underlying undamped oscillator when `γ = 0`.

```lean
def toUndamped (S : DampedHarmonicOscillator) (_hS : S.IsUndamped) :
    HarmonicOscillator
```

**`ClassicalMechanics.DampedHarmonicOscillator.toUndamped_equationOfMotion`**, a lemma, [line 598](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L598).

> When `γ = 0`, the damped equation of motion is equivalent to the equation of motion
> for the corresponding undamped harmonic oscillator.

```lean
lemma toUndamped_equationOfMotion (S : DampedHarmonicOscillator) (hS : S.IsUndamped)
    (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    S.EquationOfMotion xₜ ↔ (S.toUndamped hS).EquationOfMotion xₜ
```

## F. The Caldirola–Kanai lagrangian and the equation of motion

> The damped harmonic oscillator is not conservative, so the undamped lagrangian
> `T - V` does not reproduce the damped equation of motion. Instead we use the
> Caldirola–Kanai lagrangian, which multiplies the undamped lagrangian by the
> time-dependent factor `exp (γ/m * t)`:
>
> $$L(t, x, v) = e^{(\gamma/m) t}\left(\frac{1}{2} m \|v\|^2 - \frac{1}{2} k \|x\|^2\right)$$
>
> Setting the variational gradient of the corresponding action equal to zero
> recovers exactly the damped equation of motion `m ẍ + γ ẋ + k x = 0`.

### F.1. The lagrangian

> We define the Caldirola–Kanai lagrangian as the lagrangian of the underlying
> undamped harmonic oscillator multiplied by the exponential factor `exp (γ/m * t)`.

**`ClassicalMechanics.DampedHarmonicOscillator.lagrangian`**, a def, [line 637](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L637).

> The Caldirola–Kanai lagrangian of the damped harmonic oscillator. It is the
> lagrangian of the underlying undamped harmonic oscillator multiplied by the
> time-dependent factor `exp (γ/m * t)`.

```lean
noncomputable def lagrangian (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) : ℝ
```

#### F.1.1. Equalities for the lagrangian

> We prove some simple equalities for the lagrangian, in particular that when applied to a
> trajectory it is the exponential factor times the kinetic energy minus the potential energy,
> and that it reduces to the undamped lagrangian when the damping coefficient is zero.

**`ClassicalMechanics.DampedHarmonicOscillator.lagrangian_eq`**, a lemma, [line 650](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L650).

```lean
lemma lagrangian_eq : S.lagrangian = fun (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) =>
    exp (S.γ / S.m * t) * (1 / (2 : ℝ) * S.m * ⟪v, v⟫_ℝ - 1 / (2 : ℝ) * S.k * ⟪x, x⟫_ℝ)
```

**`ClassicalMechanics.DampedHarmonicOscillator.lagrangian_eq_exp_mul_kineticEnergy_sub_potentialEnergy`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L655).

```lean
lemma lagrangian_eq_exp_mul_kineticEnergy_sub_potentialEnergy (t : Time)
    (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    S.lagrangian t (xₜ t) (∂ₜ xₜ t) =
      exp (S.γ / S.m * t) * (S.kineticEnergy xₜ t - S.potentialEnergy (xₜ t))
```

**`ClassicalMechanics.DampedHarmonicOscillator.lagrangian_of_isUndamped`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L663).

> When the damping coefficient is zero, the Caldirola–Kanai lagrangian is the
> lagrangian of the underlying undamped harmonic oscillator.

```lean
lemma lagrangian_of_isUndamped (hS : S.IsUndamped) :
    S.lagrangian = S.toHarmonicOscillator.lagrangian
```

#### F.1.2. Smoothness of the lagrangian

> The lagrangian is smooth in all its arguments.

**`ClassicalMechanics.DampedHarmonicOscillator.contDiff_lagrangian`**, a lemma, [line 678](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L678).

```lean
lemma contDiff_lagrangian (n : WithTop ℕ∞) : ContDiff ℝ n ↿S.lagrangian
```

#### F.1.3. Gradients of the lagrangian

> We now show results related to the gradients of the lagrangian with respect to the
> position and velocity. They follow from the corresponding gradients of the undamped
> lagrangian, using that the gradient scales with the constant `exp (γ/m * t)`.

**`ClassicalMechanics.DampedHarmonicOscillator.gradient_lagrangian_position_eq`**, a lemma, [line 693](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L693).

```lean
lemma gradient_lagrangian_position_eq (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) :
    gradient (fun x => S.lagrangian t x v) x = -(exp (S.γ / S.m * t) * S.k) • x
```

**`ClassicalMechanics.DampedHarmonicOscillator.gradient_lagrangian_velocity_eq`**, a lemma, [line 703](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L703).

```lean
lemma gradient_lagrangian_velocity_eq (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) :
    gradient (S.lagrangian t x) v = (exp (S.γ / S.m * t) * S.m) • v
```

### F.2. The variational gradient of the action

> We now write down the variational gradient of the action of the damped harmonic
> oscillator, for a trajectory $x(t)$ this is equal to
>
> $$t\mapsto \left.\frac{\partial L(t, q, \dot x (t))}{\partial q}\right|_{q = x(t)} -
>   \frac{d}{dt} \left.\frac{\partial L(t, x(t), v)}{\partial v}\right|_{v = \dot x (t)}$$
>
> Setting this equal to zero corresponds to the Euler-Lagrange equations, and thereby the
> equation of motion.

**`ClassicalMechanics.DampedHarmonicOscillator.gradLagrangian`**, a def, [line 728](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L728).

> The variational gradient of the action of the damped harmonic oscillator.

```lean
noncomputable def gradLagrangian (xₜ : Time → EuclideanSpace ℝ (Fin 1)) :
    Time → EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.DampedHarmonicOscillator.gradLagrangian_eq_eulerLagrangeOp`**, a lemma, [line 732](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L732).

```lean
lemma gradLagrangian_eq_eulerLagrangeOp (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hq : ContDiff ℝ ∞ xₜ) :
    S.gradLagrangian xₜ = eulerLagrangeOp S.lagrangian xₜ
```

#### F.2.1. The variational gradient and Newton's second law

> We simplify the variational gradient of the action to the exponential factor times
> the difference between the force and mass times acceleration.

**`ClassicalMechanics.DampedHarmonicOscillator.gradLagrangian_eq_force`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L761).

> The variational gradient of the Caldirola–Kanai action is the exponential factor
> times the difference of the force and mass times acceleration appearing in
> Newton's second law.

```lean
lemma gradLagrangian_eq_force (xₜ : Time → EuclideanSpace ℝ (Fin 1)) (hx : ContDiff ℝ ∞ xₜ) :
    S.gradLagrangian xₜ = fun t : Time =>
      exp (S.γ / S.m * t) • (force S xₜ t - S.m • ∂ₜ (∂ₜ xₜ) t)
```

### F.3. Equation of motion iff the variational gradient vanishes

> The equation of motion of the damped harmonic oscillator holds if and only if the
> variational gradient of the Caldirola–Kanai action vanishes, since the exponential
> factor is never zero.

**`ClassicalMechanics.DampedHarmonicOscillator.equationOfMotion_iff_gradLagrangian_zero`**, a lemma, [line 788](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean#L788).

```lean
lemma equationOfMotion_iff_gradLagrangian_zero (xₜ : Time → EuclideanSpace ℝ (Fin 1))
    (hx : ContDiff ℝ ∞ xₜ) :
    S.EquationOfMotion xₜ ↔ S.gradLagrangian xₜ = 0
```

## Depends on

- [The Classical Harmonic Oscillator](../harmonicoscillator/basic.md)

## Sources

- [Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/DampedHarmonicOscillator/Basic.lean)
