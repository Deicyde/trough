---
catalog: module
lean: CompPoly.PolynomialMatrix.shiftedRowMeasure, CompPoly.PolynomialMatrix.shiftedMatrixMeasure, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_shiftedRowMeasure_lt, CompPoly.PolynomialMatrix.foldRange_add_eq_of_pointwise, CompPoly.PolynomialMatrix.foldRange_add_lt_of_pointwise_lt, CompPoly.PolynomialMatrix.shiftedMatrixMeasure_replaceRow_lt, CompPoly.PolynomialMatrix.muldersStorjohannStep_shiftedMatrixMeasure_lt, CompPoly.PolynomialMatrix.matrixShiftedDegreeStep?, CompPoly.PolynomialMatrix.matrixShiftedDegreeSpec?, CompPoly.PolynomialMatrix.matrixShiftedDegreeStep?_eq, CompPoly.PolynomialMatrix.matrixShiftedDegree?_eq_spec, CompPoly.PolynomialMatrix.matrixShiftedDegreeSpecFold_acc_le, CompPoly.PolynomialMatrix.matrixShiftedDegreeSpecFold_row_le, CompPoly.PolynomialMatrix.matrixShiftedDegreeSpec?_row_le, CompPoly.PolynomialMatrix.matrixShiftedDegree?_row_le, CompPoly.PolynomialMatrix.matrixShiftedDegreeSpecFold_some_of_acc_some, CompPoly.PolynomialMatrix.matrixShiftedDegreeSpecFold_exists_some_of_row, CompPoly.PolynomialMatrix.matrixShiftedDegree?_row_le_getD, CompPoly.PolynomialMatrix.shiftedRowMeasure_le_of_degree_bound, CompPoly.PolynomialMatrix.shiftedMatrixMeasure_range_le_of_degree_bound, CompPoly.PolynomialMatrix.shiftedMatrixMeasure_le_of_degree_bound, CompPoly.PolynomialMatrix.shiftedMatrixMeasure_lt_muldersStorjohannFuel
statement: formalized
proof: formalized
---

# Mulders-Storjohann Correctness Termination Measure Helpers

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Measure`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean), by Valerii Huhnin.

> Measure-decrease and fuel-bound lemmas for Mulders-Storjohann reduction.

`CompPoly.PolynomialMatrix.shiftedRowMeasure` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L24))

```lean
def shiftedRowMeasure (row : PolynomialRow F) (shift : Array Nat) : Nat
```

`CompPoly.PolynomialMatrix.shiftedMatrixMeasure` (definition, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L29))

```lean
def shiftedMatrixMeasure (M : PolynomialMatrix F) (shift : Array Nat) : Nat
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_shiftedRowMeasure_lt` (theorem, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L34))

```lean
theorem cancelShiftedLeadingTerm_shiftedRowMeasure_lt
    {target reducer : PolynomialRow F} {shift : Array Nat}
    {t r : ShiftedLeadingTerm F}
    (ht : rowShiftedLeadingTerm? target shift = some t)
    (hr : rowShiftedLeadingTerm? reducer shift = some r)
    (hpos : t.position = r.position)
    (hle : r.shiftedDegree ≤ t.shiftedDegree)
    (hsize : reducer.size = target.size) :
    shiftedRowMeasure (cancelShiftedLeadingTerm target reducer shift) shift <
      shiftedRowMeasure target shift
```

`CompPoly.PolynomialMatrix.foldRange_add_eq_of_pointwise` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L113))

```lean
theorem foldRange_add_eq_of_pointwise
    (n : Nat) {f g : Nat → Nat}
    (heq : ∀ k, k < n → f k = g k) :
    (List.range n).foldl (fun acc k ↦ acc + f k) 0 =
      (List.range n).foldl (fun acc k ↦ acc + g k) 0
```

`CompPoly.PolynomialMatrix.foldRange_add_lt_of_pointwise_lt` (theorem, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L126))

```lean
theorem foldRange_add_lt_of_pointwise_lt
    (n : Nat) {f g : Nat → Nat} {idx : Nat}
    (hidx : idx < n)
    (hlt : f idx < g idx)
    (heq : ∀ k, k < n → k ≠ idx → f k = g k) :
    (List.range n).foldl (fun acc k ↦ acc + f k) 0 <
      (List.range n).foldl (fun acc k ↦ acc + g k) 0
```

`CompPoly.PolynomialMatrix.shiftedMatrixMeasure_replaceRow_lt` (theorem, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L161))

```lean
theorem shiftedMatrixMeasure_replaceRow_lt
    {M : PolynomialMatrix F} {shift : Array Nat} {idx : Nat} {newRow : PolynomialRow F}
    (hidx : idx < M.size)
    (hlt : shiftedRowMeasure newRow shift <
      shiftedRowMeasure (M.getD idx #[]) shift) :
    shiftedMatrixMeasure (replaceRow M idx newRow) shift <
      shiftedMatrixMeasure M shift
```

`CompPoly.PolynomialMatrix.muldersStorjohannStep_shiftedMatrixMeasure_lt` (theorem, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L184))

```lean
theorem muldersStorjohannStep_shiftedMatrixMeasure_lt
    {M : PolynomialMatrix F} {shift : Array Nat} {i j : Nat}
    (hM : WellFormed M)
    (hconf : shiftedLeadingConflict? M shift = some (i, j)) :
    shiftedMatrixMeasure (muldersStorjohannStep M shift i j) shift <
      shiftedMatrixMeasure M shift
```

`CompPoly.PolynomialMatrix.matrixShiftedDegreeStep?` (definition, [line 236](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L236))

```lean
def matrixShiftedDegreeStep?
    (M : PolynomialMatrix F) (shift : Array Nat)
    (acc : Option Nat) (i : Nat) : Option Nat
```

`CompPoly.PolynomialMatrix.matrixShiftedDegreeSpec?` (definition, [line 243](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L243))

```lean
def matrixShiftedDegreeSpec? (M : PolynomialMatrix F) (shift : Array Nat) :
    Option Nat
```

`CompPoly.PolynomialMatrix.matrixShiftedDegreeStep?_eq` (theorem, [line 250](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L250))

```lean
theorem matrixShiftedDegreeStep?_eq
    (M : PolynomialMatrix F) (shift : Array Nat) :
    matrixShiftedDegreeStep? M shift =
    (fun acc i ↦
      match rowShiftedDegree? (M.getD i #[]) shift with
      | none => acc
      | some d => maxOption acc d)
```

`CompPoly.PolynomialMatrix.matrixShiftedDegree?_eq_spec` (theorem, [line 260](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L260))

```lean
theorem matrixShiftedDegree?_eq_spec
    (M : PolynomialMatrix F) (shift : Array Nat) :
    matrixShiftedDegree? M shift = matrixShiftedDegreeSpec? M shift
```

`CompPoly.PolynomialMatrix.matrixShiftedDegreeSpecFold_acc_le` (theorem, [line 268](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L268))

```lean
theorem matrixShiftedDegreeSpecFold_acc_le
    {M : PolynomialMatrix F} {shift : Array Nat}
    (xs : List Nat) {acc : Option Nat} {a D : Nat}
    (hacc : acc = some a)
    (hfold : xs.foldl (matrixShiftedDegreeStep? M shift) acc = some D) :
    a ≤ D
```

`CompPoly.PolynomialMatrix.matrixShiftedDegreeSpecFold_row_le` (theorem, [line 303](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L303))

```lean
theorem matrixShiftedDegreeSpecFold_row_le
    {M : PolynomialMatrix F} {shift : Array Nat}
    (xs : List Nat) {acc : Option Nat} {D i rowDeg : Nat}
    (hfold : xs.foldl (matrixShiftedDegreeStep? M shift) acc = some D)
    (hi : i ∈ xs)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some rowDeg) :
    rowDeg ≤ D
```

`CompPoly.PolynomialMatrix.matrixShiftedDegreeSpec?_row_le` (theorem, [line 341](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L341))

```lean
theorem matrixShiftedDegreeSpec?_row_le
    {M : PolynomialMatrix F} {shift : Array Nat} {D i rowDeg : Nat}
    (hmat : matrixShiftedDegreeSpec? M shift = some D)
    (hi : i < M.size)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some rowDeg) :
    rowDeg ≤ D
```

`CompPoly.PolynomialMatrix.matrixShiftedDegree?_row_le` (theorem, [line 352](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L352))

```lean
theorem matrixShiftedDegree?_row_le
    {M : PolynomialMatrix F} {shift : Array Nat} {D i rowDeg : Nat}
    (hmat : matrixShiftedDegree? M shift = some D)
    (hi : i < M.size)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some rowDeg) :
    rowDeg ≤ D
```

`CompPoly.PolynomialMatrix.matrixShiftedDegreeSpecFold_some_of_acc_some` (theorem, [line 362](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L362))

```lean
theorem matrixShiftedDegreeSpecFold_some_of_acc_some
    {M : PolynomialMatrix F} {shift : Array Nat}
    (xs : List Nat) {acc : Option Nat} {a : Nat}
    (hacc : acc = some a) :
    ∃ D, xs.foldl (matrixShiftedDegreeStep? M shift) acc = some D
```

`CompPoly.PolynomialMatrix.matrixShiftedDegreeSpecFold_exists_some_of_row` (theorem, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L392))

```lean
theorem matrixShiftedDegreeSpecFold_exists_some_of_row
    {M : PolynomialMatrix F} {shift : Array Nat}
    (xs : List Nat) {i rowDeg : Nat}
    (hi : i ∈ xs)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some rowDeg) :
    ∃ D, xs.foldl (matrixShiftedDegreeStep? M shift) none = some D
```

`CompPoly.PolynomialMatrix.matrixShiftedDegree?_row_le_getD` (theorem, [line 423](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L423))

```lean
theorem matrixShiftedDegree?_row_le_getD
    {M : PolynomialMatrix F} {shift : Array Nat} {i rowDeg : Nat}
    (hi : i < M.size)
    (hdeg : rowShiftedDegree? (M.getD i #[]) shift = some rowDeg) :
    rowDeg ≤ (matrixShiftedDegree? M shift).getD 0
```

`CompPoly.PolynomialMatrix.shiftedRowMeasure_le_of_degree_bound` (theorem, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L441))

```lean
theorem shiftedRowMeasure_le_of_degree_bound
    {row : PolynomialRow F} {shift : Array Nat} {d : Nat}
    (hbound : ∀ rowDeg, rowShiftedDegree? row shift = some rowDeg → rowDeg ≤ d) :
    shiftedRowMeasure row shift ≤ (d + 1) * (row.size + 1)
```

`CompPoly.PolynomialMatrix.shiftedMatrixMeasure_range_le_of_degree_bound` (theorem, [line 460](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L460))

```lean
theorem shiftedMatrixMeasure_range_le_of_degree_bound
    {M : PolynomialMatrix F} {shift : Array Nat} {d : Nat}
    (hM : WellFormed M)
    (hbound : ∀ i rowDeg, i < M.size →
      rowShiftedDegree? (M.getD i #[]) shift = some rowDeg → rowDeg ≤ d) :
    ∀ n, n ≤ M.size →
      (List.range n).foldl
        (fun acc i ↦ acc + shiftedRowMeasure (M.getD i #[]) shift)
        0 ≤ n * ((d + 1) * (MatrixWidth M + 1))
```

`CompPoly.PolynomialMatrix.shiftedMatrixMeasure_le_of_degree_bound` (theorem, [line 492](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L492))

```lean
theorem shiftedMatrixMeasure_le_of_degree_bound
    {M : PolynomialMatrix F} {shift : Array Nat} {d : Nat}
    (hM : WellFormed M)
    (hbound : ∀ i rowDeg, i < M.size →
      rowShiftedDegree? (M.getD i #[]) shift = some rowDeg → rowDeg ≤ d) :
    shiftedMatrixMeasure M shift ≤
      M.size * ((d + 1) * (MatrixWidth M + 1))
```

`CompPoly.PolynomialMatrix.shiftedMatrixMeasure_lt_muldersStorjohannFuel` (theorem, [line 503](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean#L503))

```lean
theorem shiftedMatrixMeasure_lt_muldersStorjohannFuel
    {M : PolynomialMatrix F} {shift : Array Nat}
    (hM : WellFormed M) :
    shiftedMatrixMeasure M shift < muldersStorjohannFuel M shift
```

## Depends on

- [Mulders-Storjohann Shifted Row Reduction](../muldersstorjohann.md)

## Proof depends on

- [Mulders-Storjohann Correctness Shifted Leading Conflict Helpers](conflict.md)
- [Mulders-Storjohann Correctness Shifted Leading Term Helpers](leading.md)
- [Mulders-Storjohann Correctness Matrix Row Helpers](matrixrows.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Measure.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Measure.json)
