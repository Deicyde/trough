---
catalog: module
lean: CompPoly.DenseMatrix.toRows_size, CompPoly.DenseMatrix.toRows_getD, CompPoly.DenseMatrix.normalizeAndEliminate_get, CompPoly.DenseMatrix.rref_pivots_eq_scalarRrefRows, CompPoly.DenseMatrix.homogeneousKernelBasis_eq_homogeneousKernelBasisRows, CompPoly.DenseMatrix.dotRow_eq_sum, CompPoly.DenseMatrix.homogeneousKernelBasis_width, CompPoly.DenseMatrix.homogeneousKernelBasis_isHomogeneousSolution, CompPoly.DenseMatrix.homogeneousKernelBasis_complete, CompPoly.DenseMatrix.homogeneousKernelBasis_size, CompPoly.DenseMatrix.freeColumns_size_add_pivots_size, CompPoly.DenseMatrix.homogeneousKernelBasis_size_add_rank, CompPoly.DenseMatrix.homogeneousKernelBasis_getD_freeColumn, CompPoly.DenseMatrix.homogeneousKernelBasis_linearIndependent
statement: formalized
proof: formalized
---

# Dense Homogeneous-Kernel Basis Correctness

`CompPoly.LinearAlgebra.Dense.KernelBasisCorrectness`, in [CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean), by Quang Dao.

> `homogeneousKernelBasis M` coincides with the row-array kernel
> `homogeneousKernelBasisRows (toRows M) M.cols` for every well-formed `M`: the
> two Gauss-Jordan loops make the same pivot choices and produce the same reduced
> entries. The row-array soundness and completeness theorems therefore transfer to
> the dense kernel.

> ## Row representation

`CompPoly.DenseMatrix.toRows_size` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L37))

> The number of rows of `toRows M`.

```lean
theorem toRows_size [Zero F] (M : DenseMatrix F) : M.toRows.size = M.rows
```

`CompPoly.DenseMatrix.toRows_getD` (theorem, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L41))

> Entries of `toRows M` below the matrix dimensions are the entries of `M`.

```lean
theorem toRows_getD [Zero F] (M : DenseMatrix F) {i j : Nat} (hi : i < M.rows)
    (hj : j < M.cols) : (M.toRows.getD i #[]).getD j 0 = M.get i j
```

> ## Pivot search

> ## Row operations

`CompPoly.DenseMatrix.normalizeAndEliminate_get` (theorem, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L169))

> Entries of `normalizeAndEliminate` below the matrix dimensions: the pivot row
> is divided by the pivot, and every other row loses its pivot-column multiple of
> the normalized pivot row.

```lean
theorem normalizeAndEliminate_get [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {pivotRow pivotCol row k : Nat}
    (hpr : pivotRow < M.rows) (hpc : pivotCol < M.cols)
    (hpivot : M.get pivotRow pivotCol ≠ 0) (hrow : row < M.rows) (hk : k < M.cols) :
    (normalizeAndEliminate M pivotRow pivotCol).get row k =
      if row = pivotRow then
        M.get pivotRow k / M.get pivotRow pivotCol
      else
        M.get row k -
          M.get row pivotCol * (M.get pivotRow k / M.get pivotRow pivotCol)
```

> ## Gauss-Jordan loop

`CompPoly.DenseMatrix.rref_pivots_eq_scalarRrefRows` (theorem, [line 279](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L279))

> For a well-formed matrix, `rref` records the same pivot columns as the
> row-array reduction of its rows.

```lean
theorem rref_pivots_eq_scalarRrefRows [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) :
    (rref M).pivots = (scalarRrefRows M.toRows M.cols).pivots
```

> ## The two kernel bases agree

`CompPoly.DenseMatrix.homogeneousKernelBasis_eq_homogeneousKernelBasisRows` (theorem, [line 288](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L288))

> The dense homogeneous-kernel basis equals the row-array kernel basis of the
> matrix rows.

```lean
theorem homogeneousKernelBasis_eq_homogeneousKernelBasisRows [Field F] [BEq F]
    [LawfulBEq F] {M : DenseMatrix F} (hM : WellFormed M) :
    homogeneousKernelBasis M = homogeneousKernelBasisRows M.toRows M.cols
```

> ## Soundness, completeness, and independence

`CompPoly.DenseMatrix.dotRow_eq_sum` (theorem, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L322))

> `dotRow` is the finite sum of products over the columns.

```lean
theorem dotRow_eq_sum [Semiring F] (M : DenseMatrix F) (row : Nat) (v : Array F) :
    dotRow M row v = ∑ k ∈ Finset.range M.cols, M.get row k * v.getD k 0
```

`CompPoly.DenseMatrix.homogeneousKernelBasis_width` (theorem, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L343))

> Every vector of the dense homogeneous-kernel basis has the matrix column width.

```lean
theorem homogeneousKernelBasis_width [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {v : Array F}
    (hv : v ∈ (homogeneousKernelBasis M).toList) : VectorWidth M v
```

`CompPoly.DenseMatrix.homogeneousKernelBasis_isHomogeneousSolution` (theorem, [line 351](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L351))

> **Soundness of the dense kernel basis.** Every emitted vector solves the
> homogeneous system.

```lean
theorem homogeneousKernelBasis_isHomogeneousSolution [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {v : Array F}
    (hv : v ∈ (homogeneousKernelBasis M).toList) : IsHomogeneousSolution M v
```

`CompPoly.DenseMatrix.homogeneousKernelBasis_complete` (theorem, [line 365](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L365))

> **Completeness of the dense kernel basis.** Every homogeneous solution is,
> below the column count, the linear combination of the basis vectors whose
> coefficients are its entries at the free columns of `rref M`.

```lean
theorem homogeneousKernelBasis_complete [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {v : Array F}
    (hv : IsHomogeneousSolution M v) :
    ∀ k, k < M.cols →
      v.getD k 0 =
        ∑ i ∈ Finset.range (homogeneousKernelBasis M).size,
          v.getD ((freeColumns M.cols (rref M).pivots).getD i 0) 0 *
            ((homogeneousKernelBasis M).getD i #[]).getD k 0
```

`CompPoly.DenseMatrix.homogeneousKernelBasis_size` (theorem, [line 381](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L381))

> The number of dense kernel basis vectors is the number of free columns.

```lean
theorem homogeneousKernelBasis_size [Field F] [BEq F] (M : DenseMatrix F) :
    (homogeneousKernelBasis M).size = (freeColumns M.cols (rref M).pivots).size
```

`CompPoly.DenseMatrix.freeColumns_size_add_pivots_size` (theorem, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L398))

> Strictly increasing pivot columns below `cols` and the free columns partition
> the columns `0, …, cols - 1`.

```lean
theorem freeColumns_size_add_pivots_size {cols : Nat} {pivots : Array Nat}
    (hstrict : PivotColumnsStrict pivots)
    (hlt : ∀ i, i < pivots.size → pivots.getD i 0 < cols) :
    (freeColumns cols pivots).size + pivots.size = cols
```

`CompPoly.DenseMatrix.homogeneousKernelBasis_size_add_rank` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L431))

> **Rank-nullity for the dense kernel basis.** The basis has one vector per
> non-pivot column of `rref M`.

```lean
theorem homogeneousKernelBasis_size_add_rank [Field F] [BEq F] (M : DenseMatrix F) :
    (homogeneousKernelBasis M).size + (rref M).pivots.size = M.cols
```

`CompPoly.DenseMatrix.homogeneousKernelBasis_getD_freeColumn` (theorem, [line 439](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L439))

> The `i`-th dense kernel basis vector is one at the `i`-th free column and zero
> at every other free column.

```lean
theorem homogeneousKernelBasis_getD_freeColumn [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {i j : Nat}
    (hi : i < (freeColumns M.cols (rref M).pivots).size)
    (hj : j < (freeColumns M.cols (rref M).pivots).size) :
    ((homogeneousKernelBasis M).getD i #[]).getD
        ((freeColumns M.cols (rref M).pivots).getD j 0) 0 =
      if j = i then 1 else 0
```

`CompPoly.DenseMatrix.homogeneousKernelBasis_linearIndependent` (theorem, [line 454](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean#L454))

> **Linear independence of the dense kernel basis.** A linear combination of
> the basis vectors that vanishes below the column count has all coefficients
> zero.

```lean
theorem homogeneousKernelBasis_linearIndependent [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) (c : Nat → F)
    (hc : ∀ k, k < M.cols →
      ∑ i ∈ Finset.range (homogeneousKernelBasis M).size,
        c i * ((homogeneousKernelBasis M).getD i #[]).getD k 0 = 0) :
    ∀ i, i < (homogeneousKernelBasis M).size → c i = 0
```

## Depends on

- [Row-Array Homogeneous Kernels](rowarray.md)
- [Dense RREF Shape Correctness](rrefshape.md)

## Proof depends on

- [Row-Array Homogeneous-Kernel Correctness](rowarraycorrectness.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/Dense/KernelBasisCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.KernelBasisCorrectness.json)
