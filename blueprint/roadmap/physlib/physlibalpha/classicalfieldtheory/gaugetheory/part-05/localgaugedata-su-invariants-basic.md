---
declaration: module
origin: cited
lean: SU.planeInclusion, SU.planeInclusion_apply, SU.planeInclusion_transpose_mul, SU.conjTranspose_planeInclusion, SU.planeMatrix, SU.planeMatrix_one, SU.planeMatrix_mul, SU.conjTranspose_planeMatrix
statement: formalized
proof: formalized
---

# Elements of `SU(N)` in a coordinate plane, and what commutes with them

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.SU.Invariants.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean): 56 declarations, 37 with a docstring.

## i. Overview

> For two distinct coordinates `p` and `q`, an element `U` of `SU(2)` acts on the plane they span
> and fixes the other coordinates: this is `SU.planeEmbed p q`, a group homomorphism from `SU(2)`
> to `SU(N)` (A, B). Writing `P` for the inclusion of the plane, the embedded element is
> `1 + P (U - 1) Pᵀ`, and conjugating `P M Pᵀ` by it gives `P (U M U†) Pᵀ`, so the action on the
> matrices supported on the plane is computed in `SU(2)`.
>
> Three elements of `SU(2)` do all the work: a diagonal phase `diag (u, ū)`, the rotation by a
> quarter turn, and the rotation by an eighth of a turn. Embedded in every plane, they force a
> matrix commuting with all of `SU(N)` to be scalar (C), and a linear endomorphism of the
> complexified Lie algebra `ℂ ⊗[ℝ] su(N)` commuting with the adjoint action to be scalar (D); the
> latter is computed on the matrices `adjMat A`, which identify the complexified Lie algebra with the
> traceless complex matrices. These are the two facts behind the
> classification of the invariant tensors of `SU(N)` with a fundamental and an anti-fundamental
> index, and with one or two adjoint indices.

## ii. Key results

> - `SU.planeEmbed` : `SU(2)` acting on the plane of two coordinates, as a subgroup of `SU(N)`.
> - `SU.eq_smul_one_of_commute` : a matrix commuting with `SU(N)` is scalar.
> - `suTensor.eq_smul_id_of_commute_adjRep` : an endomorphism of the complexified Lie algebra
>   commuting with the adjoint action is scalar.

## iv. References

> * None.

## A. The plane matrices

**`SU.planeInclusion`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L66).

> The inclusion of the plane of the coordinates `p` and `q`: the `N × 2` matrix whose columns
> are the basis vectors `e_p` and `e_q`.

```lean
def planeInclusion (p q : Fin N) : Matrix (Fin N) (Fin 2) ℂ
```

**`SU.planeInclusion_apply`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L70).

```lean
lemma planeInclusion_apply (p q : Fin N) (x : Fin N) (i : Fin 2) :
    planeInclusion p q x i = if x = ![p, q] i then 1 else 0
```

**`SU.planeInclusion_transpose_mul`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L74).

> The inclusion of the plane of two distinct coordinates is an isometry.

```lean
lemma planeInclusion_transpose_mul {p q : Fin N} (hpq : p ≠ q) :
    (planeInclusion p q)ᵀ * planeInclusion p q = 1
```

**`SU.conjTranspose_planeInclusion`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L82).

> The inclusion of the plane has real entries, so its conjugate transpose is its transpose.

```lean
lemma conjTranspose_planeInclusion (p q : Fin N) :
    (planeInclusion p q)ᴴ = (planeInclusion p q)ᵀ
```

**`SU.planeMatrix`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L90).

> The matrix acting as `U` on the plane of the coordinates `p` and `q` and as the identity on
> the other coordinates.

```lean
def planeMatrix (p q : Fin N) (U : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin N) (Fin N) ℂ
```

**`SU.planeMatrix_one`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L97).

> The plane matrix of the identity is the identity.

```lean
lemma planeMatrix_one : planeMatrix p q 1 = 1
```

**`SU.planeMatrix_mul`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L101).

> The plane matrices multiply as the matrices on the plane.

```lean
lemma planeMatrix_mul (hpq : p ≠ q) (U V : Matrix (Fin 2) (Fin 2) ℂ) :
    planeMatrix p q U * planeMatrix p q V = planeMatrix p q (U * V)
```

**`SU.conjTranspose_planeMatrix`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L116).

> The conjugate transpose of a plane matrix is the plane matrix of the conjugate
> transpose.

```lean
lemma conjTranspose_planeMatrix (U : Matrix (Fin 2) (Fin 2) ℂ) :
    (planeMatrix p q U)ᴴ = planeMatrix p q Uᴴ
```

**`SU.det_planeMatrix`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L127).

> A plane matrix has the determinant of the matrix on the plane.

```lean
lemma det_planeMatrix (hpq : p ≠ q) (U : Matrix (Fin 2) (Fin 2) ℂ) :
    (planeMatrix p q U).det = U.det
```

**`SU.planeMatrix_mul_planeInclusion`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L133).

> A plane matrix moves the plane as the matrix on the plane does.

```lean
lemma planeMatrix_mul_planeInclusion (hpq : p ≠ q) (U : Matrix (Fin 2) (Fin 2) ℂ) :
    planeMatrix p q U * planeInclusion p q = planeInclusion p q * U
```

**`SU.transpose_planeInclusion_mul_planeMatrix`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L141).

> The transpose of the inclusion of the plane intertwines a plane matrix with the matrix on
> the plane.

```lean
lemma transpose_planeInclusion_mul_planeMatrix (hpq : p ≠ q) (U : Matrix (Fin 2) (Fin 2) ℂ) :
    (planeInclusion p q)ᵀ * planeMatrix p q U = U * (planeInclusion p q)ᵀ
```

**`SU.planeMatrix_conj`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L148).

> Conjugating a matrix supported on the plane by a plane matrix conjugates it on the plane.

```lean
lemma planeMatrix_conj (hpq : p ≠ q) (U M : Matrix (Fin 2) (Fin 2) ℂ) :
    planeMatrix p q U * (planeInclusion p q * M * (planeInclusion p q)ᵀ) * (planeMatrix p q U)ᴴ
      = planeInclusion p q * (U * M * Uᴴ) * (planeInclusion p q)ᵀ
```

**`SU.planeBlock_conj`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L158).

> The block on the plane of a matrix conjugated by a plane matrix is the conjugate of its
> block.

```lean
lemma planeBlock_conj (hpq : p ≠ q) (U : Matrix (Fin 2) (Fin 2) ℂ) (C : Matrix (Fin N) (Fin N) ℂ) :
    (planeInclusion p q)ᵀ * (planeMatrix p q U * C * (planeMatrix p q U)ᴴ) * planeInclusion p q
      = U * ((planeInclusion p q)ᵀ * C * planeInclusion p q) * Uᴴ
```

**`SU.planeBlock_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L170).

> The entries of the block on the plane are the entries of the matrix at the two
> coordinates.

```lean
lemma planeBlock_apply (C : Matrix (Fin N) (Fin N) ℂ) (i j : Fin 2) :
    ((planeInclusion p q)ᵀ * C * planeInclusion p q) i j = C (![p, q] i) (![p, q] j)
```

**`SU.planeMatrix_diagonal`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L175).

> A plane matrix of a diagonal matrix is diagonal.

```lean
lemma planeMatrix_diagonal (hpq : p ≠ q) (a b : ℂ) :
    planeMatrix p q (diagonal ![a, b])
      = diagonal fun x => if x = p then a else if x = q then b else 1
```

## B. The plane embedding of `SU(2)`

**`SU.planeEmbed`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L193).

> `SU(2)` acting on the plane of the coordinates `p` and `q` and trivially on the others: a
> homomorphism from `SU(2)` to `SU(N)`.

```lean
noncomputable def planeEmbed (p q : Fin N) (hpq : p ≠ q) : SU 2 →* SU N
```

**`SU.planeEmbed_val`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L204).

```lean
lemma planeEmbed_val (hpq : p ≠ q) (U : SU 2) : (planeEmbed p q hpq U).1 = planeMatrix p q U.1
```

**`SU.diagPhase`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L208).

> The diagonal element `diag (u, ū)` of `SU(2)`, for a complex number `u` of modulus one.

```lean
noncomputable def diagPhase (u : ℂ) (hu : u * star u = 1) : SU 2
```

**`SU.diagPhase_val`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L221).

```lean
lemma diagPhase_val (u : ℂ) (hu : u * star u = 1) :
    (diagPhase u hu).1 = diagonal ![u, star u]
```

**`SU.rotation`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L225).

> The rotation `!![c, -s; s, c]` of `SU(2)`, for real `c` and `s` with `c² + s² = 1`.

```lean
noncomputable def rotation (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) : SU 2
```

**`SU.rotation_val`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L236).

```lean
lemma rotation_val (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    (rotation c s h).1 = !![(c : ℂ), -s; s, c]
```

## C. Matrices commuting with `SU(N)`

> The diagonal phase `diag (i, -i)` in the plane of `p` and `q` negates the entries at `(p, q)`
> and `(q, p)` of a matrix it commutes with, and the quarter turn exchanges the diagonal entries
> at `p` and `q`.

**`SU.planeBlock_eq_of_conj_eq`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L251).

> A matrix fixed by conjugation by a plane matrix has its block on the plane fixed by
> conjugation by the matrix on the plane.

```lean
lemma planeBlock_eq_of_conj_eq (hpq : p ≠ q) {U : Matrix (Fin 2) (Fin 2) ℂ}
    {C : Matrix (Fin N) (Fin N) ℂ} (hC : planeMatrix p q U * C * (planeMatrix p q U)ᴴ = C) :
    U * ((planeInclusion p q)ᵀ * C * planeInclusion p q) * Uᴴ
      = (planeInclusion p q)ᵀ * C * planeInclusion p q
```

**`SU.conj_eq_of_commute`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L258).

> A matrix commuting with every element of `SU(N)` is fixed by conjugation.

```lean
lemma conj_eq_of_commute {C : Matrix (Fin N) (Fin N) ℂ} (hC : ∀ g : SU N, g.1 * C = C * g.1)
    (g : SU N) : g.1 * C * g.1ᴴ = C
```

**`SU.apply_eq_of_commute`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L267).

> A matrix commuting with every element of `SU(N)` is diagonal, with equal diagonal
> entries.

```lean
lemma apply_eq_of_commute {C : Matrix (Fin N) (Fin N) ℂ} (hC : ∀ g : SU N, g.1 * C = C * g.1)
    (hpq : p ≠ q) : C p q = 0 ∧ C p p = C q q
```

**`SU.eq_smul_one_of_commute`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L285).

> A matrix commuting with every element of `SU(N)` is scalar.

```lean
lemma eq_smul_one_of_commute {C : Matrix (Fin N) (Fin N) ℂ}
    (hC : ∀ g : SU N, g.1 * C = C * g.1) : ∃ z : ℂ, C = z • 1
```

## D. Endomorphisms of the complexified Lie algebra commuting with `SU(N)`

**`suTensor.offDiag`**, a def, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L314).

> The matrix unit at `(x, y)` off the diagonal, as an element of the complexified Lie algebra,
> and zero on the diagonal.

```lean
noncomputable def offDiag (x y : Fin N) : SUAlgebraComplexified N
```

**`suTensor.diagDiff`**, a def, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L319).

> The difference of the diagonal matrix units at `x` and at `y`, as an element of the
> complexified Lie algebra.

```lean
noncomputable def diagDiff (x y : Fin N) : SUAlgebraComplexified N
```

**`suTensor.adjMat_offDiag`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L322).

```lean
lemma adjMat_offDiag (x y : Fin N) :
    adjMat N (offDiag x y) = if x = y then 0 else single x y 1
```

**`suTensor.adjMat_offDiag_of_ne`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L329).

```lean
lemma adjMat_offDiag_of_ne {x y : Fin N} (h : x ≠ y) : adjMat N (offDiag x y) = single x y 1
```

**`suTensor.offDiag_self`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L333).

```lean
lemma offDiag_self (x : Fin N) : offDiag x x = 0
```

**`suTensor.adjMat_diagDiff`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L337).

```lean
lemma adjMat_diagDiff (x y : Fin N) : adjMat N (diagDiff x y) = single x x 1 - single y y 1
```

**`suTensor.diagDiff_self`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L341).

```lean
lemma diagDiff_self (x : Fin N) : diagDiff x x = 0
```

**`suTensor.planeInclusion_single`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L346).

> The inclusion of the plane carries the matrix units of the plane to those of the
> coordinates.

```lean
lemma planeInclusion_single (p q : Fin N) (i j : Fin 2) :
    planeInclusion p q * single i j (1 : ℂ) * (planeInclusion p q)ᵀ
      = single (![p, q] i) (![p, q] j) 1
```

**`suTensor.adjMat_adjRep_planeEmbed`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L366).

> The adjoint action of an element of `SU(2)` embedded in a plane on a matrix supported on the
> plane.

```lean
lemma adjMat_adjRep_planeEmbed {p q : Fin N} (hpq : p ≠ q) (U : SU 2)
    (A : SUAlgebraComplexified N) (M : Matrix (Fin 2) (Fin 2) ℂ)
    (hA : adjMat N A = planeInclusion p q * M * (planeInclusion p q)ᵀ) :
    adjMat N (adjRep N (planeEmbed p q hpq U) A)
      = planeInclusion p q * (U.1 * M * U.1ᴴ) * (planeInclusion p q)ᵀ
```

**`suTensor.sqrtI`**, a def, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L375).

> The phase `(1 + i) / √2`, a square root of `i` of modulus one.

```lean
noncomputable def sqrtI : ℂ
```

**`suTensor.sqrt_two_mul_sqrt_two`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L377).

```lean
lemma sqrt_two_mul_sqrt_two : (Real.sqrt 2 : ℂ) * (Real.sqrt 2 : ℂ) = 2
```

**`suTensor.sqrt_two_ne_zero`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L381).

```lean
lemma sqrt_two_ne_zero : (Real.sqrt 2 : ℂ) ≠ 0
```

**`suTensor.star_sqrtI`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L384).

```lean
lemma star_sqrtI : star sqrtI = (1 - Complex.I) / (Real.sqrt 2 : ℂ)
```

**`suTensor.sqrtI_mul_star`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L387).

```lean
lemma sqrtI_mul_star : sqrtI * star sqrtI = 1
```

**`suTensor.sqrtI_mul_self`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L393).

```lean
lemma sqrtI_mul_self : sqrtI * sqrtI = Complex.I
```

**`suTensor.star_sqrtI_mul_self`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L399).

```lean
lemma star_sqrtI_mul_self : star sqrtI * star sqrtI = -Complex.I
```

**`suTensor.sqrtI_ne_I`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L402).

```lean
lemma sqrtI_ne_I : sqrtI ≠ Complex.I
```

**`suTensor.star_sqrtI_ne_I`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L408).

```lean
lemma star_sqrtI_ne_I : star sqrtI ≠ Complex.I
```

**`suTensor.adjMat_adjRep_apply_of_diagonal`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L416).

> The adjoint action of a diagonal matrix of `SU(N)` scales the entry at `(x, y)` by
> `d x * star (d y)`.

```lean
lemma adjMat_adjRep_apply_of_diagonal {g : SU N} {d : Fin N → ℂ} (hg : g.1 = diagonal d)
    (A : SUAlgebraComplexified N) (x y : Fin N) :
    adjMat N (adjRep N g A) x y = d x * adjMat N A x y * star (d y)
```

**`suTensor.map_offDiag_eq_smul`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L428).

> For `p ≠ q`, an endomorphism commuting with the adjoint action sends the matrix unit at
> `(p, q)` to a multiple of itself. The phase `diag (ω, ω̄)` in the plane of `p` and `q`, with
> `ω² = i`, multiplies that matrix unit by `i` and no other entry by `i`.

```lean
lemma map_offDiag_eq_smul (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) {p q : Fin N} (hpq : p ≠ q) :
    L (offDiag p q) = adjMat N (L (offDiag p q)) p q • offDiag p q
```

**`suTensor.adjRep_quarterTurn_offDiag`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L475).

> The quarter turn in the plane of `p` and `q` sends the matrix unit at `(p, q)` to minus the
> one at `(q, p)`.

```lean
lemma adjRep_quarterTurn_offDiag {p q : Fin N} (hpq : p ≠ q) :
    adjRep N (planeEmbed p q hpq (rotation 0 1 (by norm_num))) (offDiag p q) = -offDiag q p
```

**`suTensor.coeff_offDiag_swap`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L490).

> The coefficients of the matrix units at `(p, q)` and at `(q, p)` agree.

```lean
lemma coeff_offDiag_swap (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) {p q : Fin N} (hpq : p ≠ q) :
    adjMat N (L (offDiag q p)) q p = adjMat N (L (offDiag p q)) p q
```

**`suTensor.invSqrtTwo`**, a def, [line 500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L500).

> The cosine of an eighth of a turn, `1 / √2`.

```lean
noncomputable def invSqrtTwo : ℝ
```

**`suTensor.invSqrtTwo_sq_add`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L502).

```lean
lemma invSqrtTwo_sq_add : invSqrtTwo ^ 2 + invSqrtTwo ^ 2 = 1
```

**`suTensor.invSqrtTwo_mul_self`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L506).

```lean
lemma invSqrtTwo_mul_self : (invSqrtTwo : ℂ) * invSqrtTwo = 1 / 2
```

**`suTensor.adjRep_eighthTurn_offDiag`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L513).

> The eighth turn in the plane of `p` and `q` sends the sum of the matrix units at `(p, q)`
> and at `(q, p)` to minus the difference of the diagonal matrix units at `p` and at `q`.

```lean
lemma adjRep_eighthTurn_offDiag {p q : Fin N} (hpq : p ≠ q) :
    adjRep N (planeEmbed p q hpq (rotation invSqrtTwo invSqrtTwo invSqrtTwo_sq_add))
      (offDiag p q + offDiag q p) = -diagDiff p q
```

**`suTensor.map_diagDiff_eq_smul`**, a lemma, [line 535](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L535).

> For `p ≠ q`, an endomorphism commuting with the adjoint action scales the difference of the
> diagonal matrix units at `p` and at `q` by the coefficient of the matrix unit at `(p, q)`.

```lean
lemma map_diagDiff_eq_smul (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) {p q : Fin N} (hpq : p ≠ q) :
    L (diagDiff p q) = adjMat N (L (offDiag p q)) p q • diagDiff p q
```

**`suTensor.coeff_offDiag_eq`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L548).

> For distinct `p`, `q` and `r`, the coefficients of the matrix units at `(p, q)` and at
> `(p, r)` agree: the difference of the diagonal units at `p` and `r` is the sum of those at `p`
> and `q` and at `q` and `r`.

```lean
lemma coeff_offDiag_eq (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) {p q r : Fin N} (hpq : p ≠ q) (hpr : p ≠ r)
    (hqr : q ≠ r) : adjMat N (L (offDiag p r)) p r = adjMat N (L (offDiag p q)) p q
```

**`suTensor.exists_coeff_offDiag_eq`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L561).

> All the matrix units off the diagonal have the same coefficient under an endomorphism
> commuting with the adjoint action.

```lean
lemma exists_coeff_offDiag_eq (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) :
    ∃ μ : ℂ, ∀ x y : Fin N, x ≠ y → adjMat N (L (offDiag x y)) x y = μ
```

**`suTensor.eq_sum_offDiag_add_sum_diagDiff`**, a lemma, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L591).

> An element of the complexified Lie algebra is the combination of the entries of its matrix off
> the diagonal against the matrix
> units, and of its diagonal entries against the differences of the diagonal matrix units at a
> fixed coordinate.

```lean
lemma eq_sum_offDiag_add_sum_diagDiff (A : SUAlgebraComplexified N) (x₀ : Fin N) :
    A = ∑ x, ∑ y, adjMat N A x y • offDiag x y + ∑ x, adjMat N A x x • diagDiff x x₀
```

**`suTensor.eq_smul_id_of_commute_adjRep`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean#L626).

> An endomorphism of the complexified Lie algebra commuting with the adjoint action of every
> element of `SU(N)` is scalar: a form of Schur's lemma for the adjoint representation.

```lean
lemma eq_smul_id_of_commute_adjRep (hL : ∀ (g : SU N) (A : SUAlgebraComplexified N),
    L (adjRep N g A) = adjRep N g (L A)) :
    ∃ z : ℂ, L = z • LinearMap.id
```

## Depends on

- [The adjoint representation of `SU(N)`](../part-04/localgaugedata-su-adjoint.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Basic.lean)
