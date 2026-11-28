---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.RowApproximates, CompPoly.PolynomialMatrix.Approximant.truncateX_eq_zero_iff_X_pow_dvd, CompPoly.PolynomialMatrix.Approximant.truncateX_zero_eq_zero, CompPoly.PolynomialMatrix.Approximant.pm_toPoly_finset_sum, CompPoly.PolynomialMatrix.Approximant.rowGet_rowMulMatrixWith_toPoly, CompPoly.PolynomialMatrix.Approximant.rowApproximates_iff, CompPoly.PolynomialMatrix.Approximant.rowApproximates_rowSub, CompPoly.PolynomialMatrix.Approximant.polynomialScaleCoeffX_toPoly, CompPoly.PolynomialMatrix.Approximant.rowApproximates_rowScaleCoeffX, CompPoly.PolynomialMatrix.Approximant.rowApproximates_cancelKernelLeafLeadingTerm, CompPoly.PolynomialMatrix.Approximant.insertKernelLeafPivotRowWithFuel_approximates, CompPoly.PolynomialMatrix.Approximant.pivotRows_approximates, CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots_approximates, CompPoly.PolynomialMatrix.Approximant.compactNonzeroRows_subset, CompPoly.PolynomialMatrix.Approximant.compactNonzeroRows_nonzero, CompPoly.PolynomialMatrix.Approximant.coeffXPower_toPoly, CompPoly.PolynomialMatrix.Approximant.rowApproximates_monomialUnitRow, CompPoly.PolynomialMatrix.Approximant.getD_le_maxOrder, CompPoly.PolynomialMatrix.Approximant.missingCompletionRows_approximates, CompPoly.PolynomialMatrix.Approximant.completeMissingPivotRows_approximates, CompPoly.PolynomialMatrix.Approximant.divXTrunc_coeff, CompPoly.PolynomialMatrix.Approximant.rowMulMatrixWith_ctx, CompPoly.PolynomialMatrix.Approximant.natArray_map_getD, CompPoly.PolynomialMatrix.Approximant.matrixWidth_eq_of_first_row, CompPoly.PolynomialMatrix.Approximant.getD_mem_matrixRows, CompPoly.PolynomialMatrix.Approximant.rowApproximates_composed
statement: formalized
proof: formalized
---

# X-Adic Row Soundness Toolkit

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.XAdicSoundness`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean), by Valerii Huhnin.

> The `RowApproximates` predicate, its divisibility characterization, closure
> under the row operations used by the leaf reduction and completion steps, and
> the soundness of one divide-and-conquer composition step.

> ## X-adic row soundness toolkit
>
> Semantic tools for proving that every row produced by the recursive PM-basis
> driver satisfies the X-adic approximant conditions.  Soundness is phrased via
> `X^order` divisibility of the `toPoly` image, which makes it closed under the
> row operations used by the reduction, completion, and composition steps.

`CompPoly.PolynomialMatrix.Approximant.RowApproximates` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L44))

> A row approximates an X-adic problem when every column product vanishes to
> the required order.

```lean
def RowApproximates (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) (row : PolynomialRow F) : Prop
```

`CompPoly.PolynomialMatrix.Approximant.truncateX_eq_zero_iff_X_pow_dvd` (theorem, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L51))

> Truncation vanishes exactly on `X^order`-multiples under `toPoly`.

```lean
theorem truncateX_eq_zero_iff_X_pow_dvd (order : Nat) (p : CPolynomial F) :
    truncateX order p = 0 ↔ (Polynomial.X : Polynomial F) ^ order ∣ p.toPoly
```

`CompPoly.PolynomialMatrix.Approximant.truncateX_zero_eq_zero` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L71))

> Truncation of the zero polynomial is zero.

```lean
theorem truncateX_zero_eq_zero (order : Nat) :
    truncateX (F := F) order 0 = 0
```

`CompPoly.PolynomialMatrix.Approximant.pm_toPoly_finset_sum` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L87))

> `toPoly` commutes with finite range sums.

```lean
theorem pm_toPoly_finset_sum (f : Nat → CPolynomial F) (n : Nat) :
    (∑ k ∈ Finset.range n, f k).toPoly = ∑ k ∈ Finset.range n, (f k).toPoly
```

`CompPoly.PolynomialMatrix.Approximant.rowGet_rowMulMatrixWith_toPoly` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L110))

> Column entries of a row-by-matrix product as sums over the matrix height,
> under `toPoly`.

```lean
theorem rowGet_rowMulMatrixWith_toPoly (mulCtx : CPolynomial.MulContext F)
    (row : PolynomialRow F) (M : PolynomialMatrix F) {j : Nat}
    (hj : j < MatrixWidth M) :
    (rowGet (rowMulMatrixWith mulCtx row M) j).toPoly =
      ∑ k ∈ Finset.range M.size,
        (rowGet row k).toPoly * (rowGet (M.getD k #[]) j).toPoly
```

`CompPoly.PolynomialMatrix.Approximant.rowApproximates_iff` (theorem, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L150))

> Divisibility form of the approximant condition, one column at a time.

```lean
theorem rowApproximates_iff (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) (row : PolynomialRow F) :
    RowApproximates mulCtx problem row ↔
      ∀ j, j < problem.orders.size → j < MatrixWidth problem.matrix →
        (Polynomial.X : Polynomial F) ^ (problem.orders.getD j 0) ∣
          ∑ k ∈ Finset.range problem.matrix.size,
            (rowGet row k).toPoly *
              (rowGet (problem.matrix.getD k #[]) j).toPoly
```

`CompPoly.PolynomialMatrix.Approximant.rowApproximates_rowSub` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L173))

> Row subtraction preserves the approximant condition.

```lean
theorem rowApproximates_rowSub (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) {a b : PolynomialRow F}
    (ha : RowApproximates mulCtx problem a)
    (hb : RowApproximates mulCtx problem b) :
    RowApproximates mulCtx problem (rowSub a b)
```

`CompPoly.PolynomialMatrix.Approximant.polynomialScaleCoeffX_toPoly` (theorem, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L201))

> Coefficient-shift scaling under `toPoly`.

```lean
theorem polynomialScaleCoeffX_toPoly (c : F) (d : Nat) (p : CPolynomial F) :
    (polynomialScaleCoeffX c d p).toPoly =
      Polynomial.C c * Polynomial.X ^ d * p.toPoly
```

`CompPoly.PolynomialMatrix.Approximant.rowApproximates_rowScaleCoeffX` (theorem, [line 269](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L269))

> Coefficient-shift row scaling preserves the approximant condition.

```lean
theorem rowApproximates_rowScaleCoeffX (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) {row : PolynomialRow F} (c : F) (d : Nat)
    (h : RowApproximates mulCtx problem row) :
    RowApproximates mulCtx problem (rowScaleCoeffX c d row)
```

`CompPoly.PolynomialMatrix.Approximant.rowApproximates_cancelKernelLeafLeadingTerm` (theorem, [line 288](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L288))

> Leading-term cancellation preserves the approximant condition.

```lean
theorem rowApproximates_cancelKernelLeafLeadingTerm
    (mulCtx : CPolynomial.MulContext F) (problem : XAdicProblem F)
    {target reducer : PolynomialRow F} (shift : Array Nat)
    (htarget : RowApproximates mulCtx problem target)
    (hreducer : RowApproximates mulCtx problem reducer) :
    RowApproximates mulCtx problem
      (cancelKernelLeafLeadingTerm target reducer shift)
```

`CompPoly.PolynomialMatrix.Approximant.insertKernelLeafPivotRowWithFuel_approximates` (theorem, [line 307](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L307))

> Pivot-table insertion preserves the approximant condition of all stored
> rows.

```lean
theorem insertKernelLeafPivotRowWithFuel_approximates
    (mulCtx : CPolynomial.MulContext F) (problem : XAdicProblem F) :
    ∀ (fuel : Nat) (pivots : Array (Option (PolynomialRow F)))
      (shift : Array Nat) (row : PolynomialRow F),
      (∀ p r, pivots.getD p none = some r → RowApproximates mulCtx problem r) →
      RowApproximates mulCtx problem row →
      ∀ p r,
        (insertKernelLeafPivotRowWithFuel fuel pivots shift row).getD p none =
          some r →
        RowApproximates mulCtx problem r
```

`CompPoly.PolynomialMatrix.Approximant.pivotRows_approximates` (theorem, [line 383](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L383))

> Rows extracted from a sound pivot table satisfy the approximant
> condition.

```lean
theorem pivotRows_approximates (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) {pivots : Array (Option (PolynomialRow F))}
    (hpivots : ∀ p r, pivots.getD p none = some r →
      RowApproximates mulCtx problem r)
    {row : PolynomialRow F} (hrow : row ∈ MatrixRows (pivotRows pivots)) :
    RowApproximates mulCtx problem row
```

`CompPoly.PolynomialMatrix.Approximant.reduceKernelLeafRowsByPivots_approximates` (theorem, [line 401](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L401))

> Pivot-table reduction preserves the approximant condition.

```lean
theorem reduceKernelLeafRowsByPivots_approximates
    (mulCtx : CPolynomial.MulContext F) (problem : XAdicProblem F)
    {rows : PolynomialMatrix F} (shift : Array Nat)
    (hrows : ∀ row, row ∈ MatrixRows rows → RowApproximates mulCtx problem row)
    {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (reduceKernelLeafRowsByPivots rows shift)) :
    RowApproximates mulCtx problem row
```

`CompPoly.PolynomialMatrix.Approximant.compactNonzeroRows_subset` (theorem, [line 446](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L446))

> Compaction preserves row membership soundness.

```lean
theorem compactNonzeroRows_subset {rows : PolynomialMatrix F}
    {row : PolynomialRow F} (hrow : row ∈ MatrixRows (compactNonzeroRows rows)) :
    row ∈ MatrixRows rows
```

`CompPoly.PolynomialMatrix.Approximant.compactNonzeroRows_nonzero` (theorem, [line 456](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L456))

> Compacted rows are nonzero.

```lean
theorem compactNonzeroRows_nonzero {rows : PolynomialMatrix F}
    {row : PolynomialRow F} (hrow : row ∈ MatrixRows (compactNonzeroRows rows)) :
    rowIsZero row = false
```

`CompPoly.PolynomialMatrix.Approximant.coeffXPower_toPoly` (theorem, [line 464](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L464))

> The monomial `coeffXPower c d` under `toPoly`.

```lean
theorem coeffXPower_toPoly (c : F) (d : Nat) :
    (coeffXPower c d).toPoly = Polynomial.C c * Polynomial.X ^ d
```

`CompPoly.PolynomialMatrix.Approximant.rowApproximates_monomialUnitRow` (theorem, [line 484](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L484))

> Monomial unit rows of sufficiently high degree satisfy every X-adic
> condition.

```lean
theorem rowApproximates_monomialUnitRow (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) {i d : Nat}
    (hd : ∀ j, j < problem.orders.size → problem.orders.getD j 0 ≤ d) :
    RowApproximates mulCtx problem
      (monomialUnitRow problem.matrix.size i d)
```

`CompPoly.PolynomialMatrix.Approximant.getD_le_maxOrder` (theorem, [line 518](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L518))

> Every entry of the order vector is bounded by `maxOrder`.

```lean
theorem getD_le_maxOrder (problem : XAdicProblem F) {j : Nat}
    (hj : j < problem.orders.size) :
    problem.orders.getD j 0 ≤ maxOrder problem
```

`CompPoly.PolynomialMatrix.Approximant.missingCompletionRows_approximates` (theorem, [line 553](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L553))

> Missing-pivot completion rows satisfy every X-adic condition.

```lean
theorem missingCompletionRows_approximates (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) (shift : Array Nat) (rows : PolynomialMatrix F)
    {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (missingCompletionRows problem shift rows)) :
    RowApproximates mulCtx problem row
```

`CompPoly.PolynomialMatrix.Approximant.completeMissingPivotRows_approximates` (theorem, [line 568](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L568))

> Pivot completion preserves the approximant condition.

```lean
theorem completeMissingPivotRows_approximates (mulCtx : CPolynomial.MulContext F)
    (problem : XAdicProblem F) (shift : Array Nat) {rows : PolynomialMatrix F}
    (hrows : ∀ row, row ∈ MatrixRows rows → RowApproximates mulCtx problem row)
    {row : PolynomialRow F}
    (hrow : row ∈ MatrixRows (completeMissingPivotRows problem shift rows)) :
    RowApproximates mulCtx problem row
```

> ## Composition soundness

`CompPoly.PolynomialMatrix.Approximant.divXTrunc_coeff` (theorem, [line 582](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L582))

> Coefficients of the shifted truncation `divXTrunc`.

```lean
theorem divXTrunc_coeff (shift order : Nat) (p : CPolynomial F) (t : Nat) :
    CPolynomial.coeff (divXTrunc shift order p) t =
      if t < order then CPolynomial.coeff p (t + shift) else 0
```

`CompPoly.PolynomialMatrix.Approximant.rowMulMatrixWith_ctx` (theorem, [line 593](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L593))

> The row-by-matrix product does not depend on the multiplication context.

```lean
theorem rowMulMatrixWith_ctx (ctx₁ ctx₂ : CPolynomial.MulContext F)
    (row : PolynomialRow F) (M : PolynomialMatrix F) :
    rowMulMatrixWith ctx₁ row M = rowMulMatrixWith ctx₂ row M
```

`CompPoly.PolynomialMatrix.Approximant.natArray_map_getD` (theorem, [line 604](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L604))

> `getD` of a mapped natural-number array at an in-bounds index.

```lean
theorem natArray_map_getD (f : Nat → Nat) (a : Array Nat) {j : Nat}
    (hj : j < a.size) :
    (a.map f).getD j 0 = f (a.getD j 0)
```

`CompPoly.PolynomialMatrix.Approximant.matrixWidth_eq_of_first_row` (theorem, [line 613](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L613))

> A nonempty matrix with uniform row width `n` has `MatrixWidth` `n`.

```lean
theorem matrixWidth_eq_of_first_row {M : PolynomialMatrix F} {n : Nat}
    (hne : 0 < M.size)
    (hsize : ∀ r ∈ MatrixRows M, r.size = n) :
    MatrixWidth M = n
```

`CompPoly.PolynomialMatrix.Approximant.getD_mem_matrixRows` (theorem, [line 622](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L622))

> In-bounds `getD` rows are matrix rows.

```lean
theorem getD_mem_matrixRows {M : PolynomialMatrix F} {l : Nat}
    (hl : l < M.size) : M.getD l #[] ∈ MatrixRows M
```

`CompPoly.PolynomialMatrix.Approximant.rowApproximates_composed` (theorem, [line 677](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean#L677))

> Soundness of one PM-basis composition step: a residual-approximant row
> times a lower-approximant basis approximates the full problem.

```lean
theorem rowApproximates_composed (mulCtx : CPolynomial.MulContext F)
    {problem : XAdicProblem F} {d₁ : Nat}
    {P₁ Rmat : PolynomialMatrix F}
    (hP₁ : ∀ r ∈ MatrixRows P₁,
      RowApproximates mulCtx
        { orders := lowerOrders problem d₁, matrix := problem.matrix } r ∧
      r.size = problem.matrix.size)
    (hRsize : Rmat.size = P₁.size)
    (hRwidth : 0 < P₁.size → MatrixWidth problem.matrix ≤ MatrixWidth Rmat)
    (hR : ∀ l j, l < P₁.size → j < problem.orders.size →
      j < MatrixWidth problem.matrix →
      ∀ t, t < problem.orders.getD j 0 - d₁ →
        CPolynomial.coeff (rowGet (Rmat.getD l #[]) j) t =
          CPolynomial.coeff
            (rowGet (rowMulMatrixWith mulCtx (P₁.getD l #[]) problem.matrix) j)
            (t + d₁))
    {p₂ : PolynomialRow F}
    (hp₂ : RowApproximates mulCtx
      { orders := residualOrders problem d₁, matrix := Rmat } p₂) :
    RowApproximates mulCtx problem (rowMulMatrixWith mulCtx p₂ P₁)
```

## Depends on

- [Scalar Kernel-Leaf PM-Basis Definitions](kernelleaf.md)

## Proof depends on

- [Mulders-Storjohann Correctness Row and Row-Span Helpers](../../muldersstorjohanncorrectness/rowops.md)
- [Strassen Polynomial-Matrix Product Correctness](../../strassencorrectness.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis/XAdicSoundness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.XAdicSoundness.json)
