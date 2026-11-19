---
catalog: module
lean: CPoly.CMvMonomial.instDelimitedCodec, CPoly.CMvMonomial.instDelimitedCodecVector, CPoly.CMvMonomial.valid_iff, CPoly.CMvMonomial.encode_eq, CPoly.CMvMonomial.instLawfulBEqCmp, CPoly.Unlawful.ofList_toList, CPoly.CMvPolynomial.instDelimitedCodec, CPoly.CMvPolynomial.valid_iff, CPoly.CMvPolynomial.encode_eq
statement: formalized
proof: formalized
---

# Serialization of multivariate polynomials

`CompPoly.Multivariate.Bytes`, in [CompPoly/Multivariate/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean), by Derek Sorensen.

> A `CMvPolynomial n R` is a sorted map from exponent vectors to nonzero coefficients, so its
> `toList` is already a canonical sequence of terms. It encodes as a `u64` term count followed
> by the terms in key order, each term its `n` exponents as `u64` words and then its coefficient.
> Decoding rebuilds the map and drops zero coefficients, so it lands on the polynomial. There is
> no fixed-width multivariate codec: genuinely multivariate protocol messages are multilinear,
> and those have the dense codec of `CompPoly.Multilinear.Bytes`.
>
> A polynomial is `Valid` when its term count and every exponent fit in a `u64` and its
> coefficients are valid.

> ## Monomials: `n` exponents, no count

`CPoly.CMvMonomial.instDelimitedCodec` (instance, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L34))

```lean
instance CMvMonomial.instDelimitedCodec (n : ℕ) : DelimitedCodec (CMvMonomial n)
```

`CPoly.CMvMonomial.instDelimitedCodecVector` (instance, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L39))

> The same codec at `Vector ℕ n`, the underlying type of `CMvMonomial n`, for goals that
> instance search sees only after unfolding (the `#m[…]` notation elaborates to a `Vector`).

```lean
instance CMvMonomial.instDelimitedCodecVector (n : ℕ) : DelimitedCodec (Vector ℕ n)
```

`CPoly.CMvMonomial.valid_iff` (theorem, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L42))

```lean
theorem CMvMonomial.valid_iff {n : ℕ} (m : CMvMonomial n) :
    Valid m ↔ ∀ e ∈ (m : Vector ℕ n).toList, e < 2 ^ 64
```

`CPoly.CMvMonomial.encode_eq` (theorem, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L45))

```lean
theorem CMvMonomial.encode_eq {n : ℕ} (m : CMvMonomial n) :
    encode m = encodeList (m : Vector ℕ n).toList
```

> ## Rebuilding a map from its own term list

`CPoly.CMvMonomial.instLawfulBEqCmp` (instance, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L53))

> `compare` and `==` agree on monomials: both decide equality. Built from `LawfulEqCmp` and
> `LawfulBEq` rather than transported from `Vector.compareLex`, whose instance body is not
> available to the kernel here.

```lean
instance CMvMonomial.instLawfulBEqCmp (n : ℕ) :
    LawfulBEqCmp (Ord.compare (α := CMvMonomial n))
```

`CPoly.Unlawful.ofList_toList` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L63))

> A tree map is the map of its own term list.

```lean
theorem Unlawful.ofList_toList (p : Unlawful n R) : Unlawful.ofList p.toList = p
```

> ## Polynomials

`CPoly.CMvPolynomial.instDelimitedCodec` (instance, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L87))

> A `u64` term count, then each term as `n` exponents and a coefficient.

```lean
instance CMvPolynomial.instDelimitedCodec [DelimitedCodec R] :
    DelimitedCodec (CMvPolynomial n R)
```

`CPoly.CMvPolynomial.valid_iff` (theorem, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L97))

```lean
theorem CMvPolynomial.valid_iff [DelimitedCodec R] (p : CMvPolynomial n R) :
    Valid p ↔ p.1.toList.length < 2 ^ 64 ∧
      ∀ t ∈ p.1.toList, (∀ e ∈ (t.1 : Vector ℕ n).toList, e < 2 ^ 64) ∧ Valid t.2
```

`CPoly.CMvPolynomial.encode_eq` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean#L101))

```lean
theorem CMvPolynomial.encode_eq [DelimitedCodec R] (p : CMvPolynomial n R) :
    encode p = encodeU64 p.1.toList.length ++ encodeList p.1.toList
```

## Depends on

- [Self-delimiting byte codecs](../data/bytes/delimited.md)
- [Computable multivariate polynomials](basic.md)

## Sources

- [CompPoly/Multivariate/Bytes.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/Bytes.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.Bytes.json)
