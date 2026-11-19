---
catalog: module
lean: CompPoly.CPolynomial.Raw.eval₂, CompPoly.CPolynomial.Raw.eval₂Horner, CompPoly.CPolynomial.Raw.eval, CompPoly.CPolynomial.Raw.evalHorner, CompPoly.CPolynomial.Raw.addRaw, CompPoly.CPolynomial.Raw.add, CompPoly.CPolynomial.Raw.smul, CompPoly.CPolynomial.Raw.smulRight, CompPoly.CPolynomial.Raw.nsmulRaw, CompPoly.CPolynomial.Raw.nsmul, CompPoly.CPolynomial.Raw.mulPowX, CompPoly.CPolynomial.Raw.mulX, CompPoly.CPolynomial.Raw.mulRaw, CompPoly.CPolynomial.Raw.mul, CompPoly.CPolynomial.Raw.pow, CompPoly.CPolynomial.Raw.powBySqUntrimmed, CompPoly.CPolynomial.Raw.powBySq, CompPoly.CPolynomial.Raw.truncate, CompPoly.CPolynomial.Raw.takeLow, CompPoly.CPolynomial.Raw.reverse, CompPoly.CPolynomial.Raw.mulLowConvolution, CompPoly.CPolynomial.Raw.MulLowContext, CompPoly.CPolynomial.Raw.degreeBound, CompPoly.CPolynomial.Raw.natDegreeBound, CompPoly.CPolynomial.Raw.monic, CompPoly.CPolynomial.Raw.divX, CompPoly.CPolynomial.Raw.neg, CompPoly.CPolynomial.Raw.sub
statement: formalized
proof: formalized
---

# Raw Univariate Polynomial Operations

`CompPoly.Univariate.Raw.Ops`, in [CompPoly/Univariate/Raw/Ops.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen, Desmond Coles, Natalie Klaus, Dimitris Mitsios.

> Operations and evaluation lemmas for raw computable univariate polynomials.

`CompPoly.CPolynomial.Raw.eval₂` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L36))

> Evaluates a `CPolynomial.Raw` at `x : S` using a ring homomorphism `f : R →+* S`.
>
> Computes `f(a₀) + f(a₁) * x + f(a₂) * x² + ...` where `aᵢ` are the coefficients.

```lean
def eval₂ [Semiring R] [Semiring S] (f : R →+* S) (x : S) (p : CPolynomial.Raw R) : S
```

`CompPoly.CPolynomial.Raw.eval₂Horner` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L43))

> Evaluates a `CPolynomial.Raw` at `x : S` using Horner's method.
>
> Computes `f(aₙ) + x * (f(aₙ₋₁) + x * (... + x * f(a₀)))` via a right fold.

```lean
def eval₂Horner [Semiring R] [Semiring S] (f : R →+* S) (x : S) (p : CPolynomial.Raw R) : S
```

`CompPoly.CPolynomial.Raw.eval` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L48))

> Evaluates a `CPolynomial.Raw` at a given value

```lean
def eval [Semiring R] (x : R) (p : CPolynomial.Raw R) : R
```

`CompPoly.CPolynomial.Raw.evalHorner` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L53))

> Evaluates a `CPolynomial.Raw` at a given value using Horner's method.

```lean
def evalHorner [Semiring R] (x : R) (p : CPolynomial.Raw R) : R
```

`CompPoly.CPolynomial.Raw.addRaw` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L60))

> Raw addition: pointwise sum of coefficient arrays (padded to equal length).
>
> The result may have trailing zeros and should be trimmed for canonical form.

```lean
def addRaw [Zero R] [Add R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.add` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L66))

> Addition of two `CPolynomial.Raw`s, with result trimmed.

```lean
def add [Zero R] [Add R] [BEq R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.smul` (definition, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L73))

> Scalar multiplication: multiplies each coefficient by `r`.

```lean
def smul [Mul R] (r : R) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.smulRight` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L81))

> Right scalar multiplication: multiplies each coefficient by `r` on the right.
>
> Corresponds to `p.toPoly * Polynomial.C r`, in contrast to `smul` which corresponds
> to `Polynomial.C r * p.toPoly`. The distinction matters in non-commutative semirings.

```lean
def smulRight [Mul R] (r : R) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.nsmulRaw` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L86))

> Raw scalar multiplication by a natural number (may have trailing zeros).

```lean
def nsmulRaw [Semiring R] (n : ℕ) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.nsmul` (definition, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L91))

> Scalar multiplication of `CPolynomial.Raw` by a natural number, with result trimmed.

```lean
def nsmul [Semiring R] [BEq R] (n : ℕ) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mulPowX` (definition, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L100))

> Multiplication by `X^i`: shifts coefficients right by `i` positions (prepends `i` zeros).

```lean
def mulPowX [Zero R] (i : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mulX` (definition, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L105))

> Multiplication of a `CPolynomial.Raw` by `X`, reduces to `mulPowX 1`.

```lean
def mulX [Zero R] (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mulRaw` (definition, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L115))

> Multiplication accumulator using the naive `O(n²)` algorithm: `Σᵢ (aᵢ * q) * X^i`.
>
> The partial sums are combined with the untrimmed `addRaw`, so the result may carry
> trailing zeros and should be trimmed for canonical form. Deferring the trim to the
> end (see `mul`) avoids an `O(size)` scan after every partial sum.

```lean
def mulRaw [Semiring R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mul` (definition, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L123))

> Multiplication using the naive `O(n²)` algorithm: `Σᵢ (aᵢ * q) * X^i`.
>
> Trims only once, at the end of the convolution fold, rather than after every
> partial sum (`mulRaw` does the untrimmed accumulation).

```lean
def mul [Semiring R] [BEq R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.pow` (definition, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L129))

> Exponentiation of a `CPolynomial.Raw` by a natural number `n` via repeated multiplication.
> This is the specification; `powBySq` is the efficient O(log n) implementation.

```lean
def pow [Semiring R] [BEq R] (p : CPolynomial.Raw R) (n : Nat) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.powBySqUntrimmed` (definition, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L141))

> Repeated-squaring core that accumulates with the untrimmed `mulRaw`, deferring
> the canonicalization trim to the outer `powBySq` wrapper. The output may carry
> trailing zeros and is not in canonical form.
>
> For $ n > 0 $, computes $ p ^ n $ by recursing on $ n / 2 $:
> * If $ n $ is even: $ (p ^ {n/2})^2 $
> * If $ n $ is odd:  $ p \cdot (p ^ {n/2})^2 $

```lean
def powBySqUntrimmed [Semiring R] (p : CPolynomial.Raw R) : Nat → CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.powBySq` (definition, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L154))

> Exponentiation via repeated squaring: $ O(\log n) $ multiplications
> instead of $ O(n) $. Delegates to `powBySqUntrimmed` and trims only once
> at the end, rather than after every squaring step.

```lean
def powBySq [Semiring R] [BEq R] (p : CPolynomial.Raw R) (n : Nat) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.truncate` (definition, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L168))

> Keep only the stored coefficients with index `< k`.

```lean
def truncate [Zero R] (k : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.takeLow` (definition, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L173))

> Return exactly the first `k` coefficients, padding missing coefficients with zero.

```lean
def takeLow [Zero R] (k : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.reverse` (definition, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L178))

> Reverse the first `n` coefficients, padding missing coefficients with zero.

```lean
def reverse [Zero R] (n : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mulLowConvolution` (definition, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L183))

> Low product computed by the coefficient convolution formula.

```lean
def mulLowConvolution [Semiring R] (k : Nat) (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.MulLowContext` (structure, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L188))

> Backend for computing the low `k` coefficients of a raw product.

```lean
structure MulLowContext (R : Type*) [Semiring R] [BEq R] [LawfulBEq R] where
  /-- Return the low `k` coefficients of `p * q`. -/
  mulLow : Nat → CPolynomial.Raw R → CPolynomial.Raw R → CPolynomial.Raw R
  /-- The backend does not return coefficients at degree `>= k`. -/
  size_le : ∀ k p q, (mulLow k p q).size ≤ k
  /-- Low coefficients agree with ordinary raw multiplication. -/
  coeff_of_lt : ∀ k p q i, i < k → (mulLow k p q).coeff i = (p * q).coeff i
```

`CompPoly.CPolynomial.Raw.degreeBound` (definition, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L197))

> Upper bound on degree: `size - 1` if non-empty, `⊥` if empty.

```lean
def degreeBound (p : CPolynomial.Raw R) : WithBot Nat
```

`CompPoly.CPolynomial.Raw.natDegreeBound` (definition, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L203))

> Convert `degreeBound` to a natural number by sending `⊥` to `0`.

```lean
def natDegreeBound (p : CPolynomial.Raw R) : Nat
```

`CompPoly.CPolynomial.Raw.monic` (definition, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L207))

> Check if a `CPolynomial.Raw` is monic, i.e. its leading coefficient is 1.

```lean
def monic [Zero R] [One R] [BEq R] (p : CPolynomial.Raw R) : Bool
```

`CompPoly.CPolynomial.Raw.divX` (definition, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L210))

> Pseudo-division by `X`: removes the constant term and shifts remaining coefficients left.

```lean
def divX (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.neg` (definition, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L218))

> Negation of a `CPolynomial.Raw`.

```lean
def neg [Neg R] (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.sub` (definition, [line 222](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean#L222))

> Subtraction of two `CPolynomial.Raw`s.

```lean
def sub [Zero R] [Add R] [Neg R] [BEq R]
    (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

## Depends on

- [Raw Computable Univariate Polynomials](core.md)

## Sources

- [CompPoly/Univariate/Raw/Ops.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Ops.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Raw.Ops.json)
