---
catalog: module
lean: CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_lt, CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_no_larger_tie, CompPoly.PolynomialMatrix.list_find?_some_of_exists, CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_some_of_degree, CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_le_of_entry_eq_degree, CompPoly.PolynomialMatrix.shiftedEntryDegree?_eq_some_of_rowGet_ne_zero, CompPoly.PolynomialMatrix.shiftedEntryDegree?_eq_some_iff_data, CompPoly.PolynomialMatrix.rowShiftedDegree?_entry_bound, CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_entry_eq, CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_some_of_position, CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_some_data, CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_coeff_ne_zero, CompPoly.PolynomialMatrix.cpoly_coeff_mul_natDegree_add_ne_zero, CompPoly.PolynomialMatrix.cpoly_natDegree_monomial_le, CompPoly.PolynomialMatrix.cpoly_natDegree_monomial_mul_le, CompPoly.PolynomialMatrix.cpoly_coeff_monomial_mul, CompPoly.PolynomialMatrix.cpoly_natDegree_sub_shift_le, CompPoly.PolynomialMatrix.cpoly_natDegree_sub_shift_lt, CompPoly.PolynomialMatrix.rowShiftedDegree?_le_of_entry_bound, CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_entry_bound, CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_entry_strict_of_pos_lt, CompPoly.PolynomialMatrix.rowScaleMonomial_entry_bound_of_leading_terms, CompPoly.PolynomialMatrix.rowScaleMonomial_entry_strict_of_pos_lt, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_coeff_cancel, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_no_target_shifted_entry, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_entry_bound, CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_entry_strict_of_pos_lt
statement: formalized
proof: formalized
---

# Mulders-Storjohann Correctness Shifted Leading Term Helpers

`CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Leading`, in [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean), by Valerii Huhnin.

> Shifted leading-position data and cancellation degree bounds.

`CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_lt` (theorem, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L26))

```lean
theorem rowShiftedLeadingPosition?_lt
    {row : PolynomialRow F} {shift : Array Nat} {pos : Nat}
    (hpos : rowShiftedLeadingPosition? row shift = some pos) :
    pos < row.size
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_no_larger_tie` (theorem, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L44))

```lean
theorem rowShiftedLeadingPosition?_no_larger_tie
    {row : PolynomialRow F} {shift : Array Nat} {degree pos k : Nat}
    (hdeg : rowShiftedDegree? row shift = some degree)
    (hpos : rowShiftedLeadingPosition? row shift = some pos)
    (hk : k < row.size) (hposk : pos < k) :
    shiftedEntryDegree? row shift k ≠ some degree
```

`CompPoly.PolynomialMatrix.list_find?_some_of_exists` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L95))

```lean
theorem list_find?_some_of_exists
    {α : Type*} (xs : List α) (pred : α → Bool)
    (hexists : ∃ x ∈ xs, pred x = true) :
    ∃ x, xs.find? pred = some x
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_some_of_degree` (theorem, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L116))

```lean
theorem rowShiftedLeadingPosition?_some_of_degree
    {row : PolynomialRow F} {shift : Array Nat} {degree : Nat}
    (hdeg : rowShiftedDegree? row shift = some degree) :
    ∃ pos, rowShiftedLeadingPosition? row shift = some pos
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_le_of_entry_eq_degree` (theorem, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L137))

```lean
theorem rowShiftedLeadingPosition?_le_of_entry_eq_degree
    {row : PolynomialRow F} {shift : Array Nat} {degree pos k : Nat}
    (hdeg : rowShiftedDegree? row shift = some degree)
    (hpos : rowShiftedLeadingPosition? row shift = some pos)
    (hk : k < row.size)
    (hentry : shiftedEntryDegree? row shift k = some degree) :
    k ≤ pos
```

`CompPoly.PolynomialMatrix.shiftedEntryDegree?_eq_some_of_rowGet_ne_zero` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L149))

```lean
theorem shiftedEntryDegree?_eq_some_of_rowGet_ne_zero
    {row : PolynomialRow F} {shift : Array Nat} {j : Nat}
    (hne : rowGet row j ≠ 0) :
    shiftedEntryDegree? row shift j =
      some ((rowGet row j).natDegree + shift.getD j 0)
```

`CompPoly.PolynomialMatrix.shiftedEntryDegree?_eq_some_iff_data` (theorem, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L161))

```lean
theorem shiftedEntryDegree?_eq_some_iff_data
    {row : PolynomialRow F} {shift : Array Nat} {j d : Nat} :
    shiftedEntryDegree? row shift j = some d ↔
      rowGet row j ≠ 0 ∧
        (rowGet row j).natDegree + shift.getD j 0 = d
```

`CompPoly.PolynomialMatrix.rowShiftedDegree?_entry_bound` (theorem, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L183))

```lean
theorem rowShiftedDegree?_entry_bound
    {row : PolynomialRow F} {shift : Array Nat} {degree j : Nat}
    (hdeg : rowShiftedDegree? row shift = some degree)
    (hj : j < row.size) (hne : rowGet row j ≠ 0) :
    (rowGet row j).natDegree + shift.getD j 0 ≤ degree
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingPosition?_entry_eq` (theorem, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L192))

```lean
theorem rowShiftedLeadingPosition?_entry_eq
    {row : PolynomialRow F} {shift : Array Nat} {degree pos : Nat}
    (hdeg : rowShiftedDegree? row shift = some degree)
    (hpos : rowShiftedLeadingPosition? row shift = some pos) :
    shiftedEntryDegree? row shift pos = some degree
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_some_of_position` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L208))

```lean
theorem rowShiftedLeadingTerm?_some_of_position
    {row : PolynomialRow F} {shift : Array Nat} {pos : Nat}
    (hpos : rowShiftedLeadingPosition? row shift = some pos) :
    ∃ term : ShiftedLeadingTerm F,
      rowShiftedLeadingTerm? row shift = some term ∧ term.position = pos
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_some_data` (theorem, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L235))

```lean
theorem rowShiftedLeadingTerm?_some_data
    {row : PolynomialRow F} {shift : Array Nat} {term : ShiftedLeadingTerm F}
    (hterm : rowShiftedLeadingTerm? row shift = some term) :
    rowShiftedDegree? row shift = some term.shiftedDegree ∧
      rowShiftedLeadingPosition? row shift = some term.position ∧
      rowGet row term.position ≠ 0 ∧
      term.degree = (rowGet row term.position).natDegree ∧
      term.shiftedDegree = term.degree + shift.getD term.position 0 ∧
      term.coeff = (rowGet row term.position).coeff term.degree
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_coeff_ne_zero` (theorem, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L264))

```lean
theorem rowShiftedLeadingTerm?_coeff_ne_zero
    {row : PolynomialRow F} {shift : Array Nat} {term : ShiftedLeadingTerm F}
    (hterm : rowShiftedLeadingTerm? row shift = some term) :
    term.coeff ≠ 0
```

`CompPoly.PolynomialMatrix.cpoly_coeff_mul_natDegree_add_ne_zero` (theorem, [line 277](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L277))

```lean
theorem cpoly_coeff_mul_natDegree_add_ne_zero
    {P Q : CPolynomial F} (hP : P ≠ 0) (hQ : Q ≠ 0) :
    (P * Q).coeff (P.natDegree + Q.natDegree) ≠ 0
```

`CompPoly.PolynomialMatrix.cpoly_natDegree_monomial_le` (theorem, [line 293](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L293))

```lean
theorem cpoly_natDegree_monomial_le (d : Nat) (c : F) :
    (CPolynomial.monomial d c).natDegree ≤ d
```

`CompPoly.PolynomialMatrix.cpoly_natDegree_monomial_mul_le` (theorem, [line 300](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L300))

```lean
theorem cpoly_natDegree_monomial_mul_le
    (d : Nat) (c : F) (P : CPolynomial F) :
    (CPolynomial.monomial d c * P).natDegree ≤ d + P.natDegree
```

`CompPoly.PolynomialMatrix.cpoly_coeff_monomial_mul` (theorem, [line 307](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L307))

```lean
theorem cpoly_coeff_monomial_mul
    (n d : Nat) (c : F) (P : CPolynomial F) :
    (CPolynomial.monomial n c * P).coeff (d + n) =
      c * P.coeff d
```

`CompPoly.PolynomialMatrix.cpoly_natDegree_sub_shift_le` (theorem, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L320))

```lean
theorem cpoly_natDegree_sub_shift_le
    {P Q : CPolynomial F} {shiftDegree bound : Nat}
    (hP : P ≠ 0 → P.natDegree + shiftDegree ≤ bound)
    (hQ : Q ≠ 0 → Q.natDegree + shiftDegree ≤ bound)
    (hne : P - Q ≠ 0) :
    (P - Q).natDegree + shiftDegree ≤ bound
```

`CompPoly.PolynomialMatrix.cpoly_natDegree_sub_shift_lt` (theorem, [line 342](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L342))

```lean
theorem cpoly_natDegree_sub_shift_lt
    {P Q : CPolynomial F} {shiftDegree bound : Nat}
    (hP : P ≠ 0 → P.natDegree + shiftDegree < bound)
    (hQ : Q ≠ 0 → Q.natDegree + shiftDegree < bound)
    (hne : P - Q ≠ 0) :
    (P - Q).natDegree + shiftDegree < bound
```

`CompPoly.PolynomialMatrix.rowShiftedDegree?_le_of_entry_bound` (theorem, [line 364](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L364))

```lean
theorem rowShiftedDegree?_le_of_entry_bound
    {row : PolynomialRow F} {shift : Array Nat} {degree bound : Nat}
    (hbound : ∀ k, k < row.size → rowGet row k ≠ 0 →
      (rowGet row k).natDegree + shift.getD k 0 ≤ bound)
    (hdeg : rowShiftedDegree? row shift = some degree) :
    degree ≤ bound
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_entry_bound` (theorem, [line 377](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L377))

```lean
theorem rowShiftedLeadingTerm?_entry_bound
    {row : PolynomialRow F} {shift : Array Nat} {term : ShiftedLeadingTerm F}
    (hterm : rowShiftedLeadingTerm? row shift = some term)
    {k : Nat} (hk : k < row.size) (hne : rowGet row k ≠ 0) :
    (rowGet row k).natDegree + shift.getD k 0 ≤ term.shiftedDegree
```

`CompPoly.PolynomialMatrix.rowShiftedLeadingTerm?_entry_strict_of_pos_lt` (theorem, [line 387](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L387))

```lean
theorem rowShiftedLeadingTerm?_entry_strict_of_pos_lt
    {row : PolynomialRow F} {shift : Array Nat} {term : ShiftedLeadingTerm F}
    (hterm : rowShiftedLeadingTerm? row shift = some term)
    {k : Nat} (hk : k < row.size) (hposlt : term.position < k)
    (hne : rowGet row k ≠ 0) :
    (rowGet row k).natDegree + shift.getD k 0 < term.shiftedDegree
```

`CompPoly.PolynomialMatrix.rowScaleMonomial_entry_bound_of_leading_terms` (theorem, [line 408](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L408))

```lean
theorem rowScaleMonomial_entry_bound_of_leading_terms
    {target reducer : PolynomialRow F} {shift : Array Nat}
    {t r : ShiftedLeadingTerm F}
    (ht : rowShiftedLeadingTerm? target shift = some t)
    (hr : rowShiftedLeadingTerm? reducer shift = some r)
    (hpos : t.position = r.position)
    (hle : r.shiftedDegree ≤ t.shiftedDegree)
    {k : Nat} (hk : k < reducer.size)
    (hne : rowGet
      (rowScaleMonomial (t.coeff / r.coeff) (t.degree - r.degree) reducer) k ≠ 0) :
    (rowGet
      (rowScaleMonomial (t.coeff / r.coeff) (t.degree - r.degree) reducer) k).natDegree +
        shift.getD k 0 ≤ t.shiftedDegree
```

`CompPoly.PolynomialMatrix.rowScaleMonomial_entry_strict_of_pos_lt` (theorem, [line 448](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L448))

```lean
theorem rowScaleMonomial_entry_strict_of_pos_lt
    {target reducer : PolynomialRow F} {shift : Array Nat}
    {t r : ShiftedLeadingTerm F}
    (ht : rowShiftedLeadingTerm? target shift = some t)
    (hr : rowShiftedLeadingTerm? reducer shift = some r)
    (hpos : t.position = r.position)
    (hle : r.shiftedDegree ≤ t.shiftedDegree)
    {k : Nat} (hk : k < reducer.size) (hposlt : t.position < k)
    (hne : rowGet
      (rowScaleMonomial (t.coeff / r.coeff) (t.degree - r.degree) reducer) k ≠ 0) :
    (rowGet
      (rowScaleMonomial (t.coeff / r.coeff) (t.degree - r.degree) reducer) k).natDegree +
        shift.getD k 0 < t.shiftedDegree
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_coeff_cancel` (theorem, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L485))

```lean
theorem cancelShiftedLeadingTerm_coeff_cancel
    {target reducer : PolynomialRow F} {shift : Array Nat}
    {t r : ShiftedLeadingTerm F}
    (ht : rowShiftedLeadingTerm? target shift = some t)
    (hr : rowShiftedLeadingTerm? reducer shift = some r)
    (hpos : t.position = r.position)
    (hle : r.shiftedDegree ≤ t.shiftedDegree)
    (hrcoeff : r.coeff ≠ 0) :
    (rowGet (cancelShiftedLeadingTerm target reducer shift) t.position).coeff t.degree = 0
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_no_target_shifted_entry` (theorem, [line 536](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L536))

```lean
theorem cancelShiftedLeadingTerm_no_target_shifted_entry
    {target reducer : PolynomialRow F} {shift : Array Nat}
    {t r : ShiftedLeadingTerm F}
    (ht : rowShiftedLeadingTerm? target shift = some t)
    (hr : rowShiftedLeadingTerm? reducer shift = some r)
    (hpos : t.position = r.position)
    (hle : r.shiftedDegree ≤ t.shiftedDegree) :
    shiftedEntryDegree? (cancelShiftedLeadingTerm target reducer shift) shift t.position ≠
      some t.shiftedDegree
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_entry_bound` (theorem, [line 566](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L566))

```lean
theorem cancelShiftedLeadingTerm_entry_bound
    {target reducer : PolynomialRow F} {shift : Array Nat}
    {t r : ShiftedLeadingTerm F}
    (ht : rowShiftedLeadingTerm? target shift = some t)
    (hr : rowShiftedLeadingTerm? reducer shift = some r)
    (hpos : t.position = r.position)
    (hle : r.shiftedDegree ≤ t.shiftedDegree)
    (hsize : reducer.size = target.size)
    {k : Nat} (hk : k < target.size)
    (hne : rowGet (cancelShiftedLeadingTerm target reducer shift) k ≠ 0) :
    (rowGet (cancelShiftedLeadingTerm target reducer shift) k).natDegree +
        shift.getD k 0 ≤ t.shiftedDegree
```

`CompPoly.PolynomialMatrix.cancelShiftedLeadingTerm_entry_strict_of_pos_lt` (theorem, [line 604](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean#L604))

```lean
theorem cancelShiftedLeadingTerm_entry_strict_of_pos_lt
    {target reducer : PolynomialRow F} {shift : Array Nat}
    {t r : ShiftedLeadingTerm F}
    (ht : rowShiftedLeadingTerm? target shift = some t)
    (hr : rowShiftedLeadingTerm? reducer shift = some r)
    (hpos : t.position = r.position)
    (hle : r.shiftedDegree ≤ t.shiftedDegree)
    (hsize : reducer.size = target.size)
    {k : Nat} (hk : k < target.size) (hposlt : t.position < k)
    (hne : rowGet (cancelShiftedLeadingTerm target reducer shift) k ≠ 0) :
    (rowGet (cancelShiftedLeadingTerm target reducer shift) k).natDegree +
        shift.getD k 0 < t.shiftedDegree
```

## Depends on

- [Mulders-Storjohann Shifted Row Reduction](../muldersstorjohann.md)

## Proof depends on

- [Mulders-Storjohann Correctness Row and Row-Span Helpers](rowops.md)
- [Degrees and degree bounds under `toPoly`](../../../univariate/part-02/topoly/degree.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/MuldersStorjohannCorrectness/Leading.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.MuldersStorjohannCorrectness.Leading.json)
