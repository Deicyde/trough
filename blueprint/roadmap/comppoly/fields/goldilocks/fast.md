---
catalog: module
lean: Goldilocks.Fast.Field, Goldilocks.Fast.raw, Goldilocks.Fast.raw_mk, Goldilocks.Fast.raw_eq_val, Goldilocks.Fast.reduceUInt64, Goldilocks.Fast.reduceUInt64_cast, Goldilocks.Fast.zero, Goldilocks.Fast.one, Goldilocks.Fast.ofCanonicalNat, Goldilocks.Fast.ofNat, Goldilocks.Fast.ofUInt64, Goldilocks.Fast.ofField, Goldilocks.Fast.ofInt, Goldilocks.Fast.toNat, Goldilocks.Fast.toNat_mk, Goldilocks.Fast.toNat_eq_val_toNat, Goldilocks.Fast.toField, Goldilocks.Fast.add, Goldilocks.Fast.neg, Goldilocks.Fast.sub, Goldilocks.Fast.mul, Goldilocks.Fast.square, Goldilocks.Fast.squareN, Goldilocks.Fast.pow, Goldilocks.Fast.inv, Goldilocks.Fast.div, Goldilocks.Fast.instZeroField, Goldilocks.Fast.instOneField, Goldilocks.Fast.raw_zero, Goldilocks.Fast.raw_one, Goldilocks.Fast.toNat_zero, Goldilocks.Fast.toNat_one, Goldilocks.Fast.instAddField, Goldilocks.Fast.instNegField, Goldilocks.Fast.instSubField, Goldilocks.Fast.instMulField, Goldilocks.Fast.instInvField, Goldilocks.Fast.instDivField, Goldilocks.Fast.instNatCastField, Goldilocks.Fast.instIntCastField, Goldilocks.Fast.instNatSMulField, Goldilocks.Fast.instIntSMulField, Goldilocks.Fast.instPowFieldNat, Goldilocks.Fast.instPowFieldInt, Goldilocks.Fast.instNNRatCastField, Goldilocks.Fast.instRatCastField, Goldilocks.Fast.instNNRatSMulField, Goldilocks.Fast.instRatSMulField, Goldilocks.Fast.toNat_ofNat, Goldilocks.Fast.toNat_ofUInt64, Goldilocks.Fast.toNat_ofField, Goldilocks.Fast.toField_ofNat, Goldilocks.Fast.toField_ofUInt64, Goldilocks.Fast.toField_ofInt, Goldilocks.Fast.toField_ofField, Goldilocks.Fast.ofField_toField, Goldilocks.Fast.toField_injective, Goldilocks.Fast.toField_zero, Goldilocks.Fast.toField_one, Goldilocks.Fast.toField_add, Goldilocks.Fast.toField_neg, Goldilocks.Fast.toField_sub, Goldilocks.Fast.toField_mul, Goldilocks.Fast.toField_mul_def, Goldilocks.Fast.toField_square, Goldilocks.Fast.toField_squareN, Goldilocks.Fast.toField_pow, Goldilocks.Fast.toField_inv, Goldilocks.Fast.toField_div, Goldilocks.Fast.toField_natCast, Goldilocks.Fast.toField_intCast, Goldilocks.Fast.toField_nsmul, Goldilocks.Fast.toField_zsmul, Goldilocks.Fast.toField_npow, Goldilocks.Fast.toField_zpow, Goldilocks.Fast.toField_nnratCast, Goldilocks.Fast.toField_ratCast, Goldilocks.Fast.toField_nnqsmul, Goldilocks.Fast.toField_qsmul, Goldilocks.Fast.ringEquiv, Goldilocks.Fast.ringEquiv_apply, Goldilocks.Fast.ringEquiv_symm_apply, Goldilocks.Fast.instField, Goldilocks.Fast.instCommRing, Goldilocks.Fast.instNonBinaryField
statement: formalized
proof: formalized
---

# Fast Goldilocks Field

`CompPoly.Fields.Goldilocks.Fast`, in [CompPoly/Fields/Goldilocks/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean), by Varun Thakore.

> Verified `UInt64`-backed implementation of Goldilocks arithmetic, `p = 2^64 - 2^32 + 1`.
> The carrier is a subtype of `UInt64` holding canonical representatives, wrapping the raw
> kernels from `FastDefs` with the bounds proved in `FastReduction`. Every operation is
> identified with its counterpart in the canonical `ZMod` model, and the field instances
> are transferred across `toField`.
>
> Reduction rests on `2^64 ≡ 2^32 - 1 (mod p)`, which folds a 128-bit product back into one
> word with shifts, additions and carry corrections.

> ## Carrier and arithmetic

`Goldilocks.Fast.Field` (abbreviation, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L34))

> The fast native-word Goldilocks field carrier, stored as a canonical residue.

```lean
abbrev Field : Type
```

`Goldilocks.Fast.raw` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L41))

> The raw canonical word backing a fast Goldilocks element.

```lean
def raw (x : Field) : UInt64
```

`Goldilocks.Fast.raw_mk` (theorem, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L45))

> Reading the raw word from a subtype literal returns its stored word.

```lean
theorem raw_mk (x : UInt64) (h : x.toNat < Goldilocks.fieldSize) :
    raw ⟨x, h⟩ = x
```

`Goldilocks.Fast.raw_eq_val` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L50))

> `raw` is the underlying `UInt64` value.

```lean
theorem raw_eq_val (x : Field) : raw x = x.val
```

`Goldilocks.Fast.reduceUInt64` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L54))

> Reduce a native `UInt64` modulo Goldilocks.

```lean
def reduceUInt64 (x : UInt64) : Field
```

`Goldilocks.Fast.reduceUInt64_cast` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L59))

> One-word reduction preserves the represented canonical field element.

```lean
theorem reduceUInt64_cast (x : UInt64) :
    ((reduceUInt64 x).val.toNat : Goldilocks.Field) =
      (x.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.zero` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L66))

> The zero fast Goldilocks element.

```lean
def zero : Field
```

`Goldilocks.Fast.one` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L70))

> The one fast Goldilocks element.

```lean
def one : Field
```

`Goldilocks.Fast.ofCanonicalNat` (definition, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L74))

> Build a fast element from a canonical natural representative.

```lean
def ofCanonicalNat (n : Nat) (h : n < Goldilocks.fieldSize) : Field
```

`Goldilocks.Fast.ofNat` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L84))

> Convert a natural number into fast canonical representation.

```lean
def ofNat (n : Nat) : Field
```

`Goldilocks.Fast.ofUInt64` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L89))

> Convert a 64-bit word into fast canonical representation.

```lean
def ofUInt64 (x : UInt64) : Field
```

`Goldilocks.Fast.ofField` (definition, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L94))

> Convert from the canonical `ZMod` Goldilocks field into fast canonical form.

```lean
def ofField (x : Goldilocks.Field) : Field
```

`Goldilocks.Fast.ofInt` (definition, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L99))

> Convert an integer into fast canonical representation.

```lean
def ofInt (z : Int) : Field
```

`Goldilocks.Fast.toNat` (definition, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L104))

> Convert a fast Goldilocks element to its canonical natural representative.

```lean
def toNat (x : Field) : Nat
```

`Goldilocks.Fast.toNat_mk` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L110))

> Reading the natural representative of a subtype literal returns its stored word's
> natural value.

```lean
theorem toNat_mk (x : UInt64) (h : x.toNat < Goldilocks.fieldSize) :
    toNat ⟨x, h⟩ = x.toNat
```

`Goldilocks.Fast.toNat_eq_val_toNat` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L115))

> `toNat` is the natural value of the underlying `UInt64` word.

```lean
theorem toNat_eq_val_toNat (x : Field) : toNat x = x.val.toNat
```

`Goldilocks.Fast.toField` (definition, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L119))

> Convert a fast Goldilocks element to the canonical `ZMod` Goldilocks field.

```lean
def toField (x : Field) : Goldilocks.Field
```

`Goldilocks.Fast.add` (definition, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L124))

> Fast modular addition in canonical form.

```lean
def add (x y : Field) : Field
```

`Goldilocks.Fast.neg` (definition, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L129))

> Fast modular negation in canonical form.

```lean
def neg (x : Field) : Field
```

`Goldilocks.Fast.sub` (definition, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L134))

> Fast modular subtraction in canonical form.

```lean
def sub (x y : Field) : Field
```

`Goldilocks.Fast.mul` (definition, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L139))

> Fast modular multiplication in canonical form.

```lean
def mul (x y : Field) : Field
```

`Goldilocks.Fast.square` (definition, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L144))

> Fast squaring.

```lean
def square (x : Field) : Field
```

`Goldilocks.Fast.squareN` (definition, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L149))

> Repeated squaring, `squareN x n = x^(2^n)`, as a tail-recursive loop.

```lean
def squareN (x : Field) : Nat → Field
```

`Goldilocks.Fast.pow` (definition, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L155))

> Exponentiation through the lazy ladder `powLazy`, canonicalized once.

```lean
def pow (x : Field) (n : Nat) : Field
```

`Goldilocks.Fast.inv` (definition, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L164))

> Fast modular inversion through the lazy Fermat chain `invLazy`, canonicalized once.

```lean
def inv (x : Field) : Field
```

`Goldilocks.Fast.div` (definition, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L169))

> Division through inversion and fast multiplication.

```lean
def div (x y : Field) : Field
```

`Goldilocks.Fast.instZeroField` (instance, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L173))

> Use fast zero for standard `0` notation.

```lean
instance instZeroField : Zero Field
```

`Goldilocks.Fast.instOneField` (instance, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L177))

> Use fast one for standard `1` notation.

```lean
instance instOneField : One Field
```

`Goldilocks.Fast.raw_zero` (theorem, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L182))

> The raw word backing fast zero is zero.

```lean
theorem raw_zero : raw (0 : Field) = 0
```

`Goldilocks.Fast.raw_one` (theorem, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L186))

> The raw word backing fast one is one.

```lean
theorem raw_one : raw (1 : Field) = 1
```

`Goldilocks.Fast.toNat_zero` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L190))

> The natural representative of fast zero is zero.

```lean
theorem toNat_zero : toNat (0 : Field) = 0
```

`Goldilocks.Fast.toNat_one` (theorem, [line 194](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L194))

> The natural representative of fast one is one.

```lean
theorem toNat_one : toNat (1 : Field) = 1
```

`Goldilocks.Fast.instAddField` (instance, [line 197](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L197))

> Use fast addition for standard `+` notation.

```lean
instance instAddField : Add Field
```

`Goldilocks.Fast.instNegField` (instance, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L201))

> Use fast negation for standard unary `-` notation.

```lean
instance instNegField : Neg Field
```

`Goldilocks.Fast.instSubField` (instance, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L205))

> Use fast subtraction for standard `-` notation.

```lean
instance instSubField : Sub Field
```

`Goldilocks.Fast.instMulField` (instance, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L209))

> Use fast multiplication for standard `*` notation.

```lean
instance instMulField : Mul Field
```

`Goldilocks.Fast.instInvField` (instance, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L213))

> Use fast inversion for standard inverse notation.

```lean
instance instInvField : Inv Field
```

`Goldilocks.Fast.instDivField` (instance, [line 217](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L217))

> Use fast division for standard `/` notation.

```lean
instance instDivField : Div Field
```

`Goldilocks.Fast.instNatCastField` (instance, [line 221](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L221))

> Use `ofNat` for natural-number casts into fast Goldilocks.

```lean
instance instNatCastField : NatCast Field
```

`Goldilocks.Fast.instIntCastField` (instance, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L225))

> Interpret integer casts through the canonical Goldilocks field.

```lean
instance instIntCastField : IntCast Field
```

`Goldilocks.Fast.instNatSMulField` (instance, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L229))

> Natural scalar multiplication is multiplication by the corresponding fast natural cast.

```lean
instance instNatSMulField : SMul Nat Field
```

`Goldilocks.Fast.instIntSMulField` (instance, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L233))

> Integer scalar multiplication is multiplication by the corresponding fast integer cast.

```lean
instance instIntSMulField : SMul Int Field
```

`Goldilocks.Fast.instPowFieldNat` (instance, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L237))

> Use fast binary exponentiation for natural powers.

```lean
instance instPowFieldNat : Pow Field Nat
```

`Goldilocks.Fast.instPowFieldInt` (instance, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L241))

> Use fast natural powers and inversion for integer powers.

```lean
instance instPowFieldInt : Pow Field Int
```

`Goldilocks.Fast.instNNRatCastField` (instance, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L248))

> Interpret nonnegative rational casts through the canonical Goldilocks field.

```lean
instance instNNRatCastField : NNRatCast Field
```

`Goldilocks.Fast.instRatCastField` (instance, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L252))

> Interpret rational casts through the canonical Goldilocks field.

```lean
instance instRatCastField : RatCast Field
```

`Goldilocks.Fast.instNNRatSMulField` (instance, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L256))

> Nonnegative rational scalar multiplication is transported through the canonical field.

```lean
instance instNNRatSMulField : SMul ℚ≥0 Field
```

`Goldilocks.Fast.instRatSMulField` (instance, [line 260](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L260))

> Rational scalar multiplication is transported through the canonical field.

```lean
instance instRatSMulField : SMul ℚ Field
```

> ## Correctness against the canonical model

`Goldilocks.Fast.toNat_ofNat` (theorem, [line 288](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L288))

> The natural representative of a fast value built from `n` is `n` reduced modulo the
> Goldilocks modulus.

```lean
theorem toNat_ofNat (n : Nat) :
    toNat (ofNat n) = n % Goldilocks.fieldSize
```

`Goldilocks.Fast.toNat_ofUInt64` (theorem, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L296))

> The natural representative of a fast value built from a `UInt64` is that word's
> natural value reduced modulo the Goldilocks modulus.

```lean
theorem toNat_ofUInt64 (x : UInt64) :
    toNat (ofUInt64 x) = x.toNat % Goldilocks.fieldSize
```

`Goldilocks.Fast.toNat_ofField` (theorem, [line 321](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L321))

> Converting from the canonical `ZMod` field to fast form preserves the canonical
> representative.

```lean
theorem toNat_ofField (x : Goldilocks.Field) : toNat (ofField x) = x.val
```

`Goldilocks.Fast.toField_ofNat` (theorem, [line 328](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L328))

> Converting a natural number to fast form agrees with the same natural cast in the
> canonical field.

```lean
theorem toField_ofNat (n : Nat) :
    toField (ofNat n) = (n : Goldilocks.Field)
```

`Goldilocks.Fast.toField_ofUInt64` (theorem, [line 338](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L338))

> Converting a `UInt64` to fast form agrees with casting its natural value into the
> canonical field.

```lean
theorem toField_ofUInt64 (x : UInt64) :
    toField (ofUInt64 x) = (x.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.toField_ofInt` (theorem, [line 345](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L345))

> Converting an integer to fast form agrees with casting it into the canonical field.

```lean
theorem toField_ofInt (z : Int) :
    toField (ofInt z) = (z : Goldilocks.Field)
```

`Goldilocks.Fast.toField_ofField` (theorem, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L353))

> Converting from the canonical field to fast form and back is the identity.

```lean
theorem toField_ofField (x : Goldilocks.Field) : toField (ofField x) = x
```

`Goldilocks.Fast.ofField_toField` (theorem, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L360))

> Converting from fast form to the canonical field and back is the identity.

```lean
theorem ofField_toField (x : Field) : ofField (toField x) = x
```

`Goldilocks.Fast.toField_injective` (theorem, [line 369](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L369))

> The canonical-field interpretation distinguishes fast Goldilocks values.

```lean
theorem toField_injective : Function.Injective toField
```

`Goldilocks.Fast.toField_zero` (theorem, [line 393](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L393))

> Fast zero maps to canonical zero.

```lean
theorem toField_zero : toField (0 : Field) = 0
```

`Goldilocks.Fast.toField_one` (theorem, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L398))

> Fast one maps to canonical one.

```lean
theorem toField_one : toField (1 : Field) = 1
```

`Goldilocks.Fast.toField_add` (theorem, [line 403](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L403))

> Fast addition agrees with canonical-field addition.

```lean
theorem toField_add (x y : Field) : toField (x + y) = toField x + toField y
```

`Goldilocks.Fast.toField_neg` (theorem, [line 410](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L410))

> Fast negation agrees with canonical-field negation.

```lean
theorem toField_neg (x : Field) : toField (-x) = -toField x
```

`Goldilocks.Fast.toField_sub` (theorem, [line 417](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L417))

> Fast subtraction agrees with canonical-field subtraction.

```lean
theorem toField_sub (x y : Field) : toField (x - y) = toField x - toField y
```

`Goldilocks.Fast.toField_mul` (theorem, [line 424](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L424))

> Fast multiplication agrees with canonical-field multiplication.

```lean
theorem toField_mul (x y : Field) : toField (x * y) = toField x * toField y
```

`Goldilocks.Fast.toField_mul_def` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L431))

> The named fast multiplication function agrees with canonical-field multiplication.

```lean
theorem toField_mul_def (x y : Field) : toField (mul x y) = toField x * toField y
```

`Goldilocks.Fast.toField_square` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L436))

> Fast squaring agrees with multiplying the canonical field value by itself.

```lean
theorem toField_square (x : Field) : toField (square x) = toField x * toField x
```

`Goldilocks.Fast.toField_squareN` (theorem, [line 442](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L442))

> Repeated fast squaring agrees with raising to `2^n` in the canonical field.

```lean
theorem toField_squareN (x : Field) (n : Nat) :
    toField (squareN x n) = toField x ^ (2 ^ n)
```

`Goldilocks.Fast.toField_pow` (theorem, [line 457](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L457))

> Fast natural-power computation agrees with powers in the canonical field.

```lean
theorem toField_pow (x : Field) (n : Nat) : toField (pow x n) = toField x ^ n
```

`Goldilocks.Fast.toField_inv` (theorem, [line 481](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L481))

> Fast inversion agrees with inversion in the canonical field.

```lean
theorem toField_inv (x : Field) : toField x⁻¹ = (toField x)⁻¹
```

`Goldilocks.Fast.toField_div` (theorem, [line 494](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L494))

> Fast division agrees with division in the canonical field.

```lean
theorem toField_div (x y : Field) : toField (x / y) = toField x / toField y
```

`Goldilocks.Fast.toField_natCast` (theorem, [line 501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L501))

> Natural casts in the fast field agree with natural casts in the canonical field.

```lean
theorem toField_natCast (n : Nat) : toField (n : Field) = (n : Goldilocks.Field)
```

`Goldilocks.Fast.toField_intCast` (theorem, [line 507](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L507))

> Integer casts in the fast field agree with integer casts in the canonical field.

```lean
theorem toField_intCast (n : Int) : toField (n : Field) = (n : Goldilocks.Field)
```

`Goldilocks.Fast.toField_nsmul` (theorem, [line 513](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L513))

> Fast natural scalar multiplication agrees with canonical-field scalar multiplication.

```lean
theorem toField_nsmul (n : Nat) (x : Field) : toField (n • x) = n • toField x
```

`Goldilocks.Fast.toField_zsmul` (theorem, [line 520](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L520))

> Fast integer scalar multiplication agrees with canonical-field scalar multiplication.

```lean
theorem toField_zsmul (n : Int) (x : Field) : toField (n • x) = n • toField x
```

`Goldilocks.Fast.toField_npow` (theorem, [line 527](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L527))

> Standard fast natural powers agree with powers in the canonical field.

```lean
theorem toField_npow (x : Field) (n : Nat) : toField (x ^ n) = toField x ^ n
```

`Goldilocks.Fast.toField_zpow` (theorem, [line 533](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L533))

> Standard fast integer powers agree with integer powers in the canonical field.

```lean
theorem toField_zpow (x : Field) (n : Int) : toField (x ^ n) = toField x ^ n
```

`Goldilocks.Fast.toField_nnratCast` (theorem, [line 546](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L546))

> Nonnegative rational casts in the fast field agree with canonical-field casts.

```lean
theorem toField_nnratCast (q : ℚ≥0) : toField (q : Field) = (q : Goldilocks.Field)
```

`Goldilocks.Fast.toField_ratCast` (theorem, [line 552](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L552))

> Rational casts in the fast field agree with canonical-field casts.

```lean
theorem toField_ratCast (q : ℚ) : toField (q : Field) = (q : Goldilocks.Field)
```

`Goldilocks.Fast.toField_nnqsmul` (theorem, [line 559](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L559))

> Fast nonnegative rational scalar multiplication agrees with canonical-field scalar
> multiplication.

```lean
theorem toField_nnqsmul (q : ℚ≥0) (x : Field) : toField (q • x) = q • toField x
```

`Goldilocks.Fast.toField_qsmul` (theorem, [line 565](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L565))

> Fast rational scalar multiplication agrees with canonical-field scalar multiplication.

```lean
theorem toField_qsmul (q : ℚ) (x : Field) : toField (q • x) = q • toField x
```

> ## Canonical bridge and field instances

`Goldilocks.Fast.ringEquiv` (definition, [line 573](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L573))

> Ring equivalence between the fast representation and canonical Goldilocks.

```lean
def ringEquiv : Field ≃+* Goldilocks.Field
```

`Goldilocks.Fast.ringEquiv_apply` (theorem, [line 583](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L583))

> Applying `ringEquiv` is the same as interpreting a fast value canonically.

```lean
theorem ringEquiv_apply (x : Field) : ringEquiv x = toField x
```

`Goldilocks.Fast.ringEquiv_symm_apply` (theorem, [line 587](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L587))

> Applying the inverse `ringEquiv` converts a canonical value into fast form.

```lean
theorem ringEquiv_symm_apply (x : Goldilocks.Field) : ringEquiv.symm x = ofField x
```

`Goldilocks.Fast.instField` (instance, [line 590](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L590))

> Field instance transferred from canonical Goldilocks through `toField`.

```lean
instance (priority := low) instField : _root_.Field Field
```

`Goldilocks.Fast.instCommRing` (instance, [line 612](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L612))

> Commutative-ring instance inherited from the transferred field structure.

```lean
instance (priority := low) instCommRing : CommRing Field
```

`Goldilocks.Fast.instNonBinaryField` (instance, [line 616](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean#L616))

> Fast Goldilocks is a non-binary field.

```lean
instance (priority := low) instNonBinaryField : NonBinaryField Field
```

## Depends on

- [Fast Goldilocks: word-level correctness](fastreduction.md)

## Sources

- [CompPoly/Fields/Goldilocks/Fast.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Goldilocks.Fast.json)
