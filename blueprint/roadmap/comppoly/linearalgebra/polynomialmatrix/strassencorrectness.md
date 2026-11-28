---
catalog: module
lean: CompPoly.PolynomialMatrix.le_nextPowerOfTwoAtLeast, CompPoly.PolynomialMatrix.natArraySlice_getD, CompPoly.PolynomialMatrix.maxNatArrays_getD, CompPoly.PolynomialMatrix.rowGet_of_size_le, CompPoly.PolynomialMatrix.truncateX_zero, CompPoly.PolynomialMatrix.truncateX_add, CompPoly.PolynomialMatrix.truncateX_sub, CompPoly.PolynomialMatrix.truncateX_truncateX, CompPoly.PolynomialMatrix.truncateX_sum, CompPoly.PolynomialMatrix.truncateX_mul_of_productCoeffCap_le, CompPoly.PolynomialMatrix.ofFn_size, CompPoly.PolynomialMatrix.getD_ofFn, CompPoly.PolynomialMatrix.rowGet_ofFn, CompPoly.PolynomialMatrix.MatrixWidth_ofFn, CompPoly.PolynomialMatrix.MatrixWidth_ofFn_square, CompPoly.PolynomialMatrix.ofFn_congr, CompPoly.PolynomialMatrix.rowMulMatrixWith_size, CompPoly.PolynomialMatrix.rowGet_rowMulMatrixWith, CompPoly.PolynomialMatrix.rowGet_rowMulMatrixWith_of_width_le, CompPoly.PolynomialMatrix.mulWith_eq_ofFn, CompPoly.PolynomialMatrix.mulWith_size, CompPoly.PolynomialMatrix.mulWith_getD, CompPoly.PolynomialMatrix.matrixRows_mulWith, CompPoly.PolynomialMatrix.rowMulMatrixBoundedWith_eq_rowMulMatrixWith, CompPoly.PolynomialMatrix.mulBoundedWith_eq_mulWith, CompPoly.PolynomialMatrix.rowGet_rowTruncateColumns, CompPoly.PolynomialMatrix.truncateColumns_size, CompPoly.PolynomialMatrix.truncateColumns_getD, CompPoly.PolynomialMatrix.rowMulMatrixTruncColumnWith_eq, CompPoly.PolynomialMatrix.mulTruncColumnWith_eq, CompPoly.PolynomialMatrix.add_ofFn, CompPoly.PolynomialMatrix.sub_ofFn, CompPoly.PolynomialMatrix.mulWith_ofFn_ofFn, CompPoly.PolynomialMatrix.truncateColumns_ofFn, CompPoly.PolynomialMatrix.mulStrassenWithFuel_eq_mulWith, CompPoly.PolynomialMatrix.mulStrassenWith_eq_mulWith, CompPoly.PolynomialMatrix.mulStrassenWith_size, CompPoly.PolynomialMatrix.mulStrassenWith_getD, CompPoly.PolynomialMatrix.matrixRows_mulStrassenWith, CompPoly.PolynomialMatrix.mulTruncColumnStrassenWithFuel_eq_truncateColumns, CompPoly.PolynomialMatrix.mulTruncColumnStrassenWith_eq_truncateColumns, CompPoly.PolynomialMatrix.mulTruncColumnStrassenWith_size, CompPoly.PolynomialMatrix.mulTruncColumnStrassenWith_entry
statement: formalized
proof: formalized
---

# Strassen Polynomial-Matrix Product Correctness

`CompPoly.LinearAlgebra.PolynomialMatrix.StrassenCorrectness`, in [CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean), by Valerii Huhnin.

> Correctness proofs for the Strassen-style polynomial-matrix products in
> `CompPoly.LinearAlgebra.PolynomialMatrix.Operations`:
>
> * `rowGet_rowMulMatrixWith`: entry semantics of the naive row-by-matrix product.
> * `mulBoundedWith_eq_mulWith`: the degree-capped low-product reconstruction equals
>   the naive product.
> * `mulStrassenWith_eq_mulWith` and `mulStrassenWithFuel_eq_mulWith`: the Strassen
>   recursion computes exactly the naive matrix product, as arrays.
> * `mulTruncColumnStrassenWith_eq_truncateColumns` and
>   `mulTruncColumnStrassenWith_entry`: the column-truncated Strassen recursion
>   computes exactly the column-truncated naive product.

> ## Generic array and fold helpers

`CompPoly.PolynomialMatrix.le_nextPowerOfTwoAtLeast` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L99))

> `nextPowerOfTwoAtLeast` is at least its target.

```lean
theorem le_nextPowerOfTwoAtLeast (target : Nat) :
    target ≤ nextPowerOfTwoAtLeast target
```

`CompPoly.PolynomialMatrix.natArraySlice_getD` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L104))

> Entry access for `natArraySlice`.

```lean
theorem natArraySlice_getD (values : Array Nat) (start count j : Nat) :
    (natArraySlice values start count).getD j 0 =
      if j < count then values.getD (start + j) 0 else 0
```

`CompPoly.PolynomialMatrix.maxNatArrays_getD` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L110))

> Entry access for `maxNatArrays`.

```lean
theorem maxNatArrays_getD (a b : Array Nat) (j : Nat) :
    (maxNatArrays a b).getD j 0 = max (a.getD j 0) (b.getD j 0)
```

> ## Row access helpers

`CompPoly.PolynomialMatrix.rowGet_of_size_le` (theorem, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L121))

> Reading a row past its width yields zero.

```lean
theorem rowGet_of_size_le [Zero F] {row : PolynomialRow F} {j : Nat}
    (hj : row.size ≤ j) : rowGet row j = 0
```

> ## `truncateX` algebra

`CompPoly.PolynomialMatrix.truncateX_zero` (theorem, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L137))

> Truncation of the zero polynomial.

```lean
theorem truncateX_zero [Semiring F] [BEq F] [LawfulBEq F] (order : Nat) :
    truncateX order (0 : CPolynomial F) = 0
```

`CompPoly.PolynomialMatrix.truncateX_add` (theorem, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L144))

> Truncation distributes over addition.

```lean
theorem truncateX_add [Semiring F] [BEq F] [LawfulBEq F] (order : Nat)
    (p q : CPolynomial F) :
    truncateX order (p + q) = truncateX order p + truncateX order q
```

`CompPoly.PolynomialMatrix.truncateX_sub` (theorem, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L155))

> Truncation distributes over subtraction.

```lean
theorem truncateX_sub [Ring F] [BEq F] [LawfulBEq F] (order : Nat)
    (p q : CPolynomial F) :
    truncateX order (p - q) = truncateX order p - truncateX order q
```

`CompPoly.PolynomialMatrix.truncateX_truncateX` (theorem, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L166))

> Nested truncations keep the smaller order.

```lean
theorem truncateX_truncateX [Semiring F] [BEq F] [LawfulBEq F] (o o' : Nat)
    (p : CPolynomial F) :
    truncateX o (truncateX o' p) = truncateX (min o o') p
```

`CompPoly.PolynomialMatrix.truncateX_sum` (theorem, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L179))

> Truncation distributes over finite range sums.

```lean
theorem truncateX_sum [Semiring F] [BEq F] [LawfulBEq F] (order n : Nat)
    (f : Nat → CPolynomial F) :
    truncateX order (∑ k ∈ Finset.range n, f k) =
      ∑ k ∈ Finset.range n, truncateX order (f k)
```

`CompPoly.PolynomialMatrix.truncateX_mul_of_productCoeffCap_le` (theorem, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L207))

> A product is unchanged by truncation past its coefficient cap.

```lean
theorem truncateX_mul_of_productCoeffCap_le [Semiring F] [BEq F] [LawfulBEq F]
    {p q : CPolynomial F} {order : Nat} (h : productCoeffCap p q ≤ order) :
    truncateX order (p * q) = p * q
```

> ## `ofFn` access toolkit

`CompPoly.PolynomialMatrix.ofFn_size` (theorem, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L226))

> Row count of `ofFn`.

```lean
theorem ofFn_size [Zero F] (rows width : Nat) (entry : Nat → Nat → CPolynomial F) :
    (ofFn rows width entry).size = rows
```

`CompPoly.PolynomialMatrix.getD_ofFn` (theorem, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L237))

> Row access for `ofFn` with zero defaults.

```lean
theorem getD_ofFn [Zero F] (rows width : Nat) (entry : Nat → Nat → CPolynomial F)
    (i : Nat) :
    (ofFn rows width entry).getD i #[] =
      if i < rows then ((List.range width).map (entry i)).toArray else #[]
```

`CompPoly.PolynomialMatrix.rowGet_ofFn` (theorem, [line 244](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L244))

> Entry access for `ofFn` with zero defaults.

```lean
theorem rowGet_ofFn [Zero F] (rows width : Nat) (entry : Nat → Nat → CPolynomial F)
    (i j : Nat) :
    rowGet ((ofFn rows width entry).getD i #[]) j =
      if i < rows ∧ j < width then entry i j else 0
```

`CompPoly.PolynomialMatrix.MatrixWidth_ofFn` (theorem, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L264))

> Width of `ofFn`.

```lean
theorem MatrixWidth_ofFn [Zero F] (rows width : Nat)
    (entry : Nat → Nat → CPolynomial F) :
    MatrixWidth (ofFn rows width entry) = if rows = 0 then 0 else width
```

`CompPoly.PolynomialMatrix.MatrixWidth_ofFn_square` (theorem, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L276))

> Width of a square `ofFn`.

```lean
theorem MatrixWidth_ofFn_square [Zero F] (n : Nat)
    (entry : Nat → Nat → CPolynomial F) :
    MatrixWidth (ofFn n n entry) = n
```

`CompPoly.PolynomialMatrix.ofFn_congr` (theorem, [line 283](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L283))

> Two `ofFn` matrices with entrywise-equal in-range entries are equal.

```lean
theorem ofFn_congr [Zero F] {rows width : Nat} {f g : Nat → Nat → CPolynomial F}
    (h : ∀ i < rows, ∀ j < width, f i j = g i j) :
    ofFn rows width f = ofFn rows width g
```

> ## Naive product semantics

`CompPoly.PolynomialMatrix.rowMulMatrixWith_size` (theorem, [line 304](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L304))

> Width of a naive row-by-matrix product.

```lean
theorem rowMulMatrixWith_size [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (row : PolynomialRow F)
    (M : PolynomialMatrix F) :
    (rowMulMatrixWith mulCtx row M).size = MatrixWidth M
```

`CompPoly.PolynomialMatrix.rowGet_rowMulMatrixWith` (theorem, [line 311](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L311))

> Entry semantics of the naive row-by-matrix product.

```lean
theorem rowGet_rowMulMatrixWith [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (row : PolynomialRow F)
    (M : PolynomialMatrix F) {j : Nat} (hj : j < MatrixWidth M) :
    rowGet (rowMulMatrixWith mulCtx row M) j =
      ∑ k ∈ Finset.range row.size, rowGet row k * rowGet (M.getD k #[]) j
```

`CompPoly.PolynomialMatrix.rowGet_rowMulMatrixWith_of_width_le` (theorem, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L320))

> The naive row-by-matrix product is zero past the matrix width.

```lean
theorem rowGet_rowMulMatrixWith_of_width_le [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (row : PolynomialRow F)
    (M : PolynomialMatrix F) {j : Nat} (hj : MatrixWidth M ≤ j) :
    rowGet (rowMulMatrixWith mulCtx row M) j = 0
```

`CompPoly.PolynomialMatrix.mulWith_eq_ofFn` (theorem, [line 350](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L350))

> The naive matrix product as an `ofFn` matrix of convolution sums.

```lean
theorem mulWith_eq_ofFn [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (A B : PolynomialMatrix F) :
    mulWith mulCtx A B =
      ofFn A.size (MatrixWidth B) (fun i j ↦
        ∑ k ∈ Finset.range B.size,
          rowGet (A.getD i #[]) k * rowGet (B.getD k #[]) j)
```

`CompPoly.PolynomialMatrix.mulWith_size` (theorem, [line 364](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L364))

> Row count of the naive matrix product.

```lean
theorem mulWith_size [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (A B : PolynomialMatrix F) :
    (mulWith mulCtx A B).size = A.size
```

`CompPoly.PolynomialMatrix.mulWith_getD` (theorem, [line 370](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L370))

> Rows of the naive matrix product.

```lean
theorem mulWith_getD [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (A B : PolynomialMatrix F) {i : Nat}
    (hi : i < A.size) :
    (mulWith mulCtx A B).getD i #[] = rowMulMatrixWith mulCtx (A.getD i #[]) B
```

`CompPoly.PolynomialMatrix.matrixRows_mulWith` (theorem, [line 377](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L377))

> Row list of the naive matrix product.

```lean
theorem matrixRows_mulWith [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (A B : PolynomialMatrix F) :
    MatrixRows (mulWith mulCtx A B) =
      (MatrixRows A).map fun row ↦ rowMulMatrixWith mulCtx row B
```

> ## Bounded product correctness

`CompPoly.PolynomialMatrix.rowMulMatrixBoundedWith_eq_rowMulMatrixWith` (theorem, [line 386](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L386))

> The degree-capped row product equals the naive row product.

```lean
theorem rowMulMatrixBoundedWith_eq_rowMulMatrixWith [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (row : PolynomialRow F) (M : PolynomialMatrix F) :
    rowMulMatrixBoundedWith lowCtx row M =
      rowMulMatrixWith lowCtx.mulContext row M
```

`CompPoly.PolynomialMatrix.mulBoundedWith_eq_mulWith` (theorem, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L402))

> The degree-capped matrix product equals the naive matrix product.

```lean
theorem mulBoundedWith_eq_mulWith [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (A B : PolynomialMatrix F) :
    mulBoundedWith lowCtx A B = mulWith lowCtx.mulContext A B
```

> ## Column-truncated naive product semantics

`CompPoly.PolynomialMatrix.rowGet_rowTruncateColumns` (theorem, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L412))

> Entry access for column truncation of a row.

```lean
theorem rowGet_rowTruncateColumns [Semiring F] [BEq F] [LawfulBEq F]
    (orders : Array Nat) (row : PolynomialRow F) (j : Nat) :
    rowGet (rowTruncateColumns orders row) j =
      truncateX (orders.getD j 0) (rowGet row j)
```

`CompPoly.PolynomialMatrix.truncateColumns_size` (theorem, [line 423](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L423))

> Row count of a column-truncated matrix.

```lean
theorem truncateColumns_size [Semiring F] [BEq F] [LawfulBEq F]
    (orders : Array Nat) (M : PolynomialMatrix F) :
    (truncateColumns orders M).size = M.size
```

`CompPoly.PolynomialMatrix.truncateColumns_getD` (theorem, [line 429](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L429))

> Rows of a column-truncated matrix.

```lean
theorem truncateColumns_getD [Semiring F] [BEq F] [LawfulBEq F]
    (orders : Array Nat) (M : PolynomialMatrix F) {i : Nat} (hi : i < M.size) :
    (truncateColumns orders M).getD i #[] =
      rowTruncateColumns orders (M.getD i #[])
```

`CompPoly.PolynomialMatrix.rowMulMatrixTruncColumnWith_eq` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L436))

> The truncated row product is the truncation of the naive row product.

```lean
theorem rowMulMatrixTruncColumnWith_eq [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (orders : Array Nat) (row : PolynomialRow F)
    (M : PolynomialMatrix F) :
    rowMulMatrixTruncColumnWith lowCtx orders row M =
      rowTruncateColumns orders (rowMulMatrixWith lowCtx.mulContext row M)
```

`CompPoly.PolynomialMatrix.mulTruncColumnWith_eq` (theorem, [line 450](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L450))

> The column-truncated product is the truncation of the naive product.

```lean
theorem mulTruncColumnWith_eq [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (orders : Array Nat) (A B : PolynomialMatrix F) :
    mulTruncColumnWith lowCtx orders A B =
      truncateColumns orders (mulWith lowCtx.mulContext A B)
```

> ## Structural `ofFn` rewrites for the block combinators

`CompPoly.PolynomialMatrix.add_ofFn` (theorem, [line 462](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L462))

> Pointwise addition of equally shaped `ofFn` matrices.

```lean
theorem add_ofFn [Semiring F] [BEq F] [LawfulBEq F] (rows width : Nat)
    (f g : Nat → Nat → CPolynomial F) :
    add (ofFn rows width f) (ofFn rows width g) =
      ofFn rows width (fun i j ↦ f i j + g i j)
```

`CompPoly.PolynomialMatrix.sub_ofFn` (theorem, [line 474](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L474))

> Pointwise subtraction of equally shaped `ofFn` matrices.

```lean
theorem sub_ofFn [Ring F] [BEq F] [LawfulBEq F] (rows width : Nat)
    (f g : Nat → Nat → CPolynomial F) :
    sub (ofFn rows width f) (ofFn rows width g) =
      ofFn rows width (fun i j ↦ f i j - g i j)
```

`CompPoly.PolynomialMatrix.mulWith_ofFn_ofFn` (theorem, [line 486](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L486))

> The naive product of square `ofFn` matrices.

```lean
theorem mulWith_ofFn_ofFn [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (n : Nat)
    (f g : Nat → Nat → CPolynomial F) :
    mulWith mulCtx (ofFn n n f) (ofFn n n g) =
      ofFn n n (fun i j ↦ ∑ k ∈ Finset.range n, f i k * g k j)
```

`CompPoly.PolynomialMatrix.truncateColumns_ofFn` (theorem, [line 499](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L499))

> Column truncation of an `ofFn` matrix.

```lean
theorem truncateColumns_ofFn [Semiring F] [BEq F] [LawfulBEq F] (orders : Array Nat)
    (rows width : Nat) (entry : Nat → Nat → CPolynomial F) :
    truncateColumns orders (ofFn rows width entry) =
      ofFn rows width (fun i j ↦ truncateX (orders.getD j 0) (entry i j))
```

> ## Strassen seven-product sum identities

> ## Padding step

> ## Full Strassen correctness

`CompPoly.PolynomialMatrix.mulStrassenWithFuel_eq_mulWith` (theorem, [line 619](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L619))

> The fuel-bounded Strassen product equals the naive matrix product.

```lean
theorem mulStrassenWithFuel_eq_mulWith [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff fuel : Nat) (A B : PolynomialMatrix F) :
    mulStrassenWithFuel lowCtx leafCutoff fuel A B = mulWith lowCtx.mulContext A B
```

`CompPoly.PolynomialMatrix.mulStrassenWith_eq_mulWith` (theorem, [line 671](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L671))

> The Strassen product equals the naive matrix product.

```lean
theorem mulStrassenWith_eq_mulWith [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) (A B : PolynomialMatrix F) :
    mulStrassenWith lowCtx leafCutoff A B = mulWith lowCtx.mulContext A B
```

`CompPoly.PolynomialMatrix.mulStrassenWith_size` (theorem, [line 677](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L677))

> Row count of the Strassen product.

```lean
theorem mulStrassenWith_size [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) (A B : PolynomialMatrix F) :
    (mulStrassenWith lowCtx leafCutoff A B).size = A.size
```

`CompPoly.PolynomialMatrix.mulStrassenWith_getD` (theorem, [line 683](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L683))

> Rows of the Strassen product are the naive row-by-matrix products.

```lean
theorem mulStrassenWith_getD [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) (A B : PolynomialMatrix F)
    {i : Nat} (hi : i < A.size) :
    (mulStrassenWith lowCtx leafCutoff A B).getD i #[] =
      rowMulMatrixWith lowCtx.mulContext (A.getD i #[]) B
```

`CompPoly.PolynomialMatrix.matrixRows_mulStrassenWith` (theorem, [line 691](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L691))

> Row list of the Strassen product.

```lean
theorem matrixRows_mulStrassenWith [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) (A B : PolynomialMatrix F) :
    MatrixRows (mulStrassenWith lowCtx leafCutoff A B) =
      (MatrixRows A).map fun row ↦ rowMulMatrixWith lowCtx.mulContext row B
```

> ## Column-truncated Strassen correctness

`CompPoly.PolynomialMatrix.mulTruncColumnStrassenWithFuel_eq_truncateColumns` (theorem, [line 701](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L701))

> The fuel-bounded column-truncated Strassen product equals the
> column-truncated naive matrix product.

```lean
theorem mulTruncColumnStrassenWithFuel_eq_truncateColumns [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff fuel : Nat) (orders : Array Nat)
    (A B : PolynomialMatrix F) :
    mulTruncColumnStrassenWithFuel lowCtx leafCutoff fuel orders A B =
      truncateColumns orders (mulWith lowCtx.mulContext A B)
```

`CompPoly.PolynomialMatrix.mulTruncColumnStrassenWith_eq_truncateColumns` (theorem, [line 788](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L788))

> The column-truncated Strassen product equals the column-truncated naive
> matrix product.

```lean
theorem mulTruncColumnStrassenWith_eq_truncateColumns [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) (orders : Array Nat)
    (A B : PolynomialMatrix F) :
    mulTruncColumnStrassenWith lowCtx leafCutoff orders A B =
      truncateColumns orders (mulWith lowCtx.mulContext A B)
```

`CompPoly.PolynomialMatrix.mulTruncColumnStrassenWith_size` (theorem, [line 797](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L797))

> Row count of the column-truncated Strassen product.

```lean
theorem mulTruncColumnStrassenWith_size [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) (orders : Array Nat)
    (A B : PolynomialMatrix F) :
    (mulTruncColumnStrassenWith lowCtx leafCutoff orders A B).size = A.size
```

`CompPoly.PolynomialMatrix.mulTruncColumnStrassenWith_entry` (theorem, [line 806](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean#L806))

> Entries of the column-truncated Strassen product are the order-truncated
> naive product entries.

```lean
theorem mulTruncColumnStrassenWith_entry [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) (orders : Array Nat)
    (A B : PolynomialMatrix F) {i : Nat} (hi : i < A.size) (j : Nat) :
    rowGet ((mulTruncColumnStrassenWith lowCtx leafCutoff orders A B).getD i #[]) j =
      truncateX (orders.getD j 0)
        (rowGet (rowMulMatrixWith lowCtx.mulContext (A.getD i #[]) B) j)
```

## Depends on

- [Polynomial-Matrix Operations](operations.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/StrassenCorrectness.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.StrassenCorrectness.json)
