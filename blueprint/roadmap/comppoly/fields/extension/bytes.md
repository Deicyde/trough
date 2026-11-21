---
catalog: module
lean: CompPoly.Extension.Ext.byteCodec_width, CompPoly.Extension.Ext.toBytes_eq
statement: formalized
proof: formalized
---

# Serialization of field extensions

`CompPoly.Fields.Extension.Bytes`, in [CompPoly/Fields/Extension/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bytes.lean), by Derek Sorensen.

> An element of `Ext P` is its coefficient vector, ascending powers of the adjoined root, and it
> encodes as the concatenation of the coefficient encodings: `P.d * width F` bytes. This is how
> arkworks and plonky3 serialize extension fields, and it is *not* the little-endian expansion of
> the element's base-`q` canonical natural, which is why `Ext` carries a `ByteCodec` but no
> `CanonicalNat`.
>
> A challenge in `Ext P` is likewise read coefficient by coefficient from `P.d * k` bytes
> (`Deserialize (Ext P) (Vector UInt8 (P.d * k))`), matching how a sponge over the base field
> samples extension elements.
>
> `CompPoly.Data.Bytes.CanonicalNat` is imported so that an extension of a `ZMod` base field
> serializes with no further imports.

`CompPoly.Extension.Ext.byteCodec_width` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bytes.lean#L43))

```lean
theorem byteCodec_width [ByteCodec F] :
    ByteCodec.width (Ext P) = P.d * ByteCodec.width F
```

`CompPoly.Extension.Ext.toBytes_eq` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bytes.lean#L46))

```lean
theorem toBytes_eq [ByteCodec F] (x : Ext P) : ByteCodec.toBytes x = ByteCodec.toBytes x.coeffs
```

## Depends on

- [Byte codecs of vectors](../../data/bytes/vector.md)
- [Computable arithmetic for monic quotient presentations](arithmetic.md)

## Sources

- [CompPoly/Fields/Extension/Bytes.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Extension/Bytes.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Extension.Bytes.json)
