---
catalog: module
lean: Float.Model.UnpackedFloat.isNaNBits, Float.Model.UnpackedFloat.Sign.ofBitVec_toBitVec, Float.Model.UnpackedFloat.Sign.toBitVec_ofBitVec, Float.Model.UnpackedFloat.Sign.forall_iff, Float.Model.UnpackedFloat.unpackSign_packComponents, Float.Model.UnpackedFloat.packComponents_unpackSign_unpackExponent_unpackMantissa, Float.Model.UnpackedFloat.pack_unpack, Float.Model.UnpackedFloat.pack_unpack_of_valid, Float.Model.UnpackedFloat.unpack_inj_of_valid, Float.Model.UnpackedFloat.isNaNBits_packedNaN, Float.Model.UnpackedFloat.unpack_packedNaN, Float.Model.UnpackedFloat.unpack_packedZero, Float.Model.UnpackedFloat.isNaN_iff, Float.Model.UnpackedFloat.unpack_eq_notANumber_iff_of_valid, Float.Model.UnpackedFloat.unpack_eq_zero_iff_of_valid, Float.Model.UnpackedFloat.isNaN_unpack_iff_of_valid, Float.Model.UnpackedFloat.beq_iff_ne_notANumber_and_eq, Float.Model.UnpackedFloat.unpack_beq_unpack_iff, Float.toBits_inj, Float32.toBits_inj, Float.ofBits_toBits, Float32.ofBits_toBits, Float.isNaN_eq_decide_eq_nan, Float32.isNaN_eq_decide_eq_nan, Float.beq_iff_ne_nan_and_eq, Float32.beq_iff_ne_nan_and_eq, Float.nan_beq_eq_false, Float32.nan_beq_eq_false, Float.beq_nan_eq_false, Float32.beq_nan_eq_false, Float.beq_self_iff, Float32.beq_self_iff, Float.beq_self_eq_false_iff, Float32.beq_self_eq_false_iff, Float.bne_eq, Float32.bne_eq
statement: formalized
proof: formalized
---

# Float/Lemmas

`Batteries.Data.Float.Lemmas`, in [Batteries/Data/Float/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean), by Robin Arnez.

`Float.Model.UnpackedFloat.isNaNBits` (definition, [line 15](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L15))

> Returns true if the bits represent an NaN value

```lean
def isNaNBits {spec : Format} (b : BitVec spec.numBits) : Bool
```

`Float.Model.UnpackedFloat.Sign.ofBitVec_toBitVec` (theorem, [line 21](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L21))

```lean
theorem ofBitVec_toBitVec (s : Sign) :
    Sign.ofBitVec s.toBitVec = s
```

`Float.Model.UnpackedFloat.Sign.toBitVec_ofBitVec` (theorem, [line 26](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L26))

```lean
theorem toBitVec_ofBitVec (b : BitVec 1) :
    (Sign.ofBitVec b).toBitVec = b
```

`Float.Model.UnpackedFloat.Sign.forall_iff` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L30))

```lean
protected theorem forall_iff {p : Sign → Prop} :
    (∀ s : Sign, p s) ↔ p .positive ∧ p .negative
```

`Float.Model.UnpackedFloat.unpackSign_packComponents` (theorem, [line 42](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L42))

```lean
theorem unpackSign_packComponents {spec : Format} (s e m) :
    unpackSign (packComponents spec s e m) = s.toBitVec
```

`Float.Model.UnpackedFloat.packComponents_unpackSign_unpackExponent_unpackMantissa` (theorem, [line 47](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L47))

```lean
theorem packComponents_unpackSign_unpackExponent_unpackMantissa
    {spec : Format} (b : BitVec spec.numBits) :
    packComponents spec
      (Sign.ofBitVec (unpackSign b)) (unpackExponent b) (unpackMantissa b) = b
```

`Float.Model.UnpackedFloat.pack_unpack` (theorem, [line 59](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L59))

```lean
theorem pack_unpack {spec : Format} (b : BitVec spec.numBits) :
    (unpack spec b).pack spec = if isNaNBits b then packedNaN spec else b
```

`Float.Model.UnpackedFloat.pack_unpack_of_valid` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L115))

```lean
theorem pack_unpack_of_valid {spec : Format} {b : BitVec spec.numBits}
    (hvalid : spec.Valid b) : (unpack spec b).pack spec = b
```

`Float.Model.UnpackedFloat.unpack_inj_of_valid` (theorem, [line 120](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L120))

```lean
theorem unpack_inj_of_valid {spec : Format} {b b' : BitVec spec.numBits}
    (hb : spec.Valid b) (hb' : spec.Valid b') :
    unpack spec b = unpack spec b' ↔ b = b'
```

`Float.Model.UnpackedFloat.isNaNBits_packedNaN` (theorem, [line 129](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L129))

```lean
theorem isNaNBits_packedNaN {spec : Format} : isNaNBits (packedNaN spec)
```

`Float.Model.UnpackedFloat.unpack_packedNaN` (theorem, [line 137](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L137))

```lean
theorem unpack_packedNaN {spec : Format} : unpack spec (packedNaN spec) = notANumber
```

`Float.Model.UnpackedFloat.unpack_packedZero` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L143))

```lean
theorem unpack_packedZero {spec : Format} {sign : Sign} :
    unpack spec (packedZero spec sign) = .zero sign
```

`Float.Model.UnpackedFloat.isNaN_iff` (theorem, [line 148](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L148))

```lean
theorem isNaN_iff : isNaN x ↔ x = notANumber
```

`Float.Model.UnpackedFloat.unpack_eq_notANumber_iff_of_valid` (theorem, [line 151](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L151))

```lean
theorem unpack_eq_notANumber_iff_of_valid {spec : Format} {b : BitVec spec.numBits}
    (hvalid : spec.Valid b) : unpack spec b = notANumber ↔ b = packedNaN spec
```

`Float.Model.UnpackedFloat.unpack_eq_zero_iff_of_valid` (theorem, [line 155](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L155))

```lean
theorem unpack_eq_zero_iff_of_valid {spec : Format} {sign : Sign} {b : BitVec spec.numBits}
    (hvalid : spec.Valid b) : unpack spec b = zero sign ↔ b = packedZero spec sign
```

`Float.Model.UnpackedFloat.isNaN_unpack_iff_of_valid` (theorem, [line 159](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L159))

```lean
theorem isNaN_unpack_iff_of_valid {spec : Format} {b : BitVec spec.numBits}
    (hvalid : spec.Valid b) : (unpack spec b).isNaN ↔ b = packedNaN spec
```

`Float.Model.UnpackedFloat.beq_iff_ne_notANumber_and_eq` (theorem, [line 163](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L163))

```lean
theorem beq_iff_ne_notANumber_and_eq (a b : UnpackedFloat) :
    a.beq b ↔ a ≠ notANumber ∧ b ≠ notANumber ∧
      (a = b ∨ (a = .zero .positive ∧ b = .zero .negative) ∨
        (a = .zero .negative ∧ b = .zero .positive))
```

`Float.Model.UnpackedFloat.unpack_beq_unpack_iff` (theorem, [line 171](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L171))

```lean
theorem unpack_beq_unpack_iff {spec : Format} {b b' : BitVec spec.numBits}
    (hb : spec.Valid b) (hb' : spec.Valid b') :
    (unpack spec b).beq (unpack spec b') ↔ b ≠ packedNaN spec ∧ b' ≠ packedNaN spec ∧
        (b = b' ∨ (b = packedZero spec .positive ∧ b' = packedZero spec .negative) ∨
          (b = packedZero spec .negative ∧ b' = packedZero spec .positive))
```

`Float.toBits_inj` (theorem, [line 181](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L181))

```lean
theorem Float.toBits_inj {f f' : Float} : f.toBits = f'.toBits ↔ f = f'
```

`Float32.toBits_inj` (theorem, [line 184](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L184))

```lean
theorem Float32.toBits_inj {f f' : Float32} : f.toBits = f'.toBits ↔ f = f'
```

`Float.ofBits_toBits` (theorem, [line 188](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L188))

```lean
theorem Float.ofBits_toBits (f : Float) : ofBits f.toBits = f
```

`Float32.ofBits_toBits` (theorem, [line 193](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L193))

```lean
theorem Float32.ofBits_toBits (f : Float32) : ofBits f.toBits = f
```

`Float.isNaN_eq_decide_eq_nan` (theorem, [line 198](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L198))

```lean
theorem Float.isNaN_eq_decide_eq_nan {f : Float} : isNaN f = decide (f = nan)
```

`Float32.isNaN_eq_decide_eq_nan` (theorem, [line 203](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L203))

```lean
theorem Float32.isNaN_eq_decide_eq_nan {f : Float32} : isNaN f = decide (f = nan)
```

`Float.beq_iff_ne_nan_and_eq` (theorem, [line 207](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L207))

```lean
theorem Float.beq_iff_ne_nan_and_eq {f f' : Float} :
    f == f' ↔ f ≠ nan ∧ f' ≠ nan ∧ (f = f' ∨ (f = 0 ∧ f' = -0) ∨ (f = -0 ∧ f' = 0))
```

`Float32.beq_iff_ne_nan_and_eq` (theorem, [line 212](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L212))

```lean
theorem Float32.beq_iff_ne_nan_and_eq {f f' : Float32} :
    f == f' ↔ f ≠ nan ∧ f' ≠ nan ∧ (f = f' ∨ (f = 0 ∧ f' = -0) ∨ (f = -0 ∧ f' = 0))
```

`Float.nan_beq_eq_false` (theorem, [line 218](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L218))

```lean
theorem Float.nan_beq_eq_false (f : Float) : (nan == f) = false
```

`Float32.nan_beq_eq_false` (theorem, [line 222](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L222))

```lean
theorem Float32.nan_beq_eq_false (f : Float32) : (nan == f) = false
```

`Float.beq_nan_eq_false` (theorem, [line 226](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L226))

```lean
theorem Float.beq_nan_eq_false (f : Float) : (f == nan) = false
```

`Float32.beq_nan_eq_false` (theorem, [line 230](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L230))

```lean
theorem Float32.beq_nan_eq_false (f : Float32) : (f == nan) = false
```

`Float.beq_self_iff` (theorem, [line 234](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L234))

```lean
theorem Float.beq_self_iff {f : Float} : f == f ↔ f ≠ nan
```

`Float32.beq_self_iff` (theorem, [line 238](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L238))

```lean
theorem Float32.beq_self_iff {f : Float32} : f == f ↔ f ≠ nan
```

`Float.beq_self_eq_false_iff` (theorem, [line 242](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L242))

```lean
theorem Float.beq_self_eq_false_iff {f : Float} : (f == f) = false ↔ f = nan
```

`Float32.beq_self_eq_false_iff` (theorem, [line 246](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L246))

```lean
theorem Float32.beq_self_eq_false_iff {f : Float32} : (f == f) = false ↔ f = nan
```

`Float.bne_eq` (theorem, [line 253](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L253))

> This theorem is true for all types but most other types have `LawfulBEq` where
> `bne_self_eq_false` or `bne_iff_ne` apply.

```lean
theorem Float.bne_eq {f : Float} : (f != f) = (!f == f)
```

`Float32.bne_eq` (theorem, [line 259](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean#L259))

> This theorem is true for all types but most other types have `LawfulBEq` where
> `bne_self_eq_false` or `bne_iff_ne` apply.

```lean
theorem Float32.bne_eq {f : Float32} : (f != f) = (!f == f)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Float/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Float.Lemmas.json)
