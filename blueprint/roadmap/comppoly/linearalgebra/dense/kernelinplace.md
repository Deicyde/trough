---
catalog: module
lean: CompPoly.DenseMatrix.swapRowsData, CompPoly.DenseMatrix.scaleRowData, CompPoly.DenseMatrix.addScaledRowData, CompPoly.DenseMatrix.findPivotRowData, CompPoly.DenseMatrix.normalizeAndEliminateData, CompPoly.DenseMatrix.rrefLoopData, CompPoly.DenseMatrix.rrefInPlace, CompPoly.DenseMatrix.homogeneousKernelBasisInPlace, CompPoly.DenseMatrix.homogeneousWitnessInPlace
statement: formalized
proof: formalized
---

# In-Place Dense Homogeneous Kernels

`CompPoly.LinearAlgebra.Dense.KernelInPlace`, in [CompPoly/LinearAlgebra/Dense/KernelInPlace.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean), by Valerii Huhnin.

> A memory-efficient executable variant of the dense Gauss-Jordan homogeneous-kernel
> backend.
>
> The functions in `RowOps.lean` and `Kernel.lean` thread a whole `DenseMatrix`
> structure through every row operation. Because `scaleRow`/`addScaledRow`/`swapRows`
> read the matrix through `M.get` while the structure `M` is still live, the backing
> `Array` is multiply-referenced at the first `setD`, so `Array.setIfInBounds` copies
> the entire array on every row-operation call. Gauss-Jordan elimination performs
> `Θ(rows)` row operations per pivot and `Θ(min rows cols)` pivots, so the copies turn
> an `O(n³)` algorithm into `O(n⁴)` work plus `Θ(n⁴)` words of short-lived allocation.
>
> This module performs the same arithmetic, in the same order, threading a bare
> `Array F` (with the dimensions carried as separate `Nat` arguments) through the
> reduction. The array is uniquely referenced as it flows from one operation to the
> next, so `setIfInBounds` mutates in place after at most one fork from a shared input.
> The reduced matrix and pivot data are bit-for-bit identical to `rref`, so the
> extracted witnesses agree with `homogeneousWitness`.
>
> The free-column witness extraction (`freeColumns`, `basisVectorForFreeColumn`) is
> cheap and shared verbatim with `Kernel.lean`.

`CompPoly.DenseMatrix.swapRowsData` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L44))

> Swap rows `rowA` and `rowB` of a width-`cols` row-major array, in place.

```lean
def swapRowsData [Zero F] (cols rowA rowB : Nat) (data : Array F) : Array F
```

`CompPoly.DenseMatrix.scaleRowData` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L60))

> Scale row `row` of a width-`cols` row-major array by `factor`, in place.

```lean
def scaleRowData [Field F] (cols row : Nat) (factor : F) (data : Array F) :
    Array F
```

`CompPoly.DenseMatrix.addScaledRowData` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L71))

> Add `factor` times row `source` to row `target` (with `target ≠ source`), in
> place.

```lean
def addScaledRowData [Field F] (cols target source : Nat) (factor : F)
    (data : Array F) : Array F
```

`CompPoly.DenseMatrix.findPivotRowData` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L82))

> Find a pivot row at or below `startRow` in column `col`.

```lean
def findPivotRowData [Zero F] [BEq F] (rows cols startRow col : Nat)
    (data : Array F) : Option Nat
```

`CompPoly.DenseMatrix.normalizeAndEliminateData` (definition, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L93))

> Normalize the pivot row and clear the pivot column in every other row, in
> place.

```lean
def normalizeAndEliminateData [Field F] [BEq F] (rows cols pivotRow pivotCol : Nat)
    (data : Array F) : Array F
```

`CompPoly.DenseMatrix.rrefLoopData` (definition, [line 108](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L108))

> Fuel-bounded Gauss-Jordan reduction over a bare row-major array.

```lean
def rrefLoopData [Field F] [BEq F] :
    Nat → Nat → Nat → Nat → Nat → Array F → Array Nat → Array F × Array Nat
```

`CompPoly.DenseMatrix.rrefInPlace` (definition, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L127))

> Reduced row-echelon form with pivot-column metadata, computed in place.
>
> This destructures `M` so the backing array is owned by the reduction loop rather
> than aliased through the structure, which is what lets `setIfInBounds` mutate in
> place. The result equals `rref M`.

```lean
def rrefInPlace [Field F] [BEq F] (M : DenseMatrix F) : RrefResult F
```

`CompPoly.DenseMatrix.homogeneousKernelBasisInPlace` (definition, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L134))

> Homogeneous kernel basis extracted from the in-place RREF free columns.

```lean
def homogeneousKernelBasisInPlace [Field F] [BEq F] (M : DenseMatrix F) :
    Array (Array F)
```

`CompPoly.DenseMatrix.homogeneousWitnessInPlace` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean#L142))

> One nonzero homogeneous-kernel witness via in-place reduction, if a free
> column exists. Output-identical to `homogeneousWitness`.

```lean
def homogeneousWitnessInPlace [Field F] [BEq F] (M : DenseMatrix F) :
    Option (Array F)
```

## Depends on

- [Dense Homogeneous Kernels](kernel.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/KernelInPlace.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/KernelInPlace.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.KernelInPlace.json)
