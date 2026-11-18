---
declaration: module
origin: cited
lean: Electromagnetism.ThreeDimension.electricField_eq_3D, Electromagnetism.ThreeDimension.magneticField_eq_3D
statement: formalized
proof: formalized
---

# Three-Dimensional Electromagnetism

The module `Physlib.Electromagnetism.ThreeDimension.Basic`, [Physlib/Electromagnetism/ThreeDimension/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/Basic.lean): 2 declarations, 2 with a docstring, 2 listed as significant.

> This directory provides a three-dimensional, vector-calculus-facing layer for
> electromagnetism.
>
> The backend theory is formulated in a tensorial and dimension-general way.
> Here we re-express the relevant constructions in the familiar language of
> scalar and vector potentials, electric and magnetic fields, and spatial
> derivatives.

## Fields from potentials

> In this section we rewrite the electric and magnetic fields associated to an
> electromagnetic potential in terms of the scalar and vector potentials, using
> the standard vector-calculus expressions.

**`Electromagnetism.ThreeDimension.electricField_eq_3D`**, a theorem, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/Basic.lean#L49). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The electric field written in terms of the scalar and vector potentials as `- ∇ φ - ∂ₜ A`.

```lean
theorem electricField_eq_3D :
    E = fun t x => - ∇ (φ t) x - ∂ₜ (fun t => A t x) t
```

**`Electromagnetism.ThreeDimension.magneticField_eq_3D`**, a theorem, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/Basic.lean#L55). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The magnetic field written as the curl of the vector potential as `∇ ⨯ A`.

```lean
theorem magneticField_eq_3D :
    B = fun t x => (∇ ⨯ (A t)) x
```

## Depends on

- [The Magnetic Field (Kinematics/MagneticField)](../kinematics/magneticfield.md)

## Sources

- [Physlib/Electromagnetism/ThreeDimension/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/ThreeDimension/Basic.lean)
