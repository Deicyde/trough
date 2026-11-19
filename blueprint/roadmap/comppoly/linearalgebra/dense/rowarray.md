---
catalog: module
lean: CompPoly.DenseMatrix.toRows, CompPoly.DenseMatrix.swapScalarRows, CompPoly.DenseMatrix.findScalarPivotRow, CompPoly.DenseMatrix.normalizeScalarRow, CompPoly.DenseMatrix.addScaledScalarRow, CompPoly.DenseMatrix.normalizeAndEliminateScalarRows, CompPoly.DenseMatrix.ScalarRrefResult, CompPoly.DenseMatrix.scalarRrefRowsLoop, CompPoly.DenseMatrix.scalarRrefRows, CompPoly.DenseMatrix.basisVectorForFreeColumnRows, CompPoly.DenseMatrix.homogeneousKernelBasisRows
statement: formalized
proof: formalized
---

# Row-Array Homogeneous Kernels

`CompPoly.LinearAlgebra.Dense.RowArray`, in [CompPoly/LinearAlgebra/Dense/RowArray.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean), by Valerii Huhnin.

> Gauss-Jordan reduction and homogeneous-kernel extraction for a matrix stored as
> an array of rows, `Array (Array F)`, with the column count passed separately.
> Rows may be ragged; missing entries read as zero.
>
> The algorithm performs the same pivot search, swap, normalization, and
> elimination as `DenseMatrix.rref`, and the kernel basis is read off the free
> columns exactly as in `DenseMatrix.homogeneousKernelBasis`.
> Correctness is in `CompPoly.LinearAlgebra.Dense.RowArrayCorrectness`.

`CompPoly.DenseMatrix.toRows` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L32))

> The rows of a dense matrix as a row array, each of width `M.cols`.

```lean
def toRows [Zero F] (M : DenseMatrix F) : Array (Array F)
```

`CompPoly.DenseMatrix.swapScalarRows` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L38))

> Swap two scalar rows in a row-array matrix.

```lean
def swapScalarRows (rows : Array (Array F)) (rowA rowB : Nat) :
    Array (Array F)
```

`CompPoly.DenseMatrix.findScalarPivotRow` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L45))

> Find a nonzero pivot row at or below `startRow` in column `col`.

```lean
def findScalarPivotRow (rows : Array (Array F)) (startRow col : Nat) :
    Option Nat
```

`CompPoly.DenseMatrix.normalizeScalarRow` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L51))

> Scale a scalar row so that column `pivotCol` becomes one.

```lean
def normalizeScalarRow (row : Array F) (pivotCol : Nat) : Array F
```

`CompPoly.DenseMatrix.addScaledScalarRow` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L59))

> Add `factor * source` to `target`, using zero defaults for ragged rows.

```lean
def addScaledScalarRow (target source : Array F) (factor : F) : Array F
```

`CompPoly.DenseMatrix.normalizeAndEliminateScalarRows` (definition, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L64))

> Normalize one pivot row and clear the pivot column in all other rows.

```lean
def normalizeAndEliminateScalarRows (rows : Array (Array F))
    (pivotRow pivotCol : Nat) : Array (Array F)
```

`CompPoly.DenseMatrix.ScalarRrefResult` (structure, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L86))

> RREF result for a scalar row-array matrix.

```lean
structure ScalarRrefResult where
  rows : Array (Array F)
  pivots : Array Nat
```

`CompPoly.DenseMatrix.scalarRrefRowsLoop` (definition, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L91))

> Fuel-bounded row-array RREF for tiny scalar coefficient matrices.

```lean
def scalarRrefRowsLoop (cols : Nat) :
    Nat → Nat → Nat → Array (Array F) → Array Nat → ScalarRrefResult (F := F)
```

`CompPoly.DenseMatrix.scalarRrefRows` (definition, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L107))

> Row-array RREF for tiny scalar coefficient matrices.

```lean
def scalarRrefRows (rows : Array (Array F)) (cols : Nat) :
    ScalarRrefResult (F := F)
```

`CompPoly.DenseMatrix.basisVectorForFreeColumnRows` (definition, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L112))

> Kernel basis vector for one free column of a row-array RREF matrix.

```lean
def basisVectorForFreeColumnRows (rows : Array (Array F))
    (pivots : Array Nat) (cols free : Nat) : Array F
```

`CompPoly.DenseMatrix.homogeneousKernelBasisRows` (definition, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean#L123))

> Homogeneous scalar-kernel basis for a row-array matrix.

```lean
def homogeneousKernelBasisRows (rows : Array (Array F)) (cols : Nat) :
    Array (Array F)
```

## Depends on

- [Dense Homogeneous Kernels](kernel.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/RowArray.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/RowArray.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.RowArray.json)
