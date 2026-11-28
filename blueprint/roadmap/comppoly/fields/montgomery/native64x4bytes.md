---
catalog: module
lean: Montgomery.Native64x4.FastField.toNat_eq_val_toField, Montgomery.Native64x4.FastField.toNat_ofField, Montgomery.Native64x4.FastField.ofField_cast_toNat, Montgomery.Native64x4.FastField.canonicalNat_bound, Montgomery.Native64x4.FastField.canonicalNat_toNat, Montgomery.Native64x4.FastField.canonicalNat_ofNat, Montgomery.Native64x4.FastField.byteCodec_width, Montgomery.Native64x4.FastField.toBytes_ofField, Montgomery.Native64x4.FastField.toBytes_eq_toBytes_toField
statement: formalized
proof: formalized
---

# Serialization of the four-limb Montgomery carrier

`CompPoly.Fields.Montgomery.Native64x4Bytes`, in [CompPoly/Fields/Montgomery/Native64x4Bytes.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean), by Derek Sorensen, Georgios Raikos.

> `Native64x4.FastField modulus` stores a Montgomery residue in four 64-bit limbs.  Its canonical
> natural is the value after one Montgomery reduction, `FastField.toNat`, so the bytes agree with
> the `ZMod modulus` codec (`toBytes_ofField`, `toNat_ofField`).  Decoding converts through
> `ofField`.

`Montgomery.Native64x4.FastField.toNat_eq_val_toField` (theorem, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L31))

> The canonical natural of a fast element is the residue of its canonical field value.

```lean
theorem toNat_eq_val_toField (x : FastField modulus) : toNat x = (toField x).val
```

`Montgomery.Native64x4.FastField.toNat_ofField` (theorem, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L35))

> Carrier agreement: the canonical natural of `ofField n` is the residue `n.val`.

```lean
theorem toNat_ofField (n : ZMod modulus) : toNat (ofField n) = n.val
```

`Montgomery.Native64x4.FastField.ofField_cast_toNat` (theorem, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L38))

```lean
theorem ofField_cast_toNat (x : FastField modulus) : ofField (toNat x : ZMod modulus) = x
```

`Montgomery.Native64x4.FastField.canonicalNat_bound` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L46))

```lean
theorem canonicalNat_bound : CanonicalNat.bound (FastField modulus) = modulus
```

`Montgomery.Native64x4.FastField.canonicalNat_toNat` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L48))

```lean
theorem canonicalNat_toNat (x : FastField modulus) : CanonicalNat.toNat x = toNat x
```

`Montgomery.Native64x4.FastField.canonicalNat_ofNat` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L50))

```lean
theorem canonicalNat_ofNat (n : ℕ) :
    CanonicalNat.ofNat (F := FastField modulus) n = ofField (n : ZMod modulus)
```

`Montgomery.Native64x4.FastField.byteCodec_width` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L53))

```lean
theorem byteCodec_width : ByteCodec.width (FastField modulus) = Bytes.bytesFor modulus
```

`Montgomery.Native64x4.FastField.toBytes_ofField` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L57))

> The fast carrier and `ZMod modulus` encode the same element identically.

```lean
theorem toBytes_ofField (n : ZMod modulus) :
    ByteCodec.toBytes (ofField n) = ByteCodec.toBytes n
```

`Montgomery.Native64x4.FastField.toBytes_eq_toBytes_toField` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean#L63))

> Encoding then converting to the spec field is encoding in the spec field.

```lean
theorem toBytes_eq_toBytes_toField (x : FastField modulus) :
    ByteCodec.toBytes x = ByteCodec.toBytes (toField x)
```

## Depends on

- [Byte codecs from canonical naturals](../../data/bytes/canonicalnat.md)
- [Fast four-limb Montgomery fields](native64x4field.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x4Bytes.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Bytes.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x4Bytes.json)
