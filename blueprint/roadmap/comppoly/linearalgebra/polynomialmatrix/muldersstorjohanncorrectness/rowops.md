---
catalog: module
lean: CompPoly.PolynomialMatrix.rowScalePolynomial_size, CompPoly.PolynomialMatrix.rowScaleMonomial_size, CompPoly.PolynomialMatrix.rowNeg_size, CompPoly.PolynomialMatrix.rowAdd_size, CompPoly.PolynomialMatrix.rowSub_size, CompPoly.PolynomialMatrix.rowGet_rowAdd, CompPoly.PolynomialMatrix.rowGet_rowScalePolynomial, CompPoly.PolynomialMatrix.rowGet_rowNeg, CompPoly.PolynomialMatrix.rowGet_rowSub, CompPoly.PolynomialMatrix.rowGet_rowScaleMonomial, CompPoly.PolynomialMatrix.rowGet_zeroRow, CompPoly.PolynomialMatrix.rowScalePolynomial_zeroRow, CompPoly.PolynomialMatrix.rowScalePolynomial_eq_zeroRow_of_rowIsZero, CompPoly.PolynomialMatrix.zeroRow_rowIsZero, CompPoly.PolynomialMatrix.rowScalePolynomial_zero, CompPoly.PolynomialMatrix.rowAdd_zeroRow_zeroRow, CompPoly.PolynomialMatrix.rowAdd_zeroRow_right, CompPoly.PolynomialMatrix.rowScalePolynomial_rowAdd, CompPoly.PolynomialMatrix.rowAdd_assoc, CompPoly.PolynomialMatrix.rowAdd_rowNeg_left, CompPoly.PolynomialMatrix.rowSub_add_cancel, CompPoly.PolynomialMatrix.rowAdd_medial, CompPoly.PolynomialMatrix.rowScalePolynomial_add, CompPoly.PolynomialMatrix.rowScalePolynomial_assoc, CompPoly.PolynomialMatrix.getD_map_mul, CompPoly.PolynomialMatrix.getD_ofFn_add, CompPoly.PolynomialMatrix.rowAdd_rowLinearCombination_range, CompPoly.PolynomialMatrix.rowAdd_rowLinearCombination, CompPoly.PolynomialMatrix.rowAdd_mem_rowSpan, CompPoly.PolynomialMatrix.C_neg_one_mul, CompPoly.PolynomialMatrix.rowNeg_eq_rowScalePolynomial, CompPoly.PolynomialMatrix.rowScalePolynomial_rowLinearCombination_range, CompPoly.PolynomialMatrix.rowScalePolynomial_rowLinearCombination, CompPoly.PolynomialMatrix.rowScalePolynomial_mem_rowSpan, CompPoly.PolynomialMatrix.rowScaleMonomial_mem_rowSpan, CompPoly.PolynomialMatrix.rowNeg_mem_rowSpan, CompPoly.PolynomialMatrix.rowSub_mem_rowSpan, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_mem_rowSpan, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_target_mem_rowSpan, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_size
statement: formalized
proof: formalized
---

# Mulders-Storjohann Correctness Row and Row-Span Helpers

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.RowOps`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean), by Valerii Huhnin.

> Row operation and row-span lemmas used by the Mulders-Storjohann correctness proof.

`CompPoly.PolynomialMatrix.rowScalePolynomial_size` (theorem, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L26))

```lean
theorem rowScalePolynomial_size (c : CPolynomial F) (row : PolynomialRow F) :
    (rowScalePolynomial c row).size = row.size
```

`CompPoly.PolynomialMatrix.rowScaleMonomial_size` (theorem, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L30))

```lean
theorem rowScaleMonomial_size (c : F) (d : Nat) (row : PolynomialRow F) :
    (rowScaleMonomial c d row).size = row.size
```

`CompPoly.PolynomialMatrix.rowNeg_size` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L35))

```lean
theorem rowNeg_size (row : PolynomialRow F) :
    (rowNeg row).size = row.size
```

`CompPoly.PolynomialMatrix.rowAdd_size` (theorem, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L40))

```lean
theorem rowAdd_size (a b : PolynomialRow F) :
    (rowAdd a b).size = max a.size b.size
```

`CompPoly.PolynomialMatrix.rowSub_size` (theorem, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L45))

```lean
theorem rowSub_size (a b : PolynomialRow F) :
    (rowSub a b).size = max a.size b.size
```

`CompPoly.PolynomialMatrix.rowGet_rowAdd` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L50))

```lean
theorem rowGet_rowAdd (a b : PolynomialRow F) (j : Nat) :
    rowGet (rowAdd a b) j = rowGet a j + rowGet b j
```

`CompPoly.PolynomialMatrix.rowGet_rowScalePolynomial` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L64))

```lean
theorem rowGet_rowScalePolynomial
    (c : CPolynomial F) (row : PolynomialRow F) (j : Nat) :
    rowGet (rowScalePolynomial c row) j = c * rowGet row j
```

`CompPoly.PolynomialMatrix.rowGet_rowNeg` (theorem, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L77))

```lean
theorem rowGet_rowNeg (row : PolynomialRow F) (j : Nat) :
    rowGet (rowNeg row) j = -rowGet row j
```

`CompPoly.PolynomialMatrix.rowGet_rowSub` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L89))

```lean
theorem rowGet_rowSub (a b : PolynomialRow F) (j : Nat) :
    rowGet (rowSub a b) j = rowGet a j - rowGet b j
```

`CompPoly.PolynomialMatrix.rowGet_rowScaleMonomial` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L93))

```lean
theorem rowGet_rowScaleMonomial
    (c : F) (d : Nat) (row : PolynomialRow F) (j : Nat) :
    rowGet (rowScaleMonomial c d row) j =
      CPolynomial.monomial d c * rowGet row j
```

`CompPoly.PolynomialMatrix.rowGet_zeroRow` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L100))

```lean
theorem rowGet_zeroRow (width j : Nat) :
    rowGet (zeroRow (F := F) width) j = 0
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_zeroRow` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L112))

```lean
theorem rowScalePolynomial_zeroRow (c : CPolynomial F) (width : Nat) :
    rowScalePolynomial c (zeroRow (F := F) width) = zeroRow width
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_eq_zeroRow_of_rowIsZero` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L120))

```lean
theorem rowScalePolynomial_eq_zeroRow_of_rowIsZero
    (c : CPolynomial F) {row : PolynomialRow F} (hrow : RowIsZero row) :
    rowScalePolynomial c row = zeroRow row.size
```

`CompPoly.PolynomialMatrix.zeroRow_rowIsZero` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L134))

```lean
theorem zeroRow_rowIsZero (width : Nat) :
    RowIsZero (zeroRow (F := F) width)
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_zero` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L141))

```lean
theorem rowScalePolynomial_zero (row : PolynomialRow F) :
    rowScalePolynomial (0 : CPolynomial F) row = zeroRow row.size
```

`CompPoly.PolynomialMatrix.rowAdd_zeroRow_zeroRow` (theorem, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L160))

```lean
theorem rowAdd_zeroRow_zeroRow (width : Nat) :
    rowAdd (zeroRow (F := F) width) (zeroRow width) = zeroRow width
```

`CompPoly.PolynomialMatrix.rowAdd_zeroRow_right` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L173))

```lean
theorem rowAdd_zeroRow_right
    {width : Nat} (row : PolynomialRow F) (hsize : row.size = width) :
    rowAdd row (zeroRow (F := F) width) = row
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_rowAdd` (theorem, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L186))

```lean
theorem rowScalePolynomial_rowAdd
    (c : CPolynomial F) (a b : PolynomialRow F) :
    rowScalePolynomial c (rowAdd a b) =
      rowAdd (rowScalePolynomial c a) (rowScalePolynomial c b)
```

`CompPoly.PolynomialMatrix.rowAdd_assoc` (theorem, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L197))

```lean
theorem rowAdd_assoc (a b c : PolynomialRow F) :
    rowAdd (rowAdd a b) c = rowAdd a (rowAdd b c)
```

`CompPoly.PolynomialMatrix.rowAdd_rowNeg_left` (theorem, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L210))

```lean
theorem rowAdd_rowNeg_left (row : PolynomialRow F) :
    rowAdd (rowNeg row) row = zeroRow row.size
```

`CompPoly.PolynomialMatrix.rowSub_add_cancel` (theorem, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L223))

```lean
theorem rowSub_add_cancel
    {a b : PolynomialRow F} (hsize : b.size = a.size) :
    rowAdd (rowSub a b) b = a
```

`CompPoly.PolynomialMatrix.rowAdd_medial` (theorem, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L231))

```lean
theorem rowAdd_medial (a b c d : PolynomialRow F) :
    rowAdd (rowAdd a b) (rowAdd c d) =
      rowAdd (rowAdd a c) (rowAdd b d)
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_add` (theorem, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L247))

```lean
theorem rowScalePolynomial_add
    (c d : CPolynomial F) (row : PolynomialRow F) :
    rowAdd (rowScalePolynomial c row) (rowScalePolynomial d row) =
      rowScalePolynomial (c + d) row
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_assoc` (theorem, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L262))

```lean
theorem rowScalePolynomial_assoc
    (c d : CPolynomial F) (row : PolynomialRow F) :
    rowScalePolynomial c (rowScalePolynomial d row) =
      rowScalePolynomial (c * d) row
```

`CompPoly.PolynomialMatrix.getD_map_mul` (theorem, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L272))

```lean
theorem getD_map_mul
    (coeffs : Array (CPolynomial F)) (c : CPolynomial F) (i : Nat) :
    (coeffs.map (fun q ↦ c * q)).getD i 0 = c * coeffs.getD i 0
```

`CompPoly.PolynomialMatrix.getD_ofFn_add` (theorem, [line 284](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L284))

```lean
theorem getD_ofFn_add
    (n : Nat) (coeffsA coeffsB : Array (CPolynomial F)) {i : Nat} (hi : i < n) :
    (Array.ofFn
        (fun k : Fin n ↦ coeffsA.getD k.1 0 + coeffsB.getD k.1 0)).getD i 0 =
      coeffsA.getD i 0 + coeffsB.getD i 0
```

`CompPoly.PolynomialMatrix.rowAdd_rowLinearCombination_range` (theorem, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L295))

```lean
theorem rowAdd_rowLinearCombination_range
    {M : PolynomialMatrix F} (coeffsA coeffsB : Array (CPolynomial F)) :
    ∀ n, n ≤ M.size →
      rowAdd
        ((List.range n).foldl
          (fun acc i ↦
            rowAdd acc
              (rowScalePolynomial (coeffsA.getD i 0) (M.getD i #[])))
          (zeroRow (MatrixWidth M)))
        ((List.range n).foldl
          (fun acc i ↦
            rowAdd acc
              (rowScalePolynomial (coeffsB.getD i 0) (M.getD i #[])))
          (zeroRow (MatrixWidth M))) =
      ((List.range n).foldl
        (fun acc i ↦
          rowAdd acc
            (rowScalePolynomial
              ((Array.ofFn
                (fun k : Fin M.size ↦ coeffsA.getD k.1 0 + coeffsB.getD k.1 0)).getD i 0)
              (M.getD i #[])))
        (zeroRow (MatrixWidth M)))
```

`CompPoly.PolynomialMatrix.rowAdd_rowLinearCombination` (theorem, [line 329](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L329))

```lean
theorem rowAdd_rowLinearCombination
    {M : PolynomialMatrix F} (coeffsA coeffsB : Array (CPolynomial F)) :
    rowAdd (rowLinearCombination coeffsA M) (rowLinearCombination coeffsB M) =
      rowLinearCombination
        (Array.ofFn
          (fun k : Fin M.size ↦ coeffsA.getD k.1 0 + coeffsB.getD k.1 0)) M
```

`CompPoly.PolynomialMatrix.rowAdd_mem_rowSpan` (theorem, [line 340](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L340))

```lean
theorem rowAdd_mem_rowSpan
    {M : PolynomialMatrix F} {a b : PolynomialRow F}
    (ha : a ∈ RowSpan M) (hb : b ∈ RowSpan M) :
    rowAdd a b ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.C_neg_one_mul` (theorem, [line 352](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L352))

```lean
theorem C_neg_one_mul (p : CPolynomial F) :
    CPolynomial.C (-1 : F) * p = -p
```

`CompPoly.PolynomialMatrix.rowNeg_eq_rowScalePolynomial` (theorem, [line 357](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L357))

```lean
theorem rowNeg_eq_rowScalePolynomial (row : PolynomialRow F) :
    rowNeg row = rowScalePolynomial (CPolynomial.C (-1 : F)) row
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_rowLinearCombination_range` (theorem, [line 365](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L365))

```lean
theorem rowScalePolynomial_rowLinearCombination_range
    {M : PolynomialMatrix F} (c : CPolynomial F) (coeffs : Array (CPolynomial F)) :
    ∀ n,
      rowScalePolynomial c
        ((List.range n).foldl
          (fun acc i ↦
            rowAdd acc
              (rowScalePolynomial (coeffs.getD i 0) (M.getD i #[])))
          (zeroRow (MatrixWidth M))) =
      ((List.range n).foldl
        (fun acc i ↦
          rowAdd acc
            (rowScalePolynomial ((coeffs.map fun q ↦ c * q).getD i 0)
              (M.getD i #[])))
        (zeroRow (MatrixWidth M)))
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_rowLinearCombination` (theorem, [line 391](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L391))

```lean
theorem rowScalePolynomial_rowLinearCombination
    {M : PolynomialMatrix F} (c : CPolynomial F) (coeffs : Array (CPolynomial F)) :
    rowScalePolynomial c (rowLinearCombination coeffs M) =
      rowLinearCombination (coeffs.map fun q ↦ c * q) M
```

`CompPoly.PolynomialMatrix.rowScalePolynomial_mem_rowSpan` (theorem, [line 399](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L399))

```lean
theorem rowScalePolynomial_mem_rowSpan
    {M : PolynomialMatrix F} {row : PolynomialRow F}
  (c : CPolynomial F) (hrow : row ∈ RowSpan M) :
    rowScalePolynomial c row ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.rowScaleMonomial_mem_rowSpan` (theorem, [line 407](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L407))

```lean
theorem rowScaleMonomial_mem_rowSpan
    {M : PolynomialMatrix F} {row : PolynomialRow F}
    (c : F) (d : Nat) (hrow : row ∈ RowSpan M) :
    rowScaleMonomial c d row ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.rowNeg_mem_rowSpan` (theorem, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L415))

```lean
theorem rowNeg_mem_rowSpan
    {M : PolynomialMatrix F} {row : PolynomialRow F}
    (hrow : row ∈ RowSpan M) :
    rowNeg row ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.rowSub_mem_rowSpan` (theorem, [line 423](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L423))

```lean
theorem rowSub_mem_rowSpan
    {M : PolynomialMatrix F} {a b : PolynomialRow F}
    (ha : a ∈ RowSpan M) (hb : b ∈ RowSpan M) :
    rowSub a b ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_mem_rowSpan` (theorem, [line 430](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L430))

```lean
theorem cancelShiftedLeadingTerm_mem_rowSpan
    {M : PolynomialMatrix F} {target reducer : PolynomialRow F} {shift : Array Nat}
    (htarget : target ∈ RowSpan M) (hreducer : reducer ∈ RowSpan M) :
    cancelShiftedLeadingTerm target reducer shift ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_target_mem_rowSpan` (theorem, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L441))

```lean
theorem cancelShiftedLeadingTerm_target_mem_rowSpan
    {M : PolynomialMatrix F} {target reducer : PolynomialRow F} {shift : Array Nat}
    (hcancel : cancelShiftedLeadingTerm target reducer shift ∈ RowSpan M)
    (hreducer : reducer ∈ RowSpan M)
    (hsize : reducer.size = target.size) :
    target ∈ RowSpan M
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_size` (theorem, [line 468](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean#L468))

```lean
theorem cancelShiftedLeadingTerm_size
    {target reducer : PolynomialRow F} {shift : Array Nat}
    (hsize : reducer.size = target.size) :
    (cancelShiftedLeadingTerm target reducer shift).size = target.size
```

## Depends on

- [Mulders-Storjohann Shifted Row Reduction](../muldersstorjohann.md)
- [Row Span for Polynomial Matrices](../rowspan.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/RowOps.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.RowOps.json)
