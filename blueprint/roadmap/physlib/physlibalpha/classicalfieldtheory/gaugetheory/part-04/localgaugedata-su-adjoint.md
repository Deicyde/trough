---
declaration: module
origin: cited
lean: suTensor.adjBasis, suTensor.adjBasis_apply, suTensor.val_inv_mul_val, suTensor.val_inv, suTensor.adjRep, suTensor.adjMat, suTensor.adjMat_tmul, suTensor.adjMat_adjBasis
statement: formalized
proof: formalized
---

# The adjoint representation of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.SU.Adjoint`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean): 27 declarations, 21 with a docstring.

## i. Overview

> The adjoint representation of `SU(N)` acts on the complexified Lie algebra
> `SUAlgebraComplexified N = ℂ ⊗[ℝ] su(N)` as the complexification of the conjugation action
> `X ↦ g X g⁻¹` on `su(N)` (A). The generalized Gell-Mann matrices, a real basis of `su(N)`, give the
> basis `adjBasis N` of the complexified Lie algebra. Sending `z ⊗ X` to the matrix `z X` identifies
> the complexified Lie algebra with the traceless complex matrices (`adjMat`), injectively
> (`adjMat_injective`) and onto (`adjMat_ofTraceless`), and on matrices the adjoint action is
> conjugation (`adjMat_adjRep`). The coordinates in the Gell-Mann basis are the trace pairings
> `tr (λ_a A) / 2`.
>
> In the Gell-Mann basis the adjoint action of `g` has the matrix `adjMatrix g`, with entries
> `tr (λ_a g λ_b g⁻¹) / 2`: real, the Gell-Mann matrices being hermitian, and orthogonal, the matrix
> of `g⁻¹` being the transpose (B).
>
> The trace form `A ⊗ B ↦ tr (A B)` is symmetric and nondegenerate, the trace pairing with a Gell-Mann
> matrix being twice the coordinate, and it is invariant under the adjoint action, so it is the
> contraction `adjContr` of two adjoint indices (C).

## ii. Key results

> - `suTensor.adjRep` : the adjoint representation on the complexified Lie algebra.
> - `suTensor.adjMat` : the complexified Lie algebra as traceless complex matrices.
> - `suTensor.adjMatrix` : the matrix of the adjoint action in the Gell-Mann basis.
> - `suTensor.adjMatrix_inv` : the matrix of `g⁻¹` is the transpose of that of `g`.
> - `suTensor.traceForm_nondegenerate` : the trace form is nondegenerate.
> - `suTensor.adjContr` : the contraction of two adjoint indices.

## iv. References

> * None.

## A. The adjoint representation on the complexified Lie algebra

**`suTensor.adjBasis`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L70).

> The generalized Gell-Mann basis `1 ⊗ λ_a` of the complexified Lie algebra `ℂ ⊗[ℝ] su(N)`.

```lean
noncomputable def adjBasis : Basis (GellMann.Index N) ℂ (SUAlgebraComplexified N)
```

**`suTensor.adjBasis_apply`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L73).

```lean
lemma adjBasis_apply (a : GellMann.Index N) :
    adjBasis N a = (1 : ℂ) ⊗ₜ[ℝ] GellMann.realBasis a
```

**`suTensor.val_inv_mul_val`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L79).

```lean
lemma val_inv_mul_val (g : SU N) : (g⁻¹).1 * g.1 = 1
```

**`suTensor.val_inv`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L83).

```lean
lemma val_inv (g : SU N) : (g⁻¹).1 = star g.1
```

**`suTensor.adjRep`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L93).

> The adjoint representation on the complexified Lie algebra: the complexification of the
> adjoint action `X ↦ g X g⁻¹` on `su(N)`.

```lean
noncomputable def adjRep : Representation ℂ (SU N) (SUAlgebraComplexified N)
```

**`suTensor.adjMat`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L104).

> The matrix of an element of the complexified Lie algebra, `z ⊗ X ↦ z X`: a traceless complex
> matrix.

```lean
noncomputable def adjMat : SUAlgebraComplexified N →ₗ[ℂ] Matrix (Fin N) (Fin N) ℂ
```

**`suTensor.adjMat_tmul`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L110).

```lean
lemma adjMat_tmul (z : ℂ) (X : SUAlgebra N) : adjMat N (z ⊗ₜ X) = z • X.1
```

**`suTensor.adjMat_adjBasis`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L113).

```lean
lemma adjMat_adjBasis (a : GellMann.Index N) : adjMat N (adjBasis N a) = GellMann.matrix a
```

**`suTensor.trace_adjMat`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L117).

> The matrix of an element of the complexified Lie algebra is traceless.

```lean
lemma trace_adjMat (A : SUAlgebraComplexified N) : (adjMat N A).trace = 0
```

**`suTensor.adjMat_adjRep`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L124).

> The adjoint representation moves the matrix by conjugation.

```lean
lemma adjMat_adjRep (g : SU N) (A : SUAlgebraComplexified N) :
    adjMat N (adjRep N g A) = g.1 * adjMat N A * (g⁻¹).1
```

**`suTensor.adjBasis_repr_apply`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L135).

> The coordinates in the Gell-Mann basis are read off by the trace form,
> `A = ∑ (tr (λ_a A) / 2) λ_a`.

```lean
lemma adjBasis_repr_apply (A : SUAlgebraComplexified N) (a : GellMann.Index N) :
    (adjBasis N).repr A a = (GellMann.matrix a * adjMat N A).trace / 2
```

**`suTensor.adjMat_injective`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L144).

> An element of the complexified Lie algebra is determined by its matrix.

```lean
lemma adjMat_injective : Function.Injective (adjMat N)
```

**`suTensor.ofTraceless`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L148).

> The element of the complexified Lie algebra with a given traceless matrix.

```lean
noncomputable def ofTraceless (M : Matrix (Fin N) (Fin N) ℂ) : SUAlgebraComplexified N
```

**`suTensor.adjMat_ofTraceless`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L153).

> Every traceless matrix is the matrix of an element of the complexified Lie algebra.

```lean
lemma adjMat_ofTraceless {M : Matrix (Fin N) (Fin N) ℂ} (hM : M.trace = 0) :
    adjMat N (ofTraceless M) = M
```

## B. The matrix of the adjoint action

**`suTensor.adjMatrix`**, an abbrev, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L169).

> The matrix of the adjoint action of `g` in the Gell-Mann basis.

```lean
noncomputable abbrev adjMatrix (g : SU N) : Matrix (GellMann.Index N) (GellMann.Index N) ℂ
```

**`suTensor.adjMatrix_apply`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L173).

> The entries of the matrix of the adjoint action, `tr (λ_a g λ_b g⁻¹) / 2`.

```lean
lemma adjMatrix_apply (g : SU N) (a b : GellMann.Index N) :
    adjMatrix g a b = (GellMann.matrix a * (g.1 * GellMann.matrix b * (g⁻¹).1)).trace / 2
```

**`suTensor.star_adjMatrix_apply`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L178).

> The matrix of the adjoint action is real, the Gell-Mann matrices being hermitian.

```lean
lemma star_adjMatrix_apply (g : SU N) (a b : GellMann.Index N) :
    star (adjMatrix g a b) = adjMatrix g a b
```

**`suTensor.adjMatrix_inv`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L190).

> The matrix of the adjoint action of `g⁻¹` is the transpose of that of `g`, by the cyclicity
> of the trace.

```lean
lemma adjMatrix_inv (g : SU N) : adjMatrix g⁻¹ = (adjMatrix g)ᵀ
```

**`suTensor.adjMatrix_inv_mul`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L200).

> The matrix of the adjoint action of `g⁻¹` times that of `g` is the identity.

```lean
lemma adjMatrix_inv_mul (g : SU N) : adjMatrix g⁻¹ * adjMatrix g = 1
```

## C. The trace form and the contraction

**`suTensor.traceForm`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L213).

> The trace form `A ⊗ B ↦ tr (A B)` on the complexified Lie algebra.

```lean
noncomputable def traceForm : LinearMap.BilinForm ℂ (SUAlgebraComplexified N)
```

**`suTensor.traceForm_apply`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L221).

```lean
lemma traceForm_apply (A B : SUAlgebraComplexified N) :
    traceForm N A B = (adjMat N A * adjMat N B).trace
```

**`suTensor.traceForm_isSymm`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L225).

> The trace form is symmetric.

```lean
lemma traceForm_isSymm : (traceForm N).IsSymm
```

**`suTensor.traceForm_adjBasis`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L229).

> The trace form against a Gell-Mann basis vector is twice the coordinate.

```lean
lemma traceForm_adjBasis (A : SUAlgebraComplexified N) (a : GellMann.Index N) :
    traceForm N A (adjBasis N a) = 2 * (adjBasis N).repr A a
```

**`suTensor.traceForm_separatingLeft`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L236).

> An element orthogonal to every element under the trace form vanishes: its coordinates are its
> trace pairings with the Gell-Mann basis.

```lean
lemma traceForm_separatingLeft (A : SUAlgebraComplexified N) (hA : ∀ B, traceForm N A B = 0) :
    A = 0
```

**`suTensor.traceForm_nondegenerate`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L244).

> The trace form is nondegenerate on the complexified Lie algebra.

```lean
lemma traceForm_nondegenerate : (traceForm N).Nondegenerate
```

**`suTensor.adjContr`**, a def, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L250).

> The contraction of two adjoint indices, the trace form `A ⊗ B ↦ tr (A B)`.

```lean
noncomputable def adjContr : ((adjRep N).tprod (adjRep N)).IntertwiningMap
    (Representation.trivial ℂ (SU N) ℂ)
```

**`suTensor.adjContr_flip_injective`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean#L263).

> The trace form separates the complexified Lie algebra.

```lean
lemma adjContr_flip_injective :
    Function.Injective (TensorProduct.curry (adjContr N).toLinearMap).flip
```

## Depends on

- [The local gauge data of `SU(n)`](localgaugedata-su-basic.md)
- [The generalized Gell-Mann matrices (PhyslibAlpha)](localgaugedata-su-gellmann.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Adjoint.lean)
