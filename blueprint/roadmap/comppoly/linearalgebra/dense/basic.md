---
catalog: module
lean: CompPoly.DenseMatrix.setD, CompPoly.DenseMatrix, CompPoly.DenseMatrix.WellFormed, CompPoly.DenseMatrix.index, CompPoly.DenseMatrix.get, CompPoly.DenseMatrix.set, CompPoly.DenseMatrix.ofFn, CompPoly.DenseMatrix.dotRow, CompPoly.DenseMatrix.mulVec, CompPoly.DenseMatrix.VectorWidth, CompPoly.DenseMatrix.NonzeroVector, CompPoly.DenseMatrix.IsHomogeneousSolution
statement: formalized
proof: formalized
---

# Dense Row-Major Matrices

`CompPoly.LinearAlgebra.Dense.Basic`, in [CompPoly/LinearAlgebra/Dense/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean), by Valerii Huhnin.

> Basic dense row-major matrix storage, indexing, and homogeneous-system
> predicates.

`CompPoly.DenseMatrix.setD` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L24))

> Set an array entry when the index is in bounds; otherwise leave the array unchanged.

```lean
def setD (xs : Array alpha) (i : Nat) (a : alpha) : Array alpha
```

`CompPoly.DenseMatrix` (structure, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L30))

> A dense row-major matrix with dimensions stored explicitly.

```lean
structure DenseMatrix (F : Type*) [Zero F] where
  rows : Nat
  cols : Nat
  data : Array F
```

`CompPoly.DenseMatrix.WellFormed` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L40))

> A dense matrix stores exactly one row-major entry for every matrix coordinate.

```lean
def WellFormed [Zero F] (M : DenseMatrix F) : Prop
```

`CompPoly.DenseMatrix.index` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L44))

> Row-major index for the matrix entry `(row, col)`.

```lean
def index [Zero F] (M : DenseMatrix F) (row col : Nat) : Nat
```

`CompPoly.DenseMatrix.get` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L48))

> Read a matrix entry, returning zero outside the stored data.

```lean
def get [Zero F] (M : DenseMatrix F) (row col : Nat) : F
```

`CompPoly.DenseMatrix.set` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L52))

> Replace a matrix entry when the row-major slot is stored.

```lean
def set [Zero F] (M : DenseMatrix F) (row col : Nat) (value : F) : DenseMatrix F
```

`CompPoly.DenseMatrix.ofFn` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L56))

> Construct a dense matrix from an entry function.

```lean
def ofFn [Zero F] (rows cols : Nat) (f : Nat -> Nat -> F) : DenseMatrix F
```

`CompPoly.DenseMatrix.dotRow` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L63))

> Dot product of one matrix row with a vector.

```lean
def dotRow [Semiring F] (M : DenseMatrix F) (row : Nat) (v : Array F) : F
```

`CompPoly.DenseMatrix.mulVec` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L69))

> Matrix-vector product.

```lean
def mulVec [Semiring F] (M : DenseMatrix F) (v : Array F) : Array F
```

`CompPoly.DenseMatrix.VectorWidth` (definition, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L73))

> A vector has the same width as the matrix column count.

```lean
def VectorWidth [Zero F] (M : DenseMatrix F) (v : Array F) : Prop
```

`CompPoly.DenseMatrix.NonzeroVector` (definition, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L77))

> A vector has at least one nonzero entry.

```lean
def NonzeroVector [Zero F] (v : Array F) : Prop
```

`CompPoly.DenseMatrix.IsHomogeneousSolution` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean#L81))

> A vector solves the homogeneous system represented by `M`.

```lean
def IsHomogeneousSolution [Semiring F] (M : DenseMatrix F) (v : Array F) : Prop
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/LinearAlgebra/Dense/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Basic.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.Basic.json)
