---
catalog: module
lean: CompPoly.ByteCodec, CompPoly.ByteCodec.toBytes_injective, CompPoly.ByteCodec.toBytes_inj, CompPoly.ByteCodec.toByteArray, CompPoly.ByteCodec.data_toByteArray, CompPoly.ByteCodec.size_toByteArray, CompPoly.ByteCodec.toByteArray_injective, CompPoly.ByteCodec.ofByteArray?, CompPoly.ByteCodec.ofByteArray?_toByteArray, CompPoly.ByteCodec.serialize_eq_toByteArray, CompPoly.ByteCodec.serialize_eq_toBytes, CompPoly.ByteCodec.deserialize_byteArray_eq, CompPoly.ByteCodec.deserialize_vector_eq, CompPoly.ByteCodec.deserialize_serialize
statement: formalized
proof: formalized
---

# Fixed-width byte codecs

`CompPoly.Data.Bytes.Codec`, in [CompPoly/Data/Bytes/Codec.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean), by Derek Sorensen.

> `ByteCodec F` is a fixed-width byte encoding of `F` with a decoder that succeeds on every
> encoding. Its single law, `ofBytes?_toBytes`, makes `toBytes` injective, and from it the
> protocol-facing classes follow for free: `HasSize F UInt8`, `Serialize F ByteArray` with
> `Serialize.IsInjective`, `DeserializeOption`, and `Serde`, together with the same for
> `Vector UInt8 (width F)`.
>
> The encoding is a property of the *value*, not of the carrier: two carriers of the same field
> must give the same bytes for the same element. Scalar fields derive their codec from
> `CanonicalNat` (`ByteCodec.ofCanonicalNat`, in `CompPoly.Data.Bytes.CanonicalNat`); composite
> types such as extensions and degree-bounded polynomials concatenate the codecs of their parts.

`CompPoly.ByteCodec` (class, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L33))

> A fixed-width byte encoding of `F` whose decoder recovers every encoded element.

```lean
class ByteCodec (F : Type u) where
  /-- The number of bytes of every encoding. -/
  width : ℕ
  /-- Encode an element. -/
  toBytes : F → Vector UInt8 width
  /-- Decode `width` bytes, failing on strings that encode no element. -/
  ofBytes? : Vector UInt8 width → Option F
  ofBytes?_toBytes (x : F) : ofBytes? (toBytes x) = some x
```

`CompPoly.ByteCodec.toBytes_injective` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L48))

```lean
theorem toBytes_injective : Function.Injective (toBytes : F → Vector UInt8 (width F))
```

`CompPoly.ByteCodec.toBytes_inj` (theorem, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L54))

```lean
theorem toBytes_inj {x y : F} : toBytes x = toBytes y ↔ x = y
```

`CompPoly.ByteCodec.toByteArray` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L58))

> The encoding as a `ByteArray` of size `width F`.

```lean
def toByteArray (x : F) : ByteArray
```

`CompPoly.ByteCodec.data_toByteArray` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L60))

```lean
theorem data_toByteArray (x : F) : (toByteArray x).data = (toBytes x).toArray
```

`CompPoly.ByteCodec.size_toByteArray` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L62))

```lean
theorem size_toByteArray (x : F) : (toByteArray x).size = width F
```

`CompPoly.ByteCodec.toByteArray_injective` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L65))

```lean
theorem toByteArray_injective : Function.Injective (toByteArray : F → ByteArray)
```

`CompPoly.ByteCodec.ofByteArray?` (definition, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L72))

> Decode a `ByteArray`, failing unless it has size `width F` and encodes an element.

```lean
def ofByteArray? (b : ByteArray) : Option F
```

`CompPoly.ByteCodec.ofByteArray?_toByteArray` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L76))

```lean
theorem ofByteArray?_toByteArray (x : F) : ofByteArray? (toByteArray x) = some x
```

> ## Derived protocol interfaces

`CompPoly.ByteCodec.serialize_eq_toByteArray` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L104))

```lean
theorem serialize_eq_toByteArray (x : F) : (serialize x : ByteArray) = toByteArray x
```

`CompPoly.ByteCodec.serialize_eq_toBytes` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L106))

```lean
theorem serialize_eq_toBytes (x : F) :
    (serialize x : Vector UInt8 (width F)) = toBytes x
```

`CompPoly.ByteCodec.deserialize_byteArray_eq` (theorem, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L109))

```lean
theorem deserialize_byteArray_eq (b : ByteArray) :
    (DeserializeOption.deserialize b : Option F) = ofByteArray? b
```

`CompPoly.ByteCodec.deserialize_vector_eq` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L112))

```lean
theorem deserialize_vector_eq (v : Vector UInt8 (width F)) :
    (DeserializeOption.deserialize v : Option F) = ofBytes? v
```

`CompPoly.ByteCodec.deserialize_serialize` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean#L115))

```lean
theorem deserialize_serialize (x : F) :
    (DeserializeOption.deserialize (serialize x : ByteArray) : Option F) = some x
```

## Depends on

- [`HasSize` class](../classes/hassize.md)
- [Serialization and deserialization classes](../classes/serialize.md)

## Sources

- [CompPoly/Data/Bytes/Codec.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/Codec.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Bytes.Codec.json)
