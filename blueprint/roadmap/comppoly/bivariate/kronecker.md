---
catalog: module
lean: CompPoly.CPolynomial.coeff_mul_X_pow, CompPoly.CPolynomial.shiftPow, CompPoly.CPolynomial.coeff_shiftPow, CompPoly.CPolynomial.shiftPow_eq_mul_X_pow, CompPoly.CBivariate.kroneckerPack, CompPoly.CBivariate.kroneckerUnpack, CompPoly.CBivariate.kroneckerPack_mul, CompPoly.CBivariate.kroneckerPack_eq_sum, CompPoly.CBivariate.coeff_kroneckerPack, CompPoly.CBivariate.kroneckerPackFast, CompPoly.CBivariate.kroneckerPackFast_eq, CompPoly.CBivariate.coeff_kroneckerUnpack_of_le, CompPoly.CBivariate.coeff_kroneckerUnpack, CompPoly.CBivariate.window, CompPoly.CBivariate.coeff_window, CompPoly.CBivariate.kroneckerUnpackFast, CompPoly.CBivariate.kroneckerUnpackFast_eq, CompPoly.CBivariate.kroneckerUnpack_kroneckerPack, CompPoly.CBivariate.kroneckerUnpack_mul, CompPoly.CBivariate.kroneckerUnpackFast_mul, CompPoly.CBivariate.kroneckerUnpack_withFallback, CompPoly.CBivariate.kroneckerUnpack_withFallbackFast
statement: formalized
proof: formalized
---

# Kronecker substitution for bivariate polynomials

`CompPoly.Bivariate.Kronecker`, in [CompPoly/Bivariate/Kronecker.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean), by Dimitris Mitsios.

> Kronecker substitution turns a bivariate multiplication into a univariate multiplication by
> fixing a gap `D` and substituting `X ↦ t`, `Y ↦ t ^ D`. This sends a bivariate
> polynomial `p : CBivariate R` to a univariate polynomial `kroneckerPack D p : CPolynomial R`
> in which the coefficient of `X ^ i Y ^ j` is placed at position `D * j + i`.
>
> Packing is a ring homomorphism, so for any `p` and `q` the packed product equals the
> product of the packed operands, with no condition on degrees. A condition is needed only to
> unpack the result. The position `D * j + i` determines `i` and `j` only when `i < D`, so
> packing can be reversed exactly on polynomials with `natDegreeX < D`. Recovering a product
> `p * q` therefore needs
> `natDegreeX (p * q) < D`, and since `natDegreeX (p * q) ≤ natDegreeX p + natDegreeX q`, it is
> enough to choose `D` greater than `natDegreeX p + natDegreeX q`.
>
> Kronecker substitution is not itself an optimisation; it lets a fast univariate
> multiplication carry out the bivariate one. The NTT versions multiply through `withFallback`,
> which uses an NTT domain when one fits and otherwise multiplies the ordinary way, so it is
> always equal to `*` and adds no assumption about the domain beyond the gap condition above.
>
> ## Main results
>
> * `kroneckerPack` / `kroneckerUnpack` — the substitution and its inverse.
> * `kroneckerPack_mul` — packing is multiplicative.
> * `kroneckerUnpack_mul` — bivariate multiplication as pack, multiply, unpack.
> * `kroneckerPackFast` / `kroneckerUnpackFast` — linear-time versions, proved equal to the above.
> * `kroneckerUnpack_withFallback` / `kroneckerUnpack_withFallbackFast` — multiplication backed by
>   the classic and recursive NTT.

`CompPoly.CPolynomial.coeff_mul_X_pow` (theorem, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L54))

> Coefficient of `c * X ^ m`.

```lean
theorem coeff_mul_X_pow [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (c : CPolynomial R) (m n : ℕ) :
    coeff (c * X ^ m) n = if m ≤ n then coeff c (n - m) else 0
```

`CompPoly.CPolynomial.shiftPow` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L70))

> Multiplication by `X ^ m`, implemented as a coefficient shift.

```lean
def shiftPow [Zero R] [BEq R] [LawfulBEq R] (m : ℕ) (p : CPolynomial R) : CPolynomial R
```

`CompPoly.CPolynomial.coeff_shiftPow` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L74))

> Coefficient of `shiftPow m p`.

```lean
theorem coeff_shiftPow [Zero R] [BEq R] [LawfulBEq R] (m : ℕ) (p : CPolynomial R) (n : ℕ) :
    coeff (shiftPow m p) n = if m ≤ n then coeff p (n - m) else 0
```

`CompPoly.CPolynomial.shiftPow_eq_mul_X_pow` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L87))

> `shiftPow m p = p * X ^ m`.

```lean
theorem shiftPow_eq_mul_X_pow [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (m : ℕ) (p : CPolynomial R) : shiftPow m p = p * X ^ m
```

`CompPoly.CBivariate.kroneckerPack` (definition, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L116))

> Pack a bivariate polynomial into a univariate one with gap `D`.

```lean
def kroneckerPack [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (D : ℕ) (p : CBivariate R) : CPolynomial R
```

`CompPoly.CBivariate.kroneckerUnpack` (definition, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L121))

> Unpack a univariate polynomial into a bivariate one with gap `D`.

```lean
def kroneckerUnpack [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (D : ℕ) (P : CPolynomial R) : CBivariate R
```

`CompPoly.CBivariate.kroneckerPack_mul` (theorem, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L127))

> Packing is multiplicative.

```lean
theorem kroneckerPack_mul [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (D : ℕ) (p q : CBivariate R) :
    kroneckerPack D (p * q) = kroneckerPack D p * kroneckerPack D q
```

`CompPoly.CBivariate.kroneckerPack_eq_sum` (theorem, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L136))

> Packing written as a sum of shifted `Y`-coefficients.

```lean
theorem kroneckerPack_eq_sum [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (D : ℕ) (p : CBivariate R) :
    kroneckerPack D p
      = (CPolynomial.support p).sum
          (fun i => CPolynomial.coeff p i * CPolynomial.X ^ (D * i))
```

`CompPoly.CBivariate.coeff_kroneckerPack` (theorem, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L148))

> Coefficient of the packed polynomial, when the `X`-degree is below the gap.

```lean
theorem coeff_kroneckerPack [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    {D : ℕ} (hD : 0 < D) (p : CBivariate R) (hp : natDegreeX p < D) (n : ℕ) :
    CPolynomial.coeff (kroneckerPack D p) n = coeff p (n % D) (n / D)
```

`CompPoly.CBivariate.kroneckerPackFast` (definition, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L173))

> Efficient packing, linear in the output.

```lean
def kroneckerPackFast [Semiring R] [BEq R] [LawfulBEq R]
    (D : ℕ) (p : CBivariate R) : CPolynomial R
```

`CompPoly.CBivariate.kroneckerPackFast_eq` (theorem, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L179))

> `kroneckerPackFast` equals `kroneckerPack`.

```lean
theorem kroneckerPackFast_eq [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (D : ℕ) (p : CBivariate R) : kroneckerPackFast D p = kroneckerPack D p
```

`CompPoly.CBivariate.coeff_kroneckerUnpack_of_le` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L193))

> Unpacked coefficients with `X`-exponent at least `D` are zero.

```lean
theorem coeff_kroneckerUnpack_of_le [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] {D : ℕ} (hD : 0 < D) (P : CPolynomial R) (i j : ℕ) (hi : D ≤ i) :
    coeff (kroneckerUnpack D P) i j = 0
```

`CompPoly.CBivariate.coeff_kroneckerUnpack` (theorem, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L206))

> Unpacked coefficient at `(i, j)` with `i < D`.

```lean
theorem coeff_kroneckerUnpack [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] {D : ℕ} (hD : 0 < D) (P : CPolynomial R) (i j : ℕ) (hi : i < D) :
    coeff (kroneckerUnpack D P) i j = CPolynomial.coeff P (D * j + i)
```

`CompPoly.CBivariate.window` (definition, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L227))

> The length-`D` slice of `P` holding column `j`.

```lean
def window [Zero R] [BEq R] [LawfulBEq R] (D j : ℕ) (P : CPolynomial R) : CPolynomial R
```

`CompPoly.CBivariate.coeff_window` (theorem, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L232))

> Coefficient of a column slice.

```lean
theorem coeff_window [Zero R] [BEq R] [LawfulBEq R] (D j : ℕ) (P : CPolynomial R) (i : ℕ) :
    CPolynomial.coeff (window D j P) i =
      if i < D then CPolynomial.coeff P (D * j + i) else 0
```

`CompPoly.CBivariate.kroneckerUnpackFast` (definition, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L252))

> Efficient unpacking, assembling columns directly.

```lean
def kroneckerUnpackFast [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (D : ℕ) (P : CPolynomial R) : CBivariate R
```

`CompPoly.CBivariate.kroneckerUnpackFast_eq` (theorem, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L258))

> `kroneckerUnpackFast` equals `kroneckerUnpack`.

```lean
theorem kroneckerUnpackFast_eq [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    {D : ℕ} (hD : 0 < D) (P : CPolynomial R) :
    kroneckerUnpackFast D P = kroneckerUnpack D P
```

`CompPoly.CBivariate.kroneckerUnpack_kroneckerPack` (theorem, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L287))

> Unpacking recovers a packed polynomial when its `X`-degree is below the gap.

```lean
theorem kroneckerUnpack_kroneckerPack [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] {D : ℕ} (hD : 0 < D) (p : CBivariate R) (hp : natDegreeX p < D) :
    kroneckerUnpack D (kroneckerPack D p) = p
```

`CompPoly.CBivariate.kroneckerUnpack_mul` (theorem, [line 307](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L307))

> Bivariate multiplication as pack, univariate multiply, unpack, when the product fits
> the gap.

```lean
theorem kroneckerUnpack_mul [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] {D : ℕ} (hD : 0 < D) (p q : CBivariate R)
    (hpq : natDegreeX (p * q) < D) :
    kroneckerUnpack D (kroneckerPack D p * kroneckerPack D q) = p * q
```

`CompPoly.CBivariate.kroneckerUnpackFast_mul` (theorem, [line 315](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L315))

> `kroneckerUnpack_mul` for the efficient `kroneckerPackFast` / `kroneckerUnpackFast`.

```lean
theorem kroneckerUnpackFast_mul [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    [DecidableEq R] {D : ℕ} (hD : 0 < D) (p q : CBivariate R)
    (hpq : natDegreeX (p * q) < D) :
    kroneckerUnpackFast D (kroneckerPackFast D p * kroneckerPackFast D q) = p * q
```

`CompPoly.CBivariate.kroneckerUnpack_withFallback` (theorem, [line 323](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L323))

> Bivariate multiplication using the NTT (`withFallback`) as the univariate backend.

```lean
theorem kroneckerUnpack_withFallback [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (CPolynomial.NTT.FittingDomain R requiredLen))
    {D : ℕ} (hD : 0 < D) (p q : CBivariate R) (hpq : natDegreeX (p * q) < D) :
    kroneckerUnpack D
        (CPolynomial.NTT.FastMul.withFallback bestDomainForLength?
          (kroneckerPack D p) (kroneckerPack D q))
      = p * q
```

`CompPoly.CBivariate.kroneckerUnpack_withFallbackFast` (theorem, [line 336](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean#L336))

> Bivariate multiplication using the recursive NTT (`NTTFast.withFallback`) as the
> univariate backend.

```lean
theorem kroneckerUnpack_withFallbackFast [Field R] [BEq R] [LawfulBEq R] [DecidableEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (CPolynomial.NTT.FittingDomain R requiredLen))
    {D : ℕ} (hD : 0 < D) (p q : CBivariate R) (hpq : natDegreeX (p * q) < D) :
    kroneckerUnpack D
        (CPolynomial.NTTFast.withFallback bestDomainForLength?
          (kroneckerPack D p) (kroneckerPack D q))
      = p * q
```

## Depends on

- [Computable Bivariate Polynomials](basic.md)
- [Fast multiplication via NTT](../univariate/part-01/nttfast/fastmul.md)

## Proof depends on

- [NTTFast multiplication correctness](../univariate/part-01/nttfast/correctness/pipeline.md)
- [Proofs of Correctness for CPolynomial Operations, wrt Mathlib Specs](../univariate/part-02/topoly/impl.md)

## Sources

- [CompPoly/Bivariate/Kronecker.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/Kronecker.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Bivariate.Kronecker.json)
