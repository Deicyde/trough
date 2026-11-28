---
catalog: module
lean: CompPoly.PolynomialMatrix.ShiftedRowReducerContext
statement: formalized
proof: formalized
---

# Shifted Row Reduction Contexts

`CompPoly.LinearAlgebra.PolynomialMatrix.ShiftedReduction`, in [CompPoly/LinearAlgebra/PolynomialMatrix/ShiftedReduction.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/ShiftedReduction.lean), by Valerii Huhnin.

`CompPoly.PolynomialMatrix.ShiftedRowReducerContext` (structure, [line 21](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/ShiftedReduction.lean#L21))

> Executable shifted row-reduction backend over `F[X]`.

```lean
structure ShiftedRowReducerContext
    (F : Type*) [Field F] [BEq F] [LawfulBEq F] [DecidableEq F] where
  reduce : PolynomialMatrix F → Array Nat → PolynomialMatrix F
  shape_preserved :
    ∀ M shift,
      WellFormed M →
        MatrixShape (reduce M shift) = MatrixShape M
  rowSpan_eq :
    ∀ M shift,
      WellFormed M →
        RowSpan (reduce M shift) = RowSpan M
  weakPopov :
    ∀ M shift,
      WellFormed M →
      shift.size = MatrixWidth M →
        ShiftedWeakPopov (reduce M shift) shift
  least_row_minimal :
    ∀ M shift row,
      WellFormed M →
      shift.size = MatrixWidth M →
      row ∈ RowSpan M →
      rowShiftedDegree? row shift ≠ none →
        ∃ outRow outDeg rowDeg,
          outRow ∈ MatrixRows (reduce M shift) ∧
          rowShiftedDegree? outRow shift = some outDeg ∧
          rowShiftedDegree? row shift = some rowDeg ∧
          outDeg ≤ rowDeg
```

## Depends on

- [Row Span for Polynomial Matrices](rowspan.md)
- [Shifted Degrees for Polynomial Rows](shifted.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/ShiftedReduction.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/ShiftedReduction.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.ShiftedReduction.json)
