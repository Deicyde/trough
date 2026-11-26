---
declaration: module
origin: cited
lean: SU, SUAlgebra, SUAlgebra.adjointValue, SUAlgebra.adjointValue_val, suTensor.adjBasis, suTensor.adjBasis_apply, suTensor.val_inv_mul_val, suTensor.val_inv
statement: formalized
proof: formalized
---

# The adjoint representation of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Adjoint`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean): 41 declarations, 31 with a docstring.

> The action of `SU(N)` on its complexified Lie algebra, and its matrix in the Gell-Mann basis.

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
>
> For two distinct coordinates `p` and `q`, an element `U` of `SU(2)` acts on the plane they span
> and fixes the other coordinates. This is `SU.planeEmbed p q`, a group homomorphism from `SU(2)`
> to `SU(N)` (D), built from the plane matrices of
> `PhyslibAlpha.Mathematics.ForMathlib.DataStructures.Matrix.PlaneMatrix`. A diagonal phase
> `diag (u, ū)` and the rotation by a quarter turn, embedded in every plane, force a matrix commuting
> with all of `SU(N)` to be scalar (E). The matrix `adjMat A` of an invariant of the adjoint
> representation commutes with every element of `SU(N)`, so it is a scalar, and it is traceless, so
> the adjoint representation has no invariants but zero (F).

## ii. Key results

> - `suTensor.adjRep` : the adjoint representation on the complexified Lie algebra.
> - `suTensor.adjMat` : the complexified Lie algebra as traceless complex matrices.
> - `suTensor.adjMatrix` : the matrix of the adjoint action in the Gell-Mann basis.
> - `suTensor.adjMatrix_inv` : the matrix of `g⁻¹` is the transpose of that of `g`.
> - `suTensor.traceForm_nondegenerate` : the trace form is nondegenerate.
> - `suTensor.adjContr` : the contraction of two adjoint indices.
> - `SU.planeEmbed` : `SU(2)` acting on the plane of two coordinates, as a subgroup of `SU(N)`.
> - `SU.eq_smul_one_of_commute` : a matrix commuting with `SU(N)` is scalar.
> - `suTensor.invariants_adjRep_eq_bot` : the adjoint representation has no invariants but zero.

## iv. References

> * None.

**`SU`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L80).

> The gauge group `SU(n)`, the special unitary matrices.

```lean
abbrev SU (n : ℕ) : Type
```

**`SUAlgebra`**, an abbrev, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L83).

> The Lie algebra `su(n)`, the traceless hermitian matrices.

```lean
abbrev SUAlgebra (n : ℕ) : Type
```

**`SUAlgebra.adjointValue`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L86).

> The adjoint action `a ↦ U a U†` of `SU(n)` on `su(n)`.

```lean
noncomputable def SUAlgebra.adjointValue {n : ℕ} : Representation ℝ (SU n) (SUAlgebra n)
```

**`SUAlgebra.adjointValue_val`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L91).

```lean
lemma SUAlgebra.adjointValue_val {n : ℕ} (U : SU n) (a : SUAlgebra n) :
    (SUAlgebra.adjointValue U a).1 = U.1 * a.1 * star U.1
```

## A. The adjoint representation on the complexified Lie algebra

**`suTensor.adjBasis`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L105).

> The generalized Gell-Mann basis `1 ⊗ λ_a` of the complexified Lie algebra `ℂ ⊗[ℝ] su(N)`.

```lean
noncomputable def adjBasis : Basis (GellMann.Index N) ℂ (SUAlgebraComplexified N)
```

**`suTensor.adjBasis_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L108).

```lean
lemma adjBasis_apply (a : GellMann.Index N) :
    adjBasis N a = (1 : ℂ) ⊗ₜ[ℝ] GellMann.realBasis a
```

**`suTensor.val_inv_mul_val`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L114).

```lean
lemma val_inv_mul_val (g : SU N) : (g⁻¹).1 * g.1 = 1
```

**`suTensor.val_inv`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L118).

```lean
lemma val_inv (g : SU N) : (g⁻¹).1 = star g.1
```

**`suTensor.adjRep`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L128).

> The adjoint representation on the complexified Lie algebra, the complexification of the
> adjoint action `X ↦ g X g⁻¹` on `su(N)`.

```lean
noncomputable def adjRep : Representation ℂ (SU N) (SUAlgebraComplexified N)
```

**`suTensor.adjMat`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L139).

> The matrix of an element of the complexified Lie algebra, `z ⊗ X ↦ z X`, a traceless complex
> matrix.

```lean
noncomputable def adjMat : SUAlgebraComplexified N →ₗ[ℂ] Matrix (Fin N) (Fin N) ℂ
```

**`suTensor.adjMat_tmul`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L145).

```lean
lemma adjMat_tmul (z : ℂ) (X : SUAlgebra N) : adjMat N (z ⊗ₜ X) = z • X.1
```

**`suTensor.adjMat_adjBasis`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L148).

```lean
lemma adjMat_adjBasis (a : GellMann.Index N) : adjMat N (adjBasis N a) = GellMann.matrix a
```

**`suTensor.trace_adjMat`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L152).

> The matrix of an element of the complexified Lie algebra is traceless.

```lean
lemma trace_adjMat (A : SUAlgebraComplexified N) : (adjMat N A).trace = 0
```

**`suTensor.adjMat_adjRep`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L159).

> The adjoint representation moves the matrix by conjugation.

```lean
lemma adjMat_adjRep (g : SU N) (A : SUAlgebraComplexified N) :
    adjMat N (adjRep N g A) = g.1 * adjMat N A * (g⁻¹).1
```

**`suTensor.adjBasis_repr_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L170).

> The coordinates in the Gell-Mann basis are read off by the trace form,
> `A = ∑ (tr (λ_a A) / 2) λ_a`.

```lean
lemma adjBasis_repr_apply (A : SUAlgebraComplexified N) (a : GellMann.Index N) :
    (adjBasis N).repr A a = (GellMann.matrix a * adjMat N A).trace / 2
```

**`suTensor.adjMat_injective`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L179).

> An element of the complexified Lie algebra is determined by its matrix.

```lean
lemma adjMat_injective : Function.Injective (adjMat N)
```

**`suTensor.ofTraceless`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L183).

> The element of the complexified Lie algebra with a given traceless matrix.

```lean
noncomputable def ofTraceless (M : Matrix (Fin N) (Fin N) ℂ) : SUAlgebraComplexified N
```

**`suTensor.adjMat_ofTraceless`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L188).

> Every traceless matrix is the matrix of an element of the complexified Lie algebra.

```lean
lemma adjMat_ofTraceless {M : Matrix (Fin N) (Fin N) ℂ} (hM : M.trace = 0) :
    adjMat N (ofTraceless M) = M
```

## B. The matrix of the adjoint action

**`suTensor.adjMatrix`**, an abbrev, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L204).

> The matrix, in the Gell-Mann basis, of the adjoint action of an element of `SU(N)`.

```lean
noncomputable abbrev adjMatrix (g : SU N) : Matrix (GellMann.Index N) (GellMann.Index N) ℂ
```

**`suTensor.adjMatrix_apply`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L208).

> The entries of the matrix of the adjoint action, `tr (λ_a g λ_b g⁻¹) / 2`.

```lean
lemma adjMatrix_apply (g : SU N) (a b : GellMann.Index N) :
    adjMatrix g a b = (GellMann.matrix a * (g.1 * GellMann.matrix b * (g⁻¹).1)).trace / 2
```

**`suTensor.star_adjMatrix_apply`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L213).

> The matrix of the adjoint action is real, the Gell-Mann matrices being hermitian.

```lean
lemma star_adjMatrix_apply (g : SU N) (a b : GellMann.Index N) :
    star (adjMatrix g a b) = adjMatrix g a b
```

**`suTensor.adjMatrix_inv`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L225).

> The matrix of the adjoint action of the inverse of an element of `SU(N)` is the transpose of
> that of the element, by the cyclicity of the trace.

```lean
lemma adjMatrix_inv (g : SU N) : adjMatrix g⁻¹ = (adjMatrix g)ᵀ
```

**`suTensor.adjMatrix_inv_mul`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L236).

> The matrix of the adjoint action of the inverse of an element of `SU(N)` times that of the
> element is the identity.

```lean
lemma adjMatrix_inv_mul (g : SU N) : adjMatrix g⁻¹ * adjMatrix g = 1
```

## C. The trace form and the contraction

**`suTensor.traceForm`**, a def, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L249).

> The trace form `A ⊗ B ↦ tr (A B)` on the complexified Lie algebra.

```lean
noncomputable def traceForm : LinearMap.BilinForm ℂ (SUAlgebraComplexified N)
```

**`suTensor.traceForm_apply`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L257).

```lean
lemma traceForm_apply (A B : SUAlgebraComplexified N) :
    traceForm N A B = (adjMat N A * adjMat N B).trace
```

**`suTensor.traceForm_isSymm`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L261).

> The trace form is symmetric.

```lean
lemma traceForm_isSymm : (traceForm N).IsSymm
```

**`suTensor.traceForm_adjBasis`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L265).

> The trace form against a Gell-Mann basis vector is twice the coordinate.

```lean
lemma traceForm_adjBasis (A : SUAlgebraComplexified N) (a : GellMann.Index N) :
    traceForm N A (adjBasis N a) = 2 * (adjBasis N).repr A a
```

**`suTensor.traceForm_separatingLeft`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L272).

> An element orthogonal to every element under the trace form vanishes. Its coordinates are its
> trace pairings with the Gell-Mann basis.

```lean
lemma traceForm_separatingLeft (A : SUAlgebraComplexified N) (hA : ∀ B, traceForm N A B = 0) :
    A = 0
```

**`suTensor.traceForm_nondegenerate`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L280).

> The trace form is nondegenerate on the complexified Lie algebra.

```lean
lemma traceForm_nondegenerate : (traceForm N).Nondegenerate
```

**`suTensor.adjContr`**, a def, [line 286](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L286).

> The contraction of two adjoint indices, the trace form `A ⊗ B ↦ tr (A B)`.

```lean
noncomputable def adjContr : ((adjRep N).tprod (adjRep N)).IntertwiningMap
    (Representation.trivial ℂ (SU N) ℂ)
```

**`suTensor.adjContr_flip_injective`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L299).

> The trace form separates the complexified Lie algebra.

```lean
lemma adjContr_flip_injective :
    Function.Injective (TensorProduct.curry (adjContr N).toLinearMap).flip
```

## D. The plane embedding of `SU(2)`

**`SU.planeEmbed`**, a def, [line 323](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L323).

> `SU(2)` acting on the plane of two distinct coordinates `p` and `q` and trivially on the
> others, a homomorphism from `SU(2)` to `SU(N)`.

```lean
noncomputable def planeEmbed (p q : Fin N) (hpq : p ≠ q) : SU 2 →* SU N
```

**`SU.planeEmbed_val`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L334).

```lean
lemma planeEmbed_val (hpq : p ≠ q) (U : SU 2) : (planeEmbed p q hpq U).1 = planeMatrix p q U.1
```

**`SU.diagPhase`**, a def, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L338).

> The diagonal element `diag (u, ū)` of `SU(2)`, for any complex number `u` of modulus one.

```lean
noncomputable def diagPhase (u : ℂ) (hu : u * star u = 1) : SU 2
```

**`SU.diagPhase_val`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L351).

```lean
lemma diagPhase_val (u : ℂ) (hu : u * star u = 1) :
    (diagPhase u hu).1 = diagonal ![u, star u]
```

**`SU.rotation`**, a def, [line 356](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L356).

> The real rotation of `SU(2)` with matrix `!![c, -s; s, c]`, for any real cosine `c` and sine
> `s` with `c² + s² = 1`.

```lean
noncomputable def rotation (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) : SU 2
```

**`SU.rotation_val`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L367).

```lean
lemma rotation_val (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    (rotation c s h).1 = !![(c : ℂ), -s; s, c]
```

## E. Matrices commuting with `SU(N)`

> The diagonal phase `diag (i, -i)` in the plane of `p` and `q` negates the entries at `(p, q)`
> and `(q, p)` of a matrix it commutes with, and the quarter turn exchanges the diagonal entries
> at `p` and `q`.

**`SU.conj_eq_of_commute`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L381).

> A matrix commuting with every element of `SU(N)` is fixed by conjugation.

```lean
lemma conj_eq_of_commute {C : Matrix (Fin N) (Fin N) ℂ} (hC : ∀ g : SU N, g.1 * C = C * g.1)
    (g : SU N) : g.1 * C * g.1ᴴ = C
```

**`SU.apply_eq_of_commute`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L390).

> A matrix commuting with every element of `SU(N)` is diagonal, with equal diagonal
> entries.

```lean
lemma apply_eq_of_commute {C : Matrix (Fin N) (Fin N) ℂ} (hC : ∀ g : SU N, g.1 * C = C * g.1)
    (hpq : p ≠ q) : C p q = 0 ∧ C p p = C q q
```

**`SU.eq_smul_one_of_commute`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L408).

> A matrix commuting with every element of `SU(N)` is scalar.

```lean
lemma eq_smul_one_of_commute {C : Matrix (Fin N) (Fin N) ℂ}
    (hC : ∀ g : SU N, g.1 * C = C * g.1) : ∃ z : ℂ, C = z • 1
```

## F. One adjoint index has no invariants

> An invariant of the adjoint representation is a traceless matrix commuting with every element of
> `SU(N)`, so it is a scalar by E, and its trace vanishes.

**`suTensor.invariants_adjRep_eq_bot`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean#L439).

> The adjoint representation has no invariants but zero. The matrix of an invariant commutes
> with every element of `SU(N)`, so it is a scalar, and its trace vanishes.

```lean
lemma invariants_adjRep_eq_bot : (adjRep N).invariants = ⊥
```

## Depends on

- [The generalized Gell-Mann matrices (PhyslibAlpha)](globalgaugegroup-su-gellmann.md)
- [Matrices acting in a coordinate plane](../../../mathematics/part-02/formathlib/datastructures-matrix-planematrix.md)

## Proof depends on

- [Invariants and intertwining maps out of the trivial representation](../../../mathematics/part-02/representationtheory/invariants.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Adjoint.lean)
