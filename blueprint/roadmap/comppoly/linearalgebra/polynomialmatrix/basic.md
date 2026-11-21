---
catalog: module
lean: CompPoly.PolynomialRow, CompPoly.PolynomialMatrix, CompPoly.PolynomialMatrixShape, CompPoly.PolynomialMatrix.RowWidth, CompPoly.PolynomialMatrix.MatrixWidth, CompPoly.PolynomialMatrix.MatrixShape, CompPoly.PolynomialMatrix.MatrixRows, CompPoly.PolynomialMatrix.WellFormed, CompPoly.PolynomialMatrix.rowGet, CompPoly.PolynomialMatrix.zeroRow, CompPoly.PolynomialMatrix.rowAdd, CompPoly.PolynomialMatrix.rowNeg, CompPoly.PolynomialMatrix.rowSub, CompPoly.PolynomialMatrix.rowScalePolynomial, CompPoly.PolynomialMatrix.rowScaleMonomial, CompPoly.PolynomialMatrix.rowSubScaledShift, CompPoly.PolynomialMatrix.replaceRow
statement: formalized
proof: formalized
---

# Polynomial Rows and Matrices

`CompPoly.LinearAlgebra.PolynomialMatrix.Basic`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean), by Valerii Huhnin.

> Minimal row-oriented polynomial-matrix infrastructure for shifted row reduction.

`CompPoly.PolynomialRow` (abbreviation, [line 21](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L21))

> A polynomial row over `F[X]`.

```lean
abbrev PolynomialRow (F : Type*) [Zero F]
```

`CompPoly.PolynomialMatrix` (abbreviation, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L24))

> A polynomial matrix over `F[X]`, stored as an array of rows.

```lean
abbrev PolynomialMatrix (F : Type*) [Zero F]
```

`CompPoly.PolynomialMatrixShape` (structure, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L27))

> Runtime rectangular shape of a polynomial matrix.

```lean
structure PolynomialMatrixShape where
  rows : Nat
  width : Nat
deriving Repr, BEq, DecidableEq
```

`CompPoly.PolynomialMatrix.RowWidth` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L37))

> Width of a row.

```lean
def RowWidth [Zero F] (row : PolynomialRow F) : Nat
```

`CompPoly.PolynomialMatrix.MatrixWidth` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L41))

> Matrix width, using the first row and width `0` for an empty matrix.

```lean
def MatrixWidth [Zero F] (M : PolynomialMatrix F) : Nat
```

`CompPoly.PolynomialMatrix.MatrixShape` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L47))

> Runtime matrix shape.

```lean
def MatrixShape [Zero F] (M : PolynomialMatrix F) : PolynomialMatrixShape
```

`CompPoly.PolynomialMatrix.MatrixRows` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L51))

> Matrix rows as a list, for membership statements.

```lean
def MatrixRows [Zero F] (M : PolynomialMatrix F) : List (PolynomialRow F)
```

`CompPoly.PolynomialMatrix.WellFormed` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L55))

> A matrix is rectangular when every row has the matrix width.

```lean
def WellFormed [Zero F] (M : PolynomialMatrix F) : Prop
```

`CompPoly.PolynomialMatrix.rowGet` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L59))

> Read a row coefficient with zero default.

```lean
def rowGet [Zero F] (row : PolynomialRow F) (j : Nat) : CPolynomial F
```

`CompPoly.PolynomialMatrix.zeroRow` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L63))

> The zero row of a fixed width.

```lean
def zeroRow [Zero F] (width : Nat) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.rowAdd` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L67))

> Pointwise row addition over the maximum input width.

```lean
def rowAdd [Semiring F] [BEq F] [LawfulBEq F]
    (a b : PolynomialRow F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.rowNeg` (definition, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L73))

> Pointwise row negation.

```lean
def rowNeg [Ring F] [BEq F] [LawfulBEq F] (row : PolynomialRow F) :
    PolynomialRow F
```

`CompPoly.PolynomialMatrix.rowSub` (definition, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L78))

> Pointwise row subtraction over the maximum input width.

```lean
def rowSub [Ring F] [BEq F] [LawfulBEq F]
    (a b : PolynomialRow F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.rowScalePolynomial` (definition, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L83))

> Multiply a row by a univariate polynomial.

```lean
def rowScalePolynomial [Semiring F] [BEq F] [LawfulBEq F]
    (c : CPolynomial F) (row : PolynomialRow F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.rowScaleMonomial` (definition, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L88))

> Multiply a row by `c * X^d`.

```lean
def rowScaleMonomial [Semiring F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (c : F) (d : Nat) (row : PolynomialRow F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.rowSubScaledShift` (definition, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L95))

> Fused `a - c * X^d * b` over the maximum input width, entrywise via
> `CPolynomial.subMulMonomial`. One call costs `O(deg + d)` per entry instead of
> the `O(d * deg)` convolution behind `rowSub a (rowScaleMonomial c d b)`.

```lean
def rowSubScaledShift [Ring F] [BEq F] [LawfulBEq F]
    (a : PolynomialRow F) (c : F) (d : Nat) (b : PolynomialRow F) :
    PolynomialRow F
```

`CompPoly.PolynomialMatrix.replaceRow` (definition, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean#L102))

> Replace a row if the index is in bounds.

```lean
def replaceRow [Zero F] (M : PolynomialMatrix F) (idx : Nat) (row : PolynomialRow F) :
    PolynomialMatrix F
```

## Depends on

- [Computable Univariate Polynomials](../../univariate/part-01/basic.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Basic.json)
