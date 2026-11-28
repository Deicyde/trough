---
catalog: module
lean: CompPoly.PolynomialMatrix.truncateX, CompPoly.PolynomialMatrix.truncateX_coeff, CompPoly.PolynomialMatrix.MulLowContext, CompPoly.PolynomialMatrix.MulLowContext.fromMulContext, CompPoly.PolynomialMatrix.MulLowContext.raw, CompPoly.PolynomialMatrix.ofFn, CompPoly.PolynomialMatrix.zero, CompPoly.PolynomialMatrix.identity, CompPoly.PolynomialMatrix.transpose, CompPoly.PolynomialMatrix.rowDotWith, CompPoly.PolynomialMatrix.rowMulMatrixWith, CompPoly.PolynomialMatrix.mulWith, CompPoly.PolynomialMatrix.mul, CompPoly.PolynomialMatrix.add, CompPoly.PolynomialMatrix.sub, CompPoly.PolynomialMatrix.block, CompPoly.PolynomialMatrix.joinSquareBlocks, CompPoly.PolynomialMatrix.nextPowerOfTwoAtLeastLoop, CompPoly.PolynomialMatrix.nextPowerOfTwoAtLeast, CompPoly.PolynomialMatrix.multiplicationDimension, CompPoly.PolynomialMatrix.padSquare, CompPoly.PolynomialMatrix.trimShape, CompPoly.PolynomialMatrix.natArraySlice, CompPoly.PolynomialMatrix.maxNatArrays, CompPoly.PolynomialMatrix.polynomialCoeffCap, CompPoly.PolynomialMatrix.productCoeffCap, CompPoly.PolynomialMatrix.rowMulMatrixEntryCoeffCap, CompPoly.PolynomialMatrix.rowTruncateColumns, CompPoly.PolynomialMatrix.truncateColumns, CompPoly.PolynomialMatrix.mulTruncXWith, CompPoly.PolynomialMatrix.mulLowXWith, CompPoly.PolynomialMatrix.divXTrunc, CompPoly.PolynomialMatrix.modByMonicWith, CompPoly.PolynomialMatrix.rowModDiagonalWith, CompPoly.PolynomialMatrix.modDiagonalWith, CompPoly.PolynomialMatrix.rowMulMatrixModDiagonalWith, CompPoly.PolynomialMatrix.rowMulMatrixTruncColumnWith, CompPoly.PolynomialMatrix.mulTruncColumnWith, CompPoly.PolynomialMatrix.mulTruncColumnStrassenWithFuel, CompPoly.PolynomialMatrix.mulTruncColumnStrassenWith, CompPoly.PolynomialMatrix.rowMulMatrixBoundedWith, CompPoly.PolynomialMatrix.mulBoundedWith, CompPoly.PolynomialMatrix.mulStrassenWithFuel, CompPoly.PolynomialMatrix.mulStrassenWith, CompPoly.PolynomialMatrix.rowSatisfiesModularBool, CompPoly.PolynomialMatrix.shiftedRowDegreeProfile, CompPoly.PolynomialMatrix.RowChoice, CompPoly.PolynomialMatrix.betterRowChoice, CompPoly.PolynomialMatrix.leastShiftedDegreeRowStep?, CompPoly.PolynomialMatrix.leastShiftedDegreeChoice?, CompPoly.PolynomialMatrix.leastShiftedDegreeRow?
statement: formalized
proof: formalized
---

# Polynomial-Matrix Operations

`CompPoly.LinearAlgebra.PolynomialMatrix.Operations`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean), by Valerii Huhnin.

> Reusable executable operations for polynomial rows and row-major polynomial
> matrices.  The multiplication and reduction entry points take explicit
> univariate operation contexts so concrete fields can supply fast polynomial
> arithmetic.

`CompPoly.PolynomialMatrix.truncateX` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L34))

> Keep the coefficients of degree `< order`.

```lean
def truncateX [Zero F] [BEq F] [LawfulBEq F] (order : Nat)
    (p : CPolynomial F) : CPolynomial F
```

`CompPoly.PolynomialMatrix.truncateX_coeff` (theorem, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L40))

> Coefficients of an `X`-adic truncation.

```lean
theorem truncateX_coeff [Semiring F] [BEq F] [LawfulBEq F] (order : Nat)
    (p : CPolynomial F) (i : Nat) :
    CPolynomial.coeff (truncateX order p) i =
      if i < order then CPolynomial.coeff p i else 0
```

`CompPoly.PolynomialMatrix.MulLowContext` (structure, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L62))

> Polynomial-matrix low-product backend.  The full multiplication context is
> kept beside the low-product operation because recursive PM-basis still needs
> ordinary basis composition.

```lean
structure MulLowContext (F : Type*) [Semiring F] [BEq F] [LawfulBEq F] where
  mulContext : CPolynomial.MulContext F
  mulLow : Nat → CPolynomial F → CPolynomial F → CPolynomial F
  /-- The backend returns exactly the truncated canonical product. -/
  mulLow_eq : ∀ order p q, mulLow order p q = truncateX order (p * q)
```

`CompPoly.PolynomialMatrix.MulLowContext.fromMulContext` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L71))

> Low-product backend obtained by truncating a full univariate product.

```lean
def fromMulContext [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) : MulLowContext F
```

`CompPoly.PolynomialMatrix.MulLowContext.raw` (definition, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L83))

> Low-product backend backed directly by a raw low-product implementation.

```lean
def raw [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F)
    (rawCtx : CPolynomial.Raw.MulLowContext F) : MulLowContext F
```

`CompPoly.PolynomialMatrix.ofFn` (definition, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L106))

> Build a row-major polynomial matrix from an indexed entry function.

```lean
def ofFn [Zero F] (rows width : Nat) (entry : Nat → Nat → CPolynomial F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.zero` (definition, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L112))

> The zero matrix of a fixed shape.

```lean
def zero [Zero F] (rows width : Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.identity` (definition, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L116))

> The polynomial identity matrix of size `n`.

```lean
def identity [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F] (n : Nat) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.transpose` (definition, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L121))

> Matrix transpose, using zero defaults for ragged input rows.

```lean
def transpose [Zero F] (M : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.rowDotWith` (definition, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L126))

> Dot product of two polynomial rows using an explicit univariate
> multiplication context.

```lean
def rowDotWith [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (a b : PolynomialRow F) :
    CPolynomial F
```

`CompPoly.PolynomialMatrix.rowMulMatrixWith` (definition, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L133))

> Row-by-matrix product using an explicit univariate multiplication context.

```lean
def rowMulMatrixWith [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (row : PolynomialRow F)
    (M : PolynomialMatrix F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.mulWith` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L142))

> Matrix product using an explicit univariate multiplication context.

```lean
def mulWith [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (A B : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.mul` (definition, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L148))

> Matrix product backed by canonical univariate multiplication.

```lean
def mul [Semiring F] [BEq F] [LawfulBEq F]
    (A B : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.add` (definition, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L153))

> Pointwise matrix addition, using zero defaults for ragged inputs.

```lean
def add [Semiring F] [BEq F] [LawfulBEq F]
    (A B : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.sub` (definition, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L159))

> Pointwise matrix subtraction, using zero defaults for ragged inputs.

```lean
def sub [Ring F] [BEq F] [LawfulBEq F]
    (A B : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.block` (definition, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L165))

> Extract a rectangular block with zero defaults for out-of-range entries.

```lean
def block [Zero F] (M : PolynomialMatrix F)
    (rowStart rowCount colStart colCount : Nat) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.joinSquareBlocks` (definition, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L171))

> Join four equally sized square blocks into one square matrix.

```lean
def joinSquareBlocks [Zero F] (half : Nat)
    (C₁₁ C₁₂ C₂₁ C₂₂ : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.nextPowerOfTwoAtLeastLoop` (definition, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L186))

> Fuel-bounded doubling loop for the smallest power of two at least `target`.

```lean
def nextPowerOfTwoAtLeastLoop (target : Nat) :
    Nat → Nat → Nat
```

`CompPoly.PolynomialMatrix.nextPowerOfTwoAtLeast` (definition, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L196))

> Smallest power of two at least `target`, with `1` returned for `0`.

```lean
def nextPowerOfTwoAtLeast (target : Nat) : Nat
```

`CompPoly.PolynomialMatrix.multiplicationDimension` (definition, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L200))

> Runtime dimension controlling rectangular polynomial-matrix multiplication.

```lean
def multiplicationDimension [Zero F] (A B : PolynomialMatrix F) : Nat
```

`CompPoly.PolynomialMatrix.padSquare` (definition, [line 204](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L204))

> Pad a matrix to an `n × n` square using the zero-default block extractor.

```lean
def padSquare [Zero F] (n : Nat) (M : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.trimShape` (definition, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L209))

> Trim a matrix to a rectangular output shape.

```lean
def trimShape [Zero F] (rows width : Nat) (M : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.natArraySlice` (definition, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L214))

> Slice `count` natural-number entries, using zero defaults out of bounds.

```lean
def natArraySlice (values : Array Nat) (start count : Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.maxNatArrays` (definition, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L218))

> Pointwise maximum of two natural-number arrays.

```lean
def maxNatArrays (a b : Array Nat) : Array Nat
```

`CompPoly.PolynomialMatrix.polynomialCoeffCap` (definition, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L223))

> Number of coefficients needed to represent a polynomial exactly.

```lean
def polynomialCoeffCap [Zero F] [BEq F] (p : CPolynomial F) : Nat
```

`CompPoly.PolynomialMatrix.productCoeffCap` (definition, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L227))

> Number of low coefficients sufficient for one product term exactly.

```lean
def productCoeffCap [Zero F] [BEq F] (p q : CPolynomial F) : Nat
```

`CompPoly.PolynomialMatrix.rowMulMatrixEntryCoeffCap` (definition, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L231))

> Per-entry coefficient cap for one row-by-matrix product entry.

```lean
def rowMulMatrixEntryCoeffCap [Zero F] [BEq F]
    (row : PolynomialRow F) (M : PolynomialMatrix F) (j : Nat) : Nat
```

`CompPoly.PolynomialMatrix.rowTruncateColumns` (definition, [line 238](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L238))

> Truncate one row with independent output-column orders.

```lean
def rowTruncateColumns [Zero F] [BEq F] [LawfulBEq F]
    (orders : Array Nat) (row : PolynomialRow F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.truncateColumns` (definition, [line 244](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L244))

> Truncate a matrix with independent output-column orders.

```lean
def truncateColumns [Zero F] [BEq F] [LawfulBEq F]
    (orders : Array Nat) (M : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.mulTruncXWith` (definition, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L249))

> Multiply and retain only coefficients of degree `< order`.

```lean
def mulTruncXWith [Semiring F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (order : Nat)
    (p q : CPolynomial F) : CPolynomial F
```

`CompPoly.PolynomialMatrix.mulLowXWith` (definition, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L255))

> Low-product entry point for the first `order` coefficients.

```lean
def mulLowXWith [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (order : Nat)
    (p q : CPolynomial F) : CPolynomial F
```

`CompPoly.PolynomialMatrix.divXTrunc` (definition, [line 261](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L261))

> Divide by `X^shift` and keep `order` coefficients.

```lean
def divXTrunc [Zero F] [BEq F] [LawfulBEq F] (shift order : Nat)
    (p : CPolynomial F) : CPolynomial F
```

`CompPoly.PolynomialMatrix.modByMonicWith` (definition, [line 268](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L268))

> Reduce by a monic modulus when one is present.  A zero modulus is treated as
> an absent modulus and leaves the input unchanged.

```lean
def modByMonicWith [Field F] [BEq F] [LawfulBEq F]
    (modCtx : CPolynomial.ModContext F) (p modulus : CPolynomial F) :
    CPolynomial F
```

`CompPoly.PolynomialMatrix.rowModDiagonalWith` (definition, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L275))

> Reduce a row by independent diagonal moduli.  The output width is the number
> of supplied moduli.

```lean
def rowModDiagonalWith [Field F] [BEq F] [LawfulBEq F]
    (modCtx : CPolynomial.ModContext F) (moduli : Array (CPolynomial F))
    (row : PolynomialRow F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.modDiagonalWith` (definition, [line 282](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L282))

> Reduce every matrix row by independent diagonal moduli.

```lean
def modDiagonalWith [Field F] [BEq F] [LawfulBEq F]
    (modCtx : CPolynomial.ModContext F) (moduli : Array (CPolynomial F))
    (M : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.rowMulMatrixModDiagonalWith` (definition, [line 288](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L288))

> Row-by-matrix product followed by diagonal modular reduction.

```lean
def rowMulMatrixModDiagonalWith [Field F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (row : PolynomialRow F) (M : PolynomialMatrix F)
    (moduli : Array (CPolynomial F)) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.rowMulMatrixTruncColumnWith` (definition, [line 297](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L297))

> Row-by-matrix product with independent output-column truncation.  Column
> `j` keeps coefficients of degree `< orders[j]`; this is the residual-window
> primitive used by recursive PM-basis.

```lean
def rowMulMatrixTruncColumnWith [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (orders : Array Nat)
    (row : PolynomialRow F) (M : PolynomialMatrix F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.mulTruncColumnWith` (definition, [line 309](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L309))

> Matrix product with independent output-column truncation.

```lean
def mulTruncColumnWith [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (orders : Array Nat)
    (A B : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.mulTruncColumnStrassenWithFuel` (definition, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L316))

> Fuel-bounded Strassen-style matrix product with independent output-column
> truncation orders.

```lean
def mulTruncColumnStrassenWithFuel [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) :
    Nat → Array Nat → PolynomialMatrix F → PolynomialMatrix F → PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.mulTruncColumnStrassenWith` (definition, [line 362](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L362))

> Strassen-style matrix product with independent output-column truncation
> orders and conservative default fuel.

```lean
def mulTruncColumnStrassenWith [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat)
    (orders : Array Nat) (A B : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.rowMulMatrixBoundedWith` (definition, [line 371](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L371))

> Row-by-matrix product with per-output-entry degree caps inferred from input
> degree profiles.  This reconstructs the exact row product while routing every
> term through low-product multiplication.

```lean
def rowMulMatrixBoundedWith [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (row : PolynomialRow F)
    (M : PolynomialMatrix F) : PolynomialRow F
```

`CompPoly.PolynomialMatrix.mulBoundedWith` (definition, [line 384](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L384))

> Matrix product reconstructed from inferred per-entry degree caps.  Recursive
> composition uses this only as its small-leaf and fuel-exhausted fallback.

```lean
def mulBoundedWith [Semiring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (A B : PolynomialMatrix F) :
    PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.mulStrassenWithFuel` (definition, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L395))

> Fuel-bounded Strassen-style matrix product.
>
> Small inputs and exhausted fuel use the bounded row-column product.  Larger
> rectangular or odd-sized inputs are padded to square power-of-two shape, routed
> through the recursive block product, and trimmed back to the requested output
> shape.

```lean
def mulStrassenWithFuel [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat) :
    Nat → PolynomialMatrix F → PolynomialMatrix F → PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.mulStrassenWith` (definition, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L436))

> Strassen-style matrix product with a conservative default fuel.

```lean
def mulStrassenWith [Ring F] [BEq F] [LawfulBEq F]
    (lowCtx : MulLowContext F) (leafCutoff : Nat)
    (A B : PolynomialMatrix F) : PolynomialMatrix F
```

`CompPoly.PolynomialMatrix.rowSatisfiesModularBool` (definition, [line 443](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L443))

> Executable modular-equation row predicate.

```lean
def rowSatisfiesModularBool [Field F] [BEq F] [LawfulBEq F]
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (row : PolynomialRow F) (M : PolynomialMatrix F)
    (moduli : Array (CPolynomial F)) : Bool
```

`CompPoly.PolynomialMatrix.shiftedRowDegreeProfile` (definition, [line 450](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L450))

> Shifted row-degree profile for all rows.

```lean
def shiftedRowDegreeProfile [Zero F] [BEq F] (M : PolynomialMatrix F)
    (shift : Array Nat) : Array (Option Nat)
```

`CompPoly.PolynomialMatrix.RowChoice` (structure, [line 455](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L455))

> Candidate row selected by least-shifted-degree scanning.

```lean
structure RowChoice (F : Type*) [Zero F] where
  index : Nat
  row : PolynomialRow F
  degree : Nat
```

`CompPoly.PolynomialMatrix.betterRowChoice` (definition, [line 461](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L461))

> Tie-breaking order for least-shifted-degree row selection.

```lean
def betterRowChoice [Zero F] (candidate current : RowChoice F) : Bool
```

`CompPoly.PolynomialMatrix.leastShiftedDegreeRowStep?` (definition, [line 466](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L466))

> One left-to-right scan step for least-shifted-degree row selection.

```lean
def leastShiftedDegreeRowStep? [Zero F] [BEq F]
    (M : PolynomialMatrix F) (shift : Array Nat)
    (best : Option (RowChoice F)) (i : Nat) : Option (RowChoice F)
```

`CompPoly.PolynomialMatrix.leastShiftedDegreeChoice?` (definition, [line 480](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L480))

> Scan row indices for the best least-shifted-degree candidate.

```lean
def leastShiftedDegreeChoice? [Zero F] [BEq F]
    (M : PolynomialMatrix F) (shift : Array Nat) : Option (RowChoice F)
```

`CompPoly.PolynomialMatrix.leastShiftedDegreeRow?` (definition, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean#L485))

> Select a nonzero row of least shifted degree.

```lean
def leastShiftedDegreeRow? [Zero F] [BEq F]
    (M : PolynomialMatrix F) (shift : Array Nat) :
    Option (PolynomialRow F)
```

## Depends on

- [Shifted Degrees for Polynomial Rows](shifted.md)
- [Univariate Algorithm Contexts](../../univariate/part-01/context.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Operations.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Operations.json)
