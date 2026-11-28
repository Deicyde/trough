---
catalog: module
lean: CompPoly.PolynomialMatrix.rowLinearCombination_range_size, CompPoly.PolynomialMatrix.rowLinearCombination_size, CompPoly.PolynomialMatrix.rowCombinationTermSupport, CompPoly.PolynomialMatrix.rowCombinationTermDegree, CompPoly.PolynomialMatrix.rowCombinationTermPosition, CompPoly.PolynomialMatrix.rowGet_rowLinearCombination_range_coeff, CompPoly.PolynomialMatrix.rowGet_rowLinearCombination_coeff, CompPoly.PolynomialMatrix.rowLinearCombination_range_eq_zeroRow_of_forall_zero_or_row_zero, CompPoly.PolynomialMatrix.rowLinearCombination_eq_zeroRow_of_forall_zero_or_row_zero, CompPoly.PolynomialMatrix.rowCombinationTermSupport_nonempty_of_combination_degree_some
statement: formalized
proof: formalized
---

# Mulders-Storjohann Correctness Row Combination Helpers

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Combinations`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean), by Valerii Huhnin.

> Row-linear-combination size, coefficient, and support lemmas.

`CompPoly.PolynomialMatrix.rowLinearCombination_range_size` (theorem, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L25))

```lean
theorem rowLinearCombination_range_size
    {M : PolynomialMatrix F} (hM : WellFormed M) (coeffs : Array (CPolynomial F)) :
    ∀ n, n ≤ M.size →
      ((List.range n).foldl
          (fun acc i ↦
            rowAdd acc
              (rowScalePolynomial (coeffs.getD i 0) (M.getD i #[])))
          (zeroRow (MatrixWidth M))).size = MatrixWidth M
```

`CompPoly.PolynomialMatrix.rowLinearCombination_size` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L47))

```lean
theorem rowLinearCombination_size
    {M : PolynomialMatrix F} (hM : WellFormed M) (coeffs : Array (CPolynomial F)) :
    (rowLinearCombination coeffs M).size = MatrixWidth M
```

`CompPoly.PolynomialMatrix.rowCombinationTermSupport` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L53))

```lean
def rowCombinationTermSupport
    (coeffs : Array (CPolynomial F)) (M : PolynomialMatrix F) (shift : Array Nat) :
    Finset Nat
```

`CompPoly.PolynomialMatrix.rowCombinationTermDegree` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L60))

```lean
def rowCombinationTermDegree
    (coeffs : Array (CPolynomial F)) (M : PolynomialMatrix F) (shift : Array Nat)
    (i : Nat) : Nat
```

`CompPoly.PolynomialMatrix.rowCombinationTermPosition` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L67))

```lean
def rowCombinationTermPosition
    (M : PolynomialMatrix F) (shift : Array Nat) (i : Nat) : Nat
```

`CompPoly.PolynomialMatrix.rowGet_rowLinearCombination_range_coeff` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L72))

```lean
theorem rowGet_rowLinearCombination_range_coeff
    {M : PolynomialMatrix F} (coeffs : Array (CPolynomial F))
    (j k : Nat) :
    ∀ n,
      (rowGet
        ((List.range n).foldl
          (fun acc i ↦
            rowAdd acc
              (rowScalePolynomial (coeffs.getD i 0) (M.getD i #[])))
          (zeroRow (MatrixWidth M))) j).coeff k =
        ∑ i ∈ Finset.range n,
          ((coeffs.getD i 0) * rowGet (M.getD i #[]) j).coeff k
```

`CompPoly.PolynomialMatrix.rowGet_rowLinearCombination_coeff` (theorem, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L97))

```lean
theorem rowGet_rowLinearCombination_coeff
    {M : PolynomialMatrix F} (coeffs : Array (CPolynomial F))
    (j k : Nat) :
    (rowGet (rowLinearCombination coeffs M) j).coeff k =
      ∑ i ∈ Finset.range M.size,
        ((coeffs.getD i 0) * rowGet (M.getD i #[]) j).coeff k
```

`CompPoly.PolynomialMatrix.rowLinearCombination_range_eq_zeroRow_of_forall_zero_or_row_zero` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L107))

```lean
theorem rowLinearCombination_range_eq_zeroRow_of_forall_zero_or_row_zero
    {M : PolynomialMatrix F} (hM : WellFormed M)
    (coeffs : Array (CPolynomial F))
    (hzero : ∀ i, i < M.size →
      coeffs.getD i 0 = 0 ∨ RowIsZero (M.getD i #[])) :
    ∀ n, n ≤ M.size →
      (List.range n).foldl
          (fun acc i ↦
            rowAdd acc
              (rowScalePolynomial (coeffs.getD i 0) (M.getD i #[])))
          (zeroRow (MatrixWidth M)) =
        zeroRow (MatrixWidth M)
```

`CompPoly.PolynomialMatrix.rowLinearCombination_eq_zeroRow_of_forall_zero_or_row_zero` (theorem, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L140))

```lean
theorem rowLinearCombination_eq_zeroRow_of_forall_zero_or_row_zero
    {M : PolynomialMatrix F} (hM : WellFormed M)
    (coeffs : Array (CPolynomial F))
    (hzero : ∀ i, i < M.size →
      coeffs.getD i 0 = 0 ∨ RowIsZero (M.getD i #[])) :
    rowLinearCombination coeffs M = zeroRow (F := F) (MatrixWidth M)
```

`CompPoly.PolynomialMatrix.rowCombinationTermSupport_nonempty_of_combination_degree_some` (theorem, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean#L150))

```lean
theorem rowCombinationTermSupport_nonempty_of_combination_degree_some
    {M : PolynomialMatrix F} {shift : Array Nat}
    (hM : WellFormed M) {coeffs : Array (CPolynomial F)} {rowDeg : Nat}
    (hdeg : rowShiftedDegree? (rowLinearCombination coeffs M) shift = some rowDeg) :
    (rowCombinationTermSupport coeffs M shift).Nonempty
```

## Depends on

- [Row Span for Polynomial Matrices](../rowspan.md)
- [Shifted Degrees for Polynomial Rows](../shifted.md)

## Proof depends on

- [Mulders-Storjohann Correctness Matrix Row Helpers](matrixrows.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Combinations.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Combinations.json)
