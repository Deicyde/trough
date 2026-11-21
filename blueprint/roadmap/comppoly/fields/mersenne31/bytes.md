---
catalog: module
lean: Mersenne31.Fast.toNat_lt, Mersenne31.Fast.ofField_cast_toNat, Mersenne31.Fast.canonicalNat_bound, Mersenne31.Fast.canonicalNat_toNat, Mersenne31.Fast.byteCodec_width, Mersenne31.Fast.toBytes_ofField
statement: formalized
proof: formalized
---

# Serialization of the fast Mersenne31 carrier

`CompPoly.Fields.Mersenne31.Bytes`, in [CompPoly/Fields/Mersenne31/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Mersenne31/Bytes.lean), by Derek Sorensen.

> `Mersenne31.Fast.Field` stores the canonical residue in a `UInt32`, so its canonical natural is
> the stored word and the four-byte little-endian encoding agrees with `Mersenne31.Field`
> (`toBytes_ofField`).

`Mersenne31.Fast.toNat_lt` (theorem, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Mersenne31/Bytes.lean#L25))

```lean
theorem toNat_lt (x : Field) : toNat x < Mersenne31.fieldSize
```

`Mersenne31.Fast.ofField_cast_toNat` (theorem, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Mersenne31/Bytes.lean#L27))

```lean
theorem ofField_cast_toNat (x : Field) : ofField (toNat x : Mersenne31.Field) = x
```

`Mersenne31.Fast.canonicalNat_bound` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Mersenne31/Bytes.lean#L39))

```lean
theorem canonicalNat_bound : CanonicalNat.bound Field = Mersenne31.fieldSize
```

`Mersenne31.Fast.canonicalNat_toNat` (theorem, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Mersenne31/Bytes.lean#L41))

```lean
theorem canonicalNat_toNat (x : Field) : CanonicalNat.toNat x = toNat x
```

`Mersenne31.Fast.byteCodec_width` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Mersenne31/Bytes.lean#L43))

```lean
theorem byteCodec_width : ByteCodec.width Field = 4
```

`Mersenne31.Fast.toBytes_ofField` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Mersenne31/Bytes.lean#L46))

> The fast carrier and `Mersenne31.Field` encode the same element identically.

```lean
theorem toBytes_ofField (n : Mersenne31.Field) :
    ByteCodec.toBytes (ofField n) = ByteCodec.toBytes n
```

## Depends on

- [Byte codecs from canonical naturals](../../data/bytes/canonicalnat.md)
- [FastMersenne31 — UInt32-backed Mersenne-31 field arithmetic](fast.md)

## Sources

- [CompPoly/Fields/Mersenne31/Bytes.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Mersenne31/Bytes.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Mersenne31.Bytes.json)
