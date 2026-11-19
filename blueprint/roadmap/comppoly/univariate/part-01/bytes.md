---
catalog: module
lean: CompPoly.CPolynomial.ofArray_val, CompPoly.CPolynomial.ofFn_mem_degreeLT, CompPoly.CPolynomial.ofFn_coeff_of_mem_degreeLT, CompPoly.CPolynomial.coeffVector, CompPoly.CPolynomial.ofCoeffVector, CompPoly.CPolynomial.ofCoeffVector_coeffVector, CompPoly.CPolynomial.instByteCodecDegreeLT, CompPoly.CPolynomial.width_degreeLT, CompPoly.CPolynomial.toBytes_degreeLT, CompPoly.CPolynomial.instDelimitedCodec, CompPoly.CPolynomial.valid_iff, CompPoly.CPolynomial.valid_iff_size_lt, CompPoly.CPolynomial.encode_eq, CompPoly.CPolynomial.toList_val_eq_ofFn, CompPoly.CPolynomial.encode_eq_encodeU64_append_toBytes
statement: formalized
proof: formalized
---

# Serialization of univariate polynomials

`CompPoly.Univariate.Bytes`, in [CompPoly/Univariate/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean), by Derek Sorensen.

> Two encodings of a `CPolynomial R`, and they agree.
>
> * **Fixed width, for protocol messages.** A polynomial of degree below `n`, an element of
>   `↥(degreeLT n)`, is its first `n` coefficients, zero-padded: `n * width R` bytes through the
>   vector codec. Decoding trims. This is `ByteCodec ↥(degreeLT n)`, unconditionally injective,
>   the message shape of a sumcheck round polynomial or a FRI fold.
> * **Self-delimiting, for fixtures and hashing.** A `u64` little-endian coefficient count, then
>   the coefficients. This is `DelimitedCodec (CPolynomial R)` over any delimited coefficient
>   codec, so it nests (`CompPoly.Bivariate.Bytes`). Injective because the representation is
>   canonical: no trailing zeros, so equal coefficient lists are equal polynomials. A polynomial
>   is `Valid` when its size fits in a `u64` and its coefficients are valid.
>
> `encode_eq_encodeU64_append_toBytes` ties the two: the self-delimiting encoding is the count
> followed by the fixed-width encoding at `n = size`.

`CompPoly.CPolynomial.ofArray_val` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L39))

> Rebuilding a canonical polynomial from its own coefficient array gives it back.

```lean
theorem ofArray_val (p : CPolynomial R) : ofArray p.val = p
```

`CompPoly.CPolynomial.ofFn_mem_degreeLT` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L43))

> `ofFn` on `n` coefficients has degree below `n`.

```lean
theorem ofFn_mem_degreeLT {n : ℕ} (f : Fin n → R) : ofFn f ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.ofFn_coeff_of_mem_degreeLT` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L49))

> A polynomial of degree below `n` is `ofFn` of its first `n` coefficients.

```lean
theorem ofFn_coeff_of_mem_degreeLT {n : ℕ} {p : CPolynomial R} (hp : p ∈ degreeLT (R := R) n) :
    ofFn (fun i : Fin n => coeff p i) = p
```

> ## Fixed width: `degreeLT n`

`CompPoly.CPolynomial.coeffVector` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L63))

> The coefficient vector of a polynomial of degree below `n`, zero-padded.

```lean
def coeffVector (n : ℕ) (p : ↥(degreeLT (R := R) n)) : Vector R n
```

`CompPoly.CPolynomial.ofCoeffVector` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L67))

> The polynomial with the given `n` coefficients, as an element of `degreeLT n`.

```lean
def ofCoeffVector (n : ℕ) (v : Vector R n) : ↥(degreeLT (R := R) n)
```

`CompPoly.CPolynomial.ofCoeffVector_coeffVector` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L71))

```lean
theorem ofCoeffVector_coeffVector (n : ℕ) (p : ↥(degreeLT (R := R) n)) :
    ofCoeffVector n (coeffVector n p) = p
```

`CompPoly.CPolynomial.instByteCodecDegreeLT` (instance, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L79))

> Degree below `n`: the `n` coefficients, `n * width R` bytes.

```lean
instance instByteCodecDegreeLT [ByteCodec R] (n : ℕ) : ByteCodec ↥(degreeLT (R := R) n)
```

`CompPoly.CPolynomial.width_degreeLT` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L86))

```lean
theorem width_degreeLT [ByteCodec R] (n : ℕ) :
    ByteCodec.width ↥(degreeLT (R := R) n) = n * ByteCodec.width R
```

`CompPoly.CPolynomial.toBytes_degreeLT` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L89))

```lean
theorem toBytes_degreeLT [ByteCodec R] {n : ℕ} (p : ↥(degreeLT (R := R) n)) :
    ByteCodec.toBytes p = ByteCodec.toBytes (coeffVector n p)
```

> ## Self-delimiting: `CPolynomial R`

`CompPoly.CPolynomial.instDelimitedCodec` (instance, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L96))

> A `u64` coefficient count, then the coefficients.

```lean
instance instDelimitedCodec [DelimitedCodec R] : DelimitedCodec (CPolynomial R)
```

`CompPoly.CPolynomial.valid_iff` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L103))

```lean
theorem valid_iff [DelimitedCodec R] (p : CPolynomial R) :
    DelimitedCodec.Valid p ↔ p.val.size < 2 ^ 64 ∧ ∀ c ∈ p.val.toList, DelimitedCodec.Valid c
```

`CompPoly.CPolynomial.valid_iff_size_lt` (theorem, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L109))

> Over a fixed-width coefficient type, a polynomial is valid exactly when its size fits.

```lean
theorem valid_iff_size_lt [ByteCodec R] (p : CPolynomial R) :
    DelimitedCodec.Valid p ↔ p.val.size < 2 ^ 64
```

`CompPoly.CPolynomial.encode_eq` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L114))

```lean
theorem encode_eq [DelimitedCodec R] (p : CPolynomial R) :
    DelimitedCodec.encode p
      = DelimitedCodec.encodeU64 p.val.size ++ DelimitedCodec.encodeList p.val.toList
```

`CompPoly.CPolynomial.toList_val_eq_ofFn` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L122))

> The coefficient list of a polynomial is its coefficient function on `Fin p.val.size`.

```lean
theorem toList_val_eq_ofFn (p : CPolynomial R) :
    p.val.toList = List.ofFn fun i : Fin p.val.size => coeff p i
```

`CompPoly.CPolynomial.encode_eq_encodeU64_append_toBytes` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean#L134))

> The self-delimiting encoding is the count followed by the fixed-width encoding at
> `n = size`: the two formats agree on their common part.

```lean
theorem encode_eq_encodeU64_append_toBytes [ByteCodec R] (p : CPolynomial R) :
    DelimitedCodec.encode p
      = DelimitedCodec.encodeU64 p.val.size
        ++ (ByteCodec.toBytes (⟨p, mem_degreeLT_iff_size_le.mpr le_rfl⟩ :
            ↥(degreeLT (R := R) p.val.size))).toList
```

## Depends on

- [Self-delimiting byte codecs](../../data/bytes/delimited.md)
- [Byte codecs of vectors](../../data/bytes/vector.md)
- [Linear Algebra API for Computable Univariate Polynomials](linear.md)

## Sources

- [CompPoly/Univariate/Bytes.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Bytes.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Bytes.json)
