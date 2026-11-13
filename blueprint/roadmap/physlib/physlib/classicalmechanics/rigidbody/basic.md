---
declaration: module
origin: cited
lean: RigidBody.inertiaTensorAbout_eq_centerOfMass_add_pointMass, RigidBody, RigidBody.mass, RigidBody.rho_one, RigidBody.centerOfMass, RigidBody.inertiaTensor, RigidBody.inertiaTensor_symmetric, RigidBody.rho_coord_sub_centerOfMass
statement: formalized
proof: formalized
---

# Rigid bodies

The module `Physlib.ClassicalMechanics.RigidBody.Basic`, [Physlib/ClassicalMechanics/RigidBody/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean): 14 declarations, 13 with a docstring, 1 listed as significant.

> A rigid body is one where the distance and relative orientation between particles does not change.
> In other words, the body remains undeformed.
>
> In this module we will define the basic properties of a rigid body, including
> - mass
> - center of mass
> - inertia tensor
> - inertia tensor about an arbitrary point
>
> The moments of the last are taken about the given point rather than about the origin of the
> reference frame. The parallel-axis theorem expresses it in terms of the inertia tensor about the
> centre of mass.

## References

> * Landau and Lifshitz, Mechanics, page 100, Section 32. [ref: landau\_mechanics]

**`RigidBody`**, a structure, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L44).

> A Rigid body defined by its mass distribution.

```lean
structure RigidBody (d : ℕ) where
  /-- The mass distribution of the rigid body. -/
  ρ : C^⊤⟮𝓘(ℝ, Space d), Space d; 𝓘(ℝ, ℝ), ℝ⟯ →ₗ[ℝ] ℝ
```

**`RigidBody.mass`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L51).

> The total mass of the rigid body.

```lean
noncomputable def mass {d : ℕ} (R : RigidBody d) : ℝ
```

**`RigidBody.rho_one`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L55).

> The mass distribution applied to the constant function `1` is the total mass.

```lean
lemma rho_one {d : ℕ} (R : RigidBody d) :
    R.ρ (1 : C^⊤⟮𝓘(ℝ, Space d), Space d; 𝓘(ℝ, ℝ), ℝ⟯) = R.mass
```

**`RigidBody.centerOfMass`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L59).

> The center of mass of the rigid body.

```lean
noncomputable def centerOfMass {d : ℕ} (R : RigidBody d) : Space d
```

**`RigidBody.inertiaTensor`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L63).

> The inertia tensor of the rigid body.

```lean
noncomputable def inertiaTensor {d : ℕ} (R : RigidBody d) :
    Matrix (Fin d) (Fin d) ℝ
```

**`RigidBody.inertiaTensor_symmetric`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L68).

```lean
lemma inertiaTensor_symmetric {d : ℕ} (R : RigidBody d) (i j : Fin d) :
    R.inertiaTensor i j = R.inertiaTensor j i
```

**`RigidBody.rho_coord_sub_centerOfMass`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L74).

> The first moment of the mass distribution about its own centre of mass vanishes:
> for nonzero mass, `ρ` of the centred `j`-th coordinate function is zero.

```lean
lemma rho_coord_sub_centerOfMass {d : ℕ} (R : RigidBody d) (h : R.mass ≠ 0) (j : Fin d) :
    R.ρ (cmap (fun y => y j - R.centerOfMass j) (by fun_prop)) = 0
```

**`RigidBody.inertiaTensorAbout`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L91).

> The inertia tensor of the rigid body about the point `p`, that is with the moments taken
> about `p` rather than about the origin of the reference frame. Taking `p` to be the origin
> recovers `RigidBody.inertiaTensor`, see `RigidBody.inertiaTensorAbout_zero`.

```lean
noncomputable def inertiaTensorAbout {d : ℕ} (R : RigidBody d) (p : Space d) :
    Matrix (Fin d) (Fin d) ℝ
```

**`RigidBody.inertiaTensorAbout_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L97).

> The `(i, j)` entry of the inertia tensor about `p` as a moment of the mass distribution.

```lean
lemma inertiaTensorAbout_apply {d : ℕ} (R : RigidBody d) (p : Space d) (i j : Fin d) :
    R.inertiaTensorAbout p i j = R.ρ (cmap (fun y => (if i = j then 1 else 0) *
      ∑ k : Fin d, (y k - p k) ^ 2 - (y i - p i) * (y j - p j)) (by fun_prop))
```

**`RigidBody.inertiaTensorAbout_zero`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L103).

> The inertia tensor about the origin is the inertia tensor.

```lean
lemma inertiaTensorAbout_zero {d : ℕ} (R : RigidBody d) :
    R.inertiaTensorAbout 0 = R.inertiaTensor
```

**`RigidBody.inertiaTensorAbout_symmetric`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L109).

> The inertia tensor about any point is symmetric.

```lean
lemma inertiaTensorAbout_symmetric {d : ℕ} (R : RigidBody d) (p : Space d) (i j : Fin d) :
    R.inertiaTensorAbout p i j = R.inertiaTensorAbout p j i
```

**`RigidBody.inertiaTensorAbout_integrand_split`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L116).

> The integrand of the inertia tensor about `p` splits into the integrand about the centre of
> mass, terms linear in the centred coordinates `y − c`, and a constant built from the
> displacement `c − p`.

```lean
lemma inertiaTensorAbout_integrand_split {d : ℕ} (R : RigidBody d) (p : Space d) (i j : Fin d) :
    cmap (fun y => (if i = j then 1 else 0) * ∑ k : Fin d, (y k - p k) ^ 2
        - (y i - p i) * (y j - p j)) (by fun_prop)
      = cmap (fun y => (if i = j then 1 else 0) * ∑ k : Fin d, (y k - R.centerOfMass k) ^ 2
            - (y i - R.centerOfMass i) * (y j - R.centerOfMass j)) (by fun_prop)
        + ∑ k : Fin d, (2 * (if i = j then 1 else 0) * (R.centerOfMass k - p k)) •
            cmap (fun y => y k - R.centerOfMass k) (by fun_prop)
        - (R.centerOfMass j - p j) • cmap (fun y => y i - R.centerOfMass i) (by fun_prop)
        - (R.centerOfMass i - p i) • cmap (fun y => y j - R.centerOfMass j) (by fun_prop)
        + ((if i = j then 1 else 0) * ∑ k : Fin d, (R.centerOfMass k - p k) ^ 2
            - (R.centerOfMass i - p i) * (R.centerOfMass j - p j)) •
          (1 : C^⊤⟮𝓘(ℝ, Space d), Space d; 𝓘(ℝ, ℝ), ℝ⟯)
```

**`RigidBody.inertiaTensorAbout_eq_centerOfMass_add_pointMass`**, a theorem, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L148). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **The parallel-axis theorem**: the inertia tensor about a point `p` is the inertia tensor
> about the centre of mass `c` plus the inertia tensor about `p` of a point particle carrying the
> total mass of the body and sitting at `c`, that is `M (|c − p|² 1 − (c − p) ⊗ (c − p))`.

```lean
theorem inertiaTensorAbout_eq_centerOfMass_add_pointMass {d : ℕ} (R : RigidBody d) (h : R.mass ≠ 0)
    (p : Space d) :
    R.inertiaTensorAbout p = R.inertiaTensorAbout R.centerOfMass
      + R.mass • (⟪R.centerOfMass - p, R.centerOfMass - p⟫_ℝ • (1 : Matrix (Fin d) (Fin d) ℝ)
        - Matrix.vecMulVec ⇑(R.centerOfMass - p) ⇑(R.centerOfMass - p))
```

**`RigidBody.inertiaTensor_eq_centerOfMass_add_pointMass`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean#L163).

> The inertia tensor about the origin is the inertia tensor about the centre of mass `c` plus
> `M (|c|² 1 − c ⊗ c)`.

```lean
lemma inertiaTensor_eq_centerOfMass_add_pointMass {d : ℕ} (R : RigidBody d) (h : R.mass ≠ 0) :
    R.inertiaTensor = R.inertiaTensorAbout R.centerOfMass
      + R.mass • (⟪R.centerOfMass, R.centerOfMass⟫_ℝ • (1 : Matrix (Fin d) (Fin d) ℝ)
        - Matrix.vecMulVec ⇑R.centerOfMass ⇑R.centerOfMass)
```

## Depends on

- [Physlib.Meta.Informal.Basic](../../meta/informal/basic.md)
- [Smooth real-valued functions on space](../../spaceandtime/space/part-01/smoothfunctions.md)

## Sources

- [Physlib/ClassicalMechanics/RigidBody/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/Basic.lean)
