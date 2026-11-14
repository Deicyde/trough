---
declaration: module
origin: cited
lean: ClassicalMechanics.NortonDome, ClassicalMechanics.NortonDome.m_ne_zero, ClassicalMechanics.NortonDome.g_ne_zero, ClassicalMechanics.NortonDome.height, ClassicalMechanics.NortonDome.height_eq, ClassicalMechanics.NortonDome.height_nonneg, ClassicalMechanics.NortonDome.height_eq_zero_iff, ClassicalMechanics.NortonDome.hasDerivAt_height
statement: formalized
proof: formalized
---

# The Norton dome

The module `PhyslibAlpha.ClassicalMechanics.NortonDome.Basic`, [PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean): 51 declarations, 51 with a docstring.

> The Norton dome: energies, force, equation of motion, and the non-Lipschitz force at the apex.

## i. Overview

> The Norton dome is a point mass `m` sliding without friction, under gravity `g`, on a
> rotationally symmetric dome whose surface lies a depth `h(r) = (2/(3g)) r^{3/2}` below its
> apex at arc length `r`. Its force is continuous, yet a mass at rest on the apex may stay there
> forever or start sliding down at any later instant: the equation of motion has more than one
> solution with given initial data. It is the standard example of the failure of determinism in
> Newtonian mechanics and, mathematically, of the failure of uniqueness for an ODE whose
> right-hand side is continuous but not Lipschitz.
>
> Newton's laws, as stated, do not determine the motion. A Newtonian system that is to be
> deterministic must add something the laws do not state, a regularity condition on the force or
> a restriction on the admissible motions; which addition belongs to Newtonian mechanics is
> debated, and the folder does not decide it. It proves what each candidate condition buys and
> that the dome fails each. Reading order:
>
> - `NortonDome.Basic` (this file): the dome, its energies, force, equation of motion `r̈ = √r`,
>   and the failure of the Lipschitz condition at the apex.
> - `NortonDome.Solution`: rest at the apex and departure at any instant `T` are all solutions
>   from the same initial data, `exists_isSolution_ne`.
> - `NortonDome.PhysicalSpace`: the arc-length chart as a point mass constrained to the surface.
> - `NortonDome.NewtonianSystem`: the minimal `NewtonianSystem`; determinism, the first law and
>   the regularity conditions as predicates; a locally Lipschitz force gives determinism.
> - `NortonDome.Determinism`: the dome is not deterministic, violates the first law, and fails
>   each regularity condition.
> - `NortonDome.PeanoExistence`, `NortonDome.PosPartPow`, `NortonDome.Sqrt`: supporting
>   analysis. Peano's theorem is pending in Mathlib and stated informally; all else is proved.
>
> The configuration is the arc length `r`, carried as for the pendulum on the Euclidean lift
> `Time → EuclideanSpace ℝ (Fin 1)`. The physical dome is `r ≥ 0`; the chart is all of `ℝ`, and
> for `r < 0` the truncated square root makes the force vanish. With `T = ½ m ṙ²` and
> `V = -m g h(r) = -(2m/3) r^{3/2}` the equation of motion is `m r̈ = -dV/dr = m √r`, so
> `r̈ = √r`: `m` and `g` cancel. Norton's profile presumes units in which the constant fixing the
> size of the dome is `1`.
>
> The force `√r` is continuous but not Lipschitz at the apex, and the potential is `C¹` but not
> `C²` there; see `NortonDome.Determinism`. So the Picard–Lindelöf hypothesis, which the pendulum
> satisfies, fails for the dome. For the same reason the Euler–Lagrange theorem
> `euler_lagrange_varGradient`, which needs a smooth Lagrangian, does not apply, and the equation
> of motion is identified only with the vanishing of the pointwise Euler–Lagrange operator.

## ii. Key results

> - `NortonDome` holds the input data, the mass `m` and the gravitational acceleration `g`.
> - `NortonDome.height` is the depth `(2/(3g)) r^{3/2}` of the dome below its apex, with its
>   derivative `hasDerivAt_height` and `C¹` regularity `height_contDiff_one`.
> - `NortonDome.kineticEnergy`, `NortonDome.potentialEnergy` and `NortonDome.energy` are the
>   energies, with the gradient `gradient_potentialEnergy` of the potential and the time
>   derivatives `kineticEnergy_deriv`, `potentialEnergy_deriv` and `energy_deriv` along twice
>   differentiable curves.
> - `NortonDome.lagrangian` is the Lagrangian `T - V`, with its partial gradients
>   `gradient_lagrangian_position_eq` and `gradient_lagrangian_velocity_eq`.
> - `NortonDome.force` is the generalized force `m √r` conjugate to the arc length. It is
>   continuous, `force_continuous`, but not Lipschitz on any closed ball about the apex,
>   `not_lipschitzOnWith_force`.
> - `NortonDome.EquationOfMotion` is the equation of motion `m r̈ = F(r)`, with its scalar form
>   `equationOfMotion_iff_scalar`; `NortonDome.IsSolution` is a twice differentiable solution.
> - `NortonDome.equationOfMotion_iff_eulerLagrangeOp_zero` identifies the equation of motion,
>   for curves with differentiable velocity, with the vanishing of the Euler–Lagrange operator.
> - `NortonDome.IsSolution.energy_eq` is the conservation of energy along a solution.

## iv. References

> - Norton, J. D., *The dome: an unexpectedly simple failure of determinism*, Philosophy of
>   Science 75 (2008), 786–798.
> - Malament, D. B., *Norton's slippery slope*, Philosophy of Science 75 (2008), 799–816.

## A. The input data

> The dome is specified by the mass of the particle and the gravitational acceleration; its shape
> is fixed by Norton's formula.

**`ClassicalMechanics.NortonDome`**, a structure, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L122).

> The Norton dome is specified by the mass `m` of the particle sliding on it and the
> gravitational acceleration `g`, both positive. The configuration of the particle is the arc
> length from the apex.

```lean
structure NortonDome where
  /-- The mass of the particle. -/
  m : ℝ
  /-- The gravitational acceleration. -/
  g : ℝ
  m_pos : 0 < m
  g_pos : 0 < g
```

**`ClassicalMechanics.NortonDome.m_ne_zero`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L136).

> The mass of the particle is not equal to zero.

```lean
lemma m_ne_zero : S.m ≠ 0
```

**`ClassicalMechanics.NortonDome.g_ne_zero`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L140).

> The gravitational acceleration is not equal to zero.

```lean
lemma g_ne_zero : S.g ≠ 0
```

## B. The profile of the dome

> Norton's profile is the depth `h(r) = (2/(3g)) r^{3/2}` of the surface below the apex at arc
> length `r`, written here as `(2/(3g)) √r ^ 3` so that it is defined, and vanishes, for `r ≤ 0`.

### B.1. The height below the apex

**`ClassicalMechanics.NortonDome.height`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L159).

> The depth of the surface of the dome below its apex at arc length `r` from the apex,
> `(2/(3g)) r^{3/2}`. It vanishes at the apex and for negative arguments.

```lean
noncomputable def height (r : ℝ) : ℝ
```

**`ClassicalMechanics.NortonDome.height_eq`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L162).

> The depth of the dome below its apex, written out.

```lean
lemma height_eq (r : ℝ) : S.height r = 2 / (3 * S.g) * √r ^ 3
```

**`ClassicalMechanics.NortonDome.height_nonneg`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L165).

> The depth of the dome below its apex is non-negative.

```lean
lemma height_nonneg (r : ℝ) : 0 ≤ S.height r
```

**`ClassicalMechanics.NortonDome.height_eq_zero_iff`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L171).

> The depth of the dome below its apex vanishes exactly at and before the apex.

```lean
lemma height_eq_zero_iff (r : ℝ) : S.height r = 0 ↔ r ≤ 0
```

### B.2. The derivative of the profile

> The slope `√r / g` of the profile is continuous and vanishes at the apex, so the profile is
> `C¹`. The slope itself is not differentiable at the apex, so the profile is not `C²`.

**`ClassicalMechanics.NortonDome.hasDerivAt_height`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L186).

> The derivative of the depth of the dome with respect to the arc length is `√r / g`, at
> every `r`, including the apex.

```lean
lemma hasDerivAt_height (r : ℝ) : HasDerivAt S.height (√r / S.g) r
```

**`ClassicalMechanics.NortonDome.height_differentiable`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L193).

> The depth of the dome is a differentiable function of the arc length.

```lean
lemma height_differentiable : Differentiable ℝ S.height
```

**`ClassicalMechanics.NortonDome.deriv_height`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L197).

> The derivative of the depth of the dome with respect to the arc length is `√r / g`.

```lean
lemma deriv_height : deriv S.height = fun r => √r / S.g
```

**`ClassicalMechanics.NortonDome.height_contDiff_one`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L201).

> The depth of the dome is a `C¹` function of the arc length.

```lean
lemma height_contDiff_one : ContDiff ℝ 1 S.height
```

## C. The energies

> The kinetic energy is `½ m ṙ²`, `r` being the arc length so that the speed is `|ṙ|`, and the
> potential energy is `-m g h(r)`, normalized to vanish at the apex.

### C.1. The definitions of the energies

**`ClassicalMechanics.NortonDome.kineticEnergy`**, a def, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L224).

> The kinetic energy of the particle on the dome along a curve `r` of the arc length is
> `½ m ‖ṙ‖²`.

```lean
noncomputable def kineticEnergy (r : Time → EuclideanSpace ℝ (Fin 1)) : Time → ℝ
```

**`ClassicalMechanics.NortonDome.potentialEnergy`**, a def, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L230).

> The potential energy of the particle on the dome at arc length `x` from the apex is
> `-m g h(x 0)`, the gravitational potential at depth `h` below the apex, which vanishes at the
> apex.

```lean
noncomputable def potentialEnergy (x : EuclideanSpace ℝ (Fin 1)) : ℝ
```

**`ClassicalMechanics.NortonDome.energy`**, a def, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L234).

> The energy of the particle on the dome is the kinetic energy plus the potential energy.

```lean
noncomputable def energy (r : Time → EuclideanSpace ℝ (Fin 1)) : Time → ℝ
```

**`ClassicalMechanics.NortonDome.kineticEnergy_eq`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L238).

> The kinetic energy of the particle on the dome, written out.

```lean
lemma kineticEnergy_eq (r : Time → EuclideanSpace ℝ (Fin 1)) :
    S.kineticEnergy r = fun t => (1 / (2 : ℝ)) * S.m * ⟪∂ₜ r t, ∂ₜ r t⟫_ℝ
```

**`ClassicalMechanics.NortonDome.potentialEnergy_eq`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L243).

> The potential energy of the particle on the dome is `-(2m/3) r^{3/2}`: the gravitational
> acceleration cancels against the shape of the dome.

```lean
lemma potentialEnergy_eq (x : EuclideanSpace ℝ (Fin 1)) :
    S.potentialEnergy x = -(2 * S.m / 3) * √(x 0) ^ 3
```

**`ClassicalMechanics.NortonDome.energy_eq`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L249).

> The energy of the particle on the dome, written out.

```lean
lemma energy_eq (r : Time → EuclideanSpace ℝ (Fin 1)) :
    S.energy r = fun t => S.kineticEnergy r t + S.potentialEnergy (r t)
```

**`ClassicalMechanics.NortonDome.potentialEnergy_nonpos`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L254).

> The potential energy of the particle on the dome is non-positive, the apex being the
> highest point of the dome.

```lean
lemma potentialEnergy_nonpos (x : EuclideanSpace ℝ (Fin 1)) : S.potentialEnergy x ≤ 0
```

**`ClassicalMechanics.NortonDome.potentialEnergy_eq_zero_iff`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L260).

> The potential energy of the particle on the dome vanishes exactly at the apex, that is for
> arc length `≤ 0`.

```lean
lemma potentialEnergy_eq_zero_iff (x : EuclideanSpace ℝ (Fin 1)) :
    S.potentialEnergy x = 0 ↔ x 0 ≤ 0
```

### C.2. Differentiability and the gradient of the potential

> The potential energy is differentiable, with gradient `-m √r` times the unit vector of the
> arc-length coordinate. It is `C¹` but not `C²`, since `√r` is not differentiable at `0`.

**`ClassicalMechanics.NortonDome.differentiableAt_sqrt_coord_pow_three`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L276).

> The cube of the square root of the arc-length coordinate is differentiable on the Euclidean
> lift, at every point.

```lean
lemma differentiableAt_sqrt_coord_pow_three (x : EuclideanSpace ℝ (Fin 1)) :
    DifferentiableAt ℝ (fun y : EuclideanSpace ℝ (Fin 1) => √(y 0) ^ 3) x
```

**`ClassicalMechanics.NortonDome.differentiable_potentialEnergy`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L286).

> The potential energy of the particle on the dome is a differentiable function of the arc
> length.

```lean
lemma differentiable_potentialEnergy : Differentiable ℝ S.potentialEnergy
```

**`ClassicalMechanics.NortonDome.gradient_potentialEnergy`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L295).

> The gradient of the potential energy of the particle on the dome is `-m √r` times the unit
> vector of the arc-length coordinate.

```lean
lemma gradient_potentialEnergy (x : EuclideanSpace ℝ (Fin 1)) :
    gradient S.potentialEnergy x = -(S.m * √(x 0)) • EuclideanSpace.single 0 1
```

**`ClassicalMechanics.NortonDome.kineticEnergy_differentiable`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L307).

> Along a curve of the arc length with differentiable velocity the kinetic energy is
> differentiable in time.

```lean
lemma kineticEnergy_differentiable (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr' : Differentiable ℝ (∂ₜ r)) : Differentiable ℝ (S.kineticEnergy r)
```

**`ClassicalMechanics.NortonDome.potentialEnergy_differentiable`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L315).

> Along a differentiable curve of the arc length the potential energy is a differentiable
> function of the time.

```lean
lemma potentialEnergy_differentiable (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr : Differentiable ℝ r) : Differentiable ℝ (fun t => S.potentialEnergy (r t))
```

**`ClassicalMechanics.NortonDome.energy_differentiable`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L322).

> Along a twice differentiable curve of the arc length the energy is differentiable in
> time.

```lean
lemma energy_differentiable (r : Time → EuclideanSpace ℝ (Fin 1)) (hr : Differentiable ℝ r)
    (hr' : Differentiable ℝ (∂ₜ r)) : Differentiable ℝ (S.energy r)
```

### C.3. Time derivatives of the energies

> Along a twice differentiable curve, solution or not, the time derivatives of the energies are
> inner products against the velocity; the equation of motion makes the two contributions cancel.

**`ClassicalMechanics.NortonDome.kineticEnergy_deriv`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L337).

> The rate of change of the kinetic energy is the velocity paired with `m r̈`.

```lean
lemma kineticEnergy_deriv (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr' : Differentiable ℝ (∂ₜ r)) :
    ∂ₜ (S.kineticEnergy r) = fun t => ⟪∂ₜ r t, S.m • ∂ₜ (∂ₜ r) t⟫_ℝ
```

**`ClassicalMechanics.NortonDome.potentialEnergy_deriv`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L350).

> The rate of change of the potential energy is the velocity paired with the gradient of the
> potential.

```lean
lemma potentialEnergy_deriv (r : Time → EuclideanSpace ℝ (Fin 1)) (hr : Differentiable ℝ r) :
    ∂ₜ (fun t => S.potentialEnergy (r t)) =
      fun t => ⟪∂ₜ r t, gradient S.potentialEnergy (r t)⟫_ℝ
```

**`ClassicalMechanics.NortonDome.energy_deriv`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L361).

> The rate of change of the energy is the velocity paired with the sum of `m r̈` and the
> gradient of the potential; the equation of motion is exactly the vanishing of that sum.

```lean
lemma energy_deriv (r : Time → EuclideanSpace ℝ (Fin 1)) (hr : Differentiable ℝ r)
    (hr' : Differentiable ℝ (∂ₜ r)) :
    ∂ₜ (S.energy r) =
      fun t => ⟪∂ₜ r t, S.m • ∂ₜ (∂ₜ r) t + gradient S.potentialEnergy (r t)⟫_ℝ
```

## D. The Lagrangian

> The Lagrangian `L = ½ m ṙ² + m g h(r)` is a function on phase space. Unlike those of the
> harmonic oscillator and the pendulum it is only `C¹`; its partial gradients still exist, and
> are the force of section E and the momentum `m ṙ`.

**`ClassicalMechanics.NortonDome.lagrangian`**, a def, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L387).

> The Lagrangian of the particle on the dome, `L(t, r, ṙ) = ½ m ‖ṙ‖² - V(r)`, the kinetic
> energy minus the potential energy as a function on phase space. It does not depend on the
> time.

```lean
noncomputable def lagrangian (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) : ℝ
```

**`ClassicalMechanics.NortonDome.lagrangian_eq_kineticEnergy_sub_potentialEnergy`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L392).

> Along a curve of the arc length the Lagrangian of the particle on the dome is the kinetic
> energy minus the potential energy.

```lean
lemma lagrangian_eq_kineticEnergy_sub_potentialEnergy (t : Time)
    (r : Time → EuclideanSpace ℝ (Fin 1)) :
    S.lagrangian t (r t) (∂ₜ r t) = S.kineticEnergy r t - S.potentialEnergy (r t)
```

**`ClassicalMechanics.NortonDome.gradient_lagrangian_position_eq`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L399).

> The gradient of the Lagrangian of the particle on the dome in the arc length is minus the
> gradient of the potential energy, `m √r` times the unit vector of the arc-length
> coordinate.

```lean
lemma gradient_lagrangian_position_eq (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) :
    gradient (fun x => S.lagrangian t x v) x = (S.m * √(x 0)) • EuclideanSpace.single 0 1
```

**`ClassicalMechanics.NortonDome.gradient_lagrangian_velocity_eq`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L412).

> The gradient of the Lagrangian of the particle on the dome in the velocity is the momentum
> `m ṙ`.

```lean
lemma gradient_lagrangian_velocity_eq (t : Time) (x v : EuclideanSpace ℝ (Fin 1)) :
    gradient (S.lagrangian t x) v = S.m • v
```

## E. The force and the equation of motion

> Gravity exerts the generalized force `m √r` conjugate to the arc length, balanced against
> `m r̈`. As for the pendulum this pointwise relation is the definition of the equation of
> motion; the variational derivative of the action is not available, the Lagrangian not being
> smooth.

### E.1. The force

**`ClassicalMechanics.NortonDome.force`**, a def, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L441).

> The generalized force on the particle on the dome conjugate to the arc length, minus the
> gradient of the potential energy, `F = -∂V/∂r`.

```lean
noncomputable def force (x : EuclideanSpace ℝ (Fin 1)) : EuclideanSpace ℝ (Fin 1)
```

**`ClassicalMechanics.NortonDome.force_eq`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L446).

> The force on the particle on the dome is `m √r` times the unit vector of the arc-length
> coordinate: it points away from the apex, and vanishes there.

```lean
lemma force_eq (x : EuclideanSpace ℝ (Fin 1)) :
    S.force x = (S.m * √(x 0)) • EuclideanSpace.single 0 1
```

**`ClassicalMechanics.NortonDome.force_apply`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L451).

> The single component of the force on the particle on the dome is `m √r`.

```lean
lemma force_apply (x : EuclideanSpace ℝ (Fin 1)) : S.force x 0 = S.m * √(x 0)
```

**`ClassicalMechanics.NortonDome.force_zero`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L456).

> The force on the particle on the dome vanishes at the apex.

```lean
lemma force_zero : S.force 0 = 0
```

### E.2. Regularity of the force

> The force is continuous. It is not Lipschitz on any closed ball about the apex, since the square
> root is not Lipschitz on any `[0, ε]`: the Picard–Lindelöf hypothesis fails, which is the
> source of the non-uniqueness.

**`ClassicalMechanics.NortonDome.force_continuous`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L472).

> The force on the particle on the dome is a continuous function of the arc length.

```lean
lemma force_continuous : Continuous S.force
```

**`ClassicalMechanics.NortonDome.dist_smul_single`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L479).

> The distance between two multiples of the unit vector of the arc-length coordinate is the
> distance between the coefficients.

```lean
lemma dist_smul_single (a b : ℝ) :
    dist (a • EuclideanSpace.single (0 : Fin 1) (1 : ℝ)) (b • EuclideanSpace.single 0 1) =
      |a - b|
```

**`ClassicalMechanics.NortonDome.not_lipschitzOnWith_force`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L487).

> The force on the particle on the dome is not Lipschitz on any closed ball about the apex,
> for any Lipschitz constant.

```lean
lemma not_lipschitzOnWith_force (K : NNReal) {ε : ℝ} (hε : 0 < ε) :
    ¬ LipschitzOnWith K S.force (Metric.closedBall 0 ε)
```

### E.3. The equation of motion

**`ClassicalMechanics.NortonDome.EquationOfMotion`**, a def, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L516).

> The equation of motion of the particle on the dome: at every instant `m r̈` equals the
> generalized force `F(r) = m √r`. This pointwise relation is the definition; for curves with
> differentiable velocity it is the vanishing of the Euler–Lagrange operator of the Lagrangian,
> `equationOfMotion_iff_eulerLagrangeOp_zero`.

```lean
def EquationOfMotion (r : Time → EuclideanSpace ℝ (Fin 1)) : Prop
```

**`ClassicalMechanics.NortonDome.equationOfMotion_iff_newtons_2nd_law`**, a lemma, [line 522](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L522).

> The equation of motion with all terms on one side: at every instant `m r̈` plus the
> gradient of the potential energy vanishes. This is the combination `energy_deriv` pairs with
> the velocity.

```lean
lemma equationOfMotion_iff_newtons_2nd_law (r : Time → EuclideanSpace ℝ (Fin 1)) :
    S.EquationOfMotion r ↔
      ∀ t, S.m • ∂ₜ (∂ₜ r) t + gradient S.potentialEnergy (r t) = 0
```

**`ClassicalMechanics.NortonDome.equationOfMotion_iff_scalar`**, a lemma, [line 529](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L529).

> The equation of motion of the particle on the dome in scalar form, `r̈ = √r`. Both the mass
> and the gravitational acceleration have cancelled.

```lean
lemma equationOfMotion_iff_scalar (r : Time → EuclideanSpace ℝ (Fin 1)) :
    S.EquationOfMotion r ↔ ∀ t, ∂ₜ (∂ₜ r) t 0 = √(r t 0)
```

### E.4. Solutions

> A solution is a twice differentiable curve, position and velocity both differentiable, satisfying
> the equation of motion: the regularity of `ClassicalMechanics.ReferenceFrame.Particle` and the
> least under which the acceleration exists. Regularity is part of the definition because the bare
> pointwise equation, whose derivatives are zero wherever they do not exist, admits rough accidental
> solutions. Smoothness is not demanded: the motions leaving the apex are `C³` but not `C⁴`.

**`ClassicalMechanics.NortonDome.IsSolution`**, a def, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L557).

> A solution of the dome is a twice differentiable curve of the arc length, its position and
> velocity both differentiable, satisfying the equation of motion.

```lean
def IsSolution (r : Time → EuclideanSpace ℝ (Fin 1)) : Prop
```

**`ClassicalMechanics.NortonDome.IsSolution.differentiable`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L561).

> The position along a solution of the dome is differentiable.

```lean
lemma IsSolution.differentiable {S : NortonDome} {r : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution r) : Differentiable ℝ r
```

**`ClassicalMechanics.NortonDome.IsSolution.deriv_differentiable`**, a lemma, [line 565](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L565).

> The velocity along a solution of the dome is differentiable.

```lean
lemma IsSolution.deriv_differentiable {S : NortonDome} {r : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution r) : Differentiable ℝ (∂ₜ r)
```

**`ClassicalMechanics.NortonDome.IsSolution.equationOfMotion`**, a lemma, [line 569](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L569).

> A solution of the dome satisfies the equation of motion.

```lean
lemma IsSolution.equationOfMotion {S : NortonDome} {r : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution r) : S.EquationOfMotion r
```

## F. The Euler–Lagrange operator

> With the gradients of section D, the pointwise Euler–Lagrange operator along any curve with
> differentiable velocity is the force minus `m r̈`, so its vanishing is the equation of motion.
> The identification of this operator with the variational derivative of the action,
> `euler_lagrange_varGradient`, needs a smooth Lagrangian and so does not apply to the dome.

**`ClassicalMechanics.NortonDome.eulerLagrangeOp_lagrangian`**, a lemma, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L585).

> Along a curve of the arc length with differentiable velocity the Euler–Lagrange operator of
> the Lagrangian of the dome is the force minus `m r̈`.

```lean
lemma eulerLagrangeOp_lagrangian (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr' : Differentiable ℝ (∂ₜ r)) :
    eulerLagrangeOp S.lagrangian r = fun t => S.force (r t) - S.m • ∂ₜ (∂ₜ r) t
```

**`ClassicalMechanics.NortonDome.equationOfMotion_iff_eulerLagrangeOp_zero`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L595).

> For a curve of the arc length with differentiable velocity the equation of motion of the
> dome holds if and only if the Euler–Lagrange operator of its Lagrangian vanishes along it.

```lean
lemma equationOfMotion_iff_eulerLagrangeOp_zero (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr' : Differentiable ℝ (∂ₜ r)) :
    S.EquationOfMotion r ↔ eulerLagrangeOp S.lagrangian r = 0
```

## G. Energy conservation

> Along any twice differentiable curve satisfying the equation of motion the energy is constant.
> This follows from `energy_deriv`. Conservation of energy does not restore uniqueness: the motion
> at rest at the apex and every motion leaving it all have zero energy, which is proved in
> `NortonDome.Solution` as `energy_rest` and `energy_solution`.

**`ClassicalMechanics.NortonDome.energy_conservation_of_equationOfMotion`**, a lemma, [line 615](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L615).

> Along a twice differentiable curve of the arc length satisfying the equation of motion the
> time derivative of the energy of the dome vanishes.

```lean
lemma energy_conservation_of_equationOfMotion (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr : Differentiable ℝ r) (hr' : Differentiable ℝ (∂ₜ r)) (h : S.EquationOfMotion r) :
    ∂ₜ (S.energy r) = 0
```

**`ClassicalMechanics.NortonDome.energy_conservation_of_equationOfMotion'`**, a lemma, [line 625](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L625).

> Along a twice differentiable curve of the arc length satisfying the equation of motion the
> energy of the dome at any time is equal to its initial value.

```lean
lemma energy_conservation_of_equationOfMotion' (r : Time → EuclideanSpace ℝ (Fin 1))
    (hr : Differentiable ℝ r) (hr' : Differentiable ℝ (∂ₜ r)) (h : S.EquationOfMotion r)
    (t : Time) : S.energy r t = S.energy r 0
```

**`ClassicalMechanics.NortonDome.IsSolution.energy_eq`**, a lemma, [line 636](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean#L636).

> The energy of the dome along a solution at any time is equal to its initial value.

```lean
lemma IsSolution.energy_eq {S : NortonDome} {r : Time → EuclideanSpace ℝ (Fin 1)}
    (h : S.IsSolution r) (t : Time) : S.energy r t = S.energy r 0
```

## Depends on

- [A. Euler–Lagrange equations](../../../physlib/classicalmechanics/eulerlagrange.md)

## Proof depends on

- [The Classical Harmonic Oscillator](../../../physlib/classicalmechanics/harmonicoscillator/basic.md)
- [Calculus of the real square root near zero](sqrt.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/NortonDome/Basic.lean)
