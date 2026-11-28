---
catalog: module
lean: BF64.canonicalNat_bound, BF64.canonicalNat_toNat, BF64.byteCodec_width
statement: formalized
proof: formalized
---

# Serialization of `BF64`

`CompPoly.Fields.Binary.BF64.Bytes`, in [CompPoly/Fields/Binary/BF64/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF64/Bytes.lean), by Derek Sorensen.

> A `BF64` element is a bit pattern in the polynomial basis of
> `GF(2)[X] / (X^64 + X^4 + X^3 + X + 1)`, bit `i` the coefficient of `X^i`. Its canonical natural
> is that pattern read as an integer, and its encoding is the eight little-endian bytes of the
> word, the same bytes a `u64::to_le_bytes` of the word gives. No other presentation of
> `GF(2^64)` is implied.

`BF64.canonicalNat_bound` (theorem, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF64/Bytes.lean#L32))

```lean
theorem canonicalNat_bound : CanonicalNat.bound BF64 = 2 ^ 64
```

`BF64.canonicalNat_toNat` (theorem, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF64/Bytes.lean#L34))

```lean
theorem canonicalNat_toNat (x : BF64) : CanonicalNat.toNat x = x.toBitVec.toNat
```

`BF64.byteCodec_width` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF64/Bytes.lean#L36))

```lean
theorem byteCodec_width : ByteCodec.width BF64 = 8
```

## Depends on

- [Fixed-width byte codecs](../../../data/bytes/codec.md)
- [Canonical naturals](../../../data/classes/canonicalnat.md)
- [The computable `GF(2^64)` carrier](impl.md)

## Proof depends on

- [Byte codecs from canonical naturals](../../../data/bytes/canonicalnat.md)

## Sources

- [CompPoly/Fields/Binary/BF64/Bytes.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF64/Bytes.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.BF64.Bytes.json)
