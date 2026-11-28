---
catalog: module
lean: BF128Ghash.ConcreteBF128Ghash.canonicalNat_bound, BF128Ghash.ConcreteBF128Ghash.canonicalNat_toNat, BF128Ghash.ConcreteBF128Ghash.byteCodec_width
statement: formalized
proof: formalized
---

# Serialization of the GHASH field

`CompPoly.Fields.Binary.BF128Ghash.Bytes`, in [CompPoly/Fields/Binary/BF128Ghash/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF128Ghash/Bytes.lean), by Derek Sorensen.

> A `ConcreteBF128Ghash` element is a bit pattern in the polynomial basis of
> `GF(2)[X] / (X^128 + X^7 + X^2 + X + 1)`, bit `i` the coefficient of `X^i`. Its canonical
> natural is that pattern read as an integer and its encoding the sixteen little-endian bytes of
> the word. This is the field's own presentation; GCM's big-endian, bit-reflected block format
> is a separate wire codec and is not provided here.

`BF128Ghash.ConcreteBF128Ghash.canonicalNat_bound` (theorem, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF128Ghash/Bytes.lean#L34))

```lean
theorem canonicalNat_bound : CanonicalNat.bound ConcreteBF128Ghash = 2 ^ 128
```

`BF128Ghash.ConcreteBF128Ghash.canonicalNat_toNat` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF128Ghash/Bytes.lean#L36))

```lean
theorem canonicalNat_toNat (x : ConcreteBF128Ghash) :
    CanonicalNat.toNat x = x.toBitVec.toNat
```

`BF128Ghash.ConcreteBF128Ghash.byteCodec_width` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF128Ghash/Bytes.lean#L39))

```lean
theorem byteCodec_width : ByteCodec.width ConcreteBF128Ghash = 16
```

## Depends on

- [Fixed-width byte codecs](../../../../data/bytes/codec.md)
- [Canonical naturals](../../../../data/classes/canonicalnat.md)
- [GHASH polynomial-basis arithmetic](arithmetic.md)

## Proof depends on

- [Byte codecs from canonical naturals](../../../../data/bytes/canonicalnat.md)

## Sources

- [CompPoly/Fields/Binary/BF128Ghash/Bytes.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/BF128Ghash/Bytes.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.BF128Ghash.Bytes.json)
