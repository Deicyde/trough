---
declaration: module
origin: cited
lean: RigidBodyMotion, RigidBodyMotion.orientation_mul_transpose, RigidBodyMotion.centerOfMassVelocity, RigidBodyMotion.centerOfMassVelocity_eq, RigidBodyMotion.centerOfMassVelocity_of_comTrajectory_const, RigidBodyMotion.linearMomentum, RigidBodyMotion.linearMomentum_eq, RigidBodyMotion.displacement
statement: formalized
proof: formalized
---

# Rigid body motion

The module `Physlib.ClassicalMechanics.RigidBody.Motion`, [Physlib/ClassicalMechanics/RigidBody/Motion.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean): 25 declarations, 21 with a docstring; 1 private, not shown.

> The static `RigidBody` records a body-fixed mass distribution. To describe a rigid body *in
> motion* we record, in addition, the trajectory of its centre of mass in the inertial frame and the
> body's time-dependent orientation (a rotation about the centre of mass).
>
> From this configuration we define the velocity of the centre of mass and the body's linear
> momentum. The reference point is taken to be the centre of mass, following the decomposition of
> a rigid motion into a translation of the centre of mass plus a rotation about it.

## References

> * Landau and Lifshitz, Mechanics, Section 32. [ref: landau\_mechanics]

**`RigidBodyMotion`**, a structure, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L38).

> A motion of a rigid body in `d`-dimensional space: the body together with the inertial-frame
> trajectory of its centre of mass and its time-dependent orientation (a rotation about the centre
> of mass).

```lean
structure RigidBodyMotion (d : ℕ) extends RigidBody d where
  /-- The position of the centre of mass in the inertial frame as a function of time. -/
  comTrajectory : Time → Space d
  /-- The orientation of the body, a rotation about the centre of mass, as a function of time. -/
  orientation : Time → Matrix.specialOrthogonalGroup (Fin d) ℝ
```

**`RigidBodyMotion.orientation_mul_transpose`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L47).

> The orientation matrix is special orthogonal, so `R Rᵀ = 1`.

```lean
lemma orientation_mul_transpose {d : ℕ} (M : RigidBodyMotion d) (t : Time) :
    (M.orientation t).1 * ((M.orientation t).1)ᵀ = 1
```

**`RigidBodyMotion.centerOfMassVelocity`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L55).

> The velocity of the centre of mass of a rigid body in motion, defined as the time-derivative
> of its centre-of-mass trajectory. This is the velocity `V` in the Landau–Lifshitz decomposition
> `v = V + Ω × r` of the velocity of a point of the body.

```lean
noncomputable def centerOfMassVelocity {d : ℕ} (M : RigidBodyMotion d) :
    Time → EuclideanSpace ℝ (Fin d)
```

**`RigidBodyMotion.centerOfMassVelocity_eq`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L59).

```lean
lemma centerOfMassVelocity_eq {d : ℕ} (M : RigidBodyMotion d) :
    M.centerOfMassVelocity = ∂ₜᵥ M.comTrajectory
```

**`RigidBodyMotion.centerOfMassVelocity_of_comTrajectory_const`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L63).

> A rigid body whose centre of mass is stationary has zero centre-of-mass velocity.

```lean
lemma centerOfMassVelocity_of_comTrajectory_const {d : ℕ} (M : RigidBodyMotion d) (c : Space d)
    (h : M.comTrajectory = fun _ => c) : M.centerOfMassVelocity = 0
```

**`RigidBodyMotion.linearMomentum`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L71).

> The linear momentum of a rigid body in motion: the total mass times the velocity of the
> centre of mass.

```lean
noncomputable def linearMomentum {d : ℕ} (M : RigidBodyMotion d) :
    Time → EuclideanSpace ℝ (Fin d)
```

**`RigidBodyMotion.linearMomentum_eq`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L75).

```lean
lemma linearMomentum_eq {d : ℕ} (M : RigidBodyMotion d) :
    M.linearMomentum = fun t => M.mass • M.centerOfMassVelocity t
```

**`RigidBodyMotion.displacement`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L84).

> The rigid displacement carrying the body frame into the inertial frame at time `t`: the
> rotation `orientation t` about the centre of mass, followed by the translation placing the centre
> of mass at `comTrajectory t`.

```lean
noncomputable def displacement {d : ℕ} (M : RigidBodyMotion d) (t : Time) : Space d → Space d
```

**`RigidBodyMotion.displacement_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L89).

> The `k`-th coordinate of the rigid displacement applied to `y`.

```lean
lemma displacement_apply {d : ℕ} (M : RigidBodyMotion d) (t : Time) (y : Space d) (k : Fin d) :
    M.displacement t y k =
      (∑ j, (M.orientation t).val k j * (y j - M.centerOfMass j)) + M.comTrajectory t k
```

**`RigidBodyMotion.displacement_contDiff`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L93).

```lean
lemma displacement_contDiff {d : ℕ} (M : RigidBodyMotion d) (t : Time) :
    ContDiff ℝ ⊤ (M.displacement t)
```

**`RigidBodyMotion.orientation_mulVec_sub_centerOfMass`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L101).

> Rotating the body-frame position of `y` relative to the centre of mass gives its
> inertial-frame position relative to the moving centre of mass:
> `R(t) (y − c) = displacement t y − comTrajectory t`.

```lean
lemma orientation_mulVec_sub_centerOfMass {d : ℕ} (M : RigidBodyMotion d) (t : Time)
    (y : Space d) :
    (M.orientation t).1 *ᵥ (fun j => y j - M.centerOfMass j)
      = fun j => M.displacement t y j - M.comTrajectory t j
```

**`RigidBodyMotion.massDistribution`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L115).

> The mass distribution of the rigid body in motion at time `t`: the pushforward of the
> body-fixed mass distribution along the rigid displacement, acting on a test function `f` by
> `f ↦ ρ (f ∘ displacement t)`.

```lean
noncomputable def massDistribution {d : ℕ} (M : RigidBodyMotion d) (t : Time) : RigidBody d
```

**`RigidBodyMotion.massDistribution_mass`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L124).

> The motion preserves the total mass: the mass distribution at any time `t` has the same total
> mass as the body.

```lean
lemma massDistribution_mass {d : ℕ} (M : RigidBodyMotion d) (t : Time) :
    (M.massDistribution t).mass = M.mass
```

**`RigidBodyMotion.massDistribution_centerOfMass`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L144).

> The centre of mass of the moving mass distribution tracks the prescribed trajectory: for a
> body of nonzero mass, the centre of mass of `massDistribution M t` is exactly `comTrajectory t`.
> This is the decisive check that `comTrajectory` and `orientation` are wired correctly in
> `RigidBodyMotion`.

```lean
lemma massDistribution_centerOfMass {d : ℕ} (M : RigidBodyMotion d) (t : Time) (h : M.mass ≠ 0) :
    (M.massDistribution t).centerOfMass = M.comTrajectory t
```

**`RigidBodyMotion.velocity`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L171).

> The velocity of the material point `y` of a rigid body in motion: the inertial-frame time
> derivative of the trajectory `s ↦ displacement s y` of that point.

```lean
noncomputable def velocity {d : ℕ} (M : RigidBodyMotion d) (y : Space d) :
    Time → EuclideanSpace ℝ (Fin d)
```

**`RigidBodyMotion.velocity_eq`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L175).

```lean
lemma velocity_eq {d : ℕ} (M : RigidBodyMotion d) (y : Space d) (t : Time) :
    M.velocity y t = ∂ₜᵥ (fun s => M.displacement s y) t
```

**`RigidBodyMotion.velocity_apply`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L180).

> The `i`-th component of the velocity of a body point is the time derivative of the `i`-th
> coordinate of its inertial-frame trajectory.

```lean
lemma velocity_apply {d : ℕ} (M : RigidBodyMotion d) (y : Space d) (t : Time) (i : Fin d)
    (hd : Differentiable ℝ (fun s => M.displacement s y)) :
    M.velocity y t i = ∂ₜ (fun s => M.displacement s y i) t
```

**`RigidBodyMotion.velocity_centerOfMass`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L189).

> The material point at the centre of mass moves with the centre-of-mass velocity, for any
> motion: `v(centreOfMass) = V`. This is the velocity counterpart of `massDistribution_centerOfMass`.

```lean
lemma velocity_centerOfMass {d : ℕ} (M : RigidBodyMotion d) :
    M.velocity M.centerOfMass = M.centerOfMassVelocity
```

**`RigidBodyMotion.velocity_of_orientation_const`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L201).

> A rigid body in pure translation (constant orientation) has every point moving with the
> centre-of-mass velocity: `v = V`.

```lean
lemma velocity_of_orientation_const {d : ℕ} (M : RigidBodyMotion d) (y : Space d)
    (R : Matrix.specialOrthogonalGroup (Fin d) ℝ) (h : M.orientation = fun _ => R) :
    M.velocity y = M.centerOfMassVelocity
```

**`RigidBodyMotion.velocity_eq_deriv_orientation`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L218).

> The velocity of a body point decomposes as `v = Ṙ (y − c) + V`: the rate of change of the
> orientation acting on the body-frame position, plus the centre-of-mass velocity.

```lean
lemma velocity_eq_deriv_orientation {d : ℕ} (M : RigidBodyMotion d) (y : Space d) (t : Time)
    (i : Fin d) (hR : Differentiable ℝ (fun s => (M.orientation s).1))
    (hX : Differentiable ℝ M.comTrajectory) :
    M.velocity y t i
      = (∂ₜ (fun s => (M.orientation s).1) t *ᵥ fun j => y j - M.centerOfMass j) i
        + M.centerOfMassVelocity t i
```

**`RigidBodyMotion.velocityClosedForm`**, a def, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L257).

> The closed form `Ṙ(t) (y − c) + V(t)` of the velocity of the body point `y` at time `t`.
> Unlike `velocity` — whose junk values on non-differentiable motions need not vary continuously
> with `y` — it is polynomial in `y` for any motion, so its squared speed can be bundled as the
> smooth integrand of the total kinetic energy; for differentiable motions the two agree, see
> `velocityClosedForm_eq_velocity`.

```lean
noncomputable def velocityClosedForm {d : ℕ} (M : RigidBodyMotion d) (t : Time) (y : Space d) :
    EuclideanSpace ℝ (Fin d)
```

**`RigidBodyMotion.velocityClosedForm_apply`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L263).

> The `i`-th coordinate of the closed-form velocity.

```lean
lemma velocityClosedForm_apply {d : ℕ} (M : RigidBodyMotion d) (t : Time) (y : Space d)
    (i : Fin d) :
    M.velocityClosedForm t y i
      = (∂ₜ (fun s => (M.orientation s).1) t *ᵥ fun j => y j - M.centerOfMass j) i
        + M.centerOfMassVelocity t i
```

**`RigidBodyMotion.velocityClosedForm_val`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L271).

> The closed-form velocity as a plain vector-valued function of the coordinates of `y`.

```lean
lemma velocityClosedForm_val {d : ℕ} (M : RigidBodyMotion d) (t : Time) (y : Space d) :
    (M.velocityClosedForm t y : Fin d → ℝ)
      = (∂ₜ (fun s => (M.orientation s).1) t *ᵥ fun j => y j - M.centerOfMass j)
        + (M.centerOfMassVelocity t : Fin d → ℝ)
```

**`RigidBodyMotion.velocityClosedForm_eq_velocity`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L280).

> For a differentiable motion the closed-form velocity is the honest point velocity.

```lean
lemma velocityClosedForm_eq_velocity {d : ℕ} (M : RigidBodyMotion d) (t : Time)
    (hR : Differentiable ℝ (fun s => (M.orientation s).1))
    (hX : Differentiable ℝ M.comTrajectory) (y : Space d) :
    M.velocityClosedForm t y = M.velocity y t
```

**`RigidBodyMotion.contDiff_velocityClosedForm_inner`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean#L288).

> The squared speed of a body point, in closed form, is a smooth function of the point.

```lean
lemma contDiff_velocityClosedForm_inner {d : ℕ} (M : RigidBodyMotion d) (t : Time) :
    ContDiff ℝ ⊤ fun y : Space d => (⟪M.velocityClosedForm t y, M.velocityClosedForm t y⟫_ℝ)
```

## Depends on

- [Rigid bodies](basic.md)
- [Time Derivatives](../../spaceandtime/time/derivatives.md)

## Proof depends on

- [Time derivatives of matrix-valued functions](../../spaceandtime/time/matrixderivatives.md)

## Sources

- [Physlib/ClassicalMechanics/RigidBody/Motion.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Motion.lean)
