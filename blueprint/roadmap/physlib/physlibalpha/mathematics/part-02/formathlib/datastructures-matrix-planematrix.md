---
declaration: module
origin: cited
lean: Matrix.planeInclusion, Matrix.planeInclusion_apply, Matrix.planeInclusion_transpose_mul, Matrix.conjTranspose_planeInclusion, Matrix.planeMatrix, Matrix.planeMatrix_one, Matrix.planeMatrix_mul, Matrix.conjTranspose_planeMatrix
statement: formalized
proof: formalized
---

# Matrices acting in a coordinate plane

The module `PhyslibAlpha.Mathematics.ForMathlib.DataStructures.Matrix.PlaneMatrix`, [PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean): 17 declarations, 16 with a docstring.

> The matrices which act on the plane spanned by two coordinates and fix every other coordinate.

## i. Overview

> For two coordinates `p` and `q` of `Fin N`, the plane they span is included in `ℂ^N` by the
> `N × 2` matrix `planeInclusion p q`, whose columns are the two basis vectors. A `2 × 2` matrix `U`
> then acts on the plane and trivially on the other coordinates by the matrix
> `planeMatrix p q U = 1 + P (U - 1) Pᵀ`, with `P` the inclusion. These matrices multiply, conjugate
> and take determinants as the `2 × 2` matrices do (A), and conjugating a matrix supported on the
> plane, or restricting a conjugated matrix to the plane, is computed on the plane (B).
>
> These are the matrix facts behind embedding `SU(2)` in `SU(N)` one coordinate plane at a time.

## ii. Key results

> - `Matrix.planeInclusion` : the inclusion of the plane of two coordinates.
> - `Matrix.planeMatrix` : the matrix acting as a given `2 × 2` matrix on the plane and trivially
>   elsewhere.
> - `Matrix.planeMatrix_mul` : plane matrices multiply as the matrices on the plane.
> - `Matrix.det_planeMatrix` : a plane matrix has the determinant of the matrix on the plane.
> - `Matrix.planeMatrix_conj` : conjugation by a plane matrix of a matrix supported on the plane.

## iv. References

> * None.

## A. The plane matrices

**`Matrix.planeInclusion`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L62).

> The inclusion of the plane of the coordinates `p` and `q`, the `N × 2` matrix whose columns
> are the basis vectors `e_p` and `e_q`.

```lean
def planeInclusion (p q : Fin N) : Matrix (Fin N) (Fin 2) ℂ
```

**`Matrix.planeInclusion_apply`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L66).

```lean
lemma planeInclusion_apply (p q : Fin N) (x : Fin N) (i : Fin 2) :
    planeInclusion p q x i = if x = ![p, q] i then 1 else 0
```

**`Matrix.planeInclusion_transpose_mul`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L70).

> The inclusion of the plane of two distinct coordinates is an isometry.

```lean
lemma planeInclusion_transpose_mul {p q : Fin N} (hpq : p ≠ q) :
    (planeInclusion p q)ᵀ * planeInclusion p q = 1
```

**`Matrix.conjTranspose_planeInclusion`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L78).

> The inclusion of the plane has real entries, so its conjugate transpose is its transpose.

```lean
lemma conjTranspose_planeInclusion (p q : Fin N) :
    (planeInclusion p q)ᴴ = (planeInclusion p q)ᵀ
```

**`Matrix.planeMatrix`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L86).

> The matrix acting as `U` on the plane of the coordinates `p` and `q` and as the identity on
> the other coordinates.

```lean
def planeMatrix (p q : Fin N) (U : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin N) (Fin N) ℂ
```

**`Matrix.planeMatrix_one`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L93).

> The plane matrix of the identity is the identity.

```lean
lemma planeMatrix_one : planeMatrix p q 1 = 1
```

**`Matrix.planeMatrix_mul`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L97).

> The plane matrices multiply as the matrices on the plane.

```lean
lemma planeMatrix_mul (hpq : p ≠ q) (U V : Matrix (Fin 2) (Fin 2) ℂ) :
    planeMatrix p q U * planeMatrix p q V = planeMatrix p q (U * V)
```

**`Matrix.conjTranspose_planeMatrix`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L112).

> The conjugate transpose of a plane matrix is the plane matrix of the conjugate
> transpose.

```lean
lemma conjTranspose_planeMatrix (U : Matrix (Fin 2) (Fin 2) ℂ) :
    (planeMatrix p q U)ᴴ = planeMatrix p q Uᴴ
```

**`Matrix.det_planeMatrix`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L123).

> A plane matrix has the determinant of the matrix on the plane.

```lean
lemma det_planeMatrix (hpq : p ≠ q) (U : Matrix (Fin 2) (Fin 2) ℂ) :
    (planeMatrix p q U).det = U.det
```

**`Matrix.planeMatrix_mul_planeInclusion`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L129).

> A plane matrix moves the plane as the matrix on the plane does.

```lean
lemma planeMatrix_mul_planeInclusion (hpq : p ≠ q) (U : Matrix (Fin 2) (Fin 2) ℂ) :
    planeMatrix p q U * planeInclusion p q = planeInclusion p q * U
```

**`Matrix.transpose_planeInclusion_mul_planeMatrix`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L137).

> The transpose of the inclusion of the plane intertwines a plane matrix with the matrix on
> the plane.

```lean
lemma transpose_planeInclusion_mul_planeMatrix (hpq : p ≠ q) (U : Matrix (Fin 2) (Fin 2) ℂ) :
    (planeInclusion p q)ᵀ * planeMatrix p q U = U * (planeInclusion p q)ᵀ
```

## B. Conjugation, blocks and diagonal matrices

**`Matrix.planeMatrix_conj`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L150).

> Conjugating a matrix supported on the plane by a plane matrix conjugates it on the plane.

```lean
lemma planeMatrix_conj (hpq : p ≠ q) (U M : Matrix (Fin 2) (Fin 2) ℂ) :
    planeMatrix p q U * (planeInclusion p q * M * (planeInclusion p q)ᵀ) * (planeMatrix p q U)ᴴ
      = planeInclusion p q * (U * M * Uᴴ) * (planeInclusion p q)ᵀ
```

**`Matrix.planeBlock_conj`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L160).

> The block on the plane of a matrix conjugated by a plane matrix is the conjugate of its
> block.

```lean
lemma planeBlock_conj (hpq : p ≠ q) (U : Matrix (Fin 2) (Fin 2) ℂ) (C : Matrix (Fin N) (Fin N) ℂ) :
    (planeInclusion p q)ᵀ * (planeMatrix p q U * C * (planeMatrix p q U)ᴴ) * planeInclusion p q
      = U * ((planeInclusion p q)ᵀ * C * planeInclusion p q) * Uᴴ
```

**`Matrix.planeBlock_apply`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L172).

> The entries of the block on the plane are the entries of the matrix at the two
> coordinates.

```lean
lemma planeBlock_apply (C : Matrix (Fin N) (Fin N) ℂ) (i j : Fin 2) :
    ((planeInclusion p q)ᵀ * C * planeInclusion p q) i j = C (![p, q] i) (![p, q] j)
```

**`Matrix.planeMatrix_diagonal`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L177).

> A plane matrix of a diagonal matrix is diagonal.

```lean
lemma planeMatrix_diagonal (hpq : p ≠ q) (a b : ℂ) :
    planeMatrix p q (diagonal ![a, b])
      = diagonal fun x => if x = p then a else if x = q then b else 1
```

**`Matrix.planeBlock_eq_of_conj_eq`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L189).

> A matrix fixed by conjugation by a plane matrix has its block on the plane fixed by
> conjugation by the matrix on the plane.

```lean
lemma planeBlock_eq_of_conj_eq (hpq : p ≠ q) {U : Matrix (Fin 2) (Fin 2) ℂ}
    {C : Matrix (Fin N) (Fin N) ℂ} (hC : planeMatrix p q U * C * (planeMatrix p q U)ᴴ = C) :
    U * ((planeInclusion p q)ᵀ * C * planeInclusion p q) * Uᴴ
      = (planeInclusion p q)ᵀ * C * planeInclusion p q
```

**`Matrix.planeInclusion_single`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean#L197).

> The inclusion of the plane carries the matrix units of the plane to those of the
> coordinates.

```lean
lemma planeInclusion_single (p q : Fin N) (i j : Fin 2) :
    planeInclusion p q * single i j (1 : ℂ) * (planeInclusion p q)ᵀ
      = single (![p, q] i) (![p, q] j) 1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/DataStructures/Matrix/PlaneMatrix.lean)
