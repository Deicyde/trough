---
declaration: module
origin: cited
lean: RigidBody.angularMomentum_eq_inertiaTensor_mulVec, RigidBody.angularMomentum
statement: formalized
proof: formalized
---

# Angular momentum of a rigid body

The module `Physlib.ClassicalMechanics.RigidBody.AngularMomentum`, [Physlib/ClassicalMechanics/RigidBody/AngularMomentum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularMomentum.lean): 2 declarations, 2 with a docstring, 1 listed as significant.

> For a rigid body rotating with angular velocity `ω` about its reference point, each body point at
> position `r` moves with velocity `ω × r`, so the body's angular momentum about that point is
> `L = ∫ r × (ω × r) dm`. Expanding the double cross product,
> `r × (ω × r) = |r|² ω − (r · ω) r`, shows that `L` is linear in `ω` with matrix the inertia tensor:
> `L = I ω`.

## References

> * Landau and Lifshitz, Mechanics, Section 32. [ref: landau\_mechanics]

**`RigidBody.angularMomentum`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularMomentum.lean#L34).

> The angular momentum `L = ∫ r × (ω × r) dm` of a rigid body rotating with angular velocity `ω`
> about its reference point (each body point at `r` moving with velocity `ω × r`). Its `i`-th
> component is `ρ` applied to the scalar field `[r × (ω × r)]ᵢ`.

```lean
noncomputable def angularMomentum (R : RigidBody 3) (ω : Fin 3 → ℝ) : Fin 3 → ℝ
```

**`RigidBody.angularMomentum_eq_inertiaTensor_mulVec`**, a theorem, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularMomentum.lean#L44). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The angular momentum of a rigid body equals its inertia tensor applied to the angular velocity:
> `L = I ω`.

```lean
theorem angularMomentum_eq_inertiaTensor_mulVec (R : RigidBody 3) (ω : Fin 3 → ℝ) :
    R.angularMomentum ω = R.inertiaTensor *ᵥ ω
```

## Depends on

- [Rigid bodies](basic.md)

## Proof depends on

- [The cross product of three-dimensional vectors](../../mathematics/modules/crossproduct.md)

## Sources

- [Physlib/ClassicalMechanics/RigidBody/AngularMomentum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/AngularMomentum.lean)
