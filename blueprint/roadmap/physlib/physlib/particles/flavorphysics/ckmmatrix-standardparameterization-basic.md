---
declaration: module
origin: cited
lean: standParamAsMatrix, standParamAsMatrix_unitary, standParam, standParam.cross_product_t, standParam.eq_rows, standParam.eq_exp_of_phases, standParam.VusVubVcdSq_eq, standParam.mulExpδ₁₃_eq
statement: formalized
proof: formalized
---

# Standard parameterization for the CKM Matrix

The module `Physlib.Particles.FlavorPhysics.CKMMatrix.StandardParameterization.Basic`, [Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean): 8 declarations, 6 with a docstring.

> This file defines the standard parameterization of CKM matrices in terms of
> four real numbers `θ₁₂`, `θ₁₃`, `θ₂₃` and `δ₁₃`.
>
> We will show that every CKM matrix can be written within this standard parameterization
> in the file `FlavorPhysics.CKMMatrix.StandardParameters`.

**`standParamAsMatrix`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean#L31).

> Given four reals `θ₁₂ θ₁₃ θ₂₃ δ₁₃` the standard parameterization of the CKM matrix
> as a `3×3` complex matrix.

```lean
def standParamAsMatrix (θ₁₂ θ₁₃ θ₂₃ δ₁₃ : ℝ) : Matrix (Fin 3) (Fin 3) ℂ
```

**`standParamAsMatrix_unitary`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean#L44).

> The standard parameterization forms a unitary matrix.

```lean
lemma standParamAsMatrix_unitary (θ₁₂ θ₁₃ θ₂₃ δ₁₃ : ℝ) :
    ((standParamAsMatrix θ₁₂ θ₁₃ θ₂₃ δ₁₃)ᴴ * standParamAsMatrix θ₁₂ θ₁₃ θ₂₃ δ₁₃) = 1
```

**`standParam`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean#L59).

> A CKM Matrix from four reals `θ₁₂`, `θ₁₃`, `θ₂₃`, and `δ₁₃`. This is the standard
> parameterization of CKM matrices.

```lean
def standParam (θ₁₂ θ₁₃ θ₂₃ δ₁₃ : ℝ) : CKMMatrix
```

**`standParam.cross_product_t`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean#L68).

> The top-row of the standard parameterization is the cross product of the conjugate of the
> up and charm rows.

```lean
lemma cross_product_t (θ₁₂ θ₁₃ θ₂₃ δ₁₃ : ℝ) :
    [standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃]t =
    (conj [standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃]u ⨯₃ conj [standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃]c)
```

**`standParam.eq_rows`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean#L86).

> A CKM matrix which has rows equal to that of a standard parameterisation is equal
> to that standard parameterisation.

```lean
lemma eq_rows (U : CKMMatrix) {θ₁₂ θ₁₃ θ₂₃ δ₁₃ : ℝ} (hu : [U]u = [standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃]u)
    (hc : [U]c = [standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃]c) (hU : [U]t = conj [U]u ⨯₃ conj [U]c) :
    U = standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃
```

**`standParam.eq_exp_of_phases`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean#L95).

> Two standard parameterisations of CKM matrices are the same matrix if they have
> the same angles and the exponential of their faces is equal.

```lean
lemma eq_exp_of_phases (θ₁₂ θ₁₃ θ₂₃ δ₁₃ δ₁₃' : ℝ) (h : cexp (δ₁₃ * I) = cexp (δ₁₃' * I)) :
    standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃ = standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃'
```

**`standParam.VusVubVcdSq_eq`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean#L104).

```lean
lemma VusVubVcdSq_eq (θ₁₂ θ₁₃ θ₂₃ δ₁₃ : ℝ) (h1 : 0 ≤ Real.sin θ₁₂)
    (h2 : 0 ≤ Real.cos θ₁₃) (h3 : 0 ≤ Real.sin θ₂₃) (h4 : 0 ≤ Real.cos θ₁₂) :
    VusVubVcdSq ⟦standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃⟧ =
    Real.sin θ₁₂ ^ 2 * Real.cos θ₁₃ ^ 2 * Real.sin θ₁₃ ^ 2 * Real.sin θ₂₃ ^ 2
```

**`standParam.mulExpδ₁₃_eq`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean#L131).

```lean
lemma mulExpδ₁₃_eq (θ₁₂ θ₁₃ θ₂₃ δ₁₃ : ℝ) (h1 : 0 ≤ Real.sin θ₁₂)
    (h2 : 0 ≤ Real.cos θ₁₃) (h3 : 0 ≤ Real.sin θ₂₃) (h4 : 0 ≤ Real.cos θ₁₂) :
    mulExpδ₁₃ ⟦standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃⟧ =
    sin θ₁₂ * cos θ₁₃ ^ 2 * sin θ₂₃ * sin θ₁₃ * cos θ₁₂ * cos θ₂₃ * cexp (I * δ₁₃)
```

## Depends on

- [Invariants of the CKM Matrix](ckmmatrix-invariants.md)
- [Rows for the CKM Matrix](ckmmatrix-rows.md)

## Sources

- [Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/Basic.lean)
