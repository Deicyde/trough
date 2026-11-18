---
declaration: module
origin: cited
lean: ClassicalMechanics.NortonDome.delayedQuartic, ClassicalMechanics.NortonDome.delayedQuartic_eq, ClassicalMechanics.NortonDome.delayedQuartic_nonneg, ClassicalMechanics.NortonDome.delayedQuartic_of_le, ClassicalMechanics.NortonDome.delayedQuartic_pos, ClassicalMechanics.NortonDome.sqrt_delayedQuartic, ClassicalMechanics.NortonDome.hasDerivAt_delayedQuartic, ClassicalMechanics.NortonDome.deriv_delayedQuartic
statement: formalized
proof: formalized
---

# The motions of the Norton dome and the failure of uniqueness

The module `PhyslibAlpha.ClassicalMechanics.NortonDome.Solution`, [PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean): 38 declarations, 38 with a docstring.

> The Norton dome has infinitely many motions from rest at its apex: uniqueness fails.

## i. Overview

> A particle at rest on the apex of the Norton dome satisfies `r̈ = √r` by staying there forever,
> and also by staying until an arbitrary instant `T ≥ 0` and then sliding off along
> `r(t) = (t - T)⁴ / 144`: that curve is `C²`, vanishes with its derivative at `T`, and its
> second derivative `(t - T)² / 12` is `√r`. All these motions have the same initial position and
> velocity, so the initial data do not determine the motion. This is Norton's observation.
>
> For contrast, the pendulum's phase-space vector field is Lipschitz and Mathlib's
> `ODE_solution_unique_univ` gives `SimplePendulum.equationOfMotion_unique`; the force of the
> dome is not Lipschitz at the apex, `NortonDome.not_lipschitzOnWith_force`. Energy conservation
> does not help either, since every motion in the family has zero energy (`energy_solution`).
> Read backwards in time, in section E, a particle sliding up the dome may arrive at the apex at
> rest in finite time and stay there.

## ii. Key results

> - `NortonDome.delayedQuartic` is the real function `τ ↦ max (τ - T) 0 ⁴ / 144`, with its
>   derivatives `hasDerivAt_delayedQuartic` and `hasDerivAt_deriv_delayedQuartic`, its `C²`
>   regularity `contDiff_delayedQuartic`, and the identity `sqrt_delayedQuartic`.
> - `NortonDome.solution T` is the motion leaving the apex at the instant `T`. It is a solution,
>   `solution_isSolution`, starts from rest at the apex when `0 ≤ T`, `solution_zero` and
>   `deriv_solution_zero`, and is injective in `T`, `solution_injective`.
> - `NortonDome.rest_isSolution` is the motion staying at the apex.
> - `NortonDome.exists_isSolution_ne` is the failure of uniqueness: two distinct solutions with
>   the same initial position and velocity; `NortonDome.not_isSolution_unique` restates it as
>   the negation of the uniqueness property of the pendulum. All these motions have zero energy,
>   `NortonDome.energy_rest` and `NortonDome.energy_solution`.
> - `NortonDome.IsSolution.comp_neg` is the time-reversal symmetry of the dome, and
>   `NortonDome.arrival T` the time-reversed motion, off the apex before the instant `-T`,
>   `arrival_apply_pos`, and at rest on it from then on, `arrival_of_le`.

## iv. References

> - Norton, J. D., *The dome: an unexpectedly simple failure of determinism*, Philosophy of
>   Science 75 (2008), 786–798.
> - `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Solution` (uniqueness for a Lipschitz
>   force, for contrast).

## A. The delayed quartic

> As a function of the real time `τ`, the motion leaving the apex at the instant `T` is
> `max (τ - T) 0 ⁴ / 144`; its calculus is that of the positive-part powers of
> `NortonDome.PosPartPow`.

### A.1. Definition and sign

**`ClassicalMechanics.NortonDome.delayedQuartic`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L96).

> The delayed quartic `τ ↦ max (τ - T) 0 ⁴ / 144`: zero up to the instant `T`, and
> `(τ - T)⁴ / 144` afterwards.

```lean
noncomputable def delayedQuartic (T τ : ℝ) : ℝ
```

**`ClassicalMechanics.NortonDome.delayedQuartic_eq`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L99).

> The delayed quartic, written out.

```lean
lemma delayedQuartic_eq (T τ : ℝ) : delayedQuartic T τ = max (τ - T) 0 ^ 4 / 144
```

**`ClassicalMechanics.NortonDome.delayedQuartic_nonneg`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L102).

> The delayed quartic is non-negative.

```lean
lemma delayedQuartic_nonneg (T τ : ℝ) : 0 ≤ delayedQuartic T τ
```

**`ClassicalMechanics.NortonDome.delayedQuartic_of_le`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L107).

> The delayed quartic vanishes up to the instant `T`.

```lean
lemma delayedQuartic_of_le (T : ℝ) {τ : ℝ} (h : τ ≤ T) : delayedQuartic T τ = 0
```

**`ClassicalMechanics.NortonDome.delayedQuartic_pos`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L112).

> The delayed quartic is positive after the instant `T`.

```lean
lemma delayedQuartic_pos (T : ℝ) {τ : ℝ} (h : T < τ) : 0 < delayedQuartic T τ
```

**`ClassicalMechanics.NortonDome.sqrt_delayedQuartic`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L119).

> The square root of the delayed quartic is `max (τ - T) 0 ² / 12`, which is its second
> derivative: this is the equation of motion `r̈ = √r` of the dome along it.

```lean
lemma sqrt_delayedQuartic (T τ : ℝ) : √(delayedQuartic T τ) = max (τ - T) 0 ^ 2 / 12
```

### A.2. Derivatives and regularity

**`ClassicalMechanics.NortonDome.hasDerivAt_delayedQuartic`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L130).

> The derivative of the delayed quartic is `max (τ - T) 0 ³ / 36`.

```lean
lemma hasDerivAt_delayedQuartic (T τ : ℝ) :
    HasDerivAt (delayedQuartic T) (max (τ - T) 0 ^ 3 / 36) τ
```

**`ClassicalMechanics.NortonDome.deriv_delayedQuartic`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L137).

> The derivative of the delayed quartic, as a function.

```lean
lemma deriv_delayedQuartic (T : ℝ) :
    deriv (delayedQuartic T) = fun τ => max (τ - T) 0 ^ 3 / 36
```

**`ClassicalMechanics.NortonDome.hasDerivAt_deriv_delayedQuartic`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L142).

> The second derivative of the delayed quartic is `max (τ - T) 0 ² / 12`.

```lean
lemma hasDerivAt_deriv_delayedQuartic (T τ : ℝ) :
    HasDerivAt (deriv (delayedQuartic T)) (max (τ - T) 0 ^ 2 / 12) τ
```

**`ClassicalMechanics.NortonDome.contDiff_delayedQuartic`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L151).

> The delayed quartic is `C²`. It is in fact `C³` and not `C⁴`, which is not needed here.

```lean
lemma contDiff_delayedQuartic (T : ℝ) : ContDiff ℝ 2 (delayedQuartic T)
```

## B. The motions leaving the apex

> The motion leaving the apex at the instant `T` is the delayed quartic read on `Time`, times the
> unit vector of the arc-length coordinate.

### B.1. The definition and its values

**`ClassicalMechanics.NortonDome.solution`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L171).

> The motion of the particle on the dome leaving the apex at the instant `T`: at rest at the
> apex up to `T`, and at arc length `(t - T)⁴ / 144` from the apex afterwards.

```lean
noncomputable def solution (T : ℝ) : Time → EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.NortonDome.solution_apply`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L176).

> The arc length along the motion leaving the apex at the instant `T` is the delayed
> quartic.

```lean
lemma solution_apply (T : ℝ) (t : Time) : solution T t 0 = delayedQuartic T t.val
```

**`ClassicalMechanics.NortonDome.solution_of_le`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L180).

> The motion leaving the apex at the instant `T` is at the apex up to `T`.

```lean
lemma solution_of_le (T : ℝ) {t : Time} (h : t.val ≤ T) : solution T t = 0
```

**`ClassicalMechanics.NortonDome.solution_zero`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L184).

> The motion leaving the apex at the instant `T ≥ 0` starts at the apex.

```lean
lemma solution_zero {T : ℝ} (hT : 0 ≤ T) : solution T 0 = 0
```

**`ClassicalMechanics.NortonDome.solution_apply_pos`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L188).

> The motion leaving the apex at the instant `T` is off the apex after `T`.

```lean
lemma solution_apply_pos (T : ℝ) {t : Time} (h : T < t.val) : 0 < solution T t 0
```

### B.2. Derivatives and regularity

**`ClassicalMechanics.NortonDome.solution_contDiff`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L200).

> The motion leaving the apex at the instant `T` is `C²`.

```lean
lemma solution_contDiff (T : ℝ) : ContDiff ℝ 2 (solution T)
```

**`ClassicalMechanics.NortonDome.deriv_solution`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L206).

> The velocity along the motion leaving the apex at the instant `T` is
> `max (t - T) 0 ³ / 36`.

```lean
lemma deriv_solution (T : ℝ) :
    ∂ₜ (solution T) = fun t => (max (t.val - T) 0 ^ 3 / 36) • EuclideanSpace.single 0 1
```

**`ClassicalMechanics.NortonDome.deriv_deriv_solution`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L216).

> The acceleration along the motion leaving the apex at the instant `T` is
> `max (t - T) 0 ² / 12`.

```lean
lemma deriv_deriv_solution (T : ℝ) :
    ∂ₜ (∂ₜ (solution T)) =
      fun t => (max (t.val - T) 0 ^ 2 / 12) • EuclideanSpace.single 0 1
```

**`ClassicalMechanics.NortonDome.deriv_solution_zero`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L228).

> The motion leaving the apex at the instant `T ≥ 0` starts from rest.

```lean
lemma deriv_solution_zero {T : ℝ} (hT : 0 ≤ T) : ∂ₜ (solution T) 0 = 0
```

### B.3. The equation of motion

**`ClassicalMechanics.NortonDome.solution_equationOfMotion`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L240).

> The motion leaving the apex at the instant `T` satisfies the equation of motion of the
> dome: its acceleration `max (t - T) 0 ² / 12` is the square root of its arc length.

```lean
lemma solution_equationOfMotion (T : ℝ) : S.EquationOfMotion (solution T)
```

**`ClassicalMechanics.NortonDome.solution_isSolution`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L247).

> The motion leaving the apex at the instant `T` is a solution of the dome.

```lean
lemma solution_isSolution (T : ℝ) : S.IsSolution (solution T)
```

### B.4. Distinct instants give distinct motions

**`ClassicalMechanics.NortonDome.solution_ne_of_lt`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L260).

> Motions leaving the apex at distinct instants are distinct: at the later instant one is
> still at the apex and the other is not.

```lean
lemma solution_ne_of_lt {T T' : ℝ} (h : T < T') : solution T ≠ solution T'
```

**`ClassicalMechanics.NortonDome.solution_injective`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L267).

> The family of motions leaving the apex is injective in the instant of departure.

```lean
lemma solution_injective : Function.Injective solution
```

**`ClassicalMechanics.NortonDome.solution_ne_zero`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L275).

> No motion leaving the apex is the motion staying at it.

```lean
lemma solution_ne_zero (T : ℝ) : solution T ≠ 0
```

## C. The motion staying at the apex

> The force vanishes at the apex, so the constant curve there satisfies the equation of motion.

**`ClassicalMechanics.NortonDome.rest_isSolution`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L290).

> The motion staying at rest at the apex is a solution of the dome.

```lean
lemma rest_isSolution : S.IsSolution 0
```

**`ClassicalMechanics.NortonDome.energy_rest`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L296).

> The motion staying at the apex has zero energy.

```lean
lemma energy_rest (t : Time) : S.energy 0 t = 0
```

## D. The failure of uniqueness

> Rest at the apex and departure at any instant `T ≥ 0` are distinct solutions with the same
> initial data. So the uniqueness property `SimplePendulum.IsSolution.eq_of_initial` of the
> pendulum fails for the dome, whose force violates the Picard–Lindelöf hypothesis
> (`not_lipschitzOnWith_force`).

**`ClassicalMechanics.NortonDome.exists_isSolution_ne`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L314).

> Failure of uniqueness for the Norton dome: there are two distinct solutions of the
> dome with the same initial position and the same initial velocity. The witnesses are the
> motion staying at the apex and the motion leaving it at the instant `0`.

```lean
lemma exists_isSolution_ne :
    ∃ x y : Time → EuclideanSpace ℝ (Fin 1), S.IsSolution x ∧ S.IsSolution y ∧
      x 0 = y 0 ∧ ∂ₜ x 0 = ∂ₜ y 0 ∧ x ≠ y
```

**`ClassicalMechanics.NortonDome.not_isSolution_unique`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L324).

> The solutions of the Norton dome are not determined by their initial position and
> velocity: the uniqueness property that the simple pendulum has,
> `SimplePendulum.IsSolution.eq_of_initial`, fails for the dome.

```lean
lemma not_isSolution_unique :
    ¬ ∀ x y : Time → EuclideanSpace ℝ (Fin 1), S.IsSolution x → S.IsSolution y →
      x 0 = y 0 → ∂ₜ x 0 = ∂ₜ y 0 → x = y
```

**`ClassicalMechanics.NortonDome.exists_isSolution_of_nonneg`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L334).

> For every instant `T ≥ 0` there is a solution of the dome starting from rest at the apex
> which is at the apex up to `T` and off it afterwards: the motions from rest at the apex form
> a one-parameter family.

```lean
lemma exists_isSolution_of_nonneg {T : ℝ} (hT : 0 ≤ T) :
    ∃ r : Time → EuclideanSpace ℝ (Fin 1), S.IsSolution r ∧ r 0 = 0 ∧ ∂ₜ r 0 = 0 ∧
      (∀ t : Time, t.val ≤ T → r t = 0) ∧ (∀ t : Time, T < t.val → 0 < r t 0)
```

**`ClassicalMechanics.NortonDome.energy_solution`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L343).

> Every motion leaving the apex has zero energy: before the instant `T` it is at rest at the
> apex, and the energy is conserved. Energy conservation therefore does not single out the
> motion staying at the apex.

```lean
lemma energy_solution (T : ℝ) (t : Time) : S.energy (solution T) t = 0
```

## E. Time reversal and arrival at the apex

> The equation of motion has no velocity term, so time reversal maps solutions to solutions.
> Reversing the departure at the instant `T` gives a motion sliding up the dome, arriving at the
> apex at the instant `-T` with zero velocity, and staying there. For a locally Lipschitz force
> this is impossible; for the dome it is the non-uniqueness read backwards.

**`ClassicalMechanics.NortonDome.deriv_deriv_comp_neg_of_differentiable`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L363).

> The second derivative is unchanged by the reversal of time, for a curve whose position and
> velocity are differentiable. This is `Time.deriv_deriv_comp_neg` with its `C²` hypothesis
> weakened to the regularity of a solution.

```lean
lemma deriv_deriv_comp_neg_of_differentiable {M : Type} [NormedAddCommGroup M]
    [NormedSpace ℝ M] (f : Time → M) (hf : Differentiable ℝ f) (hf' : Differentiable ℝ (∂ₜ f))
    (t : Time) : ∂ₜ (∂ₜ (fun s => f (-s))) t = ∂ₜ (∂ₜ f) (-t)
```

**`ClassicalMechanics.NortonDome.equationOfMotion_comp_neg`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L373).

> The time reversal of a twice differentiable curve satisfying the equation of motion of the
> dome satisfies it too: the equation has no velocity term.

```lean
lemma equationOfMotion_comp_neg {r : Time → EuclideanSpace ℝ (Fin 1)} (hr : Differentiable ℝ r)
    (hr' : Differentiable ℝ (∂ₜ r)) (h : S.EquationOfMotion r) :
    S.EquationOfMotion (fun t => r (-t))
```

**`ClassicalMechanics.NortonDome.IsSolution.comp_neg`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L381).

> The time reversal of a solution of the dome is a solution.

```lean
lemma IsSolution.comp_neg {S : NortonDome} {r : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution r) : S.IsSolution (fun t => r (-t))
```

**`ClassicalMechanics.NortonDome.arrival`**, a def, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L393).

> The motion of the particle on the dome arriving at the apex at the instant `-T`: the time
> reversal of the motion leaving the apex at the instant `T`.

```lean
noncomputable def arrival (T : ℝ) : Time → EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.NortonDome.arrival_isSolution`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L396).

> The motion arriving at the apex at the instant `-T` is a solution of the dome.

```lean
lemma arrival_isSolution (T : ℝ) : S.IsSolution (arrival T)
```

**`ClassicalMechanics.NortonDome.arrival_apply_pos`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L401).

> The motion arriving at the apex at the instant `-T` is off the apex before that
> instant.

```lean
lemma arrival_apply_pos (T : ℝ) {t : Time} (h : t.val < -T) : 0 < arrival T t 0
```

**`ClassicalMechanics.NortonDome.arrival_of_le`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L406).

> The motion arriving at the apex at the instant `-T` is at the apex from that instant on:
> it reaches the apex in finite time and stays there.

```lean
lemma arrival_of_le (T : ℝ) {t : Time} (h : -T ≤ t.val) : arrival T t = 0
```

**`ClassicalMechanics.NortonDome.deriv_arrival_of_le`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean#L410).

> The motion arriving at the apex at the instant `-T` arrives with zero velocity.

```lean
lemma deriv_arrival_of_le (T : ℝ) {t : Time} (h : -T ≤ t.val) : ∂ₜ (arrival T) t = 0
```

## Depends on

- [The Norton dome](basic.md)

## Proof depends on

- [Powers of the positive part](pospartpow.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Solution.lean)
