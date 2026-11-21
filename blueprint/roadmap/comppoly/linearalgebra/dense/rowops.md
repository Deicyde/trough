---
catalog: module
lean: CompPoly.DenseMatrix.RrefResult, CompPoly.DenseMatrix.swapRows, CompPoly.DenseMatrix.scaleRow, CompPoly.DenseMatrix.addScaledRow, CompPoly.DenseMatrix.findPivotRow, CompPoly.DenseMatrix.normalizeAndEliminate, CompPoly.DenseMatrix.rrefLoop, CompPoly.DenseMatrix.rref
statement: formalized
proof: formalized
---

# Dense Row Operations

`CompPoly.LinearAlgebra.Dense.RowOps`, in [CompPoly/LinearAlgebra/Dense/RowOps.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean), by Valerii Huhnin.

> Executable row operations and Gauss-Jordan reduction for row-major matrices.

`CompPoly.DenseMatrix.RrefResult` (structure, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean#L25))

> Result of row reduction, retaining pivot columns in row order.

```lean
structure RrefResult (F : Type*) [Zero F] where
  matrix : DenseMatrix F
  pivots : Array Nat
```

`CompPoly.DenseMatrix.swapRows` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean#L30))

> Swap two rows.

```lean
def swapRows [Zero F] (M : DenseMatrix F) (rowA rowB : Nat) : DenseMatrix F
```

`CompPoly.DenseMatrix.scaleRow` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean#L44))

> Scale one row by a field element.

```lean
def scaleRow [Field F] (M : DenseMatrix F) (row : Nat) (factor : F) :
    DenseMatrix F
```

`CompPoly.DenseMatrix.addScaledRow` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean#L53))

> Add `factor` times `source` row to `target` row.

```lean
def addScaledRow [Field F] (M : DenseMatrix F) (target source : Nat)
    (factor : F) : DenseMatrix F
```

`CompPoly.DenseMatrix.findPivotRow` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean#L63))

> Find a pivot row at or below `startRow` in column `col`.

```lean
def findPivotRow [Zero F] [BEq F] (M : DenseMatrix F)
    (startRow col : Nat) : Option Nat
```

`CompPoly.DenseMatrix.normalizeAndEliminate` (definition, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean#L73))

> Normalize the pivot row and clear the pivot column in every other row.

```lean
def normalizeAndEliminate [Field F] [BEq F] (M : DenseMatrix F)
    (pivotRow pivotCol : Nat) : DenseMatrix F
```

`CompPoly.DenseMatrix.rrefLoop` (definition, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean#L88))

> Fuel-bounded Gauss-Jordan reduction.

```lean
def rrefLoop [Field F] [BEq F] :
    Nat -> Nat -> Nat -> DenseMatrix F -> Array Nat -> RrefResult F
```

`CompPoly.DenseMatrix.rref` (definition, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean#L103))

> Reduced row-echelon form with pivot-column metadata.

```lean
def rref [Field F] [BEq F] (M : DenseMatrix F) : RrefResult F
```

## Depends on

- [Dense Row-Major Matrices](basic.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/RowOps.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOps.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.RowOps.json)
