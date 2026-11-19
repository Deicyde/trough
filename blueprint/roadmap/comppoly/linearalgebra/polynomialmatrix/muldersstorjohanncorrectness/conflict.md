---
catalog: module
lean: CompPoly.PolynomialMatrix.index_lt_of_rowShiftedDegree?_getElem?_eq_some, CompPoly.PolynomialMatrix.ConflictBounds, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowFold_bounds, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?_bounds, CompPoly.PolynomialMatrix.shiftedLeadingConflictFromFold_bounds, CompPoly.PolynomialMatrix.shiftedLeadingConflictFrom?_bounds, CompPoly.PolynomialMatrix.shiftedLeadingConflict?_some_bounds, CompPoly.PolynomialMatrix.ConflictValid, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowStep?_valid, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowFold_valid, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?_valid, CompPoly.PolynomialMatrix.shiftedLeadingConflictFromFold_valid, CompPoly.PolynomialMatrix.shiftedLeadingConflictFrom?_valid, CompPoly.PolynomialMatrix.shiftedLeadingConflict?_some_valid, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowFold_some, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?_some, CompPoly.PolynomialMatrix.shiftedLeadingConflictFromFold_some, CompPoly.PolynomialMatrix.shiftedLeadingConflictFrom?_some, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowFold_none_no_conflict, CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?_none_no_conflict, CompPoly.PolynomialMatrix.shiftedLeadingConflictFromFold_none_inner_none, CompPoly.PolynomialMatrix.shiftedLeadingConflict?_none_no_conflict, CompPoly.PolynomialMatrix.shiftedLeadingConflict?_none_weakPopov
statement: formalized
proof: formalized
---

# Mulders-Storjohann Correctness Shifted Leading Conflict Helpers

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Conflict`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean), by Valerii Huhnin.

> Bounds and validity lemmas for shifted-leading-position conflict detection.

`CompPoly.PolynomialMatrix.index_lt_of_rowShiftedDegree?_getElem?_eq_some` (theorem, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L25))

```lean
theorem index_lt_of_rowShiftedDegree?_getElem?_eq_some
    {M : PolynomialMatrix F} {shift : Array Nat} {i d : Nat}
    (hdeg : rowShiftedDegree? (M[i]?.getD #[]) shift = some d) :
    i < M.size
```

`CompPoly.PolynomialMatrix.ConflictBounds` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L38))

```lean
def ConflictBounds (M : PolynomialMatrix F) : Option (Nat × Nat) → Prop
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowFold_bounds` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L43))

```lean
theorem shiftedLeadingConflictInRowFold_bounds
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat) (xs : List Nat)
    (found : Option (Nat × Nat))
    (hxs : ∀ j, j ∈ xs → i < j ∧ j < M.size)
    (hfound : ConflictBounds M found) :
    ConflictBounds M
      (xs.foldl
        (fun found j ↦
          match found with
          | some _ => found
          | none =>
              match rowShiftedLeadingPosition? (M.getD i #[]) shift,
                  rowShiftedLeadingPosition? (M.getD j #[]) shift with
              | some pi, some pj =>
                  if pi == pj then some (i, j) else none
              | _, _ => none)
        found)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?_bounds` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L86))

```lean
theorem shiftedLeadingConflictInRow?_bounds
    (M : PolynomialMatrix F) (shift : Array Nat) {i : Nat} {found : Option (Nat × Nat)}
    (hi : i < M.size) (hfound : ConflictBounds M found) :
    ConflictBounds M (shiftedLeadingConflictInRow? M shift i found)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFromFold_bounds` (theorem, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L98))

```lean
theorem shiftedLeadingConflictFromFold_bounds
    (M : PolynomialMatrix F) (shift : Array Nat) (xs : List Nat)
    (found : Option (Nat × Nat))
    (hxs : ∀ i, i ∈ xs → i < M.size)
    (hfound : ConflictBounds M found) :
    ConflictBounds M
      (xs.foldl
        (fun found i ↦ shiftedLeadingConflictInRow? M shift i found)
        found)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFrom?_bounds` (theorem, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L118))

```lean
theorem shiftedLeadingConflictFrom?_bounds
    (M : PolynomialMatrix F) (shift : Array Nat) {found : Option (Nat × Nat)}
    (hfound : ConflictBounds M found) :
    ConflictBounds M (shiftedLeadingConflictFrom? M shift found)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflict?_some_bounds` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L130))

```lean
theorem shiftedLeadingConflict?_some_bounds
    {M : PolynomialMatrix F} {shift : Array Nat} {i j : Nat}
    (hconf : shiftedLeadingConflict? M shift = some (i, j)) :
    i < M.size ∧ j < M.size ∧ i < j
```

`CompPoly.PolynomialMatrix.ConflictValid` (definition, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L140))

```lean
def ConflictValid (M : PolynomialMatrix F) (shift : Array Nat) :
    Option (Nat × Nat) → Prop
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowStep?_valid` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L149))

```lean
theorem shiftedLeadingConflictInRowStep?_valid
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat)
    {found : Option (Nat × Nat)} (j : Nat)
    (hfound : ConflictValid M shift found) :
    ConflictValid M shift (shiftedLeadingConflictInRowStep? M shift i found j)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowFold_valid` (theorem, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L179))

```lean
theorem shiftedLeadingConflictInRowFold_valid
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat)
    (xs : List Nat) {found : Option (Nat × Nat)}
    (hfound : ConflictValid M shift found) :
    ConflictValid M shift
      (xs.foldl (shiftedLeadingConflictInRowStep? M shift i) found)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?_valid` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L193))

```lean
theorem shiftedLeadingConflictInRow?_valid
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat)
    {found : Option (Nat × Nat)}
    (hfound : ConflictValid M shift found) :
    ConflictValid M shift (shiftedLeadingConflictInRow? M shift i found)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFromFold_valid` (theorem, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L202))

```lean
theorem shiftedLeadingConflictFromFold_valid
    (M : PolynomialMatrix F) (shift : Array Nat) (xs : List Nat)
    {found : Option (Nat × Nat)}
    (hfound : ConflictValid M shift found) :
    ConflictValid M shift
      (xs.foldl (shiftedLeadingConflictFromStep? M shift) found)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFrom?_valid` (theorem, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L216))

```lean
theorem shiftedLeadingConflictFrom?_valid
    (M : PolynomialMatrix F) (shift : Array Nat) {found : Option (Nat × Nat)}
    (hfound : ConflictValid M shift found) :
    ConflictValid M shift (shiftedLeadingConflictFrom? M shift found)
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflict?_some_valid` (theorem, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L224))

```lean
theorem shiftedLeadingConflict?_some_valid
    {M : PolynomialMatrix F} {shift : Array Nat} {i j : Nat}
    (hconf : shiftedLeadingConflict? M shift = some (i, j)) :
    ∃ p,
      rowShiftedLeadingPosition? (M.getD i #[]) shift = some p ∧
      rowShiftedLeadingPosition? (M.getD j #[]) shift = some p
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowFold_some` (theorem, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L237))

```lean
theorem shiftedLeadingConflictInRowFold_some
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat)
    (xs : List Nat) (pair : Nat × Nat) :
    xs.foldl (shiftedLeadingConflictInRowStep? M shift i) (some pair) = some pair
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?_some` (theorem, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L248))

```lean
theorem shiftedLeadingConflictInRow?_some
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat) (pair : Nat × Nat) :
    shiftedLeadingConflictInRow? M shift i (some pair) = some pair
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFromFold_some` (theorem, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L255))

```lean
theorem shiftedLeadingConflictFromFold_some
    (M : PolynomialMatrix F) (shift : Array Nat) (xs : List Nat) (pair : Nat × Nat) :
    xs.foldl (shiftedLeadingConflictFromStep? M shift) (some pair) = some pair
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFrom?_some` (theorem, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L265))

```lean
theorem shiftedLeadingConflictFrom?_some
    (M : PolynomialMatrix F) (shift : Array Nat) (pair : Nat × Nat) :
    shiftedLeadingConflictFrom? M shift (some pair) = some pair
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRowFold_none_no_conflict` (theorem, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L272))

```lean
theorem shiftedLeadingConflictInRowFold_none_no_conflict
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat) (xs : List Nat)
    (hfold : xs.foldl (shiftedLeadingConflictInRowStep? M shift i) none = none)
    {j p : Nat} (hj : j ∈ xs)
    (hposI : rowShiftedLeadingPosition? (M.getD i #[]) shift = some p)
    (hposJ : rowShiftedLeadingPosition? (M.getD j #[]) shift = some p) :
    False
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictInRow?_none_no_conflict` (theorem, [line 299](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L299))

```lean
theorem shiftedLeadingConflictInRow?_none_no_conflict
    {M : PolynomialMatrix F} {shift : Array Nat} {i j p : Nat}
    (hfold : shiftedLeadingConflictInRow? M shift i none = none)
    (hij : i < j) (hj : j < M.size)
    (hposI : rowShiftedLeadingPosition? (M.getD i #[]) shift = some p)
    (hposJ : rowShiftedLeadingPosition? (M.getD j #[]) shift = some p) :
    False
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflictFromFold_none_inner_none` (theorem, [line 315](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L315))

```lean
theorem shiftedLeadingConflictFromFold_none_inner_none
    (M : PolynomialMatrix F) (shift : Array Nat) (xs : List Nat)
    (hfold : xs.foldl (shiftedLeadingConflictFromStep? M shift) none = none)
    {i : Nat} (hi : i ∈ xs) :
    shiftedLeadingConflictInRow? M shift i none = none
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflict?_none_no_conflict` (theorem, [line 339](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L339))

```lean
theorem shiftedLeadingConflict?_none_no_conflict
    {M : PolynomialMatrix F} {shift : Array Nat} {i j p : Nat}
    (hconf : shiftedLeadingConflict? M shift = none)
    (hi : i < M.size) (hj : j < M.size) (hij : i < j)
    (hposI : rowShiftedLeadingPosition? (M.getD i #[]) shift = some p)
    (hposJ : rowShiftedLeadingPosition? (M.getD j #[]) shift = some p) :
    False
```

`CompPoly.PolynomialMatrix.shiftedLeadingConflict?_none_weakPopov` (theorem, [line 355](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean#L355))

```lean
theorem shiftedLeadingConflict?_none_weakPopov
    {M : PolynomialMatrix F} {shift : Array Nat}
    (hconf : shiftedLeadingConflict? M shift = none) :
    ShiftedWeakPopov M shift
```

## Depends on

- [Mulders-Storjohann Shifted Row Reduction](../muldersstorjohann.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Conflict.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Conflict.json)
