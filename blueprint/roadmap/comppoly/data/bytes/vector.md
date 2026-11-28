---
catalog: module
lean: CompPoly.ByteCodec.ofBytesList?, CompPoly.ByteCodec.ofBytesList?_toList, CompPoly.ByteCodec.encodeList, CompPoly.ByteCodec.encodeList_nil, CompPoly.ByteCodec.encodeList_cons, CompPoly.ByteCodec.length_encodeList, CompPoly.ByteCodec.decodeList, CompPoly.ByteCodec.decodeList_encodeList_of_length, CompPoly.ByteCodec.decodeList_encodeList, CompPoly.ByteCodec.instVector, CompPoly.ByteCodec.width_vector, CompPoly.ByteCodec.toList_toBytes_vector, CompPoly.Vector.ofBytesEach
statement: formalized
proof: formalized
---

# Byte codecs of vectors

`CompPoly.Data.Bytes.Vector`, in [CompPoly/Data/Bytes/Vector.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean), by Derek Sorensen.

> A `Vector F n` encodes as the concatenation of the encodings of its entries, `n * width F`
> bytes, and decodes entry by entry. This is the codec of every fixed-length composite: an
> extension field element is its coefficient vector, a multilinear polynomial its evaluation
> vector, a degree-bounded univariate polynomial its padded coefficient vector. It matches how
> arkworks and plonky3 serialize extension fields and coefficient lists.
>
> `Deserialize (Vector F n) (Vector UInt8 (n * k))` likewise decodes total, entry by entry, from
> any per-entry total decoder, which is how a vector of challenges is read from a byte sponge.

`CompPoly.ByteCodec.ofBytesList?` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L35))

> Decode a list of exactly `width F` bytes.

```lean
def ofBytesList? (l : List UInt8) : Option F
```

`CompPoly.ByteCodec.ofBytesList?_toList` (theorem, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L40))

```lean
theorem ofBytesList?_toList (x : F) : ofBytesList? (toBytes x).toList = some x
```

`CompPoly.ByteCodec.encodeList` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L47))

> The concatenated encodings of a list.

```lean
def encodeList (l : List F) : List UInt8
```

`CompPoly.ByteCodec.encodeList_nil` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L49))

```lean
theorem encodeList_nil : encodeList ([] : List F) = []
```

`CompPoly.ByteCodec.encodeList_cons` (theorem, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L51))

```lean
theorem encodeList_cons (x : F) (l : List F) :
    encodeList (x :: l) = (toBytes x).toList ++ encodeList l
```

`CompPoly.ByteCodec.length_encodeList` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L55))

```lean
theorem length_encodeList (l : List F) : (encodeList l).length = l.length * width F
```

`CompPoly.ByteCodec.decodeList` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L63))

> Decode `m` consecutive encodings, failing on leftover bytes.

```lean
def decodeList : ℕ → List UInt8 → Option (List F)
```

`CompPoly.ByteCodec.decodeList_encodeList_of_length` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L71))

```lean
theorem decodeList_encodeList_of_length {m : ℕ} {l : List F} (h : l.length = m) :
    decodeList m (encodeList l) = some l
```

`CompPoly.ByteCodec.decodeList_encodeList` (theorem, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L85))

```lean
theorem decodeList_encodeList (l : List F) : decodeList l.length (encodeList l) = some l
```

`CompPoly.ByteCodec.instVector` (instance, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L89))

> The concatenation codec of `Vector F n`: `n * width F` bytes.

```lean
instance instVector (n : ℕ) : ByteCodec (Vector F n)
```

`CompPoly.ByteCodec.width_vector` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L103))

```lean
theorem width_vector (n : ℕ) : width (Vector F n) = n * width F
```

`CompPoly.ByteCodec.toList_toBytes_vector` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L105))

```lean
theorem toList_toBytes_vector {n : ℕ} (v : Vector F n) :
    (toBytes v).toList = encodeList v.toList
```

`CompPoly.Vector.ofBytesEach` (definition, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean#L111))

> Total entry-by-entry decoding of a vector from `n * k` bytes.

```lean
def Vector.ofBytesEach {F : Type u} {k : ℕ} [Deserialize F (Vector UInt8 k)] (n : ℕ)
    (b : Vector UInt8 (n * k)) : Vector F n
```

## Depends on

- [Fixed-width byte codecs](codec.md)

## Sources

- [CompPoly/Data/Bytes/Vector.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Bytes/Vector.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Bytes.Vector.json)
