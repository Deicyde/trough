---
catalog: module
lean: Mersenne31.Fast.Field, Mersenne31.Fast.modulus, Mersenne31.Fast.modulus_toNat, Mersenne31.Fast.raw, Mersenne31.Fast.raw_mk, Mersenne31.Fast.raw_eq_val, Mersenne31.Fast.instZeroField, Mersenne31.Fast.instOneField, Mersenne31.Fast.ofNat, Mersenne31.Fast.toNat, Mersenne31.Fast.toNat_mk, Mersenne31.Fast.toNat_eq_val_toNat, Mersenne31.Fast.ofField, Mersenne31.Fast.toField, Mersenne31.Fast.ofUInt32, Mersenne31.Fast.ofInt, Mersenne31.Fast.instNatCastField, Mersenne31.Fast.instIntCastField, Mersenne31.Fast.instNNRatCastField, Mersenne31.Fast.instRatCastField, Mersenne31.Fast.raw_zero, Mersenne31.Fast.raw_one, Mersenne31.Fast.toNat_zero, Mersenne31.Fast.toNat_one, Mersenne31.Fast.toNat_ofNat, Mersenne31.Fast.toField_ofNat, Mersenne31.Fast.toField_ofUInt32, Mersenne31.Fast.toNat_ofUInt32, Mersenne31.Fast.toNat_ofField, Mersenne31.Fast.toField_ofField, Mersenne31.Fast.toField_ofInt, Mersenne31.Fast.ofField_toField, Mersenne31.Fast.toField_zero, Mersenne31.Fast.toField_one, Mersenne31.Fast.toField_natCast, Mersenne31.Fast.toField_intCast, Mersenne31.Fast.toField_nnratCast, Mersenne31.Fast.toField_ratCast, Mersenne31.Fast.add, Mersenne31.Fast.instAddField, Mersenne31.Fast.toField_add, Mersenne31.Fast.sub, Mersenne31.Fast.instSubField, Mersenne31.Fast.toField_sub, Mersenne31.Fast.neg, Mersenne31.Fast.instNegField, Mersenne31.Fast.toField_neg, Mersenne31.Fast.mul, Mersenne31.Fast.instMulField, Mersenne31.Fast.instNatSMulField, Mersenne31.Fast.instIntSMulField, Mersenne31.Fast.instNNRatSMulField, Mersenne31.Fast.instRatSMulField, Mersenne31.Fast.toField_mul, Mersenne31.Fast.square, Mersenne31.Fast.toField_square, Mersenne31.Fast.pow, Mersenne31.Fast.instPowFieldNat, Mersenne31.Fast.toField_pow, Mersenne31.Fast.inv, Mersenne31.Fast.instInvField, Mersenne31.Fast.toField_inv, Mersenne31.Fast.div, Mersenne31.Fast.instDivField, Mersenne31.Fast.toField_div, Mersenne31.Fast.instPowFieldInt, Mersenne31.Fast.toField_nsmul, Mersenne31.Fast.toField_zsmul, Mersenne31.Fast.toField_npow, Mersenne31.Fast.toField_zpow, Mersenne31.Fast.toField_nnqsmul, Mersenne31.Fast.toField_qsmul, Mersenne31.Fast.ringEquiv, Mersenne31.Fast.ringEquiv_apply, Mersenne31.Fast.ringEquiv_symm_apply, Mersenne31.Fast.instField, Mersenne31.Fast.instCommRing, Mersenne31.Fast.instNonBinaryField
statement: formalized
proof: formalized
---

# FastMersenne31 — UInt32-backed Mersenne-31 field arithmetic

`CompPoly.Fields.Mersenne31.Fast`, in [CompPoly/Fields/Mersenne31/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean), by Varun Thakore.

> This module provides a native-word implementation of Mersenne31 arithmetic as a
> sidecar to the canonical `Mersenne31.Field := ZMod Mersenne31.fieldSize`
> model.
>
> Fast field values are stored as canonical `UInt32` representatives below
> `2^31 - 1`. Multiplication reduces a bounded `UInt64` product using the Mersenne
> identity `2^31 ≡ 1 (mod 2^31 - 1)`: split at bit 31, add the halves, then perform
> one final subtraction if needed.

`Mersenne31.Fast.Field` (abbreviation, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L34))

> The fast native-word Mersenne31 field carrier, stored as a canonical `UInt32`
> representative below the prime modulus.

```lean
abbrev Field : Type
```

`Mersenne31.Fast.modulus` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L41))

> The Mersenne31 prime `2^31 - 1` as a native `UInt32`.

```lean
def modulus : UInt32
```

`Mersenne31.Fast.modulus_toNat` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L49))

> The native `UInt32` modulus agrees with the mathematical Mersenne31 modulus.

```lean
theorem modulus_toNat : modulus.toNat = Mersenne31.fieldSize
```

`Mersenne31.Fast.raw` (definition, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L77))

> The raw native word backing a fast Mersenne31 element.

```lean
def raw (x : Field) : UInt32
```

`Mersenne31.Fast.raw_mk` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L81))

> Reading the raw word from a subtype literal returns its stored word.

```lean
theorem raw_mk (x : UInt32) (h : x.toNat < Mersenne31.fieldSize) :
    raw ⟨x, h⟩ = x
```

`Mersenne31.Fast.raw_eq_val` (theorem, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L86))

> `raw` is the underlying `UInt32` value.

```lean
theorem raw_eq_val (x : Field) : raw x = x.val
```

`Mersenne31.Fast.instZeroField` (instance, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L89))

> Use the canonical zero representative for standard `0` notation.

```lean
instance instZeroField : Zero Field
```

`Mersenne31.Fast.instOneField` (instance, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L93))

> Use the canonical one representative for standard `1` notation.

```lean
instance instOneField : One Field
```

`Mersenne31.Fast.ofNat` (definition, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L105))

> Convert a natural number into fast representation by reducing modulo Mersenne31.

```lean
def ofNat (n : Nat) : Field
```

`Mersenne31.Fast.toNat` (definition, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L110))

> Convert a fast Mersenne31 element to its canonical natural representative.

```lean
def toNat (x : Field) : Nat
```

`Mersenne31.Fast.toNat_mk` (theorem, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L116))

> Reading the natural representative from a subtype literal returns the stored word's
> natural value.

```lean
theorem toNat_mk (x : UInt32) (h : x.toNat < Mersenne31.fieldSize) :
    toNat ⟨x, h⟩ = x.toNat
```

`Mersenne31.Fast.toNat_eq_val_toNat` (theorem, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L121))

> `toNat` is the natural value of the underlying `UInt32` word.

```lean
theorem toNat_eq_val_toNat (x : Field) : toNat x = x.val.toNat
```

`Mersenne31.Fast.ofField` (definition, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L125))

> Convert from the canonical `ZMod` Mersenne31 field into fast representation.

```lean
def ofField (x : Mersenne31.Field) : Field
```

`Mersenne31.Fast.toField` (definition, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L130))

> Convert a fast Mersenne31 element to the canonical `ZMod` field.

```lean
def toField (x : Field) : Mersenne31.Field
```

`Mersenne31.Fast.ofUInt32` (definition, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L135))

> Convert a 32-bit word into fast representation.

```lean
def ofUInt32 (x : UInt32) : Field
```

`Mersenne31.Fast.ofInt` (definition, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L140))

> Convert an integer into fast representation.

```lean
def ofInt (z : Int) : Field
```

`Mersenne31.Fast.instNatCastField` (instance, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L144))

> Use `ofNat` for natural-number casts into fast Mersenne31.

```lean
instance instNatCastField : NatCast Field
```

`Mersenne31.Fast.instIntCastField` (instance, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L148))

> Interpret integer casts through the canonical Mersenne31 field.

```lean
instance instIntCastField : IntCast Field
```

`Mersenne31.Fast.instNNRatCastField` (instance, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L152))

> Interpret nonnegative rational casts through the canonical Mersenne31 field.

```lean
instance instNNRatCastField : NNRatCast Field
```

`Mersenne31.Fast.instRatCastField` (instance, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L156))

> Interpret rational casts through the canonical Mersenne31 field.

```lean
instance instRatCastField : RatCast Field
```

`Mersenne31.Fast.raw_zero` (theorem, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L161))

> The raw word backing fast zero is zero.

```lean
theorem raw_zero : raw (0 : Field) = 0
```

`Mersenne31.Fast.raw_one` (theorem, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L165))

> The raw word backing fast one is one.

```lean
theorem raw_one : raw (1 : Field) = 1
```

`Mersenne31.Fast.toNat_zero` (theorem, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L169))

> The natural representative of fast zero is zero.

```lean
theorem toNat_zero : toNat (0 : Field) = 0
```

`Mersenne31.Fast.toNat_one` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L173))

> The natural representative of fast one is one.

```lean
theorem toNat_one : toNat (1 : Field) = 1
```

`Mersenne31.Fast.toNat_ofNat` (theorem, [line 194](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L194))

> Converting a natural number to fast form and reading it back gives its canonical
> representative modulo Mersenne31.

```lean
theorem toNat_ofNat (n : Nat) :
    toNat (ofNat n) = n % Mersenne31.fieldSize
```

`Mersenne31.Fast.toField_ofNat` (theorem, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L202))

> Converting a natural number to fast form agrees with the same natural cast in the
> canonical field.

```lean
theorem toField_ofNat (n : Nat) :
    toField (ofNat n) = (n : Mersenne31.Field)
```

`Mersenne31.Fast.toField_ofUInt32` (theorem, [line 212](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L212))

> Converting a `UInt32` to fast form agrees with casting its natural value into the
> canonical field.

```lean
theorem toField_ofUInt32 (x : UInt32) :
    toField (ofUInt32 x) = (x.toNat : Mersenne31.Field)
```

`Mersenne31.Fast.toNat_ofUInt32` (theorem, [line 220](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L220))

> Converting a `UInt32` to fast form and reading it back gives its value modulo
> Mersenne31.

```lean
theorem toNat_ofUInt32 (x : UInt32) :
    toNat (ofUInt32 x) = x.toNat % Mersenne31.fieldSize
```

`Mersenne31.Fast.toNat_ofField` (theorem, [line 228](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L228))

> Converting from the canonical field to fast form and reading the natural
> representative returns the canonical `ZMod` representative.

```lean
theorem toNat_ofField (x : Mersenne31.Field) : toNat (ofField x) = x.val
```

`Mersenne31.Fast.toField_ofField` (theorem, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L234))

> Converting from the canonical `ZMod` field to fast form and back is the identity.

```lean
theorem toField_ofField (x : Mersenne31.Field) :
    toField (ofField x) = x
```

`Mersenne31.Fast.toField_ofInt` (theorem, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L242))

> Converting an integer to fast form agrees with casting it into the canonical field.

```lean
theorem toField_ofInt (z : Int) :
    toField (ofInt z) = (z : Mersenne31.Field)
```

`Mersenne31.Fast.ofField_toField` (theorem, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L249))

> Converting from fast form to the canonical `ZMod` field and back is the identity.

```lean
theorem ofField_toField (x : Field) :
    ofField (toField x) = x
```

`Mersenne31.Fast.toField_zero` (theorem, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L264))

> The fast zero maps to zero in the canonical field.

```lean
theorem toField_zero : toField (0 : Field) = 0
```

`Mersenne31.Fast.toField_one` (theorem, [line 269](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L269))

> The fast one maps to one in the canonical field.

```lean
theorem toField_one : toField (1 : Field) = 1
```

`Mersenne31.Fast.toField_natCast` (theorem, [line 274](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L274))

> Natural casts in the fast field agree with natural casts in the canonical field.

```lean
theorem toField_natCast (n : Nat) :
    toField (n : Field) = (n : Mersenne31.Field)
```

`Mersenne31.Fast.toField_intCast` (theorem, [line 284](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L284))

> Integer casts in the fast field agree with integer casts in the canonical field.

```lean
theorem toField_intCast (n : Int) :
    toField (n : Field) = (n : Mersenne31.Field)
```

`Mersenne31.Fast.toField_nnratCast` (theorem, [line 291](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L291))

> Nonnegative rational casts in the fast field agree with canonical-field casts.

```lean
theorem toField_nnratCast (q : ℚ≥0) :
    toField (q : Field) = (q : Mersenne31.Field)
```

`Mersenne31.Fast.toField_ratCast` (theorem, [line 298](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L298))

> Rational casts in the fast field agree with canonical-field casts.

```lean
theorem toField_ratCast (q : ℚ) :
    toField (q : Field) = (q : Mersenne31.Field)
```

`Mersenne31.Fast.add` (definition, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L360))

> Fast modular addition.

```lean
def add (x y : Field) : Field
```

`Mersenne31.Fast.instAddField` (instance, [line 369](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L369))

> Use fast modular addition for the standard `+` notation on Mersenne31 fast elements.

```lean
instance instAddField : Add Field
```

`Mersenne31.Fast.toField_add` (theorem, [line 374](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L374))

> Fast addition agrees with addition in the canonical `ZMod` Mersenne31 field.

```lean
theorem toField_add (x y : Field) :
    toField (x + y) = toField x + toField y
```

`Mersenne31.Fast.sub` (definition, [line 400](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L400))

> Fast modular subtraction, using `x - y` when no underflow occurs and
> `x + p - y` otherwise.

```lean
def sub (x y : Field) : Field
```

`Mersenne31.Fast.instSubField` (instance, [line 429](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L429))

> Use fast modular subtraction for the standard `-` notation on Mersenne31 fast elements.

```lean
instance instSubField : Sub Field
```

`Mersenne31.Fast.toField_sub` (theorem, [line 434](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L434))

> Fast subtraction agrees with subtraction in the canonical `ZMod` Mersenne31 field.

```lean
theorem toField_sub (x y : Field) : toField (x - y) = toField x - toField y
```

`Mersenne31.Fast.neg` (definition, [line 462](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L462))

> Fast modular negation. Zero remains zero; nonzero `x` maps to `p - x`.

```lean
def neg (x : Field) : Field
```

`Mersenne31.Fast.instNegField` (instance, [line 480](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L480))

> Use fast modular negation for the standard unary `-` notation on Mersenne31 fast elements.

```lean
instance instNegField : Neg Field
```

`Mersenne31.Fast.toField_neg` (theorem, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L485))

> Fast negation agrees with negation in the canonical `ZMod` Mersenne31 field.

```lean
theorem toField_neg (x : Field) : toField (-x) = -toField x
```

`Mersenne31.Fast.mul` (definition, [line 614](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L614))

> Fast modular multiplication.

```lean
def mul (x y : Field) : Field
```

`Mersenne31.Fast.instMulField` (instance, [line 624](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L624))

> Use fast modular multiplication for the standard `*` notation on Mersenne31 fast
> elements.

```lean
instance instMulField : Mul Field
```

`Mersenne31.Fast.instNatSMulField` (instance, [line 628](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L628))

> Natural scalar multiplication is multiplication by the corresponding fast natural cast.

```lean
instance instNatSMulField : SMul Nat Field
```

`Mersenne31.Fast.instIntSMulField` (instance, [line 632](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L632))

> Integer scalar multiplication is multiplication by the corresponding fast integer cast.

```lean
instance instIntSMulField : SMul Int Field
```

`Mersenne31.Fast.instNNRatSMulField` (instance, [line 636](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L636))

> Nonnegative rational scalar multiplication is transported through the canonical field.

```lean
instance instNNRatSMulField : SMul ℚ≥0 Field
```

`Mersenne31.Fast.instRatSMulField` (instance, [line 640](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L640))

> Rational scalar multiplication is transported through the canonical field.

```lean
instance instRatSMulField : SMul ℚ Field
```

`Mersenne31.Fast.toField_mul` (theorem, [line 646](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L646))

> Fast multiplication agrees with multiplication in the canonical `ZMod` Mersenne31
> field.

```lean
theorem toField_mul (x y : Field) : toField (x * y) = toField x * toField y
```

`Mersenne31.Fast.square` (definition, [line 659](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L659))

> Fast squaring.

```lean
def square (x : Field) : Field
```

`Mersenne31.Fast.toField_square` (theorem, [line 664](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L664))

> Fast squaring agrees with multiplying the canonical field value by itself.

```lean
theorem toField_square (x : Field) : toField (square x) = toField x * toField x
```

`Mersenne31.Fast.pow` (definition, [line 670](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L670))

> Exponentiation over the fast representation using binary exponentiation.

```lean
def pow (x : Field) (n : Nat) : Field
```

`Mersenne31.Fast.instPowFieldNat` (instance, [line 674](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L674))

> Use fast binary exponentiation for natural powers.

```lean
instance instPowFieldNat : Pow Field Nat
```

`Mersenne31.Fast.toField_pow` (theorem, [line 695](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L695))

> Fast natural-power computation agrees with powers in the canonical field.

```lean
theorem toField_pow (x : Field) (n : Nat) : toField (pow x n) = toField x ^ n
```

`Mersenne31.Fast.inv` (definition, [line 726](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L726))

> Fast modular inversion using a fixed Fermat addition chain for `x^(p - 2)`.
>
> The exponent is `p - 2 = 2147483645 = 0x7FFFFFFD`. The chain builds the
> hex digits `7 F F F F F F D` by repeatedly applying `shift4Mul`, which raises
> the accumulator to the 16th power and multiplies by the next 4-bit digit.
>
> This sends zero to zero, matching Lean's field inverse convention.

```lean
def inv (x : Field) : Field
```

`Mersenne31.Fast.instInvField` (instance, [line 743](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L743))

> Use Fermat-based fast inversion for the standard inverse notation.

```lean
instance instInvField : Inv Field
```

`Mersenne31.Fast.toField_inv` (theorem, [line 836](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L836))

> Fast inversion agrees with inversion in the canonical field.

```lean
theorem toField_inv (x : Field) : toField x⁻¹ = (toField x)⁻¹
```

`Mersenne31.Fast.div` (definition, [line 854](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L854))

> Division through inversion and fast multiplication.

```lean
def div (x y : Field) : Field
```

`Mersenne31.Fast.instDivField` (instance, [line 858](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L858))

> Use fast inversion and multiplication for the standard `/` notation.

```lean
instance instDivField : Div Field
```

`Mersenne31.Fast.toField_div` (theorem, [line 863](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L863))

> Fast division agrees with division in the canonical field.

```lean
theorem toField_div (x y : Field) : toField (x / y) = toField x / toField y
```

`Mersenne31.Fast.instPowFieldInt` (instance, [line 873](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L873))

> Use fast natural powers and inversion for integer powers.

```lean
instance instPowFieldInt : Pow Field Int
```

`Mersenne31.Fast.toField_nsmul` (theorem, [line 881](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L881))

> Fast natural scalar multiplication agrees with canonical-field scalar multiplication.

```lean
theorem toField_nsmul (n : Nat) (x : Field) : toField (n • x) = n • toField x
```

`Mersenne31.Fast.toField_zsmul` (theorem, [line 887](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L887))

> Fast integer scalar multiplication agrees with canonical-field scalar multiplication.

```lean
theorem toField_zsmul (n : Int) (x : Field) : toField (n • x) = n • toField x
```

`Mersenne31.Fast.toField_npow` (theorem, [line 893](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L893))

> Standard fast natural powers agree with powers in the canonical field.

```lean
theorem toField_npow (x : Field) (n : Nat) : toField (x ^ n) = toField x ^ n
```

`Mersenne31.Fast.toField_zpow` (theorem, [line 899](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L899))

> Standard fast integer powers agree with integer powers in the canonical field.

```lean
theorem toField_zpow (x : Field) (n : Int) : toField (x ^ n) = toField x ^ n
```

`Mersenne31.Fast.toField_nnqsmul` (theorem, [line 913](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L913))

> Fast nonnegative rational scalar multiplication agrees with canonical-field scalar
> multiplication.

```lean
theorem toField_nnqsmul (q : ℚ≥0) (x : Field) : toField (q • x) = q • toField x
```

`Mersenne31.Fast.toField_qsmul` (theorem, [line 919](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L919))

> Fast rational scalar multiplication agrees with canonical-field scalar multiplication.

```lean
theorem toField_qsmul (q : ℚ) (x : Field) : toField (q • x) = q • toField x
```

`Mersenne31.Fast.ringEquiv` (definition, [line 925](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L925))

> Ring equivalence between the fast representation and canonical `Mersenne31.Field`.

```lean
def ringEquiv : Field ≃+* Mersenne31.Field
```

`Mersenne31.Fast.ringEquiv_apply` (theorem, [line 935](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L935))

> Applying `ringEquiv` is the same as interpreting a fast value canonically.

```lean
theorem ringEquiv_apply (x : Field) : ringEquiv x = toField x
```

`Mersenne31.Fast.ringEquiv_symm_apply` (theorem, [line 939](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L939))

> Applying the inverse `ringEquiv` converts a canonical value into fast form.

```lean
theorem ringEquiv_symm_apply (x : Mersenne31.Field) : ringEquiv.symm x = ofField x
```

`Mersenne31.Fast.instField` (instance, [line 943](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L943))

> Field instance transferred from canonical Mersenne31 through `toField`.

```lean
instance (priority := low) instField : _root_.Field Field
```

`Mersenne31.Fast.instCommRing` (instance, [line 965](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L965))

> Commutative-ring instance inherited from the transferred field structure.

```lean
instance (priority := low) instCommRing : CommRing Field
```

`Mersenne31.Fast.instNonBinaryField` (instance, [line 969](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean#L969))

> Fast Mersenne31 is a non-binary field.

```lean
instance (priority := low) instNonBinaryField : NonBinaryField Field
```

## Depends on

- [Mersenne prime field `2^{31} - 1`](basic.md)

## Sources

- [CompPoly/Fields/Mersenne31/Fast.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Mersenne31/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Mersenne31.Fast.json)
