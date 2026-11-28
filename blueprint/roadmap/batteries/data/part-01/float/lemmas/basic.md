---
catalog: module
lean: Float.Model.UnpackedFloat.isNaNBits, Float.Model.UnpackedFloat.Sign.ofBitVec_toBitVec, Float.Model.UnpackedFloat.Sign.toBitVec_ofBitVec, Float.Model.UnpackedFloat.Sign.forall_iff, Float.Model.UnpackedFloat.unpackSign_packComponents, Float.Model.UnpackedFloat.packComponents_unpackSign_unpackExponent_unpackMantissa, Float.Model.UnpackedFloat.pack_unpack, Float.Model.UnpackedFloat.pack_unpack_of_valid, Float.Model.UnpackedFloat.unpack_inj_of_valid, Float.Model.UnpackedFloat.isNaNBits_packedNaN, Float.Model.UnpackedFloat.unpack_packedNaN, Float.Model.UnpackedFloat.unpack_packedZero, Float.Model.UnpackedFloat.isNaN_iff, Float.Model.UnpackedFloat.unpack_eq_notANumber_iff_of_valid, Float.Model.UnpackedFloat.unpack_eq_zero_iff_of_valid, Float.Model.UnpackedFloat.isNaN_unpack_iff_of_valid, Float.Model.UnpackedFloat.beq_iff_ne_notANumber_and_eq, Float.Model.UnpackedFloat.unpack_beq_unpack_iff, Float.Model.UnpackedFloat.unpack_eq_notANumber_of_isNaNBits, Float.Model.UnpackedFloat.unpack_pack_unpack, Float.toBits_inj, Float32.toBits_inj, Float.ofBits_toBits, Float32.ofBits_toBits, Float.isNaN_eq_decide_eq_nan, Float32.isNaN_eq_decide_eq_nan, Float.beq_iff_ne_nan_and_eq, Float32.beq_iff_ne_nan_and_eq, Float.nan_beq_eq_false, Float32.nan_beq_eq_false, Float.beq_nan_eq_false, Float32.beq_nan_eq_false, Float.beq_self_iff, Float32.beq_self_iff, Float.beq_self_eq_false_iff, Float32.beq_self_eq_false_iff, Float.bne_eq, Float32.bne_eq
statement: formalized
proof: formalized
---

# Lemmas/Basic

`Batteries.Data.Float.Lemmas.Basic`, in [Batteries/Data/Float/Lemmas/Basic.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean), by Robin Arnez.

`Float.Model.UnpackedFloat.isNaNBits` (definition, [line 13](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L13))

> Returns true if the bits represent an NaN value

```lean
def isNaNBits {spec : Format} (b : BitVec spec.numBits) : Bool
```

`Float.Model.UnpackedFloat.Sign.ofBitVec_toBitVec` (theorem, [line 19](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L19))

```lean
theorem ofBitVec_toBitVec (s : Sign) :
    Sign.ofBitVec s.toBitVec = s
```

`Float.Model.UnpackedFloat.Sign.toBitVec_ofBitVec` (theorem, [line 24](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L24))

```lean
theorem toBitVec_ofBitVec (b : BitVec 1) :
    (Sign.ofBitVec b).toBitVec = b
```

`Float.Model.UnpackedFloat.Sign.forall_iff` (theorem, [line 28](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L28))

```lean
protected theorem forall_iff {p : Sign → Prop} :
    (∀ s : Sign, p s) ↔ p .positive ∧ p .negative
```

`Float.Model.UnpackedFloat.unpackSign_packComponents` (theorem, [line 40](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L40))

```lean
theorem unpackSign_packComponents {spec : Format} (s e m) :
    unpackSign (packComponents spec s e m) = s.toBitVec
```

`Float.Model.UnpackedFloat.packComponents_unpackSign_unpackExponent_unpackMantissa` (theorem, [line 45](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L45))

```lean
theorem packComponents_unpackSign_unpackExponent_unpackMantissa
    {spec : Format} (b : BitVec spec.numBits) :
    packComponents spec
      (Sign.ofBitVec (unpackSign b)) (unpackExponent b) (unpackMantissa b) = b
```

`Float.Model.UnpackedFloat.pack_unpack` (theorem, [line 57](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L57))

```lean
theorem pack_unpack {spec : Format} (b : BitVec spec.numBits) :
    (unpack spec b).pack spec = if isNaNBits b then packedNaN spec else b
```

`Float.Model.UnpackedFloat.pack_unpack_of_valid` (theorem, [line 113](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L113))

```lean
theorem pack_unpack_of_valid {spec : Format} {b : BitVec spec.numBits}
    (hvalid : spec.Valid b) : (unpack spec b).pack spec = b
```

`Float.Model.UnpackedFloat.unpack_inj_of_valid` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L118))

```lean
theorem unpack_inj_of_valid {spec : Format} {b b' : BitVec spec.numBits}
    (hb : spec.Valid b) (hb' : spec.Valid b') :
    unpack spec b = unpack spec b' ↔ b = b'
```

`Float.Model.UnpackedFloat.isNaNBits_packedNaN` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L127))

```lean
theorem isNaNBits_packedNaN {spec : Format} : isNaNBits (packedNaN spec)
```

`Float.Model.UnpackedFloat.unpack_packedNaN` (theorem, [line 135](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L135))

```lean
theorem unpack_packedNaN {spec : Format} : unpack spec (packedNaN spec) = notANumber
```

`Float.Model.UnpackedFloat.unpack_packedZero` (theorem, [line 141](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L141))

```lean
theorem unpack_packedZero {spec : Format} {sign : Sign} :
    unpack spec (packedZero spec sign) = .zero sign
```

`Float.Model.UnpackedFloat.isNaN_iff` (theorem, [line 146](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L146))

```lean
theorem isNaN_iff : isNaN x ↔ x = notANumber
```

`Float.Model.UnpackedFloat.unpack_eq_notANumber_iff_of_valid` (theorem, [line 149](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L149))

```lean
theorem unpack_eq_notANumber_iff_of_valid {spec : Format} {b : BitVec spec.numBits}
    (hvalid : spec.Valid b) : unpack spec b = notANumber ↔ b = packedNaN spec
```

`Float.Model.UnpackedFloat.unpack_eq_zero_iff_of_valid` (theorem, [line 153](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L153))

```lean
theorem unpack_eq_zero_iff_of_valid {spec : Format} {sign : Sign} {b : BitVec spec.numBits}
    (hvalid : spec.Valid b) : unpack spec b = zero sign ↔ b = packedZero spec sign
```

`Float.Model.UnpackedFloat.isNaN_unpack_iff_of_valid` (theorem, [line 157](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L157))

```lean
theorem isNaN_unpack_iff_of_valid {spec : Format} {b : BitVec spec.numBits}
    (hvalid : spec.Valid b) : (unpack spec b).isNaN ↔ b = packedNaN spec
```

`Float.Model.UnpackedFloat.beq_iff_ne_notANumber_and_eq` (theorem, [line 161](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L161))

```lean
theorem beq_iff_ne_notANumber_and_eq (a b : UnpackedFloat) :
    a.beq b ↔ a ≠ notANumber ∧ b ≠ notANumber ∧
      (a = b ∨ (a = .zero .positive ∧ b = .zero .negative) ∨
        (a = .zero .negative ∧ b = .zero .positive))
```

`Float.Model.UnpackedFloat.unpack_beq_unpack_iff` (theorem, [line 169](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L169))

```lean
theorem unpack_beq_unpack_iff {spec : Format} {b b' : BitVec spec.numBits}
    (hb : spec.Valid b) (hb' : spec.Valid b') :
    (unpack spec b).beq (unpack spec b') ↔ b ≠ packedNaN spec ∧ b' ≠ packedNaN spec ∧
        (b = b' ∨ (b = packedZero spec .positive ∧ b' = packedZero spec .negative) ∨
          (b = packedZero spec .negative ∧ b' = packedZero spec .positive))
```

`Float.Model.UnpackedFloat.unpack_eq_notANumber_of_isNaNBits` (theorem, [line 177](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L177))

```lean
theorem unpack_eq_notANumber_of_isNaNBits {spec : Format} {b : BitVec spec.numBits}
    (h : isNaNBits b) : unpack spec b = notANumber
```

`Float.Model.UnpackedFloat.unpack_pack_unpack` (theorem, [line 183](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L183))

> Unpacking forgets everything that packing an unpacked float could change.

```lean
theorem unpack_pack_unpack {spec : Format} (b : BitVec spec.numBits) :
    unpack spec (pack spec (unpack spec b)) = unpack spec b
```

`Float.toBits_inj` (theorem, [line 193](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L193))

```lean
theorem Float.toBits_inj {f f' : Float} : f.toBits = f'.toBits ↔ f = f'
```

`Float32.toBits_inj` (theorem, [line 196](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L196))

```lean
theorem Float32.toBits_inj {f f' : Float32} : f.toBits = f'.toBits ↔ f = f'
```

`Float.ofBits_toBits` (theorem, [line 200](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L200))

```lean
theorem Float.ofBits_toBits (f : Float) : ofBits f.toBits = f
```

`Float32.ofBits_toBits` (theorem, [line 205](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L205))

```lean
theorem Float32.ofBits_toBits (f : Float32) : ofBits f.toBits = f
```

`Float.isNaN_eq_decide_eq_nan` (theorem, [line 210](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L210))

```lean
theorem Float.isNaN_eq_decide_eq_nan {f : Float} : isNaN f = decide (f = nan)
```

`Float32.isNaN_eq_decide_eq_nan` (theorem, [line 215](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L215))

```lean
theorem Float32.isNaN_eq_decide_eq_nan {f : Float32} : isNaN f = decide (f = nan)
```

`Float.beq_iff_ne_nan_and_eq` (theorem, [line 219](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L219))

```lean
theorem Float.beq_iff_ne_nan_and_eq {f f' : Float} :
    f == f' ↔ f ≠ nan ∧ f' ≠ nan ∧ (f = f' ∨ (f = 0 ∧ f' = -0) ∨ (f = -0 ∧ f' = 0))
```

`Float32.beq_iff_ne_nan_and_eq` (theorem, [line 224](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L224))

```lean
theorem Float32.beq_iff_ne_nan_and_eq {f f' : Float32} :
    f == f' ↔ f ≠ nan ∧ f' ≠ nan ∧ (f = f' ∨ (f = 0 ∧ f' = -0) ∨ (f = -0 ∧ f' = 0))
```

`Float.nan_beq_eq_false` (theorem, [line 230](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L230))

```lean
theorem Float.nan_beq_eq_false (f : Float) : (nan == f) = false
```

`Float32.nan_beq_eq_false` (theorem, [line 234](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L234))

```lean
theorem Float32.nan_beq_eq_false (f : Float32) : (nan == f) = false
```

`Float.beq_nan_eq_false` (theorem, [line 238](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L238))

```lean
theorem Float.beq_nan_eq_false (f : Float) : (f == nan) = false
```

`Float32.beq_nan_eq_false` (theorem, [line 242](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L242))

```lean
theorem Float32.beq_nan_eq_false (f : Float32) : (f == nan) = false
```

`Float.beq_self_iff` (theorem, [line 246](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L246))

```lean
theorem Float.beq_self_iff {f : Float} : f == f ↔ f ≠ nan
```

`Float32.beq_self_iff` (theorem, [line 250](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L250))

```lean
theorem Float32.beq_self_iff {f : Float32} : f == f ↔ f ≠ nan
```

`Float.beq_self_eq_false_iff` (theorem, [line 254](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L254))

```lean
theorem Float.beq_self_eq_false_iff {f : Float} : (f == f) = false ↔ f = nan
```

`Float32.beq_self_eq_false_iff` (theorem, [line 258](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L258))

```lean
theorem Float32.beq_self_eq_false_iff {f : Float32} : (f == f) = false ↔ f = nan
```

`Float.bne_eq` (theorem, [line 265](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L265))

> This theorem is true for all types but most other types have `LawfulBEq` where
> `bne_self_eq_false` or `bne_iff_ne` apply.

```lean
protected theorem Float.bne_eq {f : Float} : (f != f) = (!f == f)
```

`Float32.bne_eq` (theorem, [line 271](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean#L271))

> This theorem is true for all types but most other types have `LawfulBEq` where
> `bne_self_eq_false` or `bne_iff_ne` apply.

```lean
protected theorem Float32.bne_eq {f : Float32} : (f != f) = (!f == f)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Float/Lemmas/Basic.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Basic.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.Float.Lemmas.Basic.json)
