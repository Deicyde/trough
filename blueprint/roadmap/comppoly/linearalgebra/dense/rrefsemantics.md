---
catalog: module
lean: CompPoly.DenseMatrix.findPivotRowStep, CompPoly.DenseMatrix.list_forIn_yield_eq_foldl, CompPoly.DenseMatrix.findPivotRowStep_fold_some, CompPoly.DenseMatrix.list_forIn_findPivotRowStep_eq_foldl, CompPoly.DenseMatrix.findPivotRow_fold_mem, CompPoly.DenseMatrix.findPivotRow_fold_get_ne_zero, CompPoly.DenseMatrix.findPivotRow_fold_none_get_eq_zero, CompPoly.DenseMatrix.findPivotRow_eq_fold, CompPoly.DenseMatrix.findPivotRow_some_lt, CompPoly.DenseMatrix.findPivotRow_some_ge, CompPoly.DenseMatrix.findPivotRow_some_ne_zero, CompPoly.DenseMatrix.findPivotRow_none_get_eq_zero, CompPoly.DenseMatrix.list_forIn_addScaledRow_wf, CompPoly.DenseMatrix.normalizeAndEliminate_wf, CompPoly.DenseMatrix.list_forIn_addScaledRow_solution_of_solution, CompPoly.DenseMatrix.list_forIn_addScaledRow_solution_reflect, CompPoly.DenseMatrix.isHomogeneousSolution_normalizeAndEliminate_of_solution, CompPoly.DenseMatrix.isHomogeneousSolution_of_normalizeAndEliminate_solution, CompPoly.DenseMatrix.rrefLoop_cols, CompPoly.DenseMatrix.rrefLoop_rows, CompPoly.DenseMatrix.rref_cols, CompPoly.DenseMatrix.rref_rows, CompPoly.DenseMatrix.rrefLoop_wf, CompPoly.DenseMatrix.rref_wf, CompPoly.DenseMatrix.isHomogeneousSolution_rrefLoop_of_solution, CompPoly.DenseMatrix.isHomogeneousSolution_rref, CompPoly.DenseMatrix.isHomogeneousSolution_of_rrefLoop_solution, CompPoly.DenseMatrix.isHomogeneousSolution_of_rref
statement: formalized
proof: formalized
---

# Dense RREF Semantic Correctness

`CompPoly.LinearAlgebra.Dense.RrefSemantics`, in [CompPoly/LinearAlgebra/Dense/RrefSemantics.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean), by Valerii Huhnin.

> Semantic preservation and reflection lemmas for dense row reduction.

`CompPoly.DenseMatrix.findPivotRowStep` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L25))

```lean
def findPivotRowStep [Zero F] [BEq F] (M : DenseMatrix F) (col : Nat)
    (out : Option Nat) (row : Nat) : Option Nat
```

`CompPoly.DenseMatrix.list_forIn_yield_eq_foldl` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L29))

```lean
theorem list_forIn_yield_eq_foldl {α β : Type*}
    (xs : List α) (init : β) (f : β → α → β) :
    (Id.run (forIn xs init fun x acc ↦ pure (ForInStep.yield (f acc x))) : β) =
      xs.foldl f init
```

`CompPoly.DenseMatrix.findPivotRowStep_fold_some` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L39))

```lean
theorem findPivotRowStep_fold_some [Zero F] [BEq F]
    (M : DenseMatrix F) (col : Nat) (xs : List Nat) (pivot : Nat) :
    xs.foldl (findPivotRowStep M col) (some pivot) = some pivot
```

`CompPoly.DenseMatrix.list_forIn_findPivotRowStep_eq_foldl` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L47))

```lean
theorem list_forIn_findPivotRowStep_eq_foldl [Zero F] [BEq F]
    (M : DenseMatrix F) (col : Nat) (xs : List Nat) (out : Option Nat) :
    (Id.run (forIn xs out fun row out ↦
      if out = none ∧ (M.get row col == 0) = false then
        pure (ForInStep.yield (some row))
      else
        pure (ForInStep.yield out)) : Option Nat) =
      xs.foldl (findPivotRowStep M col) out
```

`CompPoly.DenseMatrix.findPivotRow_fold_mem` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L76))

```lean
theorem findPivotRow_fold_mem [Zero F] [BEq F]
    (M : DenseMatrix F) (col : Nat) {xs : List Nat} {pivot : Nat}
    (h : xs.foldl (findPivotRowStep M col) none = some pivot) :
    pivot ∈ xs
```

`CompPoly.DenseMatrix.findPivotRow_fold_get_ne_zero` (theorem, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L98))

```lean
theorem findPivotRow_fold_get_ne_zero [Zero F] [BEq F]
    (M : DenseMatrix F) (col : Nat) {xs : List Nat} {pivot : Nat}
    (h : xs.foldl (findPivotRowStep M col) none = some pivot) :
    (M.get pivot col == 0) = false
```

`CompPoly.DenseMatrix.findPivotRow_fold_none_get_eq_zero` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L120))

```lean
theorem findPivotRow_fold_none_get_eq_zero [Zero F] [BEq F] [LawfulBEq F]
    (M : DenseMatrix F) (col : Nat) {xs : List Nat}
    (h : xs.foldl (findPivotRowStep M col) none = none) {row : Nat}
    (hrow : row ∈ xs) :
    M.get row col = 0
```

`CompPoly.DenseMatrix.findPivotRow_eq_fold` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L149))

```lean
theorem findPivotRow_eq_fold [Zero F] [BEq F]
    (M : DenseMatrix F) (start col : Nat) :
    findPivotRow M start col =
      (List.range' start (M.rows - start)).foldl (findPivotRowStep M col) none
```

`CompPoly.DenseMatrix.findPivotRow_some_lt` (theorem, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L156))

```lean
theorem findPivotRow_some_lt [Zero F] [BEq F]
    {M : DenseMatrix F} {start col pivot : Nat}
    (h : findPivotRow M start col = some pivot) :
    pivot < M.rows
```

`CompPoly.DenseMatrix.findPivotRow_some_ge` (theorem, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L165))

```lean
theorem findPivotRow_some_ge [Zero F] [BEq F]
    {M : DenseMatrix F} {start col pivot : Nat}
    (h : findPivotRow M start col = some pivot) :
    start ≤ pivot
```

`CompPoly.DenseMatrix.findPivotRow_some_ne_zero` (theorem, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L174))

```lean
theorem findPivotRow_some_ne_zero [Zero F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} {start col pivot : Nat}
    (h : findPivotRow M start col = some pivot) :
    M.get pivot col ≠ 0
```

`CompPoly.DenseMatrix.findPivotRow_none_get_eq_zero` (theorem, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L183))

```lean
theorem findPivotRow_none_get_eq_zero [Zero F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} {start col row : Nat}
    (h : findPivotRow M start col = none) (hstart : start ≤ row) (hrow : row < M.rows) :
    M.get row col = 0
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_wf` (theorem, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L191))

```lean
theorem list_forIn_addScaledRow_wf [Field F]
    (rows : List Nat) {out : DenseMatrix F} (pivotRow pivotCol : Nat)
    (hout : WellFormed out) :
    WellFormed
      (Id.run (forIn rows out fun row r ↦
        if row = pivotRow then
          pure (ForInStep.yield r)
        else
          pure (ForInStep.yield
            (addScaledRow r row pivotRow (-(r.get row pivotCol)))) :
        Id (DenseMatrix F)))
```

`CompPoly.DenseMatrix.normalizeAndEliminate_wf` (theorem, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L214))

```lean
theorem normalizeAndEliminate_wf [Field F] [BEq F]
    {M : DenseMatrix F} (hM : WellFormed M) (pivotRow pivotCol : Nat) :
    WellFormed (normalizeAndEliminate M pivotRow pivotCol)
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_solution_of_solution` (theorem, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L231))

```lean
theorem list_forIn_addScaledRow_solution_of_solution [Field F]
    (rows : List Nat) {out : DenseMatrix F} {v : Array F}
    (pivotRow pivotCol : Nat) (hpivot : pivotRow < out.rows)
    (hout : WellFormed out) (hsol : IsHomogeneousSolution out v) :
    IsHomogeneousSolution
      (Id.run (forIn rows out fun row r ↦
        if row = pivotRow then
          pure (ForInStep.yield r)
        else
          pure (ForInStep.yield
            (addScaledRow r row pivotRow (-(r.get row pivotCol)))) :
        Id (DenseMatrix F))) v
```

`CompPoly.DenseMatrix.list_forIn_addScaledRow_solution_reflect` (theorem, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L276))

```lean
theorem list_forIn_addScaledRow_solution_reflect [Field F]
    (rows : List Nat) {out : DenseMatrix F} {v : Array F}
    (pivotRow pivotCol : Nat) (hpivot : pivotRow < out.rows)
    (hout : WellFormed out)
    (hsol :
      IsHomogeneousSolution
        (Id.run (forIn rows out fun row r ↦
          if row = pivotRow then
            pure (ForInStep.yield r)
          else
            pure (ForInStep.yield
              (addScaledRow r row pivotRow (-(r.get row pivotCol)))) :
          Id (DenseMatrix F))) v) :
    IsHomogeneousSolution out v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_normalizeAndEliminate_of_solution` (theorem, [line 323](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L323))

```lean
theorem isHomogeneousSolution_normalizeAndEliminate_of_solution
    [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} {v : Array F} (hM : WellFormed M)
    {pivotRow pivotCol : Nat} (hpivotRow : pivotRow < M.rows)
    (hsol : IsHomogeneousSolution M v) :
    IsHomogeneousSolution (normalizeAndEliminate M pivotRow pivotCol) v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_of_normalizeAndEliminate_solution` (theorem, [line 349](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L349))

```lean
theorem isHomogeneousSolution_of_normalizeAndEliminate_solution
    [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} {v : Array F} (hM : WellFormed M)
    {pivotRow pivotCol : Nat} (hpivotRow : pivotRow < M.rows)
    (hpivot : M.get pivotRow pivotCol ≠ 0)
    (hsol : IsHomogeneousSolution (normalizeAndEliminate M pivotRow pivotCol) v) :
    IsHomogeneousSolution M v
```

`CompPoly.DenseMatrix.rrefLoop_cols` (theorem, [line 378](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L378))

```lean
theorem rrefLoop_cols [Field F] [BEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots,
      ((rrefLoop fuel col row M pivots).matrix).cols = M.cols
```

`CompPoly.DenseMatrix.rrefLoop_rows` (theorem, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L402))

```lean
theorem rrefLoop_rows [Field F] [BEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots,
      ((rrefLoop fuel col row M pivots).matrix).rows = M.rows
```

`CompPoly.DenseMatrix.rref_cols` (theorem, [line 426](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L426))

```lean
theorem rref_cols [Field F] [BEq F]
    (M : DenseMatrix F) : (rref M).matrix.cols = M.cols
```

`CompPoly.DenseMatrix.rref_rows` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L431))

```lean
theorem rref_rows [Field F] [BEq F]
    (M : DenseMatrix F) : (rref M).matrix.rows = M.rows
```

`CompPoly.DenseMatrix.rrefLoop_wf` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L436))

```lean
theorem rrefLoop_wf [Field F] [BEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots,
      WellFormed M → WellFormed (rrefLoop fuel col row M pivots).matrix
```

`CompPoly.DenseMatrix.rref_wf` (theorem, [line 463](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L463))

```lean
theorem rref_wf [Field F] [BEq F] {M : DenseMatrix F}
    (hM : WellFormed M) : WellFormed (rref M).matrix
```

`CompPoly.DenseMatrix.isHomogeneousSolution_rrefLoop_of_solution` (theorem, [line 468](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L468))

```lean
theorem isHomogeneousSolution_rrefLoop_of_solution
    [Field F] [BEq F] [LawfulBEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots {v : Array F},
      WellFormed M →
        IsHomogeneousSolution M v →
          IsHomogeneousSolution (rrefLoop fuel col row M pivots).matrix v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_rref` (theorem, [line 510](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L510))

```lean
theorem isHomogeneousSolution_rref [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {v : Array F}
    (hsol : IsHomogeneousSolution M v) :
    IsHomogeneousSolution (rref M).matrix v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_of_rrefLoop_solution` (theorem, [line 517](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L517))

```lean
theorem isHomogeneousSolution_of_rrefLoop_solution
    [Field F] [BEq F] [LawfulBEq F] :
    ∀ fuel col row (M : DenseMatrix F) pivots {v : Array F},
      WellFormed M →
        IsHomogeneousSolution (rrefLoop fuel col row M pivots).matrix v →
          IsHomogeneousSolution M v
```

`CompPoly.DenseMatrix.isHomogeneousSolution_of_rref` (theorem, [line 562](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean#L562))

```lean
theorem isHomogeneousSolution_of_rref [Field F] [BEq F] [LawfulBEq F]
    {M : DenseMatrix F} (hM : WellFormed M) {v : Array F}
    (hsol : IsHomogeneousSolution (rref M).matrix v) :
    IsHomogeneousSolution M v
```

## Depends on

- [Dense Row Operations](rowops.md)

## Proof depends on

- [Dense Row-Operation Correctness](rowopscorrectness.md)

## Sources

- [CompPoly/LinearAlgebra/Dense/RrefSemantics.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/Dense/RrefSemantics.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.Dense.RrefSemantics.json)
