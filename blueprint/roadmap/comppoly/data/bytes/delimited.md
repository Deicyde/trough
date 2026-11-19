---
catalog: module
lean: CompPoly.DelimitedCodec, CompPoly.DelimitedCodec.Total, CompPoly.DelimitedCodec.decode?_encode, CompPoly.DelimitedCodec.encode_inj, CompPoly.DelimitedCodec.encode_injective, CompPoly.DelimitedCodec.toByteArray, CompPoly.DelimitedCodec.ofByteArray?, CompPoly.DelimitedCodec.ofByteArray?_toByteArray, CompPoly.DelimitedCodec.toByteArray_inj, CompPoly.DelimitedCodec.serialize_eq, CompPoly.DelimitedCodec.deserialize_eq, CompPoly.DelimitedCodec.deserialize_serialize, CompPoly.DelimitedCodec.ofByteCodec, CompPoly.DelimitedCodec.valid_ofByteCodec, CompPoly.DelimitedCodec.encode_ofByteCodec, CompPoly.DelimitedCodec.toByteArray_ofByteCodec, CompPoly.DelimitedCodec.encodeU64, CompPoly.DelimitedCodec.decodeU64?, CompPoly.DelimitedCodec.length_encodeU64, CompPoly.DelimitedCodec.decodeU64?_encodeU64_append, CompPoly.DelimitedCodec.instNat, CompPoly.DelimitedCodec.valid_nat, CompPoly.DelimitedCodec.encode_nat, CompPoly.DelimitedCodec.encodeList, CompPoly.DelimitedCodec.encodeList_nil, CompPoly.DelimitedCodec.encodeList_cons, CompPoly.DelimitedCodec.decodeN?, CompPoly.DelimitedCodec.decodeN?_encodeList_append, CompPoly.DelimitedCodec.instList, CompPoly.DelimitedCodec.valid_list, CompPoly.DelimitedCodec.encode_list, CompPoly.DelimitedCodec.instProd, CompPoly.DelimitedCodec.valid_prod, CompPoly.DelimitedCodec.vectorOfList?, CompPoly.DelimitedCodec.vectorOfList?_toList, CompPoly.DelimitedCodec.vector
statement: formalized
proof: formalized
---

# Self-delimiting byte codecs

`CompPoly.Data.Bytes.Delimited`, in [CompPoly/Data/Bytes/Delimited.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean), by Derek Sorensen.

> A variable-length type such as a polynomial cannot have a `ByteCodec`, whose width is fixed.
> What it can have is a *self-delimiting* encoding: a decoder that reads exactly the bytes of one
> encoding from the front of a stream and returns the rest. `DelimitedCodec α` is that pair,
> with the one law `decode? (encode x ++ rest) = some (x, rest)`, stated for the `Valid x` the
> format can represent. Every fixed-width codec is a delimited codec with `Valid = True`
> (`DelimitedCodec.ofByteCodec`).
>
> Lengths, counts, and exponents are framed as `u64` little-endian words, the arkworks layout,
> so a natural is `Valid` when it is below `2 ^ 64` and a list when its length is and its
> entries are. `Serialize.IsInjective` is derived only for `Total` codecs, where everything is
> valid; for the others the injectivity theorem `encode_inj` carries the validity hypotheses.
> Composite codecs for lists, pairs, and fixed-length vectors are built here, and the polynomial
> codecs in `CompPoly.Univariate.Bytes`, `CompPoly.Multivariate.Bytes`, and
> `CompPoly.Bivariate.Bytes` are assembled from them.

`CompPoly.DelimitedCodec` (class, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L38))

> A self-delimiting byte encoding of `α`: `decode?` reads one encoding off the front of a
> stream and returns the remainder. `Valid` marks the elements the format represents.

```lean
class DelimitedCodec (α : Type u) where
  /-- Encode an element. -/
  encode : α → List UInt8
  /-- Read one encoding from the front of a stream, returning the element and the rest. -/
  decode? : List UInt8 → Option (α × List UInt8)
  /-- The elements the format can represent. -/
  Valid : α → Prop
  decode?_encode_append (x : α) (rest : List UInt8) (h : Valid x) :
    decode? (encode x ++ rest) = some (x, rest)
```

`CompPoly.DelimitedCodec.Total` (class, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L53))

> A codec every element of whose type is valid.

```lean
class Total (α : Type u) [DelimitedCodec α] : Prop where
  valid (x : α) : Valid x
```

`CompPoly.DelimitedCodec.decode?_encode` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L56))

```lean
theorem decode?_encode {x : α} (h : Valid x) : decode? (encode x) = some (x, [])
```

`CompPoly.DelimitedCodec.encode_inj` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L59))

```lean
theorem encode_inj {x y : α} (hx : Valid x) (hy : Valid y) (h : encode x = encode y) : x = y
```

`CompPoly.DelimitedCodec.encode_injective` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L64))

```lean
theorem encode_injective [Total α] : Function.Injective (encode : α → List UInt8)
```

`CompPoly.DelimitedCodec.toByteArray` (definition, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L68))

> The encoding as a `ByteArray`.

```lean
def toByteArray (x : α) : ByteArray
```

`CompPoly.DelimitedCodec.ofByteArray?` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L71))

> Decode a `ByteArray` holding exactly one encoding.

```lean
def ofByteArray? (b : ByteArray) : Option α
```

`CompPoly.DelimitedCodec.ofByteArray?_toByteArray` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L76))

```lean
theorem ofByteArray?_toByteArray {x : α} (h : Valid x) : ofByteArray? (toByteArray x) = some x
```

`CompPoly.DelimitedCodec.toByteArray_inj` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L79))

```lean
theorem toByteArray_inj {x y : α} (hx : Valid x) (hy : Valid y)
    (h : toByteArray x = toByteArray y) : x = y
```

> The protocol-facing instances are low priority so that a type with a `ByteCodec` keeps the
> fixed-width instances of `CompPoly.Data.Bytes.Codec`; the two agree byte for byte
> (`toByteArray_ofByteCodec`), but only one should be the canonical instance.

`CompPoly.DelimitedCodec.serialize_eq` (theorem, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L98))

```lean
theorem serialize_eq (x : α) : (serialize x : ByteArray) = toByteArray x
```

`CompPoly.DelimitedCodec.deserialize_eq` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L100))

```lean
theorem deserialize_eq (b : ByteArray) :
    (DeserializeOption.deserialize b : Option α) = ofByteArray? b
```

`CompPoly.DelimitedCodec.deserialize_serialize` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L103))

```lean
theorem deserialize_serialize {x : α} (h : Valid x) :
    (DeserializeOption.deserialize (serialize x : ByteArray) : Option α) = some x
```

> ## Fixed-width codecs are delimited

`CompPoly.DelimitedCodec.ofByteCodec` (instance, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L110))

> A fixed-width codec read as a delimited one: `width` bytes, every element valid.

```lean
instance (priority := low) ofByteCodec {β : Type v} [ByteCodec β] : DelimitedCodec β
```

`CompPoly.DelimitedCodec.valid_ofByteCodec` (theorem, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L121))

```lean
theorem valid_ofByteCodec {β : Type v} [ByteCodec β] (x : β) : Valid x ↔ True
```

`CompPoly.DelimitedCodec.encode_ofByteCodec` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L123))

```lean
theorem encode_ofByteCodec {β : Type v} [ByteCodec β] (x : β) :
    encode x = (ByteCodec.toBytes x).toList
```

`CompPoly.DelimitedCodec.toByteArray_ofByteCodec` (theorem, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L127))

> Read as a delimited codec, a fixed-width codec produces the same bytes.

```lean
theorem toByteArray_ofByteCodec {β : Type v} [ByteCodec β] (x : β) :
    DelimitedCodec.toByteArray x = ByteCodec.toByteArray x
```

> ## `u64` framing

`CompPoly.DelimitedCodec.encodeU64` (definition, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L133))

> The `u64` little-endian framing of a natural: lengths, counts, exponents.

```lean
def encodeU64 (n : ℕ) : List UInt8
```

`CompPoly.DelimitedCodec.decodeU64?` (definition, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L136))

> Read a `u64` little-endian word from the front of a stream.

```lean
def decodeU64? (l : List UInt8) : Option (ℕ × List UInt8)
```

`CompPoly.DelimitedCodec.length_encodeU64` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L139))

```lean
theorem length_encodeU64 (n : ℕ) : (encodeU64 n).length = 8
```

`CompPoly.DelimitedCodec.decodeU64?_encodeU64_append` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L141))

```lean
theorem decodeU64?_encodeU64_append {n : ℕ} (h : n < 2 ^ 64) (rest : List UInt8) :
    decodeU64? (encodeU64 n ++ rest) = some (n, rest)
```

`CompPoly.DelimitedCodec.instNat` (instance, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L152))

> Naturals framed as `u64` words; valid below `2 ^ 64`.

```lean
instance instNat : DelimitedCodec ℕ
```

`CompPoly.DelimitedCodec.valid_nat` (theorem, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L158))

```lean
theorem valid_nat (n : ℕ) : Valid n ↔ n < 2 ^ 64
```

`CompPoly.DelimitedCodec.encode_nat` (theorem, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L160))

```lean
theorem encode_nat (n : ℕ) : encode n = encodeU64 n
```

> ## Sequences

`CompPoly.DelimitedCodec.encodeList` (definition, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L165))

> The concatenated encodings of a list, with no framing.

```lean
def encodeList (l : List α) : List UInt8
```

`CompPoly.DelimitedCodec.encodeList_nil` (theorem, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L167))

```lean
theorem encodeList_nil : encodeList ([] : List α) = []
```

`CompPoly.DelimitedCodec.encodeList_cons` (theorem, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L169))

```lean
theorem encodeList_cons (x : α) (l : List α) :
    encodeList (x :: l) = encode x ++ encodeList l
```

`CompPoly.DelimitedCodec.decodeN?` (definition, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L173))

> Read `m` consecutive encodings from the front of a stream.

```lean
def decodeN? : ℕ → List UInt8 → Option (List α × List UInt8)
```

`CompPoly.DelimitedCodec.decodeN?_encodeList_append` (theorem, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L178))

```lean
theorem decodeN?_encodeList_append {l : List α} (hv : ∀ x ∈ l, Valid x) (rest : List UInt8) :
    decodeN? l.length (encodeList l ++ rest) = some (l, rest)
```

`CompPoly.DelimitedCodec.instList` (instance, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L189))

> Lists: a `u64` count, then the encodings. Valid when the count fits and the entries are
> valid.

```lean
instance instList : DelimitedCodec (List α)
```

`CompPoly.DelimitedCodec.valid_list` (theorem, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L197))

```lean
theorem valid_list (l : List α) : Valid l ↔ l.length < 2 ^ 64 ∧ ∀ x ∈ l, Valid x
```

`CompPoly.DelimitedCodec.encode_list` (theorem, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L199))

```lean
theorem encode_list (l : List α) : encode l = encodeU64 l.length ++ encodeList l
```

`CompPoly.DelimitedCodec.instProd` (instance, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L202))

> Pairs: the first encoding, then the second.

```lean
instance instProd {β : Type v} [DelimitedCodec β] : DelimitedCodec (α × β)
```

`CompPoly.DelimitedCodec.valid_prod` (theorem, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L211))

```lean
theorem valid_prod {β : Type v} [DelimitedCodec β] (p : α × β) : Valid p ↔ Valid p.1 ∧ Valid p.2
```

`CompPoly.DelimitedCodec.vectorOfList?` (definition, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L215))

> A list of exactly `n` entries as a vector.

```lean
def vectorOfList? {γ : Type v} (n : ℕ) (xs : List γ) : Option (Vector γ n)
```

`CompPoly.DelimitedCodec.vectorOfList?_toList` (theorem, [line 219](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L219))

```lean
theorem vectorOfList?_toList {γ : Type v} {n : ℕ} (v : Vector γ n) :
    vectorOfList? n v.toList = some v
```

`CompPoly.DelimitedCodec.vector` (definition, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean#L230))

> Fixed-length vectors of delimited elements: the `n` encodings with no count. Not an
> instance, since a vector of fixed-width elements already has a codec through
> `ByteCodec.instVector`; use it for element types without a `ByteCodec`.

```lean
def vector (n : ℕ) : DelimitedCodec (Vector α n)
```

## Depends on

- [Fixed-width byte codecs](codec.md)
- [Little-endian byte encodings of naturals](littleendian.md)

## Proof depends on

- [Byte codecs of vectors](vector.md)

## Sources

- [CompPoly/Data/Bytes/Delimited.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Delimited.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Bytes.Delimited.json)
