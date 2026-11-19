---
catalog: module
lean: CompPoly.PolynomialMatrix.ShiftedLeadingTerm, CompPoly.PolynomialMatrix.maxOption, CompPoly.PolynomialMatrix.shiftedEntryDegree?, CompPoly.PolynomialMatrix.rowShiftedDegree?, CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?, CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?, CompPoly.PolynomialMatrix.shiftedEntryDegree?_eq_some_iff, CompPoly.PolynomialMatrix.rowShiftedDegree?_eq_none_iff, CompPoly.PolynomialMatrix.shiftedEntryDegree?_le_of_rowShiftedDegree?_eq_some, CompPoly.PolynomialMatrix.exists_shiftedEntryDegree?_eq_of_rowShiftedDegree?_eq_some, CompPoly.PolynomialMatrix.ShiftedWeakPopov
statement: formalized
proof: formalized
---

# Shifted Degrees for Polynomial Rows

`CompPoly.LinearAlgebra.PolynomialMatrix.Shifted`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean), by Valerii Huhnin.

`CompPoly.PolynomialMatrix.ShiftedLeadingTerm` (structure, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L23))

> Shifted leading term metadata for a nonzero row.

```lean
structure ShiftedLeadingTerm (F : Type*) where
  position : Nat
  degree : Nat
  shiftedDegree : Nat
  coeff : F
deriving Repr
```

`CompPoly.PolynomialMatrix.maxOption` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L31))

> Insert a natural number into an optional running maximum.

```lean
def maxOption : Option Nat → Nat → Option Nat
```

`CompPoly.PolynomialMatrix.shiftedEntryDegree?` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L36))

> Shifted degree of one row entry. Zero entries have no degree.

```lean
def shiftedEntryDegree? [Zero F] [BEq F]
    (row : PolynomialRow F) (shift : Array Nat) (j : Nat) : Option Nat
```

`CompPoly.PolynomialMatrix.rowShiftedDegree?` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L42))

> Shifted degree of a row, with `none` exactly for zero rows.

```lean
def rowShiftedDegree? [Zero F] [BEq F]
    (row : PolynomialRow F) (shift : Array Nat) : Option Nat
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L52))

> Shifted leading position of a nonzero row. Ties use the largest column index.

```lean
def rowShiftedLeadingPosition? [Zero F] [BEq F]
    (row : PolynomialRow F) (shift : Array Nat) : Option Nat
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L63))

> Shifted leading term metadata for a nonzero row.

```lean
def rowShiftedLeadingTerm? [Zero F] [BEq F]
    (row : PolynomialRow F) (shift : Array Nat) :
    Option (ShiftedLeadingTerm F)
```

`CompPoly.PolynomialMatrix.shiftedEntryDegree?_eq_some_iff` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L86))

> A row entry has shifted degree `d` exactly when it is nonzero and `d` is its shifted degree.

```lean
theorem shiftedEntryDegree?_eq_some_iff [Zero F] [BEq F] [LawfulBEq F]
    (row : PolynomialRow F) (shift : Array Nat) (j d : Nat) :
    shiftedEntryDegree? row shift j = some d ↔
      rowGet row j ≠ 0 ∧ (rowGet row j).natDegree + shift.getD j 0 = d
```

`CompPoly.PolynomialMatrix.rowShiftedDegree?_eq_none_iff` (theorem, [line 238](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L238))

> Nonzero rows are exactly the rows with a shifted degree.

```lean
theorem rowShiftedDegree?_eq_none_iff [Zero F] [BEq F] [LawfulBEq F]
    {row : PolynomialRow F} {shift : Array Nat} :
    rowShiftedDegree? row shift = none ↔ RowIsZero row
```

`CompPoly.PolynomialMatrix.shiftedEntryDegree?_le_of_rowShiftedDegree?_eq_some` (theorem, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L252))

> A returned shifted row degree bounds every nonzero shifted entry degree.

```lean
theorem shiftedEntryDegree?_le_of_rowShiftedDegree?_eq_some
    [Zero F] [BEq F]
    {row : PolynomialRow F} {shift : Array Nat} {d j e : Nat}
    (hdeg : rowShiftedDegree? row shift = some d)
    (hj : j < row.size)
    (hentry : shiftedEntryDegree? row shift j = some e) :
    e ≤ d
```

`CompPoly.PolynomialMatrix.exists_shiftedEntryDegree?_eq_of_rowShiftedDegree?_eq_some` (theorem, [line 263](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L263))

> A returned shifted row degree is attained by some row entry.

```lean
theorem exists_shiftedEntryDegree?_eq_of_rowShiftedDegree?_eq_some
    [Zero F] [BEq F]
    {row : PolynomialRow F} {shift : Array Nat} {d : Nat}
    (hdeg : rowShiftedDegree? row shift = some d) :
    ∃ j, j < row.size ∧ shiftedEntryDegree? row shift j = some d
```

`CompPoly.PolynomialMatrix.ShiftedWeakPopov` (definition, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean#L276))

> A shifted weak-Popov matrix has distinct leading positions among nonzero rows.

```lean
def ShiftedWeakPopov [Zero F] [BEq F]
    (M : PolynomialMatrix F) (shift : Array Nat) : Prop
```

## Depends on

- [Degree Helpers for Polynomial Rows](degree.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/Shifted.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Shifted.json)
