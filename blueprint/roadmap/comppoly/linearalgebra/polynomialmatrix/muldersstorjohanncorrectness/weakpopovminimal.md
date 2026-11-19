---
catalog: module
lean: CompPoly.PolynomialMatrix.shiftedWeakPopov_least_row_minimal, CompPoly.PolynomialMatrix.muldersStorjohannReduce_least_row_minimal_of_weakPopov
statement: formalized
proof: formalized
---

# Shifted Weak-Popov Least-Row Minimality

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.WeakPopovMinimal`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/WeakPopovMinimal.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/WeakPopovMinimal.lean), by Valerii Huhnin.

> Generalized predictable-degree property: any shifted weak-Popov matrix contains a
> row whose shifted degree is a lower bound for the shifted degree of every row-span
> member. This is the reducer-independent core of
> `muldersStorjohannReduce_least_row_minimal`, stated for an arbitrary well-formed
> shifted weak-Popov matrix and without any alignment hypothesis between the shift
> size and the matrix width.

`CompPoly.PolynomialMatrix.shiftedWeakPopov_least_row_minimal` (theorem, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/WeakPopovMinimal.lean#L38))

> Predictable-degree property of shifted weak-Popov matrices: every row-span
> member with a defined shifted degree is bounded below by the shifted degree of
> some matrix row. Requires neither `shift.size = MatrixWidth B` nor any other
> shift alignment hypothesis.

```lean
theorem shiftedWeakPopov_least_row_minimal
    (B : PolynomialMatrix F) (shift : Array Nat) (row : PolynomialRow F)
    (hB : WellFormed B)
    (hpopov : ShiftedWeakPopov B shift)
    (hrow : row ∈ RowSpan B)
    (hdeg : rowShiftedDegree? row shift ≠ none) :
    ∃ outRow outDeg rowDeg,
      outRow ∈ MatrixRows B ∧
      rowShiftedDegree? outRow shift = some outDeg ∧
      rowShiftedDegree? row shift = some rowDeg ∧
      outDeg ≤ rowDeg
```

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_least_row_minimal_of_weakPopov` (theorem, [line 274](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/WeakPopovMinimal.lean#L274))

> Least-row minimality of the Mulders-Storjohann reducer, re-derived from the
> generalized shifted weak-Popov predictable-degree property.

```lean
theorem muldersStorjohannReduce_least_row_minimal_of_weakPopov
    (M : PolynomialMatrix F) (shift : Array Nat) (row : PolynomialRow F)
    (hM : WellFormed M) (hshift : shift.size = MatrixWidth M)
    (hrow : row ∈ RowSpan M)
    (hdeg : rowShiftedDegree? row shift ≠ none) :
    ∃ outRow outDeg rowDeg,
      outRow ∈ MatrixRows (muldersStorjohannReduce M shift) ∧
      rowShiftedDegree? outRow shift = some outDeg ∧
      rowShiftedDegree? row shift = some rowDeg ∧
      outDeg ≤ rowDeg
```

## Depends on

- [Mulders-Storjohann Shifted Row Reduction](../muldersstorjohann.md)
- [Row Span for Polynomial Matrices](../rowspan.md)

## Proof depends on

- [Mulders-Storjohann Correctness Row Combination Helpers](combinations.md)
- [Mulders-Storjohann Correctness Reduction Invariants](reduction.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/WeakPopovMinimal.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/WeakPopovMinimal.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.WeakPopovMinimal.json)
