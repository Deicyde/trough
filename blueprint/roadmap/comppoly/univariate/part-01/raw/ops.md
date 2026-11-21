---
catalog: module
lean: CompPoly.CPolynomial.Raw.eval₂, CompPoly.CPolynomial.Raw.eval₂Horner, CompPoly.CPolynomial.Raw.eval, CompPoly.CPolynomial.Raw.evalHorner, CompPoly.CPolynomial.Raw.addRaw, CompPoly.CPolynomial.Raw.add, CompPoly.CPolynomial.Raw.smul, CompPoly.CPolynomial.Raw.smulRight, CompPoly.CPolynomial.Raw.nsmulRaw, CompPoly.CPolynomial.Raw.nsmul, CompPoly.CPolynomial.Raw.mulPowX, CompPoly.CPolynomial.Raw.mulX, CompPoly.CPolynomial.Raw.mulRaw, CompPoly.CPolynomial.Raw.size_smul, CompPoly.CPolynomial.Raw.size_mulPowX, CompPoly.CPolynomial.Raw.size_addRaw, CompPoly.CPolynomial.Raw.add_coeff?, CompPoly.CPolynomial.Raw.smul_mulPowX_coeff, CompPoly.CPolynomial.Raw.size_mulRaw, CompPoly.CPolynomial.Raw.coeff_mulRaw, CompPoly.CPolynomial.Raw.mulRawFast, CompPoly.CPolynomial.Raw.size_mulRawFast, CompPoly.CPolynomial.Raw.getElem_mulRawFast, CompPoly.CPolynomial.Raw.mulRaw_eq_mulRawFast, CompPoly.CPolynomial.Raw.mul, CompPoly.CPolynomial.Raw.pow, CompPoly.CPolynomial.Raw.powBySqUntrimmed, CompPoly.CPolynomial.Raw.powBySq, CompPoly.CPolynomial.Raw.truncate, CompPoly.CPolynomial.Raw.takeLow, CompPoly.CPolynomial.Raw.reverse, CompPoly.CPolynomial.Raw.mulLowConvolution, CompPoly.CPolynomial.Raw.MulLowContext, CompPoly.CPolynomial.Raw.degreeBound, CompPoly.CPolynomial.Raw.natDegreeBound, CompPoly.CPolynomial.Raw.monic, CompPoly.CPolynomial.Raw.divX, CompPoly.CPolynomial.Raw.neg, CompPoly.CPolynomial.Raw.sub
statement: formalized
proof: formalized
---

# Raw Univariate Polynomial Operations

`CompPoly.Univariate.Raw.Ops`, in [CompPoly/Univariate/Raw/Ops.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen, Desmond Coles, Natalie Klaus, Dimitris Mitsios, Alexander Hicks.

> Operations and evaluation lemmas for raw computable univariate polynomials. The file also states
> the sizes of `smul`, `mulPowX`, `addRaw` and `mulRaw`, and the coefficients of `addRaw`, of a
> shifted `smul` and of `mulRaw`. It defines `mulRawFast`, a loop for `mulRaw` that computes each
> entry of the result as one sum. The `@[csimp]` lemma `mulRaw_eq_mulRawFast` makes compiled code
> compute `mulRaw` with `mulRawFast`.
>
> `size_smul`, `size_mulPowX`, `size_addRaw` and `size_mulRaw` were ported from ArkLib's raw-size
> adapter under Apache 2.0. The file header records their copyright.

`CompPoly.CPolynomial.Raw.eval₂` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L43))

> Evaluates a `CPolynomial.Raw` at `x : S` using a ring homomorphism `f : R →+* S`.
>
> Computes `f(a₀) + f(a₁) * x + f(a₂) * x² + ...` where `aᵢ` are the coefficients.

```lean
def eval₂ [Semiring R] [Semiring S] (f : R →+* S) (x : S) (p : CPolynomial.Raw R) : S
```

`CompPoly.CPolynomial.Raw.eval₂Horner` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L50))

> Evaluates a `CPolynomial.Raw` at `x : S` using Horner's method.
>
> Computes `f(aₙ) + x * (f(aₙ₋₁) + x * (... + x * f(a₀)))` via a right fold.

```lean
def eval₂Horner [Semiring R] [Semiring S] (f : R →+* S) (x : S) (p : CPolynomial.Raw R) : S
```

`CompPoly.CPolynomial.Raw.eval` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L55))

> Evaluates a `CPolynomial.Raw` at a given value

```lean
def eval [Semiring R] (x : R) (p : CPolynomial.Raw R) : R
```

`CompPoly.CPolynomial.Raw.evalHorner` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L60))

> Evaluates a `CPolynomial.Raw` at a given value using Horner's method.

```lean
def evalHorner [Semiring R] (x : R) (p : CPolynomial.Raw R) : R
```

`CompPoly.CPolynomial.Raw.addRaw` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L67))

> Raw addition: pointwise sum of coefficient arrays (padded to equal length).
>
> The result may have trailing zeros and should be trimmed for canonical form.

```lean
def addRaw [Zero R] [Add R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.add` (definition, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L73))

> Addition of two `CPolynomial.Raw`s, with result trimmed.

```lean
def add [Zero R] [Add R] [BEq R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.smul` (definition, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L80))

> Scalar multiplication: multiplies each coefficient by `r`.

```lean
def smul [Mul R] (r : R) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.smulRight` (definition, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L88))

> Right scalar multiplication: multiplies each coefficient by `r` on the right.
>
> Corresponds to `p.toPoly * Polynomial.C r`, in contrast to `smul` which corresponds
> to `Polynomial.C r * p.toPoly`. The distinction matters in non-commutative semirings.

```lean
def smulRight [Mul R] (r : R) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.nsmulRaw` (definition, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L93))

> Raw scalar multiplication by a natural number (may have trailing zeros).

```lean
def nsmulRaw [Semiring R] (n : ℕ) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.nsmul` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L98))

> Scalar multiplication of `CPolynomial.Raw` by a natural number, with result trimmed.

```lean
def nsmul [Semiring R] [BEq R] (n : ℕ) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mulPowX` (definition, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L107))

> Multiplication by `X^i`: shifts coefficients right by `i` positions (prepends `i` zeros).

```lean
def mulPowX [Zero R] (i : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mulX` (definition, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L112))

> Multiplication of a `CPolynomial.Raw` by `X`, reduces to `mulPowX 1`.

```lean
def mulX [Zero R] (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mulRaw` (definition, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L124))

> Multiplication accumulator using the naive `O(n²)` algorithm: `Σᵢ (aᵢ * q) * X^i`.
>
> The partial sums are combined with the untrimmed `addRaw`, so the result may carry
> trailing zeros and should be trimmed for canonical form. Deferring the trim to the
> end (see `mul`) avoids an `O(size)` scan after every partial sum.
>
> Compiled code computes `mulRaw` with `mulRawFast` (see `mulRaw_eq_mulRawFast`).

```lean
def mulRaw [Semiring R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

> ### Sizes and coefficients of the operations in `mulRaw`
>
> The sizes count the stored coefficients, including trailing zeros.

`CompPoly.CPolynomial.Raw.size_smul` (theorem, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L135))

> Scalar multiplication preserves the stored coefficient count.

```lean
theorem size_smul [Mul R] (x : R) (p : CPolynomial.Raw R) :
    (smul x p).size = p.size
```

`CompPoly.CPolynomial.Raw.size_mulPowX` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L141))

> Multiplication by `X^i` retains all of the prepended zero coefficients.

```lean
theorem size_mulPowX [Zero R] (i : Nat) (p : CPolynomial.Raw R) :
    (mulPowX i p).size = i + p.size
```

`CompPoly.CPolynomial.Raw.size_addRaw` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L147))

> Padded raw addition stores the larger input size.

```lean
theorem size_addRaw [Zero Q] [Add Q] {p q : CPolynomial.Raw Q} :
    (addRaw p q).size = max p.size q.size
```

`CompPoly.CPolynomial.Raw.add_coeff?` (theorem, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L153))

> Coefficient `i` of `addRaw p q` is the sum of coefficient `i` of `p` and of `q`.

```lean
theorem add_coeff? [AddZeroClass Q] (p q : CPolynomial.Raw Q) (i : ℕ) :
    (addRaw p q).coeff i = p.coeff i + q.coeff i
```

`CompPoly.CPolynomial.Raw.smul_mulPowX_coeff` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L163))

> Coefficient `k` of `smul a q` shifted by `i` places: `0` below `i`, and `a * q.coeff (k - i)`
> from `i` on.

```lean
theorem smul_mulPowX_coeff [MulZeroClass R] (a : R) (q : CPolynomial.Raw R) (i k : ℕ) :
    ((smul a q).mulPowX i).coeff k = if k < i then 0 else a * q.coeff (k - i)
```

`CompPoly.CPolynomial.Raw.size_mulRaw` (theorem, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L172))

> Raw multiplication retains every shifted row, including padding from an empty right array.

```lean
theorem size_mulRaw [Semiring R] (p q : CPolynomial.Raw R) :
    (mulRaw p q).size = if p.size = 0 then 0 else q.size + p.size - 1
```

`CompPoly.CPolynomial.Raw.coeff_mulRaw` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L193))

> Coefficient `k` of `mulRaw p q` is the convolution sum of the coefficients of `p` and `q`.

```lean
theorem coeff_mulRaw [Semiring R] (p q : CPolynomial.Raw R) (k : ℕ) :
    (mulRaw p q).coeff k =
      ∑ i ∈ Finset.range p.size, if k < i then 0 else p.coeff i * q.coeff (k - i)
```

> ### Compiled raw multiplication
>
> `mulRawFast` computes the same array as `mulRaw`. The `@[csimp]` lemma `mulRaw_eq_mulRawFast`
> makes compiled code use it. The lemma comes before `mul` and the other definitions in this file
> that use `mulRaw`. When the compiler compiles such a definition, it inlines or specializes `mulRaw`
> into the code. A `@[csimp]` lemma later in the file would not change that code.

`CompPoly.CPolynomial.Raw.mulRawFast` (definition, [line 228](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L228))

> Raw multiplication that computes each entry of the result as one sum.
>
> The result is empty when `p` is empty. Otherwise it has `q.size + p.size - 1` entries, as in
> `mulRaw`. Entry `k` is the sum of the products `p[i] * q[k - i]` over the indices `i` with
> `k + 1 - q.size ≤ i < min (k + 1) p.size`, added to `0` in increasing order of `i`. Each pair
> `(i, j)` with `i < p.size` and `j < q.size` occurs in exactly one entry, so the loop makes
> `p.size * q.size` multiplications and the same number of additions.

```lean
def mulRawFast [inst : Semiring R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.size_mulRawFast` (theorem, [line 284](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L284))

> `mulRawFast p q` is empty when `p` is empty. Otherwise it has `q.size + p.size - 1` entries.

```lean
theorem size_mulRawFast [Semiring R] (p q : CPolynomial.Raw R) :
    (mulRawFast p q).size = if p.size = 0 then 0 else q.size + p.size - 1
```

`CompPoly.CPolynomial.Raw.getElem_mulRawFast` (theorem, [line 292](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L292))

> Entry `k` of `mulRawFast p q` is the convolution sum of the coefficients of `p` and `q`.

```lean
theorem getElem_mulRawFast [Semiring R] (p q : CPolynomial.Raw R) (k : ℕ)
    (hk : k < (mulRawFast p q).size) :
    (mulRawFast p q)[k] =
      ∑ i ∈ Finset.range p.size, if k < i then 0 else p.coeff i * q.coeff (k - i)
```

`CompPoly.CPolynomial.Raw.mulRaw_eq_mulRawFast` (theorem, [line 303](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L303))

> `mulRaw` equals `mulRawFast`. As a `@[csimp]` lemma, it makes compiled code use
> `mulRawFast`.

```lean
theorem mulRaw_eq_mulRawFast : @mulRaw = @mulRawFast
```

`CompPoly.CPolynomial.Raw.mul` (definition, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L316))

> Multiplication using the naive `O(n²)` algorithm: `Σᵢ (aᵢ * q) * X^i`.
>
> Trims only once, at the end of the convolution fold, rather than after every
> partial sum (`mulRaw` does the untrimmed accumulation). Compiled code computes the product with
> `mulRawFast` (see `mulRaw_eq_mulRawFast`).

```lean
def mul [Semiring R] [BEq R] (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.pow` (definition, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L322))

> Exponentiation of a `CPolynomial.Raw` by a natural number `n` via repeated multiplication.
> This is the specification; `powBySq` is the efficient O(log n) implementation.

```lean
def pow [Semiring R] [BEq R] (p : CPolynomial.Raw R) (n : Nat) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.powBySqUntrimmed` (definition, [line 335](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L335))

> Repeated-squaring core that accumulates with the untrimmed `mulRaw`, deferring
> the canonicalization trim to the outer `powBySq` wrapper. The output may carry
> trailing zeros and is not in canonical form. Compiled code computes each product with
> `mulRawFast`.
>
> For $ n > 0 $, computes $ p ^ n $ by recursing on $ n / 2 $:
> * If $ n $ is even: $ (p ^ {n/2})^2 $
> * If $ n $ is odd:  $ p \cdot (p ^ {n/2})^2 $

```lean
def powBySqUntrimmed [Semiring R] (p : CPolynomial.Raw R) : Nat → CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.powBySq` (definition, [line 348](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L348))

> Exponentiation via repeated squaring: $ O(\log n) $ multiplications
> instead of $ O(n) $. Delegates to `powBySqUntrimmed` and trims only once
> at the end, rather than after every squaring step.

```lean
def powBySq [Semiring R] [BEq R] (p : CPolynomial.Raw R) (n : Nat) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.truncate` (definition, [line 362](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L362))

> Keep only the stored coefficients with index `< k`.

```lean
def truncate [Zero R] (k : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.takeLow` (definition, [line 367](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L367))

> Return exactly the first `k` coefficients, padding missing coefficients with zero.

```lean
def takeLow [Zero R] (k : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.reverse` (definition, [line 372](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L372))

> Reverse the first `n` coefficients, padding missing coefficients with zero.

```lean
def reverse [Zero R] (n : Nat) (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.mulLowConvolution` (definition, [line 377](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L377))

> Low product computed by the coefficient convolution formula.

```lean
def mulLowConvolution [Semiring R] (k : Nat) (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.MulLowContext` (structure, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L382))

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

`CompPoly.CPolynomial.Raw.degreeBound` (definition, [line 391](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L391))

> Upper bound on degree: `size - 1` if non-empty, `⊥` if empty.

```lean
def degreeBound (p : CPolynomial.Raw R) : WithBot Nat
```

`CompPoly.CPolynomial.Raw.natDegreeBound` (definition, [line 397](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L397))

> Convert `degreeBound` to a natural number by sending `⊥` to `0`.

```lean
def natDegreeBound (p : CPolynomial.Raw R) : Nat
```

`CompPoly.CPolynomial.Raw.monic` (definition, [line 401](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L401))

> Check if a `CPolynomial.Raw` is monic, i.e. its leading coefficient is 1.

```lean
def monic [Zero R] [One R] [BEq R] (p : CPolynomial.Raw R) : Bool
```

`CompPoly.CPolynomial.Raw.divX` (definition, [line 404](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L404))

> Pseudo-division by `X`: removes the constant term and shifts remaining coefficients left.

```lean
def divX (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.neg` (definition, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L412))

> Negation of a `CPolynomial.Raw`.

```lean
def neg [Neg R] (p : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.Raw.sub` (definition, [line 416](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean#L416))

> Subtraction of two `CPolynomial.Raw`s.

```lean
def sub [Zero R] [Add R] [Neg R] [BEq R]
    (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

## Depends on

- [Raw Computable Univariate Polynomials](core.md)

## Sources

- [CompPoly/Univariate/Raw/Ops.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Ops.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Raw.Ops.json)
