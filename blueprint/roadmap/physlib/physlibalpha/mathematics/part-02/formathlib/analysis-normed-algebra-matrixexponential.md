---
declaration: module
origin: cited
lean: Matrix.exp_fromBlocks_zero, Matrix.exp_kronecker_one_add_one_kronecker, Matrix.exp_add_smul_one, Matrix.exp_scalar
statement: formalized
proof: formalized
---

# Exponentials of block-diagonal, Kronecker and scalar matrices

The module `PhyslibAlpha.Mathematics.ForMathlib.Analysis.Normed.Algebra.MatrixExponential`, [PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixExponential.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixExponential.lean): 4 declarations, 4 with a docstring.

> The matrix exponential of a block-diagonal matrix, of a Kronecker sum and of a scalar shift.

## i. Overview

> The exponential of complex matrices commutes with the continuous ring homomorphisms built
> from block-diagonal matrices and Kronecker products. So `exp (diag(A, B))` is
> `diag(exp A, exp B)`, and `exp (A ⊗ 1 + 1 ⊗ B)` is `exp A ⊗ exp B`. The two terms of the
> Kronecker sum commute. A scalar shift `A + z 1` multiplies the exponential by `exp z`.

## ii. Key results

> - `Matrix.exp_fromBlocks_zero` : `exp (diag(A, B)) = diag(exp A, exp B)`.
> - `Matrix.exp_kronecker_one_add_one_kronecker` : `exp (A ⊗ 1 + 1 ⊗ B) = exp A ⊗ exp B`.
> - `Matrix.exp_add_smul_one` : `exp (A + z 1) = exp z • exp A`.
> - `Matrix.exp_scalar` : the exponential of a scalar matrix.

## iv. References

> * None.

## A. Block-diagonal matrices

**`Matrix.exp_fromBlocks_zero`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixExponential.lean#L61).

> The exponential of a block-diagonal matrix is block-diagonal,
> `exp (diag(A, B)) = diag(exp A, exp B)`.

```lean
lemma exp_fromBlocks_zero (A : Matrix m m ℂ) (B : Matrix n n ℂ) :
    exp (fromBlocks A 0 0 B) = fromBlocks (exp A) 0 0 (exp B)
```

## B. Kronecker products

**`Matrix.exp_kronecker_one_add_one_kronecker`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixExponential.lean#L86).

> The exponential of the Kronecker sum is the Kronecker product of the exponentials,
> `exp (A ⊗ 1 + 1 ⊗ B) = exp A ⊗ exp B`.

```lean
lemma exp_kronecker_one_add_one_kronecker (A : Matrix m m ℂ) (B : Matrix n n ℂ) :
    exp (A ⊗ₖ (1 : Matrix n n ℂ) + (1 : Matrix m m ℂ) ⊗ₖ B) = exp A ⊗ₖ exp B
```

## C. Scalar matrices

**`Matrix.exp_add_smul_one`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixExponential.lean#L124).

> Adding a scalar matrix multiplies the exponential by the exponential of the scalar.

```lean
lemma exp_add_smul_one (A : Matrix m m ℂ) (z : ℂ) :
    exp (A + z • (1 : Matrix m m ℂ)) = Complex.exp z • exp A
```

**`Matrix.exp_scalar`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixExponential.lean#L133).

> The exponential of a scalar matrix is the scalar matrix of the exponential.

```lean
lemma exp_scalar (z : ℂ) : exp (scalar m z) = scalar m (Complex.exp z)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixExponential.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/MatrixExponential.lean)
