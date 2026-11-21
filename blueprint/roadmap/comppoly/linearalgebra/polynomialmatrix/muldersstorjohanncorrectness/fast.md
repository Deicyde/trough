---
catalog: module
lean: CompPoly.PolynomialMatrix.rowSubScaledShift_size, CompPoly.PolynomialMatrix.rowGet_rowSubScaledShift, CompPoly.PolynomialMatrix.rowSubScaledShift_eq, CompPoly.PolynomialMatrix.cancelShiftedLeadingTermFast_eq, CompPoly.PolynomialMatrix.rowLeadingPositions_size, CompPoly.PolynomialMatrix.rowLeadingPositions_getD, CompPoly.PolynomialMatrix.cachedLeadingConflictInRowStep?_eq, CompPoly.PolynomialMatrix.cachedLeadingConflictInRow?_eq, CompPoly.PolynomialMatrix.cachedLeadingConflict?_eq, CompPoly.PolynomialMatrix.muldersStorjohannStepFast_eq, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuelFast_eq, CompPoly.PolynomialMatrix.muldersStorjohannReduceFast_eq, CompPoly.PolynomialMatrix.muldersStorjohannFastReducerContext
statement: formalized
proof: formalized
---

# Fast Mulders-Storjohann Reduction Agrees With the Direct Definition

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Fast`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean), by Valerii Huhnin.

> The fast reducer caches shifted leading positions once per conflict scan and
> cancels leading terms through the fused `rowSubScaledShift` update. This file
> proves it extensionally equal to `muldersStorjohannReduce`, so every
> correctness result transfers, and packages it as a certified
> `ShiftedRowReducerContext`.

> ### Row-level cancellation

`CompPoly.PolynomialMatrix.rowSubScaledShift_size` (theorem, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L31))

```lean
theorem rowSubScaledShift_size (a : PolynomialRow F) (c : F) (d : Nat)
    (b : PolynomialRow F) :
    (rowSubScaledShift a c d b).size = max a.size b.size
```

`CompPoly.PolynomialMatrix.rowGet_rowSubScaledShift` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L36))

```lean
theorem rowGet_rowSubScaledShift (a : PolynomialRow F) (c : F) (d : Nat)
    (b : PolynomialRow F) (j : Nat) :
    rowGet (rowSubScaledShift a c d b) j =
      CPolynomial.subMulMonomial (rowGet a j) c d (rowGet b j)
```

`CompPoly.PolynomialMatrix.rowSubScaledShift_eq` (theorem, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L54))

```lean
theorem rowSubScaledShift_eq (a : PolynomialRow F) (c : F) (d : Nat)
    (b : PolynomialRow F) :
    rowSubScaledShift a c d b = rowSub a (rowScaleMonomial c d b)
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTermFast_eq` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L71))

```lean
theorem cancelShiftedLeadingTermFast_eq (target reducer : PolynomialRow F)
    (shift : Array Nat) :
    cancelShiftedLeadingTermFast target reducer shift =
      cancelShiftedLeadingTerm target reducer shift
```

> ### Cached conflict scan

`CompPoly.PolynomialMatrix.rowLeadingPositions_size` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L81))

```lean
theorem rowLeadingPositions_size (M : PolynomialMatrix F)
    (shift : Array Nat) :
    (rowLeadingPositions M shift).size = M.size
```

`CompPoly.PolynomialMatrix.rowLeadingPositions_getD` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L87))

```lean
theorem rowLeadingPositions_getD (M : PolynomialMatrix F) (shift : Array Nat)
    {i : Nat} (hi : i < M.size) :
    (rowLeadingPositions M shift).getD i none =
      rowShiftedLeadingPosition? (M.getD i #[]) shift
```

`CompPoly.PolynomialMatrix.cachedLeadingConflictInRowStep?_eq` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L100))

```lean
theorem cachedLeadingConflictInRowStep?_eq (M : PolynomialMatrix F)
    (shift : Array Nat) {i j : Nat} (hi : i < M.size) (hj : j < M.size)
    (found : Option (Nat × Nat)) :
    cachedLeadingConflictInRowStep? (rowLeadingPositions M shift) i found j =
      shiftedLeadingConflictInRowStep? M shift i found j
```

`CompPoly.PolynomialMatrix.cachedLeadingConflictInRow?_eq` (theorem, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L109))

```lean
theorem cachedLeadingConflictInRow?_eq (M : PolynomialMatrix F)
    (shift : Array Nat) {i : Nat} (hi : i < M.size)
    (found : Option (Nat × Nat)) :
    cachedLeadingConflictInRow? (rowLeadingPositions M shift) i found =
      shiftedLeadingConflictInRow? M shift i found
```

`CompPoly.PolynomialMatrix.cachedLeadingConflict?_eq` (theorem, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L124))

```lean
theorem cachedLeadingConflict?_eq (M : PolynomialMatrix F) (shift : Array Nat) :
    cachedLeadingConflict? (rowLeadingPositions M shift) =
      shiftedLeadingConflict? M shift
```

> ### Step, loop, and reducer

`CompPoly.PolynomialMatrix.muldersStorjohannStepFast_eq` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L139))

```lean
theorem muldersStorjohannStepFast_eq (M : PolynomialMatrix F)
    (shift : Array Nat) (i j : Nat) :
    muldersStorjohannStepFast M shift i j = muldersStorjohannStep M shift i j
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuelFast_eq` (theorem, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L145))

```lean
theorem muldersStorjohannReduceWithFuelFast_eq :
    ∀ (fuel : Nat) (M : PolynomialMatrix F) (shift : Array Nat),
      muldersStorjohannReduceWithFuelFast fuel M shift =
        muldersStorjohannReduceWithFuel fuel M shift
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceFast_eq` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L163))

```lean
theorem muldersStorjohannReduceFast_eq (M : PolynomialMatrix F)
    (shift : Array Nat) :
    muldersStorjohannReduceFast M shift = muldersStorjohannReduce M shift
```

> ### Certified context

`CompPoly.PolynomialMatrix.muldersStorjohannFastReducerContext` (definition, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean#L174))

> Certified fast Mulders-Storjohann shifted row-reducer context. The
> implementation caches leading positions per scan and uses fused row
> cancellation; correctness transfers along `muldersStorjohannReduceFast_eq`.

```lean
def muldersStorjohannFastReducerContext (F : Type*) [Field F] [BEq F]
    [LawfulBEq F] [DecidableEq F] : ShiftedRowReducerContext F
```

## Depends on

- [Mulders-Storjohann Shifted Row Reduction](../muldersstorjohann.md)
- [Shifted Row Reduction Contexts](../shiftedreduction.md)

## Proof depends on

- [Mulders-Storjohann Correctness Reducer Minimality](minimal.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Fast.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Fast.json)
