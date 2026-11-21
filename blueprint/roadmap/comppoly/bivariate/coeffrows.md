---
catalog: module
lean: CompPoly.CBivariate.ofCoeffRow, CompPoly.CBivariate.toCoeffRow, CompPoly.CBivariate.toCoeffRow_size, CompPoly.CBivariate.weightedDegreeShift, CompPoly.CBivariate.coeff_ofCoeffRow_of_lt, CompPoly.CBivariate.coeff_ofCoeffRow_of_size_le, CompPoly.CBivariate.rowShiftedDegree?_eq_natWeightedDegree_ofCoeffRow, CompPoly.CBivariate.natWeightedDegree_ofCoeffRow_le_of_rowShiftedDegree?_le
statement: formalized
proof: formalized
---

# Coefficient Rows for Bivariate Polynomials

`CompPoly.Bivariate.CoeffRows`, in [CompPoly/Bivariate/CoeffRows.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean), by Valerii Huhnin.

> Conversions between finite `Y`-coefficient rows and `CBivariate`.

`CompPoly.CBivariate.ofCoeffRow` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean#L27))

> Interpret a polynomial row `[q_0, ..., q_l]` as `∑ q_j(X) Y^j`.

```lean
def ofCoeffRow [Zero F] [BEq F] [LawfulBEq F]
    (row : PolynomialRow F) : CBivariate F
```

`CompPoly.CBivariate.toCoeffRow` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean#L32))

> Truncate a bivariate polynomial to its first `width` `Y`-coefficient rows.

```lean
def toCoeffRow [Zero F] (width : Nat) (Q : CBivariate F) :
    PolynomialRow F
```

`CompPoly.CBivariate.toCoeffRow_size` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean#L37))

> Truncated coefficient rows have the requested width.

```lean
theorem toCoeffRow_size [Zero F] (width : Nat) (Q : CBivariate F) :
    (toCoeffRow width Q).size = width
```

`CompPoly.CBivariate.weightedDegreeShift` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean#L42))

> Lee-style shift array for `(1, w)` weighted degree.

```lean
def weightedDegreeShift (w width : Nat) : Array Nat
```

`CompPoly.CBivariate.coeff_ofCoeffRow_of_lt` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean#L46))

> Coefficient-row conversion preserves finite `Y` coefficients below row width.

```lean
theorem coeff_ofCoeffRow_of_lt [Zero F] [BEq F] [LawfulBEq F]
    (row : PolynomialRow F) {i j : Nat} (hj : j < row.size) :
    CBivariate.coeff (ofCoeffRow row) i j = CPolynomial.coeff (row.getD j 0) i
```

`CompPoly.CBivariate.coeff_ofCoeffRow_of_size_le` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean#L55))

> Coefficients past the row width vanish after row-to-bivariate conversion.

```lean
theorem coeff_ofCoeffRow_of_size_le [Zero F] [BEq F] [LawfulBEq F]
    (row : PolynomialRow F) {i j : Nat} (hj : row.size ≤ j) :
    CBivariate.coeff (ofCoeffRow row) i j = 0
```

`CompPoly.CBivariate.rowShiftedDegree?_eq_natWeightedDegree_ofCoeffRow` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean#L65))

> Row shifted degree for the Lee shift matches weighted degree of the bivariate view.

```lean
theorem rowShiftedDegree?_eq_natWeightedDegree_ofCoeffRow
    [Field F] [BEq F] [LawfulBEq F]
    (row : PolynomialRow F) (w d : Nat)
    (hdeg :
      PolynomialMatrix.rowShiftedDegree? row (weightedDegreeShift w row.size) = some d) :
    CBivariate.natWeightedDegree (ofCoeffRow row) 1 w = d
```

`CompPoly.CBivariate.natWeightedDegree_ofCoeffRow_le_of_rowShiftedDegree?_le` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean#L143))

> Weighted-degree bounded rows convert to weighted-degree bounded bivariate polynomials.

```lean
theorem natWeightedDegree_ofCoeffRow_le_of_rowShiftedDegree?_le
    [Field F] [BEq F] [LawfulBEq F]
    (row : PolynomialRow F) (w bound d : Nat)
    (hdeg :
      PolynomialMatrix.rowShiftedDegree? row (weightedDegreeShift w row.size) = some d)
    (hle : d ≤ bound) :
    CBivariate.natWeightedDegree (ofCoeffRow row) 1 w ≤ bound
```

## Depends on

- [Computable Bivariate Polynomials](basic.md)
- [Shifted Degrees for Polynomial Rows](../linearalgebra/polynomialmatrix/shifted.md)

## Sources

- [CompPoly/Bivariate/CoeffRows.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/CoeffRows.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.CoeffRows.json)
