---
catalog: module
lean: CompPoly.DenseMatrix.index_lt_of_lt, CompPoly.DenseMatrix.get_setD_index_same, CompPoly.DenseMatrix.get_setD_index_ne, CompPoly.DenseMatrix.get_setD_index_ne_same_row, CompPoly.DenseMatrix.get_setD_index_ne_same_col, CompPoly.DenseMatrix.list_foldl_array_size_of_eq, CompPoly.DenseMatrix.swapRows_cols, CompPoly.DenseMatrix.swapRows_rows, CompPoly.DenseMatrix.swapRows_wf, CompPoly.DenseMatrix.swapRows_get_of_row_ne, CompPoly.DenseMatrix.swapRows_get_left, CompPoly.DenseMatrix.swapRows_get_right, CompPoly.DenseMatrix.list_forIn_addScaledRow_rows, CompPoly.DenseMatrix.list_forIn_addScaledRow_cols, CompPoly.DenseMatrix.normalizeAndEliminate_cols, CompPoly.DenseMatrix.normalizeAndEliminate_rows, CompPoly.DenseMatrix.scaleRow_get_of_row_ne, CompPoly.DenseMatrix.scaleRow_wf, CompPoly.DenseMatrix.scaleRow_get_same, CompPoly.DenseMatrix.addScaledRow_get_of_row_ne, CompPoly.DenseMatrix.addScaledRow_wf, CompPoly.DenseMatrix.addScaledRow_get_same, CompPoly.DenseMatrix.dotRow_ext_rows, CompPoly.DenseMatrix.dotRow_scaleRow_same, CompPoly.DenseMatrix.dotRow_addScaledRow_same, CompPoly.DenseMatrix.dotRow_swapRows_left, CompPoly.DenseMatrix.dotRow_swapRows_right, CompPoly.DenseMatrix.dotRow_swapRows_of_ne, CompPoly.DenseMatrix.dotRow_scaleRow_of_ne, CompPoly.DenseMatrix.dotRow_addScaledRow_of_ne, CompPoly.DenseMatrix.isHomogeneousSolution_swapRows_of_solution, CompPoly.DenseMatrix.isHomogeneousSolution_scaleRow_of_solution, CompPoly.DenseMatrix.isHomogeneousSolution_addScaledRow_of_solution, CompPoly.DenseMatrix.isHomogeneousSolution_of_swapRows_solution, CompPoly.DenseMatrix.isHomogeneousSolution_of_scaleRow_solution, CompPoly.DenseMatrix.isHomogeneousSolution_of_addScaledRow_solution
statement: formalized
proof: formalized
---

# Dense Row-Operation Correctness

`CompPoly.LinearAlgebra.Dense.RowOpsCorrectness`, in [CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean), by Valerii Huhnin.

> Correctness lemmas for executable dense row operations.

`CompPoly.DenseMatrix.index_lt_of_lt` (theorem, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L25))

```lean
theorem index_lt_of_lt [Zero F] {M : DenseMatrix F} (hM : WellFormed M)
    {row col : Nat} (hrow : row < M.rows) (hcol : col < M.cols) :
    M.index row col < M.data.size
```

`CompPoly.DenseMatrix.get_setD_index_same` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L36))

```lean
theorem get_setD_index_same [Zero F] {M : DenseMatrix F} {data : Array F}
    {row col : Nat} (hidx : M.index row col < data.size) (value : F) :
    (setD data (M.index row col) value).getD (M.index row col) 0 = value
```

`CompPoly.DenseMatrix.get_setD_index_ne` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L43))

```lean
theorem get_setD_index_ne [Zero F] (M : DenseMatrix F) (data : Array F)
    {row col row' col' : Nat} (hcol : col < M.cols) (hcol' : col' < M.cols)
    (hne : row ≠ row' ∨ col ≠ col') (value : F) :
    (setD data (M.index row col) value).getD (M.index row' col') 0 =
      data.getD (M.index row' col') 0
```

`CompPoly.DenseMatrix.get_setD_index_ne_same_row` (theorem, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L80))

```lean
theorem get_setD_index_ne_same_row [Zero F] (M : DenseMatrix F) (data : Array F)
    {row col col' : Nat} (hcol : col < M.cols) (hcol' : col' < M.cols)
    (hne : col ≠ col') (value : F) :
    (setD data (M.index row col) value).getD (M.index row col') 0 =
      data.getD (M.index row col') 0
```

`CompPoly.DenseMatrix.get_setD_index_ne_same_col` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L87))

```lean
theorem get_setD_index_ne_same_col [Zero F] (M : DenseMatrix F) (data : Array F)
    {row row' col : Nat} (hcol : col < M.cols)
    (hne : row ≠ row') (value : F) :
    (setD data (M.index row col) value).getD (M.index row' col) 0 =
      data.getD (M.index row' col) 0
```

`CompPoly.DenseMatrix.list_foldl_array_size_of_eq` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L94))

```lean
theorem list_foldl_array_size_of_eq {α β : Type*}
    (f : Array α → β → Array α)
    (h : ∀ data x, (f data x).size = data.size) :
    ∀ (xs : List β) (data : Array α), (xs.foldl f data).size = data.size
```

`CompPoly.DenseMatrix.swapRows_cols` (theorem, [line 108](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L108))

```lean
theorem swapRows_cols [Zero F]
    (M : DenseMatrix F) (rowA rowB : Nat) :
    (swapRows M rowA rowB).cols = M.cols
```

`CompPoly.DenseMatrix.swapRows_rows` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L114))

```lean
theorem swapRows_rows [Zero F]
    (M : DenseMatrix F) (rowA rowB : Nat) :
    (swapRows M rowA rowB).rows = M.rows
```

`CompPoly.DenseMatrix.swapRows_wf` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L120))

```lean
theorem swapRows_wf [Zero F] {M : DenseMatrix F} (hM : WellFormed M)
    (rowA rowB : Nat) : WellFormed (swapRows M rowA rowB)
```

`CompPoly.DenseMatrix.swapRows_get_of_row_ne` (theorem, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L128))

```lean
theorem swapRows_get_of_row_ne [Zero F] {M : DenseMatrix F}
    {rowA rowB row col : Nat} (hcol : col < M.cols)
    (hA : rowA ≠ row) (hB : rowB ≠ row) :
    (swapRows M rowA rowB).get row col = M.get row col
```

`CompPoly.DenseMatrix.swapRows_get_left` (theorem, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L167))

```lean
theorem swapRows_get_left [Zero F] {M : DenseMatrix F}
    (hM : WellFormed M) {rowA rowB col : Nat}
    (hrowA : rowA < M.rows) (hcol : col < M.cols) :
    (swapRows M rowA rowB).get rowA col = M.get rowB col
```

`CompPoly.DenseMatrix.swapRows_get_right` (theorem, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L265))

```lean
theorem swapRows_get_right [Zero F] {M : DenseMatrix F}
    (hM : WellFormed M) {rowA rowB col : Nat}
    (hrowB : rowB < M.rows) (hcol : col < M.cols) :
    (swapRows M rowA rowB).get rowB col = M.get rowA col
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_rows` (theorem, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L360))

```lean
theorem list_forIn_addScaledRow_rows [Field F]
    (rows : List Nat) (pivotRow pivotCol : Nat) (out : DenseMatrix F) :
    (Id.run (forIn rows out fun row r ↦
      if row = pivotRow then
        pure (ForInStep.yield r)
      else
        pure (ForInStep.yield
          (addScaledRow r row pivotRow (-(r.get row pivotCol)))) :
      Id (DenseMatrix F))).rows = out.rows
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_cols` (theorem, [line 377](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L377))

```lean
theorem list_forIn_addScaledRow_cols [Field F]
    (rows : List Nat) (pivotRow pivotCol : Nat) (out : DenseMatrix F) :
    (Id.run (forIn rows out fun row r ↦
      if row = pivotRow then
        pure (ForInStep.yield r)
      else
        pure (ForInStep.yield
          (addScaledRow r row pivotRow (-(r.get row pivotCol)))) :
      Id (DenseMatrix F))).cols = out.cols
```

`CompPoly.DenseMatrix.normalizeAndEliminate_cols` (theorem, [line 394](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L394))

```lean
theorem normalizeAndEliminate_cols [Field F] [BEq F]
    (M : DenseMatrix F) (pivotRow pivotCol : Nat) :
    (normalizeAndEliminate M pivotRow pivotCol).cols = M.cols
```

`CompPoly.DenseMatrix.normalizeAndEliminate_rows` (theorem, [line 409](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L409))

```lean
theorem normalizeAndEliminate_rows [Field F] [BEq F]
    (M : DenseMatrix F) (pivotRow pivotCol : Nat) :
    (normalizeAndEliminate M pivotRow pivotCol).rows = M.rows
```

`CompPoly.DenseMatrix.scaleRow_get_of_row_ne` (theorem, [line 424](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L424))

```lean
theorem scaleRow_get_of_row_ne [Field F] {M : DenseMatrix F}
    {r row col : Nat} (factor : F) (hcol : col < M.cols) (hneq : r ≠ row) :
    (scaleRow M r factor).get row col = M.get row col
```

`CompPoly.DenseMatrix.scaleRow_wf` (theorem, [line 454](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L454))

```lean
theorem scaleRow_wf [Field F] {M : DenseMatrix F} (hM : WellFormed M)
    (row : Nat) (factor : F) : WellFormed (scaleRow M row factor)
```

`CompPoly.DenseMatrix.scaleRow_get_same` (theorem, [line 459](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L459))

```lean
theorem scaleRow_get_same [Field F] {M : DenseMatrix F}
    (hM : WellFormed M) {r col : Nat} (hr : r < M.rows) (hcol : col < M.cols)
    (factor : F) :
    (scaleRow M r factor).get r col = factor * M.get r col
```

`CompPoly.DenseMatrix.addScaledRow_get_of_row_ne` (theorem, [line 541](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L541))

```lean
theorem addScaledRow_get_of_row_ne [Field F] {M : DenseMatrix F}
    {target source row col : Nat} (factor : F) (hcol : col < M.cols)
    (hneq : target ≠ row) :
    (addScaledRow M target source factor).get row col = M.get row col
```

`CompPoly.DenseMatrix.addScaledRow_wf` (theorem, [line 574](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L574))

```lean
theorem addScaledRow_wf [Field F] {M : DenseMatrix F} (hM : WellFormed M)
    (target source : Nat) (factor : F) : WellFormed (addScaledRow M target source factor)
```

`CompPoly.DenseMatrix.addScaledRow_get_same` (theorem, [line 579](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L579))

```lean
theorem addScaledRow_get_same [Field F] {M : DenseMatrix F}
    (hM : WellFormed M) {target source col : Nat}
    (htarget : target < M.rows) (hcol : col < M.cols) (factor : F) :
    (addScaledRow M target source factor).get target col =
      M.get target col + factor * M.get source col
```

`CompPoly.DenseMatrix.dotRow_ext_rows` (theorem, [line 670](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L670))

```lean
theorem dotRow_ext_rows [Semiring F] {M N : DenseMatrix F}
    {rowN rowM : Nat} {v : Array F} (hcols : N.cols = M.cols)
    (hget : ∀ col, col < M.cols → N.get rowN col = M.get rowM col) :
    N.dotRow rowN v = M.dotRow rowM v
```

`CompPoly.DenseMatrix.dotRow_scaleRow_same` (theorem, [line 696](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L696))

```lean
theorem dotRow_scaleRow_same [Field F] {M : DenseMatrix F}
    (hM : WellFormed M) {row : Nat} (hrow : row < M.rows)
    (factor : F) (v : Array F) :
    (scaleRow M row factor).dotRow row v = factor * M.dotRow row v
```

`CompPoly.DenseMatrix.dotRow_addScaledRow_same` (theorem, [line 735](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L735))

```lean
theorem dotRow_addScaledRow_same [Field F] {M : DenseMatrix F}
    (hM : WellFormed M) {target source : Nat} (htarget : target < M.rows)
    (factor : F) (v : Array F) :
    (addScaledRow M target source factor).dotRow target v =
      M.dotRow target v + factor * M.dotRow source v
```

`CompPoly.DenseMatrix.dotRow_swapRows_left` (theorem, [line 780](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L780))

```lean
theorem dotRow_swapRows_left [Semiring F] {M : DenseMatrix F}
    (hM : WellFormed M) {rowA rowB : Nat} (hrowA : rowA < M.rows) (v : Array F) :
    (swapRows M rowA rowB).dotRow rowA v = M.dotRow rowB v
```

`CompPoly.DenseMatrix.dotRow_swapRows_right` (theorem, [line 788](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L788))

```lean
theorem dotRow_swapRows_right [Semiring F] {M : DenseMatrix F}
    (hM : WellFormed M) {rowA rowB : Nat} (hrowB : rowB < M.rows) (v : Array F) :
    (swapRows M rowA rowB).dotRow rowB v = M.dotRow rowA v
```

`CompPoly.DenseMatrix.dotRow_swapRows_of_ne` (theorem, [line 796](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L796))

```lean
theorem dotRow_swapRows_of_ne [Semiring F] {M : DenseMatrix F}
    {rowA rowB row : Nat} (hrowA : rowA ≠ row) (hrowB : rowB ≠ row)
    (v : Array F) :
    (swapRows M rowA rowB).dotRow row v = M.dotRow row v
```

`CompPoly.DenseMatrix.dotRow_scaleRow_of_ne` (theorem, [line 805](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L805))

```lean
theorem dotRow_scaleRow_of_ne [Field F] {M : DenseMatrix F}
    {scale row : Nat} (factor : F) (hneq : scale ≠ row) (v : Array F) :
    (scaleRow M scale factor).dotRow row v = M.dotRow row v
```

`CompPoly.DenseMatrix.dotRow_addScaledRow_of_ne` (theorem, [line 813](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L813))

```lean
theorem dotRow_addScaledRow_of_ne [Field F] {M : DenseMatrix F}
    {target source row : Nat} (factor : F) (hneq : target ≠ row) (v : Array F) :
    (addScaledRow M target source factor).dotRow row v = M.dotRow row v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_swapRows_of_solution` (theorem, [line 821](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L821))

```lean
theorem isHomogeneousSolution_swapRows_of_solution [Field F]
    {M : DenseMatrix F} {v : Array F} {rowA rowB : Nat}
    (hM : WellFormed M) (hrowA : rowA < M.rows) (hrowB : rowB < M.rows)
    (hsol : IsHomogeneousSolution M v) :
    IsHomogeneousSolution (swapRows M rowA rowB) v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_scaleRow_of_solution` (theorem, [line 842](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L842))

```lean
theorem isHomogeneousSolution_scaleRow_of_solution [Field F]
    {M : DenseMatrix F} {v : Array F} {target : Nat} (hM : WellFormed M)
    (htarget : target < M.rows) (factor : F)
    (hsol : IsHomogeneousSolution M v) :
    IsHomogeneousSolution (scaleRow M target factor) v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_addScaledRow_of_solution` (theorem, [line 858](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L858))

```lean
theorem isHomogeneousSolution_addScaledRow_of_solution [Field F]
    {M : DenseMatrix F} {v : Array F} {target source : Nat}
    (hM : WellFormed M) (htarget : target < M.rows) (hsource : source < M.rows)
    (factor : F) (hsol : IsHomogeneousSolution M v) :
    IsHomogeneousSolution (addScaledRow M target source factor) v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_of_swapRows_solution` (theorem, [line 874](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L874))

```lean
theorem isHomogeneousSolution_of_swapRows_solution [Field F]
    {M : DenseMatrix F} {v : Array F} {rowA rowB : Nat}
    (hM : WellFormed M) (hrowA : rowA < M.rows) (hrowB : rowB < M.rows)
    (hsol : IsHomogeneousSolution (swapRows M rowA rowB) v) :
    IsHomogeneousSolution M v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_of_scaleRow_solution` (theorem, [line 903](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L903))

```lean
theorem isHomogeneousSolution_of_scaleRow_solution [Field F]
    {M : DenseMatrix F} {v : Array F} {target : Nat} (hM : WellFormed M)
    (htarget : target < M.rows) {factor : F} (hfactor : factor ≠ 0)
    (hsol : IsHomogeneousSolution (scaleRow M target factor) v) :
    IsHomogeneousSolution M v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_of_addScaledRow_solution` (theorem, [line 923](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean#L923))

```lean
theorem isHomogeneousSolution_of_addScaledRow_solution [Field F]
    {M : DenseMatrix F} {v : Array F} {target source : Nat}
    (hM : WellFormed M) (htarget : target < M.rows) (hsource : source < M.rows)
    (hts : target ≠ source) (factor : F)
    (hsol : IsHomogeneousSolution (addScaledRow M target source factor) v) :
    IsHomogeneousSolution M v
```

## Depends on

- [Dense Row Operations](rowops.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RowOpsCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.RowOpsCorrectness.json)
