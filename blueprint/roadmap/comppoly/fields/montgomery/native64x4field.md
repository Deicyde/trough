---
catalog: module
lean: Montgomery.Native64x4.Mont64x4Field, Montgomery.Native64x4.Mont64x4Field.modulus_pos, Montgomery.Native64x4.Mont64x4Field.modulus_lt, Montgomery.Native64x4.Mont64x4Field.q_toNat, Montgomery.Native64x4.Mont64x4Field.negInv_mul_q, Montgomery.Native64x4.Mont64x4Field.two_ne_zero, Montgomery.Native64x4.Mont64x4Field.r_ne_zero, Montgomery.Native64x4.FastField, Montgomery.Native64x4.FastField.val_lt, Montgomery.Native64x4.FastField.zero, Montgomery.Native64x4.FastField.one, Montgomery.Native64x4.FastField.add, Montgomery.Native64x4.FastField.sub, Montgomery.Native64x4.FastField.neg, Montgomery.Native64x4.FastField.mul, Montgomery.Native64x4.FastField.square, Montgomery.Native64x4.FastField.pow, Montgomery.Native64x4.FastField.inv, Montgomery.Native64x4.FastField.div, Montgomery.Native64x4.FastField.toLimbs4, Montgomery.Native64x4.FastField.toNat, Montgomery.Native64x4.FastField.toField, Montgomery.Native64x4.FastField.ofCanonicalNat, Montgomery.Native64x4.FastField.ofNat, Montgomery.Native64x4.FastField.ofField, Montgomery.Native64x4.FastField.ofInt, Montgomery.Native64x4.FastField.zero_def, Montgomery.Native64x4.FastField.one_def, Montgomery.Native64x4.FastField.add_def, Montgomery.Native64x4.FastField.neg_def, Montgomery.Native64x4.FastField.sub_def, Montgomery.Native64x4.FastField.mul_def, Montgomery.Native64x4.FastField.inv_def, Montgomery.Native64x4.FastField.div_def, Montgomery.Native64x4.FastField.square_def, Montgomery.Native64x4.FastField.val_mul, Montgomery.Native64x4.FastField.toNat_lt, Montgomery.Native64x4.FastField.toField_ofCanonicalNat, Montgomery.Native64x4.FastField.toNat_ofCanonicalNat, Montgomery.Native64x4.FastField.toField_ofField, Montgomery.Native64x4.FastField.ofField_toField, Montgomery.Native64x4.FastField.toField_injective, Montgomery.Native64x4.FastField.toField_zero, Montgomery.Native64x4.FastField.toField_one, Montgomery.Native64x4.FastField.toField_add, Montgomery.Native64x4.FastField.toField_sub, Montgomery.Native64x4.FastField.toField_neg, Montgomery.Native64x4.FastField.toField_mul, Montgomery.Native64x4.FastField.toField_square, Montgomery.Native64x4.FastField.toField_pow, Montgomery.Native64x4.FastField.toField_inv, Montgomery.Native64x4.FastField.toField_div, Montgomery.Native64x4.FastField.toField_natCast, Montgomery.Native64x4.FastField.toField_intCast, Montgomery.Native64x4.FastField.toField_nsmul, Montgomery.Native64x4.FastField.toField_zsmul, Montgomery.Native64x4.FastField.toField_npow, Montgomery.Native64x4.FastField.toField_zpow, Montgomery.Native64x4.FastField.toField_nnratCast, Montgomery.Native64x4.FastField.toField_ratCast, Montgomery.Native64x4.FastField.toField_nnqsmul, Montgomery.Native64x4.FastField.toField_qsmul, Montgomery.Native64x4.FastField.ringEquiv, Montgomery.Native64x4.FastField.ringEquiv_apply, Montgomery.Native64x4.FastField.ringEquiv_symm_apply, Montgomery.Native64x4.FastField.instField, Montgomery.Native64x4.FastField.instNonBinaryField
statement: formalized
proof: formalized
---

# Fast four-limb Montgomery fields

`CompPoly.Fields.Montgomery.Native64x4Field`, in [CompPoly/Fields/Montgomery/Native64x4Field.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean), by Georgios Raikos.

> The carrier `{ x : Limbs4 // x.toNat < modulus }` stores the Montgomery residue
> `x * 2 ^ 256 mod modulus` for any prime modulus below `2 ^ 256`; `toField` divides by `2 ^ 256`
> and lands in `ZMod modulus`, and all arithmetic is transported along that ring isomorphism.
>
> ## Main results
>
> * `FastField` — the carrier, `{ x : Limbs4 // x.toNat < modulus }`
> * `toField_add`, `toField_mul`, … — `@[simp]` equivalences with the canonical field
> * `Mont64x4Field` — the per-field constants class
> * `ringEquiv`, `instField` — the ring isomorphism and the transferred `Field` instance

> ## Per-field constants

`Montgomery.Native64x4.Mont64x4Field` (class, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L37))

> Per-field data for a fast four-limb Montgomery field with radix `R = 2 ^ 256`.  All side
> conditions are concrete numeral facts, discharged by `decide` at instantiation.

```lean
class Mont64x4Field (modulus : ℕ) where
  /-- `modulus` is prime. -/
  prime : modulus.Prime
  /-- The modulus in four 64-bit limbs. -/
  modulusLimbs : Limbs4
  /-- `2 ^ 256 mod modulus`, the Montgomery representation of one. -/
  rModModulus : Limbs4
  /-- `(2 ^ 256) ^ 2 mod modulus`, used to enter Montgomery form. -/
  r2ModModulus : Limbs4
  /-- `-modulus⁻¹ mod 2 ^ 64`, used by Montgomery reduction. -/
  montgomeryNegInv : UInt64
  modulusLimbs_toNat : modulusLimbs.toNat = modulus := by decide
  two_lt_modulus : 2 < modulus := by decide
  rModModulus_toNat : rModModulus.toNat = 2 ^ 256 % modulus := by decide
  r2ModModulus_toNat : r2ModModulus.toNat = (2 ^ 256) ^ 2 % modulus := by decide
  montgomeryNegInv_mul_modulus_mod_two_pow_64 :
    montgomeryNegInv.toNat * modulus % 2 ^ 64 = 2 ^ 64 - 1 := by decide
```

> ## Modulus facts

`Montgomery.Native64x4.Mont64x4Field.modulus_pos` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L63))

```lean
theorem modulus_pos : 0 < modulus
```

`Montgomery.Native64x4.Mont64x4Field.modulus_lt` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L65))

```lean
theorem modulus_lt : modulus < 2 ^ 256
```

`Montgomery.Native64x4.Mont64x4Field.q_toNat` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L69))

```lean
theorem q_toNat : P.modulusLimbs.toNat = modulus
```

`Montgomery.Native64x4.Mont64x4Field.negInv_mul_q` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L71))

```lean
theorem negInv_mul_q : P.montgomeryNegInv.toNat * P.modulusLimbs.toNat % 2 ^ 64 = 2 ^ 64 - 1
```

`Montgomery.Native64x4.Mont64x4Field.two_ne_zero` (theorem, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L77))

```lean
theorem two_ne_zero : (2 : ZMod modulus) ≠ 0
```

`Montgomery.Native64x4.Mont64x4Field.r_ne_zero` (theorem, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L82))

```lean
theorem r_ne_zero : ((2 ^ 256 : ℕ) : ZMod modulus) ≠ 0
```

> ## The carrier

`Montgomery.Native64x4.FastField` (definition, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L93))

> The fast carrier: four 64-bit limbs holding a Montgomery residue below `modulus`, erasing
> to `Limbs4` at runtime.

```lean
def FastField (modulus : ℕ) [Mont64x4Field modulus] : Type
```

`Montgomery.Native64x4.FastField.val_lt` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L105))

```lean
theorem val_lt (x : FastField modulus) : x.val.toNat < P.modulusLimbs.toNat
```

> ### Arithmetic

`Montgomery.Native64x4.FastField.zero` (definition, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L112))

> The zero element.

```lean
def zero (modulus : ℕ) [P : Mont64x4Field modulus] : FastField modulus
```

`Montgomery.Native64x4.FastField.one` (definition, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L118))

> The one element, the Montgomery residue `2 ^ 256 mod modulus`.

```lean
def one (modulus : ℕ) [P : Mont64x4Field modulus] : FastField modulus
```

`Montgomery.Native64x4.FastField.add` (definition, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L124))

> Fast modular addition in Montgomery form.

```lean
def add (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.sub` (definition, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L130))

> Fast modular subtraction in Montgomery form.

```lean
def sub (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.neg` (definition, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L136))

> Fast modular negation in Montgomery form.

```lean
def neg (x : FastField modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.mul` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L142))

> Fast Montgomery multiplication.

```lean
def mul (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.square` (definition, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L149))

> Fast squaring.

```lean
def square (x : FastField modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.pow` (definition, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L152))

> Exponentiation by repeated squaring.

```lean
def pow (x : FastField modulus) (n : ℕ) : FastField modulus
```

`Montgomery.Native64x4.FastField.inv` (definition, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L156))

> Inversion by Fermat's little theorem, `x⁻¹ = x ^ (modulus - 2)`.

```lean
def inv (x : FastField modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.div` (definition, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L159))

> Division through inversion.

```lean
def div (x y : FastField modulus) : FastField modulus
```

> ### Conversions

`Montgomery.Native64x4.FastField.toLimbs4` (definition, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L164))

> The canonical limb representative of a fast element: one Montgomery reduction.

```lean
def toLimbs4 (x : FastField modulus) : Limbs4
```

`Montgomery.Native64x4.FastField.toNat` (definition, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L168))

> The canonical natural representative of a fast element.

```lean
def toNat (x : FastField modulus) : ℕ
```

`Montgomery.Native64x4.FastField.toField` (definition, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L171))

> The canonical `ZMod` value of a fast element.

```lean
def toField (x : FastField modulus) : ZMod modulus
```

`Montgomery.Native64x4.FastField.ofCanonicalNat` (definition, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L180))

> Build a fast element from a canonical natural representative.

```lean
def ofCanonicalNat (n : ℕ) (h : n < modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.ofNat` (definition, [line 187](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L187))

> Convert a natural number into fast Montgomery form.

```lean
def ofNat (modulus : ℕ) [P : Mont64x4Field modulus] (n : ℕ) : FastField modulus
```

`Montgomery.Native64x4.FastField.ofField` (definition, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L191))

> Convert from the canonical field into fast Montgomery form.

```lean
def ofField (x : ZMod modulus) : FastField modulus
```

`Montgomery.Native64x4.FastField.ofInt` (definition, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L195))

> Convert an integer into fast Montgomery form.

```lean
def ofInt (modulus : ℕ) [P : Mont64x4Field modulus] (n : Int) :
    FastField modulus
```

`Montgomery.Native64x4.FastField.zero_def` (theorem, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L223))

```lean
theorem zero_def : (0 : FastField modulus) = FastField.zero modulus
```

`Montgomery.Native64x4.FastField.one_def` (theorem, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L224))

```lean
theorem one_def : (1 : FastField modulus) = FastField.one modulus
```

`Montgomery.Native64x4.FastField.add_def` (theorem, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L225))

```lean
theorem add_def (x y : FastField modulus) : x + y = FastField.add x y
```

`Montgomery.Native64x4.FastField.neg_def` (theorem, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L226))

```lean
theorem neg_def (x : FastField modulus) : -x = FastField.neg x
```

`Montgomery.Native64x4.FastField.sub_def` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L227))

```lean
theorem sub_def (x y : FastField modulus) : x - y = FastField.sub x y
```

`Montgomery.Native64x4.FastField.mul_def` (theorem, [line 228](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L228))

```lean
theorem mul_def (x y : FastField modulus) : x * y = FastField.mul x y
```

`Montgomery.Native64x4.FastField.inv_def` (theorem, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L229))

```lean
theorem inv_def (x : FastField modulus) : x⁻¹ = FastField.inv x
```

`Montgomery.Native64x4.FastField.div_def` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L230))

```lean
theorem div_def (x y : FastField modulus) : x / y = x * y⁻¹
```

`Montgomery.Native64x4.FastField.square_def` (theorem, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L231))

```lean
theorem square_def (x : FastField modulus) : FastField.square x = x * x
```

`Montgomery.Native64x4.FastField.val_mul` (theorem, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L234))

> The limbs of a product.

```lean
theorem val_mul (x y : FastField modulus) :
    (x * y).val = Native64x4.mul P.modulusLimbs P.montgomeryNegInv x.val y.val
```

> ## Correctness

`Montgomery.Native64x4.FastField.toNat_lt` (theorem, [line 277](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L277))

```lean
theorem toNat_lt (x : FastField modulus) : toNat x < modulus
```

`Montgomery.Native64x4.FastField.toField_ofCanonicalNat` (theorem, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L296))

```lean
theorem toField_ofCanonicalNat {n : ℕ} (h : n < modulus) :
    toField (ofCanonicalNat n h) = (n : ZMod modulus)
```

`Montgomery.Native64x4.FastField.toNat_ofCanonicalNat` (theorem, [line 302](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L302))

```lean
theorem toNat_ofCanonicalNat {n : ℕ} (h : n < modulus) : toNat (ofCanonicalNat n h) = n
```

`Montgomery.Native64x4.FastField.toField_ofField` (theorem, [line 307](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L307))

> Converting from the canonical field to fast form and back is the identity.

```lean
theorem toField_ofField (x : ZMod modulus) : toField (ofField x) = x
```

`Montgomery.Native64x4.FastField.ofField_toField` (theorem, [line 312](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L312))

> Converting from fast form to the canonical field and back is the identity.

```lean
theorem ofField_toField (x : FastField modulus) : ofField (toField x) = x
```

`Montgomery.Native64x4.FastField.toField_injective` (theorem, [line 321](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L321))

> The canonical-field interpretation distinguishes fast values.

```lean
theorem toField_injective : Function.Injective (toField (modulus := modulus))
```

> ### Field operations

`Montgomery.Native64x4.FastField.toField_zero` (theorem, [line 327](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L327))

```lean
theorem toField_zero : toField (0 : FastField modulus) = 0
```

`Montgomery.Native64x4.FastField.toField_one` (theorem, [line 332](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L332))

```lean
theorem toField_one : toField (1 : FastField modulus) = 1
```

`Montgomery.Native64x4.FastField.toField_add` (theorem, [line 338](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L338))

```lean
theorem toField_add (x y : FastField modulus) : toField (x + y) = toField x + toField y
```

`Montgomery.Native64x4.FastField.toField_sub` (theorem, [line 345](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L345))

```lean
theorem toField_sub (x y : FastField modulus) : toField (x - y) = toField x - toField y
```

`Montgomery.Native64x4.FastField.toField_neg` (theorem, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L353))

```lean
theorem toField_neg (x : FastField modulus) : toField (-x) = -toField x
```

`Montgomery.Native64x4.FastField.toField_mul` (theorem, [line 361](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L361))

```lean
theorem toField_mul (x y : FastField modulus) : toField (x * y) = toField x * toField y
```

`Montgomery.Native64x4.FastField.toField_square` (theorem, [line 376](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L376))

```lean
theorem toField_square (x : FastField modulus) : toField (square x) = toField x * toField x
```

`Montgomery.Native64x4.FastField.toField_pow` (theorem, [line 380](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L380))

```lean
theorem toField_pow (x : FastField modulus) (n : ℕ) : toField (pow x n) = toField x ^ n
```

`Montgomery.Native64x4.FastField.toField_inv` (theorem, [line 406](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L406))

```lean
theorem toField_inv (x : FastField modulus) : toField x⁻¹ = (toField x)⁻¹
```

`Montgomery.Native64x4.FastField.toField_div` (theorem, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L415))

```lean
theorem toField_div (x y : FastField modulus) : toField (x / y) = toField x / toField y
```

`Montgomery.Native64x4.FastField.toField_natCast` (theorem, [line 420](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L420))

```lean
theorem toField_natCast (n : ℕ) : toField (n : FastField modulus) = (n : ZMod modulus)
```

`Montgomery.Native64x4.FastField.toField_intCast` (theorem, [line 426](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L426))

```lean
theorem toField_intCast (n : Int) : toField (n : FastField modulus) = (n : ZMod modulus)
```

`Montgomery.Native64x4.FastField.toField_nsmul` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L431))

```lean
theorem toField_nsmul (n : ℕ) (x : FastField modulus) : toField (n • x) = n • toField x
```

`Montgomery.Native64x4.FastField.toField_zsmul` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L436))

```lean
theorem toField_zsmul (n : Int) (x : FastField modulus) : toField (n • x) = n • toField x
```

`Montgomery.Native64x4.FastField.toField_npow` (theorem, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L441))

```lean
theorem toField_npow (x : FastField modulus) (n : ℕ) : toField (x ^ n) = toField x ^ n
```

`Montgomery.Native64x4.FastField.toField_zpow` (theorem, [line 446](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L446))

```lean
theorem toField_zpow (x : FastField modulus) (n : Int) : toField (x ^ n) = toField x ^ n
```

`Montgomery.Native64x4.FastField.toField_nnratCast` (theorem, [line 460](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L460))

```lean
theorem toField_nnratCast (q : ℚ≥0) : toField (q : FastField modulus) = (q : ZMod modulus)
```

`Montgomery.Native64x4.FastField.toField_ratCast` (theorem, [line 465](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L465))

```lean
theorem toField_ratCast (q : ℚ) : toField (q : FastField modulus) = (q : ZMod modulus)
```

`Montgomery.Native64x4.FastField.toField_nnqsmul` (theorem, [line 470](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L470))

```lean
theorem toField_nnqsmul (q : ℚ≥0) (x : FastField modulus) : toField (q • x) = q • toField x
```

`Montgomery.Native64x4.FastField.toField_qsmul` (theorem, [line 475](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L475))

```lean
theorem toField_qsmul (q : ℚ) (x : FastField modulus) : toField (q • x) = q • toField x
```

> ### Algebraic structure

`Montgomery.Native64x4.FastField.ringEquiv` (definition, [line 482](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L482))

> Ring equivalence between the fast Montgomery representation and the canonical field.

```lean
def ringEquiv (modulus : ℕ) [P : Mont64x4Field modulus] :
    FastField modulus ≃+* ZMod modulus
```

`Montgomery.Native64x4.FastField.ringEquiv_apply` (theorem, [line 492](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L492))

```lean
theorem ringEquiv_apply {x : FastField modulus} : ringEquiv modulus x = toField x
```

`Montgomery.Native64x4.FastField.ringEquiv_symm_apply` (theorem, [line 495](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L495))

```lean
theorem ringEquiv_symm_apply {x : ZMod modulus} : (ringEquiv modulus).symm x = ofField x
```

`Montgomery.Native64x4.FastField.instField` (instance, [line 498](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L498))

> Field instance transferred from the canonical field through `toField`.

```lean
instance instField : _root_.Field (FastField modulus)
```

`Montgomery.Native64x4.FastField.instNonBinaryField` (instance, [line 502](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean#L502))

> A fast four-limb field is non-binary.

```lean
instance instNonBinaryField : NonBinaryField (FastField modulus)
```

## Depends on

- [Non-binary fields and polynomial utilities](../basic.md)
- [Four-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x4defs.md)

## Proof depends on

- [Correctness of four-limb CIOS Montgomery multiplication](native64x4mul.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x4Field.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Field.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x4Field.json)
