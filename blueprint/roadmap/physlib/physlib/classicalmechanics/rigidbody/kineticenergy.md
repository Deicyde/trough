---
declaration: module
origin: cited
lean: RigidBody.rotationalKineticEnergy_eq_integral, RigidBodyMotion.kineticEnergy_eq_translational_add_rotational, RigidBodyMotion.kineticEnergy_eq_translational_add_angularVelocity, RigidBodyMotion.kineticEnergy_eq_translational_add_bodyAngularVelocity, RigidBody.rotationalKineticEnergy, RigidBody.rotationalKineticEnergy_eq_angularMomentum, RigidBodyMotion.kineticEnergy, RigidBodyMotion.kineticEnergy_eq_integral_velocity
statement: formalized
proof: formalized
---

# Kinetic energy of a rigid body

The module `Physlib.ClassicalMechanics.RigidBody.KineticEnergy`, [Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean): 9 declarations, 9 with a docstring, 4 listed as significant.

> For a rigid body rotating with angular velocity `ω` about its reference point the point at
> position `r` has velocity `ω × r`, so its kinetic energy is `T = ½ ∫ |ω × r|² dm`. Since
> `|ω × r|² = ω · (r × (ω × r))` and the angular momentum is `L = ∫ r × (ω × r) dm = I ω`, the
> kinetic energy is the quadratic form `T = ½ ω · L = ½ ω · I ω` in the inertia tensor.
>
> For a rigid body in motion the total kinetic energy is the mass integral of half the squared
> speed of its points, `T = ½ ∫ ⟪v, v⟫ dm`. König's theorem splits it into the kinetic energy of
> the centre of mass plus the rotational energy about the centre of mass,
> `T = ½ M ⟪V, V⟫ + ½ ∫ |Ṙ (y − c)|² dm`: the cross term vanishes because the first moment of the
> mass distribution about its centre of mass is zero. In three dimensions the rotational term is
> `½ ∫ |ω × r|² dm`, with `ω` the angular velocity vector and `r` the position of the body point
> relative to the centre of mass.
>
> The total kinetic energy is defined with the point velocity taken in the closed form
> `Ṙ(t) (y − c) + V(t)` (`velocityClosedForm`), which is polynomial in the body point and hence
> smooth for any motion; for differentiable motions it agrees with the honest point velocity
> `∂ₜ (displacement · y)`, recovering `T = ½ ∫ ⟪v, v⟫ dm` (`kineticEnergy_eq_integral_velocity`).

## References

> * Landau and Lifshitz, Mechanics, Section 32. [ref: landau\_mechanics]

**`RigidBody.rotationalKineticEnergy`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L50).

> The rotational kinetic energy of a rigid body rotating with angular velocity `ω` about its
> reference point: half the contraction of `ω` with the inertia tensor, `T = ½ ω · (I ω)`.

```lean
noncomputable def rotationalKineticEnergy (R : RigidBody 3) (ω : Fin 3 → ℝ) : ℝ
```

**`RigidBody.rotationalKineticEnergy_eq_angularMomentum`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L55).

> The rotational kinetic energy is half the contraction of the angular velocity with the angular
> momentum: `T = ½ ω · L`.

```lean
lemma rotationalKineticEnergy_eq_angularMomentum (R : RigidBody 3) (ω : Fin 3 → ℝ) :
    R.rotationalKineticEnergy ω = (1 / (2 : ℝ)) * (ω ⬝ᵥ R.angularMomentum ω)
```

**`RigidBody.rotationalKineticEnergy_eq_integral`**, a theorem, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L62). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The rotational kinetic energy equals the mass integral of the local rotational speed squared:
> `T = ½ ∫ |ω × r|² dm`.

```lean
theorem rotationalKineticEnergy_eq_integral (R : RigidBody 3) (ω : Fin 3 → ℝ) :
    R.rotationalKineticEnergy ω
      = (1 / (2 : ℝ)) * R.ρ ⟨fun x => (ω ⨯₃ (x : Fin 3 → ℝ)) ⬝ᵥ (ω ⨯₃ (x : Fin 3 → ℝ)),
        ContDiff.contMDiff <| (contDiff_cross_dotProduct_cross ω).comp
          (contDiff_pi.mpr fun i => Space.eval_contDiff i)⟩
```

**`RigidBodyMotion.kineticEnergy`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L84).

> The total kinetic energy of a rigid body in motion at time `t`: half the mass integral of the
> squared speed of the body points, `T = ½ ∫ ⟪v, v⟫ dm`, with the point velocity taken in the
> closed form `velocityClosedForm`.

```lean
noncomputable def kineticEnergy {d : ℕ} (M : RigidBodyMotion d) (t : Time) : ℝ
```

**`RigidBodyMotion.kineticEnergy_eq_integral_velocity`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L90).

> For a differentiable motion the integrand of `kineticEnergy` is the squared speed of the
> honest point velocity: `T = ½ ∫ ⟪v, v⟫ dm` with `v = ∂ₜ (displacement · y)`.

```lean
lemma kineticEnergy_eq_integral_velocity {d : ℕ} (M : RigidBodyMotion d) (t : Time)
    (hR : Differentiable ℝ (fun s => (M.orientation s).1))
    (hX : Differentiable ℝ M.comTrajectory) :
    M.kineticEnergy t = (1 / (2 : ℝ)) * M.ρ (cmap
      (fun y => (⟪M.velocity y t, M.velocity y t⟫_ℝ))
      (by
        simp only [← M.velocityClosedForm_eq_velocity t hR hX]
        exact M.contDiff_velocityClosedForm_inner t))
```

**`RigidBodyMotion.kineticEnergy_integrand_split`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L106).

> The squared-speed integrand of `kineticEnergy` splits into the squared rotational speed
> `|Ṙ (y − c)|²`, a term linear in the body-frame coordinate `y − c`, and the constant squared
> centre-of-mass speed `⟪V, V⟫`.

```lean
lemma kineticEnergy_integrand_split {d : ℕ} (M : RigidBodyMotion d) (t : Time) :
    cmap (fun y => (⟪M.velocityClosedForm t y, M.velocityClosedForm t y⟫_ℝ))
        (M.contDiff_velocityClosedForm_inner t)
      = cmap (fun y =>
            (∂ₜ (fun s => (M.orientation s).1) t *ᵥ fun j => y j - M.centerOfMass j) ⬝ᵥ
            (∂ₜ (fun s => (M.orientation s).1) t *ᵥ fun j => y j - M.centerOfMass j))
          (by simp only [dotProduct, Matrix.mulVec]; fun_prop)
        + ∑ j, (2 * (((M.centerOfMassVelocity t : Fin d → ℝ) ᵥ*
              ∂ₜ (fun s => (M.orientation s).1) t) j)) •
            cmap (fun y => y j - M.centerOfMass j) (by fun_prop)
        + (⟪M.centerOfMassVelocity t, M.centerOfMassVelocity t⟫_ℝ) •
            (1 : C^⊤⟮𝓘(ℝ, Space d), Space d; 𝓘(ℝ, ℝ), ℝ⟯)
```

**`RigidBodyMotion.kineticEnergy_eq_translational_add_rotational`**, a theorem, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L142). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **König's theorem**, general form: the total kinetic energy of a rigid body in motion splits
> into the kinetic energy of the centre of mass plus the rotational energy about the centre of
> mass, `T = ½ M ⟪V, V⟫ + ½ ∫ |Ṙ (y − c)|² dm`.

```lean
theorem kineticEnergy_eq_translational_add_rotational {d : ℕ} (M : RigidBodyMotion d) (t : Time)
    (h : M.mass ≠ 0) :
    M.kineticEnergy t
      = (1 / (2 : ℝ)) * M.mass * (⟪M.centerOfMassVelocity t, M.centerOfMassVelocity t⟫_ℝ)
        + (1 / (2 : ℝ)) * M.ρ (cmap (fun y =>
            (∂ₜ (fun s => (M.orientation s).1) t *ᵥ fun j => y j - M.centerOfMass j) ⬝ᵥ
            (∂ₜ (fun s => (M.orientation s).1) t *ᵥ fun j => y j - M.centerOfMass j))
          (by simp only [dotProduct, Matrix.mulVec]; fun_prop))
```

**`RigidBodyMotion.kineticEnergy_eq_translational_add_angularVelocity`**, a theorem, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L159). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **König's theorem** in three dimensions: the total kinetic energy of a rigid body in motion
> splits as `T = ½ M ⟪V, V⟫ + ½ ∫ |ω × r|² dm`, with `ω` the angular velocity vector and
> `r = displacement − comTrajectory` the position of the body point relative to the centre of
> mass.

```lean
theorem kineticEnergy_eq_translational_add_angularVelocity (M : RigidBodyMotion 3) (t : Time)
    (h : M.mass ≠ 0) (hR : DifferentiableAt ℝ (fun s => (M.orientation s).1) t) :
    M.kineticEnergy t
      = (1 / (2 : ℝ)) * M.mass * (⟪M.centerOfMassVelocity t, M.centerOfMassVelocity t⟫_ℝ)
        + (1 / (2 : ℝ)) * M.ρ (cmap (fun y =>
            (M.angularVelocity t ⨯₃ fun j => M.displacement t y j - M.comTrajectory t j) ⬝ᵥ
            (M.angularVelocity t ⨯₃ fun j => M.displacement t y j - M.comTrajectory t j))
          (by
            exact (contDiff_cross_dotProduct_cross (M.angularVelocity t)).comp
              (contDiff_pi.mpr fun j =>
                ((Space.eval_contDiff j).comp (M.displacement_contDiff t)).sub
                  contDiff_const)))
```

**`RigidBodyMotion.kineticEnergy_eq_translational_add_bodyAngularVelocity`**, a theorem, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean#L183). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **König's theorem** in the body frame. The total kinetic energy `M.kineticEnergy t`, formed from
> the lab-frame point velocities, splits at the centre of mass (`centerOfMass = 0`) as
> `T = ½ M ⟪V, V⟫ + rotationalKineticEnergy ω_body`. The rotational energy is a frame-independent
> scalar, so it is evaluated here from the *body-frame* angular velocity `ω_body`: the spatial form
> `|Ṙ (y − c)|²` and the body form `|ω_body × (y − c)|²` agree because
> `Ṙ (y − c) = R (ω_body × (y − c))` and `R`, being orthogonal, preserves the norm.

```lean
theorem kineticEnergy_eq_translational_add_bodyAngularVelocity (M : RigidBodyMotion 3) (t : Time)
    (h : M.mass ≠ 0) (hR : DifferentiableAt ℝ (fun s => (M.orientation s).1) t)
    (hc : M.centerOfMass = 0) :
    M.kineticEnergy t
      = (1 / (2 : ℝ)) * M.mass * (⟪M.centerOfMassVelocity t, M.centerOfMassVelocity t⟫_ℝ)
        + M.toRigidBody.rotationalKineticEnergy (M.bodyAngularVelocity t)
```

## Depends on

- [Angular momentum of a rigid body](angularmomentum.md)
- [The angular velocity of a rigid body](angularvelocity.md)
- [The cross product of three-dimensional vectors](../../mathematics/modules/crossproduct.md)

## Proof depends on

- [Orthogonal matrices and the dot product](../../mathematics/formathlib/orthogonalmatrix.md)

## Sources

- [Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/KineticEnergy.lean)
