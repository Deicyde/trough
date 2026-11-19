---
catalog: module
lean: CompPoly.PolynomialMatrix.muldersStorjohannStep_shape_preserved, CompPoly.PolynomialMatrix.muldersStorjohannStep_rowSpan_subset, CompPoly.PolynomialMatrix.muldersStorjohannStep_rowSpan_superset, CompPoly.PolynomialMatrix.muldersStorjohannStep_wellFormed, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_shape_preserved, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_wellFormed, CompPoly.PolynomialMatrix.muldersStorjohannReduce_wellFormed, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_no_conflict_of_measure_lt, CompPoly.PolynomialMatrix.muldersStorjohannReduce_no_conflict, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_eq_of_no_conflict, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_rowSpan_subset, CompPoly.PolynomialMatrix.muldersStorjohannReduce_rowSpan_subset, CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_rowSpan_superset, CompPoly.PolynomialMatrix.muldersStorjohannReduce_rowSpan_superset, CompPoly.PolynomialMatrix.muldersStorjohannReduce_shape_preserved, CompPoly.PolynomialMatrix.muldersStorjohannReduce_rowSpan_eq, CompPoly.PolynomialMatrix.muldersStorjohannReduce_weakPopov
statement: formalized
proof: formalized
---

# Mulders-Storjohann Correctness Reduction Invariants

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Reduction`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean), by Valerii Huhnin.

> Shape, well-formedness, row-span, and weak-Popov correctness for the reducer.

`CompPoly.PolynomialMatrix.muldersStorjohannStep_shape_preserved` (theorem, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L24))

```lean
theorem muldersStorjohannStep_shape_preserved
    {M : PolynomialMatrix F} (shift : Array Nat) {i j : Nat} (hM : WellFormed M) :
    MatrixShape (muldersStorjohannStep M shift i j) = MatrixShape M
```

`CompPoly.PolynomialMatrix.muldersStorjohannStep_rowSpan_subset` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L47))

```lean
theorem muldersStorjohannStep_rowSpan_subset
    {M : PolynomialMatrix F} (shift : Array Nat) {i j : Nat} (hM : WellFormed M) :
    RowSpan (muldersStorjohannStep M shift i j) ⊆ RowSpan M
```

`CompPoly.PolynomialMatrix.muldersStorjohannStep_rowSpan_superset` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L84))

```lean
theorem muldersStorjohannStep_rowSpan_superset
    {M : PolynomialMatrix F} (shift : Array Nat) {i j : Nat}
    (hM : WellFormed M) (hi : i < M.size) (hj : j < M.size) (hne : i ≠ j) :
    RowSpan M ⊆ RowSpan (muldersStorjohannStep M shift i j)
```

`CompPoly.PolynomialMatrix.muldersStorjohannStep_wellFormed` (theorem, [line 204](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L204))

```lean
theorem muldersStorjohannStep_wellFormed
    {M : PolynomialMatrix F} (shift : Array Nat) {i j : Nat} (hM : WellFormed M) :
    WellFormed (muldersStorjohannStep M shift i j)
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_shape_preserved` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L227))

```lean
theorem muldersStorjohannReduceWithFuel_shape_preserved
    (fuel : Nat) (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    MatrixShape (muldersStorjohannReduceWithFuel fuel M shift) = MatrixShape M
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_wellFormed` (theorem, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L242))

```lean
theorem muldersStorjohannReduceWithFuel_wellFormed
    (fuel : Nat) (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    WellFormed (muldersStorjohannReduceWithFuel fuel M shift)
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_wellFormed` (theorem, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L256))

```lean
theorem muldersStorjohannReduce_wellFormed
    (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    WellFormed (muldersStorjohannReduce M shift)
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_no_conflict_of_measure_lt` (theorem, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L262))

```lean
theorem muldersStorjohannReduceWithFuel_no_conflict_of_measure_lt
    (fuel : Nat) (M : PolynomialMatrix F) (shift : Array Nat)
    (hM : WellFormed M)
    (hfuel : shiftedMatrixMeasure M shift < fuel) :
    shiftedLeadingConflict? (muldersStorjohannReduceWithFuel fuel M shift) shift = none
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_no_conflict` (theorem, [line 285](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L285))

```lean
theorem muldersStorjohannReduce_no_conflict
    (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    shiftedLeadingConflict? (muldersStorjohannReduce M shift) shift = none
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_eq_of_no_conflict` (theorem, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L295))

> The fueled reducer is deterministic: two runs that both end without a
> shifted leading conflict stopped at the same (first conflict-free) matrix of
> the common step orbit, regardless of their fuel.

```lean
theorem muldersStorjohannReduceWithFuel_eq_of_no_conflict :
    ∀ (f g : Nat) (M : PolynomialMatrix F) (shift : Array Nat),
      shiftedLeadingConflict? (muldersStorjohannReduceWithFuel f M shift) shift =
        none →
      shiftedLeadingConflict? (muldersStorjohannReduceWithFuel g M shift) shift =
        none →
      muldersStorjohannReduceWithFuel f M shift =
        muldersStorjohannReduceWithFuel g M shift
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_rowSpan_subset` (theorem, [line 329](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L329))

```lean
theorem muldersStorjohannReduceWithFuel_rowSpan_subset
    (fuel : Nat) (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    RowSpan (muldersStorjohannReduceWithFuel fuel M shift) ⊆ RowSpan M
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_rowSpan_subset` (theorem, [line 347](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L347))

```lean
theorem muldersStorjohannReduce_rowSpan_subset
    (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    RowSpan (muldersStorjohannReduce M shift) ⊆ RowSpan M
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduceWithFuel_rowSpan_superset` (theorem, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L353))

```lean
theorem muldersStorjohannReduceWithFuel_rowSpan_superset
    (fuel : Nat) (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    RowSpan M ⊆ RowSpan (muldersStorjohannReduceWithFuel fuel M shift)
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_rowSpan_superset` (theorem, [line 373](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L373))

```lean
theorem muldersStorjohannReduce_rowSpan_superset
    (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    RowSpan M ⊆ RowSpan (muldersStorjohannReduce M shift)
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_shape_preserved` (theorem, [line 379](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L379))

```lean
theorem muldersStorjohannReduce_shape_preserved
    (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    MatrixShape (muldersStorjohannReduce M shift) = MatrixShape M
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_rowSpan_eq` (theorem, [line 385](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L385))

```lean
theorem muldersStorjohannReduce_rowSpan_eq
    (M : PolynomialMatrix F) (shift : Array Nat) (hM : WellFormed M) :
    RowSpan (muldersStorjohannReduce M shift) = RowSpan M
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_weakPopov` (theorem, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean#L392))

```lean
theorem muldersStorjohannReduce_weakPopov
    (M : PolynomialMatrix F) (shift : Array Nat)
    (hM : WellFormed M) (_hshift : shift.size = MatrixWidth M) :
    ShiftedWeakPopov (muldersStorjohannReduce M shift) shift
```

## Depends on

- [Mulders-Storjohann Correctness Termination Measure Helpers](measure.md)
- [Row Span for Polynomial Matrices](../rowspan.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Reduction.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Reduction.json)
