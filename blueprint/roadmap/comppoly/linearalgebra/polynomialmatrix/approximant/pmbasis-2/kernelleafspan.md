---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.rowIsZero_eq_zeroRow, CompPoly.PolynomialMatrix.Approximant.size_pos_of_mem_matrixRows, CompPoly.PolynomialMatrix.Approximant.wellFormed_of_sizes, CompPoly.PolynomialMatrix.Approximant.eq_empty_of_mem_rowSpan_empty, CompPoly.PolynomialMatrix.Approximant.insertKernelLeaf_foldl_pivotInv, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots_rowSpan_superset, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots_rows, CompPoly.PolynomialMatrix.Approximant.rowIsZero_empty, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsIncremental_rowSpan_superset
statement: formalized
proof: formalized
---

# Kernel-Leaf Reduction Row-Span Soundness

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.KernelLeafSpan`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean), by Valerii Huhnin.

> The shifted pivot-table reduction preserves the generated row module: the
> fuel bound dominates the shifted row measure, every displaced row re-enters
> the table as a reduced combination, and the incremental reduction loop keeps
> every input row inside the span of its output.

> ## Kernel-leaf reduction row-span soundness
>
> The pivot-table reduction only ever replaces rows by row operations that are
> invertible inside the generated row module, so no original row leaves the row
> span.  The proofs below make this precise: leading-term cancellation is the
> Mulders-Storjohann cancellation in disguise, the pivot-table insertion loop is
> tracked through a fuel-indexed measure argument, and the incremental reducer
> chains the per-call result through row-span transitivity.

`CompPoly.PolynomialMatrix.Approximant.rowIsZero_eq_zeroRow` (theorem, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L127))

> A zero row is the zero row of its width.

```lean
theorem rowIsZero_eq_zeroRow {row : PolynomialRow F}
    (h : RowIsZero row) : row = zeroRow row.size
```

`CompPoly.PolynomialMatrix.Approximant.size_pos_of_mem_matrixRows` (theorem, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L180))

> Matrices with a member row are nonempty.

```lean
theorem size_pos_of_mem_matrixRows {M : PolynomialMatrix F}
    {r : PolynomialRow F} (h : r ∈ MatrixRows M) : 0 < M.size
```

`CompPoly.PolynomialMatrix.Approximant.wellFormed_of_sizes` (theorem, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L189))

> Uniform row widths make a matrix well formed.

```lean
theorem wellFormed_of_sizes {M : PolynomialMatrix F} {n : Nat}
    (h : ∀ r ∈ MatrixRows M, r.size = n) : WellFormed M
```

`CompPoly.PolynomialMatrix.Approximant.eq_empty_of_mem_rowSpan_empty` (theorem, [line 718](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L718))

> The row span of the empty matrix only contains the empty row.

```lean
theorem eq_empty_of_mem_rowSpan_empty {x : PolynomialRow F}
    (hx : x ∈ RowSpan (#[] : PolynomialMatrix F)) : x = #[]
```

`CompPoly.PolynomialMatrix.Approximant.insertKernelLeaf_foldl_pivotInv` (theorem, [line 774](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L774))

> Folded pivot-table insertion preserves the table invariant.

```lean
theorem insertKernelLeaf_foldl_pivotInv {n : Nat} :
    ∀ (l : List (PolynomialRow F)) (fuel : Nat)
      (pivots : Array (Option (PolynomialRow F))) (shift : Array Nat),
      (∀ r ∈ l, r.size = n) →
      (∀ p r, pivots.getD p none = some r →
        r.size = n ∧ rowShiftedLeadingPosition? r shift = some p) →
      ∀ p r,
        (l.foldl (fun pv r ↦ insertKernelLeafPivotRowWithFuel fuel pv shift r)
          pivots).getD p none = some r →
        r.size = n ∧ rowShiftedLeadingPosition? r shift = some p
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots_rowSpan_superset` (theorem, [line 1002](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L1002))

> The pivot-table reduction preserves the generated row module: every
> nonzero source row stays inside the row span of the reduced matrix.

```lean
theorem reduceKernelLeafRowsByPivots_rowSpan_superset [DecidableEq F]
    {rows : PolynomialMatrix F} {shift : Array Nat} {n : Nat}
    (hsizes : ∀ r ∈ MatrixRows rows, r.size = n)
    {row : PolynomialRow F} (hrow : row ∈ MatrixRows rows)
    (hnz : ¬ RowIsZero row) :
    row ∈ RowSpan (reduceKernelLeafRowsByPivots rows shift)
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots_rows` (theorem, [line 1030](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L1030))

> Reduced kernel-leaf rows keep the uniform width and are nonzero.

```lean
theorem reduceKernelLeafRowsByPivots_rows {n : Nat}
    {rows : PolynomialMatrix F} {shift : Array Nat}
    (hsizes : ∀ r ∈ MatrixRows rows, r.size = n) :
    ∀ r ∈ MatrixRows (reduceKernelLeafRowsByPivots rows shift),
      r.size = n ∧ rowIsZero r = false
```

`CompPoly.PolynomialMatrix.Approximant.rowIsZero_empty` (theorem, [line 1097](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L1097))

> The empty row is a zero row.

```lean
theorem rowIsZero_empty : RowIsZero (#[] : PolynomialRow F)
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsIncremental_rowSpan_superset` (theorem, [line 1200](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean#L1200))

> The incremental kernel-leaf reduction preserves the generated row module:
> every nonzero source row stays inside the row span of the reduced basis.

```lean
theorem reduceKernelLeafRowsIncremental_rowSpan_superset [DecidableEq F]
    {rows : PolynomialMatrix F} {shift : Array Nat} {n : Nat}
    (hsizes : ∀ r ∈ MatrixRows rows, r.size = n)
    {row : PolynomialRow F} (hrow : row ∈ MatrixRows rows)
    (hnz : ¬ RowIsZero row) :
    row ∈ RowSpan (reduceKernelLeafRowsIncremental rows shift)
```

## Depends on

- [Scalar Kernel-Leaf PM-Basis Definitions](kernelleaf.md)
- [Row Span for Polynomial Matrices](../../rowspan.md)

## Proof depends on

- [Kernel-Leaf Basis Soundness](kernelleafsoundness.md)
- [Mulders-Storjohann Correctness Termination Measure Helpers](../../muldersstorjohanncorrectness/measure.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/KernelLeafSpan.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.KernelLeafSpan.json)
