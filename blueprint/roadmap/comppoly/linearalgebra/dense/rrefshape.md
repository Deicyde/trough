---
catalog: module
lean: CompPoly.DenseMatrix.PivotColumnsShaped, CompPoly.DenseMatrix.pivotColumnsShaped_empty, CompPoly.DenseMatrix.swapRows_preserves_column_shape_of_ne, CompPoly.DenseMatrix.list_forIn_addScaledRow_get_of_not_mem, CompPoly.DenseMatrix.list_forIn_addScaledRow_get_pivotRow, CompPoly.DenseMatrix.list_forIn_addScaledRow_get_row_mem, CompPoly.DenseMatrix.list_forIn_addScaledRow_get_of_source_zero, CompPoly.DenseMatrix.normalizeAndEliminate_get_pivot, CompPoly.DenseMatrix.normalizeAndEliminate_get_row_pivot, CompPoly.DenseMatrix.normalizeAndEliminate_get_of_pivotRow_zero, CompPoly.DenseMatrix.rrefLoop_pivots_size_le_rows, CompPoly.DenseMatrix.rref_pivots_size_le_rows, CompPoly.DenseMatrix.PivotColumnsBefore, CompPoly.DenseMatrix.PivotColumnsStrict, CompPoly.DenseMatrix.pivotColumnsBefore_empty, CompPoly.DenseMatrix.pivotColumnsStrict_empty, CompPoly.DenseMatrix.pivotColumnsBefore_mono, CompPoly.DenseMatrix.pivotColumnsBefore_push, CompPoly.DenseMatrix.pivotColumnsStrict_push, CompPoly.DenseMatrix.pivotColumnsStrict_getD_ne, CompPoly.DenseMatrix.rrefLoop_pivots_getD_lt_cols, CompPoly.DenseMatrix.rref_pivots_getD_lt_cols, CompPoly.DenseMatrix.rrefLoop_pivotColumnsStrict, CompPoly.DenseMatrix.rref_pivotColumnsStrict, CompPoly.DenseMatrix.rrefLoop_pivotColumnsShaped, CompPoly.DenseMatrix.rref_pivotColumnsShaped, CompPoly.DenseMatrix.ProcessedColumnsZeroBelow, CompPoly.DenseMatrix.processedColumnsZeroBelow_pivot_step, CompPoly.DenseMatrix.rrefLoop_processedColumnsZeroBelow, CompPoly.DenseMatrix.rref_processedColumnsZeroBelow
statement: formalized
proof: formalized
---

# Dense RREF Shape Correctness

`CompPoly.LinearAlgebra.Dense.RrefShape`, in [CompPoly/LinearAlgebra/Dense/RrefShape.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean), by Valerii Huhnin.

> Pivot-column and processed-column invariants for dense row reduction.

`CompPoly.DenseMatrix.PivotColumnsShaped` (definition, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L23))

> Recorded pivot columns have the reduced-column shape expected of RREF.

```lean
def PivotColumnsShaped [Zero F] [One F] (M : DenseMatrix F)
    (pivots : Array Nat) : Prop
```

`CompPoly.DenseMatrix.pivotColumnsShaped_empty` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L29))

```lean
theorem pivotColumnsShaped_empty [Zero F] [One F] (M : DenseMatrix F) :
    PivotColumnsShaped M #[]
```

`CompPoly.DenseMatrix.swapRows_preserves_column_shape_of_ne` (theorem, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L34))

```lean
theorem swapRows_preserves_column_shape_of_ne [Zero F] [One F]
    {M : DenseMatrix F} (hM : WellFormed M) {rowA rowB pivot oldCol : Nat}
    (hrowA : rowA < M.rows) (hrowB : rowB < M.rows) (hcol : oldCol < M.cols)
    (hA : rowA ≠ pivot) (hB : rowB ≠ pivot)
    (hshape : ∀ row, row < M.rows → M.get row oldCol = if row = pivot then 1 else 0) :
    ∀ row, row < (swapRows M rowA rowB).rows →
      (swapRows M rowA rowB).get row oldCol = if row = pivot then 1 else 0
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_get_of_not_mem` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L60))

```lean
theorem list_forIn_addScaledRow_get_of_not_mem [Field F]
    (rows : List Nat) {out : DenseMatrix F} {row col pivotRow pivotCol : Nat}
    (hcol : col < out.cols) (hnot : row ∉ rows) :
    (Id.run (forIn rows out fun r M ↦
      if r = pivotRow then
        pure (ForInStep.yield M)
      else
        pure (ForInStep.yield
          (addScaledRow M r pivotRow (-(M.get r pivotCol)))) :
      Id (DenseMatrix F))).get row col = out.get row col
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_get_pivotRow` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L114))

```lean
theorem list_forIn_addScaledRow_get_pivotRow [Field F]
    (rows : List Nat) {out : DenseMatrix F} {pivotRow pivotCol : Nat}
    (hcol : pivotCol < out.cols) (hpivot : out.get pivotRow pivotCol = 1) :
    (Id.run (forIn rows out fun row M ↦
      if row = pivotRow then
        pure (ForInStep.yield M)
      else
        pure (ForInStep.yield
          (addScaledRow M row pivotRow (-(M.get row pivotCol)))) :
      Id (DenseMatrix F))).get pivotRow pivotCol = 1
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_get_row_mem` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L143))

```lean
theorem list_forIn_addScaledRow_get_row_mem [Field F]
    (rows : List Nat) {out : DenseMatrix F} {row pivotRow pivotCol : Nat}
    (hout : WellFormed out) (hpivotRow : pivotRow < out.rows)
    (hcol : pivotCol < out.cols) (hpivot : out.get pivotRow pivotCol = 1)
    (hrows : ∀ r, r ∈ rows → r < out.rows) (hnodup : rows.Nodup)
    (hmem : row ∈ rows) (hne : row ≠ pivotRow) :
    (Id.run (forIn rows out fun r M ↦
      if r = pivotRow then
        pure (ForInStep.yield M)
      else
        pure (ForInStep.yield
          (addScaledRow M r pivotRow (-(M.get r pivotCol)))) :
      Id (DenseMatrix F))).get row pivotCol = 0
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_get_of_source_zero` (theorem, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L242))

```lean
theorem list_forIn_addScaledRow_get_of_source_zero [Field F]
    (rows : List Nat) {out : DenseMatrix F} {row pivotRow oldCol pivotCol : Nat}
    (hout : WellFormed out) (hcol : oldCol < out.cols)
    (hrows : ∀ r, r ∈ rows → r < out.rows)
    (hsource : out.get pivotRow oldCol = 0) :
    (Id.run (forIn rows out fun r M ↦
      if r = pivotRow then
        pure (ForInStep.yield M)
      else
        pure (ForInStep.yield
          (addScaledRow M r pivotRow (-(M.get r pivotCol)))) :
      Id (DenseMatrix F))).get row oldCol = out.get row oldCol
```

`CompPoly.DenseMatrix.normalizeAndEliminate_get_pivot` (theorem, [line 313](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L313))

```lean
theorem normalizeAndEliminate_get_pivot [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {pivotRow pivotCol : Nat}
    (hpivotRow : pivotRow < M.rows) (hpivotCol : pivotCol < M.cols)
    (hpivot : M.get pivotRow pivotCol ≠ 0) :
    (normalizeAndEliminate M pivotRow pivotCol).get pivotRow pivotCol = 1
```

`CompPoly.DenseMatrix.normalizeAndEliminate_get_row_pivot` (theorem, [line 337](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L337))

```lean
theorem normalizeAndEliminate_get_row_pivot [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {pivotRow pivotCol row : Nat}
    (hpivotRow : pivotRow < M.rows) (hpivotCol : pivotCol < M.cols)
    (hrow : row < M.rows) (hne : row ≠ pivotRow)
    (hpivot : M.get pivotRow pivotCol ≠ 0) :
    (normalizeAndEliminate M pivotRow pivotCol).get row pivotCol = 0
```

`CompPoly.DenseMatrix.normalizeAndEliminate_get_of_pivotRow_zero` (theorem, [line 385](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L385))

```lean
theorem normalizeAndEliminate_get_of_pivotRow_zero [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {pivotRow pivotCol oldCol row : Nat}
    (hpivotRow : pivotRow < M.rows) (holdCol : oldCol < M.cols)
    (hpivotZero : M.get pivotRow oldCol = 0) :
    (normalizeAndEliminate M pivotRow pivotCol).get row oldCol = M.get row oldCol
```

`CompPoly.DenseMatrix.rrefLoop_pivots_size_le_rows` (theorem, [line 443](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L443))

```lean
theorem rrefLoop_pivots_size_le_rows [Field F] [BEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots,
      row ≤ M.rows →
        (rrefLoop fuel col row M pivots).pivots.size ≤
          pivots.size + (M.rows - row)
```

`CompPoly.DenseMatrix.rref_pivots_size_le_rows` (theorem, [line 483](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L483))

```lean
theorem rref_pivots_size_le_rows [Field F] [BEq F]
    (M : DenseMatrix F) : (rref M).pivots.size ≤ M.rows
```

`CompPoly.DenseMatrix.PivotColumnsBefore` (definition, [line 490](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L490))

> All recorded pivot columns are strictly before the current scan column.

```lean
def PivotColumnsBefore (pivots : Array Nat) (col : Nat) : Prop
```

`CompPoly.DenseMatrix.PivotColumnsStrict` (definition, [line 494](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L494))

> Pivot columns are strictly increasing in pivot-row order.

```lean
def PivotColumnsStrict (pivots : Array Nat) : Prop
```

`CompPoly.DenseMatrix.pivotColumnsBefore_empty` (theorem, [line 498](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L498))

```lean
theorem pivotColumnsBefore_empty (col : Nat) :
    PivotColumnsBefore #[] col
```

`CompPoly.DenseMatrix.pivotColumnsStrict_empty` (theorem, [line 503](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L503))

```lean
theorem pivotColumnsStrict_empty : PivotColumnsStrict #[]
```

`CompPoly.DenseMatrix.pivotColumnsBefore_mono` (theorem, [line 507](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L507))

```lean
theorem pivotColumnsBefore_mono {pivots : Array Nat} {col next : Nat}
    (h : PivotColumnsBefore pivots col) (hcol : col < next) :
    PivotColumnsBefore pivots next
```

`CompPoly.DenseMatrix.pivotColumnsBefore_push` (theorem, [line 513](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L513))

```lean
theorem pivotColumnsBefore_push {pivots : Array Nat} {col next : Nat}
    (h : PivotColumnsBefore pivots col) (hcol : col < next) :
    PivotColumnsBefore (pivots.push col) next
```

`CompPoly.DenseMatrix.pivotColumnsStrict_push` (theorem, [line 529](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L529))

```lean
theorem pivotColumnsStrict_push {pivots : Array Nat} {col : Nat}
    (hstrict : PivotColumnsStrict pivots) (hbefore : PivotColumnsBefore pivots col) :
    PivotColumnsStrict (pivots.push col)
```

`CompPoly.DenseMatrix.pivotColumnsStrict_getD_ne` (theorem, [line 555](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L555))

```lean
theorem pivotColumnsStrict_getD_ne {pivots : Array Nat}
    (hstrict : PivotColumnsStrict pivots) {i j : Nat}
    (hi : i < pivots.size) (hj : j < pivots.size) (hne : i ≠ j) :
    pivots.getD i 0 ≠ pivots.getD j 0
```

`CompPoly.DenseMatrix.rrefLoop_pivots_getD_lt_cols` (theorem, [line 569](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L569))

```lean
theorem rrefLoop_pivots_getD_lt_cols [Field F] [BEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots,
      (∀ i, i < pivots.size → pivots.getD i 0 < M.cols) →
        ∀ i, i < (rrefLoop fuel col row M pivots).pivots.size →
          (rrefLoop fuel col row M pivots).pivots.getD i 0 < M.cols
```

`CompPoly.DenseMatrix.rref_pivots_getD_lt_cols` (theorem, [line 620](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L620))

```lean
theorem rref_pivots_getD_lt_cols [Field F] [BEq F] (M : DenseMatrix F) :
    ∀ i, i < (rref M).pivots.size → (rref M).pivots.getD i 0 < M.cols
```

`CompPoly.DenseMatrix.rrefLoop_pivotColumnsStrict` (theorem, [line 627](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L627))

```lean
theorem rrefLoop_pivotColumnsStrict [Field F] [BEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots,
      PivotColumnsBefore pivots col → PivotColumnsStrict pivots →
        PivotColumnsStrict (rrefLoop fuel col row M pivots).pivots
```

`CompPoly.DenseMatrix.rref_pivotColumnsStrict` (theorem, [line 654](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L654))

```lean
theorem rref_pivotColumnsStrict [Field F] [BEq F] (M : DenseMatrix F) :
    PivotColumnsStrict (rref M).pivots
```

`CompPoly.DenseMatrix.rrefLoop_pivotColumnsShaped` (theorem, [line 660](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L660))

```lean
theorem rrefLoop_pivotColumnsShaped [Field F] [BEq F] [LawfulBEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots,
      WellFormed M →
        row = pivots.size →
          PivotColumnsBefore pivots col →
            PivotColumnsShaped M pivots →
              PivotColumnsShaped (rrefLoop fuel col row M pivots).matrix
                (rrefLoop fuel col row M pivots).pivots
```

`CompPoly.DenseMatrix.rref_pivotColumnsShaped` (theorem, [line 796](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L796))

```lean
theorem rref_pivotColumnsShaped [Field F] [BEq F] [LawfulBEq F]
    (M : DenseMatrix F) (hM : WellFormed M) :
    PivotColumnsShaped (rref M).matrix (rref M).pivots
```

`CompPoly.DenseMatrix.ProcessedColumnsZeroBelow` (definition, [line 804](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L804))

> All rows at or below the active pivot row are zero in already-scanned columns.

```lean
def ProcessedColumnsZeroBelow [Zero F] (M : DenseMatrix F)
    (activeRow col : Nat) : Prop
```

`CompPoly.DenseMatrix.processedColumnsZeroBelow_pivot_step` (theorem, [line 808](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L808))

```lean
theorem processedColumnsZeroBelow_pivot_step
    [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {row col pivotRow : Nat}
    (hrow : row < M.rows) (hcol : col < M.cols)
    (hpivotLt : pivotRow < M.rows) (hpivotGe : row ≤ pivotRow)
    (hpivotSwap : (swapRows M pivotRow row).get row col ≠ 0)
    (hproc : ProcessedColumnsZeroBelow M row col) :
    ProcessedColumnsZeroBelow
      (normalizeAndEliminate (swapRows M pivotRow row) row col)
      (row + 1) (col + 1)
```

`CompPoly.DenseMatrix.rrefLoop_processedColumnsZeroBelow` (theorem, [line 865](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L865))

```lean
theorem rrefLoop_processedColumnsZeroBelow
    [Field F] [BEq F] [LawfulBEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots,
      WellFormed M →
        row = pivots.size →
          row ≤ M.rows →
            M.cols ≤ col + fuel →
              ProcessedColumnsZeroBelow M row col →
                ProcessedColumnsZeroBelow
                  (rrefLoop fuel col row M pivots).matrix
                  (rrefLoop fuel col row M pivots).pivots.size M.cols
```

`CompPoly.DenseMatrix.rref_processedColumnsZeroBelow` (theorem, [line 947](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean#L947))

```lean
theorem rref_processedColumnsZeroBelow
    [Field F] [BEq F] [LawfulBEq F]
    (M : DenseMatrix F) (hM : WellFormed M) :
    ProcessedColumnsZeroBelow (rref M).matrix (rref M).pivots.size M.cols
```

## Depends on

- [Dense Row Operations](rowops.md)

## Proof depends on

- [Dense RREF Semantic Correctness](rrefsemantics.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/RrefShape.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/Dense/RrefShape.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.RrefShape.json)
