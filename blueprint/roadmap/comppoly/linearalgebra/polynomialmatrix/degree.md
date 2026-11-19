---
catalog: module
lean: CompPoly.PolynomialMatrix.polynomialDegree?, CompPoly.PolynomialMatrix.RowIsZero, CompPoly.PolynomialMatrix.rowIsZero, CompPoly.PolynomialMatrix.rowIsZero_iff, CompPoly.PolynomialMatrix.exists_nonzero_entry_of_rowIsZero_false
statement: formalized
proof: formalized
---

# Degree Helpers for Polynomial Rows

`CompPoly.LinearAlgebra.PolynomialMatrix.Degree`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean), by Valerii Huhnin.

`CompPoly.PolynomialMatrix.polynomialDegree?` (definition, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean#L23))

> Optional degree of a univariate polynomial, with `none` for zero.

```lean
def polynomialDegree? [Zero F] [BEq F] (p : CPolynomial F) : Option Nat
```

`CompPoly.PolynomialMatrix.RowIsZero` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean#L27))

> A row is zero when all entries are zero.

```lean
def RowIsZero [Zero F] [BEq F] (row : PolynomialRow F) : Prop
```

`CompPoly.PolynomialMatrix.rowIsZero` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean#L31))

> Executable zero-row predicate.

```lean
def rowIsZero [Zero F] [BEq F] (row : PolynomialRow F) : Bool
```

`CompPoly.PolynomialMatrix.rowIsZero_iff` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean#L35))

> Boolean and propositional zero-row predicates agree.

```lean
theorem rowIsZero_iff [Zero F] [BEq F] [LawfulBEq F]
    {row : PolynomialRow F} :
    rowIsZero row = true ↔ RowIsZero row
```

`CompPoly.PolynomialMatrix.exists_nonzero_entry_of_rowIsZero_false` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean#L52))

> Nonzero rows have an indexed nonzero entry.

```lean
theorem exists_nonzero_entry_of_rowIsZero_false [Zero F] [BEq F] [LawfulBEq F]
    {row : PolynomialRow F} (hrow : rowIsZero row = false) :
    ∃ j, j < row.size ∧ row.getD j 0 ≠ 0
```

## Depends on

- [Polynomial Rows and Matrices](basic.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Degree.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Degree.json)
