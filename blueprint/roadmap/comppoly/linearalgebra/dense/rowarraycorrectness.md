---
catalog: module
lean: CompPoly.DenseMatrix.array_getD_of_le', CompPoly.DenseMatrix.array_getD_of_lt', CompPoly.DenseMatrix.array_getD_setIfInBounds, CompPoly.DenseMatrix.addScaledScalarRow_getD, CompPoly.DenseMatrix.normalizeScalarRow_getD, CompPoly.DenseMatrix.scalarDot, CompPoly.DenseMatrix.scalarDot_empty, CompPoly.DenseMatrix.scalarDot_addScaledScalarRow, CompPoly.DenseMatrix.scalarDot_eq_pivot_mul_normalize, CompPoly.DenseMatrix.OrthRows, CompPoly.DenseMatrix.swapScalarRows_size, CompPoly.DenseMatrix.swapScalarRows_getD, CompPoly.DenseMatrix.normalizeAndEliminateScalarRows_size, CompPoly.DenseMatrix.orthRows_of_scalarRrefRows, CompPoly.DenseMatrix.normalizeAndEliminateScalarRows_getD_entry, CompPoly.DenseMatrix.ScalarRrefSpec, CompPoly.DenseMatrix.scalarRrefRows_spec, CompPoly.DenseMatrix.freeColumns_mem, CompPoly.DenseMatrix.pivotRowOfColumn?_some, CompPoly.DenseMatrix.basisVectorForFreeColumnRows_size, CompPoly.DenseMatrix.homogeneousKernelBasisRows_size, CompPoly.DenseMatrix.homogeneousKernelBasisRows_dot_eq_zero, CompPoly.DenseMatrix.freeColumns_getD_mem, CompPoly.DenseMatrix.basisVector_getD_freeColumn, CompPoly.DenseMatrix.homogeneousKernelBasisRows_size_eq, CompPoly.DenseMatrix.homogeneousKernelBasisRows_getD_eq, CompPoly.DenseMatrix.homogeneousKernelBasisRows_complete
statement: formalized
proof: formalized
---

# Row-Array Homogeneous-Kernel Correctness

`CompPoly.LinearAlgebra.Dense.RowArrayCorrectness`, in [CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean), by Valerii Huhnin.

> Soundness and completeness of the row-array RREF kernel
> `homogeneousKernelBasisRows`: every emitted vector is orthogonal to the input
> rows, and every orthogonal vector is an `F`-linear combination of the emitted
> basis, with coefficients read off at the free columns.

> ## Row-array kernel soundness
>
> Soundness of the row-array RREF kernel:
> every vector produced by `homogeneousKernelBasisRows rows cols` has size
> `cols` and is orthogonal (over the first `cols` coordinates) to every input
> row.

> ## Generic array access lemmas

`CompPoly.DenseMatrix.array_getD_of_le'` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L49))

> `getD` at an out-of-bounds index returns the default.

```lean
theorem array_getD_of_le' (xs : Array α) (d : α) {i : Nat}
    (h : xs.size ≤ i) : xs.getD i d = d
```

`CompPoly.DenseMatrix.array_getD_of_lt'` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L55))

> `getD` at an in-bounds index returns the indexed element.

```lean
theorem array_getD_of_lt' (xs : Array α) (d : α) {i : Nat}
    (h : i < xs.size) : xs.getD i d = xs[i]
```

`CompPoly.DenseMatrix.array_getD_setIfInBounds` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L61))

> `getD` after `setIfInBounds` in coordinates.

```lean
theorem array_getD_setIfInBounds (xs : Array α) (j : Nat) (a : α)
    (i : Nat) (d : α) :
    (xs.setIfInBounds j a).getD i d =
      if j = i ∧ j < xs.size then a else xs.getD i d
```

> ## Coordinate access helpers

`CompPoly.DenseMatrix.addScaledScalarRow_getD` (theorem, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L98))

> Coordinatewise description of `addScaledScalarRow`.

```lean
theorem addScaledScalarRow_getD [Field F] (target source : Array F)
    (factor : F) (k : Nat) :
    (addScaledScalarRow target source factor).getD k 0 =
      target.getD k 0 + factor * source.getD k 0
```

`CompPoly.DenseMatrix.normalizeScalarRow_getD` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L114))

> Coordinatewise description of `normalizeScalarRow` at a nonzero pivot.

```lean
theorem normalizeScalarRow_getD [Field F] [BEq F] [LawfulBEq F]
    (row : Array F) (pivotCol : Nat) (hpivot : row.getD pivotCol 0 ≠ 0)
    (k : Nat) :
    (normalizeScalarRow row pivotCol).getD k 0 =
      row.getD k 0 / row.getD pivotCol 0
```

> ## Scalar dot products and orthogonality

`CompPoly.DenseMatrix.scalarDot` (definition, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L137))

> Dot product of the first `cols` coordinates of two scalar rows, with
> zero defaults beyond the stored lengths.

```lean
def scalarDot [Field F] (cols : Nat) (r v : Array F) : F
```

`CompPoly.DenseMatrix.scalarDot_empty` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L141))

> The empty row is orthogonal to everything.

```lean
theorem scalarDot_empty [Field F] (cols : Nat) (v : Array F) :
    scalarDot cols (#[] : Array F) v = 0
```

`CompPoly.DenseMatrix.scalarDot_addScaledScalarRow` (theorem, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L148))

> `scalarDot` is additive along `addScaledScalarRow`.

```lean
theorem scalarDot_addScaledScalarRow [Field F] (cols : Nat)
    (target source v : Array F) (factor : F) :
    scalarDot cols (addScaledScalarRow target source factor) v =
      scalarDot cols target v + factor * scalarDot cols source v
```

`CompPoly.DenseMatrix.scalarDot_eq_pivot_mul_normalize` (theorem, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L159))

> A row recovers from its normalization by rescaling with the pivot.

```lean
theorem scalarDot_eq_pivot_mul_normalize [Field F] [BEq F] [LawfulBEq F]
    (cols : Nat) (row v : Array F) (pivotCol : Nat)
    (hpivot : row.getD pivotCol 0 ≠ 0) :
    scalarDot cols row v =
      row.getD pivotCol 0 * scalarDot cols (normalizeScalarRow row pivotCol) v
```

`CompPoly.DenseMatrix.OrthRows` (definition, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L172))

> Orthogonality of `v` to every row of a row-array matrix, expressed via
> total `getD` access so that out-of-range indices are harmless.

```lean
def OrthRows [Field F] (cols : Nat) (rows : Array (Array F)) (v : Array F) :
    Prop
```

> ## Elementary-step characterizations

`CompPoly.DenseMatrix.swapScalarRows_size` (theorem, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L185))

> Swapping rows preserves the row count.

```lean
theorem swapScalarRows_size (rows : Array (Array F)) (a b : Nat) :
    (swapScalarRows rows a b).size = rows.size
```

`CompPoly.DenseMatrix.swapScalarRows_getD` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L190))

> Rows of `swapScalarRows rows a b`: rows `a` and `b` are exchanged.

```lean
theorem swapScalarRows_getD (rows : Array (Array F)) {a b : Nat}
    (ha : a < rows.size) (hb : b < rows.size) (i : Nat) :
    (swapScalarRows rows a b).getD i #[] =
      if i = b then rows.getD a #[]
      else if i = a then rows.getD b #[]
      else rows.getD i #[]
```

> ## Backward span: row operations are invertible

`CompPoly.DenseMatrix.normalizeAndEliminateScalarRows_size` (theorem, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L296))

> Normalizing and eliminating preserves the row count.

```lean
theorem normalizeAndEliminateScalarRows_size [Field F] [BEq F] [LawfulBEq F]
    (rows : Array (Array F)) (pivotRow pivotCol : Nat) :
    (normalizeAndEliminateScalarRows rows pivotRow pivotCol).size = rows.size
```

`CompPoly.DenseMatrix.orthRows_of_scalarRrefRows` (theorem, [line 458](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L458))

> Orthogonality to all rows of the final RREF matrix transfers back to all
> rows of the original matrix: every row operation is invertible.

```lean
theorem orthRows_of_scalarRrefRows [Field F] [BEq F] [LawfulBEq F]
    {cols : Nat} {rows : Array (Array F)} {v : Array F}
    (h : OrthRows cols (scalarRrefRows rows cols).rows v) :
    OrthRows cols rows v
```

> ## Forward RREF shape invariants

`CompPoly.DenseMatrix.normalizeAndEliminateScalarRows_getD_entry` (theorem, [line 558](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L558))

> Entries of `normalizeAndEliminateScalarRows`: the pivot row is divided by
> the pivot, and every other row loses its pivot-column multiple of the normalized
> pivot row.

```lean
theorem normalizeAndEliminateScalarRows_getD_entry [Field F] [BEq F]
    [LawfulBEq F] (rows : Array (Array F)) (pivotRow pivotCol : Nat)
    (hpr : pivotRow < rows.size)
    (hpivot : (rows.getD pivotRow #[]).getD pivotCol 0 ≠ 0) (i k : Nat) :
    ((normalizeAndEliminateScalarRows rows pivotRow pivotCol).getD
        i #[]).getD k 0 =
      if i = pivotRow then
        (rows.getD pivotRow #[]).getD k 0 /
          (rows.getD pivotRow #[]).getD pivotCol 0
      else
        (rows.getD i #[]).getD k 0 -
          (rows.getD i #[]).getD pivotCol 0 *
            ((rows.getD pivotRow #[]).getD k 0 /
              (rows.getD pivotRow #[]).getD pivotCol 0)
```

`CompPoly.DenseMatrix.ScalarRrefSpec` (structure, [line 622](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L622))

> Shape contract satisfied by the result of `scalarRrefRows`: recorded
> pivot columns are strictly increasing and below `cols`, each pivot column is
> a unit column with its one in the corresponding pivot row, and every row at
> or beyond the pivot count vanishes on all columns below `cols`.

```lean
structure ScalarRrefSpec [Field F] (cols : Nat)
    (R : ScalarRrefResult (F := F)) : Prop where
  mono : ∀ s t, s < t → t < R.pivots.size →
    R.pivots.getD s 0 < R.pivots.getD t 0
  pivots_lt : ∀ t, t < R.pivots.size → R.pivots.getD t 0 < cols
  unit : ∀ t, t < R.pivots.size → ∀ i,
    (R.rows.getD i #[]).getD (R.pivots.getD t 0) 0 = if i = t then 1 else 0
  tail_zero : ∀ i, R.pivots.size ≤ i → ∀ k, k < cols →
    (R.rows.getD i #[]).getD k 0 = 0
```

`CompPoly.DenseMatrix.scalarRrefRows_spec` (theorem, [line 783](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L783))

> The row-array RREF driver satisfies the RREF shape contract.

```lean
theorem scalarRrefRows_spec [Field F] [BEq F] [LawfulBEq F]
    (rows : Array (Array F)) (cols : Nat) :
    ScalarRrefSpec cols (scalarRrefRows rows cols)
```

> ## Kernel basis vectors

`CompPoly.DenseMatrix.freeColumns_mem` (theorem, [line 821](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L821))

> A free column is below `cols` and is not a recorded pivot column.

```lean
theorem freeColumns_mem {cols : Nat} {pivots : Array Nat} {free : Nat}
    (h : free ∈ (freeColumns cols pivots).toList) :
    free < cols ∧ ∀ t, t < pivots.size → pivots.getD t 0 ≠ free
```

`CompPoly.DenseMatrix.pivotRowOfColumn?_some` (theorem, [line 833](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L833))

> `pivotRowOfColumn?` returns an in-range index whose recorded pivot is the
> requested column.

```lean
theorem pivotRowOfColumn?_some {pivots : Array Nat} {col t : Nat}
    (h : pivotRowOfColumn? pivots col = some t) :
    t < pivots.size ∧ pivots.getD t 0 = col
```

`CompPoly.DenseMatrix.basisVectorForFreeColumnRows_size` (theorem, [line 870](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L870))

> Each row-array kernel basis vector has `cols` entries.

```lean
theorem basisVectorForFreeColumnRows_size [Field F]
    (rows : Array (Array F)) (pivots : Array Nat) (cols free : Nat) :
    (basisVectorForFreeColumnRows rows pivots cols free).size = cols
```

> ## Main soundness theorems

`CompPoly.DenseMatrix.homogeneousKernelBasisRows_size` (theorem, [line 980](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L980))

> Every vector produced by `homogeneousKernelBasisRows rows cols` has
> exactly `cols` stored coordinates.

```lean
theorem homogeneousKernelBasisRows_size [Field F] [BEq F] [LawfulBEq F]
    {rows : Array (Array F)} {cols : Nat} {v : Array F}
    (hv : v ∈ (homogeneousKernelBasisRows rows cols).toList) :
    v.size = cols
```

`CompPoly.DenseMatrix.homogeneousKernelBasisRows_dot_eq_zero` (theorem, [line 994](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L994))

> **Soundness of the row-array kernel.**  Every vector produced by
> `homogeneousKernelBasisRows rows cols` is orthogonal, over the coordinates
> `0, …, cols - 1`, to every row of the input matrix.  No width hypothesis on
> the input rows is needed because the dot product only inspects the first
> `cols` coordinates (with zero defaults).

```lean
theorem homogeneousKernelBasisRows_dot_eq_zero [Field F] [BEq F] [LawfulBEq F]
    {rows : Array (Array F)} {cols : Nat} {v : Array F}
    (hv : v ∈ (homogeneousKernelBasisRows rows cols).toList)
    {r : Array F} (hr : r ∈ rows.toList) :
    ∑ k ∈ Finset.range cols, r.getD k 0 * v.getD k 0 = 0
```

> ### Forward span: row operations preserve orthogonality

> ### Free-column bookkeeping for the completeness theorem

`CompPoly.DenseMatrix.freeColumns_getD_mem` (theorem, [line 1138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L1138))

> In-range entries of `freeColumns` are members of it.

```lean
theorem freeColumns_getD_mem {cols : Nat} {pivots : Array Nat}
    {i : Nat} (hi : i < (freeColumns cols pivots).size) :
    (freeColumns cols pivots).getD i 0 ∈
      (freeColumns cols pivots).toList
```

`CompPoly.DenseMatrix.basisVector_getD_freeColumn` (theorem, [line 1193](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L1193))

> The basis vector of the `i`-th free column is one at that column and zero at
> every other free column.

```lean
theorem basisVector_getD_freeColumn [Field F]
    (rows : Array (Array F)) (pivots : Array Nat) (cols : Nat) {i j : Nat}
    (hi : i < (freeColumns cols pivots).size)
    (hj : j < (freeColumns cols pivots).size) :
    (basisVectorForFreeColumnRows rows pivots cols
        ((freeColumns cols pivots).getD i 0)).getD
      ((freeColumns cols pivots).getD j 0) 0 =
      if j = i then 1 else 0
```

`CompPoly.DenseMatrix.homogeneousKernelBasisRows_size_eq` (theorem, [line 1310](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L1310))

> The row-array kernel basis has one vector per free column.

```lean
theorem homogeneousKernelBasisRows_size_eq [Field F] [BEq F]
    [LawfulBEq F] (rows : Array (Array F)) (cols : Nat) :
    (homogeneousKernelBasisRows rows cols).size =
      (freeColumns cols (scalarRrefRows rows cols).pivots).size
```

`CompPoly.DenseMatrix.homogeneousKernelBasisRows_getD_eq` (theorem, [line 1318](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L1318))

> The `i`-th row-array kernel basis vector is the basis vector of the `i`-th
> free column.

```lean
theorem homogeneousKernelBasisRows_getD_eq [Field F] [BEq F]
    [LawfulBEq F] (rows : Array (Array F)) (cols : Nat) {i : Nat}
    (hi : i <
      (freeColumns cols (scalarRrefRows rows cols).pivots).size) :
    (homogeneousKernelBasisRows rows cols).getD i #[] =
      basisVectorForFreeColumnRows (scalarRrefRows rows cols).rows
        (scalarRrefRows rows cols).pivots cols
        ((freeColumns cols
          (scalarRrefRows rows cols).pivots).getD i 0)
```

`CompPoly.DenseMatrix.homogeneousKernelBasisRows_complete` (theorem, [line 1336](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean#L1336))

> **Completeness of the row-array kernel.**  Every vector orthogonal to
> all input rows over the coordinates `0, …, cols - 1` is, coordinatewise below
> `cols`, the `F`-linear combination of the emitted kernel basis vectors whose
> coefficients are the values of the vector at the corresponding free
> columns.

```lean
theorem homogeneousKernelBasisRows_complete [Field F] [BEq F] [LawfulBEq F]
    (rows : Array (Array F)) (cols : Nat) {v : Array F}
    (hv : ∀ r ∈ rows.toList,
      ∑ k ∈ Finset.range cols, r.getD k 0 * v.getD k 0 = 0) :
    ∀ k, k < cols →
      v.getD k 0 =
        ∑ i ∈ Finset.range (homogeneousKernelBasisRows rows cols).size,
          v.getD ((freeColumns cols
              (scalarRrefRows rows cols).pivots).getD i 0) 0 *
            ((homogeneousKernelBasisRows rows cols).getD i #[]).getD k 0
```

## Depends on

- [Row-Array Homogeneous Kernels](rowarray.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowArrayCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.RowArrayCorrectness.json)
