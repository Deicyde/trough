---
catalog: module
lean: AesField.canonicalNat_bound, AesField.canonicalNat_toNat, AesField.byteCodec_width
statement: formalized
proof: formalized
---

# Serialization of the AES field

`CompPoly.Fields.Binary.Aes.Bytes`, in [CompPoly/Fields/Binary/Aes/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Bytes.lean), by Derek Sorensen.

> An `AesField` element is a bit pattern in the polynomial basis of
> `GF(2)[X] / (X^8 + X^4 + X^3 + X + 1)`, bit `i` the coefficient of `X^i`, so it encodes as the
> one byte `toBitVec`. Level three of the binary tower has the same cardinality and a different
> basis; the two encodings are not interchangeable, and `AesField.toGhash` remains the only
> sanctioned bridge out of this presentation.

`AesField.canonicalNat_bound` (theorem, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Bytes.lean#L32))

```lean
theorem canonicalNat_bound : CanonicalNat.bound AesField = 2 ^ 8
```

`AesField.canonicalNat_toNat` (theorem, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Bytes.lean#L34))

```lean
theorem canonicalNat_toNat (x : AesField) : CanonicalNat.toNat x = (toBitVec x).toNat
```

`AesField.byteCodec_width` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Bytes.lean#L37))

```lean
theorem byteCodec_width : ByteCodec.width AesField = 1
```

## Depends on

- [Fixed-width byte codecs](../../../data/bytes/codec.md)
- [Canonical naturals](../../../data/classes/canonicalnat.md)
- [AES polynomial-basis coordinates and arithmetic](arithmetic.md)

## Proof depends on

- [Byte codecs from canonical naturals](../../../data/bytes/canonicalnat.md)

## Sources

- [CompPoly/Fields/Binary/Aes/Bytes.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Bytes.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Aes.Bytes.json)
