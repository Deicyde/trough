---
declaration: module
origin: cited
lean: RigidBodyMotion.velocity_eq_angularVelocity, RigidBodyMotion.angularVelocityTensor, RigidBodyMotion.angularVelocityTensor_eq, RigidBodyMotion.angularVelocityTensor_transpose, RigidBodyMotion.angularVelocityTensor_of_orientation_const, RigidBodyMotion.angularVelocity, RigidBodyMotion.angularVelocity_eq, RigidBodyMotion.crossProductMatrix_angularVelocity
statement: formalized
proof: formalized
---

# The angular velocity of a rigid body

The module `Physlib.ClassicalMechanics.RigidBody.AngularVelocity`, [Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean): 23 declarations, 19 with a docstring, 1 listed as significant.

> For a rigid body in motion the orientation `R(t) = orientation t` is a time-dependent rotation. Its
> instantaneous rate of change is encoded by the *angular velocity tensor*
> `Ω(t) = Ṙ(t) R(t)ᵀ`, the antisymmetric tensor `Ω` appearing in the Landau–Lifshitz decomposition
> `v = V + Ω × r` of the velocity of a point of the body.
>
> A basic consistency check is that `Ω` is skew-symmetric, `Ωᵀ = -Ω` (equivalently `Ω ∈ 𝔰𝔬(d)`); this
> follows by differentiating the orthogonality identity `R Rᵀ = 1`. The general product and transpose
> rules for time derivatives of matrices used for this live in
> `Physlib.SpaceAndTime.Time.MatrixDerivatives`.
>
> In three dimensions the skew-symmetric tensor `Ω` is dual to the *angular velocity vector*
> `ω(t) = Ωᵛ` via the hat map (`Physlib.Mathematics.Modules.CrossProductMatrix`), with
> `[ω]ₓ = Ω`; `ω` is the angular velocity proper, appearing in the decomposition `v = V + ω × r`
> as an honest cross product.
>
> The angular velocity can equally be expressed in the *body frame*: the moving coordinate system
> rigidly attached to the body, with origin at the centre of mass and axes rotating with the body,
> in which every material point has time-independent coordinates. The orientation `R(t)` is
> precisely the rotational part of the change of frame: a point fixed at position `a` in the body
> frame sits at `r = R(t) a` relative to the centre of mass in the lab frame (the inertial frame in
> which the trajectories of `RigidBodyMotion` are written), and a vector with lab-frame components
> `u` has body-frame components `R(t)ᵀ u`. The body frame is in general *not* inertial — it rotates
> with the body, and its origin follows the (generally accelerating) centre of mass — but it is the
> natural setting for the inertia tensor and Euler's equations, since the mass distribution, and
> with it the inertia tensor, is time-independent in body-fixed axes.
>
> The *body-frame angular velocity tensor* `Ω_body(t) = R(t)ᵀ Ṙ(t)` is defined directly from the
> orientation, mirroring the spatial `Ω = Ṙ Rᵀ` rather than being derived from it — the two tensors
> are the derivative `Ṙ` translated back to the identity from the two sides — and they are related
> by conjugation, `Ω_body = Rᵀ Ω R`. The body-frame tensor is again skew-symmetric; in three
> dimensions its dual is the *body-frame angular velocity vector* `ω_body = Ω_bodyᵛ`, the angular
> velocity `ω` resolved along the body-fixed axes, `ω_body = Rᵀ ω`.

## References

> * Landau and Lifshitz, Mechanics, Sections 31 and 32. [ref: landau\_mechanics]

**`RigidBodyMotion.angularVelocityTensor`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L66).

> The angular velocity tensor `Ω(t) = Ṙ(t) R(t)ᵀ` of a rigid body in motion, where
> `R(t) = orientation t`. It is the antisymmetric tensor `Ω` in the Landau–Lifshitz decomposition
> `v = V + Ω × r` of the velocity of a point of the body.

```lean
noncomputable def angularVelocityTensor (M : RigidBodyMotion d) (t : Time) :
    Matrix (Fin d) (Fin d) ℝ
```

**`RigidBodyMotion.angularVelocityTensor_eq`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L70).

```lean
lemma angularVelocityTensor_eq (M : RigidBodyMotion d) (t : Time) :
    M.angularVelocityTensor t = ∂ₜ (fun s => (M.orientation s).1) t * ((M.orientation t).1)ᵀ
```

**`RigidBodyMotion.angularVelocityTensor_transpose`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L77).

> The angular velocity tensor is skew-symmetric, `Ωᵀ = -Ω`: it lies in the Lie algebra `𝔰𝔬(d)`.
> This is the litmus check that `Ω = Ṙ Rᵀ` is a genuine angular-velocity tensor, and follows by
> differentiating the orthogonality identity `R Rᵀ = 1`.

```lean
lemma angularVelocityTensor_transpose (M : RigidBodyMotion d) (t : Time)
    (hR : DifferentiableAt ℝ (fun s => (M.orientation s).1) t) :
    (M.angularVelocityTensor t)ᵀ = - M.angularVelocityTensor t
```

**`RigidBodyMotion.angularVelocityTensor_of_orientation_const`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L94).

> A rigid body whose orientation is constant in time has zero angular velocity.

```lean
lemma angularVelocityTensor_of_orientation_const (M : RigidBodyMotion d)
    (R : Matrix.specialOrthogonalGroup (Fin d) ℝ) (h : M.orientation = fun _ => R) :
    M.angularVelocityTensor = 0
```

**`RigidBodyMotion.angularVelocity`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L108).

> The angular velocity *vector* `ω(t)` of a rigid body moving in three-dimensional space: the
> vector dual to the angular velocity tensor `Ω(t)` under the hat map, `ω = Ωᵛ`. It is the angular
> velocity `ω` in the Landau–Lifshitz decomposition `v = V + ω × r` of the velocity of a point of the
> body, where `ω × r` is the cross product with `ω`.

```lean
noncomputable def angularVelocity (M : RigidBodyMotion 3) (t : Time) : Fin 3 → ℝ
```

**`RigidBodyMotion.angularVelocity_eq`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L111).

```lean
lemma angularVelocity_eq (M : RigidBodyMotion 3) (t : Time) :
    M.angularVelocity t = crossProductVee (M.angularVelocityTensor t)
```

**`RigidBodyMotion.crossProductMatrix_angularVelocity`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L117).

> The hat map recovers the angular velocity tensor from the angular velocity vector, `[ω]ₓ = Ω`.
> This is the defining relationship between the vector and tensor forms of the angular velocity in
> three dimensions; it holds because `Ω` is skew-symmetric.

```lean
lemma crossProductMatrix_angularVelocity (M : RigidBodyMotion 3) (t : Time)
    (hR : DifferentiableAt ℝ (fun s => (M.orientation s).1) t) :
    crossProductMatrix (M.angularVelocity t) = M.angularVelocityTensor t
```

**`RigidBodyMotion.angularVelocity_of_orientation_const`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L124).

> A rigid body whose orientation is constant in time has zero angular velocity vector.

```lean
lemma angularVelocity_of_orientation_const (M : RigidBodyMotion 3)
    (R : Matrix.specialOrthogonalGroup (Fin 3) ℝ) (h : M.orientation = fun _ => R) :
    M.angularVelocity = 0
```

**`RigidBodyMotion.angularVelocityTensor_mul_orientation`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L133).

> The time derivative of the orientation is `Ṙ = Ω R`, recovering the orientation path from its
> angular velocity tensor `Ω = Ṙ Rᵀ` via the orthogonality `Rᵀ R = 1`.

```lean
lemma angularVelocityTensor_mul_orientation (M : RigidBodyMotion d) (t : Time) :
    M.angularVelocityTensor t * (M.orientation t).1 = ∂ₜ (fun s => (M.orientation s).1) t
```

**`RigidBodyMotion.deriv_orientation_mulVec_eq_angularVelocity_cross`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L141).

> The rotational part of the velocity of the body point `y` is the cross product of the
> angular velocity with the point's position relative to the centre of mass:
> `Ṙ(t) (y − c) = ω(t) × (displacement t y − comTrajectory t)`.

```lean
lemma deriv_orientation_mulVec_eq_angularVelocity_cross (M : RigidBodyMotion 3) (y : Space 3)
    (t : Time) (hR : DifferentiableAt ℝ (fun s => (M.orientation s).1) t) :
    ∂ₜ (fun s => (M.orientation s).1) t *ᵥ (fun j => y j - M.centerOfMass j)
      = M.angularVelocity t ⨯₃ fun j => M.displacement t y j - M.comTrajectory t j
```

**`RigidBodyMotion.velocity_eq_angularVelocity`**, a theorem, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L152). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Landau–Lifshitz velocity decomposition `v = V + ω × r` for a rigid body in three
> dimensions: the velocity of a body point is the centre-of-mass velocity plus the cross product of
> the angular velocity with the point's position relative to the centre of mass.

```lean
theorem velocity_eq_angularVelocity (M : RigidBodyMotion 3) (y : Space 3) (t : Time) (i : Fin 3)
    (hR : Differentiable ℝ (fun s => (M.orientation s).1)) (hX : Differentiable ℝ M.comTrajectory) :
    M.velocity y t i = M.centerOfMassVelocity t i
        + (M.angularVelocity t ⨯₃ fun j => M.displacement t y j - M.comTrajectory t j) i
```

**`RigidBodyMotion.bodyAngularVelocityTensor`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L161).

> The body-frame (co-rotating) angular velocity tensor `Ω_body(t) = R(t)ᵀ Ṙ(t)` of a rigid body
> in motion, where `R(t) = orientation t`.

```lean
noncomputable def bodyAngularVelocityTensor (M : RigidBodyMotion d) (t : Time) :
    Matrix (Fin d) (Fin d) ℝ
```

**`RigidBodyMotion.bodyAngularVelocityTensor_eq`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L165).

```lean
lemma bodyAngularVelocityTensor_eq (M : RigidBodyMotion d) (t : Time) :
    M.bodyAngularVelocityTensor t = ((M.orientation t).1)ᵀ * ∂ₜ (fun s => (M.orientation s).1) t
```

**`RigidBodyMotion.orientation_mul_bodyAngularVelocityTensor`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L171).

> The time derivative of the orientation is `Ṙ = R Ω_body`, recovering the orientation path from
> its body-frame angular velocity tensor via the orthogonality `R Rᵀ = 1`.

```lean
lemma orientation_mul_bodyAngularVelocityTensor (M : RigidBodyMotion d) (t : Time) :
    (M.orientation t).1 * M.bodyAngularVelocityTensor t = ∂ₜ (fun s => (M.orientation s).1) t
```

**`RigidBodyMotion.angularVelocityTensor_eq_orientation_conj`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L177).

> The spatial tensor is the body-frame tensor rotated into the inertial frame,
> `Ω = R Ω_body Rᵀ`.

```lean
lemma angularVelocityTensor_eq_orientation_conj (M : RigidBodyMotion d) (t : Time) :
    M.angularVelocityTensor t
      = (M.orientation t).1 * M.bodyAngularVelocityTensor t * ((M.orientation t).1)ᵀ
```

**`RigidBodyMotion.bodyAngularVelocityTensor_eq_orientation_conj`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L184).

> The body-frame tensor is the spatial tensor conjugated into the body frame,
> `Ω_body = Rᵀ Ω R`.

```lean
lemma bodyAngularVelocityTensor_eq_orientation_conj (M : RigidBodyMotion d) (t : Time) :
    M.bodyAngularVelocityTensor t
      = ((M.orientation t).1)ᵀ * M.angularVelocityTensor t * (M.orientation t).1
```

**`RigidBodyMotion.bodyAngularVelocityTensor_transpose`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L192).

> The body-frame angular velocity tensor is skew-symmetric, `Ω_bodyᵀ = -Ω_body`: it lies in the
> Lie algebra `𝔰𝔬(d)`, inherited from the spatial tensor by conjugation.

```lean
lemma bodyAngularVelocityTensor_transpose (M : RigidBodyMotion d) (t : Time)
    (hR : DifferentiableAt ℝ (fun s => (M.orientation s).1) t) :
    (M.bodyAngularVelocityTensor t)ᵀ = - M.bodyAngularVelocityTensor t
```

**`RigidBodyMotion.bodyAngularVelocity`**, a def, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L201).

> The body-frame angular velocity *vector* `ω_body(t)` of a rigid body moving in three-dimensional
> space: the vector dual to the body-frame angular velocity tensor `Ω_body(t)` under the hat map,
> `ω_body = Ω_bodyᵛ`.

```lean
noncomputable def bodyAngularVelocity (M : RigidBodyMotion 3) (t : Time) : Fin 3 → ℝ
```

**`RigidBodyMotion.bodyAngularVelocity_eq`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L204).

```lean
lemma bodyAngularVelocity_eq (M : RigidBodyMotion 3) (t : Time) :
    M.bodyAngularVelocity t = crossProductVee (M.bodyAngularVelocityTensor t)
```

**`RigidBodyMotion.crossProductMatrix_bodyAngularVelocity`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L209).

> The hat map recovers the body-frame angular velocity tensor from the body-frame angular
> velocity vector, `[ω_body]ₓ = Ω_body`; it holds because `Ω_body` is skew-symmetric.

```lean
lemma crossProductMatrix_bodyAngularVelocity (M : RigidBodyMotion 3) (t : Time)
    (hR : DifferentiableAt ℝ (fun s => (M.orientation s).1) t) :
    crossProductMatrix (M.bodyAngularVelocity t) = M.bodyAngularVelocityTensor t
```

**`RigidBodyMotion.bodyAngularVelocityTensor_of_orientation_const`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L217).

> A rigid body whose orientation is constant in time has zero body-frame angular velocity
> tensor.

```lean
lemma bodyAngularVelocityTensor_of_orientation_const (M : RigidBodyMotion d)
    (R : Matrix.specialOrthogonalGroup (Fin d) ℝ) (h : M.orientation = fun _ => R) :
    M.bodyAngularVelocityTensor = 0
```

**`RigidBodyMotion.bodyAngularVelocity_of_orientation_const`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L229).

> A rigid body whose orientation is constant in time has zero body-frame angular velocity
> vector.

```lean
lemma bodyAngularVelocity_of_orientation_const (M : RigidBodyMotion 3)
    (R : Matrix.specialOrthogonalGroup (Fin 3) ℝ) (h : M.orientation = fun _ => R) :
    M.bodyAngularVelocity = 0
```

**`RigidBodyMotion.deriv_orientation_mulVec_eq_orientation_bodyAngularVelocity_cross`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean#L239).

> The rotational velocity written through the body-frame angular velocity,
> `Ṙ(t) v = R(t) (ω_body(t) × v)`: the derivative of the orientation acts as the body-frame angular
> velocity `ω_body` crossed with `v`, rotated back into the inertial frame by `R`.

```lean
lemma deriv_orientation_mulVec_eq_orientation_bodyAngularVelocity_cross (M : RigidBodyMotion 3)
    (v : Fin 3 → ℝ) (t : Time)
    (hR : DifferentiableAt ℝ (fun s => (M.orientation s).1) t) :
    ∂ₜ (fun s => (M.orientation s).1) t *ᵥ v
      = (M.orientation t).1 *ᵥ (M.bodyAngularVelocity t ⨯₃ v)
```

## Depends on

- [Rigid body motion](motion.md)
- [The hat map on three-dimensional vectors](../../mathematics/modules/crossproductmatrix.md)

## Sources

- [Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularVelocity.lean)
