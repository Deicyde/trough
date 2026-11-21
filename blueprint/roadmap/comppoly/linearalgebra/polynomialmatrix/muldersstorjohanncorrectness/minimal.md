---
catalog: module
lean: CompPoly.PolynomialMatrix.muldersStorjohannReduce_least_row_minimal, CompPoly.PolynomialMatrix.muldersStorjohannReducerContext
statement: formalized
proof: formalized
---

# Mulders-Storjohann Correctness Reducer Minimality

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Minimal`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Minimal.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Minimal.lean), by Valerii Huhnin.

> Least-row minimality and the certified reducer context.

`CompPoly.PolynomialMatrix.muldersStorjohannReduce_least_row_minimal` (theorem, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Minimal.lean#L24))

```lean
theorem muldersStorjohannReduce_least_row_minimal
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

`CompPoly.PolynomialMatrix.muldersStorjohannReducerContext` (definition, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Minimal.lean#L266))

> Certified direct Mulders-Storjohann shifted row-reducer context.

```lean
def muldersStorjohannReducerContext (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    [DecidableEq F] : ShiftedRowReducerContext F
```

## Depends on

- [Mulders-Storjohann Shifted Row Reduction](../muldersstorjohann.md)
- [Shifted Row Reduction Contexts](../shiftedreduction.md)

## Proof depends on

- [Mulders-Storjohann Correctness Row Combination Helpers](combinations.md)
- [Mulders-Storjohann Correctness Reduction Invariants](reduction.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Minimal.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Minimal.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Minimal.json)
