---
catalog: module
lean: CompPoly.PolynomialMatrix.replaceRow_size, CompPoly.PolynomialMatrix.replaceRow_matrixWidth, CompPoly.PolynomialMatrix.replaceRow_shape, CompPoly.PolynomialMatrix.replaceRow_wellFormed, CompPoly.PolynomialMatrix.replaceRow_rows_mem_rowSpan, CompPoly.PolynomialMatrix.replaceRow_newRow_mem, CompPoly.PolynomialMatrix.replaceRow_oldRow_mem, CompPoly.PolynomialMatrix.matrix_getD_size_of_wellFormed, CompPoly.PolynomialMatrix.matrix_getElem?_getD_size_of_wellFormed, CompPoly.PolynomialMatrix.matrix_getD_mem_rowSpan, CompPoly.PolynomialMatrix.zeroRow_mem_rowSpan, CompPoly.PolynomialMatrix.rowLinearCombination_mem_rowSpan_of_rows_mem, CompPoly.PolynomialMatrix.rowSpan_subset_of_rows_mem, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_size_of_wellFormed
statement: formalized
proof: formalized
---

# Mulders-Storjohann Correctness Matrix Row Helpers

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.MatrixRows`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean), by Valerii Huhnin.

> Replacement-row, matrix-shape, and row-span transport lemmas.

`CompPoly.PolynomialMatrix.replaceRow_size` (theorem, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L25))

```lean
theorem replaceRow_size (M : PolynomialMatrix F) (idx : Nat) (row : PolynomialRow F) :
    (replaceRow M idx row).size = M.size
```

`CompPoly.PolynomialMatrix.replaceRow_matrixWidth` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L30))

```lean
theorem replaceRow_matrixWidth
    {M : PolynomialMatrix F} {idx : Nat} {row : PolynomialRow F}
    (hrow : row.size = MatrixWidth M) :
    MatrixWidth (replaceRow M idx row) = MatrixWidth M
```

`CompPoly.PolynomialMatrix.replaceRow_shape` (theorem, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L45))

```lean
theorem replaceRow_shape
    {M : PolynomialMatrix F} {idx : Nat} {row : PolynomialRow F}
    (hrow : row.size = MatrixWidth M) :
    MatrixShape (replaceRow M idx row) = MatrixShape M
```

`CompPoly.PolynomialMatrix.replaceRow_wellFormed` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L52))

```lean
theorem replaceRow_wellFormed
    {M : PolynomialMatrix F} {idx : Nat} {row : PolynomialRow F}
    (hM : WellFormed M) (hrow : row.size = MatrixWidth M) :
    WellFormed (replaceRow M idx row)
```

`CompPoly.PolynomialMatrix.replaceRow_rows_mem_rowSpan` (theorem, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L77))

```lean
theorem replaceRow_rows_mem_rowSpan
    {M : PolynomialMatrix F} (hM : WellFormed M) {idx : Nat} {newRow row : PolynomialRow F}
    (hnew : newRow ∈ RowSpan M)
    (hrow : row ∈ MatrixRows (replaceRow M idx newRow)) :
    row ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.replaceRow_newRow_mem` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L100))

```lean
theorem replaceRow_newRow_mem
    {M : PolynomialMatrix F} {idx : Nat} {newRow : PolynomialRow F}
    (hidx : idx < M.size) :
    newRow ∈ MatrixRows (replaceRow M idx newRow)
```

`CompPoly.PolynomialMatrix.replaceRow_oldRow_mem` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L113))

```lean
theorem replaceRow_oldRow_mem
    {M : PolynomialMatrix F} {idx k : Nat} {newRow : PolynomialRow F}
    (hk : k < M.size) (hne : idx ≠ k) :
    M[k] ∈ MatrixRows (replaceRow M idx newRow)
```

`CompPoly.PolynomialMatrix.matrix_getD_size_of_wellFormed` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L125))

```lean
theorem matrix_getD_size_of_wellFormed
    {M : PolynomialMatrix F} (hM : WellFormed M) {i : Nat} (hi : i < M.size) :
    (M.getD i #[]).size = MatrixWidth M
```

`CompPoly.PolynomialMatrix.matrix_getElem?_getD_size_of_wellFormed` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L134))

```lean
theorem matrix_getElem?_getD_size_of_wellFormed
    {M : PolynomialMatrix F} (hM : WellFormed M) {i : Nat} (hi : i < M.size) :
    (M[i]?.getD #[]).size = MatrixWidth M
```

`CompPoly.PolynomialMatrix.matrix_getD_mem_rowSpan` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L139))

```lean
theorem matrix_getD_mem_rowSpan
    {M : PolynomialMatrix F} (hM : WellFormed M) {i : Nat} (hi : i < M.size) :
    M.getD i #[] ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.zeroRow_mem_rowSpan` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L149))

```lean
theorem zeroRow_mem_rowSpan
    {M : PolynomialMatrix F} (hM : WellFormed M) :
    zeroRow (F := F) (MatrixWidth M) ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.rowLinearCombination_mem_rowSpan_of_rows_mem` (theorem, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L181))

```lean
theorem rowLinearCombination_mem_rowSpan_of_rows_mem
    {A B : PolynomialMatrix F} (hB : WellFormed B)
    (hwidth : MatrixWidth A = MatrixWidth B)
    (hrows : ∀ row, row ∈ MatrixRows A → row ∈ RowSpan B)
    (coeffs : Array (CPolynomial F)) :
    rowLinearCombination coeffs A ∈ RowSpan B
```

`CompPoly.PolynomialMatrix.rowSpan_subset_of_rows_mem` (theorem, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L216))

```lean
theorem rowSpan_subset_of_rows_mem
    {A B : PolynomialMatrix F} (hB : WellFormed B)
    (hwidth : MatrixWidth A = MatrixWidth B)
    (hrows : ∀ row, row ∈ MatrixRows A → row ∈ RowSpan B) :
    RowSpan A ⊆ RowSpan B
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_size_of_wellFormed` (theorem, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean#L225))

```lean
theorem cancelShiftedLeadingTerm_size_of_wellFormed
    {M : PolynomialMatrix F} (hM : WellFormed M) {i j : Nat}
    (hi : i < M.size) (hj : j < M.size) (shift : Array Nat) :
    (cancelShiftedLeadingTerm (M.getD i #[]) (M.getD j #[]) shift).size =
      MatrixWidth M
```

## Depends on

- [Mulders-Storjohann Shifted Row Reduction](../muldersstorjohann.md)
- [Row Span for Polynomial Matrices](../rowspan.md)

## Proof depends on

- [Mulders-Storjohann Correctness Row and Row-Span Helpers](rowops.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/MatrixRows.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.MatrixRows.json)
