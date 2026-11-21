---
catalog: module
lean: CompPoly.DenseMatrix.containsNat, CompPoly.DenseMatrix.freeColumns, CompPoly.DenseMatrix.pivotRowOfColumn?, CompPoly.DenseMatrix.basisVectorForFreeColumn, CompPoly.DenseMatrix.homogeneousKernelBasis, CompPoly.DenseMatrix.homogeneousWitness
statement: formalized
proof: formalized
---

# Dense Homogeneous Kernels

`CompPoly.LinearAlgebra.Dense.Kernel`, in [CompPoly/LinearAlgebra/Dense/Kernel.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Kernel.lean), by Valerii Huhnin.

> Executable homogeneous-kernel basis and witness extraction from row-reduced
> dense matrices.

`CompPoly.DenseMatrix.containsNat` (definition, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Kernel.lean#L26))

> Boolean membership test for natural-number arrays.

```lean
def containsNat (xs : Array Nat) (x : Nat) : Bool
```

`CompPoly.DenseMatrix.freeColumns` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Kernel.lean#L30))

> Free columns of a row-reduced matrix.

```lean
def freeColumns (cols : Nat) (pivots : Array Nat) : Array Nat
```

`CompPoly.DenseMatrix.pivotRowOfColumn?` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Kernel.lean#L34))

> Pivot row for a pivot column, if the column is a pivot.

```lean
def pivotRowOfColumn? (pivots : Array Nat) (col : Nat) : Option Nat
```

`CompPoly.DenseMatrix.basisVectorForFreeColumn` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Kernel.lean#L38))

> Kernel basis vector corresponding to one free column of an RREF matrix.

```lean
def basisVectorForFreeColumn [Field F] [BEq F] (A : DenseMatrix F)
    (pivots : Array Nat) (free : Nat) : Array F
```

`CompPoly.DenseMatrix.homogeneousKernelBasis` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Kernel.lean#L49))

> Homogeneous kernel basis extracted from the RREF free columns.

```lean
def homogeneousKernelBasis [Field F] [BEq F] (M : DenseMatrix F) :
    Array (Array F)
```

`CompPoly.DenseMatrix.homogeneousWitness` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Kernel.lean#L56))

> One nonzero homogeneous-kernel witness, if a free column exists.

```lean
def homogeneousWitness [Field F] [BEq F] (M : DenseMatrix F) : Option (Array F)
```

## Depends on

- [Dense Row Operations](rowops.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/Kernel.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/Kernel.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.Kernel.json)
