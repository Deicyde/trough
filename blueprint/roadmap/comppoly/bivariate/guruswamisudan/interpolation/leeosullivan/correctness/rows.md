---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.coeff_ofCoeffRow_rowLinearCombination_lee_of_lt, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_coeff_eq_zero_of_width_le, CompPoly.GuruswamiSudan.LeeOSullivan.coeff_koetterBasisCombination_lee_eq_zero_of_width_le, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_rowLinearCombination_lee_eq_combination, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_rowSpan_lee_spanContains, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_add_weights, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_neg_weights, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisSpanContains_add, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisSpanContains_neg, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisSpanContains_sub, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_single_weight, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisSpanContains_single, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_congr_weights, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_toCoeffRow_eq_of_width_le, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_lee_rowSpan_of_spanContains, CompPoly.GuruswamiSudan.LeeOSullivan.coeff_ofCoeffRow_rowGet, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_matrix_getD_semantic_rowSpan, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_eq_zero_of_rowShiftedDegree?_none, CompPoly.GuruswamiSudan.LeeOSullivan.rowSpan_lee_row_size, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_rowSpan_lee_coeff_eq_zero_of_width_le, CompPoly.GuruswamiSudan.LeeOSullivan.natWeightedDegree_ofCoeffRow_le_of_lee_rowShiftedDegree?_le, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_ne_zero_of_rowShiftedDegree?_some, CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_koetterBasisCombination, CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_satisfiesMultiplicityConstraints, CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_rowSpan_lee_satisfiesMultiplicityConstraints
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Row-Span Transport Helpers

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Rows`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean), by Valerii Huhnin.

> Transport between executable polynomial rows and semantic bivariate span combinations.

`CompPoly.GuruswamiSudan.LeeOSullivan.coeff_ofCoeffRow_rowLinearCombination_lee_of_lt` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L33))

> Within the Lee row width, a row-linear combination of executable Lee rows
> has the same coefficients as the corresponding bivariate basis combination.

```lean
theorem coeff_ofCoeffRow_rowLinearCombination_lee_of_lt
    (R G : CPolynomial F) (params : GSInterpParams)
    (coeffs : Array (CPolynomial F)) {k j : Nat}
    (hj : j < leeOSullivanWidth params) :
    CBivariate.coeff
        (CBivariate.ofCoeffRow
          (rowLinearCombination coeffs
            (leeOSullivanBasisRowsWithRG R G params))) k j =
      CBivariate.coeff
        (koetterBasisCombination (fun i ↦ coeffs.getD i 0)
          (leeOSullivanBasisPolynomials (F := F) R G params)) k j
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanBasisPolynomial_coeff_eq_zero_of_width_le` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L74))

> Lee basis polynomials are bounded by the Lee row width in `Y`.

```lean
theorem leeOSullivanBasisPolynomial_coeff_eq_zero_of_width_le
    (R G : CPolynomial F) (params : GSInterpParams) {idx x j : Nat}
    (hidx : idx < leeOSullivanWidth params) (hj : leeOSullivanWidth params ≤ j) :
    CBivariate.coeff (leeOSullivanBasisPolynomial R G params idx) x j = 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.coeff_koetterBasisCombination_lee_eq_zero_of_width_le` (theorem, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L146))

> Bivariate combinations of Lee basis polynomials are bounded by the Lee row
> width in `Y`.

```lean
theorem coeff_koetterBasisCombination_lee_eq_zero_of_width_le
    (R G : CPolynomial F) (params : GSInterpParams)
    (weights : Nat → CPolynomial F) {x j : Nat}
    (hj : leeOSullivanWidth params ≤ j) :
    CBivariate.coeff
        (koetterBasisCombination weights
          (leeOSullivanBasisPolynomials (F := F) R G params)) x j = 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_rowLinearCombination_lee_eq_combination` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L173))

> A polynomial-row linear combination of the executable Lee rows represents
> the same bivariate polynomial as the corresponding Lee basis combination.

```lean
theorem ofCoeffRow_rowLinearCombination_lee_eq_combination
    (R G : CPolynomial F) (params : GSInterpParams)
    (coeffs : Array (CPolynomial F)) :
    CBivariate.ofCoeffRow
        (rowLinearCombination coeffs
          (leeOSullivanBasisRowsWithRG R G params)) =
      koetterBasisCombination (fun i ↦ coeffs.getD i 0)
        (leeOSullivanBasisPolynomials (F := F) R G params)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_rowSpan_lee_spanContains` (theorem, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L202))

> A row in the executable Lee row span represents a bivariate polynomial in
> the corresponding Lee basis span.

```lean
theorem ofCoeffRow_rowSpan_lee_spanContains
    (R G : CPolynomial F) (params : GSInterpParams) {row : PolynomialRow F}
    (hrow : row ∈ RowSpan (leeOSullivanBasisRowsWithRG R G params)) :
    koetterBasisSpanContains
      (leeOSullivanBasisPolynomials (F := F) R G params)
      (CBivariate.ofCoeffRow row)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_add_weights` (theorem, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L214))

```lean
theorem koetterBasisCombination_add_weights
    (weights₁ weights₂ : Nat → CPolynomial F) (basis : Array (CBivariate F)) :
    koetterBasisCombination (fun idx ↦ weights₁ idx + weights₂ idx) basis =
      koetterBasisCombination weights₁ basis +
        koetterBasisCombination weights₂ basis
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_neg_weights` (theorem, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L235))

```lean
theorem koetterBasisCombination_neg_weights
    (weights : Nat → CPolynomial F) (basis : Array (CBivariate F)) :
    koetterBasisCombination (fun idx ↦ -weights idx) basis =
      -koetterBasisCombination weights basis
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisSpanContains_add` (theorem, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L249))

```lean
theorem koetterBasisSpanContains_add
    {basis : Array (CBivariate F)} {P Q : CBivariate F}
    (hP : koetterBasisSpanContains basis P)
    (hQ : koetterBasisSpanContains basis Q) :
    koetterBasisSpanContains basis (P + Q)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisSpanContains_neg` (theorem, [line 259](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L259))

```lean
theorem koetterBasisSpanContains_neg
    {basis : Array (CBivariate F)} {P : CBivariate F}
    (hP : koetterBasisSpanContains basis P) :
    koetterBasisSpanContains basis (-P)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisSpanContains_sub` (theorem, [line 267](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L267))

```lean
theorem koetterBasisSpanContains_sub
    {basis : Array (CBivariate F)} {P Q : CBivariate F}
    (hP : koetterBasisSpanContains basis P)
    (hQ : koetterBasisSpanContains basis Q) :
    koetterBasisSpanContains basis (P - Q)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_single_weight` (theorem, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L275))

```lean
theorem koetterBasisCombination_single_weight
    (basis : Array (CBivariate F)) {idx : Nat} (hidx : idx < basis.size)
    (weight : CPolynomial F) :
    koetterBasisCombination
        (fun j ↦ if j == idx then weight else 0) basis =
      CBivariate.ofYConstant weight * basis.getD idx 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisSpanContains_single` (theorem, [line 311](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L311))

```lean
theorem koetterBasisSpanContains_single
    (basis : Array (CBivariate F)) {idx : Nat} (hidx : idx < basis.size)
    (weight : CPolynomial F) :
    koetterBasisSpanContains basis
      (CBivariate.ofYConstant weight * basis.getD idx 0)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_congr_weights` (theorem, [line 319](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L319))

```lean
theorem koetterBasisCombination_congr_weights
    {basis : Array (CBivariate F)} {weights₁ weights₂ : Nat → CPolynomial F}
    (hweights : ∀ idx, idx < basis.size → weights₁ idx = weights₂ idx) :
    koetterBasisCombination weights₁ basis =
      koetterBasisCombination weights₂ basis
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_toCoeffRow_eq_of_width_le` (theorem, [line 330](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L330))

```lean
theorem ofCoeffRow_toCoeffRow_eq_of_width_le
    {width : Nat} {Q : CBivariate F}
    (hY : ∀ i j, width ≤ j → CBivariate.coeff Q i j = 0) :
    CBivariate.ofCoeffRow (CBivariate.toCoeffRow width Q) = Q
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_lee_rowSpan_of_spanContains` (theorem, [line 346](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L346))

```lean
theorem ofCoeffRow_lee_rowSpan_of_spanContains
    (R G : CPolynomial F) (params : GSInterpParams) {Q : CBivariate F}
    (hspan :
      koetterBasisSpanContains
        (leeOSullivanBasisPolynomials (F := F) R G params) Q) :
    ∃ row,
      row ∈ RowSpan (leeOSullivanBasisRowsWithRG R G params) ∧
        CBivariate.ofCoeffRow row = Q
```

`CompPoly.GuruswamiSudan.LeeOSullivan.coeff_ofCoeffRow_rowGet` (theorem, [line 405](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L405))

```lean
theorem coeff_ofCoeffRow_rowGet
    (row : PolynomialRow F) (i j : Nat) :
    CBivariate.coeff (CBivariate.ofCoeffRow row) i j =
      CPolynomial.coeff (rowGet row j) i
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_matrix_getD_semantic_rowSpan` (theorem, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L441))

```lean
theorem ofCoeffRow_matrix_getD_semantic_rowSpan
    (M : PolynomialMatrix F) {i : Nat} (hi : i < M.size) :
    ∃ spanRow,
      spanRow ∈ RowSpan M ∧
        CBivariate.ofCoeffRow spanRow =
          CBivariate.ofCoeffRow (M.getD i #[])
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_eq_zero_of_rowShiftedDegree?_none` (theorem, [line 453](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L453))

```lean
theorem ofCoeffRow_eq_zero_of_rowShiftedDegree?_none
    {row : PolynomialRow F} {shift : Array Nat}
    (hdeg : rowShiftedDegree? row shift = none) :
    CBivariate.ofCoeffRow row = 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.rowSpan_lee_row_size` (theorem, [line 471](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L471))

```lean
theorem rowSpan_lee_row_size
    (R G : CPolynomial F) (params : GSInterpParams) {row : PolynomialRow F}
    (hrow : row ∈ RowSpan (leeOSullivanBasisRowsWithRG R G params)) :
    row.size = leeOSullivanWidth params
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_rowSpan_lee_coeff_eq_zero_of_width_le` (theorem, [line 482](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L482))

```lean
theorem ofCoeffRow_rowSpan_lee_coeff_eq_zero_of_width_le
    (R G : CPolynomial F) (params : GSInterpParams) {row : PolynomialRow F}
    (hrow : row ∈ RowSpan (leeOSullivanBasisRowsWithRG R G params))
    {i j : Nat} (hj : leeOSullivanWidth params ≤ j) :
    CBivariate.coeff (CBivariate.ofCoeffRow row) i j = 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.natWeightedDegree_ofCoeffRow_le_of_lee_rowShiftedDegree?_le` (theorem, [line 492](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L492))

```lean
theorem natWeightedDegree_ofCoeffRow_le_of_lee_rowShiftedDegree?_le
    (params : GSInterpParams) (row : PolynomialRow F) {degree : Nat}
    (hdeg : rowShiftedDegree? row (leeOSullivanShifts params) = some degree)
    (hle : degree ≤ params.weightedDegreeBound)
    (hYBound :
      ∀ i j, leeOSullivanWidth params ≤ j →
        CBivariate.coeff (CBivariate.ofCoeffRow row) i j = 0) :
    CBivariate.natWeightedDegree (CBivariate.ofCoeffRow row) 1 (yWeight params) ≤
      params.weightedDegreeBound
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_ne_zero_of_rowShiftedDegree?_some` (theorem, [line 537](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L537))

```lean
theorem ofCoeffRow_ne_zero_of_rowShiftedDegree?_some
    {row : PolynomialRow F} {shift : Array Nat} {degree : Nat}
    (hdeg : rowShiftedDegree? row shift = some degree) :
    CBivariate.ofCoeffRow row ≠ 0
```

`CompPoly.GuruswamiSudan.LeeOSullivan.hasMultiplicityAtLeast_koetterBasisCombination` (theorem, [line 570](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L570))

> A `Y`-constant linear combination of basis entries satisfying a pointwise
> multiplicity constraint satisfies that constraint.

```lean
theorem hasMultiplicityAtLeast_koetterBasisCombination
    (weights : Nat → CPolynomial F) (basis : Array (CBivariate F))
    {x y : F} {m : Nat}
    (hbasis :
      ∀ idx, idx < basis.size →
        CBivariate.HasMultiplicityAtLeast (basis.getD idx 0) x y m) :
    CBivariate.HasMultiplicityAtLeast
      (koetterBasisCombination weights basis) x y m
```

`CompPoly.GuruswamiSudan.LeeOSullivan.koetterBasisCombination_satisfiesMultiplicityConstraints` (theorem, [line 613](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L613))

> A `Y`-constant linear combination of basis entries satisfying all packed
> multiplicity constraints satisfies the same packed constraints.

```lean
theorem koetterBasisCombination_satisfiesMultiplicityConstraints
    (weights : Nat → CPolynomial F) (basis : Array (CBivariate F))
    {points : Array (F × F)} {m : Nat}
    (hbasis :
      ∀ idx, idx < basis.size →
        CBivariate.SatisfiesMultiplicityConstraints
          (basis.getD idx 0) points m) :
    CBivariate.SatisfiesMultiplicityConstraints
      (koetterBasisCombination weights basis) points m
```

`CompPoly.GuruswamiSudan.LeeOSullivan.ofCoeffRow_rowSpan_lee_satisfiesMultiplicityConstraints` (theorem, [line 629](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean#L629))

> Any executable row in the Lee row span represents a bivariate polynomial
> satisfying the packed multiplicity constraints, provided every Lee basis entry
> does.

```lean
theorem ofCoeffRow_rowSpan_lee_satisfiesMultiplicityConstraints
    (R G : CPolynomial F) (params : GSInterpParams)
    {points : Array (F × F)} {row : PolynomialRow F}
    (hbasis :
      ∀ idx, idx < (leeOSullivanBasisPolynomials (F := F) R G params).size →
        CBivariate.SatisfiesMultiplicityConstraints
          ((leeOSullivanBasisPolynomials (F := F) R G params).getD idx 0)
          points params.multiplicity)
    (hrow : row ∈ RowSpan (leeOSullivanBasisRowsWithRG R G params)) :
    CBivariate.SatisfiesMultiplicityConstraints
      (CBivariate.ofCoeffRow row) points params.multiplicity
```

## Depends on

- [Generic Basis Combination Helpers](combinations.md)
- [Lee-O'Sullivan Correctness Common Helpers](common.md)
- [Row Span for Polynomial Matrices](../../../../../linearalgebra/polynomialmatrix/rowspan.md)

## Proof depends on

- [Lee-O'Sullivan Basis Correctness Helpers](basis.md)
- [Mulders-Storjohann Correctness Row Combination Helpers](../../../../../linearalgebra/polynomialmatrix/muldersstorjohanncorrectness/combinations.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Correctness/Rows.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Correctness.Rows.json)
