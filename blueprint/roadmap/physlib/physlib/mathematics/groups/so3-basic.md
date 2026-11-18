---
declaration: module
origin: cited
lean: GroupTheory.SO3, GroupTheory.SO3Group, GroupTheory.SO3.coe_inv, GroupTheory.SO3.toGL, GroupTheory.SO3.subtype_val_eq_toGL, GroupTheory.SO3.toGL_injective, GroupTheory.SO3.toProd, GroupTheory.SO3.toProd_eq_transpose
statement: formalized
proof: formalized
---

# The group SO(3)

The module `Physlib.Mathematics.Groups.SO3.Basic`, [Physlib/Mathematics/Groups/SO3/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean): 22 declarations (2 instances with no name), 17 with a docstring.

**`GroupTheory.SO3`**, a def, [line 22](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L22).

> The group of `3×3` real matrices with determinant 1 and `A * Aᵀ = 1`.

```lean
def SO3 : Type
```

**`GroupTheory.SO3Group`**, an instance, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L26).

> The instance of a group on `SO3`.

```lean
instance SO3Group : Group SO3
```

**An instance with no name**, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L47).

> SO3 has the subtype topology.

```lean
instance : TopologicalSpace SO3
```

**`GroupTheory.SO3.coe_inv`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L51).

```lean
lemma coe_inv (A : SO3) : (A⁻¹).1 = A.1⁻¹
```

**`GroupTheory.SO3.toGL`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L55).

> The inclusion of `SO(3)` into `GL (Fin 3) ℝ`.

```lean
def toGL : SO(3) →* GL (Fin 3) ℝ
```

**`GroupTheory.SO3.subtype_val_eq_toGL`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L60).

```lean
lemma subtype_val_eq_toGL : (Subtype.val : SO3 → Matrix (Fin 3) (Fin 3) ℝ) =
    Units.val ∘ toGL.toFun
```

**`GroupTheory.SO3.toGL_injective`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L65).

> The inclusion of `SO(3)` into `GL(3,ℝ)` is an injection.

```lean
lemma toGL_injective : Function.Injective toGL
```

**`GroupTheory.SO3.toProd`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L72).

> The inclusion of `SO(3)` into the monoid of matrices times the opposite of
> the monoid of matrices.

```lean
def toProd : SO(3) →* (Matrix (Fin 3) (Fin 3) ℝ) × (Matrix (Fin 3) (Fin 3) ℝ)ᵐᵒᵖ
```

**`GroupTheory.SO3.toProd_eq_transpose`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L75).

```lean
lemma toProd_eq_transpose : toProd A = (A.1, ⟨A.1ᵀ⟩)
```

**`GroupTheory.SO3.toProd_injective`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L77).

```lean
lemma toProd_injective : Function.Injective toProd
```

**`GroupTheory.SO3.toProd_continuous`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L82).

```lean
lemma toProd_continuous : Continuous toProd
```

**`GroupTheory.SO3.toProd_embedding`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L91).

> The embedding of `SO(3)` into the monoid of matrices times the opposite of
> the monoid of matrices.

```lean
lemma toProd_embedding : IsEmbedding toProd
```

**`GroupTheory.SO3.toGL_embedding`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L98).

> The embedding of `SO(3)` into `GL (Fin 3) ℝ`.

```lean
lemma toGL_embedding : IsEmbedding toGL.toFun
```

**An instance with no name**, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L112).

> The instance of a topological group on `SO(3)`, defined through the embedding of `SO(3)`
> into `GL(n)`.

```lean
instance : IsTopologicalGroup SO(3)
```

**`GroupTheory.SO3.det_minus_id`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L116).

> The determinant of an `SO(3)` matrix minus the identity is equal to zero.

```lean
lemma det_minus_id (A : SO(3)) : det (A.1 - 1) = 0
```

**`GroupTheory.SO3.det_id_minus`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L131).

> The determinant of the identity minus an `SO(3)` matrix is zero.

```lean
lemma det_id_minus (A : SO(3)) : det (1 - A.1) = 0
```

**`GroupTheory.SO3.one_in_spectrum`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L142).

> For every matrix in `SO(3)`, the real number `1` is in its spectrum.

```lean
lemma one_in_spectrum (A : SO(3)) : 1 ∈ spectrum ℝ (A.1)
```

**`GroupTheory.SO3.toEnd`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L150).

> The endomorphism of `EuclideanSpace ℝ (Fin 3)` associated to a element of `SO(3)`.

```lean
def toEnd (A : SO(3)) : End ℝ (EuclideanSpace ℝ (Fin 3))
```

**`GroupTheory.SO3.one_is_eigenvalue`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L155).

> Every `SO(3)` matrix has an eigenvalue equal to `1`.

```lean
lemma one_is_eigenvalue (A : SO(3)) : A.toEnd.HasEigenvalue 1
```

**`GroupTheory.SO3.exists_stationary_vec`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L162).

> For every element of `SO(3)` there exists a vector which remains unchanged under the
> action of that `SO(3)` element.

```lean
lemma exists_stationary_vec (A : SO(3)) :
    ∃ (v : EuclideanSpace ℝ (Fin 3)),
    Orthonormal ℝ (({0} : Set (Fin 3)).domRestrict (fun _ => v))
    ∧ A.toEnd v = v
```

**`GroupTheory.SO3.exists_basis_preserved`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L183).

> For every element of `SO(3)` there exists a basis indexed by `Fin 3` under which the first
> element remains invariant.

```lean
lemma exists_basis_preserved (A : SO(3)) :
    ∃ (b : OrthonormalBasis (Fin 3) ℝ (EuclideanSpace ℝ (Fin 3))), A.toEnd (b 0) = b 0
```

**`GroupTheory.SO3.eq_of_apply_two`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean#L192).

> A rotation fixing the third axis is a rotation in the first two coordinates.

```lean
lemma eq_of_apply_two (A : SO(3)) (hA : ∀ i, A.1 i 2 = if i = 2 then 1 else 0) :
    A.1 = !![A.1 0 0, A.1 0 1, 0; -A.1 0 1, A.1 0 0, 0; 0, 0, 1]
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Groups/SO3/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Groups/SO3/Basic.lean)
