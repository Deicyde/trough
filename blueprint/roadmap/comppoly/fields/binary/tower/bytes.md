---
catalog: module
lean: ConcreteBinaryTower.ConcreteBTField.canonicalNat_bound, ConcreteBinaryTower.ConcreteBTField.canonicalNat_toNat, ConcreteBinaryTower.ConcreteBTField.byteCodec_width, ConcreteBinaryTower.ConcreteBTField.byteCodec_width_eq, ConcreteBinaryTower.ConcreteBTField.byteCodec_width_three, ConcreteBinaryTower.ConcreteBTField.byteCodec_width_seven, ConcreteBinaryTower.Fast.FastBT128.toBitVec, ConcreteBinaryTower.Fast.FastBT128.ofBitVec, ConcreteBinaryTower.Fast.FastBT128.toNat_lt, ConcreteBinaryTower.Fast.FastBT128.toNat_ofNat, ConcreteBinaryTower.Fast.FastBT128.ofNat_toNat, ConcreteBinaryTower.Fast.FastBT128.ofBitVec_toBitVec, ConcreteBinaryTower.Fast.FastBT128.toBitVec_ofBitVec, ConcreteBinaryTower.Fast.FastBT128.canonicalNat_bound, ConcreteBinaryTower.Fast.FastBT128.canonicalNat_toNat, ConcreteBinaryTower.Fast.FastBT128.byteCodec_width, ConcreteBinaryTower.Fast.FastBT128.toList_toBytes_toConcrete, ConcreteBinaryTower.Fast.FastBT128.toByteArray_toConcrete
statement: formalized
proof: formalized
---

# Serialization of the binary tower

`CompPoly.Fields.Binary.Tower.Bytes`, in [CompPoly/Fields/Binary/Tower/Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean), by Derek Sorensen.

> A level-`k` tower element `ConcreteBTField k` is its `2 ^ k` low-first tower-basis coordinates.
> Its canonical natural is that bit pattern read as an integer and its encoding the little-endian
> bytes of the pattern, `bytesFor (2 ^ 2 ^ k)` of them: one byte at level three, sixteen at level
> seven. `FastBT128`, the two-limb level-seven carrier, agrees with `ConcreteBTField 7` through
> `toConcrete` (`toList_toBytes_toConcrete`, `toByteArray_toConcrete`).
>
> These are tower-basis coordinates. `AesField` at eight bits and `ConcreteBF128Ghash` at 128 bits
> use different bases, and their encodings are not interchangeable with these.

`ConcreteBinaryTower.ConcreteBTField.canonicalNat_bound` (theorem, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L38))

```lean
theorem canonicalNat_bound (k : ℕ) :
    CanonicalNat.bound (ConcreteBTField k) = 2 ^ 2 ^ k
```

`ConcreteBinaryTower.ConcreteBTField.canonicalNat_toNat` (theorem, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L41))

```lean
theorem canonicalNat_toNat {k : ℕ} (x : ConcreteBTField k) :
    CanonicalNat.toNat x = x.toNat
```

`ConcreteBinaryTower.ConcreteBTField.byteCodec_width` (theorem, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L44))

```lean
theorem byteCodec_width (k : ℕ) :
    ByteCodec.width (ConcreteBTField k) = Bytes.bytesFor (2 ^ 2 ^ k)
```

`ConcreteBinaryTower.ConcreteBTField.byteCodec_width_eq` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L49))

> A level-`k` element takes `⌈2 ^ k / 8⌉` bytes: one byte at level three, sixteen at
> level seven.

```lean
theorem byteCodec_width_eq (k : ℕ) :
    ByteCodec.width (ConcreteBTField k) = (2 ^ k + 7) / 8
```

`ConcreteBinaryTower.ConcreteBTField.byteCodec_width_three` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L53))

```lean
theorem byteCodec_width_three : ByteCodec.width (ConcreteBTField 3) = 1
```

`ConcreteBinaryTower.ConcreteBTField.byteCodec_width_seven` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L57))

```lean
theorem byteCodec_width_seven : ByteCodec.width (ConcreteBTField 7) = 16
```

`ConcreteBinaryTower.Fast.FastBT128.toBitVec` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L67))

> The two limbs read as a `2 ^ 7`-bit word, `lo` first. The width is written `2 ^ 7` so that
> the carrier's codec has the same width term as `ConcreteBTField 7`.

```lean
def toBitVec (v : FastBT128) : BitVec (2 ^ 7)
```

`ConcreteBinaryTower.Fast.FastBT128.ofBitVec` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L70))

> Split a `2 ^ 7`-bit word into two limbs.

```lean
def ofBitVec (b : BitVec (2 ^ 7)) : FastBT128
```

`ConcreteBinaryTower.Fast.FastBT128.toNat_lt` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L72))

```lean
theorem toNat_lt (v : FastBT128) : v.toNat < 2 ^ 2 ^ 7
```

`ConcreteBinaryTower.Fast.FastBT128.toNat_ofNat` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L78))

```lean
theorem toNat_ofNat (n : ℕ) : (ofNat n).toNat = n % 2 ^ 2 ^ 7
```

`ConcreteBinaryTower.Fast.FastBT128.ofNat_toNat` (theorem, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L82))

```lean
theorem ofNat_toNat (v : FastBT128) : ofNat v.toNat = v
```

`ConcreteBinaryTower.Fast.FastBT128.ofBitVec_toBitVec` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L93))

```lean
theorem ofBitVec_toBitVec (v : FastBT128) : ofBitVec (toBitVec v) = v
```

`ConcreteBinaryTower.Fast.FastBT128.toBitVec_ofBitVec` (theorem, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L96))

```lean
theorem toBitVec_ofBitVec (b : BitVec (2 ^ 7)) : toBitVec (ofBitVec b) = b
```

`ConcreteBinaryTower.Fast.FastBT128.canonicalNat_bound` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L105))

```lean
theorem canonicalNat_bound : CanonicalNat.bound FastBT128 = 2 ^ 2 ^ 7
```

`ConcreteBinaryTower.Fast.FastBT128.canonicalNat_toNat` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L107))

```lean
theorem canonicalNat_toNat (v : FastBT128) : CanonicalNat.toNat v = v.toNat
```

`ConcreteBinaryTower.Fast.FastBT128.byteCodec_width` (theorem, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L111))

```lean
theorem byteCodec_width : ByteCodec.width FastBT128 = 16
```

`ConcreteBinaryTower.Fast.FastBT128.toList_toBytes_toConcrete` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L122))

> The fast carrier and the level-seven tower field encode the same element identically.
>
> Stated on the byte lists: the two codecs' widths are both `bytesFor (2 ^ 2 ^ 7)`, but through
> different instance paths, and a `Vector`-typed statement would ask the kernel to identify them
> by evaluation, which sends it into `Nat.log2`'s well-founded recursion. Rewriting each width to
> `16` through its own width lemma avoids that.

```lean
theorem toList_toBytes_toConcrete (v : FastBT128) :
    (ByteCodec.toBytes (toConcrete v)).toList = (ByteCodec.toBytes v).toList
```

`ConcreteBinaryTower.Fast.FastBT128.toByteArray_toConcrete` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean#L133))

> The same agreement as a `ByteArray` equality, the form a transcript sees.

```lean
theorem toByteArray_toConcrete (v : FastBT128) :
    ByteCodec.toByteArray (toConcrete v) = ByteCodec.toByteArray v
```

## Depends on

- [Fixed-width byte codecs](../../../data/bytes/codec.md)
- [Little-endian byte encodings of naturals](../../../data/bytes/littleendian.md)
- [Canonical naturals](../../../data/classes/canonicalnat.md)
- [Fast Binary Tower Arithmetic](fast.md)

## Proof depends on

- [Byte codecs from canonical naturals](../../../data/bytes/canonicalnat.md)

## Sources

- [CompPoly/Fields/Binary/Tower/Bytes.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/Tower/Bytes.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.Bytes.json)
