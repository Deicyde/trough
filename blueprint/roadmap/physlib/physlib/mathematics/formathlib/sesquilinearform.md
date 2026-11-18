---
declaration: module
origin: cited
lean: LinearMap.IsPosDef, LinearMap.isPosDef_def, LinearMap.IsPosDef.isPosSemidef, LinearMap.IsPosDef.nondegenerate, LinearMap.isPosDef_iff_posDef_toMatrix
statement: formalized
proof: formalized
---

# Positive-definite sesquilinear forms

The module `Physlib.Mathematics.ForMathlib.SesquilinearForm`, [Physlib/Mathematics/ForMathlib/SesquilinearForm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SesquilinearForm.lean): 5 declarations, 4 with a docstring.

> A sesquilinear form is positive-definite when it is symmetric and strictly positive on nonzero
> vectors.

## i. Overview

> Mathlib has positive-semidefinite sesquilinear forms (`LinearMap.IsPosSemidef`) and
> positive-definite matrices (`Matrix.PosDef`), but no positive-definite sesquilinear forms.
> `LinearMap.IsPosDef` fills this gap with the shape of `LinearMap.IsPosSemidef`: a structure
> extending `LinearMap.IsSymm`. For a form `M →ₗ⋆[R] M →ₗ[R] R` symmetry is Hermiticity,
> `star (B x y) = B y x`. A positive-definite form is positive-semidefinite and nondegenerate, and
> in a basis it is positive-definite exactly when its matrix is.

## ii. Key results

> - `LinearMap.IsPosDef` : a sesquilinear form is symmetric and `0 < B x x` for `x ≠ 0`.
> - `LinearMap.IsPosDef.isPosSemidef` : a positive-definite form is positive-semidefinite.
> - `LinearMap.IsPosDef.nondegenerate` : a positive-definite form is nondegenerate.
> - `LinearMap.isPosDef_iff_posDef_toMatrix` : a form is positive-definite exactly when its matrix in
>   a basis is.

## iv. References

> - `LinearMap.IsPosSemidef` and `LinearMap.IsSymm`, in
>   `Mathlib/LinearAlgebra/SesquilinearForm/Basic.lean`;
> - `Matrix.PosDef`, in `Mathlib/LinearAlgebra/Matrix/PosDef.lean`.

## A. Positive-definite sesquilinear forms

### A.1. The definition

**`LinearMap.IsPosDef`**, a structure, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SesquilinearForm.lean#L70).

> A sesquilinear form `B` is **positive-definite** if it is symmetric and `0 < B x x` for every
> nonzero `x`.

```lean
structure IsPosDef [LT R] (B : M →ₛₗ[I₁] M →ₗ[R] R) : Prop extends isSymm : B.IsSymm where
  /-- `B` is strictly positive on nonzero vectors. -/
  pos : ∀ x, x ≠ 0 → 0 < B x x
```

**`LinearMap.isPosDef_def`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SesquilinearForm.lean#L74).

```lean
lemma isPosDef_def [LT R] {B : M →ₛₗ[I₁] M →ₗ[R] R} :
    B.IsPosDef ↔ B.IsSymm ∧ ∀ x, x ≠ 0 → 0 < B x x
```

### A.2. Consequences over a preorder

**`LinearMap.IsPosDef.isPosSemidef`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SesquilinearForm.lean#L87).

> A positive-definite form is positive-semidefinite.

```lean
lemma IsPosDef.isPosSemidef (hB : B.IsPosDef) : B.IsPosSemidef
```

**`LinearMap.IsPosDef.nondegenerate`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SesquilinearForm.lean#L92).

> A positive-definite form is nondegenerate: a nonzero `x` is not orthogonal to itself.

```lean
lemma IsPosDef.nondegenerate (hB : B.IsPosDef) : B.Nondegenerate
```

### A.3. The matrix of a positive-definite form

**`LinearMap.isPosDef_iff_posDef_toMatrix`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SesquilinearForm.lean#L110).

> A sesquilinear form is positive-definite exactly when its matrix in a basis is.

```lean
lemma isPosDef_iff_posDef_toMatrix (b : Basis n R M) : B.IsPosDef ↔ (toMatrix₂ b b B).PosDef
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/SesquilinearForm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/SesquilinearForm.lean)
