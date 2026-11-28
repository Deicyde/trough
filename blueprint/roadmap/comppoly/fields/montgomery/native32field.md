---
catalog: module
lean: Montgomery.Native32.Mont32Field, Montgomery.Native32.FastField, Montgomery.Native32.Mont32Field.modulus_pos, Montgomery.Native32.Mont32Field.modulus32_pos, Montgomery.Native32.Mont32Field.modulus64_pos, Montgomery.Native32.Mont32Field.modulus32_lt_two_pow_31, Montgomery.Native32.Mont32Field.modulus64_lt_two_pow_31, Montgomery.Native32.Mont32Field.modulus_lt_two_pow_32, Montgomery.Native32.Mont32Field.modulus_sq_lt_two_pow_64, Montgomery.Native32.Mont32Field.two_ne_zero, Montgomery.Native32.Mont32Field.two_pow_32_ne_zero, Montgomery.Native32.Mont32Field.r2ModModulus_lt_modulus, Montgomery.Native32.reduce, Montgomery.Native32.FastField.ofCanonicalNat, Montgomery.Native32.FastField.ofNat, Montgomery.Native32.FastField.ofUInt32, Montgomery.Native32.FastField.ofField, Montgomery.Native32.FastField.ofInt, Montgomery.Native32.FastField.toUInt32, Montgomery.Native32.FastField.toNat, Montgomery.Native32.FastField.toField, Montgomery.Native32.zero, Montgomery.Native32.one, Montgomery.Native32.add, Montgomery.Native32.neg, Montgomery.Native32.sub, Montgomery.Native32.mul, Montgomery.Native32.square, Montgomery.Native32.pow, Montgomery.Native32.inv, Montgomery.Native32.div, Montgomery.Native32.zero_def, Montgomery.Native32.one_def, Montgomery.Native32.add_def, Montgomery.Native32.neg_def, Montgomery.Native32.sub_def, Montgomery.Native32.mul_def, Montgomery.Native32.inv_def, Montgomery.Native32.div_def, Montgomery.Native32.square_def, Montgomery.Native32.FastField.val_toNat_lt, Montgomery.Native32.toNat_lt_modulus, Montgomery.Native32.toField_ofCanonicalNat, Montgomery.Native32.toNat_ofCanonicalNat, Montgomery.Native32.toField_ofField, Montgomery.Native32.ofField_toField, Montgomery.Native32.toField_injective, Montgomery.Native32.toField_zero, Montgomery.Native32.toField_one, Montgomery.Native32.toField_add, Montgomery.Native32.toField_sub, Montgomery.Native32.toField_neg, Montgomery.Native32.toField_mul, Montgomery.Native32.toField_square, Montgomery.Native32.toField_pow, Montgomery.Native32.toField_inv, Montgomery.Native32.toField_div, Montgomery.Native32.toField_natCast, Montgomery.Native32.toField_intCast, Montgomery.Native32.toField_nsmul, Montgomery.Native32.toField_zsmul, Montgomery.Native32.toField_npow, Montgomery.Native32.toField_zpow, Montgomery.Native32.toField_nnratCast, Montgomery.Native32.toField_ratCast, Montgomery.Native32.toField_nnqsmul, Montgomery.Native32.toField_qsmul, Montgomery.Native32.ringEquiv, Montgomery.Native32.ringEquiv_apply, Montgomery.Native32.ringEquiv_symm_apply, Montgomery.Native32.instField, Montgomery.Native32.instNonBinaryField
statement: formalized
proof: formalized
---

# Fast 32-bit Montgomery Fields

`CompPoly.Fields.Montgomery.Native32Field`, in [CompPoly/Fields/Montgomery/Native32Field.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean), by Valerii Huhnin, Georgios Raikos.

> The bounded carrier, conversions, arithmetic, and field instances built on `Native32` reduction.

`Montgomery.Native32.Mont32Field` (class, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L26))

> Per-field data for a fast 32-bit Montgomery field.

```lean
class Mont32Field (modulus : ℕ) where
  /-- `modulus` is prime. -/
  prime : modulus.Prime
  /-- `modulus` as a 32-bit word. -/
  modulus32 : UInt32
  /-- `modulus` as a 64-bit word. -/
  modulus64 : UInt64
  /-- `2^32 mod modulus`, the Montgomery representation of one. -/
  rModModulus : UInt32
  /-- `(2^32)^2 mod modulus`, used to enter Montgomery form. -/
  r2ModModulus : UInt64
  /-- `-modulus⁻¹ mod 2^32`, used by Montgomery reduction. -/
  montgomeryNegInv : UInt32
  modulus32_toNat : modulus32.toNat = modulus := by decide
  modulus64_toNat : modulus64.toNat = modulus := by decide
  two_lt_modulus : 2 < modulus := by decide
  modulus_lt_two_pow_31 : modulus < 2 ^ 31 := by decide
  rModModulus_toNat : rModModulus.toNat = 2 ^ 32 % modulus := by decide
  r2ModModulus_toNat : r2ModModulus.toNat = (2 ^ 32) ^ 2 % modulus := by decide
  montgomeryNegInv_mul_modulus_mod_two_pow_32 :
    (montgomeryNegInv.toNat * modulus) % 2 ^ 32 = 2 ^ 32 - 1 := by decide
```

`Montgomery.Native32.FastField` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L57))

> The fast carrier for a prime modulus: a native word below `modulus`,
> interpreted as a Montgomery residue. At runtime this erases to `UInt32`.

```lean
def FastField (modulus : ℕ) [Mont32Field modulus] : Type
```

`Montgomery.Native32.Mont32Field.modulus_pos` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L71))

```lean
theorem modulus_pos : 0 < modulus
```

`Montgomery.Native32.Mont32Field.modulus32_pos` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L73))

```lean
theorem modulus32_pos : 0 < P.modulus32.toNat
```

`Montgomery.Native32.Mont32Field.modulus64_pos` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L74))

```lean
theorem modulus64_pos : 0 < P.modulus64.toNat
```

`Montgomery.Native32.Mont32Field.modulus32_lt_two_pow_31` (theorem, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L75))

```lean
theorem modulus32_lt_two_pow_31 : P.modulus32.toNat < 2 ^ 31
```

`Montgomery.Native32.Mont32Field.modulus64_lt_two_pow_31` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L76))

```lean
theorem modulus64_lt_two_pow_31 : P.modulus64.toNat < 2 ^ 31
```

`Montgomery.Native32.Mont32Field.modulus_lt_two_pow_32` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L78))

```lean
theorem modulus_lt_two_pow_32 : modulus < 2 ^ 32
```

`Montgomery.Native32.Mont32Field.modulus_sq_lt_two_pow_64` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L81))

```lean
theorem modulus_sq_lt_two_pow_64 : modulus ^ 2 < 2 ^ 64
```

`Montgomery.Native32.Mont32Field.two_ne_zero` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L84))

```lean
theorem two_ne_zero : (2 : ZMod modulus) ≠ 0
```

`Montgomery.Native32.Mont32Field.two_pow_32_ne_zero` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L89))

```lean
theorem two_pow_32_ne_zero : ((2 ^ 32 : ℕ) : ZMod modulus) ≠ 0
```

`Montgomery.Native32.Mont32Field.r2ModModulus_lt_modulus` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L92))

```lean
theorem r2ModModulus_lt_modulus : (2 ^ 32) ^ 2 % modulus < modulus
```

> ## Implementation

`Montgomery.Native32.reduce` (definition, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L103))

> Montgomery reduction for inputs known to be below `p * 2^32`.

```lean
def reduce (x : UInt64) (h : x.toNat < modulus * 2 ^ 32) : FastField modulus
```

> ### Conversions

`Montgomery.Native32.FastField.ofCanonicalNat` (definition, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L114))

> Build a fast element from a canonical natural representative.

```lean
def ofCanonicalNat (n : ℕ) (h : n < modulus) : FastField modulus
```

`Montgomery.Native32.FastField.ofNat` (definition, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L128))

> Convert a natural number into fast Montgomery representation.

```lean
def ofNat (modulus : ℕ) [P : Mont32Field modulus] (n : ℕ) : FastField modulus
```

`Montgomery.Native32.FastField.ofUInt32` (definition, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L133))

> Convert a 32-bit word into fast Montgomery representation.

```lean
def ofUInt32 (modulus : ℕ) [P : Mont32Field modulus] (x : UInt32) : FastField modulus
```

`Montgomery.Native32.FastField.ofField` (definition, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L145))

> Convert from the canonical `ZMod` field into fast Montgomery form.

```lean
def ofField (x : ZMod modulus) : FastField modulus
```

`Montgomery.Native32.FastField.ofInt` (definition, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L150))

> Convert an integer into fast Montgomery representation.

```lean
def ofInt (modulus : ℕ) [P : Mont32Field modulus] (n : Int) : FastField modulus
```

`Montgomery.Native32.FastField.toUInt32` (definition, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L155))

> Convert a fast element to its canonical native-word representative.

```lean
def toUInt32 (x : FastField modulus) : UInt32
```

`Montgomery.Native32.FastField.toNat` (definition, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L162))

> Convert a fast element to its canonical natural representative.

```lean
def toNat (x : FastField modulus) : ℕ
```

`Montgomery.Native32.FastField.toField` (definition, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L166))

> Convert a fast element to the canonical `ZMod` field.

```lean
def toField (x : FastField modulus) : ZMod modulus
```

> ### Field operations

`Montgomery.Native32.zero` (definition, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L174))

> The zero fast element.

```lean
def zero (modulus : ℕ) [P : Mont32Field modulus] : FastField modulus
```

`Montgomery.Native32.one` (definition, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L177))

> The one fast element.

```lean
def one (modulus : ℕ) [P : Mont32Field modulus] : FastField modulus
```

`Montgomery.Native32.add` (definition, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L182))

> Fast modular addition in Montgomery form.

```lean
def add (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native32.neg` (definition, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L192))

> Fast modular negation in Montgomery form.

```lean
def neg (x : FastField modulus) : FastField modulus
```

`Montgomery.Native32.sub` (definition, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L206))

> Fast modular subtraction in Montgomery form.

```lean
def sub (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native32.mul` (definition, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L231))

> Fast modular multiplication in Montgomery form.

```lean
def mul (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native32.square` (definition, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L241))

> Fast squaring.

```lean
def square (x : FastField modulus) : FastField modulus
```

`Montgomery.Native32.pow` (definition, [line 245](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L245))

> Exponentiation over the fast representation using repeated squaring.

```lean
def pow (x : FastField modulus) (n : ℕ) : FastField modulus
```

`Montgomery.Native32.inv` (definition, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L251))

> Inversion in Montgomery form via Fermat's little theorem (`x⁻¹ = x^(p-2)`),
> by binary exponentiation (`pow`).

```lean
def inv (x : FastField modulus) : FastField modulus
```

`Montgomery.Native32.div` (definition, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L256))

> Division through inversion and fast multiplication.

```lean
def div (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native32.zero_def` (theorem, [line 268](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L268))

```lean
theorem zero_def : (0 : FastField modulus) = zero modulus
```

`Montgomery.Native32.one_def` (theorem, [line 269](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L269))

```lean
theorem one_def : (1 : FastField modulus) = one modulus
```

`Montgomery.Native32.add_def` (theorem, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L270))

```lean
theorem add_def (x y : FastField modulus) : x + y = add x y
```

`Montgomery.Native32.neg_def` (theorem, [line 271](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L271))

```lean
theorem neg_def (x : FastField modulus) : -x = neg x
```

`Montgomery.Native32.sub_def` (theorem, [line 272](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L272))

```lean
theorem sub_def (x y : FastField modulus) : x - y = sub x y
```

`Montgomery.Native32.mul_def` (theorem, [line 273](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L273))

```lean
theorem mul_def (x y : FastField modulus) : x * y = mul x y
```

`Montgomery.Native32.inv_def` (theorem, [line 274](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L274))

```lean
theorem inv_def (x : FastField modulus) : x⁻¹ = inv x
```

`Montgomery.Native32.div_def` (theorem, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L275))

```lean
theorem div_def (x y : FastField modulus) : x / y = x * y⁻¹
```

`Montgomery.Native32.square_def` (theorem, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L276))

```lean
theorem square_def (x : FastField modulus) : square x = x * x
```

> ## Correctness

> ### Reduction and conversions

`Montgomery.Native32.FastField.val_toNat_lt` (theorem, [line 319](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L319))

```lean
theorem FastField.val_toNat_lt (x : FastField modulus) : x.val.toNat < modulus
```

`Montgomery.Native32.toNat_lt_modulus` (theorem, [line 321](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L321))

```lean
theorem toNat_lt_modulus {x : FastField modulus} : toNat x < modulus
```

`Montgomery.Native32.toField_ofCanonicalNat` (theorem, [line 363](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L363))

```lean
theorem toField_ofCanonicalNat {n : ℕ} (h : n < modulus) :
    toField (ofCanonicalNat n h) = (n : ZMod modulus)
```

`Montgomery.Native32.toNat_ofCanonicalNat` (theorem, [line 369](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L369))

```lean
theorem toNat_ofCanonicalNat {n : ℕ} (h : n < modulus) :
    toNat (ofCanonicalNat n h) = n
```

`Montgomery.Native32.toField_ofField` (theorem, [line 375](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L375))

> Converting from the canonical field to fast form and back is the identity.

```lean
theorem toField_ofField (x : ZMod modulus) : toField (ofField x) = x
```

`Montgomery.Native32.ofField_toField` (theorem, [line 380](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L380))

> Converting from fast form to the canonical field and back is the identity.

```lean
theorem ofField_toField (x : FastField modulus) : ofField (toField x) = x
```

`Montgomery.Native32.toField_injective` (theorem, [line 390](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L390))

> The canonical-field interpretation distinguishes fast values.

```lean
theorem toField_injective : Function.Injective (toField (modulus := modulus))
```

> ### Field operations

`Montgomery.Native32.toField_zero` (theorem, [line 397](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L397))

> `toField` maps fast zero to canonical zero.

```lean
theorem toField_zero : toField (0 : FastField modulus) = 0
```

`Montgomery.Native32.toField_one` (theorem, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L402))

> `toField` maps fast one to canonical one.

```lean
theorem toField_one : toField (1 : FastField modulus) = 1
```

`Montgomery.Native32.toField_add` (theorem, [line 409](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L409))

> Fast addition agrees with addition in the canonical field.

```lean
theorem toField_add (x y : FastField modulus) : toField (x + y) = toField x + toField y
```

`Montgomery.Native32.toField_sub` (theorem, [line 422](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L422))

> Fast subtraction agrees with subtraction in the canonical field.

```lean
theorem toField_sub (x y : FastField modulus) : toField (x - y) = toField x - toField y
```

`Montgomery.Native32.toField_neg` (theorem, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L451))

> Fast negation agrees with negation in the canonical field.

```lean
theorem toField_neg (x : FastField modulus) : toField (-x) = -toField x
```

`Montgomery.Native32.toField_mul` (theorem, [line 490](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L490))

```lean
theorem toField_mul (x y : FastField modulus) : toField (x * y) = toField x * toField y
```

`Montgomery.Native32.toField_square` (theorem, [line 507](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L507))

> Fast squaring agrees with multiplication by itself in the canonical field.

```lean
theorem toField_square (x : FastField modulus) : toField (square x) = toField x * toField x
```

`Montgomery.Native32.toField_pow` (theorem, [line 512](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L512))

> Fast natural-power computation agrees with powers in the canonical field.

```lean
theorem toField_pow (x : FastField modulus) (n : ℕ) : toField (pow x n) = toField x ^ n
```

`Montgomery.Native32.toField_inv` (theorem, [line 538](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L538))

> Fast inversion agrees with inversion in the canonical field.

```lean
theorem toField_inv (x : FastField modulus) : toField x⁻¹ = (toField x)⁻¹
```

`Montgomery.Native32.toField_div` (theorem, [line 548](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L548))

> Fast division agrees with division in the canonical field.

```lean
theorem toField_div (x y : FastField modulus) : toField (x / y) = toField x / toField y
```

`Montgomery.Native32.toField_natCast` (theorem, [line 554](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L554))

> Natural casts into fast form agree with natural casts into the canonical field.

```lean
theorem toField_natCast (n : ℕ) : toField (n : FastField modulus) = (n : ZMod modulus)
```

`Montgomery.Native32.toField_intCast` (theorem, [line 561](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L561))

> Integer casts into fast form agree with integer casts into the canonical field.

```lean
theorem toField_intCast (n : Int) : toField (n : FastField modulus) = (n : ZMod modulus)
```

`Montgomery.Native32.toField_nsmul` (theorem, [line 567](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L567))

> Natural scalar multiplication is preserved by `toField`.

```lean
theorem toField_nsmul (n : ℕ) (x : FastField modulus) : toField (n • x) = n • toField x
```

`Montgomery.Native32.toField_zsmul` (theorem, [line 573](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L573))

> Integer scalar multiplication is preserved by `toField`.

```lean
theorem toField_zsmul (n : Int) (x : FastField modulus) : toField (n • x) = n • toField x
```

`Montgomery.Native32.toField_npow` (theorem, [line 579](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L579))

> Natural powers through the `Pow` instance are preserved by `toField`.

```lean
theorem toField_npow (x : FastField modulus) (n : ℕ) : toField (x ^ n) = toField x ^ n
```

`Montgomery.Native32.toField_zpow` (theorem, [line 585](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L585))

> Integer powers through the `Pow` instance are preserved by `toField`.

```lean
theorem toField_zpow (x : FastField modulus) (n : Int) : toField (x ^ n) = toField x ^ n
```

`Montgomery.Native32.toField_nnratCast` (theorem, [line 600](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L600))

> Nonnegative rational casts into fast form agree with canonical-field casts.

```lean
theorem toField_nnratCast (q : ℚ≥0) : toField (q : FastField modulus) = (q : ZMod modulus)
```

`Montgomery.Native32.toField_ratCast` (theorem, [line 606](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L606))

> Rational casts into fast form agree with canonical-field casts.

```lean
theorem toField_ratCast (q : ℚ) : toField (q : FastField modulus) = (q : ZMod modulus)
```

`Montgomery.Native32.toField_nnqsmul` (theorem, [line 612](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L612))

> Nonnegative rational scalar multiplication is preserved by `toField`.

```lean
theorem toField_nnqsmul (q : ℚ≥0) (x : FastField modulus) : toField (q • x) = q • toField x
```

`Montgomery.Native32.toField_qsmul` (theorem, [line 618](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L618))

> Rational scalar multiplication is preserved by `toField`.

```lean
theorem toField_qsmul (q : ℚ) (x : FastField modulus) : toField (q • x) = q • toField x
```

> ### Algebraic structure

`Montgomery.Native32.ringEquiv` (definition, [line 625](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L625))

> Ring equivalence between the fast Montgomery representation and the canonical field.

```lean
def ringEquiv (modulus : ℕ) [P : Mont32Field modulus] : FastField modulus ≃+* ZMod modulus
```

`Montgomery.Native32.ringEquiv_apply` (theorem, [line 634](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L634))

```lean
theorem ringEquiv_apply {x : FastField modulus} : ringEquiv modulus x = toField x
```

`Montgomery.Native32.ringEquiv_symm_apply` (theorem, [line 637](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L637))

```lean
theorem ringEquiv_symm_apply {x : ZMod modulus} :
    (ringEquiv modulus).symm x = ofField x
```

`Montgomery.Native32.instField` (instance, [line 641](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L641))

> Field instance transferred from the canonical field through `toField`.

```lean
instance instField : _root_.Field (FastField modulus)
```

`Montgomery.Native32.instNonBinaryField` (instance, [line 645](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean#L645))

> A fast 32-bit-word field is non-binary.

```lean
instance instNonBinaryField : NonBinaryField (FastField modulus)
```

## Depends on

- [Non-binary fields and polynomial utilities](../basic.md)
- [Native 32-bit Montgomery Reduction](native32.md)

## Sources

- [CompPoly/Fields/Montgomery/Native32Field.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native32Field.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native32Field.json)
