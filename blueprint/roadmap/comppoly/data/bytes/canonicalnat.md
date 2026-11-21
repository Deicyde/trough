---
catalog: module
lean: CompPoly.ByteCodec.ofCanonicalNat, CompPoly.CanonicalNat.ofBytesModOrder, CompPoly.CanonicalNat.ofByteArrayModOrder, CompPoly.CanonicalNat.deserialize_vector_eq, CompPoly.CanonicalNat.deserialize_byteArray_eq, CompPoly.CanonicalNat.ofBytesModOrder_toVecLE_toNat, CompPoly.CanonicalNat.ofByteArrayModOrder_toByteArrayLE_toNat, CompPoly.ByteCodec.ofBytesModOrder_toBytes, CompPoly.instByteCodecZMod, CompPoly.ByteCodec.width_zmod, CompPoly.ByteCodec.toBytes_zmod, CompPoly.ByteCodec.ofBytes?_zmod, CompPoly.CanonicalNat.deserialize_serialize, CompPoly.CanonicalNat.deserialize_serialize_byteArray, CompPoly.deserialize_serialize_zmod
statement: formalized
proof: formalized
---

# Byte codecs from canonical naturals

`CompPoly.Data.Bytes.CanonicalNat`, in [CompPoly/Data/Bytes/CanonicalNat.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean), by Derek Sorensen.

> A type with a `CanonicalNat` structure has a fixed-width byte codec: the little-endian bytes
> of `toNat`, `bytesFor bound` of them, decoded by `ofNat?`. This is `ByteCodec.ofCanonicalNat`,
> a definition rather than an instance so that a composite type may choose a different codec
> (an extension field concatenates its coefficients) while still having a canonical natural.
>
> The same structure gives the total decoder used for challenges: `ofBytesModOrder` reads any
> number of bytes as an integer and reduces it modulo `bound`. Reading back an exact-width
> encoding this way recovers the element (`ofBytesModOrder_toBytes`); reading more bytes than
> the width is what makes the result close to uniform.
>
> `ZMod p` receives both: `instCanonicalNatZMod` from `CompPoly.Data.Classes.CanonicalNat` and the
> derived `ByteCodec (ZMod p)` here, so every spec prime field in `CompPoly.Fields` serializes.

`CompPoly.ByteCodec.ofCanonicalNat` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L42))

> The fixed-width byte codec of a type with canonical naturals: `bytesFor bound` little-endian
> bytes of `toNat`, decoded by `ofNat?`.

```lean
def ByteCodec.ofCanonicalNat (F : Type u) [CanonicalNat F] : ByteCodec F
```

`CompPoly.CanonicalNat.ofBytesModOrder` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L57))

> Read any byte string as a little-endian integer and reduce it modulo `bound`. Total, and
> close to uniform when the string is longer than `bytesFor bound`.

```lean
def ofBytesModOrder {n : ℕ} (v : Vector UInt8 n) : F
```

`CompPoly.CanonicalNat.ofByteArrayModOrder` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L60))

> `ofBytesModOrder` on a `ByteArray` of any size.

```lean
def ofByteArrayModOrder (b : ByteArray) : F
```

`CompPoly.CanonicalNat.deserialize_vector_eq` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L66))

```lean
theorem deserialize_vector_eq {n : ℕ} (v : Vector UInt8 n) :
    (Deserialize.deserialize v : F) = ofBytesModOrder v
```

`CompPoly.CanonicalNat.deserialize_byteArray_eq` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L69))

```lean
theorem deserialize_byteArray_eq (b : ByteArray) :
    (Deserialize.deserialize b : F) = ofByteArrayModOrder b
```

`CompPoly.CanonicalNat.ofBytesModOrder_toVecLE_toNat` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L73))

> Reading back an exact-width little-endian encoding modulo the order recovers the element.

```lean
theorem ofBytesModOrder_toVecLE_toNat (x : F) :
    ofBytesModOrder (toVecLE (bytesFor (bound F)) (toNat x)) = x
```

`CompPoly.CanonicalNat.ofByteArrayModOrder_toByteArrayLE_toNat` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L79))

```lean
theorem ofByteArrayModOrder_toByteArrayLE_toNat (x : F) :
    ofByteArrayModOrder (toByteArrayLE (bytesFor (bound F)) (toNat x)) = x
```

`CompPoly.ByteCodec.ofBytesModOrder_toBytes` (theorem, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L88))

> Reading back the `ofCanonicalNat` encoding modulo the order recovers the element.

```lean
theorem ByteCodec.ofBytesModOrder_toBytes [CanonicalNat F] (x : F) :
    CanonicalNat.ofBytesModOrder ((ByteCodec.ofCanonicalNat F).toBytes x) = x
```

> ## `ZMod`

`CompPoly.instByteCodecZMod` (instance, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L95))

> The little-endian residue codec of `ZMod p`, `bytesFor p` bytes wide.

```lean
instance instByteCodecZMod (p : ℕ) [NeZero p] : ByteCodec (ZMod p)
```

`CompPoly.ByteCodec.width_zmod` (theorem, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L97))

```lean
theorem ByteCodec.width_zmod (p : ℕ) [NeZero p] : ByteCodec.width (ZMod p) = bytesFor p
```

`CompPoly.ByteCodec.toBytes_zmod` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L100))

```lean
theorem ByteCodec.toBytes_zmod {p : ℕ} [NeZero p] (x : ZMod p) :
    ByteCodec.toBytes x = toVecLE (bytesFor p) x.val
```

`CompPoly.ByteCodec.ofBytes?_zmod` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L103))

```lean
theorem ByteCodec.ofBytes?_zmod {p : ℕ} [NeZero p] (v : Vector UInt8 (bytesFor p)) :
    ByteCodec.ofBytes? v = (CanonicalNat.ofNat? (ofVecLE v) : Option (ZMod p))
```

> ## Round trips through the class interfaces
>
> For a type whose codec is `ByteCodec.ofCanonicalNat`, the total decoder inverts the serializer
> at the codec's width. Together with `ByteCodec.deserialize_serialize` (the partial decoder) and
> the `Serialize.IsInjective` instances, this is the full round-trip story a protocol relies on.

`CompPoly.CanonicalNat.deserialize_serialize` (theorem, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L119))

> The total decoder inverts the serializer at the codec's own width, whenever the codec is
> the one derived from canonical naturals.

```lean
theorem CanonicalNat.deserialize_serialize {F : Type u} [CanonicalNat F] [inst : ByteCodec F]
    (h : inst = ByteCodec.ofCanonicalNat F) (x : F) :
    (Deserialize.deserialize (serialize x : Vector UInt8 (ByteCodec.width F)) : F) = x
```

`CompPoly.CanonicalNat.deserialize_serialize_byteArray` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L125))

```lean
theorem CanonicalNat.deserialize_serialize_byteArray {F : Type u} [CanonicalNat F]
    [inst : ByteCodec F] (h : inst = ByteCodec.ofCanonicalNat F) (x : F) :
    (Deserialize.deserialize (serialize x : ByteArray) : F) = x
```

`CompPoly.deserialize_serialize_zmod` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean#L132))

> `ZMod p`: the total decoder inverts the serializer.

```lean
theorem deserialize_serialize_zmod {p : ℕ} [NeZero p] (x : ZMod p) :
    (Deserialize.deserialize (serialize x : ByteArray) : ZMod p) = x
```

## Depends on

- [Fixed-width byte codecs](codec.md)
- [Little-endian byte encodings of naturals](littleendian.md)
- [Canonical naturals](../classes/canonicalnat.md)

## Sources

- [CompPoly/Data/Bytes/CanonicalNat.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/Bytes/CanonicalNat.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Bytes.CanonicalNat.json)
