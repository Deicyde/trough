---
catalog: module
lean: Montgomery.Native32.FastField.toNat_eq_val_toField, Montgomery.Native32.FastField.toNat_ofField, Montgomery.Native32.FastField.ofField_cast_toNat, Montgomery.Native32.FastField.canonicalNat_bound, Montgomery.Native32.FastField.canonicalNat_toNat, Montgomery.Native32.FastField.canonicalNat_ofNat, Montgomery.Native32.FastField.byteCodec_width, Montgomery.Native32.FastField.toBytes_ofField, Montgomery.Native32.FastField.toBytes_eq_toBytes_toField
statement: formalized
proof: formalized
---

# Serialization of the 32-bit Montgomery carrier

`CompPoly.Fields.Montgomery.Native32Bytes`, in [CompPoly/Fields/Montgomery/Native32Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean), by Derek Sorensen.

> `Native32.FastField modulus` stores a Montgomery residue. Its canonical natural is the value
> after one Montgomery reduction, `FastField.toNat`, so the bytes are those of the abstract field
> element and agree with the `ZMod modulus` codec: `toBytes_ofField` and `toNat_ofField` are the
> agreement laws. Decoding converts through `ofField`.

`Montgomery.Native32.FastField.toNat_eq_val_toField` (theorem, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L31))

> The canonical natural of a fast element is the residue of its canonical field value.

```lean
theorem toNat_eq_val_toField (x : FastField modulus) : toNat x = (toField x).val
```

`Montgomery.Native32.FastField.toNat_ofField` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L35))

> Carrier agreement: the canonical natural of `ofField n` is the residue `n.val`.

```lean
theorem toNat_ofField (n : ZMod modulus) : toNat (ofField n) = n.val
```

`Montgomery.Native32.FastField.ofField_cast_toNat` (theorem, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L38))

```lean
theorem ofField_cast_toNat (x : FastField modulus) : ofField (toNat x : ZMod modulus) = x
```

`Montgomery.Native32.FastField.canonicalNat_bound` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L47))

```lean
theorem canonicalNat_bound : CanonicalNat.bound (FastField modulus) = modulus
```

`Montgomery.Native32.FastField.canonicalNat_toNat` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L49))

```lean
theorem canonicalNat_toNat (x : FastField modulus) : CanonicalNat.toNat x = toNat x
```

`Montgomery.Native32.FastField.canonicalNat_ofNat` (theorem, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L51))

```lean
theorem canonicalNat_ofNat (n : ℕ) :
    CanonicalNat.ofNat (F := FastField modulus) n = ofField (n : ZMod modulus)
```

`Montgomery.Native32.FastField.byteCodec_width` (theorem, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L54))

```lean
theorem byteCodec_width : ByteCodec.width (FastField modulus) = Bytes.bytesFor modulus
```

`Montgomery.Native32.FastField.toBytes_ofField` (theorem, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L58))

> The fast carrier and `ZMod modulus` encode the same element identically.

```lean
theorem toBytes_ofField (n : ZMod modulus) :
    ByteCodec.toBytes (ofField n) = ByteCodec.toBytes n
```

`Montgomery.Native32.FastField.toBytes_eq_toBytes_toField` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean#L64))

> Encoding then converting to the spec field is encoding in the spec field.

```lean
theorem toBytes_eq_toBytes_toField (x : FastField modulus) :
    ByteCodec.toBytes x = ByteCodec.toBytes (toField x)
```

## Depends on

- [Byte codecs from canonical naturals](../../data/bytes/canonicalnat.md)
- [Fast 32-bit Montgomery Fields](native32field.md)

## Sources

- [CompPoly/Fields/Montgomery/Native32Bytes.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Montgomery/Native32Bytes.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native32Bytes.json)
