---
catalog: module
lean: CompPoly.CPolynomial.NTT.FastMul.pointwiseMul, CompPoly.CPolynomial.NTT.FastMul.size_pointwiseMul, CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulSpec, CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulImpl, CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulImpl_correct, CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulSpec_coeff, CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulSpec_trim_eq_mul, CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulImpl_trim_eq_mul, CompPoly.CPolynomial.NTT.FastMul.fastMulSpec, CompPoly.CPolynomial.NTT.FastMul.fastMulImpl, CompPoly.CPolynomial.NTT.FastMul.safeFastMul, CompPoly.CPolynomial.NTT.FastMul.fastMulImpl_correct, CompPoly.CPolynomial.NTT.FastMul.fastMulSpec_eq_mul, CompPoly.CPolynomial.NTT.FastMul.fastMulImpl_eq_mul, CompPoly.CPolynomial.NTT.FastMul.safeFastMul_eq_mul, CompPoly.CPolynomial.NTT.FastMul.withFallback, CompPoly.CPolynomial.NTT.FastMul.withFallback_eq_mul
statement: formalized
proof: formalized
---

# Fast Multiplication via NTT

`CompPoly.Univariate.NTT.FastMul`, in [CompPoly/Univariate/NTT/FastMul.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean), by Salih Erdem Koçak, Doran Pamukçu.

> This file wires forward NTT, pointwise multiplication, and inverse NTT into a
> spec/implementation pipeline.

`CompPoly.CPolynomial.NTT.FastMul.pointwiseMul` (definition, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L33))

> Pointwise multiplication in evaluation form.

```lean
def pointwiseMul (D : Domain R) (a b : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.FastMul.size_pointwiseMul` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L36))

```lean
theorem size_pointwiseMul (D : Domain R) (a b : Array R) :
    (pointwiseMul D a b).size = D.n
```

`CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulSpec` (definition, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L178))

> Raw spec pipeline for NTT-based multiplication.
>
> This is the low-level array computation and deliberately does not trim the
> output.

```lean
def fastMulSpec (D : Domain R) (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulImpl` (definition, [line 212](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L212))

> Raw implementation pipeline for NTT-based multiplication.
>
> Correctness as ordinary polynomial multiplication requires
> `Domain.fits D p q`; see `fastMulImpl_trim_eq_mul`. Without this precondition,
> this function only exposes the raw NTT pipeline result, which may include cyclic
> wraparound and has no product-correctness guarantee. The output is not trimmed;
> use `FastMul.fastMulImpl` for the canonical public API.

```lean
def fastMulImpl (D : Domain R) (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulImpl_correct` (theorem, [line 220](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L220))

```lean
theorem fastMulImpl_correct (D : Domain R) (p q : CPolynomial.Raw R) :
    fastMulImpl D p q = fastMulSpec D p q
```

`CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulSpec_coeff` (theorem, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L224))

```lean
theorem fastMulSpec_coeff (D : Domain R) (p q : CPolynomial.Raw R)
    (hfit : Domain.fits D p q) (i : Nat) :
    (fastMulSpec D p q).coeff i = (p * q).coeff i
```

`CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulSpec_trim_eq_mul` (theorem, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L264))

```lean
theorem fastMulSpec_trim_eq_mul (D : Domain R) (p q : CPolynomial.Raw R)
    (hfit : Domain.fits D p q) : (fastMulSpec D p q).trim = p * q
```

`CompPoly.CPolynomial.NTT.FastMul.Raw.fastMulImpl_trim_eq_mul` (theorem, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L275))

```lean
theorem fastMulImpl_trim_eq_mul (D : Domain R) (p q : CPolynomial.Raw R)
    (hfit : Domain.fits D p q) : (fastMulImpl D p q).trim = p * q
```

`CompPoly.CPolynomial.NTT.FastMul.fastMulSpec` (definition, [line 284](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L284))

> Spec pipeline for NTT-based multiplication as a canonical polynomial.

```lean
def fastMulSpec (D : Domain R) (p q : CPolynomial R) : CPolynomial R
```

`CompPoly.CPolynomial.NTT.FastMul.fastMulImpl` (definition, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L295))

> Implementation pipeline for NTT-based multiplication as a canonical polynomial.
>
> Correctness as ordinary polynomial multiplication requires
> `Domain.fits D p.val q.val`; see `fastMulImpl_eq_mul`. Without this precondition,
> the raw NTT computation may include cyclic wraparound before canonicalization.

```lean
def fastMulImpl (D : Domain R) (p q : CPolynomial R) : CPolynomial R
```

`CompPoly.CPolynomial.NTT.FastMul.safeFastMul` (definition, [line 305](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L305))

> Safe NTT-based multiplication wrapper.
>
> This computes with `fastMulImpl`, but requires the caller to provide the
> `Domain.fits D p.val q.val` proof at the call site.

```lean
def safeFastMul
    (D : Domain R) (p q : CPolynomial R) (_hfit : Domain.fits D p.val q.val) :
    CPolynomial R
```

`CompPoly.CPolynomial.NTT.FastMul.fastMulImpl_correct` (theorem, [line 310](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L310))

```lean
theorem fastMulImpl_correct (D : Domain R) (p q : CPolynomial R) :
    fastMulImpl D p q = fastMulSpec D p q
```

`CompPoly.CPolynomial.NTT.FastMul.fastMulSpec_eq_mul` (theorem, [line 315](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L315))

```lean
theorem fastMulSpec_eq_mul (D : Domain R) (p q : CPolynomial R)
    (hfit : Domain.fits D p.val q.val) : fastMulSpec D p q = p * q
```

`CompPoly.CPolynomial.NTT.FastMul.fastMulImpl_eq_mul` (theorem, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L320))

```lean
theorem fastMulImpl_eq_mul (D : Domain R) (p q : CPolynomial R)
    (hfit : Domain.fits D p.val q.val) : fastMulImpl D p q = p * q
```

`CompPoly.CPolynomial.NTT.FastMul.safeFastMul_eq_mul` (theorem, [line 331](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L331))

> The safe wrapper is equivalent to ordinary canonical polynomial multiplication.
>
> There are no extra assumptions because the required `Domain.fits D p.val q.val`
> proof is already an argument of `safeFastMul`.

```lean
theorem safeFastMul_eq_mul (D : Domain R) (p q : CPolynomial R)
    (hfit : Domain.fits D p.val q.val) : safeFastMul D p q hfit = p * q
```

`CompPoly.CPolynomial.NTT.FastMul.withFallback` (definition, [line 342](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L342))

> NTT-backed multiplication with canonical multiplication as a fallback.
>
> The selector should return a domain fitting the required convolution length.
> When it does, this uses `fastMulImpl`; otherwise it falls back to canonical
> `CPolynomial` multiplication.

```lean
def withFallback
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (FittingDomain R requiredLen))
    (p q : CPolynomial R) : CPolynomial R
```

`CompPoly.CPolynomial.NTT.FastMul.withFallback_eq_mul` (theorem, [line 352](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean#L352))

> `withFallback` agrees with canonical polynomial multiplication.

```lean
theorem withFallback_eq_mul
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (FittingDomain R requiredLen))
    (p q : CPolynomial R) :
    withFallback bestDomainForLength? p q = p * q
```

## Depends on

- [Computable Univariate Polynomials](../basic.md)
- [Inverse NTT](inverse.md)

## Proof depends on

- [NTT and Evaluation](evaluation.md)
- [NTT Kernel Identities](kernel.md)
- [`toPoly` Equivalence](../../part-02/topoly/equiv.md)

## Sources

- [CompPoly/Univariate/NTT/FastMul.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/NTT/FastMul.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.FastMul.json)
