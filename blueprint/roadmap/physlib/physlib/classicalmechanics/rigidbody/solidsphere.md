---
declaration: module
origin: cited
lean: RigidBody.solidSphere, RigidBody.solidSphere_mass, RigidBody.solidSphere_centerOfMass
statement: formalized
proof: formalized
---

# The solid sphere as a rigid body

The module `Physlib.ClassicalMechanics.RigidBody.SolidSphere`, [Physlib/ClassicalMechanics/RigidBody/SolidSphere.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/SolidSphere.lean): 3 declarations, 2 with a docstring.

> In this module we consider the solid sphere as a rigid body, and compute its mass,
> center of mass and inertia tensor.

**`RigidBody.solidSphere`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/SolidSphere.lean#L28).

> The solid sphere as a rigid body.

```lean
noncomputable def solidSphere (d : ℕ) (m R : ℝ≥0) : RigidBody d
```

**`RigidBody.solidSphere_mass`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/SolidSphere.lean#L45).

```lean
lemma solidSphere_mass {d : ℕ} (m R : ℝ≥0) (hr : R ≠ 0) : (solidSphere d m R).mass = m
```

**`RigidBody.solidSphere_centerOfMass`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/SolidSphere.lean#L60).

> The center of mass of a solid sphere located at the origin is `0`.

```lean
lemma solidSphere_centerOfMass {d : ℕ} (m R : ℝ≥0) : (solidSphere d m R).centerOfMass = 0
```

## Depends on

- [Rigid bodies](basic.md)

## Sources

- [Physlib/ClassicalMechanics/RigidBody/SolidSphere.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/RigidBody/SolidSphere.lean)
