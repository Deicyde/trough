---
declaration: module
origin: cited
lean: SULieAlgebra.adjointContr, SULieAlgebra.adjointContr_tmul, SULieAlgebra.adjointContr_adjoint, SULieAlgebra.ofReal_adjointContr_tmul, SULieAlgebra.adjointContr_symm, SULieAlgebra.adjointContr_lie, SULieAlgebra.adjointContr_self_nonneg, SULieAlgebra.adjointContr_self_eq_zero_iff
statement: formalized
proof: formalized
---

# The contraction of adjoint indices of `SU(n)`

The module `Physlib.Mathematics.Groups.SpecialUnitary.LieAlgebra.Contractions`, [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean): 28 declarations, 22 with a docstring.

> The trace form on `su(n)` and on its complexification, and the invariant bilinear forms.

## i. Overview

> The contraction `adjointContr` of two real adjoint indices is the trace form `x ⊗ y ↦ tr (x y)` on
> `su(n)`, which is real since `x` and `y` are hermitian, and invariant under the adjoint action by
> the cyclicity of the trace. It is symmetric, invariant under the bracket, and positive definite
> since `tr (x x) = tr (x x†)` vanishes only for `x = 0` (A.1).
>
> The contraction `adjointℂContr` of two complex adjoint indices is its complexification. On the
> underlying matrices it is the trace form `A ⊗ B ↦ tr (A B)`, and it is again symmetric, invariant
> under the bracket and nondegenerate (A.2).
>
> Every bilinear form on the complexification is the contraction against an endomorphism, which
> commutes with the adjoint action if the form is invariant. By Schur's lemma such an endomorphism is
> a scalar, so every `SU(n)`-invariant bilinear form on the complexification is a multiple of the
> contraction (B).

## ii. Key results

> - `SULieAlgebra.adjointContr` : the contraction of two real adjoint indices.
> - `SULieAlgebra.adjointℂContr` : the contraction of two complex adjoint indices.
> - `SULieAlgebra.adjointContr_self_pos` : the real contraction is positive definite.
> - `SULieAlgebra.adjointℂContr_nondegenerate` : the complex contraction is nondegenerate.
> - `SULieAlgebra.intertwiningMap_eq_smul_adjointℂContr` : every intertwiner `adj ⊗ adj → ℂ` is a
>   multiple of the complex contraction.

## iv. References

> * None.

## A. The contraction of adjoint indices

### A.1. The real case

**`SULieAlgebra.adjointContr`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L72).

> The contraction of two real adjoint indices: the trace form `x ⊗ y ↦ tr (x y)` on `su(n)`,
> which is real since `x` and `y` are hermitian.

```lean
noncomputable def adjointContr {n : ℕ} : ((adjoint (n := n)).tprod adjoint).IntertwiningMap
    (Representation.trivial ℝ (specialUnitaryGroup (Fin n) ℂ) ℝ)
```

**`SULieAlgebra.adjointContr_tmul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L91).

> The real contraction is the real part of the trace, `x ⊗ y ↦ re tr (x y)`.

```lean
lemma adjointContr_tmul {n : ℕ} (x y : SULieAlgebra n ℂ) :
    adjointContr (x ⊗ₜ y) = (x.1 * y.1).trace.re
```

**`SULieAlgebra.adjointContr_adjoint`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L96).

> The adjoint representation preserves the real contraction, so `SU(n)` acts on `su(n)` by
> isometries.

```lean
lemma adjointContr_adjoint {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ) (x y : SULieAlgebra n ℂ) :
    adjointContr (adjoint g x ⊗ₜ adjoint g y) = adjointContr (x ⊗ₜ y)
```

**`SULieAlgebra.ofReal_adjointContr_tmul`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L101).

> The trace `tr (x y)` of two elements of `su(n)` is real, equal to their contraction.

```lean
lemma ofReal_adjointContr_tmul {n : ℕ} (x y : SULieAlgebra n ℂ) :
    (adjointContr (x ⊗ₜ y) : ℂ) = (x.1 * y.1).trace
```

**`SULieAlgebra.adjointContr_symm`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L109).

```lean
lemma adjointContr_symm {n : ℕ} (x y : SULieAlgebra n ℂ) :
    adjointContr (x ⊗ₜ y) = adjointContr (y ⊗ₜ x)
```

**`SULieAlgebra.adjointContr_lie`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L115).

> The real contraction is invariant under the bracket, `tr (⁅x, y⁆ z) = tr (x ⁅y, z⁆)`; in terms
> of generators, the structure constants `tr (T^a ⁅T^b, T^c⁆)` are totally antisymmetric.

```lean
lemma adjointContr_lie {n : ℕ} (x y z : SULieAlgebra n ℂ) :
    adjointContr (⁅x, y⁆ ⊗ₜ z) = adjointContr (x ⊗ₜ ⁅y, z⁆)
```

**`SULieAlgebra.adjointContr_self_nonneg`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L122).

> The real contraction is positive semidefinite: `tr (x x) = tr (x x†) ≥ 0`.

```lean
lemma adjointContr_self_nonneg {n : ℕ} (x : SULieAlgebra n ℂ) : 0 ≤ adjointContr (x ⊗ₜ x)
```

**`SULieAlgebra.adjointContr_self_eq_zero_iff`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L128).

> The real contraction of `x` with itself vanishes only for `x = 0`.

```lean
lemma adjointContr_self_eq_zero_iff {n : ℕ} (x : SULieAlgebra n ℂ) :
    adjointContr (x ⊗ₜ x) = 0 ↔ x = 0
```

**`SULieAlgebra.adjointContr_self_pos`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L135).

> The real contraction is positive definite, making it an inner product on `su(n)`.

```lean
lemma adjointContr_self_pos {n : ℕ} {x : SULieAlgebra n ℂ} (hx : x ≠ 0) :
    0 < adjointContr (x ⊗ₜ x)
```

**`SULieAlgebra.adjointContr_separating_left`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L139).

```lean
lemma adjointContr_separating_left {n : ℕ} (x : SULieAlgebra n ℂ)
    (hx : ∀ y, adjointContr (x ⊗ₜ y) = 0) : x = 0
```

**`SULieAlgebra.adjointContr_separating_right`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L143).

```lean
lemma adjointContr_separating_right {n : ℕ} (y : SULieAlgebra n ℂ)
    (hy : ∀ x, adjointContr (x ⊗ₜ y) = 0) : y = 0
```

**`SULieAlgebra.adjointContr_flip_injective`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L148).

> The real contraction separates `su(n)`: `y ↦ (x ↦ re tr (x y))` is injective.

```lean
lemma adjointContr_flip_injective {n : ℕ} :
    Function.Injective (TensorProduct.curry (adjointContr (n := n)).toLinearMap).flip
```

**`SULieAlgebra.adjointContr_isSymm`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L158).

> The real contraction, as a bilinear form, is symmetric.

```lean
lemma adjointContr_isSymm {n : ℕ} :
    LinearMap.BilinForm.IsSymm (TensorProduct.curry (adjointContr (n := n)).toLinearMap)
```

**`SULieAlgebra.adjointContr_nondegenerate`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L163).

> The real contraction, as a bilinear form, is nondegenerate.

```lean
lemma adjointContr_nondegenerate {n : ℕ} :
    (TensorProduct.curry (adjointContr (n := n)).toLinearMap).Nondegenerate
```

### A.2. The complex case

**`SULieAlgebra.adjointℂContr`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L175).

> The contraction of two complex adjoint indices: the complexification of the real contraction
> `adjointContr`.

```lean
noncomputable def adjointℂContr {n : ℕ} : ((adjointℂ (n := n)).tprod adjointℂ).IntertwiningMap
    (Representation.trivial ℂ (specialUnitaryGroup (Fin n) ℂ) ℂ)
```

**`SULieAlgebra.adjointℂContr_adjointℂ`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L193).

> The adjoint representation preserves the complex contraction.

```lean
lemma adjointℂContr_adjointℂ {n : ℕ} (g : specialUnitaryGroup (Fin n) ℂ)
    (A B : Complexification n) :
    adjointℂContr (adjointℂ g A ⊗ₜ adjointℂ g B) = adjointℂContr (A ⊗ₜ B)
```

**`SULieAlgebra.adjointℂContr_tmul`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L201).

> The contraction is the trace form, `A ⊗ B ↦ tr (A B)`.

```lean
lemma adjointℂContr_tmul (A B : Complexification n) :
    adjointℂContr (A ⊗ₜ B) = (toMatrixℂ A * toMatrixℂ B).trace
```

**`SULieAlgebra.adjointℂContr_one_tmul`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L218).

> On the real elements `1 ⊗ x` of the complexification the complex contraction is the real
> contraction, so the two agree on real gauge fields.

```lean
lemma adjointℂContr_one_tmul {n : ℕ} (x y : SULieAlgebra n ℂ) :
    adjointℂContr ((1 ⊗ₜ x) ⊗ₜ (1 ⊗ₜ y)) = adjointContr (x ⊗ₜ y)
```

**`SULieAlgebra.adjointℂContr_symm`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L223).

```lean
lemma adjointℂContr_symm {n} (A B : Complexification n) :
    adjointℂContr (A ⊗ₜ B) = adjointℂContr (B ⊗ₜ A)
```

**`SULieAlgebra.adjointℂContr_lie`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L228).

> The complex contraction is invariant under the bracket, `tr (⁅A, B⁆ C) = tr (A ⁅B, C⁆)`.

```lean
lemma adjointℂContr_lie {n} (A B C : Complexification n) :
    adjointℂContr (⁅A, B⁆ ⊗ₜ C) = adjointℂContr (A ⊗ₜ ⁅B, C⁆)
```

**`SULieAlgebra.adjointℂContr_separating_left`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L235).

```lean
lemma adjointℂContr_separating_left {n} (A : Complexification n)
    (hA : ∀ B, adjointℂContr (A ⊗ₜ B) = 0) : A = 0
```

**`SULieAlgebra.adjointℂContr_separating_right`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L242).

```lean
lemma adjointℂContr_separating_right {n} (B : Complexification n)
    (hB : ∀ A, adjointℂContr (A ⊗ₜ B) = 0) : B = 0
```

**`SULieAlgebra.adjointℂContr_flip_injective`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L247).

> The contraction separates the complexification: `B ↦ (A ↦ tr (A B))` is injective.

```lean
lemma adjointℂContr_flip_injective :
    Function.Injective (TensorProduct.curry (adjointℂContr (n := n)).toLinearMap).flip
```

**`SULieAlgebra.adjointℂContr_isSymm`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L257).

> The complex contraction, as a bilinear form, is symmetric.

```lean
lemma adjointℂContr_isSymm {n : ℕ} :
    LinearMap.BilinForm.IsSymm (TensorProduct.curry (adjointℂContr (n := n)).toLinearMap)
```

**`SULieAlgebra.adjointℂContr_nondegenerate`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L262).

> The complex contraction, as a bilinear form, is nondegenerate.

```lean
lemma adjointℂContr_nondegenerate {n : ℕ} :
    (TensorProduct.curry (adjointℂContr (n := n)).toLinearMap).Nondegenerate
```

## B. Invariant bilinear forms

**`SULieAlgebra.exists_eq_adjointℂContr_tmul`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L275).

> Every bilinear form on the complexification is the contraction against an endomorphism,
> the contraction being nondegenerate.

```lean
lemma exists_eq_adjointℂContr_tmul {n : ℕ}
    (B : Complexification n ⊗[ℂ] Complexification n →ₗ[ℂ] ℂ) :
    ∃ T : Module.End ℂ (Complexification n), ∀ A C, B (A ⊗ₜ C) = adjointℂContr (T A ⊗ₜ C)
```

**`SULieAlgebra.adjointℂ_comp_eq_of_adjointℂContr_tmul`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L284).

> The endomorphism representing an invariant bilinear form commutes with the adjoint
> action.

```lean
lemma adjointℂ_comp_eq_of_adjointℂContr_tmul {n : ℕ}
    (B : ((adjointℂ (n := n)).tprod adjointℂ).IntertwiningMap
      (Representation.trivial ℂ (specialUnitaryGroup (Fin n) ℂ) ℂ))
    {T : Module.End ℂ (Complexification n)} (hT : ∀ A C, B (A ⊗ₜ C) = adjointℂContr (T A ⊗ₜ C))
    (g : specialUnitaryGroup (Fin n) ℂ) :
    T ∘ₗ adjointℂ g = adjointℂ g ∘ₗ T
```

**`SULieAlgebra.intertwiningMap_eq_smul_adjointℂContr`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean#L300).

> Every intertwiner `adj ⊗ adj → ℂ` is a multiple of the contraction: up to scale, the
> contraction is the unique `SU(n)`-invariant bilinear form on the complexification.

```lean
lemma intertwiningMap_eq_smul_adjointℂContr {n : ℕ}
    (B : ((adjointℂ (n := n)).tprod adjointℂ).IntertwiningMap
      (Representation.trivial ℂ (specialUnitaryGroup (Fin n) ℂ) ℂ)) :
    ∃ z : ℂ, B = z • adjointℂContr
```

## Depends on

- [The adjoint representation of `SU(n)`](specialunitary-liealgebra-adjoint.md)

## Sources

- [Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SpecialUnitary/LieAlgebra/Contractions.lean)
