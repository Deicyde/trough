---
catalog: module
lean: Goldilocks.Fast.toNat_lt, Goldilocks.Fast.ofField_cast_toNat, Goldilocks.Fast.canonicalNat_bound, Goldilocks.Fast.canonicalNat_toNat, Goldilocks.Fast.byteCodec_width, Goldilocks.Fast.toBytes_ofField
statement: formalized
proof: formalized
---

# Serialization of the fast Goldilocks carrier

`CompPoly.Fields.Goldilocks.Bytes`, in [CompPoly/Fields/Goldilocks/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Bytes.lean), by Derek Sorensen.

> `Goldilocks.Fast.Field` stores the canonical residue in a `UInt64`, so its canonical natural is
> the stored word and the eight-byte little-endian encoding agrees with `Goldilocks.Field`
> (`toBytes_ofField`).

`Goldilocks.Fast.toNat_lt` (theorem, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Bytes.lean#L25))

```lean
theorem toNat_lt (x : Field) : toNat x < Goldilocks.fieldSize
```

`Goldilocks.Fast.ofField_cast_toNat` (theorem, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Bytes.lean#L27))

```lean
theorem ofField_cast_toNat (x : Field) : ofField (toNat x : Goldilocks.Field) = x
```

`Goldilocks.Fast.canonicalNat_bound` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Bytes.lean#L35))

```lean
theorem canonicalNat_bound : CanonicalNat.bound Field = Goldilocks.fieldSize
```

`Goldilocks.Fast.canonicalNat_toNat` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Bytes.lean#L37))

```lean
theorem canonicalNat_toNat (x : Field) : CanonicalNat.toNat x = toNat x
```

`Goldilocks.Fast.byteCodec_width` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Bytes.lean#L39))

```lean
theorem byteCodec_width : ByteCodec.width Field = 8
```

`Goldilocks.Fast.toBytes_ofField` (theorem, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Bytes.lean#L42))

> The fast carrier and `Goldilocks.Field` encode the same element identically.

```lean
theorem toBytes_ofField (n : Goldilocks.Field) :
    ByteCodec.toBytes (ofField n) = ByteCodec.toBytes n
```

## Depends on

- [Byte codecs from canonical naturals](../../data/bytes/canonicalnat.md)
- [Fast Goldilocks Field](fast.md)

## Sources

- [CompPoly/Fields/Goldilocks/Bytes.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Goldilocks/Bytes.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Goldilocks.Bytes.json)
